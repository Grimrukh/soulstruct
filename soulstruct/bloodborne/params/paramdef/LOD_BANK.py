from __future__ import annotations

__all__ = ["LOD_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LOD_BANK(ParamRow):
    Lv01BorderDist: float = ParamField(
        float, "lv01_BorderDist", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv01PlayDist: float = ParamField(
        float, "lv01_PlayDist", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv12BorderDist: float = ParamField(
        float, "lv12_BorderDist", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv12PlayDist: float = ParamField(
        float, "lv12_PlayDist", default=2.0,
        tooltip="TOOLTIP-TODO",
    )
    TextureLod: bool = ParamField(
        uint, "textureLod:1", bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
