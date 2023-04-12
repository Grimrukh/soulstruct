from __future__ import annotations

__all__ = [
    "DynamicParamField",
    "pad_field",
    "bit_pad_field",
    "ParamRow",
    "MAP_PARAM_TYPES",
    "PARAM_VALUE_TYPING",
    "ParamFieldMetadata",
    "ParamField",
    "ParamPad",
    "ParamBitPad",
]

import abc
import ast
import logging
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum
from types import MappingProxyType

from soulstruct.base.game_types import GAME_INT_TYPE
from soulstruct.base.params.paramdef.field_types import base_type
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger(__name__)


class ParamEnum(IntEnum):
    """Base class for all internal enums used by Param fields, e.g. `ITEMLOT_ITEMCATEGORY`."""
    pass


class DynamicParamField(abc.ABC):
    """Called with a `ParamRow` instance.

    Returns a dynamic field type, suffix for the display field name, and tooltip.
    """

    # All types that could be returned by `__call__` for general validity checks.
    POSSIBLE_TYPES = set()

    @abc.abstractmethod
    def __call__(self, data: ParamRow) -> tuple[GAME_INT_TYPE, str, str]:
        ...


def pad_field(n):
    return f"<Pad:{n}>"


def bit_pad_field(n):
    return f"<BitPad:{n}>"


# TODO: Param types should just use these new binary types.
MAP_PARAM_TYPES = {
    "dummy8": byte,  # pad field
    "u8": byte,
    "u16": ushort,
    "u32": uint,
    "s8": sbyte,
    "s16": short,
    "s32": int,
    "f32": float,
    "f64": double,
    "fixstr": str,  # decoded
    "fixstrW": str,  # decoded
}


PARAM_VALUE_TYPING = tp.Union[int, bool, float, str, bytes]


@dataclass(slots=True)
class ParamRow(BinaryStruct):
    """Base class for `ParamDef`-spawned classes. Instances appear directly in `Param.rows`."""

    # Cached on first use. Maps binary field names (i.e. not including Name/RawName) to `ParamFieldMetadata` instances.
    _FIELD_PARAM_METADATA: tp.ClassVar[MappingProxyType[str, ParamFieldMetadata]] = None

    RawName: bytes = field(default=b"", metadata={"NOT_BINARY": True})
    Name: str = field(default="", metadata={"NOT_BINARY": True})

    def __iter__(self) -> tp.Iterator[tuple[str, PARAM_VALUE_TYPING]]:
        """Similar to `.items()`. Returns a tuple of `(name, value)` pairs."""
        return iter((field_name, getattr(self, field_name)) for field_name in self.get_binary_field_names())

    def __getitem__(self, field_name_or_nickname: str) -> PARAM_VALUE_TYPING:
        if field_name_or_nickname.lower() == "name":
            return self.Name
        elif field_name_or_nickname.lower() == "rawname":
            return self.RawName

        for binary_field in self.get_binary_fields():
            if binary_field.name == field_name_or_nickname:
                return getattr(self, binary_field.name)
            elif binary_field.metadata["param"].internal_name == field_name_or_nickname:
                return getattr(self, binary_field.name)
        raise KeyError(f"No field with internal name or nickname '{field_name_or_nickname}'.")

    def __setitem__(self, field_name_or_nickname: str, value: PARAM_VALUE_TYPING):
        if field_name_or_nickname.lower() == "name":
            self.Name = value
            return
        elif field_name_or_nickname.lower() == "rawname":
            self.RawName = value
            return

        for binary_field in self.get_binary_fields():
            if binary_field.name == field_name_or_nickname:
                setattr(self, binary_field.name, value)
                return
            elif binary_field.metadata["param"].internal_name == field_name_or_nickname:
                setattr(self, binary_field.name, value)
                return
        raise KeyError(f"No field with internal name or nickname '{field_name_or_nickname}'.")

    @classmethod
    def get_internal_names(cls) -> tuple[str, ...]:
        """Returns a tuple of all internal names (in order) for this Param type."""
        return tuple(metadata.internal_name for metadata in cls.get_all_field_metadata().values())

    @classmethod
    def get_all_field_metadata(cls) -> MappingProxyType[str, ParamFieldMetadata]:
        """Returns a mapping of all binary field names to their `ParamFieldMetadata` instances."""
        if cls._FIELD_PARAM_METADATA is None:
            field_types = tp.get_type_hints(cls)
            field_metadata = {}
            for f in cls.get_binary_fields():
                metadata = f.metadata.get("param")  # type: ParamFieldMetadata  # must always exist
                if not metadata.game_type:
                    metadata.game_type = field_types[f.name]
                field_metadata[f.name] = metadata
            cls._FIELD_PARAM_METADATA = MappingProxyType(field_metadata)

        return cls._FIELD_PARAM_METADATA

    @classmethod
    def get_field_metadata(cls, field_name: str) -> ParamFieldMetadata:
        return cls.get_all_field_metadata()[field_name]

    def to_dict(
        self, ignore_pads=True, ignore_defaults=True, use_internal_names=False
    ) -> dict[str, PARAM_VALUE_TYPING]:
        """Allows options for not including pads, defaults, or sizes, and whether keys are internal names.

        NOTE: `RawName` is written as its string repr, e.g. 'b"name"', which will be read with `literal_eval`.
        """
        data = {"RawName": repr(self.RawName), "Name": self.Name}
        for binary_field in self.get_binary_fields():
            info = binary_field.metadata["param"]  # type: ParamFieldMetadata
            if ignore_pads and info.is_pad:
                continue  # ignore pad
            value = getattr(self, binary_field.name)
            if ignore_defaults and value == binary_field.default:
                continue  # ignore default value
            key = info.internal_name if use_internal_names else binary_field.name
            data[key] = value
        return data

    def update(self, **kwargs):
        for field_name, field_value in kwargs.items():
            self.__setitem__(field_name, field_value)

    @property
    def try_name(self) -> str:
        return self.Name if self.Name else repr(self.RawName)

    @property
    def field_nicknames(self) -> tuple[str, ...]:
        return self.get_binary_field_names()

    def __repr__(self):
        names = [f"\n    {key} = {value}" for key, value in self.to_dict(ignore_pads=True)]
        return f"\nName: {self.try_name}" + "".join(names)

    @classmethod
    def from_dict(cls, data: dict[str, tp.Any]):
        """`RawName` is written to dictionary as a string repr."""
        raw_name = ast.literal_eval(data.pop("RawName"))  # type: bytes
        return cls(RawName=raw_name, **data)

    @classmethod
    def from_reader(cls, reader: BinaryReader, raw_name: bytes, name: str = "") -> ParamRow:
        try:
            row = cls.from_bytes(reader)
        except Exception as ex:
            raise ValueError(f"Could not read ParamRow of data type `{cls.__name__}`: {ex}")
        row.RawName = raw_name
        row.Name = name
        return row

    # `to_writer()` does not need overriding, as name is packed later.

    def pack_name(self, writer: BinaryWriter, encoding: str):
        raw_name = self.Name.encode(encoding) if self.Name else self.RawName
        terminator = b"\0\0" if encoding.replace("-", "").startswith("utf16") else b"\0"
        raw_name = raw_name.rstrip(b"\0") + terminator
        writer.append(raw_name)

    def compare(self, other_row: ParamRow):
        """Prints each field that differs between the given `ParamRow` and this one (ignoring names)."""
        for field_name, field_value in iter(self):
            other_value = other_row[field_name]
            if other_value != field_value:
                print(f"  {field_name}: this = {field_value}, other = {other_value}")


