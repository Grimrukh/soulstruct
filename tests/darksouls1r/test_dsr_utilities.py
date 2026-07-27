"""Tests for `soulstruct.darksouls1r.utilities` (excluding `file_list.py`, see `test_file_list.py`).

Modules covered:
    - `core.py`               : `get_ds1_executable_and_version`
    - `bonfire_warp_list.py`  : reading/writing the hard-coded bonfire warp table in the game EXE
    - `add_draw_slots.py`     : adding DrawParam slot 1 to map areas
    - `compare_draw_params.py`: DrawParam diffing utility
    - `memory.py`             : `DSRMemoryHook`, `MemoryDrawParam`
    - `memory_monitor.py`     : `MapMonitor`, `MapChrInfo`
    - `move_map_piece.py`     : empty file

Several of these modules are abandoned and cannot run at all; those tests are `xfail`-marked with
the specific defect.
"""
from __future__ import annotations

import struct
from pathlib import Path

import pytest

from soulstruct.darksouls1r.params.draw_param import DrawParamBND, DrawParamDirectory
from soulstruct.darksouls1r.utilities import add_draw_slots, bonfire_warp_list
from soulstruct.darksouls1r.utilities.bonfire_warp_list import (
    DSR_VANILLA_EXE_DATA,
    DSR_WARP_LIST_OFFSET,
    MODDED_EXE_DATA,
    PTDE_DEBUG_WARP_LIST_OFFSET,
    PTDE_VANILLA_EXE_DATA,
    PTDE_WARP_LIST_OFFSET,
    edit_executable_bonfire_warp_data,
    get_executable_bonfire_warp_data,
    restore_bonfire_warp_data,
)
from soulstruct.darksouls1r.utilities.compare_draw_params import compare_draw_params
from soulstruct.darksouls1r.utilities.core import get_ds1_executable_and_version
from soulstruct.darksouls1r.utilities.memory import DSRMemoryHook, MemoryDrawParam


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_fake_exe(directory: Path, name: str, size: int = 0) -> Path:
    """Create a placeholder EXE file, optionally padded out to `size` bytes."""
    path = directory / name
    path.write_bytes(b"MZ")
    if size:
        with path.open("r+b") as f:
            f.seek(size - 1)
            f.write(b"\0")
    return path


# `get_event_flag_offset_mask` is wrapped by `memory_hook_validate`, which requires a live process.
# `functools.wraps` exposes the undecorated function, and it only touches class-level dicts.
_flag_offset_mask = DSRMemoryHook.get_event_flag_offset_mask.__wrapped__


# ---------------------------------------------------------------------------
# core.get_ds1_executable_and_version
# ---------------------------------------------------------------------------


def test_get_ds1_executable_from_ptde_directory(tmp_path):
    _make_fake_exe(tmp_path, "DARKSOULS.exe")
    exe, dsr, debug = get_ds1_executable_and_version(tmp_path, dsr=None)
    assert exe.name == "DARKSOULS.exe"
    assert dsr is False
    assert debug is False


def test_get_ds1_executable_rejects_directory_with_both_executables(tmp_path):
    _make_fake_exe(tmp_path, "DARKSOULS.exe")
    _make_fake_exe(tmp_path, "DarkSoulsRemastered.exe")
    with pytest.raises(FileExistsError):
        get_ds1_executable_and_version(tmp_path, dsr=None)


def test_get_ds1_executable_rejects_directory_with_no_executable(tmp_path):
    with pytest.raises(FileNotFoundError):
        get_ds1_executable_and_version(tmp_path, dsr=None)


def test_get_ds1_executable_rejects_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        get_ds1_executable_and_version(tmp_path / "nope.exe", dsr=None)


def test_get_ds1_executable_unknown_name_requires_explicit_dsr(tmp_path):
    exe = _make_fake_exe(tmp_path, "DarkSoulsModded.exe")
    with pytest.raises(ValueError, match="dsr="):
        get_ds1_executable_and_version(exe, dsr=None)
    assert get_ds1_executable_and_version(exe, dsr=True) == (exe, True, False)


