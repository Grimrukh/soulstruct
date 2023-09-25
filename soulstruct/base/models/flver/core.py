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
from .submesh import FaceSet, Submesh
from .version import Version
from .vertex import BufferLayout, VertexBuffer, VertexBufferSizeError

import numpy as np

try:
    Self = tp.Self
except AttributeError:
    Self = "FLVER"

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
    Submesh: tp.ClassVar = Submesh
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
    submeshes: list[Submesh] = field(default_factory=list)
    buffer_layouts: list[BufferLayout] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
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

        submeshes = [
            Submesh.from_flver_reader(reader, bounding_box_has_unknown=header.version == Version.Sekiro)
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
            check_ds1_layouts(buffer_layouts, vertex_buffers, submeshes, materials)

        textures = {i: Texture.from_flver_reader(reader, encoding=encoding) for i in range(header.texture_count)}

        # TODO: Sekiro has an additional unknown structure here.

        for material in materials:
            # Each texture is only assigned to ONE material. Texture is popped from `textures` after first assignment.
            material.assign_textures(textures)
        if textures:
            raise ValueError(f"{len(textures)} textures were left over after assignment to materials.")

        for i, submesh in enumerate(submeshes):
            submesh.assign_face_sets(face_sets)
            submesh.assign_vertex_buffers(vertex_buffers, buffer_layouts)
            uv_factor = 2048 if header.version >= Version.DarkSouls2_NT else 1024

            try:
                submesh.vertex_arrays = [
                    vertex_buffer.read_buffer(reader, buffer_layouts, header.vertex_data_offset, uv_factor)
                    for vertex_buffer in submesh.vertex_buffers
                ]
            except VertexBufferSizeError as ex:
                mtd_name = materials[submesh.material_index].mtd_name
                _LOGGER.warning(
                    f"Submesh {i} in FLVER (MTD '{mtd_name}') has a vertex buffer size {ex.vertex_size}, but its "
                    f"buffer layout has size {ex.layout_size}). Submesh marked with `invalid_layout_size = True`; "
                    f"handle this as needed."
                )
                submesh.invalid_layout_size = True
        if face_sets:
            raise ValueError(f"{len(face_sets)} face sets were left over after assignment to submeshes.")
        if vertex_buffers:
            raise ValueError(f"{len(vertex_buffers)} vertex buffers were left over after assignment to submeshes.")

        return header.to_object(
            cls,
            big_endian=header.endian == b"B\0",
            dummies=dummies,
            gx_lists=gx_lists,
            materials=materials,
            bones=bones,
            submeshes=submeshes,
            buffer_layouts=buffer_layouts,
        )

    @classmethod
    def from_path(cls, path: str | Path) -> Self:
        """Reports invalid buffer layouts."""
        flver = super(FLVER, cls).from_path(path)
        assert isinstance(flver, FLVER)
        if any(mesh.invalid_layout_size for mesh in flver.submeshes):
            _LOGGER.warning(f"FLVER '{Path(path).name}' has one or more submeshes with invalid vertex buffer sizes.")
        return flver

    @classmethod
    def from_chrbnd(cls, chrbnd: Binder) -> Self:
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
        for mesh in self.submeshes:
            allow_primitive_restarts = len(mesh.vertices) < 0xFFFF  # max unsigned short value
            for face_set in mesh.face_sets:
                face_set_true_count, face_set_total_count = face_set.get_face_counts(allow_primitive_restarts)
                true_face_count += face_set_true_count
                total_face_count += face_set_total_count

        if self.version < Version.Bloodborne_DS3_A:
            # Set header's `vertex_index_size` to the largest size detected across all `FaceSet`s (16 or 32).
            header_vertex_indices_size = 16
            for mesh in self.submeshes:
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
            mesh_count=len(self.submeshes),
            vertex_buffer_count=sum(len(mesh.vertex_buffers) for mesh in self.submeshes),
            true_face_count=true_face_count,
            total_face_count=total_face_count,
            vertex_indices_size=header_vertex_indices_size,
            face_set_count=sum(len(mesh.face_sets) for mesh in self.submeshes),
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

        for mesh in self.submeshes:
            mesh.to_flver_writer(writer)

        for mesh in self.submeshes:
            for face_set in mesh.face_sets:
                if header_vertex_indices_size == 0:
                    face_set_vertex_index_size = face_set.get_vertex_index_size()
                else:
                    face_set_vertex_index_size = header_vertex_indices_size
                face_set.to_flver_writer(writer, face_set_vertex_index_size)

        for mesh in self.submeshes:
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
        for i, mesh in enumerate(self.submeshes):
            mesh.pack_bounding_box(writer)

        writer.pad_align(16)
        bone_indices_start = writer.position
        for i, mesh in enumerate(self.submeshes):
            mesh.pack_bone_indices(writer, bone_indices_start=bone_indices_start)

        writer.pad_align(16)
        first_face_set_index = 0
        for i, mesh in enumerate(self.submeshes):
            mesh.pack_face_set_indices(writer, first_face_set_index)
            first_face_set_index += len(mesh.face_sets)

        writer.pad_align(16)
        first_vertex_buffer_index = 0
        for mesh in self.submeshes:
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

        for i, mesh in enumerate(self.submeshes):
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

    def to_obj(self, name="FLVER", submeshes=()) -> str:
        if isinstance(submeshes, int):
            submeshes = [submeshes]
        vertex_offset = 0
        mesh_objs = []
        for i, mesh in enumerate(self.submeshes):
            if submeshes and i not in submeshes:
                continue  # skip this mesh
            mesh_objs.append(mesh.to_obj(name=f"{name} Mesh {i}", vertex_offset=vertex_offset))
            vertex_offset += len(mesh.vertices)
        return "\n\n".join(mesh_objs)

    def write_obj(self, obj_path: Path | str = None, obj_name="", make_dirs=True, submeshes=()):
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
        obj_str = self.to_obj(name=obj_name, submeshes=submeshes)
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
        if self.submeshes:
            submeshes = "[\n    " + "\n    ".join(repr(self.submeshes)[1:-1].split("\n")) + "\n  ]"
        else:
            submeshes = "[]"
        return (
            f"FLVER(\n"
            f"  bones = {bones}\n"
            f"  dummies = {dummies}\n"
            f"  materials = {materials}\n"
            f"  gx_lists = {gx_lists}\n"
            f"  submeshes = {submeshes}\n"
            ")"
        )

    def draw(self, auto_show=False, show_mesh_face_sets=(), show_origin=False, axes=None, **kwargs):
        import matplotlib.pyplot as plt
        if show_mesh_face_sets == "all":
            show_mesh_face_sets = tuple(range(len(self.submeshes)))
        if axes is None:
            axes = plt.figure().add_subplot(111, projection="3d")
        for i, mesh in enumerate(self.submeshes):
            mesh.draw(
                show_origin=show_origin and mesh is self.submeshes[-1],
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

    def get_submesh_material(self, submesh_index: int) -> Material:
        return self.materials[self.submeshes[submesh_index].material_index]

    def get_submesh_buffer_layout(self, submesh_index: int, vertex_array_index=0) -> BufferLayout:
        return self.buffer_layouts[self.submeshes[submesh_index].vertex_buffers[vertex_array_index].layout_index]

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
        for submesh in self.submeshes:
            for vertex in submesh.vertices:
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

    # endregion

    # region Bones

    def sort_submesh_bone_indices(self):
        """Sort all local `submesh.bone_indices` in ascending order and update local bone indices of all vertices.

        Handles both standard bone weights (where a weight <= 0.0 indicates an unused bone index that should NOT be
        remapped as though it were actually bone zero) and 'pose' bone weights, as is used by map pieces (all indices
        are the same single bone index used to offset the vertex, all weights are 0.0).
        """
        for submesh in self.submeshes:
            if submesh.bone_indices is None:
                continue  # this submesh has global vertex bone indices

            sorted_indices = np.argsort(submesh.bone_indices)
            # Sort now, and use `sorted_indices` to remap vertex data below.
            submesh.bone_indices = submesh.bone_indices[sorted_indices]

            for vertex_array in submesh.vertex_arrays:
                # Check map piece 'pose' case, where all four weights are 0.0:
                if all(weight == 0.0 for weight in vertex_array[[f"bone_weight_{c}" for c in "abcd"]][0]):
                    bone_index = vertex_array["bone_index_a"]  # all four indices should be the same for each vertex
                    new_bone_index = sorted_indices[bone_index]
                    for c in "abcd":
                        vertex_array[f"bone_index_{c}"] = new_bone_index
                else:
                    # Standard case, where at least one bone weight is non-zero.
                    for c in "abcd":
                        # Only remap indices of `vertex_array` where `bone_weight_{c}` is non-zero.
                        non_zero_vertices = np.nonzero(vertex_array[f"bone_weight_{c}"])[0]
                        bone_indices = vertex_array[f"bone_index_{c}"][non_zero_vertices]
                        vertex_array[f"bone_index_{c}"][non_zero_vertices] = sorted_indices[bone_indices]

    def refresh_bone_bounding_boxes(self, in_armature_space=False, only_bones: tp.Container[int] = ()):
        """Refresh the bounding box of each bone by finding every vertex in every submesh weighted to it."""

        if not in_armature_space:
            bone_arma_translate_inv_rotates = [
                (translate, rotate.inverse())
                for translate, rotate, _ in self.get_bone_armature_space_transforms()
            ]
        else:
            # Unused.
            bone_arma_translate_inv_rotates = []

        # 3D arrays that track min/max vertex positions for each bone and axis.
        bone_mins = SINGLE_MAX * np.ones((len(self.bones), 3))
        bone_maxs = SINGLE_MIN * np.ones((len(self.bones), 3))

        for i, submesh in enumerate(self.submeshes):

            for vertex_array in submesh.vertex_arrays:

                weighted_vertices_indices = []

                position = np.column_stack([vertex_array[f"position_{c}"] for c in "xyz"])  # (n, 3) array
                bone_index_a = vertex_array["bone_index_a"]
                if submesh.bone_indices is not None:
                    # Remap bone indices to global indices.
                    bone_index_a = submesh.bone_indices[bone_index_a]
                try:
                    bone_weight_a = vertex_array["bone_weight_a"]
                except ValueError:
                    # No bone weights (map piece 'pose' mode). We only need to look at first bone index (always used).
                    for bone_index in range(len(self.bones)):
                        weighted_vertices_indices.append(bone_index_a == bone_index)
                else:
                    bone_index_b = vertex_array["bone_index_b"]
                    bone_index_c = vertex_array["bone_index_c"]
                    bone_index_d = vertex_array["bone_index_d"]
                    if submesh.bone_indices is not None:
                        # Remap bone indices to global indices.
                        bone_index_b = submesh.bone_indices[bone_index_b]
                        bone_index_c = submesh.bone_indices[bone_index_c]
                        bone_index_d = submesh.bone_indices[bone_index_d]
                    # Check if all bone indices are the same, in which case we can skip the weight check.
                    if (
                        np.all(bone_index_a == bone_index_b)
                        and np.all(bone_index_a == bone_index_c)
                        and np.all(bone_index_a == bone_index_d)
                    ):
                        # Only one bone index (map piece 'pose' mode).
                        for bone_index in range(len(self.bones)):
                            weighted_vertices_indices.append(bone_index_a == bone_index)
                    else:
                        # Use bone weights to determine when bone indices are used.
                        # TODO: Currently making NO assumptions about bone index ordering. So we don't, say, stop after
                        #  encountering the first non-zero weight for each vertex (not sure how we'd do that with array
                        #  ops anyway).
                        bone_weight_b = vertex_array["bone_weight_b"]
                        bone_weight_c = vertex_array["bone_weight_c"]
                        bone_weight_d = vertex_array["bone_weight_d"]
                        for bone_index in range(len(self.bones)):
                            # Rather complication logical boolean check. We want to find out if `bone_index` is used
                            # as any of the four bone indices, AND the corresponding bone weight is greater than zero.
                            weighted_vertices_indices.append(
                                ((bone_weight_a > 0.0) & (bone_index_a == bone_index))
                                | ((bone_weight_b > 0.0) & (bone_index_b == bone_index))
                                | ((bone_weight_c > 0.0) & (bone_index_c == bone_index))
                                | ((bone_weight_d > 0.0) & (bone_index_d == bone_index))
                            )

                for bone_index, vertex_indices in enumerate(weighted_vertices_indices):
                    if only_bones and bone_index not in only_bones:
                        continue
                    if not np.any(vertex_indices):
                        continue  # bone unused by this submesh array

                    bone_vertex_positions = position[vertex_indices, :]  # only vertex rows where bone is used

                    if not in_armature_space:
                        # Transform vertex positions into bone local space (typical for characters).
                        arma_translate, inv_arma_rotate = bone_arma_translate_inv_rotates[bone_index]
                        bone_vertex_positions -= arma_translate.data
                        bone_vertex_positions = bone_vertex_positions @ inv_arma_rotate.data.T

                    bone_vertex_mins = np.min(bone_vertex_positions, axis=0)  # (x, y, z) minimum for bone/submesh/array
                    bone_vertex_maxs = np.max(bone_vertex_positions, axis=0)  # (x, y, z) maximum for bone/submesh/array

                    # Update FLVER-wide bone minimum and maximums.
                    bone_mins[bone_index] = np.min((bone_mins[bone_index], bone_vertex_mins), axis=0)
                    bone_maxs[bone_index] = np.max((bone_maxs[bone_index], bone_vertex_maxs), axis=0)

        # Update bone bounding boxes.
        for bone_i, bone in enumerate(self.bones):
            if only_bones and bone_i not in only_bones:
                continue
            # print(f"BEFORE: {bone.name}: {bone.bounding_box_min} -> {bone.bounding_box_max}")
            bone.bounding_box_min = Vector3(bone_mins[bone_i])
            bone.bounding_box_max = Vector3(bone_maxs[bone_i])
            # print(f"    --> {bone.name}: {bone.bounding_box_min} -> {bone.bounding_box_max}")

    def refresh_bounding_boxes(self):
        """Refresh global bounding box of FLVER from minimum and maximum positions of all submesh vertices."""

        # This is trivial with NumPy vertex data.
        vertex_min = np.array([SINGLE_MIN] * 3)
        vertex_max = np.array([SINGLE_MAX] * 3)

        for submesh in self.submeshes:
            for vertex_array in submesh.vertex_arrays:
                position = vertex_array[["position_x", "position_y", "position_z"]]
                vertex_min = np.min((vertex_min, np.min(position, axis=0)))
                vertex_max = np.max((vertex_max, np.max(position, axis=0)))

        self.bounding_box_min = Vector3(vertex_min)
        self.bounding_box_max = Vector3(vertex_max)

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

        Map pieces sometimes use bone indices as an offset for certain submeshes (or even a subset of a mesh's 
        vertices), but never use bone weights (in DS1 at least).

        This method checks every vertex and is therefore reasonably expensive to compute, so do it sparingly.
        """
        for m in self.submeshes:
            for v in m.vertices:
                if any(v.bone_weights):
                    return False
        return True

    # endregion
