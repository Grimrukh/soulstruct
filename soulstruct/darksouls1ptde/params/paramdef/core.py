from __future__ import annotations

__all__ = ["ParamDef", "ParamDefBND"]

import typing as tp

from soulstruct.base.params.paramdef import (
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)


class ParamDef(_BaseParamDef):

    # Version default overrides.
    unicode: bool = False
    format_version: int = 104


class ParamDefBND(_BaseParamDefBND):
    PARAMDEF_CLASS: tp.ClassVar = ParamDef
