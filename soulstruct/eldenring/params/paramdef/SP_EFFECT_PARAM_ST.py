from __future__ import annotations

__all__ = ["SP_EFFECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
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
        float, "NoGuardDamageRate", default=1.0,
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
    LookAtTargetPosOffset: float = ParamField(
        float, "lookAtTargetPosOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
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
        tooltip="Multiplier applied to amount of fall damage taken by character. Cannot prevent lethal falls.",
    )
    SoulsFromKillsMultiplier: float = ParamField(
        float, "soulRate", default=0.0,
        tooltip="Multiplier applied to the amount of souls received when enemies or bosses are killed.",
    )
    MaxEquipLoadMultiplier: float = ParamField(
        float, "equipWeightChangeRate", default=0.0,
        tooltip="Multiplier applied to the character's maximum equip load.",
    )
    MaxItemLoadMultiplier: float = ParamField(
        float, "allItemWeightChangeRate", default=0.0,
        tooltip="Multiplier applied to how much the character can carry, equipped or not. Seems to have no effect in "
                "Dark Souls 1.",
    )
    SoulAmountChange: int = ParamField(
        int, "soul", default=0,
        tooltip="Amount of souls received (if positive) or taken away (if negative) every time the special effect is "
                "updated.",
    )
    AnimationIDOffset: int = ParamField(
        int, "animIdOffset", default=-1,
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
    SightSearchEnemyRate: float = ParamField(
        float, "sightSearchEnemyRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyHearingMultiplier: float = ParamField(
        float, "hearingSearchEnemyRate", default=1.0,
        tooltip="Percentage multiplier in enemy hearing range when looking for this character.",
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
    RegistDiseaseChangeRate: float = ParamField(
        float, "registDiseaseChangeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
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
        float, "soulStealRate", default=0.0,
        tooltip="Internal description says 'defense against HP when NPCs are robbed by soul steal'. Probably unused.",
    )
    EffectDurationMultiplier: float = ParamField(
        float, "lifeReductionRate", default=0.0,
        tooltip="Multiplier applied to the duration of the effect specified in EffectDurationMultiplierType. Used "
                "only by Hawkeye Gough to reduce poison and toxic duration in vanilla game.",
    )
    HPRecoveryRate: float = ParamField(
        float, "hpRecoverRate", default=0.0,
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
    MagicSubCategoryChange1: int = ParamField(
        byte, "magicSubCategoryChange1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicSubCategoryChange2: int = ParamField(
        byte, "magicSubCategoryChange2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
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
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=254,
        tooltip="Attack type attached to hits while special effect is active.",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=254,
        tooltip="Element attached to hits while special effect is active.",
    )
    SpecialState: int = ParamField(
        ushort, "stateInfo", SP_EFFECT_TYPE, default=0,
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
        ushort, "lifeReductionType", SP_EFFECT_TYPE, default=0,
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
    FreezeDamageRate: int = ParamField(
        byte, "freezeDamageRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectSelf: bool = ParamField(
        byte, "effectTargetSelf:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target self.",
    )
    CanAffectAlly: bool = ParamField(
        byte, "effectTargetFriend:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target self.",
    )
    CanAffectEnemy: bool = ParamField(
        byte, "effectTargetEnemy:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target enemies.",
    )
    CanAffectPlayer: bool = ParamField(
        byte, "effectTargetPlayer:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target player characters.",
    )
    CanAffectAI: bool = ParamField(
        byte, "effectTargetAI:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target non-player characters.",
    )
    CanAffectPlayers: bool = ParamField(
        byte, "effectTargetLive:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target humans.",
    )
    CanAffectPhantoms: bool = ParamField(
        byte, "effectTargetGhost:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target phantoms (white or black).",
    )
    DisableSleep: bool = ParamField(
        byte, "disableSleep:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMadness: bool = ParamField(
        byte, "disableMadness:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanAffectAttacker: bool = ParamField(
        byte, "effectTargetAttacker:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Effect will target character when they attack (e.g. HP drain).",
    )
    DisplayIconWhenInactive: bool = ParamField(
        byte, "dispIconNonactive:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Display icon even when special effect is inactive (not sure what that means). Never enabled.",
    )
    RegainGaugeDamage: bool = ParamField(
        byte, "regainGaugeDamage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    UseIntelligenceScaling: bool = ParamField(
        byte, "bAdjustMagicAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, special effect damage will be scaled by character intelligence (I believe).",
    )
    UseFaithScaling: bool = ParamField(
        byte, "bAdjustFaithAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, special effect damage will be scaled by character faith (I believe).",
    )
    ForNewGamePlus: bool = ParamField(
        byte, "bGameClearBonus:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, this effect will be applied multiple times depending on the NG+ cycle (I think).",
    )
    AffectsMagic: bool = ParamField(
        byte, "magParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, multipliers will be applied to magic attacks.",
    )
    AffectsMiracles: bool = ParamField(
        byte, "miracleParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, multipliers will be applied to miracle attacks.",
    )
    ClearSoul: bool = ParamField(
        byte, "clearSoul:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unused Demon's Souls remnant.",
    )
    RequestWhitePhantomSummon: bool = ParamField(
        byte, "requestSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by White Sign Soapstone.",
    )
    RequestBlackPhantomSummon: bool = ParamField(
        byte, "requestBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Red Sign Soapstone.",
    )
    RequestInvasion: bool = ParamField(
        byte, "requestForceJoinBlackSOS:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only be (Cracked) Red Eye Orb.",
    )
    RequestKick: bool = ParamField(
        byte, "requestKickSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Not used by any item. Likely kicks all clients out of your world.",
    )
    RequestReturnToOwnWorld: bool = ParamField(
        byte, "requestLeaveSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Black Separation Crystal.",
    )
    RequestNPCInvasion: bool = ParamField(
        byte, "requestNpcInveda:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Black Eye Orb (Lautrec quest and cut Shiva quest).",
    )
    Immortal: bool = ParamField(
        byte, "noDead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character cannot die. Never used in vanilla game.",
    )
    CurrentHPIgnoresMaxHPChange: bool = ParamField(
        byte, "bCurrHPIndependeMaxHP:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, changes to maximum HP will not affect current HP (unless it must be reduced to new "
                "maximum).",
    )
    IgnoreCorrosion: bool = ParamField(
        byte, "corrosionIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore corrosion damage to durability. Used only by Demon's Souls junk.",
    )
    IgnoreSightReduction: bool = ParamField(
        byte, "sightSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore any changes to their sight range from other special effects. Used "
                "only by Demon's Souls junk.",
    )
    IgnoreHearingReduction: bool = ParamField(
        byte, "hearingSearchCutIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore any changes to their hearing range from other special effects. Used "
                "only by Demon's Souls junk.",
    )
    IgnoreMagicDisabling: bool = ParamField(
        byte, "antiMagicIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, character will ignore any special effect that attempts to disable their magic. Used only by "
                "Demon's Souls junk.",
    )
    IgnoreFakeTargets: bool = ParamField(
        byte, "fakeTargetIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unknown; never used.",
    )
    IgnoreUndeadFakeTargets: bool = ParamField(
        byte, "fakeTargetIgnoreUndead:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unknown; never used.",
    )
    IgnoreBeastFakeTargets: bool = ParamField(
        byte, "fakeTargetIgnoreAnimal:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unknown; never used.",
    )
    IgnoreGravity: bool = ParamField(
        byte, "grabityIgnore:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Ignore gravity. (Not sure if this actually works.)",
    )
    PoisonImmunity: bool = ParamField(
        byte, "disablePoison:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to poison.",
    )
    ToxicImmunity: bool = ParamField(
        byte, "disableDisease:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to toxic.",
    )
    BleedImmunity: bool = ParamField(
        byte, "disableBlood:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to curse.",
    )
    CurseImmunity: bool = ParamField(
        byte, "disableCurse:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Immune to poison.",
    )
    EnableCharming: bool = ParamField(
        byte, "enableCharm:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Not sure if this refers to the Alluring Skull. May not work at all.",
    )
    EnableLifeTime: bool = ParamField(
        byte, "enableLifeTime:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Internal description: 'Is the life extended when setting a flag by TAE?'. Effect unknown. Used by "
                "Dragon Head and Torso Stones and some internal summon-related effects.",
    )
    UseStrengthScaling: bool = ParamField(
        byte, "bAdjustStrengthAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    UseDexterityScaling: bool = ParamField(
        byte, "bAdjustAgilityAblity:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EraseOnBonfireRecover: bool = ParamField(
        byte, "eraseOnBonfireRecover:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    GrabAttackParamChange: bool = ParamField(
        byte, "throwAttackParamChange:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    RequestColiseumExit: bool = ParamField(
        byte, "requestLeaveColiseumSession:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Used only by Purple Coward's Crystal.",
    )
    AffectedByEffectExtension: bool = ParamField(
        byte, "isExtendSpEffectLife:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If True, this special effect will be affected by special state (193), i.e. the effect used by the "
                "vanilla Lingering Dragoncrest Ring, that extends effect durations.",
    )
    HasTarget: bool = ParamField(
        byte, "hasTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ReplanningOnFire: bool = ParamField(
        byte, "replanningOnFire:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AffectsCharactersWithNoCovenant: bool = ParamField(
        byte, "vowType0:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters with no covenant.",
    )
    AffectsWayOfWhite: bool = ParamField(
        byte, "vowType1:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Way of White covenant.",
    )
    AffectsPrincessGuard: bool = ParamField(
        byte, "vowType2:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Princess's Guard covenant.",
    )
    AffectsWarriorOfSunlight: bool = ParamField(
        byte, "vowType3:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Warriors of Sunlight covenant.",
    )
    AffectsDarkwraith: bool = ParamField(
        byte, "vowType4:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Darkwraith covenant.",
    )
    AffectsPathOfTheDragon: bool = ParamField(
        byte, "vowType5:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Path of the Dragon covenant.",
    )
    AffectsGravelordServant: bool = ParamField(
        byte, "vowType6:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Gravelord Servant covenant.",
    )
    AffectsForestHunter: bool = ParamField(
        byte, "vowType7:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Forest Hunters covenant.",
    )
    AffectsDarkmoonBlade: bool = ParamField(
        byte, "vowType8:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Blades of the Darkmoon covenant.",
    )
    AffectsChaosServant: bool = ParamField(
        byte, "vowType9:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in the Chaos Servants covenant.",
    )
    AffectsCovenant10: bool = ParamField(
        byte, "vowType10:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant11: bool = ParamField(
        byte, "vowType11:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant12: bool = ParamField(
        byte, "vowType12:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant13: bool = ParamField(
        byte, "vowType13:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant14: bool = ParamField(
        byte, "vowType14:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    AffectsCovenant15: bool = ParamField(
        byte, "vowType15:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Determines if this special effect will affect characters in unused covenant.",
    )
    RepAtkDmgLv: int = ParamField(
        sbyte, "repAtkDmgLv", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SightSearchRate: float = ParamField(
        float, "sightSearchRate", default=1.0,
        tooltip="TODO",
    )
    EffectTargetsEnemyTarget: bool = ParamField(
        byte, "effectTargetOpposeTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EffectTargetsAllyTarget: bool = ParamField(
        byte, "effectTargetFriendlyTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    EffectTargetsSelfTarget: bool = ParamField(
        byte, "effectTargetSelfTarget:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
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
        tooltip="TODO",
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
        tooltip="TODO",
    )
    AntiDarkSightModelPoint: int = ParamField(
        int, "antiDarkSightDmypolyId", game_type=ModelDummy, default=-1,
        tooltip="TODO",
    )
    ConditionHPRate: float = ParamField(
        float, "conditionHpRate", default=-1.0,
        tooltip="TODO",
    )
    StaminaConsumptionRate: float = ParamField(
        float, "consumeStaminaRate", default=1.0,
        tooltip="TODO",
    )
    ItemDropRate: float = ParamField(
        float, "itemDropRate", default=0.0,
        tooltip="TODO",
    )
    ChangePoisonResistance: int = ParamField(
        int, "changePoisonResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeToxicResistance: int = ParamField(
        int, "changeDiseaseResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeBleedingResistance: int = ParamField(
        int, "changeBloodResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeFrenzyResistance: int = ParamField(
        int, "changeCurseResistPoint", default=0,
        tooltip="TODO",
    )
    ChangeFreezeResistPoint: int = ParamField(
        int, "changeFreezeResistPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackRate: float = ParamField(
        float, "slashAttackRate", default=1.0,
        tooltip="TODO",
    )
    BluntAttackRate: float = ParamField(
        float, "blowAttackRate", default=1.0,
        tooltip="TODO",
    )
    ThrustAttackRate: float = ParamField(
        float, "thrustAttackRate", default=1.0,
        tooltip="TODO",
    )
    NeutralAttackRate: float = ParamField(
        float, "neutralAttackRate", default=1.0,
        tooltip="TODO",
    )
    SlashAttackPowerRate: float = ParamField(
        float, "slashAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    BluntAttackPowerRate: float = ParamField(
        float, "blowAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    ThrustAttackPowerRate: float = ParamField(
        float, "thrustAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    NeutralAttackPowerRate: float = ParamField(
        float, "neutralAttackPowerRate", default=1.0,
        tooltip="TODO",
    )
    SlashAttackPower: int = ParamField(
        int, "slashAttackPower", default=0,
        tooltip="TODO",
    )
    BluntAttackPower: int = ParamField(
        int, "blowAttackPower", default=0,
        tooltip="TODO",
    )
    ThrustAttackPower: int = ParamField(
        int, "thrustAttackPower", default=0,
        tooltip="TODO",
    )
    NeutralAttackPower: int = ParamField(
        int, "neutralAttackPower", default=0,
        tooltip="TODO",
    )
    ChangeStrength: int = ParamField(
        int, "changeStrengthPoint", default=0,
        tooltip="TODO",
    )
    ChangeDexterity: int = ParamField(
        int, "changeAgilityPoint", default=0,
        tooltip="TODO",
    )
    ChangeBloodtinge: int = ParamField(
        int, "changeMagicPoint", default=0,
        tooltip="TODO",
    )
    ChangeArcane: int = ParamField(
        int, "changeFaithPoint", default=0,
        tooltip="TODO",
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
    AddBehaviorJudgeIDAdd: int = ParamField(
        ushort, "addBehaviorJudgeId_add", default=0,
        tooltip="Always zero. Unknown effect. Internal description suggests that this is a constant added to all "
                "behavior judge IDs (from TAE) issued by character.",
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
        tooltip="TODO",
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
        tooltip="TODO",
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
    PoiseAddition: float = ParamField(
        float, "changeSuperArmorPoint", default=0.0,
        tooltip="Amount added (if positive) or subtracted (if negative) from character's poise.",
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
    Pad3: float = ParamField(
        float, "unk2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "unk3[4]")
