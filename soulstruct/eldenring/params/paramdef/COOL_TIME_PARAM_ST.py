from __future__ import annotations

__all__ = ["COOL_TIME_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class COOL_TIME_PARAM_ST(ParamRow):
    LimitationTime: float = ParamField(
        float, "limitationTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ObserveTime: float = ParamField(
        float, "observeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
