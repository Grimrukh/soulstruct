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
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    SwordArtsType: int = ParamField(
        byte, "swordArtsType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArtsSpeedType: int = ParamField(
        byte, "artsSpeedType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefStatus: int = ParamField(
        sbyte, "refStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsRefRightArts: int = ParamField(
        byte, "isRefRightArts:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutLeftHand: int = ParamField(
        byte, "isGrayoutLeftHand:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutRightHand: int = ParamField(
        byte, "isGrayoutRightHand:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGrayoutBothHand: int = ParamField(
        byte, "isGrayoutBothHand:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "reserve2:4")
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
        sbyte, "shieldIconType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad[1]")
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiUsageId: int = ParamField(
        int, "aiUsageId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
