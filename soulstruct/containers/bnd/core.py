"""NOTE: This file is Python 3.9 compatible for Blender 3.X use."""
__all__ = ["BaseBND", "BND3", "BND4"]

import abc
import logging
import typing as tp

from soulstruct.base.binder_entry import BinderEntryHeader, BinderEntry
from soulstruct.containers.base import BaseBinder, BinderHashTable, BinderFlags
from soulstruct.utilities.binary import BinaryStruct, BinaryReader, BinaryWriter

_LOGGER = logging.getLogger(__name__)


class BaseBND(BaseBinder, abc.ABC):
    """No additional data."""


class BND3(BaseBND):
    """BND used before Dark Souls 2 (2014)."""

    # Not actually used, but here for reference.
    HEADER_STRUCT = BinaryStruct(
        ("version", "4s", b"BND3"),
        ("signature", "8s"),
        ("flags", "b"),
        ("big_endian", "?"),
        ("bit_big_endian", "?"),
        "x",
        ("entry_count", "i"),
        ("file_size", "i"),
        "8x",
    )

    # No extra `MANIFEST_FIELDS`.

    def unpack_header(self, reader: BinaryReader) -> int:
        self.big_endian = reader.unpack_value("?", offset=0xD)
        reader.byte_order = ">" if self.big_endian else "<"
        self.bit_big_endian = reader.unpack_value("?", offset=0xE)
        reader.unpack_value("4s", asserted=b"BND3")
        self.signature = reader.unpack_value("8s").decode("ascii").rstrip("\0")
        self.flags = BinderFlags.read(reader, self.bit_big_endian)
        reader.byte_order = ">" if self.big_endian or self.flags.is_big_endian else "<"
        reader.seek(2, 1)  # skip peeked endian bytes
        reader.assert_pad(1)
        entry_count = reader.unpack_value("i")
        reader.seek(12, 1)  # skip file size
        return entry_count

    def unpack(self, reader: BinaryReader, **kwargs):
        entry_count = self.unpack_header(reader)

        entry_headers = [
            BinderEntryHeader.from_bnd3_reader(reader, self.flags, self.bit_big_endian)
            for _ in range(entry_count)
        ]
        for entry_header in entry_headers:
            self.add_entry(BinderEntry.from_header(reader, entry_header))

    def pack_header(self, writer: BinaryWriter):
        writer.append(b"BND3")
        writer.pack("8s", self.signature.encode("ascii"))
        self.flags.pack(writer, self.bit_big_endian)
        writer.pack("?", self.big_endian)
        writer.pack("?", self.bit_big_endian)
        writer.pad(1)
        writer.pack("i", len(self._entries))
        writer.reserve("file_size", "i")
        writer.pad(8)

    def pack(self) -> bytes:
        writer = BinaryWriter(big_endian=self.big_endian or self.flags.is_big_endian)
        self.pack_header(writer)

        entries = list(sorted(self._entries, key=lambda e: e.id))
        entry_headers = [entry.get_header(self.flags) for entry in entries]
        for entry_header in entry_headers:
            entry_header.pack_bnd3(writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            for entry, entry_header in zip(entries, entry_headers):
                writer.fill("path_offset", writer.position, obj=entry_header)
                # NOTE: BND paths are *not* encoded in `shift_jis_2004`, unlike most other strings, but are `shift-jis`.
                # The relevant difference is that escaped backslashes are encoded as the yen symbol in `shift_jis_2004`.
                writer.append(entry.get_packed_path(encoding="shift-jis"))

        for entry, entry_header in zip(entries, entry_headers):
            writer.fill("data_offset", writer.position, obj=entry_header)
            writer.append(entry.data)

        writer.fill("file_size", writer.position)

        return writer.finish()

    def get_json_header(self) -> dict[str, tp.Any]:
        return {
            "version": "BND3",
            "signature": self.signature,
            "flags": self.flags,
            "big_endian": self.big_endian,
            "bit_big_endian": self.bit_big_endian,
            "use_id_prefix": self.has_repeated_entry_names,
            "dcx_type": self.dcx_type,
        }


class BND4(BaseBND):
    """BND used since Dark Souls 2 (2014)."""

    # Not actually used, but here for reference.
    HEADER_STRUCT = BinaryStruct(
        ("version", "4s", b"BND4"),
        ("unknown1", "?"),
        ("unknown2", "?"),
        "3x",
        ("big_endian", "?"),
        ("bit_little_endian", "?"),  # note reversal
        "x",
        ("entry_count", "i"),
        ("header_size", "q", 0x40),
        ("signature", "8s"),  # Real signature may be shorter, but packing will pad it out.
        ("entry_header_size", "q"),
        ("data_offset", "q"),
        ("unicode", "?"),
        ("flags", "b"),
        ("hash_table_type", "B"),  # 0, 1, 4, or 128
        "5x",
        ("hash_table_offset", "q"),  # only non-zero if hash_table_type == 4
    )

    MANIFEST_FIELDS = BaseBinder.MANIFEST_FIELDS + (
        "unicode",
        "hash_table_type",
        "unknown1",
        "unknown2",
    )

    unknown1: bool
    unknown2: bool
    unicode: bool
    hash_table_type: int

    def __init__(self, file_source=None, dcx_type=None):
        self.unknown1 = False
        self.unknown2 = False
        self.unicode = False  # If False, paths are written in Shift-JIS.
        self.hash_table_type = 0

        self._most_recent_hash_table = b""
        self._most_recent_entry_count = 0
        self._most_recent_paths = []

        super().__init__(file_source=file_source, dcx_type=dcx_type)

    def unpack_header(self, reader: BinaryReader):
        reader.unpack_value("4s", asserted=b"BND4")
        self.unknown1 = reader.unpack_value("?")
        self.unknown2 = reader.unpack_value("?")
        reader.assert_pad(3)
        self.big_endian = reader.unpack_value("?")
        self.bit_big_endian = not reader.unpack_value("?")  # note reversal
        reader.assert_pad(1)

        reader.byte_order = ">" if self.big_endian else "<"  # no need to check flags for an override in BND4

        entry_count = reader.unpack_value("i")
        reader.unpack_value("q", asserted=0x40)  # header size
        self.signature = reader.unpack_value("8s").decode("ascii").rstrip("\0")
        entry_header_size = reader.unpack_value("q")
        data_offset = reader.unpack_value("q")  # end of all headers, including hash table
        self.unicode = reader.unpack_value("?")
        self.flags = BinderFlags.read(reader, self.bit_big_endian)
        self.hash_table_type = reader.unpack_value("B")
        reader.assert_pad(5)
        hash_table_offset = reader.unpack_value("q")

        return entry_count, entry_header_size, hash_table_offset, data_offset

    def unpack(self, reader: BinaryReader, **kwargs):
        entry_count, entry_header_size, hash_table_offset, data_offset = self.unpack_header(reader)

        flags_header_size = self.flags.get_bnd_entry_header_size()
        if entry_header_size != flags_header_size:
            raise ValueError(
                f"Expected BND entry header size {flags_header_size} based on flags\n"
                f"{self.flags:08b}, but BND header says {entry_header_size}."
            )
        if self.hash_table_type != 4 and hash_table_offset != 0:
            _LOGGER.warning(
                f"Found non-zero hash table offset {hash_table_offset}, but header says this BND has no hash "
                f"table."
            )

        entry_headers = [
            BinderEntryHeader.from_bnd4_reader(reader, self.flags, self.bit_big_endian, self.unicode)
            for _ in range(entry_count)
        ]
        for entry_header in entry_headers:
            self.add_entry(BinderEntry.from_header(reader, entry_header))

        if self.hash_table_type == 4:
            # Save the initial hash table.
            reader.seek(hash_table_offset)
            self._most_recent_hash_table = reader.read(data_offset - hash_table_offset)
        self._most_recent_entry_count = len(self._entries)
        self._most_recent_paths = [entry.path for entry in self._entries]

    def pack_header(self, writer: BinaryWriter):
        writer.append(b"BND4")
        writer.pack("?", self.unknown1)
        writer.pack("?", self.unknown2)
        writer.pad(3)
        writer.pack("?", self.big_endian)
        writer.pack("?", not self.bit_big_endian)  # note reversal
        writer.pad(1)

        writer.pack("i", len(self._entries))
        writer.pack("q", 0x40)  # header size
        writer.pack("8s", self.signature.encode("ascii"))
        writer.pack("q", self.flags.get_bnd_entry_header_size())
        writer.reserve("data_offset", "q")
        writer.pack("?", self.unicode)
        self.flags.pack(writer, self.bit_big_endian)
        writer.pack("B", self.hash_table_type)
        writer.pad(5)
        if self.hash_table_type == 4:
            writer.reserve("hash_table_offset", "q")
        else:
            writer.pad(8)

    def pack(self) -> bytes:
        writer = BinaryWriter(big_endian=self.big_endian)
        self.pack_header(writer)

        path_encoding = ("utf-16-be" if self.big_endian else "utf-16-le") if self.unicode else "shift-jis"
        rebuild_hash_table = not self._most_recent_hash_table

        if not self._most_recent_hash_table or len(self._entries) != self._most_recent_entry_count:
            rebuild_hash_table = True
        else:
            # Check if any entry paths have changed.
            for i, entry in enumerate(self._entries):
                if entry.path != self._most_recent_paths[i]:
                    rebuild_hash_table = True
                    break

        self._most_recent_entry_count = len(self._entries)
        self._most_recent_paths = [entry.path for entry in self._entries]

        entries = list(sorted(self._entries, key=lambda e: e.id))
        entry_headers = [entry.get_header(self.flags) for entry in entries]
        for entry_header in entry_headers:
            entry_header.pack_bnd4(writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            for entry, entry_header in zip(entries, entry_headers):
                writer.fill("path_offset", writer.position, obj=entry_header)
                # NOTE: BND paths are *not* encoded in `shift_jis_2004`, unlike most other strings, but are `shift-jis`.
                # The relevant difference is that escaped backslashes are encoded as the yen symbol in `shift_jis_2004`.
                writer.append(entry.get_packed_path(encoding=path_encoding))

        if self.hash_table_type == 4:
            writer.fill("hash_table_offset", writer.position)
            if rebuild_hash_table:
                writer.append(BinderHashTable.build_hash_table(self._entries))
            else:
                writer.append(self._most_recent_hash_table)

        writer.fill("data_offset", writer.position)

        for entry, entry_header in zip(entries, entry_headers):
            writer.fill("data_offset", writer.position, obj=entry_header)
            writer.append(entry.data + b"\0" * 10)  # ten pad bytes between each entry (for byte-perfect writes)

        return writer.finish()

    def get_json_header(self) -> dict[str, tp.Any]:
        return {
            "version": "BND4",
            "signature": self.signature,
            "flags": self.flags,
            "big_endian": self.big_endian,
            "bit_big_endian": self.bit_big_endian,
            "unicode": self.unicode,
            "hash_table_type": self.hash_table_type,
            "unknown1": self.unknown1,
            "unknown2": self.unknown2,
            "use_id_prefix": self.has_repeated_entry_names,
            "dcx_type": self.dcx_type,
        }
