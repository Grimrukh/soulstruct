"""Pure-unit tests for `soulstruct.base.game_types`.

Covers the `GameObject` / `GameObjectInt` typing hierarchy, the `Map` dataclass, MSB entity game types,
and `GameEnumsManager` (which loads user enum modules for EVS decompilation).

No game data required. `xfail`-marked tests document genuine library defects (see `02-utilities.md`).
"""
from __future__ import annotations

import enum
import logging
import sys
from pathlib import Path

import pytest

from soulstruct.base.game_types import (
    Animation,
    Asset,
    BaseAIScript,
    BattleAIScript,
    Character,
    CharacterModel,
    Collision,
    ConnectCollision,
    Cutscene,
    DummyAsset,
    DummyCharacter,
    DummyObject,
    EquipmentModel,
    Flag,
    FlagRange,
    GameObject,
    GameObjectInt,
    Icon,
    LogicAIScript,
    Map,
    MapEntity,
    MapEntry,
    MapEvent,
    MapModel,
    MapPart,
    MapPiece,
    MapPieceModel,
    ModelDummy,
    Navmesh,
    NavmeshModel,
    Object,
    ObjActEvent,
    ObjectModel,
    PlayerAnimation,
    PlayerStart,
    Region,
    SoundEvent,
    SpawnerEvent,
    TalkScript,
    Text,
    Texture,
    VFXEvent,
    VisualEffect,
)
from soulstruct.base.game_types.basic_types import (
    BaseGameParam,
    BaseParam,
    GameObjectIntSequence,
    MapFlagSuffix,
)
from soulstruct.base.game_types.game_enums_manager import GameEnumInfo


# ===========================================================================
# GameObject / GameObjectInt hierarchy
# ===========================================================================


def test_game_object_event_arg_fmt_default_raises():
    with pytest.raises(TypeError):
        GameObject.get_event_arg_fmt()
    with pytest.raises(TypeError):
        MapEntry.get_event_arg_fmt()


@pytest.mark.parametrize(
    "game_type,fmt",
    [
        (Flag, "i"),
        (Region, "I"),
        (MapPart, "i"),
        (Character, "i"),
        (Object, "i"),
        (Asset, "i"),
        (Collision, "i"),
        (VFXEvent, "i"),
        (SpawnerEvent, "i"),
        (ObjActEvent, "I"),
        (Navmesh, None),
        (ConnectCollision, None),
    ],
)
def test_event_arg_fmts(game_type, fmt):
    assert game_type.get_event_arg_fmt() == fmt


def test_game_object_int_is_int_enum():
    class Characters(Character):
        BlackKnight = 1000000

    assert issubclass(Characters, GameObjectInt)
    assert issubclass(Characters, GameObject)
    assert isinstance(Characters.BlackKnight, int)
    assert Characters.BlackKnight == 1000000
    assert Characters.BlackKnight + 1 == 1000001
    assert Characters.BlackKnight.name == "BlackKnight"


def test_game_object_int_meta_first_value():
    class Things(GameObjectInt, first_value=1000):
        A = enum.auto()
        B = enum.auto()
        C = enum.auto()

    assert [m.value for m in Things] == [1000, 1001, 1002]


def test_game_object_int_meta_default_auto():
    """With no class arguments, standard `IntEnum` `auto()` behaviour (1, 2, 3, ...) applies."""

    class Things(GameObjectInt):
        A = enum.auto()
        B = enum.auto()

    assert [m.value for m in Things] == [1, 2]


def test_game_object_int_meta_first_value_defaults_to_zero_with_max_count():
    class Things(GameObjectInt, max_count=3):
        A = enum.auto()
        B = enum.auto()

    assert [m.value for m in Things] == [0, 1]


def test_game_object_int_meta_last_value_is_exclusive():
    """GOTCHA: `max_count = last_value - first_value`, so `last_value` is EXCLUSIVE."""

    class Things(GameObjectInt, first_value=10, last_value=13):
        A = enum.auto()
        B = enum.auto()
        C = enum.auto()

    assert [m.value for m in Things] == [10, 11, 12]


