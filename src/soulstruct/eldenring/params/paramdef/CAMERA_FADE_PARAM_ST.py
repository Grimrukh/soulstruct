from __future__ import annotations

__all__ = ["CAMERA_FADE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CAMERA_FADE_PARAM_ST(ParamRow):
    NearMinDist: float = ParamField(
        float32, "NearMinDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NearMaxDist: float = ParamField(
        float32, "NearMaxDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FarMinDist: float = ParamField(
        float32, "FarMinDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FarMaxDist: float = ParamField(
        float32, "FarMaxDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MiddleAlpha: float = ParamField(
        float32, "MiddleAlpha", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "dummy[12]")
