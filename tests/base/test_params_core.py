"""Tests for the shared `Param` / `ParamRow` machinery in `soulstruct.base.params`.

Uses the committed PTDE `GameParam.parambnd` as a realistic vehicle; per-game param behaviour is
tested elsewhere.
"""
from __future__ import annotations

import logging
import time

import pytest

from soulstruct.base.params.param import Param, TypedParam
from soulstruct.base.params.param_row import (
    ParamRow,
    ParamField,
    ParamPad,
    ParamBitPad,
    ParamFieldMetadata,
    DynamicParamField,
    pad_field,
    bit_pad_field,
)
from soulstruct.base.params.flags import ParamFlags1, ParamFlags2
from soulstruct.base.params.utilities import (
    ParamFieldComparisonType,
    ParamFieldSearchCondition,
    find_param_rows,
)
from soulstruct.utilities.binary import int32, float32, uint8


def assert_bytes_equal(actual: bytes, expected: bytes, context: str = "") -> None:
    """Local copy of the `conftest` helper (`--import-mode=importlib` hides `conftest` from imports)."""
    if actual == expected:
        return
    prefix = f"{context}: " if context else ""
    limit = min(len(actual), len(expected))
    for i in range(limit):
        if actual[i] != expected[i]:
            raise AssertionError(
                f"{prefix}byte mismatch at offset 0x{i:X} ({actual[i]:#04x} != {expected[i]:#04x}); "
                f"lengths {len(actual)} vs {len(expected)}."
            )
    raise AssertionError(f"{prefix}length differs ({len(actual)} != {len(expected)}), common prefix matches.")


# ---------------------------------------------------------------------------
# Pure-unit fixtures: a tiny hand-made `ParamRow` subclass.
# ---------------------------------------------------------------------------


