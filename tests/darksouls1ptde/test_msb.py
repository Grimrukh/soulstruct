"""Tests for DS1 PTDE MSB (map studio) files.

Rewritten from the original `unittest` module; intent preserved:
  - read the whole vanilla `map/MapStudio` directory, write it, and read it back;
  - open the committed Depths MSB, duplicate a character and a treasure, write, reload, and compare
    every entry of every subtype;
  - JSON round-trip.
Plus pure-unit checks on the MSB subtype tables and entity-ID range guidelines.
"""
from __future__ import annotations

import logging
import shutil

import pytest

from soulstruct.darksouls1ptde.maps import MSB, MapStudioDirectory
from soulstruct.darksouls1ptde.maps.constants import DEPTHS, ALL_MAPS
from soulstruct.darksouls1ptde.maps.enums import (
    CollisionHitFilter,
    MSBEventSubtype,
    MSBModelSubtype,
    MSBPartSubtype,
    MSBRegionSubtype,
    MSBSupertype,
)
from soulstruct.dcx import DCXType
from soulstruct.utilities.maths import Vector3


# ---------------------------------------------------------------------------
# Pure-unit: class configuration
# ---------------------------------------------------------------------------


def test_ptde_msb_configuration():
    assert MSB.HAS_HEADER is False
    assert MSB.LONG_VARINTS is False
    assert MSB.NAME_ENCODING == "shift_jis_2004"
    assert MSB.IS_BIG_ENDIAN is False
    assert MSB().dcx_type == DCXType.Null, "PTDE MSBs are uncompressed."


def test_subtype_list_names_match_entry_tables():
    """Every subtype registered in `MSB_ENTRY_SUBTYPES` must have a matching `MSBEntryList` field."""
    for supertype, subtypes in MSB.MSB_ENTRY_SUBTYPES.items():
        for subtype_enum, info in subtypes.items():
            assert info.subtype_list_name in MSB.get_subtype_list_names(), (
                f"{supertype}/{subtype_enum.name}: '{info.subtype_list_name}' is not an MSB field."
            )
            msb = MSB()
            entry_list = getattr(msb, info.subtype_list_name)
            assert entry_list.supertype == supertype
            assert entry_list.entry_class is info.entry_class


def test_no_duplicate_subtype_list_names():
    names = [
        info.subtype_list_name
        for subtypes in MSB.MSB_ENTRY_SUBTYPES.values()
        for info in subtypes.values()
    ]
    assert len(names) == len(set(names)), f"Duplicate subtype list names: {names}"


def test_supertype_enums_are_complete():
    assert set(MSB.MSB_ENTRY_SUBTYPES) == set(MSBSupertype)
    assert set(MSB.MSB_ENTRY_SUPERTYPES) == set(MSBSupertype)
    assert set(MSB.MSB_SUPERTYPE_SUBTYPE_ENUMS) == set(MSBSupertype)
    assert set(MSB.MSB_ENTRY_SUBTYPE_OFFSETS) == set(MSBSupertype)
    for supertype, subtype_enum_cls in MSB.MSB_SUPERTYPE_SUBTYPE_ENUMS.items():
        assert set(MSB.MSB_ENTRY_SUBTYPES[supertype]) == set(subtype_enum_cls)


def test_subtype_enum_values_are_unique():
    for enum_cls in (MSBModelSubtype, MSBEventSubtype, MSBRegionSubtype, MSBPartSubtype):
        values = [member.value for member in enum_cls]
        assert len(values) == len(set(values)), f"{enum_cls.__name__} has duplicate values."


def test_entity_game_types_reference_real_subtype_lists():
    for subtype_list_name in MSB.ENTITY_GAME_TYPES:
        assert subtype_list_name in MSB.get_subtype_list_names(), (
            f"`ENTITY_GAME_TYPES` key '{subtype_list_name}' is not an MSB subtype list."
        )


