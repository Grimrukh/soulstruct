from __future__ import annotations

__all__ = ["FLVER"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.containers import Binder, TPF
from soulstruct.utilities.maths import Vector3, Vector4, Matrix3, SINGLE_MIN, SINGLE_MAX
from soulstruct.utilities.binary import *

from .bone import FLVERBone
from .dummy import Dummy
from .layout_repair import check_ds1_layouts
from .material import GXList, Material, Texture
from .mesh import FaceSet, Mesh
from .version import Version
from .vertex import BufferLayout, VertexBuffer, VertexBufferSizeError

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class FLVERStruct(BinaryStruct):
    _file_type: bytes = field(init=False, **BinaryString(6, asserted=b"FLVER"))
    endian: bytes = field(**BinaryString(2, asserted=[b"L\0", b"R\0"]))
    version: Version = field(**Binary(int))
    vertex_data_offset: int
    vertex_data_size: int
    dummy_count: int
    material_count: int
    bone_count: int
    mesh_count: int
    vertex_buffer_count: int
    bounding_box_min: Vector3
    bounding_box_max: Vector3
    true_face_count: int
    total_face_count: int
    vertex_indices_size: byte = field(**Binary(asserted=[0, 8, 16, 32]))
    unicode: bool
    unk_x4a: bool
    _pad1: bytes = field(init=False, **BinaryPad(1))
    unk_x4c: int
    face_set_count: int
    buffer_layout_count: int
    texture_count: int
    unk_x5c: byte
    unk_x5d: byte
    _pad2: bytes = field(init=False, **BinaryPad(10))
    unk_x68: int
    _pad3: bytes = field(init=False, **BinaryPad(20))


# noinspection PyDataclass
@dataclass(slots=True)
class FLVER(GameFile):
    """Model format used since Dark Souls PTDE.

    Technically, this format is FLVER2. Demon's Souls used an older version, `FLVER0`, which is not supported here.
    """

    # Convenience access to classes.
    Bone: tp.ClassVar = FLVERBone
    Dummy: tp.ClassVar = Dummy
    GXList: tp.ClassVar = GXList
    Material: tp.ClassVar = Material
    Mesh: tp.ClassVar = Mesh
    BufferLayout: tp.ClassVar = BufferLayout
    VertexBuffer: tp.ClassVar = VertexBuffer

    EXT: tp.ClassVar = ".flver"

    # Header information that can't be inferred, and must be stored from unpack or manually set. They default to DSR.
    # (These fields have no underscore prefix in `FLVERStruct` and will be passed here automatically.)
    big_endian: bool = False
    version: Version = Version.DarkSouls_A
    bounding_box_min: Vector3 = field(default_factory=Vector3.zero)
    bounding_box_max: Vector3 = field(default_factory=Vector3.zero)
    vertex_indices_size: int = 16
    unicode: bool = True
    unk_x4a: bool = False
    unk_x4c: int = 0
    unk_x5c: int = 0
    unk_x5d: int = 0
    unk_x68: int = 0

    dummies: list[Dummy] = field(default_factory=list)
    gx_lists: list[GXList] = field(default_factory=list)
    materials: list[Material] = field(default_factory=list)
    bones: list[Bone] = field(default_factory=list)
    meshes: list[Mesh] = field(default_factory=list)
    buffer_layouts: list[BufferLayout] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader):
        byte_order = ByteOrder.from_reader_peek(reader, 2, 6, b"R\0", b"L\0")
        reader.default_byte_order = byte_order  # applies to all FLVER structs
        header = FLVERStruct.from_bytes(reader)

        encoding = "utf-16-le" if header.unicode else "shift_jis_2004"

        dummies = [Dummy.from_flver_reader(reader, header.version) for _ in range(header.dummy_count)]

        gx_list_indices = {}  # type: dict[int, int]  # maps `_gx_offset` in `Material` to `self.gx_lists` index
        gx_lists = []
        materials = [
            Material.from_flver_reader(
                reader,
                encoding=encoding,
                version=header.version,
                gx_lists=gx_lists,
                gx_list_indices=gx_list_indices,
            )
            for _ in range(header.material_count)
        ]

        bones = [FLVERBone.from_flver_reader(reader, encoding=encoding) for _ in range(header.bone_count)]

        meshes = [
            Mesh.from_flver_reader(reader, bounding_box_has_unknown=header.version == Version.Sekiro)
            for _ in range(header.mesh_count)
        ]

        face_sets = {
            i: FaceSet.from_flver_reader(
                reader,
                header_vertex_index_size=header.vertex_indices_size,
                vertex_data_offset=header.vertex_data_offset,
            )
            for i in range(header.face_set_count)
        }

        vertex_buffers = {i: VertexBuffer.from_flver_reader(reader) for i in range(header.vertex_buffer_count)}

        buffer_layouts = [BufferLayout.from_flver_reader(reader) for _ in range(header.buffer_layout_count)]

        if header.version == Version.DarkSouls_A:
            # Check for botched DS1R buffer layouts (thanks QLOC!).
            check_ds1_layouts(buffer_layouts, vertex_buffers, meshes, materials)

        textures = {i: Texture.from_flver_reader(reader, encoding=encoding) for i in range(header.texture_count)}

        # TODO: Sekiro has an additional unknown structure here.

        for material in materials:
            # Each texture is only assigned to ONE material. Texture is popped from `textures` after first assignment.
            material.assign_textures(textures)
        if textures:
            raise ValueError(f"{len(textures)} textures were left over after assignment to materials.")

        for i, mesh in enumerate(meshes):
            mesh.assign_face_sets(face_sets)
            mesh.assign_vertex_buffers(vertex_buffers, buffer_layouts)
            uv_factor = 2048 if header.version >= Version.DarkSouls2_NT else 1024

            try:
                mesh.read_vertices(reader, header.vertex_data_offset, buffer_layouts, uv_factor)
            except VertexBufferSizeError as ex:
                _LOGGER.warning(
                    f"Mesh {i} in FLVER has an invalid vertex buffer size ({ex.vertex_size} rather than layout size "
                    f"{ex.layout_size}). Mesh marked with `invalid_vertex_size=True`; handle this as needed."
                )
                mesh.invalid_vertex_size = True
        if face_sets:
            raise ValueError(f"{len(face_sets)} face sets were left over after assignment to meshes.")
        if vertex_buffers:
            raise ValueError(f"{len(vertex_buffers)} vertex buffers were left over after assignment to meshes.")

        return header.to_object(
            cls,
            big_endian=header.endian == b"B\0",
            dummies=dummies,
            gx_lists=gx_lists,
            materials=materials,
            bones=bones,
            meshes=meshes,
            buffer_layouts=buffer_layouts,
        )

    @classmethod
    def from_chrbnd(cls, chrbnd: Binder) -> FLVER:
        """Open CHRBND from given `chrbnd_source` and load its `.flver` file (with or without DCX extension).

        Will raise an exception if no FLVER files or multiple FLVER files exist in the BND.
        """
        flver_entry = chrbnd.find_entry_matching_name(r".*\.flver(\.dcx)?$")
        return cls.from_bytes(flver_entry)

    def to_writer(self) -> BinaryWriter:

        byte_order = ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian
        encoding = byte_order.get_utf_16_encoding() if self.unicode else "shift_jis_2004"

        true_face_count = 0
        total_face_count = 0
        for mesh in self.meshes:
            allow_primitive_restarts = len(mesh.vertices) < 2 ** 16 - 1  # max unsigned short value
            for face_set in mesh.face_sets:
                face_set_true_count, face_set_total_count = face_set.get_face_counts(allow_primitive_restarts)
                true_face_count += face_set_true_count
                total_face_count += face_set_total_count

        if self.version < Version.Bloodborne_DS3_A:
            # Set header's `vertex_index_size` to the largest size detected across all `FaceSet`s (16 or 32).
            header_vertex_indices_size = 16
            for mesh in self.meshes:
                for face_set in mesh.face_sets:
                    face_set_vertex_index_size = face_set.get_vertex_index_size()
                    header_vertex_indices_size = max(header_vertex_indices_size, face_set_vertex_index_size)
        else:
            # Vertex size is stored per `VertexBuffer`.
            header_vertex_indices_size = 0

        header = FLVERStruct.from_object(
            self,
            byte_order=byte_order,
            endian=b"B" if self.big_endian else b"L",
            vertex_data_offset=RESERVED,
            vertex_data_size=RESERVED,
            dummy_count=len(self.dummies),
            material_count=len(self.materials),
            bone_count=len(self.bones),
            mesh_count=len(self.meshes),
            vertex_buffer_count=sum(len(mesh.vertex_buffers) for mesh in self.meshes),
            true_face_count=true_face_count,
            total_face_count=total_face_count,
            vertex_indices_size=header_vertex_indices_size,
            face_set_count=sum(len(mesh.face_sets) for mesh in self.meshes),
            buffer_layout_count=len(self.buffer_layouts),
            texture_count=sum(len(material.textures) for material in self.materials),
        )

        writer = header.to_writer(reserve_obj=self)

        for dummy in self.dummies:
            dummy.to_flver_writer(writer, self.version)

        for material in self.materials:
            material.to_flver_writer(writer)

        for bone in self.bones:
            bone.to_flver_writer(writer)

        for mesh in self.meshes:
            mesh.to_flver_writer(writer)

        for mesh in self.meshes:
            for face_set in mesh.face_sets:
                if header_vertex_indices_size == 0:
                    face_set_vertex_index_size = face_set.get_vertex_index_size()
                else:
                    face_set_vertex_index_size = header_vertex_indices_size
                face_set.to_flver_writer(writer, face_set_vertex_index_size)

        for mesh in self.meshes:
            for i, vertex_buffer in enumerate(mesh.vertex_buffers):
                vertex_buffer.to_flver_writer(
                    writer,
                    self.version,
                    mesh_vertex_buffer_index=i,
                    buffer_layouts=self.buffer_layouts,
                    mesh_vertex_count=len(mesh.vertices),
                )

        for i, buffer_layout in enumerate(self.buffer_layouts):
            buffer_layout.to_flver_writer(writer)

        first_texture_index = 0
        for i, material in enumerate(self.materials):
            material.pack_textures(writer, first_texture_index=first_texture_index)
            first_texture_index += len(material.textures)

        # TODO: Write unknown Sekiro struct here.

        # Indexed data only after this point, with 16 pad bytes between each data type.

        writer.pad_align(16)
        for i, buffer_layout in enumerate(self.buffer_layouts):
            buffer_layout.pack_members(writer)

        writer.pad_align(16)
        for i, mesh in enumerate(self.meshes):
            mesh.pack_bounding_box(writer)

        writer.pad_align(16)
        bone_indices_start = writer.position
        for i, mesh in enumerate(self.meshes):
            mesh.pack_bone_indices(writer, bone_indices_start=bone_indices_start)

        writer.pad_align(16)
        first_face_set_index = 0
        for i, mesh in enumerate(self.meshes):
            mesh.pack_face_set_indices(writer, first_face_set_index)
            first_face_set_index += len(mesh.face_sets)

        writer.pad_align(16)
        first_vertex_buffer_index = 0
        for mesh in self.meshes:
            mesh.pack_vertex_buffer_indices(writer, first_vertex_buffer_index)
            first_vertex_buffer_index += len(mesh.vertex_buffers)

        writer.pad_align(16)
        gx_offsets = []
        for gx_list in self.gx_lists:
            gx_offsets.append(writer.position)
            gx_list.to_flver_writer(writer)
        for material in self.materials:
            material.fill_gx_offset(writer, gx_offsets)

        writer.pad_align(16)
        for material in self.materials:
            material.pack_strings(writer, encoding)
            for texture in material.textures:
                texture.pack_strings(writer, encoding=encoding)

        writer.pad_align(16)
        for bone in self.bones:
            bone.pack_name(writer, encoding=encoding)

        alignment = 32 if self.version <= 0x2000E else 16
        writer.pad_align(alignment)
        if self.version in {Version.DarkSouls2_NT, Version.DarkSouls2}:
            writer.pad(32)

        vertex_data_start = writer.position
        writer.fill("vertex_data_offset", vertex_data_start, obj=self)

        for i, mesh in enumerate(self.meshes):
            for face_set in mesh.face_sets:
                if header_vertex_indices_size == 0:
                    face_set_vertex_index_size = face_set.get_vertex_index_size()
                else:
                    face_set_vertex_index_size = header_vertex_indices_size
                writer.pad_align(16)
                face_set.pack_vertex_indices(
                    writer,
                    vertex_index_size=face_set_vertex_index_size,
                    vertex_indices_offset=writer.position - vertex_data_start,
                )

            for vertex_buffer, vertex_array in zip(mesh.vertex_buffers, mesh.vertex_arrays):
                writer.pad_align(16)
                uv_factor = 2048 if self.version >= Version.DarkSouls2_NT else 1024
                vertex_buffer.pack_buffer(
                    writer,
                    buffer_layouts=self.buffer_layouts,
                    vertex_array=vertex_array,
                    buffer_offset=writer.position - vertex_data_start,
                    uv_factor=uv_factor,
                )

        writer.pad_align(16)
        writer.fill("vertex_data_size", writer.position - vertex_data_start, obj=self)
        if self.version in {Version.DarkSouls2_NT, Version.DarkSouls2}:
            writer.pad(32)

        return writer

    def to_obj(self, name="FLVER", meshes=()) -> str:
        if isinstance(meshes, int):
            meshes = [meshes]
        vertex_offset = 0
        mesh_objs = []
        for i, mesh in enumerate(self.meshes):
            if meshes and i not in meshes:
                continue  # skip this mesh
            mesh_objs.append(mesh.to_obj(name=f"{name} Mesh {i}", vertex_offset=vertex_offset))
            vertex_offset += len(mesh.vertices)
        return "\n\n".join(mesh_objs)

    def write_obj(self, obj_path: Path | str = None, obj_name="", make_dirs=True, meshes=()):
        if obj_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            obj_path = self.path
            if obj_path.suffix == ".dcx":
                obj_path = obj_path.with_name(obj_path.stem)
            obj_path = obj_path.with_suffix(".obj")
        else:
            obj_path = Path(obj_path)
            if obj_path.suffix != ".obj":
                obj_path = obj_path.with_suffix(".obj")
        if make_dirs:
            obj_path.parent.mkdir(parents=True, exist_ok=True)
        if not obj_name:
            obj_name = obj_path.stem
        obj_str = self.to_obj(name=obj_name, meshes=meshes)
        with obj_path.open("w") as f:
            f.write(obj_str)

    def to_string(self) -> str:
        if self.bones:
            bones = "[\n    " + "\n    ".join(repr(self.bones)[1:-1].split("\n")) + "\n  ]"
        else:
            bones = "[]"
        if self.dummies:
            dummies = "[\n    " + "\n    ".join(repr(self.dummies)[1:-1].split("\n")) + "\n  ]"
        else:
            dummies = "[]"
        if self.materials:
            materials = "[\n    " + "\n    ".join(repr(self.materials)[1:-1].split("\n")) + "\n  ]"
        else:
            materials = "[]"
        if self.gx_lists:
            gx_lists = "[\n    " + "\n    ".join(repr(self.gx_lists)[1:-1].split("\n")) + "\n  ]"
        else:
            gx_lists = "[]"
        if self.meshes:
            meshes = "[\n    " + "\n    ".join(repr(self.meshes)[1:-1].split("\n")) + "\n  ]"
        else:
            meshes = "[]"
        return (
            f"FLVER(\n"
            f"  bones = {bones}\n"
            f"  dummies = {dummies}\n"
            f"  materials = {materials}\n"
            f"  gx_lists = {gx_lists}\n"
            f"  meshes = {meshes}\n"
            ")"
        )

    def draw(self, auto_show=False, show_mesh_face_sets=(), show_origin=False, axes=None, **kwargs):
        import matplotlib.pyplot as plt
        if show_mesh_face_sets == "all":
            show_mesh_face_sets = tuple(range(len(self.meshes)))
        if axes is None:
            axes = plt.figure().add_subplot(111, projection="3d")
        for i, mesh in enumerate(self.meshes):
            mesh.draw(
                show_origin=show_origin and mesh is self.meshes[-1],
                show_face_sets=show_mesh_face_sets,
                auto_show=False,
                axes=axes,
                **kwargs,
            )
        for bone in self.bones:
            bone_position = bone.get_armature_space_transform(self.bones)[0]
            axes.scatter(*bone_position.to_xzy(), color="blue", s=10)
        if auto_show:
            plt.show()

    def scale_all_translations(self, scale_factor: float | Vector3 | Vector4):
        """Modifies the FLVER in place by scaling all dummies, bones, and vertices by `factor`.

        Will NOT have full functionality in-game until Havok physics files are modified as well.
        """
        if isinstance(scale_factor, Vector4):
            scale_factor = Vector3((scale_factor.x, scale_factor.y, scale_factor.z))
        for dummy in self.dummies:
            dummy.translate *= scale_factor
        for bone in self.bones:
            bone.translate *= scale_factor
        for mesh in self.meshes:
            for vertex in mesh.vertices:
                # Vertex positions are just lists, not Vectors, and we want to keep them that way.
                if isinstance(scale_factor, Vector3):
                    vertex.position = [scale_factor[i] * vertex.position[i] for i in range(3)]
                else:
                    vertex.position = [scale_factor * vertex.position[i] for i in range(3)]

    # region Materials/Textures

    def replace_tpf_name(self, old_name: str, new_name: str):
        """Iterate over all `Material` textures and replace all '{old_name}.tga' names with '{new_name}.tga'."""
        for material in self.materials:
            for texture in material.textures:
                # TODO: To be safe, probably make sure we're only replacing the file name of the path.
                texture.path = texture.path.replace(old_name, new_name)

    def get_all_texture_paths(self) -> set[Path]:
        """Get set of all texture paths from all materials, which typically end in '.tga'.

        Ignores textures with empty `path`.
        """
        return {
            Path(texture.path)
            for material in self.materials
            for texture in material.textures if texture.path
        }

    def get_tpfbhd_directory_path(self) -> Path:
        """Looks for folder containing TPFBHD files adjacent to FLVER's directory.

        Only works for map pieces right now, and requires them to be loaded from their native location (e.g.
        `{data}/map/m10_00_00_00`).
        """
        if not self.path:
            raise ValueError(f"Cannot automatically find `tpfbhd` directory (FLVER path is unknown).")
        flver_parent = self.path.parent
        map_directory_match = re.match(r"^(m\d\d)_\d\d_\d\d_\d\d$", flver_parent.name)
        if not map_directory_match:
            raise ValueError(f"FLVER is not located in a map folder (`mAA_BB_CC_DD`).")
        tpfbhd_directory = flver_parent / f"../{map_directory_match.group(1)}"
        if not tpfbhd_directory.is_dir():
            raise FileNotFoundError(f"Required TPFBHD directory does not exist: {tpfbhd_directory}")
        return tpfbhd_directory

    def find_all_tpfs(self, tpfbhd_directory: None | str | Path = None) -> dict[Path, TPF]:
        if tpfbhd_directory is None:
            tpfbhd_directory = self.get_tpfbhd_directory_path()
        else:
            tpfbhd_directory = Path(tpfbhd_directory)
        tpf_paths = [(p, re.compile(rf"{p.stem}\.tpf(\.dcx)?$")) for p in self.get_all_texture_paths()]
        tpf_sources = {}
        for bhd_path in tpfbhd_directory.glob("*.tpfbhd"):
            bxf = Binder.from_path(bhd_path)
            for entry in bxf.entries:
                for tpf_path, tpf_re in reversed(tpf_paths):
                    if tpf_re.match(entry.name):
                        tpf_paths.remove((tpf_path, tpf_re))
                        tpf_sources[tpf_path] = TPF.from_bytes(entry.data)
                        break
                if not tpf_paths:
                    break
            if not tpf_paths:
                break
        return tpf_sources

    def get_mesh_material(self, mesh_or_index: Mesh | int) -> Material:
        if isinstance(mesh_or_index, int):
            if mesh_or_index >= len(self.meshes):
                raise ValueError(f"Invalid mesh index: {mesh_or_index} (only {len(self.meshes)} meshes in FLVER).")
            return self.materials[self.meshes[mesh_or_index].material_index]
        elif isinstance(mesh_or_index, Mesh):
            if mesh_or_index not in self.meshes:
                raise ValueError("Given mesh is not in this FLVER.")
            return self.materials[mesh_or_index.material_index]
        raise TypeError("Argument must be a `FLVER.Mesh` in this FLVER or a mesh index.")

    # endregion

    # region Bones

    def sort_mesh_bone_indices(self):
        """Sort all `mesh.bone_indices` in ascending order and update local bone indices of all vertices.

        Handles both standard bone weights (where a weight of -1.0 means no weight) and 'pose' bone weights, as is used
        by map pieces (all indices are the same, all weights are 0.0).

        TODO: Will likely become much more efficient when vertex data is kept in a NumPy array.
        """
        for mesh in self.meshes:
            if not mesh.bone_indices:
                continue  # this mesh/FLVER has global vertex bone indices
            old_mesh_indices = mesh.bone_indices.copy()
            mesh.bone_indices.sort()
            for vertex in mesh.vertices:
                # Check map piece 'pose' case, where all four weights are 0.0:
                if all(weight == 0.0 for weight in vertex.bone_weights):
                    bone_index = old_mesh_indices[vertex.bone_indices[0]]  # all four indices should be the same
                    vertex.bone_indices = [mesh.bone_indices.index(bone_index)] * 4  # new mesh bone index
                    continue

                # Standard case, where at least one bone weight is non-zero:
                for i in range(len(vertex.bone_indices)):
                    if vertex.bone_weights[i] == 0.0:
                        continue  # no bone index
                    bone_index = old_mesh_indices[vertex.bone_indices[i]]
                    vertex.bone_indices[i] = mesh.bone_indices.index(bone_index)  # new mesh bone index

    def refresh_bounding_boxes(
        self,
        refresh_bone_bounding_boxes=False,
        bone_bounding_boxes_in_armature_space=False,
    ):
        """Refresh global bounding box of FLVER from minimum and maximum of all mesh vertices.

        Can optionally refresh bone bounding boxes as well in the same vertex loop, rather than needing to call that
        method (below) separately and loop over all vertices again.
        """
        bone_local_vertex_x = {}  # type: dict[int, list[float]]
        bone_local_vertex_y = {}  # type: dict[int, list[float]]
        bone_local_vertex_z = {}  # type: dict[int, list[float]]
        if refresh_bone_bounding_boxes:
            # Create default (undefined) bounding boxes.
            bone_arma_translate_inv_rotates = [
                (transform[0], transform[1].inverse())
                for transform in self.get_bone_armature_space_transforms()
            ]
        else:
            bone_arma_translate_inv_rotates = []

        def add_bone_vertex(_v, _bone_index: int):
            # Unfortunately, we need to convert every vertex to the bone's space to compare it against the
            # current bounding box, because the bounding box is in bone space.
            arma_translate, inv_arma_rotate = bone_arma_translate_inv_rotates[_bone_index]
            if bone_bounding_boxes_in_armature_space:
                v_local = _v.position  # use armature space for bone bounding box min/max
            else:
                v_local = inv_arma_rotate @ Vector3(
                    (  # squeezing out whatever performance we can
                        _v.position[0] - arma_translate.x,
                        _v.position[1] - arma_translate.y,
                        _v.position[2] - arma_translate.z,
                    )
                )
            bone_local_vertex_x.setdefault(_bone_index, []).append(v_local[0])
            bone_local_vertex_y.setdefault(_bone_index, []).append(v_local[1])
            bone_local_vertex_z.setdefault(_bone_index, []).append(v_local[2])

        all_x = []
        all_y = []
        all_z = []
        for i, mesh in enumerate(self.meshes):
            for v in mesh.vertices:
                all_x.append(v.position[0])
                all_y.append(v.position[1])
                all_z.append(v.position[2])

                if not refresh_bone_bounding_boxes:
                    continue

                if all(weight == 0.0 for weight in v.bone_weights):
                    # Map piece 'pose' case, where all four weights are 0.0. All four bone indices are the same bone.
                    bone_index = mesh.bone_indices[v.bone_indices[0]]  # all four indices should be the same
                    add_bone_vertex(v, bone_index)

                for v_bone_index, bone_weight in zip(v.bone_indices, v.bone_weights):
                    if bone_weight == 0.0:
                        continue  # bone index is unused
                    bone_index = mesh.bone_indices[v_bone_index] if mesh.bone_indices else v_bone_index
                    add_bone_vertex(v, bone_index)

        if refresh_bone_bounding_boxes:
            for bone_index, bone in enumerate(self.bones):
                if bone_index in bone_local_vertex_x:
                    bone.bounding_box_min = Vector3((
                        min(bone_local_vertex_x[bone_index]),
                        min(bone_local_vertex_y[bone_index]),
                        min(bone_local_vertex_z[bone_index]),
                    ))
                    bone.bounding_box_max = Vector3((
                        max(bone_local_vertex_x[bone_index]),
                        max(bone_local_vertex_y[bone_index]),
                        max(bone_local_vertex_z[bone_index]),
                    ))
                else:
                    bone.bounding_box_min = Vector3((SINGLE_MAX, SINGLE_MAX, SINGLE_MAX))
                    bone.bounding_box_max = Vector3((SINGLE_MIN, SINGLE_MIN, SINGLE_MIN))

        if all_x or all_y or all_z:
            self.bounding_box_min = Vector3((min(all_x), min(all_y), min(all_z)))
            self.bounding_box_max = Vector3((max(all_x), max(all_y), max(all_z)))
        else:
            # No vertex data in ANY mesh. Highly suspect, obviously.
            _LOGGER.warning("No vertex data in any mesh. Setting FLVER bounding box min/max to zero vectors.")
            self.bounding_box_min = Vector3.zero()
            self.bounding_box_max = Vector3.zero()

    # TODO: method that recalculates a single bone's bounding box, which is slightly more efficient in that it can skip
    #  any meshes that don't have it as a `mesh.bone_index`.

    def get_root_bones(self) -> list[FLVERBone]:
        """Return all bones with no parent."""
        return [bone for bone in self.bones if bone.parent_index == -1]

    def get_bone_armature_space_transforms(self) -> list[tuple[Vector3, Matrix3, Vector3]]:
        """Compute the FLVER armature space transforms of all bones at once by moving downward through the hierarchy.

        Note that bone scale is not inherited. All scale values are local.

        Also note that we can't cache this because any/all parent bone transforms could change. It's inexpensive anyway.
        """
        root_bones = self.get_root_bones()
        # Start with local transforms. They will be changed to armature space transforms one at a time, recursively.
        armature_space_transforms = [bone.get_local_transform() for bone in self.bones]
        done_indices = set()

        def local_to_parent_space(bone: FLVERBone, parent_transform: tuple[Vector3, Matrix3, Vector3]):
            index = bone.get_bone_index(self.bones)
            if index in done_indices:
                raise ValueError(f"Bone '{bone.name}' is a child of multiple bones.")
            done_indices.add(index)
            local_translate, local_rotate_matrix, local_scale = armature_space_transforms[index]
            parent_translate, parent_rotate_matrix, _ = parent_transform
            bone_armature_transform = (
                parent_translate + parent_rotate_matrix @ local_translate,
                parent_rotate_matrix @ local_rotate_matrix,
                local_scale,  # scale not inherited
            )
            armature_space_transforms[index] = bone_armature_transform
            for child_bone in bone.get_all_immediate_children(self.bones):
                local_to_parent_space(child_bone, bone_armature_transform)

        for root_bone in root_bones:
            local_to_parent_space(root_bone, (Vector3.zero(), Matrix3.identity(), Vector3.one()))

        return armature_space_transforms

    def set_bone_armature_space_transforms(self, armature_space_transforms: list[tuple[Vector3, Matrix3, Vector3]]):
        """Use given `armature_space_transforms` to set the local transforms of each `FLVERBone`, by applying the
        inverse of each parent's armature space transform (conveniently available).

        NOTE: Bone scale is NOT inherited. All scale vectors in `armature_space_transforms` will be treated as local
        bone scale vectors.
        """

        if (arma_count := len(armature_space_transforms)) != len(self.bones):
            raise ValueError(f"Expected {len(self.bones)} armature space transforms, but got {arma_count}.")

        parent_inv_rots = {}  # type: dict[int, Matrix3]

        for bone_index, bone in enumerate(self.bones):
            arma_transform = armature_space_transforms[bone_index]
            parent_index = bone.parent_index
            if parent_index == -1:
                # Root bone: armature space transform is local transform.
                bone.set_local_transform(arma_transform)
                continue

            # Get parent transform and apply inverse to this bone's armature space transform.
            arma_translate, arma_rotate_matrix, arma_scale = arma_transform
            parent_arma_translate, parent_arma_rotate_matrix, _ = armature_space_transforms[parent_index]
            parent_arma_inv_rotate = parent_inv_rots.setdefault(parent_index, parent_arma_rotate_matrix.inverse())

            bone.set_local_transform((
                parent_arma_inv_rotate @ (arma_translate - parent_arma_translate),
                parent_arma_inv_rotate @ arma_rotate_matrix,
                arma_scale,  # scale not inherited
            ))

    def check_if_all_zero_bone_weights(self) -> bool:
        """Reliable (so far) indicator of map piece FLVER, as opposed to character/object FLVER.

        Map pieces sometimes use bone indices as an offset for certain meshes (or even a subset of a mesh's vertices),
        but never use bone weights (in DS1 at least).

        This method checks every vertex and is therefore reasonably expensive to compute, so do it sparingly.
        """
        for m in self.meshes:
            for v in m.vertices:
                if any(v.bone_weights):
                    return False
        return True

    # endregion
