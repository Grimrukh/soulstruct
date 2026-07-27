"""Tests for DSR `DrawParamBND` / `DrawParamDirectory` (`param/DrawParam`).

DSR ships eleven `*_DrawParam.parambnd.dcx` files: one per map area (`a10`-`a18`, plus the `a99` test map)
and one `default` (menus). Each holds up to two "slots" of each DrawParam (slot 0 and slot 1), keyed by
Param stem (`FogBank`, `LightBank`, ...).

Two vanilla DSR DrawParams (`ToneMapBank` and `ToneCorrectBank`) are *corrupt* -- their rows are 32 bytes
where the DSR PARAMDEF expects 36 -- so `DrawParamBND.assign_param_from_entry()` falls back to the PTDE
row type and converts. That fallback is DSR-specific and is exercised here.
"""
from __future__ import annotations

import pytest

from soulstruct.dcx import DCXType
from soulstruct.darksouls1r.params.draw_param import DrawParam, DrawParamBND, DrawParamDirectory
from soulstruct.games import DARK_SOULS_DSR

CORRUPT_VANILLA_PARAMS = ("ToneMapBank", "ToneCorrectBank")


@pytest.fixture(scope="module")
def drawparam_dir(request):
    from soulstruct.config import Config

    root = Config.DSR_PATH
    if not root or not (root := __import__("pathlib").Path(root)).is_dir():
        pytest.skip("Dark Souls: Remastered directory not found.")
    path = root / "param/DrawParam"
    if not path.is_dir():
        pytest.skip(f"Missing DSR DrawParam directory: {path}")
    return DrawParamDirectory.from_path(path)


# ---------------------------------------------------------------------------
# Class configuration (pure unit, no game data)
# ---------------------------------------------------------------------------


def test_class_config():
    assert DrawParamDirectory.FILE_CLASS is DrawParamBND
    assert DrawParamDirectory.FILE_EXTENSION == ".parambnd"
    assert DrawParamBND.DEFAULT_ENTRY_ROOT.endswith("\\param\\DrawParam")
    assert DrawParamBND()._get_dcx_type() == DARK_SOULS_DSR.default_dcx_type
    assert DrawParamBND()._get_dcx_type() != DCXType.Null, "DSR DrawParamBNDs are DCX-compressed."


def test_draw_param_areas_cover_all_ds1_areas():
    areas = DrawParamDirectory.DRAW_PARAM_AREAS
    for area in range(10, 19):
        assert f"a{area}" in areas
    assert "a99" in areas  # test map
    assert "default" in areas  # menus
    assert len(areas) == 11


def test_get_all_file_stems_matches_areas():
    stems = DrawParamDirectory.get_all_file_stems()
    assert len(stems) == len(DrawParamDirectory.DRAW_PARAM_AREAS)
    assert set(stems) == {f"{area}_DrawParam" for area in DrawParamDirectory.DRAW_PARAM_AREAS}
    assert len(set(stems)) == len(stems)


def test_file_name_pattern_matches_real_dsr_names():
    import re

    pattern = re.compile(DrawParamDirectory.FILE_NAME_PATTERN + r"(\.dcx)?$")
    assert pattern.match("a10_DrawParam.parambnd.dcx")
    assert pattern.match("default_DrawParam.parambnd.dcx")
    assert pattern.match("a99_DrawParam.parambnd")
    assert not pattern.match("GameParam.parambnd.dcx")


# ---------------------------------------------------------------------------
# Live DSR DrawParam directory
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_directory_loads_all_areas(drawparam_dir):
    assert sorted(drawparam_dir.files) == sorted(DrawParamDirectory.get_all_file_stems())
    assert isinstance(drawparam_dir.a10, DrawParamBND)
    assert isinstance(drawparam_dir.default, DrawParamBND)


