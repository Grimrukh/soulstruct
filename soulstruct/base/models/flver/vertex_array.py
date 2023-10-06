from __future__ import annotations

__all__ = [
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
    "VertexArrayHeaderStruct",
    "VertexArrayLayout",
    "VertexArray",
    "VertexDataSizeError",
]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

import numpy as np

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger(__name__)


class VertexDataCodec(tp.NamedTuple):
    """Holds format-dependent decompression and compression functions for a vertex data field."""
    decompress: tp.Callable
    compress: tp.Callable

    @classmethod
    def from_uv_factor(cls, uv_factor):
        return cls(
            decompress=lambda x: x / uv_factor,
            compress=lambda x: x * uv_factor,
        )


# All the different codecs (decompression/compression functions) for vertex data.
NULL_CODEC = VertexDataCodec(
    lambda x: x,
    lambda x: x,
)
INT_TO_FLOAT_127 = VertexDataCodec(
    lambda i: i / 127.0,
    lambda f: f * 127,
)
INT_TO_FLOAT_255 = VertexDataCodec(
    lambda i: i / 255.0,
    lambda f: f * 255,
)
INT_TO_FLOAT_32767 = VertexDataCodec(
    lambda i: i / 32767.0,
    lambda f: f * 32767,
)
INT_TO_FLOAT_127_SIGNED = VertexDataCodec(
    lambda i: (i - 127.0) / 127.0,
    lambda f: f * 127 + 127,
)
INT_TO_FLOAT_255_SIGNED = VertexDataCodec(
    lambda i: (i - 255.0) / 255.0,
    lambda f: f * 255 + 255,
)
INT_TO_FLOAT_32767_SIGNED = VertexDataCodec(
    lambda i: (i - 32767.0) / 32767.0,
    lambda f: f * 32767 + 32767,
)


class VertexDataFormatEnum(IntEnum):
    """Internal IDs of data storage type and exact fields."""
    Float2 = 0x01
    Float3 = 0x02
    Float4 = 0x03
    FourBytesA = 0x10
    FourBytesB = 0x11
    NormalWFirst = 0x12
    FourBytesC = 0x13
    UV = 0x15  # two shorts
    UVPair = 0x16
    ShortBoneIndices = 0x18  # only used for bone indices
    FourShortsToFloats = 0x1A
    FourShortsToFloatsB = 0x2E  # unused thus far
    FourBytesD = 0x2F
    EdgeCompressed = 0xF0  # not supported by Soulstruct

    def get_size(self):
        return VERTEX_FORMAT_ENUM_SIZES[self]

    def has_two_uvs(self):
        return self in {VertexDataFormatEnum.Float4, VertexDataFormatEnum.UVPair}

    def has_uncompressed_uvs(self):
        return self in {VertexDataFormatEnum.Float2, VertexDataFormatEnum.Float3, VertexDataFormatEnum.Float4}


VERTEX_FORMAT_ENUM_SIZES = {
    VertexDataFormatEnum.Float2: 8,
    VertexDataFormatEnum.Float3: 12,
    VertexDataFormatEnum.Float4: 16,
    VertexDataFormatEnum.FourBytesA: 4,
    VertexDataFormatEnum.FourBytesB: 4,
    VertexDataFormatEnum.NormalWFirst: 8,
    VertexDataFormatEnum.FourBytesC: 4,
    VertexDataFormatEnum.UV: 4,
    VertexDataFormatEnum.UVPair: 8,
    VertexDataFormatEnum.ShortBoneIndices: 8,
    VertexDataFormatEnum.FourShortsToFloats: 8,
    VertexDataFormatEnum.FourShortsToFloatsB: 8,
    VertexDataFormatEnum.FourBytesD: 4,
    VertexDataFormatEnum.EdgeCompressed: 1,
}


