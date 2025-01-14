from __future__ import annotations

__all__ = [
    "TPFTexture",
    "TPF",
    "TPFPlatform",
    "TextureType",
    "batch_get_tpf_texture_png_data",
    "batch_get_tpf_texture_tga_data",
]

import abc
import logging
import math
import multiprocessing
import re
import shutil
import tempfile
import typing as tp
import zlib
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.base.textures.dds import *
from soulstruct.base.textures.texconv import TexconvError, texconv
from soulstruct.dcx import DCXType, decompress
from soulstruct.utilities.binary import *
from soulstruct.utilities.files import read_json, write_json


_LOGGER = logging.getLogger("soulstruct")


class TPFPlatform(IntEnum):
    PC = 0
    Xbox360 = 1
    PS3 = 2
    PS4 = 4
    XboxOne = 5

    def get_byte_order(self):
        if self in {TPFPlatform.Xbox360, TPFPlatform.PS3}:
            return ByteOrder.BigEndian
        return ByteOrder.LittleEndian


class TextureType(IntEnum):
    Texture = 0  # one 2D texture
    Cubemap = 1  # six 2D textures
    Volume = 2  # one 3D texture


# The `TPFTexture.STRUCT.format` field is some other internal enum, which we need to map to DXGI_FORMAT for consoles.
TPF_TEXTURE_FORMAT_TO_DXGI_FORMAT = {
    0: DXGI_FORMAT.BC1_UNORM,
    1: DXGI_FORMAT.BC1_UNORM,
    3: DXGI_FORMAT.BC2_UNORM,
    5: DXGI_FORMAT.BC3_UNORM,
    6: DXGI_FORMAT.B5G5R5A1_UNORM,
    8: DXGI_FORMAT.R8G8B8A8_UNORM,
    9: DXGI_FORMAT.B8G8R8A8_UNORM,
    10: DXGI_FORMAT.R8G8B8A8_UNORM,
    16: DXGI_FORMAT.A8_UNORM,
    22: DXGI_FORMAT.R16G16B16A16_UNORM,
    23: DXGI_FORMAT.BC3_UNORM,
    24: DXGI_FORMAT.BC4_UNORM,
    25: DXGI_FORMAT.BC1_UNORM,
    29: DXGI_FORMAT.BC1_UNORM,
    33: DXGI_FORMAT.BC3_UNORM,
    100: DXGI_FORMAT.BC6H_UF16,
    102: DXGI_FORMAT.BC7_UNORM,
    103: DXGI_FORMAT.BC4_UNORM,
    104: DXGI_FORMAT.BC5_UNORM,
    105: DXGI_FORMAT.R8G8B8A8_UNORM,
    106: DXGI_FORMAT.BC7_UNORM,
    107: DXGI_FORMAT.BC7_UNORM,
    108: DXGI_FORMAT.BC1_UNORM,
    109: DXGI_FORMAT.BC1_UNORM,
    110: DXGI_FORMAT.BC3_UNORM,
    112: DXGI_FORMAT.BC7_UNORM_SRGB,
    113: DXGI_FORMAT.BC6H_UF16,
    115: DXGI_FORMAT.BC6H_UF16,
}


