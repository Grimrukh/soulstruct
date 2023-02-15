from __future__ import annotations

__all__ = ["BUDDY_STONE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BUDDY_STONE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    TalkChrEntityId: int = ParamField(
        uint, "talkChrEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EliminateTargetEntityId: int = ParamField(
        uint, "eliminateTargetEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonedEventFlagId: int = ParamField(
        uint, "summonedEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSpecial: bool = ParamField(
        byte, "isSpecial:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad1:7", bit_count=7)
    _Pad1: bytes = ParamPad(3, "pad2[3]")
    BuddyId: int = ParamField(
        int, "buddyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectId: int = ParamField(
        int, "dopingSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActivateRange: int = ParamField(
        ushort, "activateRange", default=100,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteReturnRange: int = ParamField(
        short, "overwriteReturnRange", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteActivateRegionEntityId: int = ParamField(
        uint, "overwriteActivateRegionEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarnRegionEntityId: int = ParamField(
        uint, "warnRegionEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(24, "pad3[24]")
