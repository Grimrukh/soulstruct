from __future__ import annotations

__all__ = ["SHADOW_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo

SHADOW_BANK = {
    "param_type": "SHADOW_BANK",
    "file_name": "ShadowBank",
    "nickname": "Shadows",
    "fields": [
        ParamFieldInfo(
            "lightDegRotX", "ShadowSourceRotationX", True, int, "Rotation (X-axis) of shadow-casting light source."
        ),
        ParamFieldInfo(
            "lightDegRotY", "ShadowSourceRotationY", True, int, "Rotation (Y-axis) of shadow-casting light source."
        ),
        ParamFieldInfo(
            "densityRatio",
            "ShadowDensityPercentage",
            True,
            int,
            "Density of cast shadow (0-100), where 100 is the darkest.",
        ),
        ParamFieldInfo("colR", "ShadowRed", True, int, "Red channel (0-255) of cast shadow."),
        ParamFieldInfo("colG", "ShadowGreen", True, int, "Green channel (0-255) of cast shadow."),
        ParamFieldInfo("colB", "ShadowBlue", True, int, "Blue channel (0-255) of cast shadow."),
        ParamFieldInfo(
            "beginDist",
            "ShadowStartDistance",
            True,
            float,
            "Minimum distance (m) at which shadows are cast. A value of 0 means the camera's near-clip plane is "
            "used.",
        ),
        ParamFieldInfo("endDist", "ShadowEndDistance", True, float, "Maximum distance (m) at which shadows are cast."),
        ParamFieldInfo(
            "calibulateFar",
            "HeadOnDistanceReduction",
            True,
            float,
            "Shorten the shadow end distance by this distance when facing the light source direction.",
        ),
        ParamFieldInfo("fadeBeginDist", "FadeStartDistance", True, float, "Shadow starts fading at this distance."),
        ParamFieldInfo(
            "fadeDist", "FadeDistance", True, float, "Distance (after start distance) until shadow is fully faded."
        ),
        ParamFieldInfo(
            "persedDepthOffset",
            "DepthOffset",
            True,
            float,
            "Depth offset for shadows. With negative values, self-shadows are less likely to occur.",
        ),
        ParamFieldInfo(
            "ｇradFactor",
            "ShadowMapStrength",
            True,
            float,
            "Negative values weaken the shadow map, positive values strengthen it.",
        ),
        ParamFieldInfo(
            "shadowVolumeDepth",
            "ShadowVolumeDepth",
            True,
            float,
            "Increase this value to cast shadows on tall objects such as buildings.",
        ),
    ],
}
