import ast
from enum import IntEnum
from typing import Union
import soulstruct.emevd.shared.instructions as instr
from soulstruct.emevd.shared.enums import *

GAME_TYPES = {'Character', 'Region', 'Object', 'Flag', 'ItemLot',
              'Item', 'Weapon', 'Armor', 'Ring', 'Good', 'Hitbox', 'Text'}
uint = 'I'
short = 'h'
ushort = 'H'
char = 'b'
uchar = 'B'


class NoSkipOrTerminateError(Exception):
    pass


class NoNegateError(Exception):
    pass


def _get_value_condition(
        value, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False,
        skip_if_true_func=None, skip_if_false_func=None,
        if_true_func=None, if_false_func=None,
        end_if_true_func=None, end_if_false_func=None,
        restart_if_true_func=None, restart_if_false_func=None):

    if skip_lines > 0:
        if condition is not None or end_event or restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if skip_if_true_func is None or skip_if_false_func is None:
            raise NoSkipOrTerminateError
        if negate:
            return skip_if_true_func(skip_lines, value)
        return skip_if_false_func(skip_lines, value)
    elif skip_lines < 0:
        raise ValueError("You cannot skip a negative number of lines.")

    if condition is not None:
        if condition not in range(-7, 8):
            raise ValueError("Condition register index must be between -7 and 7.")
        if end_event or restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if negate:
            return if_false_func(condition, value)
        return if_true_func(condition, value)

    if end_event:
        if restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if negate:
            if end_if_false_func is None:
                raise NoSkipOrTerminateError
            return end_if_false_func(value)
        if end_if_true_func is None:
            raise NoSkipOrTerminateError
        return end_if_true_func(value)

    if restart_event:
        if negate:
            if restart_if_false_func is None:
                raise NoSkipOrTerminateError
            return restart_if_false_func(value)
        if restart_if_true_func is None:
            raise NoSkipOrTerminateError
        return restart_if_true_func(value)

    raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


class Flag(IntEnum):
    """ Condition upon a flag as a shortcut to condition upon it being enabled. """
    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagOn, skip_if_false_func=instr.SkipLinesIfFlagOff,
            if_true_func=instr.IfFlagOn, if_false_func=instr.IfFlagOff,
            end_if_true_func=instr.EndIfFlagOn, end_if_false_func=instr.EndIfFlagOff,
            restart_if_true_func=instr.RestartIfFlagOn, restart_if_false_func=instr.RestartIfFlagOff)


class Entity(IntEnum):
    """ Base class for anything that appears in the MSB. """
    pass


class MapEntity(Entity):
    """ Base class for things with coordinates in the MSB: Objects, Regions, and Characters. """
    def __call__(self, negate=False, condition=None, skip_lines=0):
        raise NotImplementedError

    @property
    def map_entity_type(self):
        raise NotImplementedError


class Object(MapEntity):
    """ Condition upon an object as a shortcut to condition upon it *not* being destroyed. """
    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        try:
            value = self.value
        except AttributeError:
            value = self
        return _get_value_condition(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfObjectNotDestroyed, skip_if_false_func=instr.SkipLinesIfObjectDestroyed,
            if_true_func=instr.IfObjectNotDestroyed, if_false_func=instr.IfObjectDestroyed,
            end_if_true_func=instr.EndIfObjectNotDestroyed, end_if_false_func=instr.EndIfObjectDestroyed,
            restart_if_true_func=instr.RestartIfObjectNotDestroyed, restart_if_false_func=instr.RestartIfObjectDestroyed)

    @property
    def map_entity_type(self):
        return MapEntityType.Object


class Region(MapEntity):
    """ Condition upon a region as a shortcut to condition upon the player being inside it (condition only). """
    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return _get_value_condition(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            if_true_func=instr.IfPlayerInsideRegion, if_false_func=instr.IfPlayerOutsideRegion)

    @property
    def map_entity_type(self):
        return MapEntityType.Region


class Character(MapEntity):
    """ Condition upon a character as a shortcut to condition upon them being alive. """
    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return _get_value_condition(
            value=value, negate=negate, condition=condition, skip_lines=0,
            if_true_func=instr.IfAlive, if_false_func=instr.IfDead)

    @property
    def map_entity_type(self):
        return MapEntityType.Character


class EventEntity(Entity):
    """ Base class for things that appear in the 'events' section of the MSB, such as sounds, ObjActs, and FX. """
    pass


class Hitbox(Entity):
    """ Hitbox (or 'collision') added in MSB. No additional state. """
    pass


class Item(IntEnum):
    """ Condition upon an item as a shortcut to condition upon the player *having* it (not in Bottomless Box). """
    def __call__(self, negate=False, condition=None):
        raise NotImplementedError

    @property
    def item_type(self):
        raise NotImplementedError


class Weapon(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=lambda c, weapon: instr.IfPlayerOwnsWeapon(c, weapon, including_box=False),
            if_false_func=lambda c, weapon: instr.IfPlayerDoesNotOwnWeapon(c, weapon, including_box=False))

    @property
    def item_type(self):
        return ItemType.Weapon


class Armor(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=lambda c, armor: instr.IfPlayerOwnsArmor(c, armor, including_box=False),
            if_false_func=lambda c, armor: instr.IfPlayerDoesNotOwnArmor(c, armor, including_box=False))

    @property
    def item_type(self):
        return ItemType.Armor