def test_game_object_int_meta_rejects_last_value_and_max_count():
    with pytest.raises(ValueError):
        class Things(GameObjectInt, first_value=1, last_value=5, max_count=4):
            A = enum.auto()


def test_game_object_int_meta_rejects_unknown_kwargs():
    with pytest.raises(TypeError):
        class Things(GameObjectInt, bogus_kwarg=1):
            A = enum.auto()


@pytest.mark.xfail(
    reason="BUG: the `max_count` guard in `GameObjectIntMeta.__prepare__._generate_next_value_` formats "
           "`cls.__name__`, but `cls` there is the class NAME STRING passed to `__prepare__`. Exceeding "
           "`max_count` raises `AttributeError: 'str' object has no attribute '__name__'` instead of the "
           "intended, informative `ValueError`.",
    strict=False,
)
def test_game_object_int_meta_max_count_raises_value_error():
    with pytest.raises(ValueError):
        class Things(GameObjectInt, first_value=1000, max_count=2):
            A = enum.auto()
            B = enum.auto()
            C = enum.auto()  # one too many


def test_game_object_int_sequence():
    seq = GameObjectIntSequence((Region, 8))
    assert seq.game_object_int_type is Region
    assert seq.count == 8
    assert isinstance(seq, type)


def test_game_object_int_sequence_validation():
    with pytest.raises(TypeError):
        GameObjectIntSequence((Region,))  # wrong length
    with pytest.raises(TypeError):
        GameObjectIntSequence((int, 8))  # not a `GameObjectInt`
    with pytest.raises(TypeError):
        GameObjectIntSequence(())


def test_param_base_types_require_nickname():
    with pytest.raises(NotImplementedError):
        BaseParam.get_param_nickname()
    with pytest.raises(NotImplementedError):
        BaseGameParam.get_param_nickname()
    assert issubclass(BaseGameParam, BaseParam)
    assert issubclass(BaseParam, GameObjectInt)


def test_text_requires_category():
    with pytest.raises(NotImplementedError):
        Text.get_text_category()


def test_obj_act_event_rejects_entity_id_range():
    with pytest.raises(TypeError):
        ObjActEvent.get_id_start_and_max()


def test_misc_game_int_types_are_game_object_ints():
    for game_type in (
        ModelDummy, Texture, Icon, EquipmentModel, VisualEffect, TalkScript, Cutscene, Text,
        Animation, PlayerAnimation, BaseAIScript, LogicAIScript, BattleAIScript,
    ):
        assert issubclass(game_type, GameObjectInt), game_type
    assert issubclass(PlayerAnimation, Animation)
    assert issubclass(LogicAIScript, BaseAIScript)
    assert issubclass(BattleAIScript, BaseAIScript)


def test_map_flag_suffix_is_plain_int_enum():
    """NOTE: `MapFlagSuffix` is NOT a `GameObjectInt`; `EVSParser` resolves it against a map base flag."""
    assert not issubclass(MapFlagSuffix, GameObject)
    assert issubclass(MapFlagSuffix, enum.IntEnum)


def test_flag_range():
    fr = FlagRange(100, 200)
    assert fr.first == 100
    assert fr.last == 200
    assert tuple(fr) == (100, 200)
    assert list(fr) == [100, 200]
    assert fr[0] == 100
    assert fr[1] == 200
    assert repr(fr) == "(100, 200)"
    with pytest.raises(ValueError):
        _ = fr[2]
    assert issubclass(FlagRange, GameObject)
    assert not issubclass(FlagRange, GameObjectInt)


# ===========================================================================
# MSB game types
# ===========================================================================


def test_map_entity_hierarchy():
    assert issubclass(MapEntity, MapEntry)
    assert issubclass(MapEntity, GameObjectInt)
    for part_type in (MapPiece, Object, Asset, Character, PlayerStart, Collision, Navmesh, ConnectCollision):
        assert issubclass(part_type, MapPart), part_type
        assert issubclass(part_type, MapEntity), part_type
    assert issubclass(DummyObject, Object)
    assert issubclass(DummyAsset, Asset)
    assert issubclass(DummyCharacter, Character)
    for event_type in (SoundEvent, VFXEvent, SpawnerEvent, ObjActEvent):
        assert issubclass(event_type, MapEvent), event_type
    for model_type in (MapPieceModel, ObjectModel, CharacterModel, NavmeshModel):
        assert issubclass(model_type, MapModel), model_type
        assert not issubclass(model_type, MapEntity), model_type  # models have no entity ID


