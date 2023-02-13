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
    IconId: int = ParamField(
        int, "iconId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConditionHp: float = ParamField(
        float, "conditionHp", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    EffectEndurance: float = ParamField(
        float, "effectEndurance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MotionInterval: float = ParamField(
        float, "motionInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxHpRate: float = ParamField(
        float, "maxHpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxMpRate: float = ParamField(
        float, "maxMpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxStaminaRate: float = ParamField(
        float, "maxStaminaRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashDamageCutRate: float = ParamField(
        float, "slashDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowDamageCutRate: float = ParamField(
        float, "blowDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamageCutRate: float = ParamField(
        float, "thrustDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralDamageCutRate: float = ParamField(
        float, "neutralDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamageCutRate: float = ParamField(
        float, "magicDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageCutRate: float = ParamField(
        float, "fireDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDamageCutRate: float = ParamField(
        float, "thunderDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsAttackRate: float = ParamField(
        float, "physicsAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackRate: float = ParamField(
        float, "magicAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackRate: float = ParamField(
        float, "fireAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderAttackRate: float = ParamField(
        float, "thunderAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsAttackPowerRate: float = ParamField(
        float, "physicsAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackPowerRate: float = ParamField(
        float, "magicAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackPowerRate: float = ParamField(
        float, "fireAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderAttackPowerRate: float = ParamField(
        float, "thunderAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsAttackPower: int = ParamField(
        int, "physicsAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackPower: int = ParamField(
        int, "magicAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackPower: int = ParamField(
        int, "fireAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderAttackPower: int = ParamField(
        int, "thunderAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsDiffenceRate: float = ParamField(
        float, "physicsDiffenceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDiffenceRate: float = ParamField(
        float, "magicDiffenceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDiffenceRate: float = ParamField(
        float, "fireDiffenceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDiffenceRate: float = ParamField(
        float, "thunderDiffenceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsDiffence: int = ParamField(
        int, "physicsDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDiffence: int = ParamField(
        int, "magicDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireDiffence: int = ParamField(
        int, "fireDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDiffence: int = ParamField(
        int, "thunderDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoGuardDamageRate: float = ParamField(
        float, "NoGuardDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VitalSpotChangeRate: float = ParamField(
        float, "vitalSpotChangeRate", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    NormalSpotChangeRate: float = ParamField(
        float, "normalSpotChangeRate", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    LookAtTargetPosOffset: float = ParamField(
        float, "lookAtTargetPosOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorId: int = ParamField(
        int, "behaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpRate: float = ParamField(
        float, "changeHpRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpPoint: int = ParamField(
        int, "changeHpPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpRate: float = ParamField(
        float, "changeMpRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpPoint: int = ParamField(
        int, "changeMpPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MpRecoverChangeSpeed: int = ParamField(
        int, "mpRecoverChangeSpeed", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeStaminaRate: float = ParamField(
        float, "changeStaminaRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeStaminaPoint: int = ParamField(
        int, "changeStaminaPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaRecoverChangeSpeed: int = ParamField(
        int, "staminaRecoverChangeSpeed", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicEffectTimeChange: float = ParamField(
        float, "magicEffectTimeChange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    InsideDurability: int = ParamField(
        int, "insideDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxDurability: int = ParamField(
        int, "maxDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaAttackRate: float = ParamField(
        float, "staminaAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PoizonAttackPower: int = ParamField(
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
    FallDamageRate: float = ParamField(
        float, "fallDamageRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SoulRate: float = ParamField(
        float, "soulRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EquipWeightChangeRate: float = ParamField(
        float, "equipWeightChangeRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AllItemWeightChangeRate: float = ParamField(
        float, "allItemWeightChangeRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Soul: int = ParamField(
        int, "soul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnimIdOffset: int = ParamField(
        int, "animIdOffset", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HaveSoulRate: float = ParamField(
        float, "haveSoulRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    TargetPriority: float = ParamField(
        float, "targetPriority", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchEnemyRate: float = ParamField(
        float, "sightSearchEnemyRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchEnemyRate: float = ParamField(
        float, "hearingSearchEnemyRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GrabityRate: float = ParamField(
        float, "grabityRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistPoizonChangeRate: float = ParamField(
        float, "registPoizonChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistDiseaseChangeRate: float = ParamField(
        float, "registDiseaseChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistBloodChangeRate: float = ParamField(
        float, "registBloodChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistCurseChangeRate: float = ParamField(
        float, "registCurseChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SoulStealRate: float = ParamField(
        float, "soulStealRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeReductionRate: float = ParamField(
        float, "lifeReductionRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HpRecoverRate: float = ParamField(
        float, "hpRecoverRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceSpEffectId: int = ParamField(
        int, "replaceSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CycleOccurrenceSpEffectId: int = ParamField(
        int, "cycleOccurrenceSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AtkOccurrenceSpEffectId: int = ParamField(
        int, "atkOccurrenceSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardDefFlickPowerRate: float = ParamField(
        float, "guardDefFlickPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardStaminaCutRate: float = ParamField(
        float, "guardStaminaCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RayCastPassedTime: int = ParamField(
        short, "rayCastPassedTime", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange1: int = ParamField(
        byte, "magicSubCategoryChange1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange2: int = ParamField(
        byte, "magicSubCategoryChange2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BowDistRate: int = ParamField(
        short, "bowDistRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpCategory: int = ParamField(
        ushort, "spCategory", SP_EFFECT_SPCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CategoryPriority: int = ParamField(
        byte, "categoryPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaveCategory: int = ParamField(
        sbyte, "saveCategory", SP_EFFECT_SAVE_CATEGORY, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMagicSlot: int = ParamField(
        byte, "changeMagicSlot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMiracleSlot: int = ParamField(
        byte, "changeMiracleSlot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HeroPointDamage: int = ParamField(
        sbyte, "heroPointDamage", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefFlickPower: int = ParamField(
        byte, "defFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlickDamageCutRate: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BloodDamageRate: int = ParamField(
        byte, "bloodDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvNone: int = ParamField(
        sbyte, "dmgLv_None", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvS: int = ParamField(
        sbyte, "dmgLv_S", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvM: int = ParamField(
        sbyte, "dmgLv_M", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvL: int = ParamField(
        sbyte, "dmgLv_L", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvBlowM: int = ParamField(
        sbyte, "dmgLv_BlowM", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvPush: int = ParamField(
        sbyte, "dmgLv_Push", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvStrike: int = ParamField(
        sbyte, "dmgLv_Strike", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvBlowS: int = ParamField(
        sbyte, "dmgLv_BlowS", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvMin: int = ParamField(
        sbyte, "dmgLv_Min", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvUppercut: int = ParamField(
        sbyte, "dmgLv_Uppercut", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvBlowLL: int = ParamField(
        sbyte, "dmgLv_BlowLL", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLvBreath: int = ParamField(
        sbyte, "dmgLv_Breath", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=254,
        tooltip="TOOLTIP-TODO",
    )
    SpAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=254,
        tooltip="TOOLTIP-TODO",
    )
    StateInfo: int = ParamField(
        ushort, "stateInfo", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamChange: int = ParamField(
        byte, "wepParamChange", SP_EFE_WEP_CHANGE_PARAM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MoveType: int = ParamField(
        byte, "moveType", SP_EFFECT_MOVE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LifeReductionType: int = ParamField(
        ushort, "lifeReductionType", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowCondition: int = ParamField(
        byte, "throwCondition", SP_EFFECT_THROW_CONDITION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddBehaviorJudgeIdcondition: int = ParamField(
        sbyte, "addBehaviorJudgeId_condition", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FreezeDamageRate: int = ParamField(
        byte, "freezeDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetSelf: bool = ParamField(
        byte, "effectTargetSelf:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetFriend: bool = ParamField(
        byte, "effectTargetFriend:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetEnemy: bool = ParamField(
        byte, "effectTargetEnemy:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetPlayer: bool = ParamField(
        byte, "effectTargetPlayer:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetAI: bool = ParamField(
        byte, "effectTargetAI:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetLive: bool = ParamField(
        byte, "effectTargetLive:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetGhost: bool = ParamField(
        byte, "effectTargetGhost:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableSleep: bool = ParamField(
        byte, "disableSleep:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMadness: bool = ParamField(
        byte, "disableMadness:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetAttacker: bool = ParamField(
        byte, "effectTargetAttacker:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DispIconNonactive: bool = ParamField(
        byte, "dispIconNonactive:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RegainGaugeDamage: bool = ParamField(
        byte, "regainGaugeDamage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BAdjustMagicAblity: bool = ParamField(
        byte, "bAdjustMagicAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BAdjustFaithAblity: bool = ParamField(
        byte, "bAdjustFaithAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BGameClearBonus: bool = ParamField(
        byte, "bGameClearBonus:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    MagParamChange: bool = ParamField(
        byte, "magParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    MiracleParamChange: bool = ParamField(
        byte, "miracleParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ClearSoul: bool = ParamField(
        byte, "clearSoul:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestSOS: bool = ParamField(
        byte, "requestSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestBlackSOS: bool = ParamField(
        byte, "requestBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestForceJoinBlackSOS: bool = ParamField(
        byte, "requestForceJoinBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestKickSession: bool = ParamField(
        byte, "requestKickSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestLeaveSession: bool = ParamField(
        byte, "requestLeaveSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestNpcInveda: bool = ParamField(
        byte, "requestNpcInveda:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    NoDead: bool = ParamField(
        byte, "noDead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BCurrHPIndependeMaxHP: bool = ParamField(
        byte, "bCurrHPIndependeMaxHP:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CorrosionIgnore: bool = ParamField(
        byte, "corrosionIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchCutIgnore: bool = ParamField(
        byte, "sightSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchCutIgnore: bool = ParamField(
        byte, "hearingSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AntiMagicIgnore: bool = ParamField(
        byte, "antiMagicIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnore: bool = ParamField(
        byte, "fakeTargetIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreUndead: bool = ParamField(
        byte, "fakeTargetIgnoreUndead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreAnimal: bool = ParamField(
        byte, "fakeTargetIgnoreAnimal:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    GrabityIgnore: bool = ParamField(
        byte, "grabityIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisablePoison: bool = ParamField(
        byte, "disablePoison:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableDisease: bool = ParamField(
        byte, "disableDisease:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableBlood: bool = ParamField(
        byte, "disableBlood:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableCurse: bool = ParamField(
        byte, "disableCurse:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableCharm: bool = ParamField(
        byte, "enableCharm:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLifeTime: bool = ParamField(
        byte, "enableLifeTime:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BAdjustStrengthAblity: bool = ParamField(
        byte, "bAdjustStrengthAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BAdjustAgilityAblity: bool = ParamField(
        byte, "bAdjustAgilityAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EraseOnBonfireRecover: bool = ParamField(
        byte, "eraseOnBonfireRecover:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ThrowAttackParamChange: bool = ParamField(
        byte, "throwAttackParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestLeaveColiseumSession: bool = ParamField(
        byte, "requestLeaveColiseumSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsExtendSpEffectLife: bool = ParamField(
        byte, "isExtendSpEffectLife:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HasTarget: bool = ParamField(
        byte, "hasTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ReplanningOnFire: bool = ParamField(
        byte, "replanningOnFire:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType0: bool = ParamField(
        byte, "vowType0:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType1: bool = ParamField(
        byte, "vowType1:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType2: bool = ParamField(
        byte, "vowType2:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType3: bool = ParamField(
        byte, "vowType3:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType4: bool = ParamField(
        byte, "vowType4:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType5: bool = ParamField(
        byte, "vowType5:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType6: bool = ParamField(
        byte, "vowType6:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType7: bool = ParamField(
        byte, "vowType7:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType8: bool = ParamField(
        byte, "vowType8:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType9: bool = ParamField(
        byte, "vowType9:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType10: bool = ParamField(
        byte, "vowType10:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType11: bool = ParamField(
        byte, "vowType11:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType12: bool = ParamField(
        byte, "vowType12:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType13: bool = ParamField(
        byte, "vowType13:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType14: bool = ParamField(
        byte, "vowType14:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType15: bool = ParamField(
        byte, "vowType15:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RepAtkDmgLv: int = ParamField(
        sbyte, "repAtkDmgLv", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchRate: float = ParamField(
        float, "sightSearchRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetOpposeTarget: bool = ParamField(
        byte, "effectTargetOpposeTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetFriendlyTarget: bool = ParamField(
        byte, "effectTargetFriendlyTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetSelfTarget: bool = ParamField(
        byte, "effectTargetSelfTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetPcHorse: bool = ParamField(
        byte, "effectTargetPcHorse:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetPcDeceased: bool = ParamField(
        byte, "effectTargetPcDeceased:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsContractSpEffectLife: bool = ParamField(
        byte, "isContractSpEffectLife:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWaitModeDelete: bool = ParamField(
        byte, "isWaitModeDelete:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsIgnoreNoDamage: bool = ParamField(
        byte, "isIgnoreNoDamage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ChangeTeamType: int = ParamField(
        sbyte, "changeTeamType", SP_EFFECT_CHANGE_TEAM_TYPE, default=-1,
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
        float, "toughnessDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateA: float = ParamField(
        float, "weakDmgRateA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateB: float = ParamField(
        float, "weakDmgRateB", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateC: float = ParamField(
        float, "weakDmgRateC", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateD: float = ParamField(
        float, "weakDmgRateD", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateE: float = ParamField(
        float, "weakDmgRateE", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateF: float = ParamField(
        float, "weakDmgRateF", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float, "darkDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDiffenceRate: float = ParamField(
        float, "darkDiffenceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDiffence: int = ParamField(
        int, "darkDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackRate: float = ParamField(
        float, "darkAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackPowerRate: float = ParamField(
        float, "darkAttackPowerRate", default=1.0,
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
    AntiDarkSightDmypolyId: int = ParamField(
        int, "antiDarkSightDmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConditionHpRate: float = ParamField(
        float, "conditionHpRate", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeStaminaRate: float = ParamField(
        float, "consumeStaminaRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ItemDropRate: float = ParamField(
        float, "itemDropRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangePoisonResistPoint: int = ParamField(
        int, "changePoisonResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeDiseaseResistPoint: int = ParamField(
        int, "changeDiseaseResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeBloodResistPoint: int = ParamField(
        int, "changeBloodResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeCurseResistPoint: int = ParamField(
        int, "changeCurseResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeFreezeResistPoint: int = ParamField(
        int, "changeFreezeResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackRate: float = ParamField(
        float, "slashAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowAttackRate: float = ParamField(
        float, "blowAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustAttackRate: float = ParamField(
        float, "thrustAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralAttackRate: float = ParamField(
        float, "neutralAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackPowerRate: float = ParamField(
        float, "slashAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowAttackPowerRate: float = ParamField(
        float, "blowAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustAttackPowerRate: float = ParamField(
        float, "thrustAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralAttackPowerRate: float = ParamField(
        float, "neutralAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackPower: int = ParamField(
        int, "slashAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowAttackPower: int = ParamField(
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
    ChangeStrengthPoint: int = ParamField(
        int, "changeStrengthPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeAgilityPoint: int = ParamField(
        int, "changeAgilityPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMagicPoint: int = ParamField(
        int, "changeMagicPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeFaithPoint: int = ParamField(
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
    IsUseStatusAilmentAtkPowerCorrect: bool = ParamField(
        byte, "isUseStatusAilmentAtkPowerCorrect:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseAtkParamAtkPowerCorrect: bool = ParamField(
        byte, "isUseAtkParamAtkPowerCorrect:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DontDeleteOnDead: bool = ParamField(
        byte, "dontDeleteOnDead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableFreeze: bool = ParamField(
        byte, "disableFreeze:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableNetSync: bool = ParamField(
        byte, "isDisableNetSync:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShamanParamChange: bool = ParamField(
        byte, "shamanParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStopSearchedNotify: bool = ParamField(
        byte, "isStopSearchedNotify:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckAboveShadowTest: bool = ParamField(
        byte, "isCheckAboveShadowTest:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AddBehaviorJudgeIdadd: int = ParamField(
        ushort, "addBehaviorJudgeId_add", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaReceiveDamageRate: float = ParamField(
        float, "saReceiveDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRatePhysics: float = ParamField(
        float, "defPlayerDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateMagic: float = ParamField(
        float, "defPlayerDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateFire: float = ParamField(
        float, "defPlayerDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateThunder: float = ParamField(
        float, "defPlayerDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateDark: float = ParamField(
        float, "defPlayerDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRatePhysics: float = ParamField(
        float, "defEnemyDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateMagic: float = ParamField(
        float, "defEnemyDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateFire: float = ParamField(
        float, "defEnemyDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateThunder: float = ParamField(
        float, "defEnemyDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateDark: float = ParamField(
        float, "defEnemyDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefObjDmgCorrectRate: float = ParamField(
        float, "defObjDmgCorrectRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRatePhysics: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateMagic: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateFire: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateThunder: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateDark: float = ParamField(
        float, "atkPlayerDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRatePhysics: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateMagic: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateFire: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateThunder: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateDark: float = ParamField(
        float, "atkEnemyDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistFreezeChangeRate: float = ParamField(
        float, "registFreezeChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange1: int = ParamField(
        ushort, "invocationConditionsStateChange1", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange2: int = ParamField(
        ushort, "invocationConditionsStateChange2", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange3: int = ParamField(
        ushort, "invocationConditionsStateChange3", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HearingAiSoundLevel: int = ParamField(
        short, "hearingAiSoundLevel", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrProxyHeightRate: float = ParamField(
        float, "chrProxyHeightRate", default=1.0,
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
        float, "hearingSearchRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchEnemyAdd: float = ParamField(
        float, "hearingSearchEnemyAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ValueMagnification: float = ParamField(
        float, "value_Magnification", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ArtsConsumptionRate: float = ParamField(
        float, "artsConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicConsumptionRate: float = ParamField(
        float, "magicConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ShamanConsumptionRate: float = ParamField(
        float, "shamanConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MiracleConsumptionRate: float = ParamField(
        float, "miracleConsumptionRate", default=1.0,
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
        float, "changeHpEstusFlaskCorrectRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpEstusFlaskCorrectRate: float = ParamField(
        float, "changeMpEstusFlaskCorrectRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyIdOnGetSoul: int = ParamField(
        int, "applyIdOnGetSoul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExtendLifeRate: float = ParamField(
        float, "extendLifeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ContractLifeRate: float = ParamField(
        float, "contractLifeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefObjectAttackPowerRate: float = ParamField(
        float, "defObjectAttackPowerRate", default=1.0,
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
        byte, "deleteCriteriaDamage", SP_EFFECT_PARAM_DELETE_DAMAGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange3: int = ParamField(
        byte, "magicSubCategoryChange3", ATK_SUB_CATEGORY, default=0,
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
        byte, "wetConditionDepth", SP_EFFECT_WET_CONDITION_DEPTH, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeSaRecoveryVelocity: float = ParamField(
        float, "changeSaRecoveryVelocity", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegainRate: float = ParamField(
        float, "regainRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SaAttackPowerRate: float = ParamField(
        float, "saAttackPowerRate", default=1.0,
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
        float, "registSleepChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistMadnessChangeRate: float = ParamField(
        float, "registMadnessChangeRate", default=1.0,
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
        byte, "applyPartsGroup", SP_EFFECT_APPLY_PARTS_GROUP, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ClearTarget: bool = ParamField(
        byte, "clearTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreAjin: bool = ParamField(
        byte, "fakeTargetIgnoreAjin:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreMirageArts: bool = ParamField(
        byte, "fakeTargetIgnoreMirageArts:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestForceJoinBlackSOSB: bool = ParamField(
        byte, "requestForceJoinBlackSOS_B:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unk3534: bool = ParamField(
        byte, "unk353_4:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    ChangeSuperArmorPoint: float = ParamField(
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
        float, "poisonDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseDefDamageRate: float = ParamField(
        float, "diseaseDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodDefDamageRate: float = ParamField(
        float, "bloodDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CurseDefDamageRate: float = ParamField(
        float, "curseDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeDefDamageRate: float = ParamField(
        float, "freezeDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepDefDamageRate: float = ParamField(
        float, "sleepDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessDefDamageRate: float = ParamField(
        float, "madnessDefDamageRate", default=1.0,
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
        float, "goodsConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk2: float = ParamField(
        float, "unk2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "unk3[4]")
