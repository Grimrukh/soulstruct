from __future__ import annotations

__all__ = ["EVENT_FLAG_USAGE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EVENT_FLAG_USAGE_PARAM_ST(ParamRow):
    UsageType: int = ParamField(
        uint8, "usageType", EVENT_FLAG_USAGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlaylogCategory: int = ParamField(
        uint8, "playlogCategory", EVENT_FLAG_USAGE_PLAYLOG_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "padding1[2]")
    FlagNum: int = ParamField(
        int32, "flagNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "padding2[24]")
