"""Tests for DSR EzState talk scripts: `TalkESD`, `TalkESDBND`, and `TalkDirectory`.

The DSR-specific configuration lives in `darksouls1r/ezstate/`:

    - `TalkESD` uses ESD `VERSION = 1` and **64-bit varints** (`LONG_VARINTS = True`); PTDE uses 32-bit.
    - Loose `.esd` files are uncompressed (`dcx_type = DCXType.Null`), but the `.talkesdbnd` Binder that
      wraps them IS DCX-compressed.
    - `TalkESDBND.talk` maps talk IDs (e.g. `100613`) to `TalkESD` instances. Binder entries are NOT
      regenerated until `write()` calls `entry_autogen()`, so `len(bnd.entries)` is 0 after
      `from_esp_directory()` -- use `len(bnd.talk)`.
"""
from __future__ import annotations

import contextlib
import io
from pathlib import Path

import pytest

from soulstruct.dcx import DCXType
from soulstruct.darksouls1r.ezstate import ChrESD, TalkESD, TalkESDBND, TalkDirectory
from soulstruct.games import DARK_SOULS_DSR

ESD_NAME = "t100613.esd"
TALKESDBND_NAME = "m10_00_00_00.talkesdbnd.dcx"


@pytest.fixture
def esd_path(resource) -> Path:
    return resource(ESD_NAME)


@pytest.fixture
def talkesdbnd_path(resource) -> Path:
    return resource(TALKESDBND_NAME)


@pytest.fixture
def talkesdbnd(talkesdbnd_path) -> TalkESDBND:
    return TalkESDBND.from_path(talkesdbnd_path)


# ---------------------------------------------------------------------------
# Class configuration (pure unit, no game data)
# ---------------------------------------------------------------------------


def test_dsr_esd_uses_64_bit_varints_unlike_ptde():
    from soulstruct.darksouls1ptde.ezstate.esd.core import TalkESD as PTDE_TalkESD

    assert TalkESD.LONG_VARINTS is True
    assert TalkESD.VERSION == 1
    assert PTDE_TalkESD.LONG_VARINTS is False
    assert ChrESD.LONG_VARINTS is True


def test_loose_esd_is_uncompressed_but_binder_is_not():
    assert TalkESD()._get_dcx_type() == DCXType.Null
    assert TalkESDBND()._get_dcx_type() == DARK_SOULS_DSR.default_dcx_type
    assert TalkESDBND()._get_dcx_type() != DCXType.Null
    assert TalkESDBND.TALK_ESD_CLASS is TalkESD
    assert TalkESDBND.DEFAULT_ENTRY_ROOT.endswith("\\script\\talk")


def test_talk_directory_class_config():
    from soulstruct.darksouls1r.maps.constants import ALL_MAPS, COMMON

    assert TalkDirectory.FILE_CLASS is TalkESDBND
    # `COMMON` has no talk file, so it is excluded from `ALL_MAPS`.
    assert COMMON not in TalkDirectory.ALL_MAPS
    assert TalkDirectory.ALL_MAPS == ALL_MAPS[1:]


@pytest.mark.xfail(
    reason="API INCONSISTENCY: `TalkDirectory` excludes `COMMON` from `ALL_MAPS` (correctly -- there is "
           "no `common.talkesdbnd`) but still declares a `Common = map_property(COMMON)` attribute, "
           "which can never resolve (darksouls1r/ezstate/talk_directory.py:15 vs :19).",
    strict=False,
)
def test_talk_directory_common_property_is_not_declared():
    assert not hasattr(TalkDirectory, "Common")


# ---------------------------------------------------------------------------
# Loose `.esd` file
# ---------------------------------------------------------------------------


def test_talk_esd_read(esd_path):
    esd = TalkESD.from_path(esd_path)
    assert esd.esd_name == "t100613"
    assert esd.state_machines
    for state_machine in esd.state_machines.values():
        assert state_machine  # dict of states


def test_talk_esd_binary_roundtrip_preserves_state_machines(esd_path, tmp_path):
    esd = TalkESD.from_path(esd_path)
    esd.write(tmp_path / ESD_NAME)
    reload = TalkESD.from_path(tmp_path / ESD_NAME)
    assert list(reload.state_machines) == list(esd.state_machines)
    for sm_id, states in esd.state_machines.items():
        assert list(reload.state_machines[sm_id]) == list(states)
    assert reload.magic == esd.magic


@pytest.mark.xfail(
    reason="BUG: `ESD.to_writer()` writes `esd_name_length=len(self.esd_name) // 2`, but `esd_name` is a "
           "`str` (not encoded bytes), so 't100613' (7 chars) is written as 3 instead of the vanilla 8 "
           "(= character count + null terminator). Re-reading truncates the name to 't10061' "
           "(base/ezstate/esd/core.py:324 and :339).",
    strict=False,
)
def test_talk_esd_name_survives_roundtrip(esd_path):
    esd = TalkESD.from_path(esd_path)
    reload = TalkESD.from_bytes(bytes(esd))
    assert reload.esd_name == esd.esd_name


@pytest.mark.xfail(
    reason="BUG: same `esd_name_length` miscalculation means repacked ESDs differ from vanilla in 4 "
           "header fields (base/ezstate/esd/core.py:324, :339).",
    strict=False,
)
def test_talk_esd_repack_is_byte_identical(esd_path):
    esd = TalkESD.from_path(esd_path)
    assert bytes(esd) == esd_path.read_bytes()


