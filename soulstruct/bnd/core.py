import abc
import copy
import logging
import re
import zlib
import typing as tp
from ast import literal_eval
from io import BytesIO, IOBase
from pathlib import Path

from soulstruct.bnd.magic import *
from soulstruct.dcx import DCX
from soulstruct.utilities.core import BinaryStruct, read_chars_from_buffer, find_dcx, create_bak

__all__ = ["BND", "BND3", "BND4", "BaseBND", "BNDEntry"]
_LOGGER = logging.getLogger(__name__)


class BNDEntry:

    # Header struct is computed in BND, as it is constant across entries in the same BND.

    def __init__(self, data: bytes, entry_id: int = None, path: str = None, magic=0x40):
        self.data = data  # Packed binary data, identical to what the unpacked file would look like.
        self.id = entry_id  # Index used by the game engine to access the packed data (in most cases).
        self.path = path  # Full internal 'path' (in most cases). Encoded in shift_jis_2004 with escaped backslashes.
        self.magic = magic  # Defaults to 0x40, which seems to be used in DS1/DS3 at least.

    @classmethod
    def unpack(cls, bnd_buffer, entry_header_struct, path_encoding, count):

        entry_headers = []
        entry_header_dicts = entry_header_struct.unpack_count(bnd_buffer, count=count)

        for d in entry_header_dicts:
            bnd_buffer.seek(d.data_offset)
            path = (
                read_chars_from_buffer(bnd_buffer, offset=d.path_offset, encoding=path_encoding)
                if "path_offset" in d
                else None
            )
            data = bnd_buffer.read(d.compressed_data_size)
            if is_entry_compressed(d.entry_magic):
                data = zlib.decompressobj().decompress(data)
            entry_headers.append(cls(entry_id=d.get("entry_id", None), path=path, data=data, magic=d.entry_magic))

        return entry_headers

    def get_data_for_pack(self):
        """ Compresses data first if appropriate. Returns (data, is_compressed). """
        if is_entry_compressed(self.magic):
            return zlib.compress(self.data, level=7), True
        else:
            return self.data, False

    @property
    def data_size(self):
        return len(self.data)

    def get_packed_path(self, encoding):
        """ Encodes path in Japanese and null-terminates. """
        return self.path.encode(encoding) + b"\x00"

    @property
    def name(self):
        return Path(self.path).name

    @property
    def stem(self):
        return Path(self.path).stem

    @property
    def path_with_forward_slashes(self):
        return self.path.replace("\\", "/")

    @property
    def directory_with_forward_slashes(self):
        return str(Path(self.path).parent).replace("\\", "/")

    def __eq__(self, other_bnd_entry):
        return self.id == other_bnd_entry.id and self.path == other_bnd_entry.path and self.data == other_bnd_entry.data

    def copy(self):
        return BNDEntry(self.data, self.id, self.path)


