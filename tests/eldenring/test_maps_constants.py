"""Pure-unit tests for Elden Ring map constants (`soulstruct.eldenring.maps`).

These tests need no game data: they validate the internal consistency of the ~876 `Map`/`MapTile`
constants defined across `legacy_dungeons`, `generic_dungeons`, `overworld`, and their DLC
counterparts, plus the `MapStudioDirectory` properties built from them.

NOTE: `soulstruct.eldenring.maps.msb` is deliberately not exercised here (ER MSBs are handled by a
separate C++ library), but importing `soulstruct.eldenring.maps` does pull it in.
"""
from __future__ import annotations

import importlib
from collections import Counter

import pytest

from soulstruct.base.game_types.map_types import Map
from soulstruct.eldenring.game_types.map_types import MapTile
from soulstruct.eldenring.maps import constants as C
from soulstruct.eldenring.maps.map_studio_directory import MapStudioDirectory


MAP_MODULE_NAMES = (
    "legacy_dungeons",
    "generic_dungeons",
    "overworld",
    "dlc_legacy_dungeons",
    "dlc_generic_dungeons",
    "dlc_overworld",
)

ALL_MAPS = C.ALL_MAPS


def _map_modules():
    return {name: importlib.import_module(f"soulstruct.eldenring.maps.{name}") for name in MAP_MODULE_NAMES}


# ---------------------------------------------------------------------------
# Identity / uniqueness
# ---------------------------------------------------------------------------


def test_all_maps_is_populated():
    assert len(ALL_MAPS) > 800, "Expected ~876 Elden Ring maps in `ALL_MAPS`."
    # NOTE: identity checks, because `Map.__eq__` only compares (area_id, block_id) and would report
    # `COMMON == COMMON_FUNC` (both have `None` IDs). See `test_maps_are_set_safe` xfail.
    ids = {id(m) for m in ALL_MAPS}
    assert id(C.COMMON) in ids
    # `COMMON_FUNC` is deliberately excluded from `ALL_MAPS` (it is only added inside `get_map`).
    assert id(C.COMMON_FUNC) not in ids


def test_no_duplicate_map_ids():
    """The (area, block, cc, dd) tuple must uniquely identify a map."""
    counts = Counter((m.area_id, m.block_id, m.cc_id, m.dd_id) for m in ALL_MAPS)
    dupes = {k: v for k, v in counts.items() if v > 1}
    assert not dupes, f"Duplicate Elden Ring map IDs: {dupes}"


@pytest.mark.parametrize("attr", ["name", "variable_name", "verbose_name", "msb_file_stem", "emevd_file_stem"])
def test_no_duplicate_map_attributes(attr):
    counts = Counter(getattr(m, attr) for m in ALL_MAPS if getattr(m, attr) is not None)
    dupes = {k: v for k, v in counts.items() if v > 1}
    assert not dupes, f"Duplicate `{attr}` values across Elden Ring maps: {dupes}"


def test_variable_names_resolve_to_same_object():
    """`Map.variable_name` must be the name of the module-level constant holding that exact `Map`."""
    bad = []
    for game_map in ALL_MAPS:
        if game_map.variable_name is None:
            continue
        if getattr(C, game_map.variable_name, None) is not game_map:
            bad.append(game_map.variable_name)
    assert not bad, f"`variable_name` does not resolve to the same `Map` object: {bad}"


def test_map_stem_format():
    """Every map with an area ID must have an `mAA_BB_CC_DD` stem."""
    import re

    stem_re = re.compile(r"^m\d{2}_\d{2}_\d{2}_\d{2}$")
    for game_map in ALL_MAPS:
        if game_map.area_id is None:
            assert game_map.map_stem is None
        else:
            assert stem_re.match(game_map.map_stem), f"Bad map stem: {game_map.map_stem}"


# ---------------------------------------------------------------------------
# Per-module `__all__` hygiene
# ---------------------------------------------------------------------------


