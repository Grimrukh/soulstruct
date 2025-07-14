from __future__ import annotations

__all__ = ["WWISE_VALUE_TO_STR_CONVERT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WWISE_VALUE_TO_STR_CONVERT_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ParamStr: str = ParamField(
        str, "ParamStr[32]", encoding="shift_jis_2004", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
