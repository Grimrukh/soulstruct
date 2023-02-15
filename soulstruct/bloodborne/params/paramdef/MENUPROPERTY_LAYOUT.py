from __future__ import annotations

__all__ = ["MENUPROPERTY_LAYOUT"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENUPROPERTY_LAYOUT(ParamRow):
    LayoutPath: str = ParamField(
        bytes, "LayoutPath[16]", encoding="shift_jis_2004", length=16, default=0.0,
        tooltip="TODO",
    )
    MenuPropertyID: int = ParamField(
        int, "PropertyID", MENU_PROPERTY_ID, default=0,
        tooltip="TODO",
    )
    CaptionTextID: int = ParamField(
        int, "CaptionTextID", default=0,
        tooltip="TODO",
    )
    HelpTextID: int = ParamField(
        int, "HelpTextID", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserved[4]")
