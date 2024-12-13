from __future__ import annotations

__all__ = ["CHARMAKEMENU_LISTITEM_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CHARMAKEMENU_LISTITEM_PARAM_ST(ParamRow):
    Value: int = ParamField(
        int, "value", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaptionId: int = ParamField(
        int, "captionId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        byte, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(7, "reserved[7]")
