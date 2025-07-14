from __future__ import annotations

__all__ = ["COMMON_SYSTEM_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class COMMON_SYSTEM_PARAM_ST(ParamRow):
    MapSaveMapNameIdOnGameStart: int = ParamField(
        uint32, "mapSaveMapNameIdOnGameStart", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(60, "reserve0[60]")
