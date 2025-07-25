from __future__ import annotations

__all__ = ["SE_ACTIVATION_RANGE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SE_ACTIVATION_RANGE_PARAM_ST(ParamRow):
    ActivateRange: float = ParamField(
        float32, "activateRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