def test_ds1_entity_id_ranges_do_not_overlap():
    """The DS1 ID-range guidelines used by `EnumModuleGenerator` must be internally consistent."""
    base = DEPTHS.base_entity_id
    ranges = {}
    for game_type, range_func in MSB.ID_RANGES.items():
        bounds = range_func(base)
        first, last = bounds["first_value"], bounds["last_value"]
        assert first <= last, f"{game_type.__name__}: inverted ID range."
        ranges[game_type.__name__] = (first, last)
    names = sorted(ranges)
    for i, name_a in enumerate(names):
        a_first, a_last = ranges[name_a]
        for name_b in names[i + 1:]:
            b_first, b_last = ranges[name_b]
            assert a_last < b_first or b_last < a_first, (
                f"Entity ID ranges overlap: {name_a} {ranges[name_a]} vs {name_b} {ranges[name_b]}"
            )


def test_collision_hit_filter_solidity():
    assert CollisionHitFilter.Normal.is_solid_to_player() is True
    assert CollisionHitFilter.NoHiHitNoFeetIK.is_solid_to_player() is True
    assert CollisionHitFilter.Water_A.is_solid_to_player() is False
    assert CollisionHitFilter.KillPlane.is_solid_to_player() is False
    assert CollisionHitFilter.GroupSwitch.is_solid_to_player() is True


# ---------------------------------------------------------------------------
# Committed Depths MSB
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def depths_msb_path(request):
    path = request.path.parent / "resources" / "m10_00_00_00.msb"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


@pytest.fixture
def depths_msb(depths_msb_path) -> MSB:
    return MSB.from_path(depths_msb_path)


def _assert_msbs_equal(source: MSB, other: MSB):
    for subtype_list_name in MSB.get_subtype_list_names():
        source_entries = source[subtype_list_name]
        other_entries = other[subtype_list_name]
        assert len(source_entries) == len(other_entries), (
            f"'{subtype_list_name}' length differs: {len(source_entries)} != {len(other_entries)}"
        )
        for i, entry in enumerate(source_entries):
            assert entry == other_entries[i], f"'{subtype_list_name}'[{i}] ({entry.name}) differs."


def test_depths_msb_loads(depths_msb):
    assert depths_msb.characters.find_entry_name("c1000_0000") is not None
    assert len(depths_msb.regions) > 0
    assert len(depths_msb.collisions) > 0


def test_depths_msb_binary_round_trip(depths_msb, tmp_path):
    """unpack -> pack -> unpack must preserve every entry of every subtype."""
    out_path = tmp_path / "m10_00_00_00.msb"
    depths_msb.write(out_path)
    assert not (tmp_path / "m10_00_00_00.msb.dcx").is_file(), "PTDE MSBs must not be DCX."
    reloaded = MSB.from_path(out_path)
    _assert_msbs_equal(depths_msb, reloaded)
    assert bytes(reloaded) == bytes(depths_msb)


def test_depths_msb_duplicate_and_reload(depths_msb, tmp_path):
    """Original test intent: duplicate the main bonfire character and a treasure, then round-trip."""
    source_chr = depths_msb.characters.find_entry_name("c1000_0000")
    depths_msb.characters.duplicate(
        source_chr, name="c1000_0000_COPY", entity_id=1000999, translate=Vector3([1.0, 2.0, 3.0])
    )
    depths_msb.treasures.duplicate(0, name="TREASURE_0_COPY")

    out_path = tmp_path / "m10_00_00_00.msb"
    depths_msb.write(out_path)
    reloaded = MSB.from_path(out_path)

    new_chr = reloaded.characters.find_entry_name("c1000_0000_COPY")
    assert new_chr.entity_id == 1000999
    assert tuple(new_chr.translate) == (1.0, 2.0, 3.0)
    assert new_chr.model is not None
    assert new_chr.model.name == source_chr.model.name
    assert reloaded.treasures.find_entry_name("TREASURE_0_COPY") is not None

    _assert_msbs_equal(depths_msb, reloaded)


