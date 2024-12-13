from __future__ import annotations

__all__ = ["PLAY_REGION_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class PLAY_REGION_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    MatchAreaId: int = ParamField(
        int, "matchAreaId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayStartLimitEventFlagId: int = ParamField(
        uint, "multiPlayStartLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OtherDisableDistance: float = ParamField(
        float, "otherDisableDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PcPositionSaveLimitEventFlagId: int = ParamField(
        uint, "pcPositionSaveLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossAreaId: int = ParamField(
        uint, "bossAreaId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CultNpcWhiteGhostEntityIdbyFree: int = ParamField(
        short, "cultNpcWhiteGhostEntityId_byFree", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BMapGuradianRegion: int = ParamField(
        byte, "bMapGuradianRegion", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BYellowCostumeRegion: bool = ParamField(
        byte, "bYellowCostumeRegion:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayStartLimitEventFlagIdtargetFlagState: bool = ParamField(
        byte, "multiPlayStartLimitEventFlagId_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId1targetFlagState: bool = ParamField(
        byte, "breakInLimitEventFlagId_1_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId1targetFlagState: bool = ParamField(
        byte, "whiteSignLimitEventFlagId_1_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId1targetFlagState: bool = ParamField(
        byte, "redSignLimitEventFlagId_1_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId2targetFlagState: bool = ParamField(
        byte, "breakInLimitEventFlagId_2_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId3targetFlagState: bool = ParamField(
        byte, "breakInLimitEventFlagId_3_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId2targetFlagState: bool = ParamField(
        byte, "whiteSignLimitEventFlagId_2_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId1: int = ParamField(
        uint, "warpItemUsePermitBonfireId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId2: int = ParamField(
        uint, "warpItemUsePermitBonfireId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId3: int = ParamField(
        uint, "warpItemUsePermitBonfireId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId4: int = ParamField(
        uint, "warpItemUsePermitBonfireId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId5: int = ParamField(
        uint, "warpItemUsePermitBonfireId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId1: int = ParamField(
        uint, "warpItemProhibitionEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId2: int = ParamField(
        uint, "warpItemProhibitionEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId3: int = ParamField(
        uint, "warpItemProhibitionEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId4: int = ParamField(
        uint, "warpItemProhibitionEventFlagId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId5: int = ParamField(
        uint, "warpItemProhibitionEventFlagId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodstain: bool = ParamField(
        byte, "enableBloodstain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodMessage: bool = ParamField(
        byte, "enableBloodMessage:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableGhost: bool = ParamField(
        byte, "enableGhost:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    DispMask00: bool = ParamField(
        byte, "dispMask00:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DispMask01: bool = ParamField(
        byte, "dispMask01:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId3targetFlagState: bool = ParamField(
        byte, "whiteSignLimitEventFlagId_3_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId2targetFlagState: bool = ParamField(
        byte, "redSignLimitEventFlagId_2_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId3targetFlagState: bool = ParamField(
        byte, "redSignLimitEventFlagId_3_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsAutoIntrudePoint: bool = ParamField(
        byte, "isAutoIntrudePoint:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad1:7", bit_count=7)
    _Pad1: bytes = ParamPad(2, "pad2[2]")
    MultiPlayHASHostLimitEventFlagId: int = ParamField(
        uint, "multiPlayHASHostLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OtherMaxDistance: float = ParamField(
        float, "otherMaxDistance", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleOpenEventFlagId: int = ParamField(
        uint, "signPuddleOpenEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaNo: int = ParamField(
        byte, "areaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridXNo: int = ParamField(
        byte, "gridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridZNo: int = ParamField(
        byte, "gridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad4[1]")
    PosX: float = ParamField(
        float, "posX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosY: float = ParamField(
        float, "posY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosZ: float = ParamField(
        float, "posZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId1: int = ParamField(
        uint, "breakInLimitEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId1: int = ParamField(
        uint, "whiteSignLimitEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchAreaSignCreateLimitEventFlagId: int = ParamField(
        uint, "matchAreaSignCreateLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId1: int = ParamField(
        uint, "signAimId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId2: int = ParamField(
        uint, "signAimId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId3: int = ParamField(
        uint, "signAimId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId4: int = ParamField(
        uint, "signAimId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId5: int = ParamField(
        uint, "signAimId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId6: int = ParamField(
        uint, "signAimId_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId7: int = ParamField(
        uint, "signAimId_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId8: int = ParamField(
        uint, "signAimId_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId1: int = ParamField(
        uint, "redSignLimitEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId2: int = ParamField(
        uint, "breakInLimitEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId3: int = ParamField(
        uint, "breakInLimitEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId2: int = ParamField(
        uint, "whiteSignLimitEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId3: int = ParamField(
        uint, "whiteSignLimitEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId2: int = ParamField(
        uint, "redSignLimitEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId3: int = ParamField(
        uint, "redSignLimitEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId1: int = ParamField(
        uint, "bossId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId2: int = ParamField(
        uint, "bossId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId3: int = ParamField(
        uint, "bossId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId4: int = ParamField(
        uint, "bossId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId5: int = ParamField(
        uint, "bossId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId6: int = ParamField(
        uint, "bossId_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId7: int = ParamField(
        uint, "bossId_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId8: int = ParamField(
        uint, "bossId_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId9: int = ParamField(
        uint, "bossId_9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId10: int = ParamField(
        uint, "bossId_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId11: int = ParamField(
        uint, "bossId_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId12: int = ParamField(
        uint, "bossId_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId13: int = ParamField(
        uint, "bossId_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId14: int = ParamField(
        uint, "bossId_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId15: int = ParamField(
        uint, "bossId_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId16: int = ParamField(
        uint, "bossId_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapMenuUnlockEventId: int = ParamField(
        uint, "mapMenuUnlockEventId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(32, "pad5[32]")
