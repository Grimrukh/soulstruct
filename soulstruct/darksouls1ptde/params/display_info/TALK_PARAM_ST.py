from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *

TALK_PARAM_ST = {
    "param_type": "TALK_PARAM_ST",
    "file_name": "TalkParam",
    "nickname": "Dialogue",
    "fields": [
        ParamFieldInfo("msgId", "SubtitleText", True, Subtitle, "Text ID for dialogue subtitle."),
        ParamFieldInfo("voiceId", "VoiceSound", True, int, "Sound ID (voice) for dialogue."),
        ParamFieldInfo(
            "motionId",
            "TalkingAnimation",
            True,
            int,  # TODO: Animation
            "Animation used for talking (-1 for default, or no animation). Usually 7000 (e.g. Fair Lady) or 7001 "
            "(e.g. Andre) when used.",
        ),
        ParamFieldInfo(
            "returnPos",
            "ReturnConversation",
            False,
            DialogueParam,
            "Conversation ID to use instead if the player has 'returned' to this conversation. Used exactly once "
            "for one line by the Crestfallen Warrior, so presumably works, but probably not useful.",
        ),
        ParamFieldInfo(
            "reactionId",
            "ReactionConversation",
            False,
            DialogueParam,
            "Conversation ID to use as 'reaction'. Always -1.",
        ),
        ParamFieldInfo(
            "eventId",
            "EventFlag",
            False,
            Flag,
            "Flag that is enabled when conversation plays (I assume). Used exactly once, for the same Crestfallen "
            "Warrior line that uses the ReturnConversation field.",
        ),
        ParamFieldInfo(
            "isMotionLoop",
            "IsMotionLoop",
            True,
            bool,
            "If True, specified TalkingAnimation will loop while dialogue is being spoken. Always True for any "
            "entry that has a non-default TalkingAnimation (e.g. Andre).",
        ),
        ParamFieldInfo("pad0[7]", "Pad", False, pad_field(7), "Null padding."),
    ],
}
