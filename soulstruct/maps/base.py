from __future__ import annotations

__all__ = ["MSBEntry", "MSBEntryList", "MSBEntryEntity", "MSBEntryEntityCoordinates"]

import abc
import copy
import logging
import re
import typing as tp
from copy import deepcopy
from io import BytesIO, BufferedReader

from soulstruct.maps.core import MAP_ENTRY_TYPES
from soulstruct.utilities import BinaryStruct, read_chars_from_buffer
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation

_DUPLICATE_TAG_MATCH = re.compile(r" <(\d+)>$")
_LOGGER = logging.getLogger(__name__)

EntryType = tp.TypeVar("EntryType", bound="MSBEntry")


class MSBEntry(abc.ABC):

    ENTRY_TYPE = None
    FIELD_INFO = {}

    def __init__(self):
        self.name = None
        self.description = None  # Used for convenience in Soulstruct projects.

    @abc.abstractmethod
    def pack(self):
        """Pack to bytes."""

    @abc.abstractmethod
    def unpack(self, msb_buffer):
        """Unpack from open `MSB` buffer."""

    def get_name_to_pack(self):
        """Remove duplicate tags '<i>' from end of name."""
        return _DUPLICATE_TAG_MATCH.sub("", self.name)

    def __getitem__(self, field_name):
        if field_name in self.FIELD_INFO:
            return getattr(self, field_name)
        raise KeyError(f"Field {field_name} does not exist in MSB entry type {self.__class__.__name__}.")

    def __setitem__(self, field_name, value):
        """Alias for setting the given attribute.

        `field_name` must be 'name', 'description', or a key in the `FIELD_INFO` dictionary for this class.
        """
        if field_name.startswith("_") and hasattr(self, field_name):
            setattr(self, field_name, value)
        elif field_name in {"name", "description"} or field_name in self.FIELD_INFO:
            setattr(self, field_name, value)
        else:
            raise KeyError(f"Field {repr(field_name)} does not exist in MSB entry type {self.__class__.__name__}.")

    def set(self, **kwargs):
        """Update any attribute fields with keyword arguments.

        Argument keys starting with double underscore are ignored so that `BinaryStruct`-produced dictionaries can
        easily be passed in. See `__setitem__()` for more.
        """
        for field_name, value in kwargs.items():
            if not field_name.startswith("__"):
                self[field_name] = value

    def copy(self):
        return deepcopy(self)

    @property
    def field_names(self):
        return list(self.FIELD_INFO.keys())


