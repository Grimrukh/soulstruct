"""Tests for DS1 PTDE DrawParam (per-map-area lighting params).

DrawParam is the most idiosyncratic Param family in DS1:
  - one `aXX_DrawParam.parambnd` per *map area* (plus `default_DrawParam.parambnd` for menus),
  - each Binder holds up to two "slots" per param type (`m15_LightBank.param`, `m15_1_LightBank.param`),
  - `sXX`-prefixed entries (`s15_LightBank.param`) are a debug variant stored under the `s_` stem.
"""
from __future__ import annotations

import logging

import pytest

from soulstruct.darksouls1ptde.params.draw_param import (
    DrawParam,
    DrawParamBND,
    DrawParamDirectory,
    TypedDrawParam,
)
from soulstruct.darksouls1ptde.params.draw_param.drawparambnd import _DRAW_PARAM_FILE_NAME_RE
from soulstruct.darksouls1ptde.params import paramdef
from soulstruct.dcx import DCXType


AREA_STEMS = ("a10", "a11", "a12", "a13", "a14", "a15", "a16", "a17", "a18", "a99", "default")

# Only `a15` (Sen's Fortress / Anor Londo) uses slot 1 in vanilla PTDE.
SLOT_1_AREAS = {"a15"}
# `LodBank` only exists in `default_DrawParam`; `s_LightBank` exists in every area BND but not `default`.
DEFAULT_ONLY_STEMS = {"LodBank"}
AREA_ONLY_STEMS = {"s_LightBank"}


# ---------------------------------------------------------------------------
# Pure-unit: class configuration and helpers
# ---------------------------------------------------------------------------


def test_draw_param_is_uncompressed():
    from soulstruct.games import DARK_SOULS_PTDE

    assert DARK_SOULS_PTDE.default_dcx_type == DCXType.Null
    # NOTE: the class-level `dcx_type = ...` assignments in `DrawParam` (core.py:17) and
    # `DrawParamBND` (drawparambnd.py:88) are DEAD -- the dataclass metaclass re-declares `dcx_type`
    # as a field with default `None`. What actually matters is `_get_dcx_type()`, which falls back
    # to the game default (`Null` for PTDE).
    assert DrawParamBND().dcx_type is None
    assert DrawParamBND()._get_dcx_type() == DCXType.Null, "PTDE DrawParamBNDs are not compressed."
    assert TypedDrawParam(paramdef.LIGHT_BANK)()._get_dcx_type() == DCXType.Null


def test_draw_param_areas_and_file_stems():
    assert tuple(DrawParamDirectory.DRAW_PARAM_AREAS) == AREA_STEMS
    assert DrawParamDirectory.get_all_file_stems() == [f"{a}_DrawParam" for a in AREA_STEMS]
    assert DrawParamDirectory.FILE_EXTENSION == ".parambnd"
    assert DrawParamDirectory.FILE_CLASS is DrawParamBND


def test_param_nicknames_are_bijective():
    nicknames = DrawParamBND.PARAM_NICKNAMES
    keys = list(nicknames.keys())
    values = list(nicknames.values())
    assert len(keys) == len(set(keys))
    assert len(values) == len(set(values))
    for key in keys:
        assert nicknames[nicknames[key]] == key, f"BiDict not bijective for {key}."


def test_param_types_cover_all_nicknames():
    assert set(DrawParamBND.PARAM_TYPES) == set(DrawParamBND.PARAM_NICKNAMES.keys())


def test_every_nickname_has_slot_0_and_slot_1_properties():
    for stem, nickname in DrawParamBND.PARAM_NICKNAMES.items():
        # `s_LightBank`'s properties are named `DebugBakedLight_*` rather than `s_BakedLight_*`.
        prop_base = "DebugBakedLight" if stem == "s_LightBank" else nickname
        for slot in (0, 1):
            attr = f"{prop_base}_{slot}"
            assert isinstance(getattr(DrawParamBND, attr, None), property), (
                f"`DrawParamBND.{attr}` property missing for stem '{stem}'."
            )


