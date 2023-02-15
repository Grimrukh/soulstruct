from __future__ import annotations

__all__ = ["FOG_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FOG_BANK(ParamRow):
    FogStartDistance: int = ParamField(
        short, "fogBeginZ", default=0,
        tooltip="Distance (m) at which fog begins.",
    )
    FogEndDistance: int = ParamField(
        short, "fogEndZ", default=100,
        tooltip="Distance (m) at which fog ends.",
    )
    RotationZ: int = ParamField(
        short, "degRotZ", default=0,
        tooltip="Rotation of fog around the Z axis.",
    )
    RotationW: int = ParamField(
        short, "degRotW", default=100,
        tooltip="Rotation of fog around the W axis.",
    )
    Red: int = ParamField(
        short, "colR", default=255,
        tooltip="Red color channel (0-255).",
    )
    Green: int = ParamField(
        short, "colG", default=255,
        tooltip="Green color channel (0-255).",
    )
    Blue: int = ParamField(
        short, "colB", default=255,
        tooltip="Blue color channel (0-255).",
    )
    Alpha: int = ParamField(
        short, "colA", default=100,
        tooltip="Alpha channel (0-255).",
    )
