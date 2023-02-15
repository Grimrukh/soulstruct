from __future__ import annotations

__all__ = ["WEATHER_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WEATHER_PARAM_ST(ParamRow):
    SfxId: int = ParamField(
        int, "SfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WindSfxId: int = ParamField(
        int, "WindSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GroundHitSfxId: int = ParamField(
        int, "GroundHitSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundId: int = ParamField(
        int, "SoundId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetTime: float = ParamField(
        float, "WetTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    GparamId: int = ParamField(
        uint, "GparamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NextLotIngameSecondsMin: int = ParamField(
        uint, "NextLotIngameSecondsMin", default=3600,
        tooltip="TOOLTIP-TODO",
    )
    NextLotIngameSecondsMax: int = ParamField(
        uint, "NextLotIngameSecondsMax", default=7200,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId00: int = ParamField(
        int, "WetSpEffectId00", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId01: int = ParamField(
        int, "WetSpEffectId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId02: int = ParamField(
        int, "WetSpEffectId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId03: int = ParamField(
        int, "WetSpEffectId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WetSpEffectId04: int = ParamField(
        int, "WetSpEffectId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdInoor: int = ParamField(
        int, "SfxIdInoor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdOutdoor: int = ParamField(
        int, "SfxIdOutdoor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRate: float = ParamField(
        float, "aiSightRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DistViewWeatherGparamOverrideWeight: float = ParamField(
        float, "DistViewWeatherGparamOverrideWeight", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
