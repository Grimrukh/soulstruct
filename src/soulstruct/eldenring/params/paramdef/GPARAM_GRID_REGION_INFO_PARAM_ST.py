from __future__ import annotations

__all__ = ["GPARAM_GRID_REGION_INFO_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class GPARAM_GRID_REGION_INFO_PARAM_ST(ParamRow):
    GparamGridRegionId: int = ParamField(
        uint, "GparamGridRegionId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(28, "Reserve[28]")
