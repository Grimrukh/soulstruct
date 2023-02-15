from __future__ import annotations

__all__ = ["WEATHER_LOT_TEX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WEATHER_LOT_TEX_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SrcR: int = ParamField(
        byte, "srcR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcG: int = ParamField(
        byte, "srcG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcB: int = ParamField(
        byte, "srcB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    WeatherLogId: int = ParamField(
        int, "weatherLogId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(4, "pad2[4]")
