"""NOTE: This file is Python 3.9 compatible for Blender 3.X use."""
from __future__ import annotations

__all__ = ["FLVER"]

import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.containers import Binder
from soulstruct.containers.tpf import TPF
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader, BinaryWriter

from .bone import Bone
from .dummy import Dummy
from .material import GXList, Material, Texture
from .mesh import FaceSet, Mesh
from .version import Version
from .vertex import BufferLayout, VertexBuffer, VertexBufferSizeError

_LOGGER = logging.getLogger(__name__)


class FLVERHeader(BinaryObject):

    STRUCT = BinaryStruct(
        ("file_type", "6s", "FLVER\0"),
        ("endian", "2s"),  # TODO: b"L\0" or b"B\0"
        ("version", "i"),  # `Version`
        ("vertex_data_offset", "i"),
        ("vertex_data_size", "i"),
        ("dummy_count", "i"),
        ("material_count", "i"),
        ("bone_count", "i"),
        ("mesh_count", "i"),
        ("vertex_buffer_count", "i"),
        ("bounding_box_min", "3f"),  # `Vector3`
        ("bounding_box_max", "3f"),  # `Vector3`
        ("true_face_count", "i"),  # does not include motion blur meshes or degenerate faces
        ("total_face_count", "i"),  # all faces
        ("vertex_indices_size", "B"),  # 0, 8, 16, 32
        ("unicode", "?"),
        ("unk_x4a", "?"),
        "x",
        ("unk_x4c", "i"),
        ("face_set_count", "i"),
        ("buffer_layout_count", "i"),
        ("texture_count", "i"),
        ("unk_x5c", "B"),
        ("unk_x5d", "B"),
        "10x",
        ("unk_x68", "i"),
        "20x",
    )

    endian: bytes
    version: Version
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
    vertex_indices_size: int
    unicode: bool
    unk_x4a: bool
    unk_x4c: int
    face_set_count: int
    buffer_layout_count: int
    texture_count: int
    unk_x5c: int
    unk_x5d: int
    unk_x68: int

    def pack(
        self,
        writer: BinaryWriter,
        dummy_count: int,
        material_count: int,
        bone_count: int,
        mesh_count: int,
        vertex_buffer_count: int,
        face_set_count: int,
        buffer_layout_count: int,
        texture_count: int,
        true_face_count: int,
        total_face_count: int,
        vertex_indices_size: int,
    ):
        """All fields are static or can be immediately updated, except the few reserved below."""
        self.dummy_count = dummy_count
        self.material_count = material_count
        self.bone_count = bone_count
        self.mesh_count = mesh_count
        self.vertex_buffer_count = vertex_buffer_count
        self.face_set_count = face_set_count
        self.buffer_layout_count = buffer_layout_count
        self.texture_count = texture_count
        self.true_face_count = true_face_count
        self.total_face_count = total_face_count
        self.vertex_indices_size = vertex_indices_size
        writer.pack_struct(
            self.STRUCT,
            self,
            vertex_data_offset=writer.AUTO_RESERVE,
            vertex_data_size=writer.AUTO_RESERVE,
        )