def test_module_all_lists_are_complete_and_valid():
    for name, mod in _map_modules().items():
        declared = getattr(mod, "__all__", None)
        assert declared is not None, f"`{name}` has no `__all__`."
        for exported in declared:
            assert hasattr(mod, exported), f"`{name}.__all__` names missing attribute '{exported}'."
        defined = {k for k, v in vars(mod).items() if isinstance(v, Map) and not k.startswith("_")}
        missing = defined - set(declared)
        assert not missing, f"`{name}` defines maps not in `__all__`: {sorted(missing)}"


def test_every_defined_map_is_in_all_maps():
    all_ids = {id(m) for m in ALL_MAPS}
    for name, mod in _map_modules().items():
        for var, game_map in vars(mod).items():
            if isinstance(game_map, Map) and not var.startswith("_"):
                assert id(game_map) in all_ids, f"`{name}.{var}` is not included in `ALL_MAPS`."


def test_map_constant_names_are_upper_snake_case():
    """All ER map constants should be UPPER_SNAKE_CASE.

    Known offender: `m42_01_00_00` in `dlc_generic_dungeons` (an unnamed DLC Ruined Forge).
    """
    offenders = []
    for name, mod in _map_modules().items():
        for var, game_map in vars(mod).items():
            if isinstance(game_map, Map) and not var.startswith("_") and var != var.upper():
                offenders.append(f"{name}.{var}")
    assert offenders == ["dlc_generic_dungeons.m42_01_00_00"], (
        f"Unexpected non-UPPER_CASE map constants: {offenders}"
    )


# ---------------------------------------------------------------------------
# Overworld tile grid rules (documented at the top of `overworld.py`)
# ---------------------------------------------------------------------------


def _tiles():
    return [m for m in ALL_MAPS if isinstance(m, MapTile)]


def test_overworld_tiles_use_expected_area_ids():
    for tile in _tiles():
        assert tile.area_id in (60, 61), f"Unexpected tile area ID {tile.area_id} for {tile.variable_name}"


def test_tile_size_ids():
    """`dd_id` is 2 (large), 1 (medium) or 0 (small); alternates add 10."""
    for tile in _tiles():
        assert tile.dd_id in (0, 1, 2, 10, 11, 12), f"Bad tile size ID {tile.dd_id} for {tile.variable_name}"


def test_tile_parent_relationship():
    """A child tile's X/Y must be 2*parent X/Y (+0 or +1) and its size must be one step smaller."""
    for tile in _tiles():
        parent = tile.parent_tile
        if parent is None:
            continue
        assert tile.dd_id % 10 == (parent.dd_id % 10) - 1, (
            f"{tile.variable_name} (dd={tile.dd_id}) has parent {parent.variable_name} (dd={parent.dd_id})"
        )
        assert tile.block_id in (2 * parent.block_id, 2 * parent.block_id + 1), (
            f"{tile.variable_name} x={tile.block_id} not a child of {parent.variable_name} x={parent.block_id}"
        )
        assert tile.cc_id in (2 * parent.cc_id, 2 * parent.cc_id + 1), (
            f"{tile.variable_name} y={tile.cc_id} not a child of {parent.variable_name} y={parent.cc_id}"
        )
        assert tile.area_id == parent.area_id


def test_alternate_tiles_have_alternate_parents():
    """Alternate tiles (dd_id >= 10) must descend only from other alternate tiles."""
    for tile in _tiles():
        if tile.dd_id >= 10 and tile.parent_tile is not None:
            assert tile.parent_tile.dd_id >= 10, (
                f"Alternate tile {tile.variable_name} has non-alternate parent {tile.parent_tile.variable_name}"
            )


def test_maptile_rejects_invalid_coordinates():
    with pytest.raises(MapTile.MapTileException):
        MapTile(7, 10, 2)  # x below minimum
    with pytest.raises(MapTile.MapTileException):
        MapTile(10, 6, 2)  # y below minimum
    with pytest.raises(MapTile.MapTileException):
        MapTile(20, 20, 2)  # large tile with medium-tile x
    with pytest.raises(MapTile.MapTileException):
        MapTile(10, 10, 3)  # invalid size ID


