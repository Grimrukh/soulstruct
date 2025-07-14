from __future__ import annotations

__all__ = ["NETWORK_AREA_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NETWORK_AREA_PARAM_ST(ParamRow):
    CellSizeX: float = ParamField(
        float32, "cellSizeX", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    CellSizeY: float = ParamField(
        float32, "cellSizeY", default=8.0,
        tooltip="TOOLTIP-TODO",
    )
    CellSizeZ: float = ParamField(
        float32, "cellSizeZ", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    CellOffsetX: float = ParamField(
        float32, "cellOffsetX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CellOffsetY: float = ParamField(
        float32, "cellOffsetY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CellOffsetZ: float = ParamField(
        float32, "cellOffsetZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodstain: bool = ParamField(
        uint8, "enableBloodstain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodMessage: bool = ParamField(
        uint8, "enableBloodMessage:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableGhost: bool = ParamField(
        uint8, "enableGhost:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableMultiPlay: bool = ParamField(
        uint8, "enableMultiPlay:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableRingSearch: bool = ParamField(
        uint8, "enableRingSearch:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableBreakInSearch: bool = ParamField(
        uint8, "enableBreakInSearch:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "dummy[3]")
