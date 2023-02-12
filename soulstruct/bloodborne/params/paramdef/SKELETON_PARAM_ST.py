from __future__ import annotations

__all__ = ["SKELETON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SKELETON_PARAM_ST(ParamRow):
    NeckTurnGain: float = ParamField(
        float, "neckTurnGain", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OriginalGroundHeightMS: int = ParamField(
        short, "originalGroundHeightMS", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MinAnkleHeightMS: int = ParamField(
        short, "minAnkleHeightMS", default=-30,
        tooltip="TOOLTIP-TODO",
    )
    MaxAnkleHeightMS: int = ParamField(
        short, "maxAnkleHeightMS", default=70,
        tooltip="TOOLTIP-TODO",
    )
    CosineMaxKneeAngle: int = ParamField(
        short, "cosineMaxKneeAngle", default=-95,
        tooltip="TOOLTIP-TODO",
    )
    CosineMinKneeAngle: int = ParamField(
        short, "cosineMinKneeAngle", default=55,
        tooltip="TOOLTIP-TODO",
    )
    FootPlantedAnkleHeightMS: int = ParamField(
        short, "footPlantedAnkleHeightMS", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FootRaisedAnkleHeightMS: int = ParamField(
        short, "footRaisedAnkleHeightMS", default=30,
        tooltip="TOOLTIP-TODO",
    )
    RaycastDistanceUp: int = ParamField(
        short, "raycastDistanceUp", default=70,
        tooltip="TOOLTIP-TODO",
    )
    RaycastDistanceDown: int = ParamField(
        short, "raycastDistanceDown", default=55,
        tooltip="TOOLTIP-TODO",
    )
    FootEndLSX: int = ParamField(
        short, "footEndLS_X", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootEndLSY: int = ParamField(
        short, "footEndLS_Y", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootEndLSZ: int = ParamField(
        short, "footEndLS_Z", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OnOffGain: int = ParamField(
        short, "onOffGain", default=18,
        tooltip="TOOLTIP-TODO",
    )
    GroundAscendingGain: int = ParamField(
        short, "groundAscendingGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    GroundDescendingGain: int = ParamField(
        short, "groundDescendingGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    FootRaisedGain: int = ParamField(
        short, "footRaisedGain", default=20,
        tooltip="TOOLTIP-TODO",
    )
    FootPlantedGain: int = ParamField(
        short, "footPlantedGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    FootUnlockGain: int = ParamField(
        short, "footUnlockGain", default=80,
        tooltip="TOOLTIP-TODO",
    )
    KneeAxisType: int = ParamField(
        byte, "kneeAxisType", SKELETON_PARAM_KNEE_AXIS_DIR, default=4,
        tooltip="TOOLTIP-TODO",
    )
    UseFootLocking: int = ParamField(
        byte, "useFootLocking", RAGDOLL_PARAM_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootPlacementOn: int = ParamField(
        byte, "footPlacementOn", RAGDOLL_PARAM_BOOL, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TwistKneeAxisType: int = ParamField(
        byte, "twistKneeAxisType", SKELETON_PARAM_KNEE_AXIS_DIR, default=1,
        tooltip="TOOLTIP-TODO",
    )
    NeckTurnPriority: int = ParamField(
        sbyte, "neckTurnPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeckTurnMaxAngle: int = ParamField(
        byte, "neckTurnMaxAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
