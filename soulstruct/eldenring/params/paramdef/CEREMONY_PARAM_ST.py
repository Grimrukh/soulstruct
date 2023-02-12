from __future__ import annotations

__all__ = ["CEREMONY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CEREMONY_PARAM_ST(ParamRowData):
    EventLayerId: int = ParamField(
        int, "eventLayerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapStudioLayerId: int = ParamField(
        int, "mapStudioLayerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayAreaOffset: int = ParamField(
        int, "multiPlayAreaOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideMapPlaceNameId: int = ParamField(
        int, "overrideMapPlaceNameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverrideSaveMapNameId: int = ParamField(
        int, "overrideSaveMapNameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(16, "pad2[16]")
