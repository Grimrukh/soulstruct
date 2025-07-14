from __future__ import annotations

__all__ = ["FE_TEXT_EFFECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class FE_TEXT_EFFECT_PARAM_ST(ParamRow):
    ResId: int = ParamField(
        int16, "resId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
    TextId: int = ParamField(
        int32, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeId: int = ParamField(
        int32, "seId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CanMixMapName: bool = ParamField(
        uint8, "canMixMapName:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad3:7", bit_count=7)
    _Pad1: bytes = ParamPad(19, "pad2[19]")
