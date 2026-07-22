"""Demon's Souls event support.

IMPORTANT: `soulstruct.demonssouls.events` is currently **enums only**. There is no `EMEVD` class,
no EMEDF, no EVS parser and no `EventDirectory` for Demon's Souls, even though
`DEMONS_SOULS.default_file_paths` advertises an `EventDirectory`. These tests pin down what does
exist and document what does not.
"""
from __future__ import annotations

import importlib
from enum import IntEnum

import pytest

from soulstruct.demonssouls.events import enums as des_enums
from soulstruct.games import DEMONS_SOULS


def test_events_package_is_enums_only():
    events = importlib.import_module("soulstruct.demonssouls.events")
    # `events/__init__.py` is empty: the enums module must be imported explicitly.
    assert not hasattr(events, "EMEVD")
    assert not hasattr(events, "EventDirectory")
    # `events/__init__.py` is literally empty (0 bytes); `enums` only appears as an attribute
    # because this test module imports it directly.
    assert events.__file__.endswith("__init__.py")
    assert "EMEVD" not in dir(events)


@pytest.mark.parametrize("submodule", ["emevd", "event_directory", "utilities"])
def test_des_has_no_emevd_implementation(submodule: str):
    with pytest.raises(ImportError):
        importlib.import_module(f"soulstruct.demonssouls.events.{submodule}")


def test_des_declares_an_event_directory_it_cannot_read():
    """Documents the declared-but-hollow capability (see `tests/misc/test_game_support_matrix.py`)."""
    assert DEMONS_SOULS.default_file_paths["EventDirectory"] == "event"
    with pytest.raises(ImportError):
        DEMONS_SOULS.from_game_submodule_import("events", "EMEVD")


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


def test_enums_all_is_complete():
    missing = [name for name in des_enums.__all__ if not hasattr(des_enums, name)]
    assert not missing, missing


def test_every_public_enum_class_is_exported():
    """No enum class defined in `enums.py` may be missing from `__all__`."""
    declared = set(des_enums.__all__)
    unexported = [
        name for name, obj in vars(des_enums).items()
        if isinstance(obj, type) and issubclass(obj, IntEnum) and not name.startswith("_")
        and obj.__module__ == des_enums.__name__ and name not in declared
    ]
    # These are defined but deliberately not exported by `__all__` (unused by any EMEVD parser yet).
    known_unexported = {
        "MessageCategory", "InfoMenuType", "TalkAttribute", "PlayerDeathType",
        "SummonParamType", "InvadeType",
    }
    assert set(unexported) <= known_unexported, (
        f"New enum classes are not exported by `demonssouls.events.enums.__all__`: "
        f"{sorted(set(unexported) - known_unexported)}"
    )


def test_condition_group_has_main_and_symmetric_slots():
    condition_group = des_enums.ConditionGroup
    values = {int(member) for member in condition_group}
    assert 0 in values, "`MAIN` (0) missing from `ConditionGroup`."
    positives = {v for v in values if v > 0}
    negatives = {-v for v in values if v < 0}
    assert positives == negatives, f"AND/OR condition slots are asymmetric: {sorted(values)}"


def test_reserved_player_ids_match_game_enums_manager():
    from soulstruct.demonssouls.game_types.game_enums_manager import GameEnumsManager

    assert des_enums.PLAYER == 10000
    for i in range(1, 10):
        assert getattr(des_enums, f"CLIENT_PLAYER_{i}") == 10000 + i
    assert GameEnumsManager.RESERVED_GLOBAL_IDS[10000] == "PLAYER"


@pytest.mark.parametrize(
    "enum_name",
    [
        "AIStatusType", "BitOperation", "ButtonType", "CharacterType", "ComparisonType",
        "CoordEntityType", "FlagSetting", "FlagType", "ItemType", "OnOffChange", "SoundType",
        "TeamType", "TriggerAttribute", "WorldTendencyType",
    ],
)
def test_enum_member_values_are_unique(enum_name: str):
    """Duplicate values silently alias members (a classic copy-paste bug in these tables)."""
    enum_cls = getattr(des_enums, enum_name)
    members = list(enum_cls.__members__.items())
    aliases = [name for name, member in members if member.name != name]
    assert not aliases, f"{enum_name} has aliased members (duplicate values): {aliases}"


def test_item_type_matches_param_types():
    """DeS `game_types` item params must map onto `ItemType` members."""
    from soulstruct.demonssouls.game_types import (
        AccessoryParam, ArmorParam, GoodParam, WeaponParam,
    )

    mapping = {
        WeaponParam: des_enums.ItemType.Weapon,
        ArmorParam: des_enums.ItemType.Armor,
        AccessoryParam: des_enums.ItemType.Ring,
        GoodParam: des_enums.ItemType.Good,
    }
    for param_cls, expected in mapping.items():
        assert param_cls.get_item_enum() == expected


def test_sound_types_align_with_msb_sound_event_default():
    """`MSBSoundEvent.sound_type` defaults to `SoundType.m_Music.value`."""
    from soulstruct.demonssouls.maps.events import MSBSoundEvent

    sound_event = MSBSoundEvent(name="s0")
    assert sound_event.sound_type == des_enums.SoundType.m_Music.value


def test_game_enums_manager_valid_game_types_are_exported():
    import soulstruct.demonssouls.game_types as des_game_types
    from soulstruct.demonssouls.game_types.game_enums_manager import GameEnumsManager

    missing = [
        gt.__name__ for gt in GameEnumsManager.VALID_GAME_TYPES
        if getattr(des_game_types, gt.__name__, None) is not gt
    ]
    assert not missing, f"`VALID_GAME_TYPES` entries not exported by DeS `game_types`: {missing}"


@pytest.mark.xfail(
    reason="`demonssouls/game_types/game_enums_manager.py` was copy-pasted from Dark Souls 1 and "
           "lists `SpawnPointEvent` and `NavigationEvent`, neither of which is a Demon's Souls MSB "
           "entry subtype (see `demonssouls/maps/enums.py:MSBEventSubtype`).",
    strict=False,
)
def test_game_enums_manager_valid_game_types_exist_in_des_msb():
    import dataclasses

    from soulstruct.demonssouls.game_types.game_enums_manager import GameEnumsManager
    from soulstruct.demonssouls.maps.msb import MSB

    msb_field_names = {f.name for f in dataclasses.fields(MSB)}
    msb_game_types = {
        game_type for list_name, game_type in MSB.ENTITY_GAME_TYPES.items() if list_name in msb_field_names
    }
    map_entry_types = [
        gt for gt in GameEnumsManager.VALID_GAME_TYPES
        if gt.__name__.endswith(("Event", "Start")) or gt.__name__ in {"MapPiece", "Object", "Character", "Collision"}
    ]
    bad = [gt.__name__ for gt in map_entry_types if gt not in msb_game_types]
    assert not bad, f"`VALID_GAME_TYPES` includes MSB types Demon's Souls does not have: {bad}"


# ---------------------------------------------------------------------------
# Game-data (skipped without a Demon's Souls installation)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_des_event_directory_exists_but_is_unreadable(des_root):
    """Demon's Souls ships EMEVD files that Soulstruct currently cannot parse."""
    event_dir = des_root / DEMONS_SOULS.default_file_paths["EventDirectory"]
    if not event_dir.is_dir():
        pytest.skip(f"Missing DeS event directory: {event_dir}")
    assert list(event_dir.glob("*.emevd*")), "No DeS EMEVD files found."
    with pytest.raises(ImportError):
        importlib.import_module("soulstruct.demonssouls.events.emevd")
