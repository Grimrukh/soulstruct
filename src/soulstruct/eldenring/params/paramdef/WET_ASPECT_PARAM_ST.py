from __future__ import annotations

__all__ = ["WET_ASPECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class WET_ASPECT_PARAM_ST(ParamRow):
    BaseColorR: int = ParamField(
        uint8, "baseColorR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseColorG: int = ParamField(
        uint8, "baseColorG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseColorB: int = ParamField(
        uint8, "baseColorB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "reserve_0[1]")
    BaseColorA: float = ParamField(
        float32, "baseColorA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Metallic: int = ParamField(
        uint8, "metallic", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "reserve_1[1]")
    _Pad2: bytes = ParamPad(1, "reserve_2[1]")
    _Pad3: bytes = ParamPad(1, "reserve_3[1]")
    MetallicRate: float = ParamField(
        float32, "metallicRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShininessRate: float = ParamField(
        float32, "shininessRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Shininess: int = ParamField(
        uint8, "shininess", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(11, "reserve_4[11]")
