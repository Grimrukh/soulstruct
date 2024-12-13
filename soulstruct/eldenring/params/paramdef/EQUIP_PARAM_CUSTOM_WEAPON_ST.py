from __future__ import annotations

__all__ = ["EQUIP_PARAM_CUSTOM_WEAPON_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_CUSTOM_WEAPON_ST(ParamRow):
    BaseWepId: int = ParamField(
        int, "baseWepId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GemId: int = ParamField(
        int, "gemId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceLv: int = ParamField(
        byte, "reinforceLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(7, "pad[7]")
