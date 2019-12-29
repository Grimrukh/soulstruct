from enum import IntEnum
from typing import Union

from soulstruct.events.internal import get_value_test
from soulstruct.events.shared import instructions as instr
from soulstruct.enums.shared import ItemType
from soulstruct.game_types.basic_types import GameObject

__all__ = ['Item', 'Weapon', 'Armor', 'Ring', 'Rune', 'Good', 'ItemLot',
           'ItemInt', 'WeaponInt', 'ArmorInt', 'RingInt', 'RuneInt', 'GoodInt', 'ItemLotInt']


class Item(GameObject, IntEnum):
    """Base class for items.

    Unfortunately, the naming of item types is inconsistent. There are four types of items, which are internally called
    'Weapon', 'Protector', 'Accessory', and 'Good'. (Note that the 'Accessory' type is used for runes in Bloodborne.)

    The name 'Equipment' is sometimes used to describe this general item type, and in the internal text of Dark Souls
    Remastered, the name 'Item' is used to refer to the type 'Good' (which is probably what most people think of when
    they read the name 'Item').

    In Soulstruct, the name 'Item' exclusively refers to this base type (i.e. anything that can appear in your in-game
    inventory) and the name 'Good' is used for the main item type (i.e. things you do not wear). This is consistent with
    terms such as ItemLot. The name 'Equipment' is not used. I have also renamed 'Protector' to 'Armor', and 'Accessory'
    to 'Ring' (with an alias 'Rune').

    You can refer to an instance of any Item to test if the player currently has that item (not in Bottomless Box).
    """

    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return get_value_test(
            value=value, negate=negate, condition=condition,
            if_true_func=lambda c, i: getattr(instr, f'IfPlayerHas{self.item_type.name}')(c, i, False),
            if_false_func=lambda c, i: getattr(instr, f'IfPlayerDoesNotHave{self.item_type.name}')(c, i, False))

    @property
    def item_type(self) -> ItemType:
        raise NotImplementedError("You must use a subclass of Item.")


class Weapon(Item):
    @property
    def item_type(self):
        return ItemType.Weapon


class Armor(Item):
    @property
    def item_type(self):
        return ItemType.Armor


class Ring(Item):
    @property
    def item_type(self):
        return ItemType.Ring


Rune = Ring


class Good(Item):
    @property
    def item_type(self):
        return ItemType.Good


class ItemLot(GameObject, IntEnum):
    """No additional functionality (yet)."""
    pass


ItemLotInt = Union[ItemLot, int]
ItemInt = Union[Item, int]
WeaponInt = Union[Weapon, int]
ArmorInt = Union[Armor, int]
RingInt = Union[Ring, int]
RuneInt = Union[Rune, int]
GoodInt = Union[Good, int]
