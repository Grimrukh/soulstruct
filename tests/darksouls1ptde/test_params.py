"""Tests for DS1 PTDE `GameParamBND` (the main `param/GameParam/GameParam.parambnd`).

Rewritten from the original `unittest` module; intent preserved (read bundled ParamDefBND, open the
committed vanilla `GameParam.parambnd`, round-trip it through binary and JSON), plus pure-unit
consistency checks on the nickname/property/game-type tables.
"""
from __future__ import annotations

import logging

import pytest

from soulstruct.containers import BinderVersion
from soulstruct.darksouls1ptde.params import GameParamBND, ParamDefBND
from soulstruct.darksouls1ptde.params import paramdef
from soulstruct.darksouls1ptde.game_types.param_types import BaseGameParam
from soulstruct.dcx import DCXType


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def paramdef_bnd() -> ParamDefBND:
    return ParamDefBND.from_bundled("DARK_SOULS_PTDE")


@pytest.fixture(scope="module")
def gameparam_path(request):
    path = request.path.parent / "resources" / "GameParam.parambnd"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


@pytest.fixture(scope="module")
def gameparam(gameparam_path) -> GameParamBND:
    return GameParamBND.from_path(gameparam_path)


# ---------------------------------------------------------------------------
# Pure-unit: class table consistency
# ---------------------------------------------------------------------------


def test_param_nicknames_are_bijective():
    nicknames = GameParamBND.PARAM_NICKNAMES
    keys = list(nicknames.keys())
    values = list(nicknames.values())
    assert len(keys) == len(set(keys)), "Duplicate internal param names."
    assert len(values) == len(set(values)), "Duplicate param nicknames."
    for key in keys:
        assert nicknames[nicknames[key]] == key


def test_every_nickname_has_a_property():
    """`param_property` getters must exist for every nickname, since the GUI/API uses them."""
    for internal_name, nickname in GameParamBND.PARAM_NICKNAMES.items():
        assert isinstance(getattr(GameParamBND, nickname, None), property), (
            f"`GameParamBND.{nickname}` property missing (internal name '{internal_name}')."
        )


def test_game_types_keys_are_valid_nicknames():
    for nickname, game_type in GameParamBND.GAME_TYPES.items():
        assert nickname in GameParamBND.PARAM_NICKNAMES.values(), (
            f"`GAME_TYPES` key '{nickname}' is not a known param nickname."
        )
        assert isinstance(game_type, type) and issubclass(game_type, BaseGameParam), (
            f"`GAME_TYPES['{nickname}']` is not a `BaseGameParam` subclass: {game_type}"
        )


def test_ptde_binder_configuration():
    assert GameParamBND.EXT == ".parambnd"
    assert GameParamBND.IS_SPLIT_BXF is False
    # NOTE: the class-level `version`/`v4_info`/`dcx_type` assignments are shadowed by the Binder
    # dataclass fields. `version` happens to be re-applied (V3), but `v4_info = None` is DEAD: a
    # fresh instance still gets a default `BinderVersion4Info`. Harmless for V3 Binders (v4_info is
    # only packed for V4) but misleading.
    assert GameParamBND().version == BinderVersion.V3
    assert GameParamBND().v4_info is not None  # documents the dead `v4_info = None` assignment
    # PTDE is uncompressed (DSR uses DCX).
    assert GameParamBND()._get_dcx_type() == DCXType.Null
    assert GameParamBND.PARAMDEF_MODULE is paramdef


def test_paramdef_module_has_row_type_for_every_param(paramdef_bnd):
    """Every param type in the bundled ParamDefBND should have a generated row class."""
    missing = [name for name in paramdef_bnd.paramdefs if not hasattr(paramdef, name)]
    assert not missing, f"`params.paramdef` is missing row classes: {missing}"


# ---------------------------------------------------------------------------
# Bundled ParamDefBND
# ---------------------------------------------------------------------------


def test_bundled_paramdefbnd_loads(paramdef_bnd):
    assert len(paramdef_bnd.paramdefs) > 30
    assert "EQUIP_PARAM_WEAPON_ST" in paramdef_bnd.paramdefs
    assert "LIGHT_BANK" in paramdef_bnd.paramdefs  # DrawParam types live here too


def test_bundled_paramdefbnd_is_cached(paramdef_bnd):
    assert ParamDefBND.from_bundled("DARK_SOULS_PTDE") is paramdef_bnd


# ---------------------------------------------------------------------------
# Committed vanilla GameParam.parambnd
# ---------------------------------------------------------------------------


def test_gameparam_loads_all_params(gameparam):
    assert set(gameparam.params) == set(GameParamBND.PARAM_NICKNAMES.keys())
    for name, param in gameparam.params.items():
        assert param.rows, f"Param '{name}' has no rows."


