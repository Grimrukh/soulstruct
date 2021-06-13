"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""
from __future__ import annotations

__all__ = ["FaceSetFlags", "FaceSet", "Mesh"]

import logging
import random
import typing as tp
from enum import IntEnum

from soulstruct.utilities.text import indent_lines
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader, BinaryWriter

from .bounding_box import BoundingBox, BoundingBoxWithUnknown
from .vertex import BufferLayout, Vertex, VertexBuffer

_LOGGER = logging.getLogger(__name__)


class FaceSetFlags(IntEnum):

    LodLevel1 = 0b0000_0001
    LodLevel2 = 0b0000_0010
    EdgeCompressed = 0b0100_0000
    MotionBlur = 0b1000_0000

    def has_flag(self, flag_int: int):
        return flag_int & self.value


class FaceSet(BinaryObject):

    STRUCT = BinaryStruct(
        "3x",
        ("flags", "B"),
        ("triangle_strip", "?"),
        ("cull_back_faces", "?"),
        ("unk_x06", "h"),
        ("__vertex_indices_count", "i"),
        ("__vertex_indices_offset", "i"),
        # Header stops here for versions < 0x20005, which are not supported by Soulstruct.
        ("__vertex_indices_length", "i"),  # not needed
        "4x",
        ("__vertex_index_size", "i"),  # 0 (from header), 16, or 32
        "4x",
    )

    flags: int
    triangle_strip: bool
    cull_back_faces: bool
    unk_x06: int
    vertex_indices: tp.List[int]

    def unpack(self, reader: BinaryReader, header_vertex_index_size: int, vertex_data_offset: int):
        face_set = reader.unpack_struct(self.STRUCT)

        vertex_index_size = face_set.pop("__vertex_index_size")
        if vertex_index_size == 0:
            vertex_index_size = header_vertex_index_size

        if vertex_index_size == 8:
            raise NotImplementedError("Soulstruct cannot support edge-compressed FLVER face sets.")
        elif vertex_index_size in {16, 32}:
            vertex_indices_count = face_set.pop("__vertex_indices_count")
            vertex_indices_offset = face_set.pop("__vertex_indices_offset")
            with reader.temp_offset(vertex_data_offset + vertex_indices_offset):
                fmt = f"<{vertex_indices_count}{'H' if vertex_index_size == 16 else 'I'}"
                self.vertex_indices = list(reader.unpack(fmt))
        else:
            raise ValueError(f"Unsupported face set index size: {vertex_index_size}")

        self.set(**face_set)

    def pack(self, writer: BinaryWriter, vertex_index_size: int):
        writer.pack_struct(
            self.STRUCT,
            self,
            __vertex_indices_count=len(self.vertex_indices),
            __vertex_indices_offset=writer.AUTO_RESERVE,
            __vertex_indices_length=len(self.vertex_indices) * vertex_index_size // 8,
            __vertex_index_size=vertex_index_size,
        )

    def pack_vertex_indices(self, writer: BinaryWriter, vertex_index_size: int, vertex_indices_offset: int):
        self.fill(writer, __vertex_indices_offset=vertex_indices_offset)
        if vertex_index_size == 16:
            fmt = f"{len(self.vertex_indices)}H"
        elif vertex_index_size == 32:
            fmt = f"{len(self.vertex_indices)}i"
        else:
            raise NotImplementedError(f"Unsupported vertex index size for `pack()`: {vertex_index_size}")
        writer.pack(fmt, *self.vertex_indices)

    def get_face_counts(self, allow_primitive_restarts: bool) -> tp.Tuple[int, int]:
        if self.triangle_strip:
            true_face_count = 0
            total_face_count = 0
            for i in range(len(self.vertex_indices) - 2):
                triplet = self.vertex_indices[i:i + 3]
                if not allow_primitive_restarts or 0xFFFF not in triplet:
                    total_face_count += 1
                    if not self.has_flag(FaceSetFlags.MotionBlur) and len(set(triplet)) == 3:
                        # Vertices are not MotionBlur and not degenerate.
                        true_face_count += 1
            return true_face_count, total_face_count
        else:
            return len(self.vertex_indices) // 3, len(self.vertex_indices) // 3

    def get_vertex_index_size(self) -> int:
        for vertex_index in self.vertex_indices:
            if vertex_index > 2 ** 16:  # unsigned short max value (+1)
                return 32
        return 16

    def has_flag(self, flag: FaceSetFlags):
        return flag.has_flag(self.flags)

    def triangulate(self, allow_primitive_restarts: bool, include_degenerate_faces=False) -> tp.List[int]:
        """Convert triangle strip to triangle list (i.e. every triangle is a separate vertex index triplet).

        Returns a copy of `self.vertex_indices` if `self.triangle_strip=False` already.

        If `allow_primitive_restarts=True`, a vertex index of 0xFFFF will reset `flip` to False. Only use this if the
        number of vertices in the mesh is less than 0xFFFF (otherwise the primitive command is ambiguous).

        Also excludes degenerate faces (where two or more vertex indices are identical) by default.
        """
        if not self.triangle_strip:
            return self.vertex_indices.copy()

        triangle_list = []
        flip = False
        for i in range(len(self.vertex_indices) - 2):
            triplet = self.vertex_indices[i:i + 3]
            if allow_primitive_restarts and 0xFFFF in triplet:
                flip = False  # restart the strip
                continue
            if len(set(triplet)) == 3 or include_degenerate_faces:
                triangle_list.extend(reversed(triplet) if flip else triplet)
            flip = not flip
        return triangle_list

    def get_triangles(
        self, allow_primitive_restarts: bool, include_degenerate_faces=False
    ) -> tp.List[tp.Tuple[int, int, int]]:
        """Get triangle list and return the triplets as tuples inside a list."""
        tri = self.triangulate(allow_primitive_restarts, include_degenerate_faces)
        return [(tri[i], tri[i + 1], tri[i + 2]) for i in range(0, len(tri), 3)]

    def get_connected_vertex_indices(self, vertex_index: int) -> tp.Set[int]:
        """Find all vertices connected to the given `vertex_index`, including `vertex_index` itself."""
        triangles = self.get_triangles(allow_primitive_restarts=False, include_degenerate_faces=False)
        connected = {vertex_index}
        for tri in (set(t) for t in triangles):
            if connected.intersection(tri):
                connected |= tri
        return connected

    @classmethod
    def from_triangles(cls, triangles: tp.List[tp.Tuple[int, int, int], ...], cull_back_faces=True):
        """Create a `FaceSet` with `triangle_strip=False` from a list of three-index triangle tuples.

        TODO: Currently sets `flags=0` and `unk_x06=0`, which is correct so far in my usage.
        """
        return cls(
            flags=0,
            unk_x06=0,
            triangle_strip=False,
            cull_back_faces=cull_back_faces,
            vertex_indices=[i for tri in triangles for i in tri],
        )

    def __repr__(self):
        if self.flags == 0 and self.unk_x06 == 0 and self.triangle_strip:
            # Simple repr.
            return f"FaceSet({len(self.vertex_indices)} vertices, cull_back_faces = {self.cull_back_faces})"
        return (
            f"FaceSet(\n"
            f"  flags = {self.flags}\n"
            f"  triangle_strip = {self.triangle_strip}\n"
            f"  cull_back_faces = {self.cull_back_faces}\n"
            f"  unk_x06 = {self.unk_x06}\n"
            f"  vertex_indices = <{len(self.vertex_indices)} indices>\n"
            f")"
        )


