"""Tests for `soulstruct.base.params.paramdef`: `ParamDef`, `ParamDefField`, `ParamDefBND`,
`field_types`, and Paramdex XML loading.
"""
from __future__ import annotations

import logging
from pathlib import Path

import pytest

from soulstruct.base.params.exceptions import ParamError
from soulstruct.base.params.paramdef import field_types as ft
from soulstruct.base.params.paramdef.core import ParamDef
from soulstruct.base.params.paramdef.paramdef_field import ParamDefField, ParamDefEditFlags
from soulstruct.base.params.paramdef.exceptions import ParamDefError


# ---------------------------------------------------------------------------
# `field_types` primitive contract
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "cls, size, fmt, py_type, minimum, maximum",
    [
        (ft.u8, 1, "<B", int, 0, 255),
        (ft.u16, 2, "<H", int, 0, 65535),
        (ft.u32, 4, "<I", int, 0, 2 ** 32 - 1),
        (ft.s8, 1, "<b", int, -128, 127),
        (ft.s16, 2, "<h", int, -32768, 32767),
        (ft.s32, 4, "<i", int, -(2 ** 31), 2 ** 31 - 1),
        (ft.dummy8, 1, "<B", int, 0, 255),
    ],
)
def test_integer_field_types(cls, size, fmt, py_type, minimum, maximum):
    assert cls.size() == size
    assert cls.format() == fmt
    assert cls.python_type() is py_type
    assert cls.minimum() == minimum
    assert cls.maximum() == maximum
    assert cls.default() == 0
    assert cls.bit_size() == size * 8


def test_float_field_types():
    assert ft.f32.size() == 4 and ft.f32.format() == "<f" and ft.f32.python_type() is float
    assert ft.f64.size() == 8 and ft.f64.format() == "<d"
    assert ft.f32.minimum() == -float("inf") and ft.f32.maximum() == float("inf")
    assert ft.f32.default() == 0.0
    assert ft.angle32.size() == 4 and ft.angle32.format() == "<f"


def test_string_field_types():
    assert ft.fixstr.size() == 1
    assert ft.fixstrW.size() == 2
    assert ft.fixstr.python_type() is str
    assert ft.fixstr.default() == ""
    assert ft.fixstr.minimum() is None and ft.fixstr.maximum() is None
    assert ft.fixstr.write("ab", 4) == b"ab\0\0"
    assert ft.fixstrW.write("ab", 8) == "ab".encode("utf-16-le") + b"\0\0\0\0"


def test_dummy8_is_a_u8_subclass():
    assert issubclass(ft.dummy8, ft.u8)
    assert issubclass(ft.dummy8, ft.unsigned)


# ---------------------------------------------------------------------------
# `ParamDefField` construction (via Paramdex XML nodes, which need no binary data)
# ---------------------------------------------------------------------------


def _xml_node(xml: str):
    from xml.etree import ElementTree

    return ElementTree.fromstring(xml)


def test_paramdef_field_from_paramdex_basic():
    node = _xml_node('<Field Def="s32 spEffectId0 = -1"><DisplayName>SpEffect 0</DisplayName></Field>')
    f = ParamDefField.from_paramdex_xml(0, node, "TEST_PARAM_ST")
    assert f.name == "spEffectId0"
    assert f.display_type is ft.s32
    assert f.size == 4
    assert f.length == 1
    assert f.bit_count == -1
    assert f.default == -1
    assert f.display_name == "SpEffect 0"
    assert f.py_type is int
    assert f.py_fmt == "<i"
    assert f.py_type_min == -(2 ** 31)


def test_paramdef_field_from_paramdex_array():
    node = _xml_node('<Field Def="dummy8 pad1[4]" />')
    f = ParamDefField.from_paramdex_xml(1, node, "TEST_PARAM_ST")
    assert f.size == 4
    assert f.length == 4
    assert f.display_type is ft.dummy8


def test_paramdef_field_from_paramdex_bit_field():
    node = _xml_node('<Field Def="u8 isFoo:1" />')
    f = ParamDefField.from_paramdex_xml(2, node, "TEST_PARAM_ST")
    assert f.bit_count == 1
    assert f.size == 1


