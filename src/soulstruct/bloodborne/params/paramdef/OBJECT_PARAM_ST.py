from __future__ import annotations

__all__ = ["OBJECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class OBJECT_PARAM_ST(ParamRow):
    ObjectHP: int = ParamField(
        int16, "hp", default=-1,
        tooltip="Amount of damage object can take before it is destroyed. (Set to -1 for invulnerability.)",
    )
    MinAttackForDamage: int = ParamField(
        uint16, "defense", default=0,
        tooltip="Minimum attack power required to damage object. Attacks with less power than this will deal no "
                "damage.",
    )
    ExternalTextureID: int = ParamField(
        int16, "extRefTexId", default=-1,
        tooltip="Internal description: 'mAA / mAA_????.tpf (-1: None) (AA: Area number)'.",
    )
    MaterialID: int = ParamField(
        int16, "materialId", default=-1,
        tooltip="Treated the same as floor material. (Set to -1 to use default.)",
    )
    MaxDestructionAnimationID: int = ParamField(
        uint8, "animBreakIdMax", default=0,
        tooltip="Upper limit of range of destruction animations, which seem to always start at 0.",
    )
    CollidesWithCamera: bool = ParamField(
        uint8, "isCamHit:1", bit_count=1, default=False,
        tooltip="If True, the camera will collide with this object.",
    )
    BrokenByPlayerCollision: bool = ParamField(
        uint8, "isBreakByPlayerCollide:1", bit_count=1, default=False,
        tooltip="If True, the player will break the object just by touching it.",
    )
    HasDestructionAnimation: bool = ParamField(
        uint8, "isAnimBreak:1", bit_count=1, default=False,
        tooltip="If True, the object will use an animation when destroyed rather than using physics-based "
                "destruction.",
    )
    HitByPiercingBullets: bool = ParamField(
        uint8, "isPenetrationBulletHit:1", bit_count=1, default=False,
        tooltip="If True, the object can be damaged by Bullets with target-piercing enabled.",
    )
    CharacterCollision: bool = ParamField(
        uint8, "isChrHit:1", bit_count=1, default=True,
        tooltip="If False, characters will pass through the object (e.g. branches).",
    )
    DeflectsAttacks: bool = ParamField(
        uint8, "isAttackBacklash:1", bit_count=1, default=True,
        tooltip="If True, attacks will bounce off the object as though it were a wall.",
    )
    CannotSpawnBroken: bool = ParamField(
        uint8, "isDisableBreakForFirstAppear:1", bit_count=1, default=False,
        tooltip="If True, the object cannot be destroyed when the player first spawns.",
    )
    IsLadder: bool = ParamField(
        uint8, "isLadder:1", bit_count=1, default=False,
        tooltip="Object is a ladder.",
    )
    StopAnimationDuringCutscenes: bool = ParamField(
        uint8, "isAnimPauseOnRemoPlay:1", bit_count=1, default=False,
        tooltip="If True, object animation will not play in cutscenes.",
    )
    PreventAllDamage: bool = ParamField(
        uint8, "isDamageNoHit:1", bit_count=1, default=False,
        tooltip="If True, all damage to the object will be prevented. (Not sure if this is the same effet as settings "
                "its HP to -1.)",
    )
    IsMovingObject: bool = ParamField(
        uint8, "isMoveObj:1", bit_count=1, default=False,
        tooltip="If True, this object can move.",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad_1:5", bit_count=5)
    DefaultLOD: int = ParamField(
        int8, "defaultLodParamId", default=-1,
        tooltip="Default LOD (level of default) parameter.",
    )
    DestructionSoundEffect: int = ParamField(
        int32, "breakSfxId", game_type=VisualEffect, default=-1,
        tooltip="Sound effect played upon destruction. (Set to -1 to use default value, which is apparently 80.)",
    )
    NavmeshFlag: int = ParamField(
        uint8, "navimeshFlag", OBJECT_NAVIMESH_FLAG, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad_2[1]")
    PaintRenderTargetSize: int = ParamField(
        uint16, "paintRenderTargetSize", default=256,
        tooltip="TODO",
    )
    BreakAISoundID: int = ParamField(
        int32, "breakAiSoundId", game_type=AISoundParam, default=0,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad_3[8]")
