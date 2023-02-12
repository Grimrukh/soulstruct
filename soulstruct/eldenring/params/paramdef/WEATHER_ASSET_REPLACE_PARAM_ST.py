from __future__ import annotations

__all__ = ["WEATHER_ASSET_REPLACE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WEATHER_ASSET_REPLACE_PARAM_ST(ParamRowData):
    MapId: int = ParamField(
        uint, "mapId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TransitionSrcWeather: int = ParamField(
        short, "TransitionSrcWeather", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "padding0[2]")
    IsFireAsh: int = ParamField(
        byte, "isFireAsh", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "padding1[3]")
    Reserved2: int = ParamField(
        uint, "reserved2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AssetId0: int = ParamField(
        int, "AssetId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId1: int = ParamField(
        int, "AssetId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId2: int = ParamField(
        int, "AssetId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId3: int = ParamField(
        int, "AssetId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId4: int = ParamField(
        int, "AssetId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId5: int = ParamField(
        int, "AssetId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId6: int = ParamField(
        int, "AssetId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId7: int = ParamField(
        int, "AssetId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserved0[8]")
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
    _Pad3: bytes = ParamPad(4, "reserved1[4]")
