from __future__ import annotations

__all__ = ["LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST(ParamRowData):
    Lv00: float = ParamField(
        float, "Lv00", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv01: float = ParamField(
        float, "Lv01", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv02: float = ParamField(
        float, "Lv02", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv03: float = ParamField(
        float, "Lv03", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv04: float = ParamField(
        float, "Lv04", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv05: float = ParamField(
        float, "Lv05", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv06: float = ParamField(
        float, "Lv06", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv07: float = ParamField(
        float, "Lv07", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv08: float = ParamField(
        float, "Lv08", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv09: float = ParamField(
        float, "Lv09", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv10: float = ParamField(
        float, "Lv10", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv11: float = ParamField(
        float, "Lv11", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv12: float = ParamField(
        float, "Lv12", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv13: float = ParamField(
        float, "Lv13", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv14: float = ParamField(
        float, "Lv14", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv15: float = ParamField(
        float, "Lv15", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv16: float = ParamField(
        float, "Lv16", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv17: float = ParamField(
        float, "Lv17", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv18: float = ParamField(
        float, "Lv18", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv19: float = ParamField(
        float, "Lv19", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Lv20: float = ParamField(
        float, "Lv20", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(44, "reserve[44]")
