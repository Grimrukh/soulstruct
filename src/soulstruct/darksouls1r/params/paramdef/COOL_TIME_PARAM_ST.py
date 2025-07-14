from __future__ import annotations

__all__ = ["COOL_TIME_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class COOL_TIME_PARAM_ST(ParamRow):
    limitationTime_0: float = ParamField(
        float32, "limitationTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_0: float = ParamField(
        float32, "observationTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    limitationTime_1: float = ParamField(
        float32, "limitationTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_1: float = ParamField(
        float32, "observationTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    limitationTime_2: float = ParamField(
        float32, "limitationTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_2: float = ParamField(
        float32, "observationTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    limitationTime_3: float = ParamField(
        float32, "limitationTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_3: float = ParamField(
        float32, "observationTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
