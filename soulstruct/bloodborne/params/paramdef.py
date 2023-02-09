from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND", "GET_BUNDLED_PARAMDEF"]

import logging
import typing as tp
from dataclasses import dataclass

from soulstruct.base.params.paramdef import (
    ParamDefField as _BaseParamDefField,
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)

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


@dataclass(slots=True)
class ParamDef(_BaseParamDef):

    FIELD_CLASS: tp.ClassVar = ParamDefField

    unicode: bool = True
    format_version = 201

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


def GET_BUNDLED_PARAMDEF() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.get_game().name}.")
        _BUNDLED = ParamDefBND()
    return _BUNDLED
