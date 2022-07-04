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
    "SoundEvent",
    "VFXEvent",
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
    "NavigationEventTyping",
    "VFXEventTyping",
]

import typing as tp

from soulstruct.base.game_types.map_types import Map, MapEntry, MapEntity, MapTyping


class MapModel(MapEntry):
    """3D model ID of something."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Models", None

    @classmethod
    def get_msb_class_name(cls) -> str:
        """All MSB models use the same class."""
        return "MSBModel"


class MapPieceModel(MapModel):
    """Map piece model (e.g. m0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "MapPieces") if pluralized_subtype else ("Models", "MapPiece")


class ObjectModel(MapModel):
    """Object model (e.g. o0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Objects") if pluralized_subtype else ("Models", "Object")


class CharacterModel(MapModel):
    """Character model (e.g. c0000).

    Note that c0000 can appear in either the Characters or Players parts list in an MSB.
    """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Characters") if pluralized_subtype else ("Models", "Character")


class PlayerModel(MapModel):
    """Sometimes c0000 is registered as this type instead of a CharacterModel."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Players") if pluralized_subtype else ("Models", "Player")


class CollisionModel(MapModel):
    """Map piece model (e.g. h0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Collisions") if pluralized_subtype else ("Models", "Collision")


class NavmeshModel(MapModel):
    """Navmesh model (e.g. n0000). """
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Models", "Navmeshes") if pluralized_subtype else ("Models", "Navmesh")


class MapEvent(MapEntity):
    """Base class for things that appear in the 'events' section of the MSB, such as sounds, ObjActs, and VFX."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Events", None

    def auto_region_name(self):
        event_enum_subclass = self.__class__.__bases__[0]
        while event_enum_subclass.__bases__[0] is not MapEvent:
            event_enum_subclass = event_enum_subclass.__bases__[0]
        return f"_{event_enum_subclass.__name__}_{self.name.lstrip('_')}"


class SoundEvent(MapEvent):
    """Sound event in MSB attached to a Region (a 'map sound'), which can be enabled or disabled.

    Note that these are enabled on map load, so you may want to disable it (e.g. boss music) in your constructor event.
    """

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Sounds") if pluralized_subtype else ("Events", "Sound")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 3800, 3899


class VFXEvent(MapEvent):
    """VFX event (visual effect, e.g. fog gate) in MSB attached to a region.

    Can be created or deleted. When deleted, the particles already emitted can be allowed to live out their remaining
    life (`erase_root_only=True` by default).
    """

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "VFX") if pluralized_subtype else ("Events", "VFX")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 3400, 3599


class TreasureEvent(MapEvent):
    """Treasure event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Treasure") if pluralized_subtype else ("Events", "Treasure")


class SpawnerEvent(MapEvent):
    """Spawner event (causes linked enemies to respawn) in MSB attached to a region. Can be enabled or disabled."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Spawners") if pluralized_subtype else ("Events", "Spawner")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 3600, 3699


class MessageEvent(MapEvent):
    """Message event in MSB that causes a "developer message" to appear in a region. Can be enabled or disabled."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Messages") if pluralized_subtype else ("Events", "Message")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 3700, 3799


class ObjActEvent(MapEvent):
    """ObjAct (object activation event) added in MSB.

    It can be used in conditions as a test for the ObjAct event being triggered.
    """
    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "ObjActs") if pluralized_subtype else ("Events", "ObjAct")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        raise TypeError("`ObjActEvent` does not use normal entity IDs, but uses special flags instead.")


# TODO: New Bloodborne MSB event types.


class SpawnPointEvent(MapEvent):
    """Spawn point attached to an MSB region."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "SpawnPoints") if pluralized_subtype else ("Events", "SpawnPoint")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 3900, 3949  # 3950-3989 reserved for bonfire spawn points


class MapOffsetEvent(MapEvent):
    """Map offset event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "MapOffsets") if pluralized_subtype else ("Events", "MapOffset")


class NavigationEvent(MapEvent):
    """Event attached to an MSB navmesh part.

    Enable/disable/toggle functions require you to specify a navigation type; only the flags for that type will be
    modified in the navmesh.
    """

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Navigation") if pluralized_subtype else ("Events", "Navigation")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        # return 4000, 4199
        raise TypeError(
            "Navigation entity IDs are also baked into navmesh NVM geometry, so automatic enumeration is not yet "
            "supported."
        )


class EnvironmentEvent(MapEvent):
    """Environment event in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "Environments") if pluralized_subtype else ("Events", "Environment")