def test_depths_msb_entity_ids_are_unique_per_subtype(depths_msb):
    """Entity IDs bind MSB entries to `game_types` enums, so duplicates within a subtype make the
    generated enum module ambiguous.

    NOTE: vanilla DS1 does NOT respect this everywhere -- the Depths MSB has two Collisions with
    entity ID 1003000 -- so Collisions are excluded (see the `MSB.ID_RANGES` docstring).
    """
    known_vanilla_offenders = {"collisions"}
    for subtype_list_name in MSB.ENTITY_GAME_TYPES:
        if subtype_list_name in known_vanilla_offenders:
            continue
        entity_ids = [
            entry.entity_id for entry in depths_msb[subtype_list_name]
            if getattr(entry, "entity_id", -1) > 0
        ]
        assert len(entity_ids) == len(set(entity_ids)), (
            f"Duplicate entity IDs in '{subtype_list_name}': {entity_ids}"
        )


def test_id_ranges_are_offsets_from_map_base_id(depths_msb):
    """`MSB.ID_RANGES` are *guidelines* for new entities, not invariants of vanilla data (vanilla
    Depths characters use raw IDs like 6130). Check only that they scale with `map_base_id`."""
    from soulstruct.darksouls1ptde.game_types.map_types import Character

    zero = MSB.ID_RANGES[Character](0)
    depths = MSB.ID_RANGES[Character](DEPTHS.base_entity_id)
    assert depths["first_value"] - zero["first_value"] == DEPTHS.base_entity_id
    assert depths["last_value"] - zero["last_value"] == DEPTHS.base_entity_id


def test_depths_msb_new_c1000(depths_msb):
    new_chr = depths_msb.new_c1000("DEBUG_WARP")
    assert new_chr.model is not None
    assert new_chr.model.name == "c1000"
    assert depths_msb.characters.find_entry_name("DEBUG_WARP") is new_chr


def test_depths_msb_auto_model_rejects_bad_part(depths_msb):
    from soulstruct.darksouls1ptde.maps.parts import MSBMapPiece

    map_piece = depths_msb.map_pieces[0] if depths_msb.map_pieces else None
    if map_piece is None:
        pytest.skip("No map pieces in Depths MSB.")
    assert isinstance(map_piece, MSBMapPiece)
    model = depths_msb.auto_model(map_piece, map_piece.model.name, map_stem="m10_00_00_00")
    assert model is map_piece.model


def test_depths_msb_json_round_trip(depths_msb, tmp_path):
    json_path = tmp_path / "m10_00_00_00.json"
    depths_msb.write_json(json_path)
    reloaded = MSB.from_json(json_path)
    _assert_msbs_equal(depths_msb, reloaded)


def test_depths_msb_deep_copy_repacks_identically(depths_msb):
    """`copy.deepcopy` must rebuild every entry's referrer tracker so the copy is still packable."""
    import copy as copy_module

    duplicate = copy_module.deepcopy(depths_msb)
    assert duplicate is not depths_msb
    _assert_msbs_equal(depths_msb, duplicate)
    assert bytes(duplicate) == bytes(depths_msb)
    # Entries were genuinely copied, and the copies' references point within the copy.
    part = duplicate.map_pieces[0]
    assert part is not depths_msb.map_pieces[0]
    assert any(model is part.model for model in duplicate.map_piece_models)
    assert part.model is not depths_msb.map_pieces[0].model


