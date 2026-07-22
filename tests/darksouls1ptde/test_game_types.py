"""Pure-unit tests for `soulstruct.darksouls1ptde.game_types`.

`game_types` is the glue between EVS scripts, MSB entries and Params: EVS instructions are typed
with these classes, `GameEnumsManager` decides which ones may appear in generated entity-ID enum
modules, and MSB `ENTITY_GAME_TYPES` maps subtype lists to them.

Almost everything here runs without game data; the MSB binding test uses the committed Depths MSB.
"""
from __future__ import annotations

import inspect

import pytest

from soulstruct.base.game_types.basic_types import GameObject
from soulstruct.darksouls1ptde import game_types
from soulstruct.darksouls1ptde.game_types import *  # noqa: F403
from soulstruct.darksouls1ptde.game_types import map_types, param_types, sound_types, text_types
from soulstruct.darksouls1ptde.game_types.game_enums_manager import GameEnumsManager
from soulstruct.darksouls1ptde.maps.msb import MSB
from soulstruct.darksouls1ptde.params import GameParamBND
from soulstruct.darksouls1ptde.text import MSGDirectory


SUBMODULES = (map_types, param_types, sound_types, text_types)


# ---------------------------------------------------------------------------
# Module exports
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("module", SUBMODULES, ids=lambda m: m.__name__.rsplit(".", 1)[-1])
def test_all_exports_resolve(module):
    for name in module.__all__:
        assert hasattr(module, name), f"`{module.__name__}.__all__` exports missing name: {name}"


@pytest.mark.parametrize("module", SUBMODULES, ids=lambda m: m.__name__.rsplit(".", 1)[-1])
def test_all_exports_are_reachable_from_package(module):
    for name in module.__all__:
        assert hasattr(game_types, name), (
            f"`{name}` is exported by `{module.__name__}` but not visible on `game_types`."
        )


def test_no_export_name_collisions_between_submodules():
    seen = {}
    for module in SUBMODULES:
        for name in module.__all__:
            if name in seen and getattr(seen[name], name) is not getattr(module, name):
                pytest.fail(
                    f"Name '{name}' is exported by both `{seen[name].__name__}` and "
                    f"`{module.__name__}` with different objects."
                )
            seen[name] = module


# ---------------------------------------------------------------------------
# Param types
# ---------------------------------------------------------------------------


def _concrete_param_types():
    for name in param_types.__all__:
        value = getattr(param_types, name)
        if not (inspect.isclass(value) and issubclass(value, BaseParam)):
            continue
        if name.startswith("Base"):
            continue
        yield name, value


# `AttackParam` and `BehaviorParam` deliberately raise `ValueError`: DS1 splits each into a
# player and non-player Param, so a single nickname is ambiguous.
AMBIGUOUS_PARAM_TYPES = {"AttackParam", "BehaviorParam"}


def test_game_param_types_have_valid_nicknames():
    """`get_param_nickname()` must name a real `GameParamBND` param (or a DrawParam)."""
    valid = set(GameParamBND.PARAM_NICKNAMES.values())
    from soulstruct.darksouls1ptde.params.draw_param import DrawParamBND

    valid |= set(DrawParamBND.PARAM_NICKNAMES.values())
    checked = 0
    for name, param_type in _concrete_param_types():
        if name in AMBIGUOUS_PARAM_TYPES:
            with pytest.raises(ValueError):
                param_type.get_param_nickname()
            continue
        try:
            nickname = param_type.get_param_nickname()
        except NotImplementedError:
            pytest.fail(f"`{name}.get_param_nickname()` is not implemented.")
        assert nickname in valid, f"`{name}.get_param_nickname()` -> unknown nickname {nickname!r}."
        checked += 1
    assert checked > 20, "Param type scan found suspiciously few concrete types."