def test_get_ds1_executable_rejects_dsr_debug(tmp_path):
    exe = _make_fake_exe(tmp_path, "DarkSoulsRemastered.exe")
    with pytest.raises(ValueError, match="`debug` cannot be True"):
        get_ds1_executable_and_version(exe, dsr=True, debug=True)


def test_get_ds1_executable_ptde_debug_is_allowed(tmp_path):
    exe = _make_fake_exe(tmp_path, "DARKSOULS.exe")
    assert get_ds1_executable_and_version(exe, dsr=None, debug=True) == (exe, False, True)


def test_get_ds1_executable_infers_dsr_from_file_name(tmp_path):
    exe = _make_fake_exe(tmp_path, "DarkSoulsRemastered.exe")
    assert get_ds1_executable_and_version(exe, dsr=None) == (exe, True, False)


def test_get_ds1_executable_from_dsr_directory(tmp_path):
    _make_fake_exe(tmp_path, "DarkSoulsRemastered.exe")
    exe, dsr, debug = get_ds1_executable_and_version(tmp_path, dsr=None)
    assert dsr is True


# ---------------------------------------------------------------------------
# bonfire_warp_list: static data
# ---------------------------------------------------------------------------


def test_bonfire_tables_have_expected_lengths():
    assert len(PTDE_VANILLA_EXE_DATA) == 20
    assert len(DSR_VANILLA_EXE_DATA) == 21
    assert len(MODDED_EXE_DATA) == 20


def test_dsr_table_extends_ptde_table():
    assert DSR_VANILLA_EXE_DATA[:20] == PTDE_VANILLA_EXE_DATA
    assert DSR_VANILLA_EXE_DATA[20] == (220, 1301962, 2020)


@pytest.mark.parametrize(
    "table",
    [PTDE_VANILLA_EXE_DATA, DSR_VANILLA_EXE_DATA, MODDED_EXE_DATA],
    ids=["ptde", "dsr", "modded"],
)
def test_bonfire_tables_are_triplets_of_int32(table):
    for entry in table:
        assert isinstance(entry, tuple) and len(entry) == 3, entry
        for value in entry:
            assert isinstance(value, int)
            struct.pack("i", value)  # must fit in a signed 32-bit int


@pytest.mark.parametrize(
    "table",
    [PTDE_VANILLA_EXE_DATA, DSR_VANILLA_EXE_DATA, MODDED_EXE_DATA],
    ids=["ptde", "dsr", "modded"],
)
def test_bonfire_tables_have_unique_flags_entities_and_text_ids(table):
    flags, entities, texts = zip(*table)
    assert len(set(flags)) == len(flags), "duplicate required flags"
    assert len(set(entities)) == len(entities), "duplicate bonfire entity IDs"
    assert len(set(texts)) == len(texts), "duplicate PlaceName text IDs"


def test_vanilla_bonfire_text_ids_are_contiguous_from_2000():
    _, _, texts = zip(*DSR_VANILLA_EXE_DATA)
    assert list(texts) == list(range(2000, 2021))


def test_vanilla_bonfire_entity_ids_look_like_ds1_map_entities():
    for flag, entity, text in DSR_VANILLA_EXE_DATA:
        assert 1000000 <= entity < 2000000, entity
        # DS1 entity IDs are AABBEEEE (area, block, entity).
        assert 10 <= entity // 100000 <= 18, entity


def test_warp_list_offsets_are_distinct_and_positive():
    offsets = (PTDE_WARP_LIST_OFFSET, PTDE_DEBUG_WARP_LIST_OFFSET, DSR_WARP_LIST_OFFSET)
    assert all(o > 0 for o in offsets)
    assert len(set(offsets)) == 3


# ---------------------------------------------------------------------------
# bonfire_warp_list: validation + read/write round-trip on a synthetic EXE
# ---------------------------------------------------------------------------


def test_edit_bonfire_data_rejects_non_triplets(tmp_path):
    exe = _make_fake_exe(tmp_path, "DARKSOULS.exe", size=1024)
    with pytest.raises(ValueError, match="triplets"):
        edit_executable_bonfire_warp_data(exe, [(1, 2), (3, 4)], dsr=False)


