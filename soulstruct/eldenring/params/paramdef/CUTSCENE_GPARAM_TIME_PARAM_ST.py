from __future__ import annotations

__all__ = ["CUTSCENE_GPARAM_TIME_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CUTSCENE_GPARAM_TIME_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: bool = ParamField(
        byte, "disableParam_Debug:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    DstTimezoneMorning: int = ParamField(
        byte, "DstTimezone_Morning", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneNoon: int = ParamField(
        byte, "DstTimezone_Noon", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneAfterNoon: int = ParamField(
        byte, "DstTimezone_AfterNoon", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneEvening: int = ParamField(
        byte, "DstTimezone_Evening", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneNight: int = ParamField(
        byte, "DstTimezone_Night", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneDeepNightA: int = ParamField(
        byte, "DstTimezone_DeepNightA", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneDeepNightB: int = ParamField(
        byte, "DstTimezone_DeepNightB", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "reserved[1]")
    PostPlayIngameTime: float = ParamField(
        float, "PostPlayIngameTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
