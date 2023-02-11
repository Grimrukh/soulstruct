from __future__ import annotations

__all__ = ["ITEMLOT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import ItemLotReference


# noinspection PyDataclass
@dataclass(slots=True)
class ITEMLOT_PARAM_ST(ParamRowData):
    lotItemId01: int = ParamField(
        int, "lotItemId01", default=0, dynamic_callback=ItemLotReference(1),
        tooltip="TODO",
    )
    lotItemId02: int = ParamField(
        int, "lotItemId02", default=0, dynamic_callback=ItemLotReference(2),
        tooltip="TODO",
    )
    lotItemId03: int = ParamField(
        int, "lotItemId03", default=0, dynamic_callback=ItemLotReference(3),
        tooltip="TODO",
    )
    lotItemId04: int = ParamField(
        int, "lotItemId04", default=0, dynamic_callback=ItemLotReference(4),
        tooltip="TODO",
    )
    lotItemId05: int = ParamField(
        int, "lotItemId05", default=0, dynamic_callback=ItemLotReference(5),
        tooltip="TODO",
    )
    lotItemId06: int = ParamField(
        int, "lotItemId06", default=0, dynamic_callback=ItemLotReference(6),
        tooltip="TODO",
    )
    lotItemId07: int = ParamField(
        int, "lotItemId07", default=0, dynamic_callback=ItemLotReference(7),
        tooltip="TODO",
    )
    lotItemId08: int = ParamField(
        int, "lotItemId08", default=0, dynamic_callback=ItemLotReference(8),
        tooltip="TODO",
    )
    Item1Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory01", default=0,
        tooltip="Type of item (slot 1).",
    )
    Item2Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory02", default=0,
        tooltip="Type of item (slot 2).",
    )
    Item3Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory03", default=0,
        tooltip="Type of item (slot 3).",
    )
    Item4Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory04", default=0,
        tooltip="Type of item (slot 4).",
    )
    Item5Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory05", default=0,
        tooltip="Type of item (slot 5).",
    )
    Item6Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory06", default=0,
        tooltip="Type of item (slot 6).",
    )
    Item7Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory07", default=0,
        tooltip="Type of item (slot 7).",
    )
    Item8Category: ITEMLOT_ITEMCATEGORY = ParamField(
        int, "lotItemCategory08", default=0,
        tooltip="Type of item (slot 8).",
    )
    Item1ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint01", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item2ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint02", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item3ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint03", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item4ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint04", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item5ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint05", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item6ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint06", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item7ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint07", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item8ChancePoints: int = ParamField(
        ushort, "lotItemBasePoint08", default=0,
        tooltip="Relative chance (divided by total chance points across all eight slots) that this item will be "
                "dropped.",
    )
    Item1CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint01", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item2CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint02", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item3CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint03", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item4CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint04", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item5CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint05", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item6CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint06", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item7CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint07", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item8CumulativePoints: int = ParamField(
        ushort, "cumulateLotPoint08", default=0,
        tooltip="Points that will be cumulatively added to this slot's chance points every time the item lot is "
                "rolled. This",
    )
    Item1Flag: Flag = ParamField(
        int, "getItemFlagId01", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item2Flag: Flag = ParamField(
        int, "getItemFlagId02", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item3Flag: Flag = ParamField(
        int, "getItemFlagId03", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item4Flag: Flag = ParamField(
        int, "getItemFlagId04", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item5Flag: Flag = ParamField(
        int, "getItemFlagId05", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item6Flag: Flag = ParamField(
        int, "getItemFlagId06", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item7Flag: Flag = ParamField(
        int, "getItemFlagId07", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    Item8Flag: Flag = ParamField(
        int, "getItemFlagId08", default=0, hide=True,
        tooltip="Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
                "used.",
    )
    ItemFlag: Flag = ParamField(
        int, "getItemFlagId", default=-1,
        tooltip="Flag enabled when any item from this item lot is picked up.",
    )
    FirstCumulativeFlag: Flag = ParamField(
        int, "cumulateNumFlagId", default=-1,
        tooltip="First of eight consecutive flags used to store the cumulative points for this item lot.",
    )
    MaxCumulativeAdditions: int = ParamField(
        byte, "cumulateNumMax", default=0,
        tooltip="Maximum number of times that cumulative points will be added to the total. I suspect that the "
                "cumulative slot may be awarded automatically after this; if not, I don't know how the Symbol of "
                "Avarice always drops after all seven Mimics are killed.",
    )
    ItemLotRarity: int = ParamField(
        byte, "lotItem_Rarity", default=0,
        tooltip="Overall rarity of item lot, from 0 to 3. Used fairly consistently, but seems to have no effect. Set "
                "to 2 for all character drops except Crystal Lizards, who have 3.",
    )
    Item1Count: int = ParamField(
        byte, "lotItemNum01", default=0,
        tooltip="Count of item (slot 1).",
    )
    Item2Count: int = ParamField(
        byte, "lotItemNum02", default=0,
        tooltip="Count of item (slot 2).",
    )
    Item3Count: int = ParamField(
        byte, "lotItemNum03", default=0,
        tooltip="Count of item (slot 3).",
    )
    Item4Count: int = ParamField(
        byte, "lotItemNum04", default=0,
        tooltip="Count of item (slot 4).",
    )
    Item5Count: int = ParamField(
        byte, "lotItemNum05", default=0,
        tooltip="Count of item (slot 5).",
    )
    Item6Count: int = ParamField(
        byte, "lotItemNum06", default=0,
        tooltip="Count of item (slot 6).",
    )
    Item7Count: int = ParamField(
        byte, "lotItemNum07", default=0,
        tooltip="Count of item (slot 7).",
    )
    Item8Count: int = ParamField(
        byte, "lotItemNum08", default=0,
        tooltip="Count of item (slot 8).",
    )
    Item1LuckEnabled: bool = ParamField(
        ushort, "enableLuck01:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item2LuckEnabled: bool = ParamField(
        ushort, "enableLuck02:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item3LuckEnabled: bool = ParamField(
        ushort, "enableLuck03:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item4LuckEnabled: bool = ParamField(
        ushort, "enableLuck04:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item5LuckEnabled: bool = ParamField(
        ushort, "enableLuck05:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item6LuckEnabled: bool = ParamField(
        ushort, "enableLuck06:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item7LuckEnabled: bool = ParamField(
        ushort, "enableLuck07:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item8LuckEnabled: bool = ParamField(
        ushort, "enableLuck08:1", bit_count=1, default=False,
        tooltip="If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
                "empty item slot so that rarer items have a relatively better chance of dropping.",
    )
    Item1ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset01:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item2ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset02:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item3ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset03:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item4ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset04:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item5ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset05:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item6ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset06:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item7ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset07:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
    Item8ResetCumulativePointsOnDrop: bool = ParamField(
        ushort, "cumulateReset08:1", bit_count=1, default=False,
        tooltip="If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
    )
