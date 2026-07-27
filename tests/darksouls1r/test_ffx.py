"""Tests for `soulstruct.darksouls1r.ffx` (FFXBND particle/visual-effect containers).

`FFXBND` is a thin `Binder` subclass. There is NO FFX file parsing in Soulstruct: `ffx/core.py`
contains only a module docstring pointing users at Meowmaritus's FXMLR tool. The only real logic
is `entry_autogen()` (entry renaming/renumbering) and `support_msb()` (FFX dependency gathering).
"""
from __future__ import annotations

import typing as tp

import pytest

from soulstruct.containers import Binder, BinderEntry, BinderVersion
from soulstruct.darksouls1r.ffx import FFXBND
from soulstruct.darksouls1r.ffx import core as ffx_core
from soulstruct.darksouls1r.ffx.ffxbnd import (
    DEFAULT_CHARACTER_FFX_SOURCES,
    DEFAULT_REQUIRED_FFX_IDS,
    _BLOCK_FFXBND_RE,
    _FFX_STEM_MATCH,
    _FLVER_STEM_MATCH,
    _TPF_STEM_MATCH,
)

FFX_DIR = "N:\\FRPG\\data\\Sfx\\OutputData\\Main\\Effect_x64"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _entry(name: str, data: bytes = b"\x00", entry_id: int | None = None) -> BinderEntry:
    return BinderEntry(data=data, entry_id=entry_id, path=f"{FFX_DIR}\\{name}", flags=0x2)


def _ffxbnd(*names: str) -> FFXBND:
    ffxbnd = FFXBND()
    for i, name in enumerate(names):
        ffxbnd.add_entry(_entry(name, data=bytes([i % 251]) * 4, entry_id=i))
    return ffxbnd


# ---------------------------------------------------------------------------
# Module shape / dead code
# ---------------------------------------------------------------------------


def test_ffx_core_module_is_a_stub():
    """`ffx/core.py` defines nothing: FFX files themselves are NOT parsed by Soulstruct."""
    public = [name for name in vars(ffx_core) if not name.startswith("__")]
    assert public == [], f"`ffx/core.py` unexpectedly defines: {public}"
    assert "FXMLR" in ffx_core.__doc__


def test_ffxbnd_is_a_binder_subclass():
    assert issubclass(FFXBND, Binder)
    assert FFXBND.EXT == ".ffxbnd"
    assert FFXBND.NAME_PREFIX == "FRPG_SfxBnd_"


def test_block_ffxbnd_regex_is_unused_dead_code():
    """`_BLOCK_FFXBND_RE` is defined but referenced nowhere in the module."""
    import inspect

    from soulstruct.darksouls1r.ffx import ffxbnd as ffxbnd_module

    source = inspect.getsource(ffxbnd_module)
    assert source.count("_BLOCK_FFXBND_RE") == 1, "regex is now used; update this test"
    # Still assert it behaves as documented, in case it is ever wired up.
    assert _BLOCK_FFXBND_RE.search("FRPG_SfxBnd_m10_01.ffxbnd.dcx")
    assert not _BLOCK_FFXBND_RE.search("FRPG_SfxBnd_m10.ffxbnd.dcx")


# ---------------------------------------------------------------------------
# Stem regexes
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("stem", ["f0000472", "f1", "f1234567"])
def test_ffx_stem_match(stem):
    assert _FFX_STEM_MATCH.match(stem)


@pytest.mark.parametrize("stem", ["s15221", "s00020"])
def test_flver_stem_match(stem):
    assert _FLVER_STEM_MATCH.match(stem)


@pytest.mark.parametrize("stem", ["s15221", "s15221_n", "s15221_s", "s15221_h"])
def test_tpf_stem_match(stem):
    assert _TPF_STEM_MATCH.match(stem)


