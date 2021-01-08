"""TODO: Dictionary read/write for all classes."""
from __future__ import annotations

import abc
import io
import logging
import re
import typing as tp
from copy import deepcopy
from functools import wraps

from soulstruct.maps.core import MapFieldInfo, MapError
from soulstruct.utilities import read_chars_from_buffer, unpack_from_buffer
from soulstruct.utilities.binary_struct import BinaryStruct
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation

if tp.TYPE_CHECKING:
    from soulstruct.maps.enums import MSBSubtype

_LOGGER = logging.getLogger(__name__)

_DUPLICATE_TAG_MATCH = re.compile(r"(.*)<(\d+)>$")


class MSBEntry(abc.ABC):

    ENTRY_SUBTYPE = None  # type: MSBSubtype
    FIELD_INFO = {}  # type: dict[str, MapFieldInfo]
    FIELD_ORDER = ()  # If given, fields will be displayed in this order. Otherwise uses order of `FIELD_INFO` keys.

    def __init__(self, source=None, **kwargs):
        """Base class for entries of any type and subtype that appear in an `MSB` (under one of the four entry lists).

        If `source` is given, it must be binary data (`bytes` or a byte buffer). You are unlikely to ever do this
        yourself; it is typically only done when a complete `MSB` is unpacked. No keyword arguments may be given in this
        case other than `description`, which will override an unpacked `description` for games that have that field.

        If `source` is not given, any keyword arguments may be given that are valid attributes for the instantiated
        subclass. In this case, `name` is compulsory; all other unspecified values will be set to their defaults.
        """
        self.name = ""
        self.description = ""  # supported by Soulstruct even when game lacks it

        if isinstance(source, bytes):
            source = io.BytesIO(source)
        if isinstance(source, io.BufferedIOBase):
            description = kwargs.pop("description", None)
            if kwargs:
                raise ValueError("Cannot instantiate MSB entry using `kwargs` if binary `source` is given.")
            self.set_defaults()
            self.unpack(source)
            if self.description and description is not None:
                _LOGGER.warning(f"`description` arg will override unpacked description for MSB entry '{self.name}'.")
                self.description = description
        elif source is None:
            try:
                self.name = kwargs.pop("name")
            except KeyError:
                raise ValueError(f"`name` must be given to `{self.__class__.__name__}` if no binary `source` is given.")
            self.description = kwargs.pop("description", "")
            for field_name, field_info in self.FIELD_INFO.items():
                try:
                    value = kwargs.pop(field_name)
                except KeyError:
                    try:
                        value = field_info.default.copy()  # mutable default
                    except AttributeError:
                        value = field_info.default  # immutable default
                setattr(self, field_name, value)
            if kwargs:
                raise ValueError(f"Invalid arguments for MSB entry class `{self.__class__.__name__}`: {tuple(kwargs)}")
        else:
            raise TypeError(f"`{self.__class__.__name__}` source must be a buffer, `bytes`, or `None` (default).")

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
            if field_name not in self.FIELD_INFO:
                raise KeyError(f"Field {repr(field_name)} does not exist in MSB entry type {self.__class__.__name__}.")
            setattr(self, field_name, value)

    def set(self, **kwargs):
        """Update any attribute fields with keyword arguments.

        Argument keys starting with double underscore are ignored so that `BinaryStruct`-produced dictionaries can
        easily be passed in. See `__setitem__()` for more.
        """
        for field_name, value in kwargs.items():
            if not field_name.startswith("__"):
                self[field_name] = value

    def set_defaults(self):
        for field_name, field_info in self.FIELD_INFO.items():
            try:
                setattr(self, field_name, field_info.default)
            except AttributeError as ex:
                raise AttributeError(
                    f"Could not set attribute '{field_name}' in class `{self.__class__.__name__}`.\n"
                    f"Error: {ex}")

    def copy(self):
        return deepcopy(self)

    @property
    def field_names(self):
        if self.FIELD_ORDER:
            return self.FIELD_ORDER
        return tuple(self.FIELD_INFO.keys())

    @property
    def all_field_names(self):
        """Includes hidden field names absent from `FIELD_ORDER`, which appear after all non-hidden fields."""
        if not self.FIELD_ORDER:
            return self.field_names  # no hidden fields or desired display order
        field_names = self.field_names
        hidden_fields = [field for field in self.FIELD_INFO.keys() if field not in field_names]
        return self.FIELD_ORDER + tuple(hidden_fields)

    def __repr__(self):
        kwargs = {}
        default = self.__class__(name="__DEFAULT__")
        for name in self.field_names:
            value = getattr(self, name)
            default_value = getattr(default, name)
            if value == default_value:
                continue  # ignore default values
            kwargs[name] = value
        if kwargs:
            fields = "\n    ".join(f"{k}={repr(v)}," for k, v in kwargs.items())
            return f"{self.__class__.__name__}(\n    name={repr(self.name)},\n    {fields}\n)"
        return f"{self.__class__.__name__}(name={repr(self.name)})"


