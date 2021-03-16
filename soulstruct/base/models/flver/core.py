from __future__ import annotations

__all__ = ["FLVER"]

import io
import typing as tp
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject

from .bone import Bone
from .dummy import Dummy
from .material import GXList, Material, Texture
from .mesh import FaceSet, Mesh
from .version import Version
from .vertex import BufferLayout, VertexBuffer


class FLVERHeader(BinaryObject):

    STRUCT = BinaryStruct(
        ("file_type", "6s", "FLVER\0"),
        ("endian", "2s"),  # TODO: b"L\0" or b"B\0"
        ("version", "i"),  # `Version`
        ("data_offset", "i"),
        ("data_size", "i"),
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
    data_offset: int
    data_size: int
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


class FLVER(GameFile):
    """Model format used since Dark Souls PTDE.

    Technically, this format is FLVER2. Demon's Souls used a different format, FLVER0, which is not supported here.
    """

    header: FLVERHeader

    def __init__(
        self,
        file_source: tp.Union[None, str, Path, bytes, io.BufferedIOBase] = None,
        dcx_magic: tuple[int, int] = (),
        **kwargs,
    ):
        self.header = FLVERHeader()
        self.dummies = []  # type: list[Dummy]
        self.gx_lists = []  # type: list[GXList]
        self.materials = []  # type: list[Material]
        self.bones = []  # type: list[Bone]
        self.meshes = []  # type: list[Mesh]
        self.buffer_layouts = []  # type: list[BufferLayout]
        # TODO

        super().__init__(file_source, dcx_magic, **kwargs)

    def unpack(self, buffer: io.BufferedIOBase, **kwargs):
        self.header = FLVERHeader(buffer)

        self.dummies = [
            Dummy(buffer, dict(color_is_argb=self.header.version == Version.DarkSouls2))
            for _ in range(self.header.dummy_count)
        ]

        gx_list_indices = {}  # type: dict[int, int]  # maps `_gx_offset` in `Material` to `self.gx_lists` index
        self.gx_lists = []
        self.materials = [
            Material(
                buffer,
                dict(
                    unicode=self.header.unicode,
                    version=self.header.version,
                    gx_lists=self.gx_lists,
                    gx_list_indices=gx_list_indices,
                )
            )
            for _ in range(self.header.material_count)
        ]

        self.bones = [
            Bone(buffer, dict(unicode=self.header.unicode))
            for _ in range(self.header.bone_count)
        ]

        self.meshes = [
            Mesh(buffer, dict(bounding_box_has_unknown=self.header.version == Version.Sekiro))
            for _ in range(self.header.mesh_count)
        ]

        face_sets = {
            i: FaceSet(
                buffer,
                dict(
                    header_index_size=self.header.vertex_indices_size,
                    data_offset=self.header.data_offset,
                )
            )
            for i in range(self.header.face_set_count)
        }

        vertex_buffers = {i: VertexBuffer(buffer) for i in range(self.header.vertex_buffer_count)}

        self.buffer_layouts = [BufferLayout(buffer) for _ in range(self.header.buffer_layout_count)]

        textures = {i: Texture(buffer, dict(unicode=self.header.unicode)) for i in range(self.header.texture_count)}

        # TODO: Sekiro has an additional unknown structure here.

        for material in self.materials:
            # Each texture is only assigned to ONE material. Texture is popped from `textures` after first assignment.
            material.assign_textures(textures)
        if textures:
            raise ValueError(f"{len(textures)} `Texture`s were left over after assignment to `Material`s.")

        for mesh in self.meshes:
            mesh.assign_face_sets(face_sets)
            mesh.assign_vertex_buffers(vertex_buffers, self.buffer_layouts)
            mesh.read_vertices(buffer, self.header.data_offset, self.buffer_layouts, self.header.version)
        if face_sets:
            raise ValueError(f"{len(face_sets)} `FaceSet`s were left over after assignment to `Mesh`es.")
        if vertex_buffers:
            raise ValueError(f"{len(vertex_buffers)} `VertexBuffer`s were left over after assignment to `Mesh`es.")

    def pack(self):

        # Update header counts.
        self.header.dummy_count = len(self.dummies)
        self.header.material_count = len(self.materials)
        self.header.bone_count = len(self.bones)
        self.header.mesh_count = len(self.meshes)
        self.header.vertex_buffer_count = sum(len(mesh.vertex_buffers) for mesh in self.meshes)
        self.header.face_set_count = sum(len(mesh.face_sets) for mesh in self.meshes)
        self.header.buffer_layout_count = len(self.buffer_layouts)
        self.header.texture_count = sum(len(material.textures) for material in self.materials)

        self.header.true_face_count = 0
        self.header.total_face_count = 0
        for mesh in self.meshes:
            allow_primitive_restarts = len(mesh.vertices) < 2 ** 16 - 1  # max unsigned short value
            for face_set in mesh.face_sets:
                face_set_true_count, face_set_total_count = face_set.get_face_counts(allow_primitive_restarts)
                self.header.true_face_count += face_set_true_count
                self.header.total_face_count += face_set_total_count

        if self.header.version < Version.Bloodborne_DS3_A:
            # Set header's `vertex_index_size` to the largest size detected across all `FaceSet`s (16 or 32).
            self.header.vertex_indices_size = 16
            for mesh in self.meshes:
                for face_set in mesh.face_sets:
                    face_set_vertex_index_size = face_set.get_vertex_index_size()
                    self.header.vertex_indices_size = max(self.header.vertex_indices_size, face_set_vertex_index_size)
        else:
            # Vertex size is stored per `VertexBuffer`.
            self.header.vertex_indices_size = 0

        # Header `data_offset` and `data_size` are set just before final write.

        packed_dummies = b"".join(dummy.pack(self.header.version) for dummy in self.dummies)
        packed_materials = b"".join(material.pack(i) for i, material in enumerate(self.materials))

        # TODO: Set header `data_offset` and `data_size`.
        packed_header = self.header.pack()