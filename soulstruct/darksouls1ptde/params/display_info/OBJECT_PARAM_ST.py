from __future__ import annotations

__all__ = ["OBJECT_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, bit_pad_field
from soulstruct.darksouls1ptde.game_types import *


OBJECT_PARAM_ST = {
    "param_type": "OBJECT_PARAM_ST",
    "file_name": "ObjectParam",
    "nickname": "Objects",
    "fields": [
        ParamFieldInfo(
            "hp",
            "ObjectHP",
            True,
            int,
            "Amount of damage object can take before it is destroyed. (Set to -1 for invulnerability.)",
        ),
        ParamFieldInfo(
            "defense",
            "MinAttackForDamage",
            True,
            int,
            "Minimum attack power required to damage object. Attacks with less power than this will deal no "
            "damage.",
        ),
        ParamFieldInfo(
            "extRefTexId",
            "ExternalTextureID",
            False,
            int,
            "Internal description: 'mAA / mAA_????.tpf (-1: None) (AA: Area number)'.",
        ),
        ParamFieldInfo(
            "materialId",
            "MaterialID",
            True,
            TerrainParam,
            "Treated the same as floor material. (Set to -1 to use default.)",
        ),
        ParamFieldInfo(
            "animBreakIdMax",
            "MaxDestructionAnimationID",
            False,
            int,  # TODO: Animation
            "Upper limit of range of destruction animations, which seem to always start at 0.",
        ),
        ParamFieldInfo(
            "isCamHit:1", "CollidesWithCamera", True, bool, "If True, the camera will collide with this object."
        ),
        ParamFieldInfo(
            "isBreakByPlayerCollide:1",
            "BrokenByPlayerCollision",
            True,
            bool,
            "If True, the player will break the object just by touching it.",
        ),
        ParamFieldInfo(
            "isAnimBreak:1",
            "HasDestructionAnimation",
            True,
            bool,
            "If True, the object will use an animation when destroyed rather than using physics-based destruction.",
        ),
        ParamFieldInfo(
            "isPenetrationBulletHit:1",
            "HitByPiercingBullets",
            True,
            bool,
            "If True, the object can be damaged by Bullets with target-piercing enabled.",
        ),
        ParamFieldInfo(
            "isChrHit:1",
            "CharacterCollision",
            True,
            bool,
            "If False, characters will pass through the object (e.g. branches).",
        ),
        ParamFieldInfo(
            "isAttackBacklash:1",
            "DeflectsAttacks",
            True,
            bool,
            "If True, attacks will bounce off the object as though it were a wall.",
        ),
        ParamFieldInfo(
            "isDisableBreakForFirstAppear:1",
            "CannotSpawnBroken",
            True,
            bool,
            "If True, the object cannot be destroyed when the player first spawns.",
        ),
        ParamFieldInfo("isLadder:1", "IsLadder", True, bool, "Object is a ladder."),
        ParamFieldInfo(
            "isAnimPauseOnRemoPlay:1",
            "StopAnimationDuringCutscenes",
            True,
            bool,
            "If True, object animation will not play in cutscenes.",
        ),
        ParamFieldInfo(
            "isDamageNoHit:1",
            "PreventAllDamage",
            True,
            bool,
            "If True, all damage to the object will be prevented. (Not sure if this is the same effet as settings "
            "its HP to -1.)",
        ),
        ParamFieldInfo("isMoveObj:1", "IsMovingObject", True, bool, "If True, this object can move."),
        ParamFieldInfo("pad_1:5", "Pad1", False, bit_pad_field(5), "Null padding."),
        # TODO: LOD type.
        ParamFieldInfo("defaultLodParamId", "DefaultLOD", True, int, "Default LOD (level of default) parameter."),
        ParamFieldInfo(
            "breakSfxId",
            "DestructionSoundEffect",
            True,
            SFXSound,
            "Sound effect played upon destruction. (Set to -1 to use default value, which is apparently 80.)",
        ),
    ],
}
