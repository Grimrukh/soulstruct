from __future__ import annotations

__all__ = ["GAME_INFO_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class GAME_INFO_PARAM(ParamRow):
    TitleMsgId: int = ParamField(
        int32, "titleMsgId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ContentMsgId: int = ParamField(
        int32, "contentMsgId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Value: int = ParamField(
        int32, "value", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int32, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EventId: int = ParamField(
        int32, "eventId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "Pad[12]")