def test_stem_regexes_are_not_anchored_at_end():
    """These patterns use `.match`, not `.fullmatch`, so they accept trailing junk."""
    assert _FFX_STEM_MATCH.match("f0000472_garbage")
    assert _TPF_STEM_MATCH.match("s15221_zzz")


# ---------------------------------------------------------------------------
# entry_autogen
# ---------------------------------------------------------------------------


def test_entry_autogen_assigns_id_ranges_and_sorts():
    ffxbnd = _ffxbnd(
        "s00020.tpf", "f0000540.ffx", "s15223.flver", "f0000472.ffx", "s00006.tpf", "s15222.flver",
    )
    ffxbnd.entry_autogen()
    assert [(e.entry_id, e.name) for e in ffxbnd.entries] == [
        (0, "f0000472.ffx"),
        (1, "f0000540.ffx"),
        (100000, "s00006.tpf"),
        (100001, "s00020.tpf"),
        (200000, "s15222.flver"),
        (200001, "s15223.flver"),
    ]


def test_entry_autogen_zero_pads_names():
    ffxbnd = _ffxbnd("f472.ffx", "s20.tpf", "s15223.flver")
    ffxbnd.entry_autogen()
    assert [e.name for e in ffxbnd.entries] == ["f0000472.ffx", "s00020.tpf", "s15223.flver"]


def test_entry_autogen_strips_unknown_suffixes():
    ffxbnd = _ffxbnd("f0000472_MyEdit.ffx", "s15223_MyEdit.flver")
    ffxbnd.entry_autogen()
    assert [e.name for e in ffxbnd.entries] == ["f0000472.ffx", "s15223.flver"]


@pytest.mark.parametrize("suffix", ["n", "s", "h"])
def test_entry_autogen_preserves_known_tpf_suffixes(suffix):
    ffxbnd = _ffxbnd(f"s15221_{suffix}.tpf")
    ffxbnd.entry_autogen()
    assert ffxbnd.entries[0].name == f"s15221_{suffix}.tpf"


def test_entry_autogen_strips_extra_suffix_after_known_tpf_suffix():
    ffxbnd = _ffxbnd("s15221_n_MyInfo.tpf")
    ffxbnd.entry_autogen()
    assert ffxbnd.entries[0].name == "s15221_n.tpf"


def test_entry_autogen_strips_unknown_tpf_suffix():
    ffxbnd = _ffxbnd("s15221_MyInfo.tpf")
    ffxbnd.entry_autogen()
    assert ffxbnd.entries[0].name == "s15221.tpf"


def test_entry_autogen_rejects_foreign_extension():
    ffxbnd = _ffxbnd("f0000472.ffx")
    ffxbnd.add_entry(_entry("something.dds", entry_id=999))
    with pytest.raises(ValueError, match="invalid extension"):
        ffxbnd.entry_autogen()


def test_entry_autogen_rejects_bad_ffx_stem():
    ffxbnd = _ffxbnd("x0000472.ffx")
    with pytest.raises((ValueError, AttributeError)):
        ffxbnd.entry_autogen()


def test_entry_autogen_is_idempotent():
    ffxbnd = _ffxbnd("s00020.tpf", "f472.ffx", "s15223.flver", "s15221_n.tpf")
    ffxbnd.entry_autogen()
    first = [(e.entry_id, e.name) for e in ffxbnd.entries]
    ffxbnd.entry_autogen()
    assert [(e.entry_id, e.name) for e in ffxbnd.entries] == first


def test_entry_autogen_keeps_entry_data():
    ffxbnd = _ffxbnd("s00020.tpf", "f472.ffx")
    data_by_name = {e.name.split("_")[0]: e.data for e in ffxbnd.entries}
    ffxbnd.entry_autogen()
    for entry in ffxbnd.entries:
        stem_prefix = entry.name[0]
        assert entry.data in data_by_name.values(), stem_prefix


