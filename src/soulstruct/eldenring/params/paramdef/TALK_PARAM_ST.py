from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class TALK_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
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
    MsgIdfemale: int = ParamField(
        int32, "msgId_female", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VoiceIdfemale: int = ParamField(
        int32, "voiceId_female", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LipSyncStart: int = ParamField(
        int16, "lipSyncStart", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LipSyncTime: int = ParamField(
        int16, "lipSyncTime", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "pad2[4]")
    Timeout: float = ParamField(
        float32, "timeout", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    TalkAnimationId: int = ParamField(
        int32, "talkAnimationId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsForceDisp: bool = ParamField(
        uint8, "isForceDisp:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad3:7", bit_count=7)
    _Pad2: bytes = ParamPad(31, "pad1[31]")
