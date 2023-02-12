from __future__ import annotations

__all__ = ["REVERB_AUX_SEND_BUS_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class REVERB_AUX_SEND_BUS_PARAM_ST(ParamRowData):
    ReverbAuxSendBusName: bytes = ParamField(
        bytes, "ReverbAuxSendBusName[32]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
