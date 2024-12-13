from __future__ import annotations

__all__ = ["RETURN_POINT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


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
        int, "returnAnimId", game_type=Animation, default=-1,
        tooltip="TODO",
    )
    IsRegistDeadReturn: int = ParamField(
        byte, "isRegistDeadReturn", RETURN_POINT_TYPE_YES_NO, default=0,
        tooltip="TODO",
    )
    WarpChair: int = ParamField(
        sbyte, "warpChairNo", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(18, "pad1[18]")
