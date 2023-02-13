from __future__ import annotations

__all__ = ["BULLET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BULLET_PARAM_ST(ParamRow):
    AtkIdBullet: int = ParamField(
        int, "atkId_Bullet", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdBullet: int = ParamField(
        int, "sfxId_Bullet", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdHit: int = ParamField(
        int, "sfxId_Hit", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdFlick: int = ParamField(
        int, "sfxId_Flick", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Life: float = ParamField(
        float, "life", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    Dist: float = ParamField(
        float, "dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShootInterval: float = ParamField(
        float, "shootInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityInRange: float = ParamField(
        float, "gravityInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityOutRange: float = ParamField(
        float, "gravityOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HormingStopRange: float = ParamField(
        float, "hormingStopRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    InitVellocity: float = ParamField(
        float, "initVellocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelInRange: float = ParamField(
        float, "accelInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelOutRange: float = ParamField(
        float, "accelOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxVellocity: float = ParamField(
        float, "maxVellocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinVellocity: float = ParamField(
        float, "minVellocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelTime: float = ParamField(
        float, "accelTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HomingBeginDist: float = ParamField(
        float, "homingBeginDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HitRadius: float = ParamField(
        float, "hitRadius", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    HitRadiusMax: float = ParamField(
        float, "hitRadiusMax", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    SpreadTime: float = ParamField(
        float, "spreadTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ExpDelay: float = ParamField(
        float, "expDelay", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HormingOffsetRange: float = ParamField(
        float, "hormingOffsetRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DmgHitRecordLifeTime: float = ParamField(
        float, "dmgHitRecordLifeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ExternalForce: float = ParamField(
        float, "externalForce", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIDForShooter: int = ParamField(
        int, "spEffectIDForShooter", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoSearchNPCThinkID: int = ParamField(
        int, "autoSearchNPCThinkID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitBulletID: int = ParamField(
        int, "HitBulletID", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId0: int = ParamField(
        int, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId2: int = ParamField(
        int, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId3: int = ParamField(
        int, "spEffectId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId4: int = ParamField(
        int, "spEffectId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NumShoot: int = ParamField(
        ushort, "numShoot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HomingAngle: int = ParamField(
        short, "homingAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShootAngle: int = ParamField(
        short, "shootAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShootAngleInterval: int = ParamField(
        short, "shootAngleInterval", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShootAngleXInterval: int = ParamField(
        short, "shootAngleXInterval", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DamageDamp: int = ParamField(
        sbyte, "damageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpelDamageDamp: int = ParamField(
        sbyte, "spelDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageDamp: int = ParamField(
        sbyte, "fireDamageDamp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDamageDamp: int = ParamField(
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
    ShootAngleXZ: int = ParamField(
        sbyte, "shootAngleXZ", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockShootLimitAng: int = ParamField(
        byte, "lockShootLimitAng", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    PrevVelocityDirRate: int = ParamField(
        byte, "prevVelocityDirRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=254,
        tooltip="TOOLTIP-TODO",
    )
    SpAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=254,
        tooltip="TOOLTIP-TODO",
    )
    MaterialAttackType: int = ParamField(
        byte, "Material_AttackType", BEHAVIOR_ATK_TYPE, default=254,
        tooltip="TOOLTIP-TODO",
    )
    MaterialAttackMaterial: int = ParamField(
        byte, "Material_AttackMaterial", WEP_MATERIAL_ATK, default=254,
        tooltip="TOOLTIP-TODO",
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
        tooltip="TOOLTIP-TODO",
    )
    FollowType: int = ParamField(
        byte, "FollowType:3", BULLET_FOLLOW_TYPE, bit_count=3, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EmittePosType: int = ParamField(
        byte, "EmittePosType:3", BULLET_EMITTE_POS_TYPE, bit_count=3, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAttackSFX: bool = ParamField(
        byte, "isAttackSFX:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEndlessHit: bool = ParamField(
        byte, "isEndlessHit:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsPenetrateMap: bool = ParamField(
        byte, "isPenetrateMap:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitBothTeam: bool = ParamField(
        byte, "isHitBothTeam:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseSharedHitList: bool = ParamField(
        byte, "isUseSharedHitList:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseMultiDmyPolyIfPlace: bool = ParamField(
        byte, "isUseMultiDmyPolyIfPlace:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitOtherBulletForceEraseA: bool = ParamField(
        byte, "isHitOtherBulletForceEraseA:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitOtherBulletForceEraseB: bool = ParamField(
        byte, "isHitOtherBulletForceEraseB:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitForceMagic: bool = ParamField(
        byte, "isHitForceMagic:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsIgnoreSfxIfHitWater: bool = ParamField(
        byte, "isIgnoreSfxIfHitWater:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsIgnoreMoveStateIfHitWater: bool = ParamField(
        byte, "isIgnoreMoveStateIfHitWater:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHitDarkForceMagic: bool = ParamField(
        byte, "isHitDarkForceMagic:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
    IsInheritSpeedToChild: bool = ParamField(
        byte, "isInheritSpeedToChild:1", ON_OFF, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
