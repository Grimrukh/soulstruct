from __future__ import annotations

__all__ = ["MSBEntry"]

import abc
import copy
import logging
import re
import typing as tp
from collections import ChainMap
from dataclasses import dataclass, field, fields, MISSING
from enum import IntEnum
from types import MappingProxyType, ModuleType

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import BaseVector, Vector2, Vector3, Vector4
from soulstruct.utilities.text import pad_chars

from .enums import BaseMSBSubtype, MSBSupertype
from .field_info import MapFieldMetadata, FIELD_INFO
from .utils import MSBBrokenEntryReference, GroupBitSet128, GroupBitSet256

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBEntry"

if tp.TYPE_CHECKING:
    from .core import MSB

_LOGGER = logging.getLogger(__name__)


# Maps valid `MSBEntry` field type annotation strings to their actual types.
# Note that other types may be acceptable, e.g. `int` can be converted to `float`.
# `MSBEntry` references are handled separately.
_BASIC_ENTRY_TYPES = {
    "bool": bool,
    "int": int,
    "float": float,
    # No `bytes` fields in entries.
    "str": str,
    "list[int]": list,
    "list[float]": list,
    # No `tuple` fields in entries (makes element assignment too annoying).
    "GroupBitSet128": GroupBitSet128,
    "GroupBitSet256": GroupBitSet256,
    "Vector2": Vector2,
    "Vector3": Vector3,
    "Vector4": Vector4,
}


