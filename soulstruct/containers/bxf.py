"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""
from __future__ import annotations

__all__ = ["BaseBXF", "BXF3", "BXF4"]

import abc
import logging
import typing as tp
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryReader, BinaryWriter, get_blake2b_hash

from .base import BaseBinder, BinderHashTable
from .dcx import DCX
from .entry import BinderEntryHeader, BinderEntry
from .flags import BinderFlags

_LOGGER = logging.getLogger(__name__)


class BaseBXF(BaseBinder, abc.ABC):

    def __init__(
        self,
        file_source: GameFile.Typing = None,
        bdt_source: GameFile.Typing = None,
        dcx_magic: tp.Tuple[int, int] = (),
    ):
        """Data archive that is basically a `BND` split into a `BHD` header file and `BDT` data file.

        If only `file_source` is given, it must be the path of a BHD file, BDT file, or previously unpacked directory.
        If it is a file, its type (`BHD` or `BDT`) will be identified and whichever file was NOT given will be located
        next to the given file. Otherwise, `bdt_source` can be used to explicitly load the BDT file from anywhere
        (though it would be unusual for it to be in a different folder) and both sources can be any of the standard
        `GameFile` supported types. Obviously, `file_source` must be the BHD in this case.

        The `path` of the instance will always be the BHD, not the BHD file.
        """
        if bdt_source is None:
            if not isinstance(file_source, (str, Path)):
                raise TypeError(
                    f"If BXF `header_source` is not given, `file_source` must be a file path, with its paired header "
                    f"or data file next to it (or it must be a previously unpacked BXF folder)."
                )
            file_source = Path(file_source)
            if file_source.is_dir() and (file_source / "binder_manifest.json").is_file():
                pass  # will be handled by parent class
            elif file_source.name.endswith("bhd"):
                bdt_source = file_source.with_name(file_source.name[:-3] + "bdt")
                if not bdt_source.is_file():
                    raise FileNotFoundError(f"Could not find BDT data file next to BHD header file: {file_source}")
            elif file_source.name.endswith("bdt"):
                bdt_source = file_source
                file_source = bdt_source.with_name(bdt_source.name[:-3] + "bhd")
                if not file_source.is_file():
                    raise FileNotFoundError(f"Could not find BHD header file next to BDT data file: {bdt_source}")
            else:
                raise ValueError(f"Could not tell if file source {file_source} is a BHD or BDT file.")

        super().__init__(file_source, dcx_magic=dcx_magic, bdt_source=bdt_source)

    @abc.abstractmethod
    def unpack_header(self, reader: BinaryReader) -> tp.List[BinderEntryHeader]:
        ...

    @abc.abstractmethod
    def unpack(self, reader: BinaryReader, bdt_source: GameFile.Typing = None):
        ...

    @abc.abstractmethod
    def pack_header(self, writer: BinaryWriter):
        ...

    @abc.abstractmethod
    def pack(self) -> tp.Tuple[bytes, bytes]:
        """Returns `BHD` bytes and `BDT` bytes."""

    def write(
        self,
        file_path: tp.Union[None, str, Path] = None,
        bdt_file_path: tp.Union[None, str, Path] = None,
        make_dirs=True,
        check_hash=False,
    ):
        """Writes both the `BHD` and `BDT` files at once.

        Missing directories in given path will be created automatically if `make_dirs` is True. Otherwise, they must
        already exist.

        Will compress with DCX automatically and add `.dcx` file extension if `.dcx_magic` is defined. Will also
        automatically create a `.bak` version of the `file_path`, if a backup does not already exist.

        Args:
            file_path (None, str, Path): file path to write `BHD` to. Defaults to `self.path`, which is automatically
                set at instance creation if a file path is used as a source.
            bdt_file_path (None, str, Path): file path to write `BDT` to. Defaults to `self.path` with "bdt"
                replacing "bhd", if a file path is used as a source.
            make_dirs (bool): if True, any absent directories in both `file_path` and `bdt_file_path` will be created.
            check_hash (bool): if True, files will not be written if both BHD and BDT files with same hashes already
                exist. (Default: False)
        """
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        if bdt_file_path is None:
            name_parts = file_path.name.split(".")
            bdt_name = name_parts[0] + "." + ".".join(name_parts[1:]).replace("bhd", "bdt")
            bdt_file_path = file_path.with_name(bdt_name)
        if make_dirs:
            bdt_file_path.parent.mkdir(parents=True, exist_ok=True)
        packed_bhd, packed_bdt = self.pack()
        if self.dcx_magic:
            # I haven't actually seen any BDT archives with DCX compression.
            packed_bhd = DCX(packed_bhd, magic=self.dcx_magic).pack()
            packed_bdt = DCX(packed_bdt, magic=self.dcx_magic).pack()
        if check_hash and file_path.is_file() and bdt_file_path.is_file():
            bhd_match = get_blake2b_hash(file_path) == get_blake2b_hash(packed_bhd)
            bdt_match = get_blake2b_hash(bdt_file_path) == get_blake2b_hash(packed_bdt)
            if bhd_match and bdt_match:
                return  # don't write file
        self.create_bak(file_path, make_dirs=make_dirs)
        self.create_bak(bdt_file_path, make_dirs=make_dirs)
        with file_path.open("wb") as f:
            f.write(packed_bhd)
        with bdt_file_path.open("wb") as f:
            f.write(packed_bdt)


