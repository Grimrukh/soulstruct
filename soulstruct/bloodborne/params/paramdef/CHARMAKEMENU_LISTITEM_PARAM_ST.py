from __future__ import annotations

__all__ = ["CHARMAKEMENU_LISTITEM_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARMAKEMENU_LISTITEM_PARAM_ST(ParamRowData):
    Value: int = ParamField(
        int, "Value", default=0,
        tooltip="TODO",
    )
    CaptionID: int = ParamField(
        int, "CaptionID", default=0,
        tooltip="TODO",
    )
    IconID: int = ParamField(
        byte, "IconID", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(7, "reserved[7]")