def test_supertype_only_types():
    assert MapModel.get_msb_entry_supertype_subtype() == ("Models", None)
    assert MapEvent.get_msb_entry_supertype_subtype() == ("Events", None)
    assert Region.get_msb_entry_supertype_subtype() == ("Regions", None)
    assert MapPart.get_msb_entry_supertype_subtype() == ("Parts", None)


@pytest.mark.parametrize(
    "game_type,singular,plural",
    [
        (MapPieceModel, "MapPieceModel", "MapPieceModels"),
        (ObjectModel, "ObjectModel", "ObjectModels"),
        (CharacterModel, "CharacterModel", "CharacterModels"),
        (MapPiece, "MapPiece", "MapPieces"),
        (Object, "Object", "Objects"),
        (Asset, "Asset", "Assets"),
        (Character, "Character", "Characters"),
        (Collision, "Collision", "Collisions"),
        (Navmesh, "Navmesh", "Navmeshes"),
        (PlayerStart, "PlayerStart", "PlayerStarts"),
        (ConnectCollision, "ConnectCollision", "ConnectCollisions"),
        (DummyObject, "DummyObject", "DummyObjects"),
        (DummyCharacter, "DummyCharacter", "DummyCharacters"),
        (SoundEvent, "Sound", "Sounds"),
        (SpawnerEvent, "Spawner", "Spawners"),
        (ObjActEvent, "ObjAct", "ObjActs"),
    ],
)
def test_supertype_subtype_names(game_type, singular, plural):
    supertype, subtype = game_type.get_msb_entry_supertype_subtype()
    assert subtype == singular
    assert game_type.get_msb_entry_supertype_subtype(pluralized_subtype=True)[1] == plural
    assert supertype in {"Models", "Events", "Regions", "Parts"}


@pytest.mark.xfail(
    reason="BUG: `NavmeshModel.get_msb_entry_supertype_subtype(True)` returns the typo 'NavmesheModels' "
           "instead of 'NavmeshModels'.",
    strict=False,
)
def test_navmesh_model_plural_typo():
    assert NavmeshModel.get_msb_entry_supertype_subtype(True) == ("Models", "NavmeshModels")


@pytest.mark.xfail(
    reason="BUG: `DummyAsset.get_msb_entry_supertype_subtype` is a copy-paste of `DummyObject`'s and returns "
           "'DummyObject'/'DummyObjects' instead of 'DummyAsset'/'DummyAssets'.",
    strict=False,
)
def test_dummy_asset_subtype_names():
    assert DummyAsset.get_msb_entry_supertype_subtype() == ("Parts", "DummyAsset")
    assert DummyAsset.get_msb_entry_supertype_subtype(True) == ("Parts", "DummyAssets")


def test_map_event_auto_region_name():
    class Sounds(SoundEvent):
        BossMusic = 1023000

    assert Sounds.BossMusic.auto_region_name() == "_SoundEvent_BossMusic"

    class VFX(VFXEvent):
        _FogGate = 1023001

    assert VFX._FogGate.auto_region_name() == "_VFXEvent_FogGate"


# ===========================================================================
# Map
# ===========================================================================


def test_map_basic_construction():
    m = Map(10, 2, name="FirelinkShrine", verbose_name="Firelink Shrine", variable_name="FIRELINK_SHRINE")
    assert m.map_stem == "m10_02_00_00"
    assert m.emevd_file_stem == "m10_02_00_00"
    assert m.msb_file_stem == "m10_02_00_00"
    assert m.ai_file_stem == "m10_02_00_00"
    assert m.esd_file_stem == "m10_02_00_00"
    assert m.base_entity_id == 1020000
    assert m.stem_set() == {"m10_02_00_00"}
    assert repr(m) == "m10_02_00_00"
    assert list(m) == [10, 2, 0, 0]
    assert [m[i] for i in range(4)] == [10, 2, 0, 0]
    with pytest.raises(ValueError):
        _ = m[4]
    assert m.get_connected_map_id() == (10, 2, 0, 0)


