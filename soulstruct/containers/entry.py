"""Entry used in `BaseBinder` subclasses, including `BND` and `BXF`.

File is located here, rather than in `soulstruct.containers`, because it is both a valid `GameFile` source *and* one
element appearing inside `BaseBinder` subclass of `GameFile`, and must therefore be carefully placed to avoid circular
imports in Soulstruct.
"""
from __future__ import annotations

import typing as tp
import zlib
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path

from soulstruct.utilities.binary import *

if tp.TYPE_CHECKING:
    from soulstruct.base.base_binary_file import BASE_BINARY_FILE_T
    from .core import BinderFlags


class BinderEntryFlags(IntEnum):
    """Note that `SoulsFormats` represents these flags as big-endian, including in Yabber XML files. I have noted the
    comparative values next to each bit flag."""

    Compressed = 0b0000_0001  # BE: 0x80
    Flag1 = 0b0000_0010  # BE: 0x40
    Flag2 = 0b0000_0100  # BE: 0x20
    Flag3 = 0b0000_1000  # BE: 0x10
    Flag4 = 0b0001_0000  # BE: 0x08
    Flag5 = 0b0010_0000  # BE: 0x04
    Flag6 = 0b0100_0000  # BE: 0x02
    Flag7 = 0b1000_0000  # BE: 0x01

    @classmethod
    def is_compressed(cls, value: int):
        return value & cls.Compressed != 0  # big endian: 0x80

    @classmethod
    def from_byte(cls, byte_value: int, bit_big_endian: bool) -> int:
        """Read a byte, reverse its bits if necessary, and return integer flags."""
        if not bit_big_endian:
            # Reverse bit order.
            return int(f"{byte_value:08b}"[::-1], 2)
        return byte_value

    @classmethod
    def to_byte(cls, value: int, bit_big_endian: bool) -> int:
        """Reverse bits of `value` if necessary, and return it."""
        if not bit_big_endian:
            return int(f"{value:08b}"[::-1], 2)
        return value


@dataclass(slots=True)
class BinderEntryHeader:
    """Header for `BinderEntry`.

    Normally, these would be processed quietly and loaded straight into `BinderEntry` instances, but because BXF binders
    store the headers in a separate BHD file to the BDT data file, they have their own class here.

    NOTE: Does not use a `BinaryStruct` because the layout is too flexible, based on both binder and binder entry flags.
    """

    flags: int
    compressed_size: int
    entry_id: int | None = None
    path: str | None = None
    uncompressed_size: int | None = None
    data_offset: int = -1

    @classmethod
    def from_reader_v3(cls, reader: BinaryReader, binder_flags: BinderFlags, bit_big_endian: bool):
        flags = BinderEntryFlags.from_byte(reader["B"], bit_big_endian)
        reader.assert_pad(3)
        compressed_size = reader["i"]
        data_offset = reader["q" if binder_flags.has_long_offsets else "I"]
        entry_id = reader["i"] if binder_flags.has_ids else None
        if binder_flags.has_names:
            path_offset = reader["i"]
            path = reader.unpack_string(path_offset, encoding="shift-jis")  # NOT `shift_jis_2004`
        else:
            path = None
        uncompressed_size = reader["i"] if binder_flags.has_compression else None
        return cls(
            flags=flags,
            compressed_size=compressed_size,
            entry_id=entry_id,
            path=path,
            uncompressed_size=uncompressed_size,
            data_offset=data_offset,
        )

    def into_bnd3_writer(self, writer: BinaryWriter, binder_flags: BinderFlags, bit_big_endian: bool):
        writer.pack("B", BinderEntryFlags.to_byte(self.flags, bit_big_endian))
        writer.pad(3)
        writer.pack("i", self.compressed_size)
        writer.reserve("entry_data_offset", "q" if binder_flags.has_long_offsets else "I", obj=self)
        if binder_flags.has_ids:
            writer.pack("i", self.entry_id)
        if binder_flags.has_names:
            writer.reserve("entry_path_offset", "i", obj=self)
        if binder_flags.has_compression:
            writer.pack("i", self.uncompressed_size)

    @classmethod
    def from_reader_v4(cls, reader: BinaryReader, binder_flags: BinderFlags, bit_big_endian: bool, unicode: bool):
        flags = BinderEntryFlags.from_byte(reader["B"], bit_big_endian)
        reader.assert_pad(3)
        assert reader["i"] == -1
        compressed_size = reader["q"]
        uncompressed_size = reader["q"] if binder_flags.has_compression else None
        data_offset = reader["q" if binder_flags.has_long_offsets else "I"]
        entry_id = reader["i"] if binder_flags.has_ids else None
        if binder_flags.has_names:
            path_offset = reader["I"]
            path = reader.unpack_string(path_offset, encoding="utf-16-le" if unicode else "shift-jis")
        else:
            path = None
        return cls(
            flags=flags,
            compressed_size=compressed_size,
            entry_id=entry_id,
            path=path,
            uncompressed_size=uncompressed_size,
            data_offset=data_offset,
        )

    def into_bnd4_writer(self, writer: BinaryWriter, binder_flags: BinderFlags, bit_big_endian: bool):
        writer.pack("B", BinderEntryFlags.to_byte(self.flags, bit_big_endian))
        writer.pad(3)
        writer.pack("i", -1)
        writer.pack("q", self.compressed_size)
        if binder_flags.has_compression:
            writer.pack("q", self.uncompressed_size)
        writer.reserve("entry_data_offset", "q" if binder_flags.has_long_offsets else "I", obj=self)
        if binder_flags.has_ids:
            writer.pack("i", self.entry_id)
        if binder_flags.has_names:
            writer.reserve("entry_path_offset", "i", obj=self)

    def pack_path(self, header_writer: BinaryWriter, path_bytes: bytes):
        header_writer.fill("entry_path_offset", header_writer.position, obj=self)
        header_writer.append(path_bytes)

    def pack_data(self, header_writer: BinaryWriter, entry_writer: BinaryWriter, entry_data: bytes):
        header_writer.fill("entry_data_offset", entry_writer.position, obj=self)
        entry_writer.append(entry_data)