class BXF3(BaseBXF):

    def unpack_header(self, reader: BinaryReader) -> tp.List[BinderEntryHeader]:
        self.big_endian = reader.unpack_value("?", offset=0xD)
        reader.byte_order = ">" if self.big_endian else "<"
        self.bit_big_endian = reader.unpack_value("?", offset=0xE)
        reader.unpack_value("4s", asserted=b"BHF3")
        self.signature = reader.unpack_value("8s").decode("ascii").rstrip("\0")
        self.flags = BinderFlags.read(reader, self.bit_big_endian)
        reader.byte_order = ">" if self.big_endian or self.flags.is_big_endian else "<"
        reader.seek(2, 1)  # skip peeked endian bytes
        reader.assert_pad(1)
        entry_count = reader.unpack_value("i")
        reader.seek(12, 1)  # skip file size
        return [
            BinderEntryHeader.from_bnd3_reader(reader, self.flags, self.bit_big_endian)
            for _ in range(entry_count)
        ]

    def unpack(self, reader: BinaryReader, bdt_source: GameFile.Typing = None):
        entry_headers = self.unpack_header(reader)
        bdt_reader = BinaryReader(bdt_source)
        bdt_reader.seek(0x10)  # skip useless BDT header
        for entry_header in entry_headers:
            self.add_entry(BinderEntry.from_header(bdt_reader, entry_header))

    def pack_header(self, writer: BinaryWriter):
        writer.append(b"BHF3")
        writer.pack("8s", self.signature.encode("ascii"))
        self.flags.pack(writer, self.bit_big_endian)
        writer.pack("?", self.big_endian)
        writer.pack("?", self.bit_big_endian)
        writer.pad(1)
        writer.pack("i", len(self._entries))
        writer.pad(12)

    def pack(self) -> tp.Tuple[bytes, bytes]:
        header_writer = BinaryWriter(big_endian=self.big_endian or self.flags.is_big_endian)
        data_writer = BinaryWriter(big_endian=self.big_endian or self.flags.is_big_endian)
        self.pack_header(header_writer)

        entries = list(sorted(self._entries, key=lambda e: e.id))
        entry_headers = [entry.get_header(self.flags) for entry in entries]
        for entry_header in entry_headers:
            entry_header.pack_bnd3(header_writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            for entry, entry_header in zip(entries, entry_headers):
                header_writer.fill("path_offset", header_writer.position, obj=entry_header)
                # NOTE: BND paths are *not* encoded in `shift_jis_2004`, unlike most other strings, but are `shift-jis`.
                # The relevant difference is that escaped backslashes are encoded as the yen symbol in `shift_jis_2004`.
                header_writer.append(entry.get_packed_path(encoding="shift-jis"))

        # Useless BDT3 header.
        data_writer.append(b"BDF3")
        data_writer.pack("8s", self.signature.encode("ascii"))
        data_writer.pad(4)

        for entry, entry_header in zip(entries, entry_headers):
            header_writer.fill("data_offset", data_writer.position, obj=entry_header)
            data_writer.append(entry.data)

        return header_writer.finish(), data_writer.finish()

    def get_json_header(self) -> tp.Dict[str, tp.Any]:
        return {
            "version": "BXF3",
            "signature": self.signature,
            "flags": self.flags,
            "big_endian": self.big_endian,
            "bit_big_endian": self.bit_big_endian,
            "use_id_prefix": self.has_repeated_entry_names,
            "dcx_magic": self.dcx_magic,
        }


class BXF4(BaseBXF):

    unknown1: bool
    unknown2: bool
    hash_table_type: int
    unicode: bool

    def __init__(
        self,
        file_source: GameFile.Typing = None,
        bdt_source: GameFile.Typing = None,
        dcx_magic: tp.Tuple[int, int] = (),
    ):
        self.unknown1 = False
        self.unknown2 = False
        self.hash_table_type = 0
        self.unicode = True
        self._most_recent_hash_table = b""
        super().__init__(file_source, bdt_source, dcx_magic)

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

        flags_header_size = self.flags.get_bnd_entry_header_size()
        if entry_header_size != flags_header_size:
            raise ValueError(
                f"Expected BND entry header size {flags_header_size} based on flags\n"
                f"{self.flags:08b}, but BND header says {entry_header_size}."
            )
        if self.hash_table_type != 4 and hash_table_offset != 0:
            _LOGGER.warning(
                f"Found non-zero hash table offset {hash_table_offset}, but header says this BHD has no hash "
                f"table."
            )

        entry_headers = [
            BinderEntryHeader.from_bnd4_reader(reader, self.flags, self.bit_big_endian, self.unicode)
            for _ in range(entry_count)
        ]

        if self.hash_table_type == 4:
            # Save the initial hash table.
            reader.seek(hash_table_offset)
            self._most_recent_hash_table = reader.read(data_offset - hash_table_offset)

        return entry_headers

    def unpack(self, reader: BinaryReader, bdt_source: GameFile.Typing = None):
        entry_headers = self.unpack_header(reader)
        bdt_reader = BinaryReader(bdt_source)
        bdt_reader.seek(0x30)  # skip useless BDT header
        for entry_header in entry_headers:
            self.add_entry(BinderEntry.from_header(bdt_reader, entry_header))

    def pack_header(self, writer: BinaryWriter):
        writer.append(b"BHF4")
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

    def pack(self) -> tp.Tuple[bytes, bytes]:
        header_writer = BinaryWriter(big_endian=self.big_endian or self.flags.is_big_endian)
        data_writer = BinaryWriter(big_endian=self.big_endian or self.flags.is_big_endian)
        self.pack_header(header_writer)

        path_encoding = ("utf-16-be" if self.big_endian else "utf-16-le") if self.unicode else "shift-jis"
        entries = list(sorted(self._entries, key=lambda e: e.id))

        rebuild_hash_table = not self._most_recent_hash_table
        if not self._most_recent_hash_table or len(entries) != self._most_recent_entry_count:
            rebuild_hash_table = True
        else:
            # Check if any entry paths have changed.
            for i, entry in enumerate(entries):
                if entry.path != self._most_recent_paths[i]:
                    rebuild_hash_table = True
                    break
        self._most_recent_entry_count = len(entries)
        self._most_recent_paths = [entry.path for entry in entries]

        entry_headers = [entry.get_header(self.flags) for entry in entries]
        for entry_header in entry_headers:
            entry_header.pack_bnd4(header_writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            for entry, entry_header in zip(entries, entry_headers):
                header_writer.fill("path_offset", header_writer.position, obj=entry_header)
                # NOTE: BND paths are *not* encoded in `shift_jis_2004`, unlike most other strings, but are `shift-jis`.
                # The relevant difference is that escaped backslashes are encoded as the yen symbol in `shift_jis_2004`.
                header_writer.append(entry.get_packed_path(encoding=path_encoding))

        if self.hash_table_type == 4:
            header_writer.fill("hash_table_offset", header_writer.position)
            if rebuild_hash_table:
                header_writer.append(BinderHashTable.build_hash_table(self._entries))
            else:
                header_writer.append(self._most_recent_hash_table)

        header_writer.fill("data_offset", header_writer.position)

        # Useless BDT4 header.
        data_writer.append(b"BDF4")
        data_writer.pack("?", self.unknown1)
        data_writer.pack("?", self.unknown2)
        data_writer.pad(3)
        data_writer.pack("?", self.big_endian)
        data_writer.pack("?", not self.bit_big_endian)
        data_writer.pad(5)
        data_writer.pack("q", 0x30)  # header size
        data_writer.pack("8s", self.signature.encode("ascii"))
        data_writer.pad(16)

        for entry, entry_header in zip(entries, entry_headers):
            header_writer.fill("data_offset", data_writer.position, obj=entry_header)
            data_writer.append(entry.data + b"\0" * 10)  # ten pad bytes between each entry (for byte-perfect writes)

        return header_writer.finish(), data_writer.finish()

    def get_json_header(self) -> tp.Dict[str, tp.Any]:
        return {
            "version": "BXF4",
            "signature": self.signature,
            "flags": self.flags,
            "big_endian": self.big_endian,
            "bit_big_endian": self.bit_big_endian,
            "unicode": self.unicode,
            "hash_table_type": self.hash_table_type,
            "unknown1": self.unknown1,
            "unknown2": self.unknown2,
            "use_id_prefix": self.has_repeated_entry_names,
            "dcx_magic": self.dcx_magic,
        }
