"""Pure-unit tests for `soulstruct.darksouls1r.maps.constants` (and the PTDE constants it re-exports).

These tests never touch game data, so they always run. They assert the internal consistency of the DSR
map table (`ALL_MAPS`), the `get_map()` lookup, and the hand-written `VANILLA_MSB_TRANSLATIONS` dict.
"""
from __future__ import annotations

import re
from collections import Counter

import pytest

from soulstruct.darksouls1r.maps import ALL_MAPS, get_map
from soulstruct.darksouls1r.maps.constants import (
    COMMON,
    DEPTHS,
    DARKROOT_GARDEN,
    UNDEAD_ASYLUM,
    VANILLA_MSB_TRANSLATIONS,
    get_map_variable_name,
)

MAP_STEM_RE = re.compile(r"^m\d\d_\d\d_\d\d_\d\d$")
# DS1 entity IDs are seven digits: `AABX***` where the map is `mAA_0B_00_00` and `X` groups the entry
# supertype (e.g. 2 = regions, 3 = events, 4 = navigation events).
ENTITY_ID_RE = re.compile(r"^(\d\d)(\d)(\d)(\d\d\d)$")
PYTHON_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


# ---------------------------------------------------------------------------
# `ALL_MAPS` table consistency
# ---------------------------------------------------------------------------


def test_all_maps_is_non_empty_tuple():
    assert isinstance(ALL_MAPS, tuple)
    assert len(ALL_MAPS) == 18  # 17 real maps + `COMMON`


@pytest.mark.parametrize("attr", ["name", "variable_name"])
def test_map_names_are_unique(attr):
    values = [getattr(m, attr) for m in ALL_MAPS]
    duplicates = sorted(v for v, count in Counter(values).items() if count > 1)
    assert not duplicates, f"Duplicate `Map.{attr}` values in DSR `ALL_MAPS`: {duplicates}"


def test_map_ids_are_unique():
    """No two maps may share an (area_id, block_id) pair, or `get_map()` becomes ambiguous."""
    ids = [(m.area_id, m.block_id) for m in ALL_MAPS if m.area_id is not None]
    duplicates = sorted(i for i, count in Counter(ids).items() if count > 1)
    assert not duplicates, f"Duplicate (area_id, block_id) in DSR `ALL_MAPS`: {duplicates}"


@pytest.mark.parametrize("stem_attr", ["msb_file_stem", "emevd_file_stem", "esd_file_stem", "ai_file_stem"])
def test_file_stems_are_unique(stem_attr):
    """Two maps writing to the same file stem would silently clobber each other in directory classes."""
    stems = [getattr(m, stem_attr) for m in ALL_MAPS if getattr(m, stem_attr)]
    duplicates = sorted(s for s, count in Counter(stems).items() if count > 1)
    assert not duplicates, f"Duplicate `Map.{stem_attr}` values in DSR `ALL_MAPS`: {duplicates}"


def test_msb_file_stems_are_well_formed():
    for game_map in ALL_MAPS:
        if game_map.msb_file_stem is None:
            continue
        assert MAP_STEM_RE.match(game_map.msb_file_stem), (
            f"Bad MSB file stem for {game_map.variable_name}: {game_map.msb_file_stem}"
        )


def test_variable_names_are_valid_python_identifiers():
    """`variable_name` is emitted into generated EVS/enums modules, so it must be importable."""
    for game_map in ALL_MAPS:
        assert PYTHON_NAME_RE.match(game_map.variable_name), game_map.variable_name


def test_common_map_has_no_msb():
    assert COMMON.msb_file_stem is None
    assert COMMON.emevd_file_stem == "common"


def test_darkroot_garden_uses_dlc_msb():
    """DSR always has the DLC, so Darkroot must use the '_01' MSB (not the '_00' pre-DLC one)."""
    assert DARKROOT_GARDEN.msb_file_stem == "m12_00_00_01"


# ---------------------------------------------------------------------------
# `get_map()` lookup
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "source",
    ["m10_00_00_00", "Depths", (10, 0), DEPTHS],
)
def test_get_map_accepts_multiple_source_types(source):
    assert get_map(source) is DEPTHS


def test_get_map_round_trips_every_map():
    for game_map in ALL_MAPS:
        if game_map.msb_file_stem is None:
            continue
        assert get_map(game_map.msb_file_stem) is game_map
        assert get_map((game_map.area_id, game_map.block_id)) is game_map


def test_get_map_raises_for_unknown_map():
    with pytest.raises((KeyError, ValueError)):
        get_map("m77_77_00_00")


def test_get_map_variable_name_known_and_unknown():
    assert get_map_variable_name(UNDEAD_ASYLUM) == "UNDEAD_ASYLUM"
    # Unknown maps fall back to a literal tuple string.
    assert get_map_variable_name((77, 7, 0, 0)) == "(77, 7, 0, 0)"


# ---------------------------------------------------------------------------
# `VANILLA_MSB_TRANSLATIONS`
# ---------------------------------------------------------------------------


def test_translations_dict_is_non_empty_and_typed():
    assert len(VANILLA_MSB_TRANSLATIONS) > 1000
    for entity_id, name in VANILLA_MSB_TRANSLATIONS.items():
        assert isinstance(entity_id, int)
        assert isinstance(name, str) and name


def test_translation_names_are_valid_python_identifiers():
    """Translated names end up as MSB entry names, which become enum member names in generated modules."""
    bad = sorted(name for name in VANILLA_MSB_TRANSLATIONS.values() if not PYTHON_NAME_RE.match(name))
    assert not bad, f"Translated MSB names that are not valid Python identifiers: {bad}"


def test_translation_entity_ids_have_ds1_format():
    bad = sorted(eid for eid in VANILLA_MSB_TRANSLATIONS if not ENTITY_ID_RE.match(str(eid)))
    assert not bad, f"Entity IDs not in DS1 `1AABX***` format: {bad}"


def test_translation_entity_ids_belong_to_known_maps():
    """Every translated entity ID's `AAB` prefix must correspond to a real DSR map."""
    known_prefixes = {
        f"{m.area_id:02d}{m.block_id:d}" for m in ALL_MAPS if m.area_id is not None
    }
    bad = sorted({str(eid)[:3] for eid in VANILLA_MSB_TRANSLATIONS} - known_prefixes)
    assert not bad, f"Translated entity IDs for unknown map prefixes: {bad}"


def test_translated_names_are_unique_within_each_map_and_id_class():
    """Two entries of the same *kind* in the same map must not get the same translated name.

    The 'X' digit of `AABX***` separates supertypes (regions are X=2, sound events X=3, etc.), so this
    check catches real `find_entry_name()` ambiguity without flagging the (intentional) vanilla practice
    of naming e.g. a boss music *region* and a boss music *sound event* the same thing.
    """
    by_group = {}  # type: dict[tuple[str, str], list[tuple[int, str]]]
    for entity_id, name in VANILLA_MSB_TRANSLATIONS.items():
        match = ENTITY_ID_RE.match(str(entity_id))
        map_prefix = match.group(1) + match.group(2)
        id_class = match.group(3)
        by_group.setdefault((map_prefix, id_class), []).append((entity_id, name))

    clashes = []
    for group, items in sorted(by_group.items()):
        counts = Counter(name for _, name in items)
        for name, count in counts.items():
            if count > 1:
                ids = sorted(eid for eid, n in items if n == name)
                clashes.append((group, name, ids))
    assert not clashes, f"Duplicate translated names within one map + ID class: {clashes}"
