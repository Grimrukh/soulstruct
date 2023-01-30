__all__ = ["BND"]

import enum
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.binder_entry import BinderEntryHeader, BinderEntry
from soulstruct.containers.base import *
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger(__name__)


class BNDVersion(enum.Enum):
    BND3 = 3  # used before Dark Souls 2 (2014)
    BND4 = 4  # used from Dark Souls 2 (2014) onwards


@dataclass(slots=True)
class BND3Header(BinaryStruct):
    version: bytes = field(init=False, metadata=fixed_bytes(4, asserted_value=b"BND3"))
    signature: str = field(metadata=fixed_str(8, "ASCII"))
    flags: byte
    big_endian: bool
    bit_big_endian: bool
    _pad1: bytes = field(init=False, metadata=pad(1))
    entry_count: int
    file_size: int
    _pad2: bytes = field(init=False, metadata=pad(8))

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian


@dataclass(slots=True)
class BND4Header(BinaryStruct):
    version: bytes = field(init=False, metadata=fixed_bytes(4, asserted_value=b"BND4"))
    unk1: bool
    unk2: bool
    _pad1: bytes = field(init=False, metadata=pad(3))
    big_endian: bool
    bit_little_endian: bool
    _pad2: bytes = field(init=False, metadata=pad(1))
    entry_count: int
    header_size: long = field(init=False, metadata=asserted(0x40))
    signature: str = field(metadata=fixed_str(8, "ASCII"))
    entry_header_size: long
    data_offset: long
    unicode: bool
    flags: byte
    hash_table_type: byte = field(metadata=asserted([0, 1, 4, 128]))
    _pad3: bytes = field(init=False, metadata=pad(5))
    hash_table_offset: long  # only non-zero if `hash_table_type = 4`

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian


