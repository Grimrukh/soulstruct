from __future__ import annotations

__all__ = ["AUTO_CREATE_ENV_SOUND_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class AUTO_CREATE_ENV_SOUND_PARAM_ST(ParamRow):
    RangeMin: float = ParamField(
        float32, "RangeMin", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    RangeMax: float = ParamField(
        float32, "RangeMax", default=25.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeMin: float = ParamField(
        float32, "LifeTimeMin", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeMax: float = ParamField(
        float32, "LifeTimeMax", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    DeleteDist: float = ParamField(
        float32, "DeleteDist", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    NearDist: float = ParamField(
        float32, "NearDist", default=15.0,
        tooltip="TOOLTIP-TODO",
    )
    LimiteRotateMin: float = ParamField(
        float32, "LimiteRotateMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimiteRotateMax: float = ParamField(
        float32, "LimiteRotateMax", default=180.0,
        tooltip="TOOLTIP-TODO",
    )
