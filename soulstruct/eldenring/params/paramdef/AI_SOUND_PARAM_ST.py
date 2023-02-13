from __future__ import annotations

__all__ = ["AI_SOUND_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
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
    OpposeTarget: bool = ParamField(
        byte, "opposeTarget:1", AI_SOUND_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    FriendlyTarget: bool = ParamField(
        byte, "friendlyTarget:1", AI_SOUND_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SelfTarget: bool = ParamField(
        byte, "selfTarget:1", AI_SOUND_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableOnTargetPCompany: bool = ParamField(
        byte, "disableOnTargetPCompany:1", AI_SOUND_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Rank: int = ParamField(
        byte, "rank", AI_SOUND_RANK, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForgetTime: float = ParamField(
        float, "forgetTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    Priority: int = ParamField(
        int, "priority", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId: int = ParamField(
        int, "soundBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AiSoundLevel: int = ParamField(
        byte, "aiSoundLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaningState: int = ParamField(
        byte, "replaningState", AI_SOUND_REPLANNING_STATE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "pad1[6]")
