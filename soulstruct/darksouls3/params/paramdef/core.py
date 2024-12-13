from __future__ import annotations

__all__ = ["ParamDef", "ParamDefBND"]

import logging
import typing as tp
from dataclasses import dataclass

from soulstruct.base.params.paramdef import ParamDef as _BaseParamDef, ParamDefBND as _BaseParamDefBND

_LOGGER = logging.getLogger("soulstruct")
_BUNDLED = None


class ParamDef(_BaseParamDef):

    unicode: bool = True
    format_version = 202


class ParamDefBND(_BaseParamDefBND):
    # TODO: I don't think DS3 has a `ParamDefBND`. Will need Paramdex, like Elden Ring.
    PARAMDEF_CLASS: tp.ClassVar = ParamDef
