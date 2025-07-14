from __future__ import annotations

__all__ = ["TUTORIAL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class TUTORIAL_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    MenuType: int = ParamField(
        uint8, "menuType", TUTORIAL_MENU_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TriggerType: int = ParamField(
        uint8, "triggerType", TUTORIAL_TRIGGER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RepeatType: int = ParamField(
        uint8, "repeatType", TUTORIAL_REPEAT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    ImageId: int = ParamField(
        uint16, "imageId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad2[2]")
    UnlockEventFlagId: int = ParamField(
        uint32, "unlockEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId: int = ParamField(
        int32, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DisplayMinTime: float = ParamField(
        float32, "displayMinTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DisplayTime: float = ParamField(
        float32, "displayTime", default=3.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "pad3[4]")
