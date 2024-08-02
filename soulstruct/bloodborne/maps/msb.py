from __future__ import annotations

__all__ = ["MSB", "MSBSubtypeInfo", "MSBSupertype"]

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
    MSBSupertype.MODELS: {
        "MapPieceModel": MSBSubtypeInfo(MSBModelSubtype.MapPieceModel, MSBMapPieceModel, "map_piece_models"),
        "ObjectModel": MSBSubtypeInfo(MSBModelSubtype.ObjectModel, MSBObjectModel, "object_models"),
        "CharacterModel": MSBSubtypeInfo(MSBModelSubtype.CharacterModel, MSBCharacterModel, "character_models"),
        "ItemModel": MSBSubtypeInfo(MSBModelSubtype.ItemModel, MSBItemModel, "item_models"),
        "PlayerModel": MSBSubtypeInfo(MSBModelSubtype.PlayerModel, MSBPlayerModel, "player_models"),
        "CollisionModel": MSBSubtypeInfo(MSBModelSubtype.CollisionModel, MSBCollisionModel, "collision_models"),
        "NavmeshModel": MSBSubtypeInfo(MSBModelSubtype.NavmeshModel, MSBNavmeshModel, "navmesh_models"),
        "OtherModel": MSBSubtypeInfo(MSBModelSubtype.OtherModel, MSBOtherModel, "other_models"),
    },
    MSBSupertype.EVENTS: {
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
    MSBSupertype.REGIONS: {
        "All": MSBSubtypeInfo(MSBRegionSubtype.All, MSBRegion, "regions"),
    },
    MSBSupertype.PARTS: {
        "MapPiece": MSBSubtypeInfo(MSBPartSubtype.MapPiece, MSBMapPiece, "map_pieces"),
        "Object": MSBSubtypeInfo(MSBPartSubtype.Object, MSBObject, "objects"),
        "Character": MSBSubtypeInfo(MSBPartSubtype.Character, MSBCharacter, "characters"),
        # 3 unused.
        "PlayerStart": MSBSubtypeInfo(MSBPartSubtype.PlayerStart, MSBPlayerStart, "player_starts"),
        "Collision": MSBSubtypeInfo(MSBPartSubtype.Collision, MSBCollision, "collisions"),
        # 6 unused.
        # 7 unused.
        "Navmesh": MSBSubtypeInfo(MSBPartSubtype.Navmesh, MSBNavmesh, "navmeshes"),
        "DummyObject": MSBSubtypeInfo(MSBPartSubtype.DummyObject, MSBDummyObject, "unused_objects"),
        "DummyCharacter": MSBSubtypeInfo(MSBPartSubtype.DummyCharacter, MSBDummyCharacter, "unused_characters"),
        "ConnectCollision": MSBSubtypeInfo(MSBPartSubtype.ConnectCollision, MSBConnectCollision, "connect_collisions"),
        "OtherPart": MSBSubtypeInfo(MSBPartSubtype.OtherPart, MSBOtherPart, "other_parts"),
    },
}


def empty(supertype_prefix: str, subtype_enum_name: str) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(f"{supertype_prefix}_PARAM_ST")
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum_name]
    return lambda: MSBEntryList((), supertype=supertype, subtype_info=subtype_info)


