"""Pure-unit tests for Elden Ring `game_types` (`soulstruct.eldenring.game_types`).

`game_types` are the marker classes used to annotate EVS event arguments and MSB entity references:
`Character`, `Asset`, `Region`, `Flag`, plus `*Param` (GameParam row references) and `Text` (FMG
entry references). They are almost pure metadata, so all of these tests are cheap and need no game
install -- but they are exactly the layer where copy/paste from earlier games goes unnoticed.
"""
from __future__ import annotations

import inspect

import pytest

from soulstruct.base.game_types.basic_types import GameObject
from soulstruct.eldenring import game_types as ER
from soulstruct.eldenring.game_types import map_types, param_types, sound_types, text_types
from soulstruct.eldenring.game_types.game_enums_manager import GameEnumsManager
from soulstruct.eldenring.game_types.map_types import Map, MapTile
from soulstruct.eldenring.maps.enums import MSBPartSubtype, MSBRegionSubtype
from soulstruct.eldenring.text import MSGDirectory


# ---------------------------------------------------------------------------
# `__all__` hygiene
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("module", [map_types, param_types, text_types])
def test_module_all_entries_exist(module):
    for name in module.__all__:
        assert hasattr(module, name), f"`{module.__name__}.__all__` names missing attribute '{name}'."


def test_text_typing_alias_is_exported():
    """`TextTyping` is defined in `text_types` but omitted from its `__all__`."""
    assert hasattr(text_types, "TextTyping")
    assert "TextTyping" not in text_types.__all__, (
        "If `TextTyping` was added to `__all__`, update this test (it is a known omission)."
    )


@pytest.mark.xfail(
    reason="BUG: `eldenring/game_types/sound_types.py` declares `_all__` (one leading underscore) instead "
           "of `__all__`, so `from .sound_types import *` re-exports `IntEnum` into "
           "`soulstruct.eldenring.game_types`. (The typo also masks a second bug: the intended list "
           "contains 'SoundEvent', which that module does not define.)",
    strict=False,
)
def test_sound_types_declares_all():
    assert hasattr(sound_types, "__all__"), "`sound_types` uses `_all__` (typo) instead of `__all__`."
    assert not hasattr(ER, "IntEnum"), "`IntEnum` leaked into `soulstruct.eldenring.game_types`."


# ---------------------------------------------------------------------------
# Sound types
# ---------------------------------------------------------------------------


def test_sound_type_enum_letters():
    st = sound_types.SoundType
    assert st.s_SFX == 5
    assert st.m_Music == 6
    assert st.v_Voice == 7
    # Every member's name starts with the FEV file letter prefix (except the one unknown type).
    for member in st:
        if member.name == "unk_GeometrySet":
            continue
        assert member.name[1] == "_", f"Unexpected SoundType member name: {member.name}"


def test_sound_subclasses_report_their_enum():
    assert sound_types.MusicSound.get_sound_enum() is sound_types.SoundType.m_Music
    assert sound_types.SFXSound.get_sound_enum() is sound_types.SoundType.s_SFX
    assert sound_types.ObjectSound.get_sound_enum() is sound_types.SoundType.o_Object
    assert sound_types.VoiceSound.get_sound_enum() is sound_types.SoundType.v_Voice
    assert sound_types.CharacterMotionSound.get_sound_enum() is sound_types.SoundType.c_CharacterMotion
    with pytest.raises(NotImplementedError):
        sound_types.Sound.get_sound_enum()


# ---------------------------------------------------------------------------
# Param types
# ---------------------------------------------------------------------------


def _param_type_classes():
    return {
        name: obj
        for name in param_types.__all__
        if inspect.isclass(obj := getattr(param_types, name)) and issubclass(obj, param_types.BaseParam)
    }


def test_param_types_define_nicknames():
    """Every concrete `*Param` game type must return a nickname or raise a deliberate `ValueError`."""
    for name, cls in _param_type_classes().items():
        if name in ("BaseParam", "BaseGameParam", "BaseItemParam"):
            continue
        try:
            nickname = cls.get_param_nickname()
        except ValueError:
            continue  # ambiguous (e.g. AttackParam -> Player/NonPlayer)
        except NotImplementedError:
            pytest.fail(f"{name}.get_param_nickname() is not implemented.")
        else:
            assert isinstance(nickname, str) and nickname, name


def test_item_param_types_resolve_item_enums():
    """Item param types must map to an `ItemType` EMEVD enum without circular-import errors."""
    for cls in (
        param_types.WeaponParam,
        param_types.ArmorParam,
        param_types.GoodParam,
        param_types.AccessoryParam,
        param_types.GemParam,
    ):
        assert cls.get_item_enum() is not None
        assert cls.get_event_arg_fmt() == "I"
    with pytest.raises(NotImplementedError):
        param_types.BaseItemParam.get_item_enum()


def test_item_lot_param_uses_signed_event_arg():
    assert param_types.ItemLotParam.get_event_arg_fmt() == "i"


def test_param_nicknames_are_unique():
    nicknames = []
    for name, cls in _param_type_classes().items():
        try:
            nicknames.append(cls.get_param_nickname())
        except (ValueError, NotImplementedError):
            continue
    assert len(nicknames) == len(set(nicknames)), "Two ER param game types share a nickname."


# ---------------------------------------------------------------------------
# Text types
# ---------------------------------------------------------------------------


def _text_type_classes():
    from soulstruct.base.game_types import Text

    return {
        name: obj
        for name in text_types.__all__
        if inspect.isclass(obj := getattr(text_types, name)) and issubclass(obj, Text) and obj is not Text
    }


