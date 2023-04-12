from __future__ import annotations

__all__ = [
    "Map",
    "MapTyping",
    "MapEntry",
    "MapEntity",

    "MapModel",
    "MapPieceModel",
    "ObjectModel",
    "CharacterModel",
    "PlayerModel",
    "CollisionModel",
    "NavmeshModel",

    "MapEvent",
    "LightEvent",
    "SoundEvent",
    "VFXEvent",
    "WindEvent",
    "TreasureEvent",
    "SpawnerEvent",
    "MessageEvent",
    "ObjActEvent",
    "SpawnPointEvent",
    "MapOffsetEvent",
    "NavigationEvent",
    "EnvironmentEvent",
    "NPCInvasionEvent",

    "MapPart",
    "MapPiece",
    "Object",
    "Character",
    "Collision",
    "PlayerStart",
    "Navmesh",
    "UnusedObject",
    "UnusedCharacter",
    "MapConnection",

    "Region",
    "RegionVolume",
    "RegionPoint",
    "RegionCircle",
    "RegionSphere",
    "RegionCylinder",
    "RegionRect",
    "RegionBox",

    "MapPartTyping",
    "CoordEntityTyping",
    "ObjectTyping",
    "RegionTyping",
    "CharacterTyping",
    "AnimatedEntityTyping",
    "MapPieceTyping",
    "CollisionTyping",
    "SoundEventTyping",
    "EnvironmentEventTyping",
    "NavigationEventTyping",
    "VFXEventTyping",
    "NPCInvasionEventTyping",
    
    "ID_RANGES",
]

from soulstruct.base.game_types.map_types import *


# Callables with `map_base_id` to get prescribed DS1 entity ID range for each MSB entity type, as class kwargs.
#   Usage: `class Characters(Character, **ID_RANGES[Character](map_base_id)): ...`
# Note that these are GUIDELINES for vanilla usage, but are not always followed. A few maps also have clashing IDs over
# different supertypes in vanilla DS1.
ID_RANGES = {
    RegionVolume: lambda map_base_id: dict(first_value=2000 + map_base_id, last_value=2499 + map_base_id),
    RegionPoint: lambda map_base_id: dict(first_value=2500 + map_base_id, last_value=2899 + map_base_id),

    MapPiece: lambda map_base_id: dict(first_value=3000 + map_base_id, last_value=3199 + map_base_id),
    Collision: lambda map_base_id: dict(first_value=3200 + map_base_id, last_value=3399 + map_base_id),
    Object: lambda map_base_id: dict(first_value=1000 + map_base_id, last_value=1899 + map_base_id),
    # IDs 1900-1989 are reserved for bonfire object entities.
    Character: lambda map_base_id: dict(first_value=0 + map_base_id, last_value=899 + map_base_id),
    # IDs 900-989 are reserved for bonfire character entities.
    PlayerStart: lambda map_base_id: dict(first_value=990 + map_base_id, last_value=999 + map_base_id),

    SoundEvent: lambda map_base_id: dict(first_value=3800 + map_base_id, last_value=3899 + map_base_id),
    VFXEvent: lambda map_base_id: dict(first_value=3400 + map_base_id, last_value=3599 + map_base_id),
    SpawnerEvent: lambda map_base_id: dict(first_value=3600 + map_base_id, last_value=3699 + map_base_id),
    MessageEvent: lambda map_base_id: dict(first_value=3700 + map_base_id, last_value=3799 + map_base_id),
    SpawnPointEvent: lambda map_base_id: dict(first_value=3900 + map_base_id, last_value=3949 + map_base_id),
}
