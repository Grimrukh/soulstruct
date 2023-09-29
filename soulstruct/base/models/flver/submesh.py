from __future__ import annotations

__all__ = ["FaceSetFlags", "FaceSet", "Submesh"]

import logging
import random
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

import numpy as np

from soulstruct.utilities.text import indent_lines
from soulstruct.utilities.binary import *

from .bounding_box import BoundingBox, BoundingBoxWithUnknown
from .vertex import BufferLayout, VertexBuffer

if tp.TYPE_CHECKING:
    from .core import FLVER
    from .material import Material

_LOGGER = logging.getLogger(__name__)


class FaceSetFlags(IntEnum):

    LodLevel1 = 0b0000_0001
    LodLevel2 = 0b0000_0010
    EdgeCompressed = 0b0100_0000
    MotionBlur = 0b1000_0000

    def has_flag(self, flag_int: int):
        return flag_int & self.value


@dataclass(slots=True)
class FaceSetStruct(BinaryStruct):

    _pad1: bytes = field(init=False, **BinaryPad(3))
    flags: byte
    triangle_strip: bool
    cull_back_faces: bool
    unk_x06: short
    _vertex_indices_count: int
    _vertex_indices_offset: int
    # NOTE: Fields stop here for FLVER versions < 0x20005, which are not supported by Soulstruct.
    _vertex_indices_length: int  # len(self.vertex_indices) * vertex_index_size // 8
    _pad2: bytes = field(init=False, **BinaryPad(4))
    _vertex_index_size: int = field(**Binary(asserted=[0, 16, 32]))  # 0 means size is set by FLVER header
    _pad3: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True)
