from __future__ import annotations

__all__ = ["MSB"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBSubtypeInfo, MSBEntryList
from soulstruct.utilities.binary import *

from .constants import get_map
from .enums import MSBModelSubtype, MSBEventSubtype, MSBRegionSubtype, MSBPartSubtype
from .models import *
from .events import *
from .regions import *
from .parts import *


@dataclass(slots=True)
class MSBEntrySuperlistHeader(NewBinaryStruct):
    _version: int = field(init=False, **Binary(asserted=3))
    entry_offset_count: int
    name_offset: long


class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[tp.Type[NewBinaryStruct]] = MSBEntrySuperlistHeader
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[int, MSBSubtypeInfo]]] = {
        "MODEL_PARAM_ST": {
            0: MSBSubtypeInfo(MSBModelSubtype.MapPiece, MSBMapPieceModel, "map_piece_models"),
            1: MSBSubtypeInfo(MSBModelSubtype.Object, MSBObjectModel, "object_models"),
            2: MSBSubtypeInfo(MSBModelSubtype.Character, MSBCharacterModel, "character_models"),
            3: MSBSubtypeInfo(MSBModelSubtype.Item, MSBItemModel, "item_models"),
            4: MSBSubtypeInfo(MSBModelSubtype.Player, MSBPlayerModel, "player_models"),
            5: MSBSubtypeInfo(MSBModelSubtype.Collision, MSBCollisionModel, "collision_models"),
            6: MSBSubtypeInfo(MSBModelSubtype.Navmesh, MSBNavmeshModel, "navmesh_models"),
            -1: MSBSubtypeInfo(MSBModelSubtype.Other, MSBOtherModel, "other_models"),
        },
        "EVENT_PARAM_ST": {
            # 0 (Light) unused.
            1: MSBSubtypeInfo(MSBEventSubtype.Sound, MSBSoundEvent, "sounds"),
            2: MSBSubtypeInfo(MSBEventSubtype.VFX, MSBVFXEvent, "vfx"),
            # 3 (Wind) unused.
            4: MSBSubtypeInfo(MSBEventSubtype.Treasure, MSBTreasureEvent, "treasures"),
            5: MSBSubtypeInfo(MSBEventSubtype.Spawner, MSBSpawnerEvent, "spawners"),
            6: MSBSubtypeInfo(MSBEventSubtype.Message, MSBMessageEvent, "messages"),
            7: MSBSubtypeInfo(MSBEventSubtype.ObjAct, MSBObjActEvent, "obj_acts"),
            8: MSBSubtypeInfo(MSBEventSubtype.SpawnPoint, MSBSpawnPointEvent, "spawn_points"),
            9: MSBSubtypeInfo(MSBEventSubtype.MapOffset, MSBMapOffsetEvent, "map_offsets"),
            10: MSBSubtypeInfo(MSBEventSubtype.Navigation, MSBNavigationEvent, "navigation"),
            11: MSBSubtypeInfo(MSBEventSubtype.Environment, MSBEnvironmentEvent, "environments"),
            # 12 (NPC Invasions) unused.
            13: MSBSubtypeInfo(MSBEventSubtype.WindVFX, MSBWindVFXEvent, "wind_vfx"),
            14: MSBSubtypeInfo(MSBEventSubtype.PatrolRoute, MSBPatrolRouteEvent, "patrol_routes"),
            15: MSBSubtypeInfo(MSBEventSubtype.DarkLock, MSBDarkLockEvent, "dark_locks"),
            16: MSBSubtypeInfo(MSBEventSubtype.Platoon, MSBPlatoonEvent, "platoons"),
            17: MSBSubtypeInfo(MSBEventSubtype.MultiSummon, MSBMultiSummonEvent, "multi_summons"),
            -1: MSBSubtypeInfo(MSBEventSubtype.Other, MSBOtherEvent, "other_events"),
        },
        "POINT_PARAM_ST": {
            0: MSBSubtypeInfo(MSBRegionSubtype.Point, MSBRegionPoint, "points"),
            1: MSBSubtypeInfo(MSBRegionSubtype.Circle, MSBRegionCircle, "circles"),
            2: MSBSubtypeInfo(MSBRegionSubtype.Sphere, MSBRegionSphere, "spheres"),
            3: MSBSubtypeInfo(MSBRegionSubtype.Cylinder, MSBRegionCylinder, "cylinders"),
            4: MSBSubtypeInfo(MSBRegionSubtype.Rect, MSBRegionRect, "rects"),
            5: MSBSubtypeInfo(MSBRegionSubtype.Box, MSBRegionBox, "boxes"),
        },
        "PARTS_PARAM_ST": {
            0: MSBSubtypeInfo(MSBPartSubtype.MapPiece, MSBMapPiece, "map_pieces"),
            1: MSBSubtypeInfo(MSBPartSubtype.Object, MSBObject, "objects"),
            2: MSBSubtypeInfo(MSBPartSubtype.Character, MSBCharacter, "characters"),
            # 3 unused.
            4: MSBSubtypeInfo(MSBPartSubtype.PlayerStart, MSBPlayerStart, "player_starts"),
            5: MSBSubtypeInfo(MSBPartSubtype.Collision, MSBCollision, "collisions"),
            # 6 unused.
            # 7 unused.
            8: MSBSubtypeInfo(MSBPartSubtype.Navmesh, MSBNavmesh, "navmeshes"),
            9: MSBSubtypeInfo(MSBPartSubtype.UnusedObject, MSBUnusedObject, "unused_objects"),
            10: MSBSubtypeInfo(MSBPartSubtype.UnusedCharacter, MSBUnusedCharacter, "unused_characters"),
            11: MSBSubtypeInfo(MSBPartSubtype.MapConnection, MSBMapConnection, "map_connections"),
            -1: MSBSubtypeInfo(MSBPartSubtype.Other, MSBOtherPart, "other_parts"),
        },
    }
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

    # TODO: default factory methods need supertype name, subtype enum, subtype class
    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=MSBEntryList)
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=MSBEntryList)
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=MSBEntryList)
    item_models: MSBEntryList[MSBItemModel] = field(default_factory=MSBEntryList)
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=MSBEntryList)
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=MSBEntryList)
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=MSBEntryList)
    other_models: MSBEntryList[MSBOtherModel] = field(default_factory=MSBEntryList)

    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=MSBEntryList)
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=MSBEntryList)
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=MSBEntryList)
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=MSBEntryList)
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=MSBEntryList)
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=MSBEntryList)
    spawn_points: MSBEntryList[MSBSpawnPointEvent] = field(default_factory=MSBEntryList)
    map_offsets: MSBEntryList[MSBMapOffsetEvent] = field(default_factory=MSBEntryList)
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=MSBEntryList)
    environments: MSBEntryList[MSBEnvironmentEvent] = field(default_factory=MSBEntryList)
    wind_vfx: MSBEntryList[MSBWindVFXEvent] = field(default_factory=MSBEntryList)
    patrol_routes: MSBEntryList[MSBPatrolRouteEvent] = field(default_factory=MSBEntryList)
    dark_locks: MSBEntryList[MSBDarkLockEvent] = field(default_factory=MSBEntryList)
    platoons: MSBEntryList[MSBPlatoonEvent] = field(default_factory=MSBEntryList)
    multi_summons: MSBEntryList[MSBMultiSummonEvent] = field(default_factory=MSBEntryList)
    other_events: MSBEntryList[MSBOtherEvent] = field(default_factory=MSBEntryList)

    points: MSBEntryList[MSBRegionPoint] = field(default_factory=MSBEntryList)
    circles: MSBEntryList[MSBRegionCircle] = field(default_factory=MSBEntryList)
    spheres: MSBEntryList[MSBRegionSphere] = field(default_factory=MSBEntryList)
    cylinders: MSBEntryList[MSBRegionCylinder] = field(default_factory=MSBEntryList)
    rects: MSBEntryList[MSBRegionRect] = field(default_factory=MSBEntryList)
    boxes: MSBEntryList[MSBRegionBox] = field(default_factory=MSBEntryList)

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=MSBEntryList)
    objects: MSBEntryList[MSBObject] = field(default_factory=MSBEntryList)
    characters: MSBEntryList[MSBCharacter] = field(default_factory=MSBEntryList)
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=MSBEntryList)
    collisions: MSBEntryList[MSBCollision] = field(default_factory=MSBEntryList)
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=MSBEntryList)
    unused_objects: MSBEntryList[MSBUnusedObject] = field(default_factory=MSBEntryList)
    unused_characters: MSBEntryList[MSBUnusedCharacter] = field(default_factory=MSBEntryList)
    map_connections: MSBEntryList[MSBMapConnection] = field(default_factory=MSBEntryList)
    other_parts: MSBEntryList[MSBOtherPart] = field(default_factory=MSBEntryList)

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
        new_collision = self.collisions.duplicate(
            copy_entry=collision, at_next_index=at_next_index, **kwargs,
        )
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
