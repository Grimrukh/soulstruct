from __future__ import annotations

__all__ = ["QWC_CHANGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class QWC_CHANGE_PARAM_ST(ParamRowData):
    pcAttrB: int = ParamField(
        short, "pcAttrB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    pcAttrW: int = ParamField(
        short, "pcAttrW", default=0,
        tooltip="TOOLTIP-TODO",
    )
    pcAttrL: int = ParamField(
        short, "pcAttrL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    pcAttrR: int = ParamField(
        short, "pcAttrR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    areaAttrB: int = ParamField(
        short, "areaAttrB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    areaAttrW: int = ParamField(
        short, "areaAttrW", default=0,
        tooltip="TOOLTIP-TODO",
    )
    areaAttrL: int = ParamField(
        short, "areaAttrL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    areaAttrR: int = ParamField(
        short, "areaAttrR", default=0,
        tooltip="TOOLTIP-TODO",
    )
