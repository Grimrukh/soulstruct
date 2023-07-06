__all__ = [
    "MSBSupertype",
    "MSBModelSubtype",
    "MSBEventSubtype",
    "MSBRegionSubtype",
    "MSBPartSubtype",
    "CollisionHitFilter",
]

from enum import IntEnum

from soulstruct.base.maps.msb.enums import *


class MSBModelSubtype(BaseMSBModelSubtype):
    MapPieceModel = 0
    ObjectModel = 1
    CharacterModel = 2
    PlayerModel = 4
    CollisionModel = 5
    NavmeshModel = 6

    @classmethod
    def get_sib_path_stem(cls):
        return "N:\\FRPG\\data\\Model\\"

    @classmethod
    def get_plural_supertype_name(cls):
        return "Models"


class MSBEventSubtype(BaseMSBEventSubtype):
    Light = 0
    Sound = 1
    VFX = 2
    Wind = 3
    Treasure = 4
    Spawner = 5
    Message = 6
    ObjAct = 7
    SpawnPoint = 8
    MapOffset = 9
    Navigation = 10
    Environment = 11
    NPCInvasion = 12

    @classmethod
    def get_plural_supertype_name(cls):
        return "Events"


class MSBRegionSubtype(BaseMSBRegionSubtype):
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5

    @classmethod
    def get_plural_supertype_name(cls):
        return "Regions"


class MSBPartSubtype(BaseMSBPartSubtype):
    MapPiece = 0
    Object = 1
    Character = 2
    # 3 is unused.
    PlayerStart = 4
    Collision = 5
    # 6 is unused.
    # 7 is unused.
    Navmesh = 8
    UnusedObject = 9
    UnusedCharacter = 10
    MapConnection = 11

    @classmethod
    def get_plural_supertype_name(cls):
        return "Parts"


class CollisionHitFilter(IntEnum):
    """Defines behavior of `MSBCollision` instances in maps. Courtesy of horkrux."""
    NoHiHitNoFeetIK = 0  # solid
    NoHiHit_1 = 1  # solid
    NoHiHit_2 = 2  # solid
    NoHiHit_3 = 3  # solid
    NoHiHit_4 = 4  # solid
    NoHiHit_5 = 5  # solid
    NoHiHit_6 = 6  # solid
    NoHiHit_7 = 7  # solid
    Normal = 8  # solid
    Water_A = 9  # blue
    Unknown_10 = 10
    Solid_ForNPCsOnly_A = 11  # blue
    Unknown_12 = 12
    DeathCam = 13  # white
    LethalFall = 14  # red
    KillPlane = 15  # black
    Water_B = 16  # dark blue
    GroupSwitch = 17  # turquoise; in elevator shafts
    Unknown_18 = 18
    Solid_ForNPCsOnly_B = 19  # turquoise
    LevelExit_A = 20  # purple
    Slide = 21  # yellow
    FallProtection = 22  # permeable for projectiles
    LevelExit_B = 23  # glowing turquoise

    def is_solid_to_player(self) -> bool:
        """Generous definition. Currently includes some unknown types for safety."""
        if self <= 8:
            return True
        return self in {
            self.Unknown_10,
            self.Unknown_12,
            self.GroupSwitch,
            self.Unknown_18,
        }