def test_entry_autogen_directory_is_preserved():
    ffxbnd = _ffxbnd("f472.ffx")
    ffxbnd.entry_autogen()
    assert ffxbnd.entries[0].path.startswith(FFX_DIR)


# ---------------------------------------------------------------------------
# Entry lookup helpers
# ---------------------------------------------------------------------------


def test_get_entries_partition_by_id_range():
    ffxbnd = _ffxbnd("f0000472.ffx", "s00020.tpf", "s15223.flver")
    ffxbnd.entry_autogen()
    assert [e.name for e in ffxbnd.get_ffx_entries()] == ["f0000472.ffx"]
    assert [e.name for e in ffxbnd.get_tpf_entries()] == ["s00020.tpf"]
    assert [e.name for e in ffxbnd.get_flver_entries()] == ["s15223.flver"]


def test_get_entries_by_id_maps():
    ffxbnd = _ffxbnd("f0000472.ffx", "s00020.tpf", "s15223.flver")
    ffxbnd.entry_autogen()
    assert set(ffxbnd.get_ffx_entries_by_ffx_id()) == {472}
    assert set(ffxbnd.get_tpf_entries_by_tpf_id_and_suffix()) == {(20, "")}
    assert set(ffxbnd.get_flver_entries_by_flver_id()) == {15223}


def test_get_tpf_entries_by_tpf_id_handles_suffixed_names():
    ffxbnd = _ffxbnd("s15221.tpf", "s15221_n.tpf", "s15221_s.tpf")
    ffxbnd.entry_autogen()
    by_id_and_suffix = ffxbnd.get_tpf_entries_by_tpf_id_and_suffix()
    assert sorted(by_id_and_suffix.keys()) == [(15221, ""), (15221, "n"), (15221, "s")]


def test_get_ffx_entries_uses_id_range_not_extension():
    """The partition helpers trust `entry_id` ranges, NOT file extensions.

    A TPF added without running `entry_autogen()` first is therefore reported as an FFX.
    """
    ffxbnd = FFXBND(version=BinderVersion.V3)
    ffxbnd.add_entry(_entry("s00020.tpf", entry_id=5))
    assert [e.name for e in ffxbnd.get_ffx_entries()] == ["s00020.tpf"]
    assert ffxbnd.get_tpf_entries() == []


# ---------------------------------------------------------------------------
# Static FFX dependency tables
# ---------------------------------------------------------------------------


def test_required_ffx_ids_and_sources_cover_the_same_characters():
    assert set(DEFAULT_REQUIRED_FFX_IDS) == set(DEFAULT_CHARACTER_FFX_SOURCES)


def test_every_required_ffx_id_has_a_known_source():
    missing = {
        chr_id: [i for i in ids if i not in DEFAULT_CHARACTER_FFX_SOURCES[chr_id]]
        for chr_id, ids in DEFAULT_REQUIRED_FFX_IDS.items()
    }
    missing = {k: v for k, v in missing.items() if v}
    assert not missing, missing


def test_every_source_ffx_id_is_actually_required():
    extra = {
        chr_id: [i for i in sources if i not in DEFAULT_REQUIRED_FFX_IDS[chr_id]]
        for chr_id, sources in DEFAULT_CHARACTER_FFX_SOURCES.items()
    }
    extra = {k: v for k, v in extra.items() if v}
    assert not extra, extra


def test_required_ffx_id_lists_have_no_duplicates():
    dupes = {c: ids for c, ids in DEFAULT_REQUIRED_FFX_IDS.items() if len(set(ids)) != len(ids)}
    assert not dupes, dupes


def test_ffx_source_names_use_expected_prefix():
    for chr_id, sources in DEFAULT_CHARACTER_FFX_SOURCES.items():
        for ffx_id, stem in sources.items():
            assert stem.startswith(FFXBND.NAME_PREFIX), (chr_id, ffx_id, stem)


