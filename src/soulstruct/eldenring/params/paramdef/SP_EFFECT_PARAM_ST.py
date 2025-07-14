from __future__ import annotations

__all__ = ["SP_EFFECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SP_EFFECT_PARAM_ST(ParamRow):
    StatusIcon: int = ParamField(
        int32, "iconId", game_type=Icon, default=-1,
        tooltip="Icon that appears in HUD under stamina bar while special effect is active. Set to -1 for no icon.",
    )
    MaxHPPercentageForEffect: float = ParamField(
        float32, "conditionHp", default=-1.0,
        tooltip="Special effect will only take effect if character's current HP is less than or equal to this "
                "percentage (from 0 to 100). Set to -1 for no HP condition.",
    )
    EffectDuration: float = ParamField(
        float32, "effectEndurance", default=0.0,
        tooltip="Duration of special effect. Set to 0 for an effect that occurs for only one frame (e.g. to award "
                "souls) or to -1 for an effect that will last until specifically removed or its source is lost (e.g. "
                "rings).",
    )
    UpdateInterval: float = ParamField(
        float32, "motionInterval", default=0.0,
        tooltip="Time (in seconds) between applications of the special effect, while active. Set to higher values to "
                "have the effect apply less frequently. Set to 0 to have it occur every frame.",
    )
    MaxHPMultiplier: float = ParamField(
        float32, "maxHpRate", default=1.0,
        tooltip="Multiplier applied to maximum HP.",
    )
    MaxMPMultiplier: float = ParamField(
        float32, "maxMpRate", default=1.0,
        tooltip="Multiplier applied to maximum MP. (Unused in Dark Souls; does NOT refer to spell usages.)",
    )
    MaxStaminaMultiplier: float = ParamField(
        float32, "maxStaminaRate", default=1.0,
        tooltip="Multiplier applied to maximum stamina.",
    )
    IncomingSlashDamageMultiplier: float = ParamField(
        float32, "slashDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming slashing physical damage.",
    )
    IncomingStrikeDamageMultiplier: float = ParamField(
        float32, "blowDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming striking physical damage.",
    )
    IncomingThrustDamageMultiplier: float = ParamField(
        float32, "thrustDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming thrusting physical damage.",
    )
    IncomingNeutralDamageMultiplier: float = ParamField(
        float32, "neutralDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming neutral physical damage.",
    )
    IncomingMagicDamageMultiplier: float = ParamField(
        float32, "magicDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming magic damage.",
    )
    IncomingFireDamageMultiplier: float = ParamField(
        float32, "fireDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming fire damage.",
    )
    IncomingLightningDamageMultiplier: float = ParamField(
        float32, "thunderDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming lightning damage.",
    )
    OutgoingPhysicalDamageMultiplier: float = ParamField(
        float32, "physicsAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing physical damage (of any type).",
    )
    OutgoingMagicDamageMultiplier: float = ParamField(
        float32, "magicAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing magic damage.",
    )
    OutgoingFireDamageMultiplier: float = ParamField(
        float32, "fireAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing fire damage.",
    )
    OutgoingLightningDamageMultiplier: float = ParamField(
        float32, "thunderAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing lightning damage.",
    )
    PhysicalAttackPowerMultiplier: float = ParamField(
        float32, "physicsAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's physical attack power (of any type).",
    )
    MagicAttackPowerMultiplier: float = ParamField(
        float32, "magicAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's magic attack power.",
    )
    FireAttackPowerMultiplier: float = ParamField(
        float32, "fireAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's fire attack power.",
    )
    LightningAttackPowerMultiplier: float = ParamField(
        float32, "thunderAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's lightning attack power.",
    )
    PhysicalAttackPowerAddition: int = ParamField(
        int32, "physicsAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's physical attack power (of any type).",
    )
    MagicAttackPowerAddition: int = ParamField(
        int32, "magicAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's magic attack power.",
    )
    FireAttackPowerAddition: int = ParamField(
        int32, "fireAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's fire attack power.",
    )
    LightningAttackPowerAddition: int = ParamField(
        int32, "thunderAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's lightning attack power.",
    )
    PhysicalDefenseMultiplier: float = ParamField(
        float32, "physicsDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's physical defense (all types).",
    )
    MagicDefenseMultiplier: float = ParamField(
        float32, "magicDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's magic defense.",
    )
    FireDefenseMultiplier: float = ParamField(
        float32, "fireDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's fire defense.",
    )
    LightningDefenseMultiplier: float = ParamField(
        float32, "thunderDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's lightning defense.",
    )
    PhysicalDefenseAddition: int = ParamField(
        int32, "physicsDiffence", default=0,
        tooltip="Value to add to or subtract from character's physical defense.",
    )
    MagicDefenseAddition: int = ParamField(
        int32, "magicDiffence", default=0,
        tooltip="Value to add to or subtract from character's magic defense.",
    )
    FireDefenseAddition: int = ParamField(
        int32, "fireDiffence", default=0,
        tooltip="Value to add to or subtract from character's fire defense.",
    )
    LightningDefenseAddition: int = ParamField(
        int32, "thunderDiffence", default=0,
        tooltip="Value to add to or subtract from character's lightning defense.",
    )
    NoGuardIncomingDamageMultiplier: float = ParamField(
        float32, "NoGuardDamageRate", default=0.0,
        tooltip="Multiplier to use instead of usual multiplier if character is not guarding. (Always set to 0 in "
                "vanilla game, which must deactivate it. Only an educated guess that it refers to incoming damage, "
                "not outgoing.)",
    )
    CriticalHitIncomingDamageMultiplier: float = ParamField(
        float32, "vitalSpotChangeRate", default=-1.0,
        tooltip="Multiplier to use instead of usual multiplier if character is hit in a weak spot. (Always set to -1 "
                "in vanilla game, which deactivates it. Only an educated guess that it affects incoming damage.)",
    )
    NonCriticalHitIncomingDamageMultiplier: float = ParamField(
        float32, "normalSpotChangeRate", default=-1.0,
        tooltip="Multiplier to use instead of usual multiplier if character is *not* hit in a weak spot. (Always set "
                "to -1 in vanilla game, which deactivates it. Only an educated guess that it affects incoming "
                "damage.)",
    )
    LookAtTargetPosOffset: float = ParamField(
        float32, "lookAtTargetPosOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorToTrigger: int = ParamField(
        int32, "behaviorId", game_type=BehaviorParam, default=-1,
        tooltip="Behavior ID to trigger (which can in turn trigger an Attack or Bullet) whenever special effect is "
                "applied. Set to -1 to use no behavior.",
    )
    HPReductionPercentage: float = ParamField(
        float32, "changeHpRate", default=0.0,
        tooltip="Percentage reduction of maximum HP (from 0 to 100). Negative values (to -100) will restore that "
                "percentage instead. Applied every time the special effect updates.",
    )
    HPPointsLost: int = ParamField(
        int32, "changeHpPoint", default=0,
        tooltip="HP value to subtract (if positive) or add (if negative) to character's current HP on every update of "
                "the special effect.",
    )
    MPReductionPercentage: float = ParamField(
        float32, "changeMpRate", default=0.0,
        tooltip="Percentage reduction of maximum MP (from 0 to 100). Negative values (to -100) will restore that "
                "percentage instead. Applied every time the special effect updates. (Unused in Dark Souls 1.)",
    )
    MPPointsLost: int = ParamField(
        int32, "changeMpPoint", default=0,
        tooltip="MP value to subtract (if positive) or add (if negative) to character's current MP on every update of "
                "the special effect. (Unused in Dark Souls 1.)",
    )
    MPRecoverySpeedChange: int = ParamField(
        int32, "mpRecoverChangeSpeed", default=0,
        tooltip="Points added to or subtracted from MP recovery formula. (Unused in Dark Souls 1.)",
    )
    StaminaReductionPercentage: float = ParamField(
        float32, "changeStaminaRate", default=0.0,
        tooltip="Percentage reduction of maximum stamina (from 0 to 100). Negative values (to -100) will restore that "
                "percentage instead. Applied every time the special effect updates.",
    )
    StaminaPointsLost: int = ParamField(
        int32, "changeStaminaPoint", default=0,
        tooltip="Stamina value to subtract (if positive) or add (if negative) to character's current stamina on every "
                "update of the special effect.",
    )
    StaminaRecoverySpeedChange: int = ParamField(
        int32, "staminaRecoverChangeSpeed", default=0,
        tooltip="Points added to or subtracted from stamina recovery formula. I believe this affects the amount of "
                "stamina restored every second. (For reference, a Green Blossom adds 40 points.)",
    )
    MagicEffectTimeChange: float = ParamField(
        float32, "magicEffectTimeChange", default=0.0,
        tooltip="Name suggests this changes the duration of magic effects, but it is never used (always zero).",
    )
    CurrentDurabilityAddition: int = ParamField(
        int32, "insideDurability", default=0,
        tooltip="Amount of durability to subtract (if positive) or add (if negative) to current durability on every "
                "update of the special effect. The equipment affected is determined by...",
    )
    MaxDurabilityAddition: int = ParamField(
        int32, "maxDurability", default=0,
        tooltip="Amount of durability to subtract (if positive) or add (if negative) to the character's maximum "
                "durability while the special effect is active. The equipment affected is determined by...",
    )
    OutgoingStaminaDamageMultiplier: float = ParamField(
        float32, "staminaAttackRate", default=1.0,
        tooltip="Multiplier applied to the amount of damage dealt to targets' stamina.",
    )
    PoisonDamage: int = ParamField(
        int32, "poizonAttackPower", default=0,
        tooltip="Amount of poison damage (in units of resistance) added to the character on every update. Negative "
                "values will heal poison damage instead (e.g. Purple Moss Clump). Unclear how this distinguishes "
                "between reducing build-up and actually healing the status.",
    )
    DiseaseAttackPower: int = ParamField(
        int32, "diseaseAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BloodAttackPower: int = ParamField(
        int32, "bloodAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseAttackPower: int = ParamField(
        int32, "curseAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageMultiplier: float = ParamField(
        float32, "fallDamageRate", default=0.0,
        tooltip="Multiplier applied to amount of fall damage taken by character. Cannot prevent lethal falls.",
    )
    SoulsFromKillsMultiplier: float = ParamField(
        float32, "soulRate", default=0.0,
        tooltip="Multiplier applied to the amount of souls received when enemies or bosses are killed.",
    )
    MaxEquipLoadMultiplier: float = ParamField(
        float32, "equipWeightChangeRate", default=0.0,
        tooltip="Multiplier applied to the character's maximum equip load.",
    )
    MaxItemLoadMultiplier: float = ParamField(
        float32, "allItemWeightChangeRate", default=0.0,
        tooltip="Multiplier applied to how much the character can carry, equipped or not. Seems to have no effect in "
                "Dark Souls 1.",
    )
    SoulAmountChange: int = ParamField(
        int32, "soul", default=0,
        tooltip="Amount of souls received (if positive) or taken away (if negative) every time the special effect is "
                "updated.",
    )
    AnimationIDOffset: int = ParamField(
        int32, "animIdOffset", default=-1,
        tooltip="Override default animation ID offset of character, which can change their animation set temporarily.",
    )
    SoulRewardMultiplier: float = ParamField(
        float32, "haveSoulRate", default=1.0,
        tooltip="Multiplier applied to the amount of souls given to the player when they kill this character (e.g. "
                "enemies in NG+).",
    )
    TargetPriorityChange: float = ParamField(
        float32, "targetPriority", default=0.0,
        tooltip="Value added to or subtract from this character's priority in the target queue. Higher priority means "
                "they are more likely to be targeted by enemies.",
    )
    SightSearchEnemyRate: float = ParamField(
        float32, "sightSearchEnemyRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyHearingMultiplier: float = ParamField(
        float32, "hearingSearchEnemyRate", default=1.0,
        tooltip="Percentage multiplier in enemy hearing range when looking for this character.",
    )
    AnimationSpeedMultiplier: float = ParamField(
        float32, "grabityRate", default=1.0,
        tooltip="Multiplier applied to all of this character's animations. Values other than 1 can lead to cool but "
                "potentially glitchy behavior (e.g. desynchronized grab animations and missed collision).",
    )
    PoisonResistanceMultiplier: float = ParamField(
        float32, "registPoizonChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum poison resistance.",
    )
    RegistDiseaseChangeRate: float = ParamField(
        float32, "registDiseaseChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BleedResistanceMultiplier: float = ParamField(
        float32, "registBloodChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum bleed resistance.",
    )
    CurseResistanceMultiplier: float = ParamField(
        float32, "registCurseChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum curse resistance.",
    )
    SoulStealMultiplier: float = ParamField(
        float32, "soulStealRate", default=0.0,
        tooltip="Internal description says 'defense against HP when NPCs are robbed by soul steal'. Probably unused.",
    )
    EffectDurationMultiplier: float = ParamField(
        float32, "lifeReductionRate", default=0.0,
        tooltip="Multiplier applied to the duration of the effect specified in EffectDurationMultiplierType. Used "
                "only by Hawkeye Gough to reduce poison and toxic duration in vanilla game.",
    )
    HPRecoveryRate: float = ParamField(
        float32, "hpRecoverRate", default=0.0,
        tooltip="Multiplier applied to any increase in character's current HP.",
    )
    NextSpecialEffect: int = ParamField(
        int32, "replaceSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect to apply to character automatically when this special effect ends (if not terminated "
                "manually by an event).",
    )
    SpecialEffectPerUpdate: int = ParamField(
        int32, "cycleOccurrenceSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect to apply to character every time this special effect updates (e.g. Symbol of Avarice "
                "HP reduction).",
    )
    SpecialEffectOnAttack: int = ParamField(
        int32, "atkOccurrenceSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect to apply to any target hit by an attack.  WARNING: This will not trigger unless "
                "SpecialStateIndex is set to 152 (Rotten Pine Resin effect), which will in turn cause your weapon to "
                "glow purple unless the visual effect is disabled.",
    )
    GuardDefenseFlickPowerRate: float = ParamField(
        float32, "guardDefFlickPowerRate", default=1.0,
        tooltip="Unknown; never used.",
    )
    GuardStaminaMultiplier: float = ParamField(
        float32, "guardStaminaCutRate", default=1.0,
        tooltip="Values larger than 1 mean *less* stamina is used when blocking.",
    )
    RayCastPassingTime: int = ParamField(
        int16, "rayCastPassedTime", default=-1,
        tooltip="Internal description says 'Gaze passing: activation time (milliseconds).' Likely unused.",
    )
    MagicSubCategoryChange1: int = ParamField(
        uint8, "magicSubCategoryChange1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange2: int = ParamField(
        uint8, "magicSubCategoryChange2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BowRangePercentageChange: int = ParamField(
        int16, "bowDistRate", default=0,
        tooltip="Percentage change (from 0 to 100) in bow range. Requires SpecialStateIndex BowBoostRange (168) to "
                "work.",
    )
    SpecialEffectCategory: int = ParamField(
        uint16, "spCategory", SP_EFFECT_SPCATEGORY, default=0,
        tooltip="Category of special effect. This effect will override (i.e. cancel out) all other active effects "
                "with the same category when it is added.",
    )
    SpecialEffectPriority: int = ParamField(
        uint8, "categoryPriority", default=0,
        tooltip="Priority ordering for special effect to be applied on each update (lower values are updated first).",
    )
    SaveCategory: int = ParamField(
        int8, "saveCategory", SP_EFFECT_SAVE_CATEGORY, default=-1,
        tooltip="Determines automatic game saving behavior (used for status ailments only). Set to -1 for no saving.",
    )
    AttunementSlotCountChange: int = ParamField(
        uint8, "changeMagicSlot", default=0,
        tooltip="Increase (positive) or decrease (negative) number of attunement slots available.",
    )
    AttunementMiracleSlotCountChange: int = ParamField(
        uint8, "changeMiracleSlot", default=0,
        tooltip="Miracle slots are not even separate from other magic slots, so this is likely an abandoned field.",
    )
    HumanityDamage: int = ParamField(
        int8, "heroPointDamage", default=0,
        tooltip="Damage applied to soft humanity count. Negative values will add soft humanity.",
    )
    RiposteDefenseAddition: int = ParamField(
        uint8, "defFlickPower", default=0,
        tooltip="Value added to or subtracted from defense against riposte attacks.",
    )
    FlickDamageMultiplier: int = ParamField(
        uint8, "flickDamageCutRate", default=0,
        tooltip="Multiplier to use instead of usual multiplier on incoming (I assume) riposte attacks. Never used.",
    )
    IncomingBleedDamagePercentage: int = ParamField(
        uint8, "bloodDamageRate", default=100,
        tooltip="Percentage of incoming bleed damage received (usually 100).",
    )
    ReplaceNoImpactLevel: int = ParamField(
        int8, "dmgLv_None", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of NoImpact level.",
    )
    ReplaceSmallImpactLevel: int = ParamField(
        int8, "dmgLv_S", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Small impact level.",
    )
    ReplaceMediumImpactLevel: int = ParamField(
        int8, "dmgLv_M", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Medium impact level.",
    )
    ReplaceLargeImpactLevel: int = ParamField(
        int8, "dmgLv_L", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Large impact level.",
    )
    ReplaceBlowoffImpactLevel: int = ParamField(
        int8, "dmgLv_BlowM", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Blowoff impact level.",
    )
    ReplacePushImpactLevel: int = ParamField(
        int8, "dmgLv_Push", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Push impact level.",
    )
    ReplaceStrikeImpactLevel: int = ParamField(
        int8, "dmgLv_Strike", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Strike impact level.",
    )
    ReplaceSmallBlowImpactLevel: int = ParamField(
        int8, "dmgLv_BlowS", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Blow impact level.",
    )
    ReplaceMinimalImpactLevel: int = ParamField(
        int8, "dmgLv_Min", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Minimal impact level.",
    )
    ReplaceLaunchImpactLevel: int = ParamField(
        int8, "dmgLv_Uppercut", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Launch impact level.",
    )
    ReplaceBlowBackwardImpactLevel: int = ParamField(
        int8, "dmgLv_BlowLL", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of BlowBackward impact level.",
    )
    ReplaceBreathBurnImpactLevel: int = ParamField(
        int8, "dmgLv_Breath", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of BreathBurn impact level.",
    )
    AttackAttribute: int = ParamField(
        uint8, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=254,
        tooltip="Attack type attached to hits while special effect is active.",
    )
    ElementAttribute: int = ParamField(
        uint8, "spAttribute", ATKPARAM_SPATTR_TYPE, default=254,
        tooltip="Element attached to hits while special effect is active.",
    )
    SpecialState: int = ParamField(
        uint16, "stateInfo", SP_EFFECT_TYPE, default=0,
        tooltip="Hard-coded special state to use. Also determines visual effect from Special Effect Visuals table.",
    )
    AffectedWeaponType: int = ParamField(
        uint8, "wepParamChange", SP_EFE_WEP_CHANGE_PARAM, default=0,
        tooltip="Weapon category that is affected by special effect. ",
    )
    MovementType: int = ParamField(
        uint8, "moveType", SP_EFFECT_MOVE_TYPE, default=0,
        tooltip="Determines how movement is affected. (Does not correspond to Movement param entries.)",
    )
    EffectDurationMultiplierType: int = ParamField(
        uint16, "lifeReductionType", SP_EFFECT_TYPE, default=0,
        tooltip="Type of effect whose duration is affected by EffectDurationMultiplier. Known values: 2 = poison, 5 = "
                "toxic.",
    )
    ThrowCondition: int = ParamField(
        uint8, "throwCondition", SP_EFFECT_THROW_CONDITION_TYPE, default=0,
        tooltip="Determines how throws are affected while special effect is active. Values still unknown (rarely "
                "used).",
    )
    AddBehaviorJudgeIDCondition: int = ParamField(
        int8, "addBehaviorJudgeId_condition", default=-1,
        tooltip="Unclear; used only to manage the Hydra as more heads are cut off. All other values are -1.",
    )
    FreezeDamageRate: int = ParamField(
        uint8, "freezeDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectSelf: bool = ParamField(
        uint8, "effectTargetSelf:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target self.",
    )
    CanAffectAlly: bool = ParamField(
        uint8, "effectTargetFriend:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target self.",
    )
    CanAffectEnemy: bool = ParamField(
        uint8, "effectTargetEnemy:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target enemies.",
    )
    CanAffectPlayer: bool = ParamField(
        uint8, "effectTargetPlayer:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target player characters.",
    )
    CanAffectAI: bool = ParamField(
        uint8, "effectTargetAI:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target non-player characters.",
    )
    CanAffectPlayers: bool = ParamField(
        uint8, "effectTargetLive:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target humans.",
    )
    CanAffectPhantoms: bool = ParamField(
        uint8, "effectTargetGhost:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target phantoms (white or black).",
    )
    DisableSleep: bool = ParamField(
        uint8, "disableSleep:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMadness: bool = ParamField(
        uint8, "disableMadness:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectAttacker: bool = ParamField(
        uint8, "effectTargetAttacker:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target character when they attack (e.g. HP drain).",
    )
    DisplayIconWhenInactive: bool = ParamField(
        uint8, "dispIconNonactive:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Display icon even when special effect is inactive (not sure what that means). Never enabled.",
    )
    RegainGaugeDamage: bool = ParamField(
        uint8, "regainGaugeDamage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    UseIntelligenceScaling: bool = ParamField(
        uint8, "bAdjustMagicAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, special effect damage will be scaled by character intelligence (I believe).",
    )
    UseFaithScaling: bool = ParamField(
        uint8, "bAdjustFaithAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, special effect damage will be scaled by character faith (I believe).",
    )
    ForNewGamePlus: bool = ParamField(
        uint8, "bGameClearBonus:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, this effect will be applied multiple times depending on the NG+ cycle (I think).",
    )
    AffectsMagic: bool = ParamField(
        uint8, "magParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, multipliers will be applied to magic attacks.",
    )
    AffectsMiracles: bool = ParamField(
        uint8, "miracleParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, multipliers will be applied to miracle attacks.",
    )
    ClearSoul: bool = ParamField(
        uint8, "clearSoul:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unused Demon's Souls remnant.",
    )
    RequestWhitePhantomSummon: bool = ParamField(
        uint8, "requestSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by White Sign Soapstone.",
    )
    RequestBlackPhantomSummon: bool = ParamField(
        uint8, "requestBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Red Sign Soapstone.",
    )
    RequestInvasion: bool = ParamField(
        uint8, "requestForceJoinBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only be (Cracked) Red Eye Orb.",
    )
    RequestKick: bool = ParamField(
        uint8, "requestKickSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Not used by any item. Likely kicks all clients out of your world.",
    )
    RequestReturnToOwnWorld: bool = ParamField(
        uint8, "requestLeaveSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Black Separation Crystal.",
    )
    RequestNPCInvasion: bool = ParamField(
        uint8, "requestNpcInveda:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Black Eye Orb (Lautrec quest and cut Shiva quest).",
    )
    Immortal: bool = ParamField(
        uint8, "noDead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character cannot die. Never used in vanilla game.",
    )
    CurrentHPIgnoresMaxHPChange: bool = ParamField(
        uint8, "bCurrHPIndependeMaxHP:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, changes to maximum HP will not affect current HP (unless it must be reduced to new "
                "maximum).",
    )
    IgnoreCorrosion: bool = ParamField(
        uint8, "corrosionIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore corrosion damage to durability. Used only by Demon's Souls junk.",
    )
    IgnoreSightReduction: bool = ParamField(
        uint8, "sightSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore any changes to their sight range from other special effects. Used "
                "only by Demon's Souls junk.",
    )
    IgnoreHearingReduction: bool = ParamField(
        uint8, "hearingSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore any changes to their hearing range from other special effects. Used "
                "only by Demon's Souls junk.",
    )
    IgnoreMagicDisabling: bool = ParamField(
        uint8, "antiMagicIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore any special effect that attempts to disable their magic. Used only by "
                "Demon's Souls junk.",
    )
    IgnoreFakeTargets: bool = ParamField(
        uint8, "fakeTargetIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unknown; never used.",
    )
    IgnoreUndeadFakeTargets: bool = ParamField(
        uint8, "fakeTargetIgnoreUndead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unknown; never used.",
    )
    IgnoreBeastFakeTargets: bool = ParamField(
        uint8, "fakeTargetIgnoreAnimal:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unknown; never used.",
    )
    IgnoreGravity: bool = ParamField(
        uint8, "grabityIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Ignore gravity. (Not sure if this actually works.)",
    )
    PoisonImmunity: bool = ParamField(
        uint8, "disablePoison:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to poison.",
    )
    ToxicImmunity: bool = ParamField(
        uint8, "disableDisease:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to toxic.",
    )
    BleedImmunity: bool = ParamField(
        uint8, "disableBlood:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to curse.",
    )
    CurseImmunity: bool = ParamField(
        uint8, "disableCurse:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to poison.",
    )
    EnableCharming: bool = ParamField(
        uint8, "enableCharm:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Not sure if this refers to the Alluring Skull. May not work at all.",
    )
    EnableLifeTime: bool = ParamField(
        uint8, "enableLifeTime:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Internal description: 'Is the life extended when setting a flag by TAE?'. Effect unknown. Used by "
                "Dragon Head and Torso Stones and some internal summon-related effects.",
    )
    UseStrengthScaling: bool = ParamField(
        uint8, "bAdjustStrengthAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    UseDexterityScaling: bool = ParamField(
        uint8, "bAdjustAgilityAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EraseOnBonfireRecover: bool = ParamField(
        uint8, "eraseOnBonfireRecover:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    GrabAttackParamChange: bool = ParamField(
        uint8, "throwAttackParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    RequestColiseumExit: bool = ParamField(
        uint8, "requestLeaveColiseumSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Purple Coward's Crystal.",
    )
    AffectedByEffectExtension: bool = ParamField(
        uint8, "isExtendSpEffectLife:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, this special effect will be affected by special state (193), i.e. the effect used by the "
                "vanilla Lingering Dragoncrest Ring, that extends effect durations.",
    )
    HasTarget: bool = ParamField(
        uint8, "hasTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ReplanningOnFire: bool = ParamField(
        uint8, "replanningOnFire:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCharactersWithNoCovenant: bool = ParamField(
        uint8, "vowType0:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters with no covenant.",
    )
    AffectsWayOfWhite: bool = ParamField(
        uint8, "vowType1:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Way of White covenant.",
    )
    AffectsPrincessGuard: bool = ParamField(
        uint8, "vowType2:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Princess's Guard covenant.",
    )
    AffectsWarriorOfSunlight: bool = ParamField(
        uint8, "vowType3:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Warriors of Sunlight covenant.",
    )
    AffectsDarkwraith: bool = ParamField(
        uint8, "vowType4:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Darkwraith covenant.",
    )
    AffectsPathOfTheDragon: bool = ParamField(
        uint8, "vowType5:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Path of the Dragon covenant.",
    )
    AffectsGravelordServant: bool = ParamField(
        uint8, "vowType6:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Gravelord Servant covenant.",
    )
    AffectsForestHunter: bool = ParamField(
        uint8, "vowType7:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Forest Hunters covenant.",
    )
    AffectsDarkmoonBlade: bool = ParamField(
        uint8, "vowType8:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Blades of the Darkmoon covenant.",
    )
    AffectsChaosServant: bool = ParamField(
        uint8, "vowType9:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Chaos Servants covenant.",
    )
    AffectsCovenant10: bool = ParamField(
        uint8, "vowType10:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant11: bool = ParamField(
        uint8, "vowType11:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant12: bool = ParamField(
        uint8, "vowType12:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant13: bool = ParamField(
        uint8, "vowType13:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant14: bool = ParamField(
        uint8, "vowType14:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant15: bool = ParamField(
        uint8, "vowType15:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    RepAtkDmgLv: int = ParamField(
        int8, "repAtkDmgLv", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchRate: float = ParamField(
        float32, "sightSearchRate", default=1.0,
        tooltip="TODO",
    )
    EffectTargetsEnemyTarget: bool = ParamField(
        uint8, "effectTargetOpposeTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EffectTargetsAllyTarget: bool = ParamField(
        uint8, "effectTargetFriendlyTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EffectTargetsSelfTarget: bool = ParamField(
        uint8, "effectTargetSelfTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EffectTargetPcHorse: bool = ParamField(
        uint8, "effectTargetPcHorse:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectTargetPcDeceased: bool = ParamField(
        uint8, "effectTargetPcDeceased:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsContractSpEffectLife: bool = ParamField(
        uint8, "isContractSpEffectLife:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWaitModeDelete: bool = ParamField(
        uint8, "isWaitModeDelete:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsIgnoreNoDamage: bool = ParamField(
        uint8, "isIgnoreNoDamage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ChangeTeamType: int = ParamField(
        int8, "changeTeamType", SP_EFFECT_CHANGE_TEAM_TYPE, default=-1,
        tooltip="TODO",
    )
    DmypolyId: int = ParamField(
        int16, "dmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId: int = ParamField(
        int32, "vfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuOverFireId: int = ParamField(
        int32, "accumuOverFireId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuOverVal: int = ParamField(
        int32, "accumuOverVal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuUnderFireId: int = ParamField(
        int32, "accumuUnderFireId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuUnderVal: int = ParamField(
        int32, "accumuUnderVal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccumuVal: int = ParamField(
        int32, "accumuVal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeangX: int = ParamField(
        uint8, "eye_angX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeangY: int = ParamField(
        uint8, "eye_angY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddDeceasedLv: int = ParamField(
        int16, "addDeceasedLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VfxId1: int = ParamField(
        int32, "vfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId2: int = ParamField(
        int32, "vfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId3: int = ParamField(
        int32, "vfxId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId4: int = ParamField(
        int32, "vfxId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId5: int = ParamField(
        int32, "vfxId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId6: int = ParamField(
        int32, "vfxId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VfxId7: int = ParamField(
        int32, "vfxId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FreezeAttackPower: int = ParamField(
        int32, "freezeAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AppearAiSoundId: int = ParamField(
        int32, "AppearAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddFootEffectSfxId: int = ParamField(
        int16, "addFootEffectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DexterityCancelSystemOnlyAddDexterity: int = ParamField(
        int8, "dexterityCancelSystemOnlyAddDexterity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TeamOffenseEffectivity: int = ParamField(
        int8, "teamOffenseEffectivity", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessDamageCutRate: float = ParamField(
        float32, "toughnessDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateA: float = ParamField(
        float32, "weakDmgRateA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateB: float = ParamField(
        float32, "weakDmgRateB", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateC: float = ParamField(
        float32, "weakDmgRateC", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateD: float = ParamField(
        float32, "weakDmgRateD", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateE: float = ParamField(
        float32, "weakDmgRateE", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDmgRateF: float = ParamField(
        float32, "weakDmgRateF", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float32, "darkDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDiffenceRate: float = ParamField(
        float32, "darkDiffenceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDiffence: int = ParamField(
        int32, "darkDiffence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackRate: float = ParamField(
        float32, "darkAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackPowerRate: float = ParamField(
        float32, "darkAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackPower: int = ParamField(
        int32, "darkAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AntiDarkSightRadius: float = ParamField(
        float32, "antiDarkSightRadius", default=0.0,
        tooltip="TODO",
    )
    AntiDarkSightModelPoint: int = ParamField(
        int32, "antiDarkSightDmypolyId", game_type=ModelDummy, default=-1,
        tooltip="TODO",
    )
    ConditionHPRate: float = ParamField(
        float32, "conditionHpRate", default=-1.0,
        tooltip="TODO",
    )
    StaminaConsumptionRate: float = ParamField(
        float32, "consumeStaminaRate", default=1.0,
        tooltip="TODO",
    )
    ItemDropRate: float = ParamField(
        float32, "itemDropRate", default=0.0,
        tooltip="TODO",
    )
    ChangePoisonResistance: int = ParamField(
        int32, "changePoisonResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeToxicResistance: int = ParamField(
        int32, "changeDiseaseResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeBleedingResistance: int = ParamField(
        int32, "changeBloodResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeFrenzyResistance: int = ParamField(
        int32, "changeCurseResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeFreezeResistPoint: int = ParamField(
        int32, "changeFreezeResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackRate: float = ParamField(
        float32, "slashAttackRate", default=1.0,
        tooltip="TODO",
    )
    BluntAttackRate: float = ParamField(
        float32, "blowAttackRate", default=1.0,
        tooltip="TODO",
    )
    ThrustAttackRate: float = ParamField(
        float32, "thrustAttackRate", default=1.0,
        tooltip="TODO",
    )
    NeutralAttackRate: float = ParamField(
        float32, "neutralAttackRate", default=1.0,
        tooltip="TODO",
    )
    SlashAttackPowerRate: float = ParamField(
        float32, "slashAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    BluntAttackPowerRate: float = ParamField(
        float32, "blowAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    ThrustAttackPowerRate: float = ParamField(
        float32, "thrustAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    NeutralAttackPowerRate: float = ParamField(
        float32, "neutralAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    SlashAttackPower: int = ParamField(
        int32, "slashAttackPower", default=0,
        tooltip="TODO",
    )
    BluntAttackPower: int = ParamField(
        int32, "blowAttackPower", default=0,
        tooltip="TODO",
    )
    ThrustAttackPower: int = ParamField(
        int32, "thrustAttackPower", default=0,
        tooltip="TODO",
    )
    NeutralAttackPower: int = ParamField(
        int32, "neutralAttackPower", default=0,
        tooltip="TODO",
    )
    ChangeStrength: int = ParamField(
        int32, "changeStrengthPoint", default=0,
        tooltip="TODO",
    )
    ChangeDexterity: int = ParamField(
        int32, "changeAgilityPoint", default=0,
        tooltip="TODO",
    )
    ChangeBloodtinge: int = ParamField(
        int32, "changeMagicPoint", default=0,
        tooltip="TODO",
    )
    ChangeArcane: int = ParamField(
        int32, "changeFaithPoint", default=0,
        tooltip="TODO",
    )
    ChangeLuckPoint: int = ParamField(
        int32, "changeLuckPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointStr: int = ParamField(
        int8, "recoverArtsPoint_Str", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointDex: int = ParamField(
        int8, "recoverArtsPoint_Dex", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointMagic: int = ParamField(
        int8, "recoverArtsPoint_Magic", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RecoverArtsPointMiracle: int = ParamField(
        int8, "recoverArtsPoint_Miracle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessDamageRate: int = ParamField(
        uint8, "madnessDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    IsUseStatusAilmentAtkPowerCorrect: bool = ParamField(
        uint8, "isUseStatusAilmentAtkPowerCorrect:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseAtkParamAtkPowerCorrect: bool = ParamField(
        uint8, "isUseAtkParamAtkPowerCorrect:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DontDeleteOnDead: bool = ParamField(
        uint8, "dontDeleteOnDead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableFreeze: bool = ParamField(
        uint8, "disableFreeze:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableNetSync: bool = ParamField(
        uint8, "isDisableNetSync:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShamanParamChange: bool = ParamField(
        uint8, "shamanParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStopSearchedNotify: bool = ParamField(
        uint8, "isStopSearchedNotify:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckAboveShadowTest: bool = ParamField(
        uint8, "isCheckAboveShadowTest:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AddBehaviorJudgeIDAdd: int = ParamField(
        uint16, "addBehaviorJudgeId_add", default=0,
        tooltip="Always zero. Unknown effect. Internal description suggests that this is a constant added to all "
                "behavior judge IDs (from TAE) issued by character.",
    )
    SaReceiveDamageRate: float = ParamField(
        float32, "saReceiveDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRatePhysics: float = ParamField(
        float32, "defPlayerDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateMagic: float = ParamField(
        float32, "defPlayerDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateFire: float = ParamField(
        float32, "defPlayerDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateThunder: float = ParamField(
        float32, "defPlayerDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefPlayerDmgCorrectRateDark: float = ParamField(
        float32, "defPlayerDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRatePhysics: float = ParamField(
        float32, "defEnemyDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateMagic: float = ParamField(
        float32, "defEnemyDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateFire: float = ParamField(
        float32, "defEnemyDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateThunder: float = ParamField(
        float32, "defEnemyDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefEnemyDmgCorrectRateDark: float = ParamField(
        float32, "defEnemyDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefObjDmgCorrectRate: float = ParamField(
        float32, "defObjDmgCorrectRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRatePhysics: float = ParamField(
        float32, "atkPlayerDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateMagic: float = ParamField(
        float32, "atkPlayerDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateFire: float = ParamField(
        float32, "atkPlayerDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateThunder: float = ParamField(
        float32, "atkPlayerDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPlayerDmgCorrectRateDark: float = ParamField(
        float32, "atkPlayerDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRatePhysics: float = ParamField(
        float32, "atkEnemyDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateMagic: float = ParamField(
        float32, "atkEnemyDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateFire: float = ParamField(
        float32, "atkEnemyDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateThunder: float = ParamField(
        float32, "atkEnemyDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnemyDmgCorrectRateDark: float = ParamField(
        float32, "atkEnemyDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistFreezeChangeRate: float = ParamField(
        float32, "registFreezeChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange1: int = ParamField(
        uint16, "invocationConditionsStateChange1", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange2: int = ParamField(
        uint16, "invocationConditionsStateChange2", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvocationConditionsStateChange3: int = ParamField(
        uint16, "invocationConditionsStateChange3", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HearingAiSoundLevel: int = ParamField(
        int16, "hearingAiSoundLevel", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrProxyHeightRate: float = ParamField(
        float32, "chrProxyHeightRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AddAwarePointCorrectValueforMe: float = ParamField(
        float32, "addAwarePointCorrectValue_forMe", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddAwarePointCorrectValueforTarget: float = ParamField(
        float32, "addAwarePointCorrectValue_forTarget", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchEnemyAdd: float = ParamField(
        float32, "sightSearchEnemyAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchAdd: float = ParamField(
        float32, "sightSearchAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchAdd: float = ParamField(
        float32, "hearingSearchAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HearingSearchRate: float = ParamField(
        float32, "hearingSearchRate", default=1.0,
        tooltip="TODO",
    )
    HearingSearchEnemyAdd: float = ParamField(
        float32, "hearingSearchEnemyAdd", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ValueMagnification: float = ParamField(
        float32, "value_Magnification", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ArtsConsumptionRate: float = ParamField(
        float32, "artsConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicConsumptionRate: float = ParamField(
        float32, "magicConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ShamanConsumptionRate: float = ParamField(
        float32, "shamanConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MiracleConsumptionRate: float = ParamField(
        float32, "miracleConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpEstusFlaskRate: int = ParamField(
        int32, "changeHpEstusFlaskRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpEstusFlaskPoint: int = ParamField(
        int32, "changeHpEstusFlaskPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpEstusFlaskRate: int = ParamField(
        int32, "changeMpEstusFlaskRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpEstusFlaskPoint: int = ParamField(
        int32, "changeMpEstusFlaskPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeHpEstusFlaskCorrectRate: float = ParamField(
        float32, "changeHpEstusFlaskCorrectRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMpEstusFlaskCorrectRate: float = ParamField(
        float32, "changeMpEstusFlaskCorrectRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyIdOnGetSoul: int = ParamField(
        int32, "applyIdOnGetSoul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExtendLifeRate: float = ParamField(
        float32, "extendLifeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ContractLifeRate: float = ParamField(
        float32, "contractLifeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefObjectAttackPowerRate: float = ParamField(
        float32, "defObjectAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EffectEndDeleteDecalGroupId: int = ParamField(
        int16, "effectEndDeleteDecalGroupId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AddLifeForceStatus: int = ParamField(
        int8, "addLifeForceStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddWillpowerStatus: int = ParamField(
        int8, "addWillpowerStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddEndureStatus: int = ParamField(
        int8, "addEndureStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddVitalityStatus: int = ParamField(
        int8, "addVitalityStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddStrengthStatus: int = ParamField(
        int8, "addStrengthStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddDexterityStatus: int = ParamField(
        int8, "addDexterityStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddMagicStatus: int = ParamField(
        int8, "addMagicStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddFaithStatus: int = ParamField(
        int8, "addFaithStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AddLuckStatus: int = ParamField(
        int8, "addLuckStatus", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeleteCriteriaDamage: int = ParamField(
        uint8, "deleteCriteriaDamage", SP_EFFECT_PARAM_DELETE_DAMAGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange3: int = ParamField(
        uint8, "magicSubCategoryChange3", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpAttributeVariationValue: int = ParamField(
        uint8, "spAttributeVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkFlickPower: int = ParamField(
        uint8, "atkFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WetConditionDepth: int = ParamField(
        uint8, "wetConditionDepth", SP_EFFECT_WET_CONDITION_DEPTH, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeSaRecoveryVelocity: float = ParamField(
        float32, "changeSaRecoveryVelocity", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegainRate: float = ParamField(
        float32, "regainRate", default=1.0,
        tooltip="TODO",
    )
    SaAttackPowerRate: float = ParamField(
        float32, "saAttackPowerRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepAttackPower: int = ParamField(
        int32, "sleepAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessAttackPower: int = ParamField(
        int32, "madnessAttackPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RegistSleepChangeRate: float = ParamField(
        float32, "registSleepChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegistMadnessChangeRate: float = ParamField(
        float32, "registMadnessChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeSleepResistPoint: int = ParamField(
        int32, "changeSleepResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeMadnessResistPoint: int = ParamField(
        int32, "changeMadnessResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SleepDamageRate: int = ParamField(
        uint8, "sleepDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ApplyPartsGroup: int = ParamField(
        uint8, "applyPartsGroup", SP_EFFECT_APPLY_PARTS_GROUP, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ClearTarget: bool = ParamField(
        uint8, "clearTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreAjin: bool = ParamField(
        uint8, "fakeTargetIgnoreAjin:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    FakeTargetIgnoreMirageArts: bool = ParamField(
        uint8, "fakeTargetIgnoreMirageArts:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RequestForceJoinBlackSOSB: bool = ParamField(
        uint8, "requestForceJoinBlackSOS_B:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDestinedDeathHpMult: bool = ParamField(
        uint8, "isDestinedDeathHpMult:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Padbitold: int = ParamField(
        uint8, "padbit_old:3", bit_count=3, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHpBurnEffect: bool = ParamField(
        uint8, "isHpBurnEffect:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x3526: bool = ParamField(
        uint8, "unknown_0x352_6:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x3527: bool = ParamField(
        uint8, "unknown_0x352_7:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    Unknown0x3530: bool = ParamField(
        uint8, "unknown_0x353_0:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x3531: bool = ParamField(
        uint8, "unknown_0x353_1:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x3532: bool = ParamField(
        uint8, "unknown_0x353_2:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x3533: bool = ParamField(
        uint8, "unknown_0x353_3:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x3534: bool = ParamField(
        uint8, "unknown_0x353_4:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "unknown_0x353_5:3", bit_count=3)
    PoiseAddition: float = ParamField(
        float32, "changeSuperArmorPoint", default=0.0,
        tooltip="Amount added (if positive) or subtracted (if negative) from character's poise.",
    )
    ChangeSaPoint: float = ParamField(
        float32, "changeSaPoint", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HugeEnemyPickupHeightOverwrite: float = ParamField(
        float32, "hugeEnemyPickupHeightOverwrite", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonDefDamageRate: float = ParamField(
        float32, "poisonDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseDefDamageRate: float = ParamField(
        float32, "diseaseDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodDefDamageRate: float = ParamField(
        float32, "bloodDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CurseDefDamageRate: float = ParamField(
        float32, "curseDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeDefDamageRate: float = ParamField(
        float32, "freezeDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepDefDamageRate: float = ParamField(
        float32, "sleepDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessDefDamageRate: float = ParamField(
        float32, "madnessDefDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    OverwritemaxBackhomeDist: int = ParamField(
        uint16, "overwrite_maxBackhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverwritebackhomeDist: int = ParamField(
        uint16, "overwrite_backhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverwritebackhomeBattleDist: int = ParamField(
        uint16, "overwrite_backhomeBattleDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteBackHomeLookTargetDist: int = ParamField(
        uint16, "overwrite_BackHome_LookTargetDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodsConsumptionRate: float = ParamField(
        float32, "goodsConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardStaminaMult: float = ParamField(
        float32, "guardStaminaMult", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SpiritDeathSpEffectId: int = ParamField(
        int32, "spiritDeathSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "unk3[4]")
