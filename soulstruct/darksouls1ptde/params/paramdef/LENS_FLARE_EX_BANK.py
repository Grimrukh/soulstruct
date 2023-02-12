from __future__ import annotations

__all__ = ["LENS_FLARE_EX_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LENS_FLARE_EX_BANK(ParamRow):
    LensFlareSourceRotationX: int = ParamField(
        short, "lightDegRotX", default=0,
        tooltip="Rotation (X-axis) of visible light source (e.g. sun) that causes lens flares.",
    )
    LensFlareSourceRotationY: int = ParamField(
        short, "lightDegRotY", default=0,
        tooltip="Rotation (Y-axis) of visible light source (e.g. sun) that causes lens flares.",
    )
    LensFlareSourceRed: int = ParamField(
        short, "colR", default=255,
        tooltip="Red channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceGreen: int = ParamField(
        short, "colG", default=255,
        tooltip="Green channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceBlue: int = ParamField(
        short, "colB", default=255,
        tooltip="Blue channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceAlpha: int = ParamField(
        short, "colA", default=100,
        tooltip="Alpha channel (0-255) of visible light source (e.g. sun).",
    )
    LensFlareSourceDistance: float = ParamField(
        float, "lightDist", default=300.0,
        tooltip="Distance of visible light source (e.g. sun). Not sure about the units.",
    )
