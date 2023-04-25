from __future__ import annotations

__all__ = ["MSB", "MSBSupertype"]

import typing as tp
from dataclasses import dataclass, field
from enum import Enum

from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBEntryList
from soulstruct.base.maps.msb.enums import BaseMSBSubtype
from soulstruct.base.maps.msb.utils import MSBSubtypeInfo
from soulstruct.utilities.binary import *
from soulstruct.utilities.future import StrEnum

from .constants import get_map
from .enums import *
from .models import *
from .events import *
from .regions import *
from .routes import *
from .parts import *


class MSBSupertype(StrEnum):
    """Same for most games."""
    MODELS = "MODEL_PARAM_ST"
    EVENTS = "EVENT_PARAM_ST"
    REGIONS = "POINT_PARAM_ST"
    ROUTES = "ROUTE_PARAM_ST"
    LAYERS = "LAYER_PARAM_ST"  # empty supertype
    PARTS = "PARTS_PARAM_ST"

    @classmethod
    def resolve(cls, supertype: str) -> MSBSupertype:
        """Resolve various forms of the supertype name into this enum."""
        if supertype.upper().startswith("MODEL"):
            return cls.MODELS
        if supertype.upper().startswith("EVENT"):
            return cls.EVENTS
        if supertype.upper().startswith("REGION") or supertype.upper().startswith("POINT"):
            return cls.REGIONS
        if supertype.upper().startswith("ROUTE"):
            return cls.ROUTES
        if supertype.upper().startswith("LAYER"):
            return cls.LAYERS
        if supertype.upper().startswith("PARTS"):
            return cls.PARTS
        raise ValueError(f"Cannot resolve unknown MSB supertype name: {supertype}")


@dataclass(slots=True)
class MSBEntrySuperlistHeader(BinaryStruct):
    _version: int = field(init=False, **Binary(asserted=73))
    entry_offset_count: int
    name_offset: long


