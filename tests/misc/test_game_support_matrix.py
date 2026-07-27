"""Cross-game completeness / declared-capability audit.

These are all pure-unit tests: they need no unpacked game data, so they run everywhere.

They answer the question "which `Game` entries in `soulstruct.games` are genuinely supported, and
which are declared-but-hollow?" by checking that each declared capability actually resolves to
importable code and to bundled resource files that exist on disk.
"""
from __future__ import annotations

import importlib
import pkgutil

import pytest

from soulstruct.games import GAMES, Game, get_game

# Games whose Soulstruct submodule is known to be a stub/partial. Recorded here so that the
# "declared capability" tests below can be strict about the games that ARE supported without
# failing on the acknowledged long tail.
STUB_SUBMODULES = {"darksouls2", "sekiro"}


# ---------------------------------------------------------------------------
# `Game` registry sanity
# ---------------------------------------------------------------------------


def test_games_tuple_matches_module_globals():
    """Every `Game` singleton exported by `soulstruct.games` must appear in `GAMES`, and vice versa."""
    import soulstruct.games as games_module

    exported = {
        name for name in games_module.__all__
        if isinstance(getattr(games_module, name), Game)
    }
    in_tuple = {game.variable_name for game in GAMES}
    assert exported == in_tuple, f"`__all__` Game exports {exported} != `GAMES` {in_tuple}"


def test_game_variable_names_match_module_attribute_names():
    import soulstruct.games as games_module

    for game in GAMES:
        assert hasattr(games_module, game.variable_name), (
            f"`Game.variable_name` {game.variable_name!r} is not a module attribute."
        )
        assert getattr(games_module, game.variable_name) is game


def test_game_aliases_are_unique_and_normalised():
    """No two games may share an alias, and aliases must be lowercase with no spaces/punctuation."""
    seen = {}
    for game in GAMES:
        for alias in game.aliases:
            assert alias == alias.lower(), f"Alias {alias!r} of {game.variable_name} is not lowercase."
            assert not any(c in alias for c in " ':"), f"Alias {alias!r} contains punctuation/space."
            assert alias not in seen, f"Alias {alias!r} shared by {seen[alias]} and {game.variable_name}."
            seen[alias] = game.variable_name


@pytest.mark.parametrize("game", GAMES, ids=lambda g: g.variable_name)
def test_get_game_resolves_all_aliases_and_names(game: Game):
    assert get_game(game) is game
    assert get_game(game.variable_name.lower()) is game
    assert get_game(game.name.lower()) is game
    for alias in game.aliases:
        assert get_game(alias) is game


@pytest.mark.parametrize(
    "raw_name, expected",
    [
        ("Dark Souls 3", "DARK_SOULS_3"),
        ("demons souls", "DEMONS_SOULS"),
        ("Sekiro Shadows Die Twice", "SEKIRO"),
        ("dark souls 2", "DARK_SOULS_2"),
    ],
)
def test_get_game_normalises_human_readable_names(raw_name: str, expected: str):
    """`get_game` advertises that "spaces, case, apostrophes, and colons in aliases don't matter"."""
    assert get_game(raw_name).variable_name == expected


# ---------------------------------------------------------------------------
# Declared capabilities
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("game", GAMES, ids=lambda g: g.variable_name)
def test_bundled_resource_paths_exist_on_disk(game: Game):
    """Every `bundled_resource_paths` entry must point at a real file/dir inside the package."""
    for key, path in game.bundled_resource_paths.items():
        assert path.exists(), f"{game.variable_name} bundled resource {key!r} missing: {path}"


def test_at_least_one_game_declares_bundled_resources():
    """Guard against the parametrised test above silently passing because every dict is empty."""
    assert any(game.bundled_resource_paths for game in GAMES)


@pytest.mark.parametrize("game", GAMES, ids=lambda g: g.variable_name)
def test_submodule_name_is_importable(game: Game):
    """`Game.submodule_name` must name a real `soulstruct.<x>` package."""
    assert game.submodule_name, f"{game.variable_name} has no `submodule_name`."
    module = game.import_game_submodule()
    assert module.__name__ == f"soulstruct.{game.submodule_name}"


@pytest.mark.parametrize("game", GAMES, ids=lambda g: g.variable_name)
def test_default_file_paths_are_relative_posix_style(game: Game):
    """`default_file_paths` values are joined onto a game root, so they must be relative."""
    for key, rel_path in game.default_file_paths.items():
        assert isinstance(rel_path, str), f"{game.variable_name}:{key} is not a `str`."
        assert not rel_path.startswith(("/", "\\")), f"{game.variable_name}:{key} is absolute: {rel_path}"
        assert ":" not in rel_path, f"{game.variable_name}:{key} looks like a drive path: {rel_path}"


# Which `default_file_paths` key requires which game submodule to exist for the path to be usable.
_FILE_PATH_KEY_REQUIREMENTS = {
    "GameParamBND": "params",
    "ParamDefBND": "params",
    "DrawParamDirectory": "params",
    "MapStudioDirectory": "maps",
    "EventDirectory": "events",
    "MSGDirectory": "text",
    "TalkDirectory": "ezstate",
}


_DECLARED_PATH_GAMES = [
    pytest.param(
        game,
        marks=pytest.mark.xfail(
            reason="`DEMONS_SOULS` declares GameParamBND/ParamDefBND/DrawParamDirectory/MSGDirectory/"
                   "TalkDirectory paths but `soulstruct.demonssouls` has no `params`, `text` or "
                   "`ezstate` submodule (games.py:129-138).",
            strict=False,
        ) if game.variable_name == "DEMONS_SOULS" else (),
        id=game.variable_name,
    )
    for game in GAMES
]


