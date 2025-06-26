from __future__ import annotations

__all__ = ["CS_AA_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_AA_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        byte, "enabled", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForceFXAA2: int = ParamField(
        byte, "forceFXAA2", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "dmy[2]")
