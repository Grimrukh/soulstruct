from __future__ import annotations

__all__ = ["MENU_VALUE_TABLE_SPEC"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENU_VALUE_TABLE_SPEC(ParamRow):
    Value: int = ParamField(
        int, "value", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextID: int = ParamField(
        int, "textId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CompareType: int = ParamField(
        sbyte, "compareType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "padding[3]")
