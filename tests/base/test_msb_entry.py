"""Pure-unit tests for the shared `MSBEntry` machinery in `soulstruct.base.maps.msb.msb_entry`.

These tests define a small synthetic `MSBEntry` class hierarchy so that the base-class logic
(field type parsing, `__setattr__` validation/coercion, reference recording, index consumption,
JSON dict conversion) can be exercised entirely in memory, with no game data required.

IMPORTANT: the synthetic classes are deliberately *not* real game classes, because several
`MSBEntry` classmethods cache results permanently on the class they are first called on
(`_FIELD_TYPES`, `_FIELD_DEFAULTS`, ...). Using throwaway classes avoids poisoning real game
classes for other tests in the same session.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, field

import pytest

from soulstruct.base.maps.msb.enums import (
    BaseMSBModelSubtype,
    BaseMSBPartSubtype,
    BaseMSBRegionSubtype,
    MSBSupertype,
)
from soulstruct.base.maps.msb.msb_entry import (
    EntryRef,
    MSBEntry,
    MSBEntryReference,
)
from soulstruct.base.maps.msb.region_shapes import BoxShape, PointShape, RegionShapeType, SphereShape
from soulstruct.base.maps.msb.utils import BitSet128, BitSet256, MSBBrokenEntryReference
from soulstruct.utilities.maths import EulerDeg, Vector2, Vector3, Vector4
from soulstruct.utilities.misc import IDList


# ---------------------------------------------------------------------------
# Synthetic entry classes
# ---------------------------------------------------------------------------


class FakeModelSubtype(BaseMSBModelSubtype):
    FakeModel = 0


class FakePartSubtype(BaseMSBPartSubtype):
    FakePart = 0
    OtherPart = 1


class FakeRegionSubtype(BaseMSBRegionSubtype):
    FakeRegion = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBFakeModel(MSBEntry):
    NAME_ENCODING = "utf-8"
    SUPERTYPE_ENUM = MSBSupertype.MODELS
    SUBTYPE_ENUM = FakeModelSubtype.FakeModel
    STRUCTS = {}

    sib_path: str = ""


@dataclass(slots=True, eq=False, repr=False)
class MSBFakeRegion(MSBEntry):
    NAME_ENCODING = "utf-8"
    SUPERTYPE_ENUM = MSBSupertype.REGIONS
    SUBTYPE_ENUM = FakeRegionSubtype.FakeRegion
    STRUCTS = {}

    translate: Vector3 = field(default_factory=Vector3.zero)
    entity_id: int = -1


@dataclass(slots=True, eq=False, repr=False)
class MSBFakePart(MSBEntry):
    NAME_ENCODING = "utf-8"
    SUPERTYPE_ENUM = MSBSupertype.PARTS
    SUBTYPE_ENUM = FakePartSubtype.FakePart
    STRUCTS = {}
    MSB_ENTRY_REFERENCES = ["model", "draw_parent"]

    model: MSBFakeModel = None
    draw_parent: MSBFakePart | None = None
    entity_id: int = -1
    health: float = 1.0
    is_enabled: bool = False
    label: str = ""
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: EulerDeg = field(default_factory=EulerDeg.zero)
    draw_groups: BitSet128 = field(default_factory=BitSet128.all_off)
    counts: list[int] = field(default_factory=lambda: [0, 0, 0])
    ratios: list[float] = field(default_factory=lambda: [0.0, 0.0])
    patrol_regions: list[MSBFakeRegion | None] = field(default_factory=lambda: [None] * 4)

    _model_index: int = -1
    _draw_parent_index: int = -1
    _patrol_regions_indices: list[int] = field(default_factory=lambda: [-1] * 4)

    def indices_to_objects(self, entry_lists):
        self._consume_index(entry_lists, "MODEL_PARAM_ST", "model")
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "patrol_regions")


def _new_part(name="part", **kwargs) -> MSBFakePart:
    return MSBFakePart(name=name, **kwargs)


# ---------------------------------------------------------------------------
# get_field_types / get_field_names / defaults
# ---------------------------------------------------------------------------


def test_get_field_types_parses_all_annotation_kinds():
    types = MSBFakePart.get_field_types()
    assert types["entity_id"] == "int"
    assert types["health"] == "float"
    assert types["is_enabled"] == "bool"
    assert types["label"] == "str"
    assert types["translate"] == "Vector3"
    assert types["rotate"] == "EulerDeg"
    assert types["draw_groups"] == "BitSet128"
    # Lists get their length baked into the type string, detected from `default_factory`.
    assert types["counts"] == "int[3]"
    assert types["ratios"] == "float[2]"
    assert types["patrol_regions"] == "MSBFakeRegion[4]"
    # `| None` is stripped from single-reference fields.
    assert types["model"] == "MSBFakeModel"
    assert types["draw_parent"] == "MSBFakePart"


def test_get_field_types_is_cached_immutable_mapping():
    first = MSBFakePart.get_field_types()
    second = MSBFakePart.get_field_types()
    assert first is second
    with pytest.raises(TypeError):
        first["entity_id"] = "float"  # MappingProxyType is read-only


def test_get_field_names_excludes_name_description_and_privates():
    names = MSBFakePart.get_field_names()
    assert "name" not in names
    assert "description" not in names
    assert not any(n.startswith("_") for n in names)
    assert "entity_id" in names and "model" in names


def test_get_field_names_visible_only_respects_hide_fields():
    @dataclass(slots=True, eq=False, repr=False)
    class MSBHidden(MSBFakePart):
        HIDE_FIELDS = ("health",)

    assert "health" in MSBHidden.get_field_names(visible_only=False)
    assert "health" not in MSBHidden.get_field_names(visible_only=True)


def test_get_default_values():
    defaults = MSBFakePart.get_default_values()
    assert defaults["entity_id"] == -1
    assert defaults["counts"] == [0, 0, 0]
    assert defaults["model"] is None
    assert "name" not in defaults
    assert "description" not in defaults


@pytest.mark.xfail(
    reason=(
        "`_FIELD_TYPES`/`_FIELD_DEFAULTS`/... are read via normal attribute lookup, so whichever "
        "class in a hierarchy computes the cache first hands it to every subclass."
    ),
    strict=False,
)
def test_field_type_cache_is_not_inherited_by_subclasses():
    """Uses throwaway classes so that no real game class is poisoned for other tests."""

    @dataclass(slots=True, eq=False, repr=False)
    class MSBCacheBase(MSBEntry):
        NAME_ENCODING = "utf-8"
        SUPERTYPE_ENUM = MSBSupertype.PARTS
        SUBTYPE_ENUM = FakePartSubtype.FakePart
        STRUCTS = {}
        base_field: int = 0

    @dataclass(slots=True, eq=False, repr=False)
    class MSBCacheChild(MSBCacheBase):
        SUBTYPE_ENUM = FakePartSubtype.OtherPart
        child_field: float = 0.0

    MSBCacheBase.get_field_types()  # populates cache on the BASE class
    child_types = MSBCacheChild.get_field_types()
    assert "child_field" in child_types


# ---------------------------------------------------------------------------
# __setattr__ validation and coercion
# ---------------------------------------------------------------------------


def test_setattr_coerces_int_to_float():
    part = _new_part()
    part.health = 3  # int accepted for float field
    assert isinstance(part.health, float)
    assert part.health == 3.0


def test_setattr_rejects_float_for_int_field():
    part = _new_part()
    with pytest.raises(TypeError):
        part.entity_id = 1.5


def test_setattr_rejects_unknown_field():
    part = _new_part()
    with pytest.raises(ValueError):
        part.no_such_field = 1


def test_setattr_builds_vectors_from_sequences():
    part = _new_part()
    part.translate = (1, 2, 3)
    assert isinstance(part.translate, Vector3)
    assert tuple(part.translate) == (1.0, 2.0, 3.0)
    with pytest.raises(ValueError):
        part.translate = (1, 2)  # wrong length


def test_setattr_builds_bitset_from_set_and_list():
    part = _new_part()
    part.draw_groups = {1, 5, 9}
    assert isinstance(part.draw_groups, BitSet128)
    assert part.draw_groups.enabled_bits == {1, 5, 9}
    part.draw_groups = [0, 0, 0, 0]  # packed uints
    assert isinstance(part.draw_groups, BitSet128)
    assert part.draw_groups.enabled_bits == set()


def test_setattr_enforces_int_list_length_and_element_type():
    part = _new_part()
    part.counts = [1, 2, 3]
    assert part.counts == [1, 2, 3]
    with pytest.raises(ValueError):
        part.counts = [1, 2]
    with pytest.raises(TypeError):
        part.counts = [1, 2, "x"]
    with pytest.raises(TypeError):
        part.counts = 5  # not a sequence


def test_setattr_float_list_coerces_ints():
    part = _new_part()
    part.ratios = [1, 2]
    assert part.ratios == [1.0, 2.0]
    assert all(isinstance(v, float) for v in part.ratios)


def test_setattr_entry_reference_type_checked():
    part = _new_part()
    model = MSBFakeModel(name="m0")
    part.model = model
    assert part.model is model
    part.model = None
    assert part.model is None
    with pytest.raises(TypeError):
        part.model = MSBFakeRegion(name="r0")  # wrong entry type


def test_setattr_entry_list_pads_with_none_and_limits_length():
    part = _new_part()
    r0, r1 = MSBFakeRegion(name="r0"), MSBFakeRegion(name="r1")
    part.patrol_regions = [r0, r1]
    assert part.patrol_regions == [r0, r1, None, None]
    with pytest.raises(ValueError):
        part.patrol_regions = [r0] * 5  # exceeds max length 4
    with pytest.raises(TypeError):
        part.patrol_regions = [MSBFakeModel(name="m0")]


def test_setattr_name_and_description_must_be_str():
    part = _new_part()
    part.name = "abc"
    part.description = "desc"
    with pytest.raises(ValueError):
        part.name = 5


def test_setattr_checks_disabled_context_manager():
    part = _new_part()
    with MSBFakePart.setattr_checks_disabled():
        part.entity_id = "not an int"  # no validation
    assert part.entity_id == "not an int"
    part.entity_id = 5  # checks restored
    with pytest.raises(TypeError):
        part.entity_id = "not an int"


@pytest.mark.xfail(
    reason=(
        "`setattr_checks_disabled()` writes `SETATTR_CHECKS_DISABLED` onto the class it is called "
        "on. After any `from_dict`/`from_msb_reader`/`copy` call, the concrete subclass owns a "
        "`False` attribute that shadows the base flag, so `MSBEntry.setattr_checks_disabled()` "
        "(the documented global idiom) silently stops working."
    ),
    strict=False,
)
def test_setattr_checks_disabled_on_base_class_applies_to_subclasses():
    MSBFakePart.copy(_new_part())  # leaves `MSBFakePart.SETATTR_CHECKS_DISABLED = False`
    assert "SETATTR_CHECKS_DISABLED" in MSBFakePart.__dict__
    part = _new_part()
    try:
        with MSBEntry.setattr_checks_disabled():
            part.entity_id = "not an int"
    finally:
        MSBEntry.SETATTR_CHECKS_DISABLED = False
    assert part.entity_id == "not an int"


def test_setitem_and_get_item_and_set():
    part = _new_part()
    part["entity_id"] = 100
    assert part["entity_id"] == 100
    part.set(entity_id=200, label="hello")
    assert part.entity_id == 200 and part.label == "hello"
    with pytest.raises(KeyError):
        _ = part["nope"]


@pytest.mark.xfail(
    reason=(
        "`MSBEntry.__setitem__` only converts `AttributeError` to `KeyError`, but `__setattr__` "
        "raises `ValueError` for unknown fields, so the documented `KeyError` never happens."
    ),
    strict=False,
)
def test_setitem_unknown_field_raises_key_error():
    part = _new_part()
    with pytest.raises(KeyError):
        part["nope"] = 1


def test_entity_id_helpers():
    part = _new_part()
    part.set_entity_id(1234)
    assert part.get_entity_id() == 1234
    model = MSBFakeModel(name="m0")
    with pytest.raises(TypeError):
        model.get_entity_id()
    with pytest.raises(TypeError):
        model.set_entity_id(1)


def test_entity_enum_setter_sets_name_and_id():
    from enum import IntEnum

    class MyEntities(IntEnum):
        BIG_GUY = 1500

    part = _new_part()
    part.entity_enum = MyEntities.BIG_GUY
    assert part.name == "BIG_GUY"
    assert part.entity_id == 1500
    with pytest.raises(AttributeError):
        _ = part.entity_enum  # getter always raises


def test_set_entity_enum_method():
    from enum import IntEnum

    class MyEntities(IntEnum):
        LITTLE_GUY = 1501

    part = _new_part()
    part.set_entity_enum(MyEntities.LITTLE_GUY)
    assert (part.name, part.entity_id) == ("LITTLE_GUY", 1501)
    with pytest.raises(TypeError):
        part.set_entity_enum(5)


# ---------------------------------------------------------------------------
# copy / equality
# ---------------------------------------------------------------------------


def test_copy_shallow_copies_entry_references_and_deep_copies_values():
    model = MSBFakeModel(name="m0")
    region = MSBFakeRegion(name="r0")
    part = _new_part(model=model, translate=Vector3((1, 2, 3)), counts=[1, 2, 3])
    part.patrol_regions = [region]
    dup = part.copy()

    assert dup is not part
    assert dup.model is model  # shallow reference preserved
    assert dup.patrol_regions[0] is region
    assert dup.patrol_regions is not part.patrol_regions
    assert dup.counts == [1, 2, 3]
    assert dup.counts is not part.counts
    dup.counts[0] = 99
    assert part.counts[0] == 1


def test_eq_compares_references_by_name():
    m1, m2 = MSBFakeModel(name="m0"), MSBFakeModel(name="m0")
    a = _new_part(model=m1)
    b = _new_part(model=m2)
    assert a == b  # same model *name*
    assert a.eq_by_reference_id(a.copy()) is True
    assert a.eq_by_reference_id(b) is False  # different instances


def test_eq_returns_false_for_none_and_other_types():
    a = _new_part()
    assert (a == None) is False  # noqa: E711
    assert (a == MSBFakeRegion(name="r")) is False


@pytest.mark.xfail(
    reason="MSBEntry.__eq__ does `value.name != other.name` without checking `other is None`.",
    strict=False,
)
def test_eq_with_one_none_reference_should_be_false_not_raise():
    a = _new_part(model=MSBFakeModel(name="m0"))
    b = _new_part(model=None)
    assert (a == b) is False


def test_repr_is_readable_and_lists_references():
    part = _new_part(name="p0", model=MSBFakeModel(name="m0"))
    part.patrol_regions = [MSBFakeRegion(name="r0")]
    text = repr(part)
    assert "MSBFakePart(" in text
    assert "MSBFakeModel('m0')" in text
    assert "MSBFakeRegion('r0')" in text
    assert "... 3 None," in text  # trailing `None` elements are summarised


# ---------------------------------------------------------------------------
# Reference tracking (`referring_entry_fields`, `inherit_referrers`)
# ---------------------------------------------------------------------------


def test_setattr_records_referring_entry_fields():
    model = MSBFakeModel(name="m0")
    part = _new_part(name="p0")
    part.model = model
    assert MSBEntryReference(part, "model") in model.referring_entry_fields


def test_setattr_records_array_referring_entry_fields():
    region = MSBFakeRegion(name="r0")
    part = _new_part(name="p0")
    part.patrol_regions = [None, region]
    assert MSBEntryReference(part, "patrol_regions", 1) in region.referring_entry_fields


def test_referring_entry_fields_accumulate_stale_entries():
    """Reassigning a field never removes the old referrer record: the list only ever grows."""
    model = MSBFakeModel(name="m0")
    part = _new_part(name="p0")
    part.model = model
    part.model = model
    part.model = None
    assert len(model.referring_entry_fields) == 2, (
        "Known behaviour: `referring_entry_fields` is append-only and keeps stale entries."
    )


def test_inherit_referrers_repoints_single_and_array_references():
    old = MSBFakeRegion(name="old")
    new = MSBFakeRegion(name="new")
    part = _new_part(name="p0")
    part.patrol_regions = [old, None, None, None]

    new.inherit_referrers(old)
    assert part.patrol_regions[0] is new
    assert old.referring_entry_fields == []
    assert MSBEntryReference(part, "patrol_regions", 0) in new.referring_entry_fields


def test_inherit_referrers_rejects_different_type():
    region = MSBFakeRegion(name="r")
    model = MSBFakeModel(name="m")
    with pytest.raises(TypeError):
        model.inherit_referrers(region)


def test_inherit_referrers_skips_stale_references(caplog):
    old = MSBFakeRegion(name="old")
    other = MSBFakeRegion(name="other")
    new = MSBFakeRegion(name="new")
    part = _new_part(name="p0")
    part.patrol_regions = [old, None, None, None]
    part.patrol_regions[0] = other  # direct list mutation; reference record now stale

    new.inherit_referrers(old)
    assert part.patrol_regions[0] is other  # untouched
    assert new.referring_entry_fields == []


# ---------------------------------------------------------------------------
# Index <-> object resolution
# ---------------------------------------------------------------------------


def _make_entry_lists(models=(), parts=(), regions=()):
    return {
        "MODEL_PARAM_ST": IDList(models),
        "PARTS_PARAM_ST": IDList(parts),
        "POINT_PARAM_ST": IDList(regions),
    }


def test_consume_index_resolves_and_nulls_index_field():
    model = MSBFakeModel(name="m0")
    part = _new_part(name="p0")
    object.__setattr__(part, "_model_index", 0)
    part.indices_to_objects(_make_entry_lists(models=[model], parts=[part], regions=[]))
    assert part.model is model
    assert part._model_index is None
    assert MSBEntryReference(part, "model") in model.referring_entry_fields


def test_consume_index_minus_one_means_none():
    part = _new_part(name="p0")
    part.indices_to_objects(_make_entry_lists(models=[], parts=[part], regions=[]))
    assert part.model is None
    assert part.draw_parent is None


def test_consume_index_out_of_range_becomes_broken_reference():
    part = _new_part(name="p0")
    object.__setattr__(part, "_model_index", 7)
    part.indices_to_objects(_make_entry_lists(models=[MSBFakeModel(name="m0")], parts=[part]))
    assert isinstance(part.model, MSBBrokenEntryReference)
    assert part.model.index == 7
    assert part.model.name == "MODEL_PARAM_ST"


def test_consume_indices_resolves_array():
    r0, r1 = MSBFakeRegion(name="r0"), MSBFakeRegion(name="r1")
    part = _new_part(name="p0")
    object.__setattr__(part, "_patrol_regions_indices", [1, -1, 0, -1])
    part.indices_to_objects(_make_entry_lists(parts=[part], regions=[r0, r1]))
    assert part.patrol_regions == [r1, None, r0, None]
    assert part._patrol_regions_indices is None


def test_consume_index_twice_raises():
    """`_consume_index` sets the index field to `None`, and does not tolerate being re-run.

    Anything that calls `MSB._dereference_msb_entries` (or a subtype's `indices_to_objects`) a
    second time on already-dereferenced entries gets an opaque `TypeError` from `IDList`.
    """
    part = _new_part(name="p0")
    entry_lists = _make_entry_lists(models=[], parts=[part], regions=[])
    part.indices_to_objects(entry_lists)
    with pytest.raises(TypeError):
        part.indices_to_objects(entry_lists)


def test_bitset_field_with_set_default_factory_breaks_ignore_defaults():
    """`BaseMSBPart` declares `draw_groups: BIT_SET_T = field(default_factory=set)`.

    `get_default_values()` returns the *raw* factory output (an empty `set`), but `__setattr__`
    converts assigned values to `BitSet`, and `BitSet128() != set()`. Any game subclass that does
    not override the default factory will therefore always serialise its group fields, even when
    empty. (DS1/ER override it with `BitSet128.all_off`; Bloodborne does not.)
    """

    @dataclass(slots=True, eq=False, repr=False)
    class MSBSetDefaultPart(MSBEntry):
        NAME_ENCODING = "utf-8"
        SUPERTYPE_ENUM = MSBSupertype.PARTS
        SUBTYPE_ENUM = FakePartSubtype.OtherPart
        STRUCTS = {}
        draw_groups: BitSet128 = field(default_factory=set)

    part = MSBSetDefaultPart(name="p")
    assert isinstance(part.draw_groups, BitSet128)
    assert MSBSetDefaultPart.get_default_values()["draw_groups"] == set()
    assert "draw_groups" in part.to_dict(ignore_defaults=True)


def test_try_index_round_trips_single_and_array():
    m0, m1 = MSBFakeModel(name="m0"), MSBFakeModel(name="m1")
    r0, r1 = MSBFakeRegion(name="r0"), MSBFakeRegion(name="r1")
    part = _new_part(name="p0", model=m1)
    part.patrol_regions = [r1, None, r0]

    models = IDList([m0, m1])
    regions = IDList([r0, r1])
    assert part.try_index(models, "model") == 1
    assert part.try_index(regions, "patrol_regions") == [1, -1, 0, -1]

    part.model = None
    assert part.try_index(models, "model") == -1


def test_try_index_raises_for_entry_missing_from_list():
    part = _new_part(name="p0", model=MSBFakeModel(name="m0"))
    with pytest.raises(ValueError):
        part.try_index(IDList(), "model")


def test_entry_ref_metadata_generator():
    meta = EntryRef("PARTS_PARAM_ST")
    assert meta["metadata"]["msb_ref"] == ("PARTS_PARAM_ST", "")
    meta = EntryRef("POINT_PARAM_ST", "patrol_regions", array_size=8)
    assert meta["metadata"]["msb_ref"] == ("POINT_PARAM_ST", "patrol_regions")


# ---------------------------------------------------------------------------
# dict / JSON dict conversion
# ---------------------------------------------------------------------------


def test_to_dict_omits_defaults_by_default():
    part = _new_part(name="p0")
    data = part.to_dict()
    assert data == {"name": "p0"}
    part.entity_id = 5
    assert part.to_dict() == {"name": "p0", "entity_id": 5}
    full = part.to_dict(ignore_defaults=False)
    assert "description" in full and "health" in full and "patrol_regions" in full


def test_from_dict_round_trip():
    part = _new_part(name="p0", entity_id=7, label="x")
    restored = MSBFakePart.from_dict(part.to_dict())
    assert restored.name == "p0"
    assert restored.entity_id == 7
    assert restored.label == "x"


def test_is_valid_ref_dict():
    assert MSBEntry.is_valid_ref_dict({"subtype_list_name": "characters", "subtype_index": 0})
    assert MSBEntry.is_valid_ref_dict({"subtype": ["PARTS_PARAM_ST", "Character"], "entry_name": "c0"})
    assert not MSBEntry.is_valid_ref_dict({"subtype_index": 0})
    assert not MSBEntry.is_valid_ref_dict(
        {"subtype": "x", "subtype_index": 0, "entry_name": "y"}
    )


def test_from_json_dict_defers_reference_dicts():
    data = {
        "name": "p0",
        "entity_id": 3,
        "model": {"subtype": ["MODEL_PARAM_ST", "FakeModel"], "entry_name": "m0"},
        "patrol_regions": [
            None,
            {"subtype": ["POINT_PARAM_ST", "FakeRegion"], "subtype_index": 2},
        ],
    }
    entry, deferred = MSBFakePart.from_json_dict(data)
    assert entry.name == "p0" and entry.entity_id == 3
    assert set(deferred) == {"model", "patrol_regions"}
    assert deferred["patrol_regions"][0] is None


def test_from_json_dict_rejects_bad_reference_dict():
    with pytest.raises(ValueError):
        MSBFakePart.from_json_dict({"name": "p0", "model": {"bogus": 1}})
    with pytest.raises(ValueError):
        MSBFakePart.from_json_dict({"entity_id": 1})  # no 'name'


def test_custom_json_decoders_cover_bitsets_and_vectors():
    decoders = MSBFakePart.get_custom_json_decoders()
    assert decoders["draw_groups"] == [BitSet128.from_repr]
    assert decoders["translate"] == [Vector3]
    # `rotate` uses the raw `EulerDeg` constructor with a legacy `Vector3` fallback.
    assert decoders["rotate"][0] is EulerDeg


@pytest.mark.xfail(
    reason=(
        "`EulerDeg` is not a `BaseVector`, so `to_json_dict` leaves it for `MSB.JSONEncoder`, which "
        "writes `repr()`. The registered decoder is the `EulerDeg` constructor (not `from_repr`), "
        "so the string cannot be read back."
    ),
    strict=False,
)
def test_euler_deg_json_string_round_trips():
    euler = EulerDeg((1.0, 2.0, 3.0))
    decoder = MSBFakePart.get_custom_json_decoders()["rotate"][0]
    assert tuple(decoder(repr(euler))) == (1.0, 2.0, 3.0)


def test_vector_json_round_trips_as_list():
    for vec_type, value in ((Vector2, (1.0, 2.0)), (Vector3, (1.0, 2.0, 3.0)), (Vector4, (1.0, 2, 3, 4))):
        vec = vec_type(value)
        assert tuple(vec_type(list(vec))) == tuple(float(v) for v in value)


# ---------------------------------------------------------------------------
# BitSet
# ---------------------------------------------------------------------------


def test_bitset_uint_round_trip():
    bits = BitSet128({0, 31, 32, 127})
    uints = bits.to_uints()
    assert len(uints) == 4
    assert BitSet128(uints).enabled_bits == {0, 31, 32, 127}


def test_bitset_repr_round_trip():
    bits = BitSet256({3, 200})
    assert BitSet256.from_repr(repr(bits)).enabled_bits == {3, 200}
    assert BitSet128.from_repr("BitSet128()").enabled_bits == set()
    assert BitSet128.from_repr("BitSet128(5)").enabled_bits == {5}
    with pytest.raises(ValueError):
        BitSet128.from_repr("BitSet256(1)")


def test_bitset_set_ops():
    a = BitSet128({1, 2, 3})
    b = BitSet128({3, 4})
    assert (a & b).enabled_bits == {3}
    assert (a | b).enabled_bits == {1, 2, 3, 4}
    assert (a - b).enabled_bits == {1, 2}
    assert 2 in a and 4 not in a
    assert BitSet128.all_off().enabled_bits == set()
    assert len(BitSet128.all_on().enabled_bits) == 128
    assert BitSet128.from_range(2, 4).enabled_bits == {2, 3, 4}
    with pytest.raises(ValueError):
        BitSet128.from_range(4, 2)


def test_bitset_copy_is_independent():
    a = BitSet128({1})
    b = a.copy()
    b.add(2)
    assert a.enabled_bits == {1}
    assert b.enabled_bits == {1, 2}


def test_bitset_rejects_bad_types():
    with pytest.raises(TypeError):
        BitSet128("nope")
    with pytest.raises(TypeError):
        BitSet128({1, 5000})  # bit index too large


# ---------------------------------------------------------------------------
# Region shapes (part of the entry field type system)
# ---------------------------------------------------------------------------


def test_region_shape_json_round_trip():
    for shape in (PointShape(), SphereShape(3.0), BoxShape(1.0, 2.0, 3.0)):
        json_dict = shape.to_json_dict()
        assert json_dict["shape_type"] == shape.SHAPE_TYPE.name
        restored = type(shape).from_json_dict(copy.deepcopy(json_dict))
        assert restored == shape


def test_region_shape_json_rejects_mismatched_type():
    with pytest.raises(ValueError):
        BoxShape.from_json_dict(SphereShape(1.0).to_json_dict())


def test_region_shape_three_dimensions_conversion():
    box = BoxShape(1.0, 2.0, 3.0)
    assert box.get_three_dimensions() == (1.0, 3.0, 2.0)  # (width, height, depth)
    sphere = SphereShape(5.0)
    sphere.set_three_dimensions((7.0, 8.0, 9.0))
    assert sphere.radius == 7.0


def test_region_shape_type_groups():
    assert RegionShapeType.get_volume_types() == {
        RegionShapeType.Sphere, RegionShapeType.Cylinder, RegionShapeType.Box
    }
    assert RegionShapeType.get_2d_types() == {RegionShapeType.Circle, RegionShapeType.Rect}
