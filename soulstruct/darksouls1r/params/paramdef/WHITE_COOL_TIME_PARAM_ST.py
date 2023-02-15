from __future__ import annotations

__all__ = ["WHITE_COOL_TIME_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1r.game_types import *
from soulstruct.darksouls1r.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WHITE_COOL_TIME_PARAM_ST(ParamRow):
    timeLimit0: float = ParamField(
        float, "timeLimit0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    timeLimit1: float = ParamField(
        float, "timeLimit1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    timeLimit2: float = ParamField(
        float, "timeLimit2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    timeLimit3: float = ParamField(
        float, "timeLimit3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