def test_item_param_types_report_item_enums():
    from soulstruct.darksouls1ptde.events.enums import ItemType

    expected = {
        WeaponParam: ItemType.Weapon,
        ArmorParam: ItemType.Armor,
        AccessoryParam: ItemType.Ring,
        GoodParam: ItemType.Good,
    }
    for param_type, item_type in expected.items():
        assert param_type.get_item_enum() == item_type
        assert issubclass(param_type, BaseItemParam)


def test_base_item_param_requires_subclass():
    with pytest.raises(NotImplementedError):
        BaseItemParam.get_item_enum()


def test_gameparambnd_game_types_match_param_type_nicknames():
    for nickname, game_type in GameParamBND.GAME_TYPES.items():
        if game_type.__name__ in AMBIGUOUS_PARAM_TYPES:
            # e.g. `BehaviorParam` is used for both "PlayerBehaviors" and "NonPlayerBehaviors".
            continue
        assert game_type.get_param_nickname() == nickname, (
            f"`GAME_TYPES['{nickname}']` is `{game_type.__name__}` whose nickname is "
            f"{game_type.get_param_nickname()!r}."
        )


# ---------------------------------------------------------------------------
# Text types
# ---------------------------------------------------------------------------


def test_text_types_map_to_real_msgdirectory_categories():
    categories = set(MSGDirectory.GET_ALL_CATEGORIES())
    for name in text_types.__all__:
        value = getattr(text_types, name)
        if not (inspect.isclass(value) and issubclass(value, Text)) or value is Text:
            continue
        category = value.get_text_category()
        assert category in categories, (
            f"`{name}.get_text_category()` -> {category!r}, which is not an `MSGDirectory` category."
        )


def test_text_type_event_arg_formats_are_valid():
    for name in text_types.__all__:
        value = getattr(text_types, name)
        if not (inspect.isclass(value) and issubclass(value, GameObject)):
            continue
        try:
            fmt = value.get_event_arg_fmt()
        except (NotImplementedError, AttributeError, TypeError):
            continue  # base `Text` and some subtypes are not usable as EVS event args
        assert fmt in {"B", "b", "H", "h", "I", "i", "f", "s"}, f"{name}: bad event arg fmt {fmt!r}."


# ---------------------------------------------------------------------------
# Sound types
# ---------------------------------------------------------------------------


def test_sound_type_enum_values_are_unique():
    values = [member.value for member in SoundType]
    assert len(values) == len(set(values))


def test_sound_subclasses_report_their_sound_type():
    expected = {
        MusicSound: SoundType.m_Music,
        SFXSound: SoundType.s_SFX,
        ObjectSound: SoundType.o_Object,
        VoiceSound: SoundType.v_Voice,
        CharacterMotionSound: SoundType.c_CharacterMotion,
    }
    for sound_cls, sound_type in expected.items():
        assert sound_cls.get_sound_enum() == sound_type
        assert issubclass(sound_cls, Sound)


def test_base_sound_requires_subclass():
    with pytest.raises(NotImplementedError):
        Sound.get_sound_enum()


def test_sound_type_prefix_letters_match_names():
    """`SoundType` member names encode the FEV file prefix letter (e.g. `s_SFX` -> 's')."""
    for member in SoundType:
        assert member.name[1] == "_", f"{member.name}: expected '<letter>_<Name>' format."
        assert member.name[0].isalpha()


# ---------------------------------------------------------------------------
# GameEnumsManager
# ---------------------------------------------------------------------------


def test_valid_game_types_are_game_objects():
    assert GameEnumsManager.VALID_GAME_TYPES
    for game_type in GameEnumsManager.VALID_GAME_TYPES:
        assert inspect.isclass(game_type)
        assert issubclass(game_type, GameObject), f"{game_type} is not a `GameObject` subclass."
    assert len(set(GameEnumsManager.VALID_GAME_TYPES)) == len(GameEnumsManager.VALID_GAME_TYPES)


