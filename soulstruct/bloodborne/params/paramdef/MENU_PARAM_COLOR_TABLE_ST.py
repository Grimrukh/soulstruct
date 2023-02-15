from __future__ import annotations

__all__ = ["MENU_PARAM_COLOR_TABLE_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENU_PARAM_COLOR_TABLE_ST(ParamRow):
    RedChannel: int = ParamField(
        byte, "r", default=255,
        tooltip="Red value of RGBA color (0-255).",
    )
    GreenChannel: int = ParamField(
        byte, "g", default=255,
        tooltip="Green value of RGBA color (0-255).",
    )
    BlueChannel: int = ParamField(
        byte, "b", default=255,
        tooltip="Blue value of RGBA color (0-255).",
    )
    AlphaChannel: int = ParamField(
        byte, "a", default=255,
        tooltip="Alpha value of RGBA color (0-255). Higher is more opaque.",
    )
