from __future__ import annotations

__all__ = ["ACTIONBUTTON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ACTIONBUTTON_PARAM_ST(ParamRow):
    RegionType: int = ParamField(
        byte, "regionType", ACTION_BUTTON_REGION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Category: int = ParamField(
        byte, "category", ACTION_BUTTON_CATEGORY, default=0,
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
        byte, "angleCheckType", ACTION_BUTTON_ANGLE_CHECK_TYPE, default=0,
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
        byte, "textBoxType", ACTION_BUTTON_TEXT_BOX_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "padding3[2]")
    _BitPad0: int = ParamBitPad(byte, "padding5:1", bit_count=1)
    IsInvalidForRide: bool = ParamField(
        byte, "isInvalidForRide:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutForRide: bool = ParamField(
        byte, "isGrayoutForRide:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInvalidForCrouching: bool = ParamField(
        byte, "isInvalidForCrouching:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutForCrouching: bool = ParamField(
        byte, "isGrayoutForCrouching:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "padding4:3", bit_count=3)
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
    _Pad3: bytes = ParamPad(28, "padding6[28]")
