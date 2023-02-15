from __future__ import annotations

__all__ = ["QWC_CHANGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class QWC_CHANGE_PARAM_ST(ParamRow):
    PcAttrB: int = ParamField(
        short, "pcAttrB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcAttrW: int = ParamField(
        short, "pcAttrW", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcAttrL: int = ParamField(
        short, "pcAttrL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcAttrR: int = ParamField(
        short, "pcAttrR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrB: int = ParamField(
        short, "areaAttrB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrW: int = ParamField(
        short, "areaAttrW", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrL: int = ParamField(
        short, "areaAttrL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrR: int = ParamField(
        short, "areaAttrR", default=0,
        tooltip="TOOLTIP-TODO",
    )
