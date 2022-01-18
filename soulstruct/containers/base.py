"""NOTE: This file is Python 3.9 compatible for Blender 3.X use."""
from __future__ import annotations

__all__ = ["BinderError", "BaseBinder", "BinderHashTable"]

import abc
import io
import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.base.game_file import GameFile, InvalidGameFileTypeError
from soulstruct.base.binder_entry import BinderEntry
from soulstruct.utilities.binary import BinaryReader, BinaryStruct, BinaryWriter
from soulstruct.utilities.files import read_json, write_json

_LOGGER = logging.getLogger(__name__)


class BinderFlags(int):
    """Bit flags for binder file. Note that the bit order is 'big endian' here.

    TODO: Determine which file types in which games use which magic values, so they can be initialized to defaults.
    """

    @property
    def is_big_endian(self):
        return self & 0b0000_0001  # 0x80

    @property
    def has_ids(self):
        return self & 0b0000_0010  # 0x40

    @property
    def has_names_1(self):
        return self & 0b0000_0100  # 0x20

    @property
    def has_names_2(self):
        return self & 0b0000_1000  # 0x10

    @property
    def has_names(self):
        """Looks for either 'names' flag. Unsure what the difference is."""
        return self & (0b0000_0100 | 0b0000_1000)

    @property
    def has_long_offsets(self):
        return self & 0b0001_0000  # 0x08

    @property
    def has_compression(self):
        return self & 0b0010_0000  # 0x04

    @property
    def has_flag_6(self):
        return self & 0b0100_0000  # 0x02

    @property
    def has_flag_7(self):
        return self & 0b1000_0000  # 0x01

    @classmethod
    def read(cls, reader: BinaryReader, bit_big_endian: bool) -> BinderFlags:
        """Read a byte, reverse it if necessary, and return flags integer."""
        flags = cls(reader.unpack_value("B"))
        if not bit_big_endian and not (flags.is_big_endian and not flags.has_flag_7):
            flags = cls(int(f"{flags:08b}"[::-1], 2))
        return flags

    def pack(self, writer: BinaryWriter, bit_big_endian: bool):
        if not bit_big_endian and not (self.is_big_endian and not self.has_flag_7):
            writer.pack("B", int(f"{self:08b}"[::-1], 2))
        else:
            writer.pack("B", self)

    def get_bnd_entry_header_size(self) -> int:
        """Calculate binder entry header size."""
        size = 16  # Base size.
        if self.has_ids:
            size += 4
        if self.has_names_1 or self.has_names_2:
            size += 4
        if self.has_compression:
            size += 8
        size += 8 if self.has_long_offsets else 4
        return size


class BinderError(Exception):
    pass


