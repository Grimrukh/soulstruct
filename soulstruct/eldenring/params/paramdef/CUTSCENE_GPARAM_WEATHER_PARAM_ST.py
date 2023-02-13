from __future__ import annotations

__all__ = ["CUTSCENE_GPARAM_WEATHER_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CUTSCENE_GPARAM_WEATHER_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: bool = ParamField(
        byte, "disableParam_Debug:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    DstWeatherSunny: int = ParamField(
        short, "DstWeather_Sunny", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherClearSky: int = ParamField(
        short, "DstWeather_ClearSky", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherWeakCloudy: int = ParamField(
        short, "DstWeather_WeakCloudy", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherCloud: int = ParamField(
        short, "DstWeather_Cloud", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherRain: int = ParamField(
        short, "DstWeather_Rain", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyRain: int = ParamField(
        short, "DstWeather_HeavyRain", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherStorm: int = ParamField(
        short, "DstWeather_Storm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherStormForBattle: int = ParamField(
        short, "DstWeather_StormForBattle", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherSnow: int = ParamField(
        short, "DstWeather_Snow", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavySnow: int = ParamField(
        short, "DstWeather_HeavySnow", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherFog: int = ParamField(
        short, "DstWeather_Fog", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyFog: int = ParamField(
        short, "DstWeather_HeavyFog", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherSandStorm: int = ParamField(
        short, "DstWeather_SandStorm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyFogRain: int = ParamField(
        short, "DstWeather_HeavyFogRain", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PostPlayIngameWeather: int = ParamField(
        short, "PostPlayIngameWeather", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IndoorOutdoorType: int = ParamField(
        byte, "IndoorOutdoorType", CUTSCENE_INDOOR_OUTDOOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSunny: int = ParamField(
        byte, "TakeOverDstWeather_Sunny", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherClearSky: int = ParamField(
        byte, "TakeOverDstWeather_ClearSky", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherWeakCloudy: int = ParamField(
        byte, "TakeOverDstWeather_WeakCloudy", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherCloud: int = ParamField(
        byte, "TakeOverDstWeather_Cloud", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherRain: int = ParamField(
        byte, "TakeOverDstWeather_Rain", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyRain: int = ParamField(
        byte, "TakeOverDstWeather_HeavyRain", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherStorm: int = ParamField(
        byte, "TakeOverDstWeather_Storm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherStormForBattle: int = ParamField(
        byte, "TakeOverDstWeather_StormForBattle", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSnow: int = ParamField(
        byte, "TakeOverDstWeather_Snow", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavySnow: int = ParamField(
        byte, "TakeOverDstWeather_HeavySnow", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherFog: int = ParamField(
        byte, "TakeOverDstWeather_Fog", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyFog: int = ParamField(
        byte, "TakeOverDstWeather_HeavyFog", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSandStorm: int = ParamField(
        byte, "TakeOverDstWeather_SandStorm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyFogRain: int = ParamField(
        byte, "TakeOverDstWeather_HeavyFogRain", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(7, "reserved[7]")
    DstWeatherSnowstorm: int = ParamField(
        short, "DstWeather_Snowstorm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherLightningStorm: int = ParamField(
        short, "DstWeather_LightningStorm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved3: int = ParamField(
        short, "DstWeather_Reserved3", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved4: int = ParamField(
        short, "DstWeather_Reserved4", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved5: int = ParamField(
        short, "DstWeather_Reserved5", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved6: int = ParamField(
        short, "DstWeather_Reserved6", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved7: int = ParamField(
        short, "DstWeather_Reserved7", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved8: int = ParamField(
        short, "DstWeather_Reserved8", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSnowstorm: int = ParamField(
        byte, "TakeOverDstWeather_Snowstorm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherLightningStorm: int = ParamField(
        byte, "TakeOverDstWeather_LightningStorm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved3: int = ParamField(
        byte, "TakeOverDstWeather_Reserved3", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved4: int = ParamField(
        byte, "TakeOverDstWeather_Reserved4", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved5: int = ParamField(
        byte, "TakeOverDstWeather_Reserved5", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved6: int = ParamField(
        byte, "TakeOverDstWeather_Reserved6", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved7: int = ParamField(
        byte, "TakeOverDstWeather_Reserved7", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved8: int = ParamField(
        byte, "TakeOverDstWeather_Reserved8", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableApplyMapGdRegionIdForGparam: int = ParamField(
        byte, "IsEnableApplyMapGdRegionIdForGparam", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "reserved2[1]")
    OverrideMapGdRegionId: int = ParamField(
        short, "OverrideMapGdRegionId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(12, "reserved1[12]")
