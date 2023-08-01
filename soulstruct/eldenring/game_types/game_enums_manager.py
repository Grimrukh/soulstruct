
from soulstruct.base.game_types.game_enums_manager import GameEnumsManager as _BaseGameEnumsManager
from soulstruct.eldenring.game_types import *


class GameEnumsManager(_BaseGameEnumsManager):

    VALID_GAME_TYPES = (
        Flag,
        MapPart,
        MapPiece,
        Asset,
        Character,
        PlayerStart,
        Collision,
        SoundEvent,
        VFXEvent,
        SpawnerEvent,
        MessageEvent,
        SpawnPointEvent,
        NavigationEvent,
        # TODO: New region subtypes? EMEDF would need to specify them to be any use...
        #  Could also still use `RegionPoint` vs. `RegionVolume` for enum/argument purposes?
        Region,
        Text,
        ItemLotParam,
        WeaponParam,
        ArmorParam,
        GoodParam,
        AccessoryParam,
        Animation,
    )