@dataclass(slots=True, eq=False, repr=False)
class MSBEntry(abc.ABC):
    """Base class for entries of any type and subtype that appear in an `MSB` (under one of four entry superlists)."""

    # Shared between all game MSB entries. TODO: Infer from `reader.long_varints`?
    NAME_ENCODING: tp.ClassVar[str]
    # Required to look up default field info (and just of general relevance). Defined in the four base classes.
    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype]
    # Generally only used to check against unpacked indices (which should have already been 'peeked' by the MSB).
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBSubtype]
    # These fields will be marked as hidden in the GUI.
    HIDE_FIELDS: tp.ClassVar[tuple[str, ...]] = ()
    # Number of bits in draw/display/navmesh/backread groups (e.g. 128 or 256).
    GROUP_BIT_COUNT: tp.ClassVar[int]
    # Cached when first accessed. Maps field names to their default values. Immutable.
    _FIELD_DEFAULTS: tp.ClassVar[MappingProxyType[str, tp.Any]] = None
    # Cached when first accessed. Maps field names to types for enforcement, or type names for `MSBEntry` subclasses.
    _FIELD_TYPES: tp.ClassVar[MappingProxyType[str, str | tp.Type[tp.Any]]] = None
    # Cached when first accessed. Maps field names to `(nickname, tooltip, display_type)` tuples.
    _FIELD_DISPLAY_INFO: tp.ClassVar[MappingProxyType[str, tuple[str, str, tp.Type[tp.Any]]]] = None
    # Cached when first accessed. Maps field names to functions that convert JSON string values to that field's type.
    _CUSTOM_JSON_DECODERS: tp.ClassVar[MappingProxyType[str, tp.Callable[[str], tp.Any]]] = None

    # Prevents `__setattr__` type checks when creating instances from binary `MSB` (for efficiency). Can also be enabled
    # and disabled by the user at will.
    SETATTR_CHECKS_DISABLED: tp.ClassVar[bool] = False

    # Structs for header, supertype data, and (optional but common) subtype data.
    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[tp.Type[BinaryStruct]]
    SUPERTYPE_DATA_STRUCT: tp.ClassVar[tp.Type[BinaryStruct]]
    SUBTYPE_DATA_STRUCT: tp.ClassVar[tp.Type[BinaryStruct]]

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

        cls.SETATTR_CHECKS_DISABLED = True  # will be re-enabled in `__post_init__`
        msb_entry = cls(**kwargs)
        cls.SETATTR_CHECKS_DISABLED = False
        return msb_entry

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
        try:
            self.pack_header(writer, entry_offset, supertype_index, subtype_index, entry_lists)
        except Exception:
            print(self.to_dict(ignore_defaults=False))
            raise
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

    def set(self, **kwargs):
        """Attribute shortcut setter."""
        for key, value in kwargs.items():
            self[key] = value

    def get_entity_id(self) -> int | None:
        """`entity_id` is a critical field for most MSB entries, but not quite all of them (and not models).

        This method simply returns the `entity_id` field if it exists, or raises a TypeError otherwise.
        """
        try:
            return getattr(self, "entity_id")
        except AttributeError:
            raise TypeError(f"MSB entry subtype `{self.__class__.__name__}` does not have the `entity_id` field.")

    def set_entity_id(self, value: int):
        """`entity_id` is a critical field for most MSB entries, but not quite all of them (and not models).

        This method simply sets the `entity_id` field to `value` if it exists, or raises a TypeError otherwise.
        """
        if "entity_id" not in self.get_field_names():
            raise TypeError(f"MSB entry subtype `{self.__class__.__name__}` does not have the `entity_id` field.")
        setattr(self, "entity_id", value)

    @property
    def entity_enum(self):
        raise AttributeError(
            "You can set `MSBEntry.entity_enum` as a shortcut to set both `name` and `entity_id`, but cannot access it."
        )

    @entity_enum.setter
    def entity_enum(self, value: IntEnum):
        """Set both entry `name` and `entity_id` (if valid) for this entry."""
        if "entity_id" not in self.get_field_names():
            raise TypeError(f"MSB entry subtype `{self.__class__.__name__}` does not have the `entity_id` field.")
        self.name = value.name
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

    @classmethod
    def get_field_names(cls, visible_only=False) -> tuple[str]:
        return tuple(
            f.name for f in fields(cls)
            if f.name not in {"name", "description"}
            and not f.name.startswith("_")
            and (not visible_only or f.name not in cls.HIDE_FIELDS)
        )

    @classmethod
    def get_custom_json_decoders(cls) -> MappingProxyType[str, tp.Callable[[str], tp.Any]]:
        """Get a dictionary mapping field names to string-parsing decoders for JSON."""
        if cls._CUSTOM_JSON_DECODERS is None:
            decoders = {}
            for f in fields(cls):
                if f.type in (GroupBitSet128, GroupBitSet128.__name__):
                    decoders[f.name] = GroupBitSet128.from_repr
                elif f.type in (GroupBitSet256, GroupBitSet256.__name__):
                    decoders[f.name] = GroupBitSet256.from_repr
                else:
                    for check_type in (Vector2, Vector3, Vector4):
                        if f.type in (check_type, check_type.__name__):
                            decoders[f.name] = check_type
            cls._CUSTOM_JSON_DECODERS = MappingProxyType(decoders)

        return cls._CUSTOM_JSON_DECODERS

    def set_entity_enum(self, entity_enum: IntEnum):
        """Only works for subclasses with `entity_id` field.

        Getaround for some kind of mix-in, as `entity_id` is so common but not strictly hierarchical.
        """
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
        cls.SETATTR_CHECKS_DISABLED = True
        msb_entry = cls(**data)
        cls.SETATTR_CHECKS_DISABLED = False
        return msb_entry

    @classmethod
    def from_json_dict(cls, data: dict[str, tp.Any]) -> tuple[Self, dict[str, dict]]:
        """Defers conversion of reference dictionaries to entries: returns both the incomplete `MSBEntry` and a
        dictionary mapping field names to reference dicts."""
        try:
            kwargs = {"name": data["name"]}
        except KeyError:
            raise ValueError("`MSBEntry` JSON dict must have 'name' field.")
        deferred_refs = {}
        decoders = cls.get_custom_json_decoders()
        for field_name, field_value in data.items():
            if field_name in decoders:
                kwargs[field_name] = decoders[field_name](field_value)
            elif isinstance(field_value, dict):
                if (
                    "subtype_list_name" not in field_value or "subtype_index" not in field_value
                    or len(field_value) != 2
                ):
                    raise ValueError(
                        "`MSBEntry` JSON `dict` fields must be references to other entries with exact keys:\n"
                        "    'subtype_list_name', 'subtype_index'"
                    )
                deferred_refs[field_name] = field_value
            elif isinstance(field_value, list) and any(isinstance(element, dict) for element in field_value):
                deferred_list = []
                for element in field_value:
                    if element is None:
                        deferred_list.append(None)
                        continue
                    if (
                        "subtype_list_name" not in element or "subtype_index" not in element
                        or len(element) != 2
                    ):
                        raise ValueError(
                            "`MSBEntry` JSON `list[dict]` fields must be references to other entries with exact keys:\n"
                            "    'subtype_list_name', 'subtype_index'"
                        )
                    deferred_list.append(element)
                deferred_refs[field_name] = deferred_list
            else:
                # `__setattr__` enforcer should be able to convert all JSON values to their proper types.
                kwargs[field_name] = field_value

        cls.SETATTR_CHECKS_DISABLED = True
        msb_entry = cls(**kwargs)
        cls.SETATTR_CHECKS_DISABLED = False
        return msb_entry, deferred_refs

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        """Similar to `asdict`, but optionally (and by default) omits fields with their default values for brevity.

        Leaves `MSBEntry` fields as they are -- i.e. this is a 'shallow dict' and not truly serialized like
        `to_json_dict()`.
        """
        default_values = self.get_default_values() if ignore_defaults else {}
        data = {"name": self.name, "description": self.description}
        for name in self.get_field_names(visible_only=False):
            value = getattr(self, name)
            if default_values and value == default_values[name]:
                continue  # don't add default values to dictionary
            data[name] = value
        return data

    def to_json_dict(self, msb: MSB, ignore_defaults=True) -> dict[str, tp.Any]:
        """NOTE: This converts types to JSON-ready types. Use `.asdict()` for a straightforward field value mapping."""
        default_values = self.get_default_values() if ignore_defaults else {}
        data = {"name": self.name, "description": self.description}
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
                data[name] = ref_list
            elif isinstance(value, BaseVector):
                data[name] = list(value)
            else:
                # Custom types like `Vector3` and `GroupBitSet` can decode their own string `repr`.
                data[name] = value
        return data

    @classmethod
    def get_default_values(cls) -> MappingProxyType[str, tp.Any]:
        if cls._FIELD_DEFAULTS is not None:
            return cls._FIELD_DEFAULTS  # NOTE: immutable mapping

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

        cls._FIELD_DEFAULTS = MappingProxyType(defaults)
        return cls._FIELD_DEFAULTS

    def __setattr__(self, key: str, value: tp.Any):
        """Enforces correct type and field presence.

        This is slow and is deactivated when reading binary MSBs.
        """
        if self.__class__.SETATTR_CHECKS_DISABLED:
            # Bypass validation.
            super(MSBEntry, self).__setattr__(key, value)
            return

        field_types = self.get_field_types()

        if key in {"name", "description"}:
            if not isinstance(value, str):
                raise ValueError(f"MSB entry `{key}` must be a string.")
            super(MSBEntry, self).__setattr__(key, value)
            return

        if key == "entity_enum":
            if not isinstance(value, IntEnum):
                raise ValueError(f"MSB entry `{key}` must be an Entity.")
            super(MSBEntry, self).__setattr__(key, value)
            return

        for field_name, field_type in field_types.items():
            if key == field_name:

                if isinstance(value, property):
                    # No inspection.
                    super(MSBEntry, self).__setattr__(field_name, value)
                    return

                if (
                    field_name.startswith("_")
                    and (field_name.endswith("_index") or field_name.endswith("_indices"))
                    and value is None
                ):
                    # `None` can be assigned to internal index fields.
                    super(MSBEntry, self).__setattr__(field_name, value)
                    return

                entry_type_name, length_str = re.match(r"([\w |]+)(\[\d+])?", field_type).groups()

                if length_str is not None:
                    # List of entry subclasses or integers.
                    length = int(length_str[1:-1])  # remove brackets
                    if not isinstance(value, (list, tuple)):
                        raise TypeError(
                            f"Must assign a list/tuple to list field `{self.cls_name}.{field_name}`."
                        )
                    if entry_type_name == "int":
                        if len(value) != length:
                            raise ValueError(
                                f"Int list field `{self.cls_name}.{field_name}` must have exactly {length} elements."
                            )
                        for element in value:
                            if not isinstance(element, int):
                                raise TypeError(
                                    f"Int list field `{self.cls_name}.{field_name}` contains non-int: {value}"
                                )
                        list_value = list(value)
                    elif entry_type_name == "float":
                        if len(value) != length:
                            raise ValueError(
                                f"Float list field `{self.cls_name}.{field_name}` must have exactly {length} elements."
                            )
                        floats = []
                        for element in value:
                            if isinstance(element, int):
                                element = float(element)
                            elif not isinstance(element, float):
                                raise TypeError(
                                    f"Float list field `{self.cls_name}.{field_name}` contains non-number: {value}"
                                )
                            floats.append(element)
                        list_value = floats
                    elif entry_type_name.startswith("MSB"):  # MSBEntry
                        if len(value) > length:
                            raise ValueError(
                                f"Maximum size of entry list field `{self.cls_name}.{field_name}` is {length}."
                            )
                        list_value = []
                        for element in value:
                            if element is None:
                                list_value.append(None)
                            elif self._is_subtype(element, entry_type_name):
                                list_value.append(element)
                            else:
                                raise TypeError(
                                    f"Invalid type for entry list field `{self.cls_name}.{field_name}`: "
                                    f"{element.__class__.__name__}"
                                )
                        while len(list_value) < length:
                            list_value.append(None)
                    else:
                        raise TypeError(f"Invalid field type for `{self.cls_name}.{field_name}`: {field_type}")
                    super(MSBEntry, self).__setattr__(field_name, list_value)
                    return

                if entry_type_name.startswith("MSB"):
                    # Single entry (or None).
                    if value is not None and not self._is_subtype(value, entry_type_name):
                        if not self._is_permitted_wrong_msb_entry_type(value):
                            raise TypeError(
                                f"Invalid type for entry field `{self.cls_name}.{field_name}` of '{self.name}': "
                                f"{value.__class__.__name__} ({value})"
                            )
                    super(MSBEntry, self).__setattr__(field_name, value)
                    return

                if field_type in {"GroupBitSet128", "GroupBitSet256"}:
                    # `GroupBitSet` subclass of some maximum count.
                    if not isinstance(value, (GroupBitSet128, GroupBitSet256)):
                        value = (GroupBitSet128 if field_type.endswith("128") else GroupBitSet256)(set(value))
                    super(MSBEntry, self).__setattr__(field_name, value)
                    return

                # Type is exactly correct.
                if type(value).__name__ == field_type:
                    super(MSBEntry, self).__setattr__(key, value)
                    return

                # Try to convert to basic type.
                if field_type in {"Vector2", "Vector3", "Vector4"}:
                    vector_type = {"Vector2": Vector2, "Vector3": Vector3, "Vector4": Vector4}[field_type]
                    try:
                        vector_value = vector_type(value)
                    except (ValueError, TypeError):
                        raise ValueError(
                            f"Can only assign sequences or `{field_type}` to `{field_type}` "
                            f"field `{self.cls_name}.{field_name}`, not: {value}"
                        )
                    super(MSBEntry, self).__setattr__(key, vector_value)
                    return

                if field_type in {"bool", "int", "float", "str"}:
                    py_type = _BASIC_ENTRY_TYPES.get(field_type)
                    if isinstance(value, int) and py_type is float:
                        value = float(value)  # acceptable conversion
                    elif not isinstance(value, py_type):
                        raise TypeError(f"Invalid type for `{field_type}` field `{self.cls_name}.{field_name}: {value}")
                    super(MSBEntry, self).__setattr__(key, value)
                    return

                # Shouldn't be able to reach this, but just in case.
                raise ValueError(
                    f"Could not set/convert value {repr(value)} for assignment to field "
                    f"`{self.cls_name}.{field_name}` (type `{field_type}`)."
                )

        raise ValueError(f"Invalid `MSBEntry` subclass field: `{self.cls_name}.{key}`")

    @classmethod
    def _is_subtype(cls, value: MSBEntry, parent_type_name: str) -> bool:
        """Checks if `parent_type_name` is a parent of `value` type."""
        if "|" in parent_type_name:
            # Recur on union members.
            return any(cls._is_subtype(value, parent.strip()) for parent in parent_type_name.split("|"))
        else:
            return parent_type_name in [parent.__name__ for parent in value.__class__.__mro__]

    def _is_permitted_wrong_msb_entry_type(self, value: MSBEntry) -> bool:
        """Checks for a handful of permitted exceptions for incorrect `MSBEntry` field references."""

        # Special exceptions (with warnings) for unused character/object models, which have been known
        # to reference the wrong model type in Undead Burg in DSR (thanks QLOC?).
        if self.cls_name == "MSBUnusedCharacter" and value.__class__.__name__ == "MSBObjectModel":
            # TODO: Could do a hash check for vanilla DSR file to skip m10_01 warning. But that seems REALLY try-hard.
            # _LOGGER.warning(
            #     f"`MSBUnusedCharacter` '{self.name}' uses an `MSBObjectModel`: '{value.name}'.\n"
            #     f"    This happens, e.g., in m10_01_00_00 in vanilla DSR (unused bonfire 'o0200_0004')."
            # )
            return True
        return False

    @classmethod
    def get_field_display_info(cls, field_name: str, game_types_module: ModuleType) -> tuple[str, str, tp.Type[tp.Any]]:
        if cls._FIELD_DISPLAY_INFO is not None:
            try:
                return cls._FIELD_DISPLAY_INFO[field_name]
            except KeyError:
                raise KeyError(f"Invalid MSB entry field (no metadata): `{cls.__name__}.{field_name}`")

        # Create and cache all fields' metadata.
        field_types = cls.get_field_types()
        field_metadata = {}  # type: dict[str, tuple[str, str, tp.Type[tp.Any]]]
        for f in fields(cls):
            if f.name in {"name", "description"}:
                # Dummy metadata (not treated as regular fields for display).
                field_metadata[f.name] = (f.name.capitalize(), f.name.capitalize(), str)
                continue

            if f.name.startswith("_"):
                continue  # ignore (not a displayed field)

            metadata = f.metadata.get("msb", None)  # type: MapFieldMetadata
            if metadata is not None:
                nickname = metadata.nickname
                tooltip = metadata.tooltip
                display_type = metadata.game_type
            else:
                nickname = ""
                tooltip = ""
                display_type = None

            if not nickname or not tooltip:
                # Try to get default name and/or tooltip.
                subtype_name = cls.SUBTYPE_ENUM.name.replace("Unused", "")  # redirect 'Unused' subtypes
                keys = (f"{subtype_name}[{f.name}]", f"{cls.SUPERTYPE_ENUM.name}[{f.name}]")
                for key in keys:
                    if key in FIELD_INFO:
                        default_nickname, default_tooltip = FIELD_INFO[key]
                        if not nickname:
                            nickname = default_nickname
                        if not tooltip:
                            tooltip = default_tooltip
                        break
                else:
                    _LOGGER.warning(
                        f"No default nickname/tooltip metadata for field `{cls.__name__}.{f.name}`. Keys: {keys}"
                    )
                    nickname = f.name.capitalize()
                    tooltip = "TODO-TOOLTIP"

            if display_type is None:
                # Parse field type string.
                field_type_str = field_types[f.name]
                if re.match(r".*\[.*", field_type_str):
                    display_type = list
                elif field_type_str.startswith("MSBCharacterModel | MSBPlayerModel"):
                    # Annoying case: c0000 characters can use either character or player c0000 model.
                    display_type = getattr(game_types_module, "CharacterModel")
                elif match := re.match(r"MSB(.*Model)", field_type_str):
                    display_type = getattr(game_types_module, match.group(1))
                else:
                    # TODO: Move basic map game types to `base` submodule so `game_types_module` isn't needed here?
                    match field_type_str:
                        case "int":
                            display_type = int
                        case "float":
                            display_type = float
                        case "bool":
                            display_type = bool
                        case "str":
                            display_type = str
                        case "GroupBitSet128":
                            display_type = GroupBitSet128
                        case "GroupBitSet256":
                            display_type = GroupBitSet256
                        case "Vector2":
                            display_type = Vector2
                        case "Vector3":
                            display_type = Vector3
                        case "Vector4":
                            display_type = Vector4
                        case "MSBPart":
                            display_type = getattr(game_types_module, "MapPart")
                        case "MSBRegion":
                            display_type = getattr(game_types_module, "Region")
                        case "MSBEnvironmentEvent":
                            display_type = getattr(game_types_module, "EnvironmentEvent")
                        case "MSBCollision":
                            display_type = getattr(game_types_module, "Collision")
                        case _:
                            raise TypeError(
                                f"Cannot get display type of MSB entry field `{f.name}` type: {field_type_str}"
                            )

            field_metadata[f.name] = (nickname, tooltip, display_type)

        cls._FIELD_DISPLAY_INFO = MappingProxyType(field_metadata)
        try:
            return cls._FIELD_DISPLAY_INFO[field_name]
        except KeyError:
            raise KeyError(f"Invalid MSB entry field (no metadata): `{cls.__name__}.{field_name}`")

    @classmethod
    def all_annotations(cls) -> ChainMap:
        """Returns a dictionary-like ChainMap that includes annotations for all
           attributes defined in cls or inherited from superclasses."""
        return ChainMap(*(c.__annotations__ for c in cls.__mro__ if '__annotations__' in c.__dict__))

    @classmethod
    def get_field_types(cls):
        """NOTE: Using string types from dataclass field annotations due to circular entry type references."""
        if cls._FIELD_TYPES is not None:
            return cls._FIELD_TYPES

        f_annotations = cls.all_annotations()

        field_types = {}
        for f in fields(cls):
            ann = f_annotations[f.name]
            if not isinstance(ann, str):
                ann = ann.__name__

            # Check `MSBEntry` types first.
            if re.match(r"MSBEntry", ann):  # not allowed
                raise TypeError(f"Field {cls.__name__}.{f.name} cannot have abstract `MSBEntry` type.")
            elif re.match(r"MSB.*", ann):
                # `MSBEntry` subclass. `__setattr__` will confirm that any set `value` has this name in its MRO.
                # NOTE: Will match pipe unions and check them appropriately.
                field_types[f.name] = ann  # str
            elif ann in {"list[int]", "list[float]"} or re.match(r"list\[MSB[\w, ]*]", ann):
                # List of `MSBEntry` subclasses. Check binary metadata for length and store in type string.
                try:
                    binary = f.metadata["binary"]  # type: BinaryMetadata
                    if isinstance(binary, BinaryArrayMetadata):
                        if binary.length is None:
                            raise KeyError
                        length = binary.length
                    else:
                        raise TypeError(
                            f"Array MSB entry field `{cls.__name__}{f.name}` must have `BinaryArray` metadata."
                        )
                except KeyError:
                    if f.default_factory != MISSING:
                        # Detect length from default value.
                        length = len(f.default_factory())
                    else:
                        raise TypeError(
                            f"MSB entry type `{cls.__name__}` needs `Binary(length)` metadata for field `{f.name}`."
                        )
                field_types[f.name] = f"{ann[5:-1]}[{length}]"
            elif ann in _BASIC_ENTRY_TYPES:
                field_types[f.name] = ann
            else:
                raise TypeError(f"Could not parse field type annotation '{ann}' for `{cls.__name__}.{f.name}`.")

        cls._FIELD_TYPES = MappingProxyType(field_types)
        return cls._FIELD_TYPES

    def __repr__(self):
        field_strings = []
        for field_name, value in self.to_dict(ignore_defaults=True).items():
            if isinstance(value, MSBEntry):
                field_strings.append(f"    {field_name}=<{value.cls_name}('{value.name}')>,")
            else:
                field_strings.append(f"    {field_name}={repr(value)},")
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

    def try_index(
        self,
        entry_list: list,
        source_field_name: str,
    ) -> int | list[int]:
        """Find index of single entry or indices of all entries in list.

        Returns -1 (or puts -1 in list) if an entry is `None`. Searches by `is` (ID), NOT dataclass equality.
        Raises a `ValueError` if an entry cannot be found in the list.

        Note that unlike `MSBEntryList.index(entry)`, non-null entries MUST be present here.
        """
        entry_or_entry_list = getattr(self, source_field_name)  # type: MSBEntry | list[MSBEntry | None]
        if entry_or_entry_list is None:
            return -1  # non-set single entry
        if isinstance(entry_or_entry_list, list):
            indices = []
            for entry in entry_or_entry_list:
                if entry is None:
                    indices.append(-1)
                else:
                    for i, e in enumerate(entry_list):
                        if e is entry:
                            indices.append(i)
                            break
                    else:
                        raise ValueError(
                            f"Could not find referenced entry `{entry.name}` for "
                            f"`{self.name}.{source_field_name}` in MSB list while packing."
                        )
            return indices
        # Otherwise, single entry.
        for i, e in enumerate(entry_list):
            if e is entry_or_entry_list:
                return i
        raise ValueError(
            f"Could not find referenced entry `{entry_or_entry_list.name}` for "
            f"`{self.name}.{source_field_name}` in MSB list while packing."
        )

    @property
    def cls_name(self) -> str:
        return self.__class__.__name__

    # NOTE: No `_set_index` method needed, as indices for packing can be constructed temporarily.