MSBEntryType = tp.TypeVar("MSBEntryType", bound=MSBEntry)
EntrySpecType = tp.Union[MSBEntry, int, str]  # valid entry specifications: entry instance, local index, or name


def _entry_lookup(func):
    @wraps(func)
    def wrapped(self: MSBEntryList, entry: EntrySpecType, entry_subtype: MSBSubtype = None, *args, **kwargs):
        if isinstance(entry, int):
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


class MSBEntryList(abc.ABC, tp.Generic[MSBEntryType]):

    MAP_ENTITY_LIST_HEADER: BinaryStruct = None
    MAP_ENTITY_ENTRY_OFFSET: BinaryStruct = None
    MAP_ENTITY_LIST_TAIL: BinaryStruct = None
    NAME_ENCODING = ""
    PLURALIZED_NAME = ""
    ENTRY_SUBTYPE_ENUM: tp.Union[type, tp.Iterable] = None
    SUBTYPE_CLASSES: dict[MSBSubtype, tp.Type[MSBEntry]] = None
    SUBTYPE_OFFSET: int = None  # binary `MSBEntry` offset where subtype integer can be read from

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
            msb_entry_list_source = io.BytesIO(msb_entry_list_source)
        if isinstance(msb_entry_list_source, io.BufferedIOBase):
            self.unpack(msb_entry_list_source)
        else:
            raise TypeError(f"Invalid MSB entry list source: {msb_entry_list_source}")

    def unpack(self, msb_buffer):
        header = self.MAP_ENTITY_LIST_HEADER.unpack(msb_buffer)
        entry_offsets = [
            self.MAP_ENTITY_ENTRY_OFFSET.unpack(msb_buffer)["entry_offset"]
            for _ in range(header["entry_offset_count"] - 1)  # 'entry_offset_count' includes tail offset
        ]
        next_entry_list_offset = self.MAP_ENTITY_LIST_TAIL.unpack(msb_buffer)["next_entry_list_offset"]
        self.name = read_chars_from_buffer(msb_buffer, header["name_offset"], encoding=self.NAME_ENCODING)

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
        while len(packed_name) < 32:
            packed_name += b"\0"
        offset += len(packed_name)
        for i, entry in enumerate(entries):
            entry_offsets.append(offset)
            packed_entry = self.pack_entry(i, entry)
            packed_entries += packed_entry
            offset += len(packed_entry)

        next_entry_list_offset = offset if not is_last_table else 0

        packed_header = self.MAP_ENTITY_LIST_HEADER.pack(name_offset=name_offset, entry_offset_count=len(entries) + 1,)
        packed_header += self.MAP_ENTITY_ENTRY_OFFSET.pack([{"entry_offset": o} for o in entry_offsets])
        packed_header += self.MAP_ENTITY_LIST_TAIL.pack(next_entry_list_offset=next_entry_list_offset)

        return packed_header + packed_name + packed_entries

    @classmethod
    def ENTRY_CLASS(cls, msb_buffer):
        """Detects the appropriate subclass of `MSBPart` to instantiate, and does so."""
        entry_subtype_int = unpack_from_buffer(msb_buffer, "i", offset=cls.SUBTYPE_OFFSET, relative_offset=True)[0]
        try:
            entry_subtype = cls.ENTRY_SUBTYPE_ENUM(entry_subtype_int)
        except ValueError:
            raise MapError(f"Entry of type {cls.ENTRY_SUBTYPE_ENUM} has invalid subtype enum: {entry_subtype_int}")
        return cls.SUBTYPE_CLASSES[entry_subtype](msb_buffer)

    @abc.abstractmethod
    def pack_entry(self, index: int, entry: MSBEntryType):
        """Pack entry (some entry types may use `index`)."""

    def __iter__(self) -> tp.Iterator[MSBEntryType]:
        """Iterate over all entries."""
        return iter(self._entries)

    def __len__(self):
        """Count of all entries."""
        return len(self._entries)

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

    def __getitem__(self, entry: tp.Union[int, str]) -> MSBEntryType:
        """You can access entries using their global index or (if unique) name."""
        if isinstance(entry, int):
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
            return self._entries  # Full entry list, with types potentially intermingled.
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        return [e for e in self._entries if e.ENTRY_SUBTYPE == entry_subtype]

    def get_entry_names(self, entry_subtype=None) -> list[str]:
        """Returns a list of entry names (global or `entry_subtype`-specific)."""
        return [entry.name for entry in self.get_entries(entry_subtype=entry_subtype)]

    def get_entry_by_name(self, entry_name: str, entry_subtype=None) -> MSBEntryType:
        """Try to retrieve entry with given name.

        You can optionally specify the subtype. Names shouldn't be shared across subtypes, but if they are (or as an
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
        entry_subtype: MSBSubtype,
        copy_entry: MSBEntryType = None,
        insert_below_original=True,
        auto_add=True,
        **kwargs,
    ):
        """Create a new `MSBEntry` of the given type (or duplicate from `copy_entry=entry`), apply any `kwargs` to it,
        add it to this `MSBEntryList` if `auto_add=True` (default), then return it.

        Use the `new_{subtype}()` shortcut methods to avoid specifying `entry_subtype` and use return type hinting.
        """
        if copy_entry is not None:
            return self.duplicate_entry(
                entry=copy_entry,
                entry_subtype=entry_subtype,
                auto_add=auto_add,
                insert_below_original=insert_below_original,
                **kwargs,
            )
        if "name" not in kwargs or kwargs["name"] is None:
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

        if kwargs.get("name", "") == entry.name:
            raise ValueError(f"Name of duplicated entry cannot be set to the source entry's name: {entry.name}")
        if "name" not in kwargs or kwargs["name"] is None:
            kwargs["name"] = self._get_duplicate_tagged_name(duplicated.name)
        duplicated.set(**kwargs)

        if auto_add:
            if insert_below_original:
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

    def get_subtype_next_global_index(self, entry_subtype: MSBSubtype) -> int:
        """Returns next global index of given `entry_subtype`, e.g. for inserting a new entry into the `MSBEntryList` at
        the end of its local subtype. This is inferred by just finding the last existing instance of that subtype.

        Note that the game may not read entries that do not appear in their contiguous local subtype lists, so this
        method is often necessary to find the correct place for a new entry. (This has been confirmed for
        `MSBTreasureEvent`, for example.)
        """
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        try:
            last_global_index = max(i for i, entry in enumerate(self._entries) if entry.ENTRY_SUBTYPE == entry_subtype)
        except ValueError:  # no entries of given subtype exist yet
            # Iterate over entries in enum order to find correct global index.
            last_global_index = 0
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


class MSBEntryEntity(MSBEntry, abc.ABC):
    """Subclass of MSBEntry with 'entity_id' field (everything except Models). Useful for type checking."""

    FIELD_INFO = MSBEntry.FIELD_INFO | {
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to this entry in other game files.",
        ),
    }

    entity_id: int


class MSBEntryEntityCoordinates(MSBEntryEntity, abc.ABC):
    """Subclass of MSBEntryEntity with `translate` and `rotate` fields, and `rotate_in_world` method.

    Inherited by both `MSBPart` and `MSBRegion`).
    """

    FIELD_INFO = MSBEntryEntity.FIELD_INFO | {
        "translate": MapFieldInfo(
            "Translate",
            Vector3,
            Vector3.zero(),
            "3D coordinates of the part's position. Note that the anchor of the part is usually at its base.",
        ),
        "rotate": MapFieldInfo(
            "Rotate",
            Vector3,
            Vector3.zero(),
            "Euler angles for part rotation around its local X, Y, and Z axes.",
        ),
    }

    translate: Vector3
    rotate: Vector3

    def __init__(self, source=None, **kwargs):
        self._translate = Vector3.zero()
        self._rotate = Vector3.zero()
        super().__init__(source=source, **kwargs)

    def apply_rotation(
        self, rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float], pivot_point=(0, 0, 0), radians=False,
    ):
        """Modify entity `translate` and `rotate` by rotating entity around some `pivot_point` in world coordinates.

        Default `pivot_point` is the world origin (0, 0, 0). Default rotation units are degrees.
        """
        rotation = resolve_rotation(rotation, radians)
        pivot_point = Vector3(pivot_point)
        self._rotate = (rotation @ Matrix3.from_euler_angles(self.rotate)).to_euler_angles()
        self._translate = (rotation @ (self.translate - pivot_point)) + pivot_point

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
        if isinstance(value, (int, float)):
            self._rotate = Vector3(0, value, 0)
        else:
            self._rotate = Vector3(value)
