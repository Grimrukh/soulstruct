from enum import IntEnum
from typing import Union

from soulstruct.events.internal import get_value_test
from soulstruct.events.shared import instructions as instr
from soulstruct.enums.shared import CoordEntityType
from soulstruct.game_types.basic_types import GameObject

__all__ = ['Entity', 'EventEntity', 'CoordEntity',
           'MapSound', 'ObjAct',
           'Object', 'Region', 'Character',
           'Collision',
           'EntityInt', 'CoordEntityInt', 'ObjectInt', 'RegionInt', 'CharacterInt', 'AnimatedInt', 'CollisionInt']


class Entity(GameObject, IntEnum):
    """Base class for anything that appears in the MSB."""
    pass


class EventEntity(Entity):
    """Base class for things that appear in the 'events' section of the MSB, such as sounds, ObjActs, and FX."""
    pass


class CoordEntity(Entity):
    """Base class for things with coordinates (transforms) in the MSB: Objects, Regions, and Characters."""

    def __call__(self, negate=False, condition=None, skip_lines=0):
        raise NotImplementedError

    @property
    def coord_entity_type(self):
        raise NotImplementedError


class MapSound(EventEntity):
    """Sound event in MSB attached to a Region (a 'map sound'), which can be enabled or disabled.

    Note that these are enabled on map load, so you may want to disable it (e.g. boss music) in your constructor event.
    """

    def enable(self):
        return instr.EnableMapSound(self.value)

    def disable(self):
        return instr.DisableMapSound(self.value)


class ObjAct(EventEntity):
    """ObjAct (object activation event) added in MSB.

    It can be used in conditions as a test for the ObjAct event being triggered.
    """

    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            if_true_func=instr.IfObjectActivated)


class Object(CoordEntity):
    """ Condition upon an object as a shortcut to condition upon it *not* being destroyed. """

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfObjectNotDestroyed,
            skip_if_false_func=instr.SkipLinesIfObjectDestroyed,
            if_true_func=instr.IfObjectNotDestroyed,
            if_false_func=instr.IfObjectDestroyed,
            end_if_true_func=instr.EndIfObjectNotDestroyed,
            end_if_false_func=instr.EndIfObjectDestroyed,
            restart_if_true_func=instr.RestartIfObjectNotDestroyed,
            restart_if_false_func=instr.RestartIfObjectDestroyed)

    @property
    def coord_entity_type(self):
        return CoordEntityType.Object


class Region(CoordEntity):
    """ Condition upon a region as a shortcut to condition upon the player being inside it (condition only). """

    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            if_true_func=instr.IfPlayerInsideRegion, if_false_func=instr.IfPlayerOutsideRegion)

    @property
    def coord_entity_type(self):
        return CoordEntityType.Region


class Character(CoordEntity):
    """ Condition upon a character as a shortcut to condition upon them being alive. """

    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            if_true_func=instr.IfCharacterAlive, if_false_func=instr.IfCharacterDead)

    @property
    def coord_entity_type(self):
        return CoordEntityType.Character


class Collision(Entity):
    """Collision added in MSB. No additional state."""
    pass


EntityInt = Union[Entity, int]
CoordEntityInt = Union[CoordEntity, int]
ObjectInt = Union[Object, int]
RegionInt = Union[Region, int]
CharacterInt = Union[Character, int]
AnimatedInt = Union[Character, Object, int]
CollisionInt = Union[Collision, int]