class BaseBinder(GameFile, abc.ABC):
    """Base class for both BND and BXF (BHD/BDT) binder files."""

    # `EXT` depends on files contained in binder.
    MANIFEST_FIELDS = (
        "signature",
        "flags",
        "big_endian",
        "bit_big_endian",
        "dcx_magic",
    )
    BinderEntry = BinderEntry  # for convenience

    signature: str
    flags: BinderFlags
    big_endian: bool
    bit_big_endian: bool

    def __init__(self, file_source: GameFile.Typing = None, dcx_magic=(), **kwargs):
        self.signature = ""
        self.flags = BinderFlags(0)  # no other sensible default
        self.big_endian = False
        self.bit_big_endian = False
        self._entries = []  # type: list[BinderEntry]
        super().__init__(file_source, dcx_magic=dcx_magic, **kwargs)

    def _handle_other_source_types(self, file_source, **kwargs) -> tp.Optional[BinaryReader]:
        """A Binder can also be loaded from a `binder_manifest.json` file or a directory containing such a file, or
        a dictionary containing header information to initialize a Binder with no entries."""

        if isinstance(file_source, (str, Path)):
            file_source = Path(file_source)
            if file_source.is_dir() and (file_source / "binder_manifest.json").exists():
                file_source = file_source / "binder_manifest.json"  # go to below
            if file_source.is_file() and file_source.name == "binder_manifest.json":
                directory = file_source.parent
                if directory.suffix == ".unpacked":  # only this suffix is automatically removed
                    self.path = directory.with_name(directory.name[:-9])
                else:
                    self.path = directory  # writing this path will conflict with this unpacked folder source
                self.load_unpacked_dir(directory)
                return

        if isinstance(file_source, dict):
            # Manifest dictionary. All `MANIFEST_FIELDS` must be present. Other fields will be ignored.
            manifest = self.get_manifest_header(file_source)
            for field in self.MANIFEST_FIELDS:
                try:
                    setattr(self, field, manifest[field])
                except KeyError:
                    raise KeyError(
                        f"Manifest dictionary source for `{self.__class__.__name__}` is missing field '{field}'."
                    )
            return

        raise InvalidGameFileTypeError(
            "`file_source` is not a `binder_manifest.json` file or directory containing one, or a manifest dict."
        )

    def add_entry(self, entry: BinderEntry):
        if entry in self._entries:
            raise BinderError(f"Given `BinderEntry` instance with ID {entry.id} is already in this binder.")
        if entry.id in self.entries_by_id:
            _LOGGER.warning(f"Entry ID {entry.id} appears more than once in this binder. You should fix this!")
        self._entries.append(entry)

    def remove_entry(self, id_or_path_or_basename) -> BinderEntry:
        if isinstance(id_or_path_or_basename, int):
            entry = self.entries_by_id[id_or_path_or_basename]
        elif isinstance(id_or_path_or_basename, str):
            try:
                entry = self.entries_by_path[id_or_path_or_basename]
            except KeyError:
                entry = self.entries_by_basename[id_or_path_or_basename]
        else:
            raise TypeError("Entry to be removed should be a binder entry ID (int) or path/basename (str).")
        self._entries.remove(entry)
        return entry

    def clear_entries(self):
        """Remove all entries from the BND."""
        self._entries.clear()

    @abc.abstractmethod
    def get_json_header(self) -> dict[str, tp.Any]:
        ...

    def load_unpacked_dir(self, directory):
        """Load binder from a Soulstruct-unpacked directory containing a `binder_manifest.json` file."""
        directory = Path(directory)
        if not directory.is_dir():
            raise ValueError(f"Could not find unpacked binder directory {repr(directory)}.")
        manifest = read_json(directory / "binder_manifest.json", encoding="shift-jis")
        for field, value in self.get_manifest_header(manifest).items():
            setattr(self, field, value)
        self.add_entries_from_manifest(manifest["entries"], directory, manifest["use_id_prefix"])

    @classmethod
    def get_manifest_header(cls, manifest: dict) -> dict[str, tp.Any]:
        """Extract manifest header data from given `manifest` dictionary and parse them into appropriate types.

        Other keys may be present in `manifest`, and will be ignored.
        """
        if "version" not in manifest:
            raise BinderError("JSON manifest file does not contain 'version' key.")
        all_class_names = [base.__name__ for base in cls.__mro__]
        if manifest["version"] not in all_class_names:
            raise BinderError(
                f"Version of file ({manifest['version']}) does not match "
                f"`BaseBinder` child class name ({cls.__name__})."
            )
        loaded_manifest = {}
        for field in cls.MANIFEST_FIELDS:
            if field == "flags":
                value = BinderFlags(manifest[field])
            elif field == "dcx_magic":
                value = tuple(manifest["dcx_magic"])
            else:
                value = manifest[field]
            loaded_manifest[field] = value
        return loaded_manifest

    def add_entries_from_manifest(self, entries: dict, directory: tp.Union[str, Path], use_id_prefix: bool):
        directory = Path(directory)
        unsorted_entries = {}  # maps ID to `(path, data, flags)` tuple
        for root, entry_dicts in entries.items():
            for entry in entry_dicts:
                find_entry_basename = f"__{entry['id']}__{entry['name']}" if use_id_prefix else entry['name']
                with (directory / find_entry_basename).open("rb") as entry_file:
                    entry_data = entry_file.read()
                unsorted_entries[entry['id']] = (f"{root}\\{entry['name']}", entry_data, entry['flags'])
        for entry_id, (path, data, flags) in sorted(unsorted_entries.items()):
            self.add_entry(BinderEntry(entry_id=entry_id, path=path, data=data, flags=flags))

    def write_unpacked_dir(self, directory=None):
        if not self.flags.has_names:
            raise NotImplementedError(
                "Writing unpacked binder directories is only supported for binder formats with path strings."
            )
        if directory is None:
            if self.path:
                directory = self.path.with_suffix(self.path.suffix + ".unpacked")
            else:
                raise ValueError("Cannot detect `directory` for unpacked binder automatically.")
        else:
            directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)

        entry_tree_dict = {}
        use_index_prefix = self.has_repeated_entry_names

        for i, entry in enumerate(self._entries):
            entry_directory = str(Path(entry.path).parent)  # no trailing backslash
            entry_dict = {"flags": entry.flags, "id": entry.id if self.flags.has_ids else i, "name": entry.name}
            entry_tree_dict.setdefault(entry_directory, []).append(entry_dict)
            entry_file_name = f"__{entry.id}__{entry.name}" if use_index_prefix else entry.name
            with (directory / entry_file_name).open("wb") as f:
                f.write(entry.data)

        json_dict = self.get_json_header()
        json_dict["entries"] = entry_tree_dict

        # NOTE: Binder manifest is always encoded in shift-JIS, not `shift_jis_2004`.
        write_json(directory / "binder_manifest.json", json_dict, encoding="shift-jis")

    @classmethod
    def detect(cls, binder_source: tp.Union[GameFile.Typing, dict]) -> bool:
        """Returns True if `binder_source` appears to be this subclass of `BaseBinder`. Does not support DCX sources."""
        if isinstance(binder_source, dict):
            # Manifest dictionary. Simply check version.
            return binder_source.get("version") == cls.__name__  # "BND3", "BND4", etc.

        if isinstance(binder_source, (str, Path)):
            binder_path = Path(binder_source)
            if binder_path.is_file() and binder_path.name == "binder_manifest.json":
                binder_path = binder_path.parent
            if binder_path.is_dir():
                try:
                    manifest = read_json(binder_path / "binder_manifest.json", encoding="shift_jis")
                    return manifest.get("version") == cls.__name__  # "BND3", "BND4", etc.
                except FileNotFoundError:
                    return False
            elif binder_path.is_file():
                reader = BinaryReader(binder_path)
                try:
                    version = reader.unpack_string(length=4, encoding="ascii")
                except ValueError:
                    return False
                if version[:3] in {"BHF", "BDF"}:
                    version = f"BXF{version[3]}"  # BXF header or data file
                return version == cls.__name__
            return False
        elif isinstance(binder_source, (bytes, io.BufferedIOBase)):
            binder_source = BinaryReader(binder_source)

        if isinstance(binder_source, BinaryReader):
            with binder_source.temp_offset(0):
                try:
                    version = binder_source.unpack_string(length=4, encoding="ascii")
                except ValueError:
                    return False
            if version[:3] in {"BHF", "BDF"}:
                version = f"BXF{version[3]}"  # BXF header or data file
            return version == cls.__name__

        raise TypeError(f"Cannot detect `Binder` class from source type: {binder_source}")

    @property
    def entries(self) -> list[BinderEntry]:
        """Returns an ordered list of BND entries, unpacked with the `entry_class` given to the constructor."""
        return self._entries

    @property
    def entries_by_id(self) -> dict[int, BinderEntry]:
        """Dictionary mapping entry IDs to entries.

        If there are multiple entries with the same ID in the BND, this will raise a `ValueError`. This should never
        happen; if it does, fix it by accessing the culprit entries with `.entries` and changing one or more IDs.
        """
        entries = {}
        for entry in self._entries:
            if entry.id in entries:
                raise BinderError(f"There are multiple entries with ID {entry.id}.")
            entries[entry.id] = entry
        return entries

    @property
    def entries_by_path(self) -> dict[str, BinderEntry]:
        """Dictionary mapping entry paths to (classed) entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this property will raise an exception.
        """
        entries = {}
        for entry in self._entries:
            if entry.path in entries:
                raise ValueError(f"Path '{entry.path}' appears in multiple `BNDEntry` paths.")
            entries[entry.path] = entry
        return entries

    @property
    def entries_by_basename(self) -> dict[str, BinderEntry]:
        """Dictionary mapping entry basenames to (classed) entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this property will raise an exception.
        """
        entries = {}
        for entry in self._entries:
            if entry.name in entries:
                raise ValueError(f"Basename '{entry.name}' appears in multiple BND entry paths.")
            entries[entry.name] = entry
        return entries

    @property
    def entry_count(self) -> int:
        return len(self._entries)

    @property
    def has_repeated_entry_names(self):
        entry_names = [e.name for e in self.entries]
        return len(set(entry_names)) < len(entry_names)

    def find_entries_matching_name(self, regex: str) -> list[BinderEntry]:
        """Returns a list of entries whose names match the given `regex` pattern."""
        return [entry for entry in self._entries if re.match(regex, entry.name)]

    def find_entry_matching_name(self, regex: str) -> BinderEntry:
        """Returns a single entry whose name matches the given `regex` pattern.

        Only one match must exist.
        """
        matches = [entry for entry in self._entries if re.match(regex, entry.name)]
        if len(matches) > 1:
            raise ValueError(f"Found multiple Binder entries with name matching '{regex}'.")
        if not matches:
            raise ValueError(f"No Binder entries found with name matching '{regex}'.")
        return matches[0]

    def __getitem__(self, id_or_path_or_basename) -> BinderEntry:
        """Shortcut for access by ID (int) or path (str) or basename (str).

        If the path of one entry is the basename of another entry, the former will be given precedence here, but this
        should never happen.
        """
        if isinstance(id_or_path_or_basename, int):
            return self.entries_by_id[id_or_path_or_basename]
        elif isinstance(id_or_path_or_basename, str):
            try:
                return self.entries_by_path[id_or_path_or_basename]
            except KeyError:
                return self.entries_by_basename[id_or_path_or_basename]
        raise TypeError("`BND` key should be an entry ID (int) or path/basename (str).")

    def __iter__(self) -> tp.Iterator[BinderEntry]:
        return iter(self._entries)

    def __len__(self):
        return len(self._entries)

    def __repr__(self):
        if not self._entries:
            return
        entries = f",\n    ".join(repr(entry) for entry in self._entries)
        if entries:
            entries = f"\n    {entries},\n"
        return f"{self.__class__.__name__}({entries})"