def test_map_studio_directory_json_reports_progress(depths_msb_path, tmp_path):
    """`MapStudioDirectory` JSON reads/writes accept an optional `progress` callback."""
    msb_dir = tmp_path / "MapStudio"
    msb_dir.mkdir()
    stems = ["m10_00_00_00", "m10_01_00_00", "m10_02_00_00"]
    for stem in stems:
        shutil.copy(depths_msb_path, msb_dir / f"{stem}.msb")
    msd = MapStudioDirectory.from_path(msb_dir)

    write_calls = []
    msd.write_json_directory(tmp_path / "json", progress=lambda *call: write_calls.append(call))
    read_calls = []
    MapStudioDirectory.from_json_directory(
        tmp_path / "json", progress=lambda *call: read_calls.append(call)
    )

    for calls in (write_calls, read_calls):
        assert calls, "no progress reported"
        totals = {total for _, total, _ in calls}
        assert len(totals) == 1, f"`total` changed mid-operation: {totals}"
        currents = [current for current, _, _ in calls]
        assert currents == sorted(currents), "`current` must not go backwards"
        assert currents[0] == 0
        assert currents[-1] == totals.copy().pop()
    assert {label for _, _, label in read_calls if label} >= set(stems)


# ---------------------------------------------------------------------------
# Vanilla MapStudio directory
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def map_studio_dir(ptde_root):
    path = ptde_root / "map" / "MapStudio"
    if not path.is_dir():
        pytest.skip(f"Missing PTDE MapStudio directory: {path}")
    return path


@pytest.mark.slow
def test_map_studio_directory_loads(map_studio_dir, caplog):
    with caplog.at_level(logging.CRITICAL):
        msd = MapStudioDirectory.from_path(map_studio_dir)
    expected_stems = {m.msb_file_stem for m in ALL_MAPS if m.msb_file_stem}
    assert set(msd.files) == expected_stems
    # The pre-DLC Darkroot MSB must be quietly ignored.
    assert "m12_00_00_00" not in msd.files
    assert msd.Depths is msd.files["m10_00_00_00"]
    assert msd.DarkrootGarden is msd.files["m12_00_00_01"]
    assert msd[DEPTHS] is msd.Depths
    assert msd["m10_00_00_00"] is msd.Depths


@pytest.mark.slow
def test_map_studio_directory_round_trip(map_studio_dir, tmp_path, caplog):
    """Original test intent: read whole MapStudio dir, write it, read it back."""
    with caplog.at_level(logging.CRITICAL):
        msd = MapStudioDirectory.from_path(map_studio_dir)
        packed = {stem: bytes(msb) for stem, msb in msd.files.items()}
        out_dir = tmp_path / "MapStudio"
        out_dir.mkdir()
        msd.write(out_dir)
        reloaded = MapStudioDirectory.from_path(out_dir)
    assert set(reloaded.files) == set(msd.files)
    for stem, msb in reloaded.files.items():
        assert bytes(msb) == packed[stem], f"{stem}: MSB repack is not stable."
        _assert_msbs_equal(msd.files[stem], msb)


@pytest.mark.slow
@pytest.mark.parametrize("map_stem", [m.msb_file_stem for m in ALL_MAPS if m.msb_file_stem])
def test_vanilla_msb_binary_round_trip(map_studio_dir, map_stem, tmp_path, caplog):
    path = map_studio_dir / f"{map_stem}.msb"
    if not path.is_file():
        pytest.skip(f"Missing vanilla MSB: {path}")
    with caplog.at_level(logging.CRITICAL):
        msb = MSB.from_path(path)
        packed = bytes(msb)
        out_path = tmp_path / f"{map_stem}.msb"
        msb.write(out_path)
        reloaded = MSB.from_path(out_path)
    assert bytes(reloaded) == packed
    _assert_msbs_equal(msb, reloaded)


@pytest.mark.slow
@pytest.mark.parametrize("map_stem", [m.msb_file_stem for m in ALL_MAPS if m.msb_file_stem])
def test_vanilla_msb_json_round_trip(map_studio_dir, map_stem, tmp_path, caplog):
    path = map_studio_dir / f"{map_stem}.msb"
    if not path.is_file():
        pytest.skip(f"Missing vanilla MSB: {path}")
    with caplog.at_level(logging.CRITICAL):
        msb = MSB.from_path(path)
        json_path = tmp_path / f"{map_stem}.json"
        msb.write_json(json_path)
        reloaded = MSB.from_json(json_path)
    _assert_msbs_equal(msb, reloaded)