def test_map_name_defaults_to_stem():
    m = Map(10, 2)
    assert m.name == "m10_02_00_00"
    assert m.verbose_name == "m10_02_00_00"
    assert m.variable_name is None  # never auto-set


def test_map_explicit_none_file_stems():
    m = Map(
        None, None, name="Common", emevd_file_stem="common",
        msb_file_stem=None, ai_file_stem=None, esd_file_stem=None,
    )
    assert m.map_stem is None
    assert m.msb_file_stem is None
    assert m.stem_set() == {"common"}
    with pytest.raises(ValueError):
        m.get_connected_map_id()


def test_map_requires_name_if_no_ids():
    with pytest.raises(ValueError):
        Map(None, None)


def test_map_connected_map_id_wildcards():
    m = Map(10, 2, None, None, name="Wild")
    assert m.get_connected_map_id() == (10, 2, -1, -1)
    assert m.map_stem == "m10_02_00_00"  # `None` CC/DD still format as 00


def test_map_no_map():
    m = Map.NO_MAP()
    assert m.name == "NONE"
    assert m.map_stem == "m00_00_00_00"
    assert tuple(m) == (0, 0, 0, 0)


def test_map_base_flag_is_a_short_prefix_not_a_full_flag():
    """GOTCHA: despite the field docstring's '11020000' example, `base_flag` is computed as a 4-digit prefix."""
    m = Map(10, 2)
    assert m.base_flag == 1102


def test_map_explicit_base_flag_is_respected():
    m = Map(10, 2, base_flag=11020000)
    assert m.base_flag == 11020000


@pytest.mark.xfail(
    reason="BUG: `Map.__post_init__` recomputes `self.base_entity_id` UNCONDITIONALLY in its final block "
           "(line ~153), silently discarding any explicitly-supplied value (and contradicting the guarded "
           "assignment 20 lines earlier).",
    strict=False,
)
def test_map_explicit_base_entity_id_is_respected():
    m = Map(10, 2, base_entity_id=5000000)
    assert m.base_entity_id == 5000000


@pytest.mark.xfail(
    reason="BUG: `Map.__eq__` compares only (area_id, block_id) while `Map.__hash__` hashes `msb_file_stem`. "
           "Two equal maps that differ in CC/DD (e.g. DS1 Darkroot m12_00_00_00 vs. its DLC revision "
           "m12_00_00_01) hash differently, breaking `set`/`dict` membership.",
    strict=False,
)
def test_map_hash_eq_consistency():
    a = Map(12, 0, 0, 0)
    b = Map(12, 0, 0, 1)
    assert a == b
    assert hash(a) == hash(b)
    assert len({a, b}) == 1


def test_map_sets_undeclared_flag_prefix_attribute():
    """DOCUMENTS a defect: `Map` is `@dataclass(slots=True)` but sets a non-field `flag_prefix` attribute.

    This only works because `GameObject` (the base class) has no `__slots__`, so `Map` instances still get a
    `__dict__` -- which also means `slots=True` provides none of its intended memory benefit.
    """
    m = Map(10, 2)
    assert m.flag_prefix == 1102
    assert hasattr(m, "__dict__")


# ===========================================================================
# GameEnumsManager
# ===========================================================================


ENUM_MODULE_TEMPLATE = """\
from soulstruct.darksouls1ptde.game_types import *


class Characters({character_base}):
{character_members}


class Flags(Flag):
{flag_members}
"""


@pytest.fixture
def enums_manager_cls():
    from soulstruct.darksouls1ptde.game_types.game_enums_manager import GameEnumsManager
    return GameEnumsManager


