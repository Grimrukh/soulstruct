from __future__ import annotations

__all__ = ["LOD_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LOD_BANK(ParamRow):
    Lv01BorderDist: float = ParamField(
        float32, "lv01_BorderDist", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv01PlayDist: float = ParamField(
        float32, "lv01_PlayDist", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv12BorderDist: float = ParamField(
        float32, "lv12_BorderDist", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv12PlayDist: float = ParamField(
        float32, "lv12_PlayDist", default=2.0,
        tooltip="TOOLTIP-TODO",
    )
    TextureLod: bool = ParamField(
        uint32, "textureLod:1", bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
