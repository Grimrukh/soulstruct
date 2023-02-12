from __future__ import annotations

__all__ = ["CUTSCENE_GPARAM_WEATHER_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CUTSCENE_GPARAM_WEATHER_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: int = ParamField(
        byte, "disableParam_Debug:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:6")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    DstWeatherSunny: int = ParamField(
        short, "DstWeather_Sunny", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherClearSky: int = ParamField(
        short, "DstWeather_ClearSky", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherWeakCloudy: int = ParamField(
        short, "DstWeather_WeakCloudy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherCloud: int = ParamField(
        short, "DstWeather_Cloud", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherRain: int = ParamField(
        short, "DstWeather_Rain", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyRain: int = ParamField(
        short, "DstWeather_HeavyRain", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherStorm: int = ParamField(
        short, "DstWeather_Storm", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherStormForBattle: int = ParamField(
        short, "DstWeather_StormForBattle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherSnow: int = ParamField(
        short, "DstWeather_Snow", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavySnow: int = ParamField(
        short, "DstWeather_HeavySnow", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherFog: int = ParamField(
        short, "DstWeather_Fog", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyFog: int = ParamField(
        short, "DstWeather_HeavyFog", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherSandStorm: int = ParamField(
        short, "DstWeather_SandStorm", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherHeavyFogRain: int = ParamField(
        short, "DstWeather_HeavyFogRain", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PostPlayIngameWeather: int = ParamField(
        short, "PostPlayIngameWeather", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IndoorOutdoorType: int = ParamField(
        byte, "IndoorOutdoorType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSunny: int = ParamField(
        byte, "TakeOverDstWeather_Sunny", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherClearSky: int = ParamField(
        byte, "TakeOverDstWeather_ClearSky", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherWeakCloudy: int = ParamField(
        byte, "TakeOverDstWeather_WeakCloudy", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherCloud: int = ParamField(
        byte, "TakeOverDstWeather_Cloud", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherRain: int = ParamField(
        byte, "TakeOverDstWeather_Rain", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyRain: int = ParamField(
        byte, "TakeOverDstWeather_HeavyRain", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherStorm: int = ParamField(
        byte, "TakeOverDstWeather_Storm", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherStormForBattle: int = ParamField(
        byte, "TakeOverDstWeather_StormForBattle", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSnow: int = ParamField(
        byte, "TakeOverDstWeather_Snow", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavySnow: int = ParamField(
        byte, "TakeOverDstWeather_HeavySnow", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherFog: int = ParamField(
        byte, "TakeOverDstWeather_Fog", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyFog: int = ParamField(
        byte, "TakeOverDstWeather_HeavyFog", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSandStorm: int = ParamField(
        byte, "TakeOverDstWeather_SandStorm", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherHeavyFogRain: int = ParamField(
        byte, "TakeOverDstWeather_HeavyFogRain", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(7, "reserved[7]")
    DstWeatherSnowstorm: int = ParamField(
        short, "DstWeather_Snowstorm", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherLightningStorm: int = ParamField(
        short, "DstWeather_LightningStorm", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved3: int = ParamField(
        short, "DstWeather_Reserved3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved4: int = ParamField(
        short, "DstWeather_Reserved4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved5: int = ParamField(
        short, "DstWeather_Reserved5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved6: int = ParamField(
        short, "DstWeather_Reserved6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved7: int = ParamField(
        short, "DstWeather_Reserved7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstWeatherReserved8: int = ParamField(
        short, "DstWeather_Reserved8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherSnowstorm: int = ParamField(
        byte, "TakeOverDstWeather_Snowstorm", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherLightningStorm: int = ParamField(
        byte, "TakeOverDstWeather_LightningStorm", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved3: int = ParamField(
        byte, "TakeOverDstWeather_Reserved3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved4: int = ParamField(
        byte, "TakeOverDstWeather_Reserved4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved5: int = ParamField(
        byte, "TakeOverDstWeather_Reserved5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved6: int = ParamField(
        byte, "TakeOverDstWeather_Reserved6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved7: int = ParamField(
        byte, "TakeOverDstWeather_Reserved7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TakeOverDstWeatherReserved8: int = ParamField(
        byte, "TakeOverDstWeather_Reserved8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableApplyMapGdRegionIdForGparam: int = ParamField(
        byte, "IsEnableApplyMapGdRegionIdForGparam", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "reserved2[1]")
    OverrideMapGdRegionId: int = ParamField(
        short, "OverrideMapGdRegionId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(12, "reserved1[12]")
