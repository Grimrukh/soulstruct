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
    "VertexBufferStruct",
    "VertexDataLayout",
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
    decompress_func: tp.Callable
    compress_func: tp.Callable


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


class VertexDataFormat(tp.NamedTuple):

    names: tuple[str, ...]
    compressed_format: str
    decompressed_format: str = None  # defaults to same as `compressed_format`

    # Codec can be a single pair of functions (for both compression and decompression) or a tuple of codecs matching
    # the number of `names` (for different codecs for each name). Defaults to no codec (data is not compressed).
    codec: VertexDataCodec | tuple[VertexDataCodec, ...] = NULL_CODEC

    def get_dtype_fields(self, compressed: bool, index: int = None, second_index: int = None) -> list[tuple[str, str]]:
        """Get NumPy dtype for this format, as it appears in the compressed FLVER buffer data.

        If `index` is given, the field names will be suffixed with the index (e.g. `uv_u_0`). If `second_index` is also
        given and there are four fields, the second two fields will be suffixed with the second index instead of the
        first (e.g. for `Float4` or `UVPair` UV data).
        """
        if index is not None:
            if second_index is not None and len(self.names) == 4:
                field_names = [f"{name}_{index}" for name in self.names[:2]]
                field_names += [f"{name}_{second_index}" for name in self.names[2:]]
            else:
                if second_index is not None:
                    _LOGGER.warning(
                        f"`second_index` was given for vertex data format with {len(self.names)} fields, rather than 4."
                    )
                field_names = [f"{name}_{index}" for name in self.names]
        else:
            if second_index is not None:
                _LOGGER.warning("`second_index` was given for vertex data format without `index`.")
            field_names = self.names

        field_formats = self.compressed_format if compressed else self.decompressed_format

        return [(field_name, field_format) for field_name, field_format in zip(field_names, field_formats)]


@dataclass(slots=True)
class VertexDataType(abc.ABC):
    """Information about a vertex data type."""

    # Subtype class variables.
    data_type: tp.ClassVar[int]  # value of the `data_type` field in `VertexDataTypeStruct`
    formats: tp.ClassVar[dict[tuple[int, ...], VertexDataFormat]]  # maps `data_type` IDs to their `dtype` fields/codec
    unique: tp.ClassVar[bool] = False

    # Used to look up fields and codecs in class `FORMATS`.
    format_enum: VertexDataFormatEnum
    # Instance count of this data type in its layout.
    instance_index: int = 0
    # Unknown field that seems to always be zero.
    unk_x00: int = 0
    # Offset of this type's data in the vertex buffer it describes. Optional, as data is tightly packed anyway.
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
        raise ValueError(f"Vertex data format '{self.format_enum}' unsupported for type '{self.__class__.__name__}'.")

    @property
    def size(self) -> int:
        return VERTEX_FORMAT_ENUM_SIZES[self.format_enum]


@dataclass(slots=True, init=False)
class VertexPosition(VertexDataType):
    data_type = 0
    formats = {
        (0x03,): VertexDataFormat(
            names=("position_x", "position_y", "position_z"),
            compressed_format="fff",
        ),
        (0x04,): VertexDataFormat(
            names=("position_x", "position_y", "position_z", "position_w"),
            compressed_format="ffff",
        ),
    }


