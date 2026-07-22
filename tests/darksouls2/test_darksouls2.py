"""Dark Souls II (and DS2: Scholar of the First Sin) support.

`soulstruct.darksouls2` is very nearly a stub: it contains only `ezstate` (ESD classes) and
`models` (a `MatDef` shader definition, explicitly TODO-marked as "mostly just copied from
Bloodborne"). There is no MSB, no params, no text and no EMEVD support.

These tests pin the current shape of that stub so that any future expansion is deliberate, and
assert that the two `Game` entries in `soulstruct.games` do not advertise capabilities that
do not exist.

NOTE: `tests/darksouls2/test_flver.py` (FLVER round-trips using the committed `.flv` resources)
is owned by a different test module; nothing here touches FLVER.
"""
from __future__ import annotations

import importlib

import pytest

from soulstruct.games import DARK_SOULS_2, DARK_SOULS_2_SOTFS
from soulstruct.dcx import DCXType


# ---------------------------------------------------------------------------
# `Game` entries
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("game", [DARK_SOULS_2, DARK_SOULS_2_SOTFS], ids=lambda g: g.variable_name)
def test_ds2_games_declare_no_capabilities(game):
    """Neither DS2 `Game` declares file paths or bundled resources -- correct, since none work."""
    assert game.default_file_paths == {}, "DS2 now declares file paths -- update this test."
    assert game.bundled_resource_paths == {}, "DS2 now bundles resources -- update this test."
    assert game.default_dcx_type == DCXType.DCX_DFLT_10000_24_9


def test_ds2_and_sotfs_share_the_same_submodule():
    """`DARK_SOULS_2_SOTFS.submodule_name` is `darksouls2` (TODO in `games.py:229`)."""
    assert DARK_SOULS_2.submodule_name == DARK_SOULS_2_SOTFS.submodule_name == "darksouls2"
    assert DARK_SOULS_2.import_game_submodule() is DARK_SOULS_2_SOTFS.import_game_submodule()


def test_ds2_games_are_distinct_singletons():
    assert DARK_SOULS_2 != DARK_SOULS_2_SOTFS
    assert hash(DARK_SOULS_2) != hash(DARK_SOULS_2_SOTFS)
    assert set(DARK_SOULS_2.aliases).isdisjoint(DARK_SOULS_2_SOTFS.aliases)


def test_ds2_games_lack_steam_and_executable_metadata():
    """Documents currently-missing metadata (both games are launchable Steam titles)."""
    for game in (DARK_SOULS_2, DARK_SOULS_2_SOTFS):
        assert game.steam_appid is None
        assert game.executable_name == ""
        assert game.interroot_prefix == ""


# ---------------------------------------------------------------------------
# Package shape
# ---------------------------------------------------------------------------


def test_darksouls2_package_is_a_stub():
    package = importlib.import_module("soulstruct.darksouls2")
    # Root `__init__.py` is empty: sub-packages must be imported explicitly.
    for name in ("MSB", "EMEVD", "GameParamBND", "MSGDirectory"):
        assert not hasattr(package, name)


@pytest.mark.parametrize("submodule", ["maps", "params", "events", "text"])
def test_darksouls2_has_no_data_submodules(submodule: str):
    with pytest.raises(ImportError):
        importlib.import_module(f"soulstruct.darksouls2.{submodule}")


@pytest.mark.parametrize("submodule", ["ezstate", "models"])
def test_darksouls2_existing_submodules_import(submodule: str):
    module = importlib.import_module(f"soulstruct.darksouls2.{submodule}")
    assert module is not None


# ---------------------------------------------------------------------------
# EzState (ESD)
# ---------------------------------------------------------------------------


def test_ds2_esd_classes_configured():
    from soulstruct.darksouls2.ezstate.esd import ChrESD, TalkESD

    assert TalkESD.VERSION == ChrESD.VERSION == 2
    assert TalkESD.LONG_VARINTS is True
    assert TalkESD.ESD_TYPE.name == "TALK"
    assert ChrESD.ESD_TYPE.name == "CHR"


def test_ds2_esd_version_differs_from_ds3():
    from soulstruct.darksouls2.ezstate.esd import TalkESD as DS2TalkESD
    from soulstruct.darksouls3.ezstate import TalkESD as DS3TalkESD

    assert DS2TalkESD.VERSION == 2
    assert DS3TalkESD.VERSION == 3


def test_ds2_ezstate_reexports_esd_functions():
    """`ezstate/esd/__init__.py` star-imports the shared EzState function library."""
    esd_package = importlib.import_module("soulstruct.darksouls2.ezstate.esd")
    functions = importlib.import_module("soulstruct.base.ezstate.esd.functions")
    exported = [name for name in getattr(functions, "__all__", []) if not name.startswith("_")]
    assert exported, "Base EzState functions module exports nothing."
    missing = [name for name in exported if not hasattr(esd_package, name)]
    assert not missing, f"`darksouls2.ezstate.esd` did not re-export: {missing}"


