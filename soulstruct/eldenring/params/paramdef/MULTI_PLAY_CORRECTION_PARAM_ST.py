from __future__ import annotations

__all__ = ["MULTI_PLAY_CORRECTION_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MULTI_PLAY_CORRECTION_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    Client1SpEffectId: int = ParamField(
        int, "client1SpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Client2SpEffectId: int = ParamField(
        int, "client2SpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Client3SpEffectId: int = ParamField(
        int, "client3SpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BOverrideSpEffect: int = ParamField(
        byte, "bOverrideSpEffect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(15, "pad3[15]")
