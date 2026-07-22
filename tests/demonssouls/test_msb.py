"""Demon's Souls MSB tests.

Demon's Souls is the oldest MSB format Soulstruct supports and the only **big-endian** one (PS3).
Its MSB also has a fifth supertype list, `MAPSTUDIO_TREE_ST`, that no other game has.

All tests here except the `des_root` ones are pure-unit: they build MSBs in memory.
"""
from __future__ import annotations

import dataclasses
import logging

import pytest

from soulstruct.base.maps.msb.utils import MSBSubtypeInfo
from soulstruct.demonssouls.maps import constants as des_map_constants
from soulstruct.demonssouls.maps.enums import (
    MSBEventSubtype,
    MSBModelSubtype,
    MSBPartSubtype,
    MSBRegionSubtype,
    MSBSupertype,
    MSBTreeSubtype,
)
from soulstruct.demonssouls.maps.msb import MSB
from soulstruct.demonssouls.maps.parts import (
    MSBCharacter,
    MSBCollision,
    MSBConnectCollision,
    MSBDummyCharacter,
    MSBDummyObject,
    MSBObject,
    MSBPlayerStart,
)
from soulstruct.utilities.binary import ByteOrder
from soulstruct.utilities.maths import EulerDeg, Vector3


@pytest.fixture(autouse=True)
def _quiet_msb_logging():
    """MSB packing emits `_LOGGER.warning`s (e.g. missing 'c0000_0000') that spam the console."""
    logger = logging.getLogger("soulstruct.base.maps.msb.core")
    previous = logger.level
    logger.setLevel(logging.ERROR)
    yield
    logger.setLevel(previous)


def _populated_msb(byte_order: ByteOrder = ByteOrder.BigEndian) -> MSB:
    msb = MSB(byte_order=byte_order)
    player_start = msb.player_starts.new(name="c0000_0000")
    msb.auto_model(player_start, "c0000")
    map_piece = msb.map_pieces.new(name="m1000B0_0000")
    msb.auto_model(map_piece, "m1000B0", map_stem="m10_00_00_00")
    obj = msb.objects.new(name="o0000_0000")
    msb.auto_model(obj, "o0000")
    character = msb.characters.new(name="c1000_0000", entity_id=1000)
    msb.auto_model(character, "c1000")
    collision = msb.collisions.new(name="h0000B0_0000")
    msb.auto_model(collision, "h0000B0", map_stem="m10_00_00_00")
    navmesh = msb.navmeshes.new(name="n0000B0_0000")
    msb.auto_model(navmesh, "n0000B0", map_stem="m10_00_00_00")
    msb.regions.new(name="r0", entity_id=2000)
    msb.sounds.new(name="s0", entity_id=3800)
    return msb


# ---------------------------------------------------------------------------
# Registration completeness / structure
# ---------------------------------------------------------------------------


def test_msb_is_big_endian_class():
    assert MSB.IS_BIG_ENDIAN is True
    assert MSB.HAS_HEADER is False
    assert MSB.LONG_VARINTS is False
    assert MSB.NAME_ENCODING == "shift_jis_2004"


def test_supertype_enum_values_are_msb_list_names():
    assert MSBSupertype.MODELS == "MODEL_PARAM_ST"
    assert MSBSupertype.EVENTS == "EVENT_PARAM_ST"
    assert MSBSupertype.REGIONS == "POINT_PARAM_ST"
    assert MSBSupertype.PARTS == "PARTS_PARAM_ST"
    # Extra supertype unique to Demon's Souls.
    assert MSBSupertype.TREES == "MAPSTUDIO_TREE_ST"


def test_all_five_supertypes_are_registered_consistently():
    supertypes = set(MSB.MSB_ENTRY_SUPERTYPES)
    assert supertypes == set(MSBSupertype)
    assert set(MSB.MSB_SUPERTYPE_SUBTYPE_ENUMS) == supertypes
    assert set(MSB.MSB_ENTRY_SUBTYPES) == supertypes
    assert set(MSB.MSB_ENTRY_SUBTYPE_OFFSETS) == supertypes


