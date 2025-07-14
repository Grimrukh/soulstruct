from __future__ import annotations

__all__ = ["WORLD_MAP_PIECE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WORLD_MAP_PIECE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    OpenEventFlagId: int = ParamField(
        uint32, "openEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaLeft: float = ParamField(
        float32, "openTravelAreaLeft", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaRight: float = ParamField(
        float32, "openTravelAreaRight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaTop: float = ParamField(
        float32, "openTravelAreaTop", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaBottom: float = ParamField(
        float32, "openTravelAreaBottom", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventFlagId: int = ParamField(
        uint32, "acquisitionEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventScale: float = ParamField(
        float32, "acquisitionEventScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventCenterX: float = ParamField(
        float32, "acquisitionEventCenterX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventCenterY: float = ParamField(
        float32, "acquisitionEventCenterY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventResScale: float = ParamField(
        float32, "acquisitionEventResScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventResOffsetX: float = ParamField(
        float32, "acquisitionEventResOffsetX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventResOffsetY: float = ParamField(
        float32, "acquisitionEventResOffsetY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(12, "pad[12]")
