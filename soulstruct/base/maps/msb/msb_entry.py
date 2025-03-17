from __future__ import annotations

__all__ = [
    "MSBEntry",
    "MSBEntryReference",
    "EntryRef",
    "MSBBinaryStruct",
    "MSBHeaderStruct",
    "MSBFieldDisplayInfo",
    "IDList",  # for convenience
]

import abc
import contextlib
import copy
import logging
import re
import typing as tp
from collections import ChainMap
from dataclasses import dataclass, field, fields, Field, MISSING
from enum import IntEnum
from types import MappingProxyType, ModuleType

from constrata.metadata import *
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import BaseVector, Vector2, Vector3, Vector4
from soulstruct.utilities.misc import IDList
from soulstruct.utilities.text import pad_chars

from .enums import BaseMSBSubtype, MSBSupertype
from .field_info import MapFieldMetadata, FIELD_INFO
from .utils import MSBBrokenEntryReference, BitSet128, BitSet256, BitSet1024
from .region_shapes import RegionShape, RegionShapeType, SHAPE_TYPE_CLASSES

if tp.TYPE_CHECKING:
    from .core import MSB

_LOGGER = logging.getLogger("soulstruct")


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
    "BitSet128": BitSet128,
    "BitSet256": BitSet256,
    "BitSet1024": BitSet1024,
    "Vector2": Vector2,
    "Vector3": Vector3,
    "Vector4": Vector4,
    # "BaseShape": BaseShape,  # TODO: move to base module
}


class MSBFieldDisplayInfo(tp.NamedTuple):
    nickname: str
    tooltip: str
    display_type: type[tp.Any]


class MSBEntryReference(tp.NamedTuple):
    referrer: MSBEntry
    field_name: str
    array_index: int | None = None


def EntryRef(list_name: str, field_name="", array_size: int = None) -> dict[str, tp.Any]:
    """Dataclass field metadata generator indicating a reference that should be resolved with `MSBEntry.try_index`.

    If `field_name` is empty, it will be detected by just removing '_index' suffix from the field name.
    """
    metadata = BinaryArray(array_size) if array_size is not None else {"metadata": {}}
    metadata["metadata"]["msb_ref"] = (list_name, field_name)
    return metadata


class MSBBinaryStruct(BinaryStruct, abc.ABC):
    """Allows more `MSBEntry` arguments for unpacking/packing."""

    _MSB_REF_FIELDS: tp.ClassVar[dict[str, tuple[str, ...]]] = None

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBEntry],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        """Default assumes 1:1 field name mapping."""
        return cls.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

    @classmethod
    def kwargs_to_msb_writer(
        cls,
        entry: MSBEntry,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: dict[str, IDList[MSBEntry]],
        **kwargs,
    ):
        """Default assumes 1:1 field name mapping, aside from resolving MSB references."""
        cls.preprocess_write_kwargs(entry, entry_lists, kwargs)
        cls.object_to_writer(entry, writer, **kwargs)
        cls.post_write(entry, writer, entry_offset, entry_lists)

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBEntry,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        cls._resolve_msb_ref_fields()
        for fld_name, (entry_list_name, field_name) in cls._MSB_REF_FIELDS.items():
            kwargs[fld_name] = entry.try_index(entry_lists[entry_list_name], field_name)

    @classmethod
    def _resolve_msb_ref_fields(cls):
        if cls._MSB_REF_FIELDS is None:
            cls._MSB_REF_FIELDS = {}
            for fld in cls.get_binary_fields():
                if "msb_ref" in fld.metadata:
                    msb_ref = list(fld.metadata["msb_ref"])
                    if msb_ref[1] == "":
                        # Auto-resolve now (once, permanently).
                        msb_ref[1] = fld.name.removesuffix("_index").removesuffix("_indices").lstrip("_")
                    cls._MSB_REF_FIELDS[fld.name] = tuple(msb_ref)

    @classmethod
    def post_write(
        cls,
        entry: MSBEntry,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: dict[str, IDList[MSBEntry]],
    ):
        pass


