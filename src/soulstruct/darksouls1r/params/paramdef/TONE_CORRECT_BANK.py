from __future__ import annotations

__all__ = ["TONE_CORRECT_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class TONE_CORRECT_BANK(ParamRow):
    BrightnessRed: float = ParamField(
        float32, "brightnessR", default=1.0,
        tooltip="Red channel (relative to 1) of tone correct brightness.",
    )
    BrightnessGreen: float = ParamField(
        float32, "brightnessG", default=1.0,
        tooltip="Green channel (relative to 1) of tone correct brightness.",
    )
    BrightnessBlue: float = ParamField(
        float32, "brightnessB", default=1.0,
        tooltip="Blue channel (relative to 1) of tone correct brightness.",
    )
    ContrastRed: float = ParamField(
        float32, "contrastR", default=1.0,
        tooltip="Red channel (relative to 1) of tone correct contrast.",
    )
    ContrastGreen: float = ParamField(
        float32, "contrastG", default=1.0,
        tooltip="Green channel (relative to 1) of tone correct contrast.",
    )
    ContrastBlue: float = ParamField(
        float32, "contrastB", default=1.0,
        tooltip="Blue channel (relative to 1) of tone correct contrast.",
    )
    SaturationCorrection: float = ParamField(
        float32, "saturation", default=1.0,
        tooltip="Color saturation correction value.",
    )
    HueCorrection: float = ParamField(
        float32, "hue", default=0.0,
        tooltip="Color hue correction value.",
    )
    SFXMultiplier: float = ParamField(
        float32, "sfxMultiplier", default=1.0,
        tooltip="Visual effect multiplier. (Added in DSR)",
    )
