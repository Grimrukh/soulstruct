__all__ = ["SHOP_LINEUP_PARAM"]

from soulstruct.base.params.utils import FieldDisplayInfo, DynamicFieldDisplayInfo, pad_field
from soulstruct.bloodborne.params.enums import *
from soulstruct.game_types import *


class DynamicShopRef(DynamicFieldDisplayInfo):

    POSSIBLE_TYPES = {WeaponParam, ArmorParam, RingParam, GoodParam, SpellParam}

    def __call__(self, entry) -> FieldDisplayInfo:
        item_type = entry[self.type_field_name]
        if item_type == SHOP_LINEUP_EQUIPTYPE.Weapon:
            return FieldDisplayInfo(self.name, f"Weapon", True, WeaponParam, f"Weapon to be listed in shop menu.")
        if item_type == SHOP_LINEUP_EQUIPTYPE.Armor:
            return FieldDisplayInfo(self.name, f"Armor", True, ArmorParam, f"Armor to be listed in shop menu.")
        if item_type == SHOP_LINEUP_EQUIPTYPE.Ring:
            return FieldDisplayInfo(self.name, f"Ring", True, RingParam, f"Ring to be listed in shop menu.")
        if item_type == SHOP_LINEUP_EQUIPTYPE.Good:
            return FieldDisplayInfo(self.name, f"Good", True, GoodParam, f"Good to be listed in shop menu.")
        if item_type == SHOP_LINEUP_EQUIPTYPE.Spell:
            return FieldDisplayInfo(self.name, f"Spell", True, SpellParam, f"Spell to be listed in attunement menu.")
        else:
            return FieldDisplayInfo(
                self.name,
                f"ItemID",
                True,
                int,
                f"Item to be listed in shop/attunement menu (unknown item type {item_type}).",
            )


SHOP_LINEUP_PARAM = {
    "paramdef_name": "SHOP_LINEUP_PARAM",
    "file_name": "ShopLineupParam",
    "nickname": "Shops",
    "fields": [
        DynamicShopRef("equipId", "equipType"),
        FieldDisplayInfo("value", "SoulCost", True, int, "Cost of item, in souls."),
        FieldDisplayInfo(
            "mtrlId",
            "RequiredGood",
            True,
            GoodParam,
            "Good that must be possessed for item to be listed. Used to control appearance of spells in "
            "attunement menu.",
        ),
        FieldDisplayInfo(
            "eventFlag",
            "QuantityFlag",
            True,
            Flag,
            "Flag value that holds the count of this item that have been sold already.",
        ),
        FieldDisplayInfo("qwcId", "QWCID", False, int, "Unused world tendency condition."),
        FieldDisplayInfo(
            "sellQuantity",
            "InitialQuantity",
            True,
            int,
            "Quantity of this item initially available to be sold. Set to -1 for infinite quantity.",
        ),
        FieldDisplayInfo(
            "shopType",
            "ShopMenuType",
            True,
            SHOP_LINEUP_SHOPTYPE,
            "Determines if this is a standard shop menu or the spell attunement menu.",
        ),
        FieldDisplayInfo("equipType", "ItemType", True, SHOP_LINEUP_EQUIPTYPE, "Type of item listed in menu."),
        FieldDisplayInfo("value_SAN", "ValueSAN", True, int, ""),
        FieldDisplayInfo("pad_0[6]", "Pad", False, pad_field(6), ""),
    ],
}
