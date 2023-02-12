from __future__ import annotations

__all__ = ["MENU_VALUE_TABLE_SPEC"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENU_VALUE_TABLE_SPEC(ParamRow):
    Value: float = ParamField(
        float, "value", default=0.0,
        tooltip="TODO",
    )
    TextID: int = ParamField(
        int, "textId", default=0,
        tooltip="TODO",
    )
    CompareType: MENU_VALUE_TABLE_CMP_TYPE = ParamField(
        sbyte, "compareType", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding[3]")
