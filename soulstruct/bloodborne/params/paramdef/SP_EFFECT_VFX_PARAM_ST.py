from __future__ import annotations

__all__ = ["SP_EFFECT_VFX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SP_EFFECT_VFX_PARAM_ST(ParamRow):
    OngoingVisualEffect: int = ParamField(
        int, "midstSfxId", game_type=VisualEffect, default=-1,
        tooltip="Ongoing visual effect for special effect. -1 is no effect.",
    )
    OngoingSoundEffect: int = ParamField(
        int, "midstSeId", default=-1,
        tooltip="Ongoing sound effect for special effect. -1 is no effect.",
    )
    InitialVisualEffect: int = ParamField(
        int, "initSfxId", game_type=VisualEffect, default=-1,
        tooltip="One-off visual effect when special effect begins. -1 is no effect.",
    )
    InitialSoundEffect: int = ParamField(
        int, "initSeId", default=-1,
        tooltip="One-off sound effect when special effect begins. -1 is no effect. (Does not appear to work.)",
    )
    FinishVisualEffect: int = ParamField(
        int, "finishSfxId", game_type=VisualEffect, default=-1,
        tooltip="One-off visual effect when special effect ends. -1 is no effect.",
    )
    FinishSoundEffect: int = ParamField(
        int, "finishSeId", default=-1,
        tooltip="One-off sound effect when special effect ends. -1 is no effect. (Does not appear to work.)",
    )
    HideStartDistance: float = ParamField(
        float, "camouflageBeginDist", default=-1.0,
        tooltip="Closest distance at which effect is disabled.",
    )
    HideEndDistance: float = ParamField(
        float, "camouflageEndDist", default=-1.0,
        tooltip="Furthest distance at which effect is disabled.",
    )
    TransformationArmorID: int = ParamField(
        int, "transformProtectorId", game_type=ArmorParam, default=-1,
        tooltip="Transformation armor ID. Unknown effect. -1 is no armor.",
    )
    OngoingModelPoint: int = ParamField(
        short, "midstDmyId", game_type=ModelDummy, default=-1,
        tooltip="Model point where ongoing effects are centered. -1 is model root.",
    )
    InitialModelPoint: int = ParamField(
        short, "initDmyId", game_type=ModelDummy, default=-1,
        tooltip="Model point where initial effect is centered. -1 is model root.",
    )
    FinishModelPoint: int = ParamField(
        short, "finishDmyId", game_type=ModelDummy, default=-1,
        tooltip="Model point where finish effect is centered. -1 is model root.",
    )
    EffectType: int = ParamField(
        byte, "effectType", SP_EFFECT_VFX_EFFECT_TYPE, default=0,
        tooltip="Type of effect. Enum not yet mapped.",
    )
    WeaponEnchantmentSoulParam: int = ParamField(
        byte, "soulParamIdForWepEnchant", SP_EFFECT_VFX_SOUL_PARAM_TYPE, default=0,
        tooltip="Internal description: 'Soul Param ID for weapon enchantment.' Enum not yet mapped.",
    )
    PlaybackCategory: int = ParamField(
        byte, "playCategory", SP_EFFECT_VFX_PLAYCATEGORY, default=0,
        tooltip="Only one effect in each category can be active at once (determined by PlaybackPriority).",
    )
    PlaybackPriority: int = ParamField(
        byte, "playPriority", default=0,
        tooltip="Only the lowest-numbered-priority effect in each PlaybackCategory will be active at once.",
    )
    LargeEffectExists: bool = ParamField(
        byte, "existEffectForLarge:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Indicates if a large version of the effect exists.",
    )
    SoulEffectExists: bool = ParamField(
        byte, "existEffectForSoul:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Indicates if a 'soul version' of the effect exists.",
    )
    InvisibleWhenHidden: bool = ParamField(
        byte, "effectInvisibleAtCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Indicates if the effect should be invisible when hidden (unclear exactly what this means).",
    )
    HidingActive: bool = ParamField(
        byte, "useCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="I believe this determines if the hiding range fields are actually used.",
    )
    InvisibleWhenFriendHidden: bool = ParamField(
        byte, "invisibleAtFriendCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unclear.",
    )
    AddMapAreaBlockOffset: bool = ParamField(
        byte, "addMapAreaBlockOffset:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If enabled, the three-digit area/block number for the current map will be added to all effect IDs "
                "(e.g. m13_02 -> adds 132).",
    )
    HalfHiddenOnly: bool = ParamField(
        byte, "halfCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If enabled, effects are made semi-transparent rather than fully hidden.",
    )
    TransformBodyArmor: bool = ParamField(
        byte, "transformArmor:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Indicates whether the armor transformation should be applied to the whole body.",
    )
    HideWeapon: bool = ParamField(
        byte, "isInvisibleWeapon:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Weapon is invisible if enabled.",
    )
    IsSilent: bool = ParamField(
        byte, "isSilence:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Movement noises are silenced if enabled.",
    )
    TransformHandArmor: bool = ParamField(
        byte, "transformGauntlet:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    TransformHeadArmor: bool = ParamField(
        byte, "transformHelmet:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    TransformLegsArmor: bool = ParamField(
        byte, "transformLeggings:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    TransformPriority: int = ParamField(
        byte, "transformPriority:3", bit_count=3, default=0,
        tooltip="TODO",
    )
    TransformWeaponID: int = ParamField(
        int, "transformWeaponId", game_type=WeaponParam, default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(12, "pad[12]")
