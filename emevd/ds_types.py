import ast
from enum import IntEnum
from pydses import *

DARK_SOULS_TYPES = {'Character', 'Region', 'Object', 'Flag', 'ItemLot',
                    'Item', 'Weapon', 'Armor', 'Ring', 'Good', 'Hitbox'}
NO_NEGATE_OR_SKIP = 'no_negate_or_skip'
NEGATE_ONLY = 'negate_only'
NEGATE_AND_SKIP = 'negate_and_skip'
PLAYER = 10000
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
            skip_if_true_func=skip_if_event_flag_on, skip_if_false_func=skip_if_event_flag_off,
            if_true_func=if_event_flag_on, if_false_func=if_event_flag_off,
            end_if_true_func=end_if_event_flag_on, end_if_false_func=end_if_event_flag_off,
            restart_if_true_func=restart_if_event_flag_on, restart_if_false_func=restart_if_event_flag_off)


class Entity(IntEnum):
    """ Base class for anything that appears in the MSB. """
    pass


class MapEntity(Entity):
    """ Base class for things with coordinates in the MSB: Objects, Regions, and Characters. """
    def __call__(self, negate=False, condition=None, skip_lines=0):
        raise NotImplementedError

    @property
    def category(self):
        raise NotImplementedError


class Region(MapEntity):
    """ Condition upon a region as a shortcut to condition upon the player being inside it (condition only). """
    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return _get_value_condition(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            if_true_func=if_player_inside_region, if_false_func=if_player_outside_region)

    @property
    def category(self):
        return Category.region


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
            skip_if_true_func=skip_if_object_not_destroyed, skip_if_false_func=skip_if_object_destroyed,
            if_true_func=if_object_not_destroyed, if_false_func=if_object_destroyed,
            end_if_true_func=end_if_object_not_destroyed, end_if_false_func=end_if_object_destroyed,
            restart_if_true_func=restart_if_object_not_destroyed, restart_if_false_func=restart_if_object_destroyed)

    @property
    def category(self):
        return Category.object


class Character(MapEntity):
    """ Condition upon a character as a shortcut to condition upon them being alive. """
    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return _get_value_condition(
            value=value, negate=negate, condition=condition, skip_lines=0,
            if_true_func=if_entity_alive, if_false_func=if_entity_dead)

    @property
    def category(self):
        return Category.character


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

    @staticmethod
    def get_type():
        raise NotImplementedError


class Weapon(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=if_player_has_weapon,
            if_false_func=if_player_does_not_have_weapon)

    @staticmethod
    def get_type():
        return ItemType.weapon


class Armor(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=if_player_has_armor,
            if_false_func=if_player_does_not_have_armor)

    @staticmethod
    def get_type():
        return ItemType.armor


class Ring(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=if_player_has_ring,
            if_false_func=if_player_does_not_have_ring)

    @staticmethod
    def get_type():
        return ItemType.ring


class Good(Item):
    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float)) else self.value
        return _get_value_condition(
            value=value, negate=negate, condition=condition,
            if_true_func=if_player_has_good,
            if_false_func=if_player_does_not_have_good)

    @staticmethod
    def get_type():
        return ItemType.good


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
            skip_if_true_func=skip_if_event_flag_range_not_all_off, skip_if_false_func=skip_if_event_flag_range_all_off,
            if_true_func=if_event_flag_range_not_all_off, if_false_func=if_event_flag_range_all_off,
            end_if_true_func=end_if_event_flag_range_not_all_off, end_if_false_func=end_if_event_flag_range_all_off,
            restart_if_true_func=restart_if_event_flag_range_not_all_off,
            restart_if_false_func=restart_if_event_flag_range_all_off,
        )

    def all(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return _get_value_condition(
            value=self, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=skip_if_event_flag_range_all_on, skip_if_false_func=skip_if_event_flag_range_not_all_on,
            if_true_func=if_event_flag_range_all_on, if_false_func=if_event_flag_range_not_all_on,
            end_if_true_func=end_if_event_flag_range_all_on, end_if_false_func=end_if_event_flag_range_not_all_on,
            restart_if_true_func=restart_if_event_flag_range_all_on,
            restart_if_false_func=restart_if_event_flag_range_not_all_on,
        )


class Map(object):
    def __init__(self, block_id, sub_id):
        self.block_id = block_id
        self.sub_id = sub_id

    def __eq__(self, other_map):
        return self.block_id == other_map.block_id and self.sub_id == other_map.sub_id


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
