from __future__ import annotations

__all__ = ["DIRECTION_CAMERA_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class DIRECTION_CAMERA_PARAM_ST(ParamRow):
    IsUseOption: bool = ParamField(
        byte, "isUseOption:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad2:3", bit_count=3)
    _Pad0: bytes = ParamPad(15, "pad1[15]")
