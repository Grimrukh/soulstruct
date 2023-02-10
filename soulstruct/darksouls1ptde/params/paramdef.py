from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND", "GET_BUNDLED_PARAMDEFBND"]

import logging
import typing as tp
from dataclasses import dataclass

from soulstruct.base.params.paramdef import (
    ParamDefField as _BaseParamDefField,
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)

from .defaults import DEFAULTS
from .display_info import get_param_info, get_param_info_field

if tp.TYPE_CHECKING:
    from soulstruct.base.params.param import ParamRow

_LOGGER = logging.getLogger(__name__)
_BUNDLED = None


@dataclass(slots=True)
class ParamDefField(_BaseParamDefField):

    def get_display_info(self, row: ParamRow):
        try:
            field_info = get_param_info_field(self.param_type, self.name)
        except ValueError:
            raise ValueError(f"No display information given for field '{self.name}'.")
        return field_info(row)

    def get_py_default(self):
        v = DEFAULTS[self.param_type].get(self.name, self.default)
        if self.bit_count == 1 and self.internal_type != "dummy8":
            return bool(v)
        elif self.internal_type not in {"f32", "f64"}:
            return int(v)
        return v


@dataclass(slots=True)
class ParamDef(_BaseParamDef):

    FIELD_CLASS: tp.ClassVar[tp.Type[ParamDefField]] = ParamDefField

    # Version default overrides.
    unicode: bool = False
    format_version: int = 104

    @property
    def param_info(self):
        try:
            return get_param_info(self.param_type)
        except KeyError:
            # This param has no extra information.
            return None


@dataclass(slots=True)
class ParamDefBND(_BaseParamDefBND):
    PARAMDEF_CLASS: tp.ClassVar = ParamDef


def GET_BUNDLED_PARAMDEFBND() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.get_game().name}.")
        _BUNDLED = ParamDefBND.from_bundled()
    return _BUNDLED
