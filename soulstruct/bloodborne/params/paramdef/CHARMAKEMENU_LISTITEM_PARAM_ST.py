from __future__ import annotations

__all__ = ["CHARMAKEMENU_LISTITEM_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARMAKEMENU_LISTITEM_PARAM_ST(ParamRow):
    Value: int = ParamField(
        int, "Value", default=0,
        tooltip="TODO",
    )
    CaptionID: int = ParamField(
        int, "CaptionID", default=0,
        tooltip="TODO",
    )
    IconID: int = ParamField(
        byte, "IconID", game_type=Icon, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(7, "reserved[7]")
