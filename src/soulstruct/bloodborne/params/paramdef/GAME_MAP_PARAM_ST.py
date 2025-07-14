from __future__ import annotations

__all__ = ["GAME_MAP_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class GAME_MAP_PARAM_ST(ParamRow):
    TimeSlotA: int = ParamField(
        uint8, "settingNo_timeSlotA", default=0,
        tooltip="TODO",
    )
    TimeSlotB: int = ParamField(
        uint8, "settingNo_timeSlotB", default=0,
        tooltip="TODO",
    )
    TimeSlotC: int = ParamField(
        uint8, "settingNo_timeSlotC", default=0,
        tooltip="TODO",
    )
    TimeSlotD: int = ParamField(
        uint8, "settingNo_timeSlotD", default=0,
        tooltip="TODO",
    )
