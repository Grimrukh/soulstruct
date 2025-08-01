from __future__ import annotations

__all__ = ["GRASS_LOD_RANGE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class GRASS_LOD_RANGE_PARAM_ST(ParamRow):
    LOD0range: float = ParamField(
        float32, "LOD0_range", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD0play: float = ParamField(
        float32, "LOD0_play", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD1range: float = ParamField(
        float32, "LOD1_range", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD1play: float = ParamField(
        float32, "LOD1_play", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD2range: float = ParamField(
        float32, "LOD2_range", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD2play: float = ParamField(
        float32, "LOD2_play", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
