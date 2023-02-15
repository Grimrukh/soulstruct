from __future__ import annotations

__all__ = ["TALK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class TALK_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    MsgId: int = ParamField(
        int, "msgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VoiceId: int = ParamField(
        int, "voiceId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId0: int = ParamField(
        int, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MotionId0: int = ParamField(
        int, "motionId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MotionId1: int = ParamField(
        int, "motionId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReturnPos: int = ParamField(
        int, "returnPos", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReactionId: int = ParamField(
        int, "reactionId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EventId: int = ParamField(
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
    _Pad1: bytes = ParamPad(4, "pad2[4]")
    Timeout: float = ParamField(
        float, "timeout", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    TalkAnimationId: int = ParamField(
        int, "talkAnimationId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsForceDisp: bool = ParamField(
        byte, "isForceDisp:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad3:7", bit_count=7)
    _Pad2: bytes = ParamPad(31, "pad1[31]")
