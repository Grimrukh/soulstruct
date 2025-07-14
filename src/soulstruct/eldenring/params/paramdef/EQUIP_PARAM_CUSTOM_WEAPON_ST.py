from __future__ import annotations

__all__ = ["EQUIP_PARAM_CUSTOM_WEAPON_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_CUSTOM_WEAPON_ST(ParamRow):
    BaseWepId: int = ParamField(
        int32, "baseWepId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GemId: int = ParamField(
        int32, "gemId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceLv: int = ParamField(
        uint8, "reinforceLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(7, "pad[7]")
