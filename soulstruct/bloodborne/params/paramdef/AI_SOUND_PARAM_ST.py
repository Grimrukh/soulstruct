from __future__ import annotations

__all__ = ["AI_SOUND_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class AI_SOUND_PARAM_ST(ParamRow):
    Radius: float = ParamField(
        float, "radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeFrame: float = ParamField(
        float, "lifeFrame", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BSpEffectEnable: int = ParamField(
        byte, "bSpEffectEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Type: int = ParamField(
        byte, "type", AI_SOUND_RATE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetType: int = ParamField(
        byte, "fakeTargetType", AI_SOUND_FAKE_TARGET_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    InterestCategory: int = ParamField(
        byte, "interestCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseHitDamageTeam: int = ParamField(
        byte, "useHitDamageTeam", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(19, "pad1[19]")
