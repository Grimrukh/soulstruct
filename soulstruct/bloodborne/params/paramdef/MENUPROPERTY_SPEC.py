from __future__ import annotations

__all__ = ["MENUPROPERTY_SPEC"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENUPROPERTY_SPEC(ParamRowData):
    CaptionTextID: int = ParamField(
        int, "CaptionTextID", default=0,
        tooltip="TODO",
    )
    IconID: int = ParamField(
        int, "IconID", default=0,
        tooltip="TODO",
    )
    RequiredPropertyID: MENU_PROPERTY_ID = ParamField(
        int, "RequiredPropertyID", default=0,
        tooltip="TODO",
    )
    CompareType: MENU_PROPERTY_CMP_TYPE = ParamField(
        sbyte, "CompareType", default=0,
        tooltip="TODO",
    )
    FormatType: MENU_PROPERTY_FORMAT_TYPE = ParamField(
        byte, "FormatType", default=0,
        tooltip="TODO",
    )
    AdhocCaption: bytes = ParamField(
        bytes, "AdhocCaption[9]", length=18, default=0,
        tooltip="TODO",
    )