class MSBHeaderStruct(MSBBinaryStruct, abc.ABC):
    """Supports basic headers and allows easy extension. Must be inherited to define actual field order."""

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBEntry],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        """Supports most known headers, as a base call at least."""
        kwargs = cls.from_bytes(reader).to_dict(ignore_underscore_prefix=False)  # 'private' fields handled manually

        # Neither of these is needed, if present.
        kwargs.pop("supertype_index", None)
        kwargs.pop("subtype_index", None)

        # Validate and discard (ALMOST always present).
        subtype_int = kwargs.pop("_subtype_int", entry_type.SUBTYPE_ENUM.value)
        if subtype_int != entry_type.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB subtype index for `{cls.__name__}`: {subtype_int}")

        name = reader.unpack_string(offset=entry_offset + kwargs.pop("name_offset"), encoding=entry_type.NAME_ENCODING)
        kwargs["name"] = name

        return kwargs

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBEntry,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        super(MSBHeaderStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)
        for struct_name, struct_type in entry.STRUCTS.items():
            kwargs[f"{struct_name}_offset"] = RESERVED if struct_type is not None else 0
        kwargs["name_offset"] = RESERVED
        kwargs["_subtype_int"] = entry.SUBTYPE_ENUM.value

    @classmethod
    def post_write(
        cls,
        entry: MSBEntry,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: [dict[str, IDList[MSBEntry]]],  # may be required by subclasses
    ):
        # Name is always packed first.
        writer.fill("name_offset", writer.position - entry_offset, obj=entry)
        writer.append(pad_chars(entry.name, encoding=entry.NAME_ENCODING, alignment=4))