class BaseBND(abc.ABC):

    UNPACKED_PATH_RE = re.compile(rb"\((\d*)\) (.*)")
    UNPACKED_ID_PATH_RE = re.compile(rb"\((\d*)\) (\d*): (.*)")

    binary_entries: tp.List[BNDEntry]

    def __init__(self, bnd_source=None, entry_class=None):
        """Load a BND.

        Source can be a .*bnd file, an unpacked BND directory (or the 'bnd_manifest.txt' file inside it), raw bytes,
        or an open data stream (or None to create an empty BND).

        If an entry class is given, all entry data will be passed to that class to create instances of it. The paths and
        IDs of the entries will be maintained in self.binary_entries, but the data of these entries will be overwritten
        with packed versions of the classed entry instances when the BND is packed. (Until then, any edited entry
        instances will diverge from the original binary entry data.)
        """
        self.header_struct = None
        self.entry_header_struct = None

        self.bnd_path = Path()  # Always a '.bnd' file Path after the BND is loaded.
        self.bnd_version = b""
        self.bnd_signature = b""
        self.bnd_magic = None  # Can't guess this; you'll need to specify it based on your BND type.
        self.big_endian = False
        self.dcx = ()  # Pair of DCX magic values, or empty tuple to not use DCX.

        self._entry_class = entry_class
        self._most_recent_hash_table = b""
        self._most_recent_entry_count = 0
        self._most_recent_paths = []

        self.binary_entries = []  # Always stores binary (unpacked) entries. Only updated when pack() is called.
        self._entries = []  # List of entries, instantiated with given entry class (or left as binary).

        if isinstance(bnd_source, (str, Path)):
            bnd_path = Path(bnd_source)
            if bnd_path.is_file() and bnd_path.name == "bnd_manifest.txt":
                bnd_path = bnd_path.parent
            if bnd_path.is_dir():
                if bnd_path.suffix == ".unpacked":
                    self.bnd_path = bnd_path.parent.absolute() / bnd_path.stem
                else:
                    self.bnd_path = Path(bnd_path).absolute()
                self.load_unpacked_dir(bnd_path)
            else:
                self.bnd_path = bnd_path.absolute()
                if bnd_path.suffix == ".dcx":
                    bnd_dcx = DCX(bnd_path)
                    self.unpack(bnd_dcx.data)
                    self.dcx = bnd_dcx.magic
                else:
                    with open(bnd_path, "rb") as file:
                        self.unpack(file)
        elif bnd_source is not None:
            self.unpack(bnd_source)

    @abc.abstractmethod
    def unpack(self, bnd_buffer):
        ...

    @abc.abstractmethod
    def pack(self):
        ...

    @abc.abstractmethod
    def load_unpacked_dir(self, directory):
        ...

    def add_entries_from_manifest_paths(self, file_buffer, directory):
        directory = Path(directory)
        current_directory = None
        for line in file_buffer:
            line = line.strip(b" \r\n\t")
            if not line:
                # Skip blank lines.
                continue
            if line.startswith(b"PATH:"):
                current_directory = line[5:].strip().replace(b"/", b"\\").decode("shift_jis_2004").strip("\r\n")
            else:
                if has_id(self.bnd_magic):
                    try:
                        entry_magic, entry_id, entry_basename = self.UNPACKED_ID_PATH_RE.match(line).group(1, 2, 3)
                    except (AttributeError, ValueError):
                        raise ValueError(f"Expected '(magic) ID: path' format for entry, based on magic. Received:\n"
                                         f"    {line}")
                    entry_magic, entry_id = int(entry_magic), int(entry_id)
                else:
                    if b": " in line:
                        raise ValueError("Expected simply '(magic) path', not '(magic) ID: path', based on magic.")
                    entry_id = None
                    entry_magic, entry_basename = self.UNPACKED_PATH_RE.match(line).group(1, 2)
                    entry_magic = int(entry_magic)
                entry_basename_jis = entry_basename.decode("shift_jis_2004").strip("\r\n")
                entry_path = "\\".join((current_directory, entry_basename_jis))

                with (directory / entry_basename_jis).open("rb") as entry_file:
                    entry_data = entry_file.read()

                self.add_entry(BNDEntry(entry_id=entry_id, path=entry_path, data=entry_data, magic=entry_magic))

    def write(self, bnd_path=None):
        if bnd_path is None:
            bnd_path = self.bnd_path
        else:
            bnd_path = Path(bnd_path)
            if self.dcx and bnd_path.suffix != ".dcx":
                bnd_path = bnd_path.with_suffix(bnd_path.suffix + ".dcx")
        bnd_path.parent.mkdir(parents=True, exist_ok=True)
        create_bak(bnd_path)
        packed = self.pack()

        if self.dcx:
            # Apply DCX compression.
            packed = DCX(packed, magic=self.dcx).pack()

        with bnd_path.open("wb") as f:
            f.write(packed)

    def write_unpacked_dir(self, directory=None):
        if not has_path(self.bnd_magic):
            raise TypeError("Writing unpacked BND directories is only supported when BND entries have path strings.")
        if directory is None:
            if self.bnd_path:
                directory = self.bnd_path.with_suffix(self.bnd_path.suffix + ".unpacked")
            else:
                raise ValueError("Cannot set automatic unpacked BND directory name.")
        else:
            directory = Path(directory, self.bnd_path.name + ".unpacked")

        current_directory = ""
        manifest_lines = []

        for entry in self.binary_entries:
            entry_directory = entry.directory_with_forward_slashes  # File uses forward slashes.
            if entry_directory != current_directory:
                # Write new path group to file list.
                manifest_lines.append(f" PATH: {entry_directory}")
                current_directory = entry_directory
            if has_id(self.bnd_magic):
                manifest_lines.append(f"    ({entry.magic}) {entry.id}: {entry.name}")
            else:
                manifest_lines.append(f"    ({entry.magic}) {entry.name}")
            directory.mkdir(parents=True, exist_ok=True)
            with (directory / entry.name).open("wb") as f:
                packed_entry, _ = entry.get_data_for_pack()
                f.write(packed_entry)

        # NOTE: BND manifest is always encoded in shift_jis_2004.
        with (directory / "bnd_manifest.txt").open("w", encoding="shift_jis_2004") as f:
            f.write(self.bnd_manifest_header)
            f.write("\n".join(manifest_lines))

    def add_entry(self, entry: BNDEntry):
        if entry.id in self.entries_by_id:
            _LOGGER.warning(f"Entry ID {entry.id} appears more than once in this BND. Fix this as soon as you can.")
        self.binary_entries.append(entry)
        self._entries.append(self._entry_class(entry.data) if self._entry_class else entry)

    def remove_entry(self, id_or_path_or_basename):
        if isinstance(id_or_path_or_basename, int):
            entry = self.entries_by_id[id_or_path_or_basename]
        elif isinstance(id_or_path_or_basename, str):
            try:
                entry = self.entries_by_path[id_or_path_or_basename]
            except KeyError:
                entry = self.entries_by_basename[id_or_path_or_basename]
        else:
            raise TypeError("Entry to be removed should be a BND ID (int) or path/basename (str).")
        index = self._entries.index(entry)
        self.binary_entries.pop(index)
        self._entries.pop(index)

    def clear_entries(self):
        """Remove all entries from the BND."""
        self._entries = []
        self.binary_entries = []

    @property
    def bnd_manifest_header(self):
        raise NotImplementedError

    @property
    def entries(self) -> tp.List[BNDEntry]:
        """Returns an ordered list of BND entries, unpacked with the `entry_class` given to the constructor."""
        return self._entries

    @property
    def entries_by_id(self) -> tp.Dict[int, BNDEntry]:
        """Dictionary mapping entry IDs to entries.

        If there are multiple entries with the same ID in the BND, this will raise a `ValueError`. This should never
        happen; if it does, fix it by accessing the culprit entries with `.entries` and changing one or more IDs.
        """
        entries = {}
        for binary_entry, entry in zip(self.binary_entries, self._entries):
            if binary_entry.id in entries:
                raise ValueError(f"There are multiple entries with ID {binary_entry.id}.")
            entries[binary_entry.id] = entry
        return entries

    @property
    def entries_by_path(self) -> tp.Dict[str, BNDEntry]:
        """Dictionary mapping entry paths to (classed) entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this property will raise an exception.
        """
        entries = {}
        for binary_entry, entry in zip(self.binary_entries, self._entries):
            if binary_entry.path in entries:
                raise ValueError(f"Path '{binary_entry.path}' appears in multiple BND entry paths.")
            entries[binary_entry.path] = entry
        return entries

    @property
    def entries_by_basename(self) -> tp.Dict[str, BNDEntry]:
        """Dictionary mapping entry basenames to (classed) entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this property will raise an exception.
        """
        entries = {}
        for binary_entry, entry in zip(self.binary_entries, self._entries):
            entry_name = binary_entry.name
            if entry_name in entries:
                raise ValueError(f"Basename '{entry_name}' appears in multiple BND entry paths.")
            entries[entry_name] = entry
        return entries

    @property
    def entry_count(self) -> int:
        return len(self._entries)

    def __getitem__(self, id_or_path_or_basename) -> BNDEntry:
        """ Shortcut for access by ID (int) or path (str) or basename (str).

        If one entry's path is the basename of another's, the former will be given precedence here, but this should
        never happen!
        """
        if isinstance(id_or_path_or_basename, int):
            return self.entries_by_id[id_or_path_or_basename]
        elif isinstance(id_or_path_or_basename, str):
            try:
                return self.entries_by_path[id_or_path_or_basename]
            except KeyError:
                return self.entries_by_basename[id_or_path_or_basename]
        else:
            raise TypeError("Key should be an entry ID (int) or path/basename (str).")

    def __iter__(self) -> tp.Iterator[BNDEntry]:
        return iter(self._entries)

    def __len__(self):
        return len(self._entries)

    def copy(self):
        return copy.deepcopy(self)

    @staticmethod
    def read_bnd_setting(line: bytes, setting_name: str, assert_type=None, assert_values=None):
        line = line.decode()
        if not line.startswith(setting_name):
            raise ValueError(f"Expected BND setting line to start with {repr(setting_name)}.")
        value = line[len(setting_name) :]
        if not value.startswith(" = "):
            raise ValueError(f"Expected ' = ' after BND setting name. Spaces are required.")
        value = value[3:].strip(" \r\n")
        if not value:
            raise ValueError(f"Setting {repr(setting_name)} is blank.")
        if assert_type is not None:
            try:
                value = literal_eval(value)
            except ValueError:
                raise ValueError(f"Could not evaluate setting value: '{setting_name} = {value}'")
            if not isinstance(value, assert_type):
                raise TypeError(f"Expected a value of a type {assert_type}, but found {type(value)}.")
        else:
            value = value.encode()  # Default type is raw bytes.
        if assert_values is not None and value not in assert_values:
            raise ValueError(f"{repr(value)} is not a permitted value for setting {repr(setting_name)}.")
        return value

    @classmethod
    def detect(cls, bnd_source):
        """ Returns True iff BND source appears to be a BND of this type. Does not support DCX sources. """
        if isinstance(bnd_source, (str, Path)):
            bnd_path = Path(bnd_source)
            if bnd_path.is_file() and bnd_path.name == "bnd_manifest.txt":
                bnd_path = bnd_path.parent
            if bnd_path.is_dir():
                try:
                    with (bnd_path / "bnd_manifest.txt").open("rb") as f:
                        version = cls.read_bnd_setting(f.readline(), "version")
                        return version.decode() == cls.__name__
                except FileNotFoundError:
                    return False
            elif bnd_path.is_file():
                with bnd_path.open("rb") as buffer:
                    try:
                        version = read_chars_from_buffer(buffer, length=4, encoding="utf-8")
                    except ValueError:
                        return False
                    return version == cls.__name__
            return False
        elif isinstance(bnd_source, bytes):
            bnd_source = BytesIO(bnd_source)
        if isinstance(bnd_source, IOBase):
            old_offset = bnd_source.tell()
            bnd_source.seek(0)
            try:
                version = read_chars_from_buffer(bnd_source, length=4, encoding="utf-8")
            except ValueError:
                bnd_source.seek(old_offset)
                return False
            bnd_source.seek(old_offset)
            return version == cls.__name__


