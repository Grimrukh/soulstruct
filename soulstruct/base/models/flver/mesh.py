from __future__ import annotations

__all__ = ["FaceSetFlags", "FaceSet", "Mesh"]

import io
import typing as tp

from soulstruct.utilities import unpack_from_buffer, indent_lines, Flags8
from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject

from .bounding_box import BoundingBox, BoundingBoxWithUnknown
from .vertex import LayoutSemantic, BufferLayout, Vertex, VertexBuffer
from .version import Version


class FaceSetFlags(Flags8):
    @property
    def LodLevel1(self):
        return self.flags[0]

    @property
    def LodLevel2(self):
        return self.flags[1]

    @property
    def EdgeCompressed(self):
        return self.flags[6]

    @property
    def MotionBlur(self):
        return self.flags[7]


class FaceSet(BinaryObject):

    STRUCT = BinaryStruct(
        ("flags", "B"),
        "3x",
        ("triangle_strip", "?"),
        ("cull_back_faces", "?"),
        ("unk_x06", "h"),
        ("__indices_count", "i"),
        ("__indices_offset", "i"),  # header stops here for versions < 0x20005, which are not supported by Soulstruct
        ("__indices_length", "i"),  # unused
        "4x",
        ("__index_size", "i"),  # 0 (from header), 16, or 32
        "4x",
    )

    flags: FaceSetFlags
    triangle_strip: bool
    cull_back_faces: bool
    unk_x06: int
    indices: list[int]

    def unpack(self, buffer: io.BufferedIOBase, header_index_size: int = None, data_offset: int = None):
        data = self.STRUCT.unpack(buffer)

        if (index_size := data.pop("__index_size")) == 0:
            index_size = header_index_size

        if index_size == 8:
            raise NotImplementedError("Soulstruct cannot support edge-compressed FLVER face sets (`index_size=8`).")
        elif index_size in {16, 32}:
            face_set_offset = buffer.tell()
            indices_count = data.pop("__indices_count")
            indices_offset = data.pop("__indices_offset")
            buffer.seek(data_offset + indices_offset)
            self.indices = list(unpack_from_buffer(buffer, f"<{indices_count}{'H' if index_size == 16 else 'I'}"))
            buffer.seek(face_set_offset)
        else:
            raise ValueError(f"Unsupported face set index size: {index_size}")

        self.set(**data)

    def get_face_counts(self, allow_primitive_restarts: bool) -> tuple[int, int]:
        if self.triangle_strip:
            true_face_count = 0
            total_face_count = 0
            for i in range(len(self.indices) - 2):
                triplet = self.indices[i:i + 3]
                if not allow_primitive_restarts or 0xFFFF not in triplet:
                    total_face_count += 1
                    if not self.flags.MotionBlur and len(set(triplet)) == 3:
                        # Vertices are not MotionBlur and not degenerate.
                        true_face_count += 1
            return true_face_count, total_face_count
        else:
            return len(self.indices) // 3, len(self.indices) // 3

    def get_vertex_index_size(self) -> int:
        for vertex_index in self.indices:
            if vertex_index > 2 ** 16:  # unsigned short max value (+1)
                return 32
        return 16

    def __repr__(self):
        return (
            f"FaceSet(\n"
            f"  flags = {self.flags}\n"
            f"  triangle_strip = {self.triangle_strip}\n"
            f"  cull_back_faces = {self.cull_back_faces}\n"
            f"  unk_x06 = {self.unk_x06}\n"
            f"  indices = {self.indices}\n"
            f")"
        )


