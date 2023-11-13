"""
As always, courtesy of SoulsFormats by TKGP:
    https://github.com/JKAnderson/SoulsFormats/blob/master/SoulsFormats/Formats/TPF/DDS.cs
"""
from __future__ import annotations

__all__ = [
    "DDS", "DDSHeader", "DDSD", "DDPF", "DDSCAPS", "DDSCAPS2", "DXGI_FORMAT",
    "TexconvError", "texconv", "get_converted_texture_data", "convert_dds_file", "convert_image_to_dds",
]

import logging
import subprocess
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path

from soulstruct.exceptions import SoulstructError
from soulstruct.base.game_file import GameFile
from soulstruct.utilities.files import PACKAGE_PATH
from soulstruct.utilities.binary import *

try:
    Self = tp.Self
except AttributeError:
    Self = "DDS"

_LOGGER = logging.getLogger(__name__)


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
    """Extra format enum in `DX10` headers or `TPFTexture` console headers.

    https://learn.microsoft.com/en-us/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format
    """
    UNKNOWN = 0
    R32G32B32A32_TYPELESS = 1
    R32G32B32A32_FLOAT = 2
    R32G32B32A32_UINT = 3
    R32G32B32A32_SINT = 4
    R32G32B32_TYPELESS = 5
    R32G32B32_FLOAT = 6
    R32G32B32_UINT = 7
    R32G32B32_SINT = 8
    R16G16B16A16_TYPELESS = 9
    R16G16B16A16_FLOAT = 10
    R16G16B16A16_UNORM = 11
    R16G16B16A16_UINT = 12
    R16G16B16A16_SNORM = 13
    R16G16B16A16_SINT = 14
    R32G32_TYPELESS = 15
    R32G32_FLOAT = 16
    R32G32_UINT = 17
    R32G32_SINT = 18
    R32G8X24_TYPELESS = 19
    D32_FLOAT_S8X24_UINT = 20
    R32_FLOAT_X8X24_TYPELESS = 21
    X32_TYPELESS_G8X24_UINT = 22
    R10G10B10A2_TYPELESS = 23
    R10G10B10A2_UNORM = 24
    R10G10B10A2_UINT = 25
    R11G11B10_FLOAT = 26
    R8G8B8A8_TYPELESS = 27
    R8G8B8A8_UNORM = 28
    R8G8B8A8_UNORM_SRGB = 29
    R8G8B8A8_UINT = 30
    R8G8B8A8_SNORM = 31
    R8G8B8A8_SINT = 32
    R16G16_TYPELESS = 33
    R16G16_FLOAT = 34
    R16G16_UNORM = 35
    R16G16_UINT = 36
    R16G16_SNORM = 37
    R16G16_SINT = 38
    R32_TYPELESS = 39
    D32_FLOAT = 40
    R32_FLOAT = 41
    R32_UINT = 42
    R32_SINT = 43
    R24G8_TYPELESS = 44
    D24_UNORM_S8_UINT = 45
    R24_UNORM_X8_TYPELESS = 46
    X24_TYPELESS_G8_UINT = 47
    R8G8_TYPELESS = 48
    R8G8_UNORM = 49
    R8G8_UINT = 50
    R8G8_SNORM = 51
    R8G8_SINT = 52
    R16_TYPELESS = 53
    R16_FLOAT = 54
    D16_UNORM = 55
    R16_UNORM = 56
    R16_UINT = 57
    R16_SNORM = 58
    R16_SINT = 59
    R8_TYPELESS = 60
    R8_UNORM = 61
    R8_UINT = 62
    R8_SNORM = 63
    R8_SINT = 64
    A8_UNORM = 65
    R1_UNORM = 66
    R9G9B9E5_SHAREDEXP = 67
    R8G8_B8G8_UNORM = 68
    G8R8_G8B8_UNORM = 69
    BC1_TYPELESS = 70
    BC1_UNORM = 71
    BC1_UNORM_SRGB = 72
    BC2_TYPELESS = 73
    BC2_UNORM = 74
    BC2_UNORM_SRGB = 75
    BC3_TYPELESS = 76
    BC3_UNORM = 77
    BC3_UNORM_SRGB = 78
    BC4_TYPELESS = 79
    BC4_UNORM = 80
    BC4_SNORM = 81
    BC5_TYPELESS = 82
    BC5_UNORM = 83
    BC5_SNORM = 84
    B5G6R5_UNORM = 85
    B5G5R5A1_UNORM = 86
    B8G8R8A8_UNORM = 87
    B8G8R8X8_UNORM = 88
    R10G10B10_XR_BIAS_A2_UNORM = 89
    B8G8R8A8_TYPELESS = 90
    B8G8R8A8_UNORM_SRGB = 91
    B8G8R8X8_TYPELESS = 92
    B8G8R8X8_UNORM_SRGB = 93
    BC6H_TYPELESS = 94
    BC6H_UF16 = 95
    BC6H_SF16 = 96
    BC7_TYPELESS = 97
    BC7_UNORM = 98
    BC7_UNORM_SRGB = 99
    AYUV = 100
    Y410 = 101
    Y416 = 102
    NV12 = 103
    P010 = 104
    P016 = 105
    OPAQUE_420 = 106  # DGXI_FORMAT_420_OPAQUE
    YUY2 = 107
    Y210 = 108
    Y216 = 109
    NV11 = 110
    AI44 = 111
    IA44 = 112
    P8 = 113
    A8P8 = 114
    B4G4R4A4_UNORM = 115
    P208 = 130
    V208 = 131
    V408 = 132
    FORCE_UINT = 0xffffffff


