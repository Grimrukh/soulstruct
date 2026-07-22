"""Tests for `soulstruct.eldenring.events.EventDirectory`, the all-maps EMEVD manager.

`EventDirectory` is a `GameFileMapDirectory` that maps a map stem (e.g. `m10_00_00_00`) to an `EMEVD`. It
also exposes ~880 generated `map_property` accessors (`.StormveilCastle`, `.CommonFunc`, ...).

Elden Ring is the stress case: `ALL_MAPS` has 876 entries, but only ~96 of them actually have an EMEVD file
(`emevd_file_stem is not None`); the rest are open-world tiles whose events live in their parent map.
"""
from __future__ import annotations

import shutil

import pytest

from soulstruct.eldenring.events import EventDirectory
from soulstruct.eldenring.events.emevd import EMEVD
from soulstruct.eldenring.maps.constants import (
    ALL_MAPS,
    COMMON,
    COMMON_FUNC,
    STORMVEIL_CASTLE,
    get_map,
)

RESOURCE_NAME = "m10_00_00_00.emevd.dcx"


@pytest.fixture
def m10_emevd(resource) -> EMEVD:
    return EMEVD.from_path(resource(RESOURCE_NAME))


@pytest.fixture
def m10_directory(m10_emevd) -> EventDirectory:
    """`EventDirectory` built in memory, bypassing `from_path` (which is broken for ER; see below)."""
    return EventDirectory(files={"m10_00_00_00": m10_emevd})


# ---------------------------------------------------------------------------
# Class configuration
# ---------------------------------------------------------------------------


def test_event_directory_configuration():
    assert EventDirectory.FILE_CLASS is EMEVD
    assert EventDirectory.FILE_EXTENSION == ".emevd"
    assert EventDirectory.MAP_STEM_ATTRIBUTE == "emevd_file_stem"
    assert EventDirectory.COMMON_FUNC is COMMON_FUNC
    assert EventDirectory.ALL_MAPS is ALL_MAPS
    assert EventDirectory.GET_MAP is get_map
    # Accepts binary EMEVD, EVS scripts and numeric text.
    assert EventDirectory.FILE_NAME_PATTERN == r".*\.(evs\.py|evs|py|emevd|txt)"


def test_common_and_common_func_have_map_properties():
    """ER leans on `common_func.emevd` heavily, so both 'common' files need first-class accessors."""
    assert isinstance(EventDirectory.__dict__["Common"], property)
    assert isinstance(EventDirectory.__dict__["CommonFunc"], property)
    assert COMMON.emevd_file_stem == "common"
    assert COMMON_FUNC.emevd_file_stem == "common_func"


def test_most_er_maps_have_no_emevd_stem():
    """Documents the ER-specific invariant that breaks `from_path` (see xfail tests below)."""
    stems = [game_map.emevd_file_stem for game_map in ALL_MAPS]
    assert len(stems) > 800
    assert stems.count(None) > 700, "Expected most ER open-world tiles to have no EMEVD of their own."
    real_stems = [stem for stem in stems if stem is not None]
    assert len(set(real_stems)) == len(real_stems), "EMEVD stems must be unique."
    assert "common" in real_stems


def test_common_func_is_not_in_all_maps():
    """`EventDirectory.from_path` appends COMMON_FUNC's stem separately; ALL_MAPS must not contain it."""
    stems = [game_map.emevd_file_stem for game_map in ALL_MAPS]
    assert COMMON_FUNC.emevd_file_stem not in stems
    assert COMMON.emevd_file_stem in stems


@pytest.mark.xfail(
    reason="`Map.__eq__` compares only `(area_id, block_id)` while `Map.__hash__` uses `msb_file_stem`, so "
           "the hash/eq contract is violated AND ER's 4-part map IDs are conflated: 876 ER maps collapse to "
           "165 'equal' groups, e.g. SouthwestLiurnia_SW_SE == SouthwestLiurnia_SW_NE, and "
           "COMMON == COMMON_FUNC. Any `map in ALL_MAPS` / `set(maps)` check is unreliable.",
    strict=False,
)
def test_map_equality_distinguishes_er_maps():
    assert COMMON != COMMON_FUNC
    overworld = [game_map for game_map in ALL_MAPS if game_map.area_id == 60][:2]
    assert overworld[0] != overworld[1]
    # Objects that compare equal must hash equally.
    equal_but_unequal_hash = [
        (a, b) for a in ALL_MAPS[:200] for b in ALL_MAPS[:200] if a == b and hash(a) != hash(b)
    ]
    assert not equal_but_unequal_hash


# ---------------------------------------------------------------------------
# In-memory access API
# ---------------------------------------------------------------------------


def test_map_property_access(m10_directory, m10_emevd):
    assert m10_directory.StormveilCastle is m10_emevd


def test_getitem_accepts_stem_and_map_constant(m10_directory, m10_emevd):
    assert m10_directory["m10_00_00_00"] is m10_emevd
    assert m10_directory[STORMVEIL_CASTLE] is m10_emevd


def test_getitem_raises_key_error_for_absent_map(m10_directory):
    with pytest.raises(KeyError):
        _ = m10_directory[COMMON_FUNC]
    with pytest.raises(KeyError):
        _ = m10_directory.RoundtableHold


def test_mapping_helpers(m10_directory, m10_emevd):
    assert list(m10_directory.keys()) == ["m10_00_00_00"]
    assert list(m10_directory.values()) == [m10_emevd]
    assert list(m10_directory.items()) == [("m10_00_00_00", m10_emevd)]


