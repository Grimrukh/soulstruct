from __future__ import annotations

__all__ = ["DIRECTION_CAMERA_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class DIRECTION_CAMERA_PARAM_ST(ParamRowData):
    IsUseOption: int = ParamField(
        byte, "isUseOption:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2:3")
    _Pad1: bytes = ParamPad(15, "pad1[15]")
