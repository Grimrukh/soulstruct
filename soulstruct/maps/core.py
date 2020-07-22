from enum import IntEnum

from soulstruct.utilities import BiDict


class MSB_PART_TYPE(IntEnum):
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
    MapLoadTrigger = 11


class MSB_EVENT_TYPE(IntEnum):
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


class MSB_REGION_TYPE(IntEnum):
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5


class MSB_MODEL_TYPE(IntEnum):
    MapPiece = 0
    Object = 1
    Character = 2
    Unknown = 3
    Player = 4
    Collision = 5
    Navmesh = 6


MAP_ENTRY_TYPES = {
    "Parts": BiDict(
        ("MapPieces", MSB_PART_TYPE.MapPiece),
        ("Objects", MSB_PART_TYPE.Object),
        ("Characters", MSB_PART_TYPE.Character),
        ("PlayerStarts", MSB_PART_TYPE.PlayerStart),
        ("Collisions", MSB_PART_TYPE.Collision),
        ("Navmeshes", MSB_PART_TYPE.Navmesh),
        ("UnusedObjects", MSB_PART_TYPE.UnusedObject),
        ("UnusedCharacters", MSB_PART_TYPE.UnusedCharacter),
        ("MapLoadTriggers", MSB_PART_TYPE.MapLoadTrigger),
    ),
    "Events": BiDict(
        ("Lights", MSB_EVENT_TYPE.Light),
        ("Sounds", MSB_EVENT_TYPE.Sound),
        ("FX", MSB_EVENT_TYPE.FX),
        ("Wind", MSB_EVENT_TYPE.Wind),
        ("Treasure", MSB_EVENT_TYPE.Treasure),
        ("Spawners", MSB_EVENT_TYPE.Spawner),
        ("Messages", MSB_EVENT_TYPE.Message),
        ("ObjActs", MSB_EVENT_TYPE.ObjAct),
        ("SpawnPoints", MSB_EVENT_TYPE.SpawnPoint),
        ("MapOffsets", MSB_EVENT_TYPE.MapOffset),
        ("Navigation", MSB_EVENT_TYPE.Navigation),
        ("Environment", MSB_EVENT_TYPE.Environment),
        ("NPCInvasions", MSB_EVENT_TYPE.NPCInvasion),
    ),
    "Regions": BiDict(
        ("Points", MSB_REGION_TYPE.Point),
        ("Circles", MSB_REGION_TYPE.Circle),
        ("Spheres", MSB_REGION_TYPE.Sphere),
        ("Cylinders", MSB_REGION_TYPE.Cylinder),
        ("Rectangles", MSB_REGION_TYPE.Rect),
        ("Boxes", MSB_REGION_TYPE.Box),
    ),
    "Models": BiDict(
        ("MapPieces", MSB_MODEL_TYPE.MapPiece),
        ("Objects", MSB_MODEL_TYPE.Object),
        ("Characters", MSB_MODEL_TYPE.Character),
        ("Unknown", MSB_MODEL_TYPE.Unknown),
        ("Players", MSB_MODEL_TYPE.Player),
        ("Collisions", MSB_MODEL_TYPE.Collision),
        ("Navmeshes", MSB_MODEL_TYPE.Navmesh),
    ),
}
