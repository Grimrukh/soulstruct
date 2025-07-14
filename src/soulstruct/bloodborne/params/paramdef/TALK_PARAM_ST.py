from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class TALK_PARAM_ST(ParamRow):
    SubtitleText: int = ParamField(
        int32, "msgId", default=-1,
        tooltip="Text ID for dialogue subtitle.",
    )
    VoiceSound: int = ParamField(
        int32, "voiceId", default=-1,
        tooltip="Sound ID (voice) for dialogue.",
    )
    SpecialEffectID0: int = ParamField(
        int32, "spEffectId0", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID0: int = ParamField(
        int32, "motionId0", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID1: int = ParamField(
        int32, "spEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID1: int = ParamField(
        int32, "motionId1", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID2: int = ParamField(
        int32, "spEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID2: int = ParamField(
        int32, "motionId2", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID3: int = ParamField(
        int32, "spEffectId3", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID3: int = ParamField(
        int32, "motionId3", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID4: int = ParamField(
        int32, "spEffectId4", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID4: int = ParamField(
        int32, "motionId4", default=-1,
        tooltip="TODO",
    )
    SpecialEffectID5: int = ParamField(
        int32, "spEffectId5", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    AnimationID5: int = ParamField(
        int32, "motionId5", default=-1,
        tooltip="TODO",
    )
    ReturnConversation: int = ParamField(
        int32, "returnPos", default=-1,
        tooltip="Conversation ID to use instead if the player has 'returned' to this conversation. Used exactly once "
                "for one line by the Crestfallen Warrior, so presumably works, but probably not useful.",
    )
    ReactionConversation: int = ParamField(
        int32, "reactionId", default=-1,
        tooltip="Conversation ID to use as 'reaction'. Always -1.",
    )
    EventFlag: int = ParamField(
        int32, "eventId", default=-1,
        tooltip="Flag that is enabled when conversation plays (I assume). Used exactly once, for the same Crestfallen "
                "Warrior line that uses the ReturnConversation field.",
    )
