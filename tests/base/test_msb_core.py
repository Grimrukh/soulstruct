"""Tests for the shared `MSB` container machinery (`soulstruct.base.maps.msb.core`) and
`MSBEntryList` (`soulstruct.base.maps.msb.msb_entry_list`).

The concrete DS1 (PTDE) `MSB` subclass is used purely as a vehicle for exercising *base-class*
behaviour -- cross-entry reference resolution, subtype/supertype registration, name lookup,
deletion semantics and (de)serialisation. Game-specific field checks belong in the per-game
test modules.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

import pytest

from soulstruct.base.maps.msb.enums import BaseMSBPartSubtype, MSBSupertype
from soulstruct.base.maps.msb.msb_entry import MSBEntry
from soulstruct.base.maps.msb.msb_entry_list import MSBEntryList
from soulstruct.base.maps.msb.utils import BitSet128, MSBBrokenEntryReference, MSBSubtypeInfo, merge, translate_all
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.misc import IDList

from soulstruct.darksouls1ptde.maps.msb import MSB as PTDE_MSB


PTDE_MSB_RELPATH = ("darksouls1ptde", "resources", "m10_00_00_00.msb")
DSR_MSB_RELPATH = ("darksouls1r", "resources", "m10_00_00_00.msb")


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def ptde_msb_path(tests_dir):
    path = tests_dir.joinpath(*PTDE_MSB_RELPATH)
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


@pytest.fixture
def msb(ptde_msb_path) -> PTDE_MSB:
    """Fresh `MSB` per test (tests mutate it)."""
    return PTDE_MSB.from_path(ptde_msb_path)


@pytest.fixture
def empty_msb() -> PTDE_MSB:
    return PTDE_MSB()


# ---------------------------------------------------------------------------
# Synthetic entry classes for pure `MSBEntryList` unit tests
# ---------------------------------------------------------------------------


class ListTestSubtype(BaseMSBPartSubtype):
    Widget = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBWidget(MSBEntry):
    NAME_ENCODING = "utf-8"
    SUPERTYPE_ENUM = MSBSupertype.PARTS
    SUBTYPE_ENUM = ListTestSubtype.Widget
    STRUCTS = {}

    entity_id: int = -1
    value: int = 0


def make_widget_list(*names: str) -> MSBEntryList[MSBWidget]:
    return MSBEntryList(
        [MSBWidget(name=n) for n in names],
        supertype=MSBSupertype.PARTS,
        entry_class=MSBWidget,
    )


# ---------------------------------------------------------------------------
# MSBEntryList: pure unit tests
# ---------------------------------------------------------------------------


def test_entry_list_subtype_name_and_supertype():
    entry_list = make_widget_list("a", "b")
    assert entry_list.subtype_name == "Widget"
    assert entry_list.supertype == MSBSupertype.PARTS


def test_entry_list_getitem_by_index_and_name():
    entry_list = make_widget_list("a", "b", "c")
    assert entry_list[1].name == "b"
    assert entry_list["c"].name == "c"
    with pytest.raises(KeyError):
        _ = entry_list["nope"]


def test_entry_list_find_entry_name_ambiguity():
    entry_list = make_widget_list("a", "a")
    with pytest.raises(ValueError):
        entry_list.find_entry_name("a")


def test_entry_list_find_entry_names_and_get_entry_names():
    entry_list = make_widget_list("a", "b", "c")
    assert entry_list.get_entry_names() == ["a", "b", "c"]
    assert [e.name for e in entry_list.find_entry_names({"a", "c"})] == ["a", "c"]


def test_entry_list_get_entries_by_unique_name():
    entry_list = make_widget_list("a", "b", "a", "c")
    unique, ambiguous = entry_list.get_entries_by_unique_name()
    assert set(unique) == {"b", "c"}
    assert ambiguous == {"a"}


def test_entry_list_new_appends_and_accepts_kwargs():
    entry_list = make_widget_list("a")
    new = entry_list.new(name="b", value=7)
    assert new.name == "b" and new.value == 7
    assert entry_list[-1] is new
    default = entry_list.new()
    assert default.name == "DefaultMSBWidget"


def test_entry_list_new_with_entity_enum():
    from enum import IntEnum

    class Widgets(IntEnum):
        BIG_WIDGET = 4321

    entry_list = make_widget_list()
    new = entry_list.new(entity_enum=Widgets.BIG_WIDGET)
    assert (new.name, new.entity_id) == ("BIG_WIDGET", 4321)
    with pytest.raises(ValueError):
        entry_list.new(entity_enum=Widgets.BIG_WIDGET, name="other")


def test_entry_list_default_entry_does_not_append():
    entry_list = make_widget_list("a")
    default = entry_list.default_entry()
    assert default.name == "DefaultMSBWidget"
    assert len(entry_list) == 1


def test_entry_list_duplicate_inserts_after_source():
    entry_list = make_widget_list("a", "b", "c")
    dup = entry_list.duplicate("b")
    assert dup.name == "b <COPY>"
    assert entry_list.get_entry_names() == ["a", "b", "b <COPY>", "c"]


def test_entry_list_duplicate_applies_kwargs_and_name():
    entry_list = make_widget_list("a")
    dup = entry_list.duplicate(0, name="a2", value=9)
    assert dup.name == "a2" and dup.value == 9


def test_entry_list_duplicate_at_end_with_negative_offset():
    entry_list = make_widget_list("a", "b", "c")
    dup = entry_list.duplicate("a", index_offset=-1)
    assert entry_list[-1] is dup


def test_entry_list_duplicate_foreign_entry_appends():
    entry_list = make_widget_list("a")
    foreign = MSBWidget(name="foreign")
    dup = entry_list.duplicate(foreign)
    assert entry_list[-1] is dup


def test_entry_list_new_at_index_keeps_indices_consistent():
    entry_list = make_widget_list("a", "b", "c")
    new = entry_list.new(0, name="z")
    assert entry_list[0] is new
    assert entry_list.index(new) == 0
    assert entry_list.index(entry_list[1]) == 1


def test_entry_list_remove_after_insert_removes_correct_entry():
    entry_list = make_widget_list("a", "b")
    new = entry_list.new(0, name="z")
    entry_list.remove(new)
    assert entry_list.get_entry_names() == ["a", "b"]


def test_entry_list_get_entity_id_dict_ignores_null_ids():
    entry_list = make_widget_list("a", "b", "c")
    entry_list[0].entity_id = 300
    entry_list[1].entity_id = -1
    entry_list[2].entity_id = 100
    by_id = entry_list.get_entity_id_dict()
    assert set(by_id) == {300, 100}
    assert list(entry_list.get_entity_id_dict(sort_by_entity_id=True)) == [100, 300]


def test_entry_list_get_filtered_list_deep_copies():
    entry_list = make_widget_list("a", "b")
    filtered = entry_list.get_filtered_list(lambda e: e.name == "a")
    assert filtered.get_entry_names() == ["a"]
    assert filtered[0] is not entry_list[0]
    assert filtered.subtype_name == entry_list.subtype_name
    assert entry_list.get_filtered_list(None).get_entry_names() == ["a", "b"]


def test_entry_list_sort_by_name_keeps_indices_valid():
    entry_list = make_widget_list("c", "a", "b")
    entry_list.sort_by_name()
    assert entry_list.get_entry_names() == ["a", "b", "c"]
    for i, entry in enumerate(entry_list):
        assert entry_list.index(entry) == i


def test_entry_list_rejects_duplicate_instance():
    entry_list = make_widget_list("a")
    with pytest.raises(ValueError):
        entry_list.append(entry_list[0])


def test_entry_list_to_dict():
    entry_list = make_widget_list("a")
    assert entry_list.to_dict() == {"Widget": [{"name": "a"}]}


def test_msb_subtype_info_matches_name():
    info = MSBSubtypeInfo(MSBWidget, "widgets")
    assert info.matches_name("widgets")
    assert info.matches_name("Widget")
    assert info.matches_name("Widgets")
    assert info.matches_name("MSBWidget")
    assert not info.matches_name("Gadget")


# ---------------------------------------------------------------------------
# Subtype/supertype registration and lookup
# ---------------------------------------------------------------------------


def test_subtype_list_names_cover_all_registered_subtypes(empty_msb):
    registered = {
        info.subtype_list_name
        for subtypes in PTDE_MSB.MSB_ENTRY_SUBTYPES.values()
        for info in subtypes.values()
    }
    declared = set(PTDE_MSB.get_subtype_list_names())
    assert registered == declared, "Every registered subtype must have a dataclass field, and vice versa."


def test_every_subtype_list_has_matching_supertype_and_class(empty_msb):
    for supertype_name, subtypes in PTDE_MSB.MSB_ENTRY_SUBTYPES.items():
        for subtype_enum, info in subtypes.items():
            entry_list = getattr(empty_msb, info.subtype_list_name)
            assert isinstance(entry_list, MSBEntryList)
            assert entry_list.supertype == supertype_name
            assert entry_list.entry_class is info.entry_class
            assert info.entry_class.SUBTYPE_ENUM is subtype_enum
            assert info.entry_class.SUPERTYPE_ENUM == supertype_name


def test_resolve_supertype_name_aliases():
    assert PTDE_MSB.resolve_supertype_name("models") == "MODEL_PARAM_ST"
    assert PTDE_MSB.resolve_supertype_name("EVENTS") == "EVENT_PARAM_ST"
    assert PTDE_MSB.resolve_supertype_name("regions") == "POINT_PARAM_ST"
    assert PTDE_MSB.resolve_supertype_name("POINT_PARAM_ST") == "POINT_PARAM_ST"
    assert PTDE_MSB.resolve_supertype_name("parts") == "PARTS_PARAM_ST"
    with pytest.raises(ValueError):
        PTDE_MSB.resolve_supertype_name("bogus")


def test_resolve_subtype_name_accepts_multiple_spellings():
    assert PTDE_MSB.resolve_subtype_name("characters") == "characters"
    assert PTDE_MSB.resolve_subtype_name("Character") == "characters"
    assert PTDE_MSB.resolve_subtype_name("MSBCharacter") == "characters"
    assert PTDE_MSB.resolve_subtype_name("CharacterModel") == "character_models"
    with pytest.raises(KeyError):
        PTDE_MSB.resolve_subtype_name("bogus")


def test_resolve_subtype_name_can_be_restricted_to_supertype():
    assert PTDE_MSB.resolve_subtype_name("MapPieceModel", "MODEL_PARAM_ST") == "map_piece_models"
    with pytest.raises(KeyError):
        PTDE_MSB.resolve_subtype_name("MapPiece", "MODEL_PARAM_ST")


def test_msb_getitem_uses_subtype_resolution(empty_msb):
    assert empty_msb["characters"] is empty_msb.characters
    assert empty_msb["Character"] is empty_msb.characters
    assert empty_msb["MSBCharacter"] is empty_msb.characters


def test_get_display_type_dict_ordering():
    display = PTDE_MSB.get_display_type_dict()
    assert list(display) == ["Parts", "Regions", "Events", "Models"]
    assert all(isinstance(v, tuple) and v for v in display.values())


def test_get_supertype_subtype_dict_returns_live_lists(empty_msb):
    parts_dict = empty_msb.get_parts_dict()
    for subtype_enum, entry_list in parts_dict.items():
        assert entry_list is getattr(empty_msb, PTDE_MSB.MSB_ENTRY_SUBTYPES["PARTS_PARAM_ST"][subtype_enum].subtype_list_name)


def test_get_version_dict_matches_class_vars():
    assert PTDE_MSB.get_version_dict() == {
        "has_header": PTDE_MSB.HAS_HEADER,
        "long_varints": PTDE_MSB.LONG_VARINTS,
        "name_encoding": PTDE_MSB.NAME_ENCODING,
    }


# ---------------------------------------------------------------------------
# Binary round-trips and reference resolution
# ---------------------------------------------------------------------------


def test_binary_roundtrip_is_stable(msb, tmp_path):
    packed_1 = bytes(msb.to_writer())
    reloaded = PTDE_MSB.from_bytes(packed_1)
    packed_2 = bytes(reloaded.to_writer())
    assert packed_1 == packed_2, "unpack -> pack -> unpack -> pack must be byte-stable"


def test_binary_roundtrip_preserves_all_entry_counts(msb):
    reloaded = PTDE_MSB.from_bytes(bytes(msb.to_writer()))
    for original_list, new_list in zip(msb.get_all_subtype_lists(), reloaded.get_all_subtype_lists()):
        assert len(original_list) == len(new_list)
        assert original_list.get_entry_names() == new_list.get_entry_names()


def test_binary_roundtrip_preserves_entry_equality(msb):
    reloaded = PTDE_MSB.from_bytes(bytes(msb.to_writer()))
    for original_list, new_list in zip(msb.get_all_subtype_lists(), reloaded.get_all_subtype_lists()):
        for original, new in zip(original_list, new_list):
            assert original == new, f"{original_list.subtype_name} entry '{original.name}' changed"


def test_no_broken_references_after_unpack(msb):
    """Every consumed index must have resolved to a real entry (never `MSBBrokenEntryReference`)."""
    for entry_list in msb:
        for entry in entry_list:
            for field_name in entry.get_field_names():
                value = getattr(entry, field_name)
                assert not isinstance(value, MSBBrokenEntryReference), f"{entry.name}.{field_name}"
                if isinstance(value, list):
                    assert not any(isinstance(v, MSBBrokenEntryReference) for v in value)


def test_all_referenced_entries_live_in_the_msb(msb):
    """Cross-entry references must point at objects that are actually in one of the MSB's lists."""
    all_entries = IDList()
    for entry_list in msb:
        all_entries.extend(entry_list)
    for entry_list in msb:
        for entry in entry_list:
            for field_name in entry.get_field_names():
                value = getattr(entry, field_name)
                if isinstance(value, MSBEntry):
                    assert value in all_entries, f"{entry.name}.{field_name} -> {value.name} (orphan)"
                elif isinstance(value, list):
                    for element in value:
                        if isinstance(element, MSBEntry):
                            assert element in all_entries


