from __future__ import annotations

__all__ = ["DECAL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class DECAL_PARAM_ST(ParamRow):
    TextureID: int = ParamField(
        int32, "textureId", default=-1,
        tooltip="TODO",
    )
    ModelPoint: int = ParamField(
        int32, "dmypolyId", game_type=ModelDummy, default=-1,
        tooltip="TODO",
    )
    PitchAngle: float = ParamField(
        float32, "pitchAngle", default=0.0,
        tooltip="TODO",
    )
    YawAngle: float = ParamField(
        float32, "yawAngle", default=0.0,
        tooltip="TODO",
    )
    NearDistance: float = ParamField(
        float32, "nearDistance", default=0.0,
        tooltip="TODO",
    )
    FarDistance: float = ParamField(
        float32, "farDistance", default=0.0,
        tooltip="TODO",
    )
    NearSize: float = ParamField(
        float32, "nearSize", default=0.0,
        tooltip="TODO",
    )
    FarSize: float = ParamField(
        float32, "farSize", default=0.0,
        tooltip="TODO",
    )
    MaskSpecialEffectID: int = ParamField(
        int32, "maskSpeffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    Pad10: int = ParamField(
        uint32, "pad_10:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceTextureIDWithMaterial: bool = ParamField(
        uint32, "replaceTextureId_byMaterial:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelPointCategory: int = ParamField(
        uint32, "dmypolyCategory:2", bit_count=2, default=0,
        tooltip="TODO",
    )
    Pad05: int = ParamField(
        uint32, "pad_05:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseDeferredDecal: bool = ParamField(
        uint32, "useDeferredDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    UsePaintDecal: bool = ParamField(
        uint32, "usePaintDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    BloodTypeEnable: bool = ParamField(
        uint32, "bloodTypeEnable:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BUseNormal: bool = ParamField(
        uint32, "bUseNormal:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Pad08: bool = ParamField(
        uint32, "pad_08:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Pad09: bool = ParamField(
        uint32, "pad_09:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    UsePom: bool = ParamField(
        uint32, "usePom:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    UseEmissive: bool = ParamField(
        uint32, "useEmissive:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    PutVertical: bool = ParamField(
        uint32, "putVertical:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RandomSizeMin: int = ParamField(
        int16, "randomSizeMin", default=100,
        tooltip="TODO",
    )
    RandomSizeMax: int = ParamField(
        int16, "randomSizeMax", default=100,
        tooltip="TODO",
    )
    RandomRollMin: float = ParamField(
        float32, "randomRollMin", default=0.0,
        tooltip="TODO",
    )
    RandomRollMax: float = ParamField(
        float32, "randomRollMax", default=0.0,
        tooltip="TODO",
    )
    RandomPitchMin: float = ParamField(
        float32, "randomPitchMin", default=0.0,
        tooltip="TODO",
    )
    RandomPitchMax: float = ParamField(
        float32, "randomPitchMax", default=0.0,
        tooltip="TODO",
    )
    RandomYawMin: float = ParamField(
        float32, "randomYawMin", default=0.0,
        tooltip="TODO",
    )
    RandomYawMax: float = ParamField(
        float32, "randomYawMax", default=0.0,
        tooltip="TODO",
    )
    PomHeightScale: float = ParamField(
        float32, "pomHightScale", default=1.0,
        tooltip="TODO",
    )
    PomSampleMin: int = ParamField(
        uint8, "pomSampleMin", default=8,
        tooltip="TODO",
    )
    PomSampleMax: int = ParamField(
        uint8, "pomSampleMax", default=64,
        tooltip="TODO",
    )
    BlendMode: int = ParamField(
        int8, "blendMode", DECAL_PARAM_BLEND_MODE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    AppearDirType: int = ParamField(
        int8, "appearDirType", DECAL_PARAM_DIR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveValueBegin: float = ParamField(
        float32, "emissiveValueBegin", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveValueEnd: float = ParamField(
        float32, "emissiveValueEnd", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveTime: float = ParamField(
        float32, "emissiveTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BIntpEnable: int = ParamField(
        uint8, "bIntpEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad_01[3]")
    IntpIntervalDist: float = ParamField(
        float32, "intpIntervalDist", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    BeginIntpTextureId: int = ParamField(
        int32, "beginIntpTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EndIntpTextureId: int = ParamField(
        int32, "endIntpTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AppearSfxId: int = ParamField(
        int32, "appearSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AppearSfxOffsetPos: float = ParamField(
        float32, "appearSfxOffsetPos", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaskTextureId: int = ParamField(
        int32, "maskTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseTextureId: int = ParamField(
        int32, "diffuseTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReflecTextureId: int = ParamField(
        int32, "reflecTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaskScale: float = ParamField(
        float32, "maskScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NormalTextureId: int = ParamField(
        int32, "normalTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HeightTextureId: int = ParamField(
        int32, "heightTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveTextureId: int = ParamField(
        int32, "emissiveTextureId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseColorR: int = ParamField(
        uint8, "diffuseColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseColorG: int = ParamField(
        uint8, "diffuseColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffuseColorB: int = ParamField(
        uint8, "diffuseColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad_03[1]")
    ReflecColorR: int = ParamField(
        uint8, "reflecColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ReflecColorG: int = ParamField(
        uint8, "reflecColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ReflecColorB: int = ParamField(
        uint8, "reflecColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    BLifeEnable: int = ParamField(
        uint8, "bLifeEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SiniScale: float = ParamField(
        float32, "siniScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeSec: float = ParamField(
        float32, "lifeTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FadeOutTimeSec: float = ParamField(
        float32, "fadeOutTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Priority: int = ParamField(
        int16, "priority", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BDistThinOutEnable: int = ParamField(
        uint8, "bDistThinOutEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BAlignedTexRandomVariationEnable: int = ParamField(
        uint8, "bAlignedTexRandomVariationEnable", BOOL_YESNO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutCheckDist: float = ParamField(
        float32, "distThinOutCheckDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutCheckAngleDeg: float = ParamField(
        float32, "distThinOutCheckAngleDeg", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutMaxNum: int = ParamField(
        uint8, "distThinOutMaxNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DistThinOutCheckNum: int = ParamField(
        uint8, "distThinOutCheckNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DelayAppearFrame: int = ParamField(
        int16, "delayAppearFrame", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaDiffuse: int = ParamField(
        uint32, "randVaria_Diffuse:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaMask: int = ParamField(
        uint32, "randVaria_Mask:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaReflec: int = ParamField(
        uint32, "randVaria_Reflec:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad12: int = ParamField(
        uint32, "pad_12:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaNormal: int = ParamField(
        uint32, "randVaria_Normal:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaHeight: int = ParamField(
        uint32, "randVaria_Height:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaEmissive: int = ParamField(
        uint32, "randVaria_Emissive:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad11: int = ParamField(
        uint32, "pad_11:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FadeInTimeSec: float = ParamField(
        float32, "fadeInTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutOverlapMultiRadius: float = ParamField(
        float32, "thinOutOverlapMultiRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutNeighborAddRadius: float = ParamField(
        float32, "thinOutNeighborAddRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutOverlapLimitNum: int = ParamField(
        uint32, "thinOutOverlapLimitNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutNeighborLimitNum: int = ParamField(
        uint32, "thinOutNeighborLimitNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThinOutMode: int = ParamField(
        int8, "thinOutMode", DECAL_PARAM_THIN_OUT_MODE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveColorR: int = ParamField(
        uint8, "emissiveColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveColorG: int = ParamField(
        uint8, "emissiveColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveColorB: int = ParamField(
        uint8, "emissiveColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    MaxDecalSfxCreatableSlopeAngleDeg: float = ParamField(
        float32, "maxDecalSfxCreatableSlopeAngleDeg", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(40, "pad_02[40]")
