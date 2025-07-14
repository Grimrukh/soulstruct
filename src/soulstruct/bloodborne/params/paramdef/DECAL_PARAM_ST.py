from __future__ import annotations

__all__ = ["DECAL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
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
    RandomVariationCount: int = ParamField(
        uint32, "randomVariationNum:4", bit_count=4, default=0,
        tooltip="TODO",
    )
    ReplaceTextureIDWithMaterial: bool = ParamField(
        uint32, "replaceTextureId_byMaterial:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelPointCategory: int = ParamField(
        uint32, "dmypolyCategory:2", bit_count=2, default=0,
        tooltip="TODO",
    )
    DecalShapeType: int = ParamField(
        uint32, "decalShapeType:4", bit_count=4, default=0,
        tooltip="TODO",
    )
    UseDeferredDecal: bool = ParamField(
        uint32, "useDeferredDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    UsePaintDecal: bool = ParamField(
        uint32, "usePaintDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    TargetAttackingChr: bool = ParamField(
        uint32, "targetAttackChr:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    TargetDamagedChr: bool = ParamField(
        uint32, "targetDamageChr:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    TargetOtherChr: bool = ParamField(
        uint32, "targetOtherChr:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    TargetMapObject: bool = ParamField(
        uint32, "targetMapObj:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    UsePom: bool = ParamField(
        uint32, "usePom:1", bit_count=1, default=False,
        tooltip="TODO",
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
    _Pad0: bytes = ParamPad(14, "pad_00[14]")