class BinderHashTable:

    HASH_TABLE_HEADER = BinaryStruct(
        "8x",
        ("path_hashes_offset", "q"),
        ("hash_group_count", "I"),
        ("unknown3", "i", 0x00080810),
    )
    PATH_HASH_STRUCT = BinaryStruct(
        ("hashed_value", "I"),
        ("entry_index", "i"),
    )
    HASH_GROUP_STRUCT = BinaryStruct(
        ("length", "i"),
        ("index", "i"),
    )

    @classmethod
    def build_hash_table(cls, entries):
        """ Some BND4 resources include tables of hashed entry paths, which aren't needed to read file contents, but
        need to be re-hashed to properly pack the file in case any paths have changed (or the number of entries). """

        # Group count set to first prime number greater than or equal to the number of entries divided by 7.
        for p in range(len(entries) // 7, 100000):
            if cls.is_prime(p):
                group_count = p
                break
        else:
            raise ValueError("Hash group count could not be determined.")

        hashes = []
        hash_lists = [[] for _ in range(group_count)]  # type: list[list[tuple[int, int]], ...]

        for entry_index, entry in enumerate(entries):
            hashes.append(cls.path_hash(entry.path))
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

        packed_hash_groups = cls.HASH_GROUP_STRUCT.pack_multiple(hash_groups)
        packed_hash_table_header = cls.HASH_TABLE_HEADER.pack(
            path_hashes_offset=cls.HASH_TABLE_HEADER.size + len(packed_hash_groups), hash_group_count=group_count,
        )
        packed_path_hashes = cls.PATH_HASH_STRUCT.pack_multiple(path_hashes)

        return packed_hash_table_header + packed_hash_groups + packed_path_hashes

    @staticmethod
    def path_hash(path_string: str):
        """Simple string-hashing algorithm used by FROM.

        Strings use forward-slash path separators and always start with a forward slash.
        """
        hashable = path_string.replace("\\", "/")
        if not hashable.startswith("/"):
            hashable = "/" + hashable
        h = 0
        for i, s in enumerate(hashable):
            h += i * 37 + ord(s)
        return h

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