@pytest.mark.xfail(
    reason="`GameFileMapDirectory.__repr__` (a concise `<N files>` summary) is dead code: the "
           "`PathDataclassMeta` dataclass decorator regenerates `__repr__`, so `repr(EventDirectory)` dumps "
           "every event and instruction of every map -- megabytes of text in a debugger or REPL.",
    strict=False,
)
def test_repr_is_concise(m10_directory):
    text = repr(m10_directory)
    assert len(text) < 200, f"repr is {len(text)} characters long"
    assert "1 files" in text


def test_write_without_directory_raises(m10_directory):
    assert m10_directory.directory is None
    with pytest.raises(ValueError):
        m10_directory.write()


def test_write_evs_without_directory_raises(m10_directory):
    with pytest.raises(ValueError):
        m10_directory.write_evs()


# ---------------------------------------------------------------------------
# Directory I/O
# ---------------------------------------------------------------------------


def test_from_path_rejects_missing_directory(tmp_path):
    with pytest.raises(NotADirectoryError):
        EventDirectory.from_path(tmp_path / "does_not_exist")


@pytest.mark.xfail(
    reason="`EventDirectory.from_path` ALWAYS raises TypeError for Elden Ring: the final "
           "\"Could not find some files\" warning does `', '.join(all_map_stems)`, and ~780 ER maps have "
           "`emevd_file_stem is None`. The public all-maps read API is unusable.",
    strict=False,
)
def test_from_path_reads_a_map_directory(resource, tmp_path):
    shutil.copy(resource(RESOURCE_NAME), tmp_path / RESOURCE_NAME)
    directory = EventDirectory.from_path(tmp_path)
    assert set(directory.keys()) == {"m10_00_00_00"}
    assert isinstance(directory.StormveilCastle, EMEVD)
    assert directory.directory == tmp_path


@pytest.mark.xfail(
    reason="Same `', '.join(all_map_stems)` bug in `GameFileMapDirectory.write` "
           "(`base/game_file_directory.py:206`): writing an ER `EventDirectory` also raises TypeError.",
    strict=False,
)
def test_write_directory(m10_emevd, tmp_path):
    directory = EventDirectory(files={"m10_00_00_00": m10_emevd})
    written = directory.write(tmp_path)
    assert written
    assert (tmp_path / "m10_00_00_00.emevd.dcx").is_file()


def test_from_path_ignores_unrecognised_files(resource, tmp_path, caplog):
    """Stray files (backups, scratch scripts) must be skipped, not read as EMEVD."""
    shutil.copy(resource(RESOURCE_NAME), tmp_path / RESOURCE_NAME)
    (tmp_path / "_scratch.emevd").write_bytes(b"not an emevd")
    (tmp_path / "notes.md").write_text("ignored")
    try:
        directory = EventDirectory.from_path(tmp_path)
    except TypeError:
        pytest.xfail("`from_path` is broken for ER (see `test_from_path_reads_a_map_directory`).")
    assert "_scratch" not in directory.keys()
    assert "notes" not in directory.keys()


# ---------------------------------------------------------------------------
# Live game data
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.game_data
@pytest.mark.xfail(
    reason="Same `', '.join(all_map_stems)` TypeError as `test_from_path_reads_a_map_directory`; reading "
           "the real ER `event/` directory is impossible via the public API.",
    strict=False,
)
def test_live_event_directory_reads_every_map(er_root):
    directory = EventDirectory.from_path(er_root / "event")
    assert len(directory.files) > 90
    assert isinstance(directory.CommonFunc, EMEVD)
    assert isinstance(directory.Common, EMEVD)
    assert isinstance(directory.StormveilCastle, EMEVD)
    # Every loaded stem must correspond to a real ER map with an EMEVD.
    real_stems = {m.emevd_file_stem for m in ALL_MAPS if m.emevd_file_stem}
    real_stems.add(COMMON_FUNC.emevd_file_stem)
    assert set(directory.keys()) <= real_stems


@pytest.mark.slow
@pytest.mark.game_data
def test_live_event_directory_files_are_all_readable(er_root):
    """Fallback for the broken `from_path`: read every ER EMEVD individually and check basic invariants.

    This is what `EventDirectory.from_path` would do if it did not crash.
    """
    read_count = 0
    non_empty = 0
    for path in sorted((er_root / "event").glob("*.emevd.dcx")):
        stem = path.name.split(".")[0]
        emevd = EMEVD.from_path(path)
        assert emevd.map_name == stem
        # NOTE: many open-world tile EMEVDs are legitimately empty.
        non_empty += bool(emevd.events)
        read_count += 1
    assert read_count > 400
    assert non_empty > 50


@pytest.mark.game_data
@pytest.mark.xfail(
    reason="`eldenring/maps/constants.py` gives `emevd_file_stem = None` to every open-world tile, but the "
           "game ships a real EMEVD for each of them (plus `m11_71_00_00` and a bare `m60`). ~370 of the "
           "449 ER EMEVD files therefore have no map constant, so `EventDirectory` would silently skip "
           "them ('unrecognized map stem') and never write them back.",
    strict=False,
)
def test_all_live_emevd_files_have_a_map_constant(er_root):
    known_stems = {m.emevd_file_stem for m in ALL_MAPS if m.emevd_file_stem}
    known_stems.add(COMMON_FUNC.emevd_file_stem)  # not in `ALL_MAPS`; handled separately by `EventDirectory`
    unknown = sorted(
        path.name.split(".")[0]
        for path in (er_root / "event").glob("*.emevd.dcx")
        if path.name.split(".")[0] not in known_stems
    )
    assert not unknown, f"{len(unknown)} ER EMEVD files have no map constant, e.g. {unknown[:5]}"
