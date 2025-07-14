from __future__ import annotations

__all__ = ["ACTIONBUTTON_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class ACTIONBUTTON_PARAM_ST(ParamRow):
    RegionType: int = ParamField(
        uint8, "regionType", ACTION_BUTTON_REGION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding1[3]")
    DummyPoly1: int = ParamField(
        int32, "dummyPoly1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DummyPoly2: int = ParamField(
        int32, "dummyPoly2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Radius: float = ParamField(
        float32, "radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Angle: int = ParamField(
        int32, "angle", default=180,
        tooltip="TOOLTIP-TODO",
    )
    Depth: float = ParamField(
        float32, "depth", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Width: float = ParamField(
        float32, "width", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Height: float = ParamField(
        float32, "height", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseHeightOffset: float = ParamField(
        float32, "baseHeightOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AngleCheckType: int = ParamField(
        uint8, "angleCheckType", ACTION_BUTTON_ANGLE_CHECK_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "padding2[3]")
    AllowAngle: int = ParamField(
        int32, "allowAngle", default=180,
        tooltip="TOOLTIP-TODO",
    )
    TextBoxType: int = ParamField(
        uint8, "textBoxType", ACTION_BUTTON_TEXT_BOX_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(3, "padding3[3]")
    TextId: int = ParamField(
        int32, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InvalidFlag: int = ParamField(
        int32, "invalidFlag", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GrayoutFlag: int = ParamField(
        int32, "grayoutFlag", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Priority: int = ParamField(
        int32, "priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExecInvalidTime: float = ParamField(
        float32, "execInvalidTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ExecButtonCircle: int = ParamField(
        uint8, "execButtonCircle", ACTION_BUTTON_EXEC_CIRCLE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(3, "padding4[3]")