def test_required_ffx_id_keys_look_like_character_model_ids():
    for chr_id in DEFAULT_REQUIRED_FFX_IDS:
        assert isinstance(chr_id, int)
        assert 0 <= chr_id <= 9999, chr_id


# ---------------------------------------------------------------------------
# support_msb
# ---------------------------------------------------------------------------


class _FakeCharacter:
    def __init__(self, name: str):
        self.name = name


class _FakeMSB:
    def __init__(self, *names: str):
        self.characters = [_FakeCharacter(n) for n in names]


def test_support_msb_requires_search_directories():
    ffxbnd = _ffxbnd("f0000472.ffx")
    with pytest.raises(ValueError, match="No FFX search directories"):
        ffxbnd.support_msb(_FakeMSB("c2230"), [])


def test_support_msb_uses_per_character_required_ids(tmp_path):
    """A character whose required-FFX list is empty must need no lookups at all."""
    ffxbnd = _ffxbnd("f0000472.ffx")
    ffxbnd.entry_autogen()
    # Character 2210 has an EMPTY required list, so this should be a no-op.
    assert DEFAULT_REQUIRED_FFX_IDS[2210] == []
    ffxbnd.support_msb(_FakeMSB("c2210"), [tmp_path])
    assert [e.name for e in ffxbnd.entries] == ["f0000472.ffx"]


def test_support_msb_finds_loose_ffx_file(tmp_path):
    """`find_ffx_id` step 2: loose `f*.ffx` files in a search directory."""
    ffxbnd = _ffxbnd("f0000472.ffx")
    ffxbnd.entry_autogen()
    assert DEFAULT_REQUIRED_FFX_IDS[2500] == [12500]
    # Write loose FFX 12500 required by c2500.
    (tmp_path / f"f{12500:07d}.ffx").write_bytes(b"FFX\x00")
    ffxbnd.support_msb(_FakeMSB("c2500"), tmp_path)
    ffx_names = {e.name for e in ffxbnd.entries}
    assert "f0000472.ffx" in ffx_names
    assert "f0012500.ffx" in ffx_names
    assert len(ffx_names) == 2, "loose FFX files should have been added as new entries"


def test_support_msb_accepts_single_path_not_only_sequence(tmp_path):
    ffxbnd = _ffxbnd("f0000472.ffx")
    ffxbnd.entry_autogen()
    for chr_id in DEFAULT_REQUIRED_FFX_IDS:
        (tmp_path / f"f{chr_id:07d}.ffx").write_bytes(b"FFX\x00")
    # `str` and `Path` must both be wrapped into a list.
    ffxbnd.support_msb(_FakeMSB("c2210"), str(tmp_path))


def test_support_msb_returns_none_and_sorts(tmp_path):
    """`support_msb` returns nothing and does NOT call `entry_autogen()`.

    New entries are appended with `entry_id = len(get_ffx_entries())`, so entry IDs end up in
    insertion order rather than sorted FFX-ID order. Callers must run `entry_autogen()` (or just
    `write()`, which calls it) themselves.
    """
    ffxbnd = _ffxbnd("f0099999.ffx")
    ffxbnd.entry_autogen()
    assert DEFAULT_REQUIRED_FFX_IDS[2500] == [12500]
    # Write loose FFX 12500 required by c2500.
    (tmp_path / f"f{12500:07d}.ffx").write_bytes(b"FFX\x00")
    result = ffxbnd.support_msb(_FakeMSB("c2500"), tmp_path, sort_entries=True)  # should add f0012500.ffx
    assert result is None
    names = [e.name for e in ffxbnd.entries]
    assert names == ["f0012500.ffx", "f0099999.ffx"], (
        "`support_msb` did not re-sort entries."
    )


# ---------------------------------------------------------------------------
# Game data
# ---------------------------------------------------------------------------


def _sfx_dir(dsr_root):
    sfx_dir = dsr_root / "sfx"
    if not sfx_dir.is_dir():
        pytest.skip(f"No `sfx` directory in DSR install: {sfx_dir}")
    return sfx_dir


