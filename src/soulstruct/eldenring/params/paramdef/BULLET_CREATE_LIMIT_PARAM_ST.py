from __future__ import annotations

__all__ = ["BULLET_CREATE_LIMIT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class BULLET_CREATE_LIMIT_PARAM_ST(ParamRow):
    LimitNumbyGroup: int = ParamField(
        uint8, "limitNum_byGroup", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLimitEachOwner: bool = ParamField(
        uint8, "isLimitEachOwner:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad2:7", bit_count=7)
    _Pad0: bytes = ParamPad(30, "pad[30]")
