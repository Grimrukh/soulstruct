__all__ = [

]

import abc
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

import numpy as np

from soulstruct.utilities.binary import *


# All the different codecs (decompression/compression functions) for vertex data.
_INT_TO_FLOAT_127 = (
    lambda i: i / 127.0,
    lambda f: f * 127,
)
_INT_TO_FLOAT_255 = (
    lambda i: i / 255.0,
    lambda f: f * 255,
)
_INT_TO_FLOAT_32767 = (
    lambda i: i / 32767.0,
    lambda f: f * 32767,
)
_INT_TO_FLOAT_127_SIGNED = (
    lambda i: (i - 127.0) / 127.0,
    lambda f: f * 127 + 127,
)
_INT_TO_FLOAT_255_SIGNED = (
    lambda i: (i - 255.0) / 255.0,
    lambda f: f * 255 + 255,
)
_INT_TO_FLOAT_32767_SIGNED = (
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


class VertexDataFormat(tp.NamedTuple):

    names: tuple[str, ...]
    compressed_format: str
    decompressed_format: str = None  # defaults to same as `compressed_format`

    # Codec can be a single pair of functions (for both compression and decompression) or a tuple of pairs matching
    # the number of `names` (for different codecs for each name). Defaults to no codec (data is not compressed).
    codec: tuple[tp.Callable, tp.Callable] | tuple[tuple[tp.Callable, tp.Callable] | None, ...] | None = None

    # TODO: Methods here!


class VertexDataType(abc.ABC):
    """Information about a vertex data type."""
    VALUE: int  # value of the `member_type` field in the `LayoutMember` struct
    FORMATS: dict[tuple[int, ...], VertexDataFormat]  # maps `data_type` IDs to their `dtype` fields and codec
    UNIQUE: bool = False

    # Used to look up fields and codecs in class `FORMATS`.
    format_enum: VertexDataFormatEnum


class VertexPosition(VertexDataType):
    VALUE = 0
    FORMATS = {
        (0x03,): VertexDataFormat(
            names=("position_x", "position_y", "position_z"),
            compressed_format="fff",
        ),
        (0x04,): VertexDataFormat(
            names=("position_x", "position_y", "position_z", "position_w"),
            compressed_format="ffff",
        ),
    }


class VertexBoneWeights(VertexDataType):
    VALUE = 1
    FORMATS = {
        (0x13,): VertexDataFormat(
            names=("bone_weight_a", "bone_weight_b", "bone_weight_c", "bone_weight_d"),
            compressed_format="bbbb",
            decompressed_format="ffff",
            codec=_INT_TO_FLOAT_127,
        ),
        (0x14,): VertexDataFormat(
            names=("bone_weight_a", "bone_weight_b", "bone_weight_c", "bone_weight_d"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=_INT_TO_FLOAT_127,
        ),
        (0x16, 0x1A): VertexDataFormat(
            names=("bone_weight_a", "bone_weight_b", "bone_weight_c", "bone_weight_d"),
            compressed_format="hhhh",
            decompressed_format="ffff",
            codec=_INT_TO_FLOAT_32767,
        ),
    }
    UNIQUE = True


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
    VALUE = 2
    FORMATS = {
        (0x11, 0x2F): VertexDataFormat(
            names=("bone_index_a", "bone_index_b", "bone_index_c", "bone_index_d"),
            compressed_format="BBBB",
        ),
        (0x18,): VertexDataFormat(
            names=("bone_index_a", "bone_index_b", "bone_index_c", "bone_index_d"),
            compressed_format="hhhh",
        ),
    }
    UNIQUE = True


class VertexNormal(VertexDataType):
    """Vertex normal.

    When 4D, the fourth `normal_w` component is sometimes used as a bone index, I believe. Otherwise, it seems to be
    always 127; it is never converted to a float here, regardless of its integer format.
    """
    VALUE = 3
    FORMATS = {
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
            codec=(_INT_TO_FLOAT_127_SIGNED,) * 3 + (None,),
        ),
        (0x12,): VertexDataFormat(
            names=("normal_w", "normal_y", "normal_z", "normal_x"),  # W comes first
            compressed_format="Bbbb",
            decompressed_format="fffB",
            codec=(None,) + (_INT_TO_FLOAT_127_SIGNED,) * 3,
        ),
        (0x1A,): VertexDataFormat(
            names=("normal_x", "normal_y", "normal_z", "normal_w"),
            compressed_format="hhhh",
            decompressed_format="fffh",
            codec=(_INT_TO_FLOAT_32767_SIGNED,) * 3 + (None,),
        ),
        (0x2E,): VertexDataFormat(
            names=("normal_x", "normal_y", "normal_z", "normal_w"),
            compressed_format="HHHh",
            decompressed_format="fffh",
            codec=(_INT_TO_FLOAT_32767_SIGNED,) * 3 + (None,),
        ),
    }


class VertexUV(VertexDataType):
    """Texture coordinates.

    NOTE: Some UV FORMATS contain a pair of coordinates. Indices are added for each UV slot when generated.

    All non-float UV formats will also be de-quantized using `uv_factor` from the FLVER header.
    """

    VALUE = 5
    FORMATS = {
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


class VertexTangent(VertexDataType):
    """Perpendicular to normal."""

    VALUE = 6
    FORMATS = {
        (0x03,): VertexDataFormat(
            names=("tangent_x", "tangent_y", "tangent_z"),
            compressed_format="fff",
        ),
        (0x10, 0x11, 0x13, 0x1A, 0x2F): VertexDataFormat(
            names=("tangent_x", "tangent_y", "tangent_z", "tangent_w"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=_INT_TO_FLOAT_127_SIGNED,
        ),
    }


class VertexBitangent(VertexDataType):
    """Pendicular to both normal and tangent."""

    VALUE = 7
    FORMATS = {
        (0x10, 0x11, 0x13, 0x2F): VertexDataFormat(
            names=("bitangent_x", "bitangent_y", "bitangent_z", "bitangent_w"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=_INT_TO_FLOAT_127_SIGNED,
        ),
    }
    UNIQUE = True


class VertexColor(VertexDataType):
    """Used to blend between two textures slots for '[M]' MTD materials, and for alpha for '_Alpha' and '_Edge'.

    Have not yet encountered multiple colors, but it is supported and probably used in later games.
    """

    VALUE = 10
    FORMATS = {
        (0x03,): VertexDataFormat(
            names=("color_r", "color_g", "color_b", "color_a"),
            compressed_format="ffff",
        ),
        (0x10, 0x13): VertexDataFormat(
            names=("color_r", "color_g", "color_b", "color_a"),
            compressed_format="BBBB",
            decompressed_format="ffff",
            codec=_INT_TO_FLOAT_255,
        ),
    }


VERTEX_DATA_TYPES = {
    VertexPosition.VALUE: VertexPosition,
    VertexBoneWeights.VALUE: VertexBoneWeights,
    VertexBoneIndices.VALUE: VertexBoneIndices,
    VertexNormal.VALUE: VertexNormal,
    VertexUV.VALUE: VertexUV,
    VertexTangent.VALUE: VertexTangent,
    VertexBitangent.VALUE: VertexBitangent,
    VertexColor.VALUE: VertexColor,
}


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


@dataclass(slots=True)
class LayoutMemberStruct(BinaryStruct):

    unk_x00: int
    _struct_offset: int  # just the relative offset of this struct
    format_enum: VertexDataFormatEnum = field(**Binary(int))
    data_type: int
    index: int  # instance index of this member in its layout


class VertexArray:
    """Wraps a structured NumPy array containing vertex data for a particular FLVER submesh.


    """

    array: np.ndarray
    layout: list[VertexDataType]


# TODO:
#  - convert FLVER packed 'buffer layouts' to/from lists of `VertexDataType`
#  - make dtype from list of `VertexDataType`
#  - convert dtype to list of `VertexDataType` if format enums are given for each field (FLVER subclass game defaults?)
#  - read vertex buffers into `VertexArray` from an offset, given its `buffer_layout` and `dtype`
#  - don't keep 'buffer objects' around
#  - don't keep buffer layouts around; when packing FLVER, non-unique layouts are merged
#  - attach `Material` instances to Submeshes; when packing FLVER, non-unique materials are merged
