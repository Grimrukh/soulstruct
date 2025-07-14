from __future__ import annotations

__all__ = ["SWORD_ARTS_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SWORD_ARTS_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SwordArtsType: int = ParamField(
        uint8, "swordArtsType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArtsSpeedType: int = ParamField(
        uint8, "artsSpeedType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefStatus: int = ParamField(
        int8, "refStatus", SWORD_ARTS_REF_STATUS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsRefRightArts: bool = ParamField(
        uint8, "isRefRightArts:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutLeftHand: bool = ParamField(
        uint8, "isGrayoutLeftHand:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutRightHand: bool = ParamField(
        uint8, "isGrayoutRightHand:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutBothHand: bool = ParamField(
        uint8, "isGrayoutBothHand:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "reserve2:4", bit_count=4)
    UsePointL1: int = ParamField(
        int8, "usePoint_L1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsePointL2: int = ParamField(
        int8, "usePoint_L2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsePointR1: int = ParamField(
        int8, "usePoint_R1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsePointR2: int = ParamField(
        int8, "usePoint_R2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId: int = ParamField(
        int32, "textId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointL1: int = ParamField(
        int16, "useMagicPoint_L1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointL2: int = ParamField(
        int16, "useMagicPoint_L2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointR1: int = ParamField(
        int16, "useMagicPoint_R1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseMagicPointR2: int = ParamField(
        int16, "useMagicPoint_R2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SwordArtsTypeNew: int = ParamField(
        uint16, "swordArtsTypeNew", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        uint16, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiUsageId: int = ParamField(
        int32, "aiUsageId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
