from __future__ import annotations

__all__ = ["OBJECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class OBJECT_PARAM_ST(ParamRow):
    ObjectHP: int = ParamField(
        short, "hp", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MinAttackForDamage: int = ParamField(
        ushort, "defense", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExternalTextureID: int = ParamField(
        short, "extRefTexId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialID: int = ParamField(
        short, "materialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxDestructionAnimationID: int = ParamField(
        byte, "animBreakIdMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CollidesWithCamera: int = ParamField(
        byte, "isCamHit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BrokenByPlayerCollision: int = ParamField(
        byte, "isBreakByPlayerCollide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HasDestructionAnimation: int = ParamField(
        byte, "isAnimBreak:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitByPiercingBullets: int = ParamField(
        byte, "isPenetrationBulletHit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CharacterCollision: int = ParamField(
        byte, "isChrHit:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DeflectsAttacks: int = ParamField(
        byte, "isAttackBacklash:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CannotSpawnBroken: int = ParamField(
        byte, "isDisableBreakForFirstAppear:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLadder: int = ParamField(
        byte, "isLadder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StopAnimationDuringCutscenes: int = ParamField(
        byte, "isAnimPauseOnRemoPlay:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PreventAllDamage: int = ParamField(
        byte, "isDamageNoHit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMovingObject: int = ParamField(
        byte, "isMoveObj:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsRopeBridge: int = ParamField(
        byte, "isRopeBridge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAddRigidImpulseByDamage: int = ParamField(
        byte, "isAddRigidImpulse_ByDamage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByChrRide: int = ParamField(
        byte, "isBreak_ByChrRide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBurn: int = ParamField(
        byte, "isBurn:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByEnemyCollide: int = ParamField(
        byte, "isBreakByEnemyCollide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefaultLOD: int = ParamField(
        sbyte, "defaultLodParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DestructionSoundEffect: int = ParamField(
        int, "breakSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakSfxCpId: int = ParamField(
        int, "breakSfxCpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletBehaviorId: int = ParamField(
        int, "breakBulletBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletCpId: int = ParamField(
        int, "breakBulletCpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakFallHeight: int = ParamField(
        byte, "breakFallHeight", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType0: int = ParamField(
        byte, "windEffectType_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType1: int = ParamField(
        byte, "windEffectType_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamAvoidType: int = ParamField(
        byte, "camAvoidType", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate0: float = ParamField(
        float, "windEffectRate_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate1: float = ParamField(
        float, "windEffectRate_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakStopTime: float = ParamField(
        float, "breakStopTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnTime: float = ParamField(
        float, "burnTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBraekRate: float = ParamField(
        float, "burnBraekRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId: int = ParamField(
        int, "burnSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId1: int = ParamField(
        int, "burnSfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId2: int = ParamField(
        int, "burnSfxId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId3: int = ParamField(
        int, "burnSfxId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId: int = ParamField(
        int, "burnBulletBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId1: int = ParamField(
        int, "burnBulletBehaviorId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId2: int = ParamField(
        int, "burnBulletBehaviorId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId3: int = ParamField(
        int, "burnBulletBehaviorId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletInterval: int = ParamField(
        ushort, "burnBulletInterval", default=30,
        tooltip="TOOLTIP-TODO",
    )
    NavmeshFlag: int = ParamField(
        byte, "navimeshFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CollisionType: int = ParamField(
        byte, "collisionType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletDelayTime: float = ParamField(
        float, "burnBulletDelayTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin: float = ParamField(
        float, "burnSfxDelayTimeMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin1: float = ParamField(
        float, "burnSfxDelayTimeMin_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin2: float = ParamField(
        float, "burnSfxDelayTimeMin_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin3: float = ParamField(
        float, "burnSfxDelayTimeMin_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax: float = ParamField(
        float, "burnSfxDelayTimeMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax1: float = ParamField(
        float, "burnSfxDelayTimeMax_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax2: float = ParamField(
        float, "burnSfxDelayTimeMax_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax3: float = ParamField(
        float, "burnSfxDelayTimeMax_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakAiSoundID: int = ParamField(
        int, "BreakAiSoundID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FragmentInvisibleWaitTime: float = ParamField(
        float, "FragmentInvisibleWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FragmentInvisibleTime: float = ParamField(
        float, "FragmentInvisibleTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(16, "pad_3[16]")
    RigidPenetrationScaleSoft: float = ParamField(
        float, "RigidPenetrationScale_Soft", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RigidPenetrationScaleNormal: float = ParamField(
        float, "RigidPenetrationScale_Normal", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RigidPenetrationScaleHard: float = ParamField(
        float, "RigidPenetrationScale_Hard", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LandTouchSfxId: int = ParamField(
        int, "LandTouchSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsDamageCover: int = ParamField(
        byte, "isDamageCover:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad_4[1]")
    PaintDecalTargetTextureSize: int = ParamField(
        ushort, "paintDecalTargetTextureSize", default=256,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeforDC: float = ParamField(
        float, "lifeTime_forDC", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ClothUpdateDist: float = ParamField(
        float, "clothUpdateDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactSeId: int = ParamField(
        int, "contactSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakLandingSfxId: int = ParamField(
        int, "breakLandingSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WaypointDummyPolyId0: int = ParamField(
        int, "waypointDummyPolyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WaypointParamId0: int = ParamField(
        int, "waypointParamId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBankId: int = ParamField(
        int, "soundBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefDrawParamId: int = ParamField(
        int, "refDrawParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoCreateDynamicOffsetHeight: float = ParamField(
        float, "autoCreateDynamicOffsetHeight", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Reserved0: int = ParamField(
        int, "reserved0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBreakSEId: int = ParamField(
        int, "soundBreakSEId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(40, "pad_5[40]")
