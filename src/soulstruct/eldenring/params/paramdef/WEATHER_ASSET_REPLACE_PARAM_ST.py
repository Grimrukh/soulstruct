from __future__ import annotations

__all__ = ["WEATHER_ASSET_REPLACE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WEATHER_ASSET_REPLACE_PARAM_ST(ParamRow):
    MapId: int = ParamField(
        uint32, "mapId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TransitionSrcWeather: int = ParamField(
        int16, "TransitionSrcWeather", WEATHER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "padding0[2]")
    IsFireAsh: int = ParamField(
        uint8, "isFireAsh", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "padding1[3]")
    Reserved2: int = ParamField(
        uint32, "reserved2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AssetId0: int = ParamField(
        int32, "AssetId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId1: int = ParamField(
        int32, "AssetId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId2: int = ParamField(
        int32, "AssetId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId3: int = ParamField(
        int32, "AssetId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId4: int = ParamField(
        int32, "AssetId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId5: int = ParamField(
        int32, "AssetId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId6: int = ParamField(
        int32, "AssetId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId7: int = ParamField(
        int32, "AssetId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserved0[8]")
    CreateAssetLimitId0: int = ParamField(
        int8, "CreateAssetLimitId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateAssetLimitId1: int = ParamField(
        int8, "CreateAssetLimitId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateAssetLimitId2: int = ParamField(
        int8, "CreateAssetLimitId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateAssetLimitId3: int = ParamField(
        int8, "CreateAssetLimitId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "reserved1[4]")
