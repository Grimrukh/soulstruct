from __future__ import annotations

__all__ = ["CS_REFLECTION_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_REFLECTION_QUALITY_DETAIL(ParamRowData):
    Enabled: int = ParamField(
        byte, "enabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LocalLightEnabled: int = ParamField(
        byte, "localLightEnabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LocalLightForceEnabled: int = ParamField(
        byte, "localLightForceEnabled", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "dmy[1]")
    ResolutionDivider: int = ParamField(
        uint, "resolutionDivider", default=2,
        tooltip="TOOLTIP-TODO",
    )
    SsrEnabled: int = ParamField(
        byte, "ssrEnabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SsrGaussianBlurEnabled: int = ParamField(
        byte, "ssrGaussianBlurEnabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "dmy2[2]")
    SsrDepthRejectThresholdScale: float = ParamField(
        float, "ssrDepthRejectThresholdScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SsrRayTraceStepScale: float = ParamField(
        float, "ssrRayTraceStepScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SsrFadeToViewerBias: float = ParamField(
        float, "ssrFadeToViewerBias", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SsrFresnelRejectBias: float = ParamField(
        float, "ssrFresnelRejectBias", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
