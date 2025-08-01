from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from soulstruct.base.params.param_row import *
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
    TalkingAnimation: int = ParamField(
        int32, "motionId", default=-1,
        tooltip="Animation used for talking (-1 for default, or no animation). Usually 7000 (e.g. Fair Lady) or 7001 "
                "(e.g. Andre) when used.",
    )
    ReturnConversation: int = ParamField(
        int32, "returnPos", default=0,
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
    IsMotionLoop: int = ParamField(
        uint8, "isMotionLoop", default=0,
        tooltip="If True, specified TalkingAnimation will loop while dialogue is being spoken. Always True for any "
                "entry that has a non-default TalkingAnimation (e.g. Andre).",
    )
    _Pad0: bytes = ParamPad(7, "pad0[7]")
