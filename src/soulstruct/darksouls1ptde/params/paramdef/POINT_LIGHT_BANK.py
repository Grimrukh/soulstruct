from __future__ import annotations

__all__ = ["POINT_LIGHT_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class POINT_LIGHT_BANK(ParamRow):
    FadeStartDistance: float = ParamField(
        float32, "dwindleBegin", default=0.5,
        tooltip="Distance at which player's point light begins to fade.",
    )
    FadeEndDistance: float = ParamField(
        float32, "dwindleEnd", default=2.0,
        tooltip="Distance at which player's point light finishes fading and disappears entirely.",
    )
    PointLightRed: int = ParamField(
        int16, "colR", default=255,
        tooltip="Red channel (0-255) of point light.",
    )
    PointLightGreen: int = ParamField(
        int16, "colG", default=255,
        tooltip="Green channel (0-255) of point light.",
    )
    PointLightBlue: int = ParamField(
        int16, "colB", default=255,
        tooltip="Blue channel (0-255) of point light.",
    )
    PointLightAlpha: int = ParamField(
        int16, "colA", default=100,
        tooltip="Alpha channel (0-255) of point light.",
    )
