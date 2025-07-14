from __future__ import annotations

__all__ = ["MENU_PARAM_COLOR_TABLE_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class MENU_PARAM_COLOR_TABLE_ST(ParamRow):
    RedChannel: int = ParamField(
        uint8, "r", default=255,
        tooltip="Red value of RGBA color (0-255).",
    )
    GreenChannel: int = ParamField(
        uint8, "g", default=255,
        tooltip="Green value of RGBA color (0-255).",
    )
    BlueChannel: int = ParamField(
        uint8, "b", default=255,
        tooltip="Blue value of RGBA color (0-255).",
    )
    AlphaChannel: int = ParamField(
        uint8, "a", default=255,
        tooltip="Alpha value of RGBA color (0-255). Higher means less transparent.",
    )
