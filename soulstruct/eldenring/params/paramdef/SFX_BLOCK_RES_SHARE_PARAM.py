from __future__ import annotations

__all__ = ["SFX_BLOCK_RES_SHARE_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SFX_BLOCK_RES_SHARE_PARAM(ParamRow):
    ShareBlockRsMapUidVal: int = ParamField(
        uint, "shareBlockRsMapUidVal", default=0,
        tooltip="TOOLTIP-TODO",
    )
