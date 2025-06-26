from __future__ import annotations

__all__ = ["MAP_DEFAULT_INFO_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAP_DEFAULT_INFO_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
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
        byte, "MapAiSightType", MAP_AI_SIGHT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoundIndoorType: int = ParamField(
        byte, "SoundIndoorType", SOUND_INDOOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReverbDefaultType: int = ParamField(
        sbyte, "ReverbDefaultType", SOUND_MAP_DEFAULT_REVERB_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BgmPlaceInfo: int = ParamField(
        short, "BgmPlaceInfo", SOUND_BGM_MAP_PLACE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnvPlaceInfo: int = ParamField(
        short, "EnvPlaceInfo", SOUND_ENV_MAP_PLACE_TYPE, default=0,
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
        byte, "IsEnableBlendTimezoneEnvmap", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    OverrideGIResolutionXSS: int = ParamField(
        sbyte, "OverrideGIResolution_XSS", MAP_GI_RESOLUTION_OVERRIDE_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangeBorderDistXZ: float = ParamField(
        float, "MapLoHiChangeBorderDist_XZ", default=40.0,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangeBorderDistY: float = ParamField(
        float, "MapLoHiChangeBorderDist_Y", default=40.0,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangePlayDist: float = ParamField(
        float, "MapLoHiChangePlayDist", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    MapAutoDrawGroupBackFacePixelNum: int = ParamField(
        uint, "MapAutoDrawGroupBackFacePixelNum", default=32400,
        tooltip="TOOLTIP-TODO",
    )
    PlayerLigntScale: float = ParamField(
        float, "PlayerLigntScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableTimezonnePlayerLigntScale: int = ParamField(
        byte, "IsEnableTimezonnePlayerLigntScale", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableAutoCliffWind: int = ParamField(
        byte, "isDisableAutoCliffWind", BOOL_CIRCLECROSS_TYPE, default=0,
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
        sbyte, "OverrideGIResolution_XSX", MAP_GI_RESOLUTION_OVERRIDE_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(7, "Reserve[7]")
