from __future__ import annotations

__all__ = [
    "ParamFieldInfo",
    "DynamicParamFieldInfo",
    "pad_field",
    "bit_pad_field",
    "ParamRowData",
    "MAP_PARAM_TYPES",
    "ParamField",
    "ParamPad",
    "ParamBitPad",
]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field, Field
from types import MappingProxyType

from soulstruct.base.game_types import BaseGameObject
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger(__name__)


class ParamFieldInfo:
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


class DynamicParamFieldInfo(abc.ABC):
    """Called with a `ParamEntry` instance, in which `type_field_name` is checked before returning `FieldInfo`."""

    POSSIBLE_TYPES = set()

    def __init__(self, name, type_field_name):
        self.name = name
        self.type_field_name = type_field_name

    @abc.abstractmethod
    def __call__(self, entry) -> ParamFieldInfo:
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


@dataclass(slots=True)
class ParamRowData(NewBinaryStruct):
    """Base class for `ParamDef`-spawned classes, instantiated to `ParamRow.data`."""


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
    dynamic_callback: tp.Callable[[ParamRowData], tuple[tp.Type[PRIMITIVE_FIELD_TYPING], str, str]] = None,
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
