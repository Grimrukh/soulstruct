
from soulstruct.base.events.emevd.entity_enums_manager import EntityEnumsManager as _BaseEntityEnumsManager
from soulstruct.darksouls1ptde.game_types import *
from .enums import ProtectedEntities


class EntityEnumsManager(_BaseEntityEnumsManager):

    ENTITY_ID_SUBCLASSES = {
        "parts": (MapPiece, Object, Character, PlayerStart, Collision),
        "events": (SoundEvent, VFXEvent, SpawnerEvent, MessageEvent, SpawnPointEvent, NavigationEvent),
        "regions": (RegionPoint, RegionCircle, RegionCylinder, RegionSphere, RegionRect, RegionBox),
    }
    PROTECTED_ENTITIES = ProtectedEntities
