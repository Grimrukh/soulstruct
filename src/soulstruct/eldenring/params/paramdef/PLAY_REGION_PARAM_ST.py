from __future__ import annotations

__all__ = ["PLAY_REGION_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class PLAY_REGION_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    MatchAreaId: int = ParamField(
        int32, "matchAreaId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayStartLimitEventFlagId: int = ParamField(
        uint32, "multiPlayStartLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OtherDisableDistance: float = ParamField(
        float32, "otherDisableDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PcPositionSaveLimitEventFlagId: int = ParamField(
        uint32, "pcPositionSaveLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossAreaId: int = ParamField(
        uint32, "bossAreaId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CultNpcWhiteGhostEntityIdbyFree: int = ParamField(
        int16, "cultNpcWhiteGhostEntityId_byFree", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BMapGuradianRegion: int = ParamField(
        uint8, "bMapGuradianRegion", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BYellowCostumeRegion: bool = ParamField(
        uint8, "bYellowCostumeRegion:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayStartLimitEventFlagIdtargetFlagState: bool = ParamField(
        uint8, "multiPlayStartLimitEventFlagId_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId1targetFlagState: bool = ParamField(
        uint8, "breakInLimitEventFlagId_1_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId1targetFlagState: bool = ParamField(
        uint8, "whiteSignLimitEventFlagId_1_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId1targetFlagState: bool = ParamField(
        uint8, "redSignLimitEventFlagId_1_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId2targetFlagState: bool = ParamField(
        uint8, "breakInLimitEventFlagId_2_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId3targetFlagState: bool = ParamField(
        uint8, "breakInLimitEventFlagId_3_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId2targetFlagState: bool = ParamField(
        uint8, "whiteSignLimitEventFlagId_2_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId1: int = ParamField(
        uint32, "warpItemUsePermitBonfireId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId2: int = ParamField(
        uint32, "warpItemUsePermitBonfireId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId3: int = ParamField(
        uint32, "warpItemUsePermitBonfireId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId4: int = ParamField(
        uint32, "warpItemUsePermitBonfireId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemUsePermitBonfireId5: int = ParamField(
        uint32, "warpItemUsePermitBonfireId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId1: int = ParamField(
        uint32, "warpItemProhibitionEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId2: int = ParamField(
        uint32, "warpItemProhibitionEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId3: int = ParamField(
        uint32, "warpItemProhibitionEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId4: int = ParamField(
        uint32, "warpItemProhibitionEventFlagId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WarpItemProhibitionEventFlagId5: int = ParamField(
        uint32, "warpItemProhibitionEventFlagId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodstain: bool = ParamField(
        uint8, "enableBloodstain:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableBloodMessage: bool = ParamField(
        uint8, "enableBloodMessage:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableGhost: bool = ParamField(
        uint8, "enableGhost:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    DispMask00: bool = ParamField(
        uint8, "dispMask00:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DispMask01: bool = ParamField(
        uint8, "dispMask01:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId3targetFlagState: bool = ParamField(
        uint8, "whiteSignLimitEventFlagId_3_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId2targetFlagState: bool = ParamField(
        uint8, "redSignLimitEventFlagId_2_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId3targetFlagState: bool = ParamField(
        uint8, "redSignLimitEventFlagId_3_targetFlagState:1", ON_OFF, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsAutoIntrudePoint: bool = ParamField(
        uint8, "isAutoIntrudePoint:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x451: bool = ParamField(
        uint8, "unknown_0x45_1:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad1:6", bit_count=6)
    _Pad1: bytes = ParamPad(2, "pad2[2]")
    MultiPlayHASHostLimitEventFlagId: int = ParamField(
        uint32, "multiPlayHASHostLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OtherMaxDistance: float = ParamField(
        float32, "otherMaxDistance", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleOpenEventFlagId: int = ParamField(
        uint32, "signPuddleOpenEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaNo: int = ParamField(
        uint8, "areaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridXNo: int = ParamField(
        uint8, "gridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridZNo: int = ParamField(
        uint8, "gridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad4[1]")
    PosX: float = ParamField(
        float32, "posX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosY: float = ParamField(
        float32, "posY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosZ: float = ParamField(
        float32, "posZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId1: int = ParamField(
        uint32, "breakInLimitEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId1: int = ParamField(
        uint32, "whiteSignLimitEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchAreaSignCreateLimitEventFlagId: int = ParamField(
        uint32, "matchAreaSignCreateLimitEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId1: int = ParamField(
        uint32, "signAimId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId2: int = ParamField(
        uint32, "signAimId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId3: int = ParamField(
        uint32, "signAimId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId4: int = ParamField(
        uint32, "signAimId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId5: int = ParamField(
        uint32, "signAimId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId6: int = ParamField(
        uint32, "signAimId_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId7: int = ParamField(
        uint32, "signAimId_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignAimId8: int = ParamField(
        uint32, "signAimId_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId1: int = ParamField(
        uint32, "redSignLimitEventFlagId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId2: int = ParamField(
        uint32, "breakInLimitEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInLimitEventFlagId3: int = ParamField(
        uint32, "breakInLimitEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId2: int = ParamField(
        uint32, "whiteSignLimitEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteSignLimitEventFlagId3: int = ParamField(
        uint32, "whiteSignLimitEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId2: int = ParamField(
        uint32, "redSignLimitEventFlagId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedSignLimitEventFlagId3: int = ParamField(
        uint32, "redSignLimitEventFlagId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId1: int = ParamField(
        uint32, "bossId_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId2: int = ParamField(
        uint32, "bossId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId3: int = ParamField(
        uint32, "bossId_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId4: int = ParamField(
        uint32, "bossId_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId5: int = ParamField(
        uint32, "bossId_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId6: int = ParamField(
        uint32, "bossId_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId7: int = ParamField(
        uint32, "bossId_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId8: int = ParamField(
        uint32, "bossId_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId9: int = ParamField(
        uint32, "bossId_9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId10: int = ParamField(
        uint32, "bossId_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId11: int = ParamField(
        uint32, "bossId_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId12: int = ParamField(
        uint32, "bossId_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId13: int = ParamField(
        uint32, "bossId_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId14: int = ParamField(
        uint32, "bossId_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId15: int = ParamField(
        uint32, "bossId_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BossId16: int = ParamField(
        uint32, "bossId_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapMenuUnlockEventId: int = ParamField(
        uint32, "mapMenuUnlockEventId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(32, "pad5[32]")