@dataclass(slots=True)
class ParamFieldMetadata:
    """Not a `NamedTuple` as it may be modified with defaults."""
    internal_name: str
    param_enum: tp.Type[base_type] = None
    game_type: GAME_INT_TYPE = None
    hide: bool = False
    dynamic_callback: DynamicParamField | tp.Callable[[ParamRow], tuple[GAME_INT_TYPE, str, str]] | None = None
    tooltip: str = "TOOLTIP-TODO"
    is_pad: bool = False


def ParamField(
    field_type: tp.Type[PRIMITIVE_FIELD_TYPING],
    internal_name: str,
    param_enum: tp.Type[base_type] = None,
    game_type: GAME_INT_TYPE = None,
    length: int | None = None,
    encoding: str = None,
    bit_count: int = -1,
    hide: bool = False,
    default: tp.Any = None,
    dynamic_callback: DynamicParamField | None = None,
    tooltip: str = "TOOLTIP-TODO",
):
    """For use with double asterisk in `BinaryStruct` `field()` definition.

    `dynamic_callback`, if given, should be a function that takes the `ParamRow` instance (usually to check the
    value of one specific field) and returns a tuple of `(py_type, name_suffix, tooltip)`. The `name_suffix` will be
    appended to this field nickname in the GUI to indicate the category of the dynamic reference type.
    """
    if field_type is str:
        metadata = BinaryString(fmt_or_byte_size=length, encoding=encoding)
    else:
        metadata = Binary(fmt=field_type, bit_count=bit_count)
    metadata["metadata"] |= {
        "param": ParamFieldMetadata(
            internal_name=internal_name,
            param_enum=param_enum,
            game_type=game_type,
            hide=hide,
            dynamic_callback=dynamic_callback,
            tooltip=tooltip,
        ),
    }

    return field(default=default, **metadata)


def ParamPad(size: int, internal_name: str):
    """Shortcut for a Param normal 'array' padding field (a field with type `dummy8` and [] in name)."""
    metadata = Binary(
        fmt=f"{size}s",
        # asserted=(b"\0" * size,),  # TODO: Finding non-null pad values...
    )
    metadata["metadata"] |= {
        "param": ParamFieldMetadata(
            internal_name=internal_name,
            hide=True,
            dynamic_callback=None,
            tooltip=f"Null padding ({size} bytes).",
            is_pad=True,
        ),
    }
    return field(default=b"\0" * size, **metadata)


def ParamBitPad(field_type: tp.Type[PRIMITIVE_FIELD_TYPING], internal_name: str, bit_count: int):
    """Shortcut for a Param bit-padding field (a field with type `dummy8` and `bit_count != -1` from colon in name)."""
    metadata = Binary(
        fmt=field_type,
        bit_count=bit_count,
        # asserted=[0],  # TODO: Finding non-null pad values...
    )
    metadata["metadata"] |= {
        "param": ParamFieldMetadata(
            internal_name=internal_name,
            hide=True,
            dynamic_callback=None,
            tooltip=f"Null padding ({bit_count} bits).",
        ),
    }
    return field(default=0, **metadata)
