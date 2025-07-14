from __future__ import annotations

__all__ = ["FINAL_DAMAGE_RATE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class FINAL_DAMAGE_RATE_PARAM_ST(ParamRow):
    PhysRate: float = ParamField(
        float32, "physRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagRate: float = ParamField(
        float32, "magRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireRate: float = ParamField(
        float32, "fireRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunRate: float = ParamField(
        float32, "thunRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkRate: float = ParamField(
        float32, "darkRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaRate: float = ParamField(
        float32, "staminaRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SaRate: float = ParamField(
        float32, "saRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