@dataclass(slots=True)
class TPFTexture:

    class STRUCT(BinaryStruct, abc.ABC):
        data_offset: uint
        data_size: int
        format: byte
        texture_type: TextureType = binary(byte)
        mipmap_count: byte
        texture_flags: byte

    class FLOAT_STRUCT(BinaryStruct):
        """Unknown optional data for some textures."""
        unk0: int
        size: int  # 4 * len(data)

        def unpack_data(self, reader: BinaryReader) -> list[float]:
            return list(reader.unpack(f"{self.size}f"))

    stem: str = ""  # no file extension
    format: int = 1
    texture_type: TextureType = TextureType.Texture
    mipmap_count: int = 0
    texture_flags: int = 0  # {2, 3} -> DCX-compressed (i.e. bit 1); unknown otherwise
    data: bytes = b""

    @dataclass(slots=True)
    class ConsoleInfo:
        """Extra metadata for headerless textures used in console versions.

        NOT a `BinaryStruct`, as its exact layout varies by console and is handled manually.
        """
        width: int
        height: int
        texture_count: int = 0
        unk1: int = 0  # unknown, PS3 only
        unk2: int = 0  # unknown, 0x0 or 0xAAE4 in DeS, 0xD in BB/DS3 (console)
        dxgi_format: DXGI_FORMAT = DXGI_FORMAT.UNKNOWN  # must be supplied for certain `TPFTexture.format` values (DX10)

    console_info: ConsoleInfo | None = None  # only used for console textures to supplement headerless DDS
    unknown_float_struct: tuple[int, list[float]] | None = None

    # Platform is stored in the `TPF`, not each `TPFTexture`, but it is often very convenient to associate them as
    # textures are unpacked and pooled across TPFs.
    platform: TPFPlatform | None = None

    @classmethod
    def from_tpf_reader(
        cls,
        reader: BinaryReader,
        platform: TPFPlatform,
        tpf_flags: int,
        encoding: str,
    ):
        texture_struct = cls.STRUCT.from_bytes(reader)

        if platform != TPFPlatform.PC:
            width = reader["h"]
            height = reader["h"]
            console_info = cls.ConsoleInfo(width, height)

            # Only PS4 and XboxOne actually store their DXGI_FORMAT in the `TPFTexture`, which will be set below.
            # For all other consoles, we need to remap the `STRUCT.format` enum.
            console_info.dxgi_format = TPF_TEXTURE_FORMAT_TO_DXGI_FORMAT.get(texture_struct.format, DXGI_FORMAT.UNKNOWN)

            if platform == TPFPlatform.Xbox360:
                reader.assert_pad(4)
            elif platform == TPFPlatform.PS3:
                console_info.unk1 = reader["i"]
                if tpf_flags != 0:
                    console_info.unk2 = reader["i"]
                    if console_info.unk2 not in {0, 0x69E0, 0xAAE4}:
                        raise ValueError(
                            f"`ConsoleInfo.unk2` was {console_info.unk2}, but expected one of: [0, 0x69E0, 0xAAE4]"
                        )
            elif platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
                console_info.texture_count = reader["i"]
                if console_info.texture_count not in {1, 6}:
                    f"`ConsoleInfo.texture_count` was {console_info.texture_count}, but expected 1 or 6."
                console_info.unk2 = reader["i"]
                if console_info.unk2 != 0xD:
                    f"`ConsoleInfo.unk2` was {console_info.unk2}, but expected 0xD."
            # `dxgi_format` unpacked below.
        else:
            console_info = None

        stem_offset = reader["I"]
        has_unknown_float_struct = reader["i"] == 1
        if platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
            console_info.dxgi_format = DXGI_FORMAT(reader["i"])
        if has_unknown_float_struct:
            float_struct = cls.FLOAT_STRUCT.from_bytes(reader)
            unknown_float_struct = (float_struct.unk0, float_struct.unpack_data(reader))
        else:
            unknown_float_struct = None

        with reader.temp_offset(texture_struct.pop("data_offset")):
            data = reader.read(texture_struct.pop("data_size"))
        if texture_struct.texture_flags in {2, 3}:
            # Data is DCX-compressed.
            # TODO: should enforce DCX type as 'DCP_EDGE'?
            data = decompress(data)

        stem = reader.unpack_string(offset=stem_offset, encoding=encoding)

        texture = texture_struct.to_object(
            cls,
            stem=stem,
            data=data,
            console_info=console_info,
            unknown_float_struct=unknown_float_struct,
            platform=platform,
        )

        if console_info and console_info.dxgi_format == DXGI_FORMAT.UNKNOWN:
            _LOGGER.warning(
                f"Could not determine DXGI_FORMAT for TPFTexture '{stem}' (internal format {texture_struct.format})."
            )

        return texture

    def to_tpf_writer(self, writer: BinaryWriter, platform: TPFPlatform, tpf_flags: int):
        if platform == TPFPlatform.PC:
            dds = self.get_dds()
            if dds.header.caps2 & DDSCAPS2.CUBEMAP:
                texture_type = TextureType.Cubemap
            elif dds.header.caps2 & DDSCAPS2.VOLUME:
                texture_type = TextureType.Volume
            else:
                texture_type = TextureType.Texture
            mipmap_count = dds.header.mipmap_count
        else:
            texture_type = self.texture_type
            mipmap_count = self.mipmap_count

        self.STRUCT.object_to_writer(
            self,
            writer,
            data_offset=RESERVED,
            data_size=RESERVED,
            texture_type=texture_type,
            mipmap_count=mipmap_count,
        )

        if platform != TPFPlatform.PC:
            writer.pack("h", self.console_info.width)
            writer.pack("h", self.console_info.height)
            if platform == TPFPlatform.Xbox360:
                writer.pad(4)
            elif platform == TPFPlatform.PS3:
                writer.pack("i", self.console_info.unk1)
                if tpf_flags != 0:
                    writer.pack("i", self.console_info.unk2)
            elif platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
                writer.pack("i", self.console_info.texture_count)
                writer.pack("i", self.console_info.unk2)

        writer.reserve("stem_offset", "I", obj=self)
        writer.pack("i", 0 if self.unknown_float_struct is None else 1)

        if platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
            writer.pack("i", self.console_info.dxgi_format)

        if self.unknown_float_struct is not None:
            unk0, floats = self.unknown_float_struct
            self.FLOAT_STRUCT(unk0=unk0, size=len(floats) * 4).to_writer(writer)
            writer.pack(f"{len(floats) * 4}f", *floats)

        if self.platform is not None and self.platform != platform:
            _LOGGER.warning(
                f"`TPFPlatform` assigned to `TPFTexture` {self.stem} ({self.platform}) does not match the platform of "
                f"the TPF it is being written into ({platform}). The TPF platform will be kept."
            )

    def pack_stem(self, writer: BinaryWriter, encoding_type: int):
        writer.fill_with_position("stem_offset", obj=self)
        if encoding_type == 1:  # UTF-16
            stem = self.stem.encode(encoding=writer.byte_order.get_utf_16_encoding()) + b"\0\0"
        elif encoding_type in {0, 2}:  # shift-jis
            stem = self.stem.encode(encoding="shift-jis") + b"\0"
        else:
            raise ValueError(f"Invalid TPF texture encoding type: {encoding_type}. Must be 0, 1, or 2.")
        writer.append(stem)

    def pack_data(self, writer: BinaryWriter):
        writer.fill_with_position("data_offset", obj=self)
        if self.texture_flags in {2, 3}:
            data = zlib.compress(self.data, level=7)
        else:
            data = self.data

        writer.fill("data_size", len(data), obj=self)
        writer.append(data)

    def get_dds(self) -> DDS:
        return DDS.from_bytes(self.data)

    def get_dds_fourcc(self) -> bytes:
        dds_header = DDSHeader.from_bytes(self.data)  # only need the header
        return dds_header.pixelformat.fourcc

    def get_headerized_data(self, deswizzle_platform: TPFPlatform = None) -> bytes:
        """Attempt to build a header for  headerless DDS texture to TPFTexture with header."""

        # First, we can simply check if a header is already present.
        if self.data[:4] == b"DDS ":
            return self.data  # has header

        if self.platform is None:
            # We can't guess the console format to deswizzle without the platform.
            raise DDSDeswizzleError("Cannot guess `TPFTexture.platform` value for console deswizzling. Set it first.")
        if not self.console_info:
            raise TexconvError("Cannot convert headerless DDS texture to TGA without `TPFTexture.console_info`.")
        return bytes(self.get_headerized_dds(deswizzle_platform))

    def write_dds(self, dds_path: str | Path):
        Path(dds_path).write_bytes(self.data)

    def replace_dds(self, image_path: Path | str, dds_format: str = None):
        if dds_format is None:
            dds = self.get_dds()
            dds_format = dds.texconv_format
            if "TYPELESS" in dds_format:
                old_dds_format = dds_format
                dds_format = old_dds_format.replace("TYPELESS", "UNORM")
                _LOGGER.info(f"Changing DDS format '{old_dds_format}' to '{dds_format}' for conversion.")
        image_path = Path(image_path)
        with tempfile.TemporaryDirectory() as dds_dir:
            temp_image_path = Path(dds_dir, f"temp{image_path.suffix}")
            shutil.copy2(image_path, temp_image_path)
            result = texconv("-f", dds_format, "-o", dds_dir, "-nologo", "-y", temp_image_path)
            if result.returncode == 0:
                try:
                    self.data = Path(dds_dir, "temp.dds").read_bytes()
                except FileNotFoundError:
                    stdout = result.stdout.decode()
                    raise TexconvError(
                        f"Could not convert image {image_path} to DDS with format {dds_format}:\n    {stdout}"
                    )
            else:
                stdout = result.stdout.decode()
                raise TexconvError(
                    f"Could not convert texture source bytes.\n"
                    f"   stdout: {stdout}\n"
                    f"   stderr: {result.stderr}"
                )

    def get_png_data(self, deswizzle_platform: TPFPlatform = None, fmt="rgba") -> bytes:
        with tempfile.TemporaryDirectory() as png_dir:
            temp_dds_path = Path(png_dir, "temp.dds")
            dds_data = self.get_headerized_data(deswizzle_platform)
            temp_dds_path.write_bytes(dds_data)
            Path("~/Documents/temp.dds").expanduser().write_bytes(dds_data)
            texconv_result = texconv("-o", png_dir, "-ft", "png", "-f", fmt, "-nologo", temp_dds_path)
            try:
                return Path(png_dir, "temp.png").read_bytes()
            except FileNotFoundError:
                stdout = texconv_result.stdout.decode()
                raise TexconvError(f"Could not convert texture DDS to PNG:\n    {stdout}")

    def export_png(self, png_path: str | Path, deswizzle_platform: TPFPlatform = None, fmt="rgba"):
        png_data = self.get_png_data(deswizzle_platform, fmt)
        png_path.write_bytes(png_data)

    def get_tga_data(self, deswizzle_platform: TPFPlatform) -> bytes:
        """Convert DDS to TGA.

        NOTE: `texconv` has these TGA options, but I'm not using them at the moment:
            -tga20
            -tgazeroalpha
        """
        with tempfile.TemporaryDirectory() as tga_dir:
            temp_dds_path = Path(tga_dir, "temp.dds")
            dds_data = self.get_headerized_data(deswizzle_platform)
            temp_dds_path.write_bytes(dds_data)
            Path("~/Documents/temp.dds").expanduser().write_bytes(dds_data)
            texconv_result = texconv("-o", tga_dir, "-ft", "tga", "-f", "RGBA", "-nologo", temp_dds_path)
            try:
                return Path(tga_dir, "temp.tga").read_bytes()
            except FileNotFoundError:
                stdout = texconv_result.stdout.decode()
                raise TexconvError(f"Could not convert texture DDS to TGA:\n    {stdout}")

    def export_tga(self, tga_path: str | Path, deswizzle_platform: TPFPlatform = None):
        tga_data = self.get_tga_data(deswizzle_platform)
        tga_path.write_bytes(tga_data)

    def convert_dds_format(self, output_format: str, assert_input_format: str = None) -> bool:
        """Convert `data` DDS format in place. Returns `True` if conversion succeeds."""
        dds = self.get_dds()
        current_format = dds.header.pixelformat.fourcc.decode()
        current_dxgi_format = dds.dx10_header.dxgi_format if dds.dx10_header else None
        if assert_input_format is not None and current_format != assert_input_format.encode():
            raise ValueError(
                f"TPF texture DDS format {current_format} does not match "
                f"`assert_input_format` {assert_input_format} ({current_format}"
            )
        temp_dds_path = Path(__file__).parent / "__temp__.dds"
        temp_dds_path.write_bytes(self.data)
        result = convert_dds_file(temp_dds_path, Path(__file__).parent, output_format)  # overwrite temp file
        if result.returncode == 0:
            self.data = temp_dds_path.read_bytes()
            if current_dxgi_format:
                _LOGGER.info(
                    f"Converted TPF texture {self.stem} from format {current_format} "
                    f"(DXGI {current_dxgi_format}) to {output_format}."
                )
            else:
                _LOGGER.info(f"Converted TPF texture {self.stem} from format {current_format} to {output_format}.")
            return True
        else:
            _LOGGER.error(
                f"Could not convert TPF texture {self.stem} from format {current_format} to {output_format}.\n"
                f"   stdout: {result.stdout}\n"
                f"   stderr: {result.stderr}"
            )
            return False

    @staticmethod
    def get_texture_format_info(texture_format: int) -> tuple[bytes, int, bool]:
        """Get `fourcc` code (four nulls if unused), bytes per block, and `is_compressed` for given value of
        `TPFTexture.format` (internal enum, *not* `DXGI_FORMAT`).

        `dxgi_format` for DX10 headers is supplied by `TPFTexture.console_info.dxgi_format`.

        At least one format value (10) is known to be different between PC and PS3 (R8G8B8 vs A8G8B8R8). However, this
        doesn't affect the returned values here, so I've removed it for now.
        """
        null = b"\0\0\0\0"
        match texture_format:
            case 0 | 1 | 24 | 25 | 108 | 109:
                return b"DXT1", 8, True
            case 3:
                return b"DXT3", 16, True
            case 5 | 23 | 33 | 110:
                return b"DXT5", 16, True
            case 6:
                return b"DX10", 2, False  # expected format: B5G5R5A1_UNORM
            case 9:
                return null, 4, False
            case 10:
                # TODO: Pointless?
                # if platform == TPFPlatform.PS3:
                #     return null, 4, False  # expected format: A8G8B8R8
                return null, 4, False  # PC; expected format: R8G8B8
            case 16:
                return null, 1, False
            case 22:
                return b"q\0\0\0", 8, False  # fourcc is number 0x71
            case 100:
                return b"DX10", 16, True  # expected format: BC6H_UF16
            case 102 | 106 | 107:
                return b"DX10", 16, True  # expected format: BC7_UNORM
            case 103:
                return b"ATI1", 8, True
            case 104:
                return b"ATI2", 16, True
            case 105:
                return null, 4, False
            case 112:
                return b"DX10", 16, True  # expected format: BC7_UNORM_SRGB
            case 113:
                return b"DX10", 16, True  # expected format: BC6H_UF16
            case _:
                raise ValueError(f"Unknown TPF texture format value: {texture_format}")

    def get_headerized_dds(self, deswizzle_platform: TPFPlatform = None) -> DDS:
        """Generate automatic DDS headers for headerless console textures and pack them together.

        Requires `TPFTexture.header` to specify texture width, height, and (for DX10) `DXGI_FORMAT`.
        """
        if deswizzle_platform is None:
            if self.platform is None:
                raise ValueError(
                    "Must provide `deswizzle_platform` or assign `TPFTexture.platform` to headerize DDS."
                )
            deswizzle_platform = self.platform

        if self.console_info is None:
            raise ValueError("Cannot generate DDS header for console texture without `TPFTexture.console_info`.")

        width = self.console_info.width
        height = self.console_info.height

        fourcc, block_size, is_compressed = self.get_texture_format_info(self.format)

        flags = DDSD.get_required_flags() | DDSD.MIPMAPCOUNT  # always enables `MIPMAPCOUNT`
        if is_compressed:
            flags |= DDSD.LINEARSIZE
            pitch_or_linear_size = max(1, (width + 3) // 4) * block_size  # linear size
        else:
            flags |= DDSD.PITCH
            pitch_or_linear_size = (width * block_size + 7) // 8  # pitch

        if self.mipmap_count == 0:
            mipmap_count = int(math.ceil(math.log(max(width, height), 2))) + 1
        else:
            mipmap_count = self.mipmap_count

        pixelformat = DDSPixelFormat.from_fourcc_tpf_format(fourcc, self.format)

        caps1 = DDSCAPS.TEXTURE
        if self.texture_type == TextureType.Cubemap:
            caps1 |= DDSCAPS.COMPLEX
        if mipmap_count > 1:
            caps1 |= DDSCAPS.COMPLEX | DDSCAPS.MIPMAP

        if self.texture_type == TextureType.Cubemap:
            caps2 = DDSCAPS2.get_cubemap_all_faces()
        elif self.texture_type == TextureType.Volume:
            caps2 = DDSCAPS2.VOLUME
        else:
            caps2 = 0

        dds_header = DDSHeader(
            flags=flags,
            height=height,
            width=width,
            pitch_or_linear_size=pitch_or_linear_size,
            depth=0,
            mipmap_count=mipmap_count,
            reserved_1=[0] * 11,  # unused; you often find authorship strings here ('UVER', 'NVTT', etc.)
            pixelformat=pixelformat,
            caps1=caps1,
            caps2=caps2,
            caps3=0,
            caps4=0,
            reserved_2=0,
        )

        # TODO: Any big-endian byte order on old consoles?

        if fourcc == b"DX10":
            dx10_header = DX10Header.get_default(self.console_info.dxgi_format)
            if self.texture_type == TextureType.Cubemap:
                dx10_header.misc_flag |= RESOURCE_MISC.TEXTURECUBE
        else:
            dx10_header = None

        if deswizzle_platform == TPFPlatform.PC:
            # No deswizzling required.
            return DDS(header=dds_header, dx10_header=dx10_header, data=self.data)

        # Deswizzle console DDS.
        try:
            match deswizzle_platform:
                case TPFPlatform.PS3:
                    data = deswizzle_dds_bytes_ps3(self.data, self.console_info.dxgi_format, width, height)
                case TPFPlatform.PS4:
                    data = deswizzle_dds_bytes_ps4(self.data, self.console_info.dxgi_format, width, height)
                case _:
                    raise ValueError(f"DDS deswizzling is currently only supported for PS3 and PS4 TPF textures.")
        except DDSDeswizzleError as ex:
            raise DDSDeswizzleError(
                f"Failed to deswizzle DDS texture {self.stem} from platform {deswizzle_platform} with:\n"
                f"    TPFTexture format: {self.format}\n"
                f"    Dimensions: {width} x {height}\n"
                f"    DXGI_FORMAT: {self.console_info.dxgi_format}\n"
                f"Internal error: {ex}"
            )

        return DDS(header=dds_header, dx10_header=dx10_header, data=data)

    def __repr__(self) -> str:
        return (
            f"TPFTexture(\n"
            f"    stem = '{self.stem}'\n"
            f"    format = {self.format}\n"
            f"    texture_type = {self.texture_type.name}\n"
            f"    mipmap_count = {self.mipmap_count}\n"
            f"    texture_flags = {self.texture_flags}\n"
            f"    data = <{len(self.data)} bytes>\n"
            f"    has_console_info = {self.console_info is not None}\n"
            f"    has_unknown_float_struct = {self.unknown_float_struct is not None}\n"
            f")"
        )


class TPFStruct(BinaryStruct):
    signature: bytes = binary_string(4, asserted=b"TPF\0")
    _data_size: int
    file_count: int
    platform: TPFPlatform = binary(byte)
    tpf_flags: byte = field(**(Binary(asserted=[0, 1, 2, 3])))
    encoding_type: byte = binary(asserted=[0, 1, 2])  # 2 == UTF-16, 0/1 == shift_jis_2004
    _pad1: bytes = binary_pad(1)


class TPF(GameFile):

    textures: list[TPFTexture] = field(default_factory=list)
    platform: TPFPlatform = TPFPlatform.PC
    encoding_type: int = 0
    tpf_flags: int = 0  # non-zero value on PS3 means textures have `unk2`; unknown otherwise

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> TPF:
        platform = TPFPlatform(reader["B", 0xC])
        reader.byte_order = ByteOrder.big_endian_bool(platform in {TPFPlatform.Xbox360, TPFPlatform.PS3})
        tpf_struct = TPFStruct.from_bytes(reader)

        encoding = reader.get_utf_16_encoding() if tpf_struct.encoding_type == 1 else "shift_jis_2004"
        textures = [
            TPFTexture.from_tpf_reader(reader, platform, tpf_struct.tpf_flags, encoding)
            for _ in range(tpf_struct.file_count)
        ]
        return cls(
            textures=textures, platform=platform, encoding_type=tpf_struct.encoding_type, tpf_flags=tpf_struct.tpf_flags
        )

    @classmethod
    def from_unpacked_path(cls, path: str | Path) -> tp.Self:
        """Load manifest JSON or unpacked TPF directory containing a manifest JSON."""
        path = Path(path)
        if path.is_dir():
            directory = path
            manifest_path = directory / "tpf_manifest.json"
            if not manifest_path.exists():
                raise FileNotFoundError(f"Binder manifest JSON file not found: {manifest_path}")
        elif path.name == "tpf_manifest.json":
            directory = path.parent
            manifest_path = path
        else:
            raise ValueError(
                f"Invalid file source for `{cls.__name__}`: {path}. Must be a manifest JSON file or unpacked folder "
                f"containing one."
            )

        if not manifest_path.is_file():
            raise FileNotFoundError(f"Could not find TPF manifest file: {manifest_path}")
        manifest = read_json(manifest_path, encoding="shift-jis")

        textures = []
        for entry in manifest["entries"]:

            # Legacy support for change from 'name' to 'stem'.
            if "name" in entry:
                entry["stem"] = entry.pop("name")

            dds_path = directory / f"{entry['stem']}.dds"
            if not dds_path.is_file():
                raise FileNotFoundError(f"Could not find DDS file for TPF texture {entry['stem']}: {dds_path}")
            console_info = TPFTexture.ConsoleInfo(**entry["header"]) if entry.get("header", None) is not None else None
            textures.append(TPFTexture(
                stem=entry["stem"],
                format=entry["format"],
                texture_type=TextureType[entry["texture_type"]],
                mipmap_count=entry["mipmap_count"],
                texture_flags=entry["texture_flags"],
                data=dds_path.read_bytes(),
                console_info=console_info,
                unknown_float_struct=entry.get("unknown_float_struct", None),
            ))

        tpf = cls(
            dcx_type=DCXType[manifest["dcx_type"]],
            platform=TPFPlatform[manifest["platform"]],
            encoding_type=manifest["encoding_type"],
            tpf_flags=manifest["tpf_flags"],
            textures=textures,
        )

        if directory.suffix == ".unpacked":  # only this suffix is automatically removed
            tpf.path = directory.with_name(directory.name[:-9])
        else:
            tpf.path = directory  # writing this path will conflict with this unpacked folder source

        return tpf

    def to_writer(self) -> BinaryWriter:
        """Pack TPF file to bytes."""
        byte_order = self.platform.get_byte_order()
        writer = TPFStruct.object_to_writer(self, byte_order=byte_order)

        for texture in self.textures:
            texture.to_tpf_writer(writer, self.platform, self.tpf_flags)
        for texture in self.textures:
            texture.pack_stem(writer, self.encoding_type)

        if self.platform == TPFPlatform.PS3:
            # NOTE: SoulsFormats aligns to 0x100 here, but in Demon's Souls TPFs, they sometimes align to 0x80 provided
            # that the emergent pad size is large enough (possibly at least 0x40, which is the smallest I've seen so far
            # in c7150). To better emulate vanilla files, I explicitly pad by 0x40, then align to 0x80. I'd have to look
            # at every vanilla file to confirm the minimum pad.
            writer.pad(0x40)
            writer.pad_align(0x80)

        data_start = writer.position
        data_size = 0

        for texture in self.textures:
            # TKGP notes: padding varies wildly across games, so don't worry about it too much.
            # However, from Demon's Souls TPFs on PS3, it's clear that each texture aligns to 0x80 (possibly with the
            # same minimum pad as above, but ignoring that for now).
            if self.platform == TPFPlatform.PS3:
                writer.pad_align(0x80)
            elif len(texture.data) > 0:
                writer.pad_align(4)  # default alignment
            texture_pos = writer.position
            texture.pack_data(writer)
            texture_size = writer.position - texture_pos
            data_size += texture_size

        # Demon's Souls (PS3) also aligns to 0x80 after the final texture (not included in data size). The total data
        # size in the header also excludes all the padding. (Possibly true for later TPFs too.)
        if self.platform == TPFPlatform.PS3:
            writer.pad_align(0x80)
            writer.fill("_data_size", data_size, obj=self)
        else:
            writer.fill("_data_size", writer.position - data_start, obj=self)

        writer.fill("file_count", len(self.textures), obj=self)
        return writer

    def write_unpacked_directory(self, directory=None):
        if directory is None:
            if self.path:
                directory = self.path.with_suffix(self.path.suffix + ".unpacked")
            else:
                raise ValueError("Cannot detect `directory` for unpacked binder automatically.")
        else:
            directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)

        texture_entries = []
        for texture in self.textures:
            if texture.console_info is not None:
                console_info_dict = {
                    "width": texture.console_info.width,
                    "height": texture.console_info.height,
                    "mipmaps": texture.console_info.texture_count,
                    "unk1": texture.console_info.unk1,
                    "unk2": texture.console_info.unk2,
                    "dxgi_format": texture.console_info.dxgi_format.name,
                }
            else:
                console_info_dict = None

            texture_dict = {
                "stem": texture.stem,
                "format": texture.format,
                "texture_type": texture.texture_type.name,
                "mipmap_count": texture.mipmap_count,
                "texture_flags": texture.texture_flags,
                "console_info": console_info_dict,
                "unknown_float_struct": texture.unknown_float_struct,
            }
            texture_entries.append(texture_dict)
            texture.write_dds(directory / f"{texture.stem}.dds")
        tpf_manifest = self.get_json_header()
        tpf_manifest["entries"] = texture_entries

        # NOTE: Binder manifest is always encoded in shift-JIS, not `shift_jis_2004`.
        write_json(directory / "tpf_manifest.json", tpf_manifest, encoding="shift-jis", indent=4)

    def get_json_header(self):
        return {
            "dcx_type": self.dcx_type.name,
            "platform": self.platform.name,
            "encoding_type": self.encoding_type,
            "tpf_flags": self.tpf_flags,
        }

    def convert_dds_formats(self, input_format: str, output_format: str):
        """Convert all DDS files that currently have format `input_format` to `output_format`.

        Formats should look like b"DX10", b"DXT1", etc.
        """
        fail_count = 0
        total_count = 0
        for texture in self.textures:
            dds = texture.get_dds()
            if dds.fourcc == input_format:
                success = texture.convert_dds_format(output_format)
                total_count += 1
                if not success:
                    fail_count += 1
        if fail_count > 0:
            _LOGGER.warning(
                f"Failed to convert {fail_count} out of {total_count} textures from {input_format} to {output_format}."
            )

    def find_texture_stem(self, stem: str, case_sensitive=False) -> TPFTexture:
        """Find texture by name."""
        if not case_sensitive:
            stem = stem.lower()
            for texture in self.textures:
                if texture.stem.lower() == stem:
                    return texture
        else:
            for texture in self.textures:
                if texture.stem == stem:
                    return texture
        raise ValueError(f"Could not find texture with name {stem}.")

    def get_all_png_data(self, deswizzle_platform: TPFPlatform = None, fmt="rgba") -> list[tp.Optional[bytes]]:
        png_datas = []
        for tex in self.textures:
            try:
                png_datas.append(tex.get_png_data(deswizzle_platform, fmt))
            except ValueError as ex:
                _LOGGER.warning(str(ex))
                png_datas.append(None)
        return png_datas

    def export_to_pngs(self, png_dir_path: Path | str, fmt="rgba"):
        for tex in self.textures:
            png_name = Path(f"{tex.stem}.png")
            try:
                tex.export_png(png_dir_path / png_name, fmt=fmt)
            except ValueError as ex:
                _LOGGER.warning(str(ex))

    def __iter__(self) -> tp.Iterator[TPFTexture]:
        return iter(self.textures)

    def __len__(self) -> int:
        return len(self.textures)

    def __repr__(self) -> str:
        return (
            f"TPF(\n"
            f"    textures = <{len(self.textures)} textures>\n"
            f"    platform = {self.platform.name}\n"
            f"    encoding_type = {self.encoding_type}\n"
            f"    tpf_flags = {self.tpf_flags}\n"
            f")"
        )

    @classmethod
    def collect_tpf_textures(
        cls, tpfbhd_directory: str | Path, convert_formats: tp.Tuple[str, str] = None
    ) -> dict[str, TPFTexture]:
        """Build a dictionary mapping TGA texture names to `TPFTexture` instances.

        NOTE: This decompresses/unpacks every TPF in every BXF in the directory, which can be slow and redundant. Use
        `collect_tpf_entries()` above and only open the TPFs needed (since map TPFBHD TPFs should only have one DDS
        texture in them matching the TPF entry name).
        """
        from soulstruct.containers import Binder

        tpf_re = re.compile(rf"(.*)\.tpf(\.dcx)?$")
        tpfbhd_directory = Path(tpfbhd_directory)
        textures = {}
        for bhd_path in tpfbhd_directory.glob("*.tpfbhd"):
            bxf = Binder.from_path(bhd_path)
            for entry in bxf.entries:
                match = tpf_re.match(entry.name)
                if match:
                    tpf = cls.from_bytes(entry.data)
                    if convert_formats is not None:
                        input_format, output_format = convert_formats
                        tpf.convert_dds_formats(input_format, output_format)
                    for texture in tpf.textures:
                        textures[texture.stem] = texture
        return textures