def _small_ffxbnd_path(dsr_root):
    """Smallest FFXBND in the DSR install (avoids the 67 MB 'CommonEffects' bank)."""
    sfx_dir = _sfx_dir(dsr_root)
    paths = sorted(sfx_dir.glob("FRPG_SfxBnd_*.ffxbnd.dcx"), key=lambda p: p.stat().st_size)
    if not paths:
        pytest.skip("No FFXBND files in DSR sfx directory.")
    return paths[0]


@pytest.mark.game_data
def test_vanilla_ffxbnd_reads(dsr_root):
    ffxbnd = FFXBND.from_path(_small_ffxbnd_path(dsr_root))
    assert len(ffxbnd.entries) > 0
    for entry in ffxbnd.entries:
        assert entry.suffix in (".ffx", ".tpf", ".flver"), entry.name


@pytest.mark.game_data
def test_vanilla_ffxbnd_id_ranges_match_extensions(dsr_root):
    ffxbnd = FFXBND.from_path(_small_ffxbnd_path(dsr_root))
    for entry in ffxbnd.get_ffx_entries():
        assert entry.suffix == ".ffx", entry.name
    for entry in ffxbnd.get_tpf_entries():
        assert entry.suffix == ".tpf", entry.name
    for entry in ffxbnd.get_flver_entries():
        assert entry.suffix == ".flver", entry.name


@pytest.mark.game_data
def test_vanilla_ffxbnd_binary_roundtrip(dsr_root, tmp_path):
    """unpack -> pack -> unpack must preserve every entry's name and data."""
    source = _small_ffxbnd_path(dsr_root)
    ffxbnd = FFXBND.from_path(source)
    before = {e.name: e.data for e in ffxbnd.entries}
    write_path = tmp_path / source.name
    ffxbnd.write(write_path)
    reloaded = FFXBND.from_path(write_path)
    after = {e.name: e.data for e in reloaded.entries}
    assert after == before


@pytest.mark.game_data
def test_vanilla_ffxbnd_write_renumbers_tpf_entries(dsr_root, tmp_path):
    """`entry_autogen()` runs on every write and re-sorts TPF/FLVER entries by numeric ID.

    Vanilla FFXBNDs are NOT stored in that order, so a no-op load/save changes entry IDs.
    """
    sfx_dir = _sfx_dir(dsr_root)
    candidates = [
        p for p in sorted(sfx_dir.glob("FRPG_SfxBnd_*.ffxbnd.dcx"), key=lambda p: p.stat().st_size)
        if p.stat().st_size < 5_000_000
    ]
    if not candidates:
        pytest.skip("No suitably small FFXBND files.")
    changed = None
    for path in candidates:
        ffxbnd = FFXBND.from_path(path)
        before = [(e.entry_id, e.name) for e in ffxbnd.entries]
        ffxbnd.write(tmp_path / path.name)
        after = [(e.entry_id, e.name) for e in FFXBND.from_path(tmp_path / path.name).entries]
        if before != after:
            changed = (path.name, before, after)
            break
    if changed is None:
        pytest.skip("No vanilla FFXBND in this install is stored out of `entry_autogen()` order.")
    name, before, after = changed
    assert {n for _, n in before} == {n for _, n in after}, "names must be preserved even when IDs shift"


@pytest.mark.game_data
@pytest.mark.slow
def test_all_small_vanilla_ffxbnds_read(dsr_root):
    sfx_dir = _sfx_dir(dsr_root)
    paths = [p for p in sorted(sfx_dir.glob("*.ffxbnd.dcx")) if p.stat().st_size < 3_000_000]
    if not paths:
        pytest.skip("No small FFXBND files in DSR sfx directory.")
    for path in paths:
        ffxbnd = FFXBND.from_path(path)
        assert ffxbnd.entries, path.name
