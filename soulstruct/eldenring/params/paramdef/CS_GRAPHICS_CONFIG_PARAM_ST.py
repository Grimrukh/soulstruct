from __future__ import annotations

__all__ = ["CS_GRAPHICS_CONFIG_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_GRAPHICS_CONFIG_PARAM_ST(ParamRowData):
    MtextureFilterQuality: int = ParamField(
        byte, "m_textureFilterQuality", default=2,
        tooltip="TOOLTIP-TODO",
    )
    MaaQuality: int = ParamField(
        byte, "m_aaQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MssaoQuality: int = ParamField(
        byte, "m_ssaoQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MdofQuality: int = ParamField(
        byte, "m_dofQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MmotionBlurQuality: int = ParamField(
        byte, "m_motionBlurQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MshadowQuality: int = ParamField(
        byte, "m_shadowQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MlightingQuality: int = ParamField(
        byte, "m_lightingQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MeffectQuality: int = ParamField(
        byte, "m_effectQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MdecalQuality: int = ParamField(
        byte, "m_decalQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MreflectionQuality: int = ParamField(
        byte, "m_reflectionQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MwaterQuality: int = ParamField(
        byte, "m_waterQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MshaderQuality: int = ParamField(
        byte, "m_shaderQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    MvolumetricEffectQuality: int = ParamField(
        byte, "m_volumetricEffectQuality", default=3,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "m_dummy[3]")
