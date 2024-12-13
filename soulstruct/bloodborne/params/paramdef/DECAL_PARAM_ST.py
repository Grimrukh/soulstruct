from __future__ import annotations

__all__ = ["DECAL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
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
    RandomVariationCount: int = ParamField(
        uint, "randomVariationNum:4", bit_count=4, default=0,
        tooltip="TODO",
    )
    ReplaceTextureIDWithMaterial: bool = ParamField(
        uint, "replaceTextureId_byMaterial:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelPointCategory: int = ParamField(
        uint, "dmypolyCategory:2", bit_count=2, default=0,
        tooltip="TODO",
    )
    DecalShapeType: int = ParamField(
        uint, "decalShapeType:4", bit_count=4, default=0,
        tooltip="TODO",
    )
    UseDeferredDecal: bool = ParamField(
        uint, "useDeferredDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    UsePaintDecal: bool = ParamField(
        uint, "usePaintDecal:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    TargetAttackingChr: bool = ParamField(
        uint, "targetAttackChr:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    TargetDamagedChr: bool = ParamField(
        uint, "targetDamageChr:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    TargetOtherChr: bool = ParamField(
        uint, "targetOtherChr:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    TargetMapObject: bool = ParamField(
        uint, "targetMapObj:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    UsePom: bool = ParamField(
        uint, "usePom:1", bit_count=1, default=False,
        tooltip="TODO",
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
    _Pad0: bytes = ParamPad(14, "pad_00[14]")