def test_maptile_accepts_alternate_size_ids():
    """`is_alternate=True` bypasses size validation (used for ER's `dd_id = 1X` duplicate tiles)."""
    tile = MapTile(11, 11, 12, 61, name="X", variable_name="X", is_alternate=True)
    assert tile.map_stem == "m61_11_11_12"


# ---------------------------------------------------------------------------
# `get_map` lookups
# ---------------------------------------------------------------------------


def test_get_map_by_various_sources():
    assert C.get_map("m10_00_00_00") is C.STORMVEIL_CASTLE
    assert C.get_map((10, 0, 0, 0)) is C.STORMVEIL_CASTLE
    assert C.get_map(C.STORMVEIL_CASTLE) is C.STORMVEIL_CASTLE
    assert C.get_map("StormveilCastle") is C.STORMVEIL_CASTLE


def test_get_map_includes_common_func():
    """`get_map` explicitly appends `COMMON_FUNC`, which is not in `ALL_MAPS`."""
    assert C.get_map("common_func") is C.COMMON_FUNC


def test_get_map_variable_name_fallback():
    assert C.get_map_variable_name(C.STORMVEIL_CASTLE) == "STORMVEIL_CASTLE"
    # Unknown map falls back to a tuple repr.
    assert C.get_map_variable_name((99, 99, 99, 99)) == "(99, 99, 99, 99)"


# ---------------------------------------------------------------------------
# `MapStudioDirectory`
# ---------------------------------------------------------------------------


def test_map_studio_directory_properties_match_map_names():
    props = {k for k, v in vars(MapStudioDirectory).items() if isinstance(v, property)}
    map_names = {m.name for m in ALL_MAPS}
    unknown = props - map_names
    assert not unknown, f"`MapStudioDirectory` properties with no matching `Map.name`: {sorted(unknown)[:10]}"


def test_quietly_ignored_stems_do_not_shadow_real_maps():
    real_stems = {m.msb_file_stem for m in ALL_MAPS if m.msb_file_stem}
    overlap = real_stems & MapStudioDirectory.QUIETLY_IGNORED_FILE_STEMS
    assert not overlap, f"`QUIETLY_IGNORED_FILE_STEMS` shadows real MSB stems: {sorted(overlap)}"


def test_map_studio_directory_uses_msb_stem_attribute():
    assert MapStudioDirectory.MAP_STEM_ATTRIBUTE == "msb_file_stem"
    assert MapStudioDirectory.FILE_EXTENSION == ".msb"


# ---------------------------------------------------------------------------
# Known bugs (kept as xfail so they are noticed if fixed)
# ---------------------------------------------------------------------------


def test_all_overworld_tiles_have_msb_file_stems():
    missing = [m.variable_name for m in _tiles() if not m.msb_file_stem]
    assert not missing, f"{len(missing)} overworld tiles have no `msb_file_stem` (e.g. {missing[:5]})"


def test_map_studio_directory_covers_all_maps_with_properties():
    props = {k for k, v in vars(MapStudioDirectory).items() if isinstance(v, property)}
    covered = {m.name for m in MapStudioDirectory.ALL_MAPS}
    assert props <= covered, f"{len(props - covered)} `map_property` entries have no loadable map."


@pytest.mark.xfail(
    reason="BUG: `Map.__repr__` returns `self.emevd_file_stem`, which is `None` for every `MapTile`.",
    strict=False,
)
def test_repr_of_map_tile():
    assert isinstance(repr(C.SOUTHWEST_LIURNIA), str)


def test_maps_are_set_safe():
    """Passes now that `msb_file_stem` (used by `__hash__`) is unique per map (see finding #18); the

    underlying `Map.__eq__`/`__hash__` inconsistency (eq on area/block only) is a separate, non-critical
    issue that no longer manifests here because hashes are no longer colliding.
    """
    assert len(set(ALL_MAPS)) == len(ALL_MAPS)
