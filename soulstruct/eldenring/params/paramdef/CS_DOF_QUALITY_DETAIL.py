from __future__ import annotations

__all__ = ["CS_DOF_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_DOF_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        byte, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "dmy[3]")
    ForceHiResoBlur: int = ParamField(
        int, "forceHiResoBlur", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxBlurLevel: int = ParamField(
        int, "maxBlurLevel", default=1,
        tooltip="TOOLTIP-TODO",
    )