class BND(BaseBinder):

    version: BNDVersion
    unicode: bool

    # BND4 only:
    bnd4_unknown1: bool
    bnd4_unknown2: bool
    bnd4_unicode: bool
    bnd4_hash_table_type: int
    _most_recent_hash_table: bytes = field(init=False, default=b"")
    _most_recent_entry_count: int = field(init=False, default=0)
    _most_recent_paths: list[str] = field(init=False, default_factory=lambda: [])

    def _unpack_bnd3(self, reader: BinaryReader):
        # Test for endianness is a little complicated, as `flags.is_big_endian` can override the header `big_endian`.
        self.big_endian, self.bit_big_endian = reader.unpack("??", offset=0xD)
        flags_fmt = ">B" if self.bit_big_endian else "<B"
        self.flags = BinderFlags.from_byte(reader.unpack_value(flags_fmt, offset=0xC), self.bit_big_endian)
        byte_order = ByteOrder.BigEndian if (self.big_endian or self.flags.is_big_endian) else ByteOrder.LittleEndian
        header = BND3Header.from_bytes(reader, byte_order=byte_order)
        self.signature = header.signature
        # `flags`, `big_endian`, and `bit_big_endian` already set manually above.
        self.bnd4_unknown1 = self.bnd4_unknown2 = self.bnd4_unicode = False
        self.bnd4_hash_table_type = 0
        entry_headers = [
            BinderEntryHeader.from_bnd3_reader(reader, self.flags, self.bit_big_endian)
            for _ in range(header.entry_count)
        ]
        for entry_header in entry_headers:
            self.add_entry(BinderEntry.from_header(reader, entry_header))

    def _unpack_bnd4(self, reader: BinaryReader):
        byte_order = BinaryCondition((0x9, 1), [(ByteOrder.BigEndian, b"\01"), (ByteOrder.LittleEndian, b"\00")])
        header = BND4Header.from_bytes(reader, byte_order=byte_order)  # type: BND4Header
        self.signature = header.signature
        self.flags = BinderFlags.from_byte(header.flags, not header.bit_little_endian)
        self.big_endian = header.big_endian
        self.bit_big_endian = not header.bit_little_endian  # reversed from BMD3
        self.bnd4_unicode = header.unicode
        self.bnd4_unknown1 = header.unk1
        self.bnd4_unknown2 = header.unk2
        self.bnd4_hash_table_type = header.hash_table_type
        flags_header_size = self.flags.get_bnd_entry_header_size()
        if header.entry_header_size != flags_header_size:
            raise ValueError(
                f"Expected BND entry header size {flags_header_size} based on flags\n"
                f"{self.flags:08b}, but BND header says {header.entry_header_size}."
            )
        if header.hash_table_type != 4 and header.hash_table_offset != 0:
            _LOGGER.warning(
                f"Found non-zero hash table offset {header.hash_table_offset}, but header says this BND4 has no "
                f"hash table."
            )
        entry_headers = [
            BinderEntryHeader.from_bnd4_reader(reader, self.flags, self.bit_big_endian, header.unicode)
            for _ in range(header.entry_count)
        ]
        for entry_header in entry_headers:
            self.add_entry(BinderEntry.from_header(reader, entry_header))

        if header.hash_table_type == 4:
            # Save the initial hash table.
            reader.seek(header.hash_table_offset)
            self._most_recent_hash_table = reader.read(header.data_offset - header.hash_table_offset)
        self._most_recent_entry_count = len(self._entries)
        self._most_recent_paths = [entry.path for entry in self._entries]

    def unpack(self, reader: BinaryReader):

        version = reader.peek(4)
        if version == b"BND3":
            self.version = BNDVersion.BND3
            self._unpack_bnd3(reader)
        elif version == b"BND4":
            self.version = BNDVersion.BND4
            self._unpack_bnd4(reader)
        else:
            raise ValueError(f"Could not detect BND version from first four bytes: {version}:")

    def pack(self, **kwargs) -> bytes:
        if self.version == BNDVersion.BND3:
            return self._pack_bnd3()
        elif self.version == BNDVersion.BND4:
            return self._pack_bnd4()
        else:
            raise ValueError(f"Cannot pack BND version: {self.version}")

    def _pack_bnd3(self) -> bytes:

        writer = BND3Header(
            signature=self.signature,
            flags=byte(self.flags.to_byte(self.bit_big_endian)),
            big_endian=self.big_endian,
            bit_big_endian=self.bit_big_endian,
            entry_count=len(self.entries),
            file_size=RESERVED(int),
        ).to_writer()

        entries = list(sorted(self._entries, key=lambda e: e.id))
        entry_headers = [entry.get_header(self.flags) for entry in entries]
        for entry_header in entry_headers:
            entry_header.pack_bnd3(writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            for entry, entry_header in zip(entries, entry_headers):
                writer.fill("path_offset", writer.position, obj=entry_header)
                # NOTE: BND paths are *not* encoded in `shift_jis_2004`, unlike most other strings, but are
                # `shift-jis`. The relevant difference is that escaped backslashes are decoded to the yen symbol in
                # `shift_jis_2004`, which we do not want in these files.
                writer.append(entry.get_packed_path(encoding="shift-jis"))

        for entry, entry_header in zip(entries, entry_headers):
            writer.fill("data_offset", writer.position, obj=entry_header)
            writer.append(entry.data)

        writer.fill("file_size", writer.position)

        return writer.finish()

    def _pack_bnd4(self) -> bytes:

        writer = BND4Header(
            unk1=self.bnd4_unknown1,
            unk2=self.bnd4_unknown2,
            big_endian=self.big_endian,
            bit_little_endian=not self.bit_big_endian,  # reversed
            entry_count=len(self._entries),
            signature=self.signature,
            entry_header_size=long(self.flags.get_bnd_entry_header_size()),
            data_offset=RESERVED(long),
            unicode=self.bnd4_unicode,
            flags=byte(self.flags.to_byte(self.bit_big_endian)),
            hash_table_type=byte(self.bnd4_hash_table_type),
            hash_table_offset=RESERVED(long),  # only non-zero for hash table type 4
        ).to_writer()

        path_encoding = writer.get_utf_16_encoding() if self.bnd4_unicode else "shift-jis"
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
                # NOTE: BND paths are *not* encoded in `shift_jis_2004`, unlike most other strings, but are
                # `shift-jis`. The relevant difference is that escaped backslashes are decoded to the yen symbol in
                # `shift_jis_2004`, which we do not want in these files.
                writer.append(entry.get_packed_path(encoding=path_encoding))

        if self.bnd4_hash_table_type == 4:
            writer.fill("hash_table_offset", writer.position)
            if rebuild_hash_table:
                writer.append(BinderHashTable.build_hash_table(self._entries))
            else:
                writer.append(self._most_recent_hash_table)
        else:
            writer.fill("hash_table_offset", 0)

        writer.fill("data_offset", writer.position)

        for entry, entry_header in zip(entries, entry_headers):
            writer.fill("data_offset", writer.position, obj=entry_header)
            writer.append(entry.data + b"\0" * 10)  # ten pad bytes between each entry (for byte-perfect writes)

        return writer.finish()

    def get_json_header(self) -> dict[str, tp.Any]:
        if self.version == BNDVersion.BND3:
            return {
                "version": "BND3",
                "signature": self.signature,
                "flags": self.flags,
                "big_endian": self.big_endian,
                "bit_big_endian": self.bit_big_endian,
                "use_id_prefix": self.has_repeated_entry_names,
                "dcx_type": self.dcx_type.value,
            }
        elif self.version == BNDVersion.BND4:
            return {
                "version": "BND4",
                "signature": self.signature,
                "flags": self.flags,
                "big_endian": self.big_endian,
                "bit_big_endian": self.bit_big_endian,
                "unicode": self.bnd4_unicode,
                "hash_table_type": self.bnd4_hash_table_type,
                "unknown1": self.bnd4_unknown1,
                "unknown2": self.bnd4_unknown2,
                "use_id_prefix": self.has_repeated_entry_names,
                "dcx_type": self.dcx_type.value,
            }
        else:
            raise TypeError(f"Invalid BND version: {self.version}")

    # TODO: Not a huge fan of overriding a class method with an instance method?
    def _get_manifest_fields(self):
        if self.version == BNDVersion.BND3:
            return (
                "version",
                "signature",
                "flags",
                "big_endian",
                "bit_big_endian",
                "dcx_type",
            )
        elif self.version == BNDVersion.BND4:
            return (
                "version",
                "signature",
                "flags",
                "big_endian",
                "bit_big_endian",
                "dcx_type",
                "unicode",
                "hash_table_type",
                "unknown1",
                "unknown2",
            )