def test_gameparam_nickname_properties_work(gameparam):
    assert gameparam.Weapons is gameparam.params["EquipParamWeapon"]
    assert gameparam.Armor is gameparam.params["EquipParamProtector"]
    assert gameparam.Bosses is gameparam.params["GameAreaParam"]
    # Dagger (weapon 100000) exists in vanilla DS1.
    assert 100000 in gameparam.Weapons.rows


def test_gameparam_row_field_access(gameparam):
    dagger = gameparam.Weapons[100000]
    assert isinstance(dagger.Name, str)
    assert hasattr(dagger, "Weight"), "Weapon rows should expose PARAMDEF fields as attributes."
    assert dagger.Weight > 0.0


@pytest.mark.slow
def test_gameparam_binary_round_trip(gameparam, tmp_path, caplog):
    """unpack -> pack -> unpack must be stable for every param."""
    with caplog.at_level(logging.CRITICAL):
        packed = bytes(gameparam)
        out_path = tmp_path / "GameParam.parambnd"
        gameparam.write(out_path)
        reloaded = GameParamBND.from_path(out_path)
    assert not (tmp_path / "GameParam.parambnd.dcx").is_file(), "PTDE params must not be DCX."
    assert set(reloaded.params) == set(gameparam.params)
    for name, param in gameparam.params.items():
        assert bytes(reloaded.params[name]) == bytes(param), f"Param '{name}' not stable."
    assert bytes(reloaded) == packed


@pytest.mark.slow
def test_gameparam_json_directory_round_trip(gameparam_path, tmp_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        gameparam = GameParamBND.from_path(gameparam_path)
        gameparam.write_json_directory(tmp_path / "json")
        reloaded = GameParamBND.from_json_directory(tmp_path / "json")
    assert set(reloaded.params) == set(gameparam.params)
    for name, param in gameparam.params.items():
        assert bytes(reloaded.params[name]) == bytes(param), (
            f"Param '{name}' differs after JSON round-trip."
        )


@pytest.mark.slow
@pytest.mark.xfail(
    reason=(
        "PTDE `GameParamBND.DEFAULT_ENTRY_ROOT` is 'N:\\FRPG\\data\\Param\\GameParam' but real PTDE "
        "entries live at 'N:\\FRPG\\data\\INTERROOT_win32\\param\\GameParam'. `entry_autogen()` matches "
        "existing entries by PATH, so packing appends a second copy of every Param: 38 entries "
        "become 76 and the written file doubles in size."
    ),
    strict=False,
)
def test_gameparam_pack_does_not_duplicate_entries(gameparam_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        gameparam = GameParamBND.from_path(gameparam_path)
        original_entry_count = len(gameparam.entries)
        packed = bytes(gameparam)
    assert len(gameparam.entries) == original_entry_count, (
        f"Packing changed Binder entry count: {original_entry_count} -> {len(gameparam.entries)}."
    )
    assert len(packed) < gameparam_path.stat().st_size * 1.1


@pytest.mark.xfail(
    reason=(
        "PTDE `GameParamBND.DEFAULT_ENTRY_ROOT` does not match the vanilla entry root; see "
        "`test_gameparam_pack_does_not_duplicate_entries`."
    ),
    strict=False,
)
def test_gameparam_default_entry_root_matches_vanilla(gameparam):
    """The Binder entry root must match vanilla, or `entry_autogen()` creates duplicate entries."""
    vanilla_roots = {entry.path.rsplit("\\", 1)[0] for entry in gameparam.entries}
    assert len(vanilla_roots) == 1, f"Mixed entry roots in vanilla GameParam: {vanilla_roots}"
    vanilla_root = next(iter(vanilla_roots))
    assert GameParamBND.DEFAULT_ENTRY_ROOT == vanilla_root, (
        f"`DEFAULT_ENTRY_ROOT` is {GameParamBND.DEFAULT_ENTRY_ROOT!r} but vanilla PTDE uses "
        f"{vanilla_root!r}; `entry_autogen()` will duplicate every entry."
    )


def test_rename_entries_from_text_rejects_bad_nickname(gameparam):
    with pytest.raises(ValueError):
        gameparam.rename_entries_from_text(None, param_nickname="Bullets")


# ---------------------------------------------------------------------------
# Live game directory (optional)
# ---------------------------------------------------------------------------


@pytest.mark.slow
def test_vanilla_gameparam_from_game_directory(ptde_root, caplog):
    path = ptde_root / "param" / "GameParam" / "GameParam.parambnd"
    if not path.is_file():
        pytest.skip(f"Missing vanilla GameParam: {path}")
    with caplog.at_level(logging.CRITICAL):
        gameparam = GameParamBND.from_path(path)
    assert set(gameparam.params) == set(GameParamBND.PARAM_NICKNAMES.keys())
    assert gameparam._get_dcx_type() == DCXType.Null
