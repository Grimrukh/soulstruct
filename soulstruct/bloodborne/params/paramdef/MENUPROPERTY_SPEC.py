from __future__ import annotations

__all__ = ["MENUPROPERTY_SPEC"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENUPROPERTY_SPEC(ParamRow):
    CaptionTextID: int = ParamField(
        int, "CaptionTextID", default=0,
        tooltip="TODO",
    )
    IconID: int = ParamField(
        int, "IconID", game_type=Icon, default=0,
        tooltip="TODO",
    )
    RequiredPropertyID: int = ParamField(
        int, "RequiredPropertyID", MENU_PROPERTY_ID, default=0,
        tooltip="TODO",
    )
    CompareType: int = ParamField(
        sbyte, "CompareType", MENU_PROPERTY_CMP_TYPE, default=0,
        tooltip="TODO",
    )
    FormatType: int = ParamField(
        byte, "FormatType", MENU_PROPERTY_FORMAT_TYPE, default=0,
        tooltip="TODO",
    )
    AdhocCaption: str = ParamField(
        bytes, "AdhocCaption[9]", encoding="utf-16", length=18, default=0.0,
        tooltip="TODO",
    )
