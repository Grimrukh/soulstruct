"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use.

As always, courtesy of SoulsFormats by TKGP:
    https://github.com/JKAnderson/SoulsFormats/blob/master/SoulsFormats/Formats/TPF/DDS.cs
"""

from __future__ import annotations

__all__ = ["DDS"]

import typing as tp
from enum import IntEnum, auto

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryReader, BinaryWriter, BinaryObject, BinaryStruct


class DDSD(IntEnum):
    CAPS = 0x1
    HEIGHT = 0x2
    WIDTH = 0x4
    PITCH = 0x8
    PIXELFORMAT = 0x1000
    MIPMAPCOUNT = 0x20000
    LINEARSIZE = 0x80000
    DEPTH = 0x800000


HEADER_FLAGS_TEXTURE = DDSD.CAPS | DDSD.HEIGHT | DDSD.WIDTH | DDSD.PIXELFORMAT


class DDSCAPS(IntEnum):
    COMPLEX = 0x8
    TEXTURE = 0x1000
    MIPMAP = 0x400000


class DDSCAPS2(IntEnum):
    CUBEMAP = 0x200
    CUBEMAP_POSITIVEX = 0x400
    CUBEMAP_NEGATIVEX = 0x800
    CUBEMAP_POSITIVEY = 0x1000
    CUBEMAP_NEGATIVEY = 0x2000
    CUBEMAP_POSITIVEZ = 0x4000
    CUBEMAP_NEGATIVEZ = 0x8000
    VOLUME = 0x200000


CUBEMAP_ALLFACES = (
    DDSCAPS2.CUBEMAP | DDSCAPS2.CUBEMAP_POSITIVEX | DDSCAPS2.CUBEMAP_NEGATIVEX | DDSCAPS2.CUBEMAP_POSITIVEY |
    DDSCAPS2.CUBEMAP_NEGATIVEY | DDSCAPS2.CUBEMAP_POSITIVEZ | DDSCAPS2.CUBEMAP_NEGATIVEZ
)


class DDPF(IntEnum):
    ALPHAPIXELS = 0x1
    ALPHA = 0x2
    FOURCC = 0x4
    RGB = 0x40
    YUV = 0x200
    LUMINANCE = 0x20000


class DIMENSION(IntEnum):
    TEXTURE1D = 2
    TEXTURE2D = 3
    TEXTURE3D = 4


class RESOURCE_MISC(IntEnum):
    TEXTURECUBE = 0x4


class ALPHA_MODE(IntEnum):
    UNKNOWN = 0
    STRAIGHT = 1
    PREMULTIPLIED = 2
    OPAQUE = 3
    CUSTOM = 4


class DXGI_FORMAT(IntEnum):
    UNKNOWN = auto()
    R32G32B32A32_TYPELESS = auto()
    R32G32B32A32_FLOAT = auto()
    R32G32B32A32_UINT = auto()
    R32G32B32A32_SINT = auto()
    R32G32B32_TYPELESS = auto()
    R32G32B32_FLOAT = auto()
    R32G32B32_UINT = auto()
    R32G32B32_SINT = auto()
    R16G16B16A16_TYPELESS = auto()
    R16G16B16A16_FLOAT = auto()
    R16G16B16A16_UNORM = auto()
    R16G16B16A16_UINT = auto()
    R16G16B16A16_SNORM = auto()
    R16G16B16A16_SINT = auto()
    R32G32_TYPELESS = auto()
    R32G32_FLOAT = auto()
    R32G32_UINT = auto()
    R32G32_SINT = auto()
    R32G8X24_TYPELESS = auto()
    D32_FLOAT_S8X24_UINT = auto()
    R32_FLOAT_X8X24_TYPELESS = auto()
    X32_TYPELESS_G8X24_UINT = auto()
    R10G10B10A2_TYPELESS = auto()
    R10G10B10A2_UNORM = auto()
    R10G10B10A2_UINT = auto()
    R11G11B10_FLOAT = auto()
    R8G8B8A8_TYPELESS = auto()
    R8G8B8A8_UNORM = auto()
    R8G8B8A8_UNORM_SRGB = auto()
    R8G8B8A8_UINT = auto()
    R8G8B8A8_SNORM = auto()
    R8G8B8A8_SINT = auto()
    R16G16_TYPELESS = auto()
    R16G16_FLOAT = auto()
    R16G16_UNORM = auto()
    R16G16_UINT = auto()
    R16G16_SNORM = auto()
    R16G16_SINT = auto()
    R32_TYPELESS = auto()
    D32_FLOAT = auto()
    R32_FLOAT = auto()
    R32_UINT = auto()
    R32_SINT = auto()
    R24G8_TYPELESS = auto()
    D24_UNORM_S8_UINT = auto()
    R24_UNORM_X8_TYPELESS = auto()
    X24_TYPELESS_G8_UINT = auto()
    R8G8_TYPELESS = auto()
    R8G8_UNORM = auto()
    R8G8_UINT = auto()
    R8G8_SNORM = auto()
    R8G8_SINT = auto()
    R16_TYPELESS = auto()
    R16_FLOAT = auto()
    D16_UNORM = auto()
    R16_UNORM = auto()
    R16_UINT = auto()
    R16_SNORM = auto()
    R16_SINT = auto()
    R8_TYPELESS = auto()
    R8_UNORM = auto()
    R8_UINT = auto()
    R8_SNORM = auto()
    R8_SINT = auto()
    A8_UNORM = auto()
    R1_UNORM = auto()
    R9G9B9E5_SHAREDEXP = auto()
    R8G8_B8G8_UNORM = auto()
    G8R8_G8B8_UNORM = auto()
    BC1_TYPELESS = auto()
    BC1_UNORM = auto()
    BC1_UNORM_SRGB = auto()
    BC2_TYPELESS = auto()
    BC2_UNORM = auto()
    BC2_UNORM_SRGB = auto()
    BC3_TYPELESS = auto()
    BC3_UNORM = auto()
    BC3_UNORM_SRGB = auto()
    BC4_TYPELESS = auto()
    BC4_UNORM = auto()
    BC4_SNORM = auto()
    BC5_TYPELESS = auto()
    BC5_UNORM = auto()
    BC5_SNORM = auto()
    B5G6R5_UNORM = auto()
    B5G5R5A1_UNORM = auto()
    B8G8R8A8_UNORM = auto()
    B8G8R8X8_UNORM = auto()
    R10G10B10_XR_BIAS_A2_UNORM = auto()
    B8G8R8A8_TYPELESS = auto()
    B8G8R8A8_UNORM_SRGB = auto()
    B8G8R8X8_TYPELESS = auto()
    B8G8R8X8_UNORM_SRGB = auto()
    BC6H_TYPELESS = auto()
    BC6H_UF16 = auto()
    BC6H_SF16 = auto()
    BC7_TYPELESS = auto()
    BC7_UNORM = auto()
    BC7_UNORM_SRGB = auto()
    AYUV = auto()
    Y410 = auto()
    Y416 = auto()
    NV12 = auto()
    P010 = auto()
    P016 = auto()
    OPAQUE_420 = auto()  # DXGI_FORMAT_420_OPAQUE
    YUY2 = auto()
    Y210 = auto()
    Y216 = auto()
    NV11 = auto()
    AI44 = auto()
    IA44 = auto()
    P8 = auto()
    A8P8 = auto()
    B4G4R4A4_UNORM = auto()
    P208 = auto()
    V208 = auto()
    V408 = auto()
    FORCE_UINT = auto()


class DDSHeader(BinaryObject):

    STRUCT = BinaryStruct(
        ("magic", "4s", b"DDS "),
        ("size", "i", 0x7C),
        ("flags", "I"),
        ("height", "i"),
        ("width", "i"),
        ("pitch_or_linear_size", "i"),
        ("depth", "i"),
        ("mip_map_count", "i"),
        ("reserved_1", "11i"),
        # Start of `PIXELFORMAT` in SoulsFormats.
        ("size", "i", 32),
        ("flags", "I"),
        ("fourcc", "4s"),
        ("rgb_bit_count", "i"),
        ("r_bitmask", "I"),
        ("g_bitmask", "I"),
        ("b_bitmask", "I"),
        ("a_bitmask", "I"),
        # End of `PIXELFORMAT`.
        ("caps", "I"),
        ("caps_2", "I"),
        ("caps_3", "i"),
        ("caps_4", "i"),
        ("reserved_2", "i"),
    )

    flags: int
    height: int
    width: int
    pitch_or_linear_size: int
    depth: int
    mipmap_count: int
    reserved_1: tp.Tuple[int]
    # Start of `PIXELFORMAT` in SoulsFormats.
    flags: DDPF
    fourcc: bytes
    rgb_bit_count: int
    r_bitmask: int
    g_bitmask: int
    b_bitmask: int
    a_bitmask: int
    # End of `PIXELFORMAT`.
    caps: DDSCAPS
    caps_2: DDSCAPS2
    caps_3: int
    caps_4: int
    reserved_2: int

    unpack = BinaryObject.default_unpack
    pack = BinaryObject.default_pack


class DXT10Header(BinaryObject):

    STRUCT = BinaryStruct(
        ("dxgi_format", "I"),
        ("resource_dimension", "I"),
        ("misc_flag", "I"),
        ("array_size", "I"),
        ("alpha_mode", "I"),
    )

    dxgi_format: DXGI_FORMAT
    resource_dimension: DIMENSION
    misc_flag: RESOURCE_MISC
    array_size: int
    alpha_mode: ALPHA_MODE

    unpack = BinaryObject.default_unpack
    pack = BinaryObject.default_pack


class DDS(GameFile):

    header: DDSHeader
    dxt10_header: tp.Optional[DXT10Header]

    def unpack(self, reader: BinaryReader, **kwargs):

        self.header = DDSHeader(reader)
        self.dxt10_header = DXT10Header(reader) if self.header.fourcc == b"DX10" else None

    def pack(self, **kwargs) -> bytes:
        writer = BinaryWriter()
        self.header.pack(writer)
        if self.dxt10_header:
            self.dxt10_header.pack(writer)
        return writer.finish()
