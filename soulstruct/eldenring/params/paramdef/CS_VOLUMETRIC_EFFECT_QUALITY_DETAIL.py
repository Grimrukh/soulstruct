from __future__ import annotations

__all__ = ["CS_VOLUMETRIC_EFFECT_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_VOLUMETRIC_EFFECT_QUALITY_DETAIL(ParamRow):
    FogEnabled: int = ParamField(
        byte, "fogEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogShadowEnabled: int = ParamField(
        byte, "fogShadowEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "dmy[2]")
    FogShadowSampleCountBias: int = ParamField(
        int, "fogShadowSampleCountBias", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FogLocalLightDistScale: float = ParamField(
        float, "fogLocalLightDistScale", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FogVolueSizeScaler: int = ParamField(
        uint, "fogVolueSizeScaler", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolueSizeDivider: int = ParamField(
        uint, "fogVolueSizeDivider", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeDepthScaler: int = ParamField(
        uint, "fogVolumeDepthScaler", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeDepthDivider: int = ParamField(
        uint, "fogVolumeDepthDivider", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeEnabled: int = ParamField(
        byte, "fogVolumeEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeUpScaleType: int = ParamField(
        byte, "fogVolumeUpScaleType", GRAPHICS_CONFIG_CS_GCONFIG_FOG_VOLUME_UPSCALE_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeEdgeCorrectionLevel: int = ParamField(
        byte, "fogVolumeEdgeCorrectionLevel", GRAPHICS_CONFIG_CS_GCONFIG_FOG_VOLUME_EDGE_CORRECTION_LEVEL, default=2,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeRayMarcingSampleCountOffset: int = ParamField(
        sbyte, "fogVolumeRayMarcingSampleCountOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeShadowEnabled: int = ParamField(
        byte, "fogVolumeShadowEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeForceShadowing: int = ParamField(
        byte, "fogVolumeForceShadowing", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeResolution: int = ParamField(
        byte, "fogVolumeResolution", GRAPHICS_CONFIG_CS_GCONFIG_FOG_VOLUME_RESOLUTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad2[1]")
