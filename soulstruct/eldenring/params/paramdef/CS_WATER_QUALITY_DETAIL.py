from __future__ import annotations

__all__ = ["CS_WATER_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_WATER_QUALITY_DETAIL(ParamRow):
    InteractionEnabled: int = ParamField(
        byte, "interactionEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "dmy[3]")
