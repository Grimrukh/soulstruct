from __future__ import annotations

__all__ = ["SP_EFFECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SP_EFFECT_PARAM_ST(ParamRow):
    StatusIcon: int = ParamField(
        int, "iconId", game_type=Icon, default=-1,
        tooltip="Icon that appears in HUD under stamina bar while special effect is active. Set to -1 for no icon.",
    )
    MaxHPPercentageForEffect: float = ParamField(
        float, "conditionHp", default=-1.0,
        tooltip="Special effect will only take effect if character's current HP is less than or equal to this "
                "percentage (from 0 to 100). Set to -1 for no HP condition.",
    )
    EffectDuration: float = ParamField(
        float, "effectEndurance", default=0.0,
        tooltip="Duration of special effect. Set to 0 for an effect that occurs for only one frame (e.g. to award "
                "souls) or to -1 for an effect that will last until specifically removed or its source is lost (e.g. "
                "rings).",
    )
    UpdateInterval: float = ParamField(
        float, "motionInterval", default=0.0,
        tooltip="Time (in seconds) between applications of the special effect, while active. Set to higher values to "
                "have the effect apply less frequently. Set to 0 to have it occur every frame.",
    )
    MaxHPMultiplier: float = ParamField(
        float, "maxHpRate", default=1.0,
        tooltip="Multiplier applied to maximum HP.",
    )
    MaxMPMultiplier: float = ParamField(
        float, "maxMpRate", default=1.0,
        tooltip="Multiplier applied to maximum MP. (Unused in Dark Souls; does NOT refer to spell usages.)",
    )
    MaxStaminaMultiplier: float = ParamField(
        float, "maxStaminaRate", default=1.0,
        tooltip="Multiplier applied to maximum stamina.",
    )
    IncomingSlashDamageMultiplier: float = ParamField(
        float, "slashDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming slashing physical damage.",
    )
    IncomingStrikeDamageMultiplier: float = ParamField(
        float, "blowDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming striking physical damage.",
    )
    IncomingThrustDamageMultiplier: float = ParamField(
        float, "thrustDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming thrusting physical damage.",
    )
    IncomingNeutralDamageMultiplier: float = ParamField(
        float, "neutralDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming neutral physical damage.",
    )
    IncomingMagicDamageMultiplier: float = ParamField(
        float, "magicDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming magic damage.",
    )
    IncomingFireDamageMultiplier: float = ParamField(
        float, "fireDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming fire damage.",
    )
    IncomingLightningDamageMultiplier: float = ParamField(
        float, "thunderDamageCutRate", default=1.0,
        tooltip="Multiplier applied to incoming lightning damage.",
    )
    OutgoingPhysicalDamageMultiplier: float = ParamField(
        float, "physicsAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing physical damage (of any type).",
    )
    OutgoingMagicDamageMultiplier: float = ParamField(
        float, "magicAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing magic damage.",
    )
    OutgoingFireDamageMultiplier: float = ParamField(
        float, "fireAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing fire damage.",
    )
    OutgoingLightningDamageMultiplier: float = ParamField(
        float, "thunderAttackRate", default=1.0,
        tooltip="Multiplier applied to outgoing lightning damage.",
    )
    PhysicalAttackPowerMultiplier: float = ParamField(
        float, "physicsAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's physical attack power (of any type).",
    )
    MagicAttackPowerMultiplier: float = ParamField(
        float, "magicAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's magic attack power.",
    )
    FireAttackPowerMultiplier: float = ParamField(
        float, "fireAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's fire attack power.",
    )
    LightningAttackPowerMultiplier: float = ParamField(
        float, "thunderAttackPowerRate", default=1.0,
        tooltip="Multiplier applied to character's lightning attack power.",
    )
    PhysicalAttackPowerAddition: int = ParamField(
        int, "physicsAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's physical attack power (of any type).",
    )
    MagicAttackPowerAddition: int = ParamField(
        int, "magicAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's magic attack power.",
    )
    FireAttackPowerAddition: int = ParamField(
        int, "fireAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's fire attack power.",
    )
    LightningAttackPowerAddition: int = ParamField(
        int, "thunderAttackPower", default=0,
        tooltip="Value to add to or subtract fromcharacter's lightning attack power.",
    )
    PhysicalDefenseMultiplier: float = ParamField(
        float, "physicsDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's physical defense (all types).",
    )
    MagicDefenseMultiplier: float = ParamField(
        float, "magicDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's magic defense.",
    )
    FireDefenseMultiplier: float = ParamField(
        float, "fireDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's fire defense.",
    )
    LightningDefenseMultiplier: float = ParamField(
        float, "thunderDiffenceRate", default=1.0,
        tooltip="Multiplier applied to character's lightning defense.",
    )
    PhysicalDefenseAddition: int = ParamField(
        int, "physicsDiffence", default=0,
        tooltip="Value to add to or subtract from character's physical defense.",
    )
    MagicDefenseAddition: int = ParamField(
        int, "magicDiffence", default=0,
        tooltip="Value to add to or subtract from character's magic defense.",
    )
    FireDefenseAddition: int = ParamField(
        int, "fireDiffence", default=0,
        tooltip="Value to add to or subtract from character's fire defense.",
    )
    LightningDefenseAddition: int = ParamField(
        int, "thunderDiffence", default=0,
        tooltip="Value to add to or subtract from character's lightning defense.",
    )
    NoGuardIncomingDamageMultiplier: float = ParamField(
        float, "NoGuardDamageRate", default=0.0,
        tooltip="Multiplier to use instead of usual multiplier if character is not guarding. (Always set to 0 in "
                "vanilla game, which must deactivate it. Only an educated guess that it refers to incoming damage, "
                "not outgoing.)",
    )
    CriticalHitIncomingDamageMultiplier: float = ParamField(
        float, "vitalSpotChangeRate", default=-1.0,
        tooltip="Multiplier to use instead of usual multiplier if character is hit in a weak spot. (Always set to -1 "
                "in vanilla game, which deactivates it. Only an educated guess that it affects incoming damage.)",
    )
    NonCriticalHitIncomingDamageMultiplier: float = ParamField(
        float, "normalSpotChangeRate", default=-1.0,
        tooltip="Multiplier to use instead of usual multiplier if character is *not* hit in a weak spot. (Always set "
                "to -1 in vanilla game, which deactivates it. Only an educated guess that it affects incoming "
                "damage.)",
    )
    MaxHPChangeRatio: float = ParamField(
        float, "maxHpChangeRate", default=0.0,
        tooltip="Appears to be an unused variant of MaxHPMultiplier. Always set to 0.",
    )
    BehaviorToTrigger: int = ParamField(
        int, "behaviorId", game_type=BehaviorParam, default=-1,
        tooltip="Behavior ID to trigger (which can in turn trigger an Attack or Bullet) whenever special effect is "
                "applied. Set to -1 to use no behavior.",
    )
    HPReductionPercentage: float = ParamField(
        float, "changeHpRate", default=0.0,
        tooltip="Percentage reduction of maximum HP (from 0 to 100). Negative values (to -100) will restore that "
                "percentage instead. Applied every time the special effect updates.",
    )
    HPPointsLost: int = ParamField(
        int, "changeHpPoint", default=0,
        tooltip="HP value to subtract (if positive) or add (if negative) to character's current HP on every update of "
                "the special effect.",
    )
    MPReductionPercentage: float = ParamField(
        float, "changeMpRate", default=0.0,
        tooltip="Percentage reduction of maximum MP (from 0 to 100). Negative values (to -100) will restore that "
                "percentage instead. Applied every time the special effect updates. (Unused in Dark Souls 1.)",
    )
    MPPointsLost: int = ParamField(
        int, "changeMpPoint", default=0,
        tooltip="MP value to subtract (if positive) or add (if negative) to character's current MP on every update of "
                "the special effect. (Unused in Dark Souls 1.)",
    )
    MPRecoverySpeedChange: int = ParamField(
        int, "mpRecoverChangeSpeed", default=0,
        tooltip="Points added to or subtracted from MP recovery formula. (Unused in Dark Souls 1.)",
    )
    StaminaReductionPercentage: float = ParamField(
        float, "changeStaminaRate", default=0.0,
        tooltip="Percentage reduction of maximum stamina (from 0 to 100). Negative values (to -100) will restore that "
                "percentage instead. Applied every time the special effect updates.",
    )
    StaminaPointsLost: int = ParamField(
        int, "changeStaminaPoint", default=0,
        tooltip="Stamina value to subtract (if positive) or add (if negative) to character's current stamina on every "
                "update of the special effect.",
    )
    StaminaRecoverySpeedChange: int = ParamField(
        int, "staminaRecoverChangeSpeed", default=0,
        tooltip="Points added to or subtracted from stamina recovery formula. I believe this affects the amount of "
                "stamina restored every second. (For reference, a Green Blossom adds 40 points.)",
    )
    MagicEffectTimeChange: float = ParamField(
        float, "magicEffectTimeChange", default=0.0,
        tooltip="Name suggests this changes the duration of magic effects, but it is never used (always zero).",
    )
    CurrentDurabilityAddition: int = ParamField(
        int, "insideDurability", default=0,
        tooltip="Amount of durability to subtract (if positive) or add (if negative) to current durability on every "
                "update of the special effect. The equipment affected is determined by...",
    )
    MaxDurabilityAddition: int = ParamField(
        int, "maxDurability", default=0,
        tooltip="Amount of durability to subtract (if positive) or add (if negative) to the character's maximum "
                "durability while the special effect is active. The equipment affected is determined by...",
    )
    OutgoingStaminaDamageMultiplier: float = ParamField(
        float, "staminaAttackRate", default=1.0,
        tooltip="Multiplier applied to the amount of damage dealt to targets' stamina.",
    )
    PoisonDamage: int = ParamField(
        int, "poizonAttackPower", default=0,
        tooltip="Amount of poison damage (in units of resistance) added to the character on every update. Negative "
                "values will heal poison damage instead (e.g. Purple Moss Clump). Unclear how this distinguishes "
                "between reducing build-up and actually healing the status.",
    )
    ToxicDamage: int = ParamField(
        int, "registIllness", default=0,
        tooltip="Amount of toxic damage (in units of resistance) added to the character on every update. Negative "
                "values will heal toxic damage instead (e.g. Blooming Purple Moss Clump). Unclear how this "
                "distinguishes between reducing build-up and actually healing the status.",
    )
    BleedDamage: int = ParamField(
        int, "registBlood", default=0,
        tooltip="Amount of bleed damage (in units of resistance) added to the character on every update. Negative "
                "values will heal bleed damage instead (e.g. Blood-Red Moss Clump). Unclear how this distinguishes "
                "between reducing build-up and actually healing the status.",
    )
    CurseDamage: int = ParamField(
        int, "registCurse", default=0,
        tooltip="Amount of curse damage (in units of resistance) added to the character on every update. Negative "
                "values will heal curse damage instead (e.g. Purging Stone). Unclear how this distinguishes between "
                "reducing build-up and actually healing the status.",
    )
    FallDamageMultiplier: float = ParamField(
        float, "fallDamageRate", default=1.0,
        tooltip="Multiplier applied to amount of fall damage taken by character. Cannot prevent lethal falls.",
    )
    SoulsFromKillsMultiplier: float = ParamField(
        float, "soulRate", default=1.0,
        tooltip="Multiplier applied to the amount of souls received when enemies or bosses are killed.",
    )
    MaxEquipLoadMultiplier: float = ParamField(
        float, "equipWeightChangeRate", default=1.0,
        tooltip="Multiplier applied to the character's maximum equip load.",
    )
    MaxItemLoadMultiplier: float = ParamField(
        float, "allItemWeightChangeRate", default=1.0,
        tooltip="Multiplier applied to how much the character can carry, equipped or not. Seems to have no effect in "
                "Dark Souls 1.",
    )
    SoulAmountChange: int = ParamField(
        int, "soul", default=0,
        tooltip="Amount of souls received (if positive) or taken away (if negative) every time the special effect is "
                "updated.",
    )
    AnimationIDOffset: int = ParamField(
        int, "animIdOffset", default=0,
        tooltip="Override default animation ID offset of character, which can change their animation set temporarily.",
    )
    SoulRewardMultiplier: float = ParamField(
        float, "haveSoulRate", default=1.0,
        tooltip="Multiplier applied to the amount of souls given to the player when they kill this character (e.g. "
                "enemies in NG+).",
    )
    TargetPriorityChange: float = ParamField(
        float, "targetPriority", default=0.0,
        tooltip="Value added to or subtract from this character's priority in the target queue. Higher priority means "
                "they are more likely to be targeted by enemies.",
    )
    EnemySightPercentageReduction: int = ParamField(
        int, "sightSearchEnemyCut", default=0,
        tooltip="Percentage reduction in enemy sight (from 0 to 100) when looking for this character. Not sure if "
                "negative values can be used to make this character *more* visible.",
    )
    EnemyHearingPercentageReduction: int = ParamField(
        int, "hearingSearchEnemyCut", default=0,
        tooltip="Percentage reduction in enemy hearing (from 0 to 100) when looking for this character. Not sure if "
                "negative values can be used to make this character *more* audible.",
    )
    AnimationSpeedMultiplier: float = ParamField(
        float, "grabityRate", default=1.0,
        tooltip="Multiplier applied to all of this character's animations. Values other than 1 can lead to cool but "
                "potentially glitchy behavior (e.g. desynchronized grab animations and missed collision).",
    )
    PoisonResistanceMultiplier: float = ParamField(
        float, "registPoizonChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum poison resistance.",
    )
    ToxicResistanceMultiplier: float = ParamField(
        float, "registIllnessChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum toxic resistance.",
    )
    BleedResistanceMultiplier: float = ParamField(
        float, "registBloodChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum bleed resistance.",
    )
    CurseResistanceMultiplier: float = ParamField(
        float, "registCurseChangeRate", default=1.0,
        tooltip="Multiplier applied to character's maximum curse resistance.",
    )
    SoulStealMultiplier: float = ParamField(
        float, "soulStealRate", default=1.0,
        tooltip="Internal description says 'defense against HP when NPCs are robbed by soul steal'. Probably unused.",
    )
    EffectDurationMultiplier: float = ParamField(
        float, "lifeReductionRate", default=1.0,
        tooltip="Multiplier applied to the duration of the effect specified in EffectDurationMultiplierType. Used "
                "only by Hawkeye Gough to reduce poison and toxic duration in vanilla game.",
    )
    HPRecoveryRate: float = ParamField(
        float, "hpRecoverRate", default=1.0,
        tooltip="Multiplier applied to any increase in character's current HP.",
    )
    NextSpecialEffect: int = ParamField(
        int, "replaceSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect to apply to character automatically when this special effect ends (if not terminated "
                "manually by an event).",
    )
    SpecialEffectPerUpdate: int = ParamField(
        int, "cycleOccurrenceSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect to apply to character every time this special effect updates (e.g. Symbol of Avarice "
                "HP reduction).",
    )
    SpecialEffectOnAttack: int = ParamField(
        int, "atkOccurrenceSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect to apply to any target hit by an attack.  WARNING: This will not trigger unless "
                "SpecialStateIndex is set to 152 (Rotten Pine Resin effect), which will in turn cause your weapon to "
                "glow purple unless the visual effect is disabled.",
    )
    GuardDefenseFlickPowerRate: float = ParamField(
        float, "guardDefFlickPowerRate", default=1.0,
        tooltip="Unknown; never used.",
    )
    GuardStaminaMultiplier: float = ParamField(
        float, "guardStaminaCutRate", default=1.0,
        tooltip="Values larger than 1 mean *less* stamina is used when blocking.",
    )
    RayCastPassingTime: int = ParamField(
        short, "rayCastPassedTime", default=-1,
        tooltip="Internal description says 'Gaze passing: activation time (milliseconds).' Likely unused.",
    )
    PoiseAddition: int = ParamField(
        short, "changeSuperArmorPoint", default=0,
        tooltip="Amount added (if positive) or subtracted (if negative) from character's poise.",
    )
    BowRangePercentageChange: int = ParamField(
        short, "bowDistRate", default=0,
        tooltip="Percentage change (from 0 to 100) in bow range. Requires SpecialStateIndex BowBoostRange (168) to "
                "work.",
    )
    SpecialEffectCategory: int = ParamField(
        ushort, "spCategory", SP_EFFECT_SPCATEGORY, default=0,
        tooltip="Category of special effect. This effect will override (i.e. cancel out) all other active effects "
                "with the same category when it is added.",
    )
    SpecialEffectPriority: int = ParamField(
        byte, "categoryPriority", default=0,
        tooltip="Priority ordering for special effect to be applied on each update (lower values are updated first).",
    )
    SaveCategory: int = ParamField(
        sbyte, "saveCategory", SP_EFFECT_SAVE_CATEGORY, default=-1,
        tooltip="Determines automatic game saving behavior (used for status ailments only). Set to -1 for no saving.",
    )
    AttunementSlotCountChange: int = ParamField(
        byte, "changeMagicSlot", default=0,
        tooltip="Increase (positive) or decrease (negative) number of attunement slots available.",
    )
    AttunementMiracleSlotCountChange: int = ParamField(
        byte, "changeMiracleSlot", default=0,
        tooltip="Miracle slots are not even separate from other magic slots, so this is likely an abandoned field.",
    )
    HumanityDamage: int = ParamField(
        sbyte, "heroPointDamage", default=0,
        tooltip="Damage applied to soft humanity count. Negative values will add soft humanity.",
    )
    RiposteDefenseAddition: int = ParamField(
        byte, "defFlickPower", default=0,
        tooltip="Value added to or subtracted from defense against riposte attacks.",
    )
    FlickDamageMultiplier: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="Multiplier to use instead of usual multiplier on incoming (I assume) riposte attacks. Never used.",
    )
    IncomingBleedDamagePercentage: int = ParamField(
        byte, "bloodDamageRate", default=100,
        tooltip="Percentage of incoming bleed damage received (usually 100).",
    )
    ReplaceNoImpactLevel: int = ParamField(
        sbyte, "dmgLv_None", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of NoImpact level.",
    )
    ReplaceSmallImpactLevel: int = ParamField(
        sbyte, "dmgLv_S", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Small impact level.",
    )
    ReplaceMediumImpactLevel: int = ParamField(
        sbyte, "dmgLv_M", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Medium impact level.",
    )
    ReplaceLargeImpactLevel: int = ParamField(
        sbyte, "dmgLv_L", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Large impact level.",
    )
    ReplaceBlowoffImpactLevel: int = ParamField(
        sbyte, "dmgLv_BlowM", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Blowoff impact level.",
    )
    ReplacePushImpactLevel: int = ParamField(
        sbyte, "dmgLv_Push", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Push impact level.",
    )
    ReplaceStrikeImpactLevel: int = ParamField(
        sbyte, "dmgLv_Strike", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Strike impact level.",
    )
    ReplaceSmallBlowImpactLevel: int = ParamField(
        sbyte, "dmgLv_BlowS", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Blow impact level.",
    )
    ReplaceMinimalImpactLevel: int = ParamField(
        sbyte, "dmgLv_Min", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Minimal impact level.",
    )
    ReplaceLaunchImpactLevel: int = ParamField(
        sbyte, "dmgLv_Uppercut", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of Launch impact level.",
    )
    ReplaceBlowBackwardImpactLevel: int = ParamField(
        sbyte, "dmgLv_BlowLL", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of BlowBackward impact level.",
    )
    ReplaceBreathBurnImpactLevel: int = ParamField(
        sbyte, "dmgLv_Breath", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="Impact level that will occur instead of BreathBurn impact level.",
    )
    AttackAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="Attack type attached to hits while special effect is active.",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="Element attached to hits while special effect is active.",
    )
    SpecialState: int = ParamField(
        byte, "stateInfo", SP_EFFECT_TYPE, default=0,
        tooltip="Hard-coded special state to use. Also determines visual effect from Special Effect Visuals table.",
    )
    AffectedWeaponType: int = ParamField(
        byte, "wepParamChange", SP_EFE_WEP_CHANGE_PARAM, default=0,
        tooltip="Weapon category that is affected by special effect. ",
    )
    MovementType: int = ParamField(
        byte, "moveType", SP_EFFECT_MOVE_TYPE, default=0,
        tooltip="Determines how movement is affected. (Does not correspond to Movement param entries.)",
    )
    EffectDurationMultiplierType: int = ParamField(
        byte, "lifeReductionType", SP_EFFECT_TYPE, default=0,
        tooltip="Type of effect whose duration is affected by EffectDurationMultiplier. Known values: 2 = poison, 5 = "
                "toxic.",
    )
    ThrowCondition: int = ParamField(
        byte, "throwCondition", SP_EFFECT_THROW_CONDITION_TYPE, default=0,
        tooltip="Determines how throws are affected while special effect is active. Values still unknown (rarely "
                "used).",
    )
    AddBehaviorJudgeIDCondition: int = ParamField(
        sbyte, "addBehaviorJudgeId_condition", default=-1,
        tooltip="Unclear; used only to manage the Hydra as more heads are cut off. All other values are -1.",
    )
    AddBehaviorJudgeIDAdd: int = ParamField(
        byte, "addBehaviorJudgeId_add", default=0,
        tooltip="Always zero. Unknown effect. Internal description suggests that this is a constant added to all "
                "behavior judge IDs (from TAE) issued by character.",
    )
    CanAffectSelf: bool = ParamField(
        byte, "effectTargetSelf:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target self.",
    )
    CanAffectAlly: bool = ParamField(
        byte, "effectTargetFriend:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target self.",
    )
    CanAffectEnemy: bool = ParamField(
        byte, "effectTargetEnemy:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target enemies.",
    )
    CanAffectPlayer: bool = ParamField(
        byte, "effectTargetPlayer:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target player characters.",
    )
    CanAffectAI: bool = ParamField(
        byte, "effectTargetAI:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target non-player characters.",
    )
    CanAffectPlayers: bool = ParamField(
        byte, "effectTargetLive:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target humans.",
    )
    CanAffectPhantoms: bool = ParamField(
        byte, "effectTargetGhost:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target phantoms (white or black).",
    )
    CanAffectWhitePhantoms: bool = ParamField(
        byte, "effectTargetWhiteGhost:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target white phantoms.",
    )
    CanAffectBlackPhantoms: bool = ParamField(
        byte, "effectTargetBlackGhost:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target white phantoms.",
    )
    CanAffectAttacker: bool = ParamField(
        byte, "effectTargetAttacker:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Effect will target character when they attack (e.g. HP drain).",
    )
    DisplayIconWhenInactive: bool = ParamField(
        byte, "dispIconNonactive:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Display icon even when special effect is inactive (not sure what that means). Never enabled.",
    )
    UseVisualEffect: bool = ParamField(
        byte, "useSpEffectEffect:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Use visual effect from Special Effect Visuals table (indexed by Special State field).",
    )
    UseIntelligenceScaling: bool = ParamField(
        byte, "bAdjustMagicAblity:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, special effect damage will be scaled by character intelligence (I believe).",
    )
    UseFaithScaling: bool = ParamField(
        byte, "bAdjustFaithAblity:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, special effect damage will be scaled by character faith (I believe).",
    )
    ForNewGamePlus: bool = ParamField(
        byte, "bGameClearBonus:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, this effect will be applied multiple times depending on the NG+ cycle (I think).",
    )
    AffectsMagic: bool = ParamField(
        byte, "magParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, multipliers will be applied to magic attacks.",
    )
    AffectsMiracles: bool = ParamField(
        byte, "miracleParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, multipliers will be applied to miracle attacks.",
    )
    ClearSoul: bool = ParamField(
        byte, "clearSoul:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Unused Demon's Souls remnant.",
    )
    RequestWhitePhantomSummon: bool = ParamField(
        byte, "requestSOS:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Used only by White Sign Soapstone.",
    )
    RequestBlackPhantomSummon: bool = ParamField(
        byte, "requestBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Used only by Red Sign Soapstone.",
    )
    RequestInvasion: bool = ParamField(
        byte, "requestForceJoinBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Used only be (Cracked) Red Eye Orb.",
    )
    RequestKick: bool = ParamField(
        byte, "requestKickSession:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Not used by any item. Likely kicks all clients out of your world.",
    )
    RequestReturnToOwnWorld: bool = ParamField(
        byte, "requestLeaveSession:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Used only by Black Separation Crystal.",
    )
    RequestNPCInvasion: bool = ParamField(
        byte, "requestNpcInveda:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Used only by Black Eye Orb (Lautrec quest and cut Shiva quest).",
    )
    Immortal: bool = ParamField(
        byte, "noDead:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, character cannot die. Never used in vanilla game.",
    )
    CurrentHPIgnoresMaxHPChange: bool = ParamField(
        byte, "bCurrHPIndependeMaxHP:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, changes to maximum HP will not affect current HP (unless it must be reduced to new "
                "maximum).",
    )
    IgnoreCorrosion: bool = ParamField(
        byte, "corrosionIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, character will ignore corrosion damage to durability. Used only by Demon's Souls junk.",
    )
    IgnoreSightReduction: bool = ParamField(
        byte, "sightSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, character will ignore any changes to their sight range from other special effects. Used "
                "only by Demon's Souls junk.",
    )
    IgnoreHearingReduction: bool = ParamField(
        byte, "hearingSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, character will ignore any changes to their hearing range from other special effects. Used "
                "only by Demon's Souls junk.",
    )
    IgnoreMagicDisabling: bool = ParamField(
        byte, "antiMagicIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, character will ignore any special effect that attempts to disable their magic. Used only by "
                "Demon's Souls junk.",
    )
    IgnoreFakeTargets: bool = ParamField(
        byte, "fakeTargetIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Unknown; never used.",
    )
    IgnoreUndeadFakeTargets: bool = ParamField(
        byte, "fakeTargetIgnoreUndead:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Unknown; never used.",
    )
    IgnoreBeastFakeTargets: bool = ParamField(
        byte, "fakeTargetIgnoreAnimal:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Unknown; never used.",
    )
    IgnoreGravity: bool = ParamField(
        byte, "grabityIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Ignore gravity. (Not sure if this actually works.)",
    )
    PoisonImmunity: bool = ParamField(
        byte, "disablePoison:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Immune to poison.",
    )
    ToxicImmunity: bool = ParamField(
        byte, "disableDisease:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Immune to toxic.",
    )
    BleedImmunity: bool = ParamField(
        byte, "disableBlood:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Immune to curse.",
    )
    CurseImmunity: bool = ParamField(
        byte, "disableCurse:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Immune to poison.",
    )
    EnableCharming: bool = ParamField(
        byte, "enableCharm:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Not sure if this refers to the Alluring Skull. May not work at all.",
    )
    EnableLifeTime: bool = ParamField(
        byte, "enableLifeTime:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Internal description: 'Is the life extended when setting a flag by TAE?'. Effect unknown. Used by "
                "Dragon Head and Torso Stones and some internal summon-related effects.",
    )
    HasTarget: bool = ParamField(
        byte, "hasTarget : 1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="For unused 'evil eye' mechanics, probably a Demon's Souls remnant.",
    )
    FireImmunity: bool = ParamField(
        byte, "isFireDamageCancel:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Immune to fire damage. Never enabled, and may not actually work. Needs testing.",
    )
    AffectedByEffectExtension: bool = ParamField(
        byte, "isExtendSpEffectLife:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="If True, this special effect will be affected by special state (193), i.e. the effect used by the "
                "vanilla Lingering Dragoncrest Ring, that extends effect durations.",
    )
    RequestColiseumExit: bool = ParamField(
        byte, "requestLeaveColiseumSession:1", SP_EFFECT_BOOL, bit_count=1, default=0,
        tooltip="Used only by Purple Coward's Crystal.",
    )
    _BitPad0: int = ParamBitPad(byte, "pad_2:4", bit_count=4)
    AffectsCharactersWithNoCovenant: bool = ParamField(
        byte, "vowType0:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters with no covenant.",
    )
    AffectsWayOfWhite: bool = ParamField(
        byte, "vowType1:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Way of White covenant.",
    )
    AffectsPrincessGuard: bool = ParamField(
        byte, "vowType2:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Princess's Guard covenant.",
    )
    AffectsWarriorOfSunlight: bool = ParamField(
        byte, "vowType3:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Warriors of Sunlight covenant.",
    )
    AffectsDarkwraith: bool = ParamField(
        byte, "vowType4:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Darkwraith covenant.",
    )
    AffectsPathOfTheDragon: bool = ParamField(
        byte, "vowType5:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Path of the Dragon covenant.",
    )
    AffectsGravelordServant: bool = ParamField(
        byte, "vowType6:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Gravelord Servant covenant.",
    )
    AffectsForestHunter: bool = ParamField(
        byte, "vowType7:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Forest Hunters covenant.",
    )
    AffectsDarkmoonBlade: bool = ParamField(
        byte, "vowType8:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Blades of the Darkmoon covenant.",
    )
    AffectsChaosServant: bool = ParamField(
        byte, "vowType9:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in the Chaos Servants covenant.",
    )
    AffectsCovenant10: bool = ParamField(
        byte, "vowType10:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant11: bool = ParamField(
        byte, "vowType11:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant12: bool = ParamField(
        byte, "vowType12:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant13: bool = ParamField(
        byte, "vowType13:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant14: bool = ParamField(
        byte, "vowType14:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant15: bool = ParamField(
        byte, "vowType15:1", SP_EFFECT_BOOL, bit_count=1, default=True,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    _Pad0: bytes = ParamPad(11, "pad1[11]")
