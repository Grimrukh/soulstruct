from __future__ import annotations

__all__ = ["WAYPOINT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WAYPOINT_PARAM_ST(ParamRow):
    Attribute1: int = ParamField(
        int16, "attribute1", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Attribute2: int = ParamField(
        int16, "attribute2", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Attribute3: int = ParamField(
        int16, "attribute3", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Attribute4: int = ParamField(
        int16, "attribute4", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "padding4[8]")
