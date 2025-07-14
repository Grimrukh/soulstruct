from __future__ import annotations

__all__ = ["BULLET_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class BULLET_PARAM_ST(ParamRow):
    BulletAttack: int = ParamField(
        int32, "atkId_Bullet", game_type=AttackParam, default=-1,
        tooltip="Attack parameters for bullet impact. Only certain fields in the attack parameter are used. Could be "
                "directed to either PlayerAttacks table or NonPlayerAttacks table, depending on the bullet's owner. "
                "Set to 0 if bullet has no attack data (no damage).",
    )
    ProjectileVFX: int = ParamField(
        int32, "sfxId_Bullet", game_type=VisualEffect, default=-1,
        tooltip="Visual effect ID for bullet projectile.",
    )
    ImpactVFX: int = ParamField(
        int32, "sfxId_Hit", game_type=VisualEffect, default=-1,
        tooltip="Visual effect ID for bullet impact.",
    )
    FlickVFX: int = ParamField(
        int32, "sfxId_Flick", game_type=VisualEffect, default=-1,
        tooltip="Visual effect ID for when bullet is blocked (I think). Used predominantly for arrows and throwing "
                "knives.",
    )
    LifeTime: float = ParamField(
        float32, "life", default=-1.0,
        tooltip="Maximum time before bullet will disappear on its own. -1 means it will last indefinitely.",
    )
    AttenuationDistance: float = ParamField(
        float32, "dist", default=0.0,
        tooltip="Distance at which attenuation of the projectile begins.",
    )
    LaunchInterval: float = ParamField(
        float32, "shootInterval", default=0.0,
        tooltip="Time between emitted bullets. Does nothing for bullets that only shoot once and is generally left at "
                "zero for those bullets.",
    )
    GravityBeforeAttenuation: float = ParamField(
        float32, "gravityInRange", default=0.0,
        tooltip="Downward acceleration of bullet. Rarely used.",
    )
    GravityAfterAttenuation: float = ParamField(
        float32, "gravityOutRange", default=0.0,
        tooltip="Downward acceleration of bullet after it passes the attenuation distance.",
    )
    ClosestHomingDistance: float = ParamField(
        float32, "hormingStopRange", default=0.0,
        tooltip="Bullet will stop homing if it is within this distance of its homing target. Use this to prevent "
                "homing bullets from being too oppressive.",
    )
    InitialSpeed: float = ParamField(
        float32, "initVellocity", default=0.0,
        tooltip="Initial speed of bullet.",
    )
    AccelerationBeforeAttenuation: float = ParamField(
        float32, "accelInRange", default=0.0,
        tooltip="Forward acceleration acting on bullet before it reaches the attenuation distance. Negative values "
                "will slow the bullet down.",
    )
    AccelerationAfterAttenuation: float = ParamField(
        float32, "accelOutRange", default=0.0,
        tooltip="Forward acceleration acting on bullet after it passes the attenuation distance. Negative values will "
                "slow the bullet down.",
    )
    MaxSpeed: float = ParamField(
        float32, "maxVellocity", default=0.0,
        tooltip="Maximum speed of bullet, regardless of acceleration.",
    )
    MinSpeed: float = ParamField(
        float32, "minVellocity", default=0.0,
        tooltip="Minimum speed of bullet, regardless of acceleration.",
    )
    AccelerationTime: float = ParamField(
        float32, "accelTime", default=0.0,
        tooltip="Time that acceleration is active after bullet creation.",
    )
    HomingStartDistance: float = ParamField(
        float32, "homingBeginDist", default=0.0,
        tooltip="Distance from owner at which the bullet starts homing in on targets.",
    )
    InitialHitRadius: float = ParamField(
        float32, "hitRadius", default=-1.0,
        tooltip="Initial hit radius of bullet projectile.",
    )
    FinalHitRadius: float = ParamField(
        float32, "hitRadiusMax", default=-1.0,
        tooltip="Final hit radius of bullet projectile. Set to -1 if radius does not change, which is always coupled "
                "with a value of 0 for RadiusIncreaseDuration.",
    )
    RadiusIncreaseTime: float = ParamField(
        float32, "spreadTime", default=0.0,
        tooltip="Time taken by bullet to transition from initial to final hit radius. Value of 0 are always coupled "
                "with values of -1 for RadiusIncreaseDuration. I'm not sure if this can actually decrease the hit "
                "radius if the final value is less than the initial value.",
    )
    ExpDelay: float = ParamField(
        float32, "expDelay", default=0.0,
        tooltip="Delay between impact and 'explosion' (not sure if that refers to the visual effect and/or hitbox). "
                "Never used (always zero).",
    )
    HomingOffsetRange: float = ParamField(
        float32, "hormingOffsetRange", default=0.0,
        tooltip="Internal description: 'When shooting, aim to shift each component of XYZ by this amount.' Nonzero "
                "only for Hydra blasts and Vagrant attacks.",
    )
    HitboxLifeTime: float = ParamField(
        float32, "dmgHitRecordLifeTime", default=0.0,
        tooltip="Duration of bullet impact hitbox. A value of zero means it is disabled immediately after first "
                "impact.",
    )
    ExternalForce: float = ParamField(
        float32, "externalForce", default=0.0,
        tooltip="Unknown. Used only for Gargoyle fire breath and Undead Dragon poison breath.",
    )
    OwnerSpecialEffect: int = ParamField(
        int32, "spEffectIDForShooter", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to owner when bullet is created. (Unclear if it is applied repeatedly by "
                "repeating bullets.)",
    )
    BulletAI: int = ParamField(
        int32, "autoSearchNPCThinkID", game_type=AIParam, default=0,
        tooltip="AI parameter ID for triggered floating bullets. Only used by Homing [Crystal] Soulmass (10000) and "
                "Pursuers (10001) in the vanilla game.",
    )
    BulletOnHit: int = ParamField(
        int32, "HitBulletID", default=-1,
        tooltip="Bullet emitted on impact of this bullet. Used often for 'throw'/'landing' or 'parent'/'child' "
                "combinations, like a thrown Firebomb (bullet 110) triggering a fiery explosion (bullet 111). These "
                "can be chained together indefinitely (see White Dragon Breath, bullet 11500).",
    )
    HitSpecialEffect0: int = ParamField(
        int32, "spEffectId0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 0)",
    )
    HitSpecialEffect1: int = ParamField(
        int32, "spEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 1)",
    )
    HitSpecialEffect2: int = ParamField(
        int32, "spEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 2)",
    )
    HitSpecialEffect3: int = ParamField(
        int32, "spEffectId3", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 3)",
    )
    HitSpecialEffect4: int = ParamField(
        int32, "spEffectId4", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to target hit by bullet. (Slot 4)",
    )
    BulletCount: int = ParamField(
        uint16, "numShoot", default=0,
        tooltip="Number of bullets emitted at once.",
    )
    HomingAnglePerSecond: int = ParamField(
        int16, "homingAngle", default=0,
        tooltip="Turning angle of homing bullet per second. Higher values are better for homing.",
    )
    AzimuthAngleStart: int = ParamField(
        int16, "shootAngle", default=0,
        tooltip="Angle of first bullet in degrees around the vertical axis, relative to the forward direction.",
    )
    AzimuthAngleInterval: int = ParamField(
        int16, "shootAngleInterval", default=0,
        tooltip="Angle from one bullet to the next around the vertical axis, beginning at the azimuth angle start.",
    )
    ElevationAngleInterval: int = ParamField(
        int16, "shootAngleXInterval", default=0,
        tooltip="Angle between bullets in elevation.",
    )
    PhysicalDamageDamp: int = ParamField(
        int8, "damageDamp", default=0,
        tooltip="Percentage reduction in physical damage per second.",
    )
    MagicDamageDamp: int = ParamField(
        int8, "spelDamageDamp", default=0,
        tooltip="Percentage reduction in magic damage per second.",
    )
    FireDamageDamp: int = ParamField(
        int8, "fireDamageDamp", default=0,
        tooltip="Percentage reduction in fire damage per second.",
    )
    LightningDamageDamp: int = ParamField(
        int8, "thunderDamageDamp", default=0,
        tooltip="Percentage reduction in lightning damage per second.",
    )
    StaminaDamp: int = ParamField(
        int8, "staminaDamp", default=0,
        tooltip="Percentage reduction in stamina damage per second.",
    )
    KnockbackDamp: int = ParamField(
        int8, "knockbackDamp", default=0,
        tooltip="Percentage reduction in knockback power per second.",
    )
    FirstBulletElevationAngle: int = ParamField(
        int8, "shootAngleXZ", default=0,
        tooltip="Angle of elevation of first bullet. Positive values will angle the bullets up (e.g. Quelaag's "
                "fireballs) and negative values will angle the bullets down (e.g. most breath attacks).",
    )
    LockShootLimitAngle: int = ParamField(
        uint8, "lockShootLimitAng", default=0,
        tooltip="Unknown, but likely important. Set to 30 for most basic projectile magic.",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    PreviousDirectionRatio: int = ParamField(
        uint8, "prevVelocityDirRate", default=0,
        tooltip="Internal description: 'Ratio of adding the previous moving direction to the current direction when a "
                "sliding bullet hits the wall.' Like ExternalForce, this is used only for Gargoyle and Undead Dragon "
                "breath (100) and is zero for everything else.",
    )
    AttackAttribute: int = ParamField(
        uint8, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=254,
        tooltip="Attack type. Almost always 4 ('other'), but sometimes 3 (knives/arrows/bolts).",
    )
    ElementAttribute: int = ParamField(
        uint8, "spAttribute", ATKPARAM_SPATTR_TYPE, default=254,
        tooltip="Element attached to bullet hit.",
    )
    MaterialAttackType: int = ParamField(
        uint8, "Material_AttackType", BEHAVIOR_ATK_TYPE, default=254,
        tooltip="Determines visual effects of bullet hit.",
    )
    EffectsOnHit: int = ParamField(
        uint8, "Material_AttackMaterial", WEP_MATERIAL_ATK, default=254,
        tooltip="Sound and visual effects on hit.",
    )
    IsPenetrateChr: bool = ParamField(
        uint8, "isPenetrateChr:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsPenetrateObj: bool = ParamField(
        uint8, "isPenetrateObj:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    MayRemoteDetonate: bool = ParamField(
        uint8, "mayRemoteDetonate:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad:5", bit_count=5)
    LaunchConditionType: int = ParamField(
        uint8, "launchConditionType", BULLET_LAUNCH_CONDITION_TYPE, default=0,
        tooltip="Condition for determing if a new bullet will be generated when this bullet lands or expires.",
    )
    FollowType: int = ParamField(
        uint8, "FollowType:3", BULLET_FOLLOW_TYPE, bit_count=3, default=0,
        tooltip="Follow type.",
    )
    OriginType: int = ParamField(
        uint8, "EmittePosType:3", BULLET_EMITTE_POS_TYPE, bit_count=3, default=0,
        tooltip="Origin type of bullet. Usually comes from model points ('damipoly').",
    )
    RemainAttachedToTarget: bool = ParamField(
        uint8, "isAttackSFX:1", ON_OFF, bit_count=1, default=False,
        tooltip="Set whether bullets (e.g. arrows) stay stuck upon impact.",
    )
    IsEndlessHit: bool = ParamField(
        uint8, "isEndlessHit:1", ON_OFF, bit_count=1, default=False,
        tooltip="Bullet hitbox is continuous (I think). Only used for corrosion cloud in vanilla.",
    )
    IsMapPiercing: bool = ParamField(
        uint8, "isPenetrateMap:1", ON_OFF, bit_count=1, default=False,
        tooltip="Bullet will pierce the map (e.g. Stray Demon blast).",
    )
    HitsBothTeams: bool = ParamField(
        uint8, "isHitBothTeam:1", ON_OFF, bit_count=1, default=False,
        tooltip="Bullet can hit any character.",
    )
    SharedHitCheck: bool = ParamField(
        uint8, "isUseSharedHitList:1", ON_OFF, bit_count=1, default=False,
        tooltip="Repeating bullets share the amount of times they have hit a target (usually so the target is only "
                "hit once by any of those repeating bullets).",
    )
    UsesMultipleModelPoints: bool = ParamField(
        uint8, "isUseMultiDmyPolyIfPlace:1", ON_OFF, bit_count=1, default=False,
        tooltip="Set to True if the same model point ('damipoly') is used multiple times when spawning the bullet.",
    )
    IsHitOtherBulletForceEraseA: bool = ParamField(
        uint8, "isHitOtherBulletForceEraseA:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitOtherBulletForceEraseB: bool = ParamField(
        uint8, "isHitOtherBulletForceEraseB:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanBeDeflectedByMagic: bool = ParamField(
        uint8, "isHitForceMagic:1", bit_count=1, default=False,
        tooltip="If True, this bullet will impact appropriate Force-type magic (e.g. arrows, bolts, knives).",
    )
    IgnoreVFXOnWaterHit: bool = ParamField(
        uint8, "isIgnoreSfxIfHitWater:1", bit_count=1, default=False,
        tooltip="If True, hit VFX are not produced if the bullet impacts water.",
    )
    IgnoreStateTransitionOnWaterHit: bool = ParamField(
        uint8, "isIgnoreMoveStateIfHitWater:1", bit_count=1, default=False,
        tooltip="Unclear effect, but True for knives/arrows/bolts and False otherwise.",
    )
    CanBeDeflectedByBeastRoar: bool = ParamField(
        uint8, "isHitDarkForceMagic:1", bit_count=1, default=False,
        tooltip="If True, this bullet will impact the Beast Roar deflection effect.",
    )
    DmgCalcSide: int = ParamField(
        uint8, "dmgCalcSide:2", DMG_CALC_SIDE_TYPE, bit_count=2, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableAutoHoming: bool = ParamField(
        uint8, "isEnableAutoHoming:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSyncBulletCulcDumypolyPos: bool = ParamField(
        uint8, "isSyncBulletCulcDumypolyPos:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsOwnerOverrideInitAngle: bool = ParamField(
        uint8, "isOwnerOverrideInitAngle:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInheritSfxToChild: bool = ParamField(
        uint8, "isInheritSfxToChild:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageDamp: int = ParamField(
        int8, "darkDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyHit: int = ParamField(
        int8, "bulletSfxDeleteType_byHit", BULLET_SFX_DELETE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyLifeDead: int = ParamField(
        int8, "bulletSfxDeleteType_byLifeDead", BULLET_SFX_DELETE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TargetYOffsetRange: float = ParamField(
        float32, "targetYOffsetRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShootAngleYMaxRandom: float = ParamField(
        float32, "shootAngleYMaxRandom", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShootAngleXMaxRandom: float = ParamField(
        float32, "shootAngleXMaxRandom", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateBulletId: int = ParamField(
        int32, "intervalCreateBulletId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateTimeMin: float = ParamField(
        float32, "intervalCreateTimeMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateTimeMax: float = ParamField(
        float32, "intervalCreateTimeMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PredictionShootObserveTime: float = ParamField(
        float32, "predictionShootObserveTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalCreateWaitTime: float = ParamField(
        float32, "intervalCreateWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SfxPostureType: int = ParamField(
        uint8, "sfxPostureType", BULLET_SFX_CREATE_POSTURE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateLimitGroupId: int = ParamField(
        uint8, "createLimitGroupId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad5[1]")
    ChildrenInheritSpeed: bool = ParamField(
        uint8, "isInheritSpeedToChild:1", ON_OFF, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsDisableHitSfxbyChrAndObj: bool = ParamField(
        uint8, "isDisableHitSfx_byChrAndObj:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckWallbyCenterRay: bool = ParamField(
        uint8, "isCheckWall_byCenterRay:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitFlare: bool = ParamField(
        uint8, "isHitFlare:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseBulletWallFilter: bool = ParamField(
        uint8, "isUseBulletWallFilter:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableAiProjectileDodge: bool = ParamField(
        uint8, "isDisableAiProjectileDodge:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsNonDependenceMagicForFunnleNum: bool = ParamField(
        uint8, "isNonDependenceMagicForFunnleNum:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAiInterruptShootNoDamageBullet: bool = ParamField(
        uint8, "isAiInterruptShootNoDamageBullet:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RandomCreateRadius: float = ParamField(
        float32, "randomCreateRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FollowOffsetBaseHeight: float = ParamField(
        float32, "followOffset_BaseHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AssetNoHit: int = ParamField(
        int32, "assetNo_Hit", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LifeRandomRange: float = ParamField(
        float32, "lifeRandomRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HomingAngleX: int = ParamField(
        int16, "homingAngleX", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BallisticCalcType: int = ParamField(
        uint8, "ballisticCalcType", BULLET_BALLISTIC_CALC_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttachEffectType: int = ParamField(
        uint8, "attachEffectType", BULLET_ATTACH_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SeIdBullet1: int = ParamField(
        int32, "seId_Bullet1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeIdBullet2: int = ParamField(
        int32, "seId_Bullet2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeIdHit: int = ParamField(
        int32, "seId_Hit", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeIdFlick: int = ParamField(
        int32, "seId_Flick", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerShootAngleXMin: int = ParamField(
        int16, "howitzerShootAngleXMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerShootAngleXMax: int = ParamField(
        int16, "howitzerShootAngleXMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerInitMinVelocity: float = ParamField(
        float32, "howitzerInitMinVelocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HowitzerInitMaxVelocity: float = ParamField(
        float32, "howitzerInitMaxVelocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdForceErase: int = ParamField(
        int32, "sfxId_ForceErase", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyForceErase: int = ParamField(
        int8, "bulletSfxDeleteType_byForceErase", BULLET_SFX_DELETE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad3[1]")
    FollowDmypolyforSfxPose: int = ParamField(
        int16, "followDmypoly_forSfxPose", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FollowOffsetRadius: float = ParamField(
        float32, "followOffset_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpBulletDistUpRate: float = ParamField(
        float32, "spBulletDistUpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NolockTargetDist: float = ParamField(
        float32, "nolockTargetDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad4[8]")
