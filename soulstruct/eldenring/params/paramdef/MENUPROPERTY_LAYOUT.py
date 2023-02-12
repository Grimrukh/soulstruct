from __future__ import annotations

__all__ = ["MENUPROPERTY_LAYOUT"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENUPROPERTY_LAYOUT(ParamRow):
    LayoutPath: bytes = ParamField(
        bytes, "LayoutPath[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    MenuPropertyID: int = ParamField(
        int, "PropertyID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaptionTextID: int = ParamField(
        int, "CaptionTextID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HelpTextID: int = ParamField(
        int, "HelpTextID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserved[4]")
