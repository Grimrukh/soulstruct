from __future__ import annotations

__all__ = ["CS_MOTION_BLUR_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_MOTION_BLUR_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        byte, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    OmbEnabled: int = ParamField(
        byte, "ombEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    ForceScaleVelocityBuffer: int = ParamField(
        byte, "forceScaleVelocityBuffer", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    CheapFilterMode: int = ParamField(
        byte, "cheapFilterMode", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SampleCountBias: int = ParamField(
        int, "sampleCountBias", default=-2,
        tooltip="TOOLTIP-TODO",
    )
    RecurrenceCountBias: int = ParamField(
        int, "recurrenceCountBias", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlurMaxLengthScale: float = ParamField(
        float, "blurMaxLengthScale", default=0.75,
        tooltip="TOOLTIP-TODO",
    )
