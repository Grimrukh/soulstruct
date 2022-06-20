from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND", "GET_BUNDLED_PARAMDEF"]

import logging
import typing as tp

from soulstruct.base.params.paramdef import (
    ParamDefField as _BaseParamDefField,
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)
from soulstruct.games import DarkSoulsDSRType
from soulstruct.utilities.binary import BinaryStruct

from .defaults import DEFAULTS
from .display_info import get_param_info, get_param_info_field

if tp.TYPE_CHECKING:
    from soulstruct.base.params.param import ParamRow

_LOGGER = logging.getLogger(__name__)
_BUNDLED = None


class ParamDefField(_BaseParamDefField):
    STRUCT = BinaryStruct(
        ("display_name", "64j"),
        ("display_type", "8j"),
        ("display_format", "8j"),  # %i, %u, %d, etc.
        ("default", "f"),
        ("minimum", "f"),
        ("maximum", "f"),
        ("increment", "f"),
        ("edit_flags", "i"),
        ("size", "i"),
        ("description_offset", "i"),
        ("internal_type", "32j"),  # could be an enum name (see params.enums)
        ("name", "32j"),
        ("sort_id", "i"),
    )

    def get_display_info(self, row: ParamRow):
        try:
            field_info = get_param_info_field(self.param_name, self.name)
        except ValueError:
            raise ValueError(f"No display information given for field '{self.name}'.")
        return field_info(row)

    def get_default_value(self):
        v = DEFAULTS[self.param_name].get(self.name, self.default)
        if self.bit_count == 1 and self.internal_type != "dummy8":
            return bool(v)
        elif self.internal_type == "":
            if self.display_name == "sfxMultiplier":  # malformed in ParamDef
                return v  # float
            raise ValueError(f"No internal type for {self.param_name} field {self.display_name}")
        elif self.internal_type not in {"f32", "f64"}:
            return int(v)
        return v


class ParamDef(_BaseParamDef):
    BYTE_ORDER = "<"
    HEADER_STRUCT = BinaryStruct(
        ("size", "i"),
        ("header_size", "H", 48),
        ("data_version", "H"),
        ("field_count", "H"),
        ("field_size", "H", 176),
        ("param_name", "32j"),
        ("big_endian", "B", 0),
        ("unicode", "?"),
        ("format_version", "h", 104),
    )
    FIELD_CLASS = ParamDefField

    @property
    def param_info(self):
        try:
            return get_param_info(self.param_type)
        except KeyError:
            # This param has no extra information.
            return None


class ParamDefBND(_BaseParamDefBND, DarkSoulsDSRType):
    PARAMDEF_CLASS = ParamDef


def GET_BUNDLED_PARAMDEF() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.GAME.name}.")
        _BUNDLED = ParamDefBND()
    return _BUNDLED