class Mesh(BinaryObject):

    Vertex = Vertex
    FaceSet = FaceSet

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
    bounding_box: tp.Optional[BoundingBox]

    bone_indices: tp.List[int]
    face_sets: tp.List[FaceSet]
    vertex_buffers: tp.List[VertexBuffer]
    vertices: tp.List[Vertex]

    _face_set_indices: tp.Optional[tp.List[int]]
    _vertex_buffer_indices: tp.Optional[tp.List[int]]

    invalid_vertex_size: bool

    DEFAULTS = {
        "default_bone_index": -1,
    }

    def __init__(self, reader: BinaryReader = None, **kwargs):
        self.bone_indices = []
        self.face_sets = []
        self.vertex_buffers = []
        self.vertices = []
        self.invalid_vertex_size = False
        super().__init__(reader, **kwargs)

    def unpack(self, reader: BinaryReader, bounding_box_has_unknown: bool = None):
        mesh = reader.unpack_struct(self.STRUCT)

        bounding_box_offset = mesh.pop("__bounding_box_offset")
        if bounding_box_offset == 0:
            self.bounding_box = None
        else:
            with reader.temp_offset(bounding_box_offset):
                self.bounding_box = BoundingBoxWithUnknown(reader) if bounding_box_has_unknown else BoundingBox(reader)

        bone_count = mesh.pop("__bone_count")
        with reader.temp_offset(mesh.pop("__bone_offset")):
            self.bone_indices = list(reader.unpack(f"<{bone_count}i"))

        face_set_count = mesh.pop("__face_set_count")
        with reader.temp_offset(mesh.pop("__face_set_offset")):
            self._face_set_indices = list(reader.unpack(f"<{face_set_count}i"))

        vertex_count = mesh.pop("__vertex_buffer_count")
        with reader.temp_offset(mesh.pop("__vertex_buffer_offset")):
            self._vertex_buffer_indices = list(reader.unpack(f"<{vertex_count}i"))

        self.set(**mesh)

    def assign_face_sets(self, face_sets: tp.Dict[int, FaceSet]):
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

    def assign_vertex_buffers(self, vertex_buffers: tp.Dict[int, VertexBuffer], layouts: tp.List[BufferLayout]):
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

    def read_vertices(
        self,
        reader: BinaryReader,
        vertex_data_offset: int,
        layouts: tp.List[BufferLayout],
        uv_factor: int,
    ):
        self.vertices = [Vertex() for _ in range(self.vertex_buffers[0].vertex_count)]
        for vertex_buffer in self.vertex_buffers:
            vertex_buffer.read_buffer(reader, layouts, self.vertices, vertex_data_offset, uv_factor)

    def pack(self, writer: BinaryWriter):
        writer.pack_struct(
            self.STRUCT,
            self,
            __bounding_box_offset=writer.AUTO_RESERVE,
            __bone_count=len(self.bone_indices),
            __bone_offset=writer.AUTO_RESERVE,
            __face_set_count=len(self.face_sets),
            __face_set_offset=writer.AUTO_RESERVE,
            __vertex_buffer_count=len(self.vertex_buffers),
            __vertex_buffer_offset=writer.AUTO_RESERVE,
        )

    def pack_bounding_box(self, writer: BinaryWriter):
        if self.bounding_box is None:
            writer.fill("__bounding_box_offset", 0, obj=self)
        else:
            writer.fill("__bounding_box_offset", writer.position, obj=self)
            self.bounding_box.pack(writer)

    def pack_bone_indices(self, writer: BinaryWriter, bone_indices_start: int):
        if not self.bone_indices:
            # Weird case for byte-perfect writing.
            writer.fill("__bone_offset", bone_indices_start, obj=self)
        else:
            writer.fill("__bone_offset", writer.position, obj=self)
            writer.pack(f"{len(self.bone_indices)}i", *self.bone_indices)

    def pack_face_set_indices(self, writer: BinaryWriter, first_face_set_index: int):
        writer.fill("__face_set_offset", writer.position, obj=self)
        mesh_face_set_indices = range(first_face_set_index, first_face_set_index + len(self.face_sets))
        writer.pack(f"{len(self.face_sets)}i", *mesh_face_set_indices)

    def pack_vertex_buffer_indices(self, writer: BinaryWriter, first_vertex_buffer_index: int):
        writer.fill("__vertex_buffer_offset", writer.position, obj=self)
        mesh_vertex_buffer_indices = range(
            first_vertex_buffer_index, first_vertex_buffer_index + len(self.vertex_buffers)
        )
        writer.pack(f"{len(self.vertex_buffers)}i", *mesh_vertex_buffer_indices)

    def to_obj(self, name="Mesh", vertex_offset=0) -> str:
        """Convert mesh vertices, normals, UVs, and faces to an OBJ string.

        Use `vertex_offset` to offset all vertex indices in face definitions (e.g. if other meshes' vertices have
        been defined in the same file).
        """
        lines = [f"o {name}"]
        for vertex in self.vertices:
            position = " ".join(str(x) for x in vertex.position)
            lines.append(f"v {position}")
        for vertex in self.vertices:
            normal = " ".join(str(x) for x in vertex.normal)
            lines.append(f"vn {normal}")
        for vertex in self.vertices:
            if len(vertex.uvs) > 1:
                print(vertex)
                raise NotImplementedError("Cannot convert mesh to OBJ because one or more vertices has multiple UVs.")
            uv = " ".join(str(x) for x in vertex.uvs[0])
            lines.append(f"vt {uv}")
        for i, face_set in enumerate(self.face_sets):
            lines.append(f"# Face Set {i}")
            triangles = face_set.triangulate(self.allow_primitive_restarts)
            for j in range(0, len(triangles), 3):
                # TODO: Are these UV/normal assignments correct, given that each vertex has one?
                face = " ".join("/".join([str(v + vertex_offset + 1)] * 3) for v in triangles[j:j + 3])
                lines.append(f"f {face}")
        return "\n".join(lines)

    @property
    def allow_primitive_restarts(self):
        return len(self.vertices) < 0xFFFF

    def draw(
        self,
        vertex_color="red",
        show_normals=True,
        show_face_sets=(),
        show_origin=False,
        auto_show=False,
        axes=None,
        random_face_colors=False,
        **kwargs,
    ):
        import matplotlib.pyplot as plt
        if axes is None:
            axes = plt.figure().add_subplot(111, projection="3d")
        positions = [v.position.swap_yz() for v in self.vertices]
        axes.scatter(*zip(*positions), c=vertex_color, s=1, alpha=0.1)  # note y/z swapped
        if show_normals:
            normals = [v.normal.swap_yz() for v in self.vertices]
            for position, normal in zip(positions, normals):
                axes.plot(*zip(position, position + normal), c="black", alpha=0.1)
        if show_origin:
            axes.scatter(0, 0, 0, c="black", marker="x", s=5)
        if show_face_sets == "all":
            show_face_sets = tuple(range(len(self.face_sets)))
        if show_face_sets:
            import numpy as np
            from mpl_toolkits.mplot3d import art3d
            vertices = np.array([list(v.position.swap_yz()) for v in self.vertices])
            faces = []
            for i, face_set in enumerate(self.face_sets):
                if i in show_face_sets:
                    faces += [tri for tri in face_set.get_triangles(False)]
            faces = np.array(faces)
            face_colors = list(range(len(faces)))
            if random_face_colors:
                random.shuffle(face_colors)
            colors = np.array(face_colors)
            norm = plt.Normalize(colors.min(initial=0), colors.max(initial=1))
            # noinspection PyUnresolvedReferences
            colors = plt.cm.rainbow(norm(colors))
            pc = art3d.Poly3DCollection(vertices[faces], facecolors=colors, edgecolor="black", linewidth=0.1)
            axes.add_collection(pc)
        axes.set(**kwargs)
        if auto_show:
            plt.show()

    def __repr__(self):
        # vertices = ",\n".join([f"    {v.repr_position_only()}" for v in self.vertices])
        face_sets = ",\n".join(["    " + indent_lines(repr(f)) for f in self.face_sets])
        lines = [
            "Mesh(",
            f"  material_index = {self.material_index}",
            f"  default_bone_index = {self.default_bone_index}",
            f"  bone_indices = {self.bone_indices}",
            f"  vertices = {len(self.vertices)} vertices",

        ]
        if not self.is_bind_pose:
            lines.append("  is_bind_post = False")
        if self.bounding_box:
            lines.append(f"  bounding_box = {self.bounding_box}")
        lines.append(f"  face_sets = [\n{face_sets}\n  ]")
        lines.append(")")

        return "\n".join(lines)
