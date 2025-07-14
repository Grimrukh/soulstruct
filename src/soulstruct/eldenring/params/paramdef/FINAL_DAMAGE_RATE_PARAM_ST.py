from __future__ import annotations

__all__ = ["FINAL_DAMAGE_RATE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class FINAL_DAMAGE_RATE_PARAM_ST(ParamRow):
    PhysRate: float = ParamField(
        float, "physRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagRate: float = ParamField(
        float, "magRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireRate: float = ParamField(
        float, "fireRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunRate: float = ParamField(
        float, "thunRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkRate: float = ParamField(
        float, "darkRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaRate: float = ParamField(
        float, "staminaRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SaRate: float = ParamField(
        float, "saRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
