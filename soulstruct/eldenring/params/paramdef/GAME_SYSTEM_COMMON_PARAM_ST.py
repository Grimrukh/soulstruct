from __future__ import annotations

__all__ = ["GAME_SYSTEM_COMMON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GAME_SYSTEM_COMMON_PARAM_ST(ParamRow):
    BaseToughnessRecoverTime: float = ParamField(
        float, "baseToughnessRecoverTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyLeft90: int = ParamField(
        int, "chrEventTrun_byLeft90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyRight90: int = ParamField(
        int, "chrEventTrun_byRight90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyLeft180: int = ParamField(
        int, "chrEventTrun_byLeft180", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyRight180: int = ParamField(
        int, "chrEventTrun_byRight180", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrun90TurnStartAngle: int = ParamField(
        short, "chrEventTrun_90TurnStartAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrun180TurnStartAngle: int = ParamField(
        short, "chrEventTrun_180TurnStartAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StealthAtkDamageRate: float = ParamField(
        float, "stealthAtkDamageRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FlickDamageCutRateSuccessGurad: float = ParamField(
        float, "flickDamageCutRateSuccessGurad", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NpcTalkAnimBeginDiffAngle: float = ParamField(
        float, "npcTalkAnimBeginDiffAngle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NpcTalkAnimEndDiffAngle: float = ParamField(
        float, "npcTalkAnimEndDiffAngle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorItemActionButtonParamId: int = ParamField(
        int, "sleepCollectorItemActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxInterval: float = ParamField(
        float, "allowUseBuddyItem_sfxInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxDmyPolyId: int = ParamField(
        int, "allowUseBuddyItem_sfxDmyPolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxDmyPolyIdhorse: int = ParamField(
        int, "allowUseBuddyItem_sfxDmyPolyId_horse", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxId: int = ParamField(
        int, "allowUseBuddyItem_sfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxInterval: float = ParamField(
        float, "onBuddySummon_inActivateRange_sfxInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxDmyPolyId: int = ParamField(
        int, "onBuddySummon_inActivateRange_sfxDmyPolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxDmyPolyIdhorse: int = ParamField(
        int, "onBuddySummon_inActivateRange_sfxDmyPolyId_horse", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxId: int = ParamField(
        int, "onBuddySummon_inActivateRange_sfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangespEffectIdpc: int = ParamField(
        int, "onBuddySummon_inActivateRange_spEffectId_pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninWarnRangespEffectIdpc: int = ParamField(
        int, "onBuddySummon_inWarnRange_spEffectId_pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummonatBuddyUnsummonspEffectIdpc: int = ParamField(
        int, "onBuddySummon_atBuddyUnsummon_spEffectId_pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninWarnRangespEffectIdbuddy: int = ParamField(
        int, "onBuddySummon_inWarnRange_spEffectId_buddy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MorningIngameHour: int = ParamField(
        byte, "morningIngameHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MorningIngameMinute: int = ParamField(
        byte, "morningIngameMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MorningIngameSecond: int = ParamField(
        byte, "morningIngameSecond", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoonIngameHour: int = ParamField(
        byte, "noonIngameHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoonIngameMinute: int = ParamField(
        byte, "noonIngameMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoonIngameSecond: int = ParamField(
        byte, "noonIngameSecond", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NightIngameHour: int = ParamField(
        byte, "nightIngameHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NightIngameMinute: int = ParamField(
        byte, "nightIngameMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NightIngameSecond: int = ParamField(
        byte, "nightIngameSecond", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMorningHour: int = ParamField(
        byte, "aiSightRateStart_Morning_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMorningMinute: int = ParamField(
        byte, "aiSightRateStart_Morning_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNoonHour: int = ParamField(
        byte, "aiSightRateStart_Noon_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNoonMinute: int = ParamField(
        byte, "aiSightRateStart_Noon_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartEveningHour: int = ParamField(
        byte, "aiSightRateStart_Evening_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartEveningMinute: int = ParamField(
        byte, "aiSightRateStart_Evening_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNightHour: int = ParamField(
        byte, "aiSightRateStart_Night_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNightMinute: int = ParamField(
        byte, "aiSightRateStart_Night_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMidnightHour: int = ParamField(
        byte, "aiSightRateStart_Midnight_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMidnightMinute: int = ParamField(
        byte, "aiSightRateStart_Midnight_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxThreshold: int = ParamField(
        byte, "saLargeDamageHitSfx_Threshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxSfxId: int = ParamField(
        int, "saLargeDamageHitSfx_SfxId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignCreatableDistFromSafePos: float = ParamField(
        float, "signCreatableDistFromSafePos", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestResummonDist: float = ParamField(
        float, "guestResummonDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestLeavingMessageDistMax: float = ParamField(
        float, "guestLeavingMessageDistMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestLeavingMessageDistMin: float = ParamField(
        float, "guestLeavingMessageDistMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestLeaveSessionDist: float = ParamField(
        float, "guestLeaveSessionDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointAreaRadius: float = ParamField(
        float, "retryPointAreaRadius", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorSpEffectId: int = ParamField(
        int, "sleepCollectorSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RecoverBelowMaxHpCompletionNoticeSpEffectId: int = ParamField(
        int, "recoverBelowMaxHpCompletionNoticeSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryAbsorptionProductionSfxIdbyHp: int = ParamField(
        int, "estusFlaskRecovery_AbsorptionProductionSfxId_byHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryAbsorptionProductionSfxIdbyMp: int = ParamField(
        int, "estusFlaskRecovery_AbsorptionProductionSfxId_byMp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RespawnSpecialEffectActiveCheckerSpEffectId: int = ParamField(
        int, "respawnSpecialEffectActiveCheckerSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangespEffectIdbuddy: int = ParamField(
        int, "onBuddySummon_inActivateRange_spEffectId_buddy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryAddEstusTime: float = ParamField(
        float, "estusFlaskRecovery_AddEstusTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeEnemyOfSoulCorrectRatebyHost: float = ParamField(
        float, "defeatMultiModeEnemyOfSoulCorrectRate_byHost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeEnemyOfSoulCorrectRatebyTeamGhost: float = ParamField(
        float, "defeatMultiModeEnemyOfSoulCorrectRate_byTeamGhost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeBossOfSoulCorrectRatebyHost: float = ParamField(
        float, "defeatMultiModeBossOfSoulCorrectRate_byHost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeBossOfSoulCorrectRatebyTeamGhost: float = ParamField(
        float, "defeatMultiModeBossOfSoulCorrectRate_byTeamGhost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyHpGaugeScreenOffsetbyUp: int = ParamField(
        ushort, "enemyHpGaugeScreenOffset_byUp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayRegionCollectDist: int = ParamField(
        ushort, "playRegionCollectDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectShootBulletDummypolyId: int = ParamField(
        ushort, "enemyDetectionSpEffect_ShootBulletDummypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonBreakInGoodsNum: int = ParamField(
        ushort, "bigRuneGreaterDemonBreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonBreakInGoodsId: int = ParamField(
        int, "bigRuneGreaterDemonBreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpRegionDefaultSfxId: int = ParamField(
        int, "rideJumpRegionDefaultSfxId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaAttackRateforVsRideAtk: float = ParamField(
        float, "saAttackRate_forVsRideAtk", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemySpEffectIdAfterSleepCollectorItemLot: int = ParamField(
        int, "enemySpEffectIdAfterSleepCollectorItemLot", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AfterEndingMapUid: int = ParamField(
        int, "afterEndingMapUid", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AfterEndingReturnPointEntityId: int = ParamField(
        uint, "afterEndingReturnPointEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectBulletIdbyCoopRingRedHunter: int = ParamField(
        int, "enemyDetectionSpEffect_BulletId_byCoopRing_RedHunter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectBulletIdbyInvadeOrbNone: int = ParamField(
        int, "enemyDetectionSpEffect_BulletId_byInvadeOrb_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnAccessDistView: int = ParamField(
        uint, "tutorialFlagOnAccessDistView", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnAccessRetryPoint: int = ParamField(
        uint, "tutorialFlagOnAccessRetryPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnGetGroupReward: int = ParamField(
        uint, "tutorialFlagOnGetGroupReward", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnEnterRideJumpRegion: int = ParamField(
        uint, "tutorialFlagOnEnterRideJumpRegion", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialCheckRideJumpRegionExpandRange: float = ParamField(
        float, "tutorialCheckRideJumpRegionExpandRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointActivatedPcAnimId: int = ParamField(
        int, "retryPointActivatedPcAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointActivatedDialogDelayTime: float = ParamField(
        float, "retryPointActivatedDialogDelayTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointActivatedDialogTextId: int = ParamField(
        int, "retryPointActivatedDialogTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleOpenPcAnimId: int = ParamField(
        int, "signPuddleOpenPcAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleOpenDialogDelayTime: float = ParamField(
        float, "signPuddleOpenDialogDelayTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadSpEffectBulletId: int = ParamField(
        int, "activityOfDeadSpEffect_BulletId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadSpEffectShootBulletDummypolyId: int = ParamField(
        int, "activityOfDeadSpEffect_ShootBulletDummypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadSpEffectDeadFadeOutTime: float = ParamField(
        float, "activityOfDeadSpEffect_DeadFadeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IgnorNetStateSyncTimeForThrow: float = ParamField(
        float, "ignorNetStateSyncTime_ForThrow", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointLanDisconnect: int = ParamField(
        ushort, "netPenaltyPointLanDisconnect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointProfileSignout: int = ParamField(
        ushort, "netPenaltyPointProfileSignout", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointReboot: int = ParamField(
        ushort, "netPenaltyPointReboot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPnaltyPointSuspend: int = ParamField(
        ushort, "netPnaltyPointSuspend", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyForgiveItemLimitTime: float = ParamField(
        float, "netPenaltyForgiveItemLimitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointThreshold: int = ParamField(
        ushort, "netPenaltyPointThreshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UncontrolledMoveThresholdTime: int = ParamField(
        ushort, "uncontrolledMoveThresholdTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectBulletIdbyNpcEnemy: int = ParamField(
        int, "enemyDetectionSpEffect_BulletId_byNpcEnemy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadTargetSearchSpEffectOnHitSpEffect: int = ParamField(
        int, "activityOfDeadTargetSearchSpEffect_OnHitSpEffect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadTargetSearchSpEffectMaxLength: float = ParamField(
        float, "activityOfDeadTargetSearchSpEffect_MaxLength", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightRangeLowerPromiseRate: float = ParamField(
        float, "sightRangeLowerPromiseRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxMinDamage: int = ParamField(
        short, "saLargeDamageHitSfx_MinDamage", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxForceDamage: int = ParamField(
        short, "saLargeDamageHitSfx_ForceDamage", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoloBreakInMaxPoint: int = ParamField(
        uint, "soloBreakInMaxPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcTalkTimeOutThreshold: float = ParamField(
        float, "npcTalkTimeOutThreshold", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SendPlayLogIntervalTime: float = ParamField(
        float, "sendPlayLogIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Item370MaxSfxNum: int = ParamField(
        byte, "item370_MaxSfxNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrActivateDistforLeavePC: int = ParamField(
        byte, "chrActivateDist_forLeavePC", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonDataCoopMatchingLevelUpperAbs: int = ParamField(
        short, "summonDataCoopMatchingLevelUpperAbs", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonDataCoopMatchingLevelUpperRel: int = ParamField(
        short, "summonDataCoopMatchingLevelUpperRel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonDataCoopMatchingWepLevelMul: int = ParamField(
        short, "summonDataCoopMatchingWepLevelMul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PickUpBerserkerSignSpEffectBulletId: int = ParamField(
        int, "pickUpBerserkerSignSpEffectBulletId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SucceedBerserkerSelfKillingEffectId: int = ParamField(
        int, "succeedBerserkerSelfKillingEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelWhiteSignUpperRel: int = ParamField(
        byte, "machingLevelWhiteSignUpperRel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelWhiteSignUpperAbs: int = ParamField(
        byte, "machingLevelWhiteSignUpperAbs", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelRedSignUpperRel: int = ParamField(
        byte, "machingLevelRedSignUpperRel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelRedSignUpperAbs: int = ParamField(
        byte, "machingLevelRedSignUpperAbs", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign0: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign1: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign2: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign3: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign4: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign5: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign6: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign7: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign8: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign9: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign10: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign0: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign1: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign2: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign3: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign4: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign5: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign6: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign7: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign8: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign9: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign10: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoInvadePointgenerateDist: int = ParamField(
        byte, "autoInvadePoint_generateDist", default=40,
        tooltip="TOOLTIP-TODO",
    )
    AutoInvadePointcancelDist: int = ParamField(
        byte, "autoInvadePoint_cancelDist", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SendGlobalEventLogIntervalTime: float = ParamField(
        float, "sendGlobalEventLogIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointWhite: int = ParamField(
        ushort, "addSoloBreakInPoint_White", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointBlack: int = ParamField(
        ushort, "addSoloBreakInPoint_Black", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointForceJoin: int = ParamField(
        ushort, "addSoloBreakInPoint_ForceJoin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointVisitorGuardian: int = ParamField(
        ushort, "addSoloBreakInPoint_VisitorGuardian", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointVisitorRedHunter: int = ParamField(
        ushort, "addSoloBreakInPoint_VisitorRedHunter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvincibleTimerforNetPCinitSync: int = ParamField(
        byte, "invincibleTimer_forNetPC_initSync", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvincibleTimerforNetPC: int = ParamField(
        byte, "invincibleTimer_forNetPC", default=10,
        tooltip="TOOLTIP-TODO",
    )
    RedHunterHostBossAreaGetSoulRate: float = ParamField(
        float, "redHunter_HostBossAreaGetSoulRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GhostFootprintDecalParamId: int = ParamField(
        int, "ghostFootprintDecalParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeaveAroundHostWarningTime: float = ParamField(
        float, "leaveAroundHostWarningTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HostModeCostItemId: int = ParamField(
        int, "hostModeCostItemId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AIJumpDecelerateParam: float = ParamField(
        float, "aIJump_DecelerateParam", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyDisappearDelaySec: float = ParamField(
        float, "buddyDisappearDelaySec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AIJumpAnimYMoveCorrectRateonJumpOff: float = ParamField(
        float, "aIJump_AnimYMoveCorrectRate_onJumpOff", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateNotInStealthRigidNotSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightRate_NotInStealthRigid_NotSightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateNotInStealthRigidSightHideNotStealthMode: float = ParamField(
        float, "stealthSystemSightRate_NotInStealthRigid_SightHide_NotStealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateNotInStealthRigidSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightRate_NotInStealthRigid_SightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidNotSightHideNotStealthMode: float = ParamField(
        float, "stealthSystemSightRate_InStealthRigid_NotSightHide_NotStealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidNotSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightRate_InStealthRigid_NotSightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidSightHideNotStealthMode: float = ParamField(
        float, "stealthSystemSightRate_InStealthRigid_SightHide_NotStealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightRate_InStealthRigid_SightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoactionButtonParamIdcorpse: int = ParamField(
        int, "msbEventGeomTreasureInfo_actionButtonParamId_corpse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoitemGetAnimIdcorpse: int = ParamField(
        int, "msbEventGeomTreasureInfo_itemGetAnimId_corpse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoactionButtonParamIdbox: int = ParamField(
        int, "msbEventGeomTreasureInfo_actionButtonParamId_box", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoitemGetAnimIdbox: int = ParamField(
        int, "msbEventGeomTreasureInfo_itemGetAnimId_box", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoactionButtonParamIdshine: int = ParamField(
        int, "msbEventGeomTreasureInfo_actionButtonParamId_shine", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoitemGetAnimIdshine: int = ParamField(
        int, "msbEventGeomTreasureInfo_itemGetAnimId_shine", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAssetId: int = ParamField(
        int, "signPuddleAssetId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId0: int = ParamField(
        int, "signPuddleAppearDmypolyId0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId1: int = ParamField(
        int, "signPuddleAppearDmypolyId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId2: int = ParamField(
        int, "signPuddleAppearDmypolyId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId3: int = ParamField(
        int, "signPuddleAppearDmypolyId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageRateforRidePC: float = ParamField(
        float, "fallDamageRate_forRidePC", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageRateforRideNPC: float = ParamField(
        float, "fallDamageRate_forRideNPC", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    OldMonkOfYellowCreateSignSpEffectId: int = ParamField(
        int, "OldMonkOfYellow_CreateSignSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StragglerActivateDist: float = ParamField(
        float, "StragglerActivateDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdEnableUseItemStragglerActivate: int = ParamField(
        int, "SpEffectId_EnableUseItem_StragglerActivate", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdStragglerWakeUp: int = ParamField(
        int, "SpEffectId_StragglerWakeUp", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdStragglerTarget: int = ParamField(
        int, "SpEffectId_StragglerTarget", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdStragglerOppose: int = ParamField(
        int, "SpEffectId_StragglerOppose", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpTriggerTimeRayBlocked: float = ParamField(
        float, "buddyWarp_TriggerTimeRayBlocked", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpTriggerDistToPlayer: float = ParamField(
        float, "buddyWarp_TriggerDistToPlayer", default=25.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpThresholdTimePathStacked: float = ParamField(
        float, "buddyWarp_ThresholdTimePathStacked", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpThresholdRangePathStacked: float = ParamField(
        float, "buddyWarp_ThresholdRangePathStacked", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatemorning: float = ParamField(
        float, "aiSightRate_morning", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatenoonA: float = ParamField(
        float, "aiSightRate_noonA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyPassThroughTriggerTime: float = ParamField(
        float, "buddyPassThroughTriggerTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateevening: float = ParamField(
        float, "aiSightRate_evening", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatenight: float = ParamField(
        float, "aiSightRate_night", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatemidnightA: float = ParamField(
        float, "aiSightRate_midnightA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserve4_2[4]")
    AiSightRatesunlosslight: float = ParamField(
        float, "aiSightRate_sunloss_light", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatesunlossdark: float = ParamField(
        float, "aiSightRate_sunloss_dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatesunlossveryDark: float = ParamField(
        float, "aiSightRate_sunloss_veryDark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateNotInStealthRigidNotSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightAngleReduceRate_NotInStealthRigid_NotSightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateNotInStealthRigidSightHideNotStealthMode: float = ParamField(
        float, "stealthSystemSightAngleReduceRate_NotInStealthRigid_SightHide_NotStealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateNotInStealthRigidSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightAngleReduceRate_NotInStealthRigid_SightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidNotSightHideNotStealthMode: float = ParamField(
        float, "stealthSystemSightAngleReduceRate_InStealthRigid_NotSightHide_NotStealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidNotSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightAngleReduceRate_InStealthRigid_NotSightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidSightHideNotStealthMode: float = ParamField(
        float, "stealthSystemSightAngleReduceRate_InStealthRigid_SightHide_NotStealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidSightHideStealthMode: float = ParamField(
        float, "stealthSystemSightAngleReduceRate_InStealthRigid_SightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartMorningHour: int = ParamField(
        byte, "weatherLotConditionStart_Morning_Hour", default=7,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartMorningMinute: int = ParamField(
        byte, "weatherLotConditionStart_Morning_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayHour: int = ParamField(
        byte, "weatherLotConditionStart_Day_Hour", default=12,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayMinute: int = ParamField(
        byte, "weatherLotConditionStart_Day_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartEveningHour: int = ParamField(
        byte, "weatherLotConditionStart_Evening_Hour", default=17,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartEveningMinute: int = ParamField(
        byte, "weatherLotConditionStart_Evening_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartNightHour: int = ParamField(
        byte, "weatherLotConditionStart_Night_Hour", default=19,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartNightMinute: int = ParamField(
        byte, "weatherLotConditionStart_Night_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayBreakHour: int = ParamField(
        byte, "weatherLotConditionStart_DayBreak_Hour", default=5,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayBreakMinute: int = ParamField(
        byte, "weatherLotConditionStart_DayBreak_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "weatherLotCondition_reserved[2]")
    PclightScaleChangeStartHour: int = ParamField(
        byte, "pclightScaleChangeStart_Hour", default=18,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleChangeStartMinute: int = ParamField(
        byte, "pclightScaleChangeStart_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleChangeEndHour: int = ParamField(
        byte, "pclightScaleChangeEnd_Hour", default=5,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleChangeEndMinute: int = ParamField(
        byte, "pclightScaleChangeEnd_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleByTimezone: float = ParamField(
        float, "pclightScaleByTimezone", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonSummonBuddySpecialEffectIdBuddy: int = ParamField(
        int, "bigRuneGreaterDemon_SummonBuddySpecialEffectId_Buddy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonSummonBuddySpecialEffectIdPc: int = ParamField(
        int, "bigRuneGreaterDemon_SummonBuddySpecialEffectId_Pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HomeBonfireParamId: int = ParamField(
        int, "homeBonfireParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign11: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign12: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign13: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign14: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign15: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign16: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign17: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign18: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign19: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign20: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign21: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign22: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign23: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign24: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign25: int = ParamField(
        byte, "machingWeaponLevelUpperWhiteSign_25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign11: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign12: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign13: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign14: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign15: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign16: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign17: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign18: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign19: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign20: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign21: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign22: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign23: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign24: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign25: int = ParamField(
        byte, "machingWeaponLevelUpperRedSign_25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMorningHour: int = ParamField(
        byte, "menuTimezoneStart_Morning_Hour", default=7,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMorningMinute: int = ParamField(
        byte, "menuTimezoneStart_Morning_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay1Hour: int = ParamField(
        byte, "menuTimezoneStart_Day1_Hour", default=12,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay1Minute: int = ParamField(
        byte, "menuTimezoneStart_Day1_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay2Hour: int = ParamField(
        byte, "menuTimezoneStart_Day2_Hour", default=12,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay2Minute: int = ParamField(
        byte, "menuTimezoneStart_Day2_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartEveningHour: int = ParamField(
        byte, "menuTimezoneStart_Evening_Hour", default=17,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartEveningMinute: int = ParamField(
        byte, "menuTimezoneStart_Evening_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartNightHour: int = ParamField(
        byte, "menuTimezoneStart_Night_Hour", default=19,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartNightMinute: int = ParamField(
        byte, "menuTimezoneStart_Night_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMidnightHour: int = ParamField(
        byte, "menuTimezoneStart_Midnight_Hour", default=5,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMidnightMinute: int = ParamField(
        byte, "menuTimezoneStart_Midnight_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyThreatLv: int = ParamField(
        ushort, "remotePlayerThreatLvNotify_ThreatLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyNotifyDist: float = ParamField(
        float, "remotePlayerThreatLvNotify_NotifyDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyEndNotifyDist: float = ParamField(
        float, "remotePlayerThreatLvNotify_EndNotifyDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapPointDiscoveryExpandRange: float = ParamField(
        float, "worldMapPointDiscoveryExpandRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapPointReentryExpandRange: float = ParamField(
        float, "worldMapPointReentryExpandRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyNotifyTime: int = ParamField(
        ushort, "remotePlayerThreatLvNotify_NotifyTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInArebreakInGoodsNum: int = ParamField(
        ushort, "breakIn_A_rebreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInArebreakInGoodsId: int = ParamField(
        int, "breakIn_A_rebreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSfxId: int = ParamField(
        int, "rideJumpoff_SfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSfxHeightOffset: float = ParamField(
        float, "rideJumpoff_SfxHeightOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSpEffectId: int = ParamField(
        int, "rideJumpoff_SpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSpEffectIdPc: int = ParamField(
        int, "rideJumpoff_SpEffectIdPc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UnlockExchangeMenuEventFlagId: int = ParamField(
        uint, "unlockExchangeMenuEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnlockMessageMenuEventFlagId: int = ParamField(
        uint, "unlockMessageMenuEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInOnceArebreakInGoodsNum: int = ParamField(
        ushort, "breakInOnce_A_rebreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInBrebreakInGoodsNum: int = ParamField(
        ushort, "breakIn_B_rebreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInOnceArebreakInGoodsId: int = ParamField(
        int, "breakInOnce_A_rebreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakInBrebreakInGoodsId: int = ParamField(
        int, "breakIn_B_rebreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActionButtonInputCancelTime: float = ParamField(
        float, "actionButtonInputCancelTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlockClearBonusDelayTime: float = ParamField(
        float, "blockClearBonusDelayTime", default=7.0,
        tooltip="TOOLTIP-TODO",
    )
    BonfireCheckEnemyRange: float = ParamField(
        float, "bonfireCheckEnemyRange", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(128, "reserved_124[128]")
