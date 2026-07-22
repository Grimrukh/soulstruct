"""Bloodborne `game_types` tests.

`game_types` is the layer EVS scripts and MSB field metadata use to describe what an integer *means*
(a Character entity ID, a Flag, an ItemLot param row, an FMG text ID, ...). These are all pure-unit tests.
"""
from __future__ import annotations

import pytest

import soulstruct.bloodborne.game_types as bb_game_types
from soulstruct.bloodborne.game_types import map_types, param_types, sound_types, text_types
from soulstruct.bloodborne.game_types.game_enums_manager import GameEnumsManager
from soulstruct.bloodborne.maps.enums import MSBEventSubtype, MSBModelSubtype, MSBPartSubtype


def _module_all_names(module) -> list[str]:
    return list(getattr(module, "__all__", ()))


@pytest.mark.parametrize("module", [map_types, param_types, sound_types, text_types])
def test_all_exports_exist(module):
    """Every name in `__all__` must actually be defined (a broken `__all__` breaks `from ... import *`)."""
    missing = [name for name in _module_all_names(module) if not hasattr(module, name)]
    assert not missing, f"{module.__name__}.__all__ exports undefined names: {missing}"


def test_package_star_import_covers_submodules():
    """`soulstruct.bloodborne.game_types` re-exports all four submodules via star imports."""
    for module in (map_types, param_types, sound_types, text_types):
        missing = [name for name in _module_all_names(module) if not hasattr(bb_game_types, name)]
        assert not missing, f"Names from {module.__name__} not visible on package: {missing}"


def test_game_enums_manager_types_are_game_types():
    """Every `VALID_GAME_TYPES` entry must be importable from the `game_types` package."""
    for game_type in GameEnumsManager.VALID_GAME_TYPES:
        assert hasattr(bb_game_types, game_type.__name__), (
            f"`GameEnumsManager.VALID_GAME_TYPES` contains `{game_type.__name__}`, "
            f"which is not exported by `soulstruct.bloodborne.game_types`."
        )


def test_game_enums_manager_reserved_ids():
    """PLAYER is 10000 and there are nine client player slots (Bloodborne supports large co-op sessions)."""
    reserved = GameEnumsManager.RESERVED_GLOBAL_IDS
    assert reserved[10000] == "PLAYER"
    assert [reserved[10000 + i] for i in range(1, 10)] == [f"CLIENT_PLAYER_{i}" for i in range(1, 10)]
    assert GameEnumsManager.USE_AA_BB_ABBREVIATION is True


def test_reserved_ids_match_events_enums():
    """`events.enums` must define the same PLAYER/CLIENT_PLAYER_* constants as the enums manager."""
    from soulstruct.bloodborne.events import enums as bb_event_enums

    for entity_id, name in GameEnumsManager.RESERVED_GLOBAL_IDS.items():
        assert hasattr(bb_event_enums, name), f"`events.enums` has no `{name}`."
        assert getattr(bb_event_enums, name) == entity_id


@pytest.mark.parametrize(
    "subtypes, suffix, module_all",
    [
        (list(MSBPartSubtype), "", _module_all_names(map_types)),
        (list(MSBEventSubtype), "Event", _module_all_names(map_types)),
        (list(MSBModelSubtype), "", _module_all_names(map_types)),
    ],
)
@pytest.mark.xfail(
    reason="Bloodborne's `game_types/map_types.py` just does `from soulstruct.base.game_types.map_types "
           "import *` and hard-codes a DS1-era `__all__`. The Bloodborne-only MSB subtypes (WindVFX, "
           "PatrolRoute, DarkLock, Platoon, MultiSummon, ItemModel, OtherModel, OtherPart, OtherEvent) have "
           "no corresponding game type, so they cannot be referenced in EVS scripts or entity enums.",
    strict=False,
)
def test_every_msb_subtype_has_a_game_type(subtypes, suffix, module_all):
    missing = [
        subtype.name for subtype in subtypes
        if subtype.name not in module_all and f"{subtype.name}{suffix}" not in module_all
    ]
    assert not missing, f"MSB subtypes with no `game_types` entry: {missing}"


