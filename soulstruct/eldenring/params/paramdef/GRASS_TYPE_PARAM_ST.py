from __future__ import annotations

__all__ = ["GRASS_TYPE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GRASS_TYPE_PARAM_ST(ParamRow):
    LodRange: int = ParamField(
        ushort, "lodRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Lod0ClusterType: int = ParamField(
        byte, "lod0ClusterType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Lod1ClusterType: int = ParamField(
        byte, "lod1ClusterType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Lod2ClusterType: int = ParamField(
        byte, "lod2ClusterType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad0[2]")
    DistributionType: int = ParamField(
        byte, "distributionType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDensity: float = ParamField(
        float, "baseDensity", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Model0Name: bytes = ParamField(
        bytes, "model0Name[16]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    FlatTextureName: bytes = ParamField(
        bytes, "flatTextureName[32]", length=64, default='',
        tooltip="TOOLTIP-TODO",
    )
    BillboardTextureName: bytes = ParamField(
        bytes, "billboardTextureName[32]", length=64, default='',
        tooltip="TOOLTIP-TODO",
    )
    NormalInfluence: int = ParamField(
        byte, "normalInfluence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InclinationMax: int = ParamField(
        byte, "inclinationMax", default=90,
        tooltip="TOOLTIP-TODO",
    )
    InclinationJitter: int = ParamField(
        byte, "inclinationJitter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ScaleBaseMin: int = ParamField(
        byte, "scaleBaseMin", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ScaleBaseMax: int = ParamField(
        byte, "scaleBaseMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ScaleHeightMin: int = ParamField(
        byte, "scaleHeightMin", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ScaleHeightMax: int = ParamField(
        byte, "scaleHeightMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade1r: int = ParamField(
        byte, "colorShade1_r", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade1g: int = ParamField(
        byte, "colorShade1_g", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade1b: int = ParamField(
        byte, "colorShade1_b", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade2r: int = ParamField(
        byte, "colorShade2_r", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade2g: int = ParamField(
        byte, "colorShade2_g", default=255,
        tooltip="TOOLTIP-TODO",
    )
    ColorShade2b: int = ParamField(
        byte, "colorShade2_b", default=255,
        tooltip="TOOLTIP-TODO",
    )
    FlatSplitType: int = ParamField(
        byte, "flatSplitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlatBladeCount: int = ParamField(
        byte, "flatBladeCount", default=2,
        tooltip="TOOLTIP-TODO",
    )
    FlatSlant: int = ParamField(
        sbyte, "flatSlant", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlatRadius: float = ParamField(
        float, "flatRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CastShadow: int = ParamField(
        byte, "castShadow", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WindAmplitude: int = ParamField(
        byte, "windAmplitude", default=80,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    WindCycle: int = ParamField(
        byte, "windCycle", default=40,
        tooltip="TOOLTIP-TODO",
    )
    OrientationAngle: float = ParamField(
        float, "orientationAngle", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OrientationRange: float = ParamField(
        float, "orientationRange", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Spacing: float = ParamField(
        float, "spacing", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Dithering: int = ParamField(
        byte, "dithering", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(3, "pad[3]")
    SimpleModelName: bytes = ParamField(
        bytes, "simpleModelName[16]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    Model1Name: bytes = ParamField(
        bytes, "model1Name[16]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