@dataclass(slots=True, frozen=True)
class VertexDataFormat:
    """Represents the format of a single vertex data field, including its compression/decompression codec.

    Each vertex data field is generally multi-dimensional, but the exact dimensions may also vary with format.

    NOTE: Names in fields of `compressed_dtype` and `decompressed_type` may contain '{i}' and '{j}' templates to be
    set by the caller when retrieved for array-wide dtype construction (to support multiple UV and color fields).
    """

    compressed_dtype: list[tuple[str, str, tuple[int]]]  # NumPy dtype fields (usually just one)
    decompressed_dtype: list[tuple[str, str, tuple[int]]] = None  # defaults to same as `compressed_dtype`

    # Codec can be a single pair of functions (for compression and decompression, respectively) or a tuple of codecs
    # matching the number of fields in the dtypes. Defaults to no codec (data is not compressed).
    codec: VertexDataCodec | tuple[VertexDataCodec, ...] = NULL_CODEC

    def __post_init__(self):
        if self.decompressed_dtype is None:
            object.__setattr__(self, "decompressed_dtype", self.compressed_dtype)
        if isinstance(self.codec, VertexDataCodec):
            object.__setattr__(self, "codec", (self.codec,) * len(self.compressed_dtype))
        elif len(self.codec) != len(self.compressed_dtype):
            raise ValueError(
                f"Number of codecs ({len(self.codec)}) does not match number of "
                f"dtype fields ({len(self.compressed_dtype)})."
            )

    def get_indexed_compressed_dtype(self, i: int = None, j: int = None) -> list[tuple[str, str, tuple[int]]]:
        """Get the compressed dtype with '{i}' and/or '{j}' templates filled in."""
        return [(name.format(i=i, j=j), dtype, size) for name, dtype, size in self.compressed_dtype]

    def get_indexed_decompressed_dtype(self, i: int = None, j: int = None) -> list[tuple[str, str, tuple[int]]]:
        """Get the decompressed dtype with '{i}' and/or '{j}' templates filled in."""
        return [(name.format(i=i, j=j), dtype, size) for name, dtype, size in self.decompressed_dtype]


@dataclass(slots=True)
class VertexDataType(abc.ABC):
    """Information about a vertex data type."""

    # Subtype class variables.
    type_int: tp.ClassVar[int]  # value of the `_data_type` field in `VertexDataTypeStruct`
    unique: tp.ClassVar[bool] = False
    formats: tp.ClassVar[dict[tuple[int, ...], VertexDataFormat]]  # maps `data_type` IDs to their `dtype` fields/codec

    # Used to look up fields and codecs in class `FORMATS`.
    format_enum: VertexDataFormatEnum
    # Instance count of this data type in its layout.
    instance_index: int = 0
    # Unknown field that seems to always be zero.
    unk_x00: int = 0
    # Offset of this type's data in the vertex array it describes. Optional, as data is tightly packed anyway.
    data_offset: int | None = None

    def __init__(self, format_enum: VertexDataFormatEnum, instance_index=0, unk_x00=0, data_offset=0):
        self.format_enum = format_enum
        self.instance_index = instance_index
        self.unk_x00 = unk_x00
        self.data_offset = data_offset

    def __repr__(self):
        suffix = f" (unk_x00 = {self.unk_x00})" if self.unk_x00 != 0 else ""
        name = self.__class__.__name__
        if self.instance_index > 0:
            return f"{name}({self.instance_index})<{self.size}, {self.format_enum.name}>{suffix}"
        return f"{name}<{self.size}, {self.format_enum.name}>{suffix}"

    def get_format(self) -> VertexDataFormat:
        """Get the `VertexDataFormat` for this data type's `format_enum`."""
        for enum_keys, vertex_data_format in self.formats.items():
            # Dictionaries have multiple keys to save the need to copy the same format over and over.
            # TODO: Could post-modify classes to expand these keys, but this won't run very often anyway.
            if self.format_enum.value in enum_keys:
                return vertex_data_format
        raise ValueError(
            f"Vertex data format '{self.format_enum.name}' ({self.format_enum.value}) "
            f"unsupported for type '{self.__class__.__name__}'."
        )

    @property
    def size(self) -> int:
        return VERTEX_FORMAT_ENUM_SIZES[self.format_enum]


@dataclass(slots=True, init=False, repr=False)
class VertexPosition(VertexDataType):
    type_int = 0
    formats = {
        (0x02,): VertexDataFormat(
            compressed_dtype=[("position", "f", (3,))],
        ),
        (0x03,): VertexDataFormat(
            compressed_dtype=[("position", "f", (4,))],
        ),
    }