@dataclass(slots=True, kw_only=True)
class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[str, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        MSBSupertype.MODELS: 8,
        MSBSupertype.EVENTS: 12,
        MSBSupertype.REGIONS: 8,  # always 0
        MSBSupertype.PARTS: 20,
    }
    ENTITY_GAME_TYPES: tp.ClassVar[dict[str, MapEntity]] = {}  # TODO for Bloodborne
    
    HAS_HEADER: tp.ClassVar[bool] = True
    LONG_VARINTS: tp.ClassVar[bool] = True
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty("MODEL", "MapPieceModel"))
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=empty("MODEL", "ObjectModel"))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty("MODEL", "CharacterModel"))
    item_models: MSBEntryList[MSBItemModel] = field(default_factory=empty("MODEL", "ItemModel"))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty("MODEL", "PlayerModel"))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty("MODEL", "CollisionModel"))
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=empty("MODEL", "NavmeshModel"))
    other_models: MSBEntryList[MSBOtherModel] = field(default_factory=empty("MODEL", "OtherModel"))

    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=empty("EVENT", "Sound"))
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=empty("EVENT", "VFX"))
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty("EVENT", "Treasure"))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty("EVENT", "Spawner"))
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=empty("EVENT", "Message"))
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=empty("EVENT", "ObjAct"))
    spawn_points: MSBEntryList[MSBSpawnPointEvent] = field(default_factory=empty("EVENT", "SpawnPoint"))
    map_offsets: MSBEntryList[MSBMapOffsetEvent] = field(default_factory=empty("EVENT", "MapOffset"))
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=empty("EVENT", "Navigation"))
    environments: MSBEntryList[MSBEnvironmentEvent] = field(default_factory=empty("EVENT", "Environment"))
    wind_vfx: MSBEntryList[MSBWindVFXEvent] = field(default_factory=empty("EVENT", "WindVFX"))
    patrol_routes: MSBEntryList[MSBPatrolRouteEvent] = field(default_factory=empty("EVENT", "PatrolRoute"))
    dark_locks: MSBEntryList[MSBDarkLockEvent] = field(default_factory=empty("EVENT", "DarkLock"))
    platoons: MSBEntryList[MSBPlatoonEvent] = field(default_factory=empty("EVENT", "Platoon"))
    multi_summons: MSBEntryList[MSBMultiSummonEvent] = field(default_factory=empty("EVENT", "MultiSummon"))
    other_events: MSBEntryList[MSBOtherEvent] = field(default_factory=empty("EVENT", "OtherEvent"))

    regions: MSBEntryList[MSBRegion] = field(default_factory=empty("POINT", "All"))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty("PARTS", "MapPiece"))
    objects: MSBEntryList[MSBObject] = field(default_factory=empty("PARTS", "Object"))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty("PARTS", "Character"))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty("PARTS", "PlayerStart"))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty("PARTS", "Collision"))
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=empty("PARTS", "Navmesh"))
    unused_objects: MSBEntryList[MSBDummyObject] = field(default_factory=empty("PARTS", "DummyObject"))
    unused_characters: MSBEntryList[MSBDummyCharacter] = field(default_factory=empty("PARTS", "DummyCharacter"))
    connect_collisions: MSBEntryList[MSBConnectCollision] = field(default_factory=empty("PARTS", "ConnectCollision"))
    other_parts: MSBEntryList[MSBOtherPart] = field(default_factory=empty("PARTS", "OtherPart"))

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

    def create_connect_collision_from_collision(
        self, collision: MSBCollision | str, connected_map, name=None, draw_groups=None, display_groups=None
    ):
        """Creates a new `ConnectCollision` that references and copies the transform of the given `collision`.

        The `name` and `map_id` of the new `ConnectCollision` must be given. You can also specify its `draw_groups` and
        `display_groups`. Otherwise, it will leave them as the extensive default values: [0, ..., 127].
        """
        if not isinstance(collision, MSBCollision):
            collision = self.collisions.find_entry_name(collision)
        if name is None:
            game_map = get_map(connected_map)
            name = collision.name + f"_[{game_map.area_id:02d}_{game_map.block_id:02d}]"
        if name in self.connect_collisions.get_entry_names():
            raise ValueError(f"{repr(name)} is already the name of an existing `MSBConnectCollision`.")
        connect_collision = self.connect_collisions.new(
            name=name,
            connected_map=connected_map,
            collision=collision,
            translate=collision.translate.copy(),
            rotate=collision.rotate.copy(),
            scale=collision.scale.copy(),  # for completion's sake
            model=collision.model,
        )
        if draw_groups is not None:  # otherwise keep same draw groups
            connect_collision.draw_groups = draw_groups
        if display_groups is not None:  # otherwise keep same display groups
            connect_collision.display_groups = display_groups
        return connect_collision

    def new_c1000(self, name: str, **kwargs) -> MSBCharacter:
        """Useful to create basic c1000 instances as debug warp points."""
        return self.characters.new(name=name, model_name="c1000", **kwargs)
    # endregion
