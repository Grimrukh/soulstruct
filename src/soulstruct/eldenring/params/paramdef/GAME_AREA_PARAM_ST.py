from __future__ import annotations

__all__ = ["GAME_AREA_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class GAME_AREA_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SingleplayerSoulReward: int = ParamField(
        uint32, "bonusSoul_single", default=0,
        tooltip="Souls awarded (after delay) when boss is defeated with no summons.",
    )
    MultiplayerSoulReward: int = ParamField(
        uint32, "bonusSoul_multi", default=0,
        tooltip="Souls awarded to each player (after delay) when boss is defeated with summons.",
    )
    FirstHumanityFlag: int = ParamField(
        uint32, "humanityPointCountFlagIdTop", game_type=Flag, default=0,
        tooltip="First flag for recording number of humanity drops awarded in boss's area.",
    )
    HumanityDropPoint1: int = ParamField(
        uint16, "humanityDropPoint1", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for first Humanity.",
    )
    HumanityDropPoint2: int = ParamField(
        uint16, "humanityDropPoint2", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for second Humanity.",
    )
    HumanityDropPoint3: int = ParamField(
        uint16, "humanityDropPoint3", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for third Humanity.",
    )
    HumanityDropPoint4: int = ParamField(
        uint16, "humanityDropPoint4", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for fourth Humanity.",
    )
    HumanityDropPoint5: int = ParamField(
        uint16, "humanityDropPoint5", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for fifth Humanity.",
    )
    HumanityDropPoint6: int = ParamField(
        uint16, "humanityDropPoint6", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for sixth Humanity.",
    )
    HumanityDropPoint7: int = ParamField(
        uint16, "humanityDropPoint7", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for seventh Humanity.",
    )
    HumanityDropPoint8: int = ParamField(
        uint16, "humanityDropPoint8", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for eighth Humanity.",
    )
    HumanityDropPoint9: int = ParamField(
        uint16, "humanityDropPoint9", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for ninth Humanity.",
    )
    HumanityDropPoint10: int = ParamField(
        uint16, "humanityDropPoint10", default=0,
        tooltip="Number of 'points' needed from killing enemies in the boss area for final Humanity.",
    )
    SoloBreakInPointMin: int = ParamField(
        uint32, "soloBreakInPoint_Min", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoloBreakInPointMax: int = ParamField(
        uint32, "soloBreakInPoint_Max", default=10000,
        tooltip="TOOLTIP-TODO",
    )
    DefeatBossFlagIdforSignAimList: int = ParamField(
        uint32, "defeatBossFlagId_forSignAimList", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisplayAimFlagId: int = ParamField(
        uint32, "displayAimFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FoundBossFlagId: int = ParamField(
        uint32, "foundBossFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FoundBossTextId: int = ParamField(
        int32, "foundBossTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NotFindBossTextId: int = ParamField(
        int32, "notFindBossTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BossChallengeFlagId: int = ParamField(
        uint32, "bossChallengeFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatBossFlagId: int = ParamField(
        uint32, "defeatBossFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossPosX: float = ParamField(
        float32, "bossPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BossPosY: float = ParamField(
        float32, "bossPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BossPosZ: float = ParamField(
        float32, "bossPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BossMapAreaNo: int = ParamField(
        uint8, "bossMapAreaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossMapBlockNo: int = ParamField(
        uint8, "bossMapBlockNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossMapMapNo: int = ParamField(
        uint8, "bossMapMapNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(9, "reserve[9]")
