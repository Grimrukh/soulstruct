from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class TALK_PARAM_ST(ParamRow):
    SubtitleText: Subtitle = ParamField(
        int, "msgId", default=-1,
        tooltip="Text ID for dialogue subtitle.",
    )
    VoiceSound: int = ParamField(
        int, "voiceId", default=-1,
        tooltip="Sound ID (voice) for dialogue.",
    )
    TalkingAnimation: int = ParamField(
        int, "motionId", default=-1,
        tooltip="Animation used for talking (-1 for default, or no animation). Usually 7000 (e.g. Fair Lady) or 7001 "
                "(e.g. Andre) when used.",
    )
    ReturnConversation: DialogueParam = ParamField(
        int, "returnPos", default=0, hide=True,
        tooltip="Conversation ID to use instead if the player has 'returned' to this conversation. Used exactly once "
                "for one line by the Crestfallen Warrior, so presumably works, but probably not useful.",
    )
    ReactionConversation: DialogueParam = ParamField(
        int, "reactionId", default=-1, hide=True,
        tooltip="Conversation ID to use as 'reaction'. Always -1.",
    )
    EventFlag: Flag = ParamField(
        int, "eventId", default=-1, hide=True,
        tooltip="Flag that is enabled when conversation plays (I assume). Used exactly once, for the same Crestfallen "
                "Warrior line that uses the ReturnConversation field.",
    )
    IsMotionLoop: bool = ParamField(
        byte, "isMotionLoop", default=0,
        tooltip="If True, specified TalkingAnimation will loop while dialogue is being spoken. Always True for any "
                "entry that has a non-default TalkingAnimation (e.g. Andre).",
    )
    _Pad0: bytes = ParamPad(7, "pad0[7]")
