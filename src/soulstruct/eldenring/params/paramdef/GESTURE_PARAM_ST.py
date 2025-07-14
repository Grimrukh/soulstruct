from __future__ import annotations

__all__ = ["GESTURE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class GESTURE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ItemId: int = ParamField(
        int32, "itemId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsgAnimId: int = ParamField(
        int32, "msgAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CannotUseRiding: bool = ParamField(
        uint8, "cannotUseRiding:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad2:7", bit_count=7)
    _Pad1: bytes = ParamPad(3, "pad1[3]")
