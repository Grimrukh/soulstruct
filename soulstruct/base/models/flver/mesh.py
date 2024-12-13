from __future__ import annotations

__all__ = ["FLVERMesh"]

import logging
import random
import typing as tp
from dataclasses import dataclass, field

import numpy as np

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.text import indent_lines
from .face_set import FaceSet
from .material import Material
from .vertex_array import VertexArray
from .vertex_array_layout import VertexArrayLayout
from .version import FLVERVersion

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class FLVERMesh:
    """FLVER 'submesh' that uses a single `Material`, a single `VertexArray` (despite appearing in a list), and one or
    more `FaceSet`s.

    FLVER files are exported 3D model files optimized for rendering, not editing. Model faces with different materials
    are thus already split up into multiple meshes, and may even be split further to handle large bone counts (older
    games like DS1 cannot support more than 38 bones per mesh).

    Soulstruct assigns FLVER `Material` instances directly to meshes. When packing the `FLVER`, identical materials
    used by multiple meshes will be merged.

    NOTE: In the modern FLVER2 format (2011+), each mesh stores its face data in a separate class called `FaceSet`.
    While the old FLVER0 format (Demon's Souls) does not use this class and instead stores its single face set (and
    relevant properties) directly in the `FLVERMesh` class, a single-set `FaceSet` is used here to unify the formats.
    """

    class STRUCT0(BinaryStruct):
        is_bind_pose: bool  # NOTE: named `dynamic` in SoulsFormats but clearly identical to `FLVER2.is_bind_pose`
        material_index: byte
        # start of "FaceSet properties"
        use_backface_culling: bool
        is_triangle_strip: bool  # NOTE: always `False` in version 0x14 (old Demon's Souls) but strips ARE used
        vertex_index_count: int
        # end of "FaceSet properties"
        vertex_count: int
        default_bone_index: short
        bone_indices: list[short] = binary_array(28)
        unk_x46: short
        vertex_indices_size: int  # size of vertex indices in bytes (computable if `vertex_index_count` given)
        vertex_indices_offset: int  # relative to FLVER0 vertex data offset
        vertex_array_data_size: int  # only used if header offset 1 is zero
        vertex_array_data_offset: int  # only used if header offset 1 is zero
        vertex_array_headers_offset_1: int
        vertex_array_headers_offset_2: int
        _pad0: bytes = binary_pad(4, init=False)

    class STRUCT2(BinaryStruct):
        is_bind_pose: bool
        _pad1: bytes = binary_pad(3, init=False)
        _material_index: int
        _pad2: bytes = binary_pad(8, init=False)
        default_bone_index: int
        _bone_count: int
        _bounding_box_offset: int
        _bone_offset: int
        _face_set_count: int
        _face_set_offset: int
        _vertex_array_count: int = binary(asserted=[1, 2, 3])
        _vertex_array_offset: int

    is_bind_pose: bool
    material: Material
    default_bone_index: int
    bone_indices: np.ndarray | None  # NOTE: cannot be `None` in `FLVER0` (always a 28-element array)
    vertex_arrays: list[VertexArray]  # only ever has one element in all known FLVERs
    face_sets: list[FaceSet]

    # Written by FLVER0 versions only:
    f0_unk_x46: int = 0

    # Written by FLVER2 versions only:
    uses_bounding_boxes: bool = True  # TODO: perfect candidate for a game-specific subclass ClassVar
    # TODO: These are clearly NOT min/max in later games that use the third vector below.
    #  'min' seems to be roughly half the extent of the bounding box, but it's quite rough.
    #   - center in 'local box coordinates'?
    #  'max' is quite smaller and sometimes even negative. Not quite contained to [-1, 1] range though.
    #   - center in 'FLVER bounding box normalized coordinates'?
    bounding_box_min: Vector3 = field(default_factory=Vector3.single_max)
    bounding_box_max: Vector3 = field(default_factory=Vector3.single_min)
    # TODO: Seems to be VERY close to the center of the mesh bounding box in FLVER space.
    bounding_box_unknown: Vector3 | None = None  # only used in Sekiro onward  # TODO: see above

    # Set by `FLVER` on initial creation, for convenience, to quickly identify meshes without needing `enumerate()`.
    # Can be updated with `flver.refresh_mesh_indices()`.
    index: int = -1
    # Enabled by Soulstruct when a bad layout was (attempted to be) fixed.
    layout_fixed: bool = False
    # Enabled by Soulstruct when trying to read a vertex array from a FLVER (usually DS1R) with the wrong layout.
    invalid_layout: bool = False

    # Held temporarily while unpacking FLVER2.
    _face_set_indices: list[int] | None = field(default=None, init=False)
    _vertex_array_indices: list[int] | None = field(default=None, init=False)

    @classmethod
    def from_flver0_reader(
        cls,
        reader: BinaryReader,
        vertex_index_bit_size: int,
        vertex_data_offset: int,
        materials: list[Material],
        version: FLVERVersion,
    ) -> tp.Self:
        mesh_struct = cls.STRUCT0.from_bytes(reader)

        material = materials[mesh_struct.material_index]

        if vertex_index_bit_size not in {16, 32}:
            # In practice, always 16 right now.
            raise ValueError(f"Unsupported vertex index size for `FLVER0` mesh: {vertex_index_bit_size}")

        vertex_index_fmt = f"{mesh_struct.vertex_index_count}{'H' if vertex_index_bit_size == 16 else 'i'}"
        vertex_indices_offset = vertex_data_offset + mesh_struct.vertex_indices_offset
        vertex_indices = list(reader.unpack(vertex_index_fmt, offset=vertex_indices_offset))

        # Weird array setup: two different lists of vertex arrays, and we only expect the first of the first to be used.
        # We also need a hack for older FLVER versions (e.g. Demon's Souls o9993) with neither array offset used.
        if mesh_struct.vertex_array_headers_offset_1 == 0:
            # Hack for old FLVER version.
            array_header = VertexArray.HEADER0(
                layout_index=0,
                array_length=mesh_struct.vertex_array_data_size,
                array_offset=mesh_struct.vertex_array_data_offset,
            )
        else:
            with reader.temp_offset(mesh_struct.vertex_array_headers_offset_1):
                array_headers = VertexArray.read_flver0_header_list(reader)
                if len(array_headers) == 0:
                    raise ValueError("No vertex arrays found at first array header offset in mesh.")
                for header in array_headers[1:]:
                    if header.array_length != 0:
                        raise ValueError("Multiple non-empty vertex arrays found in mesh, but only one expected.")
            array_header = array_headers[0]

        if mesh_struct.vertex_array_headers_offset_2 != 0:
            # We expect no arrays here.
            with reader.temp_offset(mesh_struct.vertex_array_headers_offset_2):
                array_headers = VertexArray.read_flver0_header_list(reader)
                if len(array_headers) > 0:
                    raise ValueError("Unexpected vertex arrays found at second array header offset in mesh.")

        # NOTE: Hacky way to determine UV factor.
        uv_factor = 1024 if reader.byte_order == ByteOrder.BigEndian else 2048
        vertex_array = VertexArray.from_flver0_reader(
            reader, array_header, material._layouts, vertex_data_offset, uv_factor
        )

        # Convert vertex indices to numpy array. We use `uint32` regardless of vertex index size.
        vertex_indices_array = np.array(vertex_indices, dtype=np.uint32)

        if version < FLVERVersion.DemonsSouls:
            # `is_triangle_strip` is False in these old FLVERs even though it IS actually a strip.
            # For this reason, I doubt this version supports non-strips.
            is_triangle_strip = True
            if 0xFFFF not in vertex_indices:
                _LOGGER.warning("Old Demon's Souls FLVER0 mesh does not contain any 0xFFFF strip separators.")
        else:
            is_triangle_strip = mesh_struct.is_triangle_strip

        if not is_triangle_strip:
            # Reshape vertex indices to `(n, 3)` 2D array for non-strip faces.
            vertex_indices_array = vertex_indices_array.reshape((-1, 3))

        # Create our lone dummy `FaceSet` for FLVER0.
        face_set = FaceSet(
            flags=0,  # not used in FLVER0
            is_triangle_strip=is_triangle_strip,
            use_backface_culling=mesh_struct.use_backface_culling,
            unk_x06=0,  # not used in FLVER0
            vertex_indices=vertex_indices_array,
        )

        return cls(
            is_bind_pose=mesh_struct.is_bind_pose,
            material=material,
            default_bone_index=mesh_struct.default_bone_index,
            bone_indices=np.array(mesh_struct.bone_indices),
            f0_unk_x46=mesh_struct.unk_x46,
            vertex_arrays=[vertex_array],
            face_sets=[face_set],
            # NOTE: We leave `uses_bounding_boxes = True` for easy FLVER2 conversion.
        )

    @classmethod
    def from_flver2_reader(
        cls,
        reader: BinaryReader,
        materials: list[Material],
        bounding_box_has_unknown: bool,
        index: int,
    ):
        mesh_struct = cls.STRUCT2.from_bytes(reader)

        _material_index = mesh_struct.pop("_material_index")
        _bone_count = mesh_struct.pop("_bone_count")
        _bounding_box_offset = mesh_struct.pop("_bounding_box_offset")
        _bone_offset = mesh_struct.pop("_bone_offset")
        _face_set_count = mesh_struct.pop("_face_set_count")
        _face_set_offset = mesh_struct.pop("_face_set_offset")
        _vertex_array_count = mesh_struct.pop("_vertex_array_count")
        _vertex_array_offset = mesh_struct.pop("_vertex_array_offset")

        bone_indices = np.array(reader.unpack(f"{_bone_count}i", offset=_bone_offset)) if _bone_count > 0 else None

        _face_set_indices = list(reader.unpack(f"{_face_set_count}i", offset=_face_set_offset))
        _vertex_array_indices = list(reader.unpack(f"{_vertex_array_count}i", offset=_vertex_array_offset))

        kwargs = {}
        if _bounding_box_offset != 0:
            with reader.temp_offset(_bounding_box_offset):
                kwargs["bounding_box_min"] = Vector3(reader.unpack("3f"))
                kwargs["bounding_box_max"] = Vector3(reader.unpack("3f"))
                kwargs["bounding_box_unknown"] = Vector3(reader.unpack("3f")) if bounding_box_has_unknown else None
        else:
            kwargs["uses_bounding_boxes"] = False

        mesh = mesh_struct.to_object(
            cls,
            material=materials[_material_index],
            bone_indices=bone_indices,
            index=index,
            vertex_arrays=[],
            face_sets=[],
            **kwargs,
        )
        mesh._face_set_indices = _face_set_indices
        mesh._vertex_array_indices = _vertex_array_indices
        return mesh

    def dereference_flver2_face_sets(self, face_sets: dict[int, FaceSet]):
        self.face_sets = []
        for i in self._face_set_indices:
            if i not in face_sets:
                raise KeyError(
                    f"Tried to assign `FaceSet` with index {i} to `FLVERMesh`, but the `FaceSet` has "
                    "already been assigned to another `FLVERMesh` (or does not exist)."
                )
            self.face_sets.append(face_sets.pop(i))
        self._face_set_indices = None

    def dereference_flver2_vertex_arrays(self, vertex_arrays: dict[int, VertexArray]):
        self.vertex_arrays = []
        for i in self._vertex_array_indices:
            if i not in vertex_arrays:
                raise KeyError(
                    f"Tried to assign `VertexBuffer` with index {i} to `FLVERMesh`, but the `VertexBuffer` has "
                    "already been assigned to another `FLVERMesh` (or does not exist)."
                )
            self.vertex_arrays.append(vertex_arrays.pop(i))
        self._vertex_array_indices = None

        # Check that all vertex arrays for this mesh have the same length.
        if self.vertex_arrays:
            if len({len(vertex_array.array) for vertex_array in self.vertex_arrays}) != 1:
                raise ValueError("Vertex arrays for mesh do not all have the same size.")
        else:
            _LOGGER.warning("Mesh has no vertex arrays.")

        if any(vertex_array.array.size == 0 for vertex_array in self.vertex_arrays):
            mat_def_name = self.material.mat_def_name if self.material else '<unknown>'
            _LOGGER.warning(
                f"Mesh in FLVER (mat def '{mat_def_name}') has an incorrect layout that could not be fixed. Mesh "
                f"marked with `invalid_layout = True`; handle this as needed."
            )
            self.invalid_layout = True

        # TODO: SoulsFormats does an extra check here for edge-compressed vertex arrays, which are not supported here.

    def to_flver0_writer(self, writer: BinaryWriter, vertex_index_bit_size: int, material_index: int):
        """Materials already collected FLVER-wide and indexed passed in here."""
        if len(self.vertex_arrays) != 1:
            raise ValueError("`FLVER0` mesh must have exactly one VertexArray.")
        if len(self.face_sets) != 1:
            raise ValueError("`FLVER0` mesh must have exactly one FaceSet.")
        if self.bone_indices is None:
            raise ValueError("`FLVER0` mesh must have a `bone_indices` array with 1 to 28 elements, not `None`.")
        if len(self.bone_indices) > 28:
            raise ValueError(f"`FLVER0` mesh can only have 28 bone indices. Too many: {self.bone_indices}")
        face_set = self.face_sets[0]
        if face_set.flags != 0:
            _LOGGER.warning(f"FaceSet `flags` not used in FLVER0. Non-zero flags {face_set.flags} ignored.")
        if face_set.unk_x06 != 0:
            _LOGGER.warning(f"FaceSet `unk_x06` not used in FLVER0. Non-zero value {face_set.unk_x06} ignored.")

        vertex_array = self.vertex_arrays[0]
        vertex_count = len(vertex_array.array)
        vertex_index_count = face_set.vertex_indices.size  # NOT `len()`
        vertex_array_data_size = vertex_array.layout.get_total_data_size() * vertex_count

        bone_indices = self.bone_indices.tolist()
        if len(bone_indices) < 28:
            # Pad out with -1.
            bone_indices += [-1] * (28 - len(bone_indices))

        mesh_struct = self.STRUCT0(
            is_bind_pose=self.is_bind_pose,
            material_index=material_index,
            use_backface_culling=face_set.use_backface_culling,
            is_triangle_strip=face_set.is_triangle_strip,
            vertex_index_count=vertex_index_count,
            vertex_count=vertex_count,
            default_bone_index=self.default_bone_index,
            bone_indices=bone_indices,
            unk_x46=self.f0_unk_x46,
            vertex_indices_size=(vertex_index_bit_size // 8) * vertex_index_count,
            vertex_indices_offset=RESERVED,
            vertex_array_data_size=vertex_array_data_size,
            vertex_array_data_offset=RESERVED,
            vertex_array_headers_offset_1=RESERVED,
            vertex_array_headers_offset_2=0,  # second header list never written
        )
        mesh_struct.to_writer(writer, reserve_obj=self)

    def pack_flver0_vertex_indices(self, writer: BinaryWriter, vertex_index_bit_size: int, vertex_indices_offset: int):
        face_set = self.face_sets[0]
        # Mesh header `vertex_indices_offset` is relative to FLVER0 vertex data offset.
        writer.fill("vertex_indices_offset", vertex_indices_offset, obj=self)
        flat_vertex_indices = face_set.vertex_indices.flatten()
        # `vertex_index_bit_size` will always be 16, currently.
        vertex_index_fmt = f"{len(flat_vertex_indices)}{'H' if vertex_index_bit_size == 16 else 'i'}"
        writer.pack(vertex_index_fmt, *flat_vertex_indices)

    def pack_flver0_vertex_array_header(self, writer: BinaryWriter, layout_index: int):
        """We only write a single header. Returns header struct for filling data offset later."""
        if len(self.vertex_arrays) != 1:
            raise ValueError("`FLVER0` mesh must have exactly one VertexArray.")
        writer.fill_with_position("vertex_array_headers_offset_1", obj=self)
        writer.pack("i", 1)  # array count
        writer.pack("i", writer.position + 12)  # very quick reserve/fill otherwise
        writer.pad(8)

        # Write single header.
        self.vertex_arrays[0].to_flver0_writer(writer, layout_index)

    def to_flver2_writer(self, writer: BinaryWriter, material_index: int):
        """Material index is the index into shared FLVER materials, so multiple meshes can point to the same one."""
        self.STRUCT2.object_to_writer(
            self,
            writer,
            _material_index=material_index,
            _bone_count=len(self.bone_indices) if self.bone_indices is not None else 0,
            _face_set_count=len(self.face_sets),
            _vertex_array_count=len(self.vertex_arrays),
        )

    def pack_flver2_bounding_boxes(self, writer: BinaryWriter):
        if not self.uses_bounding_boxes:
            writer.fill("_bounding_box_offset", 0, obj=self)
        else:
            writer.fill_with_position("_bounding_box_offset", obj=self)
            writer.pack("3f", *self.bounding_box_min)
            writer.pack("3f", *self.bounding_box_max)
            if self.bounding_box_unknown is not None:
                writer.pack("3f", *self.bounding_box_unknown)

    def pack_flver2_bone_indices(self, writer: BinaryWriter, bone_indices_start: int):
        if self.bone_indices is None:
            # Weird case for byte-perfect writing.
            writer.fill("_bone_offset", bone_indices_start, obj=self)
        else:
            writer.fill_with_position("_bone_offset", obj=self)
            writer.pack(f"{len(self.bone_indices)}i", *self.bone_indices)

    def pack_flver2_face_set_indices(self, writer: BinaryWriter, first_face_set_index: int):
        face_set_indices = [first_face_set_index + i for i in range(len(self.face_sets))]
        writer.fill_with_position("_face_set_offset", obj=self)
        writer.pack(f"{len(face_set_indices)}i", *face_set_indices)

    def pack_flver2_vertex_array_indices(self, writer: BinaryWriter, first_vertex_array_index: int):
        vertex_array_indices = [first_vertex_array_index + i for i in range(len(self.vertex_arrays))]
        writer.fill_with_position("_vertex_array_offset", obj=self)
        writer.pack(f"{len(vertex_array_indices)}i", *vertex_array_indices)

    # region FLVERMesh Methods

    @property
    def vertices(self) -> np.ndarray:
        """Shortcut for accessing the data of the first vertex array (generally the only array)."""
        return self.vertex_arrays[0].array

    @property
    def vertices_dtype(self) -> np.dtype:
        return self.vertices.dtype

    @property
    def layout(self) -> VertexArrayLayout:
        """Shortcut for accessing the layout of the first vertex array (always the only array)."""
        return self.vertex_arrays[0].layout

    @property
    def use_backface_culling(self) -> bool:
        """Backface culling is set per `FaceSet`, which makes this slightly complicated. All face sets should have the
        same value, which is enforced here. If there are no face sets, a `ValueError` is also raised."""
        if not self.face_sets:
            raise ValueError("Mesh has no face sets to check `use_backface_culling`.")
        cull = self.face_sets[0].use_backface_culling
        if any(face_set.use_backface_culling != cull for face_set in self.face_sets):
            raise ValueError("Mesh has multiple face sets with different `use_backface_culling` values.")
        return cull

    @use_backface_culling.setter
    def use_backface_culling(self, value: bool):
        """Set backface culling for all face sets in this mesh."""
        for face_set in self.face_sets:
            face_set.use_backface_culling = value

    def validate_unique_data_types(self):
        """Check that per-mesh unique `MemberType`s do not occur more than once among all members of all arrays."""
        existing_types = set()
        for vertex_array in self.vertex_arrays:
            for data_type in vertex_array.layout:
                if data_type.unique:
                    name = data_type.__class__.__name__
                    if name in existing_types:
                        raise ValueError(
                            f"Unique vertex data type `{name} found more than once across all vertex arrays of mesh."
                        )
                    existing_types.add(name)

    @property
    def first_face_set(self) -> FaceSet:
        return self.face_sets[0]

    def triangulate_flver0(self, include_degenerate_faces=False) -> np.ndarray:
        """Shortcut for triangulating first face set. Passes in vertices for a manual normal check set up by TK."""
        uses_0xffff_separators = len(self.vertices) < 0xFFFF  # should always be true for `FLVER0`
        return self.face_sets[0].triangulate(
            uses_0xffff_separators,
            include_degenerate_faces,
            flver0_vertices=self.vertices,
        )

    def triangulate_flver2(self, include_degenerate_faces=False) -> np.ndarray:
        """Shortcut for triangulating first face set."""
        uses_0xffff_separators = len(self.vertices) < 0xFFFF
        return self.face_sets[0].triangulate(uses_0xffff_separators, include_degenerate_faces)

    def refresh_bounding_boxes(self):
        if not self.uses_bounding_boxes:
            return  # nothing to refresh
        if not self.vertex_arrays:
            _LOGGER.warning("Mesh has no vertex arrays. Cannot refresh bounding box.")
            return
        self.bounding_box_min = Vector3.single_max()
        self.bounding_box_max = Vector3.single_min()
        for vertex_array in self.vertex_arrays:
            self.bounding_box_min = np.minimum(self.bounding_box_min, vertex_array.array["position"].min(axis=0))
            self.bounding_box_max = np.maximum(self.bounding_box_max, vertex_array.array["position"].max(axis=0))
        if self.bounding_box_unknown is not None:
            _LOGGER.warning("Cannot refresh `bounding_box_unknown` for Mesh (unknown values).")

    def to_obj(self, name: str = None, vertex_offset=0, vertex_array=0) -> str:
        """Convert mesh vertices, normals, UVs, and faces to an OBJ string.

        Use `vertex_offset` to offset all vertex indices in face definitions (e.g. if other meshes' vertices have
        been defined in the same file).
        """
        if name is None:
            name = f"{name}{self.index}"

        lines = [f"o {name}"]

        # Check if vertices record array has 'uv_u_1' field:
        vertex = self.vertices[0]
        if "uv_u_1" in vertex:
            raise NotImplementedError("Cannot convert mesh to OBJ because one or more vertices has multiple UVs.")
        array = self.vertex_arrays[0]

        for position in array[[f"position_{c}" for c in "xyz"]]:
            pos_str = " ".join(str(x) for x in position)
            lines.append(f"v {pos_str}")
        for normal in array[[f"normal_{c}" for c in "abcd"]]:
            normal_str = " ".join(str(x) for x in normal)
            lines.append(f"vn {normal_str}")
        for uv in array[["uv_u_0", "uv_v_0"]]:
            uv_str = " ".join(str(x) for x in uv)
            lines.append(f"vt {uv_str}")
        for i, face_set in enumerate(self.face_sets):
            lines.append(f"# Face Set {i}")
            triangles = face_set.triangulate(uses_0xffff_separators=len(self.vertex_arrays[vertex_array]) <= 0xFFFF)
            for j in range(0, len(triangles), 3):
                # TODO: Are these UV/normal assignments correct, given that each vertex has one?
                face = " ".join("/".join([str(v + vertex_offset + 1)] * 3) for v in triangles[j:j + 3])
                lines.append(f"f {face}")
        return "\n".join(lines)

    def sort_bone_indices(self):
        """Sort `bone_indices` in-place, if defined, and re-index all vertex data to match."""

        if self.bone_indices is None:
            return  # this mesh has global vertex bone indices

        sorted_indices = np.argsort(self.bone_indices)
        # Sort now, and use `sorted_indices` to remap vertex data below.
        self.bone_indices = self.bone_indices[sorted_indices]

        for vertex_array in self.vertex_arrays:
            try:
                bone_indices = vertex_array["bone_indices"]
            except ValueError:  # no bone indices
                continue

            # Check map piece 'pose' case, where weights are missing:
            try:
                bone_weights = vertex_array["bone_weights"]
            except ValueError:  # no weights
                # Map Piece case: all four indices should be the same number (all used) and can be safely re-indexed.
                vertex_array["bone_indices"] = sorted_indices[bone_indices]
            else:
                # Rigged case: at least one bone weight is non-zero, and we need to check which ones in order to
                # distinguish use of bone 0 from an unused bone index, unfortunately.

                # Get indices of all vertices with non-zero bone weights.
                used_indices = np.nonzero(bone_weights)[0]  # (n, 4) mask array
                vertex_array["bone_indices"][used_indices] = sorted_indices[bone_indices[used_indices]]

    def local_to_global_bone_indices(self):
        """Transforms `vertex_array` in-place by replacing all vertex bone indices with the global bone index in
        `mesh.bone_indices` that the vertex indexes, then clearing `self.bone_indices`.

        Will raise a `ValueError` if `mesh.bone_indices` is already None (implying vertex bone indices are already
        global).
        """
        if self.bone_indices is None:
            raise ValueError(
                "Cannot convert local vertex bone indices to global because `mesh.bone_indices` is None, suggesting "
                "that the vertex bone indices are already global FLVER bone indices."
            )
        for vertex_array in self.vertex_arrays:
            if not vertex_array.has_field("bone_indices"):
                continue
            # Simple re-index into global indices.
            vertex_array.array["bone_indices"] = self.bone_indices[vertex_array.array["bone_indices"]]
        self.bone_indices = None

    def draw_flver0(
        self,
        vertex_color="red",
        show_normals=True,
        show_origin=False,
        show_face_set=False,
        auto_show=False,
        axes=None,
        random_face_colors=False,
        **kwargs,
    ):
        def triangulate(face_set: FaceSet):
            return face_set.triangulate(
                uses_0xffff_separators=len(self.vertices) <= 0xFFFF,
                include_degenerate_faces=False,
                flver0_vertices=self.vertices,
            )

        self._draw(
            triangulate,
            vertex_color, show_normals, show_origin, (0,) if show_face_set else (),
            auto_show, axes, random_face_colors, **kwargs,
        )

    def draw_flver2(
        self,
        vertex_color="red",
        show_normals=True,
        show_origin=False,
        show_face_sets=(),
        auto_show=False,
        axes=None,
        random_face_colors=False,
        **kwargs,
    ):
        def triangulate(face_set: FaceSet):
            return face_set.triangulate(uses_0xffff_separators=len(self.vertices) <= 0xFFFF)

        self._draw(
            triangulate,
            vertex_color, show_normals, show_face_sets, show_origin, auto_show, axes, random_face_colors, **kwargs,
        )

    def _draw(
        self,
        triangulate_func: tp.Callable[[FaceSet], np.ndarray],
        vertex_color="red",
        show_normals=True,
        show_origin=False,
        show_face_sets=(),
        auto_show=False,
        axes=None,
        random_face_colors=False,
        **kwargs,
    ):
        import matplotlib.pyplot as plt
        if axes is None:
            axes = plt.figure().add_subplot(111, projection="3d")
        array = self.vertex_arrays[0]
        positions = array["position"]
        axes.scatter(*zip(*positions), c=vertex_color, s=1, alpha=0.1)  # note y/z swapped
        if show_normals:
            normals = array["normal"]
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
                    faces += [tri for tri in triangulate_func(face_set)]
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
        material = indent_lines(repr(self.material))
        lines = [
            "FLVERMesh(",
            f"  material = {material}",
            f"  default_bone_index = {self.default_bone_index}",
            f"  bone_indices = {self.bone_indices}",
            f"  vertices = <{len(self.vertices)} vertices>",
        ]
        if not self.is_bind_pose:
            lines.append("  is_bind_pose = False")
        if self.uses_bounding_boxes:
            lines.append(f"  bounding_box_min = {self.bounding_box_min}")
            lines.append(f"  bounding_box_max = {self.bounding_box_max}")
            if self.bounding_box_unknown is not None:
                lines.append(f"  bounding_box_unknown = {self.bounding_box_unknown}")
        lines.append(f"  face_sets = [\n{face_sets}\n  ]")
        lines.append(")")

        return "\n".join(lines)

    # endregion
