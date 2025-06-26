from __future__ import annotations

__all__ = ["CS_SHADER_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_SHADER_QUALITY_DETAIL(ParamRow):
    SssEnabled: int = ParamField(
        byte, "sssEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    TessellationEnabled: int = ParamField(
        byte, "tessellationEnabled", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HighPrecisionNormalEnabled: int = ParamField(
        byte, "highPrecisionNormalEnabled", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy: str = ParamField(
        str, "dmy[1]", encoding="shift_jis_2004", length=1, default='',
        tooltip="TOOLTIP-TODO",
    )
