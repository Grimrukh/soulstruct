from __future__ import annotations

__all__ = ["PERFORMANCE_CHECK_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class PERFORMANCE_CHECK_PARAM(ParamRow):
    WorkTag: int = ParamField(
        uint8, "workTag", PerformanceCheckParamWork, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CategoryTag: int = ParamField(
        uint8, "categoryTag", PerformanceCheckParamCategory, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CompareType: int = ParamField(
        uint8, "compareType", PerformanceCheckParamCompare, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "dummy1[1]")
    CompareValue: float = ParamField(
        float32, "compareValue", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "dummy2[8]")
    UserTag: str = ParamField(
        str, "userTag[16]", encoding="utf-16", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
