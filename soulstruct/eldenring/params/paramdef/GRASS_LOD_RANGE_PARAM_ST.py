from __future__ import annotations

__all__ = ["GRASS_LOD_RANGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GRASS_LOD_RANGE_PARAM_ST(ParamRow):
    LOD0range: float = ParamField(
        float, "LOD0_range", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD0play: float = ParamField(
        float, "LOD0_play", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD1range: float = ParamField(
        float, "LOD1_range", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD1play: float = ParamField(
        float, "LOD1_play", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD2range: float = ParamField(
        float, "LOD2_range", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LOD2play: float = ParamField(
        float, "LOD2_play", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