def test_sound_types_get_sound_enum():
    """Each `Sound` subclass maps to a `SoundType` enum value used by MSB sound events / EMEVD."""
    from soulstruct.bloodborne.events.enums import SoundType

    assert sound_types.MusicSound.get_sound_enum() == SoundType.m_Music
    assert sound_types.SFXSound.get_sound_enum() == SoundType.s_SFX
    with pytest.raises(NotImplementedError):
        sound_types.Sound.get_sound_enum()


@pytest.mark.xfail(
    reason="`bloodborne/game_types/sound_types.py` imports `SoundEvent` from "
           "`soulstruct.darksouls1ptde.game_types.map_types` -- a cross-game import in the Bloodborne "
           "package. It happens to resolve to the same shared base class today, but it makes Bloodborne "
           "depend on the DS1 package and will silently break if DS1 ever specialises `SoundEvent`.",
    strict=False,
)
def test_sound_types_does_not_import_from_darksouls1():
    import inspect

    source = inspect.getsource(sound_types)
    assert "darksouls1" not in source, "Cross-game import from `darksouls1ptde` in Bloodborne `sound_types`."


@pytest.mark.xfail(
    reason="`GemDropDopingParam.get_param_nickname()` (param_types.py:478) and "
           "`WindParam.get_param_nickname()` (param_types.py:576) both have a stray trailing comma, so they "
           "return a 1-tuple instead of a string.",
    strict=False,
)
def test_param_types_have_param_nicknames():
    """Every `BaseGameParam` subclass should report the Param nickname it indexes."""
    from soulstruct.base.game_types import BaseGameParam

    checked = 0
    for name in _module_all_names(param_types):
        game_type = getattr(param_types, name)
        if not (isinstance(game_type, type) and issubclass(game_type, BaseGameParam)):
            continue
        if game_type is BaseGameParam:
            continue
        try:
            nickname = game_type.get_param_nickname()
        except (NotImplementedError, ValueError):
            continue  # abstract intermediate class, or ambiguous (e.g. `AttackParam`)
        assert isinstance(nickname, str) and nickname, f"{name}.get_param_nickname() returned {nickname!r}."
        checked += 1
    assert checked > 10, "Expected many Bloodborne param game types."


@pytest.mark.xfail(
    reason="Three Bloodborne param game types return a nickname that `GameParamBND.PARAM_NICKNAMES` does not "
           "contain: `ActionButtonParam` returns 'ActionButtonPrompts' (the real nickname is 'ActionButtons'), "
           "and `GemDropDopingParam`/`WindParam` return 1-tuples because of a stray trailing comma.",
    strict=False,
)
def test_param_type_nicknames_exist_in_gameparambnd():
    """A param game type's nickname must be a real `GameParamBND` nickname, or GUI lookups fail."""
    from soulstruct.base.game_types import BaseGameParam
    from soulstruct.bloodborne.params import GameParamBND

    nicknames = set(GameParamBND.PARAM_NICKNAMES.values())
    bad = []
    for name in _module_all_names(param_types):
        game_type = getattr(param_types, name)
        if not (isinstance(game_type, type) and issubclass(game_type, BaseGameParam)) or game_type is BaseGameParam:
            continue
        try:
            nickname = game_type.get_param_nickname()
        except (NotImplementedError, ValueError):
            continue  # abstract intermediate class, or ambiguous nickname
        if nickname not in nicknames:
            bad.append(f"{name} -> '{nickname}'")
    assert not bad, f"Param game types whose nickname is not a Bloodborne param: {bad}"


def test_text_types_have_fmg_categories():
    """Every `Text` subclass must name an `MSGDirectory` category that actually exists."""
    from soulstruct.base.game_types import Text
    from soulstruct.bloodborne.text import MSGDirectory

    all_categories = set(MSGDirectory.GET_ALL_CATEGORIES())
    bad = []
    for name in _module_all_names(text_types):
        game_type = getattr(text_types, name)
        if not (isinstance(game_type, type) and issubclass(game_type, Text)) or game_type is Text:
            continue
        try:
            category = game_type.get_text_category()
        except (AttributeError, NotImplementedError):
            continue
        if category not in all_categories:
            bad.append(f"{name} -> '{category}'")
    assert not bad, f"Text game types with unknown FMG category: {bad}"