@pytest.mark.game_data
def test_area_lookup_helpers(drawparam_dir):
    assert drawparam_dir["a12"] is drawparam_dir.a12
    assert drawparam_dir["a12_DrawParam"] is drawparam_dir.a12
    assert drawparam_dir.get_drawparambnd("a12") is drawparam_dir.a12
    # `mXX` map-area names are accepted and converted to `aXX`.
    assert drawparam_dir.get_drawparambnd("m12") is drawparam_dir.a12
    assert drawparam_dir.get_drawparambnd("default") is drawparam_dir.default
    with pytest.raises(KeyError):
        drawparam_dir.get_drawparambnd("a77")


@pytest.mark.game_data
def test_get_drawparambnd_accepts_full_stem(drawparam_dir):
    assert drawparam_dir.get_drawparambnd("a10_DrawParam") is drawparam_dir.a10


@pytest.mark.game_data
def test_draw_params_have_both_slots_where_expected(drawparam_dir):
    a10 = drawparam_dir.a10
    assert a10.draw_params_0, "Slot 0 must always be populated."
    for stem, param in a10.draw_params_0.items():
        assert isinstance(param, DrawParam)
        assert param.rows


@pytest.mark.game_data
def test_named_drawparam_slot_properties(drawparam_dir):
    """`<Nickname>_<slot>` properties (e.g. `BakedLight_0`) are the documented public accessor."""
    baked_light = drawparam_dir.a10.BakedLight_0
    assert isinstance(baked_light, DrawParam)
    assert len(baked_light.rows) > 0


@pytest.mark.game_data
def test_corrupt_vanilla_tone_params_are_repaired(drawparam_dir):
    """DSR's vanilla `ToneMapBank`/`ToneCorrectBank` rows are 4 bytes short; DSR falls back to PTDE."""
    for stem in CORRUPT_VANILLA_PARAMS:
        param = drawparam_dir.default.draw_params_0[stem]
        assert param.rows, f"'{stem}' was not repaired from the PTDE row type."
        # The repaired Param must use the *DSR* row type, so it re-writes with the DSR row size.
        assert param.ROW_TYPE.__module__.startswith("soulstruct.darksouls1r."), (
            f"'{stem}' was left as a PTDE Param instead of being converted to DSR."
        )


@pytest.mark.game_data
def test_directory_binary_roundtrip(drawparam_dir, tmp_path):
    drawparam_dir.write(tmp_path / "DrawParam")
    written = sorted(p.name for p in (tmp_path / "DrawParam").iterdir())
    assert written == sorted(f"{stem}.parambnd.dcx" for stem in DrawParamDirectory.get_all_file_stems())

    reload = DrawParamDirectory.from_path(tmp_path / "DrawParam")
    assert sorted(reload.files) == sorted(drawparam_dir.files)
    for stem, bnd in drawparam_dir.files.items():
        other = reload.files[stem]
        assert sorted(bnd.draw_params_0) == sorted(other.draw_params_0)
        assert sorted(bnd.draw_params_1) == sorted(other.draw_params_1)
        for param_stem, param in bnd.draw_params_0.items():
            assert list(param.rows) == list(other.draw_params_0[param_stem].rows)


@pytest.mark.game_data
def test_directory_json_roundtrip(drawparam_dir, tmp_path):
    drawparam_dir.write_json_directory(tmp_path / "DrawParamJSON")
    reload = DrawParamDirectory.from_json_directory(tmp_path / "DrawParamJSON")
    assert sorted(reload.files) == sorted(drawparam_dir.files)
    for stem, bnd in drawparam_dir.files.items():
        other = reload.files[stem]
        assert sorted(bnd.draw_params_0) == sorted(other.draw_params_0)
        for param_stem, param in bnd.draw_params_0.items():
            assert set(param.rows) == set(other.draw_params_0[param_stem].rows)


@pytest.mark.game_data
def test_from_path_rejects_non_directory(tmp_path):
    with pytest.raises(NotADirectoryError):
        DrawParamDirectory.from_path(tmp_path / "does_not_exist")