class BND3(BaseBND):

    HEADER_STRUCT_START = (
        ("bnd_version", "4s", b"BND3"),
        ("bnd_signature", "8s"),  # Real signature may be shorter, but packing will pad it out.
        ("bnd_magic", "b"),
        ("big_endian", "?"),
    )
    HEADER_STRUCT_ENDIAN = (
        ("unknown", "?"),  # usually zero
        ("zero", "B", 0),
        ("entry_count", "i"),
        ("file_size", "i"),
        "8x",
    )

    BND_ENTRY_HEADER = (("entry_magic", "B"), "3x", ("compressed_data_size", "i"), ("data_offset", "i"))
    ENTRY_ID = ("entry_id", "i")
    NAME_OFFSET = ("path_offset", "i")
    UNCOMPRESSED_DATA_SIZE = ("uncompressed_data_size", "i")

    def __init__(self, bnd_source=None, entry_class=None):
        self.unknown = False
        super().__init__(bnd_source, entry_class)

    def unpack(self, bnd_buffer):
        if isinstance(bnd_buffer, bytes):
            bnd_buffer = BytesIO(bnd_buffer)

        self.header_struct = BinaryStruct(*self.HEADER_STRUCT_START, byte_order="<")
        header = self.header_struct.unpack(bnd_buffer)
        self.bnd_version = header["bnd_version"]
        self.bnd_signature = header["bnd_signature"]
        self.bnd_magic = header["bnd_magic"]
        self.big_endian = header["big_endian"] or is_big_endian(self.bnd_magic)
        byte_order = ">" if self.big_endian else "<"
        header.update(self.header_struct.unpack(bnd_buffer, *self.HEADER_STRUCT_ENDIAN, byte_order=byte_order))
        self.unknown = header["unknown"]

        self.entry_header_struct = BinaryStruct(*self.BND_ENTRY_HEADER, byte_order=byte_order)
        if has_id(self.bnd_magic):
            self.entry_header_struct.add_fields(self.ENTRY_ID, byte_order=byte_order)
        if has_path(self.bnd_magic):
            self.entry_header_struct.add_fields(self.NAME_OFFSET, byte_order=byte_order)
        if has_uncompressed_size(self.bnd_magic):
            self.entry_header_struct.add_fields(self.UNCOMPRESSED_DATA_SIZE, byte_order=byte_order)

        # NOTE: BND paths are *not* encoded in `shift_jis_2004`, unlike most other internal strings!
        for entry in BNDEntry.unpack(
            bnd_buffer, self.entry_header_struct, path_encoding="shift-jis", count=header["entry_count"]
        ):
            self.add_entry(entry)

    def load_unpacked_dir(self, directory):
        directory = Path(directory)
        if not directory.is_dir():
            raise ValueError(f"Could not find unpacked BND directory {repr(directory)}.")
        with (directory / "bnd_manifest.txt").open("rb") as f:
            self.bnd_version = self.read_bnd_setting(f.readline(), "version")
            self.bnd_signature = self.read_bnd_setting(f.readline(), "bnd_signature")
            self.bnd_magic = self.read_bnd_setting(f.readline(), "bnd_magic", assert_type=int)
            self.big_endian = self.read_bnd_setting(f.readline(), "big_endian", assert_type=bool)
            self.unknown = self.read_bnd_setting(f.readline(), "unknown", assert_type=bool)
            self.dcx = self.read_bnd_setting(f.readline(), "dcx", assert_type=tuple)

            self.add_entries_from_manifest_paths(f, directory)

        # Create header structs.
        self.header_struct = BinaryStruct(*self.HEADER_STRUCT_START, byte_order="<")
        byte_order = ">" if self.big_endian else "<"
        self.header_struct.add_fields(*self.HEADER_STRUCT_ENDIAN, byte_order=byte_order)
        self.entry_header_struct = BinaryStruct(*self.BND_ENTRY_HEADER, byte_order=byte_order)
        if has_id(self.bnd_magic):
            self.entry_header_struct.add_fields(self.ENTRY_ID, byte_order=byte_order)
        if has_path(self.bnd_magic):
            self.entry_header_struct.add_fields(self.NAME_OFFSET, byte_order=byte_order)
        if has_uncompressed_size(self.bnd_magic):
            self.entry_header_struct.add_fields(self.UNCOMPRESSED_DATA_SIZE, byte_order=byte_order)

    def pack(self):
        entry_header_dicts = []
        packed_entry_headers = b""
        packed_entry_paths = b""
        relative_entry_path_offsets = []
        packed_entry_data = b""
        relative_entry_data_offsets = []

        if len(self.binary_entries) != len(self._entries):
            raise ValueError(
                "Number of classed entries does not match number of binary entries.\n"
                "Make sure you use the add_entry() method to add new BND entries."
            )

        for i, entry in enumerate(self._entries):
            if not isinstance(entry, BNDEntry):
                if not hasattr(entry, "pack"):
                    raise AttributeError(f"Cannot pack BND: entry class {self._entry_class} has no pack() method.")
                self.binary_entries[i].data = entry.pack()

        for entry in sorted(self.binary_entries, key=lambda e: e.id):
            entry_header_dict = {
                "entry_magic": entry.magic,
                "compressed_data_size": entry.data_size,
                "data_offset": len(packed_entry_data),
            }
            if has_id(self.bnd_magic):
                entry_header_dict["entry_id"] = entry.id
            if has_path(self.bnd_magic):
                entry_header_dict["path_offset"] = len(packed_entry_paths)
                relative_entry_path_offsets.append(len(packed_entry_paths))  # Relative to start of packed entry paths.
                packed_entry_paths += entry.get_packed_path("shift_jis_2004")
            if has_uncompressed_size(self.bnd_magic):
                entry_header_dict["uncompressed_data_size"] = entry.data_size

            relative_entry_data_offsets.append(len(packed_entry_data))
            entry_data, is_compressed = entry.get_data_for_pack()
            if is_compressed:
                entry_header_dict["compressed_data_size"] = len(entry_data)
            packed_entry_data += entry_data
            entry_header_dicts.append(entry_header_dict)

        # Compute table offsets.
        entry_header_table_offset = self.header_struct.size
        entry_path_table_offset = entry_header_table_offset + self.entry_header_struct.size * len(self._entries)
        entry_packed_data_offset = entry_path_table_offset + len(packed_entry_paths)
        bnd_file_size = entry_packed_data_offset + len(packed_entry_data)

        # Pack BND header.
        packed_header = self.header_struct.pack(
            bnd_signature=self.bnd_signature,
            bnd_magic=self.bnd_magic,
            big_endian=self.big_endian,
            unknown=self.unknown,
            entry_count=len(self._entries),
            file_size=bnd_file_size,
        )

        # Convert relative offsets to absolute and pack entry headers.
        for entry_header_dict in entry_header_dicts:
            entry_header_dict["data_offset"] += entry_packed_data_offset
            if has_path(self.bnd_magic):
                entry_header_dict["path_offset"] += entry_path_table_offset
            packed_entry_headers += self.entry_header_struct.pack(entry_header_dict)

        return packed_header + packed_entry_headers + packed_entry_paths + packed_entry_data

    @property
    def bnd_manifest_header(self):
        bnd_signature = self.bnd_signature.rstrip(b"\0").decode()
        return (
            f"version = BND3\n"
            f"bnd_signature = {bnd_signature}\n"
            f"bnd_magic = {self.bnd_magic}\n"
            f"big_endian = {self.big_endian}\n"
            f"unknown = {self.unknown}\n"
            f"dcx = {repr(self.dcx)}\n"
            f"\n"
        )