@pytest.mark.parametrize(
    "supertype, subtype_enum",
    [
        (MSBSupertype.MODELS, MSBModelSubtype),
        (MSBSupertype.EVENTS, MSBEventSubtype),
        (MSBSupertype.REGIONS, MSBRegionSubtype),
        (MSBSupertype.PARTS, MSBPartSubtype),
        (MSBSupertype.TREES, MSBTreeSubtype),
    ],
)
def test_every_subtype_enum_member_is_registered(supertype: str, subtype_enum):
    """Every enum member declared in `maps/enums.py` must have an `MSBSubtypeInfo` in the MSB."""
    registered = MSB.MSB_ENTRY_SUBTYPES[supertype]
    missing = [member.name for member in subtype_enum if member not in registered]
    assert not missing, f"{subtype_enum.__name__} members not registered in MSB: {missing}"


def test_every_registered_subtype_has_a_matching_msb_field():
    """Every `MSBSubtypeInfo.subtype_list_name` must be a real dataclass field of `MSB`."""
    field_names = {f.name for f in dataclasses.fields(MSB)}
    for supertype, subtypes in MSB.MSB_ENTRY_SUBTYPES.items():
        for subtype_enum, info in subtypes.items():
            assert isinstance(info, MSBSubtypeInfo)
            assert info.subtype_list_name in field_names, (
                f"{supertype}/{subtype_enum.name} -> '{info.subtype_list_name}' is not an `MSB` field."
            )


def test_every_registered_entry_class_declares_matching_subtype_enum():
    for supertype, subtypes in MSB.MSB_ENTRY_SUBTYPES.items():
        for subtype_enum, info in subtypes.items():
            assert info.entry_class.SUBTYPE_ENUM == subtype_enum, info.entry_class
            assert issubclass(info.entry_class, MSB.MSB_ENTRY_SUPERTYPES[supertype])


def test_default_entry_lists_are_empty_and_correctly_typed():
    msb = MSB()
    for supertype, subtypes in MSB.MSB_ENTRY_SUBTYPES.items():
        for info in subtypes.values():
            entry_list = getattr(msb, info.subtype_list_name)
            assert len(entry_list) == 0
            assert entry_list.entry_class is info.entry_class
            assert entry_list.supertype == supertype


def test_resolve_supertype_name_handles_all_aliases():
    assert MSB.resolve_supertype_name("models") == MSBSupertype.MODELS
    assert MSB.resolve_supertype_name("EVENT_PARAM_ST") == MSBSupertype.EVENTS
    assert MSB.resolve_supertype_name("points") == MSBSupertype.REGIONS
    assert MSB.resolve_supertype_name("regions") == MSBSupertype.REGIONS
    assert MSB.resolve_supertype_name("PARTS_PARAM_ST") == MSBSupertype.PARTS
    assert MSB.resolve_supertype_name("MAPSTUDIO_TREE_ST") == MSBSupertype.TREES
    with pytest.raises(ValueError):
        MSB.resolve_supertype_name("NOT_A_SUPERTYPE")


def test_entity_id_supertypes_excludes_models_and_trees():
    assert MSB.entity_id_supertypes() == (MSBSupertype.EVENTS, MSBSupertype.REGIONS, MSBSupertype.PARTS)


@pytest.mark.xfail(
    reason="BUG: `demonssouls/maps/msb.py:111-124` `ENTITY_GAME_TYPES` was copy-pasted from Dark Souls "
           "1 and maps 'spawn_points' and 'navigation' -- neither of which is a Demon's Souls MSB "
           "entry list (DeS has no SpawnPoint or Navigation event subtype). "
           "`EnumModuleGenerator` iterates this dict and would `getattr` a non-existent attribute.",
    strict=False,
)
def test_entity_game_types_only_names_real_entry_lists():
    field_names = {f.name for f in dataclasses.fields(MSB)}
    bad = [name for name in MSB.ENTITY_GAME_TYPES if name not in field_names]
    assert not bad, f"`ENTITY_GAME_TYPES` names non-existent MSB entry lists: {bad}"


