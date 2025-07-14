from __future__ import annotations

__all__ = ["WEATHER_LOT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WEATHER_LOT_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    WeatherType0: int = ParamField(
        int16, "weatherType0", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType1: int = ParamField(
        int16, "weatherType1", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType2: int = ParamField(
        int16, "weatherType2", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType3: int = ParamField(
        int16, "weatherType3", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType4: int = ParamField(
        int16, "weatherType4", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType5: int = ParamField(
        int16, "weatherType5", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType6: int = ParamField(
        int16, "weatherType6", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType7: int = ParamField(
        int16, "weatherType7", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType8: int = ParamField(
        int16, "weatherType8", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType9: int = ParamField(
        int16, "weatherType9", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType10: int = ParamField(
        int16, "weatherType10", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType11: int = ParamField(
        int16, "weatherType11", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType12: int = ParamField(
        int16, "weatherType12", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType13: int = ParamField(
        int16, "weatherType13", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType14: int = ParamField(
        int16, "weatherType14", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeatherType15: int = ParamField(
        int16, "weatherType15", WEATHER_TYPE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight0: int = ParamField(
        uint16, "lotteryWeight0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight1: int = ParamField(
        uint16, "lotteryWeight1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight2: int = ParamField(
        uint16, "lotteryWeight2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight3: int = ParamField(
        uint16, "lotteryWeight3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight4: int = ParamField(
        uint16, "lotteryWeight4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight5: int = ParamField(
        uint16, "lotteryWeight5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight6: int = ParamField(
        uint16, "lotteryWeight6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight7: int = ParamField(
        uint16, "lotteryWeight7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight8: int = ParamField(
        uint16, "lotteryWeight8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight9: int = ParamField(
        uint16, "lotteryWeight9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight10: int = ParamField(
        uint16, "lotteryWeight10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight11: int = ParamField(
        uint16, "lotteryWeight11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight12: int = ParamField(
        uint16, "lotteryWeight12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight13: int = ParamField(
        uint16, "lotteryWeight13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight14: int = ParamField(
        uint16, "lotteryWeight14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LotteryWeight15: int = ParamField(
        uint16, "lotteryWeight15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneLimit: int = ParamField(
        uint8, "timezoneLimit", WEATHER_LOT_TIMEZONE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneStartHour: int = ParamField(
        uint8, "timezoneStartHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneStartMinute: int = ParamField(
        uint8, "timezoneStartMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneEndHour: int = ParamField(
        uint8, "timezoneEndHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TimezoneEndMinute: int = ParamField(
        uint8, "timezoneEndMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(9, "reserve[9]")
