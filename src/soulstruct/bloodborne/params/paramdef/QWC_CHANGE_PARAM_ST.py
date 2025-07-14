from __future__ import annotations

__all__ = ["QWC_CHANGE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class QWC_CHANGE_PARAM_ST(ParamRow):
    PcAttrB: int = ParamField(
        int16, "pcAttrB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcAttrW: int = ParamField(
        int16, "pcAttrW", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcAttrL: int = ParamField(
        int16, "pcAttrL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcAttrR: int = ParamField(
        int16, "pcAttrR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrB: int = ParamField(
        int16, "areaAttrB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrW: int = ParamField(
        int16, "areaAttrW", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrL: int = ParamField(
        int16, "areaAttrL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaAttrR: int = ParamField(
        int16, "areaAttrR", default=0,
        tooltip="TOOLTIP-TODO",
    )