@dataclass(slots=True, init=False, repr=False)
class VertexBoneWeights(VertexDataType):
    type_int = 1
    unique = True
    formats = {
        (0x13,): VertexDataFormat(
            compressed_dtype=[("bone_weights", "b", (4,))],
            decompressed_dtype=[("bone_weights", "f", (4,))],
            codec=INT_TO_FLOAT_127,
        ),
        (0x14,): VertexDataFormat(
            compressed_dtype=[("bone_weights", "B", (4,))],
            decompressed_dtype=[("bone_weights", "f", (4,))],
            codec=INT_TO_FLOAT_127,
        ),
        (0x16, 0x1A): VertexDataFormat(
            compressed_dtype=[("bone_weights", "h", (4,))],
            decompressed_dtype=[("bone_weights", "f", (4,))],
            codec=INT_TO_FLOAT_32767,
        ),
    }


@dataclass(slots=True, init=False, repr=False)
class VertexBoneIndices(VertexDataType):
    """Bones to which the vertex is attached.

    Indices may refer to other actual FLVER skeleton bone indices in `Submesh.bone_indices` (older games) or may just be
    FLVER skeleton bone indices themselves.

    Usage differs between rigged models (`Submesh.is_bind_pose=True`) and non-rigged models. For rigged models, up to
    four different bone indices may be used, with their own weights, as usual. But for non-rigged models, like map
    pieces, only one bone index is used (repeated four times), and is used to simply offset the vertex (usually the same
    for the whole submesh).

    Either way, EVERY vertex has at least one bone index.

    Note that unused bone indices are typically 0, not -1. Actual use of bone index 0 is therefore dependent on non-zero
    bone weights for character models.
    """
    type_int = 2
    unique = True
    formats = {
        (0x11, 0x2F): VertexDataFormat(
            compressed_dtype=[("bone_indices", "B", (4,))],
            decompressed_dtype=[("bone_indices", "i", (4,))],
            # No codec needed; just an integer size change.
        ),
        (0x18,): VertexDataFormat(
            compressed_dtype=[("bone_indices", "h", (4,))],
            decompressed_dtype=[("bone_indices", "i", (4,))],
            # No codec needed; just an integer size change.
        ),
    }


@dataclass(slots=True, init=False, repr=False)
class VertexNormal(VertexDataType):
    """Vertex normal.

    When 4D, the fourth `normal_w` component is sometimes used as a bone index, I believe. Otherwise, it seems to be
    always 127; it is never converted to a float here, regardless of its integer format.
    """
    type_int = 3
    formats = {
        (0x03,): VertexDataFormat(
            compressed_dtype=[("normal", "f", (3,))],  # only format with no `normal_w` field
        ),
        (0x04,): VertexDataFormat(
            compressed_dtype=[("normal", "f", (3,)), ("normal_w", "i", (1,))],
        ),
        (0x10, 0x11, 0x13, 0x2F): VertexDataFormat(
            compressed_dtype=[("normal", "B", (3,)), ("normal_w", "B", (1,))],
            decompressed_dtype=[("normal", "f", (3,)), ("normal_w", "B", (1,))],
            codec=(INT_TO_FLOAT_127_SIGNED, NULL_CODEC),
        ),
        (0x12,): VertexDataFormat(
            compressed_dtype=[("normal_w", "B", (1,)), ("normal", "b", (3,))],
            decompressed_dtype=[("normal_w", "B", (1,)), ("normal", "f", (3,))],
            codec=(NULL_CODEC, INT_TO_FLOAT_127_SIGNED),
        ),
        (0x1A,): VertexDataFormat(
            compressed_dtype=[("normal", "h", (3,)), ("normal_w", "h", (1,))],
            decompressed_dtype=[("normal", "f", (3,)), ("normal_w", "h", (1,))],
            codec=(INT_TO_FLOAT_32767_SIGNED, NULL_CODEC),
        ),
        (0x2E,): VertexDataFormat(
            compressed_dtype=[("normal", "H", (3,)), ("normal_w", "h", (1,))],
            decompressed_dtype=[("normal", "f", (3,)), ("normal_w", "h", (1,))],
            codec=(INT_TO_FLOAT_32767_SIGNED, NULL_CODEC),
        ),
    }


