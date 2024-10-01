from __future__ import annotations

__all__ = ["FLVER"]

import logging
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.misc import IDList
from soulstruct.base.models.base.core import BaseFLVER
from soulstruct.base.models.base.bone import FLVERBone
from soulstruct.base.models.base.dummy import Dummy
from soulstruct.base.models.base.face_set import FaceSet
from soulstruct.base.models.base.version import FLVERVersion
from .layout_repair import check_ds1_layouts
from .gx_item import GXItem
from .material import Material
from .mesh_tools import MergedMesh
from .submesh import Submesh
from .texture import Texture
from .vertex_array import VertexArrayHeaderStruct, VertexArray, VertexDataSizeError
from .vertex_array_layout import VertexArrayLayout

_LOGGER = logging.getLogger("soulstruct")


# noinspection PyDataclass
@dataclass(slots=True, repr=False)
class FLVER(BaseFLVER[Submesh]):
    """Model format used since Dark Souls PTDE.

    Technically, this format is FLVER2. Demon's Souls used an older version, `FLVER0`, which is not supported here. This
    class supports ALL games from Dark Souls to Elden Ring; minor format differences are handled internally.

    Order of packed binary FLVER information, for reference:
        - FLVER header
        - Material headers
        - Bone headers
        - Submesh headers
        - Submesh face set headers
        - Submesh vertex array headers
        - Vertex array layout headers
        - Array layout types
        - Submesh bounding boxes
        - Submesh bone indices
        - Submesh face set indices
        - Submesh vertex array indices
        - GX item lists
        - Material and texture strings
        - Bone names
        - Vertex data
    """

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):
        _file_type: bytes = field(init=False, **BinaryString(6, asserted=b"FLVER"))
        endian: bytes = field(**BinaryString(2, asserted=[b"L\0", b"B\0"]))
        version: FLVERVersion = field(**Binary(int))
        vertex_data_offset: int
        vertex_data_size: int
        dummy_count: int
        material_count: int
        bone_count: int
        mesh_count: int
        vertex_array_count: int
        bounding_box_min: Vector3
        bounding_box_max: Vector3
        true_face_count: int
        total_face_count: int
        face_set_vertex_index_bit_size: byte = field(**Binary(asserted=[0, 8, 16, 32]))
        unicode: bool
        unk_x4a: bool
        _pad1: bytes = field(init=False, **BinaryPad(1))
        unk_x4c: int
        face_set_count: int
        array_layout_count: int
        texture_count: int
        unk_x5c: byte
        unk_x5d: byte
        _pad2: bytes = field(init=False, **BinaryPad(10))
        unk_x68: int
        _pad3: bytes = field(init=False, **BinaryPad(20))

    unk_x4a: bool = False
    unk_x4c: int = 0
    unk_x5c: int = 0
    unk_x5d: int = 0
    unk_x68: int = 0

    submeshes: list[Submesh] = field(default_factory=list)  # override

    # NOTE: `Material` instances are assigned to their submeshes and are not stored separately in the FLVER.
    # On export, all unique materials are packed to the FLVER, and each submesh is assigned an index to one of them.
    
    # NOTE: `GXItem` lists are assigned to the `Material` instances that use them. They are not stored separately in the
    # FLVER. On export, all unique `GXItem` lists are packed to the FLVER, and each `Material` is assigned the offset
    # of its `GXItem` list in the FLVER.

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        byte_order = ByteOrder.from_reader_peek(reader, 2, 6, b"B\0", b"L\0")
        reader.default_byte_order = byte_order  # applies to all FLVER structs (manually passed to `VertexArray`)
        header = cls.STRUCT.from_bytes(reader)

        if header.version < 0x20000:
            raise ValueError(f"`FLVER` version {header.version} is not supported. Must be >= 0x20000.")

        encoding = "utf-16-le" if header.unicode else "shift_jis_2004"
        uv_factor = 2048 if header.version >= FLVERVersion.DarkSouls2_NT else 1024

        dummies = [Dummy.from_flver_reader(reader, header.version) for _ in range(header.dummy_count)]

        gx_item_lists = {}  # type: dict[int, list[GXItem]]  # unpacked by each `Material` as encountered
        materials = [
            Material.from_flver_reader(
                reader,
                encoding=encoding,
                version=header.version,
                gx_item_lists=gx_item_lists,
            )
            for _ in range(header.material_count)
        ]

        bones = IDList()  # type: IDList[FLVERBone]
        for _ in range(header.bone_count):
            bone = FLVERBone.from_flver_reader(reader, encoding=encoding)
            bones.append(bone)
        for bone in bones:
            bone.set_bones(bones)

        submeshes = [
            Submesh.from_flver_reader(
                reader,
                materials,
                bounding_box_has_unknown=header.version == FLVERVersion.Sekiro_EldenRing,
                index=i,
            )
            for i in range(header.mesh_count)
        ]

        face_sets = {
            i: FaceSet.from_flver_reader(
                reader,
                header_vertex_index_bit_size=header.face_set_vertex_index_bit_size,
                vertex_data_offset=header.vertex_data_offset,
            )
            for i in range(header.face_set_count)
        }

        # Buffer structs come before layouts. We load just the structs first, then combine them with their indexed
        # layout to unpack the vertex array data, which is assigned to submeshes below.
        array_headers = [VertexArrayHeaderStruct.from_bytes(reader) for _ in range(header.vertex_array_count)]

        layouts = [VertexArrayLayout.from_flver_reader(reader) for _ in range(header.array_layout_count)]
        if header.version == FLVERVersion.DarkSouls_A:
            # Check for botched DS1R array layouts (thanks QLOC!).
            # TODO: At least one DS1R map piece, m0302B0A14, has the correct layout but its data is messed up: there are
            #  16 null bytes at the start of the array (causing the last 16 actual data bytes to be truncated at EOF)
            #  and the Y and Z vertex coordinates are corrupted (appears lossy). Not sure how to handle this beyond a
            #  hard-coded list of DS1R map pieces to fix/warn (currently done in `vertex_array.py` module).
            check_ds1_layouts(layouts, array_headers, submeshes)

        # Load NumPy array wrappers with attached layouts.
        # Uses a dictionary so they can easily be dereferenced to Submeshes.
        vertex_arrays = {}
        for i, array_header in enumerate(array_headers):
            try:
                vertex_array = VertexArray.from_flver_reader(
                    reader, array_header, layouts, header.vertex_data_offset, uv_factor
                )
            except VertexDataSizeError:
                vertex_array = VertexArray(array=np.empty(0), layout=layouts[array_header.layout_index])
            vertex_arrays[i] = vertex_array

        textures = {i: Texture.from_flver_reader(reader, encoding=encoding) for i in range(header.texture_count)}

        # TODO: Sekiro has an additional unknown structure here.

        for material in materials:
            # Each texture is only assigned to ONE material. Texture is popped from `textures` after first assignment.
            material.assign_textures(textures)
        if textures:
            raise ValueError(f"{len(textures)} textures were left over after assignment to materials.")

        for i, submesh in enumerate(submeshes):
            submesh.index = i
            submesh.dereference_face_sets(face_sets)
            submesh.dereference_vertex_arrays(vertex_arrays)
            submesh.validate_unique_data_types()

        if face_sets:
            raise ValueError(f"{len(face_sets)} face sets were left over after assignment to submeshes.")
        if vertex_arrays:
            raise ValueError(f"{len(vertex_arrays)} vertex arrays were left over after assignment to submeshes.")

        return header.to_object(
            cls,
            big_endian=header.endian == b"B\0",
            dummies=dummies,
            bones=bones,
            submeshes=submeshes,
        )

    @classmethod
    def from_path(cls, path: str | Path) -> tp.Self:
        """Reports invalid array layouts."""
        flver = super(FLVER, cls).from_path(path)
        assert isinstance(flver, FLVER)
        if any(mesh.invalid_layout for mesh in flver.submeshes):
            _LOGGER.warning(f"FLVER '{Path(path).name}' has one or more submeshes with invalid vertex array sizes.")
        return flver

    def to_writer(self) -> BinaryWriter:

        byte_order = ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian
        encoding = byte_order.get_utf_16_encoding() if self.unicode else "shift_jis_2004"

        true_face_count = 0
        total_face_count = 0
        for submesh in self.submeshes:
            uses_0xffff_separators = len(submesh.vertices) <= 0xFFFF  # max unsigned short value
            for face_set in submesh.face_sets:
                face_set_true_count, face_set_total_count = face_set.get_face_counts(uses_0xffff_separators)
                true_face_count += face_set_true_count
                total_face_count += face_set_total_count

        if self.version >= FLVERVersion.Bloodborne_DS3_A:
            # FLVERs from Bloodborne onward: vertex index size is stored per `FaceSet`.
            header_face_set_vertex_index_bit_size = 0
        else:
            # All `FaceSet`s use the same vertex index size, specified in the FLVER header. We check if all face sets in
            # this FLVER support 16-bit indices. If not, we use 32-bit indices for ALL of them.
            header_face_set_vertex_index_bit_size = 16
            for submesh in self.submeshes:
                for face_set in submesh.face_sets:
                    if face_set.needs_32bit_indices():
                        _LOGGER.info(f"FLVER '{self.path}' has a face set that requires global 32-bit vertex indices.")
                        header_face_set_vertex_index_bit_size = 32
                        break
                if header_face_set_vertex_index_bit_size == 32:
                    break

        header = self.STRUCT.from_object(
            self,
            byte_order=byte_order,
            endian=b"B" if self.big_endian else b"L",
            vertex_data_offset=RESERVED,
            vertex_data_size=RESERVED,
            dummy_count=len(self.dummies),
            material_count=RESERVED,
            bone_count=len(self.bones),
            mesh_count=len(self.submeshes),
            vertex_array_count=sum(len(mesh.vertex_arrays) for mesh in self.submeshes),
            true_face_count=true_face_count,
            total_face_count=total_face_count,
            face_set_vertex_index_bit_size=header_face_set_vertex_index_bit_size,  # 0, 16, or 32
            face_set_count=sum(len(mesh.face_sets) for mesh in self.submeshes),
            array_layout_count=RESERVED,
            texture_count=RESERVED,
        )

        writer = header.to_writer(reserve_obj=self)

        for dummy in self.dummies:
            dummy.to_flver_writer(writer, self.version)

        materials_to_pack = []  # type: list[Material]  # unique materials to actually pack to FLVER
        layouts_to_pack = []  # type: list[VertexArrayLayout]  # unique layouts to actually pack to FLVER
        gx_lists_to_pack = []  # type: list[list[GXItem]]  # unique GX item lists to actually pack to FLVER
        hashed_material_indices = {}  # type: dict[int, int]  # maps material hashes to `materials_to_pack` indices
        hashed_layout_indices = {}  # type: dict[int, int]  # maps layout hashes to `layouts_to_pack` indices
        hashed_gx_list_indices = {}  # type: dict[int, int]  # maps GX list hashes to `gx_lists_to_pack` indices
        submesh_material_indices = []  # type: list[int]
        submesh_layout_indices = []  # type: list[list[int]]  # has a list per submesh (may have multiple arrays)
        gx_list_material_users = []  # type: list[list[Material]]  # maps `gx_lists_to_pack` element to `Material` list
        for submesh in self.submeshes:
            material = submesh.material
            material_hash = hash(material)  # includes name!
            if material_hash in hashed_material_indices:
                submesh_material_index = hashed_material_indices[material_hash]
            else:
                # New material.
                submesh_material_index = hashed_material_indices[material_hash] = len(materials_to_pack)
                materials_to_pack.append(material)
                # Check GX item list.
                if material.gx_items:
                    gx_items_hash = hash(tuple(material.gx_items))
                    if gx_items_hash in hashed_gx_list_indices:
                        # GX item list with identical hash is already registered for packing.
                        material_gx_list_index = hashed_gx_list_indices[gx_items_hash]
                        gx_list_material_users[material_gx_list_index].append(material)
                    else:
                        # New GX item list.
                        material_gx_list_index = len(gx_lists_to_pack)
                        hashed_gx_list_indices[gx_items_hash] = material_gx_list_index
                        gx_lists_to_pack.append(material.gx_items)
                        gx_list_material_users.append([material])
            submesh_material_indices.append(submesh_material_index)

            array_layout_indices = []
            for vertex_array in submesh.vertex_arrays:
                layout = vertex_array.layout
                layout_hash = hash(layout)
                if layout_hash in hashed_layout_indices:
                    array_layout_index = hashed_layout_indices[layout_hash]
                else:
                    # New layout.
                    array_layout_index = hashed_layout_indices[layout_hash] = len(layouts_to_pack)
                    layouts_to_pack.append(layout)
                array_layout_indices.append(array_layout_index)
            submesh_layout_indices.append(array_layout_indices)

        writer.fill("material_count", len(materials_to_pack), obj=self)
        writer.fill("array_layout_count", len(layouts_to_pack), obj=self)
        writer.fill("texture_count", sum(len(material.textures) for material in materials_to_pack), obj=self)

        # Pack materials.
        for material in materials_to_pack:
            material.to_flver_writer(writer)

        # Pack bones.
        for bone in self.bones:
            bone.set_bone_indices(self.bones)
            bone.to_flver_writer(writer, self.bones)

        # Pack submesh headers.
        for submesh, material_index in zip(self.submeshes, submesh_material_indices):
            submesh.to_flver_writer(writer, material_index)

        # Pack submesh face sets.
        face_set_index_sizes = []
        for submesh in self.submeshes:
            for face_set in submesh.face_sets:
                if header_face_set_vertex_index_bit_size != 0:
                    # Vertex size set globally in FLVER header, depending on largest face set (older FLVERs).
                    # No value is written to each Face Set.
                    face_set_vertex_index_bit_size = header_face_set_vertex_index_bit_size
                    write_index_size = False
                else:
                    # Vertex size set per `FaceSet`. These sizes are stored for packing below.
                    face_set_vertex_index_bit_size = 32 if face_set.needs_32bit_indices() else 16
                    write_index_size = True
                face_set_index_sizes.append(face_set_vertex_index_bit_size)  # to save time below
                face_set.to_flver_writer(writer, face_set_vertex_index_bit_size, write_index_size)

        # Pack submesh vertex array headers.
        for submesh, layout_indices in zip(self.submeshes, submesh_layout_indices):
            for i, (vertex_array, layout_index) in enumerate(zip(submesh.vertex_arrays, layout_indices)):
                vertex_array.to_flver_writer(
                    writer,
                    write_array_length=self.version >= 0x20005,
                    layout_index=layout_index,
                    array_index=i,
                )

        # Pack array layouts.
        for layout in layouts_to_pack:
            layout.to_flver_writer(writer)

        # Pack material textures.
        first_texture_index = 0
        for material in materials_to_pack:
            material.pack_textures(writer, first_texture_index=first_texture_index)
            first_texture_index += len(material.textures)

        # TODO: Write unknown Sekiro struct here.

        # Indexed data only after this point, aligning to 16 bytes between each data type.

        writer.pad_align(16)
        for layout in layouts_to_pack:
            layout.pack_layout_types(writer)

        writer.pad_align(16)
        for submesh in self.submeshes:
            submesh.pack_bounding_box(writer)

        writer.pad_align(16)
        bone_indices_start = writer.position
        for submesh in self.submeshes:
            submesh.pack_bone_indices(writer, bone_indices_start=bone_indices_start)

        writer.pad_align(16)
        first_face_set_index = 0
        for submesh in self.submeshes:
            submesh.pack_face_set_indices(writer, first_face_set_index)
            first_face_set_index += len(submesh.face_sets)

        writer.pad_align(16)
        first_vertex_array_index = 0
        for submesh in self.submeshes:
            submesh.pack_vertex_array_indices(writer, first_vertex_array_index)
            first_vertex_array_index += len(submesh.vertex_arrays)

        # Pack GX lists (only unique ones).
        writer.pad_align(16)
        for gx_list, material_users in zip(gx_lists_to_pack, gx_list_material_users):
            gx_list_offset = writer.position
            for gx_item in gx_list:
                gx_item.to_writer(writer)
            if not gx_list[-1].is_dummy:  # list cannot be empty here
                _LOGGER.warning("Final `GXItem` in list is not a dummy item. Appending new dummy item.")
                dummy_gx_item = GXItem.new_dummy()
                dummy_gx_item.to_writer(writer)
            for material in material_users:
                # NOTE: Material only reserves this field if it has any GX items. Otherwise, already wrote offset -1.
                material.fill_gx_offset(writer, gx_list_offset)

        # Pack materials and texture strings.
        writer.pad_align(16)
        for material in materials_to_pack:
            material.pack_strings(writer, encoding)
            for texture in material.textures:
                texture.pack_strings(writer, encoding=encoding)

        # Pack bone names.
        writer.pad_align(16)
        for bone in self.bones:
            bone.pack_name(writer, encoding=encoding)

        # Version-specific alignment/padding.
        alignment = 32 if self.version <= 0x2000E else 16
        writer.pad_align(alignment)
        if self.version in {FLVERVersion.DarkSouls2_NT, FLVERVersion.DarkSouls2}:
            writer.pad(32)

        vertex_data_start = writer.position
        writer.fill("vertex_data_offset", vertex_data_start, obj=self)

        face_set_index = 0
        uv_factor = 2048 if self.version >= FLVERVersion.DarkSouls2_NT else 1024
        for submesh in self.submeshes:
            for face_set in submesh.face_sets:
                writer.pad_align(16)
                face_set.pack_vertex_indices(
                    writer,
                    vertex_index_bit_size=face_set_index_sizes[face_set_index],
                    vertex_indices_offset=writer.position - vertex_data_start,
                )
                face_set_index += 1

            for vertex_array in submesh.vertex_arrays:
                writer.pad_align(16)
                vertex_array.pack_array(
                    writer,
                    array_offset=writer.position - vertex_data_start,
                    uv_factor=uv_factor,
                )

        writer.pad_align(16)
        writer.fill("vertex_data_size", writer.position - vertex_data_start, obj=self)
        if self.version in {FLVERVersion.DarkSouls2_NT, FLVERVersion.DarkSouls2}:
            writer.pad(32)

        return writer

    def to_merged_mesh(
        self,
        submesh_material_indices: tp.Sequence[int] = None,
        material_uv_layer_names: tp.Sequence[tp.Sequence[str]] = None,
        merge_vertices=True,
    ) -> MergedMesh:
        """Return a `BaseMergedMesh` object that combines all submeshes of this FLVER into a single mesh."""
        return MergedMesh.from_flver(self, submesh_material_indices, material_uv_layer_names, merge_vertices)

    def guess_rigged(self) -> bool:
        """Override condition: if no submesh has `is_bind_pose == True`, we also infer unrigged.

        We can't rely on the presence of 'bone_weights' in later games due to more complicated shaders.
        """
        return any(submesh.is_bind_pose for submesh in self.submeshes)
