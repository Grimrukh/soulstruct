
from soulstruct.base.events.emevd.entity_enums_manager import GameEnumsManager as _BaseGameEnumsManager
from soulstruct.darksouls1ptde.game_types import *
from .enums import ProtectedEntities


class GameEnumsManager(_BaseGameEnumsManager):

    VALID_GAME_TYPES = (
        Flag,
        MapPart,
        MapPiece,
        Object,
        Character,
        PlayerStart,
        Collision,
        SoundEvent,
        VFXEvent,
        SpawnerEvent,
        MessageEvent,
        SpawnPointEvent,
        NavigationEvent,
        RegionVolume,
        RegionPoint,
    )
    PROTECTED_ENUM = ProtectedEntities
