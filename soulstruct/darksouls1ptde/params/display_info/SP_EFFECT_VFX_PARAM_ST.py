from __future__ import annotations

__all__ = ["SP_EFFECT_VFX_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *


SP_EFFECT_VFX_PARAM_ST = {
    "param_type": "SP_EFFECT_VFX_PARAM_ST",
    "file_name": "SpEffectVfxParam",
    "nickname": "SpecialEffectVisuals",
    "fields": [
        ParamFieldInfo(
            "effectType", "EffectType", True, SP_EFFECT_VFX_EFFECT_TYPE, "Type of effect. Enum not yet mapped."
        ),
        ParamFieldInfo(
            "midstSfxId",
            "OngoingVisualEffect",
            True,
            VisualEffect,
            "Ongoing visual effect for special effect. -1 is no effect.",
        ),
        ParamFieldInfo(
            "midstSeId",
            "OngoingSoundEffect",
            True,
            SFXSound,
            "Ongoing sound effect for special effect. -1 is no effect.",
        ),
        ParamFieldInfo(
            "midstDmyId",
            "OngoingModelPoint",
            True,
            int,
            "Model point where ongoing effects are centered. -1 is model root.",
        ),
        ParamFieldInfo(
            "initSfxId",
            "InitialVisualEffect",
            True,
            VisualEffect,
            "One-off visual effect when special effect begins. -1 is no effect.",
        ),
        ParamFieldInfo(
            "initSeId",
            "InitialSoundEffect",
            False,
            SFXSound,
            "One-off sound effect when special effect begins. -1 is no effect. (Does not appear to work.)",
        ),
        ParamFieldInfo(
            "initDmyId",
            "InitialModelPoint",
            True,
            int,
            "Model point where initial effect is centered. -1 is model root.",
        ),
        ParamFieldInfo(
            "finishSfxId",
            "FinishVisualEffect",
            True,
            VisualEffect,
            "One-off visual effect when special effect ends. -1 is no effect.",
        ),
        ParamFieldInfo(
            "finishSeId",
            "FinishSoundEffect",
            False,
            SFXSound,
            "One-off sound effect when special effect ends. -1 is no effect. (Does not appear to work.)",
        ),
        ParamFieldInfo(
            "finishDmyId",
            "FinishModelPoint",
            True,
            int,
            "Model point where finish effect is centered. -1 is model root.",
        ),
        ParamFieldInfo(
            "camouflageBeginDist", "HideStartDistance", True, float, "Closest distance at which effect is disabled."
        ),
        ParamFieldInfo(
            "camouflageEndDist", "HideEndDistance", True, float, "Furthest distance at which effect is disabled."
        ),
        ParamFieldInfo(
            "transformProtectorId",
            "TransformationArmorID",
            True,
            ArmorParam,
            "Transformation armor ID. Unknown effect. -1 is no armor.",
        ),
        ParamFieldInfo(
            "soulParamIdForWepEnchant",
            "WeaponEnchantmentSoulParam",
            True,
            SP_EFFECT_VFX_SOUL_PARAM_TYPE,
            "Internal description: 'Soul Param ID for weapon enchantment.' Enum not yet mapped.",
        ),
        ParamFieldInfo(
            "playCategory",
            "PlaybackCategory",
            True,
            SP_EFFECT_VFX_PLAYCATEGORY,
            "Only one effect in each category can be active at once (determined by PlaybackPriority).",
        ),
        ParamFieldInfo(
            "playPriority",
            "PlaybackPriority",
            True,
            int,
            "Only the lowest-numbered-priority effect in each PlaybackCategory will be active at once.",
        ),
        ParamFieldInfo(
            "existEffectForLarge:1",
            "LargeEffectExists",
            True,
            bool,
            "Indicates if a large version of the effect exists.",
        ),
        ParamFieldInfo(
            "existEffectForSoul:1",
            "SoulEffectExists",
            True,
            bool,
            "Indicates if a 'soul version' of the effect exists.",
        ),
        ParamFieldInfo(
            "effectInvisibleAtCamouflage:1",
            "InvisibleWhenHidden",
            True,
            bool,
            "Indicates if the effect should be invisible when hidden (unclear exactly what this means).",
        ),
        ParamFieldInfo(
            "useCamouflage:1",
            "HidingActive",
            True,
            bool,
            "I believe this determines if the hiding range fields are actually used.",
        ),
        ParamFieldInfo("invisibleAtFriendCamouflage:1", "InvisibleWhenFriendHidden", True, bool, "Unclear."),
        ParamFieldInfo(
            "addMapAreaBlockOffset:1",
            "AddMapAreaBlockOffset",
            True,
            bool,
            "If enabled, the three-digit area/block number for the current map will be added to all effect IDs ("
            "e.g. m13_02 -> adds 132).",
        ),
        ParamFieldInfo(
            "halfCamouflage:1",
            "HalfHiddenOnly",
            True,
            bool,
            "If enabled, effects are made semi-transparent rather than fully hidden.",
        ),
        ParamFieldInfo(
            "isFullBodyTransformProtectorId:1",
            "ArmorTransformationIsFullBody",
            True,
            bool,
            "Indicates whether the armor transformation should be applied to the whole body.",
        ),
        ParamFieldInfo("isInvisibleWeapon:1", "HideWeapon", True, bool, "Weapon is invisible if enabled."),
        ParamFieldInfo("isSilence:1", "IsSilent", True, bool, "Movement noises are silenced if enabled."),
        ParamFieldInfo("pad_1:6", "Pad1", False, bit_pad_field(6), "Null padding."),
        ParamFieldInfo("pad[16]", "Pad2", False, pad_field(16), "Null padding."),
    ],
}
