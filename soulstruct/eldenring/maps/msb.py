from __future__ import annotations

__all__ = ["MSB", "MSBSubtypeInfo", "MSBSupertype", "BitSet256", "BitSet1024"]

import typing as tp
from dataclasses import field
from enum import Enum, StrEnum

from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBEntryList, MSBEntry
from soulstruct.base.maps.msb.enums import BaseMSBSubtype
from soulstruct.base.maps.msb.utils import MSBSubtypeInfo, BitSet256, BitSet1024
from soulstruct.utilities.binary import *
from soulstruct.utilities.misc import IDList

from .constants import get_map
from .enums import *
from .models import *
from .events import *
from .regions import *
from .routes import *
from .parts import *


class MSBEntrySuperlistHeader(BinaryStruct):
    _version: int = binary(asserted=73, init=False)
    entry_offset_count: int
    name_offset: long


MSB_ENTRY_SUBTYPES = {
    MSBSupertype.MODELS: {
        MSBModelSubtype.MapPieceModel: MSBSubtypeInfo(MSBMapPieceModel, "map_piece_models"),
        MSBModelSubtype.AssetModel: MSBSubtypeInfo(MSBAssetModel, "asset_models"),
        MSBModelSubtype.CharacterModel: MSBSubtypeInfo(MSBCharacterModel, "character_models"),
        MSBModelSubtype.PlayerModel: MSBSubtypeInfo(MSBPlayerModel, "player_models"),
        MSBModelSubtype.CollisionModel: MSBSubtypeInfo(MSBCollisionModel, "collision_models"),
    },
    MSBSupertype.EVENTS: {
        MSBEventSubtype.Treasure: MSBSubtypeInfo(MSBTreasureEvent, "treasures"),
        MSBEventSubtype.Spawner: MSBSubtypeInfo(MSBSpawnerEvent, "spawners"),
        MSBEventSubtype.ObjAct: MSBSubtypeInfo(MSBObjActEvent, "obj_acts"),
        MSBEventSubtype.Navigation: MSBSubtypeInfo(MSBNavigationEvent, "navigation"),
        MSBEventSubtype.NPCInvasion: MSBSubtypeInfo(MSBNPCInvasionEvent, "npc_invasions"),
        MSBEventSubtype.Platoon: MSBSubtypeInfo(MSBPlatoonEvent, "platoons"),
        MSBEventSubtype.PatrolRouteEvent: MSBSubtypeInfo(MSBPatrolRouteEvent, "patrol_route_events"),
        MSBEventSubtype.Mount: MSBSubtypeInfo(MSBMountEvent, "mounts"),
        MSBEventSubtype.SignPool: MSBSubtypeInfo(MSBSignPoolEvent, "sign_pools"),
        MSBEventSubtype.RetryPoint: MSBSubtypeInfo(MSBRetryPointEvent, "retry_points"),
        MSBEventSubtype.OtherEvent: MSBSubtypeInfo(MSBOtherEvent, "other_events"),
    },
    MSBSupertype.REGIONS: {
        MSBRegionSubtype.InvasionPoint: MSBSubtypeInfo(MSBInvasionPointRegion, "invasion_points"),
        MSBRegionSubtype.EnvironmentMapPoint: MSBSubtypeInfo(MSBEnvironmentMapPointRegion, "environment_map_points"),
        MSBRegionSubtype.Sound: MSBSubtypeInfo(MSBSoundRegion, "sounds"),
        MSBRegionSubtype.VFX: MSBSubtypeInfo(MSBVFXRegion, "vfx"),
        MSBRegionSubtype.WindVFX: MSBSubtypeInfo(MSBWindVFXRegion, "wind_vfx"),
        MSBRegionSubtype.SpawnPoint: MSBSubtypeInfo(MSBSpawnPointRegion, "spawn_points"),
        MSBRegionSubtype.Message: MSBSubtypeInfo(MSBMessageRegion, "messages"),
        MSBRegionSubtype.EnvironmentMapEffectBox: MSBSubtypeInfo(
            MSBEnvironmentMapEffectBoxRegion, "environment_map_effect_boxes"),
        MSBRegionSubtype.WindArea: MSBSubtypeInfo(MSBWindAreaRegion, "wind_areas"),
        MSBRegionSubtype.Connection: MSBSubtypeInfo(MSBConnectionRegion, "connections"),
        MSBRegionSubtype.PatrolRoute22: MSBSubtypeInfo(MSBPatrolRoute22Region, "patrol_route22s"),
        MSBRegionSubtype.BuddySummonPoint: MSBSubtypeInfo(MSBBuddySummonPointRegion, "buddy_summon_points"),
        MSBRegionSubtype.MufflingBox: MSBSubtypeInfo(MSBMufflingBoxRegion, "muffling_boxes"),
        MSBRegionSubtype.MufflingPortal: MSBSubtypeInfo(MSBMufflingPortalRegion, "muffling_portals"),
        MSBRegionSubtype.OtherSound: MSBSubtypeInfo(MSBOtherSoundRegion, "other_sounds"),
        MSBRegionSubtype.MufflingPlane: MSBSubtypeInfo(MSBMufflingPlaneRegion, "muffling_planes"),
        MSBRegionSubtype.PatrolRoute: MSBSubtypeInfo(MSBPatrolRouteRegion, "patrol_routes"),
        MSBRegionSubtype.MapPoint: MSBSubtypeInfo(MSBMapPointRegion, "map_points"),
        MSBRegionSubtype.WeatherOverride: MSBSubtypeInfo(MSBWeatherOverrideRegion, "weather_overrides"),
        MSBRegionSubtype.AutoDrawGroupPoint: MSBSubtypeInfo(MSBAutoDrawGroupPointRegion, "auto_draw_group_points"),
        MSBRegionSubtype.GroupDefeatReward: MSBSubtypeInfo(MSBGroupDefeatRewardRegion, "group_defeat_rewards"),
        MSBRegionSubtype.MapPointDiscoveryOverride: MSBSubtypeInfo(
            MSBMapPointDiscoveryOverrideRegion, "map_point_discovery_overrides"),
        MSBRegionSubtype.MapPointParticipationOverride: MSBSubtypeInfo(
            MSBMapPointParticipationOverrideRegion, "map_point_participation_overrides"),
        MSBRegionSubtype.Hitset: MSBSubtypeInfo(MSBHitsetRegion, "hitsets"),
        MSBRegionSubtype.FastTravelRestriction: MSBSubtypeInfo(
            MSBFastTravelRestrictionRegion, "fast_travel_restrictions"),
        MSBRegionSubtype.WeatherCreateAssetPoint: MSBSubtypeInfo(
            MSBWeatherCreateAssetPointRegion, "weather_create_asset_points"),
        MSBRegionSubtype.PlayArea: MSBSubtypeInfo(MSBPlayAreaRegion, "play_areas"),
        MSBRegionSubtype.EnvironmentMapOutput: MSBSubtypeInfo(MSBEnvironmentMapOutputRegion, "environment_map_outputs"),
        MSBRegionSubtype.MountJump: MSBSubtypeInfo(MSBMountJumpRegion, "mount_jumps"),
        MSBRegionSubtype.Dummy: MSBSubtypeInfo(MSBDummyRegion, "dummies"),
        MSBRegionSubtype.FallPreventionRemoval: MSBSubtypeInfo(
            MSBFallPreventionRemovalRegion, "fall_prevention_removals"),
        MSBRegionSubtype.NavmeshCutting: MSBSubtypeInfo(MSBNavmeshCuttingRegion, "navmesh_cuttings"),
        MSBRegionSubtype.MapNameOverride: MSBSubtypeInfo(MSBMapNameOverrideRegion, "map_name_overrides"),
        MSBRegionSubtype.MountJumpFall: MSBSubtypeInfo(MSBMountJumpFallRegion, "mount_jump_falls"),
        MSBRegionSubtype.HorseRideOverride: MSBSubtypeInfo(MSBHorseRideOverrideRegion, "horse_ride_overrides"),
        MSBRegionSubtype.OtherRegion: MSBSubtypeInfo(MSBOtherRegion, "other_regions"),
    },
    MSBSupertype.ROUTES: {
        MSBRouteSubtype.MufflingPortalLink: MSBSubtypeInfo(MSBMufflingPortalLink, "muffling_portal_links"),
        MSBRouteSubtype.MufflingBoxLink: MSBSubtypeInfo(MSBMufflingBoxLink, "muffling_box_links"),
        MSBRouteSubtype.OtherRoute: MSBSubtypeInfo(MSBOtherRoute, "other_routes"),
    },
    MSBSupertype.LAYERS: {},  # empty supertype
    MSBSupertype.PARTS: {
        MSBPartSubtype.MapPiece: MSBSubtypeInfo(MSBMapPiece, "map_pieces"),
        MSBPartSubtype.Asset: MSBSubtypeInfo(MSBAsset, "assets"),
        MSBPartSubtype.Character: MSBSubtypeInfo(MSBCharacter, "characters"),
        MSBPartSubtype.PlayerStart: MSBSubtypeInfo(MSBPlayerStart, "player_starts"),
        MSBPartSubtype.Collision: MSBSubtypeInfo(MSBCollision, "collisions"),
        MSBPartSubtype.DummyAsset: MSBSubtypeInfo(MSBDummyAsset, "dummy_assets"),
        MSBPartSubtype.DummyCharacter: MSBSubtypeInfo(MSBDummyCharacter, "dummy_characters"),
        MSBPartSubtype.ConnectCollision: MSBSubtypeInfo(MSBConnectCollision, "connect_collisions"),
    },
}  # type: dict[str, dict[BaseMSBSubtype, MSBSubtypeInfo]]


