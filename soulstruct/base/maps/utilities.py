from __future__ import annotations

__all__ = ["get_map", "GET_MAP_TYPING"]

import logging
import typing as tp
from pathlib import Path

from soulstruct.base.game_types.map_types import Map

_LOGGER = logging.getLogger(__name__)

SPECIAL_MAP_NAMES = (
    "aicommon",
    "common_func",
)


def get_map(source, block_id=None, game_maps: tp.Sequence[Map] = ()) -> Map:
    """Flexible-input function for retrieving valid `Map` object instances for a particular FromSoft game.

    Valid `source` values:
        (area_id: int, block_id: int), e.g., (10, 0)
        (area_id: int, block_id: int, cc_id: int, dd_id: int), e.g., (60, 44, 36, 10)
        four_digit_id: int (such as 1000)
        file_stem: str (such as "m10_00_00_00"; file extensions don't matter, both EMEVD and MSB names will be checked)
        map_name: str (such as "UNDEAD_BURG" or "UndeadBurg"; case and underscores don't matter)
    """
    if game_maps is None:
        raise ImportError("No game maps given. (You should import `get_maps` from `soulstruct.maps.{game}.maps`.)")

    source_orig = source if block_id is None else (source, block_id)

    if isinstance(source, Map):
        if block_id is not None:
            raise ValueError(f"`block_id` must be None if a `Map` instance is passed to `get_map`.")
        if source != Map.NO_MAP() and source not in game_maps:
            raise ValueError(f"Map {source} does not appear in game's maps: {game_maps}")
        return source

    if isinstance(source, (list, tuple)):
        if len(source) == 2:
            source = (source[0], source[1], 0, 0)
        try:
            area_id, block_id, cc_id, dd_id = source
        except ValueError:
            raise ValueError(
                f"Sequence source for map-finding should be two (a, b) or four (a, b, c, d) values, not: {source}."
            )
        if block_id == -1:
            block_id = 0
        if cc_id == -1:
            cc_id = 0
        if dd_id == -1:
            dd_id = 0
        matches = [
            g for g in game_maps
            if g.area_id == area_id and g.block_id == block_id and g.cc_id == cc_id and g.dd_id == dd_id
        ]
    elif isinstance(source, int):
        if block_id is not None:
            try:
                area_id = int(source)
                block_id = int(block_id)
            except ValueError:
                raise ValueError(f"Invalid map-finding source: ({source}, {block_id})")
            if block_id == -1:
                block_id = 0
            matches = [g for g in game_maps if g.area_id == area_id and g.block_id == block_id]
        else:
            source = str(int)
            if len(source) != 4:
                raise ValueError("Abbreviated map ID should be exactly four digits (100 * area_id + block_id).")
            area_id, block_id = source[:2], source[2:]
            if block_id == -1:
                block_id = 0
            matches = [g for g in game_maps if g.area_id == area_id and g.block_id == block_id]
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
        raise ValueError(f"Multiple maps matched for '{source_orig}': {[g.name for g in matches]}")
    elif not matches:
        raise ValueError(f"No maps matched for '{source_orig}'.")

    return matches[0]


class GET_MAP_TYPING(tp.Protocol):
    """Type hint for `get_map` function that can be used for base classes."""
    def __call__(self, source: tp.Union[str, tuple], block_id: int = ...):
        ...
