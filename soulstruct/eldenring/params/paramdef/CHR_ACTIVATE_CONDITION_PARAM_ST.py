from __future__ import annotations

__all__ = ["CHR_ACTIVATE_CONDITION_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHR_ACTIVATE_CONDITION_PARAM_ST(ParamRow):
    WeatherSunny: bool = ParamField(
        byte, "weatherSunny:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherClearSky: bool = ParamField(
        byte, "weatherClearSky:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherWeakCloudy: bool = ParamField(
        byte, "weatherWeakCloudy:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherCloudy: bool = ParamField(
        byte, "weatherCloudy:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherRain: bool = ParamField(
        byte, "weatherRain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyRain: bool = ParamField(
        byte, "weatherHeavyRain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherStorm: bool = ParamField(
        byte, "weatherStorm:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherStormForBattle: bool = ParamField(
        byte, "weatherStormForBattle:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherSnow: bool = ParamField(
        byte, "weatherSnow:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavySnow: bool = ParamField(
        byte, "weatherHeavySnow:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherFog: bool = ParamField(
        byte, "weatherFog:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyFog: bool = ParamField(
        byte, "weatherHeavyFog:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyFogRain: bool = ParamField(
        byte, "weatherHeavyFogRain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherSandStorm: bool = ParamField(
        byte, "weatherSandStorm:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad1:2", bit_count=2)
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
    _Pad0: bytes = ParamPad(2, "pad2[2]")