def test_paramdef_field_from_paramdex_default_display_name():
    node = _xml_node('<Field Def="s32 someField" />')
    f = ParamDefField.from_paramdex_xml(0, node, "T")
    assert f.display_name == "_Somefield"
    assert f.default == 0


def test_paramdef_field_from_paramdex_edit_flags():
    for text, expected in [("None", 0), ("Wrap", 1), ("Lock", 4), ("Wrap, Lock", 5)]:
        node = _xml_node(f'<Field Def="s32 f"><EditFlags>{text}</EditFlags></Field>')
        f = ParamDefField.from_paramdex_xml(0, node, "T")
        assert int(f.edit_flags) == expected
    node = _xml_node('<Field Def="s32 f"><EditFlags>Nonsense</EditFlags></Field>')
    with pytest.raises(ValueError):
        ParamDefField.from_paramdex_xml(0, node, "T")


def test_paramdef_edit_flags_properties():
    assert ParamDefEditFlags(0b101).is_wrap
    assert ParamDefEditFlags(0b101).is_lock
    assert not ParamDefEditFlags(0b010).is_wrap


def test_paramdef_field_versions():
    node = _xml_node('<Field Def="s32 f" RemovedVersion="200" FirstVersion="100" />')
    f = ParamDefField.from_paramdex_xml(0, node, "T")
    assert f.removed_version == 200
    assert f.first_version == 100


def test_paramdef_field_unknown_tag_raises():
    node = _xml_node('<Field Def="s32 f"><Bogus>x</Bogus></Field>')
    with pytest.raises(ValueError):
        ParamDefField.from_paramdex_xml(0, node, "T")


def test_paramdef_field_array_length_mismatch_raises(capsys):
    """`__post_init__` cross-checks the `[n]` in the name against `size // type_size`."""
    node = _xml_node('<Field Def="dummy8 pad1[4]" />')
    f = ParamDefField.from_paramdex_xml(0, node, "T")
    kwargs = {k: getattr(f, k) for k in f.__slots__ if not k.startswith("py_") and k != "length"}
    kwargs["size"] = 3  # inconsistent with [4]
    with pytest.raises(ParamDefError):
        ParamDefField(**kwargs)
    capsys.readouterr()  # swallow the stray `print()` in `__post_init__` (finding M7)


def test_paramdef_field_check_range():
    node = _xml_node('<Field Def="s8 f" />')
    f = ParamDefField.from_paramdex_xml(0, node, "T")
    f.check_range(127)
    f.check_range(-128)
    with pytest.raises(ValueError):
        f.check_range(128)
    with pytest.raises(ValueError):
        f.check_range(-129)


def test_paramdef_field_check_range_allows_nan():
    node = _xml_node('<Field Def="f32 f" />')
    f = ParamDefField.from_paramdex_xml(0, node, "T")
    f.check_range(float("nan"))  # must not raise


def test_paramdef_field_check_python_type_dummy8():
    node = _xml_node('<Field Def="dummy8 pad[2]" />')
    f = ParamDefField.from_paramdex_xml(0, node, "T")
    f.check_python_type(b"\0\0")  # OK
    with pytest.raises(ParamError):
        f.check_python_type(0)


@pytest.mark.xfail(
    reason="H3: `check_python_type()` uses `isinstance(value, self.display_type)`, but `display_type` "
           "is a memberless IntEnum/plain class, so every non-dummy8 value is rejected.",
    strict=False,
)
@pytest.mark.parametrize("def_str, value", [("s32 f", 0), ("u8 f", 1), ("f32 f", 1.0)])
def test_paramdef_field_check_python_type_accepts_valid_values(def_str, value):
    node = _xml_node(f'<Field Def="{def_str}" />')
    f = ParamDefField.from_paramdex_xml(0, node, "T")
    f.check_python_type(value)


# ---------------------------------------------------------------------------
# `ParamDef` from Paramdex XML
# ---------------------------------------------------------------------------


