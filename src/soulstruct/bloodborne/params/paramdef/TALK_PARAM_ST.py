from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class TALK_PARAM_ST(ParamRow):
    SubtitleText: int = ParamField(
        int, "msgId", default=-1,
        tooltip="Text ID for dialogue subtitle.",
    )
    VoiceSound: int = ParamField(
        int, "voiceId", default=-1,
        tooltip="Sound ID (voice) for dialogue.",
    )
    SpecialEffectID0: int = ParamField(
        int, "spEffectId0", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID0: int = ParamField(
        int, "motionId0", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID1: int = ParamField(
        int, "spEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID1: int = ParamField(
        int, "motionId1", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID2: int = ParamField(
        int, "spEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID2: int = ParamField(
        int, "motionId2", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID3: int = ParamField(
        int, "spEffectId3", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID3: int = ParamField(
        int, "motionId3", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID4: int = ParamField(
        int, "spEffectId4", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID4: int = ParamField(
        int, "motionId4", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID5: int = ParamField(
        int, "spEffectId5", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID5: int = ParamField(
        int, "motionId5", default=-1,
        tooltip="TODO",
    )
    ReturnConversation: int = ParamField(
        int, "returnPos", default=-1,
        tooltip="Conversation ID to use instead if the player has 'returned' to this conversation. Used exactly once "
                "for one line by the Crestfallen Warrior, so presumably works, but probably not useful.",
    )
    ReactionConversation: int = ParamField(
        int, "reactionId", default=-1,
        tooltip="Conversation ID to use as 'reaction'. Always -1.",
    )
    EventFlag: int = ParamField(
        int, "eventId", default=-1,
        tooltip="Flag that is enabled when conversation plays (I assume). Used exactly once, for the same Crestfallen "
                "Warrior line that uses the ReturnConversation field.",
    )
