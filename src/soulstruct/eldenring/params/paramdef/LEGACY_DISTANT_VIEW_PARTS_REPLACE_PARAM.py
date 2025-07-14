from __future__ import annotations

__all__ = ["LEGACY_DISTANT_VIEW_PARTS_REPLACE_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LEGACY_DISTANT_VIEW_PARTS_REPLACE_PARAM(ParamRow):
    TargetMapId: int = ParamField(
        int32, "TargetMapId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TargetEventId: int = ParamField(
        uint32, "TargetEventId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetId: int = ParamField(
        int32, "SrcAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetPartsNo: int = ParamField(
        int32, "SrcAssetPartsNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetId: int = ParamField(
        int32, "DstAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetPartsNo: int = ParamField(
        int32, "DstAssetPartsNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetIdRangeMin: int = ParamField(
        int32, "SrcAssetIdRangeMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SrcAssetIdRangeMax: int = ParamField(
        int32, "SrcAssetIdRangeMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetIdRangeMin: int = ParamField(
        int32, "DstAssetIdRangeMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DstAssetIdRangeMax: int = ParamField(
        int32, "DstAssetIdRangeMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId0: int = ParamField(
        int8, "LimitedMapRegionId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId1: int = ParamField(
        int8, "LimitedMapRegionId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId2: int = ParamField(
        int8, "LimitedMapRegionId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegionId3: int = ParamField(
        int8, "LimitedMapRegionId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserve[4]")
    LimitedMapRegionAssetId: int = ParamField(
        int32, "LimitedMapRegionAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegioAssetPartsNo: int = ParamField(
        int32, "LimitedMapRegioAssetPartsNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegioAssetIdRangeMin: int = ParamField(
        int32, "LimitedMapRegioAssetIdRangeMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LimitedMapRegioAssetIdRangeMax: int = ParamField(
        int32, "LimitedMapRegioAssetIdRangeMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
