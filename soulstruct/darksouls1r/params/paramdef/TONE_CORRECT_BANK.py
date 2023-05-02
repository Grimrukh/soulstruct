from __future__ import annotations

__all__ = ["TONE_CORRECT_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1r.game_types import *
from soulstruct.darksouls1r.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class TONE_CORRECT_BANK(ParamRow):
    BrightnessRed: float = ParamField(
        float, "brightnessR", default=1.0,
        tooltip="Red channel (relative to 1) of tone correct brightness.",
    )
    BrightnessGreen: float = ParamField(
        float, "brightnessG", default=1.0,
        tooltip="Green channel (relative to 1) of tone correct brightness.",
    )
    BrightnessBlue: float = ParamField(
        float, "brightnessB", default=1.0,
        tooltip="Blue channel (relative to 1) of tone correct brightness.",
    )
    ContrastRed: float = ParamField(
        float, "contrastR", default=1.0,
        tooltip="Red channel (relative to 1) of tone correct contrast.",
    )
    ContrastGreen: float = ParamField(
        float, "contrastG", default=1.0,
        tooltip="Green channel (relative to 1) of tone correct contrast.",
    )
    ContrastBlue: float = ParamField(
        float, "contrastB", default=1.0,
        tooltip="Blue channel (relative to 1) of tone correct contrast.",
    )
    SaturationCorrection: float = ParamField(
        float, "saturation", default=1.0,
        tooltip="Color saturation correction value.",
    )
    HueCorrection: float = ParamField(
        float, "hue", default=0.0,
        tooltip="Color hue correction value.",
    )
    # NOTE: Absent from `default` and `m99` DrawParams.
    VFXMultiplier: float = ParamField(
        float, "sfxMultiplier", default=1.0,
        tooltip="Visual effect multiplier. (Added in DSR)",
    )
