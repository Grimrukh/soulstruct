from __future__ import annotations

__all__ = ["SOUND_CUTSCENE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SOUND_CUTSCENE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ReverbType: int = ParamField(
        byte, "ReverbType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad0[3]")
    BgmBehaviorTypeOnStart: int = ParamField(
        short, "BgmBehaviorTypeOnStart", SOUND_CUTSCENE_BGM_BEHAVIOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OneShotBgmBehaviorOnStart: int = ParamField(
        short, "OneShotBgmBehaviorOnStart", SOUND_CUTSCENE_BGM_BEHAVIOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PostPlaySeId: int = ParamField(
        int, "PostPlaySeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PostPlaySeIdForSkip: int = ParamField(
        int, "PostPlaySeIdForSkip", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnterMapMuteStopTimeOnDrawCutscene: float = ParamField(
        float, "EnterMapMuteStopTimeOnDrawCutscene", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserved[8]")
