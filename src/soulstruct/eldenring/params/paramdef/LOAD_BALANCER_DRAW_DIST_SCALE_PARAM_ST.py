from __future__ import annotations

__all__ = ["LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST(ParamRow):
    Lv00: float = ParamField(
        float32, "Lv00", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv01: float = ParamField(
        float32, "Lv01", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv02: float = ParamField(
        float32, "Lv02", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv03: float = ParamField(
        float32, "Lv03", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv04: float = ParamField(
        float32, "Lv04", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv05: float = ParamField(
        float32, "Lv05", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv06: float = ParamField(
        float32, "Lv06", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv07: float = ParamField(
        float32, "Lv07", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv08: float = ParamField(
        float32, "Lv08", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv09: float = ParamField(
        float32, "Lv09", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv10: float = ParamField(
        float32, "Lv10", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv11: float = ParamField(
        float32, "Lv11", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv12: float = ParamField(
        float32, "Lv12", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv13: float = ParamField(
        float32, "Lv13", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv14: float = ParamField(
        float32, "Lv14", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv15: float = ParamField(
        float32, "Lv15", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv16: float = ParamField(
        float32, "Lv16", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv17: float = ParamField(
        float32, "Lv17", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv18: float = ParamField(
        float32, "Lv18", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv19: float = ParamField(
        float32, "Lv19", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv20: float = ParamField(
        float32, "Lv20", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(44, "reserve[44]")