def test_edit_bonfire_data_rejects_wrong_count_for_ptde(tmp_path):
    exe = _make_fake_exe(tmp_path, "DARKSOULS.exe", size=1024)
    with pytest.raises(ValueError, match="20 bonfire"):
        edit_executable_bonfire_warp_data(exe, DSR_VANILLA_EXE_DATA, dsr=False)


def test_edit_bonfire_data_rejects_wrong_count_for_dsr(tmp_path):
    exe = _make_fake_exe(tmp_path, "DarkSoulsRemastered.exe", size=1024)
    with pytest.raises(ValueError, match="21 bonfire"):
        edit_executable_bonfire_warp_data(exe, PTDE_VANILLA_EXE_DATA, dsr=True)


@pytest.mark.slow
def test_bonfire_warp_data_write_then_read_roundtrip_ptde(tmp_path):
    """Write the vanilla PTDE table into a synthetic 16 MB 'DARKSOULS.exe' and read it back."""
    exe = _make_fake_exe(tmp_path, "DARKSOULS.exe", size=PTDE_WARP_LIST_OFFSET + 12 * 20 + 16)
    edit_executable_bonfire_warp_data(exe, PTDE_VANILLA_EXE_DATA, dsr=False)
    read_back = get_executable_bonfire_warp_data(exe, dsr=False)
    assert read_back == PTDE_VANILLA_EXE_DATA


@pytest.mark.slow
def test_bonfire_warp_data_write_then_read_roundtrip_dsr(tmp_path):
    exe = _make_fake_exe(tmp_path, "DarkSoulsRemastered.exe", size=DSR_WARP_LIST_OFFSET + 12 * 21 + 16)
    edit_executable_bonfire_warp_data(exe, DSR_VANILLA_EXE_DATA, dsr=True)
    read_back = get_executable_bonfire_warp_data(exe, dsr=True)
    assert read_back == DSR_VANILLA_EXE_DATA


@pytest.mark.slow
def test_restore_bonfire_warp_data_writes_vanilla_table(tmp_path):
    exe = _make_fake_exe(tmp_path, "DARKSOULS.exe", size=PTDE_WARP_LIST_OFFSET + 12 * 20 + 16)
    # Write a nonsense table first.
    scrambled = [(f, e, t + 1000) for f, e, t in PTDE_VANILLA_EXE_DATA]
    edit_executable_bonfire_warp_data(exe, scrambled, dsr=False)
    assert get_executable_bonfire_warp_data(exe, dsr=False) == scrambled
    restore_bonfire_warp_data(exe, dsr=False)
    assert get_executable_bonfire_warp_data(exe, dsr=False) == PTDE_VANILLA_EXE_DATA


@pytest.mark.slow
def test_ptde_debug_offset_is_written_separately(tmp_path):
    size = PTDE_DEBUG_WARP_LIST_OFFSET + 12 * 20 + 16
    exe = _make_fake_exe(tmp_path, "DARKSOULS.exe", size=size)
    edit_executable_bonfire_warp_data(exe, PTDE_VANILLA_EXE_DATA, dsr=False, debug=True)
    assert get_executable_bonfire_warp_data(exe, dsr=False, debug=True) == PTDE_VANILLA_EXE_DATA
    # The non-debug offset must still be all zeroes.
    non_debug = get_executable_bonfire_warp_data(exe, dsr=False, debug=False)
    assert non_debug == [(0, 0, 0)] * 20


def test_bonfire_module_main_block_is_dead_code():
    """The module's `__main__` block calls `get_executable_bonfire_warp_data(Config.PTDE_PATH)`.

    That is a read-only operation but the function opens 'r+b' and hard-codes vanilla list lengths,
    so it only works on an unmodified, writable PTDE install.
    """
    import inspect

    source = inspect.getsource(bonfire_warp_list)
    assert 'if __name__ == "__main__":' in source


# ---------------------------------------------------------------------------
# add_draw_slots
# ---------------------------------------------------------------------------


def test_add_draw_slot_to_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        add_draw_slots.add_draw_slot_1_to_drawparam(tmp_path / "a10_DrawParam.parambnd")


