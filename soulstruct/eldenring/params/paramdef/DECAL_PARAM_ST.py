from __future__ import annotations

__all__ = ["DECAL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class DECAL_PARAM_ST(ParamRowData):
    TextureID: int = ParamField(
        int, "textureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ModelPoint: int = ParamField(
        int, "dmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PitchAngle: float = ParamField(
        float, "pitchAngle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    YawAngle: float = ParamField(
        float, "yawAngle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NearDistance: float = ParamField(
        float, "nearDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FarDistance: float = ParamField(
        float, "farDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NearSize: float = ParamField(
        float, "nearSize", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FarSize: float = ParamField(
        float, "farSize", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaskSpecialEffectID: int = ParamField(
        int, "maskSpeffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Pad10: int = ParamField(
        uint, "pad_10:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceTextureIDWithMaterial: int = ParamField(
        uint, "replaceTextureId_byMaterial:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelPointCategory: int = ParamField(
        uint, "dmypolyCategory:2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad05: int = ParamField(
        uint, "pad_05:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseDeferredDecal: int = ParamField(
        uint, "useDeferredDecal:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    UsePaintDecal: int = ParamField(
        uint, "usePaintDecal:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BloodTypeEnable: int = ParamField(
        uint, "bloodTypeEnable:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BUseNormal: int = ParamField(
        uint, "bUseNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad08: int = ParamField(
        uint, "pad_08:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad09: int = ParamField(
        uint, "pad_09:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsePom: int = ParamField(
        uint, "usePom:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseEmissive: int = ParamField(
        uint, "useEmissive:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PutVertical: int = ParamField(
        uint, "putVertical:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandomSizeMin: int = ParamField(
        short, "randomSizeMin", default=100,
        tooltip="TOOLTIP-TODO",
    )
    RandomSizeMax: int = ParamField(
        short, "randomSizeMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    RandomRollMin: float = ParamField(
        float, "randomRollMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RandomRollMax: float = ParamField(
        float, "randomRollMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RandomPitchMin: float = ParamField(
        float, "randomPitchMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RandomPitchMax: float = ParamField(
        float, "randomPitchMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RandomYawMin: float = ParamField(
        float, "randomYawMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RandomYawMax: float = ParamField(
        float, "randomYawMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PomHeightScale: float = ParamField(
        float, "pomHightScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PomSampleMin: int = ParamField(
        byte, "pomSampleMin", default=8,
        tooltip="TOOLTIP-TODO",
    )
    PomSampleMax: int = ParamField(
        byte, "pomSampleMax", default=64,
        tooltip="TOOLTIP-TODO",
    )
    BlendMode: int = ParamField(
        sbyte, "blendMode", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AppearDirType: int = ParamField(
        sbyte, "appearDirType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveValueBegin: float = ParamField(
        float, "emissiveValueBegin", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveValueEnd: float = ParamField(
        float, "emissiveValueEnd", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveTime: float = ParamField(
        float, "emissiveTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BIntpEnable: int = ParamField(
        byte, "bIntpEnable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad_01[3]")
    IntpIntervalDist: float = ParamField(
        float, "intpIntervalDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BeginIntpTextureId: int = ParamField(
        int, "beginIntpTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EndIntpTextureId: int = ParamField(
        int, "endIntpTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AppearSfxId: int = ParamField(
        int, "appearSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AppearSfxOffsetPos: float = ParamField(
        float, "appearSfxOffsetPos", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaskTextureId: int = ParamField(
        int, "maskTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseTextureId: int = ParamField(
        int, "diffuseTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReflecTextureId: int = ParamField(
        int, "reflecTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaskScale: float = ParamField(
        float, "maskScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    NormalTextureId: int = ParamField(
        int, "normalTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HeightTextureId: int = ParamField(
        int, "heightTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveTextureId: int = ParamField(
        int, "emissiveTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseColorR: int = ParamField(
        byte, "diffuseColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseColorG: int = ParamField(
        byte, "diffuseColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseColorB: int = ParamField(
        byte, "diffuseColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad_03[1]")
    ReflecColorR: int = ParamField(
        byte, "reflecColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ReflecColorG: int = ParamField(
        byte, "reflecColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ReflecColorB: int = ParamField(
        byte, "reflecColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    BLifeEnable: int = ParamField(
        byte, "bLifeEnable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SiniScale: float = ParamField(
        float, "siniScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeSec: float = ParamField(
        float, "lifeTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FadeOutTimeSec: float = ParamField(
        float, "fadeOutTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Priority: int = ParamField(
        short, "priority", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BDistThinOutEnable: int = ParamField(
        byte, "bDistThinOutEnable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BAlignedTexRandomVariationEnable: int = ParamField(
        byte, "bAlignedTexRandomVariationEnable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutCheckDist: float = ParamField(
        float, "distThinOutCheckDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutCheckAngleDeg: float = ParamField(
        float, "distThinOutCheckAngleDeg", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutMaxNum: int = ParamField(
        byte, "distThinOutMaxNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutCheckNum: int = ParamField(
        byte, "distThinOutCheckNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DelayAppearFrame: int = ParamField(
        short, "delayAppearFrame", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaDiffuse: int = ParamField(
        uint, "randVaria_Diffuse:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaMask: int = ParamField(
        uint, "randVaria_Mask:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaReflec: int = ParamField(
        uint, "randVaria_Reflec:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad12: int = ParamField(
        uint, "pad_12:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaNormal: int = ParamField(
        uint, "randVaria_Normal:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaHeight: int = ParamField(
        uint, "randVaria_Height:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaEmissive: int = ParamField(
        uint, "randVaria_Emissive:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad11: int = ParamField(
        uint, "pad_11:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FadeInTimeSec: float = ParamField(
        float, "fadeInTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutOverlapMultiRadius: float = ParamField(
        float, "thinOutOverlapMultiRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutNeighborAddRadius: float = ParamField(
        float, "thinOutNeighborAddRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutOverlapLimitNum: int = ParamField(
        uint, "thinOutOverlapLimitNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutNeighborLimitNum: int = ParamField(
        uint, "thinOutNeighborLimitNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutMode: int = ParamField(
        sbyte, "thinOutMode", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveColorR: int = ParamField(
        byte, "emissiveColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveColorG: int = ParamField(
        byte, "emissiveColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveColorB: int = ParamField(
        byte, "emissiveColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    MaxDecalSfxCreatableSlopeAngleDeg: float = ParamField(
        float, "maxDecalSfxCreatableSlopeAngleDeg", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(40, "pad_02[40]")