def test_ds2_ezstate_package_all_missing_is_intentional():
    """`darksouls2/ezstate/__init__.py` is empty (unlike DS3's, which re-exports ESD classes)."""
    package = importlib.import_module("soulstruct.darksouls2.ezstate")
    ds3_package = importlib.import_module("soulstruct.darksouls3.ezstate")
    assert hasattr(ds3_package, "TalkESD")
    if not hasattr(package, "TalkESD"):
        pytest.xfail(
            "API inconsistency: `soulstruct.darksouls3.ezstate` exports `TalkESD`/`ChrESD` but "
            "`soulstruct.darksouls2.ezstate/__init__.py` is empty, so `from soulstruct.darksouls2."
            "ezstate import TalkESD` fails while the DS3 equivalent works."
        )


# ---------------------------------------------------------------------------
# Models / shaders
# ---------------------------------------------------------------------------


def test_ds2_matdef_is_exported():
    from soulstruct.darksouls2.models.shaders import MatDef

    assert MatDef.__name__ == "MatDef"
    assert hasattr(MatDef, "SAMPLER_ALIASES")
    assert hasattr(MatDef, "UVLayer")


def test_ds2_matdef_sampler_aliases_are_unique():
    from soulstruct.darksouls2.models.shaders import MatDef

    aliases = list(MatDef.SAMPLER_ALIASES.values())
    assert len(aliases) == len(set(aliases)), f"Duplicate DS2 sampler aliases: {aliases}"


def test_ds2_models_package_is_empty():
    """`darksouls2/models/__init__.py` is 0 bytes; only `shaders.MatDef` exists, un-re-exported.

    Every other game's `models/__init__.py` re-exports `FLVER`, `MTD`, `MatDef` and its Binder
    types, so `from soulstruct.darksouls2.models import MatDef` fails while the DeS/DS3 equivalents
    succeed.
    """
    models = importlib.import_module("soulstruct.darksouls2.models")
    assert not hasattr(models, "__all__")
    assert not hasattr(models, "MatDef")
    shaders = importlib.import_module("soulstruct.darksouls2.models.shaders")
    assert shaders.__all__ == ["MatDef"]


def test_ds2_has_no_binder_types():
    """Unlike every other supported game, DS2 defines no CHRBND/OBJBND/PARTSBND wrappers."""
    models = importlib.import_module("soulstruct.darksouls2.models")
    for name in ("CHRBND", "OBJBND", "PARTSBND", "MAPBND"):
        assert not hasattr(models, name)


# ---------------------------------------------------------------------------
# Sekiro (also a stub; checked here to keep the long tail in one place)
# ---------------------------------------------------------------------------


def test_sekiro_package_is_a_stub():
    from soulstruct.games import SEKIRO

    assert SEKIRO.default_file_paths == {}
    assert SEKIRO.bundled_resource_paths == {}
    assert SEKIRO.default_dcx_type == DCXType.DCX_KRAK
    package = importlib.import_module("soulstruct.sekiro")
    assert not hasattr(package, "MSB")


@pytest.mark.parametrize("submodule", ["maps", "params", "events", "text", "ezstate"])
def test_sekiro_has_no_data_submodules(submodule: str):
    with pytest.raises(ImportError):
        importlib.import_module(f"soulstruct.sekiro.{submodule}")


def test_sekiro_models_exports_flver_but_not_mapbnd():
    """`sekiro/models/__init__.py` `__all__` is just `["FLVER"]`, so `MAPBND` is unreachable."""
    models = importlib.import_module("soulstruct.sekiro.models")
    assert models.__all__ == ["FLVER"]
    assert not hasattr(models, "MAPBND"), "Sekiro `MAPBND` is now exported -- update this test."
    # The class does exist, just in an un-exported submodule.
    mapbnd_module = importlib.import_module("soulstruct.sekiro.models.mapbnd")
    assert mapbnd_module.MAPBND is not None


def test_sekiro_mapbnd_instantiates_and_builds_entry_paths():
    """Contrast with DS3's `MAPBND`, whose `default_factory` bug makes it un-instantiable."""
    from soulstruct.sekiro.models.mapbnd import MAPBND
    from soulstruct.games import SEKIRO

    mapbnd = MAPBND()
    assert mapbnd.v4_info is not None
    assert mapbnd.dcx_type == SEKIRO.default_dcx_type
    flver_path = mapbnd.get_flver_entry_path("m10_00_00_00_000000")
    assert flver_path.endswith("\\m10_00_00_00\\m10_00_00_00_000000\\m10_00_00_00_000000.flver")
    assert mapbnd.get_flver_S_entry_path("m10_00_00_00_000000").endswith("_000000_S.flver")
    with pytest.raises(TypeError):
        mapbnd.get_tpf_entry_path("m10_00_00_00_000000")