@pytest.fixture
def write_enums_module(tmp_path: Path):
    """Write a temporary `mAA_BB_CC_DD_enums.py` module and clean it out of `sys.modules` afterwards."""
    written = []

    def _write(stem: str, characters: dict[str, int], flags: dict[str, int] = None) -> Path:
        flags = flags or {}
        path = tmp_path / f"{stem}.py"
        path.write_text(
            ENUM_MODULE_TEMPLATE.format(
                character_base="Character",
                character_members="\n".join(f"    {k} = {v}" for k, v in characters.items()) or "    pass",
                flag_members="\n".join(f"    {k} = {v}" for k, v in flags.items()) or "    pass",
            ),
            encoding="utf-8",
        )
        written.append(stem)
        return path

    yield _write

    for stem in written:
        sys.modules.pop(stem, None)


def test_enums_manager_empty():
    from soulstruct.darksouls1ptde.game_types.game_enums_manager import GameEnumsManager

    manager = GameEnumsManager([])
    assert manager.enums == {}
    with pytest.raises(GameEnumsManager.MissingEnumTypeError):
        manager.check_out_enum_variable(1000000, Character)


def test_enums_manager_loads_and_checks_out(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000}, {"BossDead": 11000000})
    manager = enums_manager_cls([path])
    assert "m10_00_00_00_enums" in manager.enums
    # Enum is registered under BOTH its own type and its registered parent type(s).
    assert Character in manager.enums["m10_00_00_00_enums"]
    assert MapPart in manager.enums["m10_00_00_00_enums"]
    assert Flag in manager.enums["m10_00_00_00_enums"]

    star = ["m10_00_00_00_enums"]
    assert manager.check_out_enum_variable(1000000, Character, star_import_module_names=star) == "Characters.BlackKnight"
    assert manager.check_out_enum_variable(11000000, Flag, star_import_module_names=star) == "Flags.BossDead"
    assert len(manager.used_enums) == 2


def test_enums_manager_non_star_alias(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000})
    manager = enums_manager_cls([path])
    # No star modules: alias prefix is used (DS1 PTDE uses the AA_BB abbreviation).
    variable = manager.check_out_enum_variable(1000000, Character, star_import_module_names=[])
    assert variable == "m10_00_Characters.BlackKnight"
    imports = manager.get_import_lines([], module_prefix="events.")
    assert imports == "\nfrom events.m10_00_00_00_enums import Characters as m10_00_Characters"


def test_enums_manager_star_import_lines(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000})
    manager = enums_manager_cls([path])
    star = ["m10_00_00_00_enums"]
    manager.check_out_enum_variable(1000000, Character, star_import_module_names=star)
    assert manager.get_import_lines(star, "") == "\nfrom m10_00_00_00_enums import *"


def test_enums_manager_reserved_global_ids(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000})
    manager = enums_manager_cls([path])
    assert manager.check_out_enum_variable(10000) == "PLAYER"
    assert manager.check_out_enum_variable(10001) == "CLIENT_PLAYER_1"
    assert not manager.used_enums  # reserved IDs are not 'used enums'


def test_enums_manager_reserved_id_in_module_raises(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"Player": 10000})
    with pytest.raises(ValueError, match="protected value"):
        enums_manager_cls([path])


def test_enums_manager_missing_value_and_type(enums_manager_cls, write_enums_module):
    from soulstruct.darksouls1ptde.game_types.game_enums_manager import GameEnumsManager

    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000})
    manager = enums_manager_cls([path])
    star = ["m10_00_00_00_enums"]
    with pytest.raises(GameEnumsManager.MissingEnumValueError):
        manager.check_out_enum_variable(9999999, Character, star_import_module_names=star)
    assert ("Character", 9999999) in manager.missing_enums
    assert manager.get_sorted_missing_items() == [("Character", 9999999)]
    with pytest.raises(GameEnumsManager.MissingEnumTypeError):
        manager.check_out_enum_variable(1000000, Region, star_import_module_names=star)


def test_enums_manager_ambiguous_non_star_value(enums_manager_cls, write_enums_module, caplog):
    from soulstruct.darksouls1ptde.game_types.game_enums_manager import GameEnumsManager

    p1 = write_enums_module("m10_00_00_00_enums", {"Guy": 1000000})
    p2 = write_enums_module("m10_01_00_00_enums", {"Guy": 1000000})
    with caplog.at_level(logging.CRITICAL):  # suppress expected duplicate-value warnings
        manager = enums_manager_cls([p1, p2])
    with pytest.raises(GameEnumsManager.AmbiguousEnumValueError):
        manager.check_out_enum_variable(1000000, Character, star_import_module_names=[])


