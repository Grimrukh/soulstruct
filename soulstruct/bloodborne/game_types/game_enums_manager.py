
from soulstruct.base.game_types.game_enums_manager import GameEnumsManager as _BaseGameEnumsManager
from soulstruct.bloodborne.game_types import *


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
        Text,
        ItemLotParam,
        WeaponParam,
        ArmorParam,
        GoodParam,
        AccessoryParam,
        Animation,
    )
