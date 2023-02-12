from __future__ import annotations

__all__ = ["CHR_ACTIVATE_CONDITION_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHR_ACTIVATE_CONDITION_PARAM_ST(ParamRowData):
    WeatherSunny: int = ParamField(
        byte, "weatherSunny:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherClearSky: int = ParamField(
        byte, "weatherClearSky:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherWeakCloudy: int = ParamField(
        byte, "weatherWeakCloudy:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherCloudy: int = ParamField(
        byte, "weatherCloudy:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherRain: int = ParamField(
        byte, "weatherRain:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyRain: int = ParamField(
        byte, "weatherHeavyRain:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherStorm: int = ParamField(
        byte, "weatherStorm:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherStormForBattle: int = ParamField(
        byte, "weatherStormForBattle:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherSnow: int = ParamField(
        byte, "weatherSnow:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavySnow: int = ParamField(
        byte, "weatherHeavySnow:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherFog: int = ParamField(
        byte, "weatherFog:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyFog: int = ParamField(
        byte, "weatherHeavyFog:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyFogRain: int = ParamField(
        byte, "weatherHeavyFogRain:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherSandStorm: int = ParamField(
        byte, "weatherSandStorm:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad1:2")
    TimeStartHour: int = ParamField(
        byte, "timeStartHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimeStartMin: int = ParamField(
        byte, "timeStartMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimeEndHour: int = ParamField(
        byte, "timeEndHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimeEndMin: int = ParamField(
        byte, "timeEndMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad2[2]")
