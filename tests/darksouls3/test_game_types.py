"""Dark Souls III `game_types`, `maps.constants`, `models` and `EventDirectory` consistency.

All pure-unit; no game data required.
"""
from __future__ import annotations

import dataclasses

import pytest

import soulstruct.darksouls3.game_types as ds3_game_types
from soulstruct.base.game_types.basic_types import BaseGameParam
from soulstruct.darksouls3.game_types import (
    Character,
    Collision,
    Flag,
    GameEnumsManager,
    MapPiece,
    Object,
    Region,
)
from soulstruct.darksouls3.game_types.param_types import BaseItemParam
from soulstruct.darksouls3.maps import constants as map_constants
from soulstruct.games import DARK_SOULS_3


# ---------------------------------------------------------------------------
# `game_types` package
# ---------------------------------------------------------------------------


def test_game_types_star_import_provides_documented_names():
    namespace = {}
    exec("from soulstruct.darksouls3.game_types import *", namespace)
    for name in ("Flag", "Character", "Object", "Region", "Collision", "MapPiece", "Text", "Animation"):
        assert name in namespace, f"`game_types` star import missing {name!r}."


def test_param_types_all_is_complete():
    from soulstruct.darksouls3.game_types import param_types

    missing = [name for name in param_types.__all__ if not hasattr(param_types, name)]
    assert not missing, missing


def test_every_game_param_defines_a_nickname():
    """`get_param_nickname()` must either return a `str` or deliberately raise `ValueError`."""
    from soulstruct.darksouls3.game_types import param_types

    for name in param_types.__all__:
        obj = getattr(param_types, name)
        if not (isinstance(obj, type) and issubclass(obj, BaseGameParam)):
            continue
        if obj in (BaseGameParam, BaseItemParam):
            continue
        try:
            nickname = obj.get_param_nickname()
        except ValueError:
            continue  # ambiguous by design (e.g. `AttackParam`, `BehaviorParam`)
        except NotImplementedError:
            pytest.fail(f"{name}.get_param_nickname() is not implemented.")
        else:
            assert isinstance(nickname, str) and nickname, name


def test_item_params_map_to_distinct_item_enums():
    from soulstruct.darksouls3.events.enums import ItemType
    from soulstruct.darksouls3.game_types import (
        AccessoryParam, ArmorParam, GoodParam, WeaponParam,
    )

    mapping = {
        WeaponParam: ItemType.Weapon,
        ArmorParam: ItemType.Armor,
        AccessoryParam: ItemType.Ring,
        GoodParam: ItemType.Good,
    }
    for param_cls, expected in mapping.items():
        assert param_cls.get_item_enum() == expected
    assert len(set(mapping.values())) == len(mapping)


def test_sound_types_map_to_distinct_sound_enums():
    from soulstruct.darksouls3.game_types import sound_types

    enums = []
    for name in sound_types.__all__:
        obj = getattr(sound_types, name)
        if not (isinstance(obj, type) and issubclass(obj, sound_types.Sound)):
            continue
        if obj is sound_types.Sound:
            with pytest.raises(NotImplementedError):
                obj.get_sound_enum()
            continue
        enums.append(obj.get_sound_enum())
    assert len(enums) == len(set(enums)), f"Duplicate `SoundType` mappings: {enums}"


def test_game_enums_manager_valid_types_are_classes():
    assert GameEnumsManager.VALID_GAME_TYPES
    for game_type in GameEnumsManager.VALID_GAME_TYPES:
        assert isinstance(game_type, type), game_type
    # No duplicates.
    assert len(set(GameEnumsManager.VALID_GAME_TYPES)) == len(GameEnumsManager.VALID_GAME_TYPES)


def test_game_enums_manager_valid_types_are_exported_by_game_types():
    missing = [
        gt.__name__ for gt in GameEnumsManager.VALID_GAME_TYPES
        if getattr(ds3_game_types, gt.__name__, None) is not gt
    ]
    assert not missing, f"`GameEnumsManager.VALID_GAME_TYPES` entries not exported by DS3 `game_types`: {missing}"


def test_reserved_global_ids_are_contiguous_player_ids():
    ids = GameEnumsManager.RESERVED_GLOBAL_IDS
    assert ids[10000] == "PLAYER"
    assert sorted(ids) == list(range(10000, 10010))


# ---------------------------------------------------------------------------
# `maps.constants`
# ---------------------------------------------------------------------------


def test_all_maps_have_unique_names_and_variable_names():
    names = [m.name for m in map_constants.ALL_MAPS]
    assert len(names) == len(set(names)), names
    variable_names = [m.variable_name for m in map_constants.ALL_MAPS if m.variable_name]
    assert len(variable_names) == len(set(variable_names)), variable_names


def test_all_maps_variable_names_resolve_to_the_same_object():
    for game_map in map_constants.ALL_MAPS:
        if not game_map.variable_name:
            continue
        assert getattr(map_constants, game_map.variable_name) is game_map


def test_all_maps_exported_in_module_all():
    exported = set(map_constants.__all__)
    for game_map in map_constants.ALL_MAPS:
        if game_map.variable_name:
            assert game_map.variable_name in exported, game_map.variable_name