class NPCInvasionEvent(MapEvent):
    """Event describing invasion of NPC's world (e.g. Lautrec) in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Events", "NPCInvasion") if pluralized_subtype else ("Events", "NPCInvasion")


class Region(MapEntity):
    """Condition upon a region as a shortcut to condition upon the player being inside it (condition only)."""

    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_coord_entity_type(cls):
        from ..events.emevd.enums import CoordEntityType
        return CoordEntityType.Region

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Regions", None


class RegionVolume(Region):
    """Soulstruct ABC for Spheres, Cylinders, and Boxes, which share an auto-enumeration schema separate from Points."""

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 2000, 2499


class RegionPoint(Region):
    """Single point region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Points") if pluralized_subtype else ("Regions", "Point")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 2500, 2899


class RegionCircle(Region):
    """2D circle region. Never used."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Circles") if pluralized_subtype else ("Regions", "Circle")


class RegionSphere(RegionVolume):
    """3D spherical region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Spheres") if pluralized_subtype else ("Regions", "Sphere")


class RegionCylinder(RegionVolume):
    """3D cylindrical region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Cylinders") if pluralized_subtype else ("Regions", "Cylinder")


class RegionRect(Region):
    """2D rectangular region. Never used."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Rects") if pluralized_subtype else ("Regions", "Rect")


class RegionBox(RegionVolume):
    """3D box region."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Boxes") if pluralized_subtype else ("Regions", "Box")


class MapPart(MapEntity):
    """Base class for anything that appears in the Parts section of the MSB."""
    @classmethod
    def get_event_arg_fmt(cls):
        return "i"

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return "Parts", None


class MapPiece(MapPart):
    """Map Piece added in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "MapPieces") if pluralized_subtype else ("Parts", "MapPiece")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 3000, 3199


class Object(MapPart):
    """Condition upon an object as a shortcut to condition upon it *not* being destroyed."""
    @classmethod
    def get_coord_entity_type(cls):
        from ..events.emevd.enums import CoordEntityType
        return CoordEntityType.Object

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Objects") if pluralized_subtype else ("Parts", "Object")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        """Note that range 1900-1999 is reserved for special manual assignment (bonfires, fog objects, fog VFX)."""
        return 1000, 1899


class Character(MapPart):
    """Condition upon a character as a shortcut to condition upon them being alive."""
    @classmethod
    def get_coord_entity_type(cls):
        from ..events.emevd.enums import CoordEntityType
        return CoordEntityType.Character

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Characters") if pluralized_subtype else ("Parts", "Character")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        """Note that range 0900-0999 is reserved for special manual assignment (bonfire characters)."""
        return 0, 899


class PlayerStart(MapPart):
    """PlayerStart added in MSB. Used as an argument in `Warp` instructions. No additional state."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "PlayerStarts") if pluralized_subtype else ("Parts", "PlayerStart")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 990, 999


class Collision(MapPart):
    """Collision added in MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Collisions") if pluralized_subtype else ("Parts", "Collision")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        return 3200, 3399


class Navmesh(MapPart):
    """Navmesh instance. NavmeshEvents are attached to it and manipulated with EMEVD."""
    @classmethod
    def get_event_arg_fmt(cls):
        return None  # not valid

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Navmeshes") if pluralized_subtype else ("Parts", "Navmesh")


class UnusedObject(MapPart):
    """Unused (or cutscene-only) object in MSB."""
    @classmethod
    def get_event_arg_fmt(cls):
        return None  # not valid

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "UnusedObjects") if pluralized_subtype else ("Parts", "UnusedObject")


class UnusedCharacter(MapPart):
    """Unused (or cutscene-only) character in MSB."""
    @classmethod
    def get_event_arg_fmt(cls):
        return None  # not valid

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "UnusedCharacters") if pluralized_subtype else ("Parts", "UnusedCharacter")


class MapConnection(MapPart):
    """MapConnection added in MSB. No additional state."""
    @classmethod
    def get_event_arg_fmt(cls):
        return None  # not valid

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False):
        return ("Parts", "MapConnections") if pluralized_subtype else ("Parts", "MapConnection")


MapPartTyping = tp.Union[MapPart, int]
CoordEntityTyping = tp.Union[Object, Region, Character, int]
ObjectTyping = tp.Union[Object, int]
RegionTyping = tp.Union[Region, int]
CharacterTyping = tp.Union[Character, int]
AnimatedEntityTyping = tp.Union[Character, Object, int]
MapPieceTyping = tp.Union[MapPiece, int]
CollisionTyping = tp.Union[Collision, int]
NavigationEventTyping = tp.Union[NavigationEvent, int]
EnvironmentEventTyping = tp.Union[EnvironmentEvent, int]
NPCInvasionEventTyping = tp.Union[NPCInvasionEvent, int]
VFXEventTyping = tp.Union[VFXEvent, int]