class BND4(BaseBND):

    HEADER_STRUCT_START = (
        ("bnd_version", "4s", b"BND4"),
        ("flag_1", "?"),
        ("flag_2", "?"),
        "2x",
        ("big_endian", "i"),
    )  # 0x00010000 (False) or 0x00000100 (True)
    HEADER_STRUCT_ENDIAN = (
        ("entry_count", "i"),
        ("header_size", "q", 64),
        ("bnd_signature", "8s"),  # Real signature may be shorter, but packing will pad it out.
        ("entry_header_size", "q"),
        ("data_offset", "q"),
        ("utf16_paths", "?"),
        ("bnd_magic", "b"),
        ("hash_table_type", "B"),  # 0, 1, 4, or 128
        "5x",
        ("hash_table_offset", "q"),  # only non-zero if hash_table_type == 4
    )

    BND_ENTRY_HEADER = (("entry_magic", "B"), "3x", ("minus_one", "i", -1), ("compressed_data_size", "q"))
    UNCOMPRESSED_DATA_SIZE = ("uncompressed_data_size", "q")
    DATA_OFFSET = ("data_offset", "I")
    ENTRY_ID = ("entry_id", "i")
    NAME_OFFSET = ("path_offset", "i")

    HASH_TABLE_HEADER = BinaryStruct(
        "8x", ("path_hashes_offset", "q"), ("hash_group_count", "I"), ("unknown", "i", 0x00080810)
    )
    PATH_HASH_STRUCT = BinaryStruct(("hashed_value", "I"), ("entry_index", "i"),)
    HASH_GROUP_STRUCT = BinaryStruct(("length", "i"), ("index", "i"),)

    def __init__(self, bnd_source=None, entry_class=None):
        self.bnd_flags = (False, False)  # Two unknown bools.
        self.utf16_paths = False  # If False, paths are written in Shift-JIS.
        self.hash_table_type = 0
        self.hash_table_offset = 0
        super().__init__(bnd_source, entry_class)

    def unpack(self, bnd_buffer):
        if isinstance(bnd_buffer, bytes):
            bnd_buffer = BytesIO(bnd_buffer)

        self.header_struct = BinaryStruct(*self.HEADER_STRUCT_START, byte_order="<")
        header = self.header_struct.unpack(bnd_buffer)
        self.bnd_flags = (header["flag_1"], header["flag_2"])
        self.bnd_version = header["bnd_version"]
        self.big_endian = header["big_endian"] == 0x00000100  # Magic not used to infer endianness here.
        byte_order = ">" if self.big_endian else "<"
        header.update(self.header_struct.unpack(bnd_buffer, *self.HEADER_STRUCT_ENDIAN, byte_order=byte_order))
        self.bnd_signature = header["bnd_signature"]
        self.bnd_magic = header["bnd_magic"]
        self.utf16_paths = header["utf16_paths"]
        self.hash_table_type = header["hash_table_type"]
        self.hash_table_offset = header["hash_table_offset"]
        path_encoding = ("utf-16be" if self.big_endian else "utf-16le") if self.utf16_paths else "shift_jis_2004"

        if header["entry_header_size"] != header_size(self.bnd_magic):
            raise ValueError(
                f"Expected BND entry header size {header_size(self.bnd_magic)} based on magic\n"
                f"{hex(self.bnd_magic)}, but BND header says {header['entry_header_size']}."
            )
        if self.hash_table_type != 4 and self.hash_table_offset != 0:
            _LOGGER.warning(
                f"Found non-zero hash table offset {self.hash_table_offset}, but header says this BND has no hash "
                f"table."
            )
        self.entry_header_struct = BinaryStruct(*self.BND_ENTRY_HEADER, byte_order=byte_order)
        if has_uncompressed_size(self.bnd_magic):
            self.entry_header_struct.add_fields(self.UNCOMPRESSED_DATA_SIZE, byte_order=byte_order)
        self.entry_header_struct.add_fields(self.DATA_OFFSET, byte_order=byte_order)
        if has_id(self.bnd_magic):
            self.entry_header_struct.add_fields(self.ENTRY_ID, byte_order=byte_order)
        if has_path(self.bnd_magic):
            self.entry_header_struct.add_fields(self.NAME_OFFSET, byte_order=byte_order)
        if self.bnd_magic == 0x20:
            # Extra pad.
            self.entry_header_struct.add_fields("8x")
        if header["entry_header_size"] != self.entry_header_struct.size:
            _LOGGER.warning(
                f"Entry header size given in BND header ({header['entry_header_size']}) does not match actual entry "
                f"header size ({self.entry_header_struct.size})."
            )
        for entry in BNDEntry.unpack(
            bnd_buffer, self.entry_header_struct, path_encoding=path_encoding, count=header["entry_count"]
        ):
            self.add_entry(entry)

        # Read hash table.
        if self.hash_table_type == 4:
            bnd_buffer.seek(self.hash_table_offset)
            self._most_recent_hash_table = bnd_buffer.read(header["data_offset"] - self.hash_table_offset)
        self._most_recent_entry_count = len(self.binary_entries)
        self._most_recent_paths = [entry.path for entry in self.binary_entries]

    def load_unpacked_dir(self, directory):
        directory = Path(directory)
        if not directory.is_dir():
            raise ValueError(f"Could not find unpacked BND directory {repr(directory)}.")
        with (directory / "bnd_manifest.txt").open("rb") as f:
            self.bnd_version = self.read_bnd_setting(f.readline(), "version", assert_values=[b"BND4"])
            self.bnd_signature = self.read_bnd_setting(f.readline(), "bnd_signature")
            self.bnd_magic = self.read_bnd_setting(f.readline(), "bnd_magic", assert_type=int)
            self.big_endian = self.read_bnd_setting(f.readline(), "big_endian", assert_type=bool)
            self.utf16_paths = self.read_bnd_setting(f.readline(), "utf16_paths", assert_type=bool)
            self.hash_table_type = self.read_bnd_setting(f.readline(), "hash_table_type", assert_type=int)
            self.bnd_flags = self.read_bnd_setting(f.readline(), "unknown_flags", assert_type=tuple)
            self.dcx = self.read_bnd_setting(f.readline(), "dcx", assert_type=tuple)

            self.add_entries_from_manifest_paths(f, directory)

            self._most_recent_hash_table = b""  # Hash table will need to be built on first pack.
            self._most_recent_entry_count = len(self.binary_entries)
            self._most_recent_paths = [entry.path for entry in self.binary_entries]

    def pack(self):
        entry_header_dicts = []
        packed_entry_headers = b""
        packed_entry_paths = b""
        relative_entry_path_offsets = []
        packed_entry_data = b""
        relative_entry_data_offsets = []
        rebuild_hash_table = not self._most_recent_hash_table
        path_encoding = ("utf-16be" if self.big_endian else "utf-16le") if self.utf16_paths else "shift_jis_2004"

        if len(self.binary_entries) != len(self._entries):
            raise ValueError(
                "Number of classed entries does not match number of binary entries.\n"
                "You must use the add_entry() method to add new BND entries."
            )

        if len(self.binary_entries) != self._most_recent_entry_count:
            rebuild_hash_table = True
        for i, entry in enumerate(self._entries):
            if not isinstance(entry, BNDEntry):
                if not hasattr(entry, "pack"):
                    raise AttributeError(f"Cannot pack BND: entry class {self._entry_class} has no pack() method.")
                self.binary_entries[i].data = entry.pack()
                entry = self.binary_entries[i]
            if not rebuild_hash_table and entry.path != self._most_recent_paths[i]:
                rebuild_hash_table = True

        self._most_recent_entry_count = len(self.binary_entries)
        self._most_recent_paths = [entry.path for entry in self.binary_entries]

        for entry in self.binary_entries:

            packed_entry_data += b"\0" * 10  # Each entry is separated by ten pad bytes. (Probably not necessary.)

            entry_header_dict = {
                "entry_magic": entry.magic,
                "compressed_data_size": entry.data_size,
                "data_offset": len(packed_entry_data),
            }
            if has_id(self.bnd_magic):
                entry_header_dict["entry_id"] = entry.id
            if has_path(self.bnd_magic):
                entry_header_dict["path_offset"] = len(packed_entry_paths)
                relative_entry_path_offsets.append(len(packed_entry_paths))  # Relative to start of packed entry paths.
                packed_entry_paths += entry.get_packed_path(path_encoding)
            if has_uncompressed_size(self.bnd_magic):
                entry_header_dict["uncompressed_data_size"] = entry.data_size

            relative_entry_data_offsets.append(len(packed_entry_data))
            entry_data, is_compressed = entry.get_data_for_pack()
            if is_compressed:
                entry_header_dict["compressed_data_size"] = len(entry_data)
            packed_entry_data += entry_data
            entry_header_dicts.append(entry_header_dict)

        entry_header_table_offset = self.header_struct.size
        entry_path_table_offset = entry_header_table_offset + self.entry_header_struct.size * len(self._entries)
        if self.hash_table_type == 4:
            hash_table_offset = entry_path_table_offset + len(packed_entry_paths)
            if rebuild_hash_table:
                packed_hash_table = self.build_hash_table()
            else:
                packed_hash_table = self._most_recent_hash_table
            entry_packed_data_offset = hash_table_offset + len(packed_hash_table)
        else:
            hash_table_offset = 0
            packed_hash_table = b""
            entry_packed_data_offset = entry_path_table_offset + len(packed_entry_paths)
        # BND file size not needed.

        packed_header = self.header_struct.pack(
            flag_1=self.bnd_flags[0],
            flag_2=self.bnd_flags[1],
            big_endian=self.big_endian,
            entry_count=len(self._entries),
            bnd_signature=self.bnd_signature,
            entry_header_size=self.entry_header_struct.size,
            data_offset=entry_packed_data_offset,
            utf16_paths=self.utf16_paths,
            bnd_magic=self.bnd_magic,
            hash_table_type=self.hash_table_type,
            hash_table_offset=hash_table_offset,
        )

        # Convert relative offsets to absolute and pack entry headers.
        for entry_header_dict in entry_header_dicts:
            entry_header_dict["data_offset"] += entry_packed_data_offset
            if has_path(self.bnd_magic):
                entry_header_dict["path_offset"] += entry_path_table_offset
            packed_entry_headers += self.entry_header_struct.pack(entry_header_dict)

        return packed_header + packed_entry_headers + packed_entry_paths + packed_hash_table + packed_entry_data

    @property
    def bnd_manifest_header(self):
        bnd_signature = self.bnd_signature.rstrip(b"\0").decode()
        return (
            f"version = BND4\n"
            f"bnd_signature = {bnd_signature}\n"
            f"bnd_magic = {repr(self.bnd_magic)}\n"
            f"big_endian = {self.big_endian}\n"
            f"utf16_paths = {self.utf16_paths}\n"
            f"hash_table_type = {self.hash_table_type}\n"
            f"unknown_flags = {repr(self.bnd_flags)}\n"
            f"dcx = {repr(self.dcx)}\n"
            f"\n"
        )

    @staticmethod
    def is_prime(p):
        if p < 2:
            return False
        if p == 2:
            return True
        if (p % 2) == 0:
            return False
        for i in range(3, p // 2, 2):
            if (p % i) == 0:
                return False
            if i ** 2 > p:
                return True
        return True

    def build_hash_table(self):
        """ Some BND4 resources include tables of hashed entry paths, which aren't needed to read file contents, but
        need to be re-hashed to properly pack the file in case any paths have changed (or the number of entries). """

        # Group count set to first prime number greater than or equal to the number of entries divided by 7.
        for p in range(len(self._entries) // 7, 100000):
            if self.is_prime(p):
                group_count = p
                break
        else:
            raise ValueError("Hash group count could not be determined.")

        hashes = []
        hash_lists = [[] for _ in range(group_count)]

        for entry_index, entry in enumerate(self.binary_entries):
            hashes.append(self.path_hash(entry.path))
            list_index = hashes[-1] % group_count
            hash_lists[list_index].append((hashes[-1], entry_index))

        for hash_list in hash_lists:
            hash_list.sort()  # Sort by hash value.

        hash_groups = []
        path_hashes = []

        total_hash_count = 0
        for hash_list in hash_lists:
            first_hash_index = total_hash_count
            for path_hash in hash_list:
                path_hashes.append({"hashed_value": path_hash[0], "entry_index": path_hash[1]})
                total_hash_count += 1
            hash_groups.append({"index": first_hash_index, "length": total_hash_count - first_hash_index})

        packed_hash_groups = self.HASH_GROUP_STRUCT.pack(hash_groups)
        packed_hash_table_header = self.HASH_TABLE_HEADER.pack(
            path_hashes_offset=self.HASH_TABLE_HEADER.size + len(packed_hash_groups), hash_group_count=group_count,
        )
        packed_path_hashes = self.PATH_HASH_STRUCT.pack(path_hashes)

        return packed_hash_table_header + packed_hash_groups + packed_path_hashes

    @staticmethod
    def path_hash(path_string):
        """ Simple string-hashing algorithm used by FROM. Strings use forward-slash path separators and always start
        with a forward slash. """
        hashable = path_string.replace("\\", "/")
        if not hashable.startswith("/"):
            hashable = "/" + hashable
        h = 0
        for i, s in enumerate(hashable):
            h += i * 37 + ord(s)
        return h


def BND(bnd_source=None, entry_class=None, optional_dcx=True) -> BaseBND:
    """Auto-detects BND version (BND3 or BND4) to use when opening the source, if appropriate.

    Args:
        bnd_source: path to BND file or BND file content. The BND version will be automatically detected from the data.
            If None, this function will return an empty BND4 container. (Default: None)
        entry_class: optional class to load data from each BND entry into after the BND is unpacked, which is convenient
            for any BNDs that contain file types handled by Soulstruct. (Default: None)
        optional_dcx: if 'bnd_source' is a file path and this is True, both DCX (preferred) and non-DCX versions of that
            BND path will be checked. (It doesn't matter if 'bnd_source' ends in '.dcx' already.) Set this to False to
            search only for the exact path given. (Default: True)
    """
    dcx = False
    bnd_path = None
    if isinstance(bnd_source, (str, Path)):
        if not Path(bnd_source).is_dir():
            bnd_path = Path(bnd_source).absolute()
            if optional_dcx:
                bnd_path = find_dcx(bnd_path)
            elif not bnd_path.is_file():
                raise FileNotFoundError(f"Could not find BND file: {bnd_path}")
            if bnd_path.suffix == ".dcx":
                # Must unpack DCX archive before detecting BND type.
                bnd_dcx = DCX(bnd_path)
                bnd_source = bnd_dcx.data
                dcx = bnd_dcx.magic
            else:
                bnd_source = bnd_path
    if BND3.detect(bnd_source):
        bnd = BND3(bnd_source, entry_class=entry_class)
        if dcx:
            bnd.dcx = dcx
    elif BND4.detect(bnd_source):
        bnd = BND4(bnd_source, entry_class=entry_class)
        if dcx:
            bnd.dcx = dcx
    else:
        raise TypeError("Data bytes could not be interpreted as BND3 or BND4.")
    if bnd_path is not None:
        bnd.bnd_path = bnd_path
    return bnd
