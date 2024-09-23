from __future__ import annotations

__all__ = ["Submesh"]

import logging
import random
import typing as tp
from dataclasses import dataclass, field

import numpy as np

from soulstruct.utilities.binary import *
from soulstruct.utilities.text import indent_lines
from soulstruct.base.models.base.submesh import FaceSet, BaseSubmesh
from .material import Material
from .vertex_array_layout import VertexArrayLayout
from .vertex_array import VertexArray, VertexArrayHeaderStruct

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class Submesh(BaseSubmesh[Material, VertexArrayLayout, VertexArray]):
    """FLVER0 submesh, which has only one built-in 'face set' and is simplified in other ways.

    To unify these classes in Python, we actually use a single `FaceSet` here to store the vertex indices and other
    settings. We don't permit the `flags` or `unk_x06` fields to be set, as they are not used in `FLVER0`.
    """

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):
        dynamic: byte
        material_index: byte
        # start of "FaceSet properties"
        use_backface_culling: bool
        triangle_strip: bool
        vertex_index_count: int
        # end of "FaceSet properties"
        vertex_count: int
        default_bone_index: short
        bone_indices: list[short] = field(**BinaryArray(28))
        unk_x46: short
        _vertex_indices_length: int  # computable from size and `vertex_index_count` above
        vertex_indices_offset: int  # relative to FLVER0 vertex data offset
        vertex_array_data_size: int  # only used if header offset 1 is zero
        vertex_array_data_offset: int  # only used if header offset 1 is zero
        vertex_array_headers_offset_1: int
        vertex_array_headers_offset_2: int
        _pad0: bytes = field(init=False, **BinaryPad(4))

    material: Material  # override
    vertex_arrays: list[VertexArray]  # override

    # `FLVER0` only:
    dynamic: int = 0
    unk_x46: int = 0

    @classmethod
    def from_flver_reader(
        cls,
        reader: BinaryReader,
        vertex_index_size: int,
        vertex_data_offset: int,
        materials: list[Material],
        big_endian: bool,
    ) -> tp.Self:
        submesh_struct = cls.STRUCT.from_bytes(reader)

        material = materials[submesh_struct.material_index]

        if vertex_index_size not in {16, 32}:
            raise ValueError(f"Unsupported vertex index size for `FLVER0` submesh: {vertex_index_size}")
        vertex_index_fmt = f"{submesh_struct.vertex_index_count}{'H' if vertex_index_size == 16 else 'i'}"
        vertex_indices_offset = vertex_data_offset + submesh_struct.vertex_indices_offset
        vertex_indices = list(reader.unpack(vertex_index_fmt, offset=vertex_indices_offset))

        # Weird array setup: two different lists of vertex arrays, and we only expect the first of the first to be used.
        # We also need a hack for older FLVER versions (e.g. Demon's Souls o9993) with neither array offset used.
        if submesh_struct.vertex_array_headers_offset_1 == 0:
            # Hack for old FLVER version.
            array_header = VertexArrayHeaderStruct(
                layout_index=0,
                array_length=submesh_struct.vertex_array_data_size,
                array_offset=submesh_struct.vertex_array_data_offset,
            )
        else:
            with reader.temp_offset(submesh_struct.vertex_array_headers_offset_1):
                array_headers = cls.read_array_headers(reader)
                if len(array_headers) == 0:
                    raise ValueError("No vertex arrays found at first array header offset in submesh.")
                for header in array_headers[1:]:
                    if header.array_length != 0:
                        raise ValueError("Multiple non-empty vertex arrays found in submesh, but only one expected.")
            array_header = array_headers[0]

        if submesh_struct.vertex_array_headers_offset_2 != 0:
            # We expect no arrays here.
            with reader.temp_offset(submesh_struct.vertex_array_headers_offset_2):
                array_headers = cls.read_array_headers(reader)
                if len(array_headers) > 0:
                    raise ValueError("Unexpected vertex arrays found at second array header offset in submesh.")

        # NOTE: Hacky way to determine UV factor.
        uv_factor = 1024 if reader.default_byte_order == ByteOrder.BigEndian else 2048
        vertex_array = VertexArray.from_flver_reader(
            reader, array_header, material.layouts, vertex_data_offset, uv_factor, big_endian
        )

        face_set = FaceSet(
            flags=0,  # not used in FLVER0
            triangle_strip=submesh_struct.triangle_strip,
            use_backface_culling=submesh_struct.use_backface_culling,
            unk_x06=0,  # not used in FLVER0
            vertex_indices=np.array(vertex_indices, dtype=np.uint32),
        )

        return cls(
            dynamic=submesh_struct.dynamic,
            material=material,
            default_bone_index=submesh_struct.default_bone_index,
            bone_indices=np.array(submesh_struct.bone_indices),
            unk_x46=submesh_struct.unk_x46,
            vertex_arrays=[vertex_array],
            face_sets=[face_set],
        )

    def to_flver_writer(self, writer: BinaryWriter, vertex_index_size: int, material_index: int):
        """Materials already collected FLVER-wide and indexed passed in here."""
        if len(self.vertex_arrays) != 1:
            raise ValueError("`FLVER0` Submesh must have exactly one VertexArray.")
        if len(self.face_sets) != 1:
            raise ValueError("`FLVER0` Submesh must have exactly one FaceSet.")
        face_set = self.face_sets[0]
        if face_set.flags != 0:
            _LOGGER.warning(f"FaceSet flags are not used in FLVER0. Non-zero flags {face_set.flags} ignored.")
        if face_set.unk_x06 != 0:
            _LOGGER.warning(f"FaceSet unk_x06 is not used in FLVER0. Non-zero value {face_set.unk_x06} ignored.")

        vertex_array = self.vertex_arrays[0]
        vertex_count = len(vertex_array.array)
        vertex_index_count = len(face_set.vertex_indices)
        vertex_array_data_size = vertex_array.layout.get_total_data_size() * vertex_count

        submesh_struct = self.STRUCT(
            dynamic=self.dynamic,
            material_index=material_index,
            use_backface_culling=face_set.use_backface_culling,
            triangle_strip=face_set.triangle_strip,
            vertex_index_count=vertex_index_count,
            vertex_count=vertex_count,
            default_bone_index=self.default_bone_index,
            bone_indices=self.bone_indices,
            unk_x46=self.unk_x46,
            _vertex_indices_length=(vertex_index_size // 8) * vertex_index_count,
            vertex_indices_offset=RESERVED,
            vertex_array_data_size=vertex_array_data_size,
            vertex_array_data_offset=RESERVED,
            vertex_array_headers_offset_1=RESERVED,
            vertex_array_headers_offset_2=0,  # second header list never written
        )
        submesh_struct.to_writer(writer, reserve_obj=self)

    def pack_vertex_indices(self, writer: BinaryWriter, vertex_index_size: int, vertex_indices_offset: int):
        if len(self.face_sets) != 1:
            raise ValueError("`FLVER0` Submesh must have exactly one FaceSet.")
        face_set = self.face_sets[0]
        # Submesh header `vertex_indices_offset` is relative to FLVER0 vertex data offset.
        writer.fill("vertex_indices_offset", vertex_indices_offset, obj=self)
        vertex_index_fmt = f"{len(face_set.vertex_indices)}{'H' if vertex_index_size == 16 else 'i'}"
        writer.pack(vertex_index_fmt, *face_set.vertex_indices)

    def pack_vertex_array_header(self, writer: BinaryWriter, layout_index: int):
        """We only write a single header. Returns header struct for filling data offset later."""
        if len(self.vertex_arrays) != 1:
            raise ValueError("`FLVER0` Submesh must have exactly one VertexArray.")
        writer.fill_with_position("vertex_array_headers_offset_1", obj=self)
        writer.pack("i", 1)  # array count
        writer.pack("i", writer.position + 12)  # very quick reserve/fill otherwise
        writer.pad(8)

        # Write single header.
        self.vertex_arrays[0].to_flver_writer(writer, layout_index)

    @classmethod
    def read_array_headers(cls, reader: BinaryReader) -> list[VertexArrayHeaderStruct]:
        """Array pre-header struct: 'ii8x'"""
        array_count = reader["i"]
        arrays_offset = reader["i"]
        reader.assert_pad(8)
        with reader.temp_offset(arrays_offset):  # offset should be right here anyway
            array_headers = []
            for _ in range(array_count):
                array_headers.append(VertexArrayHeaderStruct.from_bytes(reader))
        return array_headers

    def draw(
        self,
        vertex_color="red",
        show_normals=True,
        show_faces=False,
        show_origin=False,
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
        if show_faces:
            from mpl_toolkits.mplot3d import art3d
            faces = [tri for tri in self.triangulate()]
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

    def triangulate(self, include_degenerate_faces=False):
        """Shortcut for triangulating first face set.

        `FLVER0` must pass in its vertices so that normal checks can be performed.
        """
        allow_primitive_restarts = len(self.vertices) < 0xFFFF
        return self.face_sets[0].triangulate(
            allow_primitive_restarts,
            include_degenerate_faces,
            vertices_for_flver0_normal_check=self.vertices,
        )

    def __repr__(self):
        material = indent_lines(repr(self.material))
        face_set = indent_lines(repr(self.face_sets[0]))
        lines = [
            "Submesh(",
            f"  material = {material}",
            f"  default_bone_index = {self.default_bone_index}",
            f"  bone_indices = {self.bone_indices}",
            f"  vertices = <{len(self.vertices)} vertices>",
            f"  face_set = {face_set}",
            f")",
        ]

        return "\n".join(lines)
