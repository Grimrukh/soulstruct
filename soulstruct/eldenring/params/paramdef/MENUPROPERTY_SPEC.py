from __future__ import annotations

__all__ = ["MENUPROPERTY_SPEC"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENUPROPERTY_SPEC(ParamRow):
    CaptionTextID: int = ParamField(
        int, "CaptionTextID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconID: int = ParamField(
        int, "IconID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredPropertyID: int = ParamField(
        uint, "RequiredPropertyID", MENU_PROPERTY_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CompareType: int = ParamField(
        sbyte, "CompareType", MENU_PROPERTY_CMP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    FormatType: int = ParamField(
        ushort, "FormatType", MENU_PROPERTY_FORMAT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(16, "pad[16]")
