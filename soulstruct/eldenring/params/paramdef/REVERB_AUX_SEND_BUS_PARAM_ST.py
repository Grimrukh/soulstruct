from __future__ import annotations

__all__ = ["REVERB_AUX_SEND_BUS_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class REVERB_AUX_SEND_BUS_PARAM_ST(ParamRow):
    ReverbAuxSendBusName: str = ParamField(
        str, "ReverbAuxSendBusName[32]", encoding="shift_jis_2004", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
