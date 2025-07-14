from __future__ import annotations

__all__ = ["ATK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class ATK_PARAM_ST(ParamRow):
    Hitbox0Radius: float = ParamField(
        float32, "hit0_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 0).",
    )
    Hitbox1Radius: float = ParamField(
        float32, "hit1_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 1).",
    )
    Hitbox2Radius: float = ParamField(
        float32, "hit2_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 2).",
    )
    Hitbox3Radius: float = ParamField(
        float32, "hit3_Radius", default=0.0,
        tooltip="Radius of sphere/capsule hitbox (slot 3).",
    )
    KnockbackDistance: float = ParamField(
        float32, "knockbackDist", default=0.0,
        tooltip="Knockback distance of attack.",
    )
    HitStopTime: float = ParamField(
        float32, "hitStopTime", default=0.0,
        tooltip="Unclear. This isn't hitbox duration, which is determined by the duration of the triggering TAE "
                "event. It may be the duration of the 'hit' flag on the target. Always set to 0, 0.08. or 0.11.",
    )
    SpecialEffectOnHit0: int = ParamField(
        int32, "spEffectId0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 0).",
    )
    SpecialEffectOnHit1: int = ParamField(
        int32, "spEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 1).",
    )
    SpecialEffectOnHit2: int = ParamField(
        int32, "spEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 2).",
    )
    SpecialEffectOnHit3: int = ParamField(
        int32, "spEffectId3", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 3).",
    )
    SpecialEffectOnHit4: int = ParamField(
        int32, "spEffectId4", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target on hit (slot 4).",
    )
    Hitbox0StartModelPoint: int = ParamField(
        int16, "hit0_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 0). If Hitbox0EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox1StartModelPoint: int = ParamField(
        int16, "hit1_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 1). If Hitbox1EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox2StartModelPoint: int = ParamField(
        int16, "hit2_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 2). If Hitbox2EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox3StartModelPoint: int = ParamField(
        int16, "hit3_DmyPoly1", default=0,
        tooltip="Model point at origin of hitbox (slot 3). If Hitbox3EndModelPoint is not -1, the hitbox will be a "
                "capsule with hemispherical caps positioned at these origins (with a joining cylinder).",
    )
    Hitbox0EndModelPoint: int = ParamField(
        int16, "hit0_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 0). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox0StartModelPoint.",
    )
    Hitbox1EndModelPoint: int = ParamField(
        int16, "hit1_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 1). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox1StartModelPoint.",
    )
    Hitbox2EndModelPoint: int = ParamField(
        int16, "hit2_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 2). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox2StartModelPoint.",
    )
    Hitbox3EndModelPoint: int = ParamField(
        int16, "hit3_DmyPoly2", default=0,
        tooltip="Model point at end of capsule hitbox (slot 3). If this is -1, the hitbox will be a sphere placed at "
                "Hitbox3StartModelPoint.",
    )
    BlowOffCorrection: int = ParamField(
        uint16, "blowingCorrection", default=0,
        tooltip="Unknown. Never used.",
    )
    PhysicalAttackPowerPercentage: int = ParamField(
        uint16, "atkPhysCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate physical "
                "attack damage.",
    )
    MagicAttackPowerPercentage: int = ParamField(
        uint16, "atkMagCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate magic "
                "attack damage.",
    )
    FireAttackPowerPercentage: int = ParamField(
        uint16, "atkFireCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate fire attack "
                "damage.",
    )
    LightningAttackPowerPercentage: int = ParamField(
        uint16, "atkThunCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate lightning "
                "attack damage.",
    )
    StaminaAttackPowerPercentage: int = ParamField(
        uint16, "atkStamCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character attack power to calculate stamina "
                "damage.",
    )
    GuardAttackPercentage: int = ParamField(
        uint16, "guardAtkRateCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character guard attack power. Throw attacks "
                "have a value of 9900, which must essentially ignore blocking completely.",
    )
    GuardBreakPercentage: int = ParamField(
        uint16, "guardBreakCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to character guard breaking power. Not sure what "
                "that is, exactly, but this is set to 0 for parries and 100 for all other attacks.",
    )
    AttackDuringThrowPercentage: int = ParamField(
        uint16, "atkThrowEscapeCorrection", default=0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to weapon attacks during throws. Generally set to "
                "100, except for throw attacks themselves.",
    )
    SubCategory1: int = ParamField(
        uint8, "subCategory1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory2: int = ParamField(
        uint8, "subCategory2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalAttackPower: int = ParamField(
        uint16, "atkPhys", default=0,
        tooltip="Absolute physical attack power of attack.",
    )
    MagicAttackPower: int = ParamField(
        uint16, "atkMag", default=0,
        tooltip="Absolute magic attack power of attack.",
    )
    FireAttackPower: int = ParamField(
        uint16, "atkFire", default=0,
        tooltip="Absolute fire attack power of attack.",
    )
    LightningAttackPower: int = ParamField(
        uint16, "atkThun", default=0,
        tooltip="Absolute lightning attack power of attack.",
    )
    StaminaAttackPower: int = ParamField(
        uint16, "atkStam", default=0,
        tooltip="Absolute stamina attack power of attack.",
    )
    GuardAttackPower: int = ParamField(
        uint16, "guardAtkRate", default=0,
        tooltip="Absolute guard attack power of attack.",
    )
    GuardBreakPower: int = ParamField(
        uint16, "guardBreakRate", default=0,
        tooltip="Absolute guard breaking power of attack.",
    )
    _Pad0: bytes = ParamPad(1, "pad6[1]")
    IsEnableCalcDamageForBushesObj: int = ParamField(
        uint8, "isEnableCalcDamageForBushesObj", ATK_PARAM_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackPowerDuringThrows: int = ParamField(
        uint16, "atkThrowEscape", default=0,
        tooltip="Absolute attack power of attack. Never used.",
    )
    ObjectDamage: int = ParamField(
        uint16, "atkObj", default=0,
        tooltip="Amount of damage dealt to objects by this attack.",
    )
    GuardStaminaPercentage: int = ParamField(
        int16, "guardStaminaCutRate", default=0,
        tooltip="Correction applied to the stamina required to block this attack (I presume). Never used.",
    )
    GuardPercentage: int = ParamField(
        int16, "guardRate", default=0,
        tooltip="Percentage correction made to the guarding ability of the attack, as set in weapon parameters or NPC "
                "parameters. Only used to halve the guarding ability of parries (-50).",
    )
    ThrowID: int = ParamField(
        uint16, "throwTypeId", default=0,
        tooltip="Throw to trigger when attack hits. For some reason, throws are triggered using this ID, which is a "
                "field within each Throw table entry rather than the ID of the Throw table entry itself.",
    )
    Hitbox0HitType: int = ParamField(
        uint8, "hit0_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 0). Always zero, except for some whip attacks.",
    )
    Hitbox1HitType: int = ParamField(
        uint8, "hit1_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 1). Always zero, except for some whip attacks.",
    )
    Hitbox2HitType: int = ParamField(
        uint8, "hit2_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 2). Always zero, except for some whip attacks.",
    )
    Hitbox3HitType: int = ParamField(
        uint8, "hit3_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="Type of hit applied by hitbox (slot 3). Always zero, except for some whip attacks.",
    )
    Hitbox0Priority: int = ParamField(
        uint8, "hti0_Priority", default=0,
        tooltip="Priority of hitbox (slot 0). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox1Priority: int = ParamField(
        uint8, "hti1_Priority", default=0,
        tooltip="Priority of hitbox (slot 1). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox2Priority: int = ParamField(
        uint8, "hti2_Priority", default=0,
        tooltip="Priority of hitbox (slot 2). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    Hitbox3Priority: int = ParamField(
        uint8, "hti3_Priority", default=0,
        tooltip="Priority of hitbox (slot 3). If two hits occur simultaneously, only the highest priority hit occurs. "
                "Never used.",
    )
    ImpactLevel: int = ParamField(
        uint8, "dmgLevel", default=0,
        tooltip="Impact level of attack, which determines how the target reacts to it (e.g. knocked backward, "
                "launched into the air, etc.). Certain special effects on the target (e.g. Iron Flesh) may re-map "
                "this impact level to a different one.",
    )
    MapHitType: int = ParamField(
        uint8, "mapHitType", ATK_PARAM_MAP_HIT, default=0,
        tooltip="Determines how this attack interacts with the map.",
    )
    IgnoreGuardPercentage: int = ParamField(
        int8, "guardCutCancelRate", default=0,
        tooltip="Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
                "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, in "
                "favor of the simple 'IgnoreGuard' boolean field.",
    )
    AttackAttribute: int = ParamField(
        uint8, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="Type of physical damage done by attack.",
    )
    ElementAttribute: int = ParamField(
        uint8, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="Type of elemental damage done by attack. (Attacks can apply any combination of damage types, but "
                "this value will determine what visual effects the attack generates, etc.)",
    )
    VisualSoundEffectsOnAttack: int = ParamField(
        uint8, "atkType", BEHAVIOR_ATK_TYPE, default=0,
        tooltip="Determines the sounds and visual effects generated by the attack itself (before hit).",
    )
    VisualSoundEffectsOnHit: int = ParamField(
        uint8, "atkMaterial", WEP_MATERIAL_ATK, default=0,
        tooltip="Determines the sounds and visual effects generated when the attack hits. A value of 255 uses the "
                "weapon default.",
    )
    GuardRangeType: int = ParamField(
        uint8, "guardRangeType", ATKPARAM_GUARD_RANGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial1: int = ParamField(
        uint16, "defSeMaterial1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelPointSource: int = ParamField(
        uint8, "hitSourceType", ATK_PARAM_HIT_SOURCE, default=0,
        tooltip="Internal description says 'specify where you get the model point for attack'. Set to 1 for parries, "
                "ripostes, and basic body attacks (falling, rolling, etc.), and zero otherwise. Use that pattern.",
    )
    ThrowFlag: int = ParamField(
        uint8, "throwFlag", ATK_PATAM_THROWFLAG_TYPE, default=0,
        tooltip="Determines how this attack relates to throws: not at all, a throw trigger, or a throw damage "
                "parameter.",
    )
    IgnoreGuard: bool = ParamField(
        uint8, "disableGuard:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack cannot be blocked (e.g. throws).",
    )
    NoStaminaDamage: bool = ParamField(
        uint8, "disableStaminaAttack:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack will deal no stamina damage, regardless of its stamina attack power.",
    )
    NoSpecialEffects: bool = ParamField(
        uint8, "disableHitSpEffect:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack will trigger no special effects on the target. Internal description mentions "
                "this is an 'SCE bug countermeasure' (referring to the original Dark Souls demo).",
    )
    NoMissNotificationForAI: bool = ParamField(
        uint8, "IgnoreNotifyMissSwingForAI:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, the character's AI will not be informed when this attack misses. Enabled for basic body "
                "attacks (falling, rolling, ladder punches, etc.) that are generally not considered to be serious "
                "attacks.",
    )
    RepeatHitSoundEffects: bool = ParamField(
        uint8, "repeatHitSfx:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, sound effects will supposedly be repeated as long as the attack continuously hits a wall. "
                "Never enabled, which is probably a good thing.",
    )
    IsPhysicalProjectile: bool = ParamField(
        uint8, "isArrowAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="Flags if this is the attack damage parameter of a physical projectile (arrow, bolt, or throwing "
                "knife).",
    )
    IsAttackByGhost: bool = ParamField(
        uint8, "isGhostAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="Flags if this is an attack of a ghost, which presumably disables wall collision, etc.",
    )
    IgnoreInvincibilityFrames: bool = ParamField(
        uint8, "isDisableNoDamage:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="If True, this attack will ignore invincibility frames from rolling or backstepping (but not other "
                "sources of invincibility such as TAE or events).",
    )
    AtkPowforSfx: int = ParamField(
        int8, "atkPow_forSfx", ATKPARAM_SFX_ATK_POW, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDirforSfx: int = ParamField(
        int8, "atkDir_forSfx", ATKPARAM_SFX_ATK_DIR, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsEnemies: bool = ParamField(
        uint8, "opposeTarget:1", ATK_PARAM_BOOL, bit_count=1, default=True,
        tooltip="TODO",
    )
    AffectsAllies: bool = ParamField(
        uint8, "friendlyTarget:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    AffectsSelf: bool = ParamField(
        uint8, "selfTarget:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsCheckDoorPenetration: bool = ParamField(
        uint8, "isCheckDoorPenetration:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsVsRideAtk: bool = ParamField(
        uint8, "isVsRideAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAddBaseAtk: bool = ParamField(
        uint8, "isAddBaseAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeThreatLvNotify: bool = ParamField(
        uint8, "excludeThreatLvNotify:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad1:1", bit_count=1)
    AtkBehaviorId: int = ParamField(
        uint8, "atkBehaviorId", ATKPARAM_BEHAVIOR_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPowforSe: int = ParamField(
        int8, "atkPow_forSe", ATKPARAM_SE_ATK_POW, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoiseAttackPower: float = ParamField(
        float32, "atkSuperArmor", default=0.0,
        tooltip="Absolute poise attack power of attack.",
    )
    DecalID1: int = ParamField(
        int32, "decalId1", game_type=DecalParam, default=-1,
        tooltip="TODO",
    )
    DecalID2: int = ParamField(
        int32, "decalId2", game_type=DecalParam, default=-1,
        tooltip="TODO",
    )
    AppearAiSoundId: int = ParamField(
        int32, "AppearAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitAiSoundId: int = ParamField(
        int32, "HitAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleId: int = ParamField(
        int32, "HitRumbleId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByNormal: int = ParamField(
        int32, "HitRumbleIdByNormal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByMiddle: int = ParamField(
        int32, "HitRumbleIdByMiddle", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByRoot: int = ParamField(
        int32, "HitRumbleIdByRoot", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId0: int = ParamField(
        int32, "traceSfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead0: int = ParamField(
        int32, "traceDmyIdHead0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail0: int = ParamField(
        int32, "traceDmyIdTail0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId1: int = ParamField(
        int32, "traceSfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead1: int = ParamField(
        int32, "traceDmyIdHead1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail1: int = ParamField(
        int32, "traceDmyIdTail1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId2: int = ParamField(
        int32, "traceSfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead2: int = ParamField(
        int32, "traceDmyIdHead2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail2: int = ParamField(
        int32, "traceDmyIdTail2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId3: int = ParamField(
        int32, "traceSfxId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead3: int = ParamField(
        int32, "traceDmyIdHead3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail3: int = ParamField(
        int32, "traceDmyIdTail3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId4: int = ParamField(
        int32, "traceSfxId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead4: int = ParamField(
        int32, "traceDmyIdHead4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail4: int = ParamField(
        int32, "traceDmyIdTail4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId5: int = ParamField(
        int32, "traceSfxId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead5: int = ParamField(
        int32, "traceDmyIdHead5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail5: int = ParamField(
        int32, "traceDmyIdTail5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId6: int = ParamField(
        int32, "traceSfxId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead6: int = ParamField(
        int32, "traceDmyIdHead6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail6: int = ParamField(
        int32, "traceDmyIdTail6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId7: int = ParamField(
        int32, "traceSfxId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead7: int = ParamField(
        int32, "traceDmyIdHead7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail7: int = ParamField(
        int32, "traceDmyIdTail7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Hit4Radius: float = ParamField(
        float32, "hit4_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5Radius: float = ParamField(
        float32, "hit5_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6Radius: float = ParamField(
        float32, "hit6_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7Radius: float = ParamField(
        float32, "hit7_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8Radius: float = ParamField(
        float32, "hit8_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9Radius: float = ParamField(
        float32, "hit9_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10Radius: float = ParamField(
        float32, "hit10_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11Radius: float = ParamField(
        float32, "hit11_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12Radius: float = ParamField(
        float32, "hit12_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13Radius: float = ParamField(
        float32, "hit13_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14Radius: float = ParamField(
        float32, "hit14_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15Radius: float = ParamField(
        float32, "hit15_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4DmyPoly1: int = ParamField(
        int16, "hit4_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5DmyPoly1: int = ParamField(
        int16, "hit5_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6DmyPoly1: int = ParamField(
        int16, "hit6_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7DmyPoly1: int = ParamField(
        int16, "hit7_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8DmyPoly1: int = ParamField(
        int16, "hit8_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9DmyPoly1: int = ParamField(
        int16, "hit9_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10DmyPoly1: int = ParamField(
        int16, "hit10_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11DmyPoly1: int = ParamField(
        int16, "hit11_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12DmyPoly1: int = ParamField(
        int16, "hit12_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13DmyPoly1: int = ParamField(
        int16, "hit13_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14DmyPoly1: int = ParamField(
        int16, "hit14_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15DmyPoly1: int = ParamField(
        int16, "hit15_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4DmyPoly2: int = ParamField(
        int16, "hit4_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5DmyPoly2: int = ParamField(
        int16, "hit5_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6DmyPoly2: int = ParamField(
        int16, "hit6_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7DmyPoly2: int = ParamField(
        int16, "hit7_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8DmyPoly2: int = ParamField(
        int16, "hit8_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9DmyPoly2: int = ParamField(
        int16, "hit9_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10DmyPoly2: int = ParamField(
        int16, "hit10_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11DmyPoly2: int = ParamField(
        int16, "hit11_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12DmyPoly2: int = ParamField(
        int16, "hit12_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13DmyPoly2: int = ParamField(
        int16, "hit13_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14DmyPoly2: int = ParamField(
        int16, "hit14_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15DmyPoly2: int = ParamField(
        int16, "hit15_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4hitType: int = ParamField(
        uint8, "hit4_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5hitType: int = ParamField(
        uint8, "hit5_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6hitType: int = ParamField(
        uint8, "hit6_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7hitType: int = ParamField(
        uint8, "hit7_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8hitType: int = ParamField(
        uint8, "hit8_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9hitType: int = ParamField(
        uint8, "hit9_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10hitType: int = ParamField(
        uint8, "hit10_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11hitType: int = ParamField(
        uint8, "hit11_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12hitType: int = ParamField(
        uint8, "hit12_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13hitType: int = ParamField(
        uint8, "hit13_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14hitType: int = ParamField(
        uint8, "hit14_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15hitType: int = ParamField(
        uint8, "hit15_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti4Priority: int = ParamField(
        uint8, "hti4_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti5Priority: int = ParamField(
        uint8, "hti5_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti6Priority: int = ParamField(
        uint8, "hti6_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti7Priority: int = ParamField(
        uint8, "hti7_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti8Priority: int = ParamField(
        uint8, "hti8_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti9Priority: int = ParamField(
        uint8, "hti9_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti10Priority: int = ParamField(
        uint8, "hti10_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti11Priority: int = ParamField(
        uint8, "hti11_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti12Priority: int = ParamField(
        uint8, "hti12_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti13Priority: int = ParamField(
        uint8, "hti13_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti14Priority: int = ParamField(
        uint8, "hti14_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti15Priority: int = ParamField(
        uint8, "hti15_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial1: int = ParamField(
        uint16, "defSfxMaterial1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial2: int = ParamField(
        uint16, "defSeMaterial2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial2: int = ParamField(
        uint16, "defSfxMaterial2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDarkCorrection: int = ParamField(
        uint16, "atkDarkCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDark: int = ParamField(
        uint16, "atkDark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad5:1", bit_count=1)
    IsDisableParry: bool = ParamField(
        uint8, "isDisableParry:1", ATK_PARAM_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBothHandsAtkBonus: bool = ParamField(
        uint8, "isDisableBothHandsAtkBonus:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInvalidatedByNoDamageInAir: bool = ParamField(
        uint8, "isInvalidatedByNoDamageInAir:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad2: int = ParamBitPad(uint8, "pad2:4", bit_count=4)
    DmgLevelvsPlayer: int = ParamField(
        int8, "dmgLevel_vsPlayer", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    StatusAilmentAtkPowerCorrectRate: int = ParamField(
        uint16, "statusAilmentAtkPowerCorrectRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyPoint: int = ParamField(
        uint16, "spEffectAtkPowerCorrectRate_byPoint", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyRate: int = ParamField(
        uint16, "spEffectAtkPowerCorrectRate_byRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyDmg: int = ParamField(
        uint16, "spEffectAtkPowerCorrectRate_byDmg", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AtkBehaviorId2: int = ParamField(
        uint8, "atkBehaviorId_2", ATKPARAM_BEHAVIOR_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowDamageAttribute: int = ParamField(
        uint8, "throwDamageAttribute", ATKPARAM_THROWATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    StatusAilmentAtkPowerCorrectRatebyPoint: int = ParamField(
        uint16, "statusAilmentAtkPowerCorrectRate_byPoint", default=100,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteAttackElementCorrectId: int = ParamField(
        int32, "overwriteAttackElementCorrectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalBaseId1: int = ParamField(
        int16, "decalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalBaseId2: int = ParamField(
        int16, "decalBaseId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponRegainHPScale: int = ParamField(
        uint16, "wepRegainHpScale", default=100,
        tooltip="TODO",
    )
    AttackRegainHP: int = ParamField(
        uint16, "atkRegainHp", default=0,
        tooltip="TODO",
    )
    RegainTimeScale: float = ParamField(
        float32, "regainableTimeScale", default=1.0,
        tooltip="TODO",
    )
    RegainHPRateScale: float = ParamField(
        float32, "regainableHpRateScale", default=1.0,
        tooltip="TODO",
    )
    RegainableSlotID: int = ParamField(
        int8, "regainableSlotId", default=-1,
        tooltip="TODO",
    )
    SpAttributeVariationValue: int = ParamField(
        uint8, "spAttributeVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryForwardOffset: int = ParamField(
        int16, "parryForwardOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoiseAttackPercentage: float = ParamField(
        float32, "atkSuperArmorCorrection", default=0.0,
        tooltip="Multiplier (as percentage from 0 upwards) applied to damage to target poise. Generally set to 100, "
                "except for throw attacks themselves.",
    )
    DefSfxMaterialVariationValue: int = ParamField(
        uint8, "defSfxMaterialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad4[3]")
    FinalDamageRateID: int = ParamField(
        int32, "finalDamageRateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(12, "pad7_old[12]")
    SubCategory3: int = ParamField(
        uint8, "subCategory3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory4: int = ParamField(
        uint8, "subCategory4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(10, "pad7[10]")