class TOY_PARAM_ST(ParamRow):
    """Minimal generated-style `ParamRow` subclass (12 bytes)."""

    Alpha: int = ParamField(int32, "alpha", default=0, tooltip="Alpha field.")
    Beta: float = ParamField(float32, "beta", default=1.5, tooltip="Beta field.")
    FlagA: bool = ParamField(uint8, "flagA:1", bit_count=1, default=False, tooltip="Bit flag A.")
    FlagB: bool = ParamField(uint8, "flagB:1", bit_count=1, default=True, tooltip="Bit flag B.")
    _BitPad0: int = ParamBitPad(uint8, "pad0:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "pad1[3]")


@pytest.fixture(scope="module")
def toy_param_cls():
    return TypedParam(TOY_PARAM_ST)


@pytest.fixture(scope="module")
def ptde_gameparambnd(resources_module_path):
    """Loaded PTDE `GameParamBND` (module-scoped: loading takes ~2s)."""
    from soulstruct.darksouls1ptde.params import GameParamBND

    path = resources_module_path
    logging.disable(logging.WARNING)
    try:
        return GameParamBND.from_path(path)
    finally:
        logging.disable(logging.NOTSET)


@pytest.fixture(scope="module")
def resources_module_path(request):
    """Absolute path to the committed PTDE `GameParam.parambnd` (session resource, module-scoped)."""
    from pathlib import Path

    path = Path(request.config.rootpath) / "tests" / "darksouls1ptde" / "resources" / "GameParam.parambnd"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


# ---------------------------------------------------------------------------
# Pure unit tests: ParamField / ParamRow structure
# ---------------------------------------------------------------------------


def test_pad_field_helpers():
    assert pad_field(4) == "<Pad:4>"
    assert bit_pad_field(6) == "<BitPad:6>"


def test_param_row_binary_field_names_exclude_name_fields():
    names = TOY_PARAM_ST.get_binary_field_names()
    assert "Name" not in names
    assert "RawName" not in names
    assert names == ("Alpha", "Beta", "FlagA", "FlagB", "_BitPad0", "_Pad0")


def test_param_row_defaults():
    row = TOY_PARAM_ST()
    assert row.Alpha == 0
    assert row.Beta == pytest.approx(1.5)
    assert row.FlagA is False
    assert row.FlagB is True
    assert row._Pad0 == b"\0\0\0"
    assert row.Name == ""
    assert row.RawName == b""


def test_param_row_internal_names_and_metadata():
    assert TOY_PARAM_ST.get_internal_names() == ("alpha", "beta", "flagA:1", "flagB:1", "pad0:6", "pad1[3]")
    meta = TOY_PARAM_ST.get_field_metadata("Alpha")
    assert isinstance(meta, ParamFieldMetadata)
    assert meta.internal_name == "alpha"
    assert meta.tooltip == "Alpha field."
    assert meta.is_pad is False
    # `game_type` is filled in from the type hint on first `get_all_field_metadata()` call.
    assert meta.game_type is int
    assert TOY_PARAM_ST.get_field_metadata("_Pad0").is_pad is True


def test_param_row_metadata_cached():
    a = TOY_PARAM_ST.get_all_field_metadata()
    b = TOY_PARAM_ST.get_all_field_metadata()
    assert a is b
    with pytest.raises(TypeError):
        a["Alpha"] = None  # MappingProxyType is read-only


def test_param_field_metadata_get_display_type():
    meta = ParamFieldMetadata(internal_name="x", game_type=int)
    assert meta.get_display_type() is int

    class ATTACK_BOOL(int):
        pass

    meta2 = ParamFieldMetadata(internal_name="y", param_enum=ATTACK_BOOL)
    assert meta2.get_display_type() is bool  # "BOOL" in name -> redirected

    class SOME_ENUM(int):
        pass

    meta3 = ParamFieldMetadata(internal_name="z", param_enum=SOME_ENUM)
    assert meta3.get_display_type() is SOME_ENUM

    with pytest.raises(ValueError):
        ParamFieldMetadata(internal_name="w").get_display_type()


def test_dynamic_param_field_bool_redirect():
    class SOME_BOOL(int):
        pass

    class Dyn(DynamicParamField):
        def __call__(self, data):
            return SOME_BOOL, "_suffix", "tip"

    assert Dyn().as_display_type(None) == (bool, "_suffix", "tip")


def test_param_row_getitem_by_nickname_and_internal_name():
    row = TOY_PARAM_ST(Alpha=7, Beta=2.5)
    assert row["Alpha"] == 7
    assert row["alpha"] == 7
    assert row["Beta"] == pytest.approx(2.5)
    assert row["beta"] == pytest.approx(2.5)
    with pytest.raises(KeyError):
        _ = row["NotAField"]


def test_param_row_setitem_and_update():
    row = TOY_PARAM_ST()
    row["Alpha"] = 3
    row["beta"] = 9.0
    assert row.Alpha == 3
    assert row.Beta == pytest.approx(9.0)
    row.update(Alpha=11, FlagA=True)
    assert row.Alpha == 11 and row.FlagA is True
    with pytest.raises(KeyError):
        row["nope"] = 1


def test_param_row_name_and_rawname_item_access():
    row = TOY_PARAM_ST()
    row["Name"] = "hello"
    assert row["name"] == "hello"
    row["RawName"] = b"raw"
    assert row["rawname"] == b"raw"


def test_param_row_try_name():
    row = TOY_PARAM_ST(RawName=b"\x80\x81")
    assert row.try_name == repr(b"\x80\x81")
    row.Name = "Named"
    assert row.try_name == "Named"


def test_param_row_iter_yields_pairs():
    row = TOY_PARAM_ST(Alpha=5)
    pairs = dict(iter(row))
    assert pairs["Alpha"] == 5
    assert set(pairs) == set(TOY_PARAM_ST.get_binary_field_names())


def test_param_row_to_dict_options():
    row = TOY_PARAM_ST(Alpha=5, Name="n")
    d = row.to_dict()  # ignore_pads=True, ignore_defaults=True
    assert "_Pad0" not in d and "_BitPad0" not in d
    assert "Beta" not in d  # default value dropped
    assert d["Alpha"] == 5
    assert d["Name"] == "n"
    assert d["RawName"] == repr("n".encode("shift_jis_2004"))

    d_all = row.to_dict(ignore_pads=False, ignore_defaults=False)
    assert "_Pad0" in d_all and "Beta" in d_all

    d_int = row.to_dict(use_internal_names=True)
    assert "alpha" in d_int

    d_bin = row.to_dict(binary_fields_only=True)
    assert "Name" not in d_bin and "RawName" not in d_bin


def test_param_row_from_dict_roundtrip():
    row = TOY_PARAM_ST(Alpha=5, Beta=3.0, Name="n")
    d = row.to_dict(ignore_pads=False, ignore_defaults=False)
    row2 = TOY_PARAM_ST.from_dict(dict(d))
    assert row2.Alpha == 5
    assert row2.Beta == pytest.approx(3.0)
    assert row2.Name == "n"
    assert row2.RawName == b"n"


def test_param_row_from_dict_falls_back_to_rawname():
    d = {"Name": "", "RawName": repr(b"\x80raw"), "Alpha": 1}
    row = TOY_PARAM_ST.from_dict(d)
    assert row.RawName == b"\x80raw"
    assert row.Name == ""


def test_param_row_get_packed_name():
    row = TOY_PARAM_ST(Name="abc")
    assert row.get_packed_name("shift_jis_2004") == b"abc\0"
    assert TOY_PARAM_ST().get_packed_name("shift_jis_2004") == b""
    # `Name` takes precedence over `RawName`.
    row2 = TOY_PARAM_ST(Name="abc", RawName=b"zzz")
    assert row2.get_packed_name("shift_jis_2004") == b"abc\0"


def test_param_row_get_packed_name_utf16():
    row = TOY_PARAM_ST(Name="abc")
    assert row.get_packed_name("utf-16-le") == "abc".encode("utf-16-le") + b"\0\0"


def test_param_row_binary_roundtrip_with_bit_fields():
    row = TOY_PARAM_ST(Alpha=-5, Beta=0.25, FlagA=True, FlagB=False)
    data = bytes(row.to_writer())
    assert len(data) == 12
    row2 = TOY_PARAM_ST.from_bytes(data)
    assert row2.Alpha == -5
    assert row2.Beta == pytest.approx(0.25)
    # NOTE: `bit_count=1` fields come back as `int` 1/0, not `bool` (see finding L21).
    assert row2.FlagA == 1
    assert row2.FlagB == 0
    assert bytes(row2.to_writer()) == data


def test_param_row_compare(capsys):
    a = TOY_PARAM_ST(Alpha=1)
    b = TOY_PARAM_ST(Alpha=2)
    a.compare(b)
    out = capsys.readouterr().out
    assert "Alpha" in out


def test_param_row_repr_is_broken():
    ParamRow.__repr__(TOY_PARAM_ST(Alpha=1))


# ---------------------------------------------------------------------------
# Param flags
# ---------------------------------------------------------------------------


def test_param_flags():
    f1 = ParamFlags1(0b1000_0110)
    assert f1.IntDataOffset
    assert f1.LongDataOffset
    assert f1.OffsetParam
    assert not f1[0]
    assert f1.pack() == 0b1000_0110

    f2 = ParamFlags2(0b0000_0001)
    assert f2.UnicodeRowNames
    assert ParamFlags2(0).UnicodeRowNames is False or ParamFlags2(0).UnicodeRowNames == 0


def test_param_get_name_encoding():
    assert Param.get_name_encoding(False, ParamFlags2(0)) == "shift_jis_2004"
    assert Param.get_name_encoding(True, ParamFlags2(0)) == "shift_jis_2004"
    assert Param.get_name_encoding(False, ParamFlags2(1)) == "utf-16-le"
    assert Param.get_name_encoding(True, ParamFlags2(1)) == "utf-16-be"


# ---------------------------------------------------------------------------
# TypedParam
# ---------------------------------------------------------------------------


def test_typed_param_is_cached(toy_param_cls):
    assert toy_param_cls.ROW_TYPE is TOY_PARAM_ST
    assert toy_param_cls.__name__ == "Param_TOY_PARAM_ST"
    # Repeat lookups are stable with each other (see L22: the *first* call returns a different object
    # to all later calls, because the `PathDataclassMeta` metaclass registers two `Param` subclasses).
    assert TypedParam(TOY_PARAM_ST) is TypedParam(TOY_PARAM_ST)
    assert TypedParam(TOY_PARAM_ST).ROW_TYPE is TOY_PARAM_ST


def test_typed_param_first_call_is_stable():
    class ONE_OFF_PARAM_ST(ParamRow):
        A: int = ParamField(int32, "a", default=0)

    assert TypedParam(ONE_OFF_PARAM_ST) is TypedParam(ONE_OFF_PARAM_ST)


def test_typed_param_field_names(toy_param_cls):
    assert toy_param_cls(param_type="TOY_PARAM_ST").field_names == TOY_PARAM_ST.get_binary_field_names()


def test_param_setitem_accepts_row(toy_param_cls):
    p = toy_param_cls(param_type="TOY_PARAM_ST")
    p[5] = TOY_PARAM_ST(Alpha=5)
    assert p[5].Alpha == 5
    with pytest.raises(TypeError):
        p[6] = 12345


def test_param_setitem_with_dict(toy_param_cls):
    p = toy_param_cls(param_type="TOY_PARAM_ST")
    p[7] = {"Alpha": 7}
    assert p[7].Alpha == 7


def test_param_binary_roundtrip_synthetic(toy_param_cls):
    p = toy_param_cls(
        param_type="TOY_PARAM_ST",
        flags1=ParamFlags1(0),
        flags2=ParamFlags2(0),
        paramdef_data_version=1,
        paramdef_format_version=104,
        rows={
            0: TOY_PARAM_ST(Alpha=1, Beta=1.0, Name="first"),
            10: TOY_PARAM_ST(Alpha=2, Beta=2.0, Name="second"),
            20: TOY_PARAM_ST(Alpha=3, Beta=3.0),  # no name
        },
    )
    data = bytes(p)
    p2 = toy_param_cls.from_bytes(data)
    assert p2.param_type == "TOY_PARAM_ST"
    assert set(p2.rows) == {0, 10, 20}
    assert p2[0].Name == "first"
    assert p2[20].Name == ""
    assert p2[10].Alpha == 2
    assert_bytes_equal(bytes(p2), data, "synthetic Param repack")


def test_param_detect_param_type_synthetic(toy_param_cls):
    p = toy_param_cls(
        param_type="TOY_PARAM_ST",
        rows={0: TOY_PARAM_ST(), 1: TOY_PARAM_ST()},
    )
    assert Param.detect_param_type(bytes(p)) == "TOY_PARAM_ST"


def test_param_json_roundtrip_synthetic(toy_param_cls, tmp_path):
    p = toy_param_cls(
        param_type="TOY_PARAM_ST",
        rows={0: TOY_PARAM_ST(Alpha=1, Name="a"), 5: TOY_PARAM_ST(Alpha=2, Name="b")},
    )
    p.write_json(tmp_path / "toy.json")
    p2 = toy_param_cls.from_json(tmp_path / "toy.json")
    assert set(p2.rows) == set(p.rows)
    assert p2[0].Alpha == 1 and p2[0].Name == "a"
    assert bytes(p2) == bytes(p)


def test_param_from_dict_rejects_wrong_type(toy_param_cls):
    with pytest.raises(ValueError):
        toy_param_cls.from_dict({"param_type": "OTHER_PARAM_ST", "rows": {}, "big_endian": False})


def test_param_from_json_requires_row_type(tmp_path):
    with pytest.raises(TypeError):
        Param.from_json(tmp_path / "nope.json")


def test_param_empty_rows_roundtrip(toy_param_cls):
    p = toy_param_cls(param_type="TOY_PARAM_ST", rows={})
    p2 = toy_param_cls.from_bytes(bytes(p))
    assert p2.rows == {}
    assert p2.param_type == "TOY_PARAM_ST"


def test_param_preserves_big_endian(toy_param_cls):
    p = toy_param_cls(
        param_type="TOY_PARAM_ST",
        big_endian=True,
        rows={0: TOY_PARAM_ST(Alpha=1), 1: TOY_PARAM_ST(Alpha=2)},
    )
    p2 = toy_param_cls.from_bytes(bytes(p))
    assert p2.big_endian is True


# ---------------------------------------------------------------------------
# `find_param_rows` search utilities
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "comparison, left, right, expected",
    [
        (ParamFieldComparisonType.Equal, 1, 1, True),
        (ParamFieldComparisonType.NotEqual, 1, 2, True),
        (ParamFieldComparisonType.GreaterThan, 2, 1, True),
        (ParamFieldComparisonType.LessThan, 1, 2, True),
        (ParamFieldComparisonType.GreaterThanOrEqual, 1, 1, True),
        (ParamFieldComparisonType.LessThanOrEqual, 1, 2, True),
        (ParamFieldComparisonType.GreaterThan, 1, 2, False),
    ],
)
def test_param_field_comparison_type(comparison, left, right, expected):
    assert comparison.compare(left, right) is expected


