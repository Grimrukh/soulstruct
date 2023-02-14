from __future__ import annotations

__all__ = ["MSBEntry"]

import abc
import copy
import logging
import typing as tp
from dataclasses import dataclass, field, fields, MISSING
from enum import IntEnum
from types import GenericAlias

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector, Vector2, Vector3, Vector4
from soulstruct.utilities.text import pad_chars

from .enums import BaseMSBSubtype
from .utils import MSBBrokenEntryReference

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBEntry"

if tp.TYPE_CHECKING:
    from .core import MSB

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True, eq=False, repr=False)
class MSBEntry(abc.ABC):
    """Base class for entries of any type and subtype that appear in an `MSB` (under one of four entry superlists)."""

    # Shared between all game MSB entries. TODO: Infer from `reader.varint_size`?
    NAME_ENCODING: tp.ClassVar[str]
    # Generally only used to check against unpacked indices (which should have already been 'peeked' by the MSB).
    SUBTYPE_ENUM: tp.ClassVar[tp.Type[BaseMSBSubtype]]
    # These fields will be marked as hidden in the GUI.
    HIDE_FIELDS: tp.ClassVar[tuple[str, ...]] = ()
    # Cached when first accessed. Maps field names to types for enforcement.
    _FIELD_TYPES: tp.ClassVar[dict[str, str]] = {}

    # Structs for header, supertype data, and (optional but common) subtype data.
    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[tp.Type[NewBinaryStruct]]
    SUPERTYPE_DATA_STRUCT: tp.ClassVar[tp.Type[NewBinaryStruct]]
    SUBTYPE_DATA_STRUCT: tp.ClassVar[tp.Type[NewBinaryStruct]]

    # Basic data fields.
    name: str
    description: str = field(default="", kw_only=True)  # not actually present in MSB until DS2

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Default minimal method. Most subclasses can just override one of the header/data unpack methods."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)
        reader.seek(entry_offset + kwargs.pop("supertype_data_offset"))
        kwargs |= cls.unpack_supertype_data(reader)
        relative_subtype_data_offset = kwargs.pop("subtype_data_offset")
        if relative_subtype_data_offset > 0:
            reader.seek(entry_offset + relative_subtype_data_offset)
            kwargs |= cls.unpack_subtype_data(reader)

        return cls(**kwargs)

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")
        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        return header.to_dict(ignore_underscore_prefix=True) | {"name": name}

    @classmethod
    def unpack_supertype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        """Returns dictionary of ALL struct fields by default. Subclasses may want to modify them first."""
        return cls.SUPERTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

    @classmethod
    def unpack_subtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        """Returns dictionary of ALL struct fields by default. Subclasses may want to modify them first."""
        return cls.SUBTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, list[MSBEntry]]
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        entry_offset = writer.position
        self.pack_header(writer, entry_offset, supertype_index, subtype_index, entry_lists)
        supertype_data_offset = writer.position - entry_offset if self.SUPERTYPE_DATA_STRUCT is not None else 0
        writer.fill("supertype_data_offset", supertype_data_offset, obj=self)
        self.pack_supertype_data(writer, entry_offset, entry_lists)
        subtype_data_offset = writer.position - entry_offset if self.SUBTYPE_DATA_STRUCT is not None else 0
        writer.fill("subtype_data_offset", subtype_data_offset, obj=self)
        self.pack_subtype_data(writer, entry_lists)

    def pack_header(
        self,
        writer: BinaryWriter,
        entry_offset: int,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
    ):
        header_offset = writer.position
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            _supertype_index=supertype_index,
            _subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=subtype_index,
            supertype_data_offset=RESERVED,
            subtype_data_offset=RESERVED,
        )
        writer.fill("name_offset", writer.position - header_offset, obj=self)
        writer.append(pad_chars(self.name, encoding=self.NAME_ENCODING, alignment=4))

    def pack_supertype_data(self, writer: BinaryWriter, entry_offset: int, entry_lists: dict[str, list[MSBEntry]]):
        if self.SUPERTYPE_DATA_STRUCT is not None:
            self.SUPERTYPE_DATA_STRUCT.object_to_writer(self, writer)

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        if self.SUBTYPE_DATA_STRUCT is not None:
            self.SUBTYPE_DATA_STRUCT.object_to_writer(self, writer)

    def __getitem__(self, field_name: str):
        try:
            return getattr(self, field_name)
        except AttributeError:
            raise KeyError(f"Field {field_name} does not exist in MSB entry type {self.__class__.__name__}.")

    def __setitem__(self, field_name: str, value: tp.Any):
        """Alias for setting the given attribute. Resolves `IntEnum`s to values."""
        if isinstance(value, IntEnum):
            value = value.value
        try:
            setattr(self, field_name, value)
        except AttributeError:
            raise KeyError(f"Field {repr(field_name)} does not exist in MSB entry type {self.__class__.__name__}.")

    def get_entity_id(self) -> int | None:
        """`entity_id` is a critical field for most MSB entries, but not quite all of them (and not models).

        This method simply returns the `entity_id` field if it exists, or `None` otherwise.
        """
        return getattr(self, "entity_id", None)

    @property
    def entity_enum(self):
        raise AttributeError(
            "You can set `MSBEntry.entity_enum` as a way to set both `name` and `entity_id`, but cannot access it."
        )

    @entity_enum.setter
    def entity_enum(self, value: IntEnum):
        """Set both entry `name` and `entity_id` (if valid) for this entry."""
        if not hasattr(self, "entity_id"):
            raise AttributeError(f"MSB entry type `{self.__class__.__name__}` does not have an `entity_id`.")
        setattr(self, "name", value.name)
        setattr(self, "entity_id", value.value)

    def copy(self):
        """Copy entry with only shallow copies of fields referencing other `MSBEntry`s."""
        copied_dict = {}
        for f in fields(self):
            value = getattr(self, f.name)
            if isinstance(value, MSBEntry):
                # Shallow copied reference.
                copied_dict[f.name] = value
            elif isinstance(value, (list, tuple, set)):
                if any(isinstance(element, MSBEntry) for element in value):
                    # Shallow copied references.
                    copied_dict[f.name] = copy.copy(value)
                else:
                    # Deep copy list/tuple/set.
                    copied_dict[f.name] = copy.deepcopy(value)
            else:
                # Deep copy.
                copied_dict[f.name] = copy.deepcopy(value)

        return self.from_dict(copied_dict)

    def get_field_names(self, visible_only=False) -> tuple[str]:
        """Get all field names in `FIELD_ORDER`, or all names excluding basic 'name' and 'description'."""
        return tuple(
            f.name for f in fields(self)
            if f.name not in {"name", "description"}
            and (not visible_only or f.name not in self.HIDE_FIELDS)
        )

    def set_entity_enum(self, entity_enum: IntEnum):
        """Only works for subclasses with `entity_id` field."""
        if not isinstance(entity_enum, IntEnum):
            raise TypeError(f"`entity_enum` must be an `IntEnum` subclass, not `{type(entity_enum)}`.")
        if "entity_id" in self.get_field_names(visible_only=False):
            setattr(self, "entity_id", entity_enum.value)
            self.name = entity_enum.name
        else:
            raise TypeError(f"MSB entry class `{self.__class__.__name__}` has no `entity_id` field.")

    @classmethod
    def from_dict(cls, data: dict[str, tp.Any]) -> Self:
        """Standard dictionary loader."""
        return cls(**data)

    @classmethod
    def from_json_dict(cls, data: dict[str, tp.Any], msb: MSB) -> Self:
        """Converts reference dictionaries to entries."""
        try:
            kwargs = {"name": data["name"]}
        except KeyError:
            raise ValueError("`MSBEntry` JSON dict must have 'name' field.")
        for field_name, field_value in data.items():
            if isinstance(field_value, dict):
                try:
                    subtype_list_name = field_value["subtype_list_name"]
                    subtype_index = field_value["subtype_index"]
                except KeyError:
                    raise ValueError(
                        "`MSBEntry` JSON `dict` fields must be references to other entries with exact keys:\n"
                        "    'subtype_list_name', 'subtype_index'"
                    )
                try:
                    kwargs[field_name] = msb[subtype_list_name][subtype_index]
                except IndexError:
                    raise ValueError(
                        f"`MSBEntry` JSON dict '{kwargs['name']}' field `{field_name}` references an invalid entry "
                        f"in this MSB: {subtype_list_name}[{subtype_index}]"
                    )
            elif isinstance(field_value, list) and any(isinstance(element, dict) for element in field_value):
                entry_list = []
                for element in field_value:
                    if element is None:
                        entry_list.append(None)
                        continue
                    try:
                        subtype_list_name = element["subtype_list_name"]
                        subtype_index = element["subtype_index"]
                    except KeyError:
                        raise ValueError(
                            "`MSBEntry` JSON `dict` fields must be references to other entries with exact keys:\n"
                            "    'subtype_list_name', 'subtype_index'"
                        )
                    try:
                        element_entry = msb[subtype_list_name][subtype_index]
                    except IndexError:
                        raise ValueError(
                            f"`MSBEntry` JSON dict '{kwargs['name']}' field `{field_name}` references an invalid entry "
                            f"in this MSB: {subtype_list_name}[{subtype_index}]"
                        )
                    entry_list.append(element_entry)
                kwargs[field_name] = entry_list
            else:
                kwargs[field_name] = field_value  # try direct assignment

        return cls.from_dict(kwargs)

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        """Similar to `asdict`, but optionally (and by default) omits fields with their default values for brevity.

        Leaves `MSBEntry` fields as they are -- i.e. this is a 'shallow dict' and not truly serialized like
        `to_json_dict()`.
        """
        default_values = self.get_default_values() if ignore_defaults else {}
        data = {"name": self.name}
        for name in self.get_field_names(visible_only=False):
            value = getattr(self, name)
            if default_values and value == default_values[name]:
                continue  # don't add default values to dictionary
            data[name] = value
        return data

    def to_json_dict(self, msb: MSB, ignore_defaults=True) -> dict[str, tp.Any]:
        """NOTE: This converts types to JSON-ready types. Use `.asdict()` for a straightforward field value mapping."""
        default_values = self.get_default_values() if ignore_defaults else {}
        data = {"name": self.name}
        for name in self.get_field_names(visible_only=False):
            value = getattr(self, name)
            if default_values and value == default_values[name]:
                continue  # don't add default values to dictionary
            if isinstance(value, MSBEntry):
                # Construct a reference dictionary. (There are no real dictionary fields in `MSBEntry` subclasses.)
                subtype_list = msb.get_list_of_entry(value)
                data[name] = {
                    "subtype_list_name": subtype_list.subtype_info.subtype_list_name,
                    "subtype_index": subtype_list.index(value)
                }
            elif isinstance(value, list) and any(isinstance(element, MSBEntry) for element in value):
                # Construct a reference dictionary. (There are no real dictionary fields in `MSBEntry` subclasses.)
                ref_list = []
                ref_subtype_list = None
                for element in value:
                    if element is None:
                        ref_list.append(None)
                    else:
                        if ref_subtype_list is None:
                            ref_subtype_list = msb.get_list_of_entry(element)
                        ref_list.append({
                            "subtype_list_name": ref_subtype_list.subtype_info.subtype_list_name,
                            "subtype_index": ref_subtype_list.index(element)
                        })
            elif isinstance(value, Vector):
                data[name] = list(value)
            elif isinstance(value, set):
                data[name] = sorted(value)
            else:
                data[name] = value
        return data

    @classmethod
    def get_default_values(cls) -> dict[str, tp.Any]:
        defaults = {}
        for f in fields(cls):
            if f.name in {"name", "description"}:
                continue
            if f.default_factory is not MISSING:
                defaults[f.name] = f.default_factory()
            elif f.default is not MISSING:
                defaults[f.name] = f.default
            else:
                raise ValueError(f"Field {f.name} on class {cls.__name__} has no default or factory.")
        return defaults

    def __setattr__(self, key: str, value: tp.Any):
        """Enforces correct type and field presence."""
        if not self.__class__._FIELD_TYPES:
            self._cache_field_types()

        if key in {"name", "description"}:
            if not isinstance(value, str):
                raise ValueError(f"MSB entry {key} must be a string.")
            super(MSBEntry, self).__setattr__(key, value)
            return

        for field_name, field_type in self.__class__._FIELD_TYPES.items():
            # TODO: Clean up/unify all the string parsing happening here. (Fortunately the list of types to handle is
            #  not arbitrarily large.)
            if key == field_name:
                # Correct type can be assigned directly.
                if isinstance(value, property):
                    # No inspection.
                    super(MSBEntry, self).__setattr__(key, value)
                    return
                if type(value).__name__ == field_type:
                    super(MSBEntry, self).__setattr__(key, value)
                    return
                if field_type.startswith("MSB") and field_type in [cls.__name__ for cls in type(value).__mro__]:
                    # Value is a valid subclass.
                    super(MSBEntry, self).__setattr__(key, value)
                    return
                if " | " in field_type:
                    for sub_type in field_type.split(" | "):
                        if type(value).__name__ == sub_type:
                            super(MSBEntry, self).__setattr__(key, value)
                            return
                        if sub_type.startswith("MSB") and sub_type in [cls.__name__ for cls in type(value).__mro__]:
                            # Value is a valid subclass.
                            super(MSBEntry, self).__setattr__(key, value)
                            return
                # `None` is allowed for `MSBEntry` fields or field names starting with an underscore.
                if value is None:
                    if field_type.startswith("MSB") or field_name.startswith("_"):
                        super(MSBEntry, self).__setattr__(key, value)
                        return
                    raise ValueError(
                        f"`None` can only be assigned to `MSBEntry` fields or internal index fields, "
                        f"not `{self.cls_name}.{key}`."
                    )
                # Sequences.
                if field_type.startswith("tuple["):
                    if (expected := field_type.count(",") + 1) != len(value):
                        raise ValueError(f"Wrong size for field `{field_name}`. Expected {expected} elements.")
                    super(MSBEntry, self).__setattr__(key, tuple(value))
                    return
                if field_type.startswith("list["):
                    # TODO: Check binary metadata to enforce length. I am too lazy right now.
                    super(MSBEntry, self).__setattr__(key, list(value))
                    return
                if field_type == "set[int]":
                    super(MSBEntry, self).__setattr__(key, set(value))
                    return
                # Try to convert.
                if field_type in ("Vector2", "Vector3", "Vector4"):
                    if not isinstance(value, (list, tuple)):
                        raise ValueError(
                            f"Can only assign sequences or `{field_type.__name__}` to field `{field_name}`."
                        )
                    vector_type = {"Vector2": Vector2, "Vector3": Vector3, "Vector4": Vector4}[field_type]
                    vector_value = vector_type(*value)
                    super(MSBEntry, self).__setattr__(key, vector_value)
                    return
                raise ValueError(
                    f"Could not set/convert value {repr(value)} for assignment to field `{self.cls_name}.{field_name}`."
                )

        raise ValueError(f"Invalid `MSBEntry` subclass field: `{self.cls_name}.{key}`")

    @classmethod
    def _cache_field_types(cls):
        """NOTE: Using string types from dataclass fields because of circular entry type references."""
        cls._FIELD_TYPES = {}
        for f in fields(cls):
            cls._FIELD_TYPES[f.name] = f.type if isinstance(f.type, str) else f.type.__name__

    def __repr__(self):
        field_strings = []
        for field_name, value in self.to_dict(ignore_defaults=True).items():
            if isinstance(value, MSBEntry):
                field_strings.append(f"    {field_name}=<{value.cls_name}('{value.name}')>,")
            else:
                field_strings.append(f"    {field_name}={repr(value)},")
                if field_name == "translate":
                    print(field_strings[-1])

        return f"{self.cls_name}(\n" + "\n".join(field_strings) + "\n)"

    def __eq__(self, entry: MSBEntry):
        """Checks field equality, but only matches `MSBEntry` references by name."""
        if entry is None:
            return False
        if not isinstance(entry, self.__class__):
            return False
        for f in fields(self):
            value = getattr(self, f.name)
            other = getattr(entry, f.name)
            if isinstance(value, MSBEntry):
                if value.name != other.name:
                    return False
            elif isinstance(value, (list, tuple, set)):
                if any(isinstance(element, MSBEntry) for element in value):
                    # Shallow copied references.
                    for this_e, entry_e in zip(value, other):
                        if this_e is not None:
                            if entry_e is None:
                                return False  # only one is None
                            elif this_e.name != entry_e.name:
                                return False
                        elif entry_e is not None:
                            return False
                else:
                    if value != other:
                        return False
            else:
                if value != other:
                    return False
        return True

    def eq_by_reference_id(self, entry: MSBEntry):
        """Ensures that `MSBEntry` references match by `is` to avoid infinite recursion."""
        if entry is None:
            return False
        if not isinstance(entry, self.__class__):
            raise TypeError("Can only compare equality between MSB entries of the same type.")
        for f in fields(self):
            value = getattr(self, f.name)
            other = getattr(entry, f.name)
            if isinstance(value, MSBEntry):
                if value is not other:
                    return False
            elif isinstance(value, (list, tuple, set)):
                if any(isinstance(element, MSBEntry) for element in value):
                    # Shallow copied references.
                    for this_e, entry_e in zip(value, other):
                        if this_e is not entry_e:
                            return False
                else:
                    if value != other:
                        return False
            else:
                if value != other:
                    return False
        return True

    def _consume_index(self, entry_lists: dict[str, list[MSBEntry]], list_name: str, field_name: str):
        index_field_name = f"_{field_name}_index"
        index = getattr(self, index_field_name)
        try:
            entry = entry_lists[list_name][index] if index != -1 else None
        except IndexError:
            entry = MSBBrokenEntryReference(list_name, index)
        setattr(self, field_name, entry)
        setattr(self, index_field_name, None)

    def _consume_indices(self, entry_lists: dict[str, list[MSBEntry]], list_name: str, field_name: str):
        indices_field_name = f"_{field_name}_indices"
        indices = getattr(self, indices_field_name)
        entry_list = entry_lists[list_name]
        entries = []
        for index in indices:
            if index == -1:
                entry = None
            else:
                try:
                    entry = entry_list[index]
                except IndexError:
                    entry = MSBBrokenEntryReference(list_name, index)
            entries.append(entry)
        setattr(self, field_name, entries)
        setattr(self, indices_field_name, None)

    @staticmethod
    def try_index(entry_list: list, entry: MSBEntry) -> int:
        """Returns -1 if `entry` is not in `entry_list`. Checks ID, not dataclass equality."""
        if entry is None:
            return -1
        for i, e in enumerate(entry_list):
            if e is entry:
                return i
        raise ValueError(f"Could not find referenced entry `{entry.name}` in MSB list while packing.")

    @property
    def cls_name(self) -> str:
        return self.__class__.__name__

    # NOTE: No `_set_index` method needed, as indices for packing can be constructed temporarily.