PARAMDEX_XML = """<?xml version="1.0" encoding="utf-8"?>
<PARAMDEF>
  <ParamType>TEST_PARAM_ST</ParamType>
  <DataVersion>3</DataVersion>
  <BigEndian>False</BigEndian>
  <Unicode>True</Unicode>
  <FormatVersion>203</FormatVersion>
  <Fields>
    <Field Def="s32 alpha = 5"><DisplayName>Alpha</DisplayName></Field>
    <Field Def="f32 beta" />
    <Field Def="u8 gamma:1" />
    <Field Def="dummy8 pad0:7" />
    <Field Def="dummy8 pad1[3]" />
    <Field Def="s16 removedField" RemovedVersion="150" />
    <Field Def="s16 futureField" FirstVersion="300" />
  </Fields>
</PARAMDEF>
"""


@pytest.fixture
def paramdex_xml_path(tmp_path) -> Path:
    path = tmp_path / "TEST_PARAM_ST.xml"
    path.write_text(PARAMDEX_XML, encoding="utf-8")
    return path


def test_paramdef_from_paramdex_xml_latest(paramdex_xml_path):
    pd = ParamDef.from_paramdex_xml(paramdex_xml_path)
    assert pd.param_type == "TEST_PARAM_ST"
    assert pd.data_version == 3
    assert pd.format_version == 203
    # `removedField` is dropped when `version=0` (latest), `futureField` is kept.
    assert list(pd.fields) == ["alpha", "beta", "gamma:1", "pad0:7", "pad1[3]", "futureField"]
    assert pd["alpha"].default == 5
    assert pd.path == paramdex_xml_path


def test_paramdef_from_paramdex_xml_versioned(paramdex_xml_path):
    pd = ParamDef.from_paramdex_xml(paramdex_xml_path, version=100)
    names = list(pd.fields)
    assert "removedField" in names  # removed at 150 > 100
    assert "futureField" not in names  # added at 300 > 100


def test_paramdef_from_paramdex_xml_unknown_tag(tmp_path):
    path = tmp_path / "bad.xml"
    path.write_text(
        "<PARAMDEF><ParamType>T</ParamType><Bogus>1</Bogus><Fields /></PARAMDEF>", encoding="utf-8"
    )
    with pytest.raises(ValueError):
        ParamDef.from_paramdex_xml(path)


def test_paramdef_from_paramdex_xml_missing_paramtype(tmp_path):
    path = tmp_path / "bad2.xml"
    path.write_text("<PARAMDEF><Fields /></PARAMDEF>", encoding="utf-8")
    with pytest.raises(ValueError):
        ParamDef.from_paramdex_xml(path)


@pytest.mark.xfail(
    reason="M5: `bool(child.text)` is used for `<BigEndian>`/`<Unicode>`, and `bool('False') is True`.",
    strict=False,
)
def test_paramdef_paramdex_booleans(paramdex_xml_path):
    pd = ParamDef.from_paramdex_xml(paramdex_xml_path)
    assert pd.big_endian is False
    assert pd.unicode is True


def test_paramdef_get_total_size(paramdex_xml_path):
    pd = ParamDef.from_paramdex_xml(paramdex_xml_path)
    # s32(4) + f32(4) + [gamma:1 + pad0:7 -> 1 byte] + pad1[3](3) + futureField s16(2)
    assert pd.get_total_size() == 4 + 4 + 1 + 3 + 2


def test_paramdef_from_field_sequence(paramdex_xml_path):
    pd = ParamDef.from_paramdex_xml(paramdex_xml_path)
    fields = list(pd.fields.values())
    pd2 = ParamDef.from_field_sequence(fields, "OTHER_PARAM_ST")
    assert pd2.param_type == "OTHER_PARAM_ST"
    assert list(pd2.fields) == list(pd.fields)
    with pytest.raises(ValueError):
        ParamDef.from_field_sequence(fields + fields[:1], "OTHER_PARAM_ST")


def test_paramdef_is_write_only_read_only(paramdex_xml_path):
    pd = ParamDef.from_paramdex_xml(paramdex_xml_path)
    with pytest.raises(TypeError):
        pd.to_writer()


def test_paramdef_repr_and_verbose(paramdex_xml_path):
    pd = ParamDef.from_paramdex_xml(paramdex_xml_path)
    assert "TEST_PARAM_ST" in repr(pd)
    assert "alpha" in pd.verbose()