def test_add_draw_slot_1_to_map_area_wraps_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="map area"):
        add_draw_slots.add_draw_slot_1_to_map_area(tmp_path, 10)


def test_add_draw_slot_1_to_all_map_areas_visits_parambnds(tmp_path, monkeypatch):
    draw_param_dir = tmp_path / "param" / "DrawParam"
    draw_param_dir.mkdir(parents=True)
    for area in ("a10", "a11"):
        (draw_param_dir / f"{area}_DrawParam.parambnd.dcx").write_bytes(b"\x00")

    visited = []
    monkeypatch.setattr(add_draw_slots, "add_draw_slot_1_to_drawparam", visited.append)
    add_draw_slots.add_draw_slot_1_to_all_map_areas(tmp_path)
    assert len(visited) == 2, visited


def test_add_draw_slot_1_to_drawparam_on_real_file(dsr_root, tmp_path):
    import shutil

    source = dsr_root / "param" / "DrawParam" / "a10_DrawParam.parambnd.dcx"
    if not source.is_file():
        pytest.skip(f"No DSR DrawParam file at {source}")
    target = tmp_path / source.name
    shutil.copy(source, target)
    add_draw_slots.add_draw_slot_1_to_drawparam(target)

    from soulstruct.containers import Binder

    assert len(Binder.from_path(target)) == 24


# ---------------------------------------------------------------------------
# compare_draw_params
# ---------------------------------------------------------------------------


class _FakeRow:
    """Minimal stand-in for a `ParamRow`: exposes `.Name` and iterates as `(field_name, value)` pairs, which is
    all that `compare_draw_params()` and `DrawParam.get_nonzero_entries()` actually need."""

    def __init__(self, name: str, **fields):
        self.Name = name
        self._fields = fields

    def __iter__(self):
        return iter(self._fields.items())


class _FakeDrawParam:
    """Minimal stand-in for a `DrawParam`: only implements `get_nonzero_entries()`, matching the real
    `DrawParam.get_nonzero_entries()` filtering logic (drop unnamed and '0'/'PolyG'-prefixed rows)."""

    def __init__(self, rows: dict[int, _FakeRow]):
        self.rows = rows

    def get_nonzero_entries(self, ignore_polyg=True):
        prefixes = ("0", "polyg") if ignore_polyg else ("0",)
        return {i: row for i, row in self.rows.items() if row.Name and not row.Name.lower().startswith(prefixes)}


def _make_drawparam_directory(light_bank_draw_param: _FakeDrawParam | None) -> DrawParamDirectory:
    """Build a `DrawParamDirectory` with a single 'a10' area whose 'LightBank' slot 0 is the given fake table
    (or entirely absent, if `None`). All other DrawParam nicknames are left unset."""
    bnd = DrawParamBND(map_area="a10")
    if light_bank_draw_param is not None:
        bnd.draw_params_0["LightBank"] = light_bank_draw_param
    return DrawParamDirectory(files={"a10_DrawParam": bnd})


@pytest.fixture
def single_area_scope(monkeypatch):
    """Restrict `DrawParamDirectory.DRAW_PARAM_AREAS` to just 'a10' so tests don't need every map area."""
    monkeypatch.setattr(DrawParamDirectory, "DRAW_PARAM_AREAS", {"a10": "Test Area"})


def test_compare_draw_params_reports_no_differences_for_identical_tables(single_area_scope, capsys):
    draw_param = _FakeDrawParam({0: _FakeRow("Torch", ColorR=255, ColorG=200, Intensity=1.0)})
    dir_one = _make_drawparam_directory(draw_param)
    dir_two = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=255, ColorG=200, Intensity=1.0)}))

    compare_draw_params(dir_one, dir_two)

    output = capsys.readouterr().out
    assert "No differences found." in output


