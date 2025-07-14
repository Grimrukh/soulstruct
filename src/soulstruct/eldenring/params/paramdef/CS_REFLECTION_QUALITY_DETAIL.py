from __future__ import annotations

__all__ = ["CS_REFLECTION_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_REFLECTION_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        uint8, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    LocalLightEnabled: int = ParamField(
        uint8, "localLightEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    LocalLightForceEnabled: int = ParamField(
        uint8, "localLightForceEnabled", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "dmy[1]")
    ResolutionDivider: int = ParamField(
        uint32, "resolutionDivider", default=2,
        tooltip="TOOLTIP-TODO",
    )
    SsrEnabled: int = ParamField(
        uint8, "ssrEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    SsrGaussianBlurEnabled: int = ParamField(
        uint8, "ssrGaussianBlurEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "dmy2[2]")
    SsrDepthRejectThresholdScale: float = ParamField(
        float32, "ssrDepthRejectThresholdScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SsrRayTraceStepScale: float = ParamField(
        float32, "ssrRayTraceStepScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SsrFadeToViewerBias: float = ParamField(
        float32, "ssrFadeToViewerBias", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SsrFresnelRejectBias: float = ParamField(
        float32, "ssrFresnelRejectBias", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