MSB_ENTRY_SUBTYPES = {
    "MODEL_PARAM_ST": {
        "MapPieceModel": MSBSubtypeInfo(MSBModelSubtype.MapPieceModel, MSBMapPieceModel, "map_piece_models"),
        "AssetModel": MSBSubtypeInfo(MSBModelSubtype.AssetModel, MSBAssetModel, "asset_models"),
        "CharacterModel": MSBSubtypeInfo(MSBModelSubtype.CharacterModel, MSBCharacterModel, "character_models"),
        "PlayerModel": MSBSubtypeInfo(MSBModelSubtype.PlayerModel, MSBPlayerModel, "player_models"),
        "CollisionModel": MSBSubtypeInfo(MSBModelSubtype.CollisionModel, MSBCollisionModel, "collision_models"),
    },
    "EVENT_PARAM_ST": {
        "Treasure": MSBSubtypeInfo(MSBEventSubtype.Treasure, MSBTreasureEvent, "treasures"),
        "Spawner": MSBSubtypeInfo(MSBEventSubtype.Spawner, MSBSpawnerEvent, "spawners"),
        "ObjAct": MSBSubtypeInfo(MSBEventSubtype.ObjAct, MSBObjActEvent, "obj_acts"),
        "Navigation": MSBSubtypeInfo(MSBEventSubtype.Navigation, MSBNavigationEvent, "navigation"),
        "NPCInvasion": MSBSubtypeInfo(MSBEventSubtype.NPCInvasion, MSBNPCInvasionEvent, "npc_invasions"),
        "Platoon": MSBSubtypeInfo(MSBEventSubtype.Platoon, MSBPlatoonEvent, "platoons"),
        "PatrolRouteEvent": MSBSubtypeInfo(
            MSBEventSubtype.PatrolRouteEvent, MSBPatrolRouteEvent, "patrol_route_events"
        ),
        "Mount": MSBSubtypeInfo(MSBEventSubtype.Mount, MSBMountEvent, "mounts"),
        "SignPool": MSBSubtypeInfo(MSBEventSubtype.SignPool, MSBSignPoolEvent, "sign_pools"),
        "RetryPoint": MSBSubtypeInfo(MSBEventSubtype.RetryPoint, MSBRetryPointEvent, "retry_points"),
        "OtherEvent": MSBSubtypeInfo(MSBEventSubtype.OtherEvent, MSBOtherEvent, "other_events"),
    },
    "POINT_PARAM_ST": {
        "InvasionPoint": MSBSubtypeInfo(MSBRegionSubtype.InvasionPoint, MSBInvasionPointRegion, "invasion_points"),
        "EnvironmentMapPoint": MSBSubtypeInfo(
            MSBRegionSubtype.EnvironmentMapPoint, MSBEnvironmentMapPointRegion, "environment_map_points"
        ),
        "Sound": MSBSubtypeInfo(MSBRegionSubtype.Sound, MSBSoundRegion, "sounds"),
        "VFX": MSBSubtypeInfo(MSBRegionSubtype.VFX, MSBVFXRegion, "vfx"),
        "WindVFX": MSBSubtypeInfo(MSBRegionSubtype.WindVFX, MSBWindVFXRegion, "wind_vfx"),
        "SpawnPoint": MSBSubtypeInfo(MSBRegionSubtype.SpawnPoint, MSBSpawnPointRegion, "spawn_points"),
        "Message": MSBSubtypeInfo(MSBRegionSubtype.Message, MSBMessageRegion, "messages"),
        "EnvironmentMapEffectBox": MSBSubtypeInfo(
            MSBRegionSubtype.EnvironmentMapEffectBox, MSBEnvironmentMapEffectBoxRegion, "environment_map_effect_boxes"
        ),
        "WindArea": MSBSubtypeInfo(MSBRegionSubtype.WindArea, MSBWindAreaRegion, "wind_areas"),
        "Connection": MSBSubtypeInfo(MSBRegionSubtype.Connection, MSBConnectionRegion, "connections"),
        "PatrolRoute22": MSBSubtypeInfo(MSBRegionSubtype.PatrolRoute22, MSBPatrolRoute22Region, "patrol_route22s"),
        "BuddySummonPoint": MSBSubtypeInfo(
            MSBRegionSubtype.BuddySummonPoint, MSBBuddySummonPointRegion, "buddy_summon_points"
        ),
        "MufflingBox": MSBSubtypeInfo(MSBRegionSubtype.MufflingBox, MSBMufflingBoxRegion, "muffling_boxes"),
        "MufflingPortal": MSBSubtypeInfo(MSBRegionSubtype.MufflingPortal, MSBMufflingPortalRegion, "muffling_portals"),
        "OtherSound": MSBSubtypeInfo(MSBRegionSubtype.OtherSound, MSBOtherSoundRegion, "other_sounds"),
        "MufflingPlane": MSBSubtypeInfo(MSBRegionSubtype.MufflingPlane, MSBMufflingPlaneRegion, "muffling_planes"),
        "PatrolRoute": MSBSubtypeInfo(MSBRegionSubtype.PatrolRoute, MSBPatrolRouteRegion, "patrol_routes"),
        "MapPoint": MSBSubtypeInfo(MSBRegionSubtype.MapPoint, MSBMapPointRegion, "map_points"),
        "WeatherOverride": MSBSubtypeInfo(
            MSBRegionSubtype.WeatherOverride, MSBWeatherOverrideRegion, "weather_overrides"
        ),
        "AutoDrawGroupPoint": MSBSubtypeInfo(
            MSBRegionSubtype.AutoDrawGroupPoint, MSBAutoDrawGroupPointRegion, "auto_draw_group_points"
        ),
        "GroupDefeatReward": MSBSubtypeInfo(
            MSBRegionSubtype.GroupDefeatReward, MSBGroupDefeatRewardRegion, "group_defeat_rewards"
        ),
        "MapPointDiscoveryOverride": MSBSubtypeInfo(
            MSBRegionSubtype.MapPointDiscoveryOverride,
            MSBMapPointDiscoveryOverrideRegion,
            "map_point_discovery_overrides",
        ),
        "MapPointParticipationOverride": MSBSubtypeInfo(
            MSBRegionSubtype.MapPointParticipationOverride,
            MSBMapPointParticipationOverrideRegion,
            "map_point_participation_overrides",
        ),
        "Hitset": MSBSubtypeInfo(MSBRegionSubtype.Hitset, MSBHitsetRegion, "hitsets"),
        "FastTravelRestriction": MSBSubtypeInfo(
            MSBRegionSubtype.FastTravelRestriction,
            MSBFastTravelRestrictionRegion,
            "fast_travel_restrictions",
        ),
        "WeatherCreateAssetPoint": MSBSubtypeInfo(
            MSBRegionSubtype.WeatherCreateAssetPoint,
            MSBWeatherCreateAssetPointRegion,
            "weather_create_asset_points",
        ),
        "PlayArea": MSBSubtypeInfo(MSBRegionSubtype.PlayArea, MSBPlayAreaRegion, "play_areas"),
        "EnvironmentMapOutput": MSBSubtypeInfo(
            MSBRegionSubtype.EnvironmentMapOutput, MSBEnvironmentMapOutputRegion, "environment_map_outputs"
        ),
        "MountJump": MSBSubtypeInfo(MSBRegionSubtype.MountJump, MSBMountJumpRegion, "mount_jumps"),
        "Dummy": MSBSubtypeInfo(MSBRegionSubtype.Dummy, MSBDummyRegion, "dummies"),
        "FallPreventionRemoval": MSBSubtypeInfo(
            MSBRegionSubtype.FallPreventionRemoval, MSBFallPreventionRemovalRegion, "fall_prevention_removals"
        ),
        "NavmeshCutting": MSBSubtypeInfo(MSBRegionSubtype.NavmeshCutting, MSBNavmeshCuttingRegion, "navmesh_cuttings"),
        "MapNameOverride": MSBSubtypeInfo(
            MSBRegionSubtype.MapNameOverride, MSBMapNameOverrideRegion, "map_name_overrides"
        ),
        "MountJumpFall": MSBSubtypeInfo(MSBRegionSubtype.MountJumpFall, MSBMountJumpFallRegion, "mount_jump_falls"),
        "HorseRideOverride": MSBSubtypeInfo(
            MSBRegionSubtype.HorseRideOverride, MSBHorseRideOverrideRegion, "horse_ride_overrides"
        ),
        "OtherRegion": MSBSubtypeInfo(MSBRegionSubtype.OtherRegion, MSBOtherRegion, "other_regions"),
    },
    "ROUTE_PARAM_ST": {
        "MufflingPortalLink": MSBSubtypeInfo(
            MSBRouteSubtype.MufflingPortalLink, MSBMufflingPortalLink, "muffling_portal_links"
        ),
        "MufflingBoxLink": MSBSubtypeInfo(MSBRouteSubtype.MufflingBoxLink, MSBMufflingBoxLink, "muffling_box_links"),
        "OtherRoute": MSBSubtypeInfo(MSBRouteSubtype.OtherRoute, MSBOtherRoute, "other_routes"),
    },
    "LAYER_PARAM_ST": {},  # empty supertype
    "PARTS_PARAM_ST": {
        "MapPiece": MSBSubtypeInfo(MSBPartSubtype.MapPiece, MSBMapPiece, "map_pieces"),
        "Asset": MSBSubtypeInfo(MSBPartSubtype.Asset, MSBAsset, "assets"),
        "Character": MSBSubtypeInfo(MSBPartSubtype.Character, MSBCharacter, "characters"),
        "PlayerStart": MSBSubtypeInfo(MSBPartSubtype.PlayerStart, MSBPlayerStart, "player_starts"),
        "Collision": MSBSubtypeInfo(MSBPartSubtype.Collision, MSBCollision, "collisions"),
        "UnusedAsset": MSBSubtypeInfo(MSBPartSubtype.UnusedAsset, MSBUnusedAsset, "unused_assets"),
        "UnusedCharacter": MSBSubtypeInfo(MSBPartSubtype.UnusedCharacter, MSBUnusedCharacter, "unused_characters"),
        "MapConnection": MSBSubtypeInfo(MSBPartSubtype.MapConnection, MSBMapConnection, "map_connections"),
    },
}


