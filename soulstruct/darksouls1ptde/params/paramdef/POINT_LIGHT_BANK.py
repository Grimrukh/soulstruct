from __future__ import annotations

__all__ = ["POINT_LIGHT_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class POINT_LIGHT_BANK(ParamRow):
    FadeStartDistance: float = ParamField(
        float, "dwindleBegin", default=0.5,
        tooltip="Distance at which player's point light begins to fade.",
    )
    FadeEndDistance: float = ParamField(
        float, "dwindleEnd", default=2.0,
        tooltip="Distance at which player's point light finishes fading and disappears entirely.",
    )
    PointLightRed: int = ParamField(
        short, "colR", default=255,
        tooltip="Red channel (0-255) of point light.",
    )
    PointLightGreen: int = ParamField(
        short, "colG", default=255,
        tooltip="Green channel (0-255) of point light.",
    )
    PointLightBlue: int = ParamField(
        short, "colB", default=255,
        tooltip="Blue channel (0-255) of point light.",
    )
    PointLightAlpha: int = ParamField(
        short, "colA", default=100,
        tooltip="Alpha channel (0-255) of point light.",
    )
