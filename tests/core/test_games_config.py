"""Tests for `soulstruct.games`, `soulstruct.config`, `soulstruct.exceptions` and `soulstruct.version`.

All pure unit tests -- no game installation required.
"""
from __future__ import annotations

import dataclasses
import json
from pathlib import Path

import pytest

from soulstruct import exceptions, version
from soulstruct.config import Config, SoulstructConfig
from soulstruct.dcx import DCXType
from soulstruct.games import (
    BLOODBORNE,
    DARK_SOULS_2,
    DARK_SOULS_2_SOTFS,
    DARK_SOULS_3,
    DARK_SOULS_DSR,
    DARK_SOULS_PTDE,
    DEMONS_SOULS,
    ELDEN_RING,
    GAMES,
    Game,
    SEKIRO,
    get_game,
)


# ---------------------------------------------------------------------------
# `Game` registry sanity
# ---------------------------------------------------------------------------


def test_games_tuple_is_complete_and_unique():
    assert len(GAMES) == 9
    variable_names = [g.variable_name for g in GAMES]
    assert len(set(variable_names)) == len(variable_names)
    abbreviations = [g.abbreviated_name for g in GAMES]
    assert len(set(abbreviations)) == len(abbreviations)


def test_game_aliases_are_globally_unique():
    """Two games sharing an alias would make `get_game()` raise 'Ambiguous game name'."""
    seen = {}
    for game in GAMES:
        for alias in game.aliases:
            assert alias not in seen, f"Alias '{alias}' used by both {seen.get(alias)} and {game.variable_name}."
            seen[alias] = game.variable_name


def test_game_hash_and_eq():
    assert DARK_SOULS_PTDE == DARK_SOULS_PTDE
    assert DARK_SOULS_PTDE != DARK_SOULS_DSR
    assert len({DARK_SOULS_PTDE, DARK_SOULS_PTDE, DARK_SOULS_DSR}) == 2
    assert repr(DARK_SOULS_PTDE) == 'Game("DARK_SOULS_PTDE")'


def test_game_eq_with_non_game():
    assert (DARK_SOULS_PTDE == "DARK_SOULS_PTDE") is False
    assert (DARK_SOULS_PTDE is None) is False
    assert DARK_SOULS_PTDE != 5


# ---------------------------------------------------------------------------
# `get_game`
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "name, expected",
    [
        ("ptde", DARK_SOULS_PTDE),
        ("darksouls1ptde", DARK_SOULS_PTDE),
        ("DARK_SOULS_PTDE", DARK_SOULS_PTDE),
        ("dsr", DARK_SOULS_DSR),
        ("ds1r", DARK_SOULS_DSR),
        ("darksoulsremastered", DARK_SOULS_DSR),
        ("dark souls: remastered", DARK_SOULS_DSR),
        ("des", DEMONS_SOULS),
        ("demonssouls", DEMONS_SOULS),
        ("demon's souls", DEMONS_SOULS),
        ("bb", BLOODBORNE),
        ("bloodborne", BLOODBORNE),
        ("ds3", DARK_SOULS_3),
        ("darksouls3", DARK_SOULS_3),
        ("dark souls iii", DARK_SOULS_3),
        ("sekiro", SEKIRO),
        ("sdt", SEKIRO),
        ("er", ELDEN_RING),
        ("elden ring", ELDEN_RING),
        ("sotfs", DARK_SOULS_2_SOTFS),
        ("ds2", DARK_SOULS_2),
    ],
)
def test_get_game_recognised_names(name: str, expected: Game):
    assert get_game(name) is expected


def test_get_game_is_case_insensitive():
    assert get_game("PTDE") is DARK_SOULS_PTDE
    assert get_game("Elden Ring") is ELDEN_RING


def test_get_game_passthrough():
    assert get_game(DARK_SOULS_PTDE) is DARK_SOULS_PTDE


@pytest.mark.parametrize("name", ["darksouls", "darksouls1", "dks", "ds1", "ds"])
def test_get_game_ambiguous_ds1(name: str):
    with pytest.raises(ValueError, match="Ambiguous"):
        get_game(name)


