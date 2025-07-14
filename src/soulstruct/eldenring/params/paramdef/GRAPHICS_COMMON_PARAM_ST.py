from __future__ import annotations

__all__ = ["GRAPHICS_COMMON_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class GRAPHICS_COMMON_PARAM_ST(ParamRow):
    HitBulletDecalOffsetHitIns: float = ParamField(
        float32, "hitBulletDecalOffset_HitIns", default=0.05,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "reserved02[8]")
    CharaWetDecalFadeRange: float = ParamField(
        float32, "charaWetDecalFadeRange", default=0.6,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(240, "reserved04[240]")
