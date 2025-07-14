from __future__ import annotations

__all__ = ["DECAL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class DECAL_PARAM_ST(ParamRow):
    TextureID: int = ParamField(
        int, "textureId", default=-1,
        tooltip="TODO",
    )
    ModelPoint: int = ParamField(
        int, "dmypolyId", game_type=ModelDummy, default=-1,
        tooltip="TODO",
    )
    PitchAngle: float = ParamField(
        float, "pitchAngle", default=0.0,
        tooltip="TODO",
    )
    YawAngle: float = ParamField(
        float, "yawAngle", default=0.0,
        tooltip="TODO",
    )
    NearDistance: float = ParamField(
        float, "nearDistance", default=0.0,
        tooltip="TODO",
    )
    FarDistance: float = ParamField(
        float, "farDistance", default=0.0,
        tooltip="TODO",
    )
    NearSize: float = ParamField(
        float, "nearSize", default=0.0,
        tooltip="TODO",
    )
    FarSize: float = ParamField(
        float, "farSize", default=0.0,
        tooltip="TODO",
    )
    MaskSpecialEffectID: int = ParamField(
        int, "maskSpeffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    Pad10: int = ParamField(
        uint, "pad_10:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceTextureIDWithMaterial: bool = ParamField(
        uint, "replaceTextureId_byMaterial:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelPointCategory: int = ParamField(
        uint, "dmypolyCategory:2", bit_count=2, default=0,
        tooltip="TODO",
    )
    Pad05: int = ParamField(
        uint, "pad_05:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseDeferredDecal: bool = ParamField(
        uint, "useDeferredDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    UsePaintDecal: bool = ParamField(
        uint, "usePaintDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    BloodTypeEnable: bool = ParamField(
        uint, "bloodTypeEnable:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BUseNormal: bool = ParamField(
        uint, "bUseNormal:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Pad08: bool = ParamField(
        uint, "pad_08:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Pad09: bool = ParamField(
        uint, "pad_09:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    UsePom: bool = ParamField(
        uint, "usePom:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    UseEmissive: bool = ParamField(
        uint, "useEmissive:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    PutVertical: bool = ParamField(
        uint, "putVertical:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RandomSizeMin: int = ParamField(
        short, "randomSizeMin", default=100,
        tooltip="TODO",
    )
    RandomSizeMax: int = ParamField(
        short, "randomSizeMax", default=100,
        tooltip="TODO",
    )
    RandomRollMin: float = ParamField(
        float, "randomRollMin", default=0.0,
        tooltip="TODO",
    )
    RandomRollMax: float = ParamField(
        float, "randomRollMax", default=0.0,
        tooltip="TODO",
    )
    RandomPitchMin: float = ParamField(
        float, "randomPitchMin", default=0.0,
        tooltip="TODO",
    )
    RandomPitchMax: float = ParamField(
        float, "randomPitchMax", default=0.0,
        tooltip="TODO",
    )
    RandomYawMin: float = ParamField(
        float, "randomYawMin", default=0.0,
        tooltip="TODO",
    )
    RandomYawMax: float = ParamField(
        float, "randomYawMax", default=0.0,
        tooltip="TODO",
    )
    PomHeightScale: float = ParamField(
        float, "pomHightScale", default=1.0,
        tooltip="TODO",
    )
    PomSampleMin: int = ParamField(
        byte, "pomSampleMin", default=8,
        tooltip="TODO",
    )
    PomSampleMax: int = ParamField(
        byte, "pomSampleMax", default=64,
        tooltip="TODO",
    )
    BlendMode: int = ParamField(
        sbyte, "blendMode", DECAL_PARAM_BLEND_MODE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    AppearDirType: int = ParamField(
        sbyte, "appearDirType", DECAL_PARAM_DIR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveValueBegin: float = ParamField(
        float, "emissiveValueBegin", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveValueEnd: float = ParamField(
        float, "emissiveValueEnd", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EmissiveTime: float = ParamField(
        float, "emissiveTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BIntpEnable: int = ParamField(
        byte, "bIntpEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad_01[3]")
    IntpIntervalDist: float = ParamField(
        float, "intpIntervalDist", default=0.1,
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
        float, "maskScale", default=1.0,
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
        byte, "bLifeEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SiniScale: float = ParamField(
        float, "siniScale", default=1.0,
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
        byte, "bDistThinOutEnable", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BAlignedTexRandomVariationEnable: int = ParamField(
        byte, "bAlignedTexRandomVariationEnable", BOOL_YESNO_TYPE, default=0,
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
        uint, "randVaria_Diffuse:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaMask: int = ParamField(
        uint, "randVaria_Mask:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaReflec: int = ParamField(
        uint, "randVaria_Reflec:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad12: int = ParamField(
        uint, "pad_12:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaNormal: int = ParamField(
        uint, "randVaria_Normal:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaHeight: int = ParamField(
        uint, "randVaria_Height:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RandVariaEmissive: int = ParamField(
        uint, "randVaria_Emissive:4", bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Pad11: int = ParamField(
        uint, "pad_11:4", bit_count=4, default=0,
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
        sbyte, "thinOutMode", DECAL_PARAM_THIN_OUT_MODE, default=0,
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
        float, "maxDecalSfxCreatableSlopeAngleDeg", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(40, "pad_02[40]")
