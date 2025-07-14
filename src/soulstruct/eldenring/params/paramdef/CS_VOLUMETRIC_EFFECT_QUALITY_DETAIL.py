from __future__ import annotations

__all__ = ["CS_VOLUMETRIC_EFFECT_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_VOLUMETRIC_EFFECT_QUALITY_DETAIL(ParamRow):
    FogEnabled: int = ParamField(
        uint8, "fogEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogShadowEnabled: int = ParamField(
        uint8, "fogShadowEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "dmy[2]")
    FogShadowSampleCountBias: int = ParamField(
        int32, "fogShadowSampleCountBias", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FogLocalLightDistScale: float = ParamField(
        float32, "fogLocalLightDistScale", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FogVolueSizeScaler: int = ParamField(
        uint32, "fogVolueSizeScaler", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolueSizeDivider: int = ParamField(
        uint32, "fogVolueSizeDivider", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeDepthScaler: int = ParamField(
        uint32, "fogVolumeDepthScaler", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeDepthDivider: int = ParamField(
        uint32, "fogVolumeDepthDivider", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeEnabled: int = ParamField(
        uint8, "fogVolumeEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeUpScaleType: int = ParamField(
        uint8, "fogVolumeUpScaleType", GRAPHICS_CONFIG_CS_GCONFIG_FOG_VOLUME_UPSCALE_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeEdgeCorrectionLevel: int = ParamField(
        uint8, "fogVolumeEdgeCorrectionLevel", GRAPHICS_CONFIG_CS_GCONFIG_FOG_VOLUME_EDGE_CORRECTION_LEVEL, default=2,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeRayMarcingSampleCountOffset: int = ParamField(
        int8, "fogVolumeRayMarcingSampleCountOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeShadowEnabled: int = ParamField(
        uint8, "fogVolumeShadowEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeForceShadowing: int = ParamField(
        uint8, "fogVolumeForceShadowing", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FogVolumeResolution: int = ParamField(
        uint8, "fogVolumeResolution", GRAPHICS_CONFIG_CS_GCONFIG_FOG_VOLUME_RESOLUTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad2[1]")