class MSBEntryList(abc.ABC, tp.Generic[EntryType]):

    MAP_ENTITY_LIST_HEADER = BinaryStruct("4x", ("name_offset", "i"), ("entry_offset_count", "i"),)
    MAP_ENTITY_ENTRY_OFFSET = BinaryStruct(("entry_offset", "i"),)
    MAP_ENTITY_LIST_TAIL = BinaryStruct(("next_entry_list_offset", "i"),)

    ENTRY_LIST_NAME = None
    ENTRY_CLASS = None
    ENTRY_TYPE_ENUM = None

    def __init__(self, msb_entry_list_source=None, name=""):
        self.name = ""
        self._entries = []

        if msb_entry_list_source is None:
            return

        if isinstance(msb_entry_list_source, (list, tuple, dict)):
            if not name:
                raise ValueError("Name of MSB entry list must be given if created manually.")
            if name not in {"POINT_PARAM_ST", "EVENT_PARAM_ST", "PARTS_PARAM_ST", "MODEL_PARAM_ST"}:
                raise ValueError(
                    "Name of MSB entry list must be MODEL_PARAM_ST, EVENT_PARAM_ST, POINT_PARAM_ST, "
                    "or PARTS_PARAM_ST."
                )
            if isinstance(msb_entry_list_source, dict):
                msb_entry_list_source = [msb_entry_list_source[k] for k in sorted(msb_entry_list_source)]
            if isinstance(msb_entry_list_source, (list, tuple)):
                for entry in msb_entry_list_source:
                    if isinstance(entry, MSBEntry):
                        self._entries.append(entry)
                    else:
                        raise TypeError("Non-MSBEntry found in source sequence for MSB.")
            return
        if isinstance(msb_entry_list_source, bytes):
            msb_entry_list_source = BytesIO(msb_entry_list_source)
        if isinstance(msb_entry_list_source, BufferedReader):
            self.unpack(msb_entry_list_source)
        else:
            raise TypeError(f"Invalid MSB entry list source: {msb_entry_list_source}")

    def unpack(self, msb_buffer):
        header = self.MAP_ENTITY_LIST_HEADER.unpack(msb_buffer)
        entry_offsets = [
            self.MAP_ENTITY_ENTRY_OFFSET.unpack(msb_buffer)["entry_offset"]
            for _ in range(header["entry_offset_count"] - 1)
        ]
        next_entry_list_offset = self.MAP_ENTITY_LIST_TAIL.unpack(msb_buffer)["next_entry_list_offset"]
        self.name = read_chars_from_buffer(msb_buffer, header["name_offset"], encoding="utf-8")

        self._entries = []

        for entry_offset in entry_offsets:
            msb_buffer.seek(entry_offset)
            entry = self.ENTRY_CLASS(msb_buffer)
            self._entries.append(entry)

        msb_buffer.seek(next_entry_list_offset)

    def pack(self, start_offset=0, is_last_table=False):
        entries = self.get_entries()
        entry_offsets = []
        packed_entries = b""
        offset = start_offset + (
            self.MAP_ENTITY_LIST_HEADER.size
            + self.MAP_ENTITY_ENTRY_OFFSET.size * len(entries)
            + self.MAP_ENTITY_LIST_TAIL.size
        )
        packed_name = self.name.encode("utf-8")
        name_offset = offset
        while len(packed_name) % 4 != 0:
            packed_name += b"\0"
        offset += len(packed_name)
        for entry in entries:
            entry_offsets.append(offset)
            packed_entry = entry.pack()
            packed_entries += packed_entry
            offset += len(packed_entry)

        next_entry_list_offset = offset if not is_last_table else 0

        packed_header = self.MAP_ENTITY_LIST_HEADER.pack(name_offset=name_offset, entry_offset_count=len(entries) + 1,)
        packed_header += self.MAP_ENTITY_ENTRY_OFFSET.pack([{"entry_offset": o} for o in entry_offsets])
        packed_header += self.MAP_ENTITY_LIST_TAIL.pack(next_entry_list_offset=next_entry_list_offset)

        return packed_header + packed_name + packed_entries

    def __iter__(self) -> tp.Iterator[EntryType]:
        """Iterate over all entries."""
        return iter(self._entries)

    def __len__(self):
        """Count of all entries."""
        return len(self._entries)

    def __getitem__(self, entry_name_or_index) -> EntryType:
        """You can access entries using their name (if unique) or local type index."""
        if isinstance(entry_name_or_index, int):
            return self._entries[entry_name_or_index]
        elif isinstance(entry_name_or_index, str):
            return self.get_entry_by_name(entry_name_or_index)
        raise TypeError(f"`MSBEntryList` key must be an entry index or entry name, not {entry_name_or_index}.")

    def get_entry_by_name(self, entry_name: str, entry_type=None) -> EntryType:
        """Try to retrieve entry of given name. You can optionally specify the type (e.g. as a promise to yourself).

        Note that you can simply index the MSB entry list with a string (e.g. `msb.parts["h0000B0"]` as a shortcut to
        calling this method. It will raise a KeyError if the given name is not found OR if multiple entries with the
        given name (and type) are found.
        """
        entries = [entry for entry in self.get_entries(entry_type) if entry.name == entry_name]
        if not entries:
            raise KeyError(f"Entry name {entry_name} does not appear in {self.__class__.__name__}.")
        elif len(entries) >= 2:
            raise ValueError(
                f"Entry name {entry_name} appears more than once in "
                f"{self.__class__.__name__}. You must access it by index."
            )
        return entries[0]

    def get_entries(self, entry_type=None) -> tp.List[EntryType]:
        if entry_type is None:
            return self._entries  # Full entry list, with types potentially intermingled.
        entry_type = self.resolve_entry_type(entry_type)
        return [e for e in self._entries if e.ENTRY_TYPE == entry_type]

    def get_entry_names(self, entry_type=None) -> tp.List[str]:
        """Returns an ordered list of entry names (global or type-specific).

        Note that only the global index (`entry_type=None`) is valid for index links from other MSB entries, with the
        sole exception of the `MSBCollision` entry linked to by a `MapLoadTrigger` entry.
        """
        return [entry.name for entry in self.get_entries(entry_type=entry_type)]

    def get_entry_type(self, entry_name_or_index):
        """Returns type enum of given entry name or list-wide global index."""
        return self[entry_name_or_index].ENTRY_TYPE

    def get_entry_type_index(self, entry_name_or_index):
        """Get index of entry name or global index, local to its type.

        Useful for obtaining the type-sorted display index for the GUI.
        """
        if isinstance(entry_name_or_index, int):  # Convert to name.
            entry_name_or_index = self[entry_name_or_index].name
        entry_type = self.get_entry_type(entry_name_or_index)
        return self.get_entry_names(entry_type).index(entry_name_or_index)

    def get_entry_global_index(self, entry_name_or_local_index, entry_type=None):
        """Get global index of entry with given name or local entry type index. If a name is given, it must be unique.

        If a local index past the length of the given type sub-list is given, `None` is returned, which should be
        handled appropriately by the caller.
        """
        if isinstance(entry_name_or_local_index, int):
            if entry_type is None:
                raise ValueError("Cannot get global entry index from local index without specifying `entry_type`.")
            entry_type_names = self.get_entry_names(entry_type)
            if entry_name_or_local_index >= len(entry_type_names):
                return None
            entry_name = entry_type_names[entry_name_or_local_index]
        else:
            entry_name = entry_name_or_local_index
        entry_names = self.get_entry_names()
        if entry_names.count(entry_name) >= 2:
            raise ValueError(
                f"Cannot get global index of non-unique entry name {repr(entry_name)} "
                f"({entry_names.count(entry_name)} instances)."
            )
        if entry_name not in entry_names:
            raise ValueError(f"Cannot get global index of non-existent entry name {repr(entry_name)}.")
        return entry_names.index(entry_name)

    @classmethod
    def resolve_entry_type(cls, entry_type):
        """Converts any valid entry type specification into the proper type enum."""
        if isinstance(entry_type, cls.ENTRY_TYPE_ENUM):
            return entry_type
        try:
            if isinstance(entry_type, str):
                if entry_type in MAP_ENTRY_TYPES[cls.ENTRY_LIST_NAME]:
                    return MAP_ENTRY_TYPES[cls.ENTRY_LIST_NAME][entry_type]
                return getattr(cls.ENTRY_TYPE_ENUM, entry_type)
            elif isinstance(entry_type, int):
                return cls.ENTRY_TYPE_ENUM(entry_type)
            raise ValueError
        except ValueError:
            raise TypeError(f"Invalid entry type for entry list {cls.ENTRY_LIST_NAME}: {entry_type}")

    def add_entry(self, entry, global_index=None, append_to_entry_type=None):
        """Add entry at desired global index.

        If `global_index` is None, it defaults to the end of the given `append_to_entry_type` type, which in turn
        defaults to being the end of the global entry list.
        """
        if global_index is None:
            if append_to_entry_type is None:
                raise ValueError("You must provide `global_index` or `append_to_entry_type` to `add_entry()`.")
            entry_type = self.resolve_entry_type(append_to_entry_type)
            last_entry_local_index = len(self.get_entry_names(entry_type)) - 1
            if last_entry_local_index == -1:
                # No entries of given type exist. Fall back to global index.
                # TODO: Could also guess where new entry type should be inserted.
                global_index = len(self)
            else:
                global_index = self.get_entry_global_index(last_entry_local_index, entry_type) + 1
        self._entries.insert(global_index, entry)

    def delete_entry(self, entry_name_or_index) -> EntryType:
        """Delete (and return) entry at given global index or with given (unique) name."""
        if isinstance(entry_name_or_index, MSBEntry):
            entry_name_or_index = self.get_entry_global_index(entry_name_or_index.name)
        elif isinstance(entry_name_or_index, str):
            entry_name_or_index = self.get_entry_global_index(entry_name_or_index)
        if isinstance(entry_name_or_index, int):
            return self._entries.pop(entry_name_or_index)
        raise TypeError("Argument to `delete_entry()` must be an entry name or global index in its MSB list.")

    def delete_all_entries_of_type(self, entry_type):
        """Delete all entries of the given type."""
        for entry_name in self.get_entry_names(entry_type):
            self.delete_entry(entry_name)

    def duplicate_entry(self, entry_type, entry_name_or_index, insert_below_original=True, **kwargs) -> EntryType:
        """Duplicate an entry of the given type and local index or name.

        By default, the duplicated entry is inserted just below the source entry. If `insert_below_original=False`, it
        will instead be inserted at the end of its entry type (not global type).

        Any `kwargs` given will be passed to the `set()` method of the duplicated entry (which is then also returned for
        further modification if desired). Unless otherwise specified, the `name` of the new entry will also be given a
        unique '<i>' duplicate tag suffix to retain name uniqueness (which will be removed upon final pack).
        """
        local_index = self.get_entry_type_index(entry_name_or_index)
        source_entry = self.get_entries(entry_type)[local_index]
        duplicated = copy.deepcopy(source_entry)
        if kwargs.get("name", "") == source_entry.name:
            raise ValueError(f"Name of duplicated entry cannot be set to the source name: {source_entry.name})")
        if "name" not in kwargs:
            duplicate_tag_match = _DUPLICATE_TAG_MATCH.match(duplicated.name)
            existing_names = self.get_entry_names()
            if not duplicate_tag_match:
                new_duplicate_tag = 1
            else:
                # Find next available duplicate tag number.
                new_duplicate_tag = int(duplicate_tag_match.group(1)) + 1
                while f"{duplicated.name} <{new_duplicate_tag}>" in existing_names:
                    new_duplicate_tag += 1
            kwargs["name"] = f"{duplicated.name} <{new_duplicate_tag}>"
        if insert_below_original:
            global_index = self.get_entry_global_index(source_entry.name) + 1
        else:
            global_index = self.get_next_global_index_of_type(entry_type)
        self._entries.insert(global_index, duplicated)
        duplicated.set(**kwargs)
        return duplicated

    def get_next_global_index_of_type(self, entry_type) -> int:
        """Returns next global index of given `entry_type`, e.g. for inserting a new entry into the `MSBEntryList` at
        the end of its local type. This is inferred by just finding the last existing instance of that type.

        Note that Dark Souls may not read entries that do not appear in their contiguous local type lists, so this
        method is often necessary to find the correct place for a new entry.

        # TODO: Need to infer where to insert global index if no entries of that type yet exist (default ordering).
        """
        entry_type = self.resolve_entry_type(entry_type)
        last_global_index = max(i for i, entry in enumerate(self._entries) if entry.ENTRY_TYPE == entry_type)
        return last_global_index + 1
        # raise TypeError(f"Failed to detect next global index for unrecognized entry type: {entry_type}")

    def get_indices(self):
        """Returns a dictionary mapping entry names to their global indices for resolving named links before repacking.

        Raises a NameError if the same name appears more than once in the entry list, which can only happen if you
        explicitly copy a name.
        """
        entry_indices = {}
        for i, entry in enumerate(self._entries):
            if entry.name in entry_indices:
                raise NameError(
                    f"Name {repr(entry.name)} (type {entry.ENTRY_TYPE.name}) appears more than once in "
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


class MSBEntryEntity(MSBEntry, abc.ABC):
    def __init__(self):
        """Subclass of MSBEntry with 'entity_id' field (everything except Models). Useful for type checking."""
        super().__init__()
        self.entity_id = -1


class MSBEntryEntityCoordinates(MSBEntryEntity, abc.ABC):
    def __init__(self):
        """Subclass of MSBEntryEntity with `translate` and `rotate` fields, and `rotate_in_world` method.

        Inherited by both `MSBPart` and `MSBRegion`).
        """
        super().__init__()
        self._translate = Vector3.zero()
        self._rotate = Vector3.zero()

    def rotate_in_world(
        self, rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float], pivot_point=(0, 0, 0), radians=False,
    ):
        """Modify entity `translate` and `rotate` by rotating it around some `pivot_point` in world coordinates.

        Default `pivot_point` is the world origin (0, 0, 0).
        """
        rotation = resolve_rotation(rotation, radians)
        pivot_point = Vector3(pivot_point)
        # old_translate = self.translate
        # old_rotate = self.rotate
        self._rotate = (rotation @ Matrix3.from_euler_angles(self.rotate)).to_euler_angles()
        self._translate = (rotation @ (self.translate - pivot_point)) + pivot_point
        # _LOGGER.debug(f"Rotating {self.name}: {old_rotate} -> {self.rotate}\n"
        #               f"    (Translate: {old_translate} -> {self.translate})")

    @property
    def translate(self):
        return self._translate

    @translate.setter
    def translate(self, value):
        self._translate = Vector3(value)

    @property
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, value):
        self._rotate = Vector3(value)
