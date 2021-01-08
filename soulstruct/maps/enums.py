__all__ = [
    "MSBSubtype",
    "MSBModelSubtype",
    "MSBEventSubtype",
    "MSBRegionSubtype",
    "MSBPartSubtype",
    "CollisionHitFilter",
]

from enum import IntEnum


class MSBSubtype(IntEnum):
    @property
    def pluralized_name(self):
        if self.name in ("Box", "Navmesh"):
            return self.name + "es"
        elif self.name in ("VFX", "Wind", "Treasure", "Navigation", "NPCInvasion", "WindVFX", "Other"):
            return self.name
        return self.name + "s"

    @classmethod
    def get_pluralized_type_name(cls):
        raise NotImplementedError


class MSBModelSubtype(MSBSubtype):
    MapPiece = 0
    Object = 1
    Character = 2
    Item = 3
    Player = 4
    Collision = 5
    Navmesh = 6
    Other = -1

    @classmethod
    def get_pluralized_type_name(cls):
        return "Models"


class MSBEventSubtype(MSBSubtype):
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
    # Bloodborne only:
    WindVFX = 13
    PatrolRoute = 14
    DarkLock = 15
    Platoon = 16
    MultiSummon = 17
    Other = -1

    @classmethod
    def get_pluralized_type_name(cls):
        return "Events"


class MSBRegionSubtype(MSBSubtype):
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5

    @classmethod
    def get_pluralized_type_name(cls):
        return "Regions"


class MSBPartSubtype(MSBSubtype):
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
    Other = -1

    @classmethod
    def get_pluralized_type_name(cls):
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
    DeathPlane = 15  # black
    Water_B = 16  # dark blue
    GroupSwitch = 17  # turquoise; in elevator shafts
    Unknown_18 = 18
    Solid_ForNPCsOnly_B = 19  # turquoise
    LevelExit_A = 20  # purple
    Slide = 21  # yellow
    FallProtection = 22  # permeable for projectiles
    LevelExit_B = 23  # glowing turquoise
