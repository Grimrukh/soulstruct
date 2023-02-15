from __future__ import annotations

__all__ = ["SE_MATERIAL_CONVERT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SE_MATERIAL_CONVERT_PARAM_ST(ParamRow):
    SeMaterialId: int = ParamField(
        byte, "seMaterialId", MATERIAL_SE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad[3]")
