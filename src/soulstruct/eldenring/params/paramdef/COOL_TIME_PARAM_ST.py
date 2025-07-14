from __future__ import annotations

__all__ = ["COOL_TIME_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class COOL_TIME_PARAM_ST(ParamRow):
    LimitationTime0: float = ParamField(
        float, "limitationTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime0: float = ParamField(
        float, "observeTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTime1: float = ParamField(
        float, "limitationTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime1: float = ParamField(
        float, "observeTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTime2: float = ParamField(
        float, "limitationTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime2: float = ParamField(
        float, "observeTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTime3: float = ParamField(
        float, "limitationTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime3: float = ParamField(
        float, "observeTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
