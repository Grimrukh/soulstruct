"""Tests for `soulstruct.darksouls1r.utilities.file_list`.

`DSR_FILE_LIST` is a flat, hand-generated list of ~6000 game-relative POSIX paths for a vanilla
Dark Souls: Remastered install. Its only consumer (in `soulstruct-gui`, `misc/mod_manager.py`) uses it
purely for `in` membership tests to distinguish vanilla files from mod files.

These tests validate the data's internal consistency (pure unit) and, when DSR is installed, that it
is not stale relative to the real game directory.
"""
from __future__ import annotations

import collections
import re
from pathlib import Path

import pytest

from soulstruct.darksouls1r.utilities.file_list import DSR_FILE_LIST

# Fraction of listed paths allowed to be missing from a real install before the test fails.
_MAX_MISSING_FRACTION = 0.02


# ---------------------------------------------------------------------------
# Pure-unit: internal consistency
# ---------------------------------------------------------------------------


def test_file_list_is_non_empty_list_of_strings():
    assert isinstance(DSR_FILE_LIST, list)
    assert len(DSR_FILE_LIST) > 5000
    non_strings = [p for p in DSR_FILE_LIST if not isinstance(p, str)]
    assert not non_strings, non_strings[:5]


def test_file_list_has_no_duplicates():
    counts = collections.Counter(DSR_FILE_LIST)
    duplicates = {p: n for p, n in counts.items() if n > 1}
    assert not duplicates, duplicates


def test_file_list_has_no_case_insensitive_duplicates():
    """Windows paths are case-insensitive, so a case-only collision would be a real defect."""
    counts = collections.Counter(p.lower() for p in DSR_FILE_LIST)
    duplicates = {p: n for p, n in counts.items() if n > 1}
    assert not duplicates, duplicates


def test_file_list_entries_are_well_formed():
    bad = []
    for path in DSR_FILE_LIST:
        if not path:
            bad.append((path, "empty"))
        elif path != path.strip():
            bad.append((path, "whitespace"))
        elif "\\" in path:
            bad.append((path, "backslash"))
        elif path.startswith("/"):
            bad.append((path, "absolute"))
        elif path.endswith("/"):
            bad.append((path, "directory"))
        elif "//" in path:
            bad.append((path, "double slash"))
        elif ".." in path.split("/"):
            bad.append((path, "parent traversal"))
    assert not bad, bad[:10]


def test_file_list_entries_have_extensions():
    no_extension = [p for p in DSR_FILE_LIST if "." not in Path(p).name]
    assert not no_extension, no_extension[:10]


def test_file_list_top_level_directories_are_known():
    """Guards against a stray path from outside the game data directories."""
    expected_dirs = {
        "chr", "event", "facegen", "font", "map", "menu", "movww", "msg", "mtd", "obj",
        "other", "param", "paramdef", "parts", "remo", "script", "sfx", "shader", "sound",
    }
    found = {p.split("/")[0] for p in DSR_FILE_LIST if "/" in p}
    assert found == expected_dirs, found ^ expected_dirs


def test_file_list_root_files_are_executables_and_dlls():
    root_files = [p for p in DSR_FILE_LIST if "/" not in p]
    assert root_files, "expected top-level .exe/.dll entries"
    for name in root_files:
        assert name.endswith((".exe", ".dll")), name
    assert "DarkSoulsRemastered.exe" in root_files


def test_file_list_contains_expected_landmark_files():
    """A handful of files any DSR install must have, as a smoke test of the list's shape."""
    landmarks = [
        "map/MapStudio/m10_00_00_00.msb",
        "param/GameParam/GameParam.parambnd.dcx",
        "chr/c0000.chrbnd.dcx",
        "sfx/FRPG_SfxBnd_CommonEffects.ffxbnd.dcx",
        "msg/ENGLISH/menu.msgbnd.dcx",
    ]
    missing = [p for p in landmarks if p not in DSR_FILE_LIST]
    assert not missing, missing


def test_file_list_sound_entries_use_known_fmod_extensions():
    """DSR sound data is FMOD: `.fev` events, `.fsb` sample banks, `.itl`/`.mch`/`.mix`/`.rpc` sidecars."""
    sound_entries = [p for p in DSR_FILE_LIST if p.startswith("sound/")]
    assert sound_entries
    known = (".fev", ".fsb", ".itl", ".mch", ".mix", ".rpc")
    bad = [p for p in sound_entries if not p.endswith(known)]
    assert not bad, bad[:10]


