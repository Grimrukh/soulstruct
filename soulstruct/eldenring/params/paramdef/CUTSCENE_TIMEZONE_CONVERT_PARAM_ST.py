from __future__ import annotations

__all__ = ["CUTSCENE_TIMEZONE_CONVERT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CUTSCENE_TIMEZONE_CONVERT_PARAM_ST(ParamRow):
    SrcTimezoneStart: float = ParamField(
        float, "SrcTimezoneStart", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstCutscenTime: float = ParamField(
        float, "DstCutscenTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
