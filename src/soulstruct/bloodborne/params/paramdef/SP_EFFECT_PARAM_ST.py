from __future__ import annotations

__all__ = ["SP_EFFECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
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
    MaxHPChangeRatio: float = ParamField(
        float32, "maxHpChangeRate", default=0.0,
        tooltip="Appears to be an unused variant of MaxHPMultiplier. Always set to 0.",
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
    ToxicDamage: int = ParamField(
        int32, "registIllness", default=0,
        tooltip="Amount of toxic damage (in units of resistance) added to the character on every update. Negative "
                "values will heal toxic damage instead (e.g. Blooming Purple Moss Clump). Unclear how this "
                "distinguishes between reducing build-up and actually healing the status.",
    )
    BleedDamage: int = ParamField(
        int32, "registBlood", default=0,
        tooltip="Amount of bleed damage (in units of resistance) added to the character on every update. Negative "
                "values will heal bleed damage instead (e.g. Blood-Red Moss Clump). Unclear how this distinguishes "
                "between reducing build-up and actually healing the status.",
    )
    CurseDamage: int = ParamField(
        int32, "registCurse", default=0,
        tooltip="Amount of curse damage (in units of resistance) added to the character on every update. Negative "
                "values will heal curse damage instead (e.g. Purging Stone). Unclear how this distinguishes between "
                "reducing build-up and actually healing the status.",
    )
    FallDamageMultiplier: float = ParamField(
        float32, "fallDamageRate", default=1.0,
        tooltip="Multiplier applied to amount of fall damage taken by character. Cannot prevent lethal falls.",
    )
    SoulsFromKillsMultiplier: float = ParamField(
        float32, "soulRate", default=1.0,
        tooltip="Multiplier applied to the amount of souls received when enemies or bosses are killed.",
    )
    MaxEquipLoadMultiplier: float = ParamField(
        float32, "equipWeightChangeRate", default=1.0,
        tooltip="Multiplier applied to the character's maximum equip load.",
    )
    MaxItemLoadMultiplier: float = ParamField(
        float32, "allItemWeightChangeRate", default=1.0,
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
    EnemySightPercentageReduction: int = ParamField(
        int32, "sightSearchEnemyCut", default=0,
        tooltip="Percentage reduction in enemy sight (from 0 to 100) when looking for this character. Not sure if "
                "negative values can be used to make this character *more* visible.",
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
    ToxicResistanceMultiplier: float = ParamField(
        float32, "registIllnessChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum toxic resistance.",
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
        float32, "soulStealRate", default=1.0,
        tooltip="Internal description says 'defense against HP when NPCs are robbed by soul steal'. Probably unused.",
    )
    EffectDurationMultiplier: float = ParamField(
        float32, "lifeReductionRate", default=1.0,
        tooltip="Multiplier applied to the duration of the effect specified in EffectDurationMultiplierType. Used "
                "only by Hawkeye Gough to reduce poison and toxic duration in vanilla game.",
    )
    HPRecoveryRate: float = ParamField(
        float32, "hpRecoverRate", default=1.0,
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
    PoiseAddition: int = ParamField(
        int16, "changeSuperArmorPoint", default=0,
        tooltip="Amount added (if positive) or subtracted (if negative) from character's poise.",
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
        uint8, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="Attack type attached to hits while special effect is active.",
    )
    ElementAttribute: int = ParamField(
        uint8, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
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
    AddBehaviorJudgeIDAdd: int = ParamField(
        uint8, "addBehaviorJudgeId_add", default=0,
        tooltip="Always zero. Unknown effect. Internal description suggests that this is a constant added to all "
                "behavior judge IDs (from TAE) issued by character.",
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
    CanAffectWhitePhantoms: bool = ParamField(
        uint8, "effectTargetWhiteGhost:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target white phantoms.",
    )
    CanAffectBlackPhantoms: bool = ParamField(
        uint8, "effectTargetBlackGhost:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target white phantoms.",
    )
    CanAffectAttacker: bool = ParamField(
        uint8, "effectTargetAttacker:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target character when they attack (e.g. HP drain).",
    )
    DisplayIconWhenInactive: bool = ParamField(
        uint8, "dispIconNonactive:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Display icon even when special effect is inactive (not sure what that means). Never enabled.",
    )
    UseVisualEffect: bool = ParamField(
        uint8, "useSpEffectEffect:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Use visual effect from Special Effect Visuals table (indexed by Special State field).",
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
    HasTarget: bool = ParamField(
        uint8, "hasTarget : 1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="For unused 'evil eye' mechanics, probably a Demon's Souls remnant.",
    )
    FireImmunity: bool = ParamField(
        uint8, "isFireDamageCancel:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to fire damage. Never enabled, and may not actually work. Needs testing.",
    )
    AffectedByEffectExtension: bool = ParamField(
        uint8, "isExtendSpEffectLife:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, this special effect will be affected by special state (193), i.e. the effect used by the "
                "vanilla Lingering Dragoncrest Ring, that extends effect durations.",
    )
    RequestColiseumExit: bool = ParamField(
        uint8, "requestLeaveColiseumSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Purple Coward's Crystal.",
    )
    DisableBeast: bool = ParamField(
        uint8, "disableTherianthrope:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    ChargeAttackParamChange: bool = ParamField(
        uint8, "chargeAttackParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    GrabAttackParamChange: bool = ParamField(
        uint8, "throwAttackParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableEquipSlotCheck: bool = ParamField(
        uint8, "enableEquipSlotCheck:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
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
    DeathCauseID: int = ParamField(
        uint32, "deathcauseId", default=100,
        tooltip="TODO",
    )
    AntiDarkSightRadius: float = ParamField(
        float32, "antiDarkSightRadius", default=0.0,
        tooltip="TODO",
    )
    AntiDarkSightModelPoint: int = ParamField(
        int32, "antiDarkSightDmypolyId", game_type=ModelDummy, default=-1,
        tooltip="TODO",
    )
    SightSearchRate: float = ParamField(
        float32, "sightSearchRate", default=1.0,
        tooltip="TODO",
    )
    HearingSearchRate: float = ParamField(
        float32, "hearingSearchRate", default=1.0,
        tooltip="TODO",
    )
    ResistBeast: int = ParamField(
        int32, "registTherianthrope", default=0,
        tooltip="TODO",
    )
    ResistBeastChangeRate: float = ParamField(
        float32, "registTherianthropeChangeRate", default=1.0,
        tooltip="TODO",
    )
    ChangeTeamType: int = ParamField(
        int8, "changeTeamType", SP_EFFECT_CHANGE_TEAM_TYPE, default=-1,
        tooltip="TODO",
    )
    UseStrengthScaling: bool = ParamField(
        uint8, "bAdjustStrengthAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    UseDexterityScaling: bool = ParamField(
        uint8, "bAdjustAgilityAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    WeaponConvertAttribute: int = ParamField(
        uint8, "weaponConvertAttribute", SP_EFFECT_CONVERT_ATTRIBUTE, default=0,
        tooltip="TODO",
    )
    ChangeMaxQuantity: int = ParamField(
        int8, "changeMaxQuantity", default=0,
        tooltip="TODO",
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
    StaminaConsumptionRate: float = ParamField(
        float32, "consumeStaminaRate", default=1.0,
        tooltip="TODO",
    )
    AddBullets: int = ParamField(
        int8, "addBulletNum", default=0,
        tooltip="TODO",
    )
    ValidConditionPlayerWeaponState: int = ParamField(
        uint8, "validCond_PCWeponState", SP_EFE_PC_WEAPON_STATE, default=0,
        tooltip="TODO",
    )
    AddBloodBullets: int = ParamField(
        int8, "addTempBulletNum", default=0,
        tooltip="TODO",
    )
    RegainGaugeDamage: int = ParamField(
        uint8, "regainGaugeDamage", SP_EFFECT_BOOL, default=0,
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
    ChangeBeastResistance: int = ParamField(
        int32, "changeTherianthropeResistPoint", default=0,
        tooltip="TODO",
    )
    DemonDamageMultiplier: float = ParamField(
        float32, "antiDemonDamageCorrectRate", default=1.0,
        tooltip="TODO",
    )
    HolyDamageMultiplier: float = ParamField(
        float32, "antiSaintDamageCorrectRate", default=1.0,
        tooltip="TODO",
    )
    WeakADamageMultiplier: float = ParamField(
        float32, "antiWeakA_DamageCorrectRate", default=1.0,
        tooltip="TODO",
    )
    WeakBDamageMultiplier: float = ParamField(
        float32, "antiWeakB_DamageCorrectRate", default=1.0,
        tooltip="TODO",
    )
    RegainRate: float = ParamField(
        float32, "regainRate", default=1.0,
        tooltip="TODO",
    )
    ConditionHPRate: float = ParamField(
        float32, "conditionHpRate", default=-1.0,
        tooltip="TODO",
    )
    ItemDropRate: float = ParamField(
        float32, "itemDropRate", default=0.0,
        tooltip="TODO",
    )
    TransfusionHPRate: float = ParamField(
        float32, "transfusionHpRate", default=0.0,
        tooltip="TODO",
    )
    TransfusionHPPoints: int = ParamField(
        int32, "transfusionHpPoint", default=0,
        tooltip="TODO",
    )
    TransfusionHPRecoveryRate: float = ParamField(
        float32, "transfusionHpRecoverRate", default=1.0,
        tooltip="TODO",
    )
    ValidConditionStateInfo: int = ParamField(
        uint16, "validCond_StateInfo", SP_EFFECT_TYPE, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad3[2]")
