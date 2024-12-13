from __future__ import annotations

__all__ = ["BULLET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


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
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    PreviousDirectionRatio: int = ParamField(
        byte, "prevVelocityDirRate", default=0,
        tooltip="Internal description: 'Ratio of adding the previous moving direction to the current direction when a "
                "sliding bullet hits the wall.' Like ExternalForce, this is used only for Gargoyle and Undead Dragon "
                "breath (100) and is zero for everything else.",
    )
    AttackAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=254,
        tooltip="Attack type. Almost always 4 ('other'), but sometimes 3 (knives/arrows/bolts).",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=254,
        tooltip="Element attached to bullet hit.",
    )
    MaterialAttackType: int = ParamField(
        byte, "Material_AttackType", BEHAVIOR_ATK_TYPE, default=254,
        tooltip="Determines visual effects of bullet hit.",
    )
    EffectsOnHit: int = ParamField(
        byte, "Material_AttackMaterial", WEP_MATERIAL_ATK, default=254,
        tooltip="Sound and visual effects on hit.",
    )
    IsPenetrateChr: bool = ParamField(
        byte, "isPenetrateChr:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsPenetrateObj: bool = ParamField(
        byte, "isPenetrateObj:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad:6", bit_count=6)
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
    IsHitOtherBulletForceEraseA: bool = ParamField(
        byte, "isHitOtherBulletForceEraseA:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitOtherBulletForceEraseB: bool = ParamField(
        byte, "isHitOtherBulletForceEraseB:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
    DmgCalcSide: int = ParamField(
        byte, "dmgCalcSide:2", DMG_CALC_SIDE_TYPE, bit_count=2, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableAutoHoming: bool = ParamField(
        byte, "isEnableAutoHoming:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSyncBulletCulcDumypolyPos: bool = ParamField(
        byte, "isSyncBulletCulcDumypolyPos:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsOwnerOverrideInitAngle: bool = ParamField(
        byte, "isOwnerOverrideInitAngle:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInheritSfxToChild: bool = ParamField(
        byte, "isInheritSfxToChild:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageDamp: int = ParamField(
        sbyte, "darkDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyHit: int = ParamField(
        sbyte, "bulletSfxDeleteType_byHit", BULLET_SFX_DELETE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyLifeDead: int = ParamField(
        sbyte, "bulletSfxDeleteType_byLifeDead", BULLET_SFX_DELETE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TargetYOffsetRange: float = ParamField(
        float, "targetYOffsetRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShootAngleYMaxRandom: float = ParamField(
        float, "shootAngleYMaxRandom", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShootAngleXMaxRandom: float = ParamField(
        float, "shootAngleXMaxRandom", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateBulletId: int = ParamField(
        int, "intervalCreateBulletId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateTimeMin: float = ParamField(
        float, "intervalCreateTimeMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateTimeMax: float = ParamField(
        float, "intervalCreateTimeMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PredictionShootObserveTime: float = ParamField(
        float, "predictionShootObserveTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateWaitTime: float = ParamField(
        float, "intervalCreateWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SfxPostureType: int = ParamField(
        byte, "sfxPostureType", BULLET_SFX_CREATE_POSTURE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateLimitGroupId: int = ParamField(
        byte, "createLimitGroupId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad5[1]")
    ChildrenInheritSpeed: bool = ParamField(
        byte, "isInheritSpeedToChild:1", ON_OFF, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsDisableHitSfxbyChrAndObj: bool = ParamField(
        byte, "isDisableHitSfx_byChrAndObj:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckWallbyCenterRay: bool = ParamField(
        byte, "isCheckWall_byCenterRay:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitFlare: bool = ParamField(
        byte, "isHitFlare:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseBulletWallFilter: bool = ParamField(
        byte, "isUseBulletWallFilter:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad1:1", bit_count=1)
    IsNonDependenceMagicForFunnleNum: bool = ParamField(
        byte, "isNonDependenceMagicForFunnleNum:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAiInterruptShootNoDamageBullet: bool = ParamField(
        byte, "isAiInterruptShootNoDamageBullet:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RandomCreateRadius: float = ParamField(
        float, "randomCreateRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FollowOffsetBaseHeight: float = ParamField(
        float, "followOffset_BaseHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AssetNoHit: int = ParamField(
        int, "assetNo_Hit", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LifeRandomRange: float = ParamField(
        float, "lifeRandomRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HomingAngleX: int = ParamField(
        short, "homingAngleX", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BallisticCalcType: int = ParamField(
        byte, "ballisticCalcType", BULLET_BALLISTIC_CALC_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttachEffectType: int = ParamField(
        byte, "attachEffectType", BULLET_ATTACH_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SeIdBullet1: int = ParamField(
        int, "seId_Bullet1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeIdBullet2: int = ParamField(
        int, "seId_Bullet2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeIdHit: int = ParamField(
        int, "seId_Hit", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeIdFlick: int = ParamField(
        int, "seId_Flick", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerShootAngleXMin: int = ParamField(
        short, "howitzerShootAngleXMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerShootAngleXMax: int = ParamField(
        short, "howitzerShootAngleXMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerInitMinVelocity: float = ParamField(
        float, "howitzerInitMinVelocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerInitMaxVelocity: float = ParamField(
        float, "howitzerInitMaxVelocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdForceErase: int = ParamField(
        int, "sfxId_ForceErase", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyForceErase: int = ParamField(
        sbyte, "bulletSfxDeleteType_byForceErase", BULLET_SFX_DELETE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad3[1]")
    FollowDmypolyforSfxPose: int = ParamField(
        short, "followDmypoly_forSfxPose", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FollowOffsetRadius: float = ParamField(
        float, "followOffset_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpBulletDistUpRate: float = ParamField(
        float, "spBulletDistUpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NolockTargetDist: float = ParamField(
        float, "nolockTargetDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad4[8]")
