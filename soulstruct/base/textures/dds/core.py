"""
As always, courtesy of SoulsFormats by TKGP:
    https://github.com/JKAnderson/SoulsFormats/blob/master/SoulsFormats/Formats/TPF/DDS.cs
"""
from __future__ import annotations

__all__ = [
    "DDS",
    "DDSHeader",
    "DXT10Header",
    "convert_dds_file",
]

import logging
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *

from soulstruct.base.textures.texconv import texconv
from .enums import *

try:
    Self = tp.Self
except AttributeError:
    Self = "DDS"

_LOGGER = logging.getLogger(__name__)


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
    # Start of `DDS_PIXELFORMAT` struct (0x4C).
    pixelformat_size: int = field(init=False, **Binary(asserted=32))
    pixelformat_flags: DDPF = field(**Binary(uint))  # bit flags are mutually exclusive
    fourcc: bytes = field(**BinaryString(4))
    rgb_bit_count: int
    r_bitmask: uint
    g_bitmask: uint
    b_bitmask: uint
    a_bitmask: uint
    # End of `DDS_PIXELFORMAT` struct.
    caps1: uint  # `DDSCAPS` bit flags
    caps2: uint  # `DDSCAPS2` bit flags
    caps3: uint  # unused
    caps4: uint  # unused
    reserved_2: int  # unused


@dataclass(slots=True)
class DXT10Header(BinaryStruct):

    dxgi_format: DXGI_FORMAT = field(**Binary(uint))
    resource_dimension: D3D10_RESOURCE_DIMENSION = field(**Binary(uint))
    misc_flag: uint  # RESOURCE_MISC
    array_size: uint  # typically zero
    alpha_mode: ALPHA_MODE = field(**Binary(uint))

    @classmethod
    def get_default(cls, dxgi_format: DXGI_FORMAT):
        """Get standard texture header with given format."""
        dx10_header = cls(
            dxgi_format=dxgi_format,
            resource_dimension=D3D10_RESOURCE_DIMENSION.TEXTURE2D,
            misc_flag=0,
            array_size=1,
            alpha_mode=ALPHA_MODE.UNKNOWN,
        )
        dx10_header.byte_order = ByteOrder.LittleEndian
        return dx10_header


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


def convert_dds_file(
    dds_path: str | Path, output_dir: str | Path, output_format: str, input_fourcc: str = None
):
    """Convert DDS file path to a different format using DirectX-powered `texconv.exe`.

    If `input_format` is given, the source DDS will be checked to make sure it matches that format.
    """
    if input_fourcc is not None:
        # Check that DDS starts with the asserted format.
        from soulstruct.base.textures.dds import DDS
        dds = DDS.from_path(dds_path)
        if dds.header.fourcc.decode() != input_fourcc:
            raise ValueError(f"DDS format {dds.header.fourcc} does not match `input_format` {input_fourcc}")
    return texconv("-f", output_format, "-o", output_dir, "-y", dds_path)
