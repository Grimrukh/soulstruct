from __future__ import annotations

__all__ = [
    "VertexArray",
]

import logging
from dataclasses import dataclass, field

import numpy as np

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import *
from .vertex_array_layout import VertexArrayLayout

_LOGGER = logging.getLogger("soulstruct")

KNOWN_CORRUPTED_DS1R_ARRAYS = {
    "m0208B0A14": b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                  b'goz\xc3\x7fY\xf9\xff\x7fY\xf9\xff\x00\x00\x00\x00',
    "m0302B0A14": b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                  b'\xde\xd1?\xc3\x7f1\x1a\xff\x7f1\x1a\xff\x00\x00\x00\x00'
}


class VertexDataSizeError(SoulstructError):
    """Vertex array/layout size mismatch. Raised by some genuinely corrupted vanilla meshes in DSR."""

    def __init__(self, vertex_size: int, layout_size: int):
        self.vertex_size = vertex_size
        self.layout_size = layout_size
        super().__init__(
            f"Vertex array vertex size {vertex_size} not equal to size calculated from layout: {layout_size}."
        )


@dataclass(slots=True)
class VertexArray:
    """Wraps a structured NumPy array containing vertex data for a particular FLVER mesh."""

    @dataclass(slots=True)
    class HEADER0(BinaryStruct):
        """Header information about a packed FLVER0 vertex data array, which we read into a NumPy structured array."""
        layout_index: int  # index into layouts of mesh's material, rather than global FLVER layouts
        array_length: int
        array_offset: int
        _pad0: bytes = field(init=False, **BinaryPad(4))

    @dataclass(slots=True)
    class HEADER2(BinaryStruct):
        """Header information about a packed FLVER2 vertex data array, which we read into a NumPy structured array."""
        array_index: int
        layout_index: int
        vertex_size: int
        vertex_count: int
        _pad1: bytes = field(init=False, **BinaryPad(8))
        array_length: int
        array_offset: int

    array: np.ndarray
    layout: VertexArrayLayout

    @classmethod
    def from_flver0_reader(
        cls,
        flver_reader: BinaryReader,
        array_header: HEADER0,
        layouts: list[VertexArrayLayout],
        vertex_data_offset: int,  # from `FLVER0` header
        uv_factor: int,
    ):
        layout = layouts[array_header.layout_index]
        with flver_reader.temp_offset(vertex_data_offset + array_header.array_offset):
            array_data = flver_reader.read(array_header.array_length)
            array = layout.unpack_vertex_array(array_data, uv_factor)

        return cls(array, layout)

    @classmethod
    def from_flver2_reader(
        cls,
        flver_reader: BinaryReader,
        array_header: HEADER2,
        layouts: list[VertexArrayLayout],
        vertex_data_offset: int,
        uv_factor: int,
    ):
        if array_header.vertex_size != array_header.array_length / array_header.vertex_count:
            _LOGGER.warning(
                f"FLVER vertex array has vertex size {array_header.vertex_size}, but has total array length "
                f"{array_header.array_length} and vertex count {array_header.vertex_count}. Buffer length ignored."
            )

        layout = layouts[array_header.layout_index]
        layout_size = layout.get_total_data_size()
        if layout_size != array_header.vertex_size:
            # TODO: This happens in vanilla DSR FLVERs. I try to fix it ahead of time by studying material MTD names,
            #  but if we reach here, that hasn't worked. Causes seem to be missing or unexpected tangents/bitangents.
            raise VertexDataSizeError(array_header.vertex_size, layout_size)

        with flver_reader.temp_offset(vertex_data_offset + array_header.array_offset):
            array_data = flver_reader.read(array_header.array_length)
            for corrupted_key, corrupted_start in KNOWN_CORRUPTED_DS1R_ARRAYS.items():
                if array_data[:32] == corrupted_start:
                    _LOGGER.warning(
                        f"FLVER vertex array data appears to be a known corrupted case from DS1R (Map Piece "
                        f"{corrupted_key}). You may want to replace its vertex data from the same model in PTDE!"
                    )
            array = layout.unpack_vertex_array(array_data, uv_factor)

        return cls(array, layout)

    @classmethod
    def read_flver0_header_list(cls, reader: BinaryReader) -> list[HEADER0]:
        """Read array list 'ii8x' struct and read the appropriate number of `HEADER0` structs."""
        array_count = reader["i"]
        arrays_offset = reader["i"]
        reader.assert_pad(8)
        with reader.temp_offset(arrays_offset):  # offset should be right here anyway
            array_headers = []
            for _ in range(array_count):
                array_headers.append(cls.HEADER0.from_bytes(reader))
        return array_headers

    def to_flver0_writer(
        self,
        writer: BinaryWriter,
        layout_index: int,
    ):
        """Note that `layout_index` will be into a merged FLVER-wide list."""
        layout_size = self.layout.get_total_data_size()
        vertex_count = len(self.array)
        self.HEADER0.object_to_writer(
            self,
            writer,
            layout_index=layout_index,
            array_length=layout_size * vertex_count,
            array_offset=RESERVED,
        )

    def to_flver2_writer(
        self,
        writer: BinaryWriter,
        write_array_length: bool,
        layout_index: int,
        array_index: int,
    ):
        """Note that `layout_index` will be into a merged FLVER-wide list."""
        layout_size = self.layout.get_total_data_size()
        vertex_count = len(self.array)
        self.HEADER2.object_to_writer(
            self,
            writer,
            array_index=array_index,
            layout_index=layout_index,
            vertex_size=layout_size,
            vertex_count=vertex_count,
            array_length=layout_size * vertex_count if write_array_length else 0,
            array_offset=RESERVED,
        )

    def pack_array(
        self,
        writer: BinaryWriter,
        array_offset: int,
        uv_factor: int,
    ):
        """Identical for FLVER0 and FLVER2 versions."""
        writer.fill("array_offset", array_offset, obj=self)
        writer.append(self.layout.pack_vertex_array(self.array, uv_factor))

    # region Vertex Array Methods

    def has_field(self, name: str) -> bool:
        return name in self.array.dtype.names

    @property
    def dtype(self) -> np.dtype:
        """Wraps NumPy array dtype."""
        return self.array.dtype

    @property
    def guess_has_normal_w_bone_indices(self):
        """Just checks if ANY `normal_w` values are not 127 and not 0."""
        if "bone_indices" in self.array.dtype.names:
            return False  # has REAL bone indices
        if "normal_w" not in self.array.dtype.names:
            return False
        # Check if any normal_w values are not 127 and not 0.
        return np.any((self.array["normal_w"] != 127) & (self.array["normal_w"] != 0))

    def __getitem__(self, key):
        """Wraps NumPy array indexing."""
        return self.array[key]

    def __setitem__(self, key, value):
        """Wraps NumPy array indexing."""
        self.array[key] = value

    def __len__(self):
        """Wraps NumPy array length."""
        return len(self.array)

    # endregion
