from __future__ import annotations

__all__ = ["TONE_CORRECT_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo

TONE_CORRECT_BANK = {
    "param_type": "TONE_CORRECT_BANK",
    "file_name": "ToneCorrectBank",
    "nickname": "ToneCorrection",
    "fields": [
        ParamFieldInfo(
            "brightnessR", "BrightnessRed", True, float, "Red channel (relative to 1) of tone correct brightness."
        ),
        ParamFieldInfo(
            "brightnessG", "BrightnessGreen", True, float, "Green channel (relative to 1) of tone correct brightness."
        ),
        ParamFieldInfo(
            "brightnessB", "BrightnessBlue", True, float, "Blue channel (relative to 1) of tone correct brightness."
        ),
        ParamFieldInfo(
            "contrastR", "ContrastRed", True, float, "Red channel (relative to 1) of tone correct contrast."
        ),
        ParamFieldInfo(
            "contrastG", "ContrastGreen", True, float, "Green channel (relative to 1) of tone correct contrast."
        ),
        ParamFieldInfo(
            "contrastB", "ContrastBlue", True, float, "Blue channel (relative to 1) of tone correct contrast."
        ),
        ParamFieldInfo("saturation", "SaturationCorrection", True, float, "Color saturation correction value."),
        ParamFieldInfo("hue", "HueCorrection", True, float, "Color hue correction value."),
    ],
}
