from __future__ import annotations

__all__ = ["CUTSCENE_TIMEZONE_CONVERT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CUTSCENE_TIMEZONE_CONVERT_PARAM_ST(ParamRow):
    SrcTimezoneStart: float = ParamField(
        float32, "SrcTimezoneStart", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstCutscenTime: float = ParamField(
        float32, "DstCutscenTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
