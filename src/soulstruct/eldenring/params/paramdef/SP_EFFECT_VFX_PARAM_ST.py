from __future__ import annotations

__all__ = ["SP_EFFECT_VFX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
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
    IsHideFootEffectforCamouflage: bool = ParamField(
        uint8, "isHideFootEffect_forCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HalfHiddenOnly: bool = ParamField(
        uint8, "halfCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="If enabled, effects are made semi-transparent rather than fully hidden.",
    )
    IsFullBodyTransformProtectorId: bool = ParamField(
        uint8, "isFullBodyTransformProtectorId:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HideWeapon: bool = ParamField(
        uint8, "isInvisibleWeapon:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Weapon is invisible if enabled.",
    )
    IsSilent: bool = ParamField(
        uint8, "isSilence:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="Movement noises are silenced if enabled.",
    )
    IsMidstFullbody: bool = ParamField(
        uint8, "isMidstFullbody:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInitFullbody: bool = ParamField(
        uint8, "isInitFullbody:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFinishFullbody: bool = ParamField(
        uint8, "isFinishFullbody:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsVisibleDeadChr: bool = ParamField(
        uint8, "isVisibleDeadChr:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseOffsetEnchantSfxSize: bool = ParamField(
        uint8, "isUseOffsetEnchantSfxSize:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x2f7: bool = ParamField(
        uint8, "unknown_0x2f_7:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DecalId1: int = ParamField(
        int32, "decalId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalId2: int = ParamField(
        int32, "decalId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FootEffectPriority: int = ParamField(
        uint8, "footEffectPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootEffectOffset: int = ParamField(
        uint8, "footEffectOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxIdOffsetType: int = ParamField(
        uint8, "traceSfxIdOffsetType", SP_EFFECT_VFX_SOUL_PARAM_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForceDeceasedType: int = ParamField(
        uint8, "forceDeceasedType", SP_EFFECT_VFX_FORCE_DECEASED_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId0: int = ParamField(
        int32, "enchantStartDmyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId0: int = ParamField(
        int32, "enchantEndDmyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId1: int = ParamField(
        int32, "enchantStartDmyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId1: int = ParamField(
        int32, "enchantEndDmyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId2: int = ParamField(
        int32, "enchantStartDmyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId2: int = ParamField(
        int32, "enchantEndDmyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId3: int = ParamField(
        int32, "enchantStartDmyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId3: int = ParamField(
        int32, "enchantEndDmyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId4: int = ParamField(
        int32, "enchantStartDmyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId4: int = ParamField(
        int32, "enchantEndDmyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId5: int = ParamField(
        int32, "enchantStartDmyId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId5: int = ParamField(
        int32, "enchantEndDmyId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId6: int = ParamField(
        int32, "enchantStartDmyId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId6: int = ParamField(
        int32, "enchantEndDmyId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantStartDmyId7: int = ParamField(
        int32, "enchantStartDmyId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnchantEndDmyId7: int = ParamField(
        int32, "enchantEndDmyId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxIdOffsetType: int = ParamField(
        uint8, "SfxIdOffsetType", SP_EFFECT_VFX_SFX_ID_OFFSET_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamOverwriteType: int = ParamField(
        uint8, "phantomParamOverwriteType", SP_EFFECT_OVERWRITE_PHANTOM_PARAM_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamouflageMinAlpha: int = ParamField(
        uint8, "camouflageMinAlpha", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WetAspectType: int = ParamField(
        uint8, "wetAspectType", SP_EFFECT_VFX_WET_ASPECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamOverwriteId: int = ParamField(
        int32, "phantomParamOverwriteId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamId: int = ParamField(
        int32, "materialParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamInitValue: float = ParamField(
        float32, "materialParamInitValue", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamTargetValue: float = ParamField(
        float32, "materialParamTargetValue", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamFadeTime: float = ParamField(
        float32, "materialParamFadeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FootDecalMaterialOffsetOverwriteId: int = ParamField(
        int16, "footDecalMaterialOffsetOverwriteId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x96: int = ParamField(
        uint8, "unknown_0x96", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x97: int = ParamField(
        uint8, "unknown_0x97", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x98: int = ParamField(
        uint8, "unknown_0x98", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x99: int = ParamField(
        uint8, "unknown_0x99", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x9a: int = ParamField(
        uint8, "unknown_0x9a", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(9, "pad[9]")