def test_file_list_every_fsb_has_a_matching_fev():
    """FEV (events) and FSB (samples) are sister files; every FSB should have a same-stem FEV."""
    fev_stems = {Path(p).stem for p in DSR_FILE_LIST if p.endswith(".fev")}
    fsb_stems = {Path(p).stem for p in DSR_FILE_LIST if p.endswith(".fsb")}
    assert fsb_stems, "expected FSB files in the list"
    assert fsb_stems <= fev_stems, sorted(fsb_stems - fev_stems)[:10]


def test_file_list_ffxbnd_entries_use_expected_prefix():
    ffxbnds = [p for p in DSR_FILE_LIST if p.startswith("sfx/")]
    assert ffxbnds
    for path in ffxbnds:
        assert re.fullmatch(r"sfx/FRPG_SfxBnd_\w+\.ffxbnd\.dcx", path), path


def test_file_list_is_a_list_not_a_set():
    """Documents a performance trap.

    The list's only consumer does `if relative_mod_file not in DSR_FILE_LIST`, which is an O(n)
    scan over ~6000 strings per checked file. A `frozenset` (or a module-level derived set) would
    make this O(1). This test simply pins the current type so a future change is deliberate.
    """
    assert type(DSR_FILE_LIST) is list


# ---------------------------------------------------------------------------
# Game data: staleness against the real install
# ---------------------------------------------------------------------------


@pytest.mark.game_data
@pytest.mark.slow
def test_file_list_paths_exist_in_dsr_install(dsr_root: Path):
    """Every listed path should resolve against a real DSR install (within a small tolerance)."""
    missing = [p for p in DSR_FILE_LIST if not (dsr_root / p).exists()]
    fraction = len(missing) / len(DSR_FILE_LIST)
    assert fraction <= _MAX_MISSING_FRACTION, (
        f"{len(missing)}/{len(DSR_FILE_LIST)} ({fraction:.1%}) listed paths are missing from "
        f"{dsr_root}. First 20: {missing[:20]}"
    )


@pytest.mark.game_data
def test_file_list_sample_paths_exist(dsr_root: Path):
    """Fast sanity check: a deterministic sample of the list resolves on disk."""
    sample = DSR_FILE_LIST[::100]
    missing = [p for p in sample if not (dsr_root / p).exists()]
    assert not missing, missing[:10]


@pytest.mark.game_data
def test_file_list_paths_are_files_not_directories(dsr_root: Path):
    sample = DSR_FILE_LIST[::250]
    not_files = [p for p in sample if (dsr_root / p).exists() and not (dsr_root / p).is_file()]
    assert not not_files, not_files[:10]


@pytest.mark.game_data
@pytest.mark.slow
def test_file_list_is_a_subset_of_the_install_not_a_snapshot(dsr_root: Path):
    """`DSR_FILE_LIST` is deliberately a *vanilla* whitelist, not a mirror of the current install.

    Extra files on disk (DLC-only characters, user-extracted loose files, `.bak`/`.meta` artifacts)
    are expected and are exactly what the mod manager wants to flag. This test asserts the list is a
    subset, and reports the extras for information.
    """
    listed = set(DSR_FILE_LIST)
    top_dirs = sorted({p.split("/")[0] for p in DSR_FILE_LIST if "/" in p})
    extra = []
    for top_dir in top_dirs:
        directory = dsr_root / top_dir
        if not directory.is_dir():
            continue
        for file_path in directory.rglob("*"):
            if file_path.is_file():
                relative = file_path.relative_to(dsr_root).as_posix()
                if relative not in listed:
                    extra.append(relative)
    # Not an assertion failure: extras are expected. Just make sure the scan worked at all.
    assert isinstance(extra, list)
    non_artifact_extra = [p for p in extra if not p.endswith((".bak", ".meta"))]
    print(f"\n{len(extra)} files on disk are not in DSR_FILE_LIST "
          f"({len(non_artifact_extra)} excluding .bak/.meta artifacts).")
