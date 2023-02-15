from __future__ import annotations

__all__ = ["SE_ACTIVATION_RANGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SE_ACTIVATION_RANGE_PARAM_ST(ParamRow):
    ActivateRange: float = ParamField(
        float, "activateRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
