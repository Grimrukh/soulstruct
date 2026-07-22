"""Bloodborne `GameParamBND` tests.

Rewritten from the old `unittest` module. Original intent preserved: read the committed vanilla
`gameparam.parambnd.dcx`, write it, re-read it, and compare every row; then do the same via JSON.
All output goes to `tmp_path`.
"""
from __future__ import annotations

import pytest

from soulstruct.bloodborne.params import GameParamBND, ParamDefBND
from soulstruct.bloodborne.params import paramdef as bb_paramdef

PARAMBND_NAME = "gameparam.parambnd.dcx"


# ---------------------------------------------------------------------------
# Pure-unit checks on the class registry (always run)
# ---------------------------------------------------------------------------


def test_paramdef_bnd_bundled_loads():
    """Soulstruct ships a `.paramdefbnd` for Bloodborne."""
    paramdef_bnd = ParamDefBND.from_bundled("BLOODBORNE")
    assert len(paramdef_bnd.paramdefs) > 0
    # Bloodborne renamed DS1's `FACE_PARAM_ST` to `FACE_GEN_PARAM_ST` and added a NEW `FACE_PARAM_ST`.
    assert hasattr(bb_paramdef, "FACE_GEN_PARAM_ST")
    assert hasattr(bb_paramdef, "FACE_PARAM_ST")
    assert bb_paramdef.FACE_GEN_PARAM_ST is not bb_paramdef.FACE_PARAM_ST


def test_param_nicknames_are_bijective():
    """`PARAM_NICKNAMES` is a `BiDict`, so both directions must be unique."""
    names = list(GameParamBND.PARAM_NICKNAMES.keys())
    nicknames = list(GameParamBND.PARAM_NICKNAMES.values())
    assert len(set(names)) == len(names)
    assert len(set(nicknames)) == len(nicknames)


def _param_properties() -> dict[str, str]:
    """Map property name -> the `param_stem` string captured by `param_property`."""
    properties = {}
    for name, value in vars(GameParamBND).items():
        if not isinstance(value, property) or value.fget is None:
            continue
        closure = value.fget.__closure__
        if not closure:
            continue
        stem = closure[0].cell_contents
        if isinstance(stem, str):
            properties[name] = stem
    return properties


@pytest.mark.xfail(
    reason="26 of Bloodborne's `param_property(...)` calls pass the Soulstruct NICKNAME instead of the "
           "internal Binder entry stem (e.g. `AISounds = param_property(\"AISounds\")` instead of "
           "`param_property(\"AiSoundParam\")`), so `GameParamBND.AISounds` raises `KeyError`.",
    strict=False,
)
def test_param_property_stems_are_internal_param_names():
    internal_names = set(GameParamBND.PARAM_NICKNAMES.keys())
    bad = {name: stem for name, stem in _param_properties().items() if stem not in internal_names}
    assert not bad, f"`param_property` args that are not internal param names: {bad}"


def test_every_nickname_has_a_property():
    """Every `PARAM_NICKNAMES` value should be the name of a getter property on the class."""
    properties = set(_param_properties())
    missing = sorted(set(GameParamBND.PARAM_NICKNAMES.values()) - properties)
    assert not missing, f"Nicknames with no `param_property`: {missing}"


@pytest.mark.xfail(
    reason="`GAME_TYPES` keys must be `PARAM_NICKNAMES` values (they drive GUI ordering). Bloodborne has "
           "'Accessories'/'ActionButtonPrompts' keys that are not nicknames, and is missing "
           "'Rings'/'ActionButtons'/'Knockbacks'/'Ragdolls'.",
    strict=False,
)
def test_game_types_keys_are_nicknames():
    nicknames = set(GameParamBND.PARAM_NICKNAMES.values())
    unknown = sorted(set(GameParamBND.GAME_TYPES) - nicknames)
    missing = sorted(nicknames - set(GameParamBND.GAME_TYPES))
    assert not unknown and not missing, f"unknown GAME_TYPES keys: {unknown}; nicknames missing: {missing}"


@pytest.mark.xfail(
    reason="Bloodborne `GameParamBND` does not define `DEFAULT_ENTRY_ROOT` (DS1/ER do), so "
           "`entry_autogen()` raises `BinderError` and the Binder can never be written back out.",
    strict=False,
)
def test_default_entry_root_defined():
    assert getattr(GameParamBND, "DEFAULT_ENTRY_ROOT", None), "No `DEFAULT_ENTRY_ROOT` on Bloodborne GameParamBND."


