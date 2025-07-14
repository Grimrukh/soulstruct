from __future__ import annotations

__all__ = ["CHARMAKEMENU_LISTITEM_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class CHARMAKEMENU_LISTITEM_PARAM_ST(ParamRow):
    Value: int = ParamField(
        int32, "Value", default=0,
        tooltip="TODO",
    )
    CaptionID: int = ParamField(
        int32, "CaptionID", default=0,
        tooltip="TODO",
    )
    IconID: int = ParamField(
        uint8, "IconID", game_type=Icon, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(7, "reserved[7]")
