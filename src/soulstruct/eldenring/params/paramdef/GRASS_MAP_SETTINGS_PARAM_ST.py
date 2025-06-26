from __future__ import annotations

__all__ = ["GRASS_MAP_SETTINGS_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class GRASS_MAP_SETTINGS_PARAM_ST(ParamRow):
    GrassType0: int = ParamField(
        uint, "grassType0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GrassType1: int = ParamField(
        uint, "grassType1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GrassType2: int = ParamField(
        uint, "grassType2", default=0,
        tooltip="TOOLTIP-TODO",
    )
