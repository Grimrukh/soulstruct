from __future__ import annotations

__all__ = ["WORLD_MAP_PIECE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WORLD_MAP_PIECE_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    OpenEventFlagId: int = ParamField(
        uint, "openEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaLeft: float = ParamField(
        float, "openTravelAreaLeft", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaRight: float = ParamField(
        float, "openTravelAreaRight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaTop: float = ParamField(
        float, "openTravelAreaTop", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OpenTravelAreaBottom: float = ParamField(
        float, "openTravelAreaBottom", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventFlagId: int = ParamField(
        uint, "acquisitionEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventScale: float = ParamField(
        float, "acquisitionEventScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventCenterX: float = ParamField(
        float, "acquisitionEventCenterX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventCenterY: float = ParamField(
        float, "acquisitionEventCenterY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventResScale: float = ParamField(
        float, "acquisitionEventResScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventResOffsetX: float = ParamField(
        float, "acquisitionEventResOffsetX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AcquisitionEventResOffsetY: float = ParamField(
        float, "acquisitionEventResOffsetY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(12, "pad[12]")
