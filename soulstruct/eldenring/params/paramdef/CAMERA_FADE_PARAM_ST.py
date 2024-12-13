from __future__ import annotations

__all__ = ["CAMERA_FADE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CAMERA_FADE_PARAM_ST(ParamRow):
    NearMinDist: float = ParamField(
        float, "NearMinDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NearMaxDist: float = ParamField(
        float, "NearMaxDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FarMinDist: float = ParamField(
        float, "FarMinDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FarMaxDist: float = ParamField(
        float, "FarMaxDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MiddleAlpha: float = ParamField(
        float, "MiddleAlpha", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "dummy[12]")
