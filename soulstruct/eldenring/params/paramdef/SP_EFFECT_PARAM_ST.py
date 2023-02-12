from __future__ import annotations

__all__ = ["SP_EFFECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SP_EFFECT_PARAM_ST(ParamRow):
    StatusIcon: int = ParamField(
        int, "iconId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxHPPercentageForEffect: float = ParamField(
        float, "conditionHp", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EffectDuration: float = ParamField(
        float, "effectEndurance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpdateInterval: float = ParamField(
        float, "motionInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxHPMultiplier: float = ParamField(
        float, "maxHpRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxMPMultiplier: float = ParamField(
        float, "maxMpRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxStaminaMultiplier: float = ParamField(
        float, "maxStaminaRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IncomingSlashDamageMultiplier: float = ParamField(
        float, "slashDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IncomingStrikeDamageMultiplier: float = ParamField(
        float, "blowDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IncomingThrustDamageMultiplier: float = ParamField(
        float, "thrustDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IncomingNeutralDamageMultiplier: float = ParamField(
        float, "neutralDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IncomingMagicDamageMultiplier: float = ParamField(
        float, "magicDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IncomingFireDamageMultiplier: float = ParamField(
        float, "fireDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IncomingLightningDamageMultiplier: float = ParamField(
        float, "thunderDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    OutgoingPhysicalDamageMultiplier: float = ParamField(
        float, "physicsAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    OutgoingMagicDamageMultiplier: float = ParamField(
        float, "magicAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    OutgoingFireDamageMultiplier: float = ParamField(
        float, "fireAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    OutgoingLightningDamageMultiplier: float = ParamField(
        float, "thunderAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalAttackPowerMultiplier: float = ParamField(
        float, "physicsAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackPowerMultiplier: float = ParamField(
        float, "magicAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackPowerMultiplier: float = ParamField(
        float, "fireAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LightningAttackPowerMultiplier: float = ParamField(
        float, "thunderAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalAttackPowerAddition: int = ParamField(
        int, "physicsAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackPowerAddition: int = ParamField(
        int, "magicAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackPowerAddition: int = ParamField(
        int, "fireAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightningAttackPowerAddition: int = ParamField(
        int, "thunderAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalDefenseMultiplier: float = ParamField(
        float, "physicsDiffenceRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefenseMultiplier: float = ParamField(
        float, "magicDiffenceRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FireDefenseMultiplier: float = ParamField(
        float, "fireDiffenceRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LightningDefenseMultiplier: float = ParamField(
        float, "thunderDiffenceRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalDefenseAddition: int = ParamField(
        int, "physicsDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefenseAddition: int = ParamField(
        int, "magicDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireDefenseAddition: int = ParamField(
        int, "fireDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightningDefenseAddition: int = ParamField(
        int, "thunderDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoGuardIncomingDamageMultiplier: float = ParamField(
        float, "NoGuardDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CriticalHitIncomingDamageMultiplier: float = ParamField(
        float, "vitalSpotChangeRate", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NonCriticalHitIncomingDamageMultiplier: float = ParamField(
        float, "normalSpotChangeRate", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LookAtTargetPosOffset: float = ParamField(
        float, "lookAtTargetPosOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorToTrigger: int = ParamField(
        int, "behaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HPReductionPercentage: float = ParamField(
        float, "changeHpRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HPPointsLost: int = ParamField(
        int, "changeHpPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MPReductionPercentage: float = ParamField(
        float, "changeMpRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MPPointsLost: int = ParamField(
        int, "changeMpPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MPRecoverySpeedChange: int = ParamField(
        int, "mpRecoverChangeSpeed", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaReductionPercentage: float = ParamField(
        float, "changeStaminaRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaPointsLost: int = ParamField(
        int, "changeStaminaPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaRecoverySpeedChange: int = ParamField(
        int, "staminaRecoverChangeSpeed", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicEffectTimeChange: float = ParamField(
        float, "magicEffectTimeChange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CurrentDurabilityAddition: int = ParamField(
        int, "insideDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxDurabilityAddition: int = ParamField(
        int, "maxDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OutgoingStaminaDamageMultiplier: float = ParamField(
        float, "staminaAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoisonDamage: int = ParamField(
        int, "poizonAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseAttackPower: int = ParamField(
        int, "diseaseAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BloodAttackPower: int = ParamField(
        int, "bloodAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseAttackPower: int = ParamField(
        int, "curseAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageMultiplier: float = ParamField(
        float, "fallDamageRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SoulsFromKillsMultiplier: float = ParamField(
        float, "soulRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxEquipLoadMultiplier: float = ParamField(
        float, "equipWeightChangeRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxItemLoadMultiplier: float = ParamField(
        float, "allItemWeightChangeRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SoulAmountChange: int = ParamField(
        int, "soul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnimationIDOffset: int = ParamField(
        int, "animIdOffset", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoulRewardMultiplier: float = ParamField(
        float, "haveSoulRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TargetPriorityChange: float = ParamField(
        float, "targetPriority", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchEnemyRate: float = ParamField(
        float, "sightSearchEnemyRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnemyHearingMultiplier: float = ParamField(
        float, "hearingSearchEnemyRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AnimationSpeedMultiplier: float = ParamField(
        float, "grabityRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoisonResistanceMultiplier: float = ParamField(
        float, "registPoizonChangeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RegistDiseaseChangeRate: float = ParamField(
        float, "registDiseaseChangeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BleedResistanceMultiplier: float = ParamField(
        float, "registBloodChangeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CurseResistanceMultiplier: float = ParamField(
        float, "registCurseChangeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SoulStealMultiplier: float = ParamField(
        float, "soulStealRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EffectDurationMultiplier: float = ParamField(
        float, "lifeReductionRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HPRecoveryRate: float = ParamField(
        float, "hpRecoverRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NextSpecialEffect: int = ParamField(
        int, "replaceSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectPerUpdate: int = ParamField(
        int, "cycleOccurrenceSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnAttack: int = ParamField(
        int, "atkOccurrenceSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardDefenseFlickPowerRate: float = ParamField(
        float, "guardDefFlickPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    GuardStaminaMultiplier: float = ParamField(
        float, "guardStaminaCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RayCastPassingTime: int = ParamField(
        short, "rayCastPassedTime", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange1: int = ParamField(
        byte, "magicSubCategoryChange1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange2: int = ParamField(
        byte, "magicSubCategoryChange2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BowRangePercentageChange: int = ParamField(
        short, "bowDistRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectCategory: int = ParamField(
        ushort, "spCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectPriority: int = ParamField(
        byte, "categoryPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaveCategory: int = ParamField(
        sbyte, "saveCategory", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttunementSlotCountChange: int = ParamField(
        byte, "changeMagicSlot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttunementMiracleSlotCountChange: int = ParamField(
        byte, "changeMiracleSlot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityDamage: int = ParamField(
        sbyte, "heroPointDamage", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RiposteDefenseAddition: int = ParamField(
        byte, "defFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlickDamageMultiplier: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IncomingBleedDamagePercentage: int = ParamField(
        byte, "bloodDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceNoImpactLevel: int = ParamField(
        sbyte, "dmgLv_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceSmallImpactLevel: int = ParamField(
        sbyte, "dmgLv_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceMediumImpactLevel: int = ParamField(
        sbyte, "dmgLv_M", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceLargeImpactLevel: int = ParamField(
        sbyte, "dmgLv_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceBlowoffImpactLevel: int = ParamField(
        sbyte, "dmgLv_BlowM", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacePushImpactLevel: int = ParamField(
        sbyte, "dmgLv_Push", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceStrikeImpactLevel: int = ParamField(
        sbyte, "dmgLv_Strike", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceSmallBlowImpactLevel: int = ParamField(
        sbyte, "dmgLv_BlowS", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceMinimalImpactLevel: int = ParamField(
        sbyte, "dmgLv_Min", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceLaunchImpactLevel: int = ParamField(
        sbyte, "dmgLv_Uppercut", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceBlowBackwardImpactLevel: int = ParamField(
        sbyte, "dmgLv_BlowLL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceBreathBurnImpactLevel: int = ParamField(
        sbyte, "dmgLv_Breath", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackAttribute: int = ParamField(
        byte, "atkAttribute", default=254,
        tooltip="TOOLTIP-TODO",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", default=254,
        tooltip="TOOLTIP-TODO",
    )
    SpecialState: int = ParamField(
        ushort, "stateInfo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectedWeaponType: int = ParamField(
        byte, "wepParamChange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MovementType: int = ParamField(
        byte, "moveType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EffectDurationMultiplierType: int = ParamField(
        ushort, "lifeReductionType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowCondition: int = ParamField(
        byte, "throwCondition", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddBehaviorJudgeIDCondition: int = ParamField(
        sbyte, "addBehaviorJudgeId_condition", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FreezeDamageRate: int = ParamField(
        byte, "freezeDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectSelf: int = ParamField(
        byte, "effectTargetSelf:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectAlly: int = ParamField(
        byte, "effectTargetFriend:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectEnemy: int = ParamField(
        byte, "effectTargetEnemy:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectPlayer: int = ParamField(
        byte, "effectTargetPlayer:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectAI: int = ParamField(
        byte, "effectTargetAI:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectPlayers: int = ParamField(
        byte, "effectTargetLive:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectPhantoms: int = ParamField(
        byte, "effectTargetGhost:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableSleep: int = ParamField(
        byte, "disableSleep:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableMadness: int = ParamField(
        byte, "disableMadness:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectAttacker: int = ParamField(
        byte, "effectTargetAttacker:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisplayIconWhenInactive: int = ParamField(
        byte, "dispIconNonactive:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RegainGaugeDamage: int = ParamField(
        byte, "regainGaugeDamage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseIntelligenceScaling: int = ParamField(
        byte, "bAdjustMagicAblity:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseFaithScaling: int = ParamField(
        byte, "bAdjustFaithAblity:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForNewGamePlus: int = ParamField(
        byte, "bGameClearBonus:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsMagic: int = ParamField(
        byte, "magParamChange:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsMiracles: int = ParamField(
        byte, "miracleParamChange:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ClearSoul: int = ParamField(
        byte, "clearSoul:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestWhitePhantomSummon: int = ParamField(
        byte, "requestSOS:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestBlackPhantomSummon: int = ParamField(
        byte, "requestBlackSOS:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestInvasion: int = ParamField(
        byte, "requestForceJoinBlackSOS:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestKick: int = ParamField(
        byte, "requestKickSession:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestReturnToOwnWorld: int = ParamField(
        byte, "requestLeaveSession:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestNPCInvasion: int = ParamField(
        byte, "requestNpcInveda:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Immortal: int = ParamField(
        byte, "noDead:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurrentHPIgnoresMaxHPChange: int = ParamField(
        byte, "bCurrHPIndependeMaxHP:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreCorrosion: int = ParamField(
        byte, "corrosionIgnore:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreSightReduction: int = ParamField(
        byte, "sightSearchCutIgnore:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreHearingReduction: int = ParamField(
        byte, "hearingSearchCutIgnore:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreMagicDisabling: int = ParamField(
        byte, "antiMagicIgnore:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreFakeTargets: int = ParamField(
        byte, "fakeTargetIgnore:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreUndeadFakeTargets: int = ParamField(
        byte, "fakeTargetIgnoreUndead:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreBeastFakeTargets: int = ParamField(
        byte, "fakeTargetIgnoreAnimal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreGravity: int = ParamField(
        byte, "grabityIgnore:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonImmunity: int = ParamField(
        byte, "disablePoison:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ToxicImmunity: int = ParamField(
        byte, "disableDisease:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BleedImmunity: int = ParamField(
        byte, "disableBlood:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseImmunity: int = ParamField(
        byte, "disableCurse:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableCharming: int = ParamField(
        byte, "enableCharm:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableLifeTime: int = ParamField(
        byte, "enableLifeTime:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseStrengthScaling: int = ParamField(
        byte, "bAdjustStrengthAblity:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseDexterityScaling: int = ParamField(
        byte, "bAdjustAgilityAblity:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EraseOnBonfireRecover: int = ParamField(
        byte, "eraseOnBonfireRecover:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GrabAttackParamChange: int = ParamField(
        byte, "throwAttackParamChange:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestColiseumExit: int = ParamField(
        byte, "requestLeaveColiseumSession:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectedByEffectExtension: int = ParamField(
        byte, "isExtendSpEffectLife:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HasTarget: int = ParamField(
        byte, "hasTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplanningOnFire: int = ParamField(
        byte, "replanningOnFire:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCharactersWithNoCovenant: int = ParamField(
        byte, "vowType0:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsWayOfWhite: int = ParamField(
        byte, "vowType1:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsPrincessGuard: int = ParamField(
        byte, "vowType2:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsWarriorOfSunlight: int = ParamField(
        byte, "vowType3:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsDarkwraith: int = ParamField(
        byte, "vowType4:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsPathOfTheDragon: int = ParamField(
        byte, "vowType5:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsGravelordServant: int = ParamField(
        byte, "vowType6:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsForestHunter: int = ParamField(
        byte, "vowType7:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsDarkmoonBlade: int = ParamField(
        byte, "vowType8:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsChaosServant: int = ParamField(
        byte, "vowType9:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCovenant10: int = ParamField(
        byte, "vowType10:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCovenant11: int = ParamField(
        byte, "vowType11:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCovenant12: int = ParamField(
        byte, "vowType12:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCovenant13: int = ParamField(
        byte, "vowType13:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCovenant14: int = ParamField(
        byte, "vowType14:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCovenant15: int = ParamField(
        byte, "vowType15:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RepAtkDmgLv: int = ParamField(
        sbyte, "repAtkDmgLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchRate: float = ParamField(
        float, "sightSearchRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetsEnemyTarget: int = ParamField(
        byte, "effectTargetOpposeTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetsAllyTarget: int = ParamField(
        byte, "effectTargetFriendlyTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetsSelfTarget: int = ParamField(
        byte, "effectTargetSelfTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetPcHorse: int = ParamField(
        byte, "effectTargetPcHorse:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetPcDeceased: int = ParamField(
        byte, "effectTargetPcDeceased:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsContractSpEffectLife: int = ParamField(
        byte, "isContractSpEffectLife:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWaitModeDelete: int = ParamField(
        byte, "isWaitModeDelete:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsIgnoreNoDamage: int = ParamField(
        byte, "isIgnoreNoDamage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeTeamType: int = ParamField(
        sbyte, "changeTeamType", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId: int = ParamField(
        short, "dmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId: int = ParamField(
        int, "vfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuOverFireId: int = ParamField(
        int, "accumuOverFireId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuOverVal: int = ParamField(
        int, "accumuOverVal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuUnderFireId: int = ParamField(
        int, "accumuUnderFireId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuUnderVal: int = ParamField(
        int, "accumuUnderVal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuVal: int = ParamField(
        int, "accumuVal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeangX: int = ParamField(
        byte, "eye_angX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeangY: int = ParamField(
        byte, "eye_angY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddDeceasedLv: int = ParamField(
        short, "addDeceasedLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VfxId1: int = ParamField(
        int, "vfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId2: int = ParamField(
        int, "vfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId3: int = ParamField(
        int, "vfxId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId4: int = ParamField(
        int, "vfxId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId5: int = ParamField(
        int, "vfxId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId6: int = ParamField(
        int, "vfxId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId7: int = ParamField(
        int, "vfxId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FreezeAttackPower: int = ParamField(
        int, "freezeAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AppearAiSoundId: int = ParamField(
        int, "AppearAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddFootEffectSfxId: int = ParamField(
        short, "addFootEffectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DexterityCancelSystemOnlyAddDexterity: int = ParamField(
        sbyte, "dexterityCancelSystemOnlyAddDexterity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TeamOffenseEffectivity: int = ParamField(
        sbyte, "teamOffenseEffectivity", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessDamageCutRate: float = ParamField(
        float, "toughnessDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateA: float = ParamField(
        float, "weakDmgRateA", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateB: float = ParamField(
        float, "weakDmgRateB", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateC: float = ParamField(
        float, "weakDmgRateC", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateD: float = ParamField(
        float, "weakDmgRateD", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateE: float = ParamField(
        float, "weakDmgRateE", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateF: float = ParamField(
        float, "weakDmgRateF", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float, "darkDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkDiffenceRate: float = ParamField(
        float, "darkDiffenceRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkDiffence: int = ParamField(
        int, "darkDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackRate: float = ParamField(
        float, "darkAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackPowerRate: float = ParamField(
        float, "darkAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackPower: int = ParamField(
        int, "darkAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AntiDarkSightRadius: float = ParamField(
        float, "antiDarkSightRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AntiDarkSightModelPoint: int = ParamField(
        int, "antiDarkSightDmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConditionHPRate: float = ParamField(
        float, "conditionHpRate", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StaminaConsumptionRate: float = ParamField(
        float, "consumeStaminaRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ItemDropRate: float = ParamField(
        float, "itemDropRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangePoisonResistance: int = ParamField(
        int, "changePoisonResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeToxicResistance: int = ParamField(
        int, "changeDiseaseResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeBleedingResistance: int = ParamField(
        int, "changeBloodResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeFrenzyResistance: int = ParamField(
        int, "changeCurseResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeFreezeResistPoint: int = ParamField(
        int, "changeFreezeResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackRate: float = ParamField(
        float, "slashAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BluntAttackRate: float = ParamField(
        float, "blowAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ThrustAttackRate: float = ParamField(
        float, "thrustAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    NeutralAttackRate: float = ParamField(
        float, "neutralAttackRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackPowerRate: float = ParamField(
        float, "slashAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BluntAttackPowerRate: float = ParamField(
        float, "blowAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ThrustAttackPowerRate: float = ParamField(
        float, "thrustAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    NeutralAttackPowerRate: float = ParamField(
        float, "neutralAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackPower: int = ParamField(
        int, "slashAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BluntAttackPower: int = ParamField(
        int, "blowAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustAttackPower: int = ParamField(
        int, "thrustAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralAttackPower: int = ParamField(
        int, "neutralAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeStrength: int = ParamField(
        int, "changeStrengthPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeDexterity: int = ParamField(
        int, "changeAgilityPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeBloodtinge: int = ParamField(
        int, "changeMagicPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeArcane: int = ParamField(
        int, "changeFaithPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeLuckPoint: int = ParamField(
        int, "changeLuckPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointStr: int = ParamField(
        sbyte, "recoverArtsPoint_Str", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointDex: int = ParamField(
        sbyte, "recoverArtsPoint_Dex", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointMagic: int = ParamField(
        sbyte, "recoverArtsPoint_Magic", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointMiracle: int = ParamField(
        sbyte, "recoverArtsPoint_Miracle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessDamageRate: int = ParamField(
        byte, "madnessDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    IsUseStatusAilmentAtkPowerCorrect: int = ParamField(
        byte, "isUseStatusAilmentAtkPowerCorrect:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUseAtkParamAtkPowerCorrect: int = ParamField(
        byte, "isUseAtkParamAtkPowerCorrect:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DontDeleteOnDead: int = ParamField(
        byte, "dontDeleteOnDead:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableFreeze: int = ParamField(
        byte, "disableFreeze:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableNetSync: int = ParamField(
        byte, "isDisableNetSync:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShamanParamChange: int = ParamField(
        byte, "shamanParamChange:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsStopSearchedNotify: int = ParamField(
        byte, "isStopSearchedNotify:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckAboveShadowTest: int = ParamField(
        byte, "isCheckAboveShadowTest:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddBehaviorJudgeIDAdd: int = ParamField(
        ushort, "addBehaviorJudgeId_add", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaReceiveDamageRate: float = ParamField(
        float, "saReceiveDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRatePhysics: float = ParamField(
        float, "defPlayerDmgCorrectRate_Physics", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateMagic: float = ParamField(
        float, "defPlayerDmgCorrectRate_Magic", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateFire: float = ParamField(
        float, "defPlayerDmgCorrectRate_Fire", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateThunder: float = ParamField(
        float, "defPlayerDmgCorrectRate_Thunder", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateDark: float = ParamField(
        float, "defPlayerDmgCorrectRate_Dark", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRatePhysics: float = ParamField(
        float, "defEnemyDmgCorrectRate_Physics", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateMagic: float = ParamField(
        float, "defEnemyDmgCorrectRate_Magic", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateFire: float = ParamField(
        float, "defEnemyDmgCorrectRate_Fire", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateThunder: float = ParamField(
        float, "defEnemyDmgCorrectRate_Thunder", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateDark: float = ParamField(
        float, "defEnemyDmgCorrectRate_Dark", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefObjDmgCorrectRate: float = ParamField(
        float, "defObjDmgCorrectRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRatePhysics: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Physics", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateMagic: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Magic", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateFire: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Fire", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateThunder: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Thunder", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateDark: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Dark", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRatePhysics: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Physics", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateMagic: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Magic", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateFire: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Fire", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateThunder: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Thunder", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateDark: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Dark", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RegistFreezeChangeRate: float = ParamField(
        float, "registFreezeChangeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange1: int = ParamField(
        ushort, "invocationConditionsStateChange1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange2: int = ParamField(
        ushort, "invocationConditionsStateChange2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange3: int = ParamField(
        ushort, "invocationConditionsStateChange3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HearingAiSoundLevel: int = ParamField(
        short, "hearingAiSoundLevel", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrProxyHeightRate: float = ParamField(
        float, "chrProxyHeightRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AddAwarePointCorrectValueforMe: float = ParamField(
        float, "addAwarePointCorrectValue_forMe", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddAwarePointCorrectValueforTarget: float = ParamField(
        float, "addAwarePointCorrectValue_forTarget", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchEnemyAdd: float = ParamField(
        float, "sightSearchEnemyAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchAdd: float = ParamField(
        float, "sightSearchAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchAdd: float = ParamField(
        float, "hearingSearchAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchRate: float = ParamField(
        float, "hearingSearchRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchEnemyAdd: float = ParamField(
        float, "hearingSearchEnemyAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ValueMagnification: float = ParamField(
        float, "value_Magnification", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ArtsConsumptionRate: float = ParamField(
        float, "artsConsumptionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicConsumptionRate: float = ParamField(
        float, "magicConsumptionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ShamanConsumptionRate: float = ParamField(
        float, "shamanConsumptionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MiracleConsumptionRate: float = ParamField(
        float, "miracleConsumptionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpEstusFlaskRate: int = ParamField(
        int, "changeHpEstusFlaskRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpEstusFlaskPoint: int = ParamField(
        int, "changeHpEstusFlaskPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpEstusFlaskRate: int = ParamField(
        int, "changeMpEstusFlaskRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpEstusFlaskPoint: int = ParamField(
        int, "changeMpEstusFlaskPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpEstusFlaskCorrectRate: float = ParamField(
        float, "changeHpEstusFlaskCorrectRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpEstusFlaskCorrectRate: float = ParamField(
        float, "changeMpEstusFlaskCorrectRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ApplyIdOnGetSoul: int = ParamField(
        int, "applyIdOnGetSoul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExtendLifeRate: float = ParamField(
        float, "extendLifeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ContractLifeRate: float = ParamField(
        float, "contractLifeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefObjectAttackPowerRate: float = ParamField(
        float, "defObjectAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EffectEndDeleteDecalGroupId: int = ParamField(
        short, "effectEndDeleteDecalGroupId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AddLifeForceStatus: int = ParamField(
        sbyte, "addLifeForceStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddWillpowerStatus: int = ParamField(
        sbyte, "addWillpowerStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddEndureStatus: int = ParamField(
        sbyte, "addEndureStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddVitalityStatus: int = ParamField(
        sbyte, "addVitalityStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddStrengthStatus: int = ParamField(
        sbyte, "addStrengthStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddDexterityStatus: int = ParamField(
        sbyte, "addDexterityStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddMagicStatus: int = ParamField(
        sbyte, "addMagicStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddFaithStatus: int = ParamField(
        sbyte, "addFaithStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddLuckStatus: int = ParamField(
        sbyte, "addLuckStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeleteCriteriaDamage: int = ParamField(
        byte, "deleteCriteriaDamage", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange3: int = ParamField(
        byte, "magicSubCategoryChange3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpAttributeVariationValue: int = ParamField(
        byte, "spAttributeVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkFlickPower: int = ParamField(
        byte, "atkFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WetConditionDepth: int = ParamField(
        byte, "wetConditionDepth", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeSaRecoveryVelocity: float = ParamField(
        float, "changeSaRecoveryVelocity", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RegainRate: float = ParamField(
        float, "regainRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SaAttackPowerRate: float = ParamField(
        float, "saAttackPowerRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SleepAttackPower: int = ParamField(
        int, "sleepAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessAttackPower: int = ParamField(
        int, "madnessAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RegistSleepChangeRate: float = ParamField(
        float, "registSleepChangeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RegistMadnessChangeRate: float = ParamField(
        float, "registMadnessChangeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ChangeSleepResistPoint: int = ParamField(
        int, "changeSleepResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMadnessResistPoint: int = ParamField(
        int, "changeMadnessResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SleepDamageRate: int = ParamField(
        byte, "sleepDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ApplyPartsGroup: int = ParamField(
        byte, "applyPartsGroup", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ClearTarget: int = ParamField(
        byte, "clearTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreAjin: int = ParamField(
        byte, "fakeTargetIgnoreAjin:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreMirageArts: int = ParamField(
        byte, "fakeTargetIgnoreMirageArts:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequestForceJoinBlackSOSB: int = ParamField(
        byte, "requestForceJoinBlackSOS_B:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk3534: int = ParamField(
        byte, "unk353_4:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    PoiseAddition: float = ParamField(
        float, "changeSuperArmorPoint", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeSaPoint: float = ParamField(
        float, "changeSaPoint", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HugeEnemyPickupHeightOverwrite: float = ParamField(
        float, "hugeEnemyPickupHeightOverwrite", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonDefDamageRate: float = ParamField(
        float, "poisonDefDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseDefDamageRate: float = ParamField(
        float, "diseaseDefDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BloodDefDamageRate: float = ParamField(
        float, "bloodDefDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CurseDefDamageRate: float = ParamField(
        float, "curseDefDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FreezeDefDamageRate: float = ParamField(
        float, "freezeDefDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SleepDefDamageRate: float = ParamField(
        float, "sleepDefDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MadnessDefDamageRate: float = ParamField(
        float, "madnessDefDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    OverwritemaxBackhomeDist: int = ParamField(
        ushort, "overwrite_maxBackhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverwritebackhomeDist: int = ParamField(
        ushort, "overwrite_backhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverwritebackhomeBattleDist: int = ParamField(
        ushort, "overwrite_backhomeBattleDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteBackHomeLookTargetDist: int = ParamField(
        ushort, "overwrite_BackHome_LookTargetDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodsConsumptionRate: float = ParamField(
        float, "goodsConsumptionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad3[8]")
