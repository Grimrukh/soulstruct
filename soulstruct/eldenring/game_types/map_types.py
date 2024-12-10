from __future__ import annotations

__all__ = [
    "Map",
    "MapTile",
    "MapTyping",
    "MapEntry",
    "MapEntity",

    "MapModel",
    "MapPieceModel",
    "AssetModel",
    "CharacterModel",
    "PlayerModel",
    "CollisionModel",
    "NavmeshModel",

    "MapEvent",
    "LightEvent",
    "SoundEvent",
    "VFXEvent",
    "WindEvent",
    "TreasureEvent",
    "SpawnerEvent",
    "MessageEvent",
    "ObjActEvent",
    "SpawnPointEvent",
    "MapOffsetEvent",
    "NavigationEvent",
    "EnvironmentEvent",
    "NPCInvasionEvent",

    "MapPart",
    "MapPiece",
    "Asset",
    "Character",
    "Collision",
    "PlayerStart",
    "Navmesh",
    "DummyAsset",
    "DummyCharacter",
    "ConnectCollision",

    "Region",
    "InvasionPointRegion",
    "EnvironmentMapPointRegion",
    "SoundRegion",
    "SFXRegion",
    "WindSFXRegion",
    "SpawnPointRegion",
    "MessageRegion",
    "EnvironmentMapEffectBoxRegion",
    "WindAreaRegion",
    "ConnectionRegion",
    "PatrolRoute22Region",
    "BuddySummonPointRegion",
    "MufflingBoxRegion",
    "MufflingPortalRegion",
    "OtherSoundRegion",
    "MufflingPlaneRegion",
    "PatrolRouteRegion",
    "MapPointRegion",
    "WeatherOverrideRegion",
    "AutoDrawGroupPointRegion",
    "GroupDefeatRewardRegion",
    "MapPointDiscoveryOverrideRegion",
    "MapPointParticipationOverrideRegion",
    "HitsetRegion",
    "FastTravelRestrictionRegion",
    "WeatherCreateAssetPointRegion",
    "PlayAreaRegion",
    "EnvironmentMapOutputRegion",
    "MountJumpRegion",
    "DummyRegion",
    "FallPreventionRemovalRegion",
    "NavmeshCuttingRegion",
    "MapNameOverrideRegion",
    "MountJumpFallRegion",
    "HorseRideOverrideRegion",
    "OtherRegion",

    # TODO: routes

    "MapPartTyping",
    "CoordEntityTyping",
    "AssetTyping",
    "RegionTyping",
    "CharacterTyping",
    "AnimatedEntityTyping",
    "MapPieceTyping",
    "CollisionTyping",
    "SoundEventTyping",
    "NavigationEventTyping",
    "VFXEventTyping",
]

import typing as tp

from soulstruct.base.game_types.map_types import *


class MapTile(Map):
    """Map subclass for Elden Ring that simplifies arguments and has references to parent tiles."""

    class MapTileException(Exception):
        """Exception raised by an invalid X/Y coordinate for given size ID."""

    def __init__(
        self,
        x_id: int,
        y_id: int,
        size_id: int,
        area_id=60,
        name=None,
        emevd_file_stem=None,
        msb_file_stem=None,
        ai_file_stem=None,
        esd_file_stem=None,
        ffxbnd_file_name=None,
        variable_name=None,
        verbose_name=None,
        sites_of_grace=(),
        markers=(),
        parent_tile: tp.Optional[MapTile] = None,
        is_alternate=False,
    ):
        # Check X/Y validity.
        if x_id < 8 or x_id > 57:
            raise self.MapTileException(f"Map tile x = {x_id} is not valid for any map size.")
        if y_id < 7 or y_id > 63:
            raise self.MapTileException(f"Map tile y = {y_id} is not valid for any map size.")
        if size_id == 2:
            if not 8 <= x_id <= 14:
                raise self.MapTileException(f"Large tiles (02) cannot have x = {x_id}.")
            if not 7 <= y_id <= 15:
                raise self.MapTileException(f"Large tiles (02) cannot have y = {y_id}.")
        elif size_id == 1:
            if not 16 <= x_id <= 28:
                raise self.MapTileException(f"Medium tiles (01) cannot have x = {x_id}.")
            if not 15 <= y_id <= 31:
                raise self.MapTileException(f"Medium tiles (01) cannot have y = {y_id}.")
        elif size_id == 0:
            if not 32 <= x_id <= 57:
                raise self.MapTileException(f"Small tiles (00) cannot have x = {x_id}.")
            if not 30 <= y_id <= 63:
                raise self.MapTileException(f"Small tiles (00) cannot have y = {y_id}.")
        elif not is_alternate:
            raise self.MapTileException(
                f"Invalid tile size ID: {size_id}. Must be 2 (large), 1 (medium), or 0 (small)."
            )

        # TODO: Can probably simplify stem arguments.
        super().__init__(
            area_id=area_id,
            block_id=x_id,
            cc_id=y_id,
            dd_id=size_id,
            name=name,
            emevd_file_stem=emevd_file_stem,
            msb_file_stem=msb_file_stem,
            ai_file_stem=ai_file_stem,
            esd_file_stem=esd_file_stem,
            ffxbnd_file_name=ffxbnd_file_name,
            variable_name=variable_name,
            verbose_name=verbose_name,
        )
        self.sites_of_grace = sites_of_grace
        self.markers = markers
        self.parent_tile = parent_tile


