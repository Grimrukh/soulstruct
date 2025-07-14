from __future__ import annotations

__all__ = ["KEY_ASSIGN_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class KEY_ASSIGN_PARAM_ST(ParamRow):
    PadKeyId: int = ParamField(
        int32, "padKeyId", CS_PAD_KEY, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    KeyboardModifyKey: int = ParamField(
        int32, "keyboardModifyKey", CS_MODIFIER_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    KeyboardKeyId: int = ParamField(
        int32, "keyboardKeyId", CS_KEYBOARD_KEY, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MouseModifyKey: int = ParamField(
        int32, "mouseModifyKey", CS_MODIFIER_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MouseKeyId: int = ParamField(
        int32, "mouseKeyId", CS_MOUSE_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "reserved[12]")
