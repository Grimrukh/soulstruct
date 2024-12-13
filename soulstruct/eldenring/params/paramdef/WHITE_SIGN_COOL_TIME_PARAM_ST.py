from __future__ import annotations

__all__ = ["WHITE_SIGN_COOL_TIME_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WHITE_SIGN_COOL_TIME_PARAM_ST(ParamRow):
    LimitationTimeNormal: float = ParamField(
        float, "limitationTime_Normal", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTimeNormalDriedFinger: float = ParamField(
        float, "limitationTime_NormalDriedFinger", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTimeGuardian: float = ParamField(
        float, "limitationTime_Guardian", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimitationTimeGuardianDriedFinger: float = ParamField(
        float, "limitationTime_GuardianDriedFinger", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