@pytest.mark.xfail(
    reason="BUG: `demonssouls/maps/msb.py:130-146` `ID_RANGES` (docstring says 'prescribed DS1 entity "
           "ID range') includes `SpawnPointEvent`, which has no DeS MSB entry list.",
    strict=False,
)
def test_id_ranges_only_cover_real_entry_lists():
    field_names = {f.name for f in dataclasses.fields(MSB)}
    real_game_types = {
        game_type for list_name, game_type in MSB.ENTITY_GAME_TYPES.items() if list_name in field_names
    }
    bad = [gt.__name__ for gt in MSB.ID_RANGES if gt not in real_game_types]
    assert not bad, f"`ID_RANGES` covers game types with no MSB entry list: {bad}"


def test_id_ranges_are_non_overlapping_within_a_map():
    ranges = []
    for game_type, range_func in MSB.ID_RANGES.items():
        info = range_func(0)
        ranges.append((info["first_value"], info["last_value"], game_type.__name__))
    ranges.sort()
    for (first_a, last_a, name_a), (first_b, last_b, name_b) in zip(ranges, ranges[1:]):
        assert first_a <= last_a, name_a
        assert last_a < first_b, f"`ID_RANGES` overlap: {name_a} {first_a}-{last_a} vs {name_b} {first_b}-{last_b}"


def test_msb_entry_references_name_real_fields():
    """`MSB_ENTRY_REFERENCES` drives `MSB.reattach_entry_references()`; every name must be a field."""
    bad = {}
    for supertype, subtypes in MSB.MSB_ENTRY_SUBTYPES.items():
        for info in subtypes.values():
            entry_class = info.entry_class
            try:
                field_names = {f.name for f in dataclasses.fields(entry_class)}
            except TypeError:
                continue
            missing = [name for name in entry_class.MSB_ENTRY_REFERENCES if name not in field_names]
            if missing:
                bad[entry_class.__name__] = missing
    if bad:
        pytest.xfail(
            f"BUG: `MSB_ENTRY_REFERENCES` names fields that do not exist -- "
            f"`MSB.reattach_entry_references()` raises `AttributeError`: {bad}. "
            f"(DeS `MSBObject`/`MSBDummyObject` list 'draw_parent', but the DeS Object subtype struct "
            f"has no draw parent -- see the comment in demonssouls/maps/parts.py:198.)"
        )


def test_reattach_entry_references_works_for_characters():
    msb = _populated_msb()
    character = msb.characters[0]
    character.draw_parent = msb.collisions[0]
    msb.reattach_entry_references(character)
    assert character.draw_parent is msb.collisions[0]


@pytest.mark.xfail(
    reason="BUG: same root cause as `test_msb_entry_references_name_real_fields` -- DeS `MSBObject` "
           "declares a `draw_parent` reference it does not have.",
    strict=False,
)
def test_reattach_entry_references_works_for_objects():
    msb = _populated_msb()
    msb.reattach_entry_references(msb.objects[0])


# ---------------------------------------------------------------------------
# Binary round-trips (in-memory, big-endian)
# ---------------------------------------------------------------------------


def test_big_endian_msb_binary_roundtrip_is_byte_stable():
    msb = _populated_msb(ByteOrder.BigEndian)
    packed = bytes(msb)
    reloaded = MSB.from_bytes(packed)
    assert reloaded.byte_order == ByteOrder.BigEndian
    assert len(reloaded.map_pieces) == 1
    assert len(reloaded.objects) == 1
    assert len(reloaded.characters) == 1
    assert len(reloaded.collisions) == 1
    assert len(reloaded.navmeshes) == 1
    assert len(reloaded.player_starts) == 1
    assert len(reloaded.regions) == 1
    assert len(reloaded.sounds) == 1
    assert bytes(reloaded) == packed


