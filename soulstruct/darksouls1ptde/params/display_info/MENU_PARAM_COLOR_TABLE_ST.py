from __future__ import annotations

__all__ = ["MENU_PARAM_COLOR_TABLE_ST"]

from soulstruct.base.params.utils import ParamFieldInfo

MENU_PARAM_COLOR_TABLE_ST = {
    "param_type": "MENU_PARAM_COLOR_TABLE_ST",
    "file_name": "MenuColorTableParam",
    "nickname": "MenuColors",
    "fields": [
        ParamFieldInfo("r", "RedChannel", True, int, "Red value of RGBA color (0-255)."),
        ParamFieldInfo("g", "GreenChannel", True, int, "Green value of RGBA color (0-255)."),
        ParamFieldInfo("b", "BlueChannel", True, int, "Blue value of RGBA color (0-255)."),
        ParamFieldInfo("a", "AlphaChannel", True, int, "Alpha value of RGBA color (0-255). Higher means less transparent."),
    ],
}
