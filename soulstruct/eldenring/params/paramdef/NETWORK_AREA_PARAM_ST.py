from __future__ import annotations

__all__ = ["NETWORK_AREA_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NETWORK_AREA_PARAM_ST(ParamRow):
    CellSizeX: float = ParamField(
        float, "cellSizeX", default=30,
        tooltip="TOOLTIP-TODO",
    )
    CellSizeY: float = ParamField(
        float, "cellSizeY", default=8,
        tooltip="TOOLTIP-TODO",
    )
    CellSizeZ: float = ParamField(
        float, "cellSizeZ", default=30,
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
    EnableBloodstain: int = ParamField(
        byte, "enableBloodstain:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodMessage: int = ParamField(
        byte, "enableBloodMessage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableGhost: int = ParamField(
        byte, "enableGhost:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableMultiPlay: int = ParamField(
        byte, "enableMultiPlay:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableRingSearch: int = ParamField(
        byte, "enableRingSearch:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableBreakInSearch: int = ParamField(
        byte, "enableBreakInSearch:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "dummy[3]")
