"""Tests for Elden Ring `Param`/`ParamDef` handling (`soulstruct.eldenring.params`).

Elden Ring ships no `.paramdefbnd`, so `ParamDefBND` is built from the bundled Paramdex XML files
(`eldenring/params/paramdef/Paramdex/*.xml`). Soulstruct *also* ships generated `ParamRow` dataclasses
in `eldenring/params/paramdef/*.py`, which are what `GameParamBND` actually uses to unpack rows.
Those two sources can drift apart, so most tests here cross-check them.

Everything in this module is a pure unit test (no game install required); the bundled Paramdex XML
and generated modules are committed to the repo.
"""
from __future__ import annotations

from collections import Counter

import pytest

from soulstruct.base.params.param import Param, TypedParam
from soulstruct.base.params.param_row import ParamRow
from soulstruct.eldenring.params import GameParamBND, ParamDefBND
from soulstruct.eldenring.params import paramdef as paramdef_module


@pytest.fixture(scope="module")
def paramdefbnd() -> ParamDefBND:
    """Bundled Paramdex XML paramdefs (cached class-side by `from_bundled`)."""
    return ParamDefBND.from_bundled("eldenring")


@pytest.fixture(scope="module")
def generated_row_types() -> dict[str, type[ParamRow]]:
    """Generated `ParamRow` subclasses exported by `eldenring.params.paramdef`."""
    return {
        name: obj
        for name in paramdef_module.__all__
        if isinstance(obj := getattr(paramdef_module, name), type) and issubclass(obj, ParamRow)
    }


# ---------------------------------------------------------------------------
# Paramdex XML loading
# ---------------------------------------------------------------------------


def test_paramdefbnd_loads_from_bundled_paramdex(paramdefbnd):
    assert len(paramdefbnd.paramdefs) > 150
    assert "NPC_PARAM_ST" in paramdefbnd.paramdefs
    npc = paramdefbnd.paramdefs["NPC_PARAM_ST"]
    assert npc.param_type == "NPC_PARAM_ST"
    assert npc.fields
    assert npc.get_total_size() > 0


def test_paramdefbnd_from_bundled_is_cached(paramdefbnd):
    assert ParamDefBND.from_bundled("eldenring") is paramdefbnd


def test_paramdef_param_types_are_unique(paramdefbnd):
    counts = Counter(pd.param_type for pd in paramdefbnd.paramdefs.values())
    assert not [k for k, v in counts.items() if v > 1]


def test_paramdef_fields_are_ordered_and_named(paramdefbnd):
    for param_type, pdef in paramdefbnd.paramdefs.items():
        assert pdef.fields, f"{param_type} has no fields."
        for name, field in pdef.fields.items():
            assert field.name == name, f"{param_type}: field key '{name}' != field.name '{field.name}'"


# ---------------------------------------------------------------------------
# Generated `ParamRow` modules vs. Paramdex XML
# ---------------------------------------------------------------------------


def test_generated_row_types_match_xml_param_types(paramdefbnd, generated_row_types):
    py_types = set(generated_row_types)
    xml_types = set(paramdefbnd.paramdefs)
    assert py_types - xml_types == set(), f"Generated modules with no Paramdex XML: {sorted(py_types - xml_types)}"
    assert xml_types - py_types == set(), f"Paramdex XML with no generated module: {sorted(xml_types - py_types)}"


def test_generated_row_class_names_match_param_type(generated_row_types):
    for param_type, cls in generated_row_types.items():
        assert cls.__name__ == param_type


def test_generated_row_types_are_instantiable(generated_row_types):
    """Every generated `ParamRow` must build with all-default values and pack to its own size."""
    for param_type, cls in generated_row_types.items():
        row = cls()
        packed = bytes(row.to_writer())
        assert len(packed) == cls.get_size(), f"{param_type}: packed {len(packed)} bytes, expected {cls.get_size()}"


def test_generated_row_types_roundtrip_default_bytes(generated_row_types):
    """unpack(pack(default row)) must be stable for every ER param row type."""
    for param_type, cls in generated_row_types.items():
        row = cls()
        packed = bytes(row.to_writer())
        reloaded = cls.from_bytes(packed)
        assert bytes(reloaded.to_writer()) == packed, f"{param_type} did not round-trip."


@pytest.mark.xfail(
    reason="BUG: generated `NETWORK_PARAM_ST.py` is out of sync with Paramdex XML "
           "('reloadSignIntervalTime_1' vs 'reloadSignIntervalTime1'; 155 fields vs 156; 628 vs 632 bytes).",
    strict=False,
)
def test_generated_field_names_match_xml(paramdefbnd, generated_row_types):
    mismatches = {}
    for param_type, cls in generated_row_types.items():
        xml_names = [f.name for f in paramdefbnd.paramdefs[param_type].fields.values()]
        py_names = [m.internal_name for m in cls.get_all_field_metadata().values()]
        if xml_names != py_names:
            mismatches[param_type] = (len(xml_names), len(py_names))
    assert not mismatches, f"Generated paramdef modules disagree with Paramdex XML: {mismatches}"


@pytest.mark.xfail(
    reason="Row byte sizes disagree for DECAL_PARAM_ST (247 vs 248), NETWORK_PARAM_ST (632 vs 628) and "
           "PARTS_DRAW_PARAM_ST (141 vs 144). At least NETWORK_PARAM_ST is a genuine field-list mismatch; "
           "the other two may be `ParamDef.get_total_size()` bit-field accounting.",
    strict=False,
)
def test_generated_row_sizes_match_xml(paramdefbnd, generated_row_types):
    mismatches = {
        param_type: (paramdefbnd.paramdefs[param_type].get_total_size(), cls.get_size())
        for param_type, cls in generated_row_types.items()
        if paramdefbnd.paramdefs[param_type].get_total_size() != cls.get_size()
    }
    assert not mismatches, f"XML vs generated row size mismatch: {mismatches}"


