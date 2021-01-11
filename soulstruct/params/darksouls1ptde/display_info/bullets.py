__all__ = ["BULLET_PARAM_ST"]

from soulstruct.params.core import FieldDisplayInfo, pad_field
from soulstruct.params.darksouls1ptde.enums import *
from soulstruct.game_types.param_types import *


BULLET_PARAM_ST = {
    "paramdef_name": "BULLET_PARAM_ST",
    "file_name": "Bullet",  # rare case in which file name does not end in "Param"
    "nickname": "Bullets",
    "fields": [
        FieldDisplayInfo(
            "atkId_Bullet",
            "BulletAttack",
            True,
            AttackParam,
            "Attack parameters for bullet impact. Only certain fields in the attack parameter are used. Could be "
            "directed to either PlayerAttacks table or NonPlayerAttacks table, depending on the bullet's owner. "
            "Set to 0 if bullet has no attack data (no damage).",
        ),
        FieldDisplayInfo("sfxId_Bullet", "ProjectileVFX", True, int, "Visual effect ID for bullet projectile."),
        FieldDisplayInfo("sfxId_Hit", "ImpactVFX", True, int, "Visual effect ID for bullet impact."),
        FieldDisplayInfo(
            "sfxId_Flick",
            "FlickVFX",
            True,
            int,
            "Visual effect ID for when bullet is blocked (I think). Used predominantly for arrows and throwing "
            "knives.",
        ),
        FieldDisplayInfo(
            "life",
            "LifeTime",
            True,
            float,
            "Maximum time before bullet will disappear on its own. -1 means it will last indefinitely.",
        ),
        FieldDisplayInfo(
            "dist", "AttenuationDistance", True, float, "Distance at which attenuation of the projectile begins."
        ),
        FieldDisplayInfo(
            "shootInterval",
            "LaunchInterval",
            True,
            float,
            "Time between emitted bullets. Does nothing for bullets that only shoot once and is generally left at "
            "zero for those bullets.",
        ),
        FieldDisplayInfo(
            "gravityInRange",
            "GravityBeforeAttenuation",
            True,
            float,
            "Downward acceleration of bullet. Rarely used.",
        ),
        FieldDisplayInfo(
            "gravityOutRange",
            "GravityAfterAttenuation",
            True,
            float,
            "Downward acceleration of bullet after it passes the attenuation distance.",
        ),
        FieldDisplayInfo(
            "hormingStopRange",
            "ClosestHomingDistance",
            True,
            float,
            "Bullet will stop homing if it is within this distance of its homing target. Use this to prevent "
            "homing bullets from being too oppressive.",
        ),
        FieldDisplayInfo("initVellocity", "InitialSpeed", True, float, "Initial speed of bullet."),
        FieldDisplayInfo(
            "accelInRange",
            "AccelerationBeforeAttenuation",
            True,
            float,
            "Forward acceleration acting on bullet before it reaches the attenuation distance. Negative values "
            "will slow the bullet down.",
        ),
        FieldDisplayInfo(
            "accelOutRange",
            "AccelerationAfterAttenuation",
            True,
            float,
            "Forward acceleration acting on bullet after it passes the attenuation distance. Negative values will "
            "slow the bullet down.",
        ),
        FieldDisplayInfo("maxVellocity", "MaxSpeed", True, float, "Maximum speed of bullet, regardless of acceleration."),
        FieldDisplayInfo("minVellocity", "MinSpeed", True, float, "Minimum speed of bullet, regardless of acceleration."),
        FieldDisplayInfo(
            "accelTime", "AccelerationTime", True, float, "Time that acceleration is active after bullet creation."
        ),
        FieldDisplayInfo(
            "homingBeginDist",
            "HomingStartDistance",
            True,
            float,
            "Distance from owner at which the bullet starts homing in on targets.",
        ),
        FieldDisplayInfo("hitRadius", "InitialHitRadius", True, float, "Initial hit radius of bullet projectile."),
        FieldDisplayInfo(
            "hitRadiusMax",
            "FinalHitRadius",
            True,
            float,
            "Final hit radius of bullet projectile. Set to -1 if radius does not change, which is always coupled "
            "with a value of 0 for RadiusIncreaseDuration.",
        ),
        FieldDisplayInfo(
            "spreadTime",
            "RadiusIncreaseTime",
            True,
            float,
            "Time taken by bullet to transition from initial to final hit radius. Value of 0 are always coupled "
            "with values of -1 for RadiusIncreaseDuration. I'm not sure if this can actually decrease the hit "
            "radius if the final value is less than the initial value.",
        ),
        FieldDisplayInfo(
            "expDelay",
            "ExpDelay",
            False,
            float,
            "Delay between impact and 'explosion' (not sure if that refers to the visual effect and/or hitbox). "
            "Never used (always zero).",
        ),
        FieldDisplayInfo(
            "hormingOffsetRange",
            "HomingOffsetRange",
            True,
            float,
            "Internal description: 'When shooting, aim to shift each component of XYZ by this amount.' Nonzero "
            "only for Hydra blasts and Vagrant attacks.",
        ),
        FieldDisplayInfo(
            "dmgHitRecordLifeTime",
            "HitboxLifeTime",
            True,
            float,
            "Duration of bullet impact hitbox. A value of zero means it is disabled immediately after first "
            "impact.",
        ),
        FieldDisplayInfo(
            "externalForce",
            "ExternalForce",
            True,
            float,
            "Unknown. Used only for Gargoyle fire breath and Undead Dragon poison breath.",
        ),
        FieldDisplayInfo(
            "spEffectIDForShooter",
            "OwnerSpecialEffect",
            True,
            SpecialEffectParam,
            "Special effect applied to owner when bullet is created. (Unclear if it is applied repeatedly by "
            "repeating bullets.)",
        ),
        FieldDisplayInfo(
            "autoSearchNPCThinkID",
            "BulletAI",
            True,
            AIParam,
            "AI parameter ID for triggered floating bullets. Only used by Homing [Crystal] Soulmass (10000) and "
            "Pursuers (10001) in the vanilla game.",
        ),
        FieldDisplayInfo(
            "HitBulletID",
            "BulletOnHit",
            True,
            BulletParam,
            "Bullet emitted on impact of this bullet. Used often for 'throw'/'landing' or 'parent'/'child' "
            "combinations, like a thrown Firebomb (bullet 110) triggering a fiery explosion (bullet 111). These "
            "can be chained together indefinitely (see White Dragon Breath, bullet 11500).",
        ),
        FieldDisplayInfo(
            "spEffectId0",
            "HitSpecialEffect0",
            True,
            SpecialEffectParam,
            "Special effect applied to target hit by bullet. (Slot 0)",
        ),
        FieldDisplayInfo(
            "spEffectId1",
            "HitSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect applied to target hit by bullet. (Slot 1)",
        ),
        FieldDisplayInfo(
            "spEffectId2",
            "HitSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect applied to target hit by bullet. (Slot 2)",
        ),
        FieldDisplayInfo(
            "spEffectId3",
            "HitSpecialEffect3",
            True,
            SpecialEffectParam,
            "Special effect applied to target hit by bullet. (Slot 3)",
        ),
        FieldDisplayInfo(
            "spEffectId4",
            "HitSpecialEffect4",
            True,
            SpecialEffectParam,
            "Special effect applied to target hit by bullet. (Slot 4)",
        ),
        FieldDisplayInfo("numShoot", "BulletCount", True, int, "Number of bullets emitted at once."),
        FieldDisplayInfo(
            "homingAngle",
            "HomingAnglePerSecond",
            True,
            int,
            "Turning angle of homing bullet per second. Higher values are better for homing.",
        ),
        FieldDisplayInfo(
            "shootAngle",
            "AzimuthAngleStart",
            True,
            int,
            "Angle of first bullet in degrees around the vertical axis, relative to the forward direction.",
        ),
        FieldDisplayInfo(
            "shootAngleInterval",
            "AzimuthAngleInterval",
            True,
            int,
            "Angle from one bullet to the next around the vertical axis, beginning at the azimuth angle start.",
        ),
        FieldDisplayInfo(
            "shootAngleXInterval", "ElevationAngleInterval", True, int, "Angle between bullets in elevation."
        ),
        FieldDisplayInfo(
            "damageDamp", "PhysicalDamageDamp", True, int, "Percentage reduction in physical damage per second."
        ),
        FieldDisplayInfo(
            "spelDamageDamp", "MagicDamageDamp", True, int, "Percentage reduction in magic damage per second."
        ),
        FieldDisplayInfo("fireDamageDamp", "FireDamageDamp", True, int, "Percentage reduction in fire damage per second."),
        FieldDisplayInfo(
            "thunderDamageDamp",
            "LightningDamageDamp",
            True,
            int,
            "Percentage reduction in lightning damage per second.",
        ),
        FieldDisplayInfo("staminaDamp", "StaminaDamp", False, int, "Percentage reduction in stamina damage per second."),
        FieldDisplayInfo(
            "knockbackDamp", "KnockbackDamp", False, int, "Percentage reduction in knockback power per second."
        ),
        FieldDisplayInfo(
            "shootAngleXZ",
            "FirstBulletElevationAngle",
            True,
            int,
            "Angle of elevation of first bullet. Positive values will angle the bullets up (e.g. Quelaag's "
            "fireballs) and negative values will angle the bullets down (e.g. most breath attacks).",
        ),
        FieldDisplayInfo(
            "lockShootLimitAng",
            "LockShootLimitAngle",
            True,
            int,
            "Unknown, but likely important. Set to 30 for most basic projectile magic.",
        ),
        FieldDisplayInfo(
            "isPenetrate", "PiercesTargets", True, bool, "Bullet will go through objects, players, and NPCs."
        ),
        FieldDisplayInfo(
            "prevVelocityDirRate",
            "PreviousDirectionRatio",
            False,
            int,
            "Internal description: 'Ratio of adding the previous moving direction to the current direction when a "
            "sliding bullet hits the wall.' Like ExternalForce, this is used only for Gargoyle and Undead Dragon "
            "breath (100) and is zero for everything else.",
        ),
        FieldDisplayInfo(
            "atkAttribute",
            "AttackAttribute",
            True,
            ATKPARAM_ATKATTR_TYPE,
            "Attack type. Almost always 4 ('other'), but sometimes 3 (knives/arrows/bolts).",
        ),
        FieldDisplayInfo("spAttribute", "ElementAttribute", True, ATKPARAM_SPATTR_TYPE, "Element attached to bullet hit."),
        FieldDisplayInfo(
            "Material_AttackType", "MaterialAttackType", True, ATK_TYPE, "Determines visual effects of bullet hit."
        ),
        FieldDisplayInfo(
            "Material_AttackMaterial", "EffectsOnHit", True, WEP_MATERIAL_ATK, "Sound and visual effects on hit."
        ),
        FieldDisplayInfo("Material_Size", "MaterialSize", False, ATK_SIZE, "'Size' of attack. Never used.'"),
        FieldDisplayInfo(
            "launchConditionType",
            "LaunchConditionType",
            True,
            BULLET_LAUNCH_CONDITION_TYPE,
            "Condition for determing if a new bullet will be generated when this bullet lands or expires.",
        ),
        FieldDisplayInfo("FollowType:3", "FollowType", True, BULLET_FOLLOW_TYPE, "Follow type."),
        FieldDisplayInfo(
            "EmittePosType:3",
            "OriginType",
            True,
            BULLET_EMITTE_POS_TYPE,
            "Origin type of bullet. Usually comes from model points ('damipoly').",
        ),
        FieldDisplayInfo(
            "isAttackSFX:1",
            "RemainAttachedToTarget",
            True,
            bool,
            "Set whether bullets (e.g. arrows) stay stuck upon impact.",
        ),
        FieldDisplayInfo(
            "isEndlessHit:1",
            "IsEndlessHit",
            True,
            bool,
            "Bullet hitbox is continuous (I think). Only used for corrosion cloud in vanilla.",
        ),
        FieldDisplayInfo(
            "isPenetrateMap:1", "IsMapPiercing", True, bool, "Bullet will pierce the map (e.g. Stray Demon blast)."
        ),
        FieldDisplayInfo("isHitBothTeam:1", "HitsBothTeams", True, bool, "Bullet can hit any character."),
        FieldDisplayInfo(
            "isUseSharedHitList:1",
            "SharedHitCheck",
            True,
            bool,
            "Repeating bullets share the amount of times they have hit a target (usually so the target is only "
            "hit once by any of those repeating bullets).",
        ),
        FieldDisplayInfo(
            "isUseMultiDmyPolyIfPlace:1",
            "UsesMultipleModelPoints",
            True,
            bool,
            "Set to True if the same model point ('damipoly') is used multiple times when spawning the bullet.",
        ),
        FieldDisplayInfo(
            "attachEffectType:2",
            "AttachEffectType",
            False,
            BULLET_ATTACH_EFFECT_TYPE,
            "Mostly 0, but sometimes 1 (Dragon Head breath, Grant AoE, Force miracles).",
        ),
        FieldDisplayInfo(
            "isHitForceMagic:1",
            "CanBeDeflectedByMagic",
            True,
            bool,
            "If True, this bullet will impact appropriate Force-type magic (e.g. arrows, bolts, knives).",
        ),
        FieldDisplayInfo(
            "isIgnoreSfxIfHitWater:1",
            "IgnoreVFXOnWaterHit",
            True,
            bool,
            "If True, hit VFX are not produced if the bullet impacts water.",
        ),
        FieldDisplayInfo(
            "isIgnoreMoveStateIfHitWater:1",
            "IgnoreStateTransitionOnWaterHit",
            True,
            bool,
            "Unclear effect, but True for knives/arrows/bolts and False otherwise.",
        ),
        FieldDisplayInfo(
            "isHitDarkForceMagic:1",
            "CanBeDeflectedBySilverPendant",
            True,
            bool,
            "If True, this bullet will impact the Silver Pendant shield effect. True only for dark sorceries.",
        ),
        FieldDisplayInfo("pad[3]", "Pad3", False, pad_field(3), "Null padding."),
    ],
}
