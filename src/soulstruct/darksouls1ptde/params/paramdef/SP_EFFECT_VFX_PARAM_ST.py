from __future__ import annotations

__all__ = ["SP_EFFECT_VFX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class SP_EFFECT_VFX_PARAM_ST(ParamRow):
    OngoingVisualEffect: int = ParamField(
        int32, "midstSfxId", game_type=VisualEffect, default=-1,
        tooltip="Ongoing visual effect for special effect. -1 is no effect.",
    )
    OngoingSoundEffect: int = ParamField(
        int32, "midstSeId", default=-1,
        tooltip="Ongoing sound effect for special effect. -1 is no effect.",
    )
    InitialVisualEffect: int = ParamField(
        int32, "initSfxId", game_type=VisualEffect, default=-1,
        tooltip="One-off visual effect when special effect begins. -1 is no effect.",
    )
    InitialSoundEffect: int = ParamField(
        int32, "initSeId", default=-1,
        tooltip="One-off sound effect when special effect begins. -1 is no effect. (Does not appear to work.)",
    )
    FinishVisualEffect: int = ParamField(
        int32, "finishSfxId", game_type=VisualEffect, default=-1,
        tooltip="One-off visual effect when special effect ends. -1 is no effect.",
    )
    FinishSoundEffect: int = ParamField(
        int32, "finishSeId", default=-1,
        tooltip="One-off sound effect when special effect ends. -1 is no effect. (Does not appear to work.)",
    )
    HideStartDistance: float = ParamField(
        float32, "camouflageBeginDist", default=-1.0,
        tooltip="Closest distance at which effect is disabled.",
    )
    HideEndDistance: float = ParamField(
        float32, "camouflageEndDist", default=-1.0,
        tooltip="Furthest distance at which effect is disabled.",
    )
    TransformationArmorID: int = ParamField(
        int32, "transformProtectorId", game_type=ArmorParam, default=-1,
        tooltip="Transformation armor ID. Unknown effect. -1 is no armor.",
    )
    OngoingModelPoint: int = ParamField(
        int16, "midstDmyId", game_type=ModelDummy, default=-1,
        tooltip="Model point where ongoing effects are centered. -1 is model root.",
    )
    InitialModelPoint: int = ParamField(
        int16, "initDmyId", game_type=ModelDummy, default=-1,
        tooltip="Model point where initial effect is centered. -1 is model root.",
    )
    FinishModelPoint: int = ParamField(
        int16, "finishDmyId", game_type=ModelDummy, default=-1,
        tooltip="Model point where finish effect is centered. -1 is model root.",
    )
    EffectType: int = ParamField(
        uint8, "effectType", SP_EFFECT_VFX_EFFECT_TYPE, default=0,
        tooltip="Type of effect. Enum not yet mapped.",
    )
    WeaponEnchantmentSoulParam: int = ParamField(
        uint8, "soulParamIdForWepEnchant", SP_EFFECT_VFX_SOUL_PARAM_TYPE, default=0,
        tooltip="Internal description: 'Soul Param ID for weapon enchantment.' Enum not yet mapped.",
    )
    PlaybackCategory: int = ParamField(
        uint8, "playCategory", SP_EFFECT_VFX_PLAYCATEGORY, default=0,
        tooltip="Only one effect in each category can be active at once (determined by PlaybackPriority).",
    )
    PlaybackPriority: int = ParamField(
        uint8, "playPriority", default=0,
        tooltip="Only the lowest-numbered-priority effect in each PlaybackCategory will be active at once.",
    )
    LargeEffectExists: bool = ParamField(
        uint8, "existEffectForLarge:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Indicates if a large version of the effect exists.",
    )
    SoulEffectExists: bool = ParamField(
        uint8, "existEffectForSoul:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Indicates if a 'soul version' of the effect exists.",
    )
    InvisibleWhenHidden: bool = ParamField(
        uint8, "effectInvisibleAtCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Indicates if the effect should be invisible when hidden (unclear exactly what this means).",
    )
    HidingActive: bool = ParamField(
        uint8, "useCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="I believe this determines if the hiding range fields are actually used.",
    )
    InvisibleWhenFriendHidden: bool = ParamField(
        uint8, "invisibleAtFriendCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Unclear.",
    )
    AddMapAreaBlockOffset: bool = ParamField(
        uint8, "addMapAreaBlockOffset:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If enabled, the three-digit area/block number for the current map will be added to all effect IDs "
                "(e.g. m13_02 -> adds 132).",
    )
    HalfHiddenOnly: bool = ParamField(
        uint8, "halfCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If enabled, effects are made semi-transparent rather than fully hidden.",
    )
    ArmorTransformationIsFullBody: bool = ParamField(
        uint8, "isFullBodyTransformProtectorId:1", SP_EFFECT_BOOL, game_type=ArmorParam, bit_count=1, default=False,
        tooltip="Indicates whether the armor transformation should be applied to the whole body.",
    )
    HideWeapon: bool = ParamField(
        uint8, "isInvisibleWeapon:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Weapon is invisible if enabled.",
    )
    IsSilent: bool = ParamField(
        uint8, "isSilence:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Movement noises are silenced if enabled.",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad_1:6", bit_count=6)
    _Pad0: bytes = ParamPad(16, "pad[16]")
