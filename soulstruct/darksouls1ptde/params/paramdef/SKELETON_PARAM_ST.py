from __future__ import annotations

__all__ = ["SKELETON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SKELETON_PARAM_ST(ParamRow):
    neckTurnGain: float = ParamField(
        float, "neckTurnGain", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    originalGroundHeightMS: int = ParamField(
        short, "originalGroundHeightMS", default=0,
        tooltip="TOOLTIP-TODO",
    )
    minAnkleHeightMS: int = ParamField(
        short, "minAnkleHeightMS", default=-30,
        tooltip="TOOLTIP-TODO",
    )
    maxAnkleHeightMS: int = ParamField(
        short, "maxAnkleHeightMS", default=70,
        tooltip="TOOLTIP-TODO",
    )
    cosineMaxKneeAngle: int = ParamField(
        short, "cosineMaxKneeAngle", default=-95,
        tooltip="TOOLTIP-TODO",
    )
    cosineMinKneeAngle: int = ParamField(
        short, "cosineMinKneeAngle", default=55,
        tooltip="TOOLTIP-TODO",
    )
    footPlantedAnkleHeightMS: int = ParamField(
        short, "footPlantedAnkleHeightMS", default=1,
        tooltip="TOOLTIP-TODO",
    )
    footRaisedAnkleHeightMS: int = ParamField(
        short, "footRaisedAnkleHeightMS", default=30,
        tooltip="TOOLTIP-TODO",
    )
    raycastDistanceUp: int = ParamField(
        short, "raycastDistanceUp", default=70,
        tooltip="TOOLTIP-TODO",
    )
    raycastDistanceDown: int = ParamField(
        short, "raycastDistanceDown", default=55,
        tooltip="TOOLTIP-TODO",
    )
    footEndLS_X: int = ParamField(
        short, "footEndLS_X", default=0,
        tooltip="TOOLTIP-TODO",
    )
    footEndLS_Y: int = ParamField(
        short, "footEndLS_Y", default=0,
        tooltip="TOOLTIP-TODO",
    )
    footEndLS_Z: int = ParamField(
        short, "footEndLS_Z", default=0,
        tooltip="TOOLTIP-TODO",
    )
    onOffGain: int = ParamField(
        short, "onOffGain", default=18,
        tooltip="TOOLTIP-TODO",
    )
    groundAscendingGain: int = ParamField(
        short, "groundAscendingGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    groundDescendingGain: int = ParamField(
        short, "groundDescendingGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    footRaisedGain: int = ParamField(
        short, "footRaisedGain", default=20,
        tooltip="TOOLTIP-TODO",
    )
    footPlantedGain: int = ParamField(
        short, "footPlantedGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    footUnlockGain: int = ParamField(
        short, "footUnlockGain", default=80,
        tooltip="TOOLTIP-TODO",
    )
    kneeAxisType: int = ParamField(
        byte, "kneeAxisType", default=4,
        tooltip="TOOLTIP-TODO",
    )
    useFootLocking: int = ParamField(
        byte, "useFootLocking", default=0,
        tooltip="TOOLTIP-TODO",
    )
    footPlacementOn: int = ParamField(
        byte, "footPlacementOn", default=1,
        tooltip="TOOLTIP-TODO",
    )
    twistKneeAxisType: int = ParamField(
        byte, "twistKneeAxisType", default=1,
        tooltip="TOOLTIP-TODO",
    )
    neckTurnPriority: int = ParamField(
        sbyte, "neckTurnPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    neckTurnMaxAngle: int = ParamField(
        byte, "neckTurnMaxAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
