from __future__ import annotations

__all__ = [
    "VertexArray",
]

import logging
from dataclasses import dataclass, field

import numpy as np

from soulstruct.utilities.binary import *
from soulstruct.base.models.flver.vertex_array import BaseVertexArray
from .vertex_array_layout import VertexArrayLayout

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class VertexArrayHeaderStruct(BinaryStruct):
    """Header information about a packed FLVER vertex data array, which we read into a NumPy structured array.

    NOT stored inside `VertexArray` class, as FLVER classes unpack these first and use them to read arrays later.
    """
    layout_index: int  # index into layouts of submesh's material, rather than global FLVER layouts
    array_length: int
    array_offset: int
    _pad0: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True)
class VertexArray(BaseVertexArray[VertexArrayLayout]):
    """Wraps a structured NumPy array containing vertex data for a particular FLVER submesh.

    Simpler for `FLVER0`.
    """

    array: np.ndarray
    layout: VertexArrayLayout

    @classmethod
    def from_flver_reader(
        cls,
        flver_reader: BinaryReader,
        array_header: VertexArrayHeaderStruct,
        layouts: list[VertexArrayLayout],
        vertex_data_offset: int,  # from `FLVER0` header
        uv_factor: int,
    ):
        layout = layouts[array_header.layout_index]
        with flver_reader.temp_offset(vertex_data_offset + array_header.array_offset):
            array_data = flver_reader.read(array_header.array_length)
            array = layout.unpack_vertex_array(array_data, uv_factor)

        return cls(array, layout)

    def to_flver_writer(
        self,
        writer: BinaryWriter,
        layout_index: int,
    ):
        """Note that `layout_index` will be into a merged FLVER-wide list."""
        layout_size = self.layout.get_total_data_size()
        vertex_count = len(self.array)
        VertexArrayHeaderStruct.object_to_writer(
            self,
            writer,
            layout_index=layout_index,
            array_length=layout_size * vertex_count,
            array_offset=RESERVED,
        )

    def pack_array(
        self,
        writer: BinaryWriter,
        array_offset: int,
        uv_factor: int,
    ):
        writer.fill("array_offset", array_offset, obj=self)
        writer.append(self.layout.pack_vertex_array(self.array, uv_factor))
