from __future__ import annotations

__all__ = ["CUTSCENE_GPARAM_WEATHER_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CUTSCENE_GPARAM_WEATHER_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: bool = ParamField(
        uint8, "disableParam_Debug:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    DstWeatherSunny: int = ParamField(
        int16, "DstWeather_Sunny", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherClearSky: int = ParamField(
        int16, "DstWeather_ClearSky", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherWeakCloudy: int = ParamField(
        int16, "DstWeather_WeakCloudy", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherCloud: int = ParamField(
        int16, "DstWeather_Cloud", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherRain: int = ParamField(
        int16, "DstWeather_Rain", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyRain: int = ParamField(
        int16, "DstWeather_HeavyRain", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherStorm: int = ParamField(
        int16, "DstWeather_Storm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherStormForBattle: int = ParamField(
        int16, "DstWeather_StormForBattle", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherSnow: int = ParamField(
        int16, "DstWeather_Snow", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavySnow: int = ParamField(
        int16, "DstWeather_HeavySnow", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherFog: int = ParamField(
        int16, "DstWeather_Fog", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyFog: int = ParamField(
        int16, "DstWeather_HeavyFog", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherSandStorm: int = ParamField(
        int16, "DstWeather_SandStorm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyFogRain: int = ParamField(
        int16, "DstWeather_HeavyFogRain", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PostPlayIngameWeather: int = ParamField(
        int16, "PostPlayIngameWeather", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IndoorOutdoorType: int = ParamField(
        uint8, "IndoorOutdoorType", CUTSCENE_INDOOR_OUTDOOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSunny: int = ParamField(
        uint8, "TakeOverDstWeather_Sunny", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherClearSky: int = ParamField(
        uint8, "TakeOverDstWeather_ClearSky", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherWeakCloudy: int = ParamField(
        uint8, "TakeOverDstWeather_WeakCloudy", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherCloud: int = ParamField(
        uint8, "TakeOverDstWeather_Cloud", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherRain: int = ParamField(
        uint8, "TakeOverDstWeather_Rain", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyRain: int = ParamField(
        uint8, "TakeOverDstWeather_HeavyRain", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherStorm: int = ParamField(
        uint8, "TakeOverDstWeather_Storm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherStormForBattle: int = ParamField(
        uint8, "TakeOverDstWeather_StormForBattle", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSnow: int = ParamField(
        uint8, "TakeOverDstWeather_Snow", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavySnow: int = ParamField(
        uint8, "TakeOverDstWeather_HeavySnow", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherFog: int = ParamField(
        uint8, "TakeOverDstWeather_Fog", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyFog: int = ParamField(
        uint8, "TakeOverDstWeather_HeavyFog", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSandStorm: int = ParamField(
        uint8, "TakeOverDstWeather_SandStorm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyFogRain: int = ParamField(
        uint8, "TakeOverDstWeather_HeavyFogRain", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(7, "reserved[7]")
    DstWeatherSnowstorm: int = ParamField(
        int16, "DstWeather_Snowstorm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherLightningStorm: int = ParamField(
        int16, "DstWeather_LightningStorm", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved3: int = ParamField(
        int16, "DstWeather_Reserved3", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved4: int = ParamField(
        int16, "DstWeather_Reserved4", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved5: int = ParamField(
        int16, "DstWeather_Reserved5", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved6: int = ParamField(
        int16, "DstWeather_Reserved6", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved7: int = ParamField(
        int16, "DstWeather_Reserved7", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved8: int = ParamField(
        int16, "DstWeather_Reserved8", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSnowstorm: int = ParamField(
        uint8, "TakeOverDstWeather_Snowstorm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherLightningStorm: int = ParamField(
        uint8, "TakeOverDstWeather_LightningStorm", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved3: int = ParamField(
        uint8, "TakeOverDstWeather_Reserved3", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved4: int = ParamField(
        uint8, "TakeOverDstWeather_Reserved4", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved5: int = ParamField(
        uint8, "TakeOverDstWeather_Reserved5", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved6: int = ParamField(
        uint8, "TakeOverDstWeather_Reserved6", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved7: int = ParamField(
        uint8, "TakeOverDstWeather_Reserved7", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved8: int = ParamField(
        uint8, "TakeOverDstWeather_Reserved8", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableApplyMapGdRegionIdForGparam: int = ParamField(
        uint8, "IsEnableApplyMapGdRegionIdForGparam", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "reserved2[1]")
    OverrideMapGdRegionId: int = ParamField(
        int16, "OverrideMapGdRegionId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(12, "reserved1[12]")
