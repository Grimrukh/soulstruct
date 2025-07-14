from __future__ import annotations

__all__ = ["WEATHER_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class WEATHER_PARAM_ST(ParamRow):
    SfxId: int = ParamField(
        int32, "SfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WindSfxId: int = ParamField(
        int32, "WindSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GroundHitSfxId: int = ParamField(
        int32, "GroundHitSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundId: int = ParamField(
        int32, "SoundId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetTime: float = ParamField(
        float32, "WetTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    GparamId: int = ParamField(
        uint32, "GparamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NextLotIngameSecondsMin: int = ParamField(
        uint32, "NextLotIngameSecondsMin", default=3600,
        tooltip="TOOLTIP-TODO",
    )
    NextLotIngameSecondsMax: int = ParamField(
        uint32, "NextLotIngameSecondsMax", default=7200,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId00: int = ParamField(
        int32, "WetSpEffectId00", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId01: int = ParamField(
        int32, "WetSpEffectId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId02: int = ParamField(
        int32, "WetSpEffectId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId03: int = ParamField(
        int32, "WetSpEffectId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId04: int = ParamField(
        int32, "WetSpEffectId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdInoor: int = ParamField(
        int32, "SfxIdInoor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdOutdoor: int = ParamField(
        int32, "SfxIdOutdoor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRate: float = ParamField(
        float32, "aiSightRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DistViewWeatherGparamOverrideWeight: float = ParamField(
        float32, "DistViewWeatherGparamOverrideWeight", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