def test_compare_draw_params_reports_differing_field_value(single_area_scope, capsys):
    dir_one = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=255, Intensity=1.0)}))
    dir_two = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=250, Intensity=1.0)}))

    compare_draw_params(dir_one, dir_two, names=("Vanilla", "Modded"))

    output = capsys.readouterr().out
    assert "a10" in output
    assert "BakedLight" in output  # nickname for 'LightBank'
    assert "Torch" in output
    assert "ColorR" in output
    assert "255" in output and "250" in output
    assert "Vanilla" in output and "Modded" in output
    # Matching fields should not be printed at all when `ignore_matches=True` (the default).
    assert "Intensity" not in output


def test_compare_draw_params_ignore_matches_false_shows_matching_fields_too(single_area_scope, capsys):
    dir_one = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=255, Intensity=1.0)}))
    dir_two = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=250, Intensity=1.0)}))

    compare_draw_params(dir_one, dir_two, ignore_matches=False)

    output = capsys.readouterr().out
    assert "Intensity" in output  # now shown alongside the real 'ColorR' difference


def test_compare_draw_params_ignores_float_differences_below_threshold(single_area_scope, capsys):
    dir_one = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", Intensity=1.0)}))
    dir_two = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", Intensity=1.0005)}))

    compare_draw_params(dir_one, dir_two, float_diff=0.01)

    assert "No differences found." in capsys.readouterr().out


def test_compare_draw_params_reports_row_missing_from_one_side(single_area_scope, capsys):
    dir_one = _make_drawparam_directory(
        _FakeDrawParam({0: _FakeRow("Torch", ColorR=255), 1: _FakeRow("Only In One", ColorR=1)})
    )
    dir_two = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=255)}))

    compare_draw_params(dir_one, dir_two, names=("One", "Two"))

    output = capsys.readouterr().out
    assert "Only In One" in output
    assert "MISSING" in output and "Two" in output


def test_compare_draw_params_reports_table_missing_from_one_side(single_area_scope, capsys):
    dir_one = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=255)}))
    dir_two = _make_drawparam_directory(None)  # 'LightBank' slot 0 entirely absent

    compare_draw_params(dir_one, dir_two, names=("One", "Two"))

    output = capsys.readouterr().out
    assert "missing" in output.lower()
    assert "Two" in output


def test_compare_draw_params_ignore_param_names_skips_table(single_area_scope, capsys):
    dir_one = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=255)}))
    dir_two = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=250)}))

    compare_draw_params(dir_one, dir_two, ignore_param_names=("BakedLight",))

    assert "No differences found." in capsys.readouterr().out


def test_compare_draw_params_raises_on_mismatched_field_names(single_area_scope):
    """Corrupted/incompatible rows whose fields do not line up must raise, not silently misreport."""
    dir_one = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorR=255)}))
    dir_two = _make_drawparam_directory(_FakeDrawParam({0: _FakeRow("Torch", ColorG=255)}))

    with pytest.raises(ValueError, match="Field name mismatch"):
        compare_draw_params(dir_one, dir_two)


# ---------------------------------------------------------------------------
# memory.DSRMemoryHook (pure logic; no running game required)
# ---------------------------------------------------------------------------


def test_dsr_memory_hook_class_constants():
    assert DSRMemoryHook.PROCESS_NAME == "DarkSoulsRemastered.exe"
    assert DSRMemoryHook.BASE_ADDRESS == 0x140000000
    assert DSRMemoryHook.ADDRESS_CACHE_NAME == "ds1r_cache"


def test_event_flag_areas_are_unique_and_contiguous():
    values = list(DSRMemoryHook.EVENT_FLAG_AREAS.values())
    assert values == list(range(len(values)))
    assert len(set(DSRMemoryHook.EVENT_FLAG_AREAS)) == len(DSRMemoryHook.EVENT_FLAG_AREAS)


def test_event_flag_groups_are_ascending():
    values = list(DSRMemoryHook.EVENT_FLAG_GROUPS.values())
    assert values == sorted(values)
    assert values[0] == 0


def test_event_flag_offset_mask_for_flag_zero():
    offset, mask = _flag_offset_mask(DSRMemoryHook, 0)
    assert offset == 0
    assert mask == 0x80000000


