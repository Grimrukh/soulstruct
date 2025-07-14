from __future__ import annotations

__all__ = ["COOL_TIME_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class COOL_TIME_PARAM_ST(ParamRow):
    LimitationTime0: float = ParamField(
        float32, "limitationTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime0: float = ParamField(
        float32, "observeTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTime1: float = ParamField(
        float32, "limitationTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime1: float = ParamField(
        float32, "observeTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTime2: float = ParamField(
        float32, "limitationTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime2: float = ParamField(
        float32, "observeTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTime3: float = ParamField(
        float32, "limitationTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime3: float = ParamField(
        float32, "observeTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
