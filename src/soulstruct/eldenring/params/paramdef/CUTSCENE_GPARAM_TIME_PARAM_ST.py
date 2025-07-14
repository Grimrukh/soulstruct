from __future__ import annotations

__all__ = ["CUTSCENE_GPARAM_TIME_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CUTSCENE_GPARAM_TIME_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: bool = ParamField(
        uint8, "disableParam_Debug:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    DstTimezoneMorning: int = ParamField(
        uint8, "DstTimezone_Morning", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneNoon: int = ParamField(
        uint8, "DstTimezone_Noon", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneAfterNoon: int = ParamField(
        uint8, "DstTimezone_AfterNoon", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneEvening: int = ParamField(
        uint8, "DstTimezone_Evening", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneNight: int = ParamField(
        uint8, "DstTimezone_Night", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneDeepNightA: int = ParamField(
        uint8, "DstTimezone_DeepNightA", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneDeepNightB: int = ParamField(
        uint8, "DstTimezone_DeepNightB", CUTSCENE_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "reserved[1]")
    PostPlayIngameTime: float = ParamField(
        float32, "PostPlayIngameTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
