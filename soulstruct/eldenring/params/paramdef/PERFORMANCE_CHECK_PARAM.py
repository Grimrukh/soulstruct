from __future__ import annotations

__all__ = ["PERFORMANCE_CHECK_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class PERFORMANCE_CHECK_PARAM(ParamRowData):
    WorkTag: int = ParamField(
        byte, "workTag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CategoryTag: int = ParamField(
        byte, "categoryTag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CompareType: int = ParamField(
        byte, "compareType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "dummy1[1]")
    CompareValue: float = ParamField(
        float, "compareValue", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "dummy2[8]")
    UserTag: bytes = ParamField(
        bytes, "userTag[16]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
