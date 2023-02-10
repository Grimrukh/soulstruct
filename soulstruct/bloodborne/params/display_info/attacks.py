__all__ = ["ATK_PARAM_ST", "THROW_INFO_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field
from soulstruct.bloodborne.params.enums import *
from soulstruct.bloodborne.game_types import *


ATK_PARAM_ST = {
    "param_type": "ATK_PARAM_ST",
    "file_name": "AtkParam_Pc",  # also AtkParam_Npc
    "nickname": None,
    "fields": [
        ParamFieldInfo("hit0_Radius", "Hitbox0Radius", True, float, "Radius of sphere/capsule hitbox (slot 0)."),
        ParamFieldInfo("hit1_Radius", "Hitbox1Radius", True, float, "Radius of sphere/capsule hitbox (slot 1)."),
        ParamFieldInfo("hit2_Radius", "Hitbox2Radius", True, float, "Radius of sphere/capsule hitbox (slot 2)."),
        ParamFieldInfo("hit3_Radius", "Hitbox3Radius", True, float, "Radius of sphere/capsule hitbox (slot 3)."),
        ParamFieldInfo("knockbackDist", "KnockbackDistance", True, float, "Knockback distance of attack."),
        ParamFieldInfo(
            "hitStopTime",
            "HitStopTime",
            True,
            float,
            "Unclear. This isn't hitbox duration, which is determined by the duration of the triggering TAE "
            "event. It may be the duration of the 'hit' flag on the target. Always set to 0, 0.08. or 0.11.", 
        ),
        ParamFieldInfo(
            "spEffectId0",
            "SpecialEffectOnHit0",
            True,
            SpecialEffectParam,
            "Special effect applied to target on hit (slot 0).",
        ),
        ParamFieldInfo(
            "spEffectId1",
            "SpecialEffectOnHit1",
            True,
            SpecialEffectParam,
            "Special effect applied to target on hit (slot 1).",
        ),
        ParamFieldInfo(
            "spEffectId2",
            "SpecialEffectOnHit2",
            True,
            SpecialEffectParam,
            "Special effect applied to target on hit (slot 2).",
        ),
        ParamFieldInfo(
            "spEffectId3",
            "SpecialEffectOnHit3",
            True,
            SpecialEffectParam,
            "Special effect applied to target on hit (slot 3).",
        ),
        ParamFieldInfo(
            "spEffectId4",
            "SpecialEffectOnHit4",
            True,
            SpecialEffectParam,
            "Special effect applied to target on hit (slot 4).",
        ),
        ParamFieldInfo(
            "hit0_DmyPoly1",
            "Hitbox0StartModelPoint",
            True,
            int,
            "Model point at origin of hitbox (slot 0). If Hitbox0EndModelPoint is not -1, the hitbox will be a "
            "capsule with hemispherical caps positioned at these origins (with a joining cylinder).", 
        ),
        ParamFieldInfo(
            "hit1_DmyPoly1",
            "Hitbox1StartModelPoint",
            True,
            int,
            "Model point at origin of hitbox (slot 1). If Hitbox1EndModelPoint is not -1, the hitbox will be a "
            "capsule with hemispherical caps positioned at these origins (with a joining cylinder).", 
        ),
        ParamFieldInfo(
            "hit2_DmyPoly1",
            "Hitbox2StartModelPoint",
            True,
            int,
            "Model point at origin of hitbox (slot 2). If Hitbox2EndModelPoint is not -1, the hitbox will be a "
            "capsule with hemispherical caps positioned at these origins (with a joining cylinder).", 
        ),
        ParamFieldInfo(
            "hit3_DmyPoly1",
            "Hitbox3StartModelPoint",
            True,
            int,
            "Model point at origin of hitbox (slot 3). If Hitbox3EndModelPoint is not -1, the hitbox will be a "
            "capsule with hemispherical caps positioned at these origins (with a joining cylinder).", 
        ),
        ParamFieldInfo(
            "hit0_DmyPoly2",
            "Hitbox0EndModelPoint",
            True,
            int,
            "Model point at end of capsule hitbox (slot 0). If this is -1, the hitbox will be a sphere placed at "
            "Hitbox0StartModelPoint.", 
        ),
        ParamFieldInfo(
            "hit1_DmyPoly2",
            "Hitbox1EndModelPoint",
            True,
            int,
            "Model point at end of capsule hitbox (slot 1). If this is -1, the hitbox will be a sphere placed at "
            "Hitbox1StartModelPoint.", 
        ),
        ParamFieldInfo(
            "hit2_DmyPoly2",
            "Hitbox2EndModelPoint",
            True,
            int,
            "Model point at end of capsule hitbox (slot 2). If this is -1, the hitbox will be a sphere placed at "
            "Hitbox2StartModelPoint.", 
        ),
        ParamFieldInfo(
            "hit3_DmyPoly2",
            "Hitbox3EndModelPoint",
            True,
            int,
            "Model point at end of capsule hitbox (slot 3). If this is -1, the hitbox will be a sphere placed at "
            "Hitbox3StartModelPoint.", 
        ),
        ParamFieldInfo("blowingCorrection", "BlowOffCorrection", False, int, "Unknown. Never used."),
        ParamFieldInfo(
            "atkPhysCorrection",
            "PhysicalAttackPowerPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to character attack power to calculate physical "
            "attack damage.", 
        ),
        ParamFieldInfo(
            "atkMagCorrection",
            "MagicAttackPowerPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to character attack power to calculate magic "
            "attack damage.", 
        ),
        ParamFieldInfo(
            "atkFireCorrection",
            "FireAttackPowerPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to character attack power to calculate fire attack "
            "damage.", 
        ),
        ParamFieldInfo(
            "atkThunCorrection",
            "LightningAttackPowerPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to character attack power to calculate lightning "
            "attack damage.", 
        ),
        ParamFieldInfo(
            "atkStamCorrection",
            "StaminaAttackPowerPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to character attack power to calculate stamina "
            "damage.", 
        ),
        ParamFieldInfo(
            "guardAtkRateCorrection",
            "GuardAttackPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to character guard attack power. Throw attacks "
            "have a value of 9900, which must essentially ignore blocking completely.", 
        ),
        ParamFieldInfo(
            "guardBreakCorrection",
            "GuardBreakPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to character guard breaking power. Not sure what "
            "that is, exactly, but this is set to 0 for parries and 100 for all other attacks.", 
        ),
        ParamFieldInfo(
            "atkThrowEscapeCorrection",
            "AttackDuringThrowPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to weapon attacks during throws. Generally set to "
            "100, except for throw attacks themselves.", 
        ),
        ParamFieldInfo(
            "atkSuperArmorCorrection",
            "PoiseAttackPercentage",
            True,
            int,
            "Multiplier (as percentage from 0 upwards) applied to damage to target poise. Generally set to 100, "
            "except for throw attacks themselves.", 
        ),
        ParamFieldInfo("atkPhys", "PhysicalAttackPower", True, int, "Absolute physical attack power of attack."),
        ParamFieldInfo("atkMag", "MagicAttackPower", True, int, "Absolute magic attack power of attack."),
        ParamFieldInfo("atkFire", "FireAttackPower", True, int, "Absolute fire attack power of attack."),
        ParamFieldInfo("atkThun", "LightningAttackPower", True, int, "Absolute lightning attack power of attack."),
        ParamFieldInfo("atkStam", "StaminaAttackPower", True, int, "Absolute stamina attack power of attack."),
        ParamFieldInfo("guardAtkRate", "GuardAttackPower", True, int, "Absolute guard attack power of attack."),
        ParamFieldInfo("guardBreakRate", "GuardBreakPower", True, int, "Absolute guard breaking power of attack."),
        ParamFieldInfo("atkSuperArmor", "PoiseAttackPower", True, int, "Absolute poise attack power of attack."),
        ParamFieldInfo(
            "atkThrowEscape", "AttackPowerDuringThrows", False, int, "Absolute attack power of attack. Never used."
        ),
        ParamFieldInfo("atkObj", "ObjectDamage", True, int, "Amount of damage dealt to objects by this attack."),
        ParamFieldInfo(
            "guardStaminaCutRate",
            "GuardStaminaPercentage",
            False,
            int,
            "Correction applied to the stamina required to block this attack (I presume). Never used.",
        ),
        ParamFieldInfo(
            "guardRate",
            "GuardPercentage",
            True,
            int,
            "Percentage correction made to the guarding ability of the attack, as set in weapon parameters or NPC "
            "parameters. Only used to halve the guarding ability of parries (-50).", 
        ),
        ParamFieldInfo(
            "throwTypeId",
            "ThrowID",  # TODO: Link to Throws by searching in the target's ThrowID field rather than its entry ID.
            True,
            int,
            "Throw to trigger when attack hits. For some reason, throws are triggered using this ID, which is a "
            "field within each Throw table entry rather than the ID of the Throw table entry itself.",
        ),
        ParamFieldInfo(
            "hit0_hitType",
            "Hitbox0HitType",
            True,
            ATK_PARAM_HIT_TYPE,
            "Type of hit applied by hitbox (slot 0). Always zero, except for some whip attacks.",
        ),
        ParamFieldInfo(
            "hit1_hitType",
            "Hitbox1HitType",
            True,
            ATK_PARAM_HIT_TYPE,
            "Type of hit applied by hitbox (slot 1). Always zero, except for some whip attacks.",
        ),
        ParamFieldInfo(
            "hit2_hitType",
            "Hitbox2HitType",
            True,
            ATK_PARAM_HIT_TYPE,
            "Type of hit applied by hitbox (slot 2). Always zero, except for some whip attacks.",
        ),
        ParamFieldInfo(
            "hit3_hitType",
            "Hitbox3HitType",
            True,
            ATK_PARAM_HIT_TYPE,
            "Type of hit applied by hitbox (slot 3). Always zero, except for some whip attacks.",
        ),
        ParamFieldInfo(
            "hti0_Priority",
            "Hitbox0Priority",
            False,
            int,
            "Priority of hitbox (slot 0). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used.", 
        ),
        ParamFieldInfo(
            "hti1_Priority",
            "Hitbox1Priority",
            False,
            int,
            "Priority of hitbox (slot 1). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used.", 
        ),
        ParamFieldInfo(
            "hti2_Priority",
            "Hitbox2Priority",
            False,
            int,
            "Priority of hitbox (slot 2). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used.", 
        ),
        ParamFieldInfo(
            "hti3_Priority",
            "Hitbox3Priority",
            False,
            int,
            "Priority of hitbox (slot 3). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used.", 
        ),
        ParamFieldInfo(
            "dmgLevel",
            "ImpactLevel",
            True,
            ATKPARAM_REP_DMGTYPE,
            "Impact level of attack, which determines how the target reacts to it (e.g. knocked backward, "
            "launched into the air, etc.). Certain special effects on the target (e.g. Iron Flesh) may re-map "
            "this impact level to a different one.", 
        ),
        ParamFieldInfo(
            "mapHitType",
            "MapHitType",
            True,
            ATK_PARAM_MAP_HIT,
            "Determines how this attack interacts with the map.",
        ),
        ParamFieldInfo(
            "guardCutCancelRate",
            "IgnoreGuardPercentage",
            False,
            int,
            "Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
            "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, "
            "in favor of the simple 'IgnoreGuard' boolean field.", 
        ),
        ParamFieldInfo(
            "atkAttribute",
            "AttackAttribute",
            True,
            ATKPARAM_ATKATTR_TYPE,
            "Type of physical damage done by attack.",
        ),
        ParamFieldInfo(
            "spAttribute",
            "ElementAttribute",
            True,
            ATKPARAM_SPATTR_TYPE,
            "Type of elemental damage done by attack. (Attacks can apply any combination of damage types, "
            "but this value will determine what visual effects the attack generates, etc.)", 
        ),
        ParamFieldInfo(
            "atkType",
            "VisualSoundEffectsOnAttack",
            True,
            ATK_TYPE,
            "Determines the sounds and visual effects generated by the attack itself (before hit).",
        ),
        ParamFieldInfo(
            "atkMaterial",
            "VisualSoundEffectsOnHit",
            True,
            WEP_MATERIAL_ATK,
            "Determines the sounds and visual effects generated when the attack hits. A value of 255 uses the "
            "weapon default.", 
        ),
        ParamFieldInfo(
            "atkSize",
            "AttackSize",
            False,
            BEHAVIOR_ATK_SIZE,
            "Internal description says this determines the size of sounds and visual effects, but it is never "
            "used.",
        ),
        ParamFieldInfo(
            "defMaterial",
            "SoundEffectsWhileBlocking",
            True,
            WEP_MATERIAL_DEF,
            "Determines the sound effects used when guarding. Usually 255 for Player Attacks and 0 (if not a "
            "block) or 50 (if blocking) for Non-Player Attacks.", 
        ),
        ParamFieldInfo(
            "defSfxMaterial",
            "VisualEffectsWhileBlocking",
            True,
            WEP_MATERIAL_DEF_SFX,
            "Determines the visual effects used when guarding. Usually 255 for Player Attacks and 0 (if not a "
            "block) or 50 (if blocking) for Non-Player Attacks.", 
        ),
        ParamFieldInfo(
            "hitSourceType",
            "ModelPointSource",
            True,
            ATK_PARAM_HIT_SOURCE,
            "Internal description says 'specify where you get the model point for attack'. Set to 1 for parries, "
            "ripostes, and basic body attacks (falling, rolling, etc.), and zero otherwise. Use that pattern.", 
        ),
        ParamFieldInfo(
            "throwFlag",
            "ThrowFlag",
            True,
            ATK_PATAM_THROWFLAG_TYPE,
            "Determines how this attack relates to throws: not at all, a throw trigger, or a throw damage "
            "parameter.", 
        ),
        ParamFieldInfo(
            "disableGuard:1", "IgnoreGuard", True, bool, "If True, this attack cannot be blocked (e.g. throws)."
        ),
        ParamFieldInfo(
            "disableStaminaAttack:1",
            "NoStaminaDamage",
            True,
            bool,
            "If True, this attack will deal no stamina damage, regardless of its stamina attack power.",
        ),
        ParamFieldInfo(
            "disableHitSpEffect:1",
            "NoSpecialEffects",
            True,
            bool,
            "If True, this attack will trigger no special effects on the target. Internal description mentions "
            "this is an 'SCE bug countermeasure' (referring to the original Dark Souls demo).", 
        ),
        ParamFieldInfo(
            "IgnoreNotifyMissSwingForAI:1",
            "NoMissNotificationForAI",
            True,
            bool,
            "If True, the character's AI will not be informed when this attack misses. Enabled for basic body "
            "attacks (falling, rolling, ladder punches, etc.) that are generally not considered to be serious "
            "attacks.", 
        ),
        ParamFieldInfo(
            "repeatHitSfx:1",
            "RepeatHitSoundEffects",
            False,
            bool,
            "If True, sound effects will supposedly be repeated as long as the attack continuously hits a wall. "
            "Never enabled, which is probably a good thing.", 
        ),
        ParamFieldInfo(
            "isArrowAtk:1",
            "IsPhysicalProjectile",
            True,
            bool,
            "Flags if this is the attack damage parameter of a physical projectile (arrow, bolt, or throwing "
            "knife).", 
        ),
        ParamFieldInfo(
            "isGhostAtk:1",
            "IsAttackByGhost",
            True,
            bool,
            "Flags if this is an attack of a ghost, which presumably disables wall collision, etc.",
        ),
        ParamFieldInfo(
            "isDisableNoDamage:1",
            "IgnoreInvincibilityFrames",
            True,
            bool,
            "If True, this attack will ignore invincibility frames from rolling or backstepping (but not other "
            "sources of invincibility such as TAE or events).", 
        ),
        ParamFieldInfo("atkPow_forSfxSe", "AttackPowerForEffects", True, int, ""),
        ParamFieldInfo("atkDir_forSfxSe", "AttackDirectionForEffects", True, int, "Name might be wrong."),
        ParamFieldInfo("opposeTarget:1", "AffectsEnemies", True, bool, ""),
        ParamFieldInfo("friendlyTarget:1", "AffectsAllies", True, bool, ""),
        ParamFieldInfo("selfTarget:1", "AffectsSelf", True, bool, ""),
        ParamFieldInfo("isChargeAtk:1", "IsChargeAttack", True, bool, ""),
        ParamFieldInfo("isShareHitList:1", "SharesHitList", True, bool, ""),
        ParamFieldInfo("isCheckObjPenetration:1", "CollidesWithObjects", True, bool, "Value might be inverted."),
        ParamFieldInfo("pad:2", "Pad", False, bit_pad_field(2), "Null padding."),
        ParamFieldInfo("pad2", "Pad", False, pad_field(2), "Null padding."),
        ParamFieldInfo("regainableSlotId", "RegainableSlotID", True, int, ""),
        ParamFieldInfo("deathcauseId", "DeathCauseID", True, int, ""),
        ParamFieldInfo("decalId1", "DecalID1", True, int, ""),
        ParamFieldInfo("decalId2", "DecalID2", True, int, ""),
        ParamFieldInfo("appearAiSoundId", "AppearAISoundID", True, int, ""),
        ParamFieldInfo("hitAiSoundId", "HitAISoundID", True, int, ""),
        ParamFieldInfo("wepRegainHpScale", "WeaponRegainHPScale", True, int, ""),
        ParamFieldInfo("atkRegainHp", "AttackRegainHP", True, int, ""),
        ParamFieldInfo("regainableTimeScale", "RegainTimeScale", True, int, ""),
        ParamFieldInfo("regainableHpRateScale", "RegainHPRateScale", True, int, ""),
    ],
}


THROW_INFO_BANK = {
    "param_type": "THROW_INFO_BANK",
    "file_name": "ThrowParam",
    "nickname": "Throws",
    "fields": [
        ParamFieldInfo("AtkChrId", "AttackingCharacterModel", True, int, "Model ID of attacking character."),
        ParamFieldInfo("DefChrId", "DefendingCharacterModel", True, int, "Model ID of defending character."),
        ParamFieldInfo("Dist", "MaxDistance", True, float, "Maximum distance at which throw can be triggered."),
        ParamFieldInfo(
            "DiffAngMin",
            "MinDifferenceInFacingAngle",
            True,
            float,
            "Minimum angular difference between attacker's facing direction and defender's facing direction.",
        ),
        ParamFieldInfo(
            "DiffAngMax",
            "MaxDifferenceInFacingAngle",
            True,
            float,
            "Maximum angular difference between attacker's facing direction and defender's facing direction.",
        ),
        ParamFieldInfo(
            "upperYRange", "MaxDistanceAbove", True, float, "Maximum distance that defender can be above attacker."
        ),
        ParamFieldInfo(
            "lowerYRange", "MaxDistanceBelow", True, float, "Maximum distance that defender can be below attacker."
        ),
        ParamFieldInfo(
            "diffAngMyToDef",
            "MaxAngleToDefender",
            True,
            float,
            "Maximum angular difference between attacker's direction and the direction of the defender.",
        ),
        ParamFieldInfo(
            "throwTypeId", "ThrowID", True, int, "Throw ID that should be specified in Attacks to use this throw."
        ),
        ParamFieldInfo(
            "atkAnimId",
            "AttackerAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by attacker during throw.",
        ),
        ParamFieldInfo(
            "defAnimId",
            "DefenderAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by defender during throw.",
        ),
        ParamFieldInfo(
            "escHp",
            "MinHPPercentageForEscape",
            True,
            int,
            "Minimum HP percentage required to escape the throw early by mashing buttons. (Not sure if 0 prevents "
            "any escape, or if escapes are disabled by another parameter like ",
        ),
        ParamFieldInfo(
            "selfEscCycleTime",
            "EscapeCycleTime",
            True,
            int,
            "Time of escape cycle, in milliseconds. Not sure exactly what it does. Set to 100 milliseconds for "
            "throws that can be escaped, and zero otherwise.",
        ),
        ParamFieldInfo(
            "sphereCastRadiusRateTop",
            "SphereCastUpperRadiusRatio",
            True,
            int,
            "Determines size of upper hemisphere of spherecast. I believe this is a percentage relative to the "
            "model size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's "
            "model size.",
        ),
        ParamFieldInfo(
            "sphereCastRadiusRateLow",
            "SphereCastLowerRadiusRatio",
            True,
            int,
            "Determines size of lower hemisphere of spherecast. I believe this is a percentage relative to the "
            "model size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's "
            "model size.",
        ),
        ParamFieldInfo(
            "PadType",
            "ButtonMashType",
            True,
            THROW_PAD_TYPE,
            "Determines buttons that can be mashed to escape. Enumeration is unknown, but it is set to 3 for the "
            "Centipede Demon grab, Male Ghost grab, and Dark Hand grab, and 1 for every other throw.",
        ),
        ParamFieldInfo(
            "AtkEnableState",
            "AttackEnabled",
            False,
            THROW_ENABLE_STATE,
            "Internal description says 'Set the throwable throwable state type' (?). Set to 1 for all player "
            "backstabs and ripostes, and 0 otherwise (including player plunging attacks and all enemy throws).",
        ),
        ParamFieldInfo(
            "atkSorbDmyId",
            "SnapToAttackerModelPoint",
            True,
            int,
            "Model point ID on attacker that defender will be snapped to. If this is zero, 'Snap To Defender "
            "Model Point' should be non-zero, and vice versa.",
        ),
        ParamFieldInfo(
            "defSorbDmyId",
            "SnapToDefenderModelPoint",
            True,
            int,
            "Model point ID on defender that attacker will be snapped to. If this is zero, 'Snap To Attacker "
            "Model Point' should be non-zero, and vice versa.",
        ),
        ParamFieldInfo(
            "throwType",
            "ThrowType",
            True,
            THROW_TYPE,
            "Type of throw. Not sure what uses this, but it could affect various things.",
        ),
        ParamFieldInfo(
            "selfEscCycleCnt",
            "EscapeCycleCount",
            True,
            int,
            "Internal description says 'number of self-throwing cycles'. Always set to 1 when EscapeCycleTime is "
            "set to 100 (and MinHPPercentageForEscape is almost always 25). Not sure how it determines *when* you "
            "can escape the throw.",
        ),
        ParamFieldInfo(
            "dmyHasChrDirType",
            "ModelPointCharacterDirectionType",
            False,
            THROW_DMY_CHR_DIR_TYPE,
            "'Direction of model point possessed character when thrown'. Set to 1 for the Armored Tusk backstab, "
            "255 for the Iron Golem and Gaping Dragon grabs, and 0 otherwise.",
        ),
        ParamFieldInfo(
            "isTurnAtker:1",
            "AttackerTurns",
            True,
            bool,
            "Attacker will turn when throw begins (presumably before model point snapping occurs).",
        ),
        ParamFieldInfo(
            "isSkipWepCate:1",
            "SkipAttackerWeaponCategoryCheck",
            True,
            bool,
            "If True, the weapon category check for the attacker will be skipped. Enabled only for Dark Hand "
            "drain.",
        ),
        ParamFieldInfo(
            "isSkipSphereCast:1",
            "SkipSphereCast",
            True,
            bool,
            "If True, the sphere cast check will be skipped. Usually False, but True for the coffin stab, "
            "Armored Tusk backstab, and a few large enemy grabs. (Presumably, if False, the throw trigger relies "
            "on distance and character angles only and is generally easier to trigger.)",
        ),
        ParamFieldInfo("pad0:5", "Pad1", False, bit_pad_field(5), "Null padding."),
        ParamFieldInfo("pad1[4]", "Pad2", False, pad_field(4), "Null padding."),
    ],
}
