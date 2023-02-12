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
    RegionType: int = ParamField(
        byte, "regionType", ACTION_BUTTON_REGION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding1[3]")
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
    TextBoxType: int = ParamField(
        byte, "textBoxType", ACTION_BUTTON_TEXT_BOX_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(3, "padding3[3]")
    TextId: int = ParamField(
        int, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InvalidFlag: int = ParamField(
        int, "invalidFlag", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GrayoutFlag: int = ParamField(
        int, "grayoutFlag", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Priority: int = ParamField(
        int, "priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExecInvalidTime: float = ParamField(
        float, "execInvalidTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ExecButtonCircle: int = ParamField(
        byte, "execButtonCircle", ACTION_BUTTON_EXEC_CIRCLE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(3, "padding4[3]")