def test_get_game_invalid():
    with pytest.raises(ValueError, match="Invalid game name"):
        get_game("armored core")


@pytest.mark.parametrize(
    "name, expected",
    [
        ("dark souls remastered", DARK_SOULS_DSR),
        ("demons souls", DEMONS_SOULS),
        ("dark souls 3", DARK_SOULS_3),
        ("dark souls prepare to die edition", DARK_SOULS_PTDE),
    ],
)
def test_get_game_normalises_spacing_and_punctuation(name: str, expected: Game):
    assert get_game(name) is expected


# ---------------------------------------------------------------------------
# DCX type resolution per game
# ---------------------------------------------------------------------------


def test_default_dcx_types():
    assert DARK_SOULS_PTDE.default_dcx_type == DCXType.Null
    assert DARK_SOULS_DSR.default_dcx_type == DCXType.DCX_DFLT_10000_24_9
    assert BLOODBORNE.default_dcx_type == DCXType.DCX_DFLT_10000_44_9
    assert DARK_SOULS_3.default_dcx_type == DCXType.DCX_DFLT_10000_44_9
    assert SEKIRO.default_dcx_type == DCXType.DCX_KRAK
    assert ELDEN_RING.default_dcx_type == DCXType.DCX_KRAK
    assert DEMONS_SOULS.default_dcx_type == DCXType.DCX_EDGE


def test_get_dcx_type_special_overrides():
    # DSR MSBs are never DCX-compressed even though the game default is.
    assert DARK_SOULS_DSR.get_dcx_type(".msb") == DCXType.Null
    assert DARK_SOULS_DSR.get_dcx_type(".flver") == DCXType.DCX_DFLT_10000_24_9
    assert ELDEN_RING.get_dcx_type(".bin") == DCXType.Null
    assert DEMONS_SOULS.get_dcx_type(".hkx") == DCXType.Null


def test_process_dcx_path_adds_and_removes_extension():
    assert DARK_SOULS_DSR.process_dcx_path(Path("map/x.flver")).name == "x.flver.dcx"
    # `.msb` is a `special_dcx_types` Null override.
    assert DARK_SOULS_DSR.process_dcx_path(Path("map/x.msb")).name == "x.msb"
    assert DARK_SOULS_DSR.process_dcx_path(Path("map/x.msb.dcx")).name == "x.msb"
    assert DARK_SOULS_PTDE.process_dcx_path(Path("map/x.flver.dcx")).name == "x.flver"


def test_process_dcx_path_is_idempotent():
    once = ELDEN_RING.process_dcx_path(Path("chr/c0000.chrbnd"))
    assert ELDEN_RING.process_dcx_path(once) == once


def test_process_dcx_path_str_returns_str():
    result = DARK_SOULS_DSR.process_dcx_path("map/x.flver")
    assert isinstance(result, str) and result.endswith(".dcx")


def test_process_dcx_path_rejects_bad_type():
    with pytest.raises(TypeError):
        DARK_SOULS_DSR.process_dcx_path(123)


# ---------------------------------------------------------------------------
# Submodule import helpers
# ---------------------------------------------------------------------------


def test_import_game_submodule():
    module = DARK_SOULS_DSR.import_game_submodule("game_types")
    assert module.__name__ == "soulstruct.darksouls1r.game_types"


def test_import_game_submodule_without_submodule_name():
    game = Game(variable_name="X", name="X", abbreviated_name="x")
    with pytest.raises(AttributeError):
        game.import_game_submodule("maps")
    with pytest.raises(AttributeError):
        game.from_game_submodule_import("maps", "MSB")


def test_from_game_submodule_import_missing_name():
    with pytest.raises(ImportError):
        DARK_SOULS_DSR.from_game_submodule_import("game_types", "NoSuchThing")


def test_bundled_resource_paths_exist():
    """Every declared bundled resource must actually be shipped with the package."""
    missing = []
    for game in GAMES:
        for key, path in game.bundled_resource_paths.items():
            if not Path(path).exists():
                missing.append(f"{game.variable_name}.{key} -> {path}")
    assert not missing, "Missing bundled resources:\n  " + "\n  ".join(missing)