def test_param_field_search_condition_repr():
    c = ParamFieldSearchCondition("Alpha", ParamFieldComparisonType.GreaterThan, 5)
    assert repr(c) == "Alpha > 5"


def test_find_param_rows(toy_param_cls):
    p = toy_param_cls(
        param_type="TOY_PARAM_ST",
        rows={i: TOY_PARAM_ST(Alpha=i, FlagA=bool(i % 2)) for i in range(6)},
    )
    result = find_param_rows(p, [ParamFieldSearchCondition("Alpha", ParamFieldComparisonType.GreaterThan, 3)])
    assert set(result) == {4, 5}
    result = find_param_rows(
        p,
        [
            ParamFieldSearchCondition("Alpha", ParamFieldComparisonType.GreaterThanOrEqual, 2),
            ParamFieldSearchCondition("FlagA", ParamFieldComparisonType.Equal, True),
        ],
    )
    assert set(result) == {3, 5}


# ---------------------------------------------------------------------------
# Real PTDE `GameParamBND`
# ---------------------------------------------------------------------------


def test_ptde_gameparambnd_loads(ptde_gameparambnd):
    gp = ptde_gameparambnd
    assert len(gp.params) > 30
    assert "NpcParam" in gp.params
    assert all(isinstance(p, Param) for p in gp.params.values())


