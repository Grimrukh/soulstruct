from __future__ import annotations

__all__ = ["GAME_INFO_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GAME_INFO_PARAM(ParamRowData):
    TitleMsgId: int = ParamField(
        int, "titleMsgId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ContentMsgId: int = ParamField(
        int, "contentMsgId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Value: int = ParamField(
        int, "value", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EventId: int = ParamField(
        int, "eventId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "Pad[12]")