def empty_list(supertype_prefix: str, subtype_enum_name: str) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(f"{supertype_prefix}_PARAM_ST")
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum_name]
    return lambda: MSBEntryList(supertype=supertype, subtype_info=subtype_info)


@dataclass(slots=True, kw_only=True)
class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[tp.Type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_ENTRY_SUPERTYPES = {
        MSBSupertype.MODELS: MSBModel,
        MSBSupertype.EVENTS: MSBEvent,
        MSBSupertype.REGIONS: MSBRegion,
        MSBSupertype.ROUTES: MSBRoute,
        MSBSupertype.LAYERS: None,  # empty supertype (no known subtypes)
        MSBSupertype.PARTS: MSBPart,
    }
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[str, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        "MODEL_PARAM_ST": 8,
        "EVENT_PARAM_ST": 12,
        "POINT_PARAM_ST": 8,
        "ROUTE_PARAM_ST": 16,
        "LAYER_PARAM_ST": -1,  # empty supertype (no known subtypes)
        "PARTS_PARAM_ST": 12,
    }
    ENTITY_GAME_TYPES: tp.ClassVar[dict[str, MapEntity]] = {}  # TODO for Elden Ring

    HAS_HEADER: tp.ClassVar[bool] = True
    LONG_VARINTS: tp.ClassVar[bool] = True
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty_list("MODEL", "MapPieceModel"))
    asset_models: MSBEntryList[MSBAssetModel] = field(default_factory=empty_list("MODEL", "AssetModel"))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty_list("MODEL", "CharacterModel"))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty_list("MODEL", "PlayerModel"))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty_list("MODEL", "CollisionModel"))

    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty_list("EVENT", "Treasure"))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty_list("EVENT", "Spawner"))
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=empty_list("EVENT", "ObjAct"))
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=empty_list("EVENT", "Navigation"))
    npc_invasions: MSBEntryList[MSBNPCInvasionEvent] = field(default_factory=empty_list("EVENT", "NPCInvasion"))
    platoons: MSBEntryList[MSBPlatoonEvent] = field(default_factory=empty_list("EVENT", "Platoon"))
    # TODO: rename to 'patrol_routes' and change region name to 'patrol_route_points'
    patrol_route_events: MSBEntryList[MSBPatrolRouteEvent] = field(
        default_factory=empty_list("EVENT", "PatrolRouteEvent")
    )
    mounts: MSBEntryList[MSBMountEvent] = field(default_factory=empty_list("EVENT", "Mount"))
    sign_pools: MSBEntryList[MSBSignPoolEvent] = field(default_factory=empty_list("EVENT", "SignPool"))
    retry_points: MSBEntryList[MSBRetryPointEvent] = field(default_factory=empty_list("EVENT", "RetryPoint"))
    other_events: MSBEntryList[MSBOtherEvent] = field(default_factory=empty_list("EVENT", "OtherEvent"))

    invasion_points: MSBEntryList[MSBInvasionPointRegion] = field(default_factory=empty_list("POINT", "InvasionPoint"))
    environment_map_points: MSBEntryList[MSBEnvironmentMapPointRegion] = field(
        default_factory=empty_list("POINT", "EnvironmentMapPoint")
    )
    sounds: MSBEntryList[MSBSoundRegion] = field(default_factory=empty_list("POINT", "Sound"))
    vfx: MSBEntryList[MSBVFXRegion] = field(default_factory=empty_list("POINT", "VFX"))
    wind_vfx: MSBEntryList[MSBWindVFXRegion] = field(default_factory=empty_list("POINT", "WindVFX"))
    spawn_points: MSBEntryList[MSBSpawnPointRegion] = field(default_factory=empty_list("POINT", "SpawnPoint"))
    messages: MSBEntryList[MSBMessageRegion] = field(default_factory=empty_list("POINT", "Message"))
    environment_map_effect_boxes: MSBEntryList[MSBEnvironmentMapEffectBoxRegion] = field(
        default_factory=empty_list("POINT", "EnvironmentMapEffectBox")
    )
    wind_areas: MSBEntryList[MSBWindAreaRegion] = field(default_factory=empty_list("POINT", "WindArea"))
    connections: MSBEntryList[MSBConnectionRegion] = field(default_factory=empty_list("POINT", "Connection"))
    patrol_route22s: MSBEntryList[MSBPatrolRoute22Region] = field(default_factory=empty_list("POINT", "PatrolRoute22"))
    buddy_summon_points: MSBEntryList[MSBBuddySummonPointRegion] = field(
        default_factory=empty_list("POINT", "BuddySummonPoint")
    )
    muffling_boxes: MSBEntryList[MSBMufflingBoxRegion] = field(default_factory=empty_list("POINT", "MufflingBox"))
    muffling_portals: MSBEntryList[MSBMufflingPortalRegion] = field(
        default_factory=empty_list("POINT", "MufflingPortal")
    )
    other_sounds: MSBEntryList[MSBOtherSoundRegion] = field(default_factory=empty_list("POINT", "OtherSound"))
    muffling_planes: MSBEntryList[MSBMufflingPlaneRegion] = field(default_factory=empty_list("POINT", "MufflingPlane"))
    patrol_routes: MSBEntryList[MSBPatrolRouteRegion] = field(default_factory=empty_list("POINT", "PatrolRoute"))
    map_points: MSBEntryList[MSBMapPointRegion] = field(default_factory=empty_list("POINT", "MapPoint"))
    weather_overrides: MSBEntryList[MSBWeatherOverrideRegion] = field(
        default_factory=empty_list("POINT", "WeatherOverride")
    )
    auto_draw_group_points: MSBEntryList[MSBAutoDrawGroupPointRegion] = field(
        default_factory=empty_list("POINT", "AutoDrawGroupPoint")
    )
    group_defeat_rewards: MSBEntryList[MSBGroupDefeatRewardRegion] = field(
        default_factory=empty_list("POINT", "GroupDefeatReward")
    )
    map_point_discovery_overrides: MSBEntryList[MSBMapPointDiscoveryOverrideRegion] = field(
        default_factory=empty_list("POINT", "MapPointDiscoveryOverride")
    )
    map_point_participation_overrides: MSBEntryList[MSBMapPointParticipationOverrideRegion] = field(
        default_factory=empty_list("POINT", "MapPointParticipationOverride")
    )
    hitsets: MSBEntryList[MSBHitsetRegion] = field(default_factory=empty_list("POINT", "Hitset"))
    fast_travel_restrictions: MSBEntryList[MSBFastTravelRestrictionRegion] = field(
        default_factory=empty_list("POINT", "FastTravelRestriction")
    )
    weather_create_asset_points: MSBEntryList[MSBWeatherCreateAssetPointRegion] = field(
        default_factory=empty_list("POINT", "WeatherCreateAssetPoint")
    )
    play_areas: MSBEntryList[MSBPlayAreaRegion] = field(default_factory=empty_list("POINT", "PlayArea"))
    environment_map_outputs: MSBEntryList[MSBEnvironmentMapOutputRegion] = field(
        default_factory=empty_list("POINT", "EnvironmentMapOutput")
    )
    mount_jumps: MSBEntryList[MSBMountJumpRegion] = field(default_factory=empty_list("POINT", "MountJump"))
    dummies: MSBEntryList[MSBDummyRegion] = field(default_factory=empty_list("POINT", "Dummy"))
    fall_prevention_removals: MSBEntryList[MSBFallPreventionRemovalRegion] = field(
        default_factory=empty_list("POINT", "FallPreventionRemoval")
    )
    navmesh_cuttings: MSBEntryList[MSBNavmeshCuttingRegion] = field(
        default_factory=empty_list("POINT", "NavmeshCutting")
    )
    map_name_overrides: MSBEntryList[MSBMapNameOverrideRegion] = field(
        default_factory=empty_list("POINT", "MapNameOverride")
    )
    mount_jump_falls: MSBEntryList[MSBMountJumpFallRegion] = field(default_factory=empty_list("POINT", "MountJumpFall"))
    horse_ride_overrides: MSBEntryList[MSBHorseRideOverrideRegion] = field(
        default_factory=empty_list("POINT", "HorseRideOverride")
    )
    other_regions: MSBEntryList[MSBOtherRegion] = field(default_factory=empty_list("POINT", "OtherRegion"))

    muffling_portal_links: MSBEntryList[MSBMufflingPortalLink] = field(
        default_factory=empty_list("ROUTE", "MufflingPortalLink")
    )
    muffling_box_links: MSBEntryList[MSBMufflingBoxLink] = field(default_factory=empty_list("ROUTE", "MufflingBoxLink"))
    other_routes: MSBEntryList[MSBOtherRoute] = field(default_factory=empty_list("ROUTE", "OtherRoute"))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty_list("PARTS", "MapPiece"))
    assets: MSBEntryList[MSBAsset] = field(default_factory=empty_list("PARTS", "Asset"))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty_list("PARTS", "Character"))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty_list("PARTS", "PlayerStart"))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty_list("PARTS", "Collision"))
    map_connections: MSBEntryList[MSBMapConnection] = field(default_factory=empty_list("PARTS", "MapConnection"))
    unused_assets: MSBEntryList[MSBUnusedAsset] = field(default_factory=empty_list("PARTS", "UnusedAsset"))
    unused_characters: MSBEntryList[MSBUnusedCharacter] = field(default_factory=empty_list("PARTS", "UnusedCharacter"))

    # TODO: Need to check all part `model_instance_id` values are unique.
    #  Can get first one and increment from there. Unfortunately, first value seems sort of arbitrary (7000, 9000, etc).

    def pack_supertype_name(self, writer: BinaryWriter, supertype_name: str):
        packed_name = supertype_name.encode(self.NAME_ENCODING)
        writer.append(packed_name)
        writer.pad(8)

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
    def get_display_type_dict(cls) -> dict[str, tuple[BaseMSBSubtype]]:
        """Return a nested dictionary mapping MSB type names (in typical display order) to tuples of subtype enums."""
        display_dict = {}  # type: dict[str, tuple[BaseMSBSubtype]]
        for supertype_name, subtypes_info in cls.MSB_ENTRY_SUBTYPES.items():
            display_dict[supertype_name] = tuple(info.subtype_enum for info in subtypes_info.values())
        return {
            "Parts": display_dict[MSBSupertype.PARTS],
            "Regions": display_dict[MSBSupertype.REGIONS],
            "Events": display_dict[MSBSupertype.EVENTS],
            "Routes": display_dict[MSBSupertype.ROUTES],
            "Models": display_dict[MSBSupertype.MODELS],
        }

    # region Utility Methods

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