@pytest.mark.xfail(
    reason="BUG: `ParamDef.from_paramdex_xml` uses `bool(child.text)`, so '<BigEndian>False</BigEndian>' "
           "parses as True for every Elden Ring paramdef.",
    strict=False,
)
def test_paramdefs_are_little_endian(paramdefbnd):
    big_endian = [pt for pt, pd in paramdefbnd.paramdefs.items() if pd.big_endian]
    assert not big_endian, f"{len(big_endian)} Elden Ring paramdefs claim to be big-endian."


# ---------------------------------------------------------------------------
# `ParamRow` API
# ---------------------------------------------------------------------------


def test_param_row_getitem_by_nickname_and_internal_name():
    row = paramdef_module.ACTIONBUTTON_PARAM_ST()
    assert row["Radius"] == row["radius"]  # nickname and internal name
    row["Radius"] = 5.0
    assert row["radius"] == 5.0
    assert row.Radius == 5.0
    with pytest.raises(KeyError):
        _ = row["NoSuchField"]


def test_param_row_name_and_raw_name():
    row = paramdef_module.ACTIONBUTTON_PARAM_ST()
    row["Name"] = "TestRow"
    assert row.Name == "TestRow"
    assert row["name"] == "TestRow"
    assert row.get_packed_name("shift_jis_2004") == b"TestRow\0"


def test_param_row_to_dict_and_from_dict_roundtrip():
    cls = paramdef_module.ACTIONBUTTON_PARAM_ST
    row = cls(Name="Radius Test")
    row.Radius = 12.5
    data = row.to_dict(ignore_pads=True, ignore_defaults=True)
    assert data["Radius"] == 12.5
    reloaded = cls.from_dict(dict(data))
    assert reloaded.Radius == 12.5
    assert reloaded.Name == "Radius Test"


def test_param_row_internal_names_are_unique():
    for name in paramdef_module.__all__:
        obj = getattr(paramdef_module, name)
        if not (isinstance(obj, type) and issubclass(obj, ParamRow)):
            continue
        internal = obj.get_internal_names()
        assert len(internal) == len(set(internal)), f"{name} has repeated internal field names."


@pytest.mark.xfail(
    reason="BUG: `ParamBitPad` does not set `is_pad=True` (unlike `ParamPad`), so bit-padding fields are "
           "not excluded by `to_dict(ignore_pads=True)`.",
    strict=False,
)
def test_bit_pads_are_ignored_by_to_dict():
    row = paramdef_module.ACTIONBUTTON_PARAM_ST()
    data = row.to_dict(ignore_pads=True, ignore_defaults=False)
    assert not [k for k in data if "BitPad" in k]


def test_param_row_base_repr():
    row = paramdef_module.ACTIONBUTTON_PARAM_ST()
    assert isinstance(ParamRow.__repr__(row), str)


# ---------------------------------------------------------------------------
# `GameParamBND` class configuration
# ---------------------------------------------------------------------------


def test_gameparambnd_class_defaults():
    from soulstruct.containers import BinderVersion
    from soulstruct.dcx import DCXType

    assert GameParamBND.PARAMDEF_MODULE is paramdef_module
    assert GameParamBND.DEFAULT_ENTRY_ROOT == "N:\\GR\\data\\Param\\param\\GameParam"
    # Class defaults (overridden by whatever the loaded file actually says).
    defaults = GameParamBND()
    assert defaults.dcx_type == DCXType.DCX_ZSTD
    assert defaults.version == BinderVersion.V4
    assert defaults.v4_info.hash_table_type == 4


def test_gameparambnd_param_properties_reference_known_paramdefs():
    """Every `param_property` stem should be resolvable and its `Param` typed by a generated `ParamRow`."""
    props = {k for k, v in vars(GameParamBND).items() if isinstance(v, property)}
    assert len(props) > 180
    # Property names must be unique (they are class attributes, so this is implicit) and non-empty.
    assert all(props)


def test_typed_param_factory_uses_generated_row_type():
    typed = TypedParam(paramdef_module.NPC_PARAM_ST)
    assert issubclass(typed, Param)
    assert typed.ROW_TYPE is paramdef_module.NPC_PARAM_ST


@pytest.mark.xfail(
    reason="BUG: Elden Ring `GameParamBND.PARAM_NICKNAMES` is empty, so `write_json_directory()` / "
           "`from_json_directory()` raise `KeyError` on the very first param.",
    strict=False,
)
def test_param_nicknames_are_defined():
    assert GameParamBND.PARAM_NICKNAMES, "ER `GameParamBND` has no `PARAM_NICKNAMES`; JSON directory I/O is broken."


@pytest.mark.xfail(
    reason="BUG: `GameParamBND.unpack_all_param_rows` iterates `self.params.values()` while unpacking two "
           "names, raising `TypeError`/`ValueError` as soon as any `ParamDict` is present.",
    strict=False,
)
def test_unpack_all_param_rows_signature():
    bnd = GameParamBND()
    bnd.params = {"Dummy": object()}
    with pytest.raises((TypeError, ValueError)):
        bnd.unpack_all_param_rows(ParamDefBND.from_bundled("eldenring"))
    pytest.fail("`unpack_all_param_rows` unpacking bug is still present.")