def test_every_part_has_a_model_in_a_model_list(msb):
    models = msb.get_models()
    for part in msb.get_parts():
        assert part.model is not None, f"Part '{part.name}' has no model."
        assert part.model in models


def test_reordering_a_subtype_list_preserves_object_references(msb):
    """Indices are recomputed at pack time, so reordering entries must NOT break references."""
    expected = {
        char.name: (char.model.name, char.draw_parent.name if char.draw_parent else None)
        for char in msb.characters
    }
    msb.characters.sort(key=lambda e: e.name, reverse=True)
    msb.regions.sort(key=lambda e: e.name)
    reloaded = PTDE_MSB.from_bytes(bytes(msb.to_writer()))
    for char in reloaded.characters:
        model_name, parent_name = expected[char.name]
        assert char.model.name == model_name
        assert (char.draw_parent.name if char.draw_parent else None) == parent_name


def test_event_region_references_survive_region_reordering(msb):
    expected = {
        (event.name, i): (event.attached_region.name if event.attached_region else None)
        for i, event in enumerate(msb.get_events())
    }
    msb.regions.sort(key=lambda e: e.name)
    reloaded = PTDE_MSB.from_bytes(bytes(msb.to_writer()))
    for i, event in enumerate(reloaded.get_events()):
        assert (event.attached_region.name if event.attached_region else None) == expected[(event.name, i)]