def test_paramdef_module_has_every_draw_param_row_type():
    expected_row_types = {
        "DofBank": "DOF_BANK",
        "EnvLightTexBank": "ENV_LIGHT_TEX_BANK",
        "FogBank": "FOG_BANK",
        "LensFlareBank": "LENS_FLARE_BANK",
        "LensFlareExBank": "LENS_FLARE_EX_BANK",
        "LightBank": "LIGHT_BANK",
        "LightScatteringBank": "LIGHT_SCATTERING_BANK",
        "PointLightBank": "POINT_LIGHT_BANK",
        "ShadowBank": "SHADOW_BANK",
        "ToneCorrectBank": "TONE_CORRECT_BANK",
        "ToneMapBank": "TONE_MAP_BANK",
        "LodBank": "LOD_BANK",
        "s_LightBank": "LIGHT_BANK",
    }
    assert set(expected_row_types) == set(DrawParamBND.PARAM_NICKNAMES.keys())
    for row_type_name in set(expected_row_types.values()):
        assert hasattr(paramdef, row_type_name), f"`paramdef.{row_type_name}` missing."


@pytest.mark.parametrize(
    "entry_name,expected",
    [
        ("m15_LightBank.param", ("m15", None, "_LightBank")),
        ("m15_1_LightBank.param", ("m15", "_1", "_LightBank")),
        ("s15_LightBank.param", ("s15", None, "_LightBank")),
        ("default_LodBank.param", ("default", None, "_LodBank")),
        ("m10_LensFlareExBank.param", ("m10", None, "_LensFlareExBank")),
    ],
)
def test_draw_param_entry_name_regex(entry_name, expected):
    match = _DRAW_PARAM_FILE_NAME_RE.match(entry_name)
    assert match is not None, f"Regex failed to match valid entry name: {entry_name}"
    assert match.groups() == expected


@pytest.mark.parametrize("entry_name", ["LightBank.param", "m15_LightBank.txt", "x15_LightBank.param"])
def test_draw_param_entry_name_regex_rejects_bad_names(entry_name):
    assert _DRAW_PARAM_FILE_NAME_RE.match(entry_name) is None


def test_resolve_draw_param_stem_both_directions():
    assert DrawParamBND.resolve_draw_param_stem("LightBank") == "LightBank"
    assert DrawParamBND.resolve_draw_param_stem("BakedLight") == "LightBank"
    assert DrawParamDirectory.resolve_draw_param_stem("ScatteredLight") == "LightScatteringBank"
    with pytest.raises(ValueError):
        DrawParamBND.resolve_draw_param_stem("NotAParam")


def test_typed_draw_param_reuses_generated_classes():
    cls_a = TypedDrawParam(paramdef.LIGHT_BANK)
    cls_b = TypedDrawParam(paramdef.LIGHT_BANK)
    assert cls_a is cls_b, "`TypedDrawParam` must not regenerate a class for the same row type."
    assert issubclass(cls_a, DrawParam)
    assert cls_a.ROW_TYPE is paramdef.LIGHT_BANK
    assert cls_a.__name__ == "DrawParam_LIGHT_BANK"
    assert TypedDrawParam(paramdef.FOG_BANK) is not cls_a


def test_get_draw_param_entry_path_generation():
    bnd = DrawParamBND(map_area="m15")
    assert bnd.get_draw_param_entry_path("LightBank", 0).endswith("m15_LightBank.param")
    assert bnd.get_draw_param_entry_path("LightBank", 1).endswith("m15_1_LightBank.param")
    # `s_` stems are written under the `sXX` map-area prefix.
    assert bnd.get_draw_param_entry_path("s_LightBank", 0).endswith("s15_LightBank.param")
    assert bnd.get_draw_param_entry_path("s_LightBank", 1).endswith("s15_1_LightBank.param")
    with pytest.raises(ValueError):
        bnd.get_draw_param_entry_path("LightBank", 2)
    with pytest.raises(ValueError):
        DrawParamBND().get_draw_param_entry_path("LightBank", 0)  # no `map_area`


def test_get_draw_param_slot_rejects_bad_slot_and_name():
    bnd = DrawParamBND(map_area="m15")
    with pytest.raises(ValueError):
        bnd.get_draw_param_slot("LightBank", 2)
    with pytest.raises(KeyError):
        bnd.get_draw_param_slot("NotAParam", 0)


def test_get_nonzero_entries_ignore_polyg_flag():
    param = TypedDrawParam(paramdef.LIGHT_BANK)()
    param.rows = {
        0: type("_Row", (), {"Name": "0 Unused"})(),
        1: type("_Row", (), {"Name": "Real Light"})(),
        2: type("_Row", (), {"Name": "PolyG Cutscene"})(),
        3: type("_Row", (), {"Name": ""})(),
    }
    ignored = param.get_nonzero_entries(ignore_polyg=True)
    kept = param.get_nonzero_entries(ignore_polyg=False)
    assert set(ignored) == {1}, "`ignore_polyg=True` should drop 'PolyG' rows."
    assert set(kept) == {1, 2}, "`ignore_polyg=False` should keep 'PolyG' rows."