# ---------------------------------------------------------------------------
# Committed vanilla `gameparam.parambnd.dcx`
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def vanilla_params(request) -> GameParamBND:
    from pathlib import Path

    path = Path(request.path).parent / "resources" / PARAMBND_NAME
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return GameParamBND.from_path(path)


def test_gameparambnd_loads(vanilla_params):
    assert len(vanilla_params.params) > 50
    assert "EquipParamWeapon" in vanilla_params.params
    assert len(vanilla_params.params["EquipParamWeapon"].rows) > 0


def test_gameparambnd_dcx_type(vanilla_params):
    from soulstruct.dcx import DCXType

    assert vanilla_params.dcx_type == DCXType.DCX_DFLT_10000_44_9


def test_all_params_are_typed(vanilla_params):
    """No entry should fall back to the untyped `ParamDict`, which means a missing `paramdef` module."""
    from soulstruct.base.params.param_dict import ParamDict

    untyped = [stem for stem, param in vanilla_params.params.items() if isinstance(param, ParamDict)]
    assert not untyped, f"Params with no Soulstruct `paramdef` row class: {untyped}"


@pytest.mark.xfail(
    reason="Several vanilla Bloodborne param entries have no `PARAM_NICKNAMES` mapping "
           "(NewMenuColorTableParam, MenuValueTableParam, ResidentFxParam, Wind, QwcChange, QwcJudge, "
           "SkeletonParam, default_AIStandardInfoBank, default_EnemyBehaviorBank), and three mapped names "
           "(MenuValueTableSpecParam, ResidentVFXParam, WindParam) do not exist in the game at all. "
           "`write_json_directory()` therefore raises `KeyError`.",
    strict=False,
)
def test_every_vanilla_param_has_a_nickname(vanilla_params):
    unmapped = [stem for stem in vanilla_params.params if stem not in GameParamBND.PARAM_NICKNAMES.keys()]
    unused = [name for name in GameParamBND.PARAM_NICKNAMES.keys() if name not in vanilla_params.params]
    assert not unmapped and not unused, f"unmapped: {unmapped}; nicknames for missing params: {unused}"


@pytest.mark.slow
@pytest.mark.xfail(
    reason="Bloodborne `GameParamBND` has no `DEFAULT_ENTRY_ROOT`, so `entry_autogen()` (called by "
           "`to_writer()`) raises `BinderError: Neither DEFAULT_ENTRY_ROOT nor get_default_entry_path() "
           "are defined on this Binder class: GameParamBND`.",
    strict=False,
)
def test_gameparambnd_binary_roundtrip(vanilla_params, tmp_path):
    """unpack -> pack -> unpack, comparing every row of every param."""
    written = vanilla_params.write(tmp_path / PARAMBND_NAME)
    reloaded = GameParamBND.from_path(written[0])

    assert sorted(reloaded.params) == sorted(vanilla_params.params)
    for stem, source_param in vanilla_params.params.items():
        reload_param = reloaded.params[stem]
        assert len(source_param.rows) == len(reload_param.rows), f"Row count differs for '{stem}'."
        for row_id, reload_row in reload_param.items():
            assert source_param[row_id] == reload_row, (
                f"Param {source_param.param_type}, row {row_id}\n{source_param[row_id].compare(reload_row)}"
            )


@pytest.mark.slow
@pytest.mark.xfail(
    reason="`write_json_directory()` looks up `PARAM_NICKNAMES[param_stem]` for every param, and several "
           "vanilla Bloodborne param stems have no nickname, so it raises `KeyError`.",
    strict=False,
)
def test_gameparambnd_json_roundtrip(vanilla_params, tmp_path):
    """JSON directory write -> read -> write must be idempotent."""
    first_dir = tmp_path / "json_1"
    vanilla_params.write_json_directory(first_dir)
    from_json = GameParamBND.from_json_directory(first_dir)

    second_dir = tmp_path / "json_2"
    from_json.write_json_directory(second_dir)

    for json_path in sorted(first_dir.glob("*.json")):
        other = second_dir / json_path.name
        assert other.is_file(), f"Missing re-written JSON file: {other.name}"
        assert json_path.read_text(encoding="utf-8") == other.read_text(encoding="utf-8"), (
            f"JSON differs after round-trip: {json_path.name}"
        )


# ---------------------------------------------------------------------------
# Game data (skipped unless Bloodborne is installed)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
@pytest.mark.slow
def test_vanilla_installed_params_load(bb_root):
    path = bb_root / "param/gameparam/gameparam.parambnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing vanilla GameParamBND: {path}")
    game_param = GameParamBND.from_path(path)
    assert len(game_param.params) > 50
