from __future__ import annotations

__all__ = ["COOL_TIME_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1r.game_types import *
from soulstruct.darksouls1r.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class COOL_TIME_PARAM_ST(ParamRow):
    limitationTime_0: float = ParamField(
        float, "limitationTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_0: float = ParamField(
        float, "observationTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    limitationTime_1: float = ParamField(
        float, "limitationTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_1: float = ParamField(
        float, "observationTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    limitationTime_2: float = ParamField(
        float, "limitationTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_2: float = ParamField(
        float, "observationTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    limitationTime_3: float = ParamField(
        float, "limitationTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    observationTime_3: float = ParamField(
        float, "observationTime_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
