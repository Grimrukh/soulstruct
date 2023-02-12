from __future__ import annotations

__all__ = ["MAP_DEFAULT_INFO_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MAP_DEFAULT_INFO_PARAM_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    EnableFastTravelEventFlagId: int = ParamField(
        uint, "EnableFastTravelEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotTimeOffsetIngameSeconds: int = ParamField(
        int, "WeatherLotTimeOffsetIngameSeconds", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherCreateAssetLimitId: int = ParamField(
        sbyte, "WeatherCreateAssetLimitId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapAiSightType: int = ParamField(
        byte, "MapAiSightType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoundIndoorType: int = ParamField(
        byte, "SoundIndoorType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReverbDefaultType: int = ParamField(
        sbyte, "ReverbDefaultType", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BgmPlaceInfo: int = ParamField(
        short, "BgmPlaceInfo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnvPlaceInfo: int = ParamField(
        short, "EnvPlaceInfo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapAdditionalSoundBankId: int = ParamField(
        int, "MapAdditionalSoundBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapHeightForSound: int = ParamField(
        short, "MapHeightForSound", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableBlendTimezoneEnvmap: int = ParamField(
        byte, "IsEnableBlendTimezoneEnvmap", default=1,
        tooltip="TOOLTIP-TODO",
    )
    OverrideGIResolutionXSS: int = ParamField(
        sbyte, "OverrideGIResolution_XSS", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangeBorderDistXZ: float = ParamField(
        float, "MapLoHiChangeBorderDist_XZ", default=40,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangeBorderDistY: float = ParamField(
        float, "MapLoHiChangeBorderDist_Y", default=40,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangePlayDist: float = ParamField(
        float, "MapLoHiChangePlayDist", default=5,
        tooltip="TOOLTIP-TODO",
    )
    MapAutoDrawGroupBackFacePixelNum: int = ParamField(
        uint, "MapAutoDrawGroupBackFacePixelNum", default=32400,
        tooltip="TOOLTIP-TODO",
    )
    PlayerLigntScale: float = ParamField(
        float, "PlayerLigntScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableTimezonnePlayerLigntScale: int = ParamField(
        byte, "IsEnableTimezonnePlayerLigntScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableAutoCliffWind: int = ParamField(
        byte, "isDisableAutoCliffWind", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpenChrActivateThreshold: int = ParamField(
        short, "OpenChrActivateThreshold", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapMimicryEstablishmentParamId: int = ParamField(
        int, "MapMimicryEstablishmentParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverrideGIResolutionXSX: int = ParamField(
        sbyte, "OverrideGIResolution_XSX", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(7, "Reserve[7]")
