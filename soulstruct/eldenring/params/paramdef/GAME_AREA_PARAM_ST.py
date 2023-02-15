from __future__ import annotations

__all__ = ["GAME_AREA_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GAME_AREA_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    BonusSoulsingle: int = ParamField(
        uint, "bonusSoul_single", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BonusSoulmulti: int = ParamField(
        uint, "bonusSoul_multi", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityPointCountFlagIdTop: int = ParamField(
        uint, "humanityPointCountFlagIdTop", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint1: int = ParamField(
        ushort, "humanityDropPoint1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint2: int = ParamField(
        ushort, "humanityDropPoint2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint3: int = ParamField(
        ushort, "humanityDropPoint3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint4: int = ParamField(
        ushort, "humanityDropPoint4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint5: int = ParamField(
        ushort, "humanityDropPoint5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint6: int = ParamField(
        ushort, "humanityDropPoint6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint7: int = ParamField(
        ushort, "humanityDropPoint7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint8: int = ParamField(
        ushort, "humanityDropPoint8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint9: int = ParamField(
        ushort, "humanityDropPoint9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDropPoint10: int = ParamField(
        ushort, "humanityDropPoint10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoloBreakInPointMin: int = ParamField(
        uint, "soloBreakInPoint_Min", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoloBreakInPointMax: int = ParamField(
        uint, "soloBreakInPoint_Max", default=10000,
        tooltip="TOOLTIP-TODO",
    )
    DefeatBossFlagIdforSignAimList: int = ParamField(
        uint, "defeatBossFlagId_forSignAimList", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisplayAimFlagId: int = ParamField(
        uint, "displayAimFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FoundBossFlagId: int = ParamField(
        uint, "foundBossFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FoundBossTextId: int = ParamField(
        int, "foundBossTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NotFindBossTextId: int = ParamField(
        int, "notFindBossTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BossChallengeFlagId: int = ParamField(
        uint, "bossChallengeFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatBossFlagId: int = ParamField(
        uint, "defeatBossFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossPosX: float = ParamField(
        float, "bossPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BossPosY: float = ParamField(
        float, "bossPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BossPosZ: float = ParamField(
        float, "bossPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BossMapAreaNo: int = ParamField(
        byte, "bossMapAreaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossMapBlockNo: int = ParamField(
        byte, "bossMapBlockNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossMapMapNo: int = ParamField(
        byte, "bossMapMapNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(9, "reserve[9]")