def test_talk_esd_repack_is_idempotent_after_first_write(esd_path):
    """Second and subsequent repacks are stable (the name truncation converges)."""
    esd = TalkESD.from_path(esd_path)
    once = bytes(TalkESD.from_bytes(bytes(esd)))
    twice = bytes(TalkESD.from_bytes(once))
    assert twice == once


def test_talk_esd_esp_roundtrip(esd_path, tmp_path):
    esd = TalkESD.from_path(esd_path)
    esp_path = tmp_path / "t100613.esp.py"
    with contextlib.redirect_stdout(io.StringIO()):  # `Condition.to_esp()` has a stray debug `print`
        esd.write_esp_file(esp_path)
        reload = TalkESD.from_esp_file(esp_path)
    assert list(reload.state_machines) == list(esd.state_machines)
    for sm_id, states in esd.state_machines.items():
        assert list(reload.state_machines[sm_id]) == list(states)


def test_esp_export_does_not_print_to_stdout(esd_path, tmp_path, capsys):
    """`ESD.write_esp_file()` should be silent; a stray `print(s)` in `Condition.to_esp()` spams stdout."""
    esd = TalkESD.from_path(esd_path)
    esd.write_esp_file(tmp_path / "t100613.esp.py")
    captured = capsys.readouterr()
    if captured.out.strip():
        pytest.xfail(
            "BUG: `Condition.to_esp()` contains a leftover debug `print(s)` "
            "(base/ezstate/esd/condition.py:214), which dumps every decompiled condition to stdout "
            f"({len(captured.out)} chars for one ESD)."
        )


# ---------------------------------------------------------------------------
# `TalkESDBND`
# ---------------------------------------------------------------------------


def test_talkesdbnd_read(talkesdbnd):
    assert sorted(talkesdbnd.talk) == [100000, 100001, 100002, 100010, 100613, 100626, 100628]
    assert len(talkesdbnd.entries) == len(talkesdbnd.talk)
    assert isinstance(talkesdbnd.talk[100613], TalkESD)
    assert list(talkesdbnd) == list(talkesdbnd.talk)


def test_talkesdbnd_binary_roundtrip(talkesdbnd, tmp_path):
    talkesdbnd.write(tmp_path / TALKESDBND_NAME)
    reload = TalkESDBND.from_path(tmp_path / TALKESDBND_NAME)
    assert sorted(reload.talk) == sorted(talkesdbnd.talk)
    for talk_id, esd in talkesdbnd.talk.items():
        assert list(reload.talk[talk_id].state_machines) == list(esd.state_machines)


def test_talkesdbnd_entry_names_match_talk_ids(talkesdbnd):
    assert sorted(e.name for e in talkesdbnd.entries) == sorted(f"t{tid}.esd" for tid in talkesdbnd.talk)


def test_talkesdbnd_esp_directory_roundtrip(talkesdbnd, tmp_path):
    """`from_esp_directory()` deliberately does NOT create Binder entries until `write()`."""
    esp_dir = tmp_path / "esp"
    with contextlib.redirect_stdout(io.StringIO()):
        talkesdbnd.write_esp_directory(esp_dir)
        reload = TalkESDBND.from_esp_directory(esp_dir)
    assert sorted(p.name for p in esp_dir.iterdir()) == sorted(f"t{tid}.esp.py" for tid in talkesdbnd.talk)
    assert sorted(reload.talk) == sorted(talkesdbnd.talk)
    assert len(reload.entries) == 0, "Entries are only regenerated on `write()` (`entry_autogen`)."

    with contextlib.redirect_stdout(io.StringIO()):
        reload.write(tmp_path / TALKESDBND_NAME)
    rewritten = TalkESDBND.from_path(tmp_path / TALKESDBND_NAME)
    assert sorted(rewritten.talk) == sorted(talkesdbnd.talk)
    assert len(rewritten.entries) == len(talkesdbnd.talk)


# ---------------------------------------------------------------------------
# `TalkDirectory` (requires DSR install)
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.game_data
def test_talk_directory_roundtrip(dsr_root, tmp_path):
    talk_dir = TalkDirectory.from_path(dsr_root / "script/talk")
    assert talk_dir.files
    assert talk_dir.Depths is talk_dir.files["m10_00_00_00"]
    assert 100010 in talk_dir.Depths.talk

    talk_dir.write(tmp_path / "talk")
    written = sorted(p.name for p in (tmp_path / "talk").iterdir())
    assert all(name.endswith(".talkesdbnd.dcx") for name in written), written

    reload = TalkDirectory.from_path(tmp_path / "talk")
    assert sorted(reload.files) == sorted(talk_dir.files)
    for stem, source in talk_dir.files.items():
        assert sorted(reload.files[stem].talk) == sorted(source.talk)


@pytest.mark.slow
@pytest.mark.game_data
def test_talk_directory_esp_roundtrip(dsr_root, tmp_path):
    talk_dir = TalkDirectory.from_path(dsr_root / "script/talk")
    with contextlib.redirect_stdout(io.StringIO()):
        talk_dir.write_esp_directory(tmp_path / "talk_esp")
        reload = TalkDirectory.from_path(tmp_path / "talk_esp")
    assert sorted(reload.files) == sorted(talk_dir.files)
    for stem, source in talk_dir.files.items():
        assert sorted(reload.files[stem].talk) == sorted(source.talk)
