from __future__ import annotations

__all__ = ["ATK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


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
    SpecialEffectOnHit0: int = ParamField(
        int, "spEffectId0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 0).",
    )
    SpecialEffectOnHit1: int = ParamField(
        int, "spEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 1).",
    )
    SpecialEffectOnHit2: int = ParamField(
        int, "spEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 2).",
    )
    SpecialEffectOnHit3: int = ParamField(
        int, "spEffectId3", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 3).",
    )
    SpecialEffectOnHit4: int = ParamField(
        int, "spEffectId4", game_type=SpecialEffectParam, default=-1,
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
        ushort, "blowingCorrection", default=0,
        tooltip="Unknown. Never used.",
    )
    PhysicalAttackPowerPercentage: int = ParamField(
        ushort, "atkPhysCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate physical "
                "attack damage.",
    )
    MagicAttackPowerPercentage: int = ParamField(
        ushort, "atkMagCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate magic "
                "attack damage.",
    )
    FireAttackPowerPercentage: int = ParamField(
        ushort, "atkFireCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate fire attack "
                "damage.",
    )
    LightningAttackPowerPercentage: int = ParamField(
        ushort, "atkThunCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate lightning "
                "attack damage.",
    )
    StaminaAttackPowerPercentage: int = ParamField(
        ushort, "atkStamCorrection", default=0,
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
    SubCategory1: int = ParamField(
        byte, "subCategory1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory2: int = ParamField(
        byte, "subCategory2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
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
        ushort, "guardAtkRate", default=0,
        tooltip="Absolute guard attack power of attack.",
    )
    GuardBreakPower: int = ParamField(
        ushort, "guardBreakRate", default=0,
        tooltip="Absolute guard breaking power of attack.",
    )
    _Pad0: bytes = ParamPad(1, "pad6[1]")
    IsEnableCalcDamageForBushesObj: int = ParamField(
        byte, "isEnableCalcDamageForBushesObj", ATK_PARAM_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackPowerDuringThrows: int = ParamField(
        ushort, "atkThrowEscape", default=0,
        tooltip="Absolute attack power of attack. Never used.",
    )
    ObjectDamage: int = ParamField(
        ushort, "atkObj", default=0,
        tooltip="Amount of damage dealt to objects by this attack.",
    )
    GuardStaminaPercentage: int = ParamField(
        short, "guardStaminaCutRate", default=0,
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
    Hitbox0HitType: int = ParamField(
        byte, "hit0_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 0). Always zero, except for some whip attacks.",
    )
    Hitbox1HitType: int = ParamField(
        byte, "hit1_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 1). Always zero, except for some whip attacks.",
    )
    Hitbox2HitType: int = ParamField(
        byte, "hit2_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 2). Always zero, except for some whip attacks.",
    )
    Hitbox3HitType: int = ParamField(
        byte, "hit3_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 3). Always zero, except for some whip attacks.",
    )
    Hitbox0Priority: int = ParamField(
        byte, "hti0_Priority", default=0,
        tooltip="Priority of hitbox (slot 0). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox1Priority: int = ParamField(
        byte, "hti1_Priority", default=0,
        tooltip="Priority of hitbox (slot 1). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox2Priority: int = ParamField(
        byte, "hti2_Priority", default=0,
        tooltip="Priority of hitbox (slot 2). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox3Priority: int = ParamField(
        byte, "hti3_Priority", default=0,
        tooltip="Priority of hitbox (slot 3). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    ImpactLevel: int = ParamField(
        byte, "dmgLevel", default=0,
        tooltip="Impact level of attack, which determines how the target reacts to it (e.g. knocked backward, "
                "launched into the air, etc.). Certain special effects on the target (e.g. Iron Flesh) may re-map "
                "this impact level to a different one.",
    )
    MapHitType: int = ParamField(
        byte, "mapHitType", ATK_PARAM_MAP_HIT, default=0,
        tooltip="Determines how this attack interacts with the map.",
    )
    IgnoreGuardPercentage: int = ParamField(
        sbyte, "guardCutCancelRate", default=0,
        tooltip="Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
                "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, in "
                "favor of the simple 'IgnoreGuard' boolean field.",
    )
    AttackAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="Type of physical damage done by attack.",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="Type of elemental damage done by attack. (Attacks can apply any combination of damage types, but "
                "this value will determine what visual effects the attack generates, etc.)",
    )
    VisualSoundEffectsOnAttack: int = ParamField(
        byte, "atkType", BEHAVIOR_ATK_TYPE, default=0,
        tooltip="Determines the sounds and visual effects generated by the attack itself (before hit).",
    )
    VisualSoundEffectsOnHit: int = ParamField(
        byte, "atkMaterial", WEP_MATERIAL_ATK, default=0,
        tooltip="Determines the sounds and visual effects generated when the attack hits. A value of 255 uses the "
                "weapon default.",
    )
    GuardRangeType: int = ParamField(
        byte, "guardRangeType", ATKPARAM_GUARD_RANGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial1: int = ParamField(
        ushort, "defSeMaterial1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelPointSource: int = ParamField(
        byte, "hitSourceType", ATK_PARAM_HIT_SOURCE, default=0,
        tooltip="Internal description says 'specify where you get the model point for attack'. Set to 1 for parries, "
                "ripostes, and basic body attacks (falling, rolling, etc.), and zero otherwise. Use that pattern.",
    )
    ThrowFlag: int = ParamField(
        byte, "throwFlag", ATK_PATAM_THROWFLAG_TYPE, default=0,
        tooltip="Determines how this attack relates to throws: not at all, a throw trigger, or a throw damage "
                "parameter.",
    )
    IgnoreGuard: bool = ParamField(
        byte, "disableGuard:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack cannot be blocked (e.g. throws).",
    )
    NoStaminaDamage: bool = ParamField(
        byte, "disableStaminaAttack:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack will deal no stamina damage, regardless of its stamina attack power.",
    )
    NoSpecialEffects: bool = ParamField(
        byte, "disableHitSpEffect:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack will trigger no special effects on the target. Internal description mentions "
                "this is an 'SCE bug countermeasure' (referring to the original Dark Souls demo).",
    )
    NoMissNotificationForAI: bool = ParamField(
        byte, "IgnoreNotifyMissSwingForAI:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, the character's AI will not be informed when this attack misses. Enabled for basic body "
                "attacks (falling, rolling, ladder punches, etc.) that are generally not considered to be serious "
                "attacks.",
    )
    RepeatHitSoundEffects: bool = ParamField(
        byte, "repeatHitSfx:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, sound effects will supposedly be repeated as long as the attack continuously hits a wall. "
                "Never enabled, which is probably a good thing.",
    )
    IsPhysicalProjectile: bool = ParamField(
        byte, "isArrowAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="Flags if this is the attack damage parameter of a physical projectile (arrow, bolt, or throwing "
                "knife).",
    )
    IsAttackByGhost: bool = ParamField(
        byte, "isGhostAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="Flags if this is an attack of a ghost, which presumably disables wall collision, etc.",
    )
    IgnoreInvincibilityFrames: bool = ParamField(
        byte, "isDisableNoDamage:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack will ignore invincibility frames from rolling or backstepping (but not other "
                "sources of invincibility such as TAE or events).",
    )
    AtkPowforSfx: int = ParamField(
        sbyte, "atkPow_forSfx", ATKPARAM_SFX_ATK_POW, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDirforSfx: int = ParamField(
        sbyte, "atkDir_forSfx", ATKPARAM_SFX_ATK_DIR, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsEnemies: bool = ParamField(
        byte, "opposeTarget:1", ATK_PARAM_BOOL, bit_count=1, default=True,
        tooltip="TODO",
    )
    AffectsAllies: bool = ParamField(
        byte, "friendlyTarget:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    AffectsSelf: bool = ParamField(
        byte, "selfTarget:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsCheckDoorPenetration: bool = ParamField(
        byte, "isCheckDoorPenetration:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsVsRideAtk: bool = ParamField(
        byte, "isVsRideAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAddBaseAtk: bool = ParamField(
        byte, "isAddBaseAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeThreatLvNotify: bool = ParamField(
        byte, "excludeThreatLvNotify:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad1:1", bit_count=1)
    AtkBehaviorId: int = ParamField(
        byte, "atkBehaviorId", ATKPARAM_BEHAVIOR_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPowforSe: int = ParamField(
        sbyte, "atkPow_forSe", ATKPARAM_SE_ATK_POW, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoiseAttackPower: float = ParamField(
        float, "atkSuperArmor", default=0.0,
        tooltip="Absolute poise attack power of attack.",
    )
    DecalID1: int = ParamField(
        int, "decalId1", game_type=DecalParam, default=-1,
        tooltip="TODO",
    )
    DecalID2: int = ParamField(
        int, "decalId2", game_type=DecalParam, default=-1,
        tooltip="TODO",
    )
    AppearAiSoundId: int = ParamField(
        int, "AppearAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitAiSoundId: int = ParamField(
        int, "HitAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleId: int = ParamField(
        int, "HitRumbleId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByNormal: int = ParamField(
        int, "HitRumbleIdByNormal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByMiddle: int = ParamField(
        int, "HitRumbleIdByMiddle", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByRoot: int = ParamField(
        int, "HitRumbleIdByRoot", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId0: int = ParamField(
        int, "traceSfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead0: int = ParamField(
        int, "traceDmyIdHead0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail0: int = ParamField(
        int, "traceDmyIdTail0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId1: int = ParamField(
        int, "traceSfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead1: int = ParamField(
        int, "traceDmyIdHead1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail1: int = ParamField(
        int, "traceDmyIdTail1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId2: int = ParamField(
        int, "traceSfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead2: int = ParamField(
        int, "traceDmyIdHead2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail2: int = ParamField(
        int, "traceDmyIdTail2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId3: int = ParamField(
        int, "traceSfxId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead3: int = ParamField(
        int, "traceDmyIdHead3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail3: int = ParamField(
        int, "traceDmyIdTail3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId4: int = ParamField(
        int, "traceSfxId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead4: int = ParamField(
        int, "traceDmyIdHead4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail4: int = ParamField(
        int, "traceDmyIdTail4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId5: int = ParamField(
        int, "traceSfxId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead5: int = ParamField(
        int, "traceDmyIdHead5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail5: int = ParamField(
        int, "traceDmyIdTail5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId6: int = ParamField(
        int, "traceSfxId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead6: int = ParamField(
        int, "traceDmyIdHead6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail6: int = ParamField(
        int, "traceDmyIdTail6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId7: int = ParamField(
        int, "traceSfxId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead7: int = ParamField(
        int, "traceDmyIdHead7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail7: int = ParamField(
        int, "traceDmyIdTail7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Hit4Radius: float = ParamField(
        float, "hit4_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5Radius: float = ParamField(
        float, "hit5_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6Radius: float = ParamField(
        float, "hit6_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7Radius: float = ParamField(
        float, "hit7_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8Radius: float = ParamField(
        float, "hit8_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9Radius: float = ParamField(
        float, "hit9_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10Radius: float = ParamField(
        float, "hit10_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11Radius: float = ParamField(
        float, "hit11_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12Radius: float = ParamField(
        float, "hit12_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13Radius: float = ParamField(
        float, "hit13_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14Radius: float = ParamField(
        float, "hit14_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15Radius: float = ParamField(
        float, "hit15_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4DmyPoly1: int = ParamField(
        short, "hit4_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5DmyPoly1: int = ParamField(
        short, "hit5_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6DmyPoly1: int = ParamField(
        short, "hit6_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7DmyPoly1: int = ParamField(
        short, "hit7_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8DmyPoly1: int = ParamField(
        short, "hit8_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9DmyPoly1: int = ParamField(
        short, "hit9_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10DmyPoly1: int = ParamField(
        short, "hit10_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11DmyPoly1: int = ParamField(
        short, "hit11_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12DmyPoly1: int = ParamField(
        short, "hit12_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13DmyPoly1: int = ParamField(
        short, "hit13_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14DmyPoly1: int = ParamField(
        short, "hit14_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15DmyPoly1: int = ParamField(
        short, "hit15_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4DmyPoly2: int = ParamField(
        short, "hit4_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5DmyPoly2: int = ParamField(
        short, "hit5_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6DmyPoly2: int = ParamField(
        short, "hit6_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7DmyPoly2: int = ParamField(
        short, "hit7_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8DmyPoly2: int = ParamField(
        short, "hit8_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9DmyPoly2: int = ParamField(
        short, "hit9_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10DmyPoly2: int = ParamField(
        short, "hit10_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11DmyPoly2: int = ParamField(
        short, "hit11_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12DmyPoly2: int = ParamField(
        short, "hit12_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13DmyPoly2: int = ParamField(
        short, "hit13_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14DmyPoly2: int = ParamField(
        short, "hit14_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15DmyPoly2: int = ParamField(
        short, "hit15_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4hitType: int = ParamField(
        byte, "hit4_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5hitType: int = ParamField(
        byte, "hit5_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6hitType: int = ParamField(
        byte, "hit6_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7hitType: int = ParamField(
        byte, "hit7_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8hitType: int = ParamField(
        byte, "hit8_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9hitType: int = ParamField(
        byte, "hit9_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10hitType: int = ParamField(
        byte, "hit10_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11hitType: int = ParamField(
        byte, "hit11_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12hitType: int = ParamField(
        byte, "hit12_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13hitType: int = ParamField(
        byte, "hit13_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14hitType: int = ParamField(
        byte, "hit14_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15hitType: int = ParamField(
        byte, "hit15_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti4Priority: int = ParamField(
        byte, "hti4_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti5Priority: int = ParamField(
        byte, "hti5_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti6Priority: int = ParamField(
        byte, "hti6_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti7Priority: int = ParamField(
        byte, "hti7_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti8Priority: int = ParamField(
        byte, "hti8_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti9Priority: int = ParamField(
        byte, "hti9_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti10Priority: int = ParamField(
        byte, "hti10_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti11Priority: int = ParamField(
        byte, "hti11_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti12Priority: int = ParamField(
        byte, "hti12_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti13Priority: int = ParamField(
        byte, "hti13_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti14Priority: int = ParamField(
        byte, "hti14_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti15Priority: int = ParamField(
        byte, "hti15_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial1: int = ParamField(
        ushort, "defSfxMaterial1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial2: int = ParamField(
        ushort, "defSeMaterial2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial2: int = ParamField(
        ushort, "defSfxMaterial2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDarkCorrection: int = ParamField(
        ushort, "atkDarkCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDark: int = ParamField(
        ushort, "atkDark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad5:1", bit_count=1)
    IsDisableParry: bool = ParamField(
        byte, "isDisableParry:1", ATK_PARAM_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBothHandsAtkBonus: bool = ParamField(
        byte, "isDisableBothHandsAtkBonus:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInvalidatedByNoDamageInAir: bool = ParamField(
        byte, "isInvalidatedByNoDamageInAir:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad2: int = ParamBitPad(byte, "pad2:4", bit_count=4)
    DmgLevelvsPlayer: int = ParamField(
        sbyte, "dmgLevel_vsPlayer", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    StatusAilmentAtkPowerCorrectRate: int = ParamField(
        ushort, "statusAilmentAtkPowerCorrectRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyPoint: int = ParamField(
        ushort, "spEffectAtkPowerCorrectRate_byPoint", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyRate: int = ParamField(
        ushort, "spEffectAtkPowerCorrectRate_byRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyDmg: int = ParamField(
        ushort, "spEffectAtkPowerCorrectRate_byDmg", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AtkBehaviorId2: int = ParamField(
        byte, "atkBehaviorId_2", ATKPARAM_BEHAVIOR_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowDamageAttribute: int = ParamField(
        byte, "throwDamageAttribute", ATKPARAM_THROWATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    StatusAilmentAtkPowerCorrectRatebyPoint: int = ParamField(
        ushort, "statusAilmentAtkPowerCorrectRate_byPoint", default=100,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteAttackElementCorrectId: int = ParamField(
        int, "overwriteAttackElementCorrectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalBaseId1: int = ParamField(
        short, "decalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalBaseId2: int = ParamField(
        short, "decalBaseId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponRegainHPScale: int = ParamField(
        ushort, "wepRegainHpScale", default=100,
        tooltip="TODO",
    )
    AttackRegainHP: int = ParamField(
        ushort, "atkRegainHp", default=0,
        tooltip="TODO",
    )
    RegainTimeScale: float = ParamField(
        float, "regainableTimeScale", default=1.0,
        tooltip="TODO",
    )
    RegainHPRateScale: float = ParamField(
        float, "regainableHpRateScale", default=1.0,
        tooltip="TODO",
    )
    RegainableSlotID: int = ParamField(
        sbyte, "regainableSlotId", default=-1,
        tooltip="TODO",
    )
    SpAttributeVariationValue: int = ParamField(
        byte, "spAttributeVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryForwardOffset: int = ParamField(
        short, "parryForwardOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoiseAttackPercentage: float = ParamField(
        float, "atkSuperArmorCorrection", default=0.0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to damage to target poise. Generally set to 100, "
                "except for throw attacks themselves.",
    )
    DefSfxMaterialVariationValue: int = ParamField(
        byte, "defSfxMaterialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad4[3]")
    FinalDamageRateID: int = ParamField(
        int, "finalDamageRateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(12, "pad7_old[12]")
    SubCategory3: int = ParamField(
        byte, "subCategory3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory4: int = ParamField(
        byte, "subCategory4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(10, "pad7[10]")