class Ring(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=lambda c, ring: instr.IfPlayerOwnsRing(c, ring, including_box=False),
            if_false_func=lambda c, ring: instr.IfPlayerDoesNotOwnRing(c, ring, including_box=False))

    @property
    def item_type(self):
        return ItemType.Ring


class Good(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=lambda c, good: instr.IfPlayerOwnsGood(c, good, including_box=False),
            if_false_func=lambda c, good: instr.IfPlayerDoesNotOwnGood(c, good, including_box=False))

    @property
    def item_type(self):
        return ItemType.Good


class ItemLot(IntEnum):
    """ No additional functionality. """
    pass


class Text(IntEnum):
    """ No additional functionality. """
    pass


class FlagRange(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def any(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return _get_value_condition(
            value=self, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagRangeAllOff, skip_if_false_func=instr.SkipLinesIfFlagRangeAnyOn,
            if_true_func=instr.IfFlagRangeAnyOn, if_false_func=instr.IfFlagRangeAllOff,
            end_if_true_func=instr.EndIfFlagRangeAnyOn, end_if_false_func=instr.EndIfFlagRangeAllOff,
            restart_if_true_func=instr.RestartIfFlagRangeAnyOn, restart_if_false_func=instr.RestartIfFlagRangeAllOff,
        )

    def all(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return _get_value_condition(
            value=self, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagRangeAnyOff, skip_if_false_func=instr.SkipLinesIfFlagRangeAllOn,
            if_true_func=instr.IfFlagRangeAllOn, if_false_func=instr.IfFlagRangeAnyOff,
            end_if_true_func=instr.EndIfFlagRangeAllOn, end_if_false_func=instr.EndIfFlagRangeAnyOff,
            restart_if_true_func=instr.RestartIfFlagRangeAllOn, restart_if_false_func=instr.RestartIfFlagRangeAnyOff,
        )


class Map(object):
    def __init__(self, area_id, block_id):
        self.area_id = area_id
        self.block_id = block_id
        self.file_name = f'm{area_id:02d}_{block_id:02d}_00_00'

    def __eq__(self, other_map):
        return self.area_id == other_map.area_id and self.block_id == other_map.block_id

    def __iter__(self):
        yield self.area_id
        yield self.block_id

    def __repr__(self):
        return self.file_name


COMPARISON_NODES = {ast.Eq: 0, ast.NotEq: 1, ast.Gt: 2, ast.Lt: 3, ast.GtE: 4, ast.LtE: 5}
NEG_COMPARISON_NODES = {ast.Eq: 1, ast.NotEq: 0, ast.Gt: 5, ast.Lt: 4, ast.GtE: 3, ast.LtE: 2}


class ConstantCondition(object):
    """ Condition with no arguments. These conditions have 'hard-coded' methods in the EMEVD API. """

    def __init__(self, if_true_func=None, if_false_func=None,
                 skip_if_true_func=None, skip_if_false_func=None,
                 end_if_true_func=None, end_if_false_func=None,
                 restart_if_true_func=None, restart_if_false_func=None):
        self.if_true_func = if_true_func
        self.if_false_func = if_false_func
        self.skip_if_true_func = skip_if_true_func
        self.skip_if_false_func = skip_if_false_func
        self.end_if_true_func = end_if_true_func
        self.end_if_false_func = end_if_false_func
        self.restart_if_true_func = restart_if_true_func
        self.restart_if_false_func = restart_if_false_func

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        """ Constants are called with no user-level args. """

        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if self.skip_if_true_func is None:
                    raise NoSkipOrTerminateError
                return self.skip_if_true_func(skip_lines)
            if self.skip_if_false_func is None:
                raise NoSkipOrTerminateError
            return self.skip_if_false_func(skip_lines)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if condition not in range(-7, 8):
                raise ValueError("Condition register index must be between -7 and 7.")
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                return self.if_false_func(condition)
            return self.if_true_func(condition)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if self.end_if_false_func is None:
                    raise NoSkipOrTerminateError
                return self.end_if_false_func()
            if self.end_if_true_func is None:
                raise NoSkipOrTerminateError
            return self.end_if_true_func()

        if restart_event:
            if negate:
                if self.restart_if_false_func is None:
                    raise NoSkipOrTerminateError
                return self.restart_if_false_func()
            if self.restart_if_true_func is None:
                raise NoSkipOrTerminateError
            return self.restart_if_true_func()

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


# Typing hints
GameMap = Union[Map, tuple, list]
CharacterInt = Union[Character, int]
FlagInt = Union[Flag, int]
HitboxInt = Union[Hitbox, int]
MapEntityInt = Union[MapEntity, int]
ObjectInt = Union[Object, int]
AnimatedInt = Union[Character, Object, int]
RegionInt = Union[Region, int]
TextInt = Union[Text, int]
ItemLotInt = Union[ItemLot, int]
ItemInt = Union[Item, int]
WeaponInt = Union[Weapon, int]
ArmorInt = Union[Armor, int]
RingInt = Union[Ring, int]
GoodInt = Union[Good, int]
FlagRangeOrSequence = Union[FlagRange, tuple, list]
StringOffset = int
