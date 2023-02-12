from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class TALK_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    SubtitleText: int = ParamField(
        int, "msgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VoiceSound: int = ParamField(
        int, "voiceId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID0: int = ParamField(
        int, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnimationID0: int = ParamField(
        int, "motionId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnimationID1: int = ParamField(
        int, "motionId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReturnConversation: int = ParamField(
        int, "returnPos", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReactionConversation: int = ParamField(
        int, "reactionId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EventFlag: int = ParamField(
        int, "eventId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MsgIdfemale: int = ParamField(
        int, "msgId_female", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VoiceIdfemale: int = ParamField(
        int, "voiceId_female", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LipSyncStart: int = ParamField(
        short, "lipSyncStart", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LipSyncTime: int = ParamField(
        short, "lipSyncTime", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(4, "pad2[4]")
    Timeout: float = ParamField(
        float, "timeout", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TalkAnimationId: int = ParamField(
        int, "talkAnimationId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsForceDisp: int = ParamField(
        byte, "isForceDisp:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad3:7")
    _Pad4: bytes = ParamPad(31, "pad1[31]")