def test_roundtrip_preserves_entry_references():
    msb = _populated_msb()
    msb.characters[0].draw_parent = msb.collisions[0]
    connect = msb.create_connect_collision_from_collision(
        msb.collisions[0], (2, 1, 0, 0), name="h0000B0_0000_[02_01]"
    )
    assert connect.collision is msb.collisions[0]
    reloaded = MSB.from_bytes(bytes(msb))
    assert reloaded.characters[0].draw_parent is reloaded.collisions[0]
    assert reloaded.connect_collisions[0].collision is reloaded.collisions[0]
    assert reloaded.connect_collisions[0].connected_map_stem == "m02_01_00_00"


def test_roundtrip_preserves_entity_ids_and_names():
    msb = _populated_msb()
    packed = bytes(msb)
    reloaded = MSB.from_bytes(packed)
    assert reloaded.characters[0].name == "c1000_0000"
    assert reloaded.characters[0].entity_id == 1000
    assert reloaded.regions[0].entity_id == 2000
    assert reloaded.sounds[0].entity_id == 3800


@pytest.mark.xfail(
    reason="BUG: `MSB.byte_order` defaults to `ByteOrder.LittleEndian` (base/maps/msb/core.py:127) "
           "and `to_writer` uses `self.byte_order`, but `from_reader` forces big-endian when "
           "`IS_BIG_ENDIAN`. A freshly-constructed Demon's Souls `MSB()` therefore writes a "
           "little-endian file that neither the PS3 game nor Soulstruct's own reader can parse. "
           "`IS_BIG_ENDIAN` should seed the `byte_order` default.",
    strict=False,
)
def test_default_msb_byte_order_follows_is_big_endian():
    assert MSB().byte_order == ByteOrder.BigEndian
    msb = _populated_msb(byte_order=MSB().byte_order)
    MSB.from_bytes(bytes(msb))  # must not raise


def test_json_roundtrip(tmp_path):
    msb = _populated_msb()
    json_path = tmp_path / "des.msb.json"
    msb.write_json(json_path)
    reloaded = MSB.from_json(json_path)
    assert len(reloaded.characters) == len(msb.characters)
    assert reloaded.characters[0].name == msb.characters[0].name
    assert len(reloaded.map_piece_models) == len(msb.map_piece_models)


# ---------------------------------------------------------------------------
# Entry behaviour
# ---------------------------------------------------------------------------


def test_dummy_parts_subclass_their_real_counterparts():
    assert issubclass(MSBDummyObject, MSBObject)
    assert issubclass(MSBDummyCharacter, MSBCharacter)
    assert MSBDummyObject.SUBTYPE_ENUM == MSBPartSubtype.DummyObject
    assert MSBDummyCharacter.SUBTYPE_ENUM == MSBPartSubtype.DummyCharacter
    assert MSBDummyObject.SIB_PATH_TEMPLATE == ""


def test_collision_place_name_banner_property_validation():
    collision = MSBCollision(name="h0000B0")
    assert collision.place_name_banner_id == -1
    assert collision.force_place_name_banner is True
    with pytest.raises(Exception):
        collision.force_place_name_banner = False  # invalid while banner ID is -1
    collision.place_name_banner_id = 10
    collision.force_place_name_banner = False
    assert collision.force_place_name_banner is False


@pytest.mark.xfail(
    reason="BUG: `MSBCollision.navmesh_groups` documents \"defaults to being the same as "
           "`display_groups`\" and `__post_init__` implements that via an `is None` check, but "
           "`MSBEntry.__setattr__` coerces the `None` default to an empty `BitSet128` first, so "
           "`__post_init__` never fires (demonssouls/maps/parts.py:439, 450-453).",
    strict=False,
)
def test_collision_navmesh_groups_defaults_to_display_groups():
    collision = MSBCollision(name="h0000B0")
    assert collision.navmesh_groups == collision.display_groups


