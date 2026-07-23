"""Tests for the `BaseBinaryFile` / `GameFile` / `GameFileDirectory` contract and the dataclass metaclasses.

These are pure unit tests: a tiny concrete `GameFile` subclass is defined here and exercised through the
whole public API (`from_bytes`, `from_path`, `to_bytes`, `write`, JSON, DCX, `.path` handling).
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from soulstruct.base.base_binary_file import BaseBinaryFile, BaseJSONEncoder
from soulstruct.base.game_file import GameFile
from soulstruct.base.game_file_directory import GameFileDirectory
from soulstruct.base.metaclasses import DataclassMeta, PathDataclassMeta
from soulstruct.containers import Binder, BinderEntry
from soulstruct.dcx import DCXType
from soulstruct.utilities.binary import BinaryReader, BinaryWriter


# ---------------------------------------------------------------------------
# Minimal concrete `GameFile` for testing
# ---------------------------------------------------------------------------


class DummyFile(GameFile):
    """Trivial binary format: int32 `value`, int32 length, then UTF-8 `text`."""

    EXT = ".dummy"

    value: int = 0
    text: str = ""

    @classmethod
    def from_reader(cls, reader: BinaryReader):
        value = reader.unpack_value("i")
        length = reader.unpack_value("i")
        return cls(value=value, text=reader.read(length).decode())

    def to_writer(self) -> BinaryWriter:
        writer = BinaryWriter()
        writer.pack("i", self.value)
        encoded = self.text.encode()
        writer.pack("i", len(encoded))
        writer.append(encoded)
        return writer


def _dummy() -> DummyFile:
    return DummyFile(value=42, text="hello")


# ---------------------------------------------------------------------------
# Construction / dataclass behaviour
# ---------------------------------------------------------------------------


def test_construction_defaults():
    dummy = DummyFile()
    assert dummy.value == 0
    assert dummy.text == ""
    assert dummy.path is None
    assert dummy.dcx_type is None
    assert dummy.cls_name == "DummyFile"


def test_fields_are_slotted():
    """`DataclassMeta` applies `slots=True`, so unknown attributes must be rejected."""
    dummy = _dummy()
    with pytest.raises(AttributeError):
        dummy.not_a_field = 1


def test_get_field_names_excludes_internals():
    names = _dummy().get_field_names()
    assert "_path" not in names and "_dcx_type" not in names
    assert "value" in names and "text" in names


def test_base_repr_lists_fields():
    text = DummyFile.base_repr(_dummy())
    assert "DummyFile(" in text and "value=42" in text


def test_path_property_coerces_str():
    dummy = _dummy()
    dummy.path = "some/dir/file.dummy"
    assert isinstance(dummy.path, Path)
    assert dummy.path_name == "file.dummy"
    dummy.path = None
    assert dummy.path is None
    assert dummy.path_name is None


def test_path_stem_properties():
    dummy = _dummy()
    dummy.path = Path("chr/c1000.chrbnd.dcx")
    assert dummy.path_stem == "c1000.chrbnd"
    assert dummy.path_minimal_stem == "c1000"


def test_set_dcx_type_accepts_string():
    dummy = _dummy()
    dummy.dcx_type = "DCX_KRAK"
    assert dummy.dcx_type is DCXType.DCX_KRAK
    dummy.dcx_type = None
    assert dummy.dcx_type is None
    with pytest.raises(TypeError):
        dummy.dcx_type = 5


def test_copy_is_deep():
    dummy = _dummy()
    clone = dummy.copy()
    clone.value = 99
    assert dummy.value == 42
    assert clone is not dummy


# ---------------------------------------------------------------------------
# `from_bytes` / `to_bytes` / DCX layering
# ---------------------------------------------------------------------------


def test_bytes_roundtrip_without_dcx():
    dummy = _dummy()
    data = dummy.to_bytes()
    assert data == bytes(dummy)
    reloaded = DummyFile.from_bytes(data)
    assert (reloaded.value, reloaded.text) == (42, "hello")
    assert reloaded.dcx_type == DCXType.Null


@pytest.mark.parametrize(
    "dcx_type",
    [DCXType.DCX_DFLT_10000_24_9, DCXType.DCX_DFLT_10000_44_9, DCXType.DCX_DFLT_11000_44_9],
    ids=lambda t: t.name,
)
def test_bytes_roundtrip_with_dcx(dcx_type: DCXType):
    """`__bytes__` compresses automatically; `from_bytes` decompresses and records the detected type."""
    dummy = _dummy()
    dummy.dcx_type = dcx_type
    data = bytes(dummy)
    assert data[:4] == b"DCX\0"
    reloaded = DummyFile.from_bytes(data)
    assert (reloaded.value, reloaded.text) == (42, "hello")
    assert reloaded.dcx_type == dcx_type
    # Re-packing the reloaded file reproduces the same bytes.
    assert bytes(reloaded) == data


def test_from_bytes_accepts_bytearray_and_reader():
    data = bytes(_dummy())
    assert DummyFile.from_bytes(bytearray(data)).value == 42
    assert DummyFile.from_bytes(BinaryReader(data)).value == 42


def test_from_bytes_accepts_binder_entry():
    entry = BinderEntry(data=bytes(_dummy()), entry_id=0, path="N:\\x\\a.dummy")
    assert DummyFile.from_bytes(entry).text == "hello"
    assert DummyFile.from_binder_entry(entry).text == "hello"
    assert entry.to_binary_file(DummyFile).path == Path("N:\\x\\a.dummy")


def test_from_bytes_propagates_errors():
    with pytest.raises(Exception):
        DummyFile.from_bytes(b"\x01\x02")  # too short


# ---------------------------------------------------------------------------
# `from_path` / `write` / `get_file_path`
# ---------------------------------------------------------------------------


def test_write_and_from_path(tmp_path: Path):
    dummy = _dummy()
    out = tmp_path / "a.dummy"
    written = dummy.write(out)
    assert written == [out]
    reloaded = DummyFile.from_path(out)
    assert reloaded.path == out
    assert (reloaded.value, reloaded.text) == (42, "hello")


def test_write_returns_empty_when_unchanged(tmp_path: Path):
    """`write()` is a no-op (returns `[]`) when the target file already has identical contents."""
    dummy = _dummy()
    out = tmp_path / "a.dummy"
    assert dummy.write(out) == [out]
    assert dummy.write(out) == []
    assert dummy.write(out, force=True) == [out]


def test_write_uses_self_path(tmp_path: Path):
    dummy = _dummy()
    dummy.path = tmp_path / "sub" / "dir" / "a.dummy"
    assert dummy.write() == [dummy.path]
    assert dummy.path.is_file()


def test_write_without_path_raises():
    with pytest.raises(ValueError):
        _dummy().write()


def test_write_appends_dcx_extension(tmp_path: Path):
    dummy = _dummy()
    dummy.dcx_type = DCXType.DCX_DFLT_10000_24_9
    dummy.write(tmp_path / "a.dummy")
    assert (tmp_path / "a.dummy.dcx").is_file()
    assert not (tmp_path / "a.dummy").is_file()
    reloaded = DummyFile.from_path(tmp_path / "a.dummy.dcx")
    assert reloaded.dcx_type == DCXType.DCX_DFLT_10000_24_9


def test_get_file_path_rules():
    dummy = _dummy()
    dummy.dcx_type = DCXType.Null
    # `EXT` is only appended when explicitly requested.
    assert dummy.get_file_path("x/y").name == "y"
    assert dummy.get_file_path("x/y", add_auto_ext=True).name == "y.dummy"
    assert dummy.get_file_path("x/y.dummy", add_auto_ext=True).name == "y.dummy"
    # Existing '.dcx' is stripped when `dcx_type` is Null.
    assert dummy.get_file_path("x/y.dummy.dcx").name == "y.dummy"
    # '.bak' paths are never modified.
    assert dummy.get_file_path("x/y.dummy.bak").name == "y.dummy.bak"
    dummy.dcx_type = DCXType.DCX_KRAK
    assert dummy.get_file_path("x/y.dummy").name == "y.dummy.dcx"
    assert dummy.get_file_path("x/y.dummy.dcx").name == "y.dummy.dcx"


def test_get_file_path_without_path_raises():
    with pytest.raises(ValueError):
        _dummy().get_file_path(None)


def test_from_path_strips_bak_suffix(tmp_path: Path):
    dummy = _dummy()
    bak = tmp_path / "a.dummy.bak"
    bak.write_bytes(bytes(dummy))
    reloaded = DummyFile.from_path(bak)
    assert reloaded.path == tmp_path / "a.dummy"


def test_from_bak_reads_existing_backup(tmp_path: Path):
    original = tmp_path / "a.dummy"
    original.write_bytes(bytes(DummyFile(value=1, text="new")))
    (tmp_path / "a.dummy.bak").write_bytes(bytes(DummyFile(value=2, text="old")))
    loaded = DummyFile.from_bak(original)
    assert loaded.value == 2  # backup preferred


def test_from_bak_creates_backup_if_missing(tmp_path: Path):
    original = tmp_path / "a.dummy"
    original.write_bytes(bytes(_dummy()))
    loaded = DummyFile.from_bak(original)
    assert loaded.value == 42
    assert (tmp_path / "a.dummy.bak").is_file()
    assert loaded.path == original


def test_from_bak_path_keeps_real_extension(tmp_path: Path):
    original = tmp_path / "a.dummy"
    original.write_bytes(bytes(_dummy()))
    (tmp_path / "a.dummy.bak").write_bytes(bytes(_dummy()))
    loaded = DummyFile.from_bak(original)
    assert loaded.path == original


# ---------------------------------------------------------------------------
# JSON
# ---------------------------------------------------------------------------


def test_to_dict_excludes_path_and_names_dcx_type():
    dummy = _dummy()
    dummy.path = Path("x/y.dummy")
    dummy.dcx_type = DCXType.DCX_KRAK
    data = dummy.to_dict()
    assert data == {"value": 42, "text": "hello", "dcx_type": "DCX_KRAK"}
    assert "path" not in data and "_path" not in data


def test_to_dict_none_dcx_type_becomes_null():
    assert _dummy().to_dict()["dcx_type"] == "Null"


def test_json_roundtrip(tmp_path: Path):
    dummy = _dummy()
    dummy.dcx_type = DCXType.DCX_DFLT_10000_24_9
    out = tmp_path / "a.dummy"
    dummy.write_json(out)
    json_path = tmp_path / "a.dummy.json"
    assert json_path.is_file()
    reloaded = DummyFile.from_json(json_path)
    assert (reloaded.value, reloaded.text) == (42, "hello")
    assert reloaded.dcx_type is DCXType.DCX_DFLT_10000_24_9
    assert reloaded.path == json_path


def test_write_json_keeps_existing_json_suffix(tmp_path: Path):
    out = tmp_path / "a.json"
    _dummy().write_json(out)
    assert out.is_file()
    assert not (tmp_path / "a.json.json").exists()


def test_write_json_without_path_raises():
    with pytest.raises(ValueError):
        _dummy().write_json(None)


def test_from_json_rejects_non_dict(tmp_path: Path):
    bad = tmp_path / "bad.json"
    bad.write_text("[1, 2, 3]", encoding="utf-8")
    with pytest.raises(TypeError):
        DummyFile.from_json(bad)


@pytest.mark.xfail(
    reason="DEAD CODE: `BaseJSONEncoder.default()` claims to handle `DCXType`, but `DCXType` is an `IntEnum`, "
           "so `json` serialises it as a bare integer and never calls `default()`. The branch is unreachable "
           "and any `DCXType` that reaches the encoder directly is written as e.g. `10`, not \"DCX_KRAK\".",
    strict=False,
)
def test_base_json_encoder_handles_dcx_type():
    assert json.dumps(DCXType.DCX_KRAK, cls=BaseJSONEncoder) == '"DCX_KRAK"'


def test_base_json_encoder_dcx_type_actual_behaviour():
    """Documents the current (surprising) behaviour: `DCXType` serialises as its integer value."""
    assert json.dumps(DCXType.DCX_KRAK, cls=BaseJSONEncoder) == "10"
    # `to_dict()` sidesteps this by converting to the member name itself.
    assert _dummy().to_dict()["dcx_type"] == "Null"


@pytest.mark.xfail(
    reason="BUG: `BaseJSONEncoder.default()` returns `None` for any unhandled object instead of calling "
           "`super().default(o)`. Unserialisable values are silently written as JSON `null` rather than "
           "raising `TypeError`, producing quietly-corrupt JSON.",
    strict=False,
)
def test_base_json_encoder_rejects_unknown_objects():
    with pytest.raises(TypeError):
        json.dumps(object(), cls=BaseJSONEncoder)


# ---------------------------------------------------------------------------
# `get_game` detection
# ---------------------------------------------------------------------------


def test_get_game_from_module_name():
    from soulstruct.darksouls1r.maps.msb import MSB
    from soulstruct.games import DARK_SOULS_DSR

    assert MSB.get_game() is DARK_SOULS_DSR


def test_get_game_fails_for_game_independent_class():
    with pytest.raises(ValueError):
        DummyFile.get_game()


def test_default_dcx_type_falls_back_to_null_with_warning(caplog):
    """A game-independent class logs a warning and assumes no compression."""
    dummy = _dummy()
    assert dummy.dcx_type is None
    with caplog.at_level("WARNING", logger="soulstruct.base.base_binary_file"):
        data = bytes(dummy)
    assert data[:4] != b"DCX\0"
    assert any("Could not detect default DCX type" in r.message for r in caplog.records)


def test_get_default_extension_requires_ext():
    class NoExtFile(DummyFile):
        EXT = ""

    with pytest.raises(TypeError):
        NoExtFile.get_default_extension()


def test_get_default_extension_uses_game_default():
    from soulstruct.darksouls1r.maps.msb import MSB

    ext = MSB.get_default_extension()
    assert ext.startswith(".msb")


# ---------------------------------------------------------------------------
# `PathDataclassMeta` constructor overload
# ---------------------------------------------------------------------------


def test_single_path_argument_calls_from_path(tmp_path: Path):
    out = tmp_path / "a.dummy"
    _dummy().write(out)
    loaded = DummyFile(out)  # single positional `Path` -> `from_path`
    assert isinstance(loaded, DummyFile)
    assert loaded.value == 42
    assert loaded.path == out


def test_path_keyword_argument_calls_from_path(tmp_path: Path):
    out = tmp_path / "a.dummy"
    _dummy().write(out)
    loaded = DummyFile(path=out)
    assert loaded.value == 42
    loaded_str = DummyFile(path=str(out))
    assert loaded_str.value == 42


def test_path_overload_not_triggered_with_other_kwargs(tmp_path: Path):
    dummy = DummyFile(path=tmp_path / "nonexistent.dummy", value=7)
    assert dummy.value == 7
    assert dummy.path == tmp_path / "nonexistent.dummy"


def test_metaclass_types():
    assert isinstance(DummyFile, PathDataclassMeta)
    assert issubclass(PathDataclassMeta, DataclassMeta)
    assert issubclass(DummyFile, BaseBinaryFile)


def test_zero_arg_super_still_works_in_subclass(tmp_path: Path):
    """`DataclassMeta` preserves `__classcell__` so zero-argument `super()` keeps working under slots."""

    class SubFile(DummyFile):
        def to_writer(self) -> BinaryWriter:
            return super().to_writer()

    out = tmp_path / "sub.dummy"
    SubFile(value=3, text="sub").write(out)
    assert SubFile.from_path(out).text == "sub"


# ---------------------------------------------------------------------------
# `GameFile.from_binder*`
# ---------------------------------------------------------------------------


def _binder_with_dummy() -> Binder:
    binder = Binder.empty_bnd4()
    binder.dcx_type = DCXType.Null
    binder.add_entry(BinderEntry(data=bytes(_dummy()), entry_id=0, path="N:\\X\\a.dummy"))
    binder.add_entry(BinderEntry(data=bytes(DummyFile(value=7, text="two")), entry_id=1, path="N:\\X\\b.dummy"))
    return binder


def test_from_binder_by_id_and_name():
    binder = _binder_with_dummy()
    assert DummyFile.from_binder(binder, 0).value == 42
    assert DummyFile.from_binder(binder, "b.dummy").value == 7


def test_from_binder_without_pattern_raises():
    binder = _binder_with_dummy()
    assert DummyFile.PATTERN is None
    with pytest.raises(ValueError):
        DummyFile.from_binder(binder)


def test_from_binder_uses_class_pattern():
    import re as _re

    class PatternedFile(DummyFile):
        PATTERN = _re.compile(r"b\.dummy")

    binder = _binder_with_dummy()
    assert PatternedFile.from_binder(binder).value == 7


def test_from_binder_path_and_multiple(tmp_path: Path):
    binder = _binder_with_dummy()
    out = tmp_path / "test.testbnd"
    binder.write(out)
    assert DummyFile.from_binder_path(out, 1).value == 7
    files = DummyFile.multiple_from_binder_path(out, [0, 1])
    assert [f.value for f in files] == [42, 7]


# ---------------------------------------------------------------------------
# `GameFileDirectory`
# ---------------------------------------------------------------------------


class DummyDirectory(GameFileDirectory[DummyFile]):
    FILE_NAME_PATTERN = r".*\.dummy"
    FILE_CLASS = DummyFile
    FILE_EXTENSION = ".dummy"


def _make_directory(tmp_path: Path) -> Path:
    directory = tmp_path / "dummies"
    directory.mkdir()
    DummyFile(value=1, text="one").write(directory / "one.dummy")
    DummyFile(value=2, text="two").write(directory / "two.dummy")
    (directory / "ignored.txt").write_bytes(b"not a dummy")
    return directory


def test_directory_from_path(tmp_path: Path):
    directory = _make_directory(tmp_path)
    game_dir = DummyDirectory.from_path(directory)
    assert set(game_dir.keys()) == {"one", "two"}
    assert game_dir.files["one"].value == 1
    assert set(dict(game_dir.items())) == {"one", "two"}
    assert [f.value for f in sorted(game_dir.values(), key=lambda f: f.value)] == [1, 2]
    assert game_dir.directory == directory


def test_directory_from_path_missing_directory(tmp_path: Path):
    with pytest.raises(NotADirectoryError):
        DummyDirectory.from_path(tmp_path / "nope")


def test_directory_single_path_argument(tmp_path: Path):
    directory = _make_directory(tmp_path)
    game_dir = DummyDirectory(directory)  # `PathDataclassMeta` overload
    assert isinstance(game_dir, DummyDirectory)
    assert set(game_dir.keys()) == {"one", "two"}


def test_directory_write_roundtrip(tmp_path: Path):
    directory = _make_directory(tmp_path)
    game_dir = DummyDirectory.from_path(directory)
    game_dir.files["one"].value = 111
    out_dir = tmp_path / "out"
    written = game_dir.write(out_dir)
    assert len(written) == 2
    reloaded = DummyDirectory.from_path(out_dir)
    assert reloaded.files["one"].value == 111
    # Writing again with unchanged content writes nothing.
    assert reloaded.write(out_dir) == []


def test_directory_write_without_directory_raises():
    with pytest.raises(ValueError):
        DummyDirectory().write()


def test_directory_is_iterable(tmp_path: Path):
    game_dir = DummyDirectory.from_path(_make_directory(tmp_path))
    assert sorted(iter(game_dir)) == ["one", "two"]


def test_directory_no_partial_write_on_pack_failure(tmp_path: Path):
    """`no_partial_write=True` (default) must not write ANY file if one fails to pack."""

    class BadFile(DummyFile):
        def to_writer(self) -> BinaryWriter:
            raise RuntimeError("cannot pack")

    game_dir = DummyDirectory(
        directory=tmp_path / "out",
        files={"good": DummyFile(value=1, text="ok"), "bad": BadFile()},
    )
    with pytest.raises(RuntimeError):
        game_dir.write(tmp_path / "out")
    assert not (tmp_path / "out" / "good.dummy").exists()


def test_directory_partial_write_allowed(tmp_path: Path):
    class BadFile(DummyFile):
        def to_writer(self) -> BinaryWriter:
            raise RuntimeError("cannot pack")

    game_dir = DummyDirectory(
        directory=tmp_path / "out2",
        files={"good": DummyFile(value=1, text="ok"), "bad": BadFile()},
    )
    written = game_dir.write(tmp_path / "out2", no_partial_write=False)
    assert written == [tmp_path / "out2" / "good.dummy"]