@dataclass(slots=True, init=False)
class VertexBoneWeights(VertexDataType):
    data_type = 1
    formats = {
        (0x13,): VertexDataFormat(
            names=("bone_weight_a", "bone_weight_b", "bone_weight_c", "bone_weight_d"),
            compressed_format="bbbb",
            decompressed_format="ffff",
            codec=INT_TO_FLOAT_127,
        ),
        (0x14,): VertexDataFormat(
            names=("bone_weight_a", "bone_weight_b", "bone_weight_c", "bone_weight_d"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=INT_TO_FLOAT_127,
        ),
        (0x16, 0x1A): VertexDataFormat(
            names=("bone_weight_a", "bone_weight_b", "bone_weight_c", "bone_weight_d"),
            compressed_format="hhhh",
            decompressed_format="ffff",
            codec=INT_TO_FLOAT_32767,
        ),
    }
    unique = True


@dataclass(slots=True, init=False)
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
    data_type = 2
    formats = {
        (0x11, 0x2F): VertexDataFormat(
            names=("bone_index_a", "bone_index_b", "bone_index_c", "bone_index_d"),
            compressed_format="BBBB",
        ),
        (0x18,): VertexDataFormat(
            names=("bone_index_a", "bone_index_b", "bone_index_c", "bone_index_d"),
            compressed_format="hhhh",
        ),
    }
    unique = True


@dataclass(slots=True, init=False)
class VertexNormal(VertexDataType):
    """Vertex normal.

    When 4D, the fourth `normal_w` component is sometimes used as a bone index, I believe. Otherwise, it seems to be
    always 127; it is never converted to a float here, regardless of its integer format.
    """
    data_type = 3
    formats = {
        (0x03,): VertexDataFormat(
            names=("normal_x", "normal_y", "normal_z"),
            compressed_format="fff",
        ),
        (0x04,): VertexDataFormat(
            names=("normal_x", "normal_y", "normal_z", "normal_w"),
            compressed_format="fffi",
        ),
        (0x10, 0x11, 0x13, 0x2F): VertexDataFormat(
            names=("normal_x", "normal_y", "normal_z", "normal_w"),
            compressed_format="BBBB",
            decompressed_format="fffB",
            codec=(INT_TO_FLOAT_127_SIGNED,) * 3 + (NULL_CODEC,),
        ),
        (0x12,): VertexDataFormat(
            names=("normal_w", "normal_y", "normal_z", "normal_x"),  # W comes first
            compressed_format="Bbbb",
            decompressed_format="fffB",
            codec=(NULL_CODEC,) + (INT_TO_FLOAT_127_SIGNED,) * 3,
        ),
        (0x1A,): VertexDataFormat(
            names=("normal_x", "normal_y", "normal_z", "normal_w"),
            compressed_format="hhhh",
            decompressed_format="fffh",
            codec=(INT_TO_FLOAT_32767_SIGNED,) * 3 + (NULL_CODEC,),
        ),
        (0x2E,): VertexDataFormat(
            names=("normal_x", "normal_y", "normal_z", "normal_w"),
            compressed_format="HHHh",
            decompressed_format="fffh",
            codec=(INT_TO_FLOAT_32767_SIGNED,) * 3 + (NULL_CODEC,),
        ),
    }


@dataclass(slots=True, init=False)
class VertexUV(VertexDataType):
    """Texture coordinates.

    NOTE: Some UV FORMATS contain a pair of coordinates. Indices are added for each UV slot when generated.

    All non-float UV formats will also be de-quantized using `uv_factor` from the FLVER header.
    """

    data_type = 5
    formats = {
        (0x01,): VertexDataFormat(
            names=("uv_u", "uv_v"),
            compressed_format="ff",
        ),
        (0x02,): VertexDataFormat(
            names=("uv_u", "uv_v", "uv_w"),  # TODO: no idea which games/models use `uv_w` or what it does
            compressed_format="fff",
        ),
        (0x03,): VertexDataFormat(
            names=("uv_u", "uv_v", "uv_u", "uv_v"),
            compressed_format="ffff",
        ),
        (0x10, 0x11, 0x12, 0x13, 0x15): VertexDataFormat(
            names=("uv_u", "uv_v"),
            compressed_format="hh",
            decompressed_format="ff",
            # Codec handled externally.
        ),
        (0x16,): VertexDataFormat(
            names=("uv_u", "uv_v", "uv_u", "uv_v"),
            compressed_format="hhhh",
            decompressed_format="ffff",
            # Codec handled externally.
        ),
        (0x1A,): VertexDataFormat(
            names=("uv_u", "uv_v", "uv_w", "uv_zero"),  # fourth value is always zero
            compressed_format="hhhh",
            decompressed_format="ffff",
            # Codec handled externally.
        ),
    }


@dataclass(slots=True, init=False)
class VertexTangent(VertexDataType):
    """Perpendicular to normal."""

    data_type = 6
    formats = {
        (0x03,): VertexDataFormat(
            names=("tangent_x", "tangent_y", "tangent_z"),
            compressed_format="fff",
        ),
        (0x10, 0x11, 0x13, 0x1A, 0x2F): VertexDataFormat(
            names=("tangent_x", "tangent_y", "tangent_z", "tangent_w"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=INT_TO_FLOAT_127_SIGNED,
        ),
    }


@dataclass(slots=True, init=False)
class VertexBitangent(VertexDataType):
    """Pendicular to both normal and tangent."""

    data_type = 7
    formats = {
        (0x10, 0x11, 0x13, 0x2F): VertexDataFormat(
            names=("bitangent_x", "bitangent_y", "bitangent_z", "bitangent_w"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=INT_TO_FLOAT_127_SIGNED,
        ),
    }
    unique = True


@dataclass(slots=True, init=False)
class VertexColor(VertexDataType):
    """Used to blend between two textures slots for '[M]' MTD materials, and for alpha for '_Alpha' and '_Edge'.

    Have not yet encountered multiple colors, but it is supported and probably used in later games.
    """

    data_type = 10
    formats = {
        (0x03,): VertexDataFormat(
            names=("color_r", "color_g", "color_b", "color_a"),
            compressed_format="ffff",
        ),
        (0x10, 0x13): VertexDataFormat(
            names=("color_r", "color_g", "color_b", "color_a"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=INT_TO_FLOAT_255,
        ),
    }


# Data type subclass lookup.
VERTEX_DATA_TYPES = {
    VertexPosition.data_type: VertexPosition,
    VertexBoneWeights.data_type: VertexBoneWeights,
    VertexBoneIndices.data_type: VertexBoneIndices,
    VertexNormal.data_type: VertexNormal,
    VertexUV.data_type: VertexUV,
    VertexTangent.data_type: VertexTangent,
    VertexBitangent.data_type: VertexBitangent,
    VertexColor.data_type: VertexColor,
}  # type: dict[int, tp.Type[VertexDataType]]


@dataclass(slots=True)
class VertexDataTypeStruct(BinaryStruct):

    unk_x00: int
    data_offset: int  # offset of data type's data in described buffer
    format_enum: VertexDataFormatEnum = field(**Binary(int))
    _data_type: int
    instance_index: int  # instance index of this data type in its layout


@dataclass(slots=True)
class VertexBufferStruct(BinaryStruct):
    """Header information about a packed FLVER vertex data buffer, which we read into a NumPy structured array."""
    buffer_index: int
    layout_index: int
    vertex_size: int
    vertex_count: int
    _pad1: bytes = field(init=False, **BinaryPad(8))
    buffer_length: int
    buffer_offset: int


class VertexDataSizeError(SoulstructError):
    """Raised by some vanilla meshes."""

    def __init__(self, vertex_size: int, layout_size: int):
        self.vertex_size = vertex_size
        self.layout_size = layout_size
        super().__init__(
            f"Vertex buffer vertex size {vertex_size} not equal to size calculated from layout: {layout_size}."
        )


@dataclass(slots=True)
class LayoutStruct(BinaryStruct):
    layout_types_count: int
    pad1: bytes = field(init=False, **BinaryPad(8))
    layout_types_offset: int


class VertexDataLayout(list[VertexDataType]):
    """List of `VertexDataType` instances that describes a vertex buffer layout.

    Functions as a standard list, with extra methods for constructing combined `np.dtype` and reading/packing buffers.
    """

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader) -> VertexDataLayout:
        """Read a FLVER vertex buffer layout into a list of `VertexDataType` instances.

        Each instance's subclass indicates its data type, and its `format_enum` value indicates its exact fields and
        which codec to use for compression/decompression.
        """
        buffer_layout_struct = LayoutStruct.from_bytes(reader)

        with reader.temp_offset(buffer_layout_struct.layout_types_offset):
            tight_data_offset = 0
            data_types = []
            for _ in range(buffer_layout_struct.layout_types_count):
                data_type_struct = VertexDataTypeStruct.from_bytes(reader)

                if data_type_struct.data_offset != tight_data_offset:
                    _LOGGER.warning(
                        f"Layout member offset {data_type_struct.data_offset} does not match expected offset "
                        f"{tight_data_offset}."
                    )

                data_type_cls = VERTEX_DATA_TYPES[data_type_struct.pop("_data_type")]
                data_type = data_type_struct.to_object(data_type_cls)
                data_types.append(data_type)
                tight_data_offset += VERTEX_FORMAT_ENUM_SIZES[data_type.format_enum]

        return cls(data_types)

    def to_flver_writer(self, writer: BinaryWriter) -> LayoutStruct:
        """Write a FLVER vertex buffer layout from a list of `VertexDataType` instances.

        Packs the header struct and reserves its `layout_types_offset` field for later when actual types are packed.
        Returns the struct (as the owner of the reserved field).
        """
        layout_struct = LayoutStruct(layout_types_count=len(self), layout_types_offset=RESERVED)
        layout_struct.to_writer(writer)
        return layout_struct

    def pack_layout_types(self, writer: BinaryWriter, layout_struct: LayoutStruct):
        """Write actual layout data type information and fill header offset field."""
        writer.fill_with_position("layout_types_offset", layout_struct)
        for data_type in self:
            VertexDataTypeStruct.object_to_writer(data_type, writer)  # will write `data_type` class variable too

    def unpack_vertex_array(self, data: bytes, uv_factor: int) -> np.ndarray:
        """Use this layout to read a structured array of vertex data from the given raw FLVER buffer data."""
        compressed_dtype, decompressed_dtype = self.get_dtypes()
        decompression_funcs = self.get_decompression_funcs(uv_factor=uv_factor)

        compressed_array = np.frombuffer(data, dtype=compressed_dtype)
        decompressed_array = np.empty(len(compressed_array), dtype=decompressed_dtype)
        # Iterate over decompressed dtype and func.
        for decompress, (name, dtype) in zip(decompression_funcs, decompressed_dtype.fields.items()):
            decompressed_array[name] = decompress(compressed_array[name].astype(dtype[0]))
        return decompressed_array

    def pack_vertex_array(self, array: np.ndarray, uv_factor: int) -> bytes:
        """Use this layout to pack a structured array of vertex data into raw FLVER buffer data."""
        compressed_dtype, decompressed_dtype = self.get_dtypes()
        compression_funcs = self.get_compression_funcs(uv_factor=uv_factor)

        compressed_array = np.empty(len(array), dtype=compressed_dtype)
        # Iterate over compressed dtype and func.
        for compress, (name, dtype) in zip(compression_funcs, compressed_dtype.fields.items()):
            compressed_array[name] = compress(array[name].astype(dtype[0]))
        return compressed_array.tobytes()

    def get_dtypes(self) -> tuple[np.dtype, np.dtype]:
        """Get compressed and decompressed NumPy dtypes for this layout."""
        compressed_fields = []
        decompressed_fields = []
        uv_index = 0
        color_index = 0

        for data_type in self:
            if isinstance(data_type, VertexPosition) and data_type.format_enum == VertexDataFormatEnum.EdgeCompressed:
                # Explicitly not implemented yet.
                raise NotImplementedError("Cannot yet read FLVERs with edge-compressed vertex positions. Sorry!")

            # Find format. Will raise a `ValueError` here if not supported.
            vertex_data_format = data_type.get_format()

            if isinstance(data_type, VertexUV):
                if data_type.format_enum in {VertexDataFormatEnum.Float4, VertexDataFormatEnum.UVPair}:
                    # Data field contains TWO UVs.
                    compressed_fields += vertex_data_format.get_dtype_fields(
                        compressed=True, index=uv_index, second_index=uv_index + 1
                    )
                    decompressed_fields += vertex_data_format.get_dtype_fields(
                        compressed=False, index=uv_index, second_index=uv_index + 1
                    )
                    uv_index += 2
                else:
                    compressed_fields += vertex_data_format.get_dtype_fields(compressed=True, index=uv_index)
                    decompressed_fields += vertex_data_format.get_dtype_fields(compressed=False, index=uv_index)
                    uv_index += 1
            elif isinstance(data_type, VertexColor):
                compressed_fields += vertex_data_format.get_dtype_fields(compressed=True, index=color_index)
                decompressed_fields += vertex_data_format.get_dtype_fields(compressed=False, index=color_index)
                color_index += 1
            else:
                compressed_fields += vertex_data_format.get_dtype_fields(compressed=True)
                decompressed_fields += vertex_data_format.get_dtype_fields(compressed=False)

        return np.dtype(compressed_fields), np.dtype(decompressed_fields)

    def get_decompression_funcs(self, uv_factor: int = None) -> list[tp.Callable]:
        """Get list of decompression functions for every field (not just broad data type) in this layout."""
        funcs = []

        if uv_factor:
            def uv_decompress_func(x):
                return x / uv_factor
        else:
            uv_decompress_func = None

        for data_type in self:
            if isinstance(data_type, VertexPosition) and data_type.format_enum == VertexDataFormatEnum.EdgeCompressed:
                # Explicitly not implemented yet.
                raise NotImplementedError("Cannot yet read FLVERs with edge-compressed vertex positions. Sorry!")

            # Find format. Will raise a `ValueError` here if not supported.
            vertex_data_format = data_type.get_format()
            field_count = len(vertex_data_format.names)

            if isinstance(data_type, VertexUV) and vertex_data_format.decompressed_format:
                # Bake `uv_factor` into decompression.
                funcs += [uv_decompress_func] * field_count
                continue

            codec = vertex_data_format.codec
            if isinstance(codec, tuple):
                # Separate codecs for separate fields.
                funcs += list(codec)
            else:
                # Single codec for all fields.
                funcs += [codec] * field_count

        return funcs

    def get_compression_funcs(self, uv_factor: int = None) -> list[tp.Callable]:
        """Get list of compression functions for every field (not just broad data type) in this layout."""
        funcs = []

        if uv_factor:
            def uv_compress_func(x):
                return x * uv_factor
        else:
            uv_compress_func = None

        for data_type in self:
            if isinstance(data_type, VertexPosition) and data_type.format_enum == VertexDataFormatEnum.EdgeCompressed:
                # Explicitly not implemented yet.
                raise NotImplementedError("Cannot yet read FLVERs with edge-compressed vertex positions. Sorry!")

            # Find format. Will raise a `ValueError` here if not supported.
            vertex_data_format = data_type.get_format()
            field_count = len(vertex_data_format.names)

            if isinstance(data_type, VertexUV) and vertex_data_format.decompressed_format:
                # Bake `uv_factor` into decompression.
                funcs += [uv_compress_func] * field_count
                continue

            codec = vertex_data_format.codec
            if isinstance(codec, tuple):
                # Separate codecs for separate fields.
                funcs += list(codec)
            else:
                # Single codec for all fields.
                funcs += [codec] * field_count

        return funcs

    def get_total_data_size(self) -> int:
        return sum(data_type.size for data_type in self)

    def __repr__(self):
        data_types = "\n    ".join(repr(data_type) for data_type in self)
        return (
            f"VertexDataLayout(\n"
            f"    {data_types}\n"
            f") <size={self.get_total_data_size()}>"
        )


@dataclass(slots=True)
class VertexArray:
    """Wraps a structured NumPy array containing vertex data for a particular FLVER submesh."""

    array: np.ndarray
    layout: VertexDataLayout

    @classmethod
    def from_flver_reader(
        cls,
        flver_reader: BinaryReader,
        buffer_struct: VertexBufferStruct,
        layouts: list[VertexDataLayout],
        vertex_data_offset: int,
        uv_factor: int,
    ):
        if buffer_struct.vertex_size != buffer_struct.buffer_length / buffer_struct.vertex_count:
            _LOGGER.warning(
                f"FLVER vertex buffer has vertex size {buffer_struct.vertex_size}, but has total buffer length "
                f"{buffer_struct.buffer_length} and vertex count {buffer_struct.vertex_count}. Buffer length ignored."
            )

        layout = layouts[buffer_struct.layout_index]
        layout_size = layout.get_total_data_size()
        if layout_size != buffer_struct.vertex_size:
            # TODO: This happens in vanilla DSR FLVERs. I try to fix it ahead of time by studying material MTD names,
            #  but if we reach here, that hasn't worked. Causes seem to be missing or unexpected tangents/bitangents.
            raise VertexDataSizeError(buffer_struct.vertex_size, layout_size)

        with flver_reader.temp_offset(vertex_data_offset + buffer_struct.buffer_offset):
            buffer_data = flver_reader.read(buffer_struct.buffer_length)
            array = layout.unpack_vertex_array(buffer_data, uv_factor)

        return cls(array, layout)

    def to_flver_writer(
        self,
        writer: BinaryWriter,
        write_buffer_length: bool,
        layout_index: int,
        buffer_index: int,
    ):
        """Note that `layout_index` will be into a merged FLVER-wide list."""
        layout_size = self.layout.get_total_data_size()
        vertex_count = len(self.array)
        VertexBufferStruct.object_to_writer(
            self,
            writer,
            buffer_index=buffer_index,
            layout_index=layout_index,
            vertex_size=layout_size,
            vertex_count=vertex_count,
            buffer_length=layout_size * vertex_count if write_buffer_length else 0,
            buffer_offset=RESERVED,
        )

    def pack_array(
        self,
        writer: BinaryWriter,
        buffer_offset: int,
        uv_factor: int,
    ):
        writer.fill("buffer_offset", buffer_offset, obj=self)
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

# TODO:
#  - make dtype from list of `VertexDataType`
#  - convert dtype to list of `VertexDataType` if format enums are given for each field (FLVER subclass game defaults?)
#  - read vertex buffers into `VertexArray` from an offset, given its `buffer_layout` and `dtype`
#  - don't keep 'buffer objects' around
#  - don't keep buffer layouts around; when packing FLVER, non-unique layouts are merged
#  - attach `Material` instances to Submeshes; when packing FLVER, non-unique materials are merged
