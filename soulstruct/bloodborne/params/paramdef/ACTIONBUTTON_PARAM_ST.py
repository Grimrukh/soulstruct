from __future__ import annotations

__all__ = ["ACTIONBUTTON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ACTIONBUTTON_PARAM_ST(ParamRow):
    RegionType: ACTION_BUTTON_REGION_TYPE = ParamField(
        byte, "regionType", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding1[3]")
    DummyPoly1: int = ParamField(
        int, "dummyPoly1", default=-1,
        tooltip="TODO",
    )
    DummyPoly2: int = ParamField(
        int, "dummyPoly2", default=-1,
        tooltip="TODO",
    )
    Radius: float = ParamField(
        float, "radius", default=0.0,
        tooltip="TODO",
    )
    Angle: int = ParamField(
        int, "angle", default=180,
        tooltip="TODO",
    )
    Depth: float = ParamField(
        float, "depth", default=0.0,
        tooltip="TODO",
    )
    Width: float = ParamField(
        float, "width", default=0.0,
        tooltip="TODO",
    )
    Height: float = ParamField(
        float, "height", default=0.0,
        tooltip="TODO",
    )
    BottomHeightOffset: float = ParamField(
        float, "baseHeightOffset", default=0.0,
        tooltip="TODO",
    )
    AngleDifferenceCheckType: int = ParamField(
        byte, "angleCheckType", default=0,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(3, "padding2[3]")
    AllowableAngleDifference: int = ParamField(
        int, "allowAngle", default=180,
        tooltip="TODO",
    )
    TextboxType: int = ParamField(
        byte, "textBoxType", default=0,
        tooltip="TODO",
    )
    _Pad2: bytes = ParamPad(3, "padding3[3]")
    TextID: int = ParamField(
        int, "textId", default=-1,
        tooltip="TODO",
    )
    InvalidFlag: int = ParamField(
        int, "invalidFlag", default=-1,
        tooltip="TODO",
    )
    GrayoutFlag: int = ParamField(
        int, "grayoutFlag", default=-1,
        tooltip="TODO",
    )
    Priority: int = ParamField(
        int, "priority", default=0,
        tooltip="TODO",
    )
    ExecutionInvalidTime: float = ParamField(
        float, "execInvalidTime", default=0.0,
        tooltip="TODO",
    )
    ExecutionButtonCircle: int = ParamField(
        byte, "execButtonCircle", default=0,
        tooltip="TODO",
    )
    _Pad3: bytes = ParamPad(3, "padding4[3]")
