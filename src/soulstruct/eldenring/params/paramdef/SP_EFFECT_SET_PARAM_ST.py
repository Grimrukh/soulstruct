from __future__ import annotations

__all__ = ["SP_EFFECT_SET_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SP_EFFECT_SET_PARAM_ST(ParamRow):
    SpEffectId1: int = ParamField(
        int32, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId2: int = ParamField(
        int32, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId3: int = ParamField(
        int32, "spEffectId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId4: int = ParamField(
        int32, "spEffectId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
