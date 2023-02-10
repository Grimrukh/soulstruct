from __future__ import annotations

__all__ = ["ITEMLOT_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, DynamicParamFieldInfo
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *


class DynamicItemLotRef(DynamicParamFieldInfo):

    POSSIBLE_TYPES = {WeaponParam, ArmorParam, AccessoryParam, GoodParam}

    def __call__(self, entry) -> ParamFieldInfo:
        item_type = entry[self.type_field_name]
        item_lot_slot = int(self.type_field_name[-1])
        if item_type == ITEMLOT_ITEMCATEGORY.Weapon:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                WeaponParam,
                f"Item slot {item_lot_slot} (Weapon).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Armor:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                ArmorParam,
                f"Item slot {item_lot_slot} (Armor).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Ring:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                AccessoryParam,
                f"Item slot {item_lot_slot} (Ring).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Good:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                GoodParam,
                f"Item slot {item_lot_slot} (Good).",
            )
        else:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                int,
                f"Item slot {item_lot_slot} (unknown item type {item_type}).",
            )


ITEMLOT_PARAM_ST = {
    "param_type": "ITEMLOT_PARAM_ST",
    "file_name": "ItemLotParam",
    "nickname": "ItemLots",
    "fields": [
        ParamFieldInfo(
            "getItemFlagId", "ItemFlag", True, Flag, "Flag enabled when any item from this item lot is picked up."
        ),
        ParamFieldInfo(
            "cumulateNumFlagId",
            "FirstCumulativeFlag",
            True,
            Flag,
            "First of eight consecutive flags used to store the cumulative points for this item lot.",
        ),
        ParamFieldInfo(
            "cumulateNumMax",
            "MaxCumulativeAdditions",
            True,
            int,
            "Maximum number of times that cumulative points will be added to the total. I suspect that the "
            "cumulative slot may be awarded automatically after this; if not, I don't know how the Symbol of "
            "Avarice always drops after all seven Mimics are killed.",
        ),
        ParamFieldInfo(
            "lotItem_Rarity",
            "ItemLotRarity",
            True,
            int,
            "Overall rarity of item lot, from 0 to 3. Used fairly consistently, but seems to have no effect. Set "
            "to 2 for all character drops except Crystal Lizards, who have 3.",
        ),
        ParamFieldInfo("lotItemCategory01", "Item1Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 1)."),
        DynamicItemLotRef("lotItemId01", "lotItemCategory01"),
        ParamFieldInfo("lotItemNum01", "Item1Count", True, int, "Count of item (slot 1)."),
        ParamFieldInfo(
            "lotItemBasePoint01",
            "Item1ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId01",
            "Item1Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck01:1",
            "Item1LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint01",
            "Item1CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset01:1",
            "Item1ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory02", "Item2Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 2)."),
        DynamicItemLotRef("lotItemId02", "lotItemCategory02"),
        ParamFieldInfo("lotItemNum02", "Item2Count", True, int, "Count of item (slot 2)."),
        ParamFieldInfo(
            "lotItemBasePoint02",
            "Item2ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId02",
            "Item2Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck02:1",
            "Item2LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint02",
            "Item2CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset02:1",
            "Item2ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory03", "Item3Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 3)."),
        DynamicItemLotRef("lotItemId03", "lotItemCategory03"),
        ParamFieldInfo("lotItemNum03", "Item3Count", True, int, "Count of item (slot 3)."),
        ParamFieldInfo(
            "lotItemBasePoint03",
            "Item3ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId03",
            "Item3Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck03:1",
            "Item3LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint03",
            "Item3CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset03:1",
            "Item3ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory04", "Item4Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 4)."),
        DynamicItemLotRef("lotItemId04", "lotItemCategory04"),
        ParamFieldInfo("lotItemNum04", "Item4Count", True, int, "Count of item (slot 4)."),
        ParamFieldInfo(
            "lotItemBasePoint04",
            "Item4ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId04",
            "Item4Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck04:1",
            "Item4LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint04",
            "Item4CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset04:1",
            "Item4ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory05", "Item5Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 5)."),
        DynamicItemLotRef("lotItemId05", "lotItemCategory05"),
        ParamFieldInfo("lotItemNum05", "Item5Count", True, int, "Count of item (slot 5)."),
        ParamFieldInfo(
            "lotItemBasePoint05",
            "Item5ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId05",
            "Item5Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck05:1",
            "Item5LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint05",
            "Item5CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset05:1",
            "Item5ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory06", "Item6Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 6)."),
        DynamicItemLotRef("lotItemId06", "lotItemCategory06"),
        ParamFieldInfo("lotItemNum06", "Item6Count", True, int, "Count of item (slot 6)."),
        ParamFieldInfo(
            "lotItemBasePoint06",
            "Item6ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId06",
            "Item6Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck06:1",
            "Item6LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint06",
            "Item6CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset06:1",
            "Item6ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory07", "Item7Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 7)."),
        DynamicItemLotRef("lotItemId07", "lotItemCategory07"),
        ParamFieldInfo("lotItemNum07", "Item7Count", True, int, "Count of item (slot 7)."),
        ParamFieldInfo(
            "lotItemBasePoint07",
            "Item7ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId07",
            "Item7Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck07:1",
            "Item7LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint07",
            "Item7CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset07:1",
            "Item7ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory08", "Item8Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 8)."),
        DynamicItemLotRef("lotItemId08", "lotItemCategory08"),
        ParamFieldInfo("lotItemNum08", "Item8Count", True, int, "Count of item (slot 8)."),
        ParamFieldInfo(
            "lotItemBasePoint08",
            "Item8ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId08",
            "Item8Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck08:1",
            "Item8LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint08",
            "Item8CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset08:1",
            "Item8ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
    ],
}