def test_connect_collision_map_stem_getter():
    connect = MSBConnectCollision(name="h0000B0_[01_00]")
    assert connect.connected_map_id == [1, 0, 0, 0]
    assert connect.connected_map_stem == "m01_00_00_00"
    connect.connected_map_id = [2, 1, 0, 0]
    assert connect.connected_map_stem == "m02_01_00_00"


@pytest.mark.xfail(
    reason="BUG: `MSBConnectCollision.connected_map_stem` has a setter, but `MSBEntry.__setattr__` "
           "rejects any key that is not a dataclass field before Python can reach the property "
           "setter, so the setter is dead code and raises "
           "`ValueError: Invalid MSBEntry subclass field` (demonssouls/maps/parts.py:636-641).",
    strict=False,
)
def test_connect_collision_map_stem_setter():
    connect = MSBConnectCollision(name="h0000B0_[01_00]")
    connect.connected_map_stem = "m02_01_00_00"
    assert connect.connected_map_id == [2, 1, 0, 0]


def test_player_start_uses_character_model():
    msb = MSB()
    player_start = msb.player_starts.new(name="c0000_0000")
    model = msb.auto_model(player_start, "c0000")
    assert model in msb.character_models
    assert player_start.model is model


def test_auto_model_rejects_unmodelled_part_types():
    """`MSBProtoboss` (a DeS-only Part subtype) has no `auto_*_model()` branch."""
    msb = MSB()
    protoboss = msb.protobosses.new(name="pb0")
    with pytest.raises(TypeError):
        msb.auto_model(protoboss, "c1000")


def test_new_light_event_with_point_creates_region():
    msb = MSB()
    light = msb.new_light_event_with_point(Vector3([1.0, 2.0, 3.0]), EulerDeg([0.0, 0.0, 0.0]), name="light0")
    assert light.attached_region is msb.regions[0]
    assert msb.regions[0].name == "_LightEvent_light0"


@pytest.mark.xfail(
    reason="BUG: `MSB.new_light_event_with_point` guards against the key 'base_region_name' "
           "(demonssouls/maps/msb.py:383) but actually assigns `attached_region`; the other "
           "`new_*_with_*` helpers correctly guard `attached_region`. Passing `attached_region=` "
           "silently has its value overwritten instead of raising.",
    strict=False,
)
def test_new_light_event_with_point_rejects_attached_region_kwarg():
    msb = MSB()
    with pytest.raises(KeyError):
        msb.new_light_event_with_point(
            Vector3([0.0, 0.0, 0.0]), EulerDeg([0.0, 0.0, 0.0]), name="light0", attached_region=None
        )


def test_new_sound_event_with_box_creates_region():
    msb = MSB()
    sound = msb.new_sound_event_with_box(
        Vector3([0.0, 0.0, 0.0]), EulerDeg([0.0, 0.0, 0.0]), 1.0, 2.0, 3.0, name="sound0"
    )
    assert sound.attached_region is msb.regions[0]
    assert msb.regions[0].shape.width == 1.0


def test_region_points_and_volumes_partition_regions():
    msb = MSB()
    zero, no_rot = Vector3([0.0, 0.0, 0.0]), EulerDeg([0.0, 0.0, 0.0])
    msb.new_light_event_with_point(zero, no_rot, name="light0")  # creates a Point region
    msb.new_sound_event_with_box(zero, no_rot, 1.0, 1.0, 1.0, name="sound0")  # Box region
    assert len(msb.region_points) == 1
    assert len(msb.region_volumes) == 1
    assert len(msb.regions) == 2


def test_new_c1000_creates_character_and_model():
    msb = MSB()
    character = msb.new_c1000("debug_warp")
    assert character.model.name == "c1000"
    assert character.model in msb.character_models


