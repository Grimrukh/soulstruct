"""
As always, courtesy of SoulsFormats by TKGP:
    https://github.com/JKAnderson/SoulsFormats/blob/master/SoulsFormats/Formats/TPF/DDS.cs
"""
from __future__ import annotations

__all__ = [
    "DDS",
    "DDSPixelFormat",
    "DDSHeader",
    "DX10Header",
    "DDSImage",
    "convert_dds_file",
]

import logging
import math
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.dcx import DCXType
from soulstruct.utilities.binary import *

from soulstruct.base.textures.texconv import texconv
from .enums import *

_LOGGER = logging.getLogger(__name__)


class DDSPixelFormat(BinaryStruct):
    """DDS_PIXELFORMAT struct, which is embedded inside `DDSHeader` below."""
    size: int = binary(asserted=32, init=False)
    flags: uint  # `DDPF` bit flags
    fourcc: bytes = binary_string(4, default=b"\0\0\0\0")
    rgb_bit_count: int = 0
    r_bitmask: uint = 0
    g_bitmask: uint = 0
    b_bitmask: uint = 0
    a_bitmask: uint = 0

    @classmethod
    def from_fourcc_tpf_format(cls, fourcc: bytes, tpf_format: int) -> DDSPixelFormat:
        pixelformat = cls(flags=0, fourcc=fourcc)
        if fourcc != b"\0\0\0\0":
            pixelformat.flags |= DDPF.FOURCC
            pixelformat.fourcc = fourcc
        match tpf_format:
            case 6:
                pixelformat.flags |= DDPF.ALPHAPIXELS | DDPF.RGB
                pixelformat.rgb_bit_count = 16
                pixelformat.r_bitmask = 0b01111100_00000000
                pixelformat.g_bitmask = 0b00000011_11100000
                pixelformat.b_bitmask = 0b00000000_00011111
                pixelformat.a_bitmask = 0b10000000_00000000
            case 9:
                pixelformat.flags |= DDPF.ALPHAPIXELS | DDPF.RGB
                pixelformat.rgb_bit_count = 32
                pixelformat.r_bitmask = 0x00FF0000
                pixelformat.g_bitmask = 0x0000FF00
                pixelformat.b_bitmask = 0x000000FF
                pixelformat.a_bitmask = 0xFF000000
            case 10:
                pixelformat.flags |= DDPF.RGB
                pixelformat.rgb_bit_count = 32
                pixelformat.r_bitmask = 0x00FF0000
                pixelformat.g_bitmask = 0x0000FF00
                pixelformat.b_bitmask = 0x000000FF
            case 16:
                pixelformat.flags |= DDPF.ALPHA
                pixelformat.rgb_bit_count = 8
                pixelformat.a_bitmask = 0x000000FF
            case 105:
                pixelformat.flags |= DDPF.ALPHAPIXELS | DDPF.RGB
                pixelformat.rgb_bit_count = 32
                pixelformat.r_bitmask = 0x000000FF
                pixelformat.g_bitmask = 0x0000FF00
                pixelformat.b_bitmask = 0x00FF0000
                pixelformat.a_bitmask = 0xFF000000

        return pixelformat


class DDSHeader(BinaryStruct):
    magic: bytes = binary_string(4, rstrip_null=True, asserted=b"DDS ", init=False)  # note space!
    size: int = binary(asserted=0x7C, init=False)
    flags: uint
    height: int
    width: int
    pitch_or_linear_size: int
    depth: int
    mipmap_count: int
    reserved_1: list[int] = binary_array(11)  # unused; other programs sometimes write codes here like 'NVTT'
    pixelformat: DDSPixelFormat  # offset 0x4C
    caps1: uint  # `DDSCAPS` bit flags
    caps2: uint  # `DDSCAPS2` bit flags
    caps3: uint  # unused
    caps4: uint  # unused
    reserved_2: int  # unused


class DX10Header(BinaryStruct):

    dxgi_format: DXGI_FORMAT = binary(uint)
    resource_dimension: D3D10_RESOURCE_DIMENSION = binary(uint)
    misc_flag: uint  # RESOURCE_MISC; used for cubemaps
    array_size: uint  # typically one
    alpha_mode: ALPHA_MODE = binary(uint)

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
        return dx10_header


