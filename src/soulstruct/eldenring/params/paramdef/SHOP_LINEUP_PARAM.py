from __future__ import annotations

__all__ = ["SHOP_LINEUP_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import ShopReference


class SHOP_LINEUP_PARAM(ParamRow):
    ItemID: int = ParamField(
        int32, "equipId", default=0, dynamic_callback=ShopReference(),
        tooltip="TODO",
    )
    SoulCost: int = ParamField(
        int32, "value", default=-1,
        tooltip="Cost of item, in souls.",
    )
    RequiredGood: int = ParamField(
        int32, "mtrlId", default=-1,
        tooltip="Good that must be possessed for item to be listed. Used to control appearance of spells in "
                "attunement menu.",
    )
    EventFlagforStock: int = ParamField(
        uint32, "eventFlag_forStock", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EventFlagforRelease: int = ParamField(
        uint32, "eventFlag_forRelease", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InitialQuantity: int = ParamField(
        int16, "sellQuantity", default=-1,
        tooltip="Quantity of this item initially available to be sold. Set to -1 for infinite quantity.",
    )
    _Pad0: bytes = ParamPad(1, "pad3[1]")
    ItemType: int = ParamField(
        uint8, "equipType", SHOP_LINEUP_EQUIPTYPE, default=0,
        tooltip="Type of item listed in menu.",
    )
    CostType: int = ParamField(
        uint8, "costType", SHOP_LINEUP_COSTTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    SetNum: int = ParamField(
        uint16, "setNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ValueAdd: int = ParamField(
        int32, "value_Add", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ValueMagnification: float = ParamField(
        float32, "value_Magnification", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        int32, "iconId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NameMsgId: int = ParamField(
        int32, "nameMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MenuTitleMsgId: int = ParamField(
        int32, "menuTitleMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MenuIconId: int = ParamField(
        int16, "menuIconId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad2[2]")
