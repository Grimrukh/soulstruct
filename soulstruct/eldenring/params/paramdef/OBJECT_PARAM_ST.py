from __future__ import annotations

__all__ = ["OBJECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class OBJECT_PARAM_ST(ParamRow):
    ObjectHP: int = ParamField(
        short, "hp", default=-1,
        tooltip="Amount of damage object can take before it is destroyed. (Set to -1 for invulnerability.)",
    )
    MinAttackForDamage: int = ParamField(
        ushort, "defense", default=0,
        tooltip="Minimum attack power required to damage object. Attacks with less power than this will deal no "
                "damage.",
    )
    ExternalTextureID: int = ParamField(
        short, "extRefTexId", default=-1,
        tooltip="Internal description: 'mAA / mAA_????.tpf (-1: None) (AA: Area number)'.",
    )
    MaterialID: int = ParamField(
        short, "materialId", default=-1,
        tooltip="Treated the same as floor material. (Set to -1 to use default.)",
    )
    MaxDestructionAnimationID: int = ParamField(
        byte, "animBreakIdMax", default=0,
        tooltip="Upper limit of range of destruction animations, which seem to always start at 0.",
    )
    CollidesWithCamera: bool = ParamField(
        byte, "isCamHit:1", bit_count=1, default=False,
        tooltip="If True, the camera will collide with this object.",
    )
    BrokenByPlayerCollision: bool = ParamField(
        byte, "isBreakByPlayerCollide:1", bit_count=1, default=False,
        tooltip="If True, the player will break the object just by touching it.",
    )
    HasDestructionAnimation: bool = ParamField(
        byte, "isAnimBreak:1", bit_count=1, default=False,
        tooltip="If True, the object will use an animation when destroyed rather than using physics-based "
                "destruction.",
    )
    HitByPiercingBullets: bool = ParamField(
        byte, "isPenetrationBulletHit:1", bit_count=1, default=False,
        tooltip="If True, the object can be damaged by Bullets with target-piercing enabled.",
    )
    CharacterCollision: bool = ParamField(
        byte, "isChrHit:1", bit_count=1, default=True,
        tooltip="If False, characters will pass through the object (e.g. branches).",
    )
    DeflectsAttacks: bool = ParamField(
        byte, "isAttackBacklash:1", bit_count=1, default=True,
        tooltip="If True, attacks will bounce off the object as though it were a wall.",
    )
    CannotSpawnBroken: bool = ParamField(
        byte, "isDisableBreakForFirstAppear:1", bit_count=1, default=False,
        tooltip="If True, the object cannot be destroyed when the player first spawns.",
    )
    IsLadder: bool = ParamField(
        byte, "isLadder:1", bit_count=1, default=False,
        tooltip="Object is a ladder.",
    )
    StopAnimationDuringCutscenes: bool = ParamField(
        byte, "isAnimPauseOnRemoPlay:1", bit_count=1, default=False,
        tooltip="If True, object animation will not play in cutscenes.",
    )
    PreventAllDamage: bool = ParamField(
        byte, "isDamageNoHit:1", bit_count=1, default=False,
        tooltip="If True, all damage to the object will be prevented. (Not sure if this is the same effet as settings "
                "its HP to -1.)",
    )
    IsMovingObject: bool = ParamField(
        byte, "isMoveObj:1", bit_count=1, default=False,
        tooltip="If True, this object can move.",
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
    DefaultLOD: int = ParamField(
        sbyte, "defaultLodParamId", default=-1,
        tooltip="Default LOD (level of default) parameter.",
    )
    DestructionSoundEffect: int = ParamField(
        int, "breakSfxId", game_type=VisualEffect, default=-1,
        tooltip="Sound effect played upon destruction. (Set to -1 to use default value, which is apparently 80.)",
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
    NavmeshFlag: int = ParamField(
        byte, "navimeshFlag", OBJECT_NAVIMESH_FLAG, default=0,
        tooltip="TODO",
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
