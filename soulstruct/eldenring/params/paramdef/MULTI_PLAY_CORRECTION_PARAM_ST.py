from __future__ import annotations

__all__ = ["MULTI_PLAY_CORRECTION_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MULTI_PLAY_CORRECTION_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
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
        byte, "bOverrideSpEffect", MULTI_PLAY_CORRECTION_OVERRIDE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(15, "pad3[15]")