def test_ptde_gameparambnd_get_param_by_stem_and_nickname(ptde_gameparambnd):
    gp = ptde_gameparambnd
    by_stem = gp.get_param("NpcParam")
    assert by_stem is gp.params["NpcParam"]
    assert gp.get_param("NpcParam.param") is by_stem
    nickname = gp.PARAM_NICKNAMES["NpcParam"]
    assert gp.get_param(nickname) is by_stem
    with pytest.raises(KeyError):
        gp.get_param("NoSuchParam")


def test_ptde_param_row_types_are_generated_classes(ptde_gameparambnd):
    npc = ptde_gameparambnd.params["NpcParam"]
    assert npc.param_type == "NPC_PARAM_ST"
    assert npc.ROW_TYPE.__name__ == "NPC_PARAM_ST"
    row = next(iter(npc.rows.values()))
    assert isinstance(row, ParamRow)
    assert len(row.get_binary_field_names()) > 100


def test_ptde_param_row_names_decoded(ptde_gameparambnd):
    npc = ptde_gameparambnd.params["NpcParam"]
    named = [r for r in npc.rows.values() if r.Name]
    assert named, "expected at least some decoded shift-JIS row names"
    for row in named[:20]:
        # `RawName` is the source of truth and must re-encode to itself.
        assert row.Name.encode("shift_jis_2004") == row.RawName.rstrip(b"\0")