def test_removing_a_referenced_entry_clears_referrer(msb):
    collision = msb.characters[0].draw_parent
    assert collision is not None
    msb.remove_entry(collision, clear_referrers=True)
    assert msb.characters[0].draw_parent is None  # referrer cleared


def test_removing_a_referenced_entry_without_clearing_referrer(msb):
    collision = msb.characters[0].draw_parent
    assert collision is not None
    msb.remove_entry(collision, clear_referrers=False)
    assert msb.characters[0].draw_parent is collision  # referrer not cleared


def test_remove_entry_rejects_foreign_entry(msb, ptde_msb_path):
    other = PTDE_MSB.from_path(ptde_msb_path)
    with pytest.raises(ValueError):
        msb.remove_entry(other.characters[0])


def test_get_list_of_entry(msb):
    char = msb.characters[0]
    assert msb.get_list_of_entry(char) is msb.characters


def test_clear_all(msb):
    msb.clear_all()
    assert all(len(entry_list) == 0 for entry_list in msb)


def test_add_entry_dispatches_by_subtype(empty_msb):
    model = empty_msb.character_models.new(name="c1000")
    char = empty_msb.characters.entry_class(name="c1000_0000", model=model)
    empty_msb.characters.remove  # (sanity: attribute exists)
    empty_msb.add_entry(char)
    assert empty_msb.characters[-1] is char


