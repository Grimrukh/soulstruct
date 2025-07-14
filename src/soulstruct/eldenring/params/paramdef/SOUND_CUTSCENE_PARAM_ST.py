from __future__ import annotations

__all__ = ["SOUND_CUTSCENE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SOUND_CUTSCENE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ReverbType: int = ParamField(
        uint8, "ReverbType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad0[3]")
    BgmBehaviorTypeOnStart: int = ParamField(
        int16, "BgmBehaviorTypeOnStart", SOUND_CUTSCENE_BGM_BEHAVIOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OneShotBgmBehaviorOnStart: int = ParamField(
        int16, "OneShotBgmBehaviorOnStart", SOUND_CUTSCENE_BGM_BEHAVIOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PostPlaySeId: int = ParamField(
        int32, "PostPlaySeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PostPlaySeIdForSkip: int = ParamField(
        int32, "PostPlaySeIdForSkip", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnterMapMuteStopTimeOnDrawCutscene: float = ParamField(
        float32, "EnterMapMuteStopTimeOnDrawCutscene", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserved_old[8]")
    Unknown0x18: int = ParamField(
        uint8, "unknown_0x18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x19: int = ParamField(
        uint8, "unknown_0x19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x1a: int = ParamField(
        uint8, "unknown_0x1a", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x1b: int = ParamField(
        uint8, "unknown_0x1b", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "reserved[4]")
    _Pad4: bytes = ParamPad(4, "reserved2[4]")
