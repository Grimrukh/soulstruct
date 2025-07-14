from __future__ import annotations

__all__ = ["MENU_VALUE_TABLE_SPEC"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MENU_VALUE_TABLE_SPEC(ParamRow):
    Value: int = ParamField(
        int32, "value", default=0,
        tooltip="TODO",
    )
    TextID: int = ParamField(
        int32, "textId", default=0,
        tooltip="TODO",
    )
    CompareType: int = ParamField(
        int8, "compareType", MENU_VALUE_TABLE_CMP_TYPE, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding[3]")
