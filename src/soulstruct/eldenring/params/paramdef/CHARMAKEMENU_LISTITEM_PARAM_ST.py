from __future__ import annotations

__all__ = ["CHARMAKEMENU_LISTITEM_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CHARMAKEMENU_LISTITEM_PARAM_ST(ParamRow):
    Value: int = ParamField(
        int32, "value", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaptionId: int = ParamField(
        int32, "captionId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        uint8, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(7, "reserved[7]")
