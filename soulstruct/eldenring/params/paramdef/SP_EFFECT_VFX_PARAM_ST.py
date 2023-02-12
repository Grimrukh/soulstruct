from __future__ import annotations

__all__ = ["SP_EFFECT_VFX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SP_EFFECT_VFX_PARAM_ST(ParamRowData):
    OngoingVisualEffect: int = ParamField(
        int, "midstSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OngoingSoundEffect: int = ParamField(
        int, "midstSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InitialVisualEffect: int = ParamField(
        int, "initSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InitialSoundEffect: int = ParamField(
        int, "initSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FinishVisualEffect: int = ParamField(
        int, "finishSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FinishSoundEffect: int = ParamField(
        int, "finishSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HideStartDistance: float = ParamField(
        float, "camouflageBeginDist", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HideEndDistance: float = ParamField(
        float, "camouflageEndDist", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TransformationArmorID: int = ParamField(
        int, "transformProtectorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OngoingModelPoint: int = ParamField(
        short, "midstDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InitialModelPoint: int = ParamField(
        short, "initDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FinishModelPoint: int = ParamField(
        short, "finishDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EffectType: int = ParamField(
        byte, "effectType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponEnchantmentSoulParam: int = ParamField(
        byte, "soulParamIdForWepEnchant", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlaybackCategory: int = ParamField(
        byte, "playCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlaybackPriority: int = ParamField(
        byte, "playPriority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LargeEffectExists: int = ParamField(
        byte, "existEffectForLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoulEffectExists: int = ParamField(
        byte, "existEffectForSoul:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleWhenHidden: int = ParamField(
        byte, "effectInvisibleAtCamouflage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HidingActive: int = ParamField(
        byte, "useCamouflage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleWhenFriendHidden: int = ParamField(
        byte, "invisibleAtFriendCamouflage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHideFootEffectforCamouflage: int = ParamField(
        byte, "isHideFootEffect_forCamouflage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HalfHiddenOnly: int = ParamField(
        byte, "halfCamouflage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFullBodyTransformProtectorId: int = ParamField(
        byte, "isFullBodyTransformProtectorId:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HideWeapon: int = ParamField(
        byte, "isInvisibleWeapon:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSilent: int = ParamField(
        byte, "isSilence:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMidstFullbody: int = ParamField(
        byte, "isMidstFullbody:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsInitFullbody: int = ParamField(
        byte, "isInitFullbody:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFinishFullbody: int = ParamField(
        byte, "isFinishFullbody:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsVisibleDeadChr: int = ParamField(
        byte, "isVisibleDeadChr:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUseOffsetEnchantSfxSize: int = ParamField(
        byte, "isUseOffsetEnchantSfxSize:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad_1:1")
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
        byte, "traceSfxIdOffsetType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForceDeceasedType: int = ParamField(
        byte, "forceDeceasedType", default=0,
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
        byte, "SfxIdOffsetType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamOverwriteType: int = ParamField(
        byte, "phantomParamOverwriteType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamouflageMinAlpha: int = ParamField(
        byte, "camouflageMinAlpha", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WetAspectType: int = ParamField(
        byte, "wetAspectType", default=0,
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
    _Pad1: bytes = ParamPad(14, "pad[14]")
