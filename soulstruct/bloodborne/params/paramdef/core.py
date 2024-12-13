from __future__ import annotations

__all__ = ["ParamDef", "ParamDefBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.params.paramdef import (
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)


class ParamDef(_BaseParamDef):

    unicode: bool = True
    format_version = 201


class ParamDefBND(_BaseParamDefBND):

    PARAMDEF_CLASS: tp.ClassVar = ParamDef
