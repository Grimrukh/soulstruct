from __future__ import annotations

__all__ = ["LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST(ParamRowData):
    DrawDistLvBegin: int = ParamField(
        byte, "DrawDist_LvBegin", default=21,
        tooltip="TOOLTIP-TODO",
    )
    DrawDistLvEnd: int = ParamField(
        byte, "DrawDist_LvEnd", default=21,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "reserve0[2]")
    DrawDistScaleBegin: float = ParamField(
        float, "DrawDist_ScaleBegin", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DrawDistScaleEnd: float = ParamField(
        float, "DrawDist_ScaleEnd", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ShadwDrawDistLvBegin: int = ParamField(
        byte, "ShadwDrawDist_LvBegin", default=21,
        tooltip="TOOLTIP-TODO",
    )
    ShadwDrawDistLvEnd: int = ParamField(
        byte, "ShadwDrawDist_LvEnd", default=21,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "reserve1[2]")
    ShadwDrawDistScaleBegin: float = ParamField(
        float, "ShadwDrawDist_ScaleBegin", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ShadwDrawDistScaleEnd: float = ParamField(
        float, "ShadwDrawDist_ScaleEnd", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(24, "reserve2[24]")