@dataclass(slots=True, init=False, repr=False)
class VertexUV(VertexDataType):
    """Texture coordinates.

    NOTE: Some UV FORMATS contain a pair of coordinates. Indices are added for each UV slot when generated.

    All non-float UV formats will also be de-quantized using `uv_factor` from the FLVER header.
    """

    type_int = 5
    formats = {
        (0x01,): VertexDataFormat(
            compressed_dtype=[("uv_{i}", "f", (2,))],
        ),
        (0x02,): VertexDataFormat(
            compressed_dtype=[("uv_{i}", "f", (3,))],  # NOTE: no idea which games/models use `uv[2]` or what it does
        ),
        (0x03,): VertexDataFormat(
            compressed_dtype=[("uv_{i}", "f", (2,)), ("uv_{j}", "f", (2,))],
        ),
        (0x10, 0x11, 0x12, 0x13, 0x15): VertexDataFormat(
            compressed_dtype=[("uv_{i}", "h", (2,))],
            decompressed_dtype=[("uv_{i}", "f", (2,))],
            # Codec handled externally.
        ),
        (0x16,): VertexDataFormat(
            compressed_dtype=[("uv_{i}", "h", (2,)), ("uv_{j}", "h", (2,))],
            decompressed_dtype=[("uv_{i}", "f", (2,)), ("uv_{j}", "f", (2,))],
            # Codec handled externally.
        ),
        (0x1A,): VertexDataFormat(
            compressed_dtype=[("uv_{i}", "h", (4,))],  # NOTE: `uv[2]` for unknown use; `uv[3]` always zero
            decompressed_dtype=[("uv_{i}", "f", (4,))],
            # Codec handled externally.
        ),
    }


@dataclass(slots=True, init=False, repr=False)
class VertexTangent(VertexDataType):
    """Perpendicular to normal."""

    type_int = 6
    formats = {
        (0x03,): VertexDataFormat(
            compressed_dtype=[("tangent_x", "f", (3,))],
        ),
        (0x10, 0x11, 0x13, 0x1A, 0x2F): VertexDataFormat(
            compressed_dtype=[("tangent", "B", (4,))],
            decompressed_dtype=[("tangent", "f", (4,))],
            codec=INT_TO_FLOAT_127_SIGNED,
        ),
    }


@dataclass(slots=True, init=False, repr=False)
class VertexBitangent(VertexDataType):
    """Pendicular to both normal and tangent. Generally only used by multi-texture materials."""

    type_int = 7
    unique = True
    formats = {
        (0x10, 0x11, 0x13, 0x2F): VertexDataFormat(
            compressed_dtype=[("bitangent", "B", (4,))],
            decompressed_dtype=[("bitangent", "f", (4,))],
            codec=INT_TO_FLOAT_127_SIGNED,
        ),
    }


@dataclass(slots=True, init=False, repr=False)
class VertexColor(VertexDataType):
    """Used to blend between two textures slots for '[M]' MTD materials, and for alpha for '_Alpha' and '_Edge'.

    Have not yet encountered multiple colors, but it is supported and probably used in later games.
    """

    type_int = 10
    formats = {
        (0x03,): VertexDataFormat(
            compressed_dtype=[("color_{i}", "f", (4,))],
        ),
        (0x10, 0x13): VertexDataFormat(
            compressed_dtype=[("color_{i}", "B", (4,))],
            decompressed_dtype=[("color_{i}", "f", (4,))],
            codec=INT_TO_FLOAT_255,
        ),
    }


# Data type subclass lookup.
VERTEX_DATA_TYPES = {
    VertexPosition.type_int: VertexPosition,
    VertexBoneWeights.type_int: VertexBoneWeights,
    VertexBoneIndices.type_int: VertexBoneIndices,
    VertexNormal.type_int: VertexNormal,
    VertexUV.type_int: VertexUV,
    VertexTangent.type_int: VertexTangent,
    VertexBitangent.type_int: VertexBitangent,
    VertexColor.type_int: VertexColor,
}  # type: dict[int, tp.Type[VertexDataType]]


@dataclass(slots=True)
class VertexDataTypeStruct(BinaryStruct):

    unk_x00: int
    data_offset: int  # offset of data type's data in described array
    format_enum: VertexDataFormatEnum = field(**Binary(int))
    _type_int: int
    instance_index: int  # instance index of this data type in its layout


