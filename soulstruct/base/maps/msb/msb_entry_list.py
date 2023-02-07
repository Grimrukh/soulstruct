from __future__ import annotations

__all__ = ["MSBEntryList"]

import copy
import logging
import typing as tp
from enum import IntEnum

from .msb_entry import MSBEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBEntryList"

if tp.TYPE_CHECKING:
    from .enums import BaseMSBSubtype

_LOGGER = logging.getLogger(__name__)

# Generic type to use when type-hinting list attributes on `MSB` subclasses.
MSBEntryType = tp.TypeVar("MSBEntryType", bound=MSBEntry)


class MSBEntryList(list[MSBEntryType]):

    supertype_name: str
    subtype_enum: BaseMSBSubtype
    subtype_class: tp.Type[MSBEntryType]

    def __init__(
        self, supertype_name: str, subtype_enum: BaseMSBSubtype, subtype_class: tp.Type[MSBEntryType], *entries
    ):
        self.supertype_name = supertype_name
        self.subtype_enum = subtype_enum
        self.subtype_class = subtype_class
        super().__init__(*entries)

    def copy(self) -> Self:
        return copy.deepcopy(self)

    def find_entry_intenum(self, entry_intenum: IntEnum) -> MSBEntryType:
        return self.find_entry_name(entry_intenum.name)

    def find_entry_name(self, entry_name: str) -> MSBEntryType:
        """Try to retrieve entry with given name."""
        entries = [entry for entry in self if entry.name == entry_name]
        if not entries:
            raise KeyError(f"Entry name '{entry_name}' does not appear in {self.__class__.__name__}.")
        elif len(entries) >= 2:
            raise ValueError(
                f"Entry name '{entry_name}' appears more than once in {self.__class__.__name__}. You must access it by "
                f"global index or local subtype-specific index."
            )
        return entries[0]

    def find_entry_names(self, entry_names: tp.Container[str]) -> list[MSBEntryType]:
        return [entry for entry in self if entry.name in entry_names]

    def sort_by_name(self):
        """Sort entries in subtype by name, alphabetically."""
        self.sort(key=lambda entry: entry.name)

    def get_entry_names(self) -> list[str]:
        """Returns a list of `MSBEntry` names."""
        return [entry.name for entry in self]

    def get_entity_id_dict(self) -> dict[int, MSBEntry]:
        """Get a dictionary mapping entity IDs to `MSBEntry` instances for this subtype list.

        If multiple `MSBEntry` instances are found for a given ID, a warning is logged, and only the *first* one found
        is used (which matches game engine behavior).

        Raises a `TypeError` if `entity_id` is not defined on this subtype.
        """
        entries_by_id = {}
        for entry in self:
            entity_id = entry.get_entity_id()
            if entity_id is None:
                raise TypeError(f"`entity_id` is not a valid field for MSB subtype `{self.subtype_enum.name}`.")
            if entity_id <= 0:
                continue  # ignore null ID
            if entity_id in entries_by_id:
                _LOGGER.warning(
                    f"Found multiple `{self.subtype_enum.name}` entries for entity ID {entity_id}. Only using first."
                )
            else:
                entries_by_id[entity_id] = entry
        return entries_by_id

    def get_filtered_list(self, filter_func: tp.Callable[[MSBEntry], bool]) -> MSBEntryList[MSBEntryType]:
        """Returns a filtered deep copy of this subtype list by applying `filter_func` to each entry."""
        if filter_func is None:
            return self.copy()
        return MSBEntryList(
            self.supertype_name,
            self.subtype_enum,
            self.subtype_class,
            *[entry.copy() for entry in self if filter_func(entry)],
        )

    def new(self, **kwargs) -> MSBEntryType:
        """Create a new `MSBEntry` of this list's subtype and append it to list."""
        # noinspection PyArgumentList
        entry = self.subtype_class(**kwargs)
        self.append(entry)
        return entry

    def duplicate(self, entry_or_index: MSBEntryType | int, at_next_index=True, **kwargs) -> MSBEntryType:
        """Duplicate the specified `entry`.

        By default, the duplicated entry is inserted just below the source entry. If `at_next_index=False`, it
        will instead be inserted at the end of its entry subtype (not global subtype).

        Any `kwargs` given will be passed to the `set()` method of the duplicated entry (which is then also returned for
        further modification if desired). Unless otherwise specified, the `name` of the new entry will also be given a
        unique '<i>' duplicate tag suffix to retain name uniqueness (which will be removed upon final pack).

        You can also call this with `add_{subtype}(copy_entry=entry, at_next_index=True, **kwargs)`.
        """
        if isinstance(entry_or_index, int):
            entry = self[entry_or_index]
            index = entry_or_index
        elif isinstance(entry_or_index, MSBEntry):
            entry = entry_or_index
            index = self.index(entry)  # -1 if not found
        else:
            raise TypeError("`entry_or_index` must be an `MSBEntry` or index of one in this list.")
        
        duplicated = entry.copy()
        if "entity_enum" in kwargs:
            duplicated.entity_enum = kwargs.pop("entity_enum")
        elif "name" in kwargs:
            duplicated.name = kwargs.pop("name")
        else:
            duplicated.name += " <COPY>"

        for field_name, field_value in kwargs.items():
            setattr(duplicated, field_name, field_value)

        if at_next_index and index != -1:
            self.insert(index, duplicated)
        else:
            if at_next_index:
                _LOGGER.warning(
                    f"Cannot insert duplicate of entry `{entry.name}` at next index (entry is not in this list)."
                )
            self.append(duplicated)

        return duplicated

    def to_dict(self, ignore_defaults=True) -> [dict[str, list[dict[str, tp.Any]]]]:
        """Get the entry list as a dictionary mapping the entry subtype name to a list of entry dictionaries."""
        return {self.subtype_enum.name: [entry.to_dict(ignore_defaults=ignore_defaults) for entry in self]}
