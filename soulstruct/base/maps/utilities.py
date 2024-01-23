from __future__ import annotations

__all__ = ["get_map", "GET_MAP_TYPING", "MAP_SOURCE_TYPING"]

import logging
import typing as tp
from pathlib import Path

from soulstruct.base.game_types.map_types import Map

_LOGGER = logging.getLogger("soulstruct")

SPECIAL_MAP_NAMES = (
    "aicommon",
    "common_func",
)


MAP_SOURCE_TYPING = tp.Union[
    str,  # e.g. `m10_01_00_00` or `m10_01` or `m10_01_00_00.msb` or `UNDEAD_BURG` or `UndeadBurg`
    int,  # e.g. `1001` or '10010000`
    tuple[int, int],  # e.g. `(10, 1)`
    tuple[int, int, int],  # e.g. `(10, 1, 0)`
    tuple[int, int, int, int],  # e.g. `(10, 1, 0, 0)`
    list[int],  # one of the above types (sequence of length 2/3/4)
    Map,  # existing `Map` instance (to validate against allowed `game_maps` list)
]


def get_map(source: MAP_SOURCE_TYPING, game_maps: tp.Sequence[Map]) -> Map:
    """Flexible-input function for retrieving valid `Map` object instances for a particular FromSoft game.

    Valid `source` types and examples:
        str: `m10_01_00_00` or `m10_01` or `m10_01_00_00.msb` or `UNDEAD_BURG` or `UndeadBurg`
        int: `1001` or '10010000`
        [int, int]: `(10, 1)`
        [int, int, int]: `(10, 1, 0)`
        [int, int, int, int]: `(10, 1, 0, 0)`
        Map: existing `Map` instance (to validate against allowed `game_maps` list)
    """
    if not game_maps:
        raise ImportError("No game maps given. (You should import `get_maps` from `soulstruct.maps.{game}.maps`.)")

    input_source = source  # for clearer logging below

    if isinstance(source, Map):
        if source != Map.NO_MAP() and source not in game_maps:
            raise ValueError(f"Map {source} does not appear in game's maps: {game_maps}")
        return source

    if isinstance(source, (list, tuple)):
        if len(source) == 2:
            area_id, block_id, cc_id, dd_id = source[0], source[1], 0, 0
        elif len(source) == 3:
            area_id, block_id, cc_id, dd_id = source[0], source[1], source[2], 0
        elif len(source) == 4:
            area_id, block_id, cc_id, dd_id = source
        else:
            raise ValueError(f"Map source sequence must be 2, 3, or 4 elements, not: {source}")
        # Values of -1 in BB/CC/DD can match 0 (these appear in `MSBMapConnection`s sometimes).
        if block_id == -1:
            block_id = 0
        if cc_id == -1:
            cc_id = 0
        if dd_id == -1:
            dd_id = 0
        stem = f"m{area_id:02d}_{block_id:02}_{cc_id:02d}_{dd_id:02}"
        matches = [g for g in game_maps if stem in g.stem_set()]
    elif isinstance(source, int):
        source = str(int)
        if len(source) == 8:
            area_id, block_id, cc_id, dd_id = int(source[0:2]), int(source[2:4]), int(source[4:6]), int(source[6:8])
        elif len(source) == 6:
            area_id, block_id, cc_id, dd_id = int(source[0:2]), int(source[2:4]), int(source[4:6]), 0
        elif len(source) == 4:
            area_id, block_id, cc_id, dd_id = int(source[0:2]), int(source[2:4]), 0, 0
        else:
            raise ValueError("Map stem integer must be exactly 4, 6, or 8 digits (e.g. `10010000` -> `m10_01_00_00`).")
        stem = f"m{area_id:02d}_{block_id:02}_{cc_id:02d}_{dd_id:02}"
        matches = [g for g in game_maps if stem in g.stem_set()]
    elif isinstance(source, str):
        if (source.startswith("m") and "_" in source) or source.lower() in SPECIAL_MAP_NAMES:
            source = Path(source).stem  # remove file extensions
            matches = [g for g in game_maps if source in g.stem_set()]
        else:
            # Canonical name, eg `FIRELINK_SHRINE` or `FirelinkShrine`. Change to lower case and remove underscores.
            source = source.lower().replace("_", "")
            matches = [g for g in game_maps if source == g.name.lower().replace("_", "")]
    else:
        raise TypeError(f"Invalid type for map-finding source: {source} (type {type(source)})")

    if len(matches) > 1:
        raise ValueError(f"Multiple maps matched for '{input_source}': {[g.name for g in matches]}")
    elif not matches:
        raise ValueError(f"No maps matched for '{input_source}'.")

    return matches[0]


class GET_MAP_TYPING(tp.Protocol):
    """Type hint for `get_map` function that can be used for base classes.

    Does not incloude `game_maps` argument, which game-specific wrapper function will supply.
    """
    def __call__(self, source: MAP_SOURCE_TYPING):
        ...
