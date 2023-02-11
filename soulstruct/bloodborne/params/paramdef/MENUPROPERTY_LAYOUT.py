from __future__ import annotations

__all__ = ["MENUPROPERTY_LAYOUT"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENUPROPERTY_LAYOUT(ParamRowData):
    LayoutPath: bytes = ParamField(
        bytes, "LayoutPath[16]", length=16, default=0,
        tooltip="TODO",
    )
    MenuPropertyID: MENU_PROPERTY_ID = ParamField(
        int, "PropertyID", default=0,
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
