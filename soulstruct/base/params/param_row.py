from __future__ import annotations

__all__ = [
    "PARAM_GAME_TYPE",
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
from types import MappingProxyType

from soulstruct.base.game_types import GAME_INT_TYPE
from soulstruct.base.params.paramdef.field_types import base_type
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger("soulstruct")


# Param `game_type` (or display type) could be a `GameObjectInt` subclass or just a Python primitive type.
PARAM_GAME_TYPE = tp.Union[GAME_INT_TYPE, tp.Type[bool], tp.Type[int], tp.Type[float], tp.Type[str]]


class DynamicParamField(abc.ABC):
    """Called with a `ParamRow` instance.

    Returns a dynamic field type, suffix for the display field name, and tooltip.
    """

    # All types that could be returned by `__call__` for general validity checks.
    POSSIBLE_TYPES = set()

    @abc.abstractmethod
    def __call__(self, data: ParamRow) -> tuple[PARAM_GAME_TYPE, str, str]:
        """Returns `(game_type, suffix, tooltip)` tuple based on the given `ParamRow` instance."""
        ...

    def as_display_type(self, data: ParamRow) -> tuple[PARAM_GAME_TYPE, str, str]:
        """Converts dynamically returned `game_type` to a display type, which right now, is just BOOL redirect."""
        game_type, suffix, tooltip = self(data)
        if "BOOL" in game_type.__name__:
            return bool, suffix, tooltip
        return game_type, suffix, tooltip


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
        """Returns a mapping of all binary field names to their `ParamFieldMetadata` instances, constructed once on
        first call.

        Uses annotated type hints to update `game_type` of metadata if not set explicitly in `ParamRow` subclass.
        """
        if cls._FIELD_PARAM_METADATA is None:
            field_types = tp.get_type_hints(cls)
            field_metadata = {}
            for f in cls.get_binary_fields():
                metadata = f.metadata.get("param")  # type: ParamFieldMetadata  # must always exist
                if not metadata.game_type:
                    # Set `game_type` from type hint if not set explicitly in `ParamRow` subclass.
                    metadata.game_type = field_types[f.name]
                field_metadata[f.name] = metadata
            cls._FIELD_PARAM_METADATA = MappingProxyType(field_metadata)

        return cls._FIELD_PARAM_METADATA

    @classmethod
    def get_field_metadata(cls, field_name: str) -> ParamFieldMetadata:
        return cls.get_all_field_metadata()[field_name]

    def to_dict(
        self,
        ignore_pads=True,
        ignore_defaults=True,
        use_internal_names=False,
        row_name_encoding="shift_jis_2004",
        binary_fields_only=False,

    ) -> dict[str, PARAM_VALUE_TYPING]:
        """Allows options for not including pads, defaults, or sizes, and whether keys are internal names.

        NOTE: `RawName` is written as its string repr, e.g. 'b"name"', which will be read with `literal_eval`.
        It is also updated here from `Name` if `Name` is set.
        """
        if not binary_fields_only:
            if self.Name:
                # Update `RawName` before exporting dictionary.
                self.RawName = self.Name.encode(row_name_encoding)
            data = {"RawName": repr(self.RawName), "Name": self.Name}
        else:
            data = {}
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
        field_values = [f"\n    {key} = {value}" for key, value in self.to_dict(ignore_pads=True)]
        return f"\nName: {self.try_name}" + "".join(field_values)

    @classmethod
    def from_dict(cls, data: dict[str, tp.Any], row_name_encoding="shift_jis_2004"):
        """We prefer to set `RawName` from `Name`, but fall back to `RawName` if `Name` is empty."""
        if data["Name"]:
            raw_name = data["Name"].encode(row_name_encoding)  # type: bytes
            data.pop("RawName")  # replace with encoded `Name` if possible
        else:
            raw_name = ast.literal_eval(data.pop("RawName"))  # type: bytes
        return cls(RawName=raw_name, **data)

    @classmethod
    def from_reader(cls, reader: BinaryReader, raw_name: bytes, name: str = "") -> ParamRow:
        """`name` may be empty if `raw_name` failed to decode (unfortunately does happen in some vanilla Params)."""
        try:
            row = cls.from_bytes(reader)
        except Exception as ex:
            raise ValueError(f"Could not read `ParamRow` of data type `{cls.__name__}`: {ex}")
        row.RawName = raw_name
        row.Name = name
        return row

    # `to_writer()` does not need overriding, as name is packed later.

    def get_packed_name(self, encoding: str) -> bytes:
        raw_name = self.Name.encode(encoding) if self.Name else self.RawName
        terminator = b"\0\0" if encoding.replace("-", "").startswith("utf16") else b"\0"
        raw_stripped = raw_name.rstrip(b"\0")
        if not raw_stripped:
            return b""  # zero offset for name
        return raw_stripped + terminator

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
    param_enum: type[base_type] = None
    game_type: PARAM_GAME_TYPE = None  # NOTE: may be set by `ParamRow.get_all_field_metadata()` from type hint
    hide: bool = False
    dynamic_callback: DynamicParamField | None = None
    tooltip: str = "TOOLTIP-TODO"
    is_pad: bool = False

    def get_display_type(self) -> type:
        """Prefers `param_enum` to `game_type`, but redirects basic BOOL enums to Python `bool`."""
        if self.param_enum:
            if "BOOL" in self.param_enum.__name__:
                return bool
            return self.param_enum
        if self.game_type:
            return self.game_type
        raise ValueError(f"Param field {self.internal_name} has no `param_enum` or `game_type`.")


def ParamField(
    field_type: type[PRIMITIVE_FIELD_TYPING],
    internal_name: str,
    param_enum: type[base_type] = None,
    game_type: PARAM_GAME_TYPE = None,
    length: int | None = None,
    encoding: str = None,
    bit_count: int = -1,
    hide: bool = False,
    default: tp.Any = None,
    dynamic_callback: DynamicParamField | None = None,
    tooltip: str = "TOOLTIP-TODO",
):
    """`dataclasses.field()` wrapper for defining `ParamRow` binary fields.

    `dynamic_callback`, if given, should be a `DynamicParamField` callable that takes the `ParamRow` instance (usually
    to check the value of one specific field) and returns a tuple of `(py_type, name_suffix, tooltip)`. The
    `name_suffix` will be appended to this field nickname in the GUI to indicate the category of the dynamic reference
    type.
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


def ParamBitPad(field_type: type[PRIMITIVE_FIELD_TYPING], internal_name: str, bit_count: int):
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
