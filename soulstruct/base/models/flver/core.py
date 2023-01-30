from __future__ import annotations

__all__ = ["FLVER"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.containers import Binder, BND
from soulstruct.containers.tpf import TPF
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.binary import *

from .bone import Bone
from .dummy import Dummy
from .material import GXList, Material, Texture
from .mesh import FaceSet, Mesh
from .version import Version
from .vertex import BufferLayout, VertexBuffer, VertexBufferSizeError

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class FLVERHeader(BinaryStruct):
    _file_type: bytes = field(init=False, metadata=fixed_bytes(asserted_value=b"FLVER\0"))
    endian: bytes = field(metadata=fixed_bytes(asserted_value=[b"L\0", b"R\0"]))
    version: Version = field(metadata=int_enum(int))
    vertex_data_offset: int
    vertex_data_size: int
    dummy_count: int
    material_count: int
    bone_count: int
    mesh_count: int
    vertex_buffer_count: int
    bounding_box_min: Vector3 = field(metadata=vector(3))
    bounding_box_max: Vector3 = field(metadata=vector(3))
    true_face_count: int
    total_face_count: int
    vertex_indices_size: byte = field(metadata=asserted([0, 8, 16, 32]))
    unicode: bool
    unk_x4a: bool
    _pad1: bytes = field(init=False, metadata=pad(1))
    unk_x4c: int
    face_set_count: int
    buffer_layout_count: int
    texture_count: int
    unk_x5c: byte
    unk_x5d: byte
    _pad2: bytes = field(init=False, metadata=pad(10))
    unk_x68: int
    _pad3: bytes = field(init=False, metadata=pad(20))

    # TODO: caller wants to reserve `vertex_data_offset` and `vertex_data_size`


@dataclass(slots=True)
class FLVER(GameFile):
    """Model format used since Dark Souls PTDE.

    Technically, this format is FLVER2. Demon's Souls used an older version, `FLVER0`, which is not supported here.
    """

    # Convenience access to classes.
    Bone: tp.ClassVar = Bone
    Dummy: tp.ClassVar = Dummy
    GXList: tp.ClassVar = GXList
    Material: tp.ClassVar = Material
    Mesh: tp.ClassVar = Mesh
    BufferLayout: tp.ClassVar = BufferLayout
    VertexBuffer: tp.ClassVar = VertexBuffer

    EXT: tp.ClassVar = ".flver"

    dummies: list[Dummy]
    gx_lists: list[GXList]
    materials: list[Material]
    bones: list[Bone]
    meshes: list[Mesh]
    buffer_layouts: list[BufferLayout]

    # Header information that can't be automated.
    big_endian: bool
    version: Version
    bounding_box_min: Vector3
    bounding_box_max: Vector3
    vertex_indices_size: byte
    unicode: bool
    unk_x4a: bool
    unk_x4c: int
    unk_x5c: byte
    unk_x5d: byte
    unk_x68: int

    @classmethod
    def _from_reader(cls, reader: BinaryReader):
        byte_order = BinaryCondition((6, 2), [(ByteOrder.LittleEndian, b"L\0"), (ByteOrder.BigEndian, b"R\0")])
        header = FLVERHeader.from_bytes(reader, byte_order=byte_order)

        encoding = "utf-16-le" if header.unicode else "shift_jis_2004"

        dummies = [
            Dummy(reader, color_is_argb=header.version == Version.DarkSouls2)
            for _ in range(header.dummy_count)
        ]

        gx_list_indices = {}  # type: dict[int, int]  # maps `_gx_offset` in `Material` to `self.gx_lists` index
        gx_lists = []
        materials = [
            Material(
                reader,
                encoding=encoding,
                version=header.version,
                gx_lists=gx_lists,
                gx_list_indices=gx_list_indices,
            )
            for _ in range(header.material_count)
        ]

        bones = [Bone(reader, encoding=encoding) for _ in range(header.bone_count)]

        meshes = [
            Mesh(reader, bounding_box_has_unknown=header.version == Version.Sekiro)
            for _ in range(header.mesh_count)
        ]

        face_sets = {
            i: FaceSet(
                reader,
                header_vertex_index_size=header.vertex_indices_size,
                vertex_data_offset=header.vertex_data_offset,
            )
            for i in range(header.face_set_count)
        }

        vertex_buffers = {i: VertexBuffer(reader) for i in range(header.vertex_buffer_count)}

        buffer_layouts = [BufferLayout(reader) for _ in range(header.buffer_layout_count)]

        textures = {i: Texture(reader, encoding=encoding) for i in range(header.texture_count)}

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

        return cls(
            dummies,
            gx_lists,
            materials,
            bones,
            meshes,
            buffer_layouts,
            header.endian == b"B\0",
            header.version,
            header.bounding_box_min,
            header.bounding_box_max,
            header.vertex_indices_size,
            header.unicode,
            header.unk_x4a,
            header.unk_x4c,
            header.unk_x5c,
            header.unk_x5d,
            header.unk_x68,
        )

    @classmethod
    def from_chrbnd(cls, chrbnd: BND) -> FLVER:
        """Open CHRBND from given `chrbnd_source` and load its `.flver` file (with or without DCX extension).

        Will raise an exception if no FLVER files or multiple FLVER files exist in the BND.
        """
        flver_entry = chrbnd.find_entry_matching_name(r".*\.flver(\.dcx)?")
        return cls.from_bytes(flver_entry)

    def _to_writer(self) -> BinaryWriter:

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

        header_writer = FLVERHeader(
            endian=b"B\0" if self.big_endian else b"L\0",
            version=self.version,
            vertex_data_offset=RESERVED(int),
            vertex_data_size=RESERVED(int),
            dummy_count=len(self.dummies),
            material_count=len(self.materials),
            bone_count=len(self.bones),
            mesh_count=len(self.meshes),
            vertex_buffer_count=sum(len(mesh.vertex_buffers) for mesh in self.meshes),
            bounding_box_min=self.bounding_box_min,
            bounding_box_max=self.bounding_box_max,
            true_face_count=true_face_count,
            total_face_count=total_face_count,
            vertex_indices_size=header_vertex_indices_size,
            unicode=self.unicode,
            unk_x4a=self.unk_x4a,
            unk_x4c=self.unk_x4c,
            face_set_count=sum(len(mesh.face_sets) for mesh in self.meshes),
            buffer_layout_count=len(self.buffer_layouts),
            texture_count=sum(len(material.textures) for material in self.materials),
            unk_x5c=self.unk_x5c,
            unk_x5d=self.unk_x5d,
            unk_x68=self.unk_x68,
        ).to_writer()

        for dummy in self.dummies:
            dummy.pack(writer, color_is_argb=self.version == Version.DarkSouls2)

        for material in self.materials:
            material.pack(writer)

        for bone in self.bones:
            bone.pack(writer)

        for mesh in self.meshes:
            mesh.pack(writer)

        for mesh in self.meshes:
            for face_set in mesh.face_sets:
                if header_vertex_indices_size == 0:
                    face_set_vertex_index_size = face_set.get_vertex_index_size()
                else:
                    face_set_vertex_index_size = header_vertex_indices_size
                face_set.pack(writer, face_set_vertex_index_size)

        for mesh in self.meshes:
            for i, vertex_buffer in enumerate(mesh.vertex_buffers):
                vertex_buffer.pack(
                    writer,
                    self.header.version,
                    mesh_vertex_buffer_index=i,
                    buffer_layouts=self.buffer_layouts,
                    mesh_vertex_count=len(mesh.vertices),
                )

        for i, buffer_layout in enumerate(self.buffer_layouts):
            buffer_layout.pack(writer)

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
            gx_list.pack(writer)
        for material in self.materials:
            material.fill_gx_offset(writer, gx_offsets)

        writer.pad_align(16)
        for material in self.materials:
            material.pack_strings(writer, encoding)
            for texture in material.textures:
                texture.pack_zstring(writer, "path", encoding=encoding)
                texture.pack_zstring(writer, "texture_type", encoding=encoding)

        writer.pad_align(16)
        for bone in self.bones:
            bone.pack_zstring(writer, "name", encoding=encoding)

        alignment = 32 if self.header.version <= 0x2000E else 16
        writer.pad_align(alignment)
        if self.header.version in {Version.DarkSouls2_NT, Version.DarkSouls2}:
            writer.pad(32)

        vertex_data_start = writer.position
        self.header.fill(writer, vertex_data_offset=vertex_data_start)

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

            for vertex_buffer in mesh.vertex_buffers:

                for vertex in mesh.vertices:
                    vertex.prepare_pack()

                writer.pad_align(16)
                uv_factor = 2048 if self.header.version >= Version.DarkSouls2_NT else 1024
                vertex_buffer.pack_buffer(
                    writer,
                    buffer_layouts=self.buffer_layouts,
                    vertices=mesh.vertices,
                    buffer_offset=writer.position - vertex_data_start,
                    uv_factor=uv_factor,
                )

            for vertex in mesh.vertices:
                try:
                    vertex.finish_pack()
                except ValueError as ex:
                    mesh_material = self.materials[mesh.material_index]
                    raise ValueError(
                        f"Mesh {i} left in invalid state after pack.\n"
                        f"Material MTD: {mesh_material.mtd_name}\n"
                        f"Material textures: {', '.join(tex.texture_type for tex in mesh_material.textures)}"
                        f"Error: {ex}"
                    )

        writer.pad_align(16)
        self.header.fill(writer, vertex_data_size=writer.position - vertex_data_start)
        if self.header.version in {Version.DarkSouls2_NT, Version.DarkSouls2}:
            writer.pad(32)

        return writer.finish()

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
            bone_position = bone.get_absolute_translate_rotate(self.bones)[0]
            axes.scatter(*bone_position.to_xzy(), color="blue", s=10)
        if auto_show:
            plt.show()

    def scale(self, factor: float):
        """Modifies the FLVER in place by scaling all dummies, bones, and vertices by `factor`.

        Will NOT have full functionality in-game until Havok physics files are modified as well.
        """
        for dummy in self.dummies:
            dummy.position *= factor
        for bone in self.bones:
            bone.translate *= factor
        for mesh in self.meshes:
            for vertex in mesh.vertices:
                vertex.position *= factor

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
        return {Path(texture.path) for material in self.materials for texture in material.textures if texture.path}

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
        tpf_paths = [(p, re.compile(rf"{p.stem}\.tpf(\.dcx)?")) for p in self.get_all_texture_paths()]
        tpf_sources = {}
        for bhd_path in tpfbhd_directory.glob("*.tpfbhd"):
            bxf = Binder(bhd_path, create_bak_if_missing=False)
            for entry in bxf.entries:
                for tpf_path, tpf_re in reversed(tpf_paths):
                    if tpf_re.match(entry.name):
                        tpf_paths.remove((tpf_path, tpf_re))
                        tpf_sources[tpf_path] = TPF(entry.data)
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
