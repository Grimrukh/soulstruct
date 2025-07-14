from __future__ import annotations

__all__ = ["SIGN_PUDDLE_TAB_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SIGN_PUDDLE_TAB_PARAM_ST(ParamRow):
    IsDlcTab: int = ParamField(
        int, "isDlcTab", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TabTextId: int = ParamField(
        int, "tabTextId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x8: int = ParamField(
        int, "unknown_0x8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xc: int = ParamField(
        int, "unknown_0xc", default=0,
        tooltip="TOOLTIP-TODO",
    )
