from __future__ import annotations

__all__ = ["BaseMSBEntryList"]

import abc
import io
import logging
import re
import typing as tp
from enum import IntEnum
from functools import wraps

from soulstruct.utilities.binary import BinaryStruct, BinaryReader

from .msb_entry import MSBEntry
from .exceptions import MapError

if tp.TYPE_CHECKING:
    from .enums import BaseMSBSubtype

_LOGGER = logging.getLogger(__name__)

_DUPLICATE_TAG_MATCH = re.compile(r"(.*)<(\d+)>$")

MSBEntryType = tp.TypeVar("MSBEntryType", bound=MSBEntry)
# Valid ways to specify an entry: entry instance, local index, or name from a `str` or the name of an `IntEnum` member
EntrySpecType = tp.Union[MSBEntry, int, IntEnum, str]


def _entry_lookup(func):
    @wraps(func)
    def wrapped(self: BaseMSBEntryList, entry: EntrySpecType, entry_subtype: BaseMSBSubtype = None, *args, **kwargs):
        if isinstance(entry, IntEnum):
            entry = self.get_entry_by_name(entry_name=entry.name, entry_subtype=entry_subtype)
        elif isinstance(entry, int):
            entry = self.get_entries(entry_subtype)[entry]
        elif isinstance(entry, str):
            entry = self.get_entry_by_name(entry_name=entry, entry_subtype=entry_subtype)
        elif isinstance(entry, MSBEntry):
            if entry_subtype is not None and entry_subtype != entry.ENTRY_SUBTYPE:
                raise TypeError(f"Specified entry {entry} is not of specified subtype {entry_subtype.name}.")
        else:
            raise TypeError(f"`entry` must be an `MSBEntry`, local/global entry index, or unique entry name.")
        return func(self, entry, *args, **kwargs)

    return wrapped


