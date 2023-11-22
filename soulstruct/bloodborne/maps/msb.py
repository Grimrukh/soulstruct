from __future__ import annotations

__all__ = ["MSB"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBEntryList
from soulstruct.base.maps.msb.utils import MSBSubtypeInfo
from soulstruct.utilities.binary import *

from .constants import get_map
from .enums import *
from .models import *
from .events import *
from .regions import *
from .parts import *


@dataclass(slots=True)
class MSBEntrySuperlistHeader(BinaryStruct):
    _version: int = field(init=False, **Binary(asserted=3))
    entry_offset_count: int
    name_offset: long


MSB_ENTRY_SUBTYPES = {
    "MODEL_PARAM_ST": {
        "MapPieceModel": MSBSubtypeInfo(MSBModelSubtype.MapPieceModel, MSBMapPieceModel, "map_piece_models"),
        "ObjectModel": MSBSubtypeInfo(MSBModelSubtype.ObjectModel, MSBObjectModel, "object_models"),
        "CharacterModel": MSBSubtypeInfo(MSBModelSubtype.CharacterModel, MSBCharacterModel, "character_models"),
        "ItemModel": MSBSubtypeInfo(MSBModelSubtype.ItemModel, MSBItemModel, "item_models"),
        "PlayerModel": MSBSubtypeInfo(MSBModelSubtype.PlayerModel, MSBPlayerModel, "player_models"),
        "CollisionModel": MSBSubtypeInfo(MSBModelSubtype.CollisionModel, MSBCollisionModel, "collision_models"),
        "NavmeshModel": MSBSubtypeInfo(MSBModelSubtype.NavmeshModel, MSBNavmeshModel, "navmesh_models"),
        "OtherModel": MSBSubtypeInfo(MSBModelSubtype.OtherModel, MSBOtherModel, "other_models"),
    },
    "EVENT_PARAM_ST": {
        # 0 (Light) unused.
        "Sound": MSBSubtypeInfo(MSBEventSubtype.Sound, MSBSoundEvent, "sounds"),
        "VFX": MSBSubtypeInfo(MSBEventSubtype.VFX, MSBVFXEvent, "vfx"),
        # 3 (Wind) unused.
        "Treasure": MSBSubtypeInfo(MSBEventSubtype.Treasure, MSBTreasureEvent, "treasures"),
        "Spawner": MSBSubtypeInfo(MSBEventSubtype.Spawner, MSBSpawnerEvent, "spawners"),
        "Message": MSBSubtypeInfo(MSBEventSubtype.Message, MSBMessageEvent, "messages"),
        "ObjAct": MSBSubtypeInfo(MSBEventSubtype.ObjAct, MSBObjActEvent, "obj_acts"),
        "SpawnPoint": MSBSubtypeInfo(MSBEventSubtype.SpawnPoint, MSBSpawnPointEvent, "spawn_points"),
        "MapOffset": MSBSubtypeInfo(MSBEventSubtype.MapOffset, MSBMapOffsetEvent, "map_offsets"),
        "Navigation": MSBSubtypeInfo(MSBEventSubtype.Navigation, MSBNavigationEvent, "navigation"),
        "Environment": MSBSubtypeInfo(MSBEventSubtype.Environment, MSBEnvironmentEvent, "environments"),
        # 12 (NPC Invasions) unused.
        "WindVFX": MSBSubtypeInfo(MSBEventSubtype.WindVFX, MSBWindVFXEvent, "wind_vfx"),
        "PatrolRoute": MSBSubtypeInfo(MSBEventSubtype.PatrolRoute, MSBPatrolRouteEvent, "patrol_routes"),
        "DarkLock": MSBSubtypeInfo(MSBEventSubtype.DarkLock, MSBDarkLockEvent, "dark_locks"),
        "Platoon": MSBSubtypeInfo(MSBEventSubtype.Platoon, MSBPlatoonEvent, "platoons"),
        "MultiSummon": MSBSubtypeInfo(MSBEventSubtype.MultiSummon, MSBMultiSummonEvent, "multi_summons"),
        "OtherEvent": MSBSubtypeInfo(MSBEventSubtype.OtherEvent, MSBOtherEvent, "other_events"),
    },
    "POINT_PARAM_ST": {
        "Point": MSBSubtypeInfo(MSBRegionSubtype.Point, MSBRegionPoint, "points"),
        "Circle": MSBSubtypeInfo(MSBRegionSubtype.Circle, MSBRegionCircle, "circles"),
        "Sphere": MSBSubtypeInfo(MSBRegionSubtype.Sphere, MSBRegionSphere, "spheres"),
        "Cylinder": MSBSubtypeInfo(MSBRegionSubtype.Cylinder, MSBRegionCylinder, "cylinders"),
        "Rect": MSBSubtypeInfo(MSBRegionSubtype.Rect, MSBRegionRect, "rects"),
        "Box": MSBSubtypeInfo(MSBRegionSubtype.Box, MSBRegionBox, "boxes"),
    },
    "PARTS_PARAM_ST": {
        "MapPiece": MSBSubtypeInfo(MSBPartSubtype.MapPiece, MSBMapPiece, "map_pieces"),
        "Object": MSBSubtypeInfo(MSBPartSubtype.Object, MSBObject, "objects"),
        "Character": MSBSubtypeInfo(MSBPartSubtype.Character, MSBCharacter, "characters"),
        # 3 unused.
        "PlayerStart": MSBSubtypeInfo(MSBPartSubtype.PlayerStart, MSBPlayerStart, "player_starts"),
        "Collision": MSBSubtypeInfo(MSBPartSubtype.Collision, MSBCollision, "collisions"),
        # 6 unused.
        # 7 unused.
        "Navmesh": MSBSubtypeInfo(MSBPartSubtype.Navmesh, MSBNavmesh, "navmeshes"),
        "UnusedObject": MSBSubtypeInfo(MSBPartSubtype.UnusedObject, MSBUnusedObject, "unused_objects"),
        "UnusedCharacter": MSBSubtypeInfo(MSBPartSubtype.UnusedCharacter, MSBUnusedCharacter, "unused_characters"),
        "MapConnection": MSBSubtypeInfo(MSBPartSubtype.MapConnection, MSBMapConnection, "map_connections"),
        "OtherPart": MSBSubtypeInfo(MSBPartSubtype.OtherPart, MSBOtherPart, "other_parts"),
    },
}


def empty_list(supertype_prefix: str, subtype_enum_name: str) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(f"{supertype_prefix}_PARAM_ST")
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum_name]
    return lambda: MSBEntryList(supertype=supertype, subtype_info=subtype_info)


