from __future__ import annotations

from enum import IntEnum
from typing import Union

from soulstruct.events.internal import get_value_test
from soulstruct.events.shared import instructions as instr
from soulstruct.enums.shared import CoordEntityType, NavmeshType
from soulstruct.game_types.basic_types import GameObject

__all__ = [
    "Entity",
    "EventEntity",
    "CoordEntity",
    "SoundEvent",
    "FXEvent",
    "SpawnerEvent",
    "MessageEvent",
    "ObjActEvent",
    "SpawnPointEvent",
    "NavmeshEvent",
    "Object",
    "Region",
    "Character",
    "MapPiece",
    "Collision",
    "PlayerStart",
    "Navmesh",
    "MapLoadTrigger",
    "EntityInt",
    "CoordEntityInt",
    "ObjectInt",
    "RegionInt",
    "CharacterInt",
    "AnimatedInt",
    "MapPieceInt",
    "CollisionInt",
    "NavmeshEventInt",
]


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


class SoundEvent(EventEntity):
    """Sound event in MSB attached to a Region (a 'map sound'), which can be enabled or disabled.

    Note that these are enabled on map load, so you may want to disable it (e.g. boss music) in your constructor event.
    """

    def enable(self):
        return instr.EnableSoundEvent(self)

    def disable(self):
        return instr.DisableSoundEvent(self)


class FXEvent(EventEntity):
    """FX event (visual effect, e.g. fog gate) in MSB attached to a region.

    Can be created or deleted. When deleted, the particles already emitted can be allowed to live out their remaining
    life (`erase_root_only=True` by default).
    """

    def create(self):
        return instr.CreateFX(self)

    def delete(self, erase_root_only=True):
        return instr.DeleteFX(self, erase_root_only=erase_root_only)


class SpawnerEvent(EventEntity):
    """Spawner event (causes linked enemies to respawn) in MSB attached to a region. Can be enabled or disabled."""

    def enable(self):
        return instr.EnableSpawner(self)

    def disable(self):
        return instr.DisableSpawner(self)


class MessageEvent(EventEntity):
    """Message event in MSB that causes a "developer message" to appear in a region. Can be enabled or disabled."""

    def enable(self):
        return instr.EnableSoapstoneMessage(self)

    def disable(self):
        return instr.DisableSoapstoneMessage(self)


class ObjActEvent(EventEntity):
    """ObjAct (object activation event) added in MSB.

    It can be used in conditions as a test for the ObjAct event being triggered.
    """

    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines, if_true_func=instr.IfObjectActivated
        )

    def enable(self, obj: Object, relative_index=None):
        return instr.EnableObjectActivation(obj=obj, obj_act_id=self, relative_index=relative_index)

    def disable(self, obj: Object, relative_index=None):
        return instr.DisableObjectActivation(obj=obj, obj_act_id=self, relative_index=relative_index)


class SpawnPointEvent(Entity):
    """Spawn point attached to an MSB region."""

    def set_respawn(self):
        return instr.SetRespawnPoint(self)


class NavmeshEvent(Entity):
    """Navmesh event attached to an MSB navmesh part. Enable/disable/toggle functions require you to specify a
    navigation type; only the flags for that type will be modified in the navmesh."""

    def enable(self, navmesh_type: NavmeshType):
        return instr.EnableNavmeshType(self, navmesh_type)

    def disable(self, navmesh_type: NavmeshType):
        return instr.DisableNavmeshType(self, navmesh_type)

    def toggle(self, navmesh_type: NavmeshType):
        return instr.ToggleNavmeshType(self, navmesh_type)


class Object(CoordEntity):
    """ Condition upon an object as a shortcut to condition upon it *not* being destroyed. """

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfObjectNotDestroyed,
            skip_if_false_func=instr.SkipLinesIfObjectDestroyed,
            if_true_func=instr.IfObjectNotDestroyed,
            if_false_func=instr.IfObjectDestroyed,
            end_if_true_func=instr.EndIfObjectNotDestroyed,
            end_if_false_func=instr.EndIfObjectDestroyed,
            restart_if_true_func=instr.RestartIfObjectNotDestroyed,
            restart_if_false_func=instr.RestartIfObjectDestroyed,
        )

    @property
    def coord_entity_type(self):
        return CoordEntityType.Object

    def enable(self):
        return instr.EnableObject(self)

    def disable(self):
        return instr.DisableObject(self)

    def activate(self, obj_act_id: ObjActEvent, relative_index=None):
        return instr.ActivateObject(self, obj_act_id=obj_act_id, relative_index=relative_index)


class Region(CoordEntity):
    """ Condition upon a region as a shortcut to condition upon the player being inside it (condition only). """

    def __call__(self, negate=False, condition=None, skip_lines=0):
        try:
            value = self.value
        except AttributeError:
            value = self
        return get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            if_true_func=instr.IfPlayerInsideRegion,
            if_false_func=instr.IfPlayerOutsideRegion,
        )

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
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            if_true_func=instr.IfCharacterAlive,
            if_false_func=instr.IfCharacterDead,
        )

    @property
    def coord_entity_type(self):
        return CoordEntityType.Character

    def enable(self):
        return instr.EnableCharacter(self)

    def disable(self):
        return instr.EnableCharacter(self)

    def enable_collision(self):
        return instr.EnableCharacterCollision(self)

    def disable_collision(self):
        return instr.DisableCharacterCollision(self)


class MapPiece(Entity):
    """Map Piece added in MSB."""

    def enable(self):
        return instr.EnableMapPiece(self)

    def disable(self):
        return instr.DisableMapPiece(self)


class Collision(Entity):
    """Collision added in MSB."""

    def enable(self):
        return instr.EnableCollision(self)

    def disable(self):
        return instr.DisableCollision(self)

    def enable_backread_mask(self):
        return instr.EnableCollisionBackreadMask(self)

    def disable_backread_mask(self):
        return instr.DisableCollisionBackreadMask(self)


class PlayerStart(Entity):
    """PlayerStart added in MSB. Used as an argument in `Warp` instructions. No additional state."""

    pass


class Navmesh(Entity):
    """Navmesh instance. NavmeshEvents are attached to it and manipulated with EMEVD."""

    pass


class MapLoadTrigger(Entity):
    """MapConnection added in MSB. No additional state."""

    pass


EntityInt = Union[Entity, int]
CoordEntityInt = Union[CoordEntity, int]
ObjectInt = Union[Object, int]
RegionInt = Union[Region, int]
CharacterInt = Union[Character, int]
AnimatedInt = Union[Character, Object, int]
MapPieceInt = Union[MapPiece, int]
CollisionInt = Union[Collision, int]
NavmeshEventInt = Union[NavmeshEvent, int]
