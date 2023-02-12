from __future__ import annotations

__all__ = ["LOD_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LOD_BANK(ParamRow):
    lv01_BorderDist: float = ParamField(
        float, "lv01_BorderDist", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    lv01_PlayDist: float = ParamField(
        float, "lv01_PlayDist", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    lv12_BorderDist: float = ParamField(
        float, "lv12_BorderDist", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    lv12_PlayDist: float = ParamField(
        float, "lv12_PlayDist", default=2.0,
        tooltip="TOOLTIP-TODO",
    )
