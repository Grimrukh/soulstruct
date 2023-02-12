from __future__ import annotations

__all__ = ["BULLET_CREATE_LIMIT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BULLET_CREATE_LIMIT_PARAM_ST(ParamRow):
    LimitNumbyGroup: int = ParamField(
        byte, "limitNum_byGroup", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLimitEachOwner: int = ParamField(
        byte, "isLimitEachOwner:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2:7")
    _Pad1: bytes = ParamPad(30, "pad[30]")