class FLVER(GameFile):
    """Model format used since Dark Souls PTDE.

    Technically, this format is FLVER2. Demon's Souls used an older version, `FLVER0`, which is not supported here.
    """

    # Convenience access to classes.
    Bone = Bone
    Dummy = Dummy
    GXList = GXList
    Material = Material
    Mesh = Mesh
    BufferLayout = BufferLayout
    VertexBuffer = VertexBuffer

    EXT = ".flver"

    header: FLVERHeader

    dummies: list[Dummy]
    gx_lists: list[GXList]
    materials: list[Material]
    bones: list[Bone]
    meshes: list[Mesh]
    buffer_layouts: list[BufferLayout]

    def __init__(
        self,
        file_source: GameFile.Typing = None,
        dcx_type=None,
        **kwargs,
    ):
        self.header = FLVERHeader()
        self.dummies = []
        self.gx_lists = []
        self.materials = []
        self.bones = []
        self.meshes = []
        self.buffer_layouts = []

        super().__init__(file_source, dcx_type, **kwargs)

    def unpack(self, reader: BinaryReader, **kwargs):
        self.header = FLVERHeader(reader)

        encoding = "utf-16-le" if self.header.unicode else "shift_jis_2004"

        self.dummies = [
            Dummy(reader, color_is_argb=self.header.version == Version.DarkSouls2)
            for _ in range(self.header.dummy_count)
        ]

        gx_list_indices = {}  # type: dict[int, int]  # maps `_gx_offset` in `Material` to `self.gx_lists` index
        self.gx_lists = []
        self.materials = [
            Material(
                reader,
                encoding=encoding,
                version=self.header.version,
                gx_lists=self.gx_lists,
                gx_list_indices=gx_list_indices,
            )
            for _ in range(self.header.material_count)
        ]

        self.bones = [Bone(reader, encoding=encoding) for _ in range(self.header.bone_count)]

        self.meshes = [
            Mesh(reader, bounding_box_has_unknown=self.header.version == Version.Sekiro)
            for _ in range(self.header.mesh_count)
        ]

        face_sets = {
            i: FaceSet(
                reader,
                header_vertex_index_size=self.header.vertex_indices_size,
                vertex_data_offset=self.header.vertex_data_offset,
            )
            for i in range(self.header.face_set_count)
        }

        vertex_buffers = {i: VertexBuffer(reader) for i in range(self.header.vertex_buffer_count)}

        self.buffer_layouts = [BufferLayout(reader) for _ in range(self.header.buffer_layout_count)]

        textures = {i: Texture(reader, encoding=encoding) for i in range(self.header.texture_count)}

        # TODO: Sekiro has an additional unknown structure here.

        for material in self.materials:
            # Each texture is only assigned to ONE material. Texture is popped from `textures` after first assignment.
            material.assign_textures(textures)
        if textures:
            raise ValueError(f"{len(textures)} textures were left over after assignment to materials.")

        for i, mesh in enumerate(self.meshes):
            mesh.assign_face_sets(face_sets)
            mesh.assign_vertex_buffers(vertex_buffers, self.buffer_layouts)
            uv_factor = 2048 if self.header.version >= Version.DarkSouls2_NT else 1024

            try:
                mesh.read_vertices(reader, self.header.vertex_data_offset, self.buffer_layouts, uv_factor)
            except VertexBufferSizeError as ex:
                _LOGGER.warning(
                    f"Mesh {i} in FLVER {self.path.name if self.path else '<unknown>'} has an invalid vertex buffer "
                    f"size ({ex.vertex_size} rather than layout size {ex.layout_size}). Mesh marked with "
                    f"`invalid_vertex_size=True`; handle this as needed."
                )
                mesh.invalid_vertex_size = True
        if face_sets:
            raise ValueError(f"{len(face_sets)} face sets were left over after assignment to meshes.")
        if vertex_buffers:
            raise ValueError(f"{len(vertex_buffers)} vertex buffers were left over after assignment to meshes.")

    @classmethod
    def from_chrbnd(cls, chrbnd_source: GameFile.Typing) -> FLVER:
        """Open CHRBND from given `chrbnd_source` and load its `.flver` file (with or without DCX extension).

        Will raise an exception if no FLVER files or multiple FLVER files exist in the BND.
        """
        chrbnd = Binder(chrbnd_source)
        flver_entry = chrbnd.find_entry_matching_name(r".*\.flver(\.dcx)?")
        return cls(flver_entry)

    def pack(self):

        writer = BinaryWriter(big_endian=self.header.endian == b"B\0")
        encoding = ("utf-16-be" if writer.big_endian else "utf-16-le") if self.header.unicode else "shift_jis_2004"

        true_face_count = 0
        total_face_count = 0
        for mesh in self.meshes:
            allow_primitive_restarts = len(mesh.vertices) < 2 ** 16 - 1  # max unsigned short value
            for face_set in mesh.face_sets:
                face_set_true_count, face_set_total_count = face_set.get_face_counts(allow_primitive_restarts)
                true_face_count += face_set_true_count
                total_face_count += face_set_total_count

        if self.header.version < Version.Bloodborne_DS3_A:
            # Set header's `vertex_index_size` to the largest size detected across all `FaceSet`s (16 or 32).
            header_vertex_indices_size = 16
            for mesh in self.meshes:
                for face_set in mesh.face_sets:
                    face_set_vertex_index_size = face_set.get_vertex_index_size()
                    header_vertex_indices_size = max(header_vertex_indices_size, face_set_vertex_index_size)
        else:
            # Vertex size is stored per `VertexBuffer`.
            header_vertex_indices_size = 0

        self.header.pack(
            writer,
            dummy_count=len(self.dummies),
            material_count=len(self.materials),
            bone_count=len(self.bones),
            mesh_count=len(self.meshes),
            vertex_buffer_count=sum(len(mesh.vertex_buffers) for mesh in self.meshes),
            face_set_count=sum(len(mesh.face_sets) for mesh in self.meshes),
            buffer_layout_count=len(self.buffer_layouts),
            texture_count=sum(len(material.textures) for material in self.materials),
            true_face_count=true_face_count,
            total_face_count=total_face_count,
            vertex_indices_size=header_vertex_indices_size,
        )

        for dummy in self.dummies:
            dummy.pack(writer, color_is_argb=self.header.version == Version.DarkSouls2)

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

        for mesh in self.meshes:
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
                vertex.finish_pack()

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

    def write_obj(self, obj_path: tp.Union[Path, str] = None, obj_name="", make_dirs=True, meshes=()):
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
            bone_position = bone.get_absolute_translate(self.bones)
            axes.scatter(*bone_position.swap_yz(), color="blue", s=10)
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
        """Get set of all texture paths from all materials. Ignores textures with empty `path`."""
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

    def find_all_tpfs(self, tpfbhd_directory: tp.Union[None, str, Path] = None) -> dict[Path, TPF]:
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
