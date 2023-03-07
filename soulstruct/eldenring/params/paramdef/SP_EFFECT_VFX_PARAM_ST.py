from __future__ import annotations

__all__ = ["SP_EFFECT_VFX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
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
    IsHideFootEffectforCamouflage: bool = ParamField(
        byte, "isHideFootEffect_forCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HalfHiddenOnly: bool = ParamField(
        byte, "halfCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If enabled, effects are made semi-transparent rather than fully hidden.",
    )
    IsFullBodyTransformProtectorId: bool = ParamField(
        byte, "isFullBodyTransformProtectorId:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HideWeapon: bool = ParamField(
        byte, "isInvisibleWeapon:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Weapon is invisible if enabled.",
    )
    IsSilent: bool = ParamField(
        byte, "isSilence:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Movement noises are silenced if enabled.",
    )
    IsMidstFullbody: bool = ParamField(
        byte, "isMidstFullbody:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInitFullbody: bool = ParamField(
        byte, "isInitFullbody:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFinishFullbody: bool = ParamField(
        byte, "isFinishFullbody:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsVisibleDeadChr: bool = ParamField(
        byte, "isVisibleDeadChr:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseOffsetEnchantSfxSize: bool = ParamField(
        byte, "isUseOffsetEnchantSfxSize:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad_1:1", bit_count=1)
    DecalId1: int = ParamField(
        int, "decalId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalId2: int = ParamField(
        int, "decalId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FootEffectPriority: int = ParamField(
        byte, "footEffectPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootEffectOffset: int = ParamField(
        byte, "footEffectOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxIdOffsetType: int = ParamField(
        byte, "traceSfxIdOffsetType", SP_EFFECT_VFX_SOUL_PARAM_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForceDeceasedType: int = ParamField(
        byte, "forceDeceasedType", SP_EFFECT_VFX_FORCE_DECEASED_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId0: int = ParamField(
        int, "enchantStartDmyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId0: int = ParamField(
        int, "enchantEndDmyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId1: int = ParamField(
        int, "enchantStartDmyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId1: int = ParamField(
        int, "enchantEndDmyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId2: int = ParamField(
        int, "enchantStartDmyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId2: int = ParamField(
        int, "enchantEndDmyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId3: int = ParamField(
        int, "enchantStartDmyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId3: int = ParamField(
        int, "enchantEndDmyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId4: int = ParamField(
        int, "enchantStartDmyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId4: int = ParamField(
        int, "enchantEndDmyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId5: int = ParamField(
        int, "enchantStartDmyId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId5: int = ParamField(
        int, "enchantEndDmyId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId6: int = ParamField(
        int, "enchantStartDmyId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId6: int = ParamField(
        int, "enchantEndDmyId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId7: int = ParamField(
        int, "enchantStartDmyId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId7: int = ParamField(
        int, "enchantEndDmyId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdOffsetType: int = ParamField(
        byte, "SfxIdOffsetType", SP_EFFECT_VFX_SFX_ID_OFFSET_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamOverwriteType: int = ParamField(
        byte, "phantomParamOverwriteType", SP_EFFECT_OVERWRITE_PHANTOM_PARAM_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamouflageMinAlpha: int = ParamField(
        byte, "camouflageMinAlpha", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WetAspectType: int = ParamField(
        byte, "wetAspectType", SP_EFFECT_VFX_WET_ASPECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamOverwriteId: int = ParamField(
        int, "phantomParamOverwriteId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamId: int = ParamField(
        int, "materialParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamInitValue: float = ParamField(
        float, "materialParamInitValue", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamTargetValue: float = ParamField(
        float, "materialParamTargetValue", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamFadeTime: float = ParamField(
        float, "materialParamFadeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FootDecalMaterialOffsetOverwriteId: int = ParamField(
        short, "footDecalMaterialOffsetOverwriteId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(14, "pad[14]")
