from __future__ import annotations

__all__ = ["CEREMONY_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CEREMONY_PARAM_ST(ParamRow):
    EventLayerId: int = ParamField(
        int32, "eventLayerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapStudioLayerId: int = ParamField(
        int32, "mapStudioLayerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayAreaOffset: int = ParamField(
        int32, "multiPlayAreaOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideMapPlaceNameId: int = ParamField(
        int32, "overrideMapPlaceNameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverrideSaveMapNameId: int = ParamField(
        int32, "overrideSaveMapNameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(16, "pad2[16]")