def test_ptde_all_params_binary_roundtrip_stable(ptde_gameparambnd):
    """unpack -> pack -> unpack -> pack must be byte-stable for every PTDE param."""
    for stem, param in ptde_gameparambnd.params.items():
        data = bytes(param)
        reloaded = type(param).from_bytes(data)
        assert set(reloaded.rows) == set(param.rows), stem
        assert_bytes_equal(bytes(reloaded), data, f"{stem} repack")


def test_ptde_all_params_row_values_stable(ptde_gameparambnd):
    for stem, param in ptde_gameparambnd.params.items():
        reloaded = type(param).from_bytes(bytes(param))
        for row_id, row in param.rows.items():
            assert reloaded.rows[row_id] == row, f"{stem}[{row_id}]"


def test_ptde_param_json_roundtrip(ptde_gameparambnd, tmp_path):
    npc = ptde_gameparambnd.params["NpcParam"]
    npc.write_json(tmp_path / "NpcParam.json")
    reloaded = type(npc).from_json(tmp_path / "NpcParam.json")
    assert set(reloaded.rows) == set(npc.rows)
    assert_bytes_equal(bytes(reloaded), bytes(npc), "NpcParam JSON round-trip")


@pytest.mark.slow
def test_ptde_gameparambnd_json_directory_roundtrip(ptde_gameparambnd, tmp_path):
    from soulstruct.darksouls1ptde.params import GameParamBND

    ptde_gameparambnd.write_json_directory(tmp_path / "gp")
    assert (tmp_path / "gp" / "GameParamBND_manifest.json").is_file()
    reloaded = GameParamBND.from_json_directory(tmp_path / "gp")
    assert set(reloaded.params) == set(ptde_gameparambnd.params)
    for stem, param in ptde_gameparambnd.params.items():
        assert_bytes_equal(bytes(reloaded.params[stem]), bytes(param), f"{stem} via JSON directory")


