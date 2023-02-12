from __future__ import annotations

__all__ = ["KNOWLEDGE_LOADSCREEN_ITEM_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class KNOWLEDGE_LOADSCREEN_ITEM_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    UnlockFlagId: int = ParamField(
        uint, "unlockFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvalidFlagId: int = ParamField(
        uint, "invalidFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsgId: int = ParamField(
        int, "msgId", default=0,
        tooltip="TOOLTIP-TODO",
    )