# ---------------------------------------------------------------------------
# Name / entity ID lookup
# ---------------------------------------------------------------------------


def test_find_entry_name_across_all_types(msb):
    char = msb.characters[0]
    assert msb.find_entry_name(char.name) is char
    with pytest.raises(KeyError):
        msb.find_entry_name("definitely_not_here")


def test_find_entry_name_supertype_filter(msb):
    model = msb.character_models[0]
    assert msb.find_model_name(model.name) is model
    with pytest.raises(KeyError):
        msb.find_part_name(model.name)


def test_find_entry_name_subtypes_filter_uses_list_names(msb):
    char = msb.characters[0]
    assert msb.find_entry_name(char.name, subtypes=["characters"]) is char


def test_find_entry_name_subtypes_filter_accepts_subtype_enum_names(msb):
    char = msb.characters[0]
    assert msb.find_entry_name(char.name, subtypes=["Character"]) is char


def test_find_entry_by_entity_id(msb):
    char = next(c for c in msb.characters if c.entity_id > 0)
    assert msb.find_entry_by_entity_id(char.entity_id) is char
    with pytest.raises(ValueError):
        msb.find_entry_by_entity_id(0)
    with pytest.raises(KeyError):
        msb.find_entry_by_entity_id(999_999_999)


def test_get_supertype_entity_id_dicts(msb):
    by_id = msb.get_supertype_entity_id_dict("PARTS_PARAM_ST")
    assert by_id
    assert all(entity_id > 0 for entity_id in by_id)
    names = msb.get_supertype_entity_id_name_dict("PARTS_PARAM_ST")
    assert {k: v.name for k, v in by_id.items()} == names


