from __future__ import annotations

__all__ = ["LENS_FLARE_EX_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo

LENS_FLARE_EX_BANK = {
    "param_type": "LENS_FLARE_EX_BANK",
    "file_name": "LensFlareExBank",
    "nickname": "LensFlareSources",
    "fields": [
        ParamFieldInfo(
            "lightDegRotX",
            "LensFlareSourceRotationX",
            True,
            int,
            "Rotation (X-axis) of visible light source (e.g. sun) that causes lens flares.",
        ),
        ParamFieldInfo(
            "lightDegRotY",
            "LensFlareSourceRotationY",
            True,
            int,
            "Rotation (Y-axis) of visible light source (e.g. sun) that causes lens flares.",
        ),
        ParamFieldInfo(
            "colR", "LensFlareSourceRed", True, int, "Red channel (0-255) of visible light source (e.g. sun)."
        ),
        ParamFieldInfo(
            "colG", "LensFlareSourceGreen", True, int, "Green channel (0-255) of visible light source (e.g. sun)."
        ),
        ParamFieldInfo(
            "colB", "LensFlareSourceBlue", True, int, "Blue channel (0-255) of visible light source (e.g. sun)."
        ),
        ParamFieldInfo(
            "colA", "LensFlareSourceAlpha", True, int, "Alpha channel (0-255) of visible light source (e.g. sun)."
        ),
        ParamFieldInfo(
            "lightDist",
            "LensFlareSourceDistance",
            True,
            float,
            "Distance of visible light source (e.g. sun). Not sure about the units.",
        ),
    ],
}
