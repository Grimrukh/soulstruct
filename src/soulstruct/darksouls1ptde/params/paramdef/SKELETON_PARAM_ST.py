from __future__ import annotations

__all__ = ["SKELETON_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class SKELETON_PARAM_ST(ParamRow):
    NeckTurnGain: float = ParamField(
        float32, "neckTurnGain", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OriginalGroundHeightMS: int = ParamField(
        int16, "originalGroundHeightMS", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MinAnkleHeightMS: int = ParamField(
        int16, "minAnkleHeightMS", default=-30,
        tooltip="TOOLTIP-TODO",
    )
    MaxAnkleHeightMS: int = ParamField(
        int16, "maxAnkleHeightMS", default=70,
        tooltip="TOOLTIP-TODO",
    )
    CosineMaxKneeAngle: int = ParamField(
        int16, "cosineMaxKneeAngle", default=-95,
        tooltip="TOOLTIP-TODO",
    )
    CosineMinKneeAngle: int = ParamField(
        int16, "cosineMinKneeAngle", default=55,
        tooltip="TOOLTIP-TODO",
    )
    FootPlantedAnkleHeightMS: int = ParamField(
        int16, "footPlantedAnkleHeightMS", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FootRaisedAnkleHeightMS: int = ParamField(
        int16, "footRaisedAnkleHeightMS", default=30,
        tooltip="TOOLTIP-TODO",
    )
    RaycastDistanceUp: int = ParamField(
        int16, "raycastDistanceUp", default=70,
        tooltip="TOOLTIP-TODO",
    )
    RaycastDistanceDown: int = ParamField(
        int16, "raycastDistanceDown", default=55,
        tooltip="TOOLTIP-TODO",
    )
    FootEndLSX: int = ParamField(
        int16, "footEndLS_X", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootEndLSY: int = ParamField(
        int16, "footEndLS_Y", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootEndLSZ: int = ParamField(
        int16, "footEndLS_Z", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OnOffGain: int = ParamField(
        int16, "onOffGain", default=18,
        tooltip="TOOLTIP-TODO",
    )
    GroundAscendingGain: int = ParamField(
        int16, "groundAscendingGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    GroundDescendingGain: int = ParamField(
        int16, "groundDescendingGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    FootRaisedGain: int = ParamField(
        int16, "footRaisedGain", default=20,
        tooltip="TOOLTIP-TODO",
    )
    FootPlantedGain: int = ParamField(
        int16, "footPlantedGain", default=100,
        tooltip="TOOLTIP-TODO",
    )
    FootUnlockGain: int = ParamField(
        int16, "footUnlockGain", default=80,
        tooltip="TOOLTIP-TODO",
    )
    KneeAxisType: int = ParamField(
        uint8, "kneeAxisType", SKELETON_PARAM_KNEE_AXIS_DIR, default=4,
        tooltip="TOOLTIP-TODO",
    )
    UseFootLocking: int = ParamField(
        uint8, "useFootLocking", RAGDOLL_PARAM_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootPlacementOn: int = ParamField(
        uint8, "footPlacementOn", RAGDOLL_PARAM_BOOL, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TwistKneeAxisType: int = ParamField(
        uint8, "twistKneeAxisType", SKELETON_PARAM_KNEE_AXIS_DIR, default=1,
        tooltip="TOOLTIP-TODO",
    )
    NeckTurnPriority: int = ParamField(
        int8, "neckTurnPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeckTurnMaxAngle: int = ParamField(
        uint8, "neckTurnMaxAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
