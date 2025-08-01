from __future__ import annotations

__all__ = ["SFX_BLOCK_RES_SHARE_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SFX_BLOCK_RES_SHARE_PARAM(ParamRow):
    ShareBlockRsMapUidVal: int = ParamField(
        uint32, "shareBlockRsMapUidVal", default=0,
        tooltip="TOOLTIP-TODO",
    )
