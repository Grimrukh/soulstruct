from __future__ import annotations

__all__ = ["TUTORIAL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class TUTORIAL_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    MenuType: int = ParamField(
        byte, "menuType", TUTORIAL_MENU_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TriggerType: int = ParamField(
        byte, "triggerType", TUTORIAL_TRIGGER_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RepeatType: int = ParamField(
        byte, "repeatType", TUTORIAL_REPEAT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    ImageId: int = ParamField(
        ushort, "imageId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad2[2]")
    UnlockEventFlagId: int = ParamField(
        uint, "unlockEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId: int = ParamField(
        int, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DisplayMinTime: float = ParamField(
        float, "displayMinTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DisplayTime: float = ParamField(
        float, "displayTime", default=3.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "pad3[4]")
