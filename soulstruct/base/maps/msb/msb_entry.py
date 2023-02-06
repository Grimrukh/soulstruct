from __future__ import annotations

__all__ = ["MSBEntry"]

import abc
import logging
import typing as tp
from copy import deepcopy
from dataclasses import dataclass, field, fields
from enum import IntEnum

from soulstruct.base.game_types import Map
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector
from soulstruct.utilities.text import pad_chars

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBEntry"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MSBEntry(abc.ABC):
    """Base class for entries of any type and subtype that appear in an `MSB` (under one of four entry superlists)."""

    # Shared between all game MSB entries. TODO: Infer from `reader.varint_size`?
    NAME_ENCODING: tp.ClassVar[str]
    # Generally only used to check against unpacked indices (which should have already been 'peeked' by the MSB).
    SUBTYPE_INT: tp.ClassVar[int]
    # Optional custom ordering for field display in GUI.
    FIELD_ORDER: tp.ClassVar[tuple[str, ...]] = ()

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
        kwargs |= cls.SUPERTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)
        relative_subtype_data_offset = kwargs.pop("subtype_data_offset")
        if relative_subtype_data_offset > 0:
            reader.seek(entry_offset + relative_subtype_data_offset)
            kwargs |= cls.unpack_subtype_data(reader)
        return cls(**kwargs)

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("subtype_int")
        if header_subtype_int != cls.SUBTYPE_INT:
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
        self.pack_header(writer, supertype_index, subtype_index)
        self.pack_supertype_data(writer, entry_lists)
        self.pack_subtype_data(writer, entry_lists)

    def pack_header(self, writer: BinaryWriter, supertype_index: int, subtype_index: int):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            _supertype_index=supertype_index,
            subtype_int=self.SUBTYPE_INT,
            _subtype_index=subtype_index,
            supertype_data_offset=RESERVED,
            subtype_data_offset=RESERVED,
        )
        writer.fill_with_position("name_offset", self)
        writer.append(pad_chars(self.name, encoding=self.NAME_ENCODING, alignment=4))

    def pack_supertype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        writer.fill_with_position("supertype_data_offset", self)
        self.SUPERTYPE_DATA_STRUCT.object_to_writer(self, writer)

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        if self.SUBTYPE_DATA_STRUCT is not None:
            writer.fill_with_position("subtype_data_offset", self)
            self.SUBTYPE_DATA_STRUCT.object_to_writer(self, writer)
        else:
            writer.fill("subtype_data_offset", 0, self)

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

    def copy(self):
        return deepcopy(self)

    def get_field_names(self, visible_only=True) -> tuple[str]:
        """Get all field names in `FIELD_ORDER`, or all names excluding basic 'name' and 'description'."""
        if visible_only and self.FIELD_ORDER:
            return self.FIELD_ORDER
        return tuple(f.name for f in fields(self) if f.name not in {"name", "description"})

    def set_entity_enum(self, entity_enum: IntEnum):
        """Only works for subclasses with `entity_id` field."""
        if not isinstance(entity_enum, IntEnum):
            raise TypeError(f"`entity_enum` must be an `IntEnum` subclass, not `{type(entity_enum)}`.")
        if "entity_id" in self.get_field_names(visible_only=False):
            setattr(self, "entity_id", entity_enum.value)
            self.name = entity_enum.name
        else:
            raise TypeError(f"MSB entry class `{self.__class__.__name__}` has no `entity_id` field.")

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        default_values = self.get_default_values()
        data = {"name": self.name}
        for name in self.get_field_names(visible_only=False):
            value = getattr(self, name)
            if ignore_defaults and value == default_values[name]:
                continue  # don't add default values to dictionary
            if isinstance(value, Vector):
                data[name] = list(value)
            elif isinstance(value, Map):
                data[name] = str(value)
            elif isinstance(value, set):
                data[name] = sorted(value)
            else:
                data[name] = value
        return data

    def get_default_values(self) -> dict[str, tp.Any]:
        return {f.name: f.default for f in fields(self) if f.name not in {"name", "description"}}

    def __repr__(self):
        data = self.to_dict(ignore_defaults=True)
        all_fields = "\n    ".join(f"{k}={repr(v)}," for k, v in data.items())
        return f"{self.__class__.__name__}(\n    {all_fields}\n)"

    def _consume_index(self, entry_lists: dict[str, list[MSBEntry]], list_name: str, field_name: str):
        index_field_name = f"_{field_name}_index"
        index = getattr(self, index_field_name)
        entry = entry_lists[list_name][index] if index != -1 else None
        setattr(self, field_name, entry)
        setattr(self, index_field_name, None)

    # NOTE: No `_set_index` method needed, as indices for packing can be constructed temporarily.
