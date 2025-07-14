from __future__ import annotations

__all__ = ["LENS_FLARE_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LENS_FLARE_BANK(ParamRow):
    LensFlareTextureID: int = ParamField(
        int8, "texId", default=-1,
        tooltip="Texture ID of lens flare (texture name format is 'lensflare_XX'). -1 means disabled.",
    )
    IsLensFlare: int = ParamField(
        uint8, "isFlare", default=0,
        tooltip="Flare if enabled, or 'ghost' if disabled.",
    )
    EnableRotation: int = ParamField(
        uint8, "enableRoll", default=0,
        tooltip="Allows lens flare texture to rotate with camera.",
    )
    EnableScaling: int = ParamField(
        uint8, "enableScale", default=0,
        tooltip="Allows lens flare texture to change scale with camera.",
    )
    PositionRatio: float = ParamField(
        float32, "locateDistRate", default=0.0,
        tooltip="Relative position of lens flare between light source (0.0) and center of screen (1.0).",
    )
    TextureScale: float = ParamField(
        float32, "texScale", default=1.0,
        tooltip="Base scaling of lens flare texture.",
    )
    TextureRed: int = ParamField(
        int16, "colR", default=255,
        tooltip="Red channel (0-255) of lens flare texture.",
    )
    TextureGreen: int = ParamField(
        int16, "colG", default=255,
        tooltip="Green channel (0-255) of lens flare texture.",
    )
    TextureBlue: int = ParamField(
        int16, "colB", default=255,
        tooltip="Blue channel (0-255) of lens flare texture.",
    )
    TextureAlpha: int = ParamField(
        int16, "colA", default=255,
        tooltip="Alpha channel (0-255) of lens flare texture.",
    )
