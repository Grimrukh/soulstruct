from __future__ import annotations

__all__ = ["WHITE_COOL_TIME_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class WHITE_COOL_TIME_PARAM_ST(ParamRow):
    timeLimit0: float = ParamField(
        float32, "timeLimit0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    timeLimit1: float = ParamField(
        float32, "timeLimit1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    timeLimit2: float = ParamField(
        float32, "timeLimit2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    timeLimit3: float = ParamField(
        float32, "timeLimit3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
