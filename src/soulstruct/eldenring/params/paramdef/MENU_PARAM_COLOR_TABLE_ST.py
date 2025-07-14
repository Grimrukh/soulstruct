from __future__ import annotations

__all__ = ["MENU_PARAM_COLOR_TABLE_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MENU_PARAM_COLOR_TABLE_ST(ParamRow):
    LerpMode: int = ParamField(
        uint8, "lerpMode", MENU_COLOR_LERP_MODE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad1[3]")
    H: int = ParamField(
        uint16, "h", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad2[2]")
    S1: float = ParamField(
        float32, "s1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    V1: float = ParamField(
        float32, "v1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    S2: float = ParamField(
        float32, "s2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    V2: float = ParamField(
        float32, "v2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    S3: float = ParamField(
        float32, "s3", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    V3: float = ParamField(
        float32, "v3", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
