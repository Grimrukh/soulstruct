from __future__ import annotations

__all__ = ["ATK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ATK_PARAM_ST(ParamRow):
    Hitbox0Radius: float = ParamField(
        float, "hit0_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 0).",
    )
    Hitbox1Radius: float = ParamField(
        float, "hit1_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 1).",
    )
    Hitbox2Radius: float = ParamField(
        float, "hit2_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 2).",
    )
    Hitbox3Radius: float = ParamField(
        float, "hit3_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 3).",
    )
    KnockbackDistance: float = ParamField(
        float, "knockbackDist", default=0.0,
        tooltip="Knockback distance of attack.",
    )
    HitStopTime: float = ParamField(
        float, "hitStopTime", default=0.0,
        tooltip="Unclear. This isn't hitbox duration, which is determined by the duration of the triggering TAE "
                "event. It may be the duration of the 'hit' flag on the target. Always set to 0, 0.08. or 0.11.",
    )
    SpecialEffectOnHit0: SpecialEffectParam = ParamField(
        int, "spEffectId0", default=0,
        tooltip="Special effect applied to target on hit (slot 0).",
    )
    SpecialEffectOnHit1: SpecialEffectParam = ParamField(
        int, "spEffectId1", default=0,
        tooltip="Special effect applied to target on hit (slot 1).",
    )
    SpecialEffectOnHit2: SpecialEffectParam = ParamField(
        int, "spEffectId2", default=0,
        tooltip="Special effect applied to target on hit (slot 2).",
    )
    SpecialEffectOnHit3: SpecialEffectParam = ParamField(
        int, "spEffectId3", default=0,
        tooltip="Special effect applied to target on hit (slot 3).",
    )
    SpecialEffectOnHit4: SpecialEffectParam = ParamField(
        int, "spEffectId4", default=0,
        tooltip="Special effect applied to target on hit (slot 4).",
    )
    Hitbox0StartModelPoint: int = ParamField(
        short, "hit0_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 0). If Hitbox0EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox1StartModelPoint: int = ParamField(
        short, "hit1_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 1). If Hitbox1EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox2StartModelPoint: int = ParamField(
        short, "hit2_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 2). If Hitbox2EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox3StartModelPoint: int = ParamField(
        short, "hit3_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 3). If Hitbox3EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox0EndModelPoint: int = ParamField(
        short, "hit0_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 0). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox0StartModelPoint.",
    )
    Hitbox1EndModelPoint: int = ParamField(
        short, "hit1_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 1). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox1StartModelPoint.",
    )
    Hitbox2EndModelPoint: int = ParamField(
        short, "hit2_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 2). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox2StartModelPoint.",
    )
    Hitbox3EndModelPoint: int = ParamField(
        short, "hit3_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 3). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox3StartModelPoint.",
    )
    BlowOffCorrection: int = ParamField(
        ushort, "blowingCorrection", default=0, hide=True,
        tooltip="Unknown. Never used.",
    )
    PhysicalAttackPowerPercentage: int = ParamField(
        ushort, "atkPhysCorrection", default=100,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate physical "
                "attack damage.",
    )
    MagicAttackPowerPercentage: int = ParamField(
        ushort, "atkMagCorrection", default=100,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate magic "
                "attack damage.",
    )
    FireAttackPowerPercentage: int = ParamField(
        ushort, "atkFireCorrection", default=100,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate fire attack "
                "damage.",
    )
    LightningAttackPowerPercentage: int = ParamField(
        ushort, "atkThunCorrection", default=100,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate lightning "
                "attack damage.",
    )
    StaminaAttackPowerPercentage: int = ParamField(
        ushort, "atkStamCorrection", default=100,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate stamina "
                "damage.",
    )
    GuardAttackPercentage: int = ParamField(
        ushort, "guardAtkRateCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character guard attack power. Throw attacks "
                "have a value of 9900, which must essentially ignore blocking completely.",
    )
    GuardBreakPercentage: int = ParamField(
        ushort, "guardBreakCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character guard breaking power. Not sure what "
                "that is, exactly, but this is set to 0 for parries and 100 for all other attacks.",
    )
    AttackDuringThrowPercentage: int = ParamField(
        ushort, "atkThrowEscapeCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to weapon attacks during throws. Generally set to "
                "100, except for throw attacks themselves.",
    )
    PoiseAttackPercentage: int = ParamField(
        ushort, "atkSuperArmorCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to damage to target poise. Generally set to 100, "
                "except for throw attacks themselves.",
    )
    PhysicalAttackPower: int = ParamField(
        ushort, "atkPhys", default=0,
        tooltip="Absolute physical attack power of attack.",
    )
    MagicAttackPower: int = ParamField(
        ushort, "atkMag", default=0,
        tooltip="Absolute magic attack power of attack.",
    )
    FireAttackPower: int = ParamField(
        ushort, "atkFire", default=0,
        tooltip="Absolute fire attack power of attack.",
    )
    LightningAttackPower: int = ParamField(
        ushort, "atkThun", default=0,
        tooltip="Absolute lightning attack power of attack.",
    )
    StaminaAttackPower: int = ParamField(
        ushort, "atkStam", default=0,
        tooltip="Absolute stamina attack power of attack.",
    )
    GuardAttackPower: int = ParamField(
        ushort, "guardAtkRate", default=100,
        tooltip="Absolute guard attack power of attack.",
    )
    GuardBreakPower: int = ParamField(
        ushort, "guardBreakRate", default=0,
        tooltip="Absolute guard breaking power of attack.",
    )
    PoiseAttackPower: int = ParamField(
        ushort, "atkSuperArmor", default=0,
        tooltip="Absolute poise attack power of attack.",
    )
    AttackPowerDuringThrows: int = ParamField(
        ushort, "atkThrowEscape", default=0, hide=True,
        tooltip="Absolute attack power of attack. Never used.",
    )
    ObjectDamage: int = ParamField(
        ushort, "atkObj", default=0,
        tooltip="Amount of damage dealt to objects by this attack.",
    )
    GuardStaminaPercentage: int = ParamField(
        short, "guardStaminaCutRate", default=0, hide=True,
        tooltip="Correction applied to the stamina required to block this attack (I presume). Never used.",
    )
    GuardPercentage: int = ParamField(
        short, "guardRate", default=0,
        tooltip="Percentage correction made to the guarding ability of the attack, as set in weapon parameters or NPC "
                "parameters. Only used to halve the guarding ability of parries (-50).",
    )
    ThrowID: int = ParamField(
        ushort, "throwTypeId", default=0,
        tooltip="Throw to trigger when attack hits. For some reason, throws are triggered using this ID, which is a "
                "field within each Throw table entry rather than the ID of the Throw table entry itself.",
    )
    Hitbox0HitType: ATK_PARAM_HIT_TYPE = ParamField(
        byte, "hit0_hitType", default=0,
        tooltip="Type of hit applied by hitbox (slot 0). Always zero, except for some whip attacks.",
    )
    Hitbox1HitType: ATK_PARAM_HIT_TYPE = ParamField(
        byte, "hit1_hitType", default=0,
        tooltip="Type of hit applied by hitbox (slot 1). Always zero, except for some whip attacks.",
    )
    Hitbox2HitType: ATK_PARAM_HIT_TYPE = ParamField(
        byte, "hit2_hitType", default=0,
        tooltip="Type of hit applied by hitbox (slot 2). Always zero, except for some whip attacks.",
    )
    Hitbox3HitType: ATK_PARAM_HIT_TYPE = ParamField(
        byte, "hit3_hitType", default=0,
        tooltip="Type of hit applied by hitbox (slot 3). Always zero, except for some whip attacks.",
    )
    Hitbox0Priority: int = ParamField(
        byte, "hti0_Priority", default=0, hide=True,
        tooltip="Priority of hitbox (slot 0). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox1Priority: int = ParamField(
        byte, "hti1_Priority", default=0, hide=True,
        tooltip="Priority of hitbox (slot 1). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox2Priority: int = ParamField(
        byte, "hti2_Priority", default=0, hide=True,
        tooltip="Priority of hitbox (slot 2). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox3Priority: int = ParamField(
        byte, "hti3_Priority", default=0, hide=True,
        tooltip="Priority of hitbox (slot 3). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    ImpactLevel: ATKPARAM_REP_DMGTYPE = ParamField(
        byte, "dmgLevel", default=0,
        tooltip="Impact level of attack, which determines how the target reacts to it (e.g. knocked backward, "
                "launched into the air, etc.). Certain special effects on the target (e.g. Iron Flesh) may re-map "
                "this impact level to a different one.",
    )
    MapHitType: ATK_PARAM_MAP_HIT = ParamField(
        byte, "mapHitType", default=0,
        tooltip="Determines how this attack interacts with the map.",
    )
    IgnoreGuardPercentage: int = ParamField(
        sbyte, "guardCutCancelRate", default=0, hide=True,
        tooltip="Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
                "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, in "
                "favor of the simple 'IgnoreGuard' boolean field.",
    )
    AttackAttribute: ATKPARAM_ATKATTR_TYPE = ParamField(
        byte, "atkAttribute", default=0,
        tooltip="Type of physical damage done by attack.",
    )
    ElementAttribute: ATKPARAM_SPATTR_TYPE = ParamField(
        byte, "spAttribute", default=0,
        tooltip="Type of elemental damage done by attack. (Attacks can apply any combination of damage types, but "
                "this value will determine what visual effects the attack generates, etc.)",
    )
    VisualSoundEffectsOnAttack: ATK_TYPE = ParamField(
        byte, "atkType", default=0,
        tooltip="Determines the sounds and visual effects generated by the attack itself (before hit).",
    )
    VisualSoundEffectsOnHit: WEP_MATERIAL_ATK = ParamField(
        byte, "atkMaterial", default=0,
        tooltip="Determines the sounds and visual effects generated when the attack hits. A value of 255 uses the "
                "weapon default.",
    )
    AttackSize: BEHAVIOR_ATK_SIZE = ParamField(
        byte, "atkSize", default=0, hide=True,
        tooltip="Internal description says this determines the size of sounds and visual effects, but it is never "
                "used.",
    )
    SoundEffectsWhileBlocking: WEP_MATERIAL_DEF = ParamField(
        byte, "defMaterial", default=0,
        tooltip="Determines the sound effects used when guarding. Usually 255 for Player Attacks and 0 (if not a "
                "block) or 50 (if blocking) for Non-Player Attacks.",
    )
    VisualEffectsWhileBlocking: WEP_MATERIAL_DEF_SFX = ParamField(
        byte, "defSfxMaterial", default=0,
        tooltip="Determines the visual effects used when guarding. Usually 255 for Player Attacks and 0 (if not a "
                "block) or 50 (if blocking) for Non-Player Attacks.",
    )
    ModelPointSource: ATK_PARAM_HIT_SOURCE = ParamField(
        byte, "hitSourceType", default=0,
        tooltip="Internal description says 'specify where you get the model point for attack'. Set to 1 for parries, "
                "ripostes, and basic body attacks (falling, rolling, etc.), and zero otherwise. Use that pattern.",
    )
    ThrowFlag: ATK_PATAM_THROWFLAG_TYPE = ParamField(
        byte, "throwFlag", default=0,
        tooltip="Determines how this attack relates to throws: not at all, a throw trigger, or a throw damage "
                "parameter.",
    )
    IgnoreGuard: bool = ParamField(
        byte, "disableGuard:1", bit_count=1, default=False,
        tooltip="If True, this attack cannot be blocked (e.g. throws).",
    )
    NoStaminaDamage: bool = ParamField(
        byte, "disableStaminaAttack:1", bit_count=1, default=False,
        tooltip="If True, this attack will deal no stamina damage, regardless of its stamina attack power.",
    )
    NoSpecialEffects: bool = ParamField(
        byte, "disableHitSpEffect:1", bit_count=1, default=False,
        tooltip="If True, this attack will trigger no special effects on the target. Internal description mentions "
                "this is an 'SCE bug countermeasure' (referring to the original Dark Souls demo).",
    )
    NoMissNotificationForAI: bool = ParamField(
        byte, "IgnoreNotifyMissSwingForAI:1", bit_count=1, default=False,
        tooltip="If True, the character's AI will not be informed when this attack misses. Enabled for basic body "
                "attacks (falling, rolling, ladder punches, etc.) that are generally not considered to be serious "
                "attacks.",
    )
    RepeatHitSoundEffects: bool = ParamField(
        byte, "repeatHitSfx:1", bit_count=1, default=False, hide=True,
        tooltip="If True, sound effects will supposedly be repeated as long as the attack continuously hits a wall. "
                "Never enabled, which is probably a good thing.",
    )
    IsPhysicalProjectile: bool = ParamField(
        byte, "isArrowAtk:1", bit_count=1, default=False,
        tooltip="Flags if this is the attack damage parameter of a physical projectile (arrow, bolt, or throwing "
                "knife).",
    )
    IsAttackByGhost: bool = ParamField(
        byte, "isGhostAtk:1", bit_count=1, default=False,
        tooltip="Flags if this is an attack of a ghost, which presumably disables wall collision, etc.",
    )
    IgnoreInvincibilityFrames: bool = ParamField(
        byte, "isDisableNoDamage:1", bit_count=1, default=False,
        tooltip="If True, this attack will ignore invincibility frames from rolling or backstepping (but not other "
                "sources of invincibility such as TAE or events).",
    )
    _Pad0: bytes = ParamPad(1, "pad[1]")