@dataclass(slots=True)
class VertexArrayHeaderStruct(BinaryStruct):
    """Header information about a packed FLVER vertex data array, which we read into a NumPy structured array."""
    array_index: int
    layout_index: int
    vertex_size: int
    vertex_count: int
    _pad1: bytes = field(init=False, **BinaryPad(8))
    array_length: int
    array_offset: int


class VertexDataSizeError(SoulstructError):
    """Raised by some vanilla meshes."""

    def __init__(self, vertex_size: int, layout_size: int):
        self.vertex_size = vertex_size
        self.layout_size = layout_size
        super().__init__(
            f"Vertex array vertex size {vertex_size} not equal to size calculated from layout: {layout_size}."
        )


@dataclass(slots=True)
class LayoutStruct(BinaryStruct):
    layout_types_count: int
    pad1: bytes = field(init=False, **BinaryPad(8))
    layout_types_offset: int


class VertexArrayLayout(list[VertexDataType]):
    """List of `VertexDataType` instances that describes a vertex array layout.

    Functions as a standard list, with extra methods for constructing combined `np.dtype` and reading/packing arrays.
    """

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader) -> VertexArrayLayout:
        """Read a FLVER vertex array layout into a list of `VertexDataType` instances.

        Each instance's subclass indicates its data type, and its `format_enum` value indicates its exact fields and
        which codec to use for compression/decompression.
        """
        array_layout_struct = LayoutStruct.from_bytes(reader)

        with reader.temp_offset(array_layout_struct.layout_types_offset):
            tight_data_offset = 0
            data_types = []
            for _ in range(array_layout_struct.layout_types_count):
                data_type_struct = VertexDataTypeStruct.from_bytes(reader)

                if data_type_struct.data_offset != tight_data_offset:
                    _LOGGER.warning(
                        f"Vertex data type offset {data_type_struct.data_offset} does not match expected offset "
                        f"{tight_data_offset}."
                    )

                data_type_cls = VERTEX_DATA_TYPES[data_type_struct.pop("_type_int")]
                data_type = data_type_struct.to_object(data_type_cls)
                data_types.append(data_type)
                tight_data_offset += VERTEX_FORMAT_ENUM_SIZES[data_type.format_enum]

        return cls(data_types)

    def to_flver_writer(self, writer: BinaryWriter):
        layout_struct = LayoutStruct(layout_types_count=len(self), layout_types_offset=RESERVED)
        layout_struct.to_writer(writer, reserve_obj=self)
        return layout_struct

    def pack_layout_types(self, writer: BinaryWriter):
        """Write actual layout data type information and fill header offset field."""
        writer.fill_with_position("layout_types_offset", obj=self)
        data_type_offset = 0
        for data_type in self:
            VertexDataTypeStruct.object_to_writer(
                data_type,
                writer,
                data_offset=data_type_offset,
                _type_int=data_type.type_int,
            )
            data_type_offset += data_type.size

    def unpack_vertex_array(self, data: bytes, uv_factor: int) -> np.ndarray:
        """Use this layout to read a structured array of vertex data from the given raw FLVER array data."""
        compressed_dtype, decompressed_dtype = self.get_dtypes()
        codecs = self.get_codecs(uv_factor=uv_factor)

        compressed_array = np.frombuffer(data, dtype=compressed_dtype)
        decompressed_array = np.empty(len(compressed_array), dtype=decompressed_dtype)
        for codec, (name, dtype) in zip(codecs, decompressed_dtype.fields.items()):
            # NOTE: Very important to cast array to decompressed dtype FIRST, before decompressing.
            compressed_subarray = compressed_array[name].astype(dtype[0].base)
            decompressed_array[name] = codec.decompress(compressed_subarray)
        return decompressed_array

    def pack_vertex_array(self, array: np.ndarray, uv_factor: int) -> bytes:
        """Use this layout to pack a structured array of vertex data into raw FLVER array data."""
        compressed_dtype, decompressed_dtype = self.get_dtypes()
        codecs = self.get_codecs(uv_factor=uv_factor)

        compressed_array = np.empty(len(array), dtype=compressed_dtype)
        for codec, (name, dtype) in zip(codecs, compressed_dtype.fields.items()):
            # NOTE: Very important to compress FIRST, before casting array to the compressed dtype.
            compressed_subarray = codec.compress(array[name])
            compressed_array[name] = compressed_subarray.astype(dtype[0].base)
        return compressed_array.tobytes()

    def get_dtypes(self) -> tuple[np.dtype, np.dtype]:
        """Get compressed and decompressed NumPy dtypes for this layout."""
        compressed_dtype = []  # type: list[tuple[str, str, int]]
        decompressed_dtype = []  # type: list[tuple[str, str, int]]
        uv_index = 0
        color_index = 0

        for data_type in self:
            if data_type.format_enum == VertexDataFormatEnum.EdgeCompressed:
                # Explicitly not implemented yet.
                raise NotImplementedError("Cannot yet read FLVERs with edge-compressed vertex data. Sorry!")

            # Find format. Will raise a `ValueError` here if not supported.
            vertex_data_format = data_type.get_format()

            if isinstance(data_type, VertexUV):
                compressed_dtype += vertex_data_format.get_indexed_compressed_dtype(i=uv_index, j=uv_index + 1)
                decompressed_dtype += vertex_data_format.get_indexed_decompressed_dtype(i=uv_index, j=uv_index + 1)
                uv_index += 2 if data_type.format_enum.has_two_uvs() else 1
            elif isinstance(data_type, VertexColor):
                compressed_dtype += vertex_data_format.get_indexed_compressed_dtype(i=color_index)
                decompressed_dtype += vertex_data_format.get_indexed_decompressed_dtype(i=color_index)
                color_index += 1
            else:
                compressed_dtype += vertex_data_format.get_indexed_compressed_dtype()
                decompressed_dtype += vertex_data_format.get_indexed_decompressed_dtype()

        return np.dtype(compressed_dtype), np.dtype(decompressed_dtype)

    def get_codecs(self, uv_factor: int = None) -> list[VertexDataCodec]:
        """Get list of codecs with compression/decompression functions for every field (not just broad data type) in
        this layout."""
        codecs = []

        for data_type in self:
            if data_type.format_enum == VertexDataFormatEnum.EdgeCompressed:
                # Explicitly not implemented yet.
                raise NotImplementedError("Cannot yet read FLVERs with edge-compressed vertex data. Sorry!")

            # Find format. Will raise a `ValueError` here if not supported.
            vertex_data_format = data_type.get_format()
            field_count = len(vertex_data_format.compressed_dtype)

            if isinstance(data_type, VertexUV) and not data_type.format_enum.has_uncompressed_uvs():
                # Bake `uv_factor` into decompression.
                codecs += [VertexDataCodec.from_uv_factor(uv_factor)] * field_count
            else:
                codecs += list(vertex_data_format.codec)

        return codecs

    def get_total_data_size(self) -> int:
        return sum(data_type.size for data_type in self)

    def __repr__(self):
        data_types = ",\n    ".join(repr(data_type) for data_type in self)
        return (
            f"VertexArrayLayout(\n"
            f"    {data_types},\n"
            f") <size={self.get_total_data_size()}>"
        )


@dataclass(slots=True)
class VertexArray:
    """Wraps a structured NumPy array containing vertex data for a particular FLVER submesh."""

    array: np.ndarray
    layout: VertexArrayLayout

    @classmethod
    def from_flver_reader(
        cls,
        flver_reader: BinaryReader,
        array_header: VertexArrayHeaderStruct,
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
            array = layout.unpack_vertex_array(array_data, uv_factor)

        return cls(array, layout)

    def to_flver_writer(
        self,
        writer: BinaryWriter,
        write_array_length: bool,
        layout_index: int,
        array_index: int,
    ):
        """Note that `layout_index` will be into a merged FLVER-wide list."""
        layout_size = self.layout.get_total_data_size()
        vertex_count = len(self.array)
        VertexArrayHeaderStruct.object_to_writer(
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
        writer.fill("array_offset", array_offset, obj=self)
        writer.append(self.layout.pack_vertex_array(self.array, uv_factor))

    def __getitem__(self, key):
        """Wraps NumPy array indexing."""
        return self.array[key]

    def __setitem__(self, key, value):
        """Wraps NumPy array indexing."""
        self.array[key] = value

    def __len__(self):
        """Wraps NumPy array length."""
        return len(self.array)
