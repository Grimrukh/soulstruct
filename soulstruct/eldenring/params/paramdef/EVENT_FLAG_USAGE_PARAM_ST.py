from __future__ import annotations

__all__ = ["EVENT_FLAG_USAGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EVENT_FLAG_USAGE_PARAM_ST(ParamRowData):
    UsageType: int = ParamField(
        byte, "usageType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlaylogCategory: int = ParamField(
        byte, "playlogCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "padding1[2]")
    FlagNum: int = ParamField(
        int, "flagNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "padding2[24]")
