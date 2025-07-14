from __future__ import annotations

__all__ = ["GRASS_MAP_SETTINGS_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class GRASS_MAP_SETTINGS_PARAM_ST(ParamRow):
    GrassType0: int = ParamField(
        uint32, "grassType0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GrassType1: int = ParamField(
        uint32, "grassType1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GrassType2: int = ParamField(
        uint32, "grassType2", default=0,
        tooltip="TOOLTIP-TODO",
    )
