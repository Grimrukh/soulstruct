from __future__ import annotations

__all__ = ["PLAYER_COMMON_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class PLAYER_COMMON_PARAM_ST(ParamRow):
    PlayerFootEffectbySFX: int = ParamField(
        int32, "playerFootEffect_bySFX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SnipeModeDrawAlphaFadeTime: float = ParamField(
        float32, "snipeModeDrawAlpha_FadeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessRecoverCorrection: float = ParamField(
        float32, "toughnessRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseMagicSlotSize: int = ParamField(
        uint8, "baseMagicSlotSize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseAccSlotNum: int = ParamField(
        uint8, "baseAccSlotNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "reserved02[2]")
    AnimeIDDropItemPick: int = ParamField(
        int32, "animeID_DropItemPick", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointSleepPlayer: float = ParamField(
        float32, "resistRecoverPoint_Sleep_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FlareOverrideHomingAngle: int = ParamField(
        int32, "flareOverrideHomingAngle", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlareOverrideHomingStopRange: float = ParamField(
        float32, "flareOverrideHomingStopRange", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AnimeIDSleepCollectorItemPick: int = ParamField(
        int32, "animeID_SleepCollectorItemPick", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnlockEventFlagBaseIdforWepAttr: int = ParamField(
        uint32, "unlockEventFlagBaseId_forWepAttr", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SystemEnchantBigRune: int = ParamField(
        int32, "systemEnchant_BigRune", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LowStatusAtkPowDown: float = ParamField(
        float32, "lowStatus_AtkPowDown", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowStatusConsumeStaminaRate: float = ParamField(
        float32, "lowStatus_ConsumeStaminaRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowStatusAtkGuardBreak: int = ParamField(
        int16, "lowStatus_AtkGuardBreak", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardStatusCorrectMaxStatusVal: int = ParamField(
        int16, "guardStatusCorrect_MaxStatusVal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnlockEventFlagStepNumforWepAttr: int = ParamField(
        uint16, "unlockEventFlagStepNum_forWepAttr", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicdamageCountNum: int = ParamField(
        uint16, "retributionMagic_damageCountNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicdamageCountRemainTime: int = ParamField(
        uint16, "retributionMagic_damageCountRemainTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicburstDmypolyId: int = ParamField(
        uint16, "retributionMagic_burstDmypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicburstMagicParamId: int = ParamField(
        int32, "retributionMagic_burstMagicParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrAimCamrideOffsetHeight: float = ParamField(
        float32, "chrAimCam_rideOffsetHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "reserved23[4]")
    ArrowCaseWepBindDmypolyId: int = ParamField(
        int32, "arrowCaseWepBindDmypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BoltPouchWepBindDmypolyId: int = ParamField(
        int32, "boltPouchWepBindDmypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskAllocateRate: float = ParamField(
        float32, "estusFlaskAllocateRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "reserved38[2]")
    KickAcceptanceDeg: int = ParamField(
        uint8, "kickAcceptanceDeg", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateLight: int = ParamField(
        uint8, "npcPlayerAnalogWeightRate_Light", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateNormal: int = ParamField(
        uint8, "npcPlayerAnalogWeightRate_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateHeavy: int = ParamField(
        uint8, "npcPlayerAnalogWeightRate_Heavy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateWeightOver: int = ParamField(
        uint8, "npcPlayerAnalogWeightRate_WeightOver", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateSuperLight: int = ParamField(
        uint8, "npcPlayerAnalogWeightRate_SuperLight", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "reserved45[4]")
    ClearCountCorrectBaseSpEffectId: int = ParamField(
        int32, "clearCountCorrectBaseSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltModelIdOffset: int = ParamField(
        int32, "arrowBoltModelIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltRemainingNumModelMaskThreshold1: int = ParamField(
        int8, "arrowBoltRemainingNumModelMaskThreshold1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltRemainingNumModelMaskThreshold2: int = ParamField(
        int8, "arrowBoltRemainingNumModelMaskThreshold2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(2, "reserved27[2]")
    ResistRecoverPointPoisionPlayer: float = ParamField(
        float32, "resistRecoverPoint_Poision_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointDeseasePlayer: float = ParamField(
        float32, "resistRecoverPoint_Desease_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointBloodPlayer: float = ParamField(
        float32, "resistRecoverPoint_Blood_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointCursePlayer: float = ParamField(
        float32, "resistRecoverPoint_Curse_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointFreezePlayer: float = ParamField(
        float32, "resistRecoverPoint_Freeze_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointPoisionEnemy: float = ParamField(
        float32, "resistRecoverPoint_Poision_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointDeseaseEnemy: float = ParamField(
        float32, "resistRecoverPoint_Desease_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointBloodEnemy: float = ParamField(
        float32, "resistRecoverPoint_Blood_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointCurseEnemy: float = ParamField(
        float32, "resistRecoverPoint_Curse_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointFreezeEnemy: float = ParamField(
        float32, "resistRecoverPoint_Freeze_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RequestTimeLeftBothHand: float = ParamField(
        float32, "requestTimeLeftBothHand", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointMadnessPlayer: float = ParamField(
        float32, "resistRecoverPoint_Madness_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AnimeIDMaterialItemPick: int = ParamField(
        int32, "animeID_MaterialItemPick", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskAllocateRateForYellowMonk: float = ParamField(
        float32, "hpEstusFlaskAllocateRateForYellowMonk", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskAllocateOffsetForYellowMonk: int = ParamField(
        int32, "hpEstusFlaskAllocateOffsetForYellowMonk", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskAllocateRateForYellowMonk: float = ParamField(
        float32, "mpEstusFlaskAllocateRateForYellowMonk", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskAllocateOffsetForYellowMonk: int = ParamField(
        int32, "mpEstusFlaskAllocateOffsetForYellowMonk", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointSleepEnemy: float = ParamField(
        float32, "resistRecoverPoint_Sleep_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointMadnessEnemy: float = ParamField(
        float32, "resistRecoverPoint_Madness_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurseItemId: int = ParamField(
        int32, "resistCurseItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurseItemMaxNum: int = ParamField(
        uint8, "resistCurseItemMaxNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(3, "reserved_123[3]")
    ResistCurseItemSpEffectBaseId: int = ParamField(
        int32, "resistCurseItemSpEffectBaseId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurseItemLotParamIdmap: int = ParamField(
        int32, "resistCurseItemLotParamId_map", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xcc: int = ParamField(
        int32, "unknown_0xcc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xd0: int = ParamField(
        int32, "unknown_0xd0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xd4: int = ParamField(
        int32, "unknown_0xd4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xd8: int = ParamField(
        int32, "unknown_0xd8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xdc: int = ParamField(
        int32, "unknown_0xdc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe0: int = ParamField(
        int32, "unknown_0xe0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(28, "reserved41[28]")