# ---------------------------------------------------------------------------
# Bundled binary `ParamDefBND` (DS1 PTDE, format version 104)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def ptde_paramdefbnd():
    from soulstruct.darksouls1ptde.params.paramdef import ParamDefBND

    logging.disable(logging.WARNING)
    try:
        return ParamDefBND.from_bundled("darksouls1ptde")
    except FileNotFoundError as ex:
        pytest.skip(f"Bundled PTDE PARAMDEFBND not available: {ex}")
    finally:
        logging.disable(logging.NOTSET)


def test_bundled_paramdefbnd_loads(ptde_paramdefbnd):
    assert len(ptde_paramdefbnd.paramdefs) > 30
    assert "NPC_PARAM_ST" in ptde_paramdefbnd.paramdefs


def test_bundled_paramdefbnd_is_cached(ptde_paramdefbnd):
    from soulstruct.darksouls1ptde.params.paramdef import ParamDefBND

    assert ParamDefBND.from_bundled("darksouls1ptde") is ptde_paramdefbnd


def test_bundled_paramdefbnd_get_paramdef(ptde_paramdefbnd):
    pd = ptde_paramdefbnd.get_paramdef("NPC_PARAM_ST")
    assert pd.param_type == "NPC_PARAM_ST"
    assert pd.format_version == 104
    assert pd.data_version == 3
    assert len(pd.fields) > 100
    with pytest.raises(KeyError):
        ptde_paramdefbnd.get_paramdef("NOT_A_PARAM")


def test_base_paramdefbnd_has_no_paramdef_class():
    """H5: the base `ParamDefBND` has `PARAMDEF_CLASS = None`, so `from_bundled` on it always fails."""
    from soulstruct.base.params.paramdef.paramdefbnd import ParamDefBND as BaseParamDefBND

    assert BaseParamDefBND.PARAMDEF_CLASS is None


def test_paramdef_total_size_matches_generated_row_struct(ptde_paramdefbnd):
    """The `ParamDef` byte size must match the generated `ParamRow` subclass struct size."""
    from soulstruct.darksouls1ptde.params import paramdef as paramdef_module

    checked = 0
    for param_type, pd in ptde_paramdefbnd.paramdefs.items():
        row_cls = getattr(paramdef_module, param_type, None)
        if row_cls is None:
            continue
        packed_size = len(bytes(row_cls().to_writer()))
        assert pd.get_total_size() == packed_size, param_type
        checked += 1
    assert checked > 20


def test_paramdef_internal_names_match_generated_row_class(ptde_paramdefbnd):
    from soulstruct.darksouls1ptde.params.paramdef import NPC_PARAM_ST

    pd = ptde_paramdefbnd.get_paramdef("NPC_PARAM_ST")
    assert list(pd.fields) == list(NPC_PARAM_ST.get_internal_names())


@pytest.mark.xfail(
    reason="M4: `get_py_default()` short-circuits on falsy defaults, so integer fields with a zero "
           "default keep the float `0.0` from the ParamDef.",
    strict=False,
)
def test_paramdef_integer_default_is_int(ptde_paramdefbnd):
    pd = ptde_paramdefbnd.get_paramdef("NPC_PARAM_ST")
    field = pd["behaviorVariationId"]
    assert field.display_type is ft.s32
    assert isinstance(field.py_default, int) and not isinstance(field.py_default, bool)


def test_paramdef_nonzero_integer_default_is_int(ptde_paramdefbnd):
    """Non-zero integer defaults *are* correctly coerced (only the falsy path is broken)."""
    pd = ptde_paramdefbnd.get_paramdef("NPC_PARAM_ST")
    int_fields = [
        f for f in pd.fields.values()
        if f.display_type in (ft.s32, ft.s16, ft.s8, ft.u32, ft.u16, ft.u8) and f.default
    ]
    assert int_fields, "expected at least one non-zero integer default in NPC_PARAM_ST"
    for f in int_fields:
        assert isinstance(f.py_default, (int, bool)), f.name


@pytest.fixture(scope="module")
def ptde_parambnd_path(request) -> Path:
    path = Path(request.config.rootpath) / "tests" / "darksouls1ptde" / "resources" / "GameParam.parambnd"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


@pytest.fixture(scope="module")
def npc_param_entry_data(ptde_parambnd_path) -> bytes:
    from soulstruct.containers import Binder

    binder = Binder.from_path(ptde_parambnd_path)
    return bytes(next(e for e in binder.entries if e.stem == "NpcParam"))
