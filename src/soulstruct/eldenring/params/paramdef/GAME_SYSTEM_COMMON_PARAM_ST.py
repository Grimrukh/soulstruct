from __future__ import annotations

__all__ = ["GAME_SYSTEM_COMMON_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class GAME_SYSTEM_COMMON_PARAM_ST(ParamRow):
    BaseToughnessRecoverTime: float = ParamField(
        float32, "baseToughnessRecoverTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyLeft90: int = ParamField(
        int32, "chrEventTrun_byLeft90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyRight90: int = ParamField(
        int32, "chrEventTrun_byRight90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyLeft180: int = ParamField(
        int32, "chrEventTrun_byLeft180", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrunbyRight180: int = ParamField(
        int32, "chrEventTrun_byRight180", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrun90TurnStartAngle: int = ParamField(
        int16, "chrEventTrun_90TurnStartAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrEventTrun180TurnStartAngle: int = ParamField(
        int16, "chrEventTrun_180TurnStartAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StealthAtkDamageRate: float = ParamField(
        float32, "stealthAtkDamageRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FlickDamageCutRateSuccessGurad: float = ParamField(
        float32, "flickDamageCutRateSuccessGurad", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NpcTalkAnimBeginDiffAngle: float = ParamField(
        float32, "npcTalkAnimBeginDiffAngle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NpcTalkAnimEndDiffAngle: float = ParamField(
        float32, "npcTalkAnimEndDiffAngle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorItemActionButtonParamId: int = ParamField(
        int32, "sleepCollectorItemActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxInterval: float = ParamField(
        float32, "allowUseBuddyItem_sfxInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxDmyPolyId: int = ParamField(
        int32, "allowUseBuddyItem_sfxDmyPolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxDmyPolyIdhorse: int = ParamField(
        int32, "allowUseBuddyItem_sfxDmyPolyId_horse", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AllowUseBuddyItemsfxId: int = ParamField(
        int32, "allowUseBuddyItem_sfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxInterval: float = ParamField(
        float32, "onBuddySummon_inActivateRange_sfxInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxDmyPolyId: int = ParamField(
        int32, "onBuddySummon_inActivateRange_sfxDmyPolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxDmyPolyIdhorse: int = ParamField(
        int32, "onBuddySummon_inActivateRange_sfxDmyPolyId_horse", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangesfxId: int = ParamField(
        int32, "onBuddySummon_inActivateRange_sfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangespEffectIdpc: int = ParamField(
        int32, "onBuddySummon_inActivateRange_spEffectId_pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninWarnRangespEffectIdpc: int = ParamField(
        int32, "onBuddySummon_inWarnRange_spEffectId_pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummonatBuddyUnsummonspEffectIdpc: int = ParamField(
        int32, "onBuddySummon_atBuddyUnsummon_spEffectId_pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninWarnRangespEffectIdbuddy: int = ParamField(
        int32, "onBuddySummon_inWarnRange_spEffectId_buddy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MorningIngameHour: int = ParamField(
        uint8, "morningIngameHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MorningIngameMinute: int = ParamField(
        uint8, "morningIngameMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MorningIngameSecond: int = ParamField(
        uint8, "morningIngameSecond", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoonIngameHour: int = ParamField(
        uint8, "noonIngameHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoonIngameMinute: int = ParamField(
        uint8, "noonIngameMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoonIngameSecond: int = ParamField(
        uint8, "noonIngameSecond", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NightIngameHour: int = ParamField(
        uint8, "nightIngameHour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NightIngameMinute: int = ParamField(
        uint8, "nightIngameMinute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NightIngameSecond: int = ParamField(
        uint8, "nightIngameSecond", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMorningHour: int = ParamField(
        uint8, "aiSightRateStart_Morning_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMorningMinute: int = ParamField(
        uint8, "aiSightRateStart_Morning_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNoonHour: int = ParamField(
        uint8, "aiSightRateStart_Noon_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNoonMinute: int = ParamField(
        uint8, "aiSightRateStart_Noon_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartEveningHour: int = ParamField(
        uint8, "aiSightRateStart_Evening_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartEveningMinute: int = ParamField(
        uint8, "aiSightRateStart_Evening_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNightHour: int = ParamField(
        uint8, "aiSightRateStart_Night_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartNightMinute: int = ParamField(
        uint8, "aiSightRateStart_Night_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMidnightHour: int = ParamField(
        uint8, "aiSightRateStart_Midnight_Hour", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateStartMidnightMinute: int = ParamField(
        uint8, "aiSightRateStart_Midnight_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxThreshold: int = ParamField(
        uint8, "saLargeDamageHitSfx_Threshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxSfxId: int = ParamField(
        int32, "saLargeDamageHitSfx_SfxId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignCreatableDistFromSafePos: float = ParamField(
        float32, "signCreatableDistFromSafePos", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestResummonDist: float = ParamField(
        float32, "guestResummonDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestLeavingMessageDistMax: float = ParamField(
        float32, "guestLeavingMessageDistMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestLeavingMessageDistMin: float = ParamField(
        float32, "guestLeavingMessageDistMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestLeaveSessionDist: float = ParamField(
        float32, "guestLeaveSessionDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointAreaRadius: float = ParamField(
        float32, "retryPointAreaRadius", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorSpEffectId: int = ParamField(
        int32, "sleepCollectorSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RecoverBelowMaxHpCompletionNoticeSpEffectId: int = ParamField(
        int32, "recoverBelowMaxHpCompletionNoticeSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryAbsorptionProductionSfxIdbyHp: int = ParamField(
        int32, "estusFlaskRecovery_AbsorptionProductionSfxId_byHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryAbsorptionProductionSfxIdbyMp: int = ParamField(
        int32, "estusFlaskRecovery_AbsorptionProductionSfxId_byMp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RespawnSpecialEffectActiveCheckerSpEffectId: int = ParamField(
        int32, "respawnSpecialEffectActiveCheckerSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OnBuddySummoninActivateRangespEffectIdbuddy: int = ParamField(
        int32, "onBuddySummon_inActivateRange_spEffectId_buddy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryAddEstusTime: float = ParamField(
        float32, "estusFlaskRecovery_AddEstusTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeEnemyOfSoulCorrectRatebyHost: float = ParamField(
        float32, "defeatMultiModeEnemyOfSoulCorrectRate_byHost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeEnemyOfSoulCorrectRatebyTeamGhost: float = ParamField(
        float32, "defeatMultiModeEnemyOfSoulCorrectRate_byTeamGhost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeBossOfSoulCorrectRatebyHost: float = ParamField(
        float32, "defeatMultiModeBossOfSoulCorrectRate_byHost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefeatMultiModeBossOfSoulCorrectRatebyTeamGhost: float = ParamField(
        float32, "defeatMultiModeBossOfSoulCorrectRate_byTeamGhost", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyHpGaugeScreenOffsetbyUp: int = ParamField(
        uint16, "enemyHpGaugeScreenOffset_byUp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayRegionCollectDist: int = ParamField(
        uint16, "playRegionCollectDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectShootBulletDummypolyId: int = ParamField(
        uint16, "enemyDetectionSpEffect_ShootBulletDummypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonBreakInGoodsNum: int = ParamField(
        uint16, "bigRuneGreaterDemonBreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonBreakInGoodsId: int = ParamField(
        int32, "bigRuneGreaterDemonBreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpRegionDefaultSfxId: int = ParamField(
        int32, "rideJumpRegionDefaultSfxId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaAttackRateforVsRideAtk: float = ParamField(
        float32, "saAttackRate_forVsRideAtk", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemySpEffectIdAfterSleepCollectorItemLot: int = ParamField(
        int32, "enemySpEffectIdAfterSleepCollectorItemLot", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AfterEndingMapUid: int = ParamField(
        int32, "afterEndingMapUid", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AfterEndingReturnPointEntityId: int = ParamField(
        uint32, "afterEndingReturnPointEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectBulletIdbyCoopRingRedHunter: int = ParamField(
        int32, "enemyDetectionSpEffect_BulletId_byCoopRing_RedHunter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectBulletIdbyInvadeOrbNone: int = ParamField(
        int32, "enemyDetectionSpEffect_BulletId_byInvadeOrb_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnAccessDistView: int = ParamField(
        uint32, "tutorialFlagOnAccessDistView", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnAccessRetryPoint: int = ParamField(
        uint32, "tutorialFlagOnAccessRetryPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnGetGroupReward: int = ParamField(
        uint32, "tutorialFlagOnGetGroupReward", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialFlagOnEnterRideJumpRegion: int = ParamField(
        uint32, "tutorialFlagOnEnterRideJumpRegion", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialCheckRideJumpRegionExpandRange: float = ParamField(
        float32, "tutorialCheckRideJumpRegionExpandRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointActivatedPcAnimId: int = ParamField(
        int32, "retryPointActivatedPcAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointActivatedDialogDelayTime: float = ParamField(
        float32, "retryPointActivatedDialogDelayTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetryPointActivatedDialogTextId: int = ParamField(
        int32, "retryPointActivatedDialogTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleOpenPcAnimId: int = ParamField(
        int32, "signPuddleOpenPcAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleOpenDialogDelayTime: float = ParamField(
        float32, "signPuddleOpenDialogDelayTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadSpEffectBulletId: int = ParamField(
        int32, "activityOfDeadSpEffect_BulletId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadSpEffectShootBulletDummypolyId: int = ParamField(
        int32, "activityOfDeadSpEffect_ShootBulletDummypolyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadSpEffectDeadFadeOutTime: float = ParamField(
        float32, "activityOfDeadSpEffect_DeadFadeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IgnorNetStateSyncTimeForThrow: float = ParamField(
        float32, "ignorNetStateSyncTime_ForThrow", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointLanDisconnect: int = ParamField(
        uint16, "netPenaltyPointLanDisconnect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointProfileSignout: int = ParamField(
        uint16, "netPenaltyPointProfileSignout", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointReboot: int = ParamField(
        uint16, "netPenaltyPointReboot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPnaltyPointSuspend: int = ParamField(
        uint16, "netPnaltyPointSuspend", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyForgiveItemLimitTime: float = ParamField(
        float32, "netPenaltyForgiveItemLimitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NetPenaltyPointThreshold: int = ParamField(
        uint16, "netPenaltyPointThreshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UncontrolledMoveThresholdTime: int = ParamField(
        uint16, "uncontrolledMoveThresholdTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyDetectionSpEffectBulletIdbyNpcEnemy: int = ParamField(
        int32, "enemyDetectionSpEffect_BulletId_byNpcEnemy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadTargetSearchSpEffectOnHitSpEffect: int = ParamField(
        int32, "activityOfDeadTargetSearchSpEffect_OnHitSpEffect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActivityOfDeadTargetSearchSpEffectMaxLength: float = ParamField(
        float32, "activityOfDeadTargetSearchSpEffect_MaxLength", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightRangeLowerPromiseRate: float = ParamField(
        float32, "sightRangeLowerPromiseRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxMinDamage: int = ParamField(
        int16, "saLargeDamageHitSfx_MinDamage", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SaLargeDamageHitSfxForceDamage: int = ParamField(
        int16, "saLargeDamageHitSfx_ForceDamage", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoloBreakInMaxPoint: int = ParamField(
        uint32, "soloBreakInMaxPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcTalkTimeOutThreshold: float = ParamField(
        float32, "npcTalkTimeOutThreshold", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SendPlayLogIntervalTime: float = ParamField(
        float32, "sendPlayLogIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Item370MaxSfxNum: int = ParamField(
        uint8, "item370_MaxSfxNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrActivateDistforLeavePC: int = ParamField(
        uint8, "chrActivateDist_forLeavePC", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonDataCoopMatchingLevelUpperAbs: int = ParamField(
        int16, "summonDataCoopMatchingLevelUpperAbs", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonDataCoopMatchingLevelUpperRel: int = ParamField(
        int16, "summonDataCoopMatchingLevelUpperRel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonDataCoopMatchingWepLevelMul: int = ParamField(
        int16, "summonDataCoopMatchingWepLevelMul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PickUpBerserkerSignSpEffectBulletId: int = ParamField(
        int32, "pickUpBerserkerSignSpEffectBulletId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SucceedBerserkerSelfKillingEffectId: int = ParamField(
        int32, "succeedBerserkerSelfKillingEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelWhiteSignUpperRel: int = ParamField(
        uint8, "machingLevelWhiteSignUpperRel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelWhiteSignUpperAbs: int = ParamField(
        uint8, "machingLevelWhiteSignUpperAbs", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelRedSignUpperRel: int = ParamField(
        uint8, "machingLevelRedSignUpperRel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingLevelRedSignUpperAbs: int = ParamField(
        uint8, "machingLevelRedSignUpperAbs", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign0: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign1: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign2: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign3: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign4: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign5: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign6: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign7: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign8: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign9: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign10: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign0: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign1: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign2: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign3: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign4: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign5: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign6: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign7: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign8: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign9: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign10: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoInvadePointgenerateDist: int = ParamField(
        uint8, "autoInvadePoint_generateDist", default=40,
        tooltip="TOOLTIP-TODO",
    )
    AutoInvadePointcancelDist: int = ParamField(
        uint8, "autoInvadePoint_cancelDist", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SendGlobalEventLogIntervalTime: float = ParamField(
        float32, "sendGlobalEventLogIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointWhite: int = ParamField(
        uint16, "addSoloBreakInPoint_White", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointBlack: int = ParamField(
        uint16, "addSoloBreakInPoint_Black", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointForceJoin: int = ParamField(
        uint16, "addSoloBreakInPoint_ForceJoin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointVisitorGuardian: int = ParamField(
        uint16, "addSoloBreakInPoint_VisitorGuardian", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddSoloBreakInPointVisitorRedHunter: int = ParamField(
        uint16, "addSoloBreakInPoint_VisitorRedHunter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvincibleTimerforNetPCinitSync: int = ParamField(
        uint8, "invincibleTimer_forNetPC_initSync", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvincibleTimerforNetPC: int = ParamField(
        uint8, "invincibleTimer_forNetPC", default=10,
        tooltip="TOOLTIP-TODO",
    )
    RedHunterHostBossAreaGetSoulRate: float = ParamField(
        float32, "redHunter_HostBossAreaGetSoulRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GhostFootprintDecalParamId: int = ParamField(
        int32, "ghostFootprintDecalParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeaveAroundHostWarningTime: float = ParamField(
        float32, "leaveAroundHostWarningTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HostModeCostItemId: int = ParamField(
        int32, "hostModeCostItemId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AIJumpDecelerateParam: float = ParamField(
        float32, "aIJump_DecelerateParam", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyDisappearDelaySec: float = ParamField(
        float32, "buddyDisappearDelaySec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AIJumpAnimYMoveCorrectRateonJumpOff: float = ParamField(
        float32, "aIJump_AnimYMoveCorrectRate_onJumpOff", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateNotInStealthRigidNotSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightRate_NotInStealthRigid_NotSightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateNotInStealthRigidSightHideNotStealthMode: float = ParamField(
        float32, "stealthSystemSightRate_NotInStealthRigid_SightHide_NotStealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateNotInStealthRigidSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightRate_NotInStealthRigid_SightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidNotSightHideNotStealthMode: float = ParamField(
        float32, "stealthSystemSightRate_InStealthRigid_NotSightHide_NotStealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidNotSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightRate_InStealthRigid_NotSightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidSightHideNotStealthMode: float = ParamField(
        float32, "stealthSystemSightRate_InStealthRigid_SightHide_NotStealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightRateInStealthRigidSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightRate_InStealthRigid_SightHide_StealthMode", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoactionButtonParamIdcorpse: int = ParamField(
        int32, "msbEventGeomTreasureInfo_actionButtonParamId_corpse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoitemGetAnimIdcorpse: int = ParamField(
        int32, "msbEventGeomTreasureInfo_itemGetAnimId_corpse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoactionButtonParamIdbox: int = ParamField(
        int32, "msbEventGeomTreasureInfo_actionButtonParamId_box", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoitemGetAnimIdbox: int = ParamField(
        int32, "msbEventGeomTreasureInfo_itemGetAnimId_box", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoactionButtonParamIdshine: int = ParamField(
        int32, "msbEventGeomTreasureInfo_actionButtonParamId_shine", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MsbEventGeomTreasureInfoitemGetAnimIdshine: int = ParamField(
        int32, "msbEventGeomTreasureInfo_itemGetAnimId_shine", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAssetId: int = ParamField(
        int32, "signPuddleAssetId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId0: int = ParamField(
        int32, "signPuddleAppearDmypolyId0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId1: int = ParamField(
        int32, "signPuddleAppearDmypolyId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId2: int = ParamField(
        int32, "signPuddleAppearDmypolyId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleAppearDmypolyId3: int = ParamField(
        int32, "signPuddleAppearDmypolyId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageRateforRidePC: float = ParamField(
        float32, "fallDamageRate_forRidePC", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageRateforRideNPC: float = ParamField(
        float32, "fallDamageRate_forRideNPC", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    OldMonkOfYellowCreateSignSpEffectId: int = ParamField(
        int32, "OldMonkOfYellow_CreateSignSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StragglerActivateDist: float = ParamField(
        float32, "StragglerActivateDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdEnableUseItemStragglerActivate: int = ParamField(
        int32, "SpEffectId_EnableUseItem_StragglerActivate", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdStragglerWakeUp: int = ParamField(
        int32, "SpEffectId_StragglerWakeUp", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdStragglerTarget: int = ParamField(
        int32, "SpEffectId_StragglerTarget", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdStragglerOppose: int = ParamField(
        int32, "SpEffectId_StragglerOppose", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpTriggerTimeRayBlocked: float = ParamField(
        float32, "buddyWarp_TriggerTimeRayBlocked", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpTriggerDistToPlayer: float = ParamField(
        float32, "buddyWarp_TriggerDistToPlayer", default=25.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpThresholdTimePathStacked: float = ParamField(
        float32, "buddyWarp_ThresholdTimePathStacked", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyWarpThresholdRangePathStacked: float = ParamField(
        float32, "buddyWarp_ThresholdRangePathStacked", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatemorning: float = ParamField(
        float32, "aiSightRate_morning", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatenoonA: float = ParamField(
        float32, "aiSightRate_noonA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BuddyPassThroughTriggerTime: float = ParamField(
        float32, "buddyPassThroughTriggerTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRateevening: float = ParamField(
        float32, "aiSightRate_evening", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatenight: float = ParamField(
        float32, "aiSightRate_night", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatemidnightA: float = ParamField(
        float32, "aiSightRate_midnightA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x230: int = ParamField(
        int32, "unknown_0x230", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatesunlosslight: float = ParamField(
        float32, "aiSightRate_sunloss_light", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatesunlossdark: float = ParamField(
        float32, "aiSightRate_sunloss_dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AiSightRatesunlossveryDark: float = ParamField(
        float32, "aiSightRate_sunloss_veryDark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateNotInStealthRigidNotSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightAngleReduceRate_NotInStealthRigid_NotSightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateNotInStealthRigidSightHideNotStealthMode: float = ParamField(
        float32, "stealthSystemSightAngleReduceRate_NotInStealthRigid_SightHide_NotStealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateNotInStealthRigidSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightAngleReduceRate_NotInStealthRigid_SightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidNotSightHideNotStealthMode: float = ParamField(
        float32, "stealthSystemSightAngleReduceRate_InStealthRigid_NotSightHide_NotStealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidNotSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightAngleReduceRate_InStealthRigid_NotSightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidSightHideNotStealthMode: float = ParamField(
        float32, "stealthSystemSightAngleReduceRate_InStealthRigid_SightHide_NotStealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StealthSystemSightAngleReduceRateInStealthRigidSightHideStealthMode: float = ParamField(
        float32, "stealthSystemSightAngleReduceRate_InStealthRigid_SightHide_StealthMode", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartMorningHour: int = ParamField(
        uint8, "weatherLotConditionStart_Morning_Hour", default=7,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartMorningMinute: int = ParamField(
        uint8, "weatherLotConditionStart_Morning_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayHour: int = ParamField(
        uint8, "weatherLotConditionStart_Day_Hour", default=12,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayMinute: int = ParamField(
        uint8, "weatherLotConditionStart_Day_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartEveningHour: int = ParamField(
        uint8, "weatherLotConditionStart_Evening_Hour", default=17,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartEveningMinute: int = ParamField(
        uint8, "weatherLotConditionStart_Evening_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartNightHour: int = ParamField(
        uint8, "weatherLotConditionStart_Night_Hour", default=19,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartNightMinute: int = ParamField(
        uint8, "weatherLotConditionStart_Night_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayBreakHour: int = ParamField(
        uint8, "weatherLotConditionStart_DayBreak_Hour", default=5,
        tooltip="TOOLTIP-TODO",
    )
    WeatherLotConditionStartDayBreakMinute: int = ParamField(
        uint8, "weatherLotConditionStart_DayBreak_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "weatherLotCondition_reserved[2]")
    PclightScaleChangeStartHour: int = ParamField(
        uint8, "pclightScaleChangeStart_Hour", default=18,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleChangeStartMinute: int = ParamField(
        uint8, "pclightScaleChangeStart_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleChangeEndHour: int = ParamField(
        uint8, "pclightScaleChangeEnd_Hour", default=5,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleChangeEndMinute: int = ParamField(
        uint8, "pclightScaleChangeEnd_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PclightScaleByTimezone: float = ParamField(
        float32, "pclightScaleByTimezone", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonSummonBuddySpecialEffectIdBuddy: int = ParamField(
        int32, "bigRuneGreaterDemon_SummonBuddySpecialEffectId_Buddy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BigRuneGreaterDemonSummonBuddySpecialEffectIdPc: int = ParamField(
        int32, "bigRuneGreaterDemon_SummonBuddySpecialEffectId_Pc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HomeBonfireParamId: int = ParamField(
        int32, "homeBonfireParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign11: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign12: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign13: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign14: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign15: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign16: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign17: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign18: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign19: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign20: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign21: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign22: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign23: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign24: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperWhiteSign25: int = ParamField(
        uint8, "machingWeaponLevelUpperWhiteSign_25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign11: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign12: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign13: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign14: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign15: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign16: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign17: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign18: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign19: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign20: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign21: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign22: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign23: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign24: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MachingWeaponLevelUpperRedSign25: int = ParamField(
        uint8, "machingWeaponLevelUpperRedSign_25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMorningHour: int = ParamField(
        uint8, "menuTimezoneStart_Morning_Hour", default=7,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMorningMinute: int = ParamField(
        uint8, "menuTimezoneStart_Morning_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay1Hour: int = ParamField(
        uint8, "menuTimezoneStart_Day1_Hour", default=12,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay1Minute: int = ParamField(
        uint8, "menuTimezoneStart_Day1_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay2Hour: int = ParamField(
        uint8, "menuTimezoneStart_Day2_Hour", default=12,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartDay2Minute: int = ParamField(
        uint8, "menuTimezoneStart_Day2_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartEveningHour: int = ParamField(
        uint8, "menuTimezoneStart_Evening_Hour", default=17,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartEveningMinute: int = ParamField(
        uint8, "menuTimezoneStart_Evening_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartNightHour: int = ParamField(
        uint8, "menuTimezoneStart_Night_Hour", default=19,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartNightMinute: int = ParamField(
        uint8, "menuTimezoneStart_Night_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMidnightHour: int = ParamField(
        uint8, "menuTimezoneStart_Midnight_Hour", default=5,
        tooltip="TOOLTIP-TODO",
    )
    MenuTimezoneStartMidnightMinute: int = ParamField(
        uint8, "menuTimezoneStart_Midnight_Minute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyThreatLv: int = ParamField(
        uint16, "remotePlayerThreatLvNotify_ThreatLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyNotifyDist: float = ParamField(
        float32, "remotePlayerThreatLvNotify_NotifyDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyEndNotifyDist: float = ParamField(
        float32, "remotePlayerThreatLvNotify_EndNotifyDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapPointDiscoveryExpandRange: float = ParamField(
        float32, "worldMapPointDiscoveryExpandRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapPointReentryExpandRange: float = ParamField(
        float32, "worldMapPointReentryExpandRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RemotePlayerThreatLvNotifyNotifyTime: int = ParamField(
        uint16, "remotePlayerThreatLvNotify_NotifyTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInArebreakInGoodsNum: int = ParamField(
        uint16, "breakIn_A_rebreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInArebreakInGoodsId: int = ParamField(
        int32, "breakIn_A_rebreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSfxId: int = ParamField(
        int32, "rideJumpoff_SfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSfxHeightOffset: float = ParamField(
        float32, "rideJumpoff_SfxHeightOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSpEffectId: int = ParamField(
        int32, "rideJumpoff_SpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RideJumpoffSpEffectIdPc: int = ParamField(
        int32, "rideJumpoff_SpEffectIdPc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UnlockExchangeMenuEventFlagId: int = ParamField(
        uint32, "unlockExchangeMenuEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnlockMessageMenuEventFlagId: int = ParamField(
        uint32, "unlockMessageMenuEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInOnceArebreakInGoodsNum: int = ParamField(
        uint16, "breakInOnce_A_rebreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInBrebreakInGoodsNum: int = ParamField(
        uint16, "breakIn_B_rebreakInGoodsNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInOnceArebreakInGoodsId: int = ParamField(
        int32, "breakInOnce_A_rebreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakInBrebreakInGoodsId: int = ParamField(
        int32, "breakIn_B_rebreakInGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActionButtonInputCancelTime: float = ParamField(
        float32, "actionButtonInputCancelTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlockClearBonusDelayTime: float = ParamField(
        float32, "blockClearBonusDelayTime", default=7.0,
        tooltip="TOOLTIP-TODO",
    )
    BonfireCheckEnemyRange: float = ParamField(
        float32, "bonfireCheckEnemyRange", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x2f0: int = ParamField(
        int32, "unknown_0x2f0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingLevelUnkUpperRel: int = ParamField(
        uint8, "matchingLevelUnkUpperRel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingLevelUnkUpperAbs: int = ParamField(
        uint8, "matchingLevelUnkUpperAbs", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk0: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk1: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk2: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk3: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk4: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk5: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk6: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk7: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk8: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk9: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk10: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk11: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk12: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk13: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk14: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk15: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk16: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk17: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk18: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk19: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk20: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk21: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk22: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk23: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk24: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MatchingWeaponLevelUpperUnk25: int = ParamField(
        uint8, "matchingWeaponLevelUpperUnk_25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x310: float = ParamField(
        float32, "unknown_0x310", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x314: float = ParamField(
        float32, "unknown_0x314", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x318: float = ParamField(
        float32, "unknown_0x318", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x31c: float = ParamField(
        float32, "unknown_0x31c", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x320: float = ParamField(
        float32, "unknown_0x320", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x324: float = ParamField(
        float32, "unknown_0x324", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x328: float = ParamField(
        float32, "unknown_0x328", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x32c: float = ParamField(
        float32, "unknown_0x32c", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x330: float = ParamField(
        float32, "unknown_0x330", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x334: float = ParamField(
        float32, "unknown_0x334", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x338: float = ParamField(
        float32, "unknown_0x338", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x33c: float = ParamField(
        float32, "unknown_0x33c", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x340: float = ParamField(
        float32, "unknown_0x340", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x344: float = ParamField(
        float32, "unknown_0x344", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x34c: int = ParamField(
        int32, "unknown_0x34c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x350: int = ParamField(
        int32, "unknown_0x350", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x354: int = ParamField(
        int32, "unknown_0x354", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x358: int = ParamField(
        int32, "unknown_0x358", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x35c: int = ParamField(
        int32, "unknown_0x35c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseScaduBlessingSpEffectId: int = ParamField(
        int32, "baseScaduBlessingSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseReveredSpiritAshBlessingSpEffectId: int = ParamField(
        int32, "baseReveredSpiritAshBlessingSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x368: int = ParamField(
        int32, "unknown_0x368", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x36c: int = ParamField(
        int32, "unknown_0x36c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x370: int = ParamField(
        int32, "unknown_0x370", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RidingSAReceivedRatePlayer: float = ParamField(
        float32, "ridingSAReceivedRatePlayer", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RidingSAReceivedRateNotPlayer: float = ParamField(
        float32, "ridingSAReceivedRateNotPlayer", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GlovewortCrystalSpiritBuffSpEffectId: int = ParamField(
        int32, "glovewortCrystalSpiritBuffSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x380: int = ParamField(
        int32, "unknown_0x380", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x384: float = ParamField(
        float32, "unknown_0x384", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UnknownSpEffectId0x388: int = ParamField(
        int32, "unknownSpEffectId_0x388", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnknownSpEffectId0x38c: int = ParamField(
        int32, "unknownSpEffectId_0x38c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnknownSpEffectId0x390: int = ParamField(
        int32, "unknownSpEffectId_0x390", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseReveredSpiritTorrentBlessingSpEffectId: int = ParamField(
        int32, "baseReveredSpiritTorrentBlessingSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(108, "endPad[108]")
