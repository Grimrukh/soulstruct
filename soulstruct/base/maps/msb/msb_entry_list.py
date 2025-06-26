from __future__ import annotations

__all__ = ["MSBEntryList"]

import copy
import logging
import typing as tp
from enum import IntEnum

from soulstruct.utilities.misc import IDList

from .msb_entry import MSBEntry

if tp.TYPE_CHECKING:
    from .core import MSB

_LOGGER = logging.getLogger(__name__)

# Generic type to use when type-hinting list attributes on `MSB` subclasses.
MSBEntryType = tp.TypeVar("MSBEntryType", bound=MSBEntry)


# NOT a dataclass.
class MSBEntryList(IDList[MSBEntryType]):

    supertype: str
    entry_class: type[MSBEntryType]  # may be an abstract base class for transient supertype lists

    def __init__(
        self,
        entries: tp.Iterable[MSBEntryType],
        supertype: str,
        entry_class: type[MSBEntryType],
    ):
        self.supertype = supertype
        self.entry_class = entry_class
        super().__init__(entries)

    def copy(self) -> tp.Self:
        return copy.deepcopy(self)

    def find_entry_intenum(self, entry_intenum: IntEnum) -> MSBEntryType:
        return self.find_entry_name(entry_intenum.name)

    def find_entry_name(self, entry_name: str | IntEnum) -> MSBEntryType:
        """Try to retrieve entry with given name."""
        if isinstance(entry_name, IntEnum):
            entry_name = entry_name.name
        entries = [entry for entry in self if entry.name == entry_name]
        if not entries:
            raise KeyError(f"Entry name '{entry_name}' does not appear in MSB `{self.subtype_name}` list.")
        elif len(entries) > 1:
            print(entries)
            raise ValueError(
                f"Entry name '{entry_name}' appears more than once in MSB `{self.subtype_name}` list. You must access "
                f"it by global index or local subtype-specific index."
            )
        return entries[0]

    def find_entry_names(self, entry_names: tp.Container[str]) -> list[MSBEntryType]:
        return [entry for entry in self if entry.name in entry_names]

    def __getitem__(self, index_or_name: int | IntEnum | str) -> MSBEntryType:
        if isinstance(index_or_name, IntEnum):
            # Search by enum name.
            return self.find_entry_name(index_or_name.name)
        if isinstance(index_or_name, int):
            return super().__getitem__(index_or_name)
        return self.find_entry_name(index_or_name)

    def sort_by_name(self):
        """Sort entries in subtype by name, alphabetically."""
        self.sort(key=lambda entry: entry.name)

    def get_entry_names(self) -> list[str]:
        """Returns a list of `MSBEntry` names."""
        return [entry.name for entry in self]

    def get_entries_by_unique_name(self) -> tuple[dict[str, MSBEntry], set[str]]:
        """Returns a dictionary mapping `MSBEntry` names to the entries, but only for entries with unique names.

        Also returns a set of non-unique names so users can tell if their references are missing or ambiguous.
        """
        unique_entries = {}
        non_unique_names = set()
        for entry in self:
            if entry.name in non_unique_names:
                continue
            if entry.name in unique_entries:
                # First duplicate name found.
                non_unique_names.add(entry.name)
                del unique_entries[entry.name]
            else:
                unique_entries[entry.name] = entry
        return unique_entries, non_unique_names

    def get_entity_id_dict(self, sort_by_entity_id=False) -> dict[int, MSBEntry]:
        """Get a dictionary mapping entity IDs to `MSBEntry` instances for this subtype list.

        If multiple `MSBEntry` instances are found for a given ID, a warning is logged, and only the *first* one found
        is used (which matches game engine behavior).

        Raises a `TypeError` if `entity_id` is not defined on this subtype.
        """
        entries_by_id = {}
        for entry in self:
            entity_id = entry.get_entity_id()
            if entity_id is None:
                raise TypeError(
                    f"`entity_id` is not a valid field for MSB subtype `{self.subtype_name}`."
                )
            if entity_id <= 0:
                continue  # ignore null ID
            if entity_id in entries_by_id:
                _LOGGER.warning(
                    f"Found multiple `{self.subtype_name}` entries for entity ID {entity_id}. Only using first."
                )
            else:
                entries_by_id[entity_id] = entry
        if sort_by_entity_id:
            entries_by_id = {k: entries_by_id[k] for k in sorted(entries_by_id.keys())}
        return entries_by_id

    def get_filtered_list(self, filter_func: tp.Callable[[MSBEntry], bool]) -> MSBEntryList[MSBEntryType]:
        """Returns a filtered deep copy of this subtype list by applying `filter_func` to each entry."""
        if filter_func is None:
            return self.copy()
        return MSBEntryList(
            [entry.copy() for entry in self if filter_func(entry)],
            supertype=self.supertype,
            entry_class=self.entry_class,
        )

    def default_entry(self) -> MSBEntryType:
        """Create a new `MSBEntry` of this list's subtype, with all default field values, and return it.

        Does NOT add the new entry to this list, unlike `new()`.
        """
        # noinspection PyArgumentList
        return self.entry_class(name=f"Default{self.entry_class.__name__}")

    def new(self, new_index=-1, /, **kwargs) -> MSBEntryType:
        """Create a new `MSBEntry` of this list's subtype and append it to list (or insert it at `new_index`)."""
        if "entity_enum" in kwargs:
            if "name" in kwargs or "entity_id" in kwargs:
                raise ValueError(
                    "Cannot specify both `entity_enum` and `name` or `entity_id` when creating a new MSB entry."
                )
            entity_enum = kwargs.pop("entity_enum")
            kwargs["name"] = entity_enum.name
            kwargs["entity_id"] = entity_enum.value
        # noinspection PyArgumentList
        kwargs.setdefault("name", f"Default{self.entry_class.__name__}")
        # noinspection PyArgumentList
        entry = self.entry_class(**kwargs)
        if new_index >= 0:
            self.insert(new_index, entry)
        else:
            self.append(entry)
        return entry

    def duplicate(
        self, entry_or_index_or_name: MSBEntryType | int | str | IntEnum, index_offset: int = None, **kwargs
    ) -> MSBEntryType:
        """Duplicate the specified `entry`.

        If `index_offset = 0` (default), the duplicated entry will be inserted right after the source entry. Higher
        values will insert it further ahead in the list. A value of -1 will insert it at the end of the list. If the
        source entry is not in this list, the new entry will always be added at the end.

        Any `kwargs` given will be passed to the `set()` method of the duplicated entry (which is then also returned for
        further modification if desired). Unless otherwise specified, the `name` of the new entry will also be given a
        '<COPY>' duplicate tag suffix, which must be edited/removed by the user.
        """
        if isinstance(entry_or_index_or_name, IntEnum):
            entry_or_index_or_name = entry_or_index_or_name.name
        if isinstance(entry_or_index_or_name, int):
            entry = self[entry_or_index_or_name]
            index = entry_or_index_or_name + 1
        elif isinstance(entry_or_index_or_name, str):
            entry = self.find_entry_name(entry_or_index_or_name)
            index = self.index(entry)  # -1 if not found
            if index >= 0:
                index += 1
        elif isinstance(entry_or_index_or_name, MSBEntry):
            entry = entry_or_index_or_name
            index = self.index(entry)  # -1 if not found
            if index >= 0:
                index += 1
        else:
            raise TypeError("`entry_or_index_or_name` must be an `MSBEntry` or index of one in this list.")
        
        duplicated = entry.copy()
        if "entity_enum" in kwargs:
            duplicated.entity_enum = kwargs.pop("entity_enum")
        elif "name" in kwargs:
            duplicated.name = kwargs.pop("name")
        else:
            duplicated.name += " <COPY>"

        for field_name, field_value in kwargs.items():
            setattr(duplicated, field_name, field_value)

        if index_offset is None:
            index_offset = 0 if index != -1 else -1

        if index_offset >= 0 and index != -1:
            self.insert(index + index_offset, duplicated)
        else:
            if index_offset >= 0 and index != -1:
                _LOGGER.warning(
                    f"Cannot insert duplicate of entry `{entry.name}` at index offset {index_offset} (source entry is "
                    f"not in this list). Inserting at end."
                )
            self.append(duplicated)

        return duplicated

    def to_dict(self, ignore_defaults=True) -> [dict[str, list[dict[str, tp.Any]]]]:
        """Get the entry list as a dictionary mapping the entry subtype name to a list of entry dictionaries."""
        return {
            self.subtype_name: [entry.to_dict(ignore_defaults=ignore_defaults) for entry in self]
        }

    def to_json_dict(self, msb: MSB, ignore_defaults=True) -> [dict[str, list[dict[str, tp.Any]]]]:
        """Get the entry list as a dictionary mapping the entry subtype name to a list of entry dictionaries.

        Fully serializes inter-entry references as name/index dictionaries.
        """
        return {
            self.subtype_name: [entry.to_json_dict(msb, ignore_defaults) for entry in self]
        }

    # NOTE: No `from_json_dict` method; `MSB` handles this.

    @property
    def subtype_name(self) -> str:
        return self.entry_class.SUBTYPE_ENUM.name
