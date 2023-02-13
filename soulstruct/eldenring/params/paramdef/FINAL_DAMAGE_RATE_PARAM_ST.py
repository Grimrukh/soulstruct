from __future__ import annotations

__all__ = ["FINAL_DAMAGE_RATE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FINAL_DAMAGE_RATE_PARAM_ST(ParamRow):
    Physrate: float = ParamField(
        float, "physrate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Magrate: float = ParamField(
        float, "magrate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Firerate: float = ParamField(
        float, "firerate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Thunrate: float = ParamField(
        float, "thunrate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Darkrate: float = ParamField(
        float, "darkrate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Staminarate: float = ParamField(
        float, "staminarate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Sarate: float = ParamField(
        float, "sarate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
