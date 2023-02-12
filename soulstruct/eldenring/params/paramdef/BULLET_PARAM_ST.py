from __future__ import annotations

__all__ = ["BULLET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BULLET_PARAM_ST(ParamRowData):
    BulletAttack: int = ParamField(
        int, "atkId_Bullet", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ProjectileVFX: int = ParamField(
        int, "sfxId_Bullet", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ImpactVFX: int = ParamField(
        int, "sfxId_Hit", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlickVFX: int = ParamField(
        int, "sfxId_Flick", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LifeTime: float = ParamField(
        float, "life", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttenuationDistance: float = ParamField(
        float, "dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LaunchInterval: float = ParamField(
        float, "shootInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityBeforeAttenuation: float = ParamField(
        float, "gravityInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityAfterAttenuation: float = ParamField(
        float, "gravityOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ClosestHomingDistance: float = ParamField(
        float, "hormingStopRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    InitialSpeed: float = ParamField(
        float, "initVellocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelerationBeforeAttenuation: float = ParamField(
        float, "accelInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelerationAfterAttenuation: float = ParamField(
        float, "accelOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxSpeed: float = ParamField(
        float, "maxVellocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinSpeed: float = ParamField(
        float, "minVellocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelerationTime: float = ParamField(
        float, "accelTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HomingStartDistance: float = ParamField(
        float, "homingBeginDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    InitialHitRadius: float = ParamField(
        float, "hitRadius", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FinalHitRadius: float = ParamField(
        float, "hitRadiusMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RadiusIncreaseTime: float = ParamField(
        float, "spreadTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ExpDelay: float = ParamField(
        float, "expDelay", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HomingOffsetRange: float = ParamField(
        float, "hormingOffsetRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HitboxLifeTime: float = ParamField(
        float, "dmgHitRecordLifeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ExternalForce: float = ParamField(
        float, "externalForce", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OwnerSpecialEffect: int = ParamField(
        int, "spEffectIDForShooter", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BulletAI: int = ParamField(
        int, "autoSearchNPCThinkID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BulletOnHit: int = ParamField(
        int, "HitBulletID", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitSpecialEffect0: int = ParamField(
        int, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitSpecialEffect1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitSpecialEffect2: int = ParamField(
        int, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitSpecialEffect3: int = ParamField(
        int, "spEffectId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitSpecialEffect4: int = ParamField(
        int, "spEffectId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BulletCount: int = ParamField(
        ushort, "numShoot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HomingAnglePerSecond: int = ParamField(
        short, "homingAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AzimuthAngleStart: int = ParamField(
        short, "shootAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AzimuthAngleInterval: int = ParamField(
        short, "shootAngleInterval", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ElevationAngleInterval: int = ParamField(
        short, "shootAngleXInterval", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalDamageDamp: int = ParamField(
        sbyte, "damageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamageDamp: int = ParamField(
        sbyte, "spelDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageDamp: int = ParamField(
        sbyte, "fireDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightningDamageDamp: int = ParamField(
        sbyte, "thunderDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaDamp: int = ParamField(
        sbyte, "staminaDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackDamp: int = ParamField(
        sbyte, "knockbackDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FirstBulletElevationAngle: int = ParamField(
        sbyte, "shootAngleXZ", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockShootLimitAngle: int = ParamField(
        byte, "lockShootLimitAng", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    PreviousDirectionRatio: int = ParamField(
        byte, "prevVelocityDirRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackAttribute: int = ParamField(
        byte, "atkAttribute", default=254,
        tooltip="TOOLTIP-TODO",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", default=254,
        tooltip="TOOLTIP-TODO",
    )
    MaterialAttackType: int = ParamField(
        byte, "Material_AttackType", default=254,
        tooltip="TOOLTIP-TODO",
    )
    EffectsOnHit: int = ParamField(
        byte, "Material_AttackMaterial", default=254,
        tooltip="TOOLTIP-TODO",
    )
    IsPenetrateChr: int = ParamField(
        byte, "isPenetrateChr:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsPenetrateObj: int = ParamField(
        byte, "isPenetrateObj:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad:6")
    LaunchConditionType: int = ParamField(
        byte, "launchConditionType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FollowType: int = ParamField(
        byte, "FollowType:3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OriginType: int = ParamField(
        byte, "EmittePosType:3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RemainAttachedToTarget: int = ParamField(
        byte, "isAttackSFX:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEndlessHit: int = ParamField(
        byte, "isEndlessHit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMapPiercing: int = ParamField(
        byte, "isPenetrateMap:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitsBothTeams: int = ParamField(
        byte, "isHitBothTeam:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SharedHitCheck: int = ParamField(
        byte, "isUseSharedHitList:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsesMultipleModelPoints: int = ParamField(
        byte, "isUseMultiDmyPolyIfPlace:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHitOtherBulletForceEraseA: int = ParamField(
        byte, "isHitOtherBulletForceEraseA:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHitOtherBulletForceEraseB: int = ParamField(
        byte, "isHitOtherBulletForceEraseB:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanBeDeflectedByMagic: int = ParamField(
        byte, "isHitForceMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreVFXOnWaterHit: int = ParamField(
        byte, "isIgnoreSfxIfHitWater:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreStateTransitionOnWaterHit: int = ParamField(
        byte, "isIgnoreMoveStateIfHitWater:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanBeDeflectedByBeastRoar: int = ParamField(
        byte, "isHitDarkForceMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgCalcSide: int = ParamField(
        byte, "dmgCalcSide:2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableAutoHoming: int = ParamField(
        byte, "isEnableAutoHoming:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSyncBulletCulcDumypolyPos: int = ParamField(
        byte, "isSyncBulletCulcDumypolyPos:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsOwnerOverrideInitAngle: int = ParamField(
        byte, "isOwnerOverrideInitAngle:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsInheritSfxToChild: int = ParamField(
        byte, "isInheritSfxToChild:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageDamp: int = ParamField(
        sbyte, "darkDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyHit: int = ParamField(
        sbyte, "bulletSfxDeleteType_byHit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BulletSfxDeleteTypebyLifeDead: int = ParamField(
        sbyte, "bulletSfxDeleteType_byLifeDead", default=0,
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
        byte, "sfxPostureType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateLimitGroupId: int = ParamField(
        byte, "createLimitGroupId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad5[1]")
    ChildrenInheritSpeed: int = ParamField(
        byte, "isInheritSpeedToChild:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableHitSfxbyChrAndObj: int = ParamField(
        byte, "isDisableHitSfx_byChrAndObj:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckWallbyCenterRay: int = ParamField(
        byte, "isCheckWall_byCenterRay:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHitFlare: int = ParamField(
        byte, "isHitFlare:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUseBulletWallFilter: int = ParamField(
        byte, "isUseBulletWallFilter:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad1:1")
    IsNonDependenceMagicForFunnleNum: int = ParamField(
        byte, "isNonDependenceMagicForFunnleNum:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAiInterruptShootNoDamageBullet: int = ParamField(
        byte, "isAiInterruptShootNoDamageBullet:1", default=0,
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
        byte, "ballisticCalcType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttachEffectType: int = ParamField(
        byte, "attachEffectType", default=0,
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
        sbyte, "bulletSfxDeleteType_byForceErase", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(1, "pad3[1]")
    FollowDmypolyforSfxPose: int = ParamField(
        short, "followDmypoly_forSfxPose", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FollowOffsetRadius: float = ParamField(
        float, "followOffset_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpBulletDistUpRate: float = ParamField(
        float, "spBulletDistUpRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    NolockTargetDist: float = ParamField(
        float, "nolockTargetDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(8, "pad4[8]")
