from __future__ import annotations

__all__ = ["LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST(ParamRow):
    DrawDistLvBegin: int = ParamField(
        uint8, "DrawDist_LvBegin", default=21,
        tooltip="TOOLTIP-TODO",
    )
    DrawDistLvEnd: int = ParamField(
        uint8, "DrawDist_LvEnd", default=21,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "reserve0[2]")
    DrawDistScaleBegin: float = ParamField(
        float32, "DrawDist_ScaleBegin", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DrawDistScaleEnd: float = ParamField(
        float32, "DrawDist_ScaleEnd", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ShadwDrawDistLvBegin: int = ParamField(
        uint8, "ShadwDrawDist_LvBegin", default=21,
        tooltip="TOOLTIP-TODO",
    )
    ShadwDrawDistLvEnd: int = ParamField(
        uint8, "ShadwDrawDist_LvEnd", default=21,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "reserve1[2]")
    ShadwDrawDistScaleBegin: float = ParamField(
        float32, "ShadwDrawDist_ScaleBegin", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ShadwDrawDistScaleEnd: float = ParamField(
        float32, "ShadwDrawDist_ScaleEnd", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(24, "reserve2[24]")