class Mesh(BinaryObject):

    STRUCT = BinaryStruct(
        ("is_bind_pose", "?"),
        "3x",
        ("material_index", "i"),
        "8x",
        ("default_bone_index", "i"),
        ("__bone_count", "i"),
        ("__bounding_box_offset", "i"),
        ("__bone_offset", "i"),
        ("__face_set_count", "i"),
        ("__face_set_offset", "i"),
        ("__vertex_buffer_count", "i"),  # 1, 2, or 3
        ("__vertex_buffer_offset", "i"),
    )

    is_bind_pose: bool
    material_index: int
    default_bone_index: int
    bone_indices: list[int]
    bounding_box: tp.Optional[BoundingBox]

    face_sets: list[FaceSet]
    vertex_buffers: list[VertexBuffer]
    vertices: list[Vertex]

    _face_set_indices: tp.Optional[list[int]]
    _vertex_buffer_indices: tp.Optional[list[int]]

    DEFAULTS = {
        "default_bone_index": -1,
    }

    def __init__(self, source, unpack_kwargs, **kwargs):
        self.face_sets = []
        self.vertex_buffers = []
        self.vertices = []
        super().__init__(source, unpack_kwargs, **kwargs)

    def unpack(self, buffer: io.BufferedIOBase, bounding_box_has_unknown: bool = None):
        data = self.STRUCT.unpack(buffer)
        mesh_offset = buffer.tell()

        bounding_box_offset = data.pop("__bounding_box_offset")
        if bounding_box_offset != 0:
            buffer.seek(bounding_box_offset)
            self.bounding_box = BoundingBoxWithUnknown(buffer) if bounding_box_has_unknown else BoundingBox(buffer)
        else:
            self.bounding_box = None

        buffer.seek(data.pop("__bone_offset"))
        bone_count = data.pop("__bone_count")
        self.bone_indices = list(unpack_from_buffer(buffer, f"<{bone_count}i",))

        buffer.seek(data.pop("__face_set_offset"))
        face_set_count = data.pop("__face_set_count")
        self._face_set_indices = list(unpack_from_buffer(buffer, f"<{face_set_count}i"))

        buffer.seek(data.pop("__vertex_buffer_offset"))
        vertex_count = data.pop("__vertex_buffer_count")
        self._vertex_buffer_indices = list(unpack_from_buffer(buffer, f"<{vertex_count}i"))

        buffer.seek(mesh_offset)
        self.set(**data)

    def assign_face_sets(self, face_sets: dict[int, FaceSet]):
        self.face_sets = []
        if self._face_set_indices is None:
            raise ValueError("Tried to call `assign_face_sets()` on a `Mesh` more than once.")
        for i in self._face_set_indices:
            if i not in face_sets:
                raise KeyError(
                    f"Tried to assign `FaceSet` with index {i} to `Mesh`, but the `FaceSet` has "
                    "already been assigned to another `Mesh` (or does not exist)."
                )
            self.face_sets.append(face_sets.pop(i))
        self._face_set_indices = None

    def assign_vertex_buffers(self, vertex_buffers: dict[int, VertexBuffer], layouts: list[BufferLayout]):
        self.vertex_buffers = []
        if self._vertex_buffer_indices is None:
            raise ValueError("Tried to call `assign_vertex_buffers()` on a `Mesh` more than once.")
        for i in self._vertex_buffer_indices:
            if i not in vertex_buffers:
                raise KeyError(
                    f"Tried to assign `VertexBuffer` with index {i} to `Mesh`, but the `VertexBuffer` has "
                    "already been assigned to another `Mesh` (or does not exist)."
                )
            self.vertex_buffers.append(vertex_buffers.pop(i))
        self._vertex_buffer_indices = None

        # Check that unique `LayoutSemantic` types do not occur more than once among all `BufferLayout` members.
        existing_semantics = set()
        for vertex_buffer in self.vertex_buffers:
            for member in layouts[vertex_buffer.layout_index]:
                if member.semantic.unique():
                    if member.semantic in existing_semantics:
                        raise ValueError(
                            f"Unique `LayoutSemantic` {member.semantic} found more than once in `BufferLayouts` "
                            f"of `Mesh`."
                        )
                    existing_semantics.add(member.semantic)

        # TODO: SoulsFormats does an extra check here for edge-compressed vertex buffers, which are not supported here.

    def read_vertices(self, buffer: io.BufferedIOBase, data_offset: int, layouts: list[BufferLayout], version: Version):
        self.vertices = [Vertex() for _ in range(self.vertex_buffers[0].vertex_count)]
        for vertex_buffer in self.vertex_buffers:
            vertex_buffer.read_buffer(buffer, layouts, self.vertices, data_offset, version)

    def __repr__(self):
        vertices = ",\n".join([f"    {v.repr_position_only()}" for v in self.vertices])
        face_sets = ",\n".join(["    " + indent_lines(repr(f)) for f in self.face_sets])
        return (
            f"Mesh(\n"
            f"  is_bind_pose={self.is_bind_pose}\n"
            f"  material_index={self.material_index}\n"
            f"  default_bone_index={self.default_bone_index}\n"
            f"  bone_indices={self.bone_indices}\n"
            f"  bounding_box={self.bounding_box}\n"
            f"  vertices = [\n{vertices}\n]\n"
            f"  face_sets = [\n{face_sets}\n]\n"
            f")"
        )