@pytest.mark.parametrize("game", _DECLARED_PATH_GAMES)
def test_declared_file_paths_have_backing_submodules(game: Game):
    """A `Game` that advertises e.g. a `GameParamBND` path should have a `params` submodule.

    This is the "declared but hollow" check. Failures indicate a capability advertised to the GUI
    (`soulstruct.gui.base.core` looks up `game.default_file_paths[data_class_name]`) that Soulstruct
    cannot actually service.
    """
    missing = []
    for key, submodule in _FILE_PATH_KEY_REQUIREMENTS.items():
        if key not in game.default_file_paths:
            continue
        try:
            game.import_game_submodule(submodule)
        except ImportError:
            missing.append((key, submodule))
    assert not missing, (
        f"{game.variable_name} declares default_file_paths {[m[0] for m in missing]} but has no "
        f"`soulstruct.{game.submodule_name}.{{{','.join(m[1] for m in missing)}}}` submodule."
    )


def test_ds3_declares_no_file_paths_but_has_event_support():
    """Documents the current DS3 state: EMEVD works, but no `default_file_paths` are declared.

    DS3 has full EMEVD/EVS support (`soulstruct.darksouls3.events`) but `DARK_SOULS_3.default_file_paths`
    is empty, so the GUI cannot locate the event directory. If DS3 paths are ever added, this test
    should be updated (or deleted).
    """
    from soulstruct.games import DARK_SOULS_3

    assert DARK_SOULS_3.default_file_paths == {}, "DS3 now declares file paths -- update this test."
    assert DARK_SOULS_3.bundled_resource_paths == {}, "DS3 now bundles resources -- update this test."
    # But the events submodule is real:
    events = DARK_SOULS_3.import_game_submodule("events")
    assert hasattr(events, "EMEVD")


def test_ds3_has_no_msb_support():
    """DS3 `maps` package is constants-only: there is deliberately no MSB implementation."""
    maps = importlib.import_module("soulstruct.darksouls3.maps")
    assert not hasattr(maps, "MSB"), "DS3 MSB support was added -- update this test and `games.py`."
    assert hasattr(maps, "ALL_MAPS")


@pytest.mark.parametrize("submodule_name", sorted(STUB_SUBMODULES))
def test_stub_submodules_are_importable(submodule_name: str):
    """Even stub game packages must import cleanly (they are imported by `games.py` consumers)."""
    module = importlib.import_module(f"soulstruct.{submodule_name}")
    assert module is not None


# ---------------------------------------------------------------------------
# Import health sweep
# ---------------------------------------------------------------------------

AUDITED_PACKAGES = (
    "soulstruct.darksouls3",
    "soulstruct.demonssouls",
    "soulstruct.darksouls2",
    "soulstruct.sekiro",
)


def _walk_modules(package_name: str) -> list[str]:
    package = importlib.import_module(package_name)
    names = [package_name]
    if not hasattr(package, "__path__"):
        return names
    for info in pkgutil.walk_packages(package.__path__, package_name + "."):
        # Skip private "script" modules that execute game-directory work on import-time constants.
        if info.name.rsplit(".", 1)[-1].startswith("_"):
            continue
        names.append(info.name)
    return names


ALL_AUDITED_MODULES = sorted({name for pkg in AUDITED_PACKAGES for name in _walk_modules(pkg)})


def test_module_sweep_found_modules():
    assert len(ALL_AUDITED_MODULES) > 40, ALL_AUDITED_MODULES


@pytest.mark.parametrize("module_name", ALL_AUDITED_MODULES)
def test_public_module_imports_cleanly(module_name: str):
    """Catches broken re-exports and stale references in rarely-touched game packages."""
    importlib.import_module(module_name)


@pytest.mark.parametrize("module_name", ALL_AUDITED_MODULES)
def test_module_all_entries_are_defined(module_name: str):
    """Every name in a module's `__all__` must actually exist on the module."""
    module = importlib.import_module(module_name)
    declared = getattr(module, "__all__", None)
    if not declared:
        pytest.skip(f"{module_name} declares no `__all__`.")
    missing = [name for name in declared if not hasattr(module, name)]
    assert not missing, f"{module_name}.__all__ references undefined names: {missing}"


@pytest.mark.xfail(
    reason="`darksouls3.models.__all__` lists 'MTDBND' twice and omits the imported 'MAPBND'; "
           "`darksouls3.events(.enums).__all__` and `demonssouls.events.enums.__all__` list "
           "'OnRestBehavior' twice.",
    strict=False,
)
def test_no_module_all_has_duplicates():
    offenders = {}
    for module_name in ALL_AUDITED_MODULES:
        module = importlib.import_module(module_name)
        declared = getattr(module, "__all__", None)
        if not declared:
            continue
        duplicates = sorted({name for name in declared if declared.count(name) > 1})
        if duplicates:
            offenders[module_name] = duplicates
    assert not offenders, f"`__all__` duplicate entries: {offenders}"


def test_darksouls3_models_all_covers_star_imports():
    """`MAPBND` is imported by `darksouls3.models` but missing from its `__all__`."""
    import soulstruct.darksouls3.models as models

    assert hasattr(models, "MAPBND")
    if "MAPBND" not in models.__all__:
        pytest.xfail("`darksouls3/models/__init__.py:__all__` omits MAPBND (and duplicates MTDBND).")
