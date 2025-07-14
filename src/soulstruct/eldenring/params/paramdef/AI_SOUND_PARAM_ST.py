from __future__ import annotations

__all__ = ["AI_SOUND_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
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
    OpposeTarget: bool = ParamField(
        uint8, "opposeTarget:1", AI_SOUND_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    FriendlyTarget: bool = ParamField(
        uint8, "friendlyTarget:1", AI_SOUND_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SelfTarget: bool = ParamField(
        uint8, "selfTarget:1", AI_SOUND_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableOnTargetPCompany: bool = ParamField(
        uint8, "disableOnTargetPCompany:1", AI_SOUND_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Rank: int = ParamField(
        uint8, "rank", AI_SOUND_RANK, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForgetTime: float = ParamField(
        float32, "forgetTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    Priority: int = ParamField(
        int32, "priority", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId: int = ParamField(
        int32, "soundBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AiSoundLevel: int = ParamField(
        uint8, "aiSoundLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaningState: int = ParamField(
        uint8, "replaningState", AI_SOUND_REPLANNING_STATE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "pad1[6]")
