from __future__ import annotations

__all__ = ["LENS_FLARE_EX_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LENS_FLARE_EX_BANK(ParamRow):
    LensFlareSourceRotationX: int = ParamField(
        int16, "lightDegRotX", default=0,
        tooltip="Rotation (X-axis) of visible light source (e.g. sun) that causes lens flares.",
    )
    LensFlareSourceRotationY: int = ParamField(
        int16, "lightDegRotY", default=0,
        tooltip="Rotation (Y-axis) of visible light source (e.g. sun) that causes lens flares.",
    )
    LensFlareSourceRed: int = ParamField(
        int16, "colR", default=255,
        tooltip="Red channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceGreen: int = ParamField(
        int16, "colG", default=255,
        tooltip="Green channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceBlue: int = ParamField(
        int16, "colB", default=255,
        tooltip="Blue channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceAlpha: int = ParamField(
        int16, "colA", default=100,
        tooltip="Alpha channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceDistance: float = ParamField(
        float32, "lightDist", default=300.0,
        tooltip="Distance of visible light source (e.g. sun). Not sure about the units.",
    )
