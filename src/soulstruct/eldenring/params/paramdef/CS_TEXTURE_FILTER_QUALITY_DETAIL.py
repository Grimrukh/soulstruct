from __future__ import annotations

__all__ = ["CS_TEXTURE_FILTER_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_TEXTURE_FILTER_QUALITY_DETAIL(ParamRow):
    Filter: int = ParamField(
        uint8, "filter", GX_TEXTURE_FILTER, default=3,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "dmy[3]")
    MaxAnisoLevel: int = ParamField(
        uint32, "maxAnisoLevel", default=4,
        tooltip="TOOLTIP-TODO",
    )
