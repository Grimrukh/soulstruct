from __future__ import annotations

__all__ = ["WET_ASPECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WET_ASPECT_PARAM_ST(ParamRow):
    BaseColorR: int = ParamField(
        byte, "baseColorR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseColorG: int = ParamField(
        byte, "baseColorG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseColorB: int = ParamField(
        byte, "baseColorB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "reserve_0[1]")
    BaseColorA: float = ParamField(
        float, "baseColorA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Metallic: int = ParamField(
        byte, "metallic", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "reserve_1[1]")
    _Pad2: bytes = ParamPad(1, "reserve_2[1]")
    _Pad3: bytes = ParamPad(1, "reserve_3[1]")
    MetallicRate: float = ParamField(
        float, "metallicRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShininessRate: float = ParamField(
        float, "shininessRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Shininess: int = ParamField(
        byte, "shininess", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(11, "reserve_4[11]")