def test_ptde_gameparambnd_entry_autogen_and_write(ptde_gameparambnd, tmp_path):
    from soulstruct.darksouls1ptde.params import GameParamBND

    logging.disable(logging.WARNING)
    try:
        ptde_gameparambnd.write(tmp_path / "GameParam.parambnd")
        reloaded = GameParamBND.from_path(tmp_path / "GameParam.parambnd")
    finally:
        logging.disable(logging.NOTSET)
    assert set(reloaded.params) == set(ptde_gameparambnd.params)
    npc_a = ptde_gameparambnd.params["NpcParam"]
    npc_b = reloaded.params["NpcParam"]
    assert set(npc_a.rows) == set(npc_b.rows)


def test_ptde_duplicate_row_ids_are_dropped(resources_module_path):
    """Documented invariant: `Param` is a dict, so repeated vanilla row IDs are dropped.

    Loaded independently so it is not affected by another test regenerating Binder entries.
    """
    from soulstruct.darksouls1ptde.params import GameParamBND

    logging.disable(logging.WARNING)
    try:
        gp = GameParamBND.from_path(resources_module_path)
    finally:
        logging.disable(logging.NOTSET)
    vanilla = {e.stem: len(bytes(e)) for e in gp.entries}
    # `ObjectParam` has several repeated row IDs in vanilla PTDE, so the repack must be smaller.
    assert len(bytes(gp.params["ObjectParam"])) < vanilla["ObjectParam"]


def test_ptde_find_param_rows_on_real_data(ptde_gameparambnd):
    npc = ptde_gameparambnd.params["NpcParam"]
    field = npc.ROW_TYPE.get_binary_field_names()[0]
    zero_rows = find_param_rows(npc, [ParamFieldSearchCondition(field, ParamFieldComparisonType.Equal, 0)])
    assert 0 < len(zero_rows) <= len(npc)