class DDS(GameFile):
    """Unpacks DDS header information. Does NOT handle the DDS `data` bytes."""

    header: DDSHeader = None
    dx10_header: DX10Header | None = None
    data: bytes = b""

    dcx_type: DCXType = DCXType.Null

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        header = DDSHeader.from_bytes(reader)
        dx10_header = DX10Header.from_bytes(reader) if header.pixelformat.fourcc == b"DX10" else None
        data = reader.read()  # all remaining bytes
        return cls(header=header, dx10_header=dx10_header, data=data)

    def to_writer(self) -> BinaryWriter:
        """Simply packs header(s) and data together."""
        writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
        self.header.to_writer(writer)
        if self.dx10_header:
            self.dx10_header.to_writer(writer)
        writer.append(self.data)
        return writer

    @property
    def pixelformat(self) -> DDSPixelFormat:
        return self.header.pixelformat

    @property
    def fourcc(self) -> str:
        if self.header.pixelformat.fourcc == b"\0\0\0\0":
            return ""
        return self.header.pixelformat.fourcc.decode()

    @property
    def dxgi_format(self) -> DXGI_FORMAT | None:
        """Returns DXGI format if present (DX10 format), or `None` otherwise."""
        return self.dx10_header.dxgi_format if self.dx10_header else None

    @property
    def texconv_format(self) -> str:
        """Returns DXGI format name if present, or `fourcc` otherwise, for `texconv -f` argument."""
        if self.dx10_header:
            return self.dx10_header.dxgi_format.name
        return self.fourcc

    def __repr__(self):
        if self.dx10_header:
            return f"DDS('DX10', {self.dx10_header.dxgi_format.name}, data=<{len(self.data)} bytes>)"
        return f"DDS('{self.fourcc}', data=<{len(self.data)} bytes>)"


@dataclass(slots=True)
class DDSImage:
    """Simple container with unpacking methods for the various mipmap levels inside a DDS image."""

    mipmap_levels: list[bytes] = field(default_factory=list)

    def __bytes__(self):
        """Simply concatenates all mipmap levels."""
        return b"".join(self.mipmap_levels)

    @classmethod
    def read_uncompressed_images(
        cls, reader: BinaryReader, width: int, height: int, pad_dimensions: int, image_count: int,
        mipmap_count: int, image_alignment: int, bytes_per_pixel: int,
    ) -> list[DDSImage]:
        images = []
        for _ in range(image_count):
            mipmap_levels = []
            reader.align(image_alignment)
            for i in range(mipmap_count):
                scale = 2 ** i
                mipmap_width = cls.pad_to(width // scale, pad_dimensions)
                mipmap_height = cls.pad_to(height // scale, pad_dimensions)
                mipmap_levels.append(reader.read(mipmap_width * mipmap_height * bytes_per_pixel))
            images.append(cls(mipmap_levels))
        return images

    @classmethod
    def read_compressed_images(
        cls, reader: BinaryReader, width: int, height: int, pad_dimensions: int, image_count: int,
        mipmap_count: int, image_alignment: int, bytes_per_block: int,
    ) -> list[DDSImage]:
        images = []
        for _ in range(image_count):
            mipmap_levels = []
            reader.align(image_alignment)
            for i in range(mipmap_count):
                scale = 2 ** i
                mipmap_width = cls.pad_to(width // scale, pad_dimensions)
                mipmap_height = cls.pad_to(height // scale, pad_dimensions)
                block_count = int(max(1.0, mipmap_width / 4.0)) * int(max(1.0, mipmap_height / 4.0))
                mipmap_levels.append(reader.read(block_count * bytes_per_block))
            images.append(cls(mipmap_levels))
        return images

    @staticmethod
    def pad_to(value: int, pad: int):
        return int(math.ceil(value / float(pad))) * pad


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
        if dds.fourcc != input_fourcc:
            raise ValueError(f"DDS format {dds.fourcc} does not match `input_format` {input_fourcc}")
    return texconv("-f", output_format, "-o", output_dir, "-y", dds_path)
