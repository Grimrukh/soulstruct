from __future__ import annotations

__all__ = ["NETWORK_AREA_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NETWORK_AREA_PARAM_ST(ParamRow):
    CellSizeX: float = ParamField(
        float, "cellSizeX", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    CellSizeY: float = ParamField(
        float, "cellSizeY", default=8.0,
        tooltip="TOOLTIP-TODO",
    )
    CellSizeZ: float = ParamField(
        float, "cellSizeZ", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    CellOffsetX: float = ParamField(
        float, "cellOffsetX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CellOffsetY: float = ParamField(
        float, "cellOffsetY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CellOffsetZ: float = ParamField(
        float, "cellOffsetZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodstain: bool = ParamField(
        byte, "enableBloodstain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodMessage: bool = ParamField(
        byte, "enableBloodMessage:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableGhost: bool = ParamField(
        byte, "enableGhost:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableMultiPlay: bool = ParamField(
        byte, "enableMultiPlay:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableRingSearch: bool = ParamField(
        byte, "enableRingSearch:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableBreakInSearch: bool = ParamField(
        byte, "enableBreakInSearch:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "dummy[3]")
