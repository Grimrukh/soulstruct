"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""

from __future__ import annotations

import typing as tp
import zlib
from pathlib import Path

from .flags import BinderFlags, BinderEntryFlags

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryReader, BinaryWriter


class BinderEntryHeader:
    """Header for `BinderEntry`.

    Normally, these would be processed quietly and loaded straight into `BinderEntry` instances, but because BXF binders
    store the headers in a separate BHD file to the BDT data file, they have their own class here.
    """

    flags: BinderEntryFlags
    compressed_size: int
    id: tp.Optional[int]
    path: tp.Optional[str]
    uncompressed_size: tp.Optional[int]
    data_offset: int

    def __init__(self, flags, compressed_size, entry_id=None, path=None, uncompressed_size=None, data_offset=-1):
        self.flags = BinderEntryFlags(flags)
        self.compressed_size = compressed_size
        self.id = entry_id
        self.path = path
        self.uncompressed_size = uncompressed_size
        self.data_offset = data_offset

    @classmethod
    def from_bnd3_reader(cls, reader: BinaryReader, binder_flags: BinderFlags, bit_big_endian: bool):
        flags = BinderEntryFlags.read(reader, bit_big_endian)
        reader.assert_pad(3)
        compressed_size = reader.unpack_value("i")
        data_offset = reader.unpack_value("q" if binder_flags.has_long_offsets else "I")
        entry_id = reader.unpack_value("i") if binder_flags.has_ids else None
        if binder_flags.has_names:
            path_offset = reader.unpack_value("i")
            path = reader.unpack_string(path_offset, encoding="shift-jis")  # NOT `shift_jis_2004`
        else:
            path = None
        uncompressed_size = reader.unpack_value("i") if binder_flags.has_compression else None
        return cls(
            flags=flags,
            compressed_size=compressed_size,
            entry_id=entry_id,
            path=path,
            uncompressed_size=uncompressed_size,
            data_offset=data_offset,
        )

    def pack_bnd3(self, writer: BinaryWriter, binder_flags: BinderFlags, bit_big_endian: bool):
        self.flags.pack(writer, bit_big_endian)
        writer.pad(3)
        writer.pack("i", self.compressed_size)
        writer.reserve("data_offset", "q" if binder_flags.has_long_offsets else "I", obj=self)
        if binder_flags.has_ids:
            writer.pack("i", self.id)
        if binder_flags.has_names:
            writer.reserve("path_offset", "i", obj=self)
        if binder_flags.has_compression:
            writer.pack("i", self.uncompressed_size)

    @classmethod
    def from_bnd4_reader(cls, reader: BinaryReader, binder_flags: BinderFlags, bit_big_endian: bool, unicode: bool):
        flags = BinderEntryFlags.read(reader, bit_big_endian)
        reader.assert_pad(3)
        assert reader.unpack_value("i") == -1
        compressed_size = reader.unpack_value("q")
        uncompressed_size = reader.unpack_value("q") if binder_flags.has_compression else None
        data_offset = reader.unpack_value("q" if binder_flags.has_long_offsets else "I")
        entry_id = reader.unpack_value("i") if binder_flags.has_ids else None
        if binder_flags.has_names:
            path_offset = reader.unpack_value("I")
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

    def pack_bnd4(self, writer: BinaryWriter, binder_flags: BinderFlags, bit_big_endian: bool):
        self.flags.pack(writer, bit_big_endian)
        writer.pad(3)
        writer.pack("i", -1)
        writer.pack("q", self.compressed_size)
        if binder_flags.has_compression:
            writer.pack("q", self.uncompressed_size)
        writer.reserve("data_offset", "q" if binder_flags.has_long_offsets else "I", obj=self)
        if binder_flags.has_ids:
            writer.pack("i", self.id)
        if binder_flags.has_names:
            writer.reserve("path_offset", "i", obj=self)


class BinderEntry:

    def __init__(self, data: bytes, entry_id: int = None, path: str = None, flags=0x40):
        self.data = data  # packed binary data, identical to what the unpacked file would look like (may be compressed)
        self.id = entry_id  # index that may be used by the game engine to access the packed data
        self.path = path  # full internal 'path' (in most cases), encoded in UTF-16 or Shift-JIS with double backslashes
        self.flags = BinderEntryFlags(flags)  # only one bit flag is currently known (compression)

    @classmethod
    def from_header(cls, binder_reader: BinaryReader, entry_header: BinderEntryHeader) -> BinderEntry:
        with binder_reader.temp_offset(entry_header.data_offset):
            data = binder_reader.read(entry_header.compressed_size)
        return cls(entry_id=entry_header.id, path=entry_header.path, data=data, flags=entry_header.flags)

    def get_header(self, binder_flags: BinderFlags) -> BinderEntryHeader:
        return BinderEntryHeader(
            self.flags,
            self.data_size,
            self.id,
            self.path,
            uncompressed_size=self.data_size if binder_flags.has_compression else len(self.get_uncompressed_data()),
            data_offset=-1,
        )

    def get_uncompressed_data(self) -> bytes:
        """Decompresses compressed data first, if appropriate."""
        return zlib.decompressobj().decompress(self.data) if self.flags.is_compressed else self.data

    def set_uncompressed_data(self, data: bytes):
        """Compress data (with `zlib` level 7) before setting it to `.data` attribute, if appropriate."""
        self.data = zlib.compress(data, level=7) if self.flags.is_compressed else data

    def get_packed_path(self, encoding) -> bytes:
        """Encodes path and null-terminates."""
        return self.path.encode(encoding) + b"\0"

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
    def path_with_forward_slashes(self) -> str:
        return self.path.replace("\\", "/")

    @property
    def directory_with_forward_slashes(self) -> str:
        return str(Path(self.path).parent).replace("\\", "/")

    def copy(self) -> BinderEntry:
        return BinderEntry(data=self.data, entry_id=self.id, path=self.path, flags=self.flags)

    def __eq__(self, other_bnd_entry) -> bool:
        return all(getattr(self, field) == getattr(other_bnd_entry, field) for field in ("id", "path", "magic", "data"))