def test_get_repeated_entity_ids_structure(msb):
    repeats = msb.get_repeated_entity_ids()
    assert set(repeats) == set(msb.entity_id_supertypes())
    for supertype, entries in repeats.items():
        assert isinstance(entries, IDList)


def test_resolve_entries_list_accepts_names_and_entries(msb):
    char_0, char_1 = msb.characters[0], msb.characters[1]
    resolved = msb.resolve_entries_list([char_0.name, char_1])
    assert [e.name for e in resolved] == [char_0.name, char_1.name]
    assert len(msb.resolve_entries_list([])) == 0
    with pytest.raises(TypeError):
        msb.resolve_entries_list([1234])


def test_resolve_entries_list_tolerates_repeated_entry(msb):
    char = msb.characters[0]
    resolved = msb.resolve_entries_list([char.name, char])
    assert len(resolved) == 1
    assert resolved[0] is char


def test_get_supertype_list_is_a_snapshot(msb):
    parts = msb.get_parts()
    assert len(parts) == sum(len(lst) for lst in msb if lst.supertype == "PARTS_PARAM_ST")
    parts.clear()  # transient copy
    assert len(msb.get_parts()) > 0


def test_get_regions_with_shape(msb):
    points = msb.get_regions_with_shape("point")
    assert points
    assert all(r.shape.SHAPE_TYPE.name == "Point" for r in points)


def test_get_map_stem_from_path(msb):
    assert msb.get_map_stem() == "m10_00_00_00"


def test_get_map_stem_requires_path(empty_msb):
    with pytest.raises(ValueError):
        empty_msb.get_map_stem()


def test_has_c0000_model(msb, empty_msb):
    assert msb.has_c0000_model() is True
    assert empty_msb.has_c0000_model() is False


def test_remove_unused_models(msb):
    used = {part.model.name for part in msb.get_parts() if part.model}
    removed = msb.remove_unused_models()
    assert removed
    assert not set(removed) & used
    assert all(model.name in used for model in msb.get_models())


