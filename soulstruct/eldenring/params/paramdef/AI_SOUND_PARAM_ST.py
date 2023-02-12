from __future__ import annotations

__all__ = ["AI_SOUND_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class AI_SOUND_PARAM_ST(ParamRowData):
    Radius: float = ParamField(
        float, "radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeFrame: float = ParamField(
        float, "lifeFrame", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BSpEffectEnable: int = ParamField(
        byte, "bSpEffectEnable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Type: int = ParamField(
        byte, "type", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpposeTarget: int = ParamField(
        byte, "opposeTarget:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FriendlyTarget: int = ParamField(
        byte, "friendlyTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelfTarget: int = ParamField(
        byte, "selfTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableOnTargetPCompany: int = ParamField(
        byte, "disableOnTargetPCompany:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Rank: int = ParamField(
        byte, "rank", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForgetTime: float = ParamField(
        float, "forgetTime", default=-1,
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
        byte, "replaningState", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "pad1[6]")
