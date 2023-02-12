from __future__ import annotations

__all__ = ["WEATHER_LOT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WEATHER_LOT_PARAM_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    WeatherType0: int = ParamField(
        short, "weatherType0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType1: int = ParamField(
        short, "weatherType1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType2: int = ParamField(
        short, "weatherType2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType3: int = ParamField(
        short, "weatherType3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType4: int = ParamField(
        short, "weatherType4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType5: int = ParamField(
        short, "weatherType5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType6: int = ParamField(
        short, "weatherType6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType7: int = ParamField(
        short, "weatherType7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType8: int = ParamField(
        short, "weatherType8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType9: int = ParamField(
        short, "weatherType9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType10: int = ParamField(
        short, "weatherType10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType11: int = ParamField(
        short, "weatherType11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType12: int = ParamField(
        short, "weatherType12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType13: int = ParamField(
        short, "weatherType13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType14: int = ParamField(
        short, "weatherType14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType15: int = ParamField(
        short, "weatherType15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight0: int = ParamField(
        ushort, "lotteryWeight0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight1: int = ParamField(
        ushort, "lotteryWeight1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight2: int = ParamField(
        ushort, "lotteryWeight2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight3: int = ParamField(
        ushort, "lotteryWeight3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight4: int = ParamField(
        ushort, "lotteryWeight4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight5: int = ParamField(
        ushort, "lotteryWeight5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight6: int = ParamField(
        ushort, "lotteryWeight6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight7: int = ParamField(
        ushort, "lotteryWeight7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight8: int = ParamField(
        ushort, "lotteryWeight8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight9: int = ParamField(
        ushort, "lotteryWeight9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight10: int = ParamField(
        ushort, "lotteryWeight10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight11: int = ParamField(
        ushort, "lotteryWeight11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight12: int = ParamField(
        ushort, "lotteryWeight12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight13: int = ParamField(
        ushort, "lotteryWeight13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight14: int = ParamField(
        ushort, "lotteryWeight14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight15: int = ParamField(
        ushort, "lotteryWeight15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneLimit: int = ParamField(
        byte, "timezoneLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneStartHour: int = ParamField(
        byte, "timezoneStartHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneStartMinute: int = ParamField(
        byte, "timezoneStartMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneEndHour: int = ParamField(
        byte, "timezoneEndHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneEndMinute: int = ParamField(
        byte, "timezoneEndMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(9, "reserve[9]")
