from __future__ import annotations

__all__ = ["RETURN_POINT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class RETURN_POINT_PARAM_ST(ParamRow):
    Area: int = ParamField(
        int16, "areaNo", default=0,
        tooltip="TODO",
    )
    Block: int = ParamField(
        int16, "blockNo", default=0,
        tooltip="TODO",
    )
    ReturnPointEntityID: int = ParamField(
        int32, "returnPointEntityId", default=-1,
        tooltip="TODO",
    )
    ReturnAnimationID: int = ParamField(
        int32, "returnAnimId", game_type=Animation, default=-1,
        tooltip="TODO",
    )
    IsRegistDeadReturn: int = ParamField(
        uint8, "isRegistDeadReturn", RETURN_POINT_TYPE_YES_NO, default=0,
        tooltip="TODO",
    )
    WarpChair: int = ParamField(
        int8, "warpChairNo", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(18, "pad1[18]")
