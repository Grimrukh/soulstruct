from __future__ import annotations

__all__ = ["BASECHR_SELECT_MENU_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class BASECHR_SELECT_MENU_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ChrInitParam: int = ParamField(
        uint32, "chrInitParam", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OriginChrInitParam: int = ParamField(
        uint32, "originChrInitParam", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ImageId: int = ParamField(
        int32, "imageId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId: int = ParamField(
        int32, "textId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(12, "reserve[12]")
