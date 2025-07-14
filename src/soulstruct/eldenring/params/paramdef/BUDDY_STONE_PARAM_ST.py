from __future__ import annotations

__all__ = ["BUDDY_STONE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class BUDDY_STONE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    TalkChrEntityId: int = ParamField(
        uint32, "talkChrEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EliminateTargetEntityId: int = ParamField(
        uint32, "eliminateTargetEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonedEventFlagId: int = ParamField(
        uint32, "summonedEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSpecial: bool = ParamField(
        uint8, "isSpecial:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad1:7", bit_count=7)
    _Pad1: bytes = ParamPad(3, "pad2[3]")
    BuddyId: int = ParamField(
        int32, "buddyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectId: int = ParamField(
        int32, "dopingSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActivateRange: int = ParamField(
        uint16, "activateRange", default=100,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteReturnRange: int = ParamField(
        int16, "overwriteReturnRange", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteActivateRegionEntityId: int = ParamField(
        uint32, "overwriteActivateRegionEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarnRegionEntityId: int = ParamField(
        uint32, "warnRegionEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(24, "pad3[24]")
