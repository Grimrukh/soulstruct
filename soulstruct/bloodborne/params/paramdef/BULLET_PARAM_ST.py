from __future__ import annotations

__all__ = ["BULLET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BULLET_PARAM_ST(ParamRow):
    BulletAttack: int = ParamField(
        int, "atkId_Bullet", game_type=AttackParam, default=-1,
        tooltip="Attack parameters for bullet impact. Only certain fields in the attack parameter are used. Could be "
                "directed to either PlayerAttacks table or NonPlayerAttacks table, depending on the bullet's owner. "
                "Set to 0 if bullet has no attack data (no damage).",
    )
    ProjectileVFX: int = ParamField(
        int, "sfxId_Bullet", game_type=VisualEffect, default=-1,
        tooltip="Visual effect ID for bullet projectile.",
    )
    ImpactVFX: int = ParamField(
        int, "sfxId_Hit", game_type=VisualEffect, default=-1,
        tooltip="Visual effect ID for bullet impact.",
    )
    FlickVFX: int = ParamField(
        int, "sfxId_Flick", game_type=VisualEffect, default=-1,
        tooltip="Visual effect ID for when bullet is blocked (I think). Used predominantly for arrows and throwing "
                "knives.",
    )
    LifeTime: float = ParamField(
        float, "life", default=-1.0,
        tooltip="Maximum time before bullet will disappear on its own. -1 means it will last indefinitely.",
    )
    AttenuationDistance: float = ParamField(
        float, "dist", default=0.0,
        tooltip="Distance at which attenuation of the projectile begins.",
    )
    LaunchInterval: float = ParamField(
        float, "shootInterval", default=0.0,
        tooltip="Time between emitted bullets. Does nothing for bullets that only shoot once and is generally left at "
                "zero for those bullets.",
    )
    GravityBeforeAttenuation: float = ParamField(
        float, "gravityInRange", default=0.0,
        tooltip="Downward acceleration of bullet. Rarely used.",
    )
    GravityAfterAttenuation: float = ParamField(
        float, "gravityOutRange", default=0.0,
        tooltip="Downward acceleration of bullet after it passes the attenuation distance.",
    )
    ClosestHomingDistance: float = ParamField(
        float, "hormingStopRange", default=0.0,
        tooltip="Bullet will stop homing if it is within this distance of its homing target. Use this to prevent "
                "homing bullets from being too oppressive.",
    )
    InitialSpeed: float = ParamField(
        float, "initVellocity", default=0.0,
        tooltip="Initial speed of bullet.",
    )
    AccelerationBeforeAttenuation: float = ParamField(
        float, "accelInRange", default=0.0,
        tooltip="Forward acceleration acting on bullet before it reaches the attenuation distance. Negative values "
                "will slow the bullet down.",
    )
    AccelerationAfterAttenuation: float = ParamField(
        float, "accelOutRange", default=0.0,
        tooltip="Forward acceleration acting on bullet after it passes the attenuation distance. Negative values will "
                "slow the bullet down.",
    )
    MaxSpeed: float = ParamField(
        float, "maxVellocity", default=0.0,
        tooltip="Maximum speed of bullet, regardless of acceleration.",
    )
    MinSpeed: float = ParamField(
        float, "minVellocity", default=0.0,
        tooltip="Minimum speed of bullet, regardless of acceleration.",
    )
    AccelerationTime: float = ParamField(
        float, "accelTime", default=0.0,
        tooltip="Time that acceleration is active after bullet creation.",
    )
    HomingStartDistance: float = ParamField(
        float, "homingBeginDist", default=0.0,
        tooltip="Distance from owner at which the bullet starts homing in on targets.",
    )
    InitialHitRadius: float = ParamField(
        float, "hitRadius", default=-1.0,
        tooltip="Initial hit radius of bullet projectile.",
    )
    FinalHitRadius: float = ParamField(
        float, "hitRadiusMax", default=-1.0,
        tooltip="Final hit radius of bullet projectile. Set to -1 if radius does not change, which is always coupled "
                "with a value of 0 for RadiusIncreaseDuration.",
    )
    RadiusIncreaseTime: float = ParamField(
        float, "spreadTime", default=0.0,
        tooltip="Time taken by bullet to transition from initial to final hit radius. Value of 0 are always coupled "
                "with values of -1 for RadiusIncreaseDuration. I'm not sure if this can actually decrease the hit "
                "radius if the final value is less than the initial value.",
    )
    ExpDelay: float = ParamField(
        float, "expDelay", default=0.0,
        tooltip="Delay between impact and 'explosion' (not sure if that refers to the visual effect and/or hitbox). "
                "Never used (always zero).",
    )
    HomingOffsetRange: float = ParamField(
        float, "hormingOffsetRange", default=0.0,
        tooltip="Internal description: 'When shooting, aim to shift each component of XYZ by this amount.' Nonzero "
                "only for Hydra blasts and Vagrant attacks.",
    )
    HitboxLifeTime: float = ParamField(
        float, "dmgHitRecordLifeTime", default=0.0,
        tooltip="Duration of bullet impact hitbox. A value of zero means it is disabled immediately after first "
                "impact.",
    )
    ExternalForce: float = ParamField(
        float, "externalForce", default=0.0,
        tooltip="Unknown. Used only for Gargoyle fire breath and Undead Dragon poison breath.",
    )
    OwnerSpecialEffect: int = ParamField(
        int, "spEffectIDForShooter", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to owner when bullet is created. (Unclear if it is applied repeatedly by "
                "repeating bullets.)",
    )
    BulletAI: int = ParamField(
        int, "autoSearchNPCThinkID", game_type=AIParam, default=0,
        tooltip="AI parameter ID for triggered floating bullets. Only used by Homing [Crystal] Soulmass (10000) and "
                "Pursuers (10001) in the vanilla game.",
    )
    BulletOnHit: int = ParamField(
        int, "HitBulletID", default=-1,
        tooltip="Bullet emitted on impact of this bullet. Used often for 'throw'/'landing' or 'parent'/'child' "
                "combinations, like a thrown Firebomb (bullet 110) triggering a fiery explosion (bullet 111). These "
                "can be chained together indefinitely (see White Dragon Breath, bullet 11500).",
    )
    HitSpecialEffect0: int = ParamField(
        int, "spEffectId0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 0)",
    )
    HitSpecialEffect1: int = ParamField(
        int, "spEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 1)",
    )
    HitSpecialEffect2: int = ParamField(
        int, "spEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 2)",
    )
    HitSpecialEffect3: int = ParamField(
        int, "spEffectId3", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 3)",
    )
    HitSpecialEffect4: int = ParamField(
        int, "spEffectId4", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 4)",
    )
    BulletCount: int = ParamField(
        ushort, "numShoot", default=0,
        tooltip="Number of bullets emitted at once.",
    )
    HomingAnglePerSecond: int = ParamField(
        short, "homingAngle", default=0,
        tooltip="Turning angle of homing bullet per second. Higher values are better for homing.",
    )
    AzimuthAngleStart: int = ParamField(
        short, "shootAngle", default=0,
        tooltip="Angle of first bullet in degrees around the vertical axis, relative to the forward direction.",
    )
    AzimuthAngleInterval: int = ParamField(
        short, "shootAngleInterval", default=0,
        tooltip="Angle from one bullet to the next around the vertical axis, beginning at the azimuth angle start.",
    )
    ElevationAngleInterval: int = ParamField(
        short, "shootAngleXInterval", default=0,
        tooltip="Angle between bullets in elevation.",
    )
    PhysicalDamageDamp: int = ParamField(
        sbyte, "damageDamp", default=0,
        tooltip="Percentage reduction in physical damage per second.",
    )
    MagicDamageDamp: int = ParamField(
        sbyte, "spelDamageDamp", default=0,
        tooltip="Percentage reduction in magic damage per second.",
    )
    FireDamageDamp: int = ParamField(
        sbyte, "fireDamageDamp", default=0,
        tooltip="Percentage reduction in fire damage per second.",
    )
    LightningDamageDamp: int = ParamField(
        sbyte, "thunderDamageDamp", default=0,
        tooltip="Percentage reduction in lightning damage per second.",
    )
    StaminaDamp: int = ParamField(
        sbyte, "staminaDamp", default=0,
        tooltip="Percentage reduction in stamina damage per second.",
    )
    KnockbackDamp: int = ParamField(
        sbyte, "knockbackDamp", default=0,
        tooltip="Percentage reduction in knockback power per second.",
    )
    FirstBulletElevationAngle: int = ParamField(
        sbyte, "shootAngleXZ", default=0,
        tooltip="Angle of elevation of first bullet. Positive values will angle the bullets up (e.g. Quelaag's "
                "fireballs) and negative values will angle the bullets down (e.g. most breath attacks).",
    )
    LockShootLimitAngle: int = ParamField(
        byte, "lockShootLimitAng", default=0,
        tooltip="Unknown, but likely important. Set to 30 for most basic projectile magic.",
    )
    PiercesTargets: int = ParamField(
        byte, "isPenetrate", default=0,
        tooltip="Bullet will go through objects, players, and NPCs.",
    )
    PreviousDirectionRatio: int = ParamField(
        byte, "prevVelocityDirRate", default=0,
        tooltip="Internal description: 'Ratio of adding the previous moving direction to the current direction when a "
                "sliding bullet hits the wall.' Like ExternalForce, this is used only for Gargoyle and Undead Dragon "
                "breath (100) and is zero for everything else.",
    )
    AttackAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="Attack type. Almost always 4 ('other'), but sometimes 3 (knives/arrows/bolts).",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="Element attached to bullet hit.",
    )
    MaterialAttackType: int = ParamField(
        byte, "Material_AttackType", ATK_TYPE, default=0,
        tooltip="Determines visual effects of bullet hit.",
    )
    EffectsOnHit: int = ParamField(
        byte, "Material_AttackMaterial", WEP_MATERIAL_ATK, default=0,
        tooltip="Sound and visual effects on hit.",
    )
    MaterialSize: int = ParamField(
        byte, "Material_Size", ATK_SIZE, default=0,
        tooltip="'Size' of attack. Never used.'",
    )
    LaunchConditionType: int = ParamField(
        byte, "launchConditionType", BULLET_LAUNCH_CONDITION_TYPE, default=0,
        tooltip="Condition for determing if a new bullet will be generated when this bullet lands or expires.",
    )
    FollowType: int = ParamField(
        byte, "FollowType:3", BULLET_FOLLOW_TYPE, bit_count=3, default=0,
        tooltip="Follow type.",
    )
    OriginType: int = ParamField(
        byte, "EmittePosType:3", BULLET_EMITTE_POS_TYPE, bit_count=3, default=0,
        tooltip="Origin type of bullet. Usually comes from model points ('damipoly').",
    )
    RemainAttachedToTarget: bool = ParamField(
        byte, "isAttackSFX:1", ON_OFF, bit_count=1, default=False,
        tooltip="Set whether bullets (e.g. arrows) stay stuck upon impact.",
    )
    IsEndlessHit: bool = ParamField(
        byte, "isEndlessHit:1", ON_OFF, bit_count=1, default=False,
        tooltip="Bullet hitbox is continuous (I think). Only used for corrosion cloud in vanilla.",
    )
    IsMapPiercing: bool = ParamField(
        byte, "isPenetrateMap:1", ON_OFF, bit_count=1, default=False,
        tooltip="Bullet will pierce the map (e.g. Stray Demon blast).",
    )
    HitsBothTeams: bool = ParamField(
        byte, "isHitBothTeam:1", ON_OFF, bit_count=1, default=False,
        tooltip="Bullet can hit any character.",
    )
    SharedHitCheck: bool = ParamField(
        byte, "isUseSharedHitList:1", ON_OFF, bit_count=1, default=False,
        tooltip="Repeating bullets share the amount of times they have hit a target (usually so the target is only "
                "hit once by any of those repeating bullets).",
    )
    UsesMultipleModelPoints: bool = ParamField(
        byte, "isUseMultiDmyPolyIfPlace:1", ON_OFF, bit_count=1, default=False,
        tooltip="Set to True if the same model point ('damipoly') is used multiple times when spawning the bullet.",
    )
    AttachEffectType: int = ParamField(
        byte, "attachEffectType:2", BULLET_ATTACH_EFFECT_TYPE, bit_count=2, default=0,
        tooltip="Mostly 0, but sometimes 1 (Dragon Head breath, Grant AoE, Force miracles).",
    )
    CanBeDeflectedByMagic: bool = ParamField(
        byte, "isHitForceMagic:1", bit_count=1, default=False,
        tooltip="If True, this bullet will impact appropriate Force-type magic (e.g. arrows, bolts, knives).",
    )
    IgnoreVFXOnWaterHit: bool = ParamField(
        byte, "isIgnoreSfxIfHitWater:1", bit_count=1, default=False,
        tooltip="If True, hit VFX are not produced if the bullet impacts water.",
    )
    IgnoreStateTransitionOnWaterHit: bool = ParamField(
        byte, "isIgnoreMoveStateIfHitWater:1", bit_count=1, default=False,
        tooltip="Unclear effect, but True for knives/arrows/bolts and False otherwise.",
    )
    CanBeDeflectedByBeastRoar: bool = ParamField(
        byte, "isHitDarkForceMagic:1", bit_count=1, default=False,
        tooltip="If True, this bullet will impact the Beast Roar deflection effect.",
    )
    ChildrenInheritEffect: bool = ParamField(
        byte, "isInheritEffectToChild:1", BULLET_PARAM_CIRCLE_CROSS_TYPE, bit_count=1, default=False,
        tooltip="TODO",
    )
    ChildrenInheritSpeed: bool = ParamField(
        byte, "isInheritSpeedToChild:1", BULLET_PARAM_CIRCLE_CROSS_TYPE, bit_count=1, default=False,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad[3]")
