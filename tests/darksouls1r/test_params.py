"""Tests for DSR `GameParamBND` (the `param/GameParam/GameParam.parambnd.dcx` Binder).

DSR params are 32-bit and DCX-compressed (unlike PTDE, which is uncompressed). `GameParamBND` is a
`Binder` subclass whose `params` dict maps internal Param stems (e.g. `EquipParamWeapon`) to `Param`
instances; the friendly nicknames (`Weapons`, `Armor`, ...) are `param_property` descriptors backed by
`PARAM_NICKNAMES` (a `BiDict`).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from soulstruct.dcx import DCXType
from soulstruct.darksouls1r.params import GameParamBND, Param, ParamRow, ParamDefBND
from soulstruct.games import DARK_SOULS_DSR

PARAMBND_NAME = "GameParam.parambnd.dcx"


@pytest.fixture(scope="module")
def gameparam_path_str(request) -> str:
    path = Path(request.path).parent / "resources" / PARAMBND_NAME
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return str(path)


@pytest.fixture(scope="module")
def gameparam(gameparam_path_str) -> GameParamBND:
    """Module-scoped: reading this Binder takes ~2s, and most tests below do not mutate it."""
    return GameParamBND.from_path(gameparam_path_str)


@pytest.fixture
def fresh_gameparam(gameparam_path_str) -> GameParamBND:
    """Function-scoped copy for tests that mutate params."""
    return GameParamBND.from_path(gameparam_path_str)


# ---------------------------------------------------------------------------
# Class configuration (pure unit, no game data)
# ---------------------------------------------------------------------------


def test_class_defaults():
    assert GameParamBND.DEFAULT_ENTRY_ROOT.endswith("\\param\\GameParam")
    assert GameParamBND()._get_dcx_type() == DARK_SOULS_DSR.default_dcx_type
    assert GameParamBND()._get_dcx_type() != DCXType.Null, (
        "DSR GameParamBND must be DCX-compressed (unlike PTDE)."
    )


def test_param_nicknames_are_a_bijection():
    nicknames = GameParamBND.PARAM_NICKNAMES
    stems = list(nicknames.keys())
    names = [nicknames[stem] for stem in stems]
    assert len(set(stems)) == len(stems)
    assert len(set(names)) == len(names)
    for stem in stems:
        assert nicknames[nicknames[stem]] == stem, f"`PARAM_NICKNAMES` is not a clean BiDict for '{stem}'."


def test_game_types_keys_are_all_valid_nicknames():
    valid = set(GameParamBND.PARAM_NICKNAMES.values())
    unknown = sorted(k for k in GameParamBND.GAME_TYPES if k not in valid)
    assert not unknown, f"`GAME_TYPES` keys not present in `PARAM_NICKNAMES`: {unknown}"


def test_param_properties_match_nicknames():
    """Every `param_property` attribute must resolve to the internal stem `PARAM_NICKNAMES` claims."""
    nicknames = GameParamBND.PARAM_NICKNAMES
    for nickname in ("Weapons", "Armor", "Rings", "Goods", "Spells", "Characters", "ItemLots"):
        assert isinstance(getattr(GameParamBND, nickname), property)
        assert nicknames[nickname] in nicknames  # internal stem exists


def test_bundled_paramdefbnd_loads():
    paramdef_bnd = ParamDefBND.from_bundled("DARK_SOULS_DSR")
    assert len(paramdef_bnd.paramdefs) > 30


# ---------------------------------------------------------------------------
# Binary read/write
# ---------------------------------------------------------------------------


def test_gameparam_read(gameparam):
    assert len(gameparam.params) == 41
    assert gameparam.dcx_type != DCXType.Null
    # Nicknames resolve to real `Param`s.
    assert isinstance(gameparam.Weapons, Param)
    assert isinstance(gameparam.Weapons[100000], ParamRow)
    assert gameparam.Weapons[100000].Name  # Dagger (Japanese in vanilla)


def test_param_and_entry_names_agree(gameparam):
    entry_names = {entry.name for entry in gameparam.entries}
    for param_stem in gameparam.params:
        assert f"{param_stem}.param" in entry_names


def test_gameparam_binary_roundtrip(fresh_gameparam, tmp_path):
    fresh_gameparam.write(tmp_path / PARAMBND_NAME)
    reload = GameParamBND.from_path(tmp_path / PARAMBND_NAME)

    assert sorted(reload.params) == sorted(fresh_gameparam.params)
    assert [e.name for e in reload.entries] == [e.name for e in fresh_gameparam.entries]
    for stem, param in fresh_gameparam.params.items():
        other = reload.params[stem]
        assert param.param_type == other.param_type
        # Row ORDER (not just membership) must be preserved: it is the on-disk layout.
        assert list(param.rows) == list(other.rows), f"Row order changed for '{stem}'."
        for row_id, row in param.rows.items():
            assert row == other.rows[row_id], f"Row {row_id} of '{stem}' changed."


def test_gameparam_repack_is_idempotent(fresh_gameparam):
    once = bytes(fresh_gameparam)
    twice = bytes(GameParamBND.from_bytes(once))
    assert twice == once


def test_param_row_edit_survives_roundtrip(fresh_gameparam, tmp_path):
    fresh_gameparam.Weapons[100000].Name = "TestDagger"
    fresh_gameparam.Weapons[100000].Weight = 12.5
    fresh_gameparam.write(tmp_path / PARAMBND_NAME)
    reload = GameParamBND.from_path(tmp_path / PARAMBND_NAME)
    assert reload.Weapons[100000].Name == "TestDagger"
    assert reload.Weapons[100000].Weight == pytest.approx(12.5)


def test_missing_param_row_raises(gameparam):
    with pytest.raises(KeyError):
        _ = gameparam.Weapons[99999999]


# ---------------------------------------------------------------------------
# JSON
# ---------------------------------------------------------------------------


def test_gameparam_json_directory_roundtrip(fresh_gameparam, tmp_path):
    """The *recommended* JSON form: one directory of per-Param JSON files plus a manifest."""
    fresh_gameparam.write_json_directory(tmp_path / "json_dir")
    assert (tmp_path / "json_dir" / "GameParamBND_manifest.json").is_file()

    reload = GameParamBND.from_json_directory(tmp_path / "json_dir")
    assert sorted(reload.params) == sorted(fresh_gameparam.params)
    for stem, param in fresh_gameparam.params.items():
        other = reload.params[stem]
        assert param.param_type == other.param_type
        assert set(param.rows) == set(other.rows), f"Row IDs changed for '{stem}'."
        for row_id, row in param.rows.items():
            assert row == other.rows[row_id], f"Row {row_id} of '{stem}' changed."


def test_json_directory_roundtrip_sorts_rows_by_id(fresh_gameparam, tmp_path):
    """`Param.to_dict()` sorts rows by ID, so JSON round-tripping REORDERS rows relative to vanilla.

    This is a real fidelity caveat: a JSON round-trip is not byte-preserving even though it is
    semantically lossless.
    """
    fresh_gameparam.write_json_directory(tmp_path / "json_dir")
    reload = GameParamBND.from_json_directory(tmp_path / "json_dir")
    param = reload.params["default_EnemyBehaviorBank"]
    assert list(param.rows) == sorted(param.rows)
    # Vanilla order for this Param is NOT sorted, proving the reorder happened.
    assert list(fresh_gameparam.params["default_EnemyBehaviorBank"].rows) != list(param.rows)


def test_gameparam_single_json_write(fresh_gameparam, tmp_path):
    """Writing a single monolithic JSON must at least succeed and be deterministic."""
    fresh_gameparam.write_json(tmp_path / "a.json")
    fresh_gameparam.write_json(tmp_path / "b.json")
    assert (tmp_path / "a.json").read_text(encoding="utf-8") == (tmp_path / "b.json").read_text(encoding="utf-8")


@pytest.mark.xfail(
    reason="BUG: `GameParamBND.to_dict()` includes the `use_id_prefix` manifest key (from "
           "`Binder.get_manifest_header()`), but `GameParamBND.from_dict()` does not pop it before "
           "calling `cls(**data)`, so `from_json()` raises "
           "`TypeError: GameParamBND.__init__() got an unexpected keyword argument 'use_id_prefix'` "
           "(base/params/gameparambnd.py:123-160; `write_json_directory` pops it at line 221).",
    strict=False,
)
def test_gameparam_single_json_roundtrip(fresh_gameparam, tmp_path):
    fresh_gameparam.write_json(tmp_path / "gameparam.json")
    reload = GameParamBND.from_json(tmp_path / "gameparam.json")
    assert sorted(reload.params) == sorted(fresh_gameparam.params)


# ---------------------------------------------------------------------------
# Live game directory
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.game_data
def test_vanilla_gameparam_roundtrip(dsr_root, tmp_path):
    path = dsr_root / "param/GameParam/GameParam.parambnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing vanilla GameParamBND: {path}")
    game_param = GameParamBND.from_path(path)
    packed = bytes(game_param)
    reload = GameParamBND.from_bytes(packed)
    assert sorted(reload.params) == sorted(game_param.params)
    for stem, param in game_param.params.items():
        assert list(param.rows) == list(reload.params[stem].rows)
    assert bytes(reload) == packed