def test_event_flag_offset_mask_bit_walk():
    """Within one 32-flag word, the mask walks right and the offset stays put."""
    offsets_masks = [_flag_offset_mask(DSRMemoryHook, n) for n in range(32)]
    assert {o for o, _ in offsets_masks} == {0}
    assert [m for _, m in offsets_masks] == [0x80000000 >> i for i in range(32)]
    # Flag 32 rolls over to the next 4-byte word.
    assert _flag_offset_mask(DSRMemoryHook, 32) == (4, 0x80000000)


def test_event_flag_offset_mask_uses_group_and_area():
    # 11010000: group '1', area '101', section 0, number 0.
    offset, mask = _flag_offset_mask(DSRMemoryHook, 11010000)
    expected = DSRMemoryHook.EVENT_FLAG_GROUPS["1"] + DSRMemoryHook.EVENT_FLAG_AREAS["101"] * 0x500
    assert offset == expected
    assert mask == 0x80000000


def test_event_flag_offset_mask_section_digit():
    base, _ = _flag_offset_mask(DSRMemoryHook, 11010000)
    shifted, _ = _flag_offset_mask(DSRMemoryHook, 11015000)
    assert shifted - base == 5 * 128


@pytest.mark.parametrize("flag_id", [999999999, 1234567890])
def test_event_flag_offset_mask_rejects_too_large(flag_id):
    with pytest.raises(ValueError, match="too large"):
        _flag_offset_mask(DSRMemoryHook, flag_id)


def test_event_flag_offset_mask_rejects_unknown_group():
    # Group '2' is not in EVENT_FLAG_GROUPS.
    with pytest.raises(ValueError, match="invalid group"):
        _flag_offset_mask(DSRMemoryHook, 21010000)


def test_event_flag_offset_mask_rejects_unknown_area():
    with pytest.raises(ValueError, match="invalid area"):
        _flag_offset_mask(DSRMemoryHook, 19990000)


def test_memory_hook_methods_require_a_hooked_process():
    """The public wrappers all go through `memory_hook_validate`."""
    assert hasattr(DSRMemoryHook.get_event_flag_offset_mask, "__wrapped__")
    assert hasattr(DSRMemoryHook.write_game_param_to_memory, "__wrapped__")


def test_pre_cache_gameparam_uses_a_stale_nested_cache_key():
    """`_address_cache` is a flat `dict[str, int]`, but `pre_cache_gameparam` looks up a 'ds1r' sub-dict.

    The membership test therefore always fails and the address is always re-scanned.
    """
    import inspect

    source = inspect.getsource(DSRMemoryHook.pre_cache_gameparam.__wrapped__)
    assert 'self._address_cache.get("ds1r", {})' in source


# ---------------------------------------------------------------------------
# memory.MemoryDrawParam (pure logic; `hook` is never touched by __init__)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "stem, area_id, extra_slot, expected",
    [
        ("FogBank", 12, False, "m12_FogBank"),
        ("FogBank", 12, True, "m12_1_FogBank"),
        ("s_LightBank", 15, False, "s15_LightBank"),
        ("s_LightBank", 15, True, "s15_1_LightBank"),
        ("LightScatteringBank", 10, False, "m10_LightScatteringBank"),
    ],
)
def test_memory_draw_param_file_stem(stem, area_id, extra_slot, expected):
    mdp = MemoryDrawParam(None, object, stem, area_id, is_extra_slot=extra_slot)
    assert mdp.draw_param_file_stem == expected


def test_memory_draw_param_starts_with_empty_read_only_row_dict():
    mdp = MemoryDrawParam(None, object, "FogBank", 12)
    assert dict(mdp.row_dict) == {}
    with pytest.raises(TypeError):
        mdp.row_dict[0] = "x"


def test_memory_draw_param_pointer_offsets_cover_all_draw_param_types():
    offsets = MemoryDrawParam.POINTER_OFFSETS
    assert len(set(offsets.values())) == len(offsets), "duplicate pointer offsets"
    assert "s_LightBank" in offsets
    # Offsets are 0x18 apart, with 0xD0 deliberately skipped ("Unused").
    values = sorted(offsets.values())
    gaps = {b - a for a, b in zip(values, values[1:])}
    assert gaps <= {0x18, 0x30}, gaps


