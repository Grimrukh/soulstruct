
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
        DummyCharacter,
        DummyObject,
        SoundEvent,
        VFXEvent,
        SpawnerEvent,
        MessageEvent,
        SpawnPointEvent,
        NavigationEvent,
        Region,
        Text,
        ItemLotParam,
        WeaponParam,
        ArmorParam,
        GoodParam,
        AccessoryParam,
        Animation,
    )

    RESERVED_GLOBAL_IDS = {
        10000: "PLAYER",
        10001: "CLIENT_PLAYER_1",
        10002: "CLIENT_PLAYER_2",
        10003: "CLIENT_PLAYER_3",
        10004: "CLIENT_PLAYER_4",
        10005: "CLIENT_PLAYER_5",
        10006: "CLIENT_PLAYER_6",
        10007: "CLIENT_PLAYER_7",
        10008: "CLIENT_PLAYER_8",
        10009: "CLIENT_PLAYER_9",
    }

    USE_AA_BB_ABBREVIATION = True
