from __future__ import annotations

__all__ = ["GAME_MAP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GAME_MAP_PARAM_ST(ParamRow):
    TimeSlotA: int = ParamField(
        byte, "settingNo_timeSlotA", default=0,
        tooltip="TODO",
    )
    TimeSlotB: int = ParamField(
        byte, "settingNo_timeSlotB", default=0,
        tooltip="TODO",
    )
    TimeSlotC: int = ParamField(
        byte, "settingNo_timeSlotC", default=0,
        tooltip="TODO",
    )
    TimeSlotD: int = ParamField(
        byte, "settingNo_timeSlotD", default=0,
        tooltip="TODO",
    )
