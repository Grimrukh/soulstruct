from __future__ import annotations

__all__ = ["CS_MOTION_BLUR_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_MOTION_BLUR_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        uint8, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    OmbEnabled: int = ParamField(
        uint8, "ombEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    ForceScaleVelocityBuffer: int = ParamField(
        uint8, "forceScaleVelocityBuffer", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    CheapFilterMode: int = ParamField(
        uint8, "cheapFilterMode", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SampleCountBias: int = ParamField(
        int32, "sampleCountBias", default=-2,
        tooltip="TOOLTIP-TODO",
    )
    RecurrenceCountBias: int = ParamField(
        int32, "recurrenceCountBias", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlurMaxLengthScale: float = ParamField(
        float32, "blurMaxLengthScale", default=0.75,
        tooltip="TOOLTIP-TODO",
    )
