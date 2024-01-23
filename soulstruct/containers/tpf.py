from __future__ import annotations

__all__ = [
    "TPFTexture",
    "TPF",
    "TPFPlatform",
    "TextureType",
    "TextureHeader",
    "TextureFloatStruct",
    "batch_get_tpf_texture_png_data",
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


try:
    Self = tp.Self
except AttributeError:
    Self = "TPF"

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


@dataclass(slots=True)
class TextureHeader:
    """Extra metadata for headerless textures used in console versions."""
    width: int
    height: int
    texture_count: int = 0
    unk1: int = 0  # unknown, PS3 only
    unk2: int = 0  # unknown, 0x0 or 0xAAE4 in DeS, 0xD in BB/DS3 (console)
    dxgi_format: DXGI_FORMAT = DXGI_FORMAT.UNKNOWN  # must be supplied for certain `TPFTexture.format` values (DX10)


@dataclass(slots=True)
class TextureFloatStruct(BinaryStruct):
    """Unknown optional data for some textures."""
    unk0: int
    size: int  # 4 * len(data)

    def unpack_data(self, reader: BinaryReader) -> list[float]:
        return list(reader.unpack(f"{self.size}f"))


@dataclass(slots=True)
class TPFTextureStruct(BinaryStruct, abc.ABC):
    data_offset: uint
    data_size: int
    format: byte
    texture_type: TextureType = field(**Binary(byte))
    mipmap_count: byte
    texture_flags: byte


@dataclass(slots=True)
class TPFTexture:

    name: str = ""  # no file extension (just stem)
    format: int = 1
    texture_type: TextureType = TextureType.Texture
    mipmap_count: int = 0
    texture_flags: int = 0  # {2, 3} -> DCX-compressed (i.e. bit 1); unknown otherwise
    data: bytes = b""

    header: TextureHeader | None = None  # only used for console textures to supplement headerless DDS
    unknown_float_struct: tuple[int, list[float]] | None = None

    @classmethod
    def from_tpf_reader(
        cls,
        reader: BinaryReader,
        platform: TPFPlatform,
        tpf_flags: int,
        encoding: str,
    ):
        texture_struct = TPFTextureStruct.from_bytes(reader)

        if platform != TPFPlatform.PC:
            width = reader["h"]
            height = reader["h"]
            header = TextureHeader(width, height)
            if platform == TPFPlatform.Xbox360:
                reader.assert_pad(4)
            elif platform == TPFPlatform.PS3:
                header.unk1 = reader["i"]
                if tpf_flags != 0:
                    header.unk2 = reader["i"]
                    if header.unk2 not in {0, 0x68E0, 0xAAE4}:
                        raise ValueError(
                            f"`TextureHeader.unk2` was {header.unk2}, but expected 0, 0x68E0, or 0xAAE4."
                        )
            elif platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
                header.texture_count = reader["i"]
                if header.texture_count not in {1, 6}:
                    f"`TextureHeader.texture_count` was {header.texture_count}, but expected 1 or 6."
                header.unk2 = reader["i"]
                if header.unk2 != 0xD:
                    f"`TextureHeader.unk2` was {header.unk2}, but expected 0xD."
            # `dxgi_format` unpacked below.
        else:
            header = None

        name_offset = reader["I"]
        has_unknown_float_struct = reader["i"] == 1
        if platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
            header.dxgi_format = DXGI_FORMAT(reader["i"])
        if has_unknown_float_struct:
            float_struct = TextureFloatStruct.from_bytes(reader)
            unknown_float_struct = (float_struct.unk0, float_struct.unpack_data(reader))
        else:
            unknown_float_struct = None

        with reader.temp_offset(texture_struct.pop("data_offset")):
            data = reader.read(texture_struct.pop("data_size"))
        if texture_struct.texture_flags in {2, 3}:
            # Data is DCX-compressed.
            # TODO: should enforce DCX type as 'DCP_EDGE'?
            data = decompress(data)

        name = reader.unpack_string(offset=name_offset, encoding=encoding)

        texture = texture_struct.to_object(
            cls,
            name=name,
            data=data,
            header=header,
            unknown_float_struct=unknown_float_struct,
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

        TPFTextureStruct.object_to_writer(
            self,
            writer,
            data_offset=RESERVED,
            data_size=RESERVED,
            texture_type=texture_type,
            mipmap_count=mipmap_count,
        )

        if platform != TPFPlatform.PC:
            writer.pack("h", self.header.width)
            writer.pack("h", self.header.height)
            if platform == TPFPlatform.Xbox360:
                writer.pad(4)
            elif platform == TPFPlatform.PS3:
                writer.pack("i", self.header.unk1)
                if tpf_flags != 0:
                    writer.pack("i", self.header.unk2)
            elif platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
                writer.pack("i", self.header.texture_count)
                writer.pack("i", self.header.unk2)

        writer.reserve("name_offset", "I", obj=self)
        writer.pack("i", 0 if self.unknown_float_struct is None else 1)

        if platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
            writer.pack("i", self.header.dxgi_format)

        if self.unknown_float_struct is not None:
            unk0, floats = self.unknown_float_struct
            TextureFloatStruct(unk0, len(floats) * 4).to_writer(writer)
            writer.pack(f"{len(floats) * 4}f", *floats)

    def pack_name(self, writer: BinaryWriter, encoding_type: int):
        writer.fill_with_position("name_offset", obj=self)
        if encoding_type == 1:  # UTF-16
            name = self.name.encode(encoding=writer.default_byte_order.get_utf_16_encoding()) + b"\0\0"
        elif encoding_type in {0, 2}:  # shift-jis
            name = self.name.encode(encoding="shift-jis") + b"\0"
        else:
            raise ValueError(f"Invalid TPF texture encoding: {encoding_type}. Must be 0, 1, or 2.")
        writer.append(name)

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

    def get_png_data(self, fmt="rgba", platform=TPFPlatform.PC) -> bytes:
        with tempfile.TemporaryDirectory() as png_dir:
            temp_dds_path = Path(png_dir, "temp.dds")

            if not self.data[:4] == b"DDS ":
                if not self.header:
                    raise TexconvError("Cannot convert headerless DDS texture to PNG without a `TPFTexture` header.")
                dds_data = bytes(self.get_headerized_dds(platform))
            else:
                dds_data = self.data  # already has header

            temp_dds_path.write_bytes(dds_data)
            Path("~/Documents/temp.dds").expanduser().write_bytes(dds_data)
            texconv_result = texconv("-o", png_dir, "-ft", "png", "-f", fmt, "-nologo", temp_dds_path)
            try:
                return Path(png_dir, "temp.png").read_bytes()
            except FileNotFoundError:
                stdout = texconv_result.stdout.decode()
                raise TexconvError(f"Could not convert texture DDS to PNG:\n    {stdout}")

    def export_png(self, png_path: str | Path, fmt="rgba", platform=TPFPlatform.PC):
        png_data = self.get_png_data(fmt, platform)
        png_path.write_bytes(png_data)

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
                    f"Converted TPF texture {self.name} from format {current_format} "
                    f"(DXGI {current_dxgi_format}) to {output_format}."
                )
            else:
                _LOGGER.info(f"Converted TPF texture {self.name} from format {current_format} to {output_format}.")
            return True
        else:
            _LOGGER.error(
                f"Could not convert TPF texture {self.name} from format {current_format} to {output_format}.\n"
                f"   stdout: {result.stdout}\n"
                f"   stderr: {result.stderr}"
            )
            return False

    def get_texture_format_info(
        self, platform=TPFPlatform.PC
    ) -> tuple[bytes, int, bool]:
        """Get `fourcc` code (four nulls if unused), bytes per block, and `is_compressed` for this `TPFTexture.format`.

        `dxgi_format` for DX10 headers is supplied by `TextureHeader.dxgi_format`.

        At least one format value (10) is known to be different between PC and console (R8G8B8 vs A8G8B8R8).
        """
        null = b"\0\0\0\0"
        match self.format:
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
                if platform == TPFPlatform.PS3:
                    return null, 4, False  # expected format: A8G8B8R8
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
                raise ValueError(f"Unknown TPF texture format value: {self.format}")

    def get_headerized_dds(self, platform=TPFPlatform.PC) -> DDS:
        """Generate automatic DDS headers for headerless console textures and pack them together.

        Requires `TPFTexture.header` to specify texture width, height, and (for DX10) `DXGI_FORMAT`.
        """
        width = self.header.width
        height = self.header.height

        fourcc, block_size, is_compressed = self.get_texture_format_info(platform)

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
        dds_header.byte_order = ByteOrder.LittleEndian

        if fourcc == b"DX10":
            dx10_header = DX10Header.get_default(self.header.dxgi_format)
            if self.texture_type == TextureType.Cubemap:
                dx10_header.misc_flag |= RESOURCE_MISC.TEXTURECUBE
        else:
            dx10_header = None

        # Deswizzle.
        dds_deswizzler = DDSDeswizzler(block_size, self.header.dxgi_format, pitch_or_linear_size, self.data)
        try:
            # TODO: I'm not certain if this algorithm deswizzles mipmaps as well. My suspicion is no, hence why BC7
            #  (format 102) doesn't work right now.
            data = dds_deswizzler.deswizzle_dds_bytes_ps4(width, height)
        except DDSDeswizzlerError as ex:
            raise DDSDeswizzlerError(
                f"Failed to deswizzle DDS texture {self.name} with TPF format {self.format}, width {width}, height "
                f"{height}, and DXGI_FORMAT {self.header.dxgi_format}. Internal error: {ex}"
            )

        return DDS(header=dds_header, dx10_header=dx10_header, data=data)

    def get_images(self, mipmap_count: int) -> list[DDSImage]:
        """TODO: Currently no use for this. Potentially useful to skip `texconv` altogether."""
        if not self.header:
            raise ValueError("Cannot only rebuild texture data for headerless DDS textures (with `TPFTexture` header).")
        width = self.header.width
        height = self.header.height
        texture_count = 6 if self.texture_type == TextureType.Cubemap else 1
        if texture_count != self.header.texture_count:
            raise ValueError(
                f"Texture type {self.texture_type.name} does not match `TextureHeader.texture_count` "
                f"{self.header.texture_count}. Cubemap DDS should contain 6 textures, and all others should contain 1."
            )
        pad_dimensions = 32 if self.format == 102 else 1

        _, block_size, is_compressed = self.get_texture_format_info()
        reader = BinaryReader(self.data)
        if is_compressed is not None:
            images = DDSImage.read_compressed_images(
                reader, width, height, pad_dimensions, texture_count, mipmap_count, 0x80, block_size
            )
        else:
            images = DDSImage.read_uncompressed_images(
                reader, width, height, pad_dimensions, texture_count, mipmap_count, 0x80, block_size
            )

        if self.format in {10, 102}:
            texel_size = 4 if self.format == 10 else 16
            for image in images:
                for i, mipmap_level in enumerate(image.mipmap_levels):
                    scale = 2 ** i
                    image.mipmap_levels[i] = self.deswizzle_mipmap_level(
                        mipmap_level, texel_size, width // scale, height // scale, pad_dimensions
                    )

        return images

    def _sf_deswizzle(self, images: list[DDSImage], width: int, height: int):
        """Deswizzle DDS `images` in-place."""

        padded_width = padded_height = padded_size = copy_offset = 0
        _, compressed_bpp, uncompressed_bpp = self.get_texture_format_info()
        block_size = compressed_bpp or uncompressed_bpp
        for image in images:
            current_width = width
            current_height = height
            for mipmap_level in image.mipmap_levels:
                if self.format == 105:
                    padded_width = current_width
                    padded_height = current_height
                    padded_size = padded_width * padded_height * block_size
                else:
                    padded_width = DDSImage.pad_to(current_width, 32)
                    padded_height = DDSImage.pad_to(current_height, 32)
                    padded_size = DDSImage.pad_to(padded_width, 4) * DDSImage.pad_to(padded_height, 4) * block_size

    def __repr__(self) -> str:
        return (
            f"TPFTexture(\n"
            f"    name = '{self.name}'\n"
            f"    format = {self.format}\n"
            f"    texture_type = {self.texture_type.name}\n"
            f"    mipmap_count = {self.mipmap_count}\n"
            f"    texture_flags = {self.texture_flags}\n"
            f"    data = <{len(self.data)} bytes>\n"
            f"    has_header = {self.header is not None}\n"
            f"    has_unknown_float_struct = {self.unknown_float_struct is not None}\n"
            f")"
        )


@dataclass(slots=True)
class TPFStruct(BinaryStruct):
    signature: bytes = field(**BinaryString(4, asserted=b"TPF\0"))
    _data_size: int
    file_count: int
    platform: TPFPlatform = field(**Binary(byte))
    tpf_flags: byte = field(**(Binary(asserted=[0, 1, 2, 3])))
    encoding_type: byte = field(**Binary(asserted=[0, 1, 2]))  # 2 == UTF_16, 0/1 == shift_jis_2004
    _pad1: bytes = field(**BinaryPad(1))


@dataclass(slots=True)
class TPF(GameFile):

    textures: list[TPFTexture] = field(default_factory=list)
    platform: TPFPlatform = TPFPlatform.PC
    encoding_type: int = 0
    tpf_flags: int = 0  # non-zero value on PS3 means textures have `unk2`; unknown otherwise

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> TPF:
        platform = TPFPlatform(reader["B", 0xC])
        reader.default_byte_order = ByteOrder.big_endian_bool(platform in {TPFPlatform.Xbox360, TPFPlatform.PS3})
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
    def from_unpacked_path(cls, path: str | Path) -> Self:
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
            dds_path = directory / f"{entry['name']}.dds"
            if not dds_path.is_file():
                raise FileNotFoundError(f"Could not find DDS file for TPF texture {entry['name']}: {dds_path}")
            textures.append(TPFTexture(
                name=entry["name"],
                format=entry["format"],
                texture_type=TextureType[entry["texture_type"]],
                mipmap_count=entry["mipmap_count"],
                texture_flags=entry["texture_flags"],
                data=dds_path.read_bytes(),
                header=TextureHeader(**entry["header"]) if entry.get("header", None) is not None else None,
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
            texture.pack_name(writer, self.encoding_type)

        data_start = writer.position
        for texture in self.textures:
            # TKGP notes: padding varies wildly across games, so don't worry about it too much.
            if len(texture.data) > 0:
                writer.pad_align(4)
            texture.pack_data(writer)
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
            if texture.header is not None:
                header_dict = {
                    "width": texture.header.width,
                    "height": texture.header.height,
                    "mipmaps": texture.header.texture_count,
                    "unk1": texture.header.unk1,
                    "unk2": texture.header.unk2,
                    "dxgi_format": texture.header.dxgi_format.name,
                }
            else:
                header_dict = None

            texture_dict = {
                "name": texture.name,
                "format": texture.format,
                "texture_type": texture.texture_type.name,
                "mipmap_count": texture.mipmap_count,
                "texture_flags": texture.texture_flags,
                "header": header_dict,
                "unknown_float_struct": texture.unknown_float_struct,
            }
            texture_entries.append(texture_dict)
            texture.write_dds(directory / f"{texture.name}.dds")
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

    def find_texture_name(self, name: str) -> TPFTexture:
        """Find texture by name."""
        for texture in self.textures:
            if texture.name == name:
                return texture
        raise ValueError(f"Could not find texture with name {name}.")

    def get_all_png_data(self, fmt="rgba") -> list[tp.Optional[bytes]]:
        png_datas = []
        for tex in self.textures:
            try:
                png_datas.append(tex.get_png_data(fmt))
            except ValueError as ex:
                _LOGGER.warning(str(ex))
                png_datas.append(None)
        return png_datas

    def export_to_pngs(self, png_dir_path: Path | str, fmt="rgba"):
        for tex in self.textures:
            png_name = Path(tex.name).with_suffix(".png")
            try:
                tex.export_png(png_dir_path / png_name, fmt=fmt, platform=self.platform)
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
                        textures[texture.name] = texture
        return textures


def get_png_data(tex: TPFTexture, fmt: str):
    try:
        return tex.get_png_data(fmt=fmt)
    except (TexconvError, DDSDeswizzlerError) as ex:
        _LOGGER.error(f"Failed to get TPF texture as PNG: {str(ex)}")
        return None


def batch_get_tpf_texture_png_data(
    tpf_textures: list[TPFTexture], fmt="rgba", processes: int = None
) -> list[bytes | None]:
    """Use multiprocessing to retrieve PNG data (converted from DDS) for a collection of `TPFTexture`s."""

    mp_args = [(tpf_texture, fmt) for tpf_texture in tpf_textures]

    with multiprocessing.Pool(processes=processes) as pool:
        png_data = pool.starmap(get_png_data, mp_args)  # blocks here until all done

    return png_data
