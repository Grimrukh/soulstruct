from __future__ import annotations

__all__ = ["CS_MOTION_BLUR_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_MOTION_BLUR_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        byte, "enabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    OmbEnabled: int = ParamField(
        byte, "ombEnabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ForceScaleVelocityBuffer: int = ParamField(
        byte, "forceScaleVelocityBuffer", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CheapFilterMode: int = ParamField(
        byte, "cheapFilterMode", default=0,
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
        float, "blurMaxLengthScale", default=0,
        tooltip="TOOLTIP-TODO",
    )