@dataclass(slots=True)
class BinderEntry:

    # Packed binary data, identical to what the unpacked file would look like (may be compressed).
    data: bytes
    # Index that may be used by the game engine to access the packed data.
    entry_id: int | None = None
    # Full internal 'path' (in most cases), encoded in UTF-16 or Shift-JIS with double backslashes.
    path: str | None = None
    # Only one bit flag's purpose is currently known (compression). Default seems stable across games and very common.
    flags: int = 0x2

    @classmethod
    def from_header(cls, binder_reader: BinaryReader, entry_header: BinderEntryHeader) -> BinderEntry:
        with binder_reader.temp_offset(entry_header.data_offset):
            data = binder_reader.read(entry_header.compressed_size)
        return cls(entry_id=entry_header.entry_id, path=entry_header.path, data=data, flags=entry_header.flags)

    def get_header(self, binder_flags: BinderFlags) -> BinderEntryHeader:
        return BinderEntryHeader(
            self.flags,
            self.data_size,
            self.entry_id,
            self.path,
            uncompressed_size=self.data_size if binder_flags.has_compression else len(self.get_uncompressed_data()),
            data_offset=-1,
        )

    def get_uncompressed_data(self) -> bytes:
        """Decompresses compressed data first, if appropriate."""
        return zlib.decompressobj().decompress(self.data) if BinderEntryFlags.is_compressed(self.flags) else self.data

    __bytes__ = get_uncompressed_data

    def set_uncompressed_data(self, data: bytes):
        """Compress data (with `zlib` level 7) before setting it to `.data` attribute, if appropriate."""
        self.data = zlib.compress(data, level=7) if BinderEntryFlags.is_compressed(self.flags) else data

    def set_from_binary_file(self, binary_file: BASE_BINARY_FILE_T):
        self.set_uncompressed_data(bytes(binary_file))

    def get_packed_path(self, encoding: str) -> bytes:
        """Encodes path and null-terminates."""
        terminator = b"\0\0" if encoding.replace("-", "").startswith("utf16") else b"\0"
        return self.path.encode(encoding) + terminator

    def set_path_name(self, new_name: str):
        """Update just the basename of `path`."""
        self.path = str(Path(self.path).parent.joinpath(new_name))

    def to_binary_file(self, binary_file_cls: type[BASE_BINARY_FILE_T]) -> BASE_BINARY_FILE_T:
        binary_file = binary_file_cls.from_bytes(self.get_uncompressed_data())
        binary_file.path = Path(self.path)
        return binary_file

    @property
    def id(self):
        """Legacy alias for `entry_id`."""
        return self.entry_id

    @id.setter
    def id(self, value):
        """Legacy alias for `entry_id`."""
        self.entry_id = value

    @property
    def data_size(self) -> int:
        return len(self.data)

    @property
    def name(self) -> str:
        return Path(self.path).name

    @property
    def stem(self) -> str:
        return Path(self.path).stem

    @property
    def minimal_stem(self) -> str:
        """Returns only the part of the path name before ANY dots, rather than only removing the final extension."""
        return Path(self.path).name.split(".")[0]

    @property
    def suffix(self) -> str:
        return Path(self.path).suffix

    @property
    def path_with_forward_slashes(self) -> str:
        return self.path.replace("\\", "/")

    @property
    def directory_with_forward_slashes(self) -> str:
        return str(Path(self.path).parent).replace("\\", "/")

    def copy(self) -> BinderEntry:
        return BinderEntry(data=self.data, entry_id=self.entry_id, path=self.path, flags=self.flags)

    def write(self, path: str | Path = None):
        if path is None:
            path = self.name  # relative path only
        Path(path).write_bytes(self.data)

    def __repr__(self):
        return f"BinderEntry({self.entry_id}, {hex(self.flags)}, \"{self.path}\", <{len(self.data)} bytes>)"