def test_enums_manager_repeat_in_star_modules(enums_manager_cls, write_enums_module, caplog):
    from soulstruct.darksouls1ptde.game_types.game_enums_manager import GameEnumsManager

    p1 = write_enums_module("m10_00_00_00_enums", {"Guy": 1000000})
    p2 = write_enums_module("m10_01_00_00_enums", {"Guy": 1000000})
    with caplog.at_level(logging.CRITICAL):
        manager = enums_manager_cls([p1, p2])
    with pytest.raises(GameEnumsManager.EnumValueRepeatError):
        manager.check_out_enum_variable(
            1000000, Character, star_import_module_names=["m10_00_00_00_enums", "m10_01_00_00_enums"]
        )


@pytest.mark.xfail(
    reason="BUG: `GameEnumsManager._check_out_enum` builds its 'all types' list by EXTENDING with every "
           "module's game-type keys, so the same type appears once per module AND once per hierarchy level. "
           "Each duplicate re-finds the same enum, so a single unambiguous value produces multiple 'hits' and "
           "raises a spurious `EnumValueRepeatError`. Untyped (`Any`) enum checkout is therefore broken.",
    strict=False,
)
def test_enums_manager_any_type_checkout(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000})
    manager = enums_manager_cls([path])
    variable = manager.check_out_enum_variable(1000000, star_import_module_names=["m10_00_00_00_enums"])
    assert variable == "Characters.BlackKnight"


def test_enums_manager_add_event_id(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000}, {"BossDead": 11000000})
    manager = enums_manager_cls([path])
    manager.star_import_module_names = ["m10_00_00_00_enums"]
    manager.add_event_id(11000000)
    assert manager.all_event_ids[11000000] == "Flags.BossDead"
    manager.add_event_id(12345678)  # no matching enum
    assert manager.all_event_ids[12345678] == "12345678"
    manager.add_event_id(11000000, is_common=True)
    assert 11000000 in manager.all_common_event_ids


def test_enums_manager_refresh_enums_is_idempotent(enums_manager_cls, write_enums_module, caplog):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000})
    manager = enums_manager_cls([path])
    before = {k: dict(v) for k, v in manager.enums.items()}
    with caplog.at_level(logging.CRITICAL):
        manager.refresh_enums()
    assert set(manager.enums) == set(before)
    assert set(manager.enums["m10_00_00_00_enums"]) == set(before["m10_00_00_00_enums"])


def test_game_enum_info_aliasing():
    class Characters(Character):
        BlackKnight = 1000000

    info = GameEnumInfo(Characters.BlackKnight, "m10_00_00_00_enums")
    assert info.class_name == "Characters"
    assert info.module_name == "m10_00_00_00_enums"
    assert info.get_variable_string(["m10_00_00_00_enums"], False) == "Characters.BlackKnight"
    assert info.get_variable_string([], False) == "m10_00_00_00_Characters.BlackKnight"
    assert info.get_variable_string([], True) == "m10_00_Characters.BlackKnight"
    assert info.get_import_string(True) == "Characters as m10_00_Characters"
    assert "GameEnumInfo(" in repr(info)


def test_game_enum_info_common_module_needs_no_alias():
    class CommonFlags(Flag):
        SomeFlag = 100

    info = GameEnumInfo(CommonFlags.SomeFlag, "common_enums")
    assert info.get_class_alias(False) == "CommonFlags"
    assert info.get_import_string(False) == "CommonFlags"


def test_get_sorted_missing_items_prefers_strictest_type(enums_manager_cls, write_enums_module):
    path = write_enums_module("m10_00_00_00_enums", {"BlackKnight": 1000000})
    manager = enums_manager_cls([path])
    manager.missing_enums = {("Any", 5), ("Character", 5), ("Flag", 7)}
    assert manager.get_sorted_missing_items() == [("Character", 5), ("Flag", 7)]