class FaceSet:

    flags: int
    triangle_strip: bool
    cull_back_faces: bool
    unk_x06: int
    vertex_indices: list[int] = field(default_factory=list)  # TODO: any advantage to making this a NumPy array?

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, header_vertex_index_size: int, vertex_data_offset: int) -> FaceSet:
        face_set_struct = FaceSetStruct.from_bytes(reader)

        vertex_index_size = face_set_struct.pop("_vertex_index_size")
        if vertex_index_size == 0:
            vertex_index_size = header_vertex_index_size

        if vertex_index_size == 8:
            raise NotImplementedError("Soulstruct cannot support edge-compressed FLVER face sets.")
        elif vertex_index_size in {16, 32}:
            vertex_indices_count = face_set_struct.pop("_vertex_indices_count")
            vertex_indices_offset = face_set_struct.pop("_vertex_indices_offset")
            with reader.temp_offset(vertex_data_offset + vertex_indices_offset):
                fmt = f"<{vertex_indices_count}{'H' if vertex_index_size == 16 else 'I'}"
                vertex_indices = list(reader.unpack(fmt))
        else:
            raise ValueError(f"Unsupported face set index size: {vertex_index_size}")
        return face_set_struct.to_object(cls, vertex_indices=vertex_indices)

    def to_flver_writer(self, writer: BinaryWriter, vertex_index_size: int):
        face_set_struct = FaceSetStruct.from_object(
            self,
            _vertex_indices_count=len(self.vertex_indices),
            _vertex_indices_offset=None,  # reserved
            _vertex_indices_length=len(self.vertex_indices) * vertex_index_size // 8,
            _vertex_index_size=vertex_index_size,
        )
        face_set_struct.to_writer(writer, reserve_obj=self)

    def pack_vertex_indices(self, writer: BinaryWriter, vertex_index_size: int, vertex_indices_offset: int):
        writer.fill("_vertex_indices_offset", vertex_indices_offset, obj=self)
        if vertex_index_size == 16:
            fmt = f"{len(self.vertex_indices)}H"
        elif vertex_index_size == 32:
            fmt = f"{len(self.vertex_indices)}i"
        else:
            raise NotImplementedError(f"Unsupported vertex index size for `pack()`: {vertex_index_size}")
        writer.pack(fmt, *self.vertex_indices)

    def get_face_counts(self, allow_primitive_restarts: bool) -> tuple[int, int]:
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

    def triangulate(self, allow_primitive_restarts: bool, include_degenerate_faces=False) -> list[int]:
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
        self, allow_primitive_restarts: bool, include_degenerate_faces=False, vertex_index_offset=0
    ) -> list[tuple[int, int, int]]:
        """Get triangle list and return the triplets as tuples inside a list."""
        tri = self.triangulate(allow_primitive_restarts, include_degenerate_faces)
        return [
            (
                vertex_index_offset + tri[i],
                vertex_index_offset + tri[i + 1],
                vertex_index_offset + tri[i + 2]
            ) for i in range(0, len(tri), 3)
        ]

    def get_connected_vertex_indices(self, vertex_index: int) -> set[int]:
        """Find all vertices connected to the given `vertex_index`, including `vertex_index` itself."""
        triangles = self.get_triangles(allow_primitive_restarts=False, include_degenerate_faces=False)
        connected = {vertex_index}
        for tri in (set(t) for t in triangles):
            if connected.intersection(tri):
                connected |= tri
        return connected

    @classmethod
    def from_triangles(cls, triangles: list[tuple[int, int, int], ...], cull_back_faces=True):
        """Create a `FaceSet` with `triangle_strip=False` from a list of three-index triangle tuples.

        TODO: Currently sets `flags=0` and `unk_x06=0`, which is correct so far in my usage.
        """

        if isinstance(triangles, np.ndarray):
            vertex_indices = triangles.ravel().tolist()
        else:
            vertex_indices = [i for tri in triangles for i in tri]

        return cls(
            flags=0,
            unk_x06=0,
            triangle_strip=False,
            cull_back_faces=cull_back_faces,
            vertex_indices=vertex_indices,
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


@dataclass(slots=True)
class SubmeshStruct(BinaryStruct):

    is_bind_pose: bool
    _pad1: bytes = field(init=False, **BinaryPad(3))
    material_index: int
    _pad2: bytes = field(init=False, **BinaryPad(8))
    default_bone_index: int
    _bone_count: int
    _bounding_box_offset: int
    _bone_offset: int
    _face_set_count: int
    _face_set_offset: int
    _vertex_buffer_count: int = field(**Binary(asserted=[1, 2, 3]))
    _vertex_buffer_offset: int


@dataclass(slots=True)
class Submesh:
    """A single FLVER submesh that uses a single material.

    FLVER files are exported 3D model files optimized for rendering, not editing. Model faces with different materials
    are thus already split up into multiple submeshes, and may even be split further to handle large bone counts (older
    games like DS1 cannot support more than 38 bones per submesh).
    """

    FaceSet: tp.ClassVar[tp.Type[FaceSet]] = FaceSet

    is_bind_pose: bool = False
    material_index: int = 0
    default_bone_index: int = -1
    bone_indices: np.ndarray | None = None
    bounding_box: tp.Optional[BoundingBox] = None
    face_sets: list[FaceSet] = field(default_factory=list)
    vertex_buffers: list[VertexBuffer] = field(default_factory=list)
    vertex_arrays: list[np.ndarray] = field(default_factory=list)

    invalid_layout_size: bool = False

    # Held temporarily while unpacking.
    _face_set_indices: list[int] | None = field(default=None, init=False)
    _vertex_buffer_indices: list[int] | None = field(default=None, init=False)

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, bounding_box_has_unknown: bool = None):
        mesh_struct = SubmeshStruct.from_bytes(reader)

        _bone_count = mesh_struct.pop("_bone_count")
        _bounding_box_offset = mesh_struct.pop("_bounding_box_offset")
        _bone_offset = mesh_struct.pop("_bone_offset")
        _face_set_count = mesh_struct.pop("_face_set_count")
        _face_set_offset = mesh_struct.pop("_face_set_offset")
        _vertex_buffer_count = mesh_struct.pop("_vertex_buffer_count")
        _vertex_buffer_offset = mesh_struct.pop("_vertex_buffer_offset")

        bone_indices = np.array(reader.unpack(f"{_bone_count}i", offset=_bone_offset)) if _bone_count > 0 else None

        _face_set_indices = list(reader.unpack(f"{_face_set_count}i", offset=_face_set_offset))
        _vertex_buffer_indices = list(reader.unpack(f"{_vertex_buffer_count}i", offset=_vertex_buffer_offset))

        if _bounding_box_offset != 0:
            with reader.temp_offset(_bounding_box_offset):
                box_class = BoundingBoxWithUnknown if bounding_box_has_unknown else BoundingBox
                bounding_box = box_class.from_bytes(reader)
        else:
            bounding_box = None
        submesh = mesh_struct.to_object(
            cls,
            bone_indices=bone_indices,
            bounding_box=bounding_box,
        )
        submesh._face_set_indices = _face_set_indices
        submesh._vertex_buffer_indices = _vertex_buffer_indices
        return submesh

    @property
    def vertices(self):
        """Shortcut for accessing the first vertex array (generally the only array)."""
        return self.vertex_arrays[0]

    def assign_face_sets(self, face_sets: dict[int, FaceSet]):
        self.face_sets = []
        for i in self._face_set_indices:
            if i not in face_sets:
                raise KeyError(
                    f"Tried to assign `FaceSet` with index {i} to `Submesh`, but the `FaceSet` has "
                    "already been assigned to another `Submesh` (or does not exist)."
                )
            self.face_sets.append(face_sets.pop(i))
        self._face_set_indices = None

    def assign_vertex_buffers(self, vertex_buffers: dict[int, VertexBuffer], layouts: list[BufferLayout]):
        self.vertex_buffers = []
        for i in self._vertex_buffer_indices:
            if i not in vertex_buffers:
                raise KeyError(
                    f"Tried to assign `VertexBuffer` with index {i} to `Submesh`, but the `VertexBuffer` has "
                    "already been assigned to another `Submesh` (or does not exist)."
                )
            self.vertex_buffers.append(vertex_buffers.pop(i))
        self._vertex_buffer_indices = None

        # Check that all vertex buffers for this submesh have the same length.
        if self.vertex_buffers:
            if len({buffer.get_vertex_count() for buffer in self.vertex_buffers}) != 1:
                raise ValueError("Vertex buffers for submesh do not all have the same size.")
        else:
            _LOGGER.warning("Submesh has no vertex buffers.")

        # Check that per-mesh unique `MemberType`s do not occur more than once among all members of all buffers.
        existing_types = set()
        for vertex_buffer in self.vertex_buffers:
            for member in layouts[vertex_buffer.layout_index]:
                if member.member_type.is_unique():
                    if member.member_type in existing_types:
                        raise ValueError(
                            f"Unique `LayoutFormat` {member.member_type} found more than once in `BufferLayouts` "
                            f"of `Submesh`."
                        )
                    existing_types.add(member.member_type)

        # TODO: SoulsFormats does an extra check here for edge-compressed vertex buffers, which are not supported here.

    def to_flver_writer(self, writer: BinaryWriter):
        SubmeshStruct.object_to_writer(
            self,
            writer,
            _bone_count=len(self.bone_indices) if self.bone_indices is not None else 0,
            _face_set_count=len(self.face_sets),
            _vertex_buffer_count=len(self.vertex_buffers),
        )

    def pack_bounding_box(self, writer: BinaryWriter):
        if self.bounding_box is None:
            writer.fill("_bounding_box_offset", 0, obj=self)
        else:
            writer.fill_with_position("_bounding_box_offset", obj=self)
            self.bounding_box.to_writer(writer)

    def pack_bone_indices(self, writer: BinaryWriter, bone_indices_start: int):
        if not self.bone_indices:
            # Weird case for byte-perfect writing.
            writer.fill("_bone_offset", bone_indices_start, obj=self)
        else:
            writer.fill_with_position("_bone_offset", obj=self)
            writer.pack(f"{len(self.bone_indices)}i", *self.bone_indices)

    def pack_face_set_indices(self, writer: BinaryWriter, first_face_set_index: int):
        face_set_indices = [first_face_set_index + i for i in range(len(self.face_sets))]
        writer.fill_with_position("_face_set_offset", obj=self)
        writer.pack(f"{len(face_set_indices)}i", *face_set_indices)

    def pack_vertex_buffer_indices(self, writer: BinaryWriter, first_vertex_buffer_index: int):
        vertex_buffer_indices = [first_vertex_buffer_index + i for i in range(len(self.vertex_buffers))]
        writer.fill_with_position("_vertex_buffer_offset", obj=self)
        writer.pack(f"{len(vertex_buffer_indices)}i", *vertex_buffer_indices)

    def local_to_global_bone_indices(self):
        """Transforms `vertex_array` in-place by replacing all `bone_index_{c}` indices with the global bone index in
        `mesh.bone_indices` that the vertex indexes, and remove local bone indices from the mesh (consistent with later
        games that use global bone indices by default).

        Will raise a `ValueError` if `mesh.bone_indices` is already None (implying vertex bone indices are already
        global).
        """
        if self.bone_indices is None:
            raise ValueError("Cannot convert local vertex bone indices to global because `mesh.bone_indices` is None.")
        for vertex_array in self.vertex_arrays:
            for c in "abcd":
                local_bone_index = vertex_array[f"bone_index_{c}"]
                vertex_array[f"bone_index_{c}"] = self.bone_indices[local_bone_index]
        self.bone_indices = None

    def to_obj(self, name="Submesh", vertex_offset=0, vertex_array=0) -> str:
        """Convert mesh vertices, normals, UVs, and faces to an OBJ string.

        Use `vertex_offset` to offset all vertex indices in face definitions (e.g. if other meshes' vertices have
        been defined in the same file).
        """
        lines = [f"o {name}"]

        # Check if vertices record array has 'uv_u_1' field:
        vertex = self.vertices[0]
        if "uv_u_1" in vertex:
            raise NotImplementedError("Cannot convert mesh to OBJ because one or more vertices has multiple UVs.")

        for position in self.vertex_arrays[0][[f"position_{c}" for c in "xyz"]]:
            pos_str = " ".join(str(x) for x in position)
            lines.append(f"v {pos_str}")
        for normal in self.vertex_arrays[0][[f"normal_{c}" for c in "abcd"]]:
            normal_str = " ".join(str(x) for x in normal)
            lines.append(f"vn {normal_str}")
        for uv in self.vertex_arrays[0][["uv_u_0", "uv_v_0"]]:
            uv_str = " ".join(str(x) for x in uv)
            lines.append(f"vt {uv_str}")
        for i, face_set in enumerate(self.face_sets):
            lines.append(f"# Face Set {i}")
            triangles = face_set.triangulate(allow_primitive_restarts=len(self.vertex_arrays[vertex_array] > 0xFFFF))
            for j in range(0, len(triangles), 3):
                # TODO: Are these UV/normal assignments correct, given that each vertex has one?
                face = " ".join("/".join([str(v + vertex_offset + 1)] * 3) for v in triangles[j:j + 3])
                lines.append(f"f {face}")
        return "\n".join(lines)

    def get_material(self, flver: FLVER) -> Material:
        """Shortcut accessor."""
        if self.material_index < 0:
            raise ValueError(f"Submesh has negative material index: {self.material_index}")
        return flver.materials[self.material_index]

    @property
    def layout_index(self):
        """Shortcut for returning `vertex_buffers[0].layout_index`. Raises an error if there are 2+ vertex buffers."""
        # TODO: vertex buffers should not be 'kept' after reading a FLVER at all. Store layout index/indices on submesh.
        if not self.vertex_buffers:
            raise ValueError("Submesh has no vertex buffers.")
        if len(self.vertex_buffers) > 1:
            raise ValueError("Submesh has multiple vertex buffers. Cannot use `layout_index` shortcut property.")
        return self.vertex_buffers[0].layout_index

    def get_buffer_layout(self, flver: FLVER, vertex_buffer_index=0) -> BufferLayout:
        """Shortcut for returning `flver.buffer_layouts[self.vertex_buffers[vertex_buffer_index].layout_index]`."""
        return flver.buffer_layouts[self.vertex_buffers[vertex_buffer_index].layout_index]

    def set_buffer_layout(self, flver: FLVER, layout: BufferLayout, vertex_buffer_index=0):
        """Shortcut for setting `flver.buffer_layouts[self.vertex_buffers[vertex_buffer_index].layout_index]`.

        Note, of course, that other meshes could be pointing to the same layout index! Make sure they are also both
        using the same material in that case.
        """
        flver.buffer_layouts[self.vertex_buffers[vertex_buffer_index].layout_index] = layout

    @property
    def cull_back_faces(self):
        """Get `cull_back_faces` from face set 0 and warn if other face sets have different values."""
        if not self.face_sets:
            _LOGGER.warning("Submesh has no face sets.")
            return False
        cull = self.face_sets[0].cull_back_faces
        for face_set in self.face_sets[1:]:
            if face_set.cull_back_faces != cull:
                _LOGGER.warning(f"Submesh has face sets with different `cull_back_faces` values. Using index 0: {cull}")
                return cull
        return cull

    @cull_back_faces.setter
    def cull_back_faces(self, value):
        """Set `cull_back_faces` for all face sets."""
        for face_set in self.face_sets:
            face_set.cull_back_faces = value

    def vertex_count_exceeds_ushort(self, vertex_array=0):
        return len(self.vertex_arrays[vertex_array]) < 0xFFFF

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
        positions = self.vertex_arrays[0][["position_x", "position_z", "position_y"]]
        axes.scatter(*zip(*positions), c=vertex_color, s=1, alpha=0.1)  # note y/z swapped
        if show_normals:
            normals = self.vertex_arrays[0][["normal_x", "normal_z", "normal_y"]]
            for position, normal in zip(positions, normals):
                axes.plot(*zip(position, position + normal), c="black", alpha=0.1)
        if show_origin:
            axes.scatter(0, 0, 0, c="black", marker="x", s=5)
        if show_face_sets == "all":
            show_face_sets = tuple(range(len(self.face_sets)))
        if show_face_sets:
            from mpl_toolkits.mplot3d import art3d
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
            pc = art3d.Poly3DCollection(positions[faces], facecolors=colors, edgecolor="black", linewidth=0.1)
            axes.add_collection(pc)
        axes.set(**kwargs)
        if auto_show:
            plt.show()

    def __repr__(self):
        face_sets = ",\n".join(["    " + indent_lines(repr(f)) for f in self.face_sets])
        lines = [
            "Submesh(",
            f"  material_index = {self.material_index}",
            f"  default_bone_index = {self.default_bone_index}",
            f"  bone_indices = {self.bone_indices}",
            f"  vertices = {len(self.vertices)} vertices",

        ]
        if not self.is_bind_pose:
            lines.append("  is_bind_pose = False")
        if self.bounding_box:
            lines.append(f"  bounding_box = {self.bounding_box}")
        lines.append(f"  face_sets = [\n{face_sets}\n  ]")
        lines.append(")")

        return "\n".join(lines)
