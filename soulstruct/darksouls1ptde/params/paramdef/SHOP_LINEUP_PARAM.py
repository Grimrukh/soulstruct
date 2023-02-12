from __future__ import annotations

__all__ = ["SHOP_LINEUP_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import ShopReference


# noinspection PyDataclass
@dataclass(slots=True)
class SHOP_LINEUP_PARAM(ParamRow):
    equipId: int = ParamField(
        int, "equipId", default=0, dynamic_callback=ShopReference(),
        tooltip="TODO",
    )
    SoulCost: int = ParamField(
        int, "value", default=-1,
        tooltip="Cost of item, in souls.",
    )
    RequiredGood: int = ParamField(
        int, "mtrlId", default=-1,
        tooltip="Good that must be possessed for item to be listed. Used to control appearance of spells in "
                "attunement menu.",
    )
    QuantityFlag: int = ParamField(
        int, "eventFlag", default=-1,
        tooltip="Flag value that holds the count of this item that have been sold already.",
    )
    QWCID: int = ParamField(
        int, "qwcId", default=-1,
        tooltip="Unused world tendency condition.",
    )
    InitialQuantity: int = ParamField(
        short, "sellQuantity", default=-1,
        tooltip="Quantity of this item initially available to be sold. Set to -1 for infinite quantity.",
    )
    ShopMenuType: int = ParamField(
        byte, "shopType", SHOP_LINEUP_SHOPTYPE, default=0,
        tooltip="Determines if this is a standard shop menu or the spell attunement menu.",
    )
    ItemType: int = ParamField(
        byte, "equipType", SHOP_LINEUP_EQUIPTYPE, default=0,
        tooltip="Type of item listed in menu.",
    )
    _Pad0: bytes = ParamPad(8, "pad_0[8]")
