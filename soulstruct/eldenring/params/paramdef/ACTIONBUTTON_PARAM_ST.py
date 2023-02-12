from __future__ import annotations

__all__ = ["ACTIONBUTTON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ACTIONBUTTON_PARAM_ST(ParamRowData):
    RegionType: int = ParamField(
        byte, "regionType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Category: int = ParamField(
        byte, "category", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "padding1[2]")
    DummyPoly1: int = ParamField(
        int, "dummyPoly1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DummyPoly2: int = ParamField(
        int, "dummyPoly2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Radius: float = ParamField(
        float, "radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Angle: int = ParamField(
        int, "angle", default=180,
        tooltip="TOOLTIP-TODO",
    )
    Depth: float = ParamField(
        float, "depth", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Width: float = ParamField(
        float, "width", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Height: float = ParamField(
        float, "height", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseHeightOffset: float = ParamField(
        float, "baseHeightOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AngleCheckType: int = ParamField(
        byte, "angleCheckType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "padding2[3]")
    AllowAngle: int = ParamField(
        int, "allowAngle", default=180,
        tooltip="TOOLTIP-TODO",
    )
    SpotDummyPoly: int = ParamField(
        int, "spotDummyPoly", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextBoxType: int = ParamField(
        byte, "textBoxType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "padding3[2]")
    _Pad3: bytes = ParamPad(1, "padding5:1")
    IsInvalidForRide: int = ParamField(
        byte, "isInvalidForRide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutForRide: int = ParamField(
        byte, "isGrayoutForRide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsInvalidForCrouching: int = ParamField(
        byte, "isInvalidForCrouching:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutForCrouching: int = ParamField(
        byte, "isGrayoutForCrouching:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(1, "padding4:3")
    TextId: int = ParamField(
        int, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InvalidFlag: int = ParamField(
        uint, "invalidFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GrayoutFlag: int = ParamField(
        uint, "grayoutFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideActionButtonIdForRide: int = ParamField(
        int, "overrideActionButtonIdForRide", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ExecInvalidTime: float = ParamField(
        float, "execInvalidTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(28, "padding6[28]")
