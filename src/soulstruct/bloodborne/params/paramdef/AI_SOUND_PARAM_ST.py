from __future__ import annotations

__all__ = ["AI_SOUND_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class AI_SOUND_PARAM_ST(ParamRow):
    Radius: float = ParamField(
        float32, "radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeFrame: float = ParamField(
        float32, "lifeFrame", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BSpEffectEnable: int = ParamField(
        uint8, "bSpEffectEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Type: int = ParamField(
        uint8, "type", AI_SOUND_RATE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetType: int = ParamField(
        uint8, "fakeTargetType", AI_SOUND_FAKE_TARGET_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    InterestCategory: int = ParamField(
        uint8, "interestCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseHitDamageTeam: int = ParamField(
        uint8, "useHitDamageTeam", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(19, "pad1[19]")
