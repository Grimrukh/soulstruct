from __future__ import annotations

__all__ = ["MAP_GRID_CREATE_HEIGHT_LIMIT_INFO_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAP_GRID_CREATE_HEIGHT_LIMIT_INFO_PARAM_ST(ParamRow):
    GridEnableCreateHeightMin: float = ParamField(
        float, "GridEnableCreateHeightMin", default=-99999.0,
        tooltip="TOOLTIP-TODO",
    )
    GridEnableCreateHeightMax: float = ParamField(
        float, "GridEnableCreateHeightMax", default=99999.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(24, "Reserve[24]")
