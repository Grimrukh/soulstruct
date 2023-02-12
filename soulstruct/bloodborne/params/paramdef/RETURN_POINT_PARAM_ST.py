from __future__ import annotations

__all__ = ["RETURN_POINT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class RETURN_POINT_PARAM_ST(ParamRow):
    Area: int = ParamField(
        short, "areaNo", default=0,
        tooltip="TODO",
    )
    Block: int = ParamField(
        short, "blockNo", default=0,
        tooltip="TODO",
    )
    ReturnPointEntityID: int = ParamField(
        int, "returnPointEntityId", default=-1,
        tooltip="TODO",
    )
    ReturnAnimationID: int = ParamField(
        int, "returnAnimId", default=-1,
        tooltip="TODO",
    )
    IsRegistDeadReturn: RETURN_POINT_TYPE_YES_NO = ParamField(
        byte, "isRegistDeadReturn", default=0,
        tooltip="TODO",
    )
    WarpChair: int = ParamField(
        sbyte, "warpChairNo", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(18, "pad1[18]")
