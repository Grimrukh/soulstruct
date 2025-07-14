from __future__ import annotations

__all__ = ["ITEMLOT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import ItemLotReference


class ITEMLOT_PARAM_ST(ParamRow):
    Item1: int = ParamField(
        int32, "lotItemId01", default=0, dynamic_callback=ItemLotReference(1),
        tooltip="TODO",
    )
    Item2: int = ParamField(
        int32, "lotItemId02", default=0, dynamic_callback=ItemLotReference(2),
        tooltip="TODO",
    )
    Item3: int = ParamField(
        int32, "lotItemId03", default=0, dynamic_callback=ItemLotReference(3),
        tooltip="TODO",
    )
    Item4: int = ParamField(
        int32, "lotItemId04", default=0, dynamic_callback=ItemLotReference(4),
        tooltip="TODO",
    )
    Item5: int = ParamField(
        int32, "lotItemId05", default=0, dynamic_callback=ItemLotReference(5),
        tooltip="TODO",
    )
    Item6: int = ParamField(
        int32, "lotItemId06", default=0, dynamic_callback=ItemLotReference(6),
        tooltip="TODO",
    )
    Item7: int = ParamField(
        int32, "lotItemId07", default=0, dynamic_callback=ItemLotReference(7),
        tooltip="TODO",
    )
    Item8: int = ParamField(
        int32, "lotItemId08", default=0, dynamic_callback=ItemLotReference(8),
        tooltip="TODO",
    )
    Item1Category: int = ParamField(
        int32, "lotItemCategory01", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 1).",
    )
    Item2Category: int = ParamField(
        int32, "lotItemCategory02", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 2).",
    )
    Item3Category: int = ParamField(
        int32, "lotItemCategory03", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 3).",
    )
    Item4Category: int = ParamField(
        int32, "lotItemCategory04", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 4).",
    )
    Item5Category: int = ParamField(
        int32, "lotItemCategory05", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 5).",
    )
    Item6Category: int = ParamField(
        int32, "lotItemCategory06", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 6).",
    )
    Item7Category: int = ParamField(
        int32, "lotItemCategory07", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 7).",
    )
    Item8Category: int = ParamField(
        int32, "lotItemCategory08", ITEMLOT_ITEMCATEGORY, default=0,
        tooltip="Type of item (slot 8).",
    )
    Item1ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint01", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item2ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint02", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item3ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint03", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item4ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint04", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item5ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint05", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item6ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint06", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item7ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint07", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item8ChancePoints: int = ParamField(
        uint16, "lotItemBasePoint08", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item1CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint01", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item2CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint02", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item3CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint03", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item4CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint04", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item5CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint05", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item6CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint06", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item7CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint07", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item8CumulativePoints: int = ParamField(
        uint16, "cumulateLotPoint08", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item1Flag: int = ParamField(
        int32, "getItemFlagId01", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item2Flag: int = ParamField(
        int32, "getItemFlagId02", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item3Flag: int = ParamField(
        int32, "getItemFlagId03", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item4Flag: int = ParamField(
        int32, "getItemFlagId04", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item5Flag: int = ParamField(
        int32, "getItemFlagId05", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item6Flag: int = ParamField(
        int32, "getItemFlagId06", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item7Flag: int = ParamField(
        int32, "getItemFlagId07", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item8Flag: int = ParamField(
        int32, "getItemFlagId08", game_type=Flag, default=0,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    ItemFlag: int = ParamField(
        int32, "getItemFlagId", game_type=Flag, default=-1,
        tooltip="Flag enabled when any item from this item lot is picked up.",
    )
    FirstCumulativeFlag: int = ParamField(
        int32, "cumulateNumFlagId", game_type=Flag, default=-1,
        tooltip="First of eight consecutive flags used to store the cumulative points for this item lot.",
    )
    MaxCumulativeAdditions: int = ParamField(
        uint8, "cumulateNumMax", default=0,
        tooltip="Maximum number of times that cumulative points will be added to the total. I suspect that the "
                "cumulative slot may be awarded automatically after this; if not, I don't know how the Symbol of "
                "Avarice always drops after all seven Mimics are killed.",
    )
    ItemLotRarity: int = ParamField(
        uint8, "lotItem_Rarity", default=0,
        tooltip="Overall rarity of item lot, from 0 to 3. Used fairly consistently, but seems to have no effect. Set "
                "to 2 for all character drops except Crystal Lizards, who have 3.",
    )
    Item1Count: int = ParamField(
        uint8, "lotItemNum01", default=0,
        tooltip="Count of item (slot 1).",
    )
    Item2Count: int = ParamField(
        uint8, "lotItemNum02", default=0,
        tooltip="Count of item (slot 2).",
    )
    Item3Count: int = ParamField(
        uint8, "lotItemNum03", default=0,
        tooltip="Count of item (slot 3).",
    )
    Item4Count: int = ParamField(
        uint8, "lotItemNum04", default=0,
        tooltip="Count of item (slot 4).",
    )
    Item5Count: int = ParamField(
        uint8, "lotItemNum05", default=0,
        tooltip="Count of item (slot 5).",
    )
    Item6Count: int = ParamField(
        uint8, "lotItemNum06", default=0,
        tooltip="Count of item (slot 6).",
    )
    Item7Count: int = ParamField(
        uint8, "lotItemNum07", default=0,
        tooltip="Count of item (slot 7).",
    )
    Item8Count: int = ParamField(
        uint8, "lotItemNum08", default=0,
        tooltip="Count of item (slot 8).",
    )
    Item1LuckEnabled: bool = ParamField(
        uint16, "enableLuck01:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item2LuckEnabled: bool = ParamField(
        uint16, "enableLuck02:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item3LuckEnabled: bool = ParamField(
        uint16, "enableLuck03:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item4LuckEnabled: bool = ParamField(
        uint16, "enableLuck04:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item5LuckEnabled: bool = ParamField(
        uint16, "enableLuck05:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item6LuckEnabled: bool = ParamField(
        uint16, "enableLuck06:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item7LuckEnabled: bool = ParamField(
        uint16, "enableLuck07:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item8LuckEnabled: bool = ParamField(
        uint16, "enableLuck08:1", ITEMLOT_ENABLE_LUCK, bit_count=1, default=True,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item1ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset01:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item2ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset02:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item3ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset03:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item4ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset04:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item5ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset05:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item6ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset06:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item7ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset07:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item8ResetCumulativePointsOnDrop: bool = ParamField(
        uint16, "cumulateReset08:1", ITEMLOT_CUMULATE_RESET, bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
