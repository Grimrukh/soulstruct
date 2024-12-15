from __future__ import annotations

__all__ = ["MSB", "MSBSubtypeInfo", "MSBSupertype"]

import typing as tp
from enum import StrEnum
from dataclasses import dataclass, field

from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBEntryList, MSBEntry, BaseMSBSubtype
from soulstruct.base.maps.msb.utils import MSBSubtypeInfo
from soulstruct.utilities.binary import *
from soulstruct.utilities.misc import IDList

from .constants import get_map
from .enums import *
from .models import *
from .events import *
from .regions import *
from .parts import *


class MSBEntrySuperlistHeader(BinaryStruct):
    _version: int = binary(asserted=3, init=False)
    entry_offset_count: int
    name_offset: long


MSB_ENTRY_SUBTYPES = {
    MSBSupertype.MODELS: {
        MSBModelSubtype.MapPieceModel: MSBSubtypeInfo(MSBMapPieceModel, "map_piece_models"),
        MSBModelSubtype.ObjectModel: MSBSubtypeInfo(MSBObjectModel, "object_models"),
        MSBModelSubtype.CharacterModel: MSBSubtypeInfo(MSBCharacterModel, "character_models"),
        MSBModelSubtype.ItemModel: MSBSubtypeInfo(MSBItemModel, "item_models"),
        MSBModelSubtype.PlayerModel: MSBSubtypeInfo(MSBPlayerModel, "player_models"),
        MSBModelSubtype.CollisionModel: MSBSubtypeInfo(MSBCollisionModel, "collision_models"),
        MSBModelSubtype.NavmeshModel: MSBSubtypeInfo(MSBNavmeshModel, "navmesh_models"),
        MSBModelSubtype.OtherModel: MSBSubtypeInfo(MSBOtherModel, "other_models"),
    },
    MSBSupertype.EVENTS: {
        # 0 (Light) unused.
        MSBEventSubtype.Sound: MSBSubtypeInfo(MSBSoundEvent, "sounds"),
        MSBEventSubtype.VFX: MSBSubtypeInfo(MSBVFXEvent, "vfx"),
        # 3 (Wind) unused.
        MSBEventSubtype.Treasure: MSBSubtypeInfo(MSBTreasureEvent, "treasures"),
        MSBEventSubtype.Spawner: MSBSubtypeInfo(MSBSpawnerEvent, "spawners"),
        MSBEventSubtype.Message: MSBSubtypeInfo(MSBMessageEvent, "messages"),
        MSBEventSubtype.ObjAct: MSBSubtypeInfo(MSBObjActEvent, "obj_acts"),
        MSBEventSubtype.SpawnPoint: MSBSubtypeInfo(MSBSpawnPointEvent, "spawn_points"),
        MSBEventSubtype.MapOffset: MSBSubtypeInfo(MSBMapOffsetEvent, "map_offsets"),
        MSBEventSubtype.Navigation: MSBSubtypeInfo(MSBNavigationEvent, "navigation"),
        MSBEventSubtype.Environment: MSBSubtypeInfo(MSBEnvironmentEvent, "environments"),
        # 12 (NPC Invasions) unused.
        MSBEventSubtype.WindVFX: MSBSubtypeInfo(MSBWindVFXEvent, "wind_vfx"),
        MSBEventSubtype.PatrolRoute: MSBSubtypeInfo(MSBPatrolRouteEvent, "patrol_routes"),
        MSBEventSubtype.DarkLock: MSBSubtypeInfo(MSBDarkLockEvent, "dark_locks"),
        MSBEventSubtype.Platoon: MSBSubtypeInfo(MSBPlatoonEvent, "platoons"),
        MSBEventSubtype.MultiSummon: MSBSubtypeInfo(MSBMultiSummonEvent, "multi_summons"),
        MSBEventSubtype.OtherEvent: MSBSubtypeInfo(MSBOtherEvent, "other_events"),
    },
    MSBSupertype.REGIONS: {
        MSBRegionSubtype.All: MSBSubtypeInfo(MSBRegion, "regions"),
    },
    MSBSupertype.PARTS: {
        MSBPartSubtype.MapPiece: MSBSubtypeInfo(MSBMapPiece, "map_pieces"),
        MSBPartSubtype.Object: MSBSubtypeInfo(MSBObject, "objects"),
        MSBPartSubtype.Character: MSBSubtypeInfo(MSBCharacter, "characters"),
        # 3 unused.
        MSBPartSubtype.PlayerStart: MSBSubtypeInfo(MSBPlayerStart, "player_starts"),
        MSBPartSubtype.Collision: MSBSubtypeInfo(MSBCollision, "collisions"),
        # 6 unused.
        # 7 unused.
        MSBPartSubtype.Navmesh: MSBSubtypeInfo(MSBNavmesh, "navmeshes"),
        MSBPartSubtype.DummyObject: MSBSubtypeInfo(MSBDummyObject, "dummy_objects"),
        MSBPartSubtype.DummyCharacter: MSBSubtypeInfo(MSBDummyCharacter, "dummy_characters"),
        MSBPartSubtype.ConnectCollision: MSBSubtypeInfo(MSBConnectCollision, "connect_collisions"),
        MSBPartSubtype.OtherPart: MSBSubtypeInfo(MSBOtherPart, "other_parts"),
    },
}  # type: dict[str, dict[BaseMSBSubtype, MSBSubtypeInfo]]


