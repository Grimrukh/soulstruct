from __future__ import annotations

__all__ = ["AI_SOUND_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class AI_SOUND_PARAM_ST(ParamRowData):
    Radius: float = ParamField(
        float, "radius", default=0.0,
        tooltip="TODO",
    )
    Duration: float = ParamField(
        float, "lifeFrame", default=0.0,
        tooltip="TODO",
    )
    IsAffectedbySoundRadiusMagnification: int = ParamField(
        byte, "bSpEffectEnable", default=0,
        tooltip="TODO",
    )
    RateType: int = ParamField(
        byte, "type", default=0,
        tooltip="TODO",
    )
    FakeTargetType: int = ParamField(
        byte, "fakeTargetType", default=0,
        tooltip="TODO",
    )
    InterestCategory: int = ParamField(
        byte, "interestCategory", default=0,
        tooltip="TODO",
    )
    UseHitDamageTeam: int = ParamField(
        byte, "useHitDamageTeam", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(19, "pad1[19]")
