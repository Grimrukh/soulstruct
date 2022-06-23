__all__ = [
    "MSBModelSubtype",
    "MSBEventSubtype",
    "MSBRegionSubtype",
    "MSBPartSubtype",
    "CollisionHitFilter",
]

from soulstruct.base.maps.msb.enums import *
from enum import IntEnum


class MSBModelSubtype(BaseMSBModelSubtype):
    MapPiece = 0
    Object = 1
    Character = 2
    Item = 3
    Player = 4
    Collision = 5
    Navmesh = 6
    Other = -1

    @property
    def sib_path_stem(self):
        return "N:\\SPRJ\\data\\Model\\"

    @classmethod
    def get_pluralized_type_name(cls):
        return "Models"

    def get_default_sib_path(self, name, map_id=()):

        if self in (MSBModelSubtype.MapPiece, MSBModelSubtype.Collision, MSBModelSubtype.Navmesh):
            if not isinstance(map_id, (list, tuple)) or len(map_id) not in {2, 4}:
                raise TypeError(
                    f"`map_id` for Map Pieces, Collisions, and Navmeshes must be a sequence of 2/4 map ID parts, "
                    f"e.g. (10, 2) or (10, 2, 0, 0), not {repr(map_id)}"
                )
            if len(map_id) == 2:
                map_id = (map_id[0], map_id[1], 0, 0)
            stem = self.sib_path_stem + "map\\m{:02d}_{:02d}_{:02d}_{:02d}\\".format(*map_id)
            if self == MSBModelSubtype.MapPiece:
                if not name.startswith("m"):
                    raise ValueError(f"MapPiece model name did not start with 'm': {name}")
                return stem + f"sib\\{name}.sib"
            elif self == MSBModelSubtype.Collision:
                if not name.startswith("h"):
                    raise ValueError(f"Collision model name did not start with 'h': {name}")
                return stem + f"hkxwin\\{name}.hkxwin"
            elif self == MSBModelSubtype.Navmesh:
                if not name.startswith("n"):
                    raise ValueError(f"Navmesh model name did not start with 'n': {name}")
                return stem + f"navimesh\\{name}.SIB"
        elif self in (MSBModelSubtype.Character, MSBModelSubtype.Player):
            if not name.startswith("c"):
                raise ValueError(f"Character/Player model name did not start with 'c': {name}")
            return self.sib_path_stem + f"chr\\{name}\\sib\\{name}.sib"
        elif self == MSBModelSubtype.Object:
            if not name.startswith("o"):
                raise ValueError(f"Object model name did not start with 'o': {name}")
            return self.sib_path_stem + f"obj\\{name}\\sib\\{name}.sib"
        # TODO: Item/Other defaults?
        raise ValueError(f"Invalid MSB model type: {repr(self)}. Cannot determine SIB path.")


class MSBEventSubtype(BaseMSBEventSubtype):
    Sound = 1
    VFX = 2
    Treasure = 4
    Spawner = 5
    Message = 6
    ObjAct = 7
    SpawnPoint = 8
    MapOffset = 9
    Navigation = 10
    Environment = 11
    WindVFX = 13
    PatrolRoute = 14
    DarkLock = 15
    Platoon = 16
    MultiSummon = 17
    Other = -1

    @classmethod
    def get_pluralized_type_name(cls):
        return "Events"


class MSBRegionSubtype(BaseMSBRegionSubtype):
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5

    @classmethod
    def get_pluralized_type_name(cls):
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
    KillPlane = 15  # black
    Water_B = 16  # dark blue
    GroupSwitch = 17  # turquoise; in elevator shafts
    Unknown_18 = 18
    Solid_ForNPCsOnly_B = 19  # turquoise
    LevelExit_A = 20  # purple
    Slide = 21  # yellow
    FallProtection = 22  # permeable for projectiles
    LevelExit_B = 23  # glowing turquoise
