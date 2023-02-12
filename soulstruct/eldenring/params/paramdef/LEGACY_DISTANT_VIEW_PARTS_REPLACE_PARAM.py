from __future__ import annotations

__all__ = ["LEGACY_DISTANT_VIEW_PARTS_REPLACE_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LEGACY_DISTANT_VIEW_PARTS_REPLACE_PARAM(ParamRowData):
    TargetMapId: int = ParamField(
        int, "TargetMapId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TargetEventId: int = ParamField(
        uint, "TargetEventId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetId: int = ParamField(
        int, "SrcAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetPartsNo: int = ParamField(
        int, "SrcAssetPartsNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetId: int = ParamField(
        int, "DstAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetPartsNo: int = ParamField(
        int, "DstAssetPartsNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetIdRangeMin: int = ParamField(
        int, "SrcAssetIdRangeMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetIdRangeMax: int = ParamField(
        int, "SrcAssetIdRangeMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetIdRangeMin: int = ParamField(
        int, "DstAssetIdRangeMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetIdRangeMax: int = ParamField(
        int, "DstAssetIdRangeMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId0: int = ParamField(
        sbyte, "LimitedMapRegionId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId1: int = ParamField(
        sbyte, "LimitedMapRegionId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId2: int = ParamField(
        sbyte, "LimitedMapRegionId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId3: int = ParamField(
        sbyte, "LimitedMapRegionId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserve[4]")
    LimitedMapRegionAssetId: int = ParamField(
        int, "LimitedMapRegionAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegioAssetPartsNo: int = ParamField(
        int, "LimitedMapRegioAssetPartsNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegioAssetIdRangeMin: int = ParamField(
        int, "LimitedMapRegioAssetIdRangeMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegioAssetIdRangeMax: int = ParamField(
        int, "LimitedMapRegioAssetIdRangeMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