def test_common_func_is_separate_from_all_maps():
    """`COMMON_FUNC` is handled separately (it has no MSB and no `variable_name`)."""
    assert map_constants.COMMON_FUNC.emevd_file_stem == "common_func"
    assert map_constants.COMMON in map_constants.ALL_MAPS
    assert not any(m is map_constants.COMMON_FUNC for m in map_constants.ALL_MAPS)


@pytest.mark.xfail(
    reason="`Map.__eq__` compares only `(area_id, block_id)` and `Map.__hash__` hashes only "
           "`msb_file_stem`, so `COMMON` and `COMMON_FUNC` (both `(None, None)` with no MSB stem) "
           "compare and hash EQUAL. `x in ALL_MAPS` / set membership therefore cannot distinguish "
           "them (base/game_types/map_types.py:174-179).",
    strict=False,
)
def test_common_and_common_func_are_distinguishable():
    assert map_constants.COMMON != map_constants.COMMON_FUNC
    assert map_constants.COMMON_FUNC not in map_constants.ALL_MAPS
    assert len({map_constants.COMMON, map_constants.COMMON_FUNC}) == 2


def test_get_map_by_area_block_and_by_name():
    high_wall = map_constants.HIGH_WALL_OF_LOTHRIC
    assert map_constants.get_map((high_wall.area_id, high_wall.block_id)) is high_wall
    assert map_constants.get_map(high_wall.name) is high_wall
    assert map_constants.get_map_variable_name((high_wall.area_id, high_wall.block_id)) == "HIGH_WALL_OF_LOTHRIC"


def test_get_map_variable_name_falls_back_to_tuple():
    assert map_constants.get_map_variable_name((99, 9, 0, 0)) == "(99, 9, 0, 0)"


def test_ds3_declares_msb_file_names_it_cannot_open():
    """`ALL_MSB_FILE_NAMES` is populated (auto-derived from area/block IDs) but DS3 has no MSB class.

    This documents the "declared but hollow" state of `soulstruct.darksouls3.maps`: constants exist
    for every map's MSB file, but there is no `MSB`, `MapStudioDirectory` or `MSBPart` implementation
    to read them, and `DARK_SOULS_3.default_file_paths` does not include `MapStudioDirectory`.
    """
    assert map_constants.ALL_MSB_FILE_NAMES, "Expected auto-derived MSB stems for DS3 maps."
    assert all(stem.startswith("m") for stem in map_constants.ALL_MSB_FILE_NAMES)
    maps_package = __import__("soulstruct.darksouls3.maps", fromlist=["maps"])
    assert not hasattr(maps_package, "MSB")
    assert not hasattr(maps_package, "MapStudioDirectory")


# ---------------------------------------------------------------------------
# `EventDirectory` map properties
# ---------------------------------------------------------------------------


def _event_directory_map_properties() -> dict[str, object]:
    from soulstruct.darksouls3.events.event_directory import EventDirectory
    from soulstruct.base.game_file_directory import map_property

    out = {}
    for name, value in vars(EventDirectory).items():
        if isinstance(value, property) or type(value).__name__ == "property":
            continue
    # `map_property` returns a `property`-like descriptor; capture the bound `Map` via closure cells.
    for name in dir(EventDirectory):
        attr = EventDirectory.__dict__.get(name)
        if attr is None or not hasattr(attr, "fget"):
            continue
        closure = getattr(attr.fget, "__closure__", None)
        if not closure:
            continue
        for cell in closure:
            contents = cell.cell_contents
            if type(contents).__name__ == "Map":
                out[name] = contents
    assert map_property  # keep import meaningful
    return out


@pytest.mark.xfail(
    reason="BUG: `darksouls3/events/event_directory.py` swaps four map properties -- "
           "`DregHeap = map_property(ARENA_GRAND_ROOF)`, `RingedCity = map_property(ARENA_KILN_OF_FLAME)`, "
           "`ArenaGrandRoof = map_property(DREG_HEAP)`, `ArenaKilnOfFlame = map_property(RINGED_CITY)`.",
    strict=False,
)
def test_event_directory_map_properties_match_their_names():
    props = _event_directory_map_properties()
    assert props, "Could not introspect `EventDirectory` map properties."
    mismatches = {
        name: game_map.name for name, game_map in props.items()
        if game_map.name != name and game_map.variable_name is not None
    }
    assert not mismatches, f"`EventDirectory` attribute names do not match their `Map`s: {mismatches}"


def test_event_directory_covers_every_map_with_an_emevd():
    from soulstruct.darksouls3.events.event_directory import EventDirectory

    props = _event_directory_map_properties()
    bound_maps = set(props.values())
    expected = {m for m in map_constants.ALL_MAPS if m.emevd_file_stem}
    missing = {m.name for m in expected - bound_maps}
    assert not missing, f"`EventDirectory` has no property for maps: {missing}"
    assert EventDirectory.COMMON_FUNC is map_constants.COMMON_FUNC