def empty(subtype_enum: BaseMSBSubtype) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(subtype_enum.get_supertype_name())  # for validation
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum]
    return lambda: MSBEntryList((), supertype=supertype, entry_class=subtype_info.entry_class)


class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_SUPERTYPE_ENUM: tp.ClassVar[type[StrEnum]] = MSBSupertype
    MSB_ENTRY_SUPERTYPES: tp.ClassVar[dict[str, type[MSBEntry]]] = {
        MSBSupertype.MODELS: MSBModel,
        MSBSupertype.EVENTS: MSBEvent,
        MSBSupertype.REGIONS: MSBRegion,
        MSBSupertype.PARTS: MSBPart,
    }
    MSB_SUPERTYPE_SUBTYPE_ENUMS: tp.ClassVar[dict[str, type[BaseMSBSubtype]]] = {
        MSBSupertype.MODELS: MSBModelSubtype,
        MSBSupertype.EVENTS: MSBEventSubtype,
        MSBSupertype.REGIONS: MSBRegionSubtype,
        MSBSupertype.PARTS: MSBPartSubtype,
    }
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[BaseMSBSubtype, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
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

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty(MSBModelSubtype.MapPieceModel))
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=empty(MSBModelSubtype.ObjectModel))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty(MSBModelSubtype.CharacterModel))
    item_models: MSBEntryList[MSBItemModel] = field(default_factory=empty(MSBModelSubtype.ItemModel))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty(MSBModelSubtype.PlayerModel))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty(MSBModelSubtype.CollisionModel))
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=empty(MSBModelSubtype.NavmeshModel))
    other_models: MSBEntryList[MSBOtherModel] = field(default_factory=empty(MSBModelSubtype.OtherModel))

    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=empty(MSBEventSubtype.Sound))
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=empty(MSBEventSubtype.VFX))
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty(MSBEventSubtype.Treasure))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty(MSBEventSubtype.Spawner))
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=empty(MSBEventSubtype.Message))
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=empty(MSBEventSubtype.ObjAct))
    spawn_points: MSBEntryList[MSBSpawnPointEvent] = field(default_factory=empty(MSBEventSubtype.SpawnPoint))
    map_offsets: MSBEntryList[MSBMapOffsetEvent] = field(default_factory=empty(MSBEventSubtype.MapOffset))
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=empty(MSBEventSubtype.Navigation))
    environments: MSBEntryList[MSBEnvironmentEvent] = field(default_factory=empty(MSBEventSubtype.Environment))
    wind_vfx: MSBEntryList[MSBWindVFXEvent] = field(default_factory=empty(MSBEventSubtype.WindVFX))
    patrol_routes: MSBEntryList[MSBPatrolRouteEvent] = field(default_factory=empty(MSBEventSubtype.PatrolRoute))
    dark_locks: MSBEntryList[MSBDarkLockEvent] = field(default_factory=empty(MSBEventSubtype.DarkLock))
    platoons: MSBEntryList[MSBPlatoonEvent] = field(default_factory=empty(MSBEventSubtype.Platoon))
    multi_summons: MSBEntryList[MSBMultiSummonEvent] = field(default_factory=empty(MSBEventSubtype.MultiSummon))
    other_events: MSBEntryList[MSBOtherEvent] = field(default_factory=empty(MSBEventSubtype.OtherEvent))

    regions: MSBEntryList[MSBRegion] = field(default_factory=empty(MSBRegionSubtype.All))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty(MSBPartSubtype.MapPiece))
    objects: MSBEntryList[MSBObject] = field(default_factory=empty(MSBPartSubtype.Object))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty(MSBPartSubtype.Character))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty(MSBPartSubtype.PlayerStart))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty(MSBPartSubtype.Collision))
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=empty(MSBPartSubtype.Navmesh))
    dummy_objects: MSBEntryList[MSBDummyObject] = field(default_factory=empty(MSBPartSubtype.DummyObject))
    dummy_characters: MSBEntryList[MSBDummyCharacter] = field(default_factory=empty(MSBPartSubtype.DummyCharacter))
    connect_collisions: MSBEntryList[MSBConnectCollision] = field(
        default_factory=empty(MSBPartSubtype.ConnectCollision))
    other_parts: MSBEntryList[MSBOtherPart] = field(default_factory=empty(MSBPartSubtype.OtherPart))

    @classmethod
    def _dereference_msb_entries(cls, entry_lists: dict[str, IDList[MSBEntry]]):
        # Resolve entry indices to actual object references.
        for event in entry_lists[MSBSupertype.EVENTS]:
            event: MSBEvent
            event.indices_to_objects(entry_lists)

        for region in entry_lists[MSBSupertype.REGIONS]:
            region: MSBRegion
            region.indices_to_objects(entry_lists)

        for part in entry_lists[MSBSupertype.PARTS]:
            part: MSBPart
            part.indices_to_objects(entry_lists)

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
