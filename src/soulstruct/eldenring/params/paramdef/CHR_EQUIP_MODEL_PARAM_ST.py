from __future__ import annotations

__all__ = ["CHR_EQUIP_MODEL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CHR_EQUIP_MODEL_PARAM_ST(ParamRow):
    Unknown0x0: int = ParamField(
        int, "unknown_0x0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x4: int = ParamField(
        int, "unknown_0x4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x8: int = ParamField(
        int, "unknown_0x8", default=0,
        tooltip="TOOLTIP-TODO",
    )