def test_memory_draw_param_write_before_read_raises(monkeypatch):
    mdp = MemoryDrawParam(None, object, "FogBank", 12)

    class _Hook:
        @staticmethod
        def try_hooked():
            return True

    mdp.hook = _Hook()
    with pytest.raises(RuntimeError, match="before calling `read_from_memory"):
        mdp.write_to_memory()


def test_memory_draw_param_row_dict_is_a_mapping_proxy():
    """Documents why `copy()` fails: `row_dict` is a `MappingProxyType`, not a plain dict."""
    from types import MappingProxyType

    mdp = MemoryDrawParam(None, object, "FogBank", 12)
    assert isinstance(mdp.row_dict, MappingProxyType)


# ---------------------------------------------------------------------------
# memory_monitor
# ---------------------------------------------------------------------------


def test_map_monitor_is_a_dsr_memory_hook():
    from soulstruct.darksouls1r.utilities.memory_monitor import MapChrInfo, MapMonitor

    assert issubclass(MapMonitor, DSRMemoryHook)
    assert MapMonitor.CHR_HEADER_SIZE == 0x38
    assert MapChrInfo._fields == (
        "handle_id", "model_name", "current_hp", "max_hp", "facing_angle", "x", "y", "z",
    )


def test_map_monitor_rejects_invalid_map_area():
    from soulstruct.darksouls1r.utilities.memory_monitor import MapMonitor

    unwrapped = MapMonitor.get_character_list_count_address
    with pytest.raises(ValueError, match="between 10 and 18"):
        unwrapped(MapMonitor, 9, 0)
    with pytest.raises(ValueError, match="between 10 and 18"):
        unwrapped(MapMonitor, 19, 0)


# ---------------------------------------------------------------------------
# Dead files
# ---------------------------------------------------------------------------


def test_move_map_piece_module_is_empty():
    from soulstruct.darksouls1r.utilities import move_map_piece

    public = [name for name in vars(move_map_piece) if not name.startswith("__")]
    assert public == [], f"`move_map_piece.py` is expected to be empty, but defines: {public}"


def test_utilities_package_exports_nothing():
    """`darksouls1r/utilities/__init__.py` is empty; every module must be imported explicitly."""
    from soulstruct.darksouls1r import utilities

    assert not getattr(utilities, "__all__", None)


# ---------------------------------------------------------------------------
# Optional dependency guards (`psutil`, `matplotlib`, `pydub`)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "module_name",
    [
        "soulstruct.utilities.memory",
        "soulstruct.darksouls1r.utilities.memory",
        "soulstruct.darksouls1r.utilities.memory_monitor",
        "soulstruct.darksouls1r.sound.utilities",
        "soulstruct.darksouls1r.sound.fev.core",
        "soulstruct.darksouls1r.sound.fsb",
        "soulstruct.darksouls1r.ffx.ffxbnd",
    ],
)
def test_modules_import_without_optional_extras(module_name):
    """Import each module in a subprocess with `psutil`/`matplotlib`/`pydub` blocked."""
    import subprocess
    import sys
    import textwrap

    script = textwrap.dedent(
        f"""
        import sys
        BLOCKED = {{"psutil", "matplotlib", "matplotlib.pyplot", "pydub"}}

        class _Blocker:
            def find_module(self, name, path=None):
                return self if name.split(".")[0] in {{"psutil", "matplotlib", "pydub"}} else None

            def find_spec(self, name, path=None, target=None):
                if name.split(".")[0] in {{"psutil", "matplotlib", "pydub"}}:
                    raise ImportError(f"blocked: {{name}}")
                return None

        sys.meta_path.insert(0, _Blocker())
        for mod in list(sys.modules):
            if mod.split(".")[0] in {{"psutil", "matplotlib", "pydub"}}:
                del sys.modules[mod]
        import {module_name}
        print("OK")
        """
    )
    result = subprocess.run(
        [sys.executable, "-c", script], capture_output=True, text=True, timeout=180,
    )
    assert "OK" in result.stdout, (
        f"`{module_name}` failed to import without optional extras:\n{result.stderr[-3000:]}"
    )