def test_get_models_of_part_subtype(msb):
    assert msb.get_models_of_part_subtype("Character") is msb.character_models


def test_get_or_create_model_by_part_subtype_name(msb):
    model = msb.get_or_create_model("MapPiece", "mZZZZB0", map_stem="m10_00_00_00")
    assert model.name == "mZZZZB0"
    assert model in msb.map_piece_models


# ---------------------------------------------------------------------------
# Dict / JSON serialisation
# ---------------------------------------------------------------------------


def _build_small_msb() -> PTDE_MSB:
    """Small hand-built MSB with cross-references but no rotations (see EulerDeg JSON bug)."""
    msb = PTDE_MSB()
    char_model = msb.character_models.new(name="c1000", sib_path="N:\\c1000.sib")
    col_model = msb.collision_models.new(name="h0000B0", sib_path="N:\\h0000B0.sib")
    collision = msb.collisions.new(name="h0000B0_0000", model=col_model, entity_id=3200)
    char = msb.characters.new(
        name="c1000_0000", model=char_model, entity_id=1000, draw_parent=collision,
        translate=Vector3((1.0, 2.0, 3.0)),
    )
    region = msb.regions.new(name="Point0", entity_id=2000, translate=Vector3((4.0, 5.0, 6.0)))
    sound = msb.sounds.new(name="Sound0", entity_id=3800, attached_region=region, attached_part=char)
    assert sound.attached_part is char
    return msb


def test_small_msb_binary_roundtrip():
    msb = _build_small_msb()
    packed = bytes(msb.to_writer())
    reloaded = PTDE_MSB.from_bytes(packed)
    assert reloaded.characters[0].draw_parent is reloaded.collisions[0]
    assert reloaded.sounds[0].attached_region is reloaded.regions[0]
    assert reloaded.sounds[0].attached_part is reloaded.characters[0]
    assert bytes(reloaded.to_writer()) == packed


def test_to_dict_has_expected_top_level_shape():
    data = _build_small_msb().to_dict()
    assert set(data) >= {"version", "MODEL_PARAM_ST", "PARTS_PARAM_ST", "POINT_PARAM_ST", "EVENT_PARAM_ST"}
    # Every registered subtype gets a key, even when empty.
    assert set(data["PARTS_PARAM_ST"]) == {
        info.entry_class.SUBTYPE_ENUM.name
        for info in PTDE_MSB.MSB_ENTRY_SUBTYPES["PARTS_PARAM_ST"].values()
    }
    assert [e["name"] for e in data["PARTS_PARAM_ST"]["Character"]] == ["c1000_0000"]


@pytest.mark.xfail(
    reason=(
        "`MSB.to_dict()` is not the inverse of `MSB.from_dict()`: `to_dict` leaves `BitSet` and "
        "`EulerDeg` values as live objects (relying on `MSB.JSONEncoder` at file-write time), but "
        "`from_json_dict` decoders expect their `repr` strings. Only the file round-trip works."
    ),
    strict=False,
)
def test_small_msb_dict_roundtrip():
    msb = _build_small_msb()
    data = msb.to_dict()
    restored = PTDE_MSB.from_dict(data)
    assert restored.characters[0].name == "c1000_0000"
    assert restored.characters[0].model is restored.character_models[0]
    assert restored.characters[0].draw_parent is restored.collisions[0]
    assert restored.sounds[0].attached_region is restored.regions[0]
    assert bytes(restored.to_writer()) == bytes(msb.to_writer())


def test_small_msb_json_file_roundtrip(tmp_path):
    msb = _build_small_msb()
    json_path = tmp_path / "small.msb.json"
    msb.write_json(json_path)
    restored = PTDE_MSB.from_json(json_path)
    assert bytes(restored.to_writer()) == bytes(msb.to_writer())


def test_from_dict_rejects_missing_or_wrong_version():
    data = {"version": PTDE_MSB.get_version_dict()}
    bad = dict(data)
    bad.pop("version")
    with pytest.raises(ValueError):
        PTDE_MSB.from_dict(bad)
    bad = dict(data)
    bad["version"] = {"has_header": True, "long_varints": True, "name_encoding": "utf-16-le"}
    with pytest.raises(TypeError):
        PTDE_MSB.from_dict(bad)