def _get_png_data(tex: TPFTexture, deswizzle_platform: TPFPlatform, fmt: str):
    """Function for batch operator."""
    try:
        return tex.get_png_data(deswizzle_platform=deswizzle_platform, fmt=fmt)
    except (TexconvError, DDSDeswizzleError) as ex:
        _LOGGER.error(f"Failed to get TPF texture as PNG: {str(ex)}")
        return None


def batch_get_tpf_texture_png_data(
    tpf_textures: list[TPFTexture], deswizzle_platform: TPFPlatform = None, fmt="rgba", processes: int = None
) -> list[bytes | None]:
    """Use multiprocessing to retrieve PNG data (converted from DDS) for a collection of `TPFTexture`s.

    Failed conversions will put `None` into list rather than PNG bytes.
    """

    mp_args = [(tpf_texture, deswizzle_platform, fmt) for tpf_texture in tpf_textures]

    with multiprocessing.Pool(processes=processes) as pool:
        png_data = pool.starmap(_get_png_data, mp_args)  # blocks here until all done

    return png_data


def _get_tga_data(tex: TPFTexture, deswizzle_platform: TPFPlatform):
    """Function for batch operator."""
    try:
        return tex.get_tga_data(deswizzle_platform)
    except (TexconvError, DDSDeswizzleError) as ex:
        _LOGGER.error(f"Failed to get TPF texture as TGA: {str(ex)}")
        return None


def batch_get_tpf_texture_tga_data(
    tpf_textures: list[TPFTexture], deswizzle_platform: TPFPlatform = None, processes: int = None
) -> list[bytes | None]:
    """Use multiprocessing to retrieve TGA data (converted from DDS) for a collection of `TPFTexture`s.

    Failed conversions will put `None` into list rather than TGA bytes.
    """

    mp_args = [(tpf_texture, deswizzle_platform) for tpf_texture in tpf_textures]

    with multiprocessing.Pool(processes=processes) as pool:
        tga_data = pool.starmap(_get_tga_data, mp_args)  # blocks here until all done

    return tga_data
