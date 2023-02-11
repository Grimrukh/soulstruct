from __future__ import annotations

__all__ = [
    "DynamicParamFieldInfo",
    "ParamFieldInfo",
    "DynamicParamField",
    "pad_field",
    "bit_pad_field",
    "ParamRowData",
    "MAP_PARAM_TYPES",
    "PARAM_VALUE_TYPING",
    "ParamField",
    "ParamPad",
    "ParamBitPad",
]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_types import BaseGameObject
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger(__name__)


class DynamicParamFieldInfo:
    """TODO: Deprecated."""

    def __init__(self, name, other_field):
        self.name = name
        self.other_field = other_field


class ParamFieldInfo:
    """TODO: Deprecated."""
    def __init__(self, name, nickname, is_enabled, field_type, description="TODO", default_value=None):
        self.name = name
        self.nickname = nickname
        self.is_enabled = is_enabled
        self.field_type = field_type
        self.description = description
        self.default_value = default_value

    def __call__(self, entry):
        """No harm done if you treat this as a `DynamicFieldInfo`."""
        return self

    @property
    def docstring(self):
        return f"[{self.name}] {self.description}"


class DynamicParamField(abc.ABC):
    """Called with a `ParamRowData` instance.

    Returns a dynamic field type, suffix for the display field name, and tooltip.
    """

    # All types that could be returned by `__call__` for general validity checks.
    POSSIBLE_TYPES = set()

    @abc.abstractmethod
    def __call__(self, data: ParamRowData) -> tuple[tp.Type[BaseGameObject, str, str]]:
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
    "fixstr": bytes,  # not decoded
    "fixstrW": bytes,  # not decoded
}


PARAM_VALUE_TYPING = tp.Union[int, bool, float, str, bytes]


@dataclass(slots=True)
class ParamRowData(NewBinaryStruct):
    """Base class for `ParamDef`-spawned classes, instantiated to `ParamRow.data`."""

    RawName: bytes = field(default=b"", metadata={"NOT_BINARY": True})
    Name: str = field(default="", metadata={"NOT_BINARY": True})

    def __iter__(self):
        field_names = self.get_binary_field_names()
        print(field_names)
        exit()
        return
        # return (field_name, getattr(self, field_name) for field_name in self.get_binary_field_names())

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

    def to_dict(
        self, ignore_pads=True, ignore_defaults=True, use_internal_names=False
    ) -> dict[str, PARAM_VALUE_TYPING]:
        """Allows options for not including pads, defaults, or sizes, and whether keys are internal names."""
        data = {"RawName": self.RawName, "Name": self.Name}
        for binary_field in self.get_binary_fields():
            binary = binary_field.metadata["binary"]  # type: BinaryFieldMetadata
            if ignore_pads and binary_field.type == bytes and binary.asserted:
                continue  # ignore pad
            info = binary_field.metadata["param"]  # type: ParamFieldMetadata
            value = getattr(self, binary_field.name)
            if ignore_defaults and value == info.default:
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
    def from_reader(cls, reader: BinaryReader, raw_name: bytes, name: str = "") -> ParamRowData:
        row = cls.from_bytes(reader)
        row.RawName = raw_name
        row.Name = name
        return row

    # `to_writer()` does not need overriding, as name is packed later.

    def pack_name(self, writer: BinaryWriter, encoding: str):
        raw_name = self.Name.encode(encoding) if self.Name else self.RawName
        terminator = b"\0\0" if encoding.replace("-", "").startswith("utf16") else b"\0"
        raw_name = raw_name.rstrip(b"\0") + terminator
        writer.append(raw_name)

    def compare(self, other_row: ParamRowData):
        """Prints each field that differs between the given `ParamRow` and this one (ignoring names)."""
        for field_name, field_value in iter(self):
            other_value = other_row[field_name]
            if other_value != field_value:
                print(f"  {field_name}: this = {field_value}, other = {other_value}")


@dataclass(slots=True)
class ParamFieldMetadata(NewBinaryStruct):
    internal_name: str
    hide: bool = False
    dynamic_callback: tp.Callable[[ParamRowData], tuple[tp.Type[BaseGameObject], str, str]] | None = None
    tooltip: str = "TOOLTIP-TODO"
    default: tp.Any = None


def ParamField(
    fmt: tp.Type[PRIMITIVE_FIELD_TYPING],
    internal_name: str,
    length: int | None = None,
    bit_count: int = -1,
    hide: bool = False,
    default: tp.Any = None,
    dynamic_callback: DynamicParamField | None = None,
    tooltip: str = "TOOLTIP-TODO",
):
    """For use with double asterisk in `BinaryStruct` `field()` definition.

    `dynamic_callback`, if given, should be a function that takes the `ParamRowData` instance (usually to check the
    value of one specific field) and returns a tuple of `(py_type, name_suffix, tooltip)`. The `name_suffix` will be
    appended to this field nickname in the GUI to indicate the category of the dynamic reference type.
    """
    # TODO: Scan internal name to auto-detect and asserted for 'pad[size]', and detect bit fields.
    return field(
        default=default,
        metadata={
            "binary": BinaryFieldMetadata(
                fmt=fmt,
                length=length,
                bit_count=bit_count,
            ),
            "param": ParamFieldMetadata(
                internal_name=internal_name,
                hide=hide,
                dynamic_callback=dynamic_callback,
                tooltip=tooltip,
            ),
        },
    )


def ParamPad(size: int, internal_name: str):
    """Shortcut for a Param normal 'array' padding field (a field with type `dummy8` and [] in name)."""
    return field(
        default=b"\0" * size,
        metadata={
            "binary": BinaryFieldMetadata(
                fmt=f"{size}s",
                asserted=[b"\0" * size],
            ),
            "param": ParamFieldMetadata(
                internal_name=internal_name,
                hide=True,
                dynamic_callback=None,
                tooltip=f"Null padding ({size} bytes).",
            ),
        },
    )


def ParamBitPad(fmt: tp.Type[PRIMITIVE_FIELD_TYPING], internal_name: str, bit_count: int):
    """Shortcut for a Param bit-padding field (a field with type `dummy8` and `bit_count != -1` from colon in name)."""
    return field(
        default=0,
        metadata={
            "binary": BinaryFieldMetadata(
                fmt=fmt,
                bit_count=bit_count,
                asserted=[0],
            ),
            "param": ParamFieldMetadata(
                internal_name=internal_name,
                hide=True,
                dynamic_callback=None,
                tooltip=f"Null padding ({bit_count} bits).",
            ),
        },
    )
