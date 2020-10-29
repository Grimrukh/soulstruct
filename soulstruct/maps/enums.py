__all__ = ["MSBSubtype", "MSBModelSubtype", "MSBEventSubtype", "MSBRegionSubtype", "MSBPartSubtype"]

from enum import IntEnum


class MSBSubtype(IntEnum):
    @property
    def pluralized_name(self):
        if self.name in ("Box", "Navmesh"):
            return self.name + "es"
        elif self.name in ("FX", "Wind", "Treasure", "Navigation"):
            return self.name
        return self.name + "s"

    @classmethod
    def get_pluralized_type_name(cls):
        raise NotImplementedError


class MSBModelSubtype(MSBSubtype):
    MapPiece = 0
    Object = 1
    Character = 2
    Unknown = 3
    Player = 4
    Collision = 5
    Navmesh = 6

    @classmethod
    def get_pluralized_type_name(cls):
        return "Models"


class MSBEventSubtype(MSBSubtype):
    Light = 0
    Sound = 1
    FX = 2
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

    @classmethod
    def get_pluralized_type_name(cls):
        return "Parts"
