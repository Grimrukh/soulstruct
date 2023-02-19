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
    "UnusedObject",
    "UnusedCharacter",
    "MapConnection",

    "Region",
    "RegionVolume",
    "RegionPoint",
    "RegionCircle",
    "RegionSphere",
    "RegionCylinder",
    "RegionRect",
    "RegionBox",

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

    "ID_RANGES",
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
            area_id=60,
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

# TODO
ID_RANGES = {}
#     RegionVolume: (2000, 2499),
#     RegionPoint: (2500, 2899),
#     MapPiece: (3000, 3199),
#     Object: (1000, 1899),
#     Character: (0, 899),
#     PlayerStart: (990, 999),
#     Collision: (3200, 3399),
#     SoundEvent: (3800, 3899),
#     VFXEvent: (3400, 3599),
#     SpawnerEvent: (3600, 3699),
#     MessageEvent: (3700, 3799),
#     SpawnPointEvent: (3900, 3949),
# }
