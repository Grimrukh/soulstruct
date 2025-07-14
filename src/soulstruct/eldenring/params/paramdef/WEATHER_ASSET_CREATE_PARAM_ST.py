from __future__ import annotations

__all__ = ["WEATHER_ASSET_CREATE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WEATHER_ASSET_CREATE_PARAM_ST(ParamRow):
    AssetId: int = ParamField(
        uint, "AssetId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlotNo: int = ParamField(
        uint, "SlotNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateConditionType: int = ParamField(
        byte, "CreateConditionType", WEATHER_ASSET_CREATE_CONDITION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding0[3]")
    TransitionSrcWeather: int = ParamField(
        short, "TransitionSrcWeather", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TransitionDstWeather: int = ParamField(
        short, "TransitionDstWeather", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ElapsedTimeCheckweather: int = ParamField(
        short, "ElapsedTimeCheckweather", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "padding1[2]")
    ElapsedTime: float = ParamField(
        float, "ElapsedTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CreateDelayTime: float = ParamField(
        float, "CreateDelayTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    CreateProbability: int = ParamField(
        uint, "CreateProbability", default=100,
        tooltip="TOOLTIP-TODO",
    )
    LifeTime: float = ParamField(
        float, "LifeTime", default=600.0,
        tooltip="TOOLTIP-TODO",
    )
    FadeTime: float = ParamField(
        float, "FadeTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableCreateTimeMin: float = ParamField(
        float, "EnableCreateTimeMin", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableCreateTimeMax: float = ParamField(
        float, "EnableCreateTimeMax", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    CreatePoint0: int = ParamField(
        short, "CreatePoint0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreatePoint1: int = ParamField(
        short, "CreatePoint1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreatePoint2: int = ParamField(
        short, "CreatePoint2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreatePoint3: int = ParamField(
        short, "CreatePoint3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateAssetLimitId0: int = ParamField(
        sbyte, "CreateAssetLimitId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateAssetLimitId1: int = ParamField(
        sbyte, "CreateAssetLimitId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateAssetLimitId2: int = ParamField(
        sbyte, "CreateAssetLimitId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateAssetLimitId3: int = ParamField(
        sbyte, "CreateAssetLimitId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(4, "Reserved2[4]")
