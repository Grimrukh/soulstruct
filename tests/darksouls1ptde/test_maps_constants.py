"""Pure-unit tests for `soulstruct.darksouls1ptde.maps.constants`.

These need no game data and always run. They assert that the DS1 `Map` constant table is internally
consistent: no duplicate IDs, stems, names or variable names, and that the various lookup helpers
(`get_map`, `get_map_variable_name`) agree with the table.
"""
from __future__ import annotations

import pytest

from soulstruct.darksouls1ptde.maps import constants as C
from soulstruct.darksouls1ptde.maps.constants import ALL_MAPS, get_map, get_map_variable_name
from soulstruct.darksouls1ptde.game_types.map_types import Map


# Maps that have no MSB/area of their own.
NON_ASSET_MAPS = {C.COMMON}


def test_all_exported_names_exist():
    for name in C.__all__:
        assert hasattr(C, name), f"`maps.constants.__all__` exports missing name: {name}"


def test_all_maps_contains_every_module_level_map():
    module_maps = {
        value for name, value in vars(C).items()
        if isinstance(value, Map) and not name.startswith("_")
    }
    assert module_maps == set(ALL_MAPS), (
        "Every module-level `Map` constant must appear in `ALL_MAPS` (and vice versa). "
        f"Missing from ALL_MAPS: {module_maps - set(ALL_MAPS)}; "
        f"extra in ALL_MAPS: {set(ALL_MAPS) - module_maps}"
    )


def test_no_duplicate_area_block_ids():
    seen = {}
    for game_map in ALL_MAPS:
        if game_map.area_id is None:
            continue
        key = (game_map.area_id, game_map.block_id, game_map.cc_id, game_map.dd_id)
        assert key not in seen, f"Duplicate map ID {key}: {seen.get(key)} and {game_map.name}"
        seen[key] = game_map.name
    assert len(seen) == len(ALL_MAPS) - len(NON_ASSET_MAPS)


@pytest.mark.parametrize("attr", ["name", "variable_name", "verbose_name"])
def test_no_duplicate_map_names(attr):
    values = [getattr(m, attr) for m in ALL_MAPS]
    assert len(values) == len(set(values)), f"Duplicate `Map.{attr}` values: {values}"


def test_every_map_has_variable_name_matching_module_constant():
    """`variable_name` must be the module-level constant name, or EVS output will not compile."""
    for game_map in ALL_MAPS:
        assert game_map.variable_name is not None, f"Map {game_map.name} has no `variable_name`."
        assert hasattr(C, game_map.variable_name), (
            f"Map `variable_name` '{game_map.variable_name}' is not a module-level constant."
        )
        assert getattr(C, game_map.variable_name) is game_map


@pytest.mark.parametrize("stem_attr", ["msb_file_stem", "emevd_file_stem", "ai_file_stem", "esd_file_stem"])
def test_no_duplicate_file_stems(stem_attr):
    """Two maps sharing a file stem would silently overwrite each other in a `GameFileMapDirectory`."""
    stems = [getattr(m, stem_attr) for m in ALL_MAPS if getattr(m, stem_attr)]
    assert len(stems) == len(set(stems)), f"Duplicate `{stem_attr}` values: {sorted(stems)}"


def test_map_stems_are_well_formed():
    for game_map in ALL_MAPS:
        if game_map in NON_ASSET_MAPS:
            assert game_map.map_stem is None
            continue
        assert game_map.map_stem == (
            f"m{game_map.area_id:02d}_{game_map.block_id:02d}_{game_map.cc_id:02d}_{game_map.dd_id:02d}"
        )


def test_base_entity_ids_and_flags():
    """DS1 convention: base entity ID is `aa * 100000 + bb * 10000`; base flag is `1000 + 10 * aa + bb`."""
    for game_map in ALL_MAPS:
        if game_map in NON_ASSET_MAPS:
            continue
        assert game_map.base_entity_id == 100000 * game_map.area_id + 10000 * game_map.block_id
        assert game_map.base_flag == 1000 + 10 * game_map.area_id + game_map.block_id


def test_darkroot_garden_uses_dlc_msb():
    """Darkroot's MSB is the '..._01' revision but its EMEVD/ESD/AI use '..._00'."""
    assert C.DARKROOT_GARDEN.msb_file_stem == "m12_00_00_01"
    assert C.DARKROOT_GARDEN.emevd_file_stem == "m12_00_00_00"
    assert C.DARKROOT_GARDEN.esd_file_stem == "m12_00_00_00"


def test_common_map_has_no_msb_or_esd():
    assert C.COMMON.msb_file_stem is None
    assert C.COMMON.esd_file_stem is None
    assert C.COMMON.emevd_file_stem == "common"
    assert C.COMMON.ai_file_stem == "aiCommon"


@pytest.mark.parametrize("game_map", [m for m in ALL_MAPS if m.map_stem], ids=lambda m: m.name)
def test_get_map_accepts_all_sources(game_map):
    assert get_map(game_map) is game_map
    assert get_map(game_map.map_stem) is game_map
    assert get_map(game_map.name) is game_map
    assert get_map((game_map.area_id, game_map.block_id)) is game_map


def test_get_map_variable_name_round_trip():
    for game_map in ALL_MAPS:
        if game_map.area_id is None:
            continue
        assert get_map_variable_name((game_map.area_id, game_map.block_id)) == game_map.variable_name


def test_get_map_variable_name_unknown_map_falls_back_to_tuple():
    assert get_map_variable_name((99, 0)) == "(99, 0, 0, 0)"
    assert get_map_variable_name((99, 0, 1, 2)) == "(99, 0, 1, 2)"


def test_get_map_rejects_unknown_map():
    with pytest.raises((KeyError, ValueError)):
        get_map("m99_99_99_99")


def test_drawparam_areas_cover_all_map_areas():
    """Every DS1 map area must have a `DrawParamBND` area entry, or its lighting cannot be edited."""
    from soulstruct.darksouls1ptde.params.draw_param import DrawParamDirectory

    draw_param_areas = set(DrawParamDirectory.DRAW_PARAM_AREAS)
    for game_map in ALL_MAPS:
        if game_map.area_id is None:
            continue
        assert f"a{game_map.area_id:02d}" in draw_param_areas, (
            f"No DrawParam area for map {game_map.name} (a{game_map.area_id:02d})."
        )


def test_event_directory_map_properties_match_constants():
    from soulstruct.darksouls1ptde.events.event_directory import EventDirectory

    assert set(EventDirectory.ALL_MAPS) == set(ALL_MAPS)


def test_map_studio_directory_excludes_common():
    from soulstruct.darksouls1ptde.maps.map_studio_directory import MapStudioDirectory

    assert C.COMMON not in MapStudioDirectory.ALL_MAPS
    assert set(MapStudioDirectory.ALL_MAPS) == {m for m in ALL_MAPS if m.msb_file_stem}
    assert MapStudioDirectory.MAP_STEM_ATTRIBUTE == "msb_file_stem"
