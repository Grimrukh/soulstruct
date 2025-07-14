from __future__ import annotations

__all__ = ["SIGN_PUDDLE_TAB_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SIGN_PUDDLE_TAB_PARAM_ST(ParamRow):
    IsDlcTab: int = ParamField(
        int32, "isDlcTab", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TabTextId: int = ParamField(
        int32, "tabTextId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x8: int = ParamField(
        int32, "unknown_0x8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xc: int = ParamField(
        int32, "unknown_0xc", default=0,
        tooltip="TOOLTIP-TODO",
    )
