from __future__ import annotations

__all__ = ["POINT_LIGHT_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo


POINT_LIGHT_BANK = {
    "param_type": "POINT_LIGHT_BANK",
    "file_name": "PointLightBank",
    "nickname": "PointLights",
    "fields": [
        ParamFieldInfo(
            "dwindleBegin",
            "FadeStartDistance",
            True,
            float,
            "Distance at which player's point light begins to fade.",
        ),
        ParamFieldInfo(
            "dwindleEnd",
            "FadeEndDistance",
            True,
            float,
            "Distance at which player's point light finishes fading and disappears entirely.",
        ),
        ParamFieldInfo("colR", "PointLightRed", True, int, "Red channel (0-255) of point light."),
        ParamFieldInfo("colG", "PointLightGreen", True, int, "Green channel (0-255) of point light."),
        ParamFieldInfo("colB", "PointLightBlue", True, int, "Blue channel (0-255) of point light."),
        ParamFieldInfo("colA", "PointLightAlpha", True, int, "Alpha channel (0-255) of point light."),
    ],
}
