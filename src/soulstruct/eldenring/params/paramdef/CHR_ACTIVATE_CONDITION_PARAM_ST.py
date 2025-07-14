from __future__ import annotations

__all__ = ["CHR_ACTIVATE_CONDITION_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CHR_ACTIVATE_CONDITION_PARAM_ST(ParamRow):
    WeatherSunny: bool = ParamField(
        uint8, "weatherSunny:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherClearSky: bool = ParamField(
        uint8, "weatherClearSky:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherWeakCloudy: bool = ParamField(
        uint8, "weatherWeakCloudy:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherCloudy: bool = ParamField(
        uint8, "weatherCloudy:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherRain: bool = ParamField(
        uint8, "weatherRain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyRain: bool = ParamField(
        uint8, "weatherHeavyRain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherStorm: bool = ParamField(
        uint8, "weatherStorm:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherStormForBattle: bool = ParamField(
        uint8, "weatherStormForBattle:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherSnow: bool = ParamField(
        uint8, "weatherSnow:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavySnow: bool = ParamField(
        uint8, "weatherHeavySnow:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherFog: bool = ParamField(
        uint8, "weatherFog:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyFog: bool = ParamField(
        uint8, "weatherHeavyFog:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherHeavyFogRain: bool = ParamField(
        uint8, "weatherHeavyFogRain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WeatherSandStorm: bool = ParamField(
        uint8, "weatherSandStorm:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad1:2", bit_count=2)
    TimeStartHour: int = ParamField(
        uint8, "timeStartHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimeStartMin: int = ParamField(
        uint8, "timeStartMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimeEndHour: int = ParamField(
        uint8, "timeEndHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimeEndMin: int = ParamField(
        uint8, "timeEndMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad2[2]")