# Add `MapTile` to allowed types for `game_map` EMEVD arguments.
MapTyping = tp.Union[Map, MapTile, tuple[int, int, int, int], list[int, int, int, int]]


class InvasionPointRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "InvasionPoints") if pluralized_subtype else ("Region", "InvasionPoint")


class EnvironmentMapPointRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "EnvironmentMapPoints") if pluralized_subtype else ("Region", "EnvironmentMapPoint")


class SoundRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Sounds") if pluralized_subtype else ("Region", "Sound")


class SFXRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "SFX") if pluralized_subtype else ("Region", "SFX")


class WindSFXRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "WindVFX") if pluralized_subtype else ("Region", "WindVFX")


class SpawnPointRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "SpawnPoints") if pluralized_subtype else ("Region", "SpawnPoint")


class MessageRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Messages") if pluralized_subtype else ("Region", "Message")


class EnvironmentMapEffectBoxRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "EnvironmentMapEffectBoxes") if pluralized_subtype else ("Region", "EnvironmentMapEffectBox")


class WindAreaRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "WindAreas") if pluralized_subtype else ("Region", "WindArea")


class ConnectionRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Connections") if pluralized_subtype else ("Region", "Connection")


class PatrolRoute22Region(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "PatrolRoute22s") if pluralized_subtype else ("Region", "PatrolRoute22")


class BuddySummonPointRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "BuddySummonPoints") if pluralized_subtype else ("Region", "BuddySummonPoint")


class MufflingBoxRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MufflingBoxes") if pluralized_subtype else ("Region", "MufflingBox")


class MufflingPortalRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MufflingPortals") if pluralized_subtype else ("Region", "MufflingPortal")


class OtherSoundRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "OtherSounds") if pluralized_subtype else ("Region", "OtherSound")


class MufflingPlaneRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MufflingPlanes") if pluralized_subtype else ("Region", "MufflingPlane")


class PatrolRouteRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "PatrolRoutes") if pluralized_subtype else ("Region", "PatrolRoute")


class MapPointRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MapPoints") if pluralized_subtype else ("Region", "MapPoint")


class WeatherOverrideRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "WeatherOverrides") if pluralized_subtype else ("Region", "WeatherOverride")


class AutoDrawGroupPointRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "AutoDrawGroupPoints") if pluralized_subtype else ("Region", "AutoDrawGroupPoint")


class GroupDefeatRewardRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "GroupDefeatRewards") if pluralized_subtype else ("Region", "GroupDefeatReward")


class MapPointDiscoveryOverrideRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MapPointDiscoveryOverrides") if pluralized_subtype else ("Region", "MapPointDiscoveryOverride")


class MapPointParticipationOverrideRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MapPointParticipationOverrides") if pluralized_subtype else ("Region", "MapPointParticipationOverride")


class HitsetRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Hitsets") if pluralized_subtype else ("Region", "Hitset")


class FastTravelRestrictionRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "FastTravelRestrictions") if pluralized_subtype else ("Region", "FastTravelRestriction")


class WeatherCreateAssetPointRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "WeatherCreateAssetPoints") if pluralized_subtype else ("Region", "WeatherCreateAssetPoint")


class PlayAreaRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "PlayAreas") if pluralized_subtype else ("Region", "PlayArea")


class EnvironmentMapOutputRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "EnvironmentMapOutputs") if pluralized_subtype else ("Region", "EnvironmentMapOutput")


class MountJumpRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MountJumps") if pluralized_subtype else ("Region", "MountJump")


class DummyRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Dummies") if pluralized_subtype else ("Region", "Dummy")


class FallPreventionRemovalRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "FallPreventionRemovals") if pluralized_subtype else ("Region", "FallPreventionRemoval")


class NavmeshCuttingRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "NavmeshCuttings") if pluralized_subtype else ("Region", "NavmeshCutting")


class MapNameOverrideRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MapNameOverrides") if pluralized_subtype else ("Region", "MapNameOverride")


class MountJumpFallRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "MountJumpFalls") if pluralized_subtype else ("Region", "MountJumpFall")


class HorseRideOverrideRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "HorseRideOverrides") if pluralized_subtype else ("Region", "HorseRideOverride")


class OtherRegion(Region):

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Regions", "Others") if pluralized_subtype else ("Region", "Other")


# `Object` replaced with `Asset` in these typings.
AnimatedEntityTyping = tp.Union[Asset, Character, int]
CoordEntityTyping = tp.Union[Asset, Character, Region, int]