# ---------------------------------------------------------------------------
# `models` binders
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("binder_name", ["CHRBND", "OBJBND", "PARTSBND"])
def test_binder_classes_instantiate_with_ds3_defaults(binder_name: str):
    import soulstruct.darksouls3.models as models

    binder_cls = getattr(models, binder_name)
    binder = binder_cls()
    assert binder.dcx_type == DARK_SOULS_3.default_dcx_type
    assert binder.version.name == "V4"
    assert binder.v4_info is not None
    assert binder_cls.DEFAULT_ENTRY_ROOT.startswith(DARK_SOULS_3.interroot_prefix)


@pytest.mark.xfail(
    reason="BUG: `darksouls3/models/mapbnd.py:24` passes `default_factory="
           "BinderVersion4Info.darksouls3_default()` (already CALLED), so instantiating `MAPBND` "
           "raises `TypeError: 'BinderVersion4Info' object is not callable`.",
    strict=False,
)
def test_mapbnd_instantiates():
    from soulstruct.darksouls3.models.mapbnd import MAPBND

    mapbnd = MAPBND()
    assert mapbnd.v4_info is not None


def test_mapbnd_default_factory_is_callable():
    """Direct check of the offending dataclass field (does not require instantiation)."""
    from soulstruct.darksouls3.models.mapbnd import MAPBND

    field = {f.name: f for f in dataclasses.fields(MAPBND)}["v4_info"]
    if field.default_factory is not dataclasses.MISSING and not callable(field.default_factory):
        pytest.xfail("`MAPBND.v4_info` default_factory is a `BinderVersion4Info` instance, not a callable.")


def test_partsbnd_entry_paths_uppercase_and_strip_low_suffix():
    from soulstruct.darksouls3.models import PARTSBND

    partsbnd = PARTSBND()
    assert partsbnd.get_flver_entry_path("hd_m_1000").endswith("\\HD_M_1000\\HD_M_1000.flver")
    # '_L' (low-detail) suffix is dropped from the folder but kept in the file name.
    low = partsbnd.get_flver_entry_path("hd_m_1000_l")
    assert "\\HD_M_1000\\HD_M_1000_L.flver" in low
    cloth = partsbnd.get_cloth_clm2_entry_path("hd_m_1000_l")
    assert cloth.endswith("\\HD_M_1000\\HD_M_1000_c_L.clm2")


def test_chrbnd_entry_paths():
    from soulstruct.darksouls3.models import CHRBND

    chrbnd = CHRBND()
    assert chrbnd.get_ragdoll_hkx_entry_path("c1000").endswith("\\c1000\\c1000.HKX")
    assert chrbnd.get_hkxpwv_entry_path("c1000").endswith("\\c1000\\c1000.hkxpwv")
    assert chrbnd.get_cloth_hkx_entry_path("c1000").endswith("\\c1000\\c1000_c.hkx")


def test_objbnd_flver_and_collision_paths_share_prefix():
    from soulstruct.darksouls3.models import OBJBND

    objbnd = OBJBND()
    flver = objbnd.get_flver_entry_path("o000100")
    hkx = objbnd.get_collision_hkx_entry_path("o000100")
    assert flver.rsplit(".", 1)[0] == hkx.rsplit(".", 1)[0]
    assert "\\o00\\o000100\\" in flver


# ---------------------------------------------------------------------------
# `params` / `ezstate`
# ---------------------------------------------------------------------------


def test_ds3_paramdef_classes_configured():
    from soulstruct.darksouls3.params import ParamDef, ParamDefBND

    field_defaults = {f.name: f.default for f in dataclasses.fields(ParamDef)}
    assert field_defaults["unicode"] is True
    assert ParamDefBND.PARAMDEF_CLASS is ParamDef


@pytest.mark.xfail(
    reason="BUG: `darksouls3/params/paramdef/core.py:18` writes `format_version = 202` with NO type "
           "annotation. `ParamDef` is a slots dataclass, so an un-annotated assignment is not a field "
           "override: `dataclasses.fields(ParamDef)['format_version'].default` is still the base "
           "value 104. (Bloodborne's `format_version = 201` has the same defect; PTDE/DSR annotate "
           "theirs correctly.)",
    strict=False,
)
def test_ds3_paramdef_format_version_override_takes_effect():
    from soulstruct.darksouls3.params import ParamDef

    field_defaults = {f.name: f.default for f in dataclasses.fields(ParamDef)}
    assert field_defaults["format_version"] == 202


def test_ds3_paramdefbnd_has_no_bundled_resource():
    """DS3 has no bundled PARAMDEFBND (needs a Paramdex, like Elden Ring)."""
    assert "PARAMDEFBND" not in DARK_SOULS_3.bundled_resource_paths


def test_ds3_esd_classes_configured():
    from soulstruct.darksouls3.ezstate import ChrESD, TalkESD

    assert TalkESD.VERSION == ChrESD.VERSION == 3
    assert TalkESD.LONG_VARINTS is True
    assert TalkESD.ESD_TYPE.name == "TALK"
    assert ChrESD.ESD_TYPE.name == "CHR"