# ---------------------------------------------------------------------------
# Vanilla game data
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def draw_param_dir(ptde_root):
    path = ptde_root / "param" / "DrawParam"
    if not path.is_dir():
        pytest.skip(f"Missing PTDE DrawParam directory: {path}")
    return path


@pytest.fixture(scope="module")
def a15_bnd(draw_param_dir) -> DrawParamBND:
    return DrawParamBND.from_path(draw_param_dir / "a15_DrawParam.parambnd")


def test_vanilla_drawparam_files_exist(draw_param_dir):
    for stem in AREA_STEMS:
        assert (draw_param_dir / f"{stem}_DrawParam.parambnd").is_file(), f"Missing {stem}."
        assert not (draw_param_dir / f"{stem}_DrawParam.parambnd.dcx").is_file(), (
            "PTDE DrawParamBNDs must NOT be DCX-compressed."
        )


@pytest.mark.parametrize("stem", AREA_STEMS)
def test_vanilla_drawparambnd_loads_and_round_trips(draw_param_dir, stem, tmp_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        bnd = DrawParamBND.from_path(draw_param_dir / f"{stem}_DrawParam.parambnd")
    expected_area = "default" if stem == "default" else f"m{stem[1:]}"
    assert bnd.map_area == expected_area

    # Slot 0 must be fully populated; slot 1 only for `a15`.
    slot_0 = {k for k, v in bnd.draw_params_0.items() if v is not None}
    slot_1 = {k for k, v in bnd.draw_params_1.items() if v is not None}
    assert slot_0, f"{stem}: no slot-0 DrawParams loaded."
    assert (len(slot_1) > 0) == (stem in SLOT_1_AREAS), f"{stem}: unexpected slot-1 state."

    # unpack -> pack -> unpack must be stable.
    packed = bytes(bnd)
    out_path = tmp_path / f"{stem}_DrawParam.parambnd"
    bnd.write(out_path)
    assert out_path.is_file() and not out_path.with_suffix(".parambnd.dcx").is_file()
    with caplog.at_level(logging.CRITICAL):
        reloaded = DrawParamBND.from_path(out_path)
    assert bytes(reloaded) == packed, f"{stem}: DrawParamBND repack is not stable."
    assert reloaded.map_area == bnd.map_area
    assert {k for k, v in reloaded.draw_params_0.items() if v} == slot_0
    assert {k for k, v in reloaded.draw_params_1.items() if v} == slot_1


def test_vanilla_drawparam_stems_present(draw_param_dir, caplog):
    """Which DrawParam stems exist per BND is a load-bearing invariant for the slot-0 properties."""
    all_stems = set(DrawParamBND.PARAM_NICKNAMES.keys())
    for stem in AREA_STEMS:
        with caplog.at_level(logging.CRITICAL):
            bnd = DrawParamBND.from_path(draw_param_dir / f"{stem}_DrawParam.parambnd")
        present = {k for k, v in bnd.draw_params_0.items() if v is not None}
        if stem == "default":
            assert present == all_stems - AREA_ONLY_STEMS
        else:
            assert present == all_stems - DEFAULT_ONLY_STEMS


def test_absent_param_slots_are_none(draw_param_dir):
    bnd = DrawParamBND.from_path(draw_param_dir / "a15_DrawParam.parambnd")
    # `LodBank` only exists in `default_DrawParam`
    assert bnd.Lods_0 is None
    assert bnd.Lods_1 is None


def test_a15_slot_properties(a15_bnd):
    assert a15_bnd.BakedLight_0 is not None
    assert a15_bnd.BakedLight_1 is not None
    assert a15_bnd.DebugBakedLight_0 is not None
    assert a15_bnd.get_draw_param_slot("LightBank", 0) is a15_bnd.BakedLight_0
    assert a15_bnd.get_draw_param_slot("BakedLight", 0) is a15_bnd.BakedLight_0
    assert a15_bnd.get_draw_param_slot("BakedLight.param", 1) is a15_bnd.BakedLight_1


def test_a15_entry_names_use_slot_suffixes(a15_bnd):
    names = {entry.name for entry in a15_bnd.entries}
    assert "m15_LightBank.param" in names
    assert "m15_1_LightBank.param" in names
    assert "s15_LightBank.param" in names


def test_copy_slot_0_to_slot_1(draw_param_dir, caplog):
    with caplog.at_level(logging.CRITICAL):
        bnd = DrawParamBND.from_path(draw_param_dir / "a10_DrawParam.parambnd")
    assert all(v is None for v in bnd.draw_params_1.values())
    bnd.copy_slot_0_to_slot_1()
    for stem, draw_param in bnd.draw_params_0.items():
        if draw_param is None:
            continue
        assert bnd.draw_params_1[stem] is not None
        assert bnd.draw_params_1[stem] is not draw_param, "Must be a copy, not the same object."
        assert bytes(bnd.draw_params_1[stem]) == bytes(draw_param)
    # New entries must be generated with the '_1' slot suffix.
    names = {entry.name for entry in DrawParamBND.from_path(_write(bnd, caplog)).entries}
    assert "m10_1_LightBank.param" in names


def _write(bnd, caplog):
    import tempfile
    from pathlib import Path

    out = Path(tempfile.mkdtemp()) / "a10_DrawParam.parambnd"
    with caplog.at_level(logging.CRITICAL):
        bnd.write(out)
    return out


def test_drawparambnd_json_directory_round_trip(a15_bnd, tmp_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        a15_bnd.write_json_directory(tmp_path / "a15_DrawParam")
        reloaded = DrawParamBND.from_json_directory(tmp_path / "a15_DrawParam")
    assert reloaded.map_area == a15_bnd.map_area
    for slot in (0, 1):
        source = getattr(a15_bnd, f"draw_params_{slot}")
        target = getattr(reloaded, f"draw_params_{slot}")
        assert {k for k, v in source.items() if v} == {k for k, v in target.items() if v}
        for stem, draw_param in source.items():
            if draw_param is None:
                continue
            assert bytes(target[stem]) == bytes(draw_param), f"slot {slot} '{stem}' differs."


@pytest.mark.slow
def test_drawparam_directory_round_trip(draw_param_dir, tmp_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        directory = DrawParamDirectory.from_path(draw_param_dir)
    assert set(directory.files) == set(DrawParamDirectory.get_all_file_stems())
    assert directory.a15 is directory.files["a15_DrawParam"]
    assert directory["a15"] is directory.a15
    assert directory["a15_DrawParam"] is directory.a15
    assert directory.get_drawparambnd("m15") is directory.a15
    assert directory.get_drawparambnd("a15") is directory.a15
    assert directory.get_drawparambnd("default") is directory.files["default_DrawParam"]
    with pytest.raises(KeyError):
        directory.get_drawparambnd("a77")

    packed = {stem: bytes(bnd) for stem, bnd in directory.files.items()}
    out_dir = tmp_path / "DrawParam"
    out_dir.mkdir()
    with caplog.at_level(logging.CRITICAL):
        directory.write(out_dir)
        reloaded = DrawParamDirectory.from_path(out_dir)
    assert set(reloaded.files) == set(directory.files)
    for stem, bnd in reloaded.files.items():
        assert bytes(bnd) == packed[stem], f"{stem} not stable through directory round-trip."


def test_get_drawparambnd_accepts_full_stem(draw_param_dir, caplog):
    with caplog.at_level(logging.CRITICAL):
        directory = DrawParamDirectory.from_path(draw_param_dir)
    assert directory.get_drawparambnd("a15_DrawParam") is directory.a15
    assert directory.get_drawparambnd("a15_DrawParam.parambnd") is directory.a15


@pytest.mark.slow
def test_drawparam_directory_json_round_trip(draw_param_dir, tmp_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        directory = DrawParamDirectory.from_path(draw_param_dir)
        directory.write_json_directory(tmp_path / "json")
        reloaded = DrawParamDirectory.from_json_directory(tmp_path / "json")
    assert set(reloaded.files) == set(directory.files)
    for stem, bnd in reloaded.files.items():
        source = directory.files[stem]
        assert bnd.map_area == source.map_area
        for slot in (0, 1):
            src_params = getattr(source, f"draw_params_{slot}")
            new_params = getattr(bnd, f"draw_params_{slot}")
            for param_stem, draw_param in src_params.items():
                if draw_param is None:
                    continue
                assert bytes(new_params[param_stem]) == bytes(draw_param), (
                    f"{stem} slot {slot} '{param_stem}' differs after JSON round-trip."
                )