@pytest.mark.xfail(
    reason="DESIGN TRAP: `BaseBinaryFile.get_game()` matches `game.submodule_name in cls.__module__` and "
           "returns the FIRST hit in `GAMES`. `DARK_SOULS_2` and `DARK_SOULS_2_SOTFS` share the submodule "
           "name 'darksouls2', so SOTFS can never be detected from a class module.",
    strict=False,
)
def test_submodule_names_are_unique():
    submodules = [g.submodule_name for g in GAMES if g.submodule_name]
    assert len(set(submodules)) == len(submodules)


# ---------------------------------------------------------------------------
# `SoulstructConfig`
# ---------------------------------------------------------------------------


def test_config_singleton_fields_are_paths():
    for name in ("DES_PATH", "PTDE_PATH", "DSR_PATH", "ER_PATH", "LOG_PATH"):
        assert isinstance(getattr(Config, name), Path)


def test_config_to_dict_is_json_serialisable():
    data = Config.to_dict()
    json.dumps(data)  # must not raise
    for key, value in data.items():
        if key.endswith("_PATH"):
            assert isinstance(value, str)


def test_config_dict_roundtrip():
    data = Config.to_dict()
    restored = SoulstructConfig.from_dict(data)
    for f in dataclasses.fields(SoulstructConfig):
        assert getattr(restored, f.name) == getattr(Config, f.name), f.name


def test_config_from_dict_ignores_unknown_keys():
    cfg = SoulstructConfig.from_dict({"PTDE_PATH": "C:/whatever", "LEGACY_KEY": 1})
    assert cfg.PTDE_PATH == Path("C:/whatever")


def test_config_from_dict_empty_path_stays_string():
    cfg = SoulstructConfig.from_dict({"PARAMDEX_PATH": ""})
    assert cfg.PARAMDEX_PATH == ""


def test_config_update_rejects_unknown_key():
    cfg = SoulstructConfig()
    with pytest.raises(KeyError):
        cfg.update(NOT_A_FIELD=1)


def test_config_json_path():
    assert SoulstructConfig.json_path().name == "soulstruct_config.json"


def test_config_defaults_are_independent_instances():
    """`field(default_factory=...)` means two `SoulstructConfig`s must not share mutable state."""
    a, b = SoulstructConfig(), SoulstructConfig()
    assert a.PTDE_PATH == b.PTDE_PATH
    a.PTDE_PATH = Path("C:/changed")
    assert b.PTDE_PATH != a.PTDE_PATH


# ---------------------------------------------------------------------------
# Misc root modules
# ---------------------------------------------------------------------------


def test_exception_hierarchy():
    assert issubclass(exceptions.InvalidFieldValueError, exceptions.SoulstructError)
    assert issubclass(exceptions.RestoreBackupError, exceptions.SoulstructError)
    assert issubclass(exceptions.SoulstructError, Exception)


def test_dcx_error_is_soulstruct_error():
    from soulstruct.dcx.core import DCXError

    assert issubclass(DCXError, exceptions.SoulstructError)


def test_version_matches_pyproject():
    pyproject = Path(__file__).parents[2] / "pyproject.toml"
    if not pyproject.is_file():
        pytest.skip("pyproject.toml not found (installed package?).")
    for line in pyproject.read_text(encoding="utf-8").splitlines():
        if line.startswith("version = "):
            declared = line.split("=", 1)[1].strip().strip('"')
            assert version.__version__ == declared
            return
    pytest.skip("No `version` key found in pyproject.toml.")


def test_cli_app_commands_registered():
    """`soulstruct.__main__` builds the Typer CLI at import; make sure it still imports and has commands."""
    from soulstruct.__main__ import app

    names = {c.callback.__name__ for c in app.registered_commands}
    assert {"undcx", "binderpack", "binderunpack", "tpfpack", "tpfunpack"} <= names


def test_start_module_convenience_imports():
    import soulstruct.start as start

    assert set(start.__all__) == {"Path", "FLVER", "Binder", "DCXType", "compress", "decompress"}
    for name in start.__all__:
        assert hasattr(start, name)