# ---------------------------------------------------------------------------
# Map constants
# ---------------------------------------------------------------------------


def test_des_map_constants_are_unique():
    names = [m.name for m in des_map_constants.ALL_MAPS]
    assert len(names) == len(set(names)), names


def test_des_map_variable_names_resolve():
    for game_map in des_map_constants.ALL_MAPS:
        if game_map.variable_name:
            assert getattr(des_map_constants, game_map.variable_name) is game_map


def test_map_studio_directory_properties_cover_all_msb_maps():
    from soulstruct.demonssouls.maps.map_studio_directory import MapStudioDirectory

    assert MapStudioDirectory.FILE_CLASS is MSB
    assert all(m.msb_file_stem for m in MapStudioDirectory.ALL_MAPS)
    bound = set()
    for name in dir(MapStudioDirectory):
        attr = MapStudioDirectory.__dict__.get(name)
        if attr is None or not hasattr(attr, "fget"):
            continue
        for cell in getattr(attr.fget, "__closure__", None) or ():
            if type(cell.cell_contents).__name__ == "Map":
                bound.add(cell.cell_contents.name)
    missing = {m.name for m in MapStudioDirectory.ALL_MAPS} - bound
    assert not missing, f"`MapStudioDirectory` has no property for maps: {missing}"


# ---------------------------------------------------------------------------
# Game-data round-trips (skipped without a Demon's Souls installation)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_real_msb_binary_roundtrip(des_root, tmp_path):
    from conftest import binary_roundtrip

    msb_dir = des_root / "map/mapstudio"
    if not msb_dir.is_dir():
        pytest.skip(f"Missing DeS MapStudio directory: {msb_dir}")
    paths = sorted(msb_dir.glob("*.msb"))
    if not paths:
        pytest.skip("No DeS MSB files found.")
    msb = MSB.from_path(paths[0])
    assert msb.byte_order == ByteOrder.BigEndian
    reloaded = binary_roundtrip(msb, tmp_path, paths[0].name)
    assert len(reloaded.parts) == len(msb.parts)


@pytest.mark.slow
@pytest.mark.game_data
def test_all_real_msbs_roundtrip_byte_identically(des_root, tmp_path):
    from conftest import assert_bytes_equal

    msb_dir = des_root / "map/mapstudio"
    if not msb_dir.is_dir():
        pytest.skip(f"Missing DeS MapStudio directory: {msb_dir}")
    paths = sorted(msb_dir.glob("*.msb"))
    if not paths:
        pytest.skip("No DeS MSB files found.")
    for path in paths:
        original = path.read_bytes()
        msb = MSB.from_bytes(original)
        assert_bytes_equal(bytes(msb), original, context=path.name)


@pytest.mark.slow
@pytest.mark.game_data
def test_map_studio_directory_loads(des_root):
    from soulstruct.demonssouls.maps.map_studio_directory import MapStudioDirectory

    msb_dir = des_root / "map/mapstudio"
    if not msb_dir.is_dir():
        pytest.skip(f"Missing DeS MapStudio directory: {msb_dir}")
    directory = MapStudioDirectory(msb_dir)
    assert directory.files


@pytest.mark.xfail(
    reason="BUG: the `MSB.new_*_with_*` helpers are all annotated "
           "`rotate: EulerDeg | tuple[float, float, float] | list[float]`, but "
           "`MSBEntry.__setattr__` only auto-converts sequences for `Vector2/3/4` field types -- "
           "not `EulerDeg` -- so passing a tuple raises "
           "`ValueError: Could not set/convert value ... MSBRegion.rotate` "
           "(base/maps/msb/msb_entry.py:756-767).",
    strict=False,
)
def test_new_light_event_accepts_tuple_rotate_as_annotated():
    msb = MSB()
    msb.new_light_event_with_point((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), name="light0")