@dataclass(slots=True)
class DDSHeader(BinaryStruct):
    magic: bytes = field(init=False, **BinaryString(4, rstrip_null=True, asserted=b"DDS "))  # note space!
    size: int = field(init=False, **Binary(asserted=0x7C))
    flags: uint
    height: int
    width: int
    pitch_or_linear_size: int
    depth: int
    mipmap_count: int
    reserved_1: list[int] = field(**BinaryArray(11))
    # Start of `PIXELFORMAT` in SoulsFormats.
    pixelformat_size: int = field(init=False, **Binary(asserted=32))
    pixelformat_flags: DDPF = field(**Binary(uint))
    fourcc: bytes = field(**BinaryString(4))
    rgb_bit_count: int
    r_bitmask: uint
    g_bitmask: uint
    b_bitmask: uint
    a_bitmask: uint
    # End of `PIXELFORMAT`.
    caps1: uint
    caps2: uint
    caps3: uint
    caps4: uint
    reserved_2: int


@dataclass(slots=True)
class DXT10Header(BinaryStruct):

    dxgi_format: DXGI_FORMAT = field(**Binary(uint))
    resource_dimension: DIMENSION = field(**Binary(uint))
    misc_flag: uint  # RESOURCE_MISC
    array_size: uint
    alpha_mode: ALPHA_MODE = field(**Binary(uint))


@dataclass(slots=True)
class DDS(GameFile):
    """Unpacks DDS header information.

    Does NOT unpack actual DDS information or support packing or writing.
    """

    header: DDSHeader = None
    dxt10_header: DXT10Header | None = None

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        header = DDSHeader.from_bytes(reader)
        dxt10_header = DXT10Header.from_bytes(reader) if header.fourcc == b"DX10" else None
        return cls(header=header, dxt10_header=dxt10_header)

    def to_writer(self) -> BinaryWriter:
        raise TypeError("Cannot write `DDS` files. Only the header can be unpacked.")

    @property
    def fourcc(self) -> str:
        return self.header.fourcc.decode()

    @property
    def dxgi_format(self) -> DXGI_FORMAT | None:
        """Returns DXGI format if present (DX10 format), or `None` otherwise."""
        return self.dxt10_header.dxgi_format if self.dxt10_header else None

    @property
    def texconv_format(self) -> str:
        """Returns DXGI format name if present, or `fourcc` otherwise."""
        if self.dxt10_header:
            return self.dxt10_header.dxgi_format.name
        return self.fourcc

    def __repr__(self):
        if self.dxt10_header:
            return f"DDS(DX10, dxgi_format={self.dxt10_header.dxgi_format.name})"
        return f"DDS({self.header.fourcc.decode()})"


class TexconvError(SoulstructError):
    """Error raised by `texconv` subprocess."""
    pass


def texconv(*args):
    texconv_path = PACKAGE_PATH("base/textures/texconv.exe")
    if not texconv_path.is_file():
        raise FileNotFoundError("Cannot find `texconv.exe` that should be bundled with Soulstruct in 'base/textures'.")
    return subprocess.run(
        [texconv_path, *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


# TODO: use `tempfile` module
def get_converted_texture_data(input_source: bytes | Path | str, *texconv_args) -> bytes:
    if isinstance(input_source, bytes):
        temp_dds_path = Path(__file__).parent / "__temp__.dds"
        temp_dds_path.write_bytes(input_source)
        result = texconv("-o", str(Path(__file__).parent), "-y", *texconv_args, str(temp_dds_path))
        if result.returncode == 0:
            return temp_dds_path.read_bytes()
        raise ValueError(
            f"Could not convert texture source bytes.\n"
            f"   stdout: {result.stdout}\n"
            f"   stderr: {result.stderr}"
        )
    else:
        result = texconv(*texconv_args, str(input_source))
        output_path = Path(input_source).with_suffix(".DDS")
        if result.returncode == 0 and output_path.is_file():
            return output_path.read_bytes()
        else:
            raise ValueError(
                f"Could not convert texture source {input_source}.\n"
                f"   stdout: {result.stdout}\n"
                f"   stderr: {result.stderr}"
            )


def convert_dds_file(
    dds_path: str | Path, output_dir: str | Path, output_format: str, input_fourcc: str = None
):
    """Convert DDS file path to a different format using DirectX-powered `texconv.exe`.

    If `input_format` is given, the source DDS will be checked to make sure it matches that format.
    """
    if input_fourcc is not None:
        # Check that DDS starts with the asserted format.
        dds = DDS.from_path(dds_path)
        if dds.header.fourcc.decode() != input_fourcc:
            raise ValueError(f"DDS format {dds.header.fourcc} does not match `input_format` {input_fourcc}")
    return texconv("-f", output_format, "-o", output_dir, "-y", dds_path)


def convert_image_to_dds(image_path: str | Path, output_dir: str | Path, output_format: str):
    """Convert image file path (JPG, PNG, etc.) to a different format using DirectX-powered `texconv.exe`."""
    return texconv("-f", output_format, "-o", output_dir, "-y", image_path)
