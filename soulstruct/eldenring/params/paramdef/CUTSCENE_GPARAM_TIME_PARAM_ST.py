from __future__ import annotations

__all__ = ["CUTSCENE_GPARAM_TIME_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CUTSCENE_GPARAM_TIME_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: int = ParamField(
        byte, "disableParam_Debug:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:6")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    DstTimezoneMorning: int = ParamField(
        byte, "DstTimezone_Morning", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneNoon: int = ParamField(
        byte, "DstTimezone_Noon", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneAfterNoon: int = ParamField(
        byte, "DstTimezone_AfterNoon", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneEvening: int = ParamField(
        byte, "DstTimezone_Evening", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneNight: int = ParamField(
        byte, "DstTimezone_Night", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneDeepNightA: int = ParamField(
        byte, "DstTimezone_DeepNightA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstTimezoneDeepNightB: int = ParamField(
        byte, "DstTimezone_DeepNightB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "reserved[1]")
    PostPlayIngameTime: float = ParamField(
        float, "PostPlayIngameTime", default=-1,
        tooltip="TOOLTIP-TODO",
    )
