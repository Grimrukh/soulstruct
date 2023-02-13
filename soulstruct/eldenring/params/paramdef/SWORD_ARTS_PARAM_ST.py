from __future__ import annotations

__all__ = ["SWORD_ARTS_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SWORD_ARTS_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SwordArtsType: int = ParamField(
        byte, "swordArtsType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArtsSpeedType: int = ParamField(
        byte, "artsSpeedType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefStatus: int = ParamField(
        sbyte, "refStatus", SWORD_ARTS_REF_STATUS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsRefRightArts: bool = ParamField(
        byte, "isRefRightArts:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutLeftHand: bool = ParamField(
        byte, "isGrayoutLeftHand:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutRightHand: bool = ParamField(
        byte, "isGrayoutRightHand:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutBothHand: bool = ParamField(
        byte, "isGrayoutBothHand:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "reserve2:4", bit_count=4)
    UsePointL1: int = ParamField(
        sbyte, "usePoint_L1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsePointL2: int = ParamField(
        sbyte, "usePoint_L2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsePointR1: int = ParamField(
        sbyte, "usePoint_R1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsePointR2: int = ParamField(
        sbyte, "usePoint_R2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId: int = ParamField(
        int, "textId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointL1: int = ParamField(
        short, "useMagicPoint_L1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointL2: int = ParamField(
        short, "useMagicPoint_L2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointR1: int = ParamField(
        short, "useMagicPoint_R1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointR2: int = ParamField(
        short, "useMagicPoint_R2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShieldIconType: int = ParamField(
        sbyte, "shieldIconType", SWORD_ARTS_SHIELD_ICON_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad[1]")
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiUsageId: int = ParamField(
        int, "aiUsageId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