def empty(subtype_enum: BaseMSBSubtype) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(subtype_enum.get_supertype_name())  # for validation
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum]
    return lambda: MSBEntryList((), supertype=supertype, entry_class=subtype_info.entry_class)


class MSB(_BaseMSB[MSBModel, MSBEvent, MSBRegion, MSBPart]):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_SUPERTYPE_ENUM: tp.ClassVar[type[StrEnum]] = MSBSupertype
    MSB_ENTRY_SUPERTYPES: tp.ClassVar[dict[str, type[MSBEntry]]] = {
        MSBSupertype.MODELS: MSBModel,
        MSBSupertype.EVENTS: MSBEvent,
        MSBSupertype.REGIONS: MSBRegion,
        MSBSupertype.ROUTES: MSBRoute,
        MSBSupertype.LAYERS: None,  # empty supertype (no known subtypes)
        MSBSupertype.PARTS: MSBPart,
    }
    MSB_SUPERTYPE_SUBTYPE_ENUMS: tp.ClassVar[dict[str, type[BaseMSBSubtype]]] = {
        MSBSupertype.MODELS: MSBModelSubtype,
        MSBSupertype.EVENTS: MSBEventSubtype,
        MSBSupertype.REGIONS: MSBRegionSubtype,
        MSBSupertype.ROUTES: MSBRouteSubtype,
        MSBSupertype.LAYERS: None,  # empty supertype (no known subtypes)
        MSBSupertype.PARTS: MSBPartSubtype,
    }
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[BaseMSBSubtype, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        "MODEL_PARAM_ST": 8,
        "EVENT_PARAM_ST": 12,
        "POINT_PARAM_ST": 8,
        "ROUTE_PARAM_ST": 16,
        "LAYER_PARAM_ST": -1,  # empty supertype (no known subtypes)
        "PARTS_PARAM_ST": 12,
    }
    MODEL_CLASS: tp.ClassVar[type[MSBModel]] = MSBModel
    EVENT_CLASS: tp.ClassVar[type[MSBEvent]] = MSBEvent
    REGION_CLASS: tp.ClassVar[type[MSBRegion]] = MSBRegion
    PART_CLASS: tp.ClassVar[type[MSBPart]] = MSBPart
    ROUTE_CLASS: tp.ClassVar[type[MSBRoute]] = MSBRoute
    ENTITY_GAME_TYPES: tp.ClassVar[dict[str, MapEntity]] = {}  # TODO for Elden Ring

    HAS_HEADER: tp.ClassVar[bool] = True
    LONG_VARINTS: tp.ClassVar[bool] = True
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty(MSBModelSubtype.MapPieceModel))
    asset_models: MSBEntryList[MSBAssetModel] = field(default_factory=empty(MSBModelSubtype.AssetModel))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty(MSBModelSubtype.CharacterModel))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty(MSBModelSubtype.PlayerModel))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty(MSBModelSubtype.CollisionModel))

    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty(MSBEventSubtype.Treasure))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty(MSBEventSubtype.Spawner))
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=empty(MSBEventSubtype.ObjAct))
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=empty(MSBEventSubtype.Navigation))
    npc_invasions: MSBEntryList[MSBNPCInvasionEvent] = field(default_factory=empty(MSBEventSubtype.NPCInvasion))
    platoons: MSBEntryList[MSBPlatoonEvent] = field(default_factory=empty(MSBEventSubtype.Platoon))
    # TODO: rename to 'patrol_routes' and change region name to 'patrol_route_points'
    patrol_route_events: MSBEntryList[MSBPatrolRouteEvent] = field(
        default_factory=empty(MSBEventSubtype.PatrolRouteEvent))
    mounts: MSBEntryList[MSBMountEvent] = field(default_factory=empty(MSBEventSubtype.Mount))
    sign_pools: MSBEntryList[MSBSignPoolEvent] = field(default_factory=empty(MSBEventSubtype.SignPool))
    retry_points: MSBEntryList[MSBRetryPointEvent] = field(default_factory=empty(MSBEventSubtype.RetryPoint))
    other_events: MSBEntryList[MSBOtherEvent] = field(default_factory=empty(MSBEventSubtype.OtherEvent))

    invasion_points: MSBEntryList[MSBInvasionPointRegion] = field(default_factory=empty(MSBRegionSubtype.InvasionPoint))
    environment_map_points: MSBEntryList[MSBEnvironmentMapPointRegion] = field(
        default_factory=empty(MSBRegionSubtype.EnvironmentMapPoint))
    sounds: MSBEntryList[MSBSoundRegion] = field(default_factory=empty(MSBRegionSubtype.Sound))
    vfx: MSBEntryList[MSBVFXRegion] = field(default_factory=empty(MSBRegionSubtype.VFX))
    wind_vfx: MSBEntryList[MSBWindVFXRegion] = field(default_factory=empty(MSBRegionSubtype.WindVFX))
    spawn_points: MSBEntryList[MSBSpawnPointRegion] = field(default_factory=empty(MSBRegionSubtype.SpawnPoint))
    messages: MSBEntryList[MSBMessageRegion] = field(default_factory=empty(MSBRegionSubtype.Message))
    environment_map_effect_boxes: MSBEntryList[MSBEnvironmentMapEffectBoxRegion] = field(
        default_factory=empty(MSBRegionSubtype.EnvironmentMapEffectBox))
    wind_areas: MSBEntryList[MSBWindAreaRegion] = field(default_factory=empty(MSBRegionSubtype.WindArea))
    connections: MSBEntryList[MSBConnectionRegion] = field(default_factory=empty(MSBRegionSubtype.Connection))
    patrol_route22s: MSBEntryList[MSBPatrolRoute22Region] = field(default_factory=empty(MSBRegionSubtype.PatrolRoute22))
    buddy_summon_points: MSBEntryList[MSBBuddySummonPointRegion] = field(
        default_factory=empty(MSBRegionSubtype.BuddySummonPoint))
    muffling_boxes: MSBEntryList[MSBMufflingBoxRegion] = field(default_factory=empty(MSBRegionSubtype.MufflingBox))
    muffling_portals: MSBEntryList[MSBMufflingPortalRegion] = field(
        default_factory=empty(MSBRegionSubtype.MufflingPortal))
    other_sounds: MSBEntryList[MSBOtherSoundRegion] = field(default_factory=empty(MSBRegionSubtype.OtherSound))
    muffling_planes: MSBEntryList[MSBMufflingPlaneRegion] = field(default_factory=empty(MSBRegionSubtype.MufflingPlane))
    patrol_routes: MSBEntryList[MSBPatrolRouteRegion] = field(default_factory=empty(MSBRegionSubtype.PatrolRoute))
    map_points: MSBEntryList[MSBMapPointRegion] = field(default_factory=empty(MSBRegionSubtype.MapPoint))
    weather_overrides: MSBEntryList[MSBWeatherOverrideRegion] = field(
        default_factory=empty(MSBRegionSubtype.WeatherOverride))
    auto_draw_group_points: MSBEntryList[MSBAutoDrawGroupPointRegion] = field(
        default_factory=empty(MSBRegionSubtype.AutoDrawGroupPoint))
    group_defeat_rewards: MSBEntryList[MSBGroupDefeatRewardRegion] = field(
        default_factory=empty(MSBRegionSubtype.GroupDefeatReward))
    map_point_discovery_overrides: MSBEntryList[MSBMapPointDiscoveryOverrideRegion] = field(
        default_factory=empty(MSBRegionSubtype.MapPointDiscoveryOverride))
    map_point_participation_overrides: MSBEntryList[MSBMapPointParticipationOverrideRegion] = field(
        default_factory=empty(MSBRegionSubtype.MapPointParticipationOverride))
    hitsets: MSBEntryList[MSBHitsetRegion] = field(default_factory=empty(MSBRegionSubtype.Hitset))
    fast_travel_restrictions: MSBEntryList[MSBFastTravelRestrictionRegion] = field(
        default_factory=empty(MSBRegionSubtype.FastTravelRestriction))
    weather_create_asset_points: MSBEntryList[MSBWeatherCreateAssetPointRegion] = field(
        default_factory=empty(MSBRegionSubtype.WeatherCreateAssetPoint))
    play_areas: MSBEntryList[MSBPlayAreaRegion] = field(default_factory=empty(MSBRegionSubtype.PlayArea))
    environment_map_outputs: MSBEntryList[MSBEnvironmentMapOutputRegion] = field(
        default_factory=empty(MSBRegionSubtype.EnvironmentMapOutput))
    mount_jumps: MSBEntryList[MSBMountJumpRegion] = field(default_factory=empty(MSBRegionSubtype.MountJump))
    dummies: MSBEntryList[MSBDummyRegion] = field(default_factory=empty(MSBRegionSubtype.Dummy))
    fall_prevention_removals: MSBEntryList[MSBFallPreventionRemovalRegion] = field(
        default_factory=empty(MSBRegionSubtype.FallPreventionRemoval))
    navmesh_cuttings: MSBEntryList[MSBNavmeshCuttingRegion] = field(
        default_factory=empty(MSBRegionSubtype.NavmeshCutting))
    map_name_overrides: MSBEntryList[MSBMapNameOverrideRegion] = field(
        default_factory=empty(MSBRegionSubtype.MapNameOverride))
    mount_jump_falls: MSBEntryList[MSBMountJumpFallRegion] = field(
        default_factory=empty(MSBRegionSubtype.MountJumpFall))
    horse_ride_overrides: MSBEntryList[MSBHorseRideOverrideRegion] = field(
        default_factory=empty(MSBRegionSubtype.HorseRideOverride))
    other_regions: MSBEntryList[MSBOtherRegion] = field(default_factory=empty(MSBRegionSubtype.OtherRegion))

    muffling_portal_links: MSBEntryList[MSBMufflingPortalLink] = field(
        default_factory=empty(MSBRouteSubtype.MufflingPortalLink))
    muffling_box_links: MSBEntryList[MSBMufflingBoxLink] = field(default_factory=empty(MSBRouteSubtype.MufflingBoxLink))
    other_routes: MSBEntryList[MSBOtherRoute] = field(default_factory=empty(MSBRouteSubtype.OtherRoute))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty(MSBPartSubtype.MapPiece))
    assets: MSBEntryList[MSBAsset] = field(default_factory=empty(MSBPartSubtype.Asset))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty(MSBPartSubtype.Character))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty(MSBPartSubtype.PlayerStart))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty(MSBPartSubtype.Collision))
    connect_collisions: MSBEntryList[MSBConnectCollision] = field(
        default_factory=empty(MSBPartSubtype.ConnectCollision))
    dummy_assets: MSBEntryList[MSBDummyAsset] = field(default_factory=empty(MSBPartSubtype.DummyAsset))
    dummy_characters: MSBEntryList[MSBDummyCharacter] = field(default_factory=empty(MSBPartSubtype.DummyCharacter))

    # TODO: Need to check all part `model_instance_id` values are unique.
    #  Can get first one and increment from there. Unfortunately, first value seems sort of arbitrary (7000, 9000, etc).

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

    @classmethod
    def resolve_supertype_name(cls, supertype: str) -> str:
        """Resolve various aliases for supertype names to the full MSB supertype list name.

        Handles the four standard types only, by default.
        """
        upper = supertype.upper()
        if upper.startswith("MODEL"):
            return MSBSupertype.MODELS
        if upper.startswith("EVENT"):
            return MSBSupertype.EVENTS
        if upper.startswith("REGION") or upper.startswith("POINT"):
            return MSBSupertype.REGIONS
        if upper.startswith("ROUTE"):
            return MSBSupertype.ROUTES
        if upper.startswith("LAYER"):
            return MSBSupertype.LAYERS
        if upper.startswith("PARTS"):
            return MSBSupertype.PARTS

        raise ValueError(f"Supertype name '{supertype}' not recognized.")

    def get_routes(self) -> list[MSBRoute]:
        # noinspection PyTypeChecker
        return self.get_supertype_list(MSBSupertype.ROUTES)

    def find_route_name(self, name: str | Enum, subtypes: tp.Iterable[str] = ()) -> MSBRoute:
        """Get `MSBRoute` with name `name` that is one of the given `entry_subtypes` or any type by default.

        Raises a `KeyError` if the name cannot be found, and a `ValueError` if multiple entries are found.
        """
        if isinstance(name, Enum):
            name = name.name
        # noinspection PyTypeChecker
        return self.find_entry_name(name, supertypes=[MSBSupertype.ROUTES], subtypes=subtypes)

    @classmethod
    def get_display_type_dict(cls) -> dict[str, tuple[BaseMSBSubtype, ...]]:
        """Return a nested dictionary mapping MSB type names (in typical display order) to tuples of subtype enums."""
        display_dict = {}  # type: dict[str, tuple[BaseMSBSubtype, ...]]
        for supertype_name, subtypes_info in cls.MSB_ENTRY_SUBTYPES.items():
            display_dict[supertype_name] = tuple(info.entry_class.SUBTYPE_ENUM for info in subtypes_info.values())
        return {
            "Parts": display_dict[MSBSupertype.PARTS],
            "Regions": display_dict[MSBSupertype.REGIONS],
            "Events": display_dict[MSBSupertype.EVENTS],
            "Routes": display_dict[MSBSupertype.ROUTES],
            "Models": display_dict[MSBSupertype.MODELS],
        }

    # region Utility Methods

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
