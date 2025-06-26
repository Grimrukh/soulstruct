from __future__ import annotations

__all__ = ["MENU_VALUE_TABLE_SPEC"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MENU_VALUE_TABLE_SPEC(ParamRow):
    Value: int = ParamField(
        int, "value", default=0,
        tooltip="TODO",
    )
    TextID: int = ParamField(
        int, "textId", default=0,
        tooltip="TODO",
    )
    CompareType: int = ParamField(
        sbyte, "compareType", MENU_VALUE_TABLE_CMP_TYPE, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding[3]")
