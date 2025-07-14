from __future__ import annotations

__all__ = ["AUTO_CREATE_ENV_SOUND_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class AUTO_CREATE_ENV_SOUND_PARAM_ST(ParamRow):
    RangeMin: float = ParamField(
        float, "RangeMin", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    RangeMax: float = ParamField(
        float, "RangeMax", default=25.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeMin: float = ParamField(
        float, "LifeTimeMin", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeMax: float = ParamField(
        float, "LifeTimeMax", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    DeleteDist: float = ParamField(
        float, "DeleteDist", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    NearDist: float = ParamField(
        float, "NearDist", default=15.0,
        tooltip="TOOLTIP-TODO",
    )
    LimiteRotateMin: float = ParamField(
        float, "LimiteRotateMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LimiteRotateMax: float = ParamField(
        float, "LimiteRotateMax", default=180.0,
        tooltip="TOOLTIP-TODO",
    )
