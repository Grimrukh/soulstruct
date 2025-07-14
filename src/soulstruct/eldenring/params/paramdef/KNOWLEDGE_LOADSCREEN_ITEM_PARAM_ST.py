from __future__ import annotations

__all__ = ["KNOWLEDGE_LOADSCREEN_ITEM_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class KNOWLEDGE_LOADSCREEN_ITEM_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    UnlockFlagId: int = ParamField(
        uint32, "unlockFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvalidFlagId: int = ParamField(
        uint32, "invalidFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsgId: int = ParamField(
        int32, "msgId", default=0,
        tooltip="TOOLTIP-TODO",
    )