def test_text_types_declare_categories():
    for name, cls in _text_type_classes().items():
        category = cls.get_text_category()
        assert isinstance(category, str) and category, name


@pytest.mark.xfail(
    reason="BUG: several ER `Text` game types were copied from Dark Souls and name FMG categories that "
           "do not exist in ER's `MSGDirectory`: EventText (ER has EventTextMap/EventTextTalk), "
           "Ring{Name,Summary,Description} (ER: Accessory*) and Good{Name,Summary,Description} "
           "(ER: Goods*).",
    strict=False,
)
def test_text_type_categories_exist_in_msg_directory():
    categories = set(MSGDirectory.ALL_CATEGORIES)
    bad = {
        name: cls.get_text_category()
        for name, cls in _text_type_classes().items()
        if cls.get_text_category() not in categories
    }
    assert not bad, f"ER text game types referencing non-existent FMG categories: {bad}"


def test_known_good_text_categories_exist():
    """The text types that ARE correct must stay correct."""
    categories = set(MSGDirectory.ALL_CATEGORIES)
    for cls in (
        text_types.NPCName,
        text_types.PlaceName,
        text_types.SoapstoneMessage,
        text_types.WeaponName,
        text_types.WeaponSummary,
        text_types.WeaponDescription,
        text_types.ArmorName,
        text_types.SpellName,
        text_types.Subtitle,
    ):
        assert cls.get_text_category() in categories, cls.__name__


# ---------------------------------------------------------------------------
# Map types
# ---------------------------------------------------------------------------


def test_map_class_is_shared_with_base():
    from soulstruct.base.game_types.map_types import Map as BaseMap

    assert Map is BaseMap, "ER re-exports the shared base `Map` class."
    assert issubclass(MapTile, Map)


def _region_game_types():
    from soulstruct.base.game_types.map_types import Region

    return {
        name: obj
        for name in map_types.__all__
        if inspect.isclass(obj := getattr(map_types, name)) and issubclass(obj, Region) and obj is not Region
    }


@pytest.mark.xfail(
    reason="Naming inconsistency: `SFXRegion.get_msb_entry_supertype_subtype()` returns 'SFX' but the MSB "
           "subtype enum member is `VFX`; likewise `OtherRegion` returns 'Other' vs enum `OtherRegion`. "
           "Any code mapping game types to MSB subtypes by name will miss those two.",
    strict=False,
)
def test_region_game_type_subtypes_match_msb_enum():
    subtype_names = {s.name for s in MSBRegionSubtype}
    bad = {
        name: cls.get_msb_entry_supertype_subtype()[1]
        for name, cls in _region_game_types().items()
        if cls.get_msb_entry_supertype_subtype()[1] not in subtype_names
    }
    assert not bad, f"Region game types whose subtype name is not an `MSBRegionSubtype`: {bad}"


def test_every_msb_region_subtype_has_a_game_type():
    """Allowing for the two known naming quirks, every MSB region subtype must be reachable."""
    covered = {cls.get_msb_entry_supertype_subtype()[1] for cls in _region_game_types().values()}
    aliases = {"VFX": "SFX", "OtherRegion": "Other"}
    missing = [
        s.name for s in MSBRegionSubtype
        if s.name not in covered and aliases.get(s.name) not in covered
    ]
    assert not missing, f"MSB region subtypes with no `game_types` class: {missing}"


def test_region_game_type_subtypes_are_unique():
    subtypes = [cls.get_msb_entry_supertype_subtype()[1] for cls in _region_game_types().values()]
    assert len(subtypes) == len(set(subtypes))


def test_part_subtype_game_types_exist():
    for subtype in MSBPartSubtype:
        # `PlayerStart` and `ConnectCollision` keep their names; others map directly.
        assert hasattr(map_types, subtype.name), f"No `game_types` class for MSB part subtype {subtype.name}"


def test_region_game_types_report_supertype_and_subtype():
    supertype, subtype = map_types.MufflingBoxRegion.get_msb_entry_supertype_subtype()
    assert (supertype, subtype) == ("Region", "MufflingBox")
    supertype, subtype = map_types.MufflingBoxRegion.get_msb_entry_supertype_subtype(pluralized_subtype=True)
    assert (supertype, subtype) == ("Regions", "MufflingBoxes")


def test_map_typing_union_members():
    import typing as tp

    args = tp.get_args(map_types.MapTyping)
    assert Map in args
    assert MapTile in args
    assert tuple[int, int, int, int] in args


def test_asset_typings_replace_object():
    import typing as tp

    assert map_types.Asset in tp.get_args(map_types.AnimatedEntityTyping)
    assert map_types.Asset in tp.get_args(map_types.CoordEntityTyping)


# ---------------------------------------------------------------------------
# `GameEnumsManager`
# ---------------------------------------------------------------------------


def test_game_enums_manager_valid_types_are_game_objects():
    for game_type in GameEnumsManager.VALID_GAME_TYPES:
        assert inspect.isclass(game_type)
        assert issubclass(game_type, GameObject), game_type


def test_game_enums_manager_valid_types_are_unique():
    types = GameEnumsManager.VALID_GAME_TYPES
    assert len(types) == len(set(types))


def test_reserved_global_ids():
    reserved = GameEnumsManager.RESERVED_GLOBAL_IDS
    assert reserved[10000] == "PLAYER"
    assert reserved[40000] == "TORRENT"
    assert reserved[35000] == "ALL_SPIRIT_SUMMONS"
    assert len(set(reserved.values())) == len(reserved), "Duplicate reserved enum names."