def test_reserved_global_ids():
    assert GameEnumsManager.RESERVED_GLOBAL_IDS[10000] == "PLAYER"
    for i in range(1, 10):
        assert GameEnumsManager.RESERVED_GLOBAL_IDS[10000 + i] == f"CLIENT_PLAYER_{i}"
    names = list(GameEnumsManager.RESERVED_GLOBAL_IDS.values())
    assert len(names) == len(set(names))
    assert GameEnumsManager.USE_AA_BB_ABBREVIATION is True


def test_reserved_global_ids_match_events_constants():
    from soulstruct.darksouls1ptde.events import enums as event_enums

    for entity_id, name in GameEnumsManager.RESERVED_GLOBAL_IDS.items():
        assert hasattr(event_enums, name), f"`events.enums.{name}` missing."
        assert getattr(event_enums, name) == entity_id


def test_msb_entity_game_types_are_all_valid_enum_types():
    """Every MSB subtype that can carry an entity ID must be a type the enums manager accepts."""
    valid = set(GameEnumsManager.VALID_GAME_TYPES)
    for subtype_list_name, game_type in MSB.ENTITY_GAME_TYPES.items():
        assert game_type in valid, (
            f"MSB subtype list '{subtype_list_name}' maps to `{game_type.__name__}`, which is not "
            f"in `GameEnumsManager.VALID_GAME_TYPES`."
        )


def test_map_entity_types_are_int_enums_usable_as_entity_ids():
    """MSB entity game types are `IntEnum` bases, so generated enum modules can subclass them and
    their members can be passed straight into EVS instructions as entity IDs."""
    from enum import IntEnum

    for subtype_list_name, game_type in MSB.ENTITY_GAME_TYPES.items():
        assert issubclass(game_type, IntEnum), (
            f"`{game_type.__name__}` (for '{subtype_list_name}') must be an `IntEnum` subclass."
        )
        # Generated enum modules subclass these types directly, e.g. `class Characters(Character)`.
        namespace = type(game_type).__prepare__(f"Test{game_type.__name__}", (game_type,))
        namespace["MEMBER"] = 1000000
        subclass = type(game_type)(f"Test{game_type.__name__}", (game_type,), namespace)
        assert int(subclass.MEMBER) == 1000000
        assert isinstance(subclass.MEMBER, game_type)


# ---------------------------------------------------------------------------
# Binding to real MSB entity IDs
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def depths_msb(request) -> MSB:
    path = request.path.parent / "resources" / "m10_00_00_00.msb"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return MSB.from_path(path)


def test_msb_entries_expose_entity_ids_for_every_entity_game_type(depths_msb):
    for subtype_list_name in MSB.ENTITY_GAME_TYPES:
        for entry in depths_msb[subtype_list_name]:
            assert hasattr(entry, "entity_id"), (
                f"'{subtype_list_name}' entry `{entry.name}` has no `entity_id` field, but the "
                f"subtype is registered in `MSB.ENTITY_GAME_TYPES`."
            )


def test_set_entity_enum_binds_name_and_id(depths_msb):
    """`set_entity_enum` is how generated enum modules are applied back to an MSB."""
    from enum import IntEnum

    character = depths_msb.characters[0]

    class Characters(IntEnum):
        MyBonfireCharacter = 1000123

    character.set_entity_enum(Characters.MyBonfireCharacter)
    assert character.entity_id == 1000123
    assert character.name == "MyBonfireCharacter"


def test_msb_entity_id_lookup_round_trip(depths_msb):
    """Entity IDs in the MSB are the values that EVS `game_types` enums must carry."""
    entity_entries = [
        entry
        for subtype_list_name in MSB.ENTITY_GAME_TYPES
        for entry in depths_msb[subtype_list_name]
        if getattr(entry, "entity_id", -1) > 0
    ]
    assert entity_entries, "Depths MSB should have entities with IDs."
    for entry in entity_entries:
        assert isinstance(entry.entity_id, int)
        assert entry.name, "Entities with IDs must have names (used as enum member names)."
