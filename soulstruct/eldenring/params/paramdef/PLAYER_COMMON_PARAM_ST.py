from __future__ import annotations

__all__ = ["PLAYER_COMMON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class PLAYER_COMMON_PARAM_ST(ParamRow):
    PlayerFootEffectbySFX: int = ParamField(
        int, "playerFootEffect_bySFX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SnipeModeDrawAlphaFadeTime: float = ParamField(
        float, "snipeModeDrawAlpha_FadeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessRecoverCorrection: float = ParamField(
        float, "toughnessRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseMagicSlotSize: int = ParamField(
        byte, "baseMagicSlotSize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseAccSlotNum: int = ParamField(
        byte, "baseAccSlotNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "reserved02[2]")
    AnimeIDDropItemPick: int = ParamField(
        int, "animeID_DropItemPick", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointSleepPlayer: float = ParamField(
        float, "resistRecoverPoint_Sleep_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FlareOverrideHomingAngle: int = ParamField(
        int, "flareOverrideHomingAngle", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlareOverrideHomingStopRange: float = ParamField(
        float, "flareOverrideHomingStopRange", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AnimeIDSleepCollectorItemPick: int = ParamField(
        int, "animeID_SleepCollectorItemPick", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnlockEventFlagBaseIdforWepAttr: int = ParamField(
        uint, "unlockEventFlagBaseId_forWepAttr", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SystemEnchantBigRune: int = ParamField(
        int, "systemEnchant_BigRune", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LowStatusAtkPowDown: float = ParamField(
        float, "lowStatus_AtkPowDown", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowStatusConsumeStaminaRate: float = ParamField(
        float, "lowStatus_ConsumeStaminaRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowStatusAtkGuardBreak: int = ParamField(
        short, "lowStatus_AtkGuardBreak", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardStatusCorrectMaxStatusVal: int = ParamField(
        short, "guardStatusCorrect_MaxStatusVal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnlockEventFlagStepNumforWepAttr: int = ParamField(
        ushort, "unlockEventFlagStepNum_forWepAttr", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicdamageCountNum: int = ParamField(
        ushort, "retributionMagic_damageCountNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicdamageCountRemainTime: int = ParamField(
        ushort, "retributionMagic_damageCountRemainTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicburstDmypolyId: int = ParamField(
        ushort, "retributionMagic_burstDmypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RetributionMagicburstMagicParamId: int = ParamField(
        int, "retributionMagic_burstMagicParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrAimCamrideOffsetHeight: float = ParamField(
        float, "chrAimCam_rideOffsetHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "reserved23[4]")
    ArrowCaseWepBindDmypolyId: int = ParamField(
        int, "arrowCaseWepBindDmypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BoltPouchWepBindDmypolyId: int = ParamField(
        int, "boltPouchWepBindDmypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskAllocateRate: float = ParamField(
        float, "estusFlaskAllocateRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "reserved38[2]")
    KickAcceptanceDeg: int = ParamField(
        byte, "kickAcceptanceDeg", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateLight: int = ParamField(
        byte, "npcPlayerAnalogWeightRate_Light", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateNormal: int = ParamField(
        byte, "npcPlayerAnalogWeightRate_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateHeavy: int = ParamField(
        byte, "npcPlayerAnalogWeightRate_Heavy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateWeightOver: int = ParamField(
        byte, "npcPlayerAnalogWeightRate_WeightOver", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerAnalogWeightRateSuperLight: int = ParamField(
        byte, "npcPlayerAnalogWeightRate_SuperLight", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "reserved45[4]")
    ClearCountCorrectBaseSpEffectId: int = ParamField(
        int, "clearCountCorrectBaseSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltModelIdOffset: int = ParamField(
        int, "arrowBoltModelIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltRemainingNumModelMaskThreshold1: int = ParamField(
        sbyte, "arrowBoltRemainingNumModelMaskThreshold1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltRemainingNumModelMaskThreshold2: int = ParamField(
        sbyte, "arrowBoltRemainingNumModelMaskThreshold2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(2, "reserved27[2]")
    ResistRecoverPointPoisionPlayer: float = ParamField(
        float, "resistRecoverPoint_Poision_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointDeseasePlayer: float = ParamField(
        float, "resistRecoverPoint_Desease_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointBloodPlayer: float = ParamField(
        float, "resistRecoverPoint_Blood_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointCursePlayer: float = ParamField(
        float, "resistRecoverPoint_Curse_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointFreezePlayer: float = ParamField(
        float, "resistRecoverPoint_Freeze_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointPoisionEnemy: float = ParamField(
        float, "resistRecoverPoint_Poision_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointDeseaseEnemy: float = ParamField(
        float, "resistRecoverPoint_Desease_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointBloodEnemy: float = ParamField(
        float, "resistRecoverPoint_Blood_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointCurseEnemy: float = ParamField(
        float, "resistRecoverPoint_Curse_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointFreezeEnemy: float = ParamField(
        float, "resistRecoverPoint_Freeze_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RequestTimeLeftBothHand: float = ParamField(
        float, "requestTimeLeftBothHand", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointMadnessPlayer: float = ParamField(
        float, "resistRecoverPoint_Madness_Player", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AnimeIDMaterialItemPick: int = ParamField(
        int, "animeID_MaterialItemPick", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskAllocateRateForYellowMonk: float = ParamField(
        float, "hpEstusFlaskAllocateRateForYellowMonk", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskAllocateOffsetForYellowMonk: int = ParamField(
        int, "hpEstusFlaskAllocateOffsetForYellowMonk", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskAllocateRateForYellowMonk: float = ParamField(
        float, "mpEstusFlaskAllocateRateForYellowMonk", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskAllocateOffsetForYellowMonk: int = ParamField(
        int, "mpEstusFlaskAllocateOffsetForYellowMonk", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointSleepEnemy: float = ParamField(
        float, "resistRecoverPoint_Sleep_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistRecoverPointMadnessEnemy: float = ParamField(
        float, "resistRecoverPoint_Madness_Enemy", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurseItemId: int = ParamField(
        int, "resistCurseItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurseItemMaxNum: int = ParamField(
        byte, "resistCurseItemMaxNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(3, "reserved_123[3]")
    ResistCurseItemSpEffectBaseId: int = ParamField(
        int, "resistCurseItemSpEffectBaseId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurseItemLotParamIdmap: int = ParamField(
        int, "resistCurseItemLotParamId_map", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(52, "reserved41[52]")
