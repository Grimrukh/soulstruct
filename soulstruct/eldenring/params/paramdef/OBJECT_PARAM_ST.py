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
    Hp: int = ParamField(
        short, "hp", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Defense: int = ParamField(
        ushort, "defense", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExtRefTexId: int = ParamField(
        short, "extRefTexId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialId: int = ParamField(
        short, "materialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnimBreakIdMax: int = ParamField(
        byte, "animBreakIdMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCamHit: bool = ParamField(
        byte, "isCamHit:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByPlayerCollide: bool = ParamField(
        byte, "isBreakByPlayerCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimBreak: bool = ParamField(
        byte, "isAnimBreak:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsPenetrationBulletHit: bool = ParamField(
        byte, "isPenetrationBulletHit:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsChrHit: bool = ParamField(
        byte, "isChrHit:1", bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsAttackBacklash: bool = ParamField(
        byte, "isAttackBacklash:1", bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBreakForFirstAppear: bool = ParamField(
        byte, "isDisableBreakForFirstAppear:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLadder: bool = ParamField(
        byte, "isLadder:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimPauseOnRemoPlay: bool = ParamField(
        byte, "isAnimPauseOnRemoPlay:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDamageNoHit: bool = ParamField(
        byte, "isDamageNoHit:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMoveObj: bool = ParamField(
        byte, "isMoveObj:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsRopeBridge: bool = ParamField(
        byte, "isRopeBridge:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAddRigidImpulseByDamage: bool = ParamField(
        byte, "isAddRigidImpulse_ByDamage:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByChrRide: bool = ParamField(
        byte, "isBreak_ByChrRide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBurn: bool = ParamField(
        byte, "isBurn:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByEnemyCollide: bool = ParamField(
        byte, "isBreakByEnemyCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DefaultLodParamId: int = ParamField(
        sbyte, "defaultLodParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakSfxId: int = ParamField(
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
        byte, "windEffectType_0", OBJECT_WIND_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType1: int = ParamField(
        byte, "windEffectType_1", OBJECT_WIND_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamAvoidType: int = ParamField(
        byte, "camAvoidType", OBJECT_CAM_AVOID_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate0: float = ParamField(
        float, "windEffectRate_0", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate1: float = ParamField(
        float, "windEffectRate_1", default=0.5,
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
        float, "burnBraekRate", default=0.5,
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
    NavimeshFlag: int = ParamField(
        byte, "navimeshFlag", OBJECT_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CollisionType: int = ParamField(
        byte, "collisionType", OBJECT_COLLISION_TYPE, default=0,
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
    IsDamageCover: bool = ParamField(
        byte, "isDamageCover:1", bit_count=1, default=False,
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
        float, "autoCreateDynamicOffsetHeight", default=0.1,
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
