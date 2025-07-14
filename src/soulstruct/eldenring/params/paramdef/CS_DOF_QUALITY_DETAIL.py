from __future__ import annotations

__all__ = ["CS_DOF_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_DOF_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        uint8, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "dmy[3]")
    ForceHiResoBlur: int = ParamField(
        int32, "forceHiResoBlur", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxBlurLevel: int = ParamField(
        int32, "maxBlurLevel", default=1,
        tooltip="TOOLTIP-TODO",
    )
