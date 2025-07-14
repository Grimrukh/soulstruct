from __future__ import annotations

__all__ = ["GRASS_TYPE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class GRASS_TYPE_PARAM_ST(ParamRow):
    LodRange: int = ParamField(
        uint16, "lodRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Lod0ClusterType: int = ParamField(
        uint8, "lod0ClusterType", GRASS_CLUSTER_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Lod1ClusterType: int = ParamField(
        uint8, "lod1ClusterType", GRASS_CLUSTER_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Lod2ClusterType: int = ParamField(
        uint8, "lod2ClusterType", GRASS_CLUSTER_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad0[2]")
    DistributionType: int = ParamField(
        uint8, "distributionType", GRASS_DISTRIBUTION_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDensity: float = ParamField(
        float32, "baseDensity", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Model0Name: str = ParamField(
        str, "model0Name[16]", encoding="utf-16", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    FlatTextureName: str = ParamField(
        str, "flatTextureName[32]", encoding="utf-16", length=64, default='',
        tooltip="TOOLTIP-TODO",
    )
    BillboardTextureName: str = ParamField(
        str, "billboardTextureName[32]", encoding="utf-16", length=64, default='',
        tooltip="TOOLTIP-TODO",
    )
    NormalInfluence: int = ParamField(
        uint8, "normalInfluence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InclinationMax: int = ParamField(
        uint8, "inclinationMax", default=90,
        tooltip="TOOLTIP-TODO",
    )
    InclinationJitter: int = ParamField(
        uint8, "inclinationJitter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ScaleBaseMin: int = ParamField(
        uint8, "scaleBaseMin", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ScaleBaseMax: int = ParamField(
        uint8, "scaleBaseMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ScaleHeightMin: int = ParamField(
        uint8, "scaleHeightMin", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ScaleHeightMax: int = ParamField(
        uint8, "scaleHeightMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade1r: int = ParamField(
        uint8, "colorShade1_r", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade1g: int = ParamField(
        uint8, "colorShade1_g", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade1b: int = ParamField(
        uint8, "colorShade1_b", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade2r: int = ParamField(
        uint8, "colorShade2_r", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade2g: int = ParamField(
        uint8, "colorShade2_g", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade2b: int = ParamField(
        uint8, "colorShade2_b", default=255,
        tooltip="TOOLTIP-TODO",
    )
    FlatSplitType: int = ParamField(
        uint8, "flatSplitType", GRASS_FLAT_SPLIT_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlatBladeCount: int = ParamField(
        uint8, "flatBladeCount", default=2,
        tooltip="TOOLTIP-TODO",
    )
    FlatSlant: int = ParamField(
        int8, "flatSlant", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlatRadius: float = ParamField(
        float32, "flatRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CastShadow: int = ParamField(
        uint8, "castShadow", GRASS_SHADOW_TYPE_ENUM, default=1,
        tooltip="TOOLTIP-TODO",
    )
    WindAmplitude: int = ParamField(
        uint8, "windAmplitude", default=80,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    WindCycle: int = ParamField(
        uint8, "windCycle", default=40,
        tooltip="TOOLTIP-TODO",
    )
    OrientationAngle: float = ParamField(
        float32, "orientationAngle", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    OrientationRange: float = ParamField(
        float32, "orientationRange", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    Spacing: float = ParamField(
        float32, "spacing", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Dithering: int = ParamField(
        uint8, "dithering", GRASS_DITHERING_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(3, "pad[3]")
    SimpleModelName: str = ParamField(
        str, "simpleModelName[16]", encoding="utf-16", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    Model1Name: str = ParamField(
        str, "model1Name[16]", encoding="utf-16", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
