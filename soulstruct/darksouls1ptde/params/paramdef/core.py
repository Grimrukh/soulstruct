from __future__ import annotations

__all__ = ["ParamDef", "ParamDefBND", "GET_BUNDLED_PARAMDEFBND"]

import logging
import typing as tp
from dataclasses import dataclass

from soulstruct.base.params.paramdef import (
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)

_LOGGER = logging.getLogger("soulstruct")
_BUNDLED = None


@dataclass(slots=True)
class ParamDef(_BaseParamDef):

    # Version default overrides.
    unicode: bool = False
    format_version: int = 104


@dataclass(slots=True)
class ParamDefBND(_BaseParamDefBND):
    PARAMDEF_CLASS: tp.ClassVar = ParamDef


def GET_BUNDLED_PARAMDEFBND() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.get_game().name}.")
        _BUNDLED = ParamDefBND.from_bundled()
    return _BUNDLED