@dataclass(slots=True, eq=False, repr=False)
class MSBEntry(abc.ABC):
    """Base class for entries of any type and subtype that appear in an `MSB` (under one of four entry superlists)."""

    # Shared between all game MSB entries. TODO: Infer from `reader.long_varints`?
    NAME_ENCODING: tp.ClassVar[str]
    # Required to look up default field info (and just of general relevance). Defined in classes like `BaseMSBPart`.
    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype]
    # Generally only used to check against unpacked indices (which should have already been 'peeked' by the MSB).
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBSubtype]
    # These fields will be marked as hidden in the GUI.
    HIDE_FIELDS: tp.ClassVar[tuple[str, ...]] = ()
    # Names of fields that reference other MSB entries.
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = []
    # Cached when first accessed. Maps field names to their default values. Immutable.
    _FIELD_DEFAULTS: tp.ClassVar[MappingProxyType[str, tp.Any]] = None
    # Cached when first accessed. Maps field names to types for enforcement, or type names for `MSBEntry` subclasses.
    _FIELD_TYPES: tp.ClassVar[MappingProxyType[str, str | type[tp.Any]]] = None
    # Cached when first accessed. Maps field names to `MSBFieldDisplayInfo` triplets of nickname, tooltip, display type.
    _FIELD_DISPLAY_INFO: tp.ClassVar[MappingProxyType[str, MSBFieldDisplayInfo]] = None
    # Cached when first accessed. Maps field names to functions that convert JSON string values to that field's type.
    _CUSTOM_JSON_DECODERS: tp.ClassVar[MappingProxyType[str, tp.Callable[[str], tp.Any]]] = None

    _FIELD_REGEX = {
        "msb_ref": re.compile(r"^(MSB[A-Za-z0-9]+)$"),
        "list": re.compile(r"list\[([\w |]+)\]"),
    }

    # Prevents `__setattr__` type checks when creating instances from binary `MSB` (for efficiency). Can also be enabled
    # and disabled by the user at will, which is best done temporarily via `with MSBEntry.setattr_checks_disabled():`.
    SETATTR_CHECKS_DISABLED: tp.ClassVar[bool] = False

    # Header struct containing basic information and offsets to other structs.
    HEADER_STRUCT: tp.ClassVar[type[MSBHeaderStruct]]
    # Dictionary of structs with offsets in `HEADER_STRUCT`, in the order their data should be packed back into MSB.
    # `None` indicates that a header offset should exist for that struct, but it should be zero.
    STRUCTS: tp.ClassVar[dict[str, type[MSBBinaryStruct] | None]]

    # Basic data fields.
    name: str
    description: str = field(default="", kw_only=True)  # not actually present in all games, but here as an option

    # Internal field that tracks other entries/fields/array indices that refer to this one (when indices are consumed)
    # so that those references can be maintained if this entry is, say, replaced by a new one.
    __referring_entry_fields: list[MSBEntryReference] = field(init=False, default_factory=list)

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        """Default minimal method. Most subclasses can just override one of the header/data unpack methods."""
        kwargs = cls.reader_to_entry_kwargs(reader, entry_offset=reader.position)

        with cls.setattr_checks_disabled():
            return cls(**kwargs)

    @classmethod
    def reader_to_entry_kwargs(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        """Allows for easier inheritance with the `setattr` disabling."""
        kwargs = cls.HEADER_STRUCT.reader_to_entry_kwargs(reader, cls, entry_offset)

        for struct_name, struct_type in cls.STRUCTS.items():
            try:
                struct_offset = entry_offset + kwargs.pop(f"{struct_name}_offset")
            except KeyError:
                raise ValueError(f"Struct offset not found for `{struct_name}` in `{cls.__name__}`.")
            if struct_type is None:
                if struct_offset != 0:
                    raise ValueError(f"Offset for unused struct `{struct_name}` in `{cls.__name__}` is non-zero.")
                continue
            if struct_offset == 0:
                # `STRUCTS` class attribute enforces which structs must be present in subtype.
                raise ValueError(f"Offset for used struct `{struct_name}` in `{cls.__name__}` is 0.")
            reader.seek(struct_offset)
            kwargs |= struct_type.reader_to_entry_kwargs(reader, cls, entry_offset)

        return kwargs

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, IDList[MSBEntry]]
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        entry_offset = writer.position
        self.HEADER_STRUCT.kwargs_to_msb_writer(
            self,
            writer,
            entry_offset,
            entry_lists,
            supertype_index=supertype_index,
            subtype_index=subtype_index,
        )

        for struct_name, struct_type in self.STRUCTS.items():
            if struct_type is None:
                continue  # not reserved in header
            struct_offset = writer.position - entry_offset
            writer.fill(f"{struct_name}_offset", struct_offset, obj=self)
            struct_type.kwargs_to_msb_writer(self, writer, entry_offset, entry_lists)

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
            setattr(self, field_name, value)  # will go through validation
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
        setattr(self, "entity_id", value.value)  # attribute validated (`object.__setattr__` not used)

    def copy(self):
        """Copy entry with only shallow copies of fields referencing other `MSBEntry`s."""
        copied_dict = {}
        for f in self.get_entry_fields():
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
    def get_field_names(cls, visible_only=False) -> tuple[str, ...]:
        return tuple(
            f.name for f in cls.get_entry_fields()
            if f.name not in {"name", "description"}
            and not f.name.startswith("_")
            and (not visible_only or f.name not in cls.HIDE_FIELDS)
        )

    @classmethod
    def get_custom_json_decoders(cls) -> MappingProxyType[str, tp.Callable[[str], tp.Any]]:
        """Get a dictionary mapping field names to string-parsing decoders for JSON."""
        if cls._CUSTOM_JSON_DECODERS is None:
            decoders = {}
            for f in cls.get_entry_fields():
                if f.type in (BitSet128, BitSet128.__name__):
                    decoders[f.name] = BitSet128.from_repr
                elif f.type in (BitSet256, BitSet256.__name__):
                    decoders[f.name] = BitSet256.from_repr
                elif f.type in (BitSet1024, BitSet1024.__name__):
                    decoders[f.name] = BitSet1024.from_repr
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
            object.__setattr__(self, "entity_id", entity_enum.value)
            self.name = entity_enum.name
        else:
            raise TypeError(f"MSB entry class `{self.__class__.__name__}` has no `entity_id` field.")

    @classmethod
    def from_dict(cls, data: dict[str, tp.Any]) -> tp.Self:
        """Standard dictionary loader."""
        with cls.setattr_checks_disabled():
            return cls(**data)

    @classmethod
    def from_json_dict(cls, data: dict[str, tp.Any]) -> tuple[tp.Self, dict[str, dict]]:
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
                if "shape_type" in field_value:
                    # Load as shape.
                    shape_type = RegionShapeType[field_value["shape_type"]]
                    shape_class = SHAPE_TYPE_CLASSES[shape_type]
                    kwargs[field_name] = shape_class.from_json_dict(field_value)
                    continue

                # Validate MSB entry reference dictionary.
                if not cls.is_valid_ref_dict(field_value):
                    raise ValueError(
                        "`MSBEntry` JSON `dict` fields must be references to other entries with key "
                        "'subtype_list_name' and exactly one of 'subtype_index' or 'entry_name'."
                    )
                deferred_refs[field_name] = field_value
            elif isinstance(field_value, list) and any(isinstance(element, dict) for element in field_value):
                deferred_list = []
                for element in field_value:
                    if element is None:
                        deferred_list.append(None)
                        continue
                    if not cls.is_valid_ref_dict(element):
                        raise ValueError(
                            "`MSBEntry` JSON `list[dict]` fields must be references to other entries with key "
                            "'subtype_list_name' and exactly one of 'subtype_index' or 'entry_name'."
                        )
                    deferred_list.append(element)
                deferred_refs[field_name] = deferred_list
            else:
                # `__setattr__` enforcer should be able to convert all JSON values to their proper types.
                kwargs[field_name] = field_value

        with cls.setattr_checks_disabled():
            return cls(**kwargs), deferred_refs

    @staticmethod
    def is_valid_ref_dict(ref_dict: dict[str, tp.Any]) -> bool:
        """JSON MSB entry reference can be by index or name."""
        return (
            len(ref_dict) == 2
            and ("subtype_list_name" in ref_dict or "subtype" in ref_dict)  # legacy support for 'subtype_list_name'
            and ("subtype_index" in ref_dict or "entry_name" in ref_dict)
        )

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        """Similar to `asdict`, but optionally (and by default) omits fields with their default values for brevity.

        Leaves `MSBEntry` fields as they are -- i.e. this is a 'shallow dict' and not truly serialized like
        `to_json_dict()`.
        """
        default_values = self.get_default_values() if ignore_defaults else {}
        data = {"name": self.name}
        if not ignore_defaults or self.description:
            data["description"] = self.description
        for name in self.get_field_names(visible_only=False):
            value = getattr(self, name)
            if default_values and value == default_values[name]:
                continue  # don't add default values to dictionary
            data[name] = value
        return data

    def to_json_dict(self, msb: MSB, ignore_defaults=True) -> dict[str, tp.Any]:
        """NOTE: This converts types to JSON-ready types. Use `.asdict()` for a straightforward field value mapping."""
        default_values = self.get_default_values() if ignore_defaults else {}

        data = {"name": self.name}  # type: dict[str, str | dict | list]
        if not ignore_defaults or self.description:
            data["description"] = self.description

        for name in self.get_field_names(visible_only=False):
            value = getattr(self, name)
            if default_values and value == default_values[name]:
                continue  # don't add default values to dictionary
            if isinstance(value, MSBEntry):
                # Construct a reference dictionary. (There are no real dictionary fields in `MSBEntry` subclasses.)
                try:
                    subtype_list = msb.get_list_of_entry(value)
                except ValueError as ex:
                    raise ValueError(
                        f"Invalid MSB entry `{value.name}` referenced by `{self.name}`."
                    ) from ex
                if subtype_list.supertype in {MSBSupertype.MODELS, MSBSupertype.PARTS}:
                    # Models and Parts have unique names, so we can safely reference those names instead of indices.
                    data[name] = {
                        "subtype": (subtype_list.supertype, subtype_list.subtype_name),
                        "entry_name": value.name,
                    }
                else:
                    data[name] = {
                        "subtype": (subtype_list.supertype, subtype_list.subtype_name),
                        "subtype_index": subtype_list.index(value),
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
                            "subtype": (ref_subtype_list.supertype, ref_subtype_list.subtype_name),
                            "subtype_index": ref_subtype_list.index(element)
                        })
                data[name] = ref_list
            elif isinstance(value, BaseVector):
                data[name] = list(value)
            else:
                # Custom types like `Vector3`, `BitSet`, and `RegionShape` can decode their own string `repr`.
                data[name] = value
        return data

    @classmethod
    def get_default_values(cls) -> MappingProxyType[str, tp.Any]:
        if cls._FIELD_DEFAULTS is not None:
            return cls._FIELD_DEFAULTS  # NOTE: immutable mapping

        defaults = {}
        for f in cls.get_entry_fields():
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

    @classmethod
    def get_entry_fields(cls) -> list[Field]:
        """Ignores all dataclass fields with dunders in them."""
        return [f for f in fields(cls) if "__" not in f.name]

    def __setattr__(self, key: str, value: tp.Any):
        """Enforces correct type and field presence. Also records `MSBEntry` references.

        This is slow and is deactivated when reading binary MSBs.
        """
        if self.__class__.SETATTR_CHECKS_DISABLED or "__" in key:
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

        entry_type_and_length_re = re.compile(r"([\w |]+)(\[\d+])?")

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

                entry_type_name, length_str = entry_type_and_length_re.match(field_type).groups()

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
                        for i, element in enumerate(value):
                            if element is None:
                                list_value.append(None)
                            elif self._is_subtype(element, entry_type_name):
                                list_value.append(element)
                                # Record `MSBEntry` reference with index.
                                element.referring_entry_fields.append(MSBEntryReference(self, field_name, i))
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
                                f"{value.__class__.__name__} ({value}). Expected type `{entry_type_name}`."
                            )
                    super(MSBEntry, self).__setattr__(field_name, value)
                    if value is not None:
                        # Record `MSBEntry` reference.
                        value.referring_entry_fields.append(MSBEntryReference(self, field_name))
                    return

                if field_type == "RegionShape":
                    # Region shape subclass.
                    if not isinstance(value, RegionShape):
                        raise TypeError(
                            f"Invalid type for `RegionShape` field `{self.cls_name}.{field_name}`: {value}"
                        )
                    super(MSBEntry, self).__setattr__(field_name, value)
                    return

                if field_type in {"BitSet128", "BitSet256", "BitSet1024"}:
                    # `BitSet` subclass of some maximum count.
                    if not isinstance(value, (BitSet128, BitSet256, BitSet1024)):
                        # Lists will be interpreted as packed uints, and sets as enabled bits.
                        if field_type.endswith("128"):
                            value = BitSet128(value)
                        elif field_type.endswith("256"):
                            value = BitSet256(value)
                        else:  # field_type.endswith("1024"):
                            value = BitSet1024(value)
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
    @contextlib.contextmanager
    def setattr_checks_disabled(cls):
        """Disable `__setattr__` type checks temporarily."""
        cls.SETATTR_CHECKS_DISABLED = True
        try:
            yield
        finally:
            cls.SETATTR_CHECKS_DISABLED = False

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
        if self.cls_name == "MSBDummyCharacter" and value.__class__.__name__ == "MSBObjectModel":
            # TODO: Could do a hash check for vanilla DSR file to skip m10_01 warning. But that seems REALLY try-hard.
            # _LOGGER.warning(
            #     f"`MSBDummyCharacter` '{self.name}' uses an `MSBObjectModel`: '{value.name}'.\n"
            #     f"    This happens, e.g., in m10_01_00_00 in vanilla DSR (unused bonfire 'o0200_0004')."
            # )
            return True
        if self.cls_name == "MSBDummyCharacter" and value.__class__.__name__ == "MSBAssetModel":
            # Happens in Elden Ring: e.g. 'AEG099_320'
            return True
        if self.cls_name == "MSBDummyAsset" and value.__class__.__name__ == "MSBCharacterModel":
            # Happens in Elden Ring.
            return True
        if self.cls_name == "MSBConnectCollision" and value.__class__.__name__ == "MSBMapPieceModel":
            # Happens in Elden Ring. TODO: Seems that 'ConnectCollision' class can attach to Map Pieces...
            # In Agheel's Lake, for map (32, 0, 0, 1), which is CLOSE to Sellia Crystal Tunnel (32, 8, 0, 0)...
            return True
        return False

    @classmethod
    def get_field_display_info(cls, field_name: str, game_types_module: ModuleType) -> MSBFieldDisplayInfo:
        """Retrieve display info for field `field_name` in this `MSBEntry` subclass."""

        # TODO: Add info about nested structs (e.g. GPARAM).
        if cls._FIELD_DISPLAY_INFO is not None:
            try:
                return cls._FIELD_DISPLAY_INFO[field_name]
            except KeyError:
                raise KeyError(f"Invalid MSB entry field (no metadata): `{cls.__name__}.{field_name}`")

        # Create and cache all fields' metadata.
        # TODO: Handle MSB GPARAM/SceneGPARAM (and nested structs more generally).
        #  - Can display fields as `GPARAM[Light Set ID]`, etc.
        field_types = cls.get_field_types()
        field_metadata = {}  # type: dict[str, MSBFieldDisplayInfo]
        for f in cls.get_entry_fields():
            if f.name in {"name", "description"}:
                # Dummy metadata (not treated as regular fields for display).
                field_metadata[f.name] = MSBFieldDisplayInfo(f.name.capitalize(), f.name.capitalize(), str)
                continue

            if f.name.startswith("_"):
                continue  # ignore (not a displayed field)

            metadata = f.metadata.get("msb", None)  # type: MapFieldMetadata
            if metadata is not None:
                # Some or all of these may be empty, and still need to be generated automatically below
                nickname = metadata.nickname
                tooltip = metadata.tooltip
                display_type = metadata.game_type
            else:
                # MSB field metadata is optional, unlike `ParamRow` metadata.
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
                        case "BitSet128":
                            display_type = BitSet128
                        case "BitSet256":
                            display_type = BitSet256
                        case "BitSet1024":
                            display_type = BitSet1024
                        case "RegionShape":
                            display_type = RegionShape
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

            field_metadata[f.name] = MSBFieldDisplayInfo(nickname, tooltip, display_type)

        cls._FIELD_DISPLAY_INFO = MappingProxyType(field_metadata)
        try:
            return cls._FIELD_DISPLAY_INFO[field_name]
        except KeyError:
            raise KeyError(f"Invalid MSB entry field (no metadata): `{cls.__name__}.{field_name}`")

    @classmethod
    def all_annotations(cls) -> ChainMap:
        """Returns a dictionary-like ChainMap that includes annotations for all attributes defined in `cls` or
        inherited from superclasses."""
        return ChainMap(*(c.__annotations__ for c in cls.__mro__ if '__annotations__' in c.__dict__))

    @classmethod
    def get_field_types(cls):
        """NOTE: Using string types from dataclass field annotations due to circular entry type references."""
        if cls._FIELD_TYPES is not None:
            return cls._FIELD_TYPES

        f_annotations = cls.all_annotations()

        field_types = {}
        for f in cls.get_entry_fields():
            ann = f_annotations[f.name]
            if not isinstance(ann, str):
                ann = ann.__name__  # can't be certain when annotation types will be preserved, so we always use strings

            # Check `MSBEntry` types first.
            if ann == "MSBEntry":
                # Base class reference is not allowed.
                raise TypeError(f"Field {cls.__name__}.{f.name} cannot have abstract `MSBEntry` type.")
            elif ann == "RegionShape":
                # Singular `BaseMSBRegion.shape` field, referencing a simple shape struct.
                field_types[f.name] = ann  # str
            elif list_match := cls._FIELD_REGEX["list"].match(ann):
                element_ann = list_match.group(1)
                if element_ann in {"int", "float", "bool"}:
                    pass  # fine (including reference indices)
                elif msb_ref_match := cls._FIELD_REGEX["msb_ref"].match(element_ann.removesuffix(" | None")):
                    element_ann = msb_ref_match.group(1)  # `| None` suffix removed
                else:
                    raise TypeError(f"Invalid list element type annotation '{element_ann}' for `{cls.__name__}`.")
                # Check binary metadata for length and store in type string.
                try:
                    binary_metadata = f.metadata["binary"]  # type: BinaryMetadata
                    if isinstance(binary_metadata, BinaryArrayMetadata):
                        if binary_metadata.length is None:
                            raise KeyError
                        length = binary_metadata.length
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
                field_types[f.name] = f"{element_ann}[{length}]"
            elif ann in _BASIC_ENTRY_TYPES:
                field_types[f.name] = ann
            else:
                # Try to parse as a type union of `MSBEntry` subclasses.
                entry_types = [e.strip() for e in ann.split("|")]
                parsed_types = []
                for entry_type in entry_types:
                    if entry_type == "None":
                        continue  # ignore; `None` is permitted for all entry reference fields
                    if entry_type == "MSBEntry":
                        raise TypeError(f"Field {cls.__name__}.{f.name} cannot have abstract `MSBEntry` type.")
                    if not cls._FIELD_REGEX["msb_ref"].match(entry_type):
                        raise TypeError(f"Invalid field type annotation '{ann}' for `{cls.__name__}.{f.name}`.")
                    parsed_types.append(entry_type)
                    # `MSBEntry` subclass. `__setattr__` will confirm that any set `value` has this name in its MRO.
                if not parsed_types:
                    raise TypeError(f"Could not parse field type annotation '{ann}' for `{cls.__name__}.{f.name}`.")
                field_types[f.name] = " | ".join(parsed_types)

        cls._FIELD_TYPES = MappingProxyType(field_types)
        return cls._FIELD_TYPES

    def __repr__(self):
        field_strings = []
        for field_name, value in self.to_dict(ignore_defaults=True).items():
            if isinstance(value, MSBEntry):
                field_strings.append(f"    {field_name}=<{value.cls_name}('{value.name}')>,")
            elif isinstance(value, list) and any(isinstance(e, MSBEntry) or e is None for e in value):
                field_strings.append(f"    {field_name}=[")
                # Find last index of non-`None` element.
                last_index = len(value) - 1
                while last_index >= 0 and value[last_index] is None:
                    last_index -= 1
                if last_index == -1:
                    field_strings[-1] += "]"  # no elements
                    continue
                for element in value[:last_index + 1]:
                    if element is None:
                        field_strings.append("        None,")
                    else:
                        field_strings.append(f"        <{element.cls_name}('{element.name}')>,")
                trailing_nones = len(value) - last_index - 1
                if trailing_nones > 0:
                    field_strings.append(f"        ... {trailing_nones} None,")

                field_strings.append("    ],")
            else:
                field_strings.append(f"    {field_name}={repr(value)},")
        return f"{self.cls_name}(\n" + "\n".join(field_strings) + "\n)"

    def __eq__(self, entry: MSBEntry):
        """Checks field equality, but only matches `MSBEntry` references by name."""
        if entry is None:
            return False
        if not isinstance(entry, self.__class__):
            return False
        for f in self.get_entry_fields():
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
        for f in self.get_entry_fields():
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

    def _consume_index(self, entry_lists: dict[str, IDList[MSBEntry]], list_name: str, field_name: str):
        """Resolve index to entry in `entry_lists` and set it as the field value."""
        index_field_name = f"_{field_name}_index"
        index = getattr(self, index_field_name)
        try:
            entry = entry_lists[list_name][index] if index != -1 else None
        except IndexError:
            entry = MSBBrokenEntryReference(list_name, index)
        else:
            if entry:
                entry.referring_entry_fields.append(MSBEntryReference(self, field_name))

        # Avoid using `MSBEntry.__setattr__` machinery.
        object.__setattr__(self, field_name, entry)
        object.__setattr__(self, index_field_name, None)

    def _consume_indices(self, entry_lists: dict[str, IDList[MSBEntry]], list_name: str, field_name: str):
        """Resolve all indices to entries in `entry_lists` and set them as the field value."""
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
                else:
                    entry.referring_entry_fields.append(MSBEntryReference(self, field_name, index))
            entries.append(entry)

        # Avoid using `MSBEntry.__setattr__` machinery.
        object.__setattr__(self, field_name, entries)
        object.__setattr__(self, indices_field_name, None)

    def try_index(
        self,
        entry_list: IDList[MSBEntry],
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
                    # `IDList.index` uses `is` (ID).
                    try:
                        indices.append(entry_list.index(entry))
                    except ValueError:
                        raise ValueError(
                            f"Could not find referenced entry `{entry.name}` for "
                            f"`{self.name}.{source_field_name}` in MSB list while packing."
                        )
            return indices
        # Otherwise, single entry.
        try:
            return entry_list.index(entry_or_entry_list)
        except ValueError:
            raise ValueError(
                f"Could not find referenced entry `{entry_or_entry_list.name}` for "
                f"`{self.name}.{source_field_name}` in MSB list while packing."
            )

    @property
    def cls_name(self) -> str:
        return self.__class__.__name__

    @property
    def referring_entry_fields(self) -> list[MSBEntryReference]:
        return self.__referring_entry_fields

    def inherit_referrers(self, old_entry: MSBEntry):
        """Update all referrers of `old_entry` to refer to `self` instead, then clear `old_entry`'s references.

        Usually only called when `old_entry` is being completely replaced in the MSB with this one.
        """
        if type(old_entry) is not type(self):
            raise TypeError(
                f"Cannot inherit referrers from a different MSB entry type "
                f"({type(old_entry).__name__} -/-> {type(self).__name__})."
            )
        for referrer, field_name, index in old_entry.referring_entry_fields:
            # Double-check that referrer still refers to old entry.
            if index is not None:
                ref_array = getattr(referrer, field_name)
                ref_value = ref_array[index]  # I don't believe this can ever raise an `IndexError` by type check
            else:
                ref_array = None
                ref_value = getattr(referrer, field_name)

            if ref_value is not old_entry:
                _LOGGER.warning(
                    f"Entry field '{referrer.name}.{field_name}' no longer refers to entry '{old_entry.name}'. "
                    f"Not inheriting this stale reference (still removed with all others)."
                )
                continue

            referring_entry_fields = self.referring_entry_fields
            if ref_array is not None:
                ref_array[index] = self
                referring_entry_fields.append(MSBEntryReference(referrer, field_name, index))
            else:
                setattr(referrer, field_name, self)
                referring_entry_fields.append(MSBEntryReference(referrer, field_name))

        # These old references are no longer valid.
        old_entry.referring_entry_fields.clear()

    # NOTE: No `_set_index` method needed, as indices for packing can be constructed temporarily.
