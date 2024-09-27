from __future__ import annotations

__all__ = [
    "VertexArrayLayout",
    "VertexDataCodec",
    "VERTEX_DATA_TYPES",
    "VERTEX_FORMAT_ENUM_SIZES",
    "VertexDataFormatEnum",
    "VertexDataType",
    "VertexPosition",
    "VertexBoneWeights",
    "VertexBoneIndices",
    "VertexNormal",
    "VertexUV",
    "VertexTangent",
    "VertexBitangent",
    "VertexColor",
]

import logging
from dataclasses import dataclass, field

from soulstruct.base.models.base.vertex_array_layout import *
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger("soulstruct")


class VertexArrayLayout(BaseVertexArrayLayout):
    """List of `VertexDataType` instances that describes a vertex array layout.

    Functions as a standard list, with extra methods for constructing combined `np.dtype` and reading/packing arrays.

    Very similar to modern `FLVER` but stores the data types right after the header rather than at a new FLVER offset.
    """

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):
        layout_types_count: short
        struct_size: short
        _pad0: bytes = field(init=False, **BinaryPad(12))

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader) -> VertexArrayLayout:
        """Read a FLVER vertex array layout into a list of `VertexDataType` instances.

        Each instance's subclass indicates its data type, and its `format_enum` value indicates its exact fields and
        which codec to use for compression/decompression.
        """
        layout_struct = cls.STRUCT.from_bytes(reader)

        tight_data_offset = 0
        data_types = []
        for _ in range(layout_struct.layout_types_count):
            data_type_struct = VertexDataType.STRUCT.from_bytes(reader)

            if data_type_struct.data_offset != tight_data_offset:
                _LOGGER.warning(
                    f"Vertex data type offset {data_type_struct.data_offset} does not match expected offset "
                    f"{tight_data_offset}."
                )

            data_type_cls = VERTEX_DATA_TYPES[data_type_struct.pop("_type_int")]
            data_type = data_type_struct.to_object(data_type_cls)
            data_types.append(data_type)
            tight_data_offset += VERTEX_FORMAT_ENUM_SIZES[data_type.format_enum]

        if tight_data_offset != layout_struct.struct_size:
            _LOGGER.warning(
                f"Total vertex data type size {tight_data_offset} does not match expected size "
                f"{layout_struct.struct_size}."
            )

        return cls(data_types, byte_order=reader.default_byte_order)

    def to_flver_writer(self, writer: BinaryWriter):
        """Data is written here as well."""
        layout_struct = self.STRUCT(layout_types_count=len(self), struct_size=self.get_total_data_size())
        layout_struct.to_writer(writer, reserve_obj=self)
        data_type_offset = 0
        for data_type in self:
            VertexDataType.STRUCT.object_to_writer(
                data_type,
                writer,
                data_offset=data_type_offset,
                _type_int=data_type.type_int,
            )
            data_type_offset += data_type.size
        return layout_struct  # not needed

    def pack_layout_types(self, writer: BinaryWriter):
        """Write actual layout data type information and fill header offset field."""
        raise TypeError("This method is not used in the old FLVER format.")

    # All other methods inherited.
