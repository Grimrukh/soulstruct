from __future__ import annotations

__all__ = ["CS_SHADER_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_SHADER_QUALITY_DETAIL(ParamRowData):
    SssEnabled: int = ParamField(
        byte, "sssEnabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TessellationEnabled: int = ParamField(
        byte, "tessellationEnabled", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HighPrecisionNormalEnabled: int = ParamField(
        byte, "highPrecisionNormalEnabled", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy: bytes = ParamField(
        bytes, "dmy[1]", length=1, default='',
        tooltip="TOOLTIP-TODO",
    )