@pytest.mark.xfail(
    reason=(
        "`EulerDeg` fields are JSON-encoded via `repr()` (5-decimal precision) and decoded with "
        "the `EulerDeg` constructor, which cannot parse that string. Any MSB containing a "
        "non-default `rotate` therefore fails to reload from JSON."
    ),
    strict=False,
)
def test_full_msb_json_roundtrip(msb, tmp_path):
    json_path = tmp_path / "m10_00_00_00.msb.json"
    msb.write_json(json_path)
    restored = PTDE_MSB.from_json(json_path)
    assert bytes(restored.to_writer()) == bytes(msb.to_writer())


def test_entry_array_with_mixed_subtypes_serialises():
    msb = _build_small_msb()
    obj_model = msb.object_models.new(name="o0000")
    obj = msb.objects.new(name="o0000_0000", model=obj_model)
    spawner = msb.spawners.new(name="Spawner0")
    spawner.spawn_parts = [msb.characters[0], obj]
    data = spawner.to_json_dict(msb)
    assert len(data["spawn_parts"]) >= 2


def test_to_dict_ignore_defaults_flag():
    msb = _build_small_msb()
    lean = msb.to_dict(ignore_defaults=True)
    fat = msb.to_dict(ignore_defaults=False)
    lean_char = lean["PARTS_PARAM_ST"]["Character"][0]
    fat_char = fat["PARTS_PARAM_ST"]["Character"][0]
    assert set(lean_char) < set(fat_char)


def test_write_json_adds_suffix(tmp_path):
    msb = _build_small_msb()
    msb.write_json(tmp_path / "out.msb")
    assert (tmp_path / "out.msb.json").is_file()


# ---------------------------------------------------------------------------
# `msb.utils` helpers
# ---------------------------------------------------------------------------


def test_merge_rejects_non_callable_filter():
    msb_1 = _build_small_msb()
    msb_2 = _build_small_msb()
    with pytest.raises(ValueError):
        merge(msb_1, msb_2, filter_func="not callable")


def test_merge_two_msbs():
    msb_1 = _build_small_msb()
    msb_2 = _build_small_msb()
    with pytest.raises(ValueError):
        merge(msb_1, msb_2)  # repeated names
    merged = merge(msb_1, msb_2, allow_repeated_names=True)
    assert len(merged.characters) == 2
    assert merged.characters[0] is not msb_1.characters[0]  # deep-copied


def test_merge_with_filter_func():
    msb_1 = _build_small_msb()
    msb_2 = _build_small_msb()
    merged = merge(msb_1, msb_2, filter_func=lambda e: False)
    assert all(len(entry_list) == 0 for entry_list in merged)


def test_translate_all_moves_parts_and_regions():
    msb = _build_small_msb()
    old_part = Vector3(msb.characters[0].translate)
    old_region = Vector3(msb.regions[0].translate)
    translate_all(msb, Vector3((10.0, 0.0, -5.0)))
    assert tuple(msb.characters[0].translate) == tuple(old_part + Vector3((10.0, 0.0, -5.0)))
    assert tuple(msb.regions[0].translate) == tuple(old_region + Vector3((10.0, 0.0, -5.0)))


def test_translate_all_with_selected_entries():
    msb = _build_small_msb()
    old_region = Vector3(msb.regions[0].translate)
    translate_all(msb, Vector3((10.0, 0.0, 0.0)), selected_entries=[msb.characters[0]])
    assert tuple(msb.regions[0].translate) == tuple(old_region)  # untouched
    assert msb.characters[0].translate.x == 11.0


# ---------------------------------------------------------------------------
# DSR (same base machinery, different class registration)
# ---------------------------------------------------------------------------


def test_dsr_msb_binary_roundtrip(tests_dir):
    from soulstruct.darksouls1r.maps.msb import MSB as DSR_MSB

    path = tests_dir.joinpath(*DSR_MSB_RELPATH)
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    msb = DSR_MSB.from_path(path)
    packed_1 = bytes(msb.to_writer())
    packed_2 = bytes(DSR_MSB.from_bytes(packed_1).to_writer())
    assert packed_1 == packed_2
