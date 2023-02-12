from __future__ import annotations

__all__ = ["SHADOW_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SHADOW_BANK(ParamRow):
    ShadowSourceRotationX: int = ParamField(
        short, "lightDegRotX", default=0,
        tooltip="Rotation (X-axis) of shadow-casting light source.",
    )
    ShadowSourceRotationY: int = ParamField(
        short, "lightDegRotY", default=0,
        tooltip="Rotation (Y-axis) of shadow-casting light source.",
    )
    ShadowDensityPercentage: int = ParamField(
        short, "densityRatio", default=100,
        tooltip="Density of cast shadow (0-100), where 100 is the darkest.",
    )
    ShadowRed: int = ParamField(
        short, "colR", default=0,
        tooltip="Red channel (0-255) of cast shadow.",
    )
    ShadowGreen: int = ParamField(
        short, "colG", default=0,
        tooltip="Green channel (0-255) of cast shadow.",
    )
    ShadowBlue: int = ParamField(
        short, "colB", default=0,
        tooltip="Blue channel (0-255) of cast shadow.",
    )
    ShadowStartDistance: float = ParamField(
        float, "beginDist", default=0.0,
        tooltip="Minimum distance (m) at which shadows are cast. A value of 0 means the camera's near-clip plane is "
                "used.",
    )
    ShadowEndDistance: float = ParamField(
        float, "endDist", default=300.0,
        tooltip="Maximum distance (m) at which shadows are cast.",
    )
    HeadOnDistanceReduction: float = ParamField(
        float, "calibulateFar", default=0.0,
        tooltip="Shorten the shadow end distance by this distance when facing the light source direction.",
    )
    FadeStartDistance: float = ParamField(
        float, "fadeBeginDist", default=9999.0,
        tooltip="Shadow starts fading at this distance.",
    )
    FadeDistance: float = ParamField(
        float, "fadeDist", default=-1.0,
        tooltip="Distance (after start distance) until shadow is fully faded.",
    )
    DepthOffset: float = ParamField(
        float, "persedDepthOffset", default=-9.999999747378752e-05,
        tooltip="Depth offset for shadows. With negative values, self-shadows are less likely to occur.",
    )
    ShadowMapStrength: float = ParamField(
        float, "gradFactor", default=0.0,
        tooltip="Negative values weaken the shadow map, positive values strengthen it.",
    )
    ShadowVolumeDepth: float = ParamField(
        float, "shadowVolumeDepth", default=10.0,
        tooltip="Increase this value to cast shadows on tall objects such as buildings.",
    )
