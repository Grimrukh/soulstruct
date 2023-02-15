from __future__ import annotations

__all__ = ["SP_EFFECT_SET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SP_EFFECT_SET_PARAM_ST(ParamRow):
    SpEffectId1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId2: int = ParamField(
        int, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId3: int = ParamField(
        int, "spEffectId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId4: int = ParamField(
        int, "spEffectId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
