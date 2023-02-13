from __future__ import annotations

__all__ = ["WAYPOINT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WAYPOINT_PARAM_ST(ParamRow):
    Attribute1: int = ParamField(
        short, "attribute1", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Attribute2: int = ParamField(
        short, "attribute2", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Attribute3: int = ParamField(
        short, "attribute3", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Attribute4: int = ParamField(
        short, "attribute4", WAYPOINT_ATTRIBUTE, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "padding4[8]")
