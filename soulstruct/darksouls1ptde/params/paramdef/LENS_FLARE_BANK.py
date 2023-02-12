from __future__ import annotations

__all__ = ["LENS_FLARE_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LENS_FLARE_BANK(ParamRow):
    LensFlareTextureID: int = ParamField(
        sbyte, "texId", default=-1,
        tooltip="Texture ID of lens flare (texture name format is 'lensflare_XX'). -1 means disabled.",
    )
    IsLensFlare: int = ParamField(
        byte, "isFlare", default=0,
        tooltip="Flare if enabled, or 'ghost' if disabled.",
    )
    EnableRotation: int = ParamField(
        byte, "enableRoll", default=0,
        tooltip="Allows lens flare texture to rotate with camera.",
    )
    EnableScaling: int = ParamField(
        byte, "enableScale", default=0,
        tooltip="Allows lens flare texture to change scale with camera.",
    )
    PositionRatio: float = ParamField(
        float, "locateDistRate", default=0.0,
        tooltip="Relative position of lens flare between light source (0.0) and center of screen (1.0).",
    )
    TextureScale: float = ParamField(
        float, "texScale", default=1.0,
        tooltip="Base scaling of lens flare texture.",
    )
    TextureRed: int = ParamField(
        short, "colR", default=255,
        tooltip="Red channel (0-255) of lens flare texture.",
    )
    TextureGreen: int = ParamField(
        short, "colG", default=255,
        tooltip="Green channel (0-255) of lens flare texture.",
    )
    TextureBlue: int = ParamField(
        short, "colB", default=255,
        tooltip="Blue channel (0-255) of lens flare texture.",
    )
    TextureAlpha: int = ParamField(
        short, "colA", default=255,
        tooltip="Alpha channel (0-255) of lens flare texture.",
    )
