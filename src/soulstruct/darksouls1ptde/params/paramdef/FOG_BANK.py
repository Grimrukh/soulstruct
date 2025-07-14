from __future__ import annotations

__all__ = ["FOG_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class FOG_BANK(ParamRow):
    FogStartDistance: int = ParamField(
        int16, "fogBeginZ", default=0,
        tooltip="Distance (m) at which fog begins.",
    )
    FogEndDistance: int = ParamField(
        int16, "fogEndZ", default=100,
        tooltip="Distance (m) at which fog ends.",
    )
    RotationZ: int = ParamField(
        int16, "degRotZ", default=0,
        tooltip="Rotation of fog around the Z axis.",
    )
    RotationW: int = ParamField(
        int16, "degRotW", default=100,
        tooltip="Rotation of fog around the W axis.",
    )
    Red: int = ParamField(
        int16, "colR", default=255,
        tooltip="Red color channel (0-255).",
    )
    Green: int = ParamField(
        int16, "colG", default=255,
        tooltip="Green color channel (0-255).",
    )
    Blue: int = ParamField(
        int16, "colB", default=255,
        tooltip="Blue color channel (0-255).",
    )
    Alpha: int = ParamField(
        int16, "colA", default=100,
        tooltip="Alpha channel (0-255).",
    )