@dataclass(slots=True, kw_only=True)
class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[str, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        "MODEL_PARAM_ST": 8,
        "EVENT_PARAM_ST": 12,
        "POINT_PARAM_ST": 16,
        "PARTS_PARAM_ST": 20,
    }
    ENTITY_GAME_TYPES: tp.ClassVar[dict[str, MapEntity]] = {}  # TODO for Bloodborne
    
    HAS_HEADER: tp.ClassVar[bool] = True
    LONG_VARINTS: tp.ClassVar[bool] = True
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty_list("MODEL", "MapPieceModel"))
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=empty_list("MODEL", "ObjectModel"))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty_list("MODEL", "CharacterModel"))
    item_models: MSBEntryList[MSBItemModel] = field(default_factory=empty_list("MODEL", "ItemModel"))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty_list("MODEL", "PlayerModel"))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty_list("MODEL", "CollisionModel"))
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=empty_list("MODEL", "NavmeshModel"))
    other_models: MSBEntryList[MSBOtherModel] = field(default_factory=empty_list("MODEL", "OtherModel"))

    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=empty_list("EVENT", "Sound"))
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=empty_list("EVENT", "VFX"))
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty_list("EVENT", "Treasure"))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty_list("EVENT", "Spawner"))
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=empty_list("EVENT", "Message"))
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=empty_list("EVENT", "ObjAct"))
    spawn_points: MSBEntryList[MSBSpawnPointEvent] = field(default_factory=empty_list("EVENT", "SpawnPoint"))
    map_offsets: MSBEntryList[MSBMapOffsetEvent] = field(default_factory=empty_list("EVENT", "MapOffset"))
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=empty_list("EVENT", "Navigation"))
    environments: MSBEntryList[MSBEnvironmentEvent] = field(default_factory=empty_list("EVENT", "Environment"))
    wind_vfx: MSBEntryList[MSBWindVFXEvent] = field(default_factory=empty_list("EVENT", "WindVFX"))
    patrol_routes: MSBEntryList[MSBPatrolRouteEvent] = field(default_factory=empty_list("EVENT", "PatrolRoute"))
    dark_locks: MSBEntryList[MSBDarkLockEvent] = field(default_factory=empty_list("EVENT", "DarkLock"))
    platoons: MSBEntryList[MSBPlatoonEvent] = field(default_factory=empty_list("EVENT", "Platoon"))
    multi_summons: MSBEntryList[MSBMultiSummonEvent] = field(default_factory=empty_list("EVENT", "MultiSummon"))
    other_events: MSBEntryList[MSBOtherEvent] = field(default_factory=empty_list("EVENT", "OtherEvent"))

    points: MSBEntryList[MSBRegionPoint] = field(default_factory=empty_list("POINT", "Point"))
    circles: MSBEntryList[MSBRegionCircle] = field(default_factory=empty_list("POINT", "Circle"))
    spheres: MSBEntryList[MSBRegionSphere] = field(default_factory=empty_list("POINT", "Sphere"))
    cylinders: MSBEntryList[MSBRegionCylinder] = field(default_factory=empty_list("POINT", "Cylinder"))
    rects: MSBEntryList[MSBRegionRect] = field(default_factory=empty_list("POINT", "Rect"))
    boxes: MSBEntryList[MSBRegionBox] = field(default_factory=empty_list("POINT", "Box"))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty_list("PARTS", "MapPiece"))
    objects: MSBEntryList[MSBObject] = field(default_factory=empty_list("PARTS", "Object"))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty_list("PARTS", "Character"))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty_list("PARTS", "PlayerStart"))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty_list("PARTS", "Collision"))
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=empty_list("PARTS", "Navmesh"))
    unused_objects: MSBEntryList[MSBUnusedObject] = field(default_factory=empty_list("PARTS", "UnusedObject"))
    unused_characters: MSBEntryList[MSBUnusedCharacter] = field(default_factory=empty_list("PARTS", "UnusedCharacter"))
    map_connections: MSBEntryList[MSBMapConnection] = field(default_factory=empty_list("PARTS", "MapConnection"))
    other_parts: MSBEntryList[MSBOtherPart] = field(default_factory=empty_list("PARTS", "OtherPart"))

    def pack_supertype_name(self, writer: BinaryWriter, supertype_name: str):
        packed_name = supertype_name.encode(self.NAME_ENCODING)
        writer.append(packed_name)
        writer.pad(8)

    # region Utility Methods
    def duplicate_collision_with_environment_event(
        self, collision: MSBCollision | str, at_next_index=True, **kwargs,
    ) -> MSBCollision:
        """Duplicate a Collision and any attached `MSBEnvironment` instance and its region."""
        if "name" not in kwargs:
            raise ValueError(f"Must pass `name` to Collision duplication call to duplicate attached environment event.")
        if not isinstance(collision, MSBCollision):
            collision = self.collisions.find_entry_name(collision)
        name = kwargs["name"]
        new_collision = self.collisions.duplicate(collision, at_next_index=at_next_index, **kwargs)
        if not new_collision.environment_event:
            return new_collision

        environment_event = new_collision.environment_event
        if not environment_event.attached_region:
            raise AttributeError(f"Environment event '{environment_event.name}' has no anchor Region.")
        environment_region = environment_event.attached_region
        region_subtype_list = self.get_list_of_entry(environment_region)

        new_event = self.environments.duplicate(environment_event, name=f"GI Event ({name})")
        new_event.attached_region = region_subtype_list.duplicate(environment_region, name=f"GI Region ({name})")
        new_collision.environment_event = new_event
        return new_collision

    def create_map_connection_from_collision(
        self, collision: MSBCollision | str, connected_map, name=None, draw_groups=None, display_groups=None
    ):
        """Creates a new `MapConnection` that references and copies the transform of the given `collision`.

        The `name` and `map_id` of the new `MapConnection` must be given. You can also specify its `draw_groups` and
        `display_groups`. Otherwise, it will leave them as the extensive default values: [0, ..., 127].
        """
        if not isinstance(collision, MSBCollision):
            collision = self.collisions.find_entry_name(collision)
        if name is None:
            game_map = get_map(connected_map)
            name = collision.name + f"_[{game_map.area_id:02d}_{game_map.block_id:02d}]"
        if name in self.map_connections.get_entry_names():
            raise ValueError(f"{repr(name)} is already the name of an existing `MSBMapConnection`.")
        map_connection = self.map_connections.new(
            name=name,
            connected_map=connected_map,
            collision=collision,
            translate=collision.translate.copy(),
            rotate=collision.rotate.copy(),
            scale=collision.scale.copy(),  # for completion's sake
            model=collision.model,
        )
        if draw_groups is not None:  # otherwise keep same draw groups
            map_connection.draw_groups = draw_groups
        if display_groups is not None:  # otherwise keep same display groups
            map_connection.display_groups = display_groups
        return map_connection

    def new_c1000(self, name: str, **kwargs) -> MSBCharacter:
        """Useful to create basic c1000 instances as debug warp points."""
        return self.characters.new(name=name, model_name="c1000", **kwargs)
    # endregion
