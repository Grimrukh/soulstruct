from __future__ import annotations

__all__ = ["MAP_DEFAULT_INFO_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAP_DEFAULT_INFO_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    EnableFastTravelEventFlagId: int = ParamField(
        uint32, "EnableFastTravelEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotTimeOffsetIngameSeconds: int = ParamField(
        int32, "WeatherLotTimeOffsetIngameSeconds", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherCreateAssetLimitId: int = ParamField(
        int8, "WeatherCreateAssetLimitId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapAiSightType: int = ParamField(
        uint8, "MapAiSightType", MAP_AI_SIGHT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoundIndoorType: int = ParamField(
        uint8, "SoundIndoorType", SOUND_INDOOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReverbDefaultType: int = ParamField(
        int8, "ReverbDefaultType", SOUND_MAP_DEFAULT_REVERB_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BgmPlaceInfo: int = ParamField(
        int16, "BgmPlaceInfo", SOUND_BGM_MAP_PLACE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnvPlaceInfo: int = ParamField(
        int16, "EnvPlaceInfo", SOUND_ENV_MAP_PLACE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapAdditionalSoundBankId: int = ParamField(
        int32, "MapAdditionalSoundBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapHeightForSound: int = ParamField(
        int16, "MapHeightForSound", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableBlendTimezoneEnvmap: int = ParamField(
        uint8, "IsEnableBlendTimezoneEnvmap", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    OverrideGIResolutionXSS: int = ParamField(
        int8, "OverrideGIResolution_XSS", MAP_GI_RESOLUTION_OVERRIDE_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangeBorderDistXZ: float = ParamField(
        float32, "MapLoHiChangeBorderDist_XZ", default=40.0,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangeBorderDistY: float = ParamField(
        float32, "MapLoHiChangeBorderDist_Y", default=40.0,
        tooltip="TOOLTIP-TODO",
    )
    MapLoHiChangePlayDist: float = ParamField(
        float32, "MapLoHiChangePlayDist", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    MapAutoDrawGroupBackFacePixelNum: int = ParamField(
        uint32, "MapAutoDrawGroupBackFacePixelNum", default=32400,
        tooltip="TOOLTIP-TODO",
    )
    PlayerLigntScale: float = ParamField(
        float32, "PlayerLigntScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableTimezonnePlayerLigntScale: int = ParamField(
        uint8, "IsEnableTimezonnePlayerLigntScale", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableAutoCliffWind: int = ParamField(
        uint8, "isDisableAutoCliffWind", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpenChrActivateThreshold: int = ParamField(
        int16, "OpenChrActivateThreshold", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MapMimicryEstablishmentParamId: int = ParamField(
        int32, "MapMimicryEstablishmentParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverrideGIResolutionXSX: int = ParamField(
        int8, "OverrideGIResolution_XSX", MAP_GI_RESOLUTION_OVERRIDE_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(7, "Reserve[7]")
