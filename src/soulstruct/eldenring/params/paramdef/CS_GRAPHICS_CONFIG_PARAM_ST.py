from __future__ import annotations

__all__ = ["CS_GRAPHICS_CONFIG_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_GRAPHICS_CONFIG_PARAM_ST(ParamRow):
    MtextureFilterQuality: int = ParamField(
        uint8, "m_textureFilterQuality", GX_QUALITY_LEVEL_ENUM, default=2,
        tooltip="TOOLTIP-TODO",
    )
    MaaQuality: int = ParamField(
        uint8, "m_aaQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MssaoQuality: int = ParamField(
        uint8, "m_ssaoQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MdofQuality: int = ParamField(
        uint8, "m_dofQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MmotionBlurQuality: int = ParamField(
        uint8, "m_motionBlurQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MshadowQuality: int = ParamField(
        uint8, "m_shadowQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MlightingQuality: int = ParamField(
        uint8, "m_lightingQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MeffectQuality: int = ParamField(
        uint8, "m_effectQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MdecalQuality: int = ParamField(
        uint8, "m_decalQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MreflectionQuality: int = ParamField(
        uint8, "m_reflectionQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MwaterQuality: int = ParamField(
        uint8, "m_waterQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MshaderQuality: int = ParamField(
        uint8, "m_shaderQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MvolumetricEffectQuality: int = ParamField(
        uint8, "m_volumetricEffectQuality", GX_QUALITY_LEVEL_ENUM, default=3,
        tooltip="TOOLTIP-TODO",
    )
    MRayTracingQuality: int = ParamField(
        uint8, "m_RayTracingQuality", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "m_dummy[2]")
