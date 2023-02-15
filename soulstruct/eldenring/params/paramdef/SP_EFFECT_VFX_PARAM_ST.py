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
    MidstSfxId: int = ParamField(
        int, "midstSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MidstSeId: int = ParamField(
        int, "midstSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InitSfxId: int = ParamField(
        int, "initSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InitSeId: int = ParamField(
        int, "initSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FinishSfxId: int = ParamField(
        int, "finishSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FinishSeId: int = ParamField(
        int, "finishSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CamouflageBeginDist: float = ParamField(
        float, "camouflageBeginDist", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    CamouflageEndDist: float = ParamField(
        float, "camouflageEndDist", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    TransformProtectorId: int = ParamField(
        int, "transformProtectorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MidstDmyId: int = ParamField(
        short, "midstDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InitDmyId: int = ParamField(
        short, "initDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FinishDmyId: int = ParamField(
        short, "finishDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EffectType: int = ParamField(
        byte, "effectType", SP_EFFECT_VFX_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoulParamIdForWepEnchant: int = ParamField(
        byte, "soulParamIdForWepEnchant", SP_EFFECT_VFX_SOUL_PARAM_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayCategory: int = ParamField(
        byte, "playCategory", SP_EFFECT_VFX_PLAYCATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayPriority: int = ParamField(
        byte, "playPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExistEffectForLarge: bool = ParamField(
        byte, "existEffectForLarge:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ExistEffectForSoul: bool = ParamField(
        byte, "existEffectForSoul:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EffectInvisibleAtCamouflage: bool = ParamField(
        byte, "effectInvisibleAtCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    UseCamouflage: bool = ParamField(
        byte, "useCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleAtFriendCamouflage: bool = ParamField(
        byte, "invisibleAtFriendCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHideFootEffectforCamouflage: bool = ParamField(
        byte, "isHideFootEffect_forCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HalfCamouflage: bool = ParamField(
        byte, "halfCamouflage:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFullBodyTransformProtectorId: bool = ParamField(
        byte, "isFullBodyTransformProtectorId:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInvisibleWeapon: bool = ParamField(
        byte, "isInvisibleWeapon:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSilence: bool = ParamField(
        byte, "isSilence:1", SP_EFFECT_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