class BaseMSBEntryList(abc.ABC):

    INTERNAL_NAME = ""
    MAP_ENTITY_LIST_HEADER: BinaryStruct = None
    MAP_ENTITY_ENTRY_OFFSET: BinaryStruct = None
    MAP_ENTITY_LIST_TAIL: BinaryStruct = None
    NAME_ENCODING = ""
    PLURALIZED_NAME = ""
    ENTRY_SUBTYPE_ENUM: tp.Union[type, tp.Iterable] = None
    SUBTYPE_CLASSES: dict[BaseMSBSubtype, tp.Type[MSBEntry]] = None
    SUBTYPE_OFFSET: int = None  # binary `MSBEntry` offset where subtype integer can be read from

    def __init__(self, msb_entry_list_source=None):
        self._entries = []

        if msb_entry_list_source is None:
            return

        if isinstance(msb_entry_list_source, (list, tuple, dict)):
            if isinstance(msb_entry_list_source, dict):
                msb_entry_list_source = [msb_entry_list_source[k] for k in sorted(msb_entry_list_source)]
            if isinstance(msb_entry_list_source, (list, tuple)):
                for entry in msb_entry_list_source:
                    if isinstance(entry, MSBEntry):
                        self._entries.append(entry)
                    else:
                        raise TypeError("Non-MSBEntry found in source sequence for MSB.")
            return
        if isinstance(msb_entry_list_source, (bytes, io.BufferedIOBase)):
            msb_entry_list_source = BinaryReader(msb_entry_list_source)
        if isinstance(msb_entry_list_source, BinaryReader):
            self.unpack(msb_entry_list_source)
        else:
            raise TypeError(f"Invalid MSB entry list source: {msb_entry_list_source}")

    def unpack(self, msb_reader: BinaryReader):
        header = msb_reader.unpack_struct(self.MAP_ENTITY_LIST_HEADER)
        entry_offsets = [
            msb_reader.unpack_struct(self.MAP_ENTITY_ENTRY_OFFSET)["entry_offset"]
            for _ in range(header["entry_offset_count"] - 1)  # 'entry_offset_count' includes tail offset
        ]
        next_entry_list_offset = msb_reader.unpack_struct(self.MAP_ENTITY_LIST_TAIL)["next_entry_list_offset"]
        name = msb_reader.unpack_string(offset=header["name_offset"], encoding=self.NAME_ENCODING)
        if name != self.INTERNAL_NAME:
            raise ValueError(f"MSB entry list internal name '{name}' does not match known name '{self.INTERNAL_NAME}'.")
        self._entries = []

        for entry_offset in entry_offsets:
            msb_reader.seek(entry_offset)
            entry = self.ENTRY_CLASS(msb_reader)
            self._entries.append(entry)

        msb_reader.seek(next_entry_list_offset)

    def pack(self, start_offset=0, is_last_table=False):
        entries = self.get_entries()
        entry_offsets = []
        packed_entries = b""
        offset = start_offset + (
            self.MAP_ENTITY_LIST_HEADER.size
            + self.MAP_ENTITY_ENTRY_OFFSET.size * len(entries)
            + self.MAP_ENTITY_LIST_TAIL.size
        )
        packed_name = self.INTERNAL_NAME.encode("utf-8")
        name_offset = offset
        while len(packed_name) < 16:  # TODO: used to be 32
            packed_name += b"\0"
        offset += len(packed_name)
        for i, entry in enumerate(entries):
            entry_offsets.append(offset)
            packed_entry = self.pack_entry(i, entry)
            packed_entries += packed_entry
            offset += len(packed_entry)

        next_entry_list_offset = offset if not is_last_table else 0

        packed_header = self.MAP_ENTITY_LIST_HEADER.pack(name_offset=name_offset, entry_offset_count=len(entries) + 1,)
        packed_header += self.MAP_ENTITY_ENTRY_OFFSET.pack_multiple([{"entry_offset": o} for o in entry_offsets])
        packed_header += self.MAP_ENTITY_LIST_TAIL.pack(next_entry_list_offset=next_entry_list_offset)

        return packed_header + packed_name + packed_entries

    @classmethod
    def ENTRY_CLASS(cls, msb_reader: BinaryReader):
        """Detects the appropriate subclass of `MSBEntry` to instantiate, and does so."""
        entry_subtype_int = msb_reader.unpack("i", offset=cls.SUBTYPE_OFFSET, relative_offset=True)[0]
        try:
            entry_subtype = cls.ENTRY_SUBTYPE_ENUM(entry_subtype_int)
        except ValueError:
            raise MapError(f"Entry of type {cls.ENTRY_SUBTYPE_ENUM} has invalid subtype enum: {entry_subtype_int}")
        entry_subtype_class = cls.SUBTYPE_CLASSES[entry_subtype]
        return entry_subtype_class(msb_reader)

    @abc.abstractmethod
    def pack_entry(self, index: int, entry: MSBEntryType):
        """Pack entry (some entry types may use `index`)."""

    def __iter__(self) -> tp.Iterator[MSBEntryType]:
        """Iterate over all entries."""
        return iter(self._entries)

    def __len__(self):
        """Count of all entries."""
        return len(self._entries)

    def clear(self):
        """Delete all entries of all subtypes in list."""
        self._entries.clear()

    @classmethod
    def resolve_entry_subtype(cls, entry_subtype):
        """Converts any valid entry subtype specification into the proper subtype enum."""
        if isinstance(entry_subtype, cls.ENTRY_SUBTYPE_ENUM):
            return entry_subtype
        try:
            if hasattr(entry_subtype, "get_msb_entry_type_subtype"):  # `MapEntry` subclass
                entry_subtype = entry_subtype.get_msb_entry_type_subtype()[1]
            if isinstance(entry_subtype, str):
                for e in cls.ENTRY_SUBTYPE_ENUM:
                    if entry_subtype in (e.name, e.pluralized_name):
                        return e
            elif isinstance(entry_subtype, int):
                return cls.ENTRY_SUBTYPE_ENUM(entry_subtype)
            raise ValueError
        except (TypeError, ValueError):
            raise TypeError(f"Invalid entry subtype for entry list {cls.PLURALIZED_NAME}: {entry_subtype}")

    def __getitem__(self, entry: tp.Union[int, IntEnum, str]) -> MSBEntryType:
        """You can access entries using their global index or (if unique) name."""
        if isinstance(entry, IntEnum):
            return self.get_entry_by_name(entry_name=entry.name, entry_subtype=None)
        elif isinstance(entry, int):
            return self.get_entries()[entry]
        elif isinstance(entry, str):
            return self.get_entry_by_name(entry_name=entry, entry_subtype=None)
        raise TypeError(f"`MSBEntryList` key must be a global entry index or unique entry name, not {entry}.")

    def get_entries(self, entry_subtype=None) -> list[MSBEntryType]:
        """Return a list of entries of the given subtype, or all entries in global order if no subtype is given.

        Note that only the global index (`entry_subtype=None`) is valid for index links from other MSB entries, with the
        sole exceptions of:
            - the `MSBCollision` entry linked to by an `MSBMapConnection` entry
            - the `MSBEnvironmentEvent` entry linked to by an `MSBCollision` entry
        """
        if entry_subtype is None:
            return list(self._entries)  # Full entry list, with types potentially intermingled.
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        return [e for e in self._entries if e.ENTRY_SUBTYPE == entry_subtype]

    def get_entry_names(self, entry_subtype=None) -> list[str]:
        """Returns a list of entry names (global or `entry_subtype`-specific)."""
        return [entry.name for entry in self.get_entries(entry_subtype=entry_subtype)]

    def get_entry_by_name(self, entry_name: str, entry_subtype=None) -> MSBEntryType:
        """Try to retrieve entry with given name.

        You can optionally specify the subtype. Names shouldn't be base across subtypes, but if they are (or as an
        assertion) this can be useful.

        Note that you can simply index the MSB entry list with a string (e.g. `msb.parts["h0000B0"]` as a shortcut to
        calling this method. It will raise a KeyError if the given name is not found OR if multiple entries with the
        given name (and subtype) are found.
        """
        entries = [entry for entry in self.get_entries(entry_subtype) if entry.name == entry_name]
        if not entries:
            raise KeyError(f"Entry name '{entry_name}' does not appear in {self.__class__.__name__}.")
        elif len(entries) >= 2:
            raise ValueError(
                f"Entry name '{entry_name}' appears more than once in {self.__class__.__name__}. You must access it by "
                f"global index or local subtype-specific index."
            )
        return entries[0]

    @_entry_lookup
    def get_entry_subtype(self, entry: EntrySpecType):
        """Returns subtype enum of given `entry`."""
        return entry.ENTRY_SUBTYPE

    @_entry_lookup
    def get_entry_subtype_index(self, entry: EntrySpecType):
        """Get local index of specified `entry` among entries with the same subtype."""
        return self.get_entries(entry.ENTRY_SUBTYPE).index(entry)

    @_entry_lookup
    def get_entry_global_index(self, entry: EntrySpecType):
        """Get global index of specified `entry` among all entries with this list type."""
        return self._entries.index(entry)

    def new(
        self,
        entry_subtype: tp.Union[str, BaseMSBSubtype],
        copy_entry: MSBEntryType = None,
        insert_below_original=True,
        auto_add=True,
        **kwargs,
    ):
        """Create a new `MSBEntry` of the given type (or duplicate from `copy_entry=entry`), apply any `kwargs` to it,
        add it to this `MSBEntryList` if `auto_add=True` (default), then return it.

        Use the `new_{subtype}()` shortcut methods to avoid specifying `entry_subtype` and use return type hinting.
        """
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        if copy_entry is not None:
            return self.duplicate_entry(
                entry=copy_entry,
                entry_subtype=entry_subtype,
                auto_add=auto_add,
                insert_below_original=insert_below_original,
                **kwargs,
            )
        if kwargs.get("name", None) is None and kwargs.get("entity_enum", None) is None:
            kwargs["name"] = self._get_duplicate_tagged_name(f"New {entry_subtype.name}")
        entry = self.SUBTYPE_CLASSES[entry_subtype](source=None, **kwargs)
        if auto_add:
            self.add_entry(entry)
        return entry

    def add_entry(self, entry: MSBEntryType, global_index=None):
        """Add existing `entry` at desired `global_index`.

        If `global_index` is None, it defaults to the end of the `entry`'s subtype.
        """
        if global_index is None:
            global_index = self.get_subtype_next_global_index(entry.ENTRY_SUBTYPE)
        self._entries.insert(global_index, entry)
        return entry

    @_entry_lookup
    def duplicate_entry(
        self, entry: EntrySpecType, auto_add=True, insert_below_original=True, **kwargs,
    ):
        """Duplicate the specified `entry`.

        By default, the duplicated entry is inserted just below the source entry. If `insert_below_original=False`, it
        will instead be inserted at the end of its entry subtype (not global subtype).

        Any `kwargs` given will be passed to the `set()` method of the duplicated entry (which is then also returned for
        further modification if desired). Unless otherwise specified, the `name` of the new entry will also be given a
        unique '<i>' duplicate tag suffix to retain name uniqueness (which will be removed upon final pack).

        You can also call this with `add_{subtype}(copy_entry=entry, insert_below_original=True, **kwargs)`.
        """
        duplicated = entry.copy()

        if kwargs.get("name", "") == entry.name and entry in self._entries:
            raise ValueError(f"Name of duplicated entry cannot be set to the source entry's name: {entry.name}")
        if kwargs.get("name", None) is None and kwargs.get("entity_enum", None) is None:
            # First, try a basic increment of any trailing numerals.
            if name_index_match := re.match(r"(.*)(\d+)", duplicated.name):
                name_prefix = name_index_match.group(1)
                name_suffix = int(name_index_match.group(2))
                new_suffix = format(name_suffix + 1, f"0{len(name_index_match.group(2))}d")
                new_name = name_prefix + new_suffix
                if new_name not in self.get_entry_names():
                    kwargs["name"] = new_name
                else:
                    kwargs["name"] = self._get_duplicate_tagged_name(duplicated.name)
            else:
                kwargs["name"] = self._get_duplicate_tagged_name(duplicated.name)
        duplicated.set(**kwargs)

        if auto_add:
            if insert_below_original and entry in self._entries:
                global_index = self._entries.index(entry) + 1
            else:
                global_index = self.get_subtype_next_global_index(entry.ENTRY_SUBTYPE)
            self._entries.insert(global_index, duplicated)

        return duplicated

    @_entry_lookup
    def delete_entry(self, entry: EntrySpecType) -> MSBEntryType:
        """Delete (and return) specified `entry`."""
        self._entries.remove(entry)
        return entry

    def delete_all_entries_of_subtype(self, entry_subtype):
        """Delete all entries of the given `entry_subtype`."""
        for entry in self.get_entries(entry_subtype):
            self._entries.remove(entry)

    def get_subtype_next_global_index(self, entry_subtype: BaseMSBSubtype) -> int:
        """Returns next global index of given `entry_subtype`, e.g. for inserting a new entry into the `MSBEntryList` at
        the end of its local subtype. This is inferred by just finding the last existing instance of that subtype.

        Note that the game may not read entries that do not appear in their contiguous local subtype lists, so this
        method is often necessary to find the correct place for a new entry. (This has been  confirmed for
        `MSBTreasureEvent`, for example.)
        """
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        try:
            last_global_index = max(i for i, entry in enumerate(self._entries) if entry.ENTRY_SUBTYPE == entry_subtype)
        except ValueError:  # no entries of given subtype exist yet
            # Iterate over entries in enum order to find correct global index.
            last_global_index = -1
            for subtype in self.ENTRY_SUBTYPE_ENUM:
                if subtype == entry_subtype:
                    break
                last_global_index += len(self.get_entries(subtype))
        return last_global_index + 1

    def _get_duplicate_tagged_name(self, name: str):
        """Add a duplicate tag, e.g. "<1>", to the end of the given name if 1+ entries with that name already exist.

        These tags will be removed on write to support byte-for-byte vanilla repacking, so make sure to set them
        yourself if you want to keep the names unique (highly recommended).
        """
        existing_names = self.get_entry_names()
        if name not in existing_names:
            return name  # no tag needed
        duplicate_tag_match = _DUPLICATE_TAG_MATCH.match(name)
        if not duplicate_tag_match:
            return f"{name} <1>"
        # Find next available duplicate tag number.
        name = duplicate_tag_match.group(1).rstrip()
        new_duplicate_tag = int(duplicate_tag_match.group(2)) + 1
        while f"{name} <{new_duplicate_tag}>" in existing_names:
            new_duplicate_tag += 1
        return f"{name} <{new_duplicate_tag}>"

    def get_indices(self):
        """Returns a dictionary mapping entry names to their global indices for resolving named links before repacking.

        Raises a NameError if the same name appears more than once in the entry list, which can only happen if you
        explicitly copy a name (except for `MSBEvent`s, which don't use this method).
        """
        entry_indices = {}
        for i, entry in enumerate(self._entries):
            if entry.name in entry_indices:
                raise NameError(
                    f"Name {repr(entry.name)} (type {entry.ENTRY_SUBTYPE.name}) appears more than once in "
                    f"MSB. Please ensure all map entries have unique names."
                )
            entry_indices[entry.name] = i
        return entry_indices

    def set_and_get_unique_names(self):
        """Goes through all entries and assigns <repeat> suffixes to any repeated names, so that every entry has
        a unique name for name linking purposes. These suffixes will be removed when the MSB is packed.

        Returns a dictionary mapping entry indices to those new unique names.
        """
        unique_names = {}
        repeat_count = {}
        for i, entry in enumerate(self._entries):
            if entry.name in unique_names.values():
                repeat_count.setdefault(entry.name, 0)
                repeat_count[entry.name] += 1
                entry.name += f" <{repeat_count[entry.name]}>"
            unique_names[i] = entry.name
        return unique_names

    def to_dict(self, ignore_defaults=True) -> [dict[str, list[dict[str, tp.Any]]]]:
        """Get the entry list as a dictionary mapping entry subtype names to lists of entry dictionaries."""
        data = {}
        for entry_subtype_enum in self.ENTRY_SUBTYPE_ENUM:
            subtype_entries = self.get_entries(entry_subtype_enum)
            if subtype_entries:
                data[entry_subtype_enum.name] = [
                    entry.to_dict(ignore_defaults=ignore_defaults) for entry in subtype_entries
                ]
        return data
