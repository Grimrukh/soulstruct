"""Pure-unit tests for `soulstruct.utilities` (excluding `maths`, which has its own module).

Covers `conversion`, `text`, `misc`, `files`, `inspection`, and the `binary` re-export shim.
Nothing here needs game data; a handful of tests use `tmp_path` for real file I/O.

`xfail`-marked tests document genuine library defects (see audit report `02-utilities.md`).
"""
from __future__ import annotations

import dataclasses
import json
import logging
import struct
import sys
from pathlib import Path

import pytest

from soulstruct.exceptions import RestoreBackupError
from soulstruct.utilities import binary as binary_module
from soulstruct.utilities.conversion import bit_set_to_int_group, floatify, int_group_to_bit_set
from soulstruct.utilities.files import (
    SOULSTRUCT_PATH,
    SOULSTRUCT_USER_DATA_PATH,
    create_bak,
    get_blake2b_hash_hex,
    get_md5_hash_hex,
    import_arbitrary_module,
    read_json,
    restore_bak,
    sync_directory,
    sync_file,
    write_data_to_path,
    write_json,
)
from soulstruct.utilities.inspection import (
    Timer,
    compare_dataclasses,
    find_errant_prints,
    get_dataclass_repr,
    get_hex_repr,
    profile_function,
    write_hex_repr,
)
from soulstruct.utilities.misc import (
    MISSING_REF,
    BiDict,
    Flags8,
    IDList,
    setdefault_lambda,
    traverse_path_tree,
)
from soulstruct.utilities.progress import report_progress
from soulstruct.utilities.text import (
    atoi,
    camel_case_to_spaces,
    indent_lines,
    natural_keys,
    pad_chars,
    string_to_identifier,
    word_wrap,
)


# ===========================================================================
# utilities.progress
# ===========================================================================


def test_report_progress_is_a_no_op_without_a_callback():
    """Call sites pass `progress` straight through, so `None` must be handled here, not there."""
    assert report_progress(None, 0, 10, "anything") is None


def test_report_progress_forwards_all_arguments():
    calls = []
    report_progress(lambda *args: calls.append(args), 3, 10, "MapPiece")
    report_progress(lambda *args: calls.append(args), 4, 10)
    assert calls == [(3, 10, "MapPiece"), (4, 10, "")]


def test_report_progress_does_not_swallow_callback_exceptions():
    """A callback raising is the documented way for a GUI to cancel a long operation."""

    def cancel(current, total, label):
        raise KeyboardInterrupt("user cancelled")

    with pytest.raises(KeyboardInterrupt):
        report_progress(cancel, 0, 10, "x")


# ===========================================================================
# utilities.conversion
# ===========================================================================


def test_bit_set_to_int_group_basic():
    assert bit_set_to_int_group({0}, 4) == [1, 0, 0, 0]
    assert bit_set_to_int_group({0, 1, 31}, 4) == [0b11 + 2 ** 31, 0, 0, 0]
    assert bit_set_to_int_group({32}, 4) == [0, 1, 0, 0]
    assert bit_set_to_int_group({127}, 4) == [0, 0, 0, 2 ** 31]
    assert bit_set_to_int_group(set(), 4) == [0, 0, 0, 0]


def test_bit_set_to_int_group_accepts_sequence_with_repeats(caplog):
    with caplog.at_level(logging.WARNING):
        assert bit_set_to_int_group([1, 1, 2], 4) == [0b110, 0, 0, 0]
    assert any("more than once" in r.message for r in caplog.records)


def test_bit_set_to_int_group_validation():
    with pytest.raises(ValueError):
        bit_set_to_int_group({128}, 4)  # out of range for 128-bit group
    with pytest.raises(ValueError):
        bit_set_to_int_group({-1}, 4)
    with pytest.raises(ValueError):
        bit_set_to_int_group({"x"}, 4)


def test_int_group_to_bit_set_128():
    assert int_group_to_bit_set([0b01001, 0, 0, 0], assert_size=4) == {0, 3}
    assert int_group_to_bit_set([0, 0, 0, 2 ** 31], assert_size=4) == {127}
    assert int_group_to_bit_set([0, 0, 0, 0], assert_size=4) == set()


def test_int_group_to_bit_set_validation():
    with pytest.raises(ValueError):
        int_group_to_bit_set({1, 2}, assert_size=4)  # not a list/tuple
    with pytest.raises(ValueError):
        int_group_to_bit_set([0, 0, 0], assert_size=4)  # wrong size


@pytest.mark.parametrize("bits", [{0, 3, 127}, {0, 4, 29, 30, 95, 96}, set(), {31, 32, 63, 64}])
def test_bit_set_roundtrip_128(bits):
    assert int_group_to_bit_set(bit_set_to_int_group(bits, 4), assert_size=4) == bits


@pytest.mark.parametrize("group_size,bits", [(8, {0, 130, 200}), (32, {0, 500, 1023})])
def test_bit_set_roundtrip_large_groups(group_size: int, bits: set[int]):
    assert int_group_to_bit_set(bit_set_to_int_group(bits, group_size), assert_size=group_size) == bits


def test_floatify():
    assert floatify(0) == 0.0
    assert floatify(0x3F800000) == 1.0
    assert floatify(0xC0000000) == -2.0
    # Signed variant accepts negative Python ints for the same bit patterns.
    signed = struct.unpack("<i", struct.pack("<I", 0xC0000000))[0]
    assert floatify(signed, signed=True) == -2.0


# ===========================================================================
# utilities.text
# ===========================================================================


def test_word_wrap():
    assert word_wrap("a b c", line_limit=3) == "a b\nc"
    assert "\n" not in word_wrap("short", line_limit=50)


@pytest.mark.parametrize(
    "camel,expected",
    [
        ("JSONFileName", "JSON File Name"),
        ("someVar", "some Var"),
        ("ABc", "A Bc"),
        ("lowercase", "lowercase"),
        ("", ""),
    ],
)
def test_camel_case_to_spaces(camel: str, expected: str):
    assert camel_case_to_spaces(camel) == expected


def test_string_to_identifier():
    assert string_to_identifier("Black Knight") == "BlackKnight"
    assert string_to_identifier("black knight") == "BlackKnight"
    assert string_to_identifier("123 Test") == "_123Test"
    assert string_to_identifier("SFX Foo Bar", remove_prefixes=("SFX ",)) == "FooBar"
    assert string_to_identifier("Foo!@# Bar") == "FooBar"
    assert string_to_identifier("") == ""
    # Model names like `m1234` keep an underscore separator and are not capitalized.
    assert string_to_identifier("Black Knight m1234") == "BlackKnight_m1234"


def test_string_to_identifier_preserve_models_off():
    assert string_to_identifier("Black Knight m1234", preserve_models=False) == "BlackKnightM1234"


def test_string_to_identifier_results_are_valid_python_names():
    for source in ("Black Knight", "123 Test", "Foo!@# Bar", "Black Knight m1234"):
        identifier = string_to_identifier(source)
        assert identifier.isidentifier(), identifier


def test_pad_chars_str_and_bytes():
    assert pad_chars("abc") == "abc\0"
    assert pad_chars("abc", encoding="utf-8") == b"abc\0"
    assert pad_chars("abcd", encoding="utf-8") == b"abcd\0\0\0\0"
    assert pad_chars("abc", encoding="utf-8", null_terminate=False) == b"abc\0"  # padded, not terminated
    assert pad_chars("abcd", encoding="utf-8", null_terminate=False) == b"abcd"
    assert pad_chars("abc", encoding="utf-8", alignment=8) == b"abc\0\0\0\0\0"
    assert pad_chars("abc", encoding="utf-16-le", alignment=4) == b"a\0b\0c\0\0\0"


def test_pad_chars_negative_alignment_raises():
    with pytest.raises(ValueError):
        pad_chars("abc", alignment=-1)


def test_pad_chars_zero_alignment_raises_value_error():
    with pytest.raises(ValueError):
        pad_chars("abc", alignment=0)


def test_indent_lines():
    assert indent_lines("a\nb") == "a\n    b"
    assert indent_lines("a\nb", indent=2) == "a\n  b"
    assert indent_lines("a") == "a"


def test_atoi_and_natural_keys():
    assert atoi("12") == 12
    assert atoi("ab") == "ab"
    assert natural_keys("m10_02") == ["m", 10, "_", 2, ""]
    names = ["m10_02", "m10_10", "m10_01"]
    assert sorted(names, key=natural_keys) == ["m10_01", "m10_02", "m10_10"]
    # Naive lexicographic sort gets this wrong, which is the point of `natural_keys`.
    assert sorted(names) == ["m10_01", "m10_02", "m10_10"]
    assert sorted(["x9", "x10"], key=natural_keys) == ["x9", "x10"]
    assert sorted(["x9", "x10"]) == ["x10", "x9"]


# ===========================================================================
# utilities.misc
# ===========================================================================


def test_missing_ref_singleton_and_equality():
    assert MISSING_REF is type(MISSING_REF)()  # singleton
    assert repr(MISSING_REF) == "<Missing Reference>"
    with pytest.raises(TypeError):
        _ = MISSING_REF == 1
    with pytest.raises(TypeError):
        _ = MISSING_REF in [1, 2, 3]  # `in` uses `__eq__`


def test_traverse_path_tree():
    tree = {"a": ["b", "c"], "d": {"e": ["f"]}}
    assert list(traverse_path_tree(tree)) == [("a", "b"), ("a", "c"), ("d", "e", "f")]
    # Nested dicts inside a list keep the current prefix.
    assert list(traverse_path_tree({"a": [{"b": ["c"]}]})) == [("a", "b", "c")]
    with pytest.raises(ValueError):
        list(traverse_path_tree("not a tree"))


def test_setdefault_lambda_is_lazy():
    calls = []

    def default():
        calls.append(1)
        return "made"

    d = {"a": "existing"}
    assert setdefault_lambda(d, "a", default) == "existing"
    assert calls == []  # never called
    assert setdefault_lambda(d, "b", default) == "made"
    assert calls == [1]
    assert setdefault_lambda(d, "b", default) == "made"
    assert calls == [1]  # still only called once


def test_bidict_basics():
    d = BiDict((1, "one"), (2, "two"))
    assert d[1] == "one"
    assert d["one"] == 1
    assert d[2] == "two"
    assert d["two"] == 2
    assert len(d) == 2
    assert list(d.keys()) == [1, 2]
    assert list(d.values()) == ["one", "two"]
    assert list(d.items()) == [(1, "one"), (2, "two")]
    assert list(d) == [1, 2]


def test_bidict_bad_init():
    with pytest.raises(ValueError):
        BiDict(1, 2)
    with pytest.raises(ValueError):
        BiDict((1, 2, 3))


def test_bidict_delete_and_reassign():
    d = BiDict((1, "one"), (2, "two"))
    del d[1]
    assert 1 not in d and "one" not in d
    d[2] = "dos"  # re-assigning an existing key must remove the old pair
    assert d[2] == "dos"
    assert "two" not in d


def test_flags8():
    class MyFlags(Flags8):
        pass

    f = MyFlags(0b00000101)
    assert [f[i] for i in range(8)] == [True, False, True, False, False, False, False, False]
    assert f.pack() == 5
    assert int(f) == 5
    assert repr(f) == "MyFlags(1, 0, 1, 0, 0, 0, 0, 0)"
    assert MyFlags.default().pack() == 0
    # Copy-construct from another `Flags8`.
    assert MyFlags(f).pack() == 5
    # Round-trip over all byte values.
    for byte in range(256):
        assert MyFlags(byte).pack() == byte


def test_idlist_basics():
    class Item:
        def __init__(self, name):
            self.name = name

    a, b, c = Item("a"), Item("b"), Item("c")
    lst = IDList([a, b])
    assert len(lst) == 2
    assert bool(lst)
    assert list(lst) == [a, b]
    assert lst[0] is a
    assert a in lst
    assert c not in lst
    assert lst.index(b) == 1
    lst.append(c)
    assert lst.index(c) == 2
    assert repr(lst).startswith("IDList(")


def test_idlist_uses_identity_not_equality():
    """`IDList` is keyed on `id()`, so two equal-but-distinct objects can both be members."""

    @dataclasses.dataclass
    class Item:
        name: str

    a, a_twin = Item("a"), Item("a")
    assert a == a_twin
    lst = IDList([a, a_twin])
    assert len(lst) == 2
    assert lst.index(a) == 0
    assert lst.index(a_twin) == 1
    with pytest.raises(ValueError):
        lst.append(a)  # same object twice is rejected


def test_idlist_remove_pop_clear_extend_sort_copy():
    class Item:
        def __init__(self, name):
            self.name = name

    a, b, c = Item("a"), Item("b"), Item("c")
    lst = IDList()
    lst.extend([a, b, c])
    assert [i.name for i in lst] == ["a", "b", "c"]

    lst.remove(b)
    assert [i.name for i in lst] == ["a", "c"]
    assert lst.index(c) == 1  # indices correctly decremented

    popped = lst.pop()
    assert popped is c
    assert len(lst) == 1

    lst.append(c)
    lst.append(b)
    lst.sort(key=lambda i: i.name)
    assert [i.name for i in lst] == ["a", "b", "c"]
    assert [lst.index(i) for i in (a, b, c)] == [0, 1, 2]

    copied = lst.copy()
    assert list(copied) == list(lst)
    copied.pop()
    assert len(lst) == 3  # original unaffected

    lst.clear()
    assert len(lst) == 0
    assert not lst

    with pytest.raises(ValueError):
        lst.remove(a)


def test_idlist_setitem():
    class Item:
        def __init__(self, name):
            self.name = name

    a, b, c = Item("a"), Item("b"), Item("c")
    lst = IDList([a, b])
    lst[1] = c
    assert list(lst) == [a, c]
    assert lst.index(c) == 1
    assert b not in lst
    with pytest.raises(ValueError):
        lst[0] = c  # already present


def test_idlist_insert_keeps_indices_correct():
    class Item:
        def __init__(self, name):
            self.name = name

    a, b, c = Item("a"), Item("b"), Item("c")
    lst = IDList([a, b])
    lst.insert(0, c)
    assert [i.name for i in lst] == ["c", "a", "b"]
    assert [lst.index(i) for i in (c, a, b)] == [0, 1, 2]


# ===========================================================================
# utilities.files
# ===========================================================================


def test_soulstruct_path():
    root = SOULSTRUCT_PATH()
    assert root.name == "soulstruct"
    assert root.is_dir()
    assert SOULSTRUCT_PATH("utilities", "maths").is_dir()
    assert SOULSTRUCT_PATH("utilities", "files.py").is_file()


def test_soulstruct_user_data_path():
    p = SOULSTRUCT_USER_DATA_PATH("sub", "file.json")
    assert p.name == "file.json"
    assert p.parent.name == "sub"
    assert p.is_absolute()


def test_create_bak(tmp_path: Path):
    f = tmp_path / "foo.msb"
    f.write_bytes(b"original")
    assert create_bak(f) is True
    bak = tmp_path / "foo.msb.bak"
    assert bak.is_file()
    assert bak.read_bytes() == b"original"
    # Never overwrites an existing backup.
    f.write_bytes(b"changed")
    assert create_bak(f) is False
    assert bak.read_bytes() == b"original"
    # Missing file is a no-op.
    assert create_bak(tmp_path / "nope.msb") is False


def test_restore_bak_from_bak_file(tmp_path: Path):
    f = tmp_path / "foo.msb"
    f.write_bytes(b"original")
    create_bak(f)
    f.write_bytes(b"changed")
    assert restore_bak(tmp_path / "foo.msb.bak") == 1
    assert f.read_bytes() == b"original"
    assert (tmp_path / "foo.msb.bak").is_file()  # copy, not move


def test_restore_bak_delete_baks(tmp_path: Path):
    f = tmp_path / "foo.msb"
    f.write_bytes(b"original")
    create_bak(f)
    f.write_bytes(b"changed")
    assert restore_bak(tmp_path / "foo.msb.bak", delete_baks=True) == 1
    assert f.read_bytes() == b"original"
    assert not (tmp_path / "foo.msb.bak").exists()


def test_restore_bak_suffixless_file(tmp_path: Path):
    """A file with NO suffix round-trips correctly (`foo` -> `foo.bak` -> `foo`)."""
    f = tmp_path / "foo"
    f.write_bytes(b"original")
    create_bak(f)
    f.write_bytes(b"changed")
    assert restore_bak(f) == 1
    assert f.read_bytes() == b"original"


def test_restore_bak_by_original_name(tmp_path: Path):
    f = tmp_path / "foo.msb"
    f.write_bytes(b"original")
    create_bak(f)
    f.write_bytes(b"changed")
    assert restore_bak(f) == 1
    assert f.read_bytes() == b"original"


def test_restore_bak_directory(tmp_path: Path):
    for name in ("a.msb", "b.msb"):
        p = tmp_path / name
        p.write_bytes(b"original")
        create_bak(p)
        p.write_bytes(b"changed")
    assert restore_bak(tmp_path) == 2
    assert (tmp_path / "a.msb").read_bytes() == b"original"
    assert (tmp_path / "b.msb").read_bytes() == b"original"


def test_restore_bak_directory_delete_baks(tmp_path: Path):
    p = tmp_path / "a.msb"
    p.write_bytes(b"original")
    create_bak(p)
    p.write_bytes(b"changed")
    assert restore_bak(tmp_path, delete_baks=True) == 1
    assert not (tmp_path / "a.msb.bak").exists()


def test_restore_bak_errors(tmp_path: Path):
    f = tmp_path / "foo"
    f.write_bytes(b"x")
    with pytest.raises(RestoreBackupError):
        restore_bak(f)  # no BAK exists
    with pytest.raises(RestoreBackupError):
        restore_bak(tmp_path / "does_not_exist")


def test_restore_bak_empty_directory_warns(tmp_path: Path, caplog):
    with caplog.at_level(logging.WARNING):
        assert restore_bak(tmp_path) == 0
    assert any("Could not find any" in r.message for r in caplog.records)


def test_read_write_json(tmp_path: Path):
    path = tmp_path / "data.json"
    data = {"a": 1, "b": [1, 2, 3], "c": {"d": "e"}}
    write_json(path, data)
    assert read_json(path) == data
    assert read_json(str(path)) == data
    # Non-ASCII with `ensure_ascii=False`.
    write_json(path, {"name": "ソウル"}, ensure_ascii=False)
    assert json.loads(path.read_text(encoding="utf-8"))["name"] == "ソウル"
    assert read_json(path, encoding="utf-8") == {"name": "ソウル"}


def test_read_json_decode_error(tmp_path: Path):
    path = tmp_path / "bad.json"
    path.write_text("{not json}", encoding="utf-8")
    with pytest.raises(ValueError, match="JSON decode error"):
        read_json(path)


def test_read_json_unicode_error_path(tmp_path: Path):
    path = tmp_path / "bad_unicode.json"
    path.write_bytes(b"\xff\xfe" + b'{"a": 1}')
    with pytest.raises(ValueError, match="Unicode decode error"):
        read_json(path, encoding="utf-8")


def test_read_json_unicode_error_str_path(tmp_path: Path):
    path = tmp_path / "bad_unicode.json"
    path.write_bytes(b"\xff\xfe" + b'{"a": 1}')
    with pytest.raises(ValueError, match="Unicode decode error"):
        read_json(str(path), encoding="utf-8")


def test_hash_helpers(tmp_path: Path):
    data = b"soulstruct"
    path = tmp_path / "data.bin"
    path.write_bytes(data)
    assert get_blake2b_hash_hex(data) == get_blake2b_hash_hex(path)
    assert get_blake2b_hash_hex(data) == get_blake2b_hash_hex(str(path))
    assert get_md5_hash_hex(data) == get_md5_hash_hex(path)
    assert len(get_md5_hash_hex(data)) == 32
    assert get_md5_hash_hex(b"a") != get_md5_hash_hex(b"b")
    with pytest.raises(TypeError):
        get_blake2b_hash_hex(123)
    with pytest.raises(TypeError):
        get_md5_hash_hex(123)


def test_sync_file(tmp_path: Path):
    src = tmp_path / "src.bin"
    src.write_bytes(b"hello")
    dst = tmp_path / "sub" / "dst.bin"
    assert sync_file(src, dst) is True  # created (and parent dirs made)
    assert dst.read_bytes() == b"hello"
    assert sync_file(src, dst) is False  # unchanged
    assert sync_file(src, dst, force_write=True) is True
    src.write_bytes(b"world")
    assert sync_file(src, dst) is True
    assert dst.read_bytes() == b"world"


def test_sync_directory(tmp_path: Path):
    src = tmp_path / "src"
    (src / "sub").mkdir(parents=True)
    (src / "a.txt").write_text("a")
    (src / "sub" / "b.txt").write_text("b")
    dst = tmp_path / "dst"

    copied, skipped, deleted = sync_directory(src, dst)
    assert (copied, skipped, deleted) == (2, 0, 0)
    assert (dst / "a.txt").read_text() == "a"
    assert (dst / "sub" / "b.txt").read_text() == "b"

    copied, skipped, deleted = sync_directory(src, dst)
    assert (copied, skipped, deleted) == (0, 2, 0)

    # Extraneous file in destination.
    (dst / "extra.txt").write_text("extra")
    copied, skipped, deleted = sync_directory(src, dst)
    assert deleted == 0  # not deleted without the flag
    copied, skipped, deleted = sync_directory(src, dst, delete_extraneous=True)
    assert deleted == 1
    assert not (dst / "extra.txt").exists()


def test_write_data_to_path(tmp_path: Path):
    dst = tmp_path / "sub" / "out.bin"
    assert write_data_to_path(b"first", dst, make_backup=False) is True
    assert dst.read_bytes() == b"first"
    assert write_data_to_path(b"first", dst, make_backup=False) is False  # unchanged
    assert write_data_to_path(b"second", dst, make_backup=False) is True
    assert dst.read_bytes() == b"second"
    # Same length, different content, must still be detected.
    assert write_data_to_path(b"secxnd", dst, make_backup=False) is True
    assert dst.read_bytes() == b"secxnd"
    # `force` always writes.
    assert write_data_to_path(b"secxnd", dst, force=True, make_backup=False) is True


def test_write_data_to_path_makes_backup(tmp_path: Path):
    dst = tmp_path / "out.bin"
    dst.write_bytes(b"original")
    assert write_data_to_path(b"new", dst) is True
    assert (tmp_path / "out.bin.bak").read_bytes() == b"original"


def test_write_data_to_path_force_makes_dirs(tmp_path: Path):
    dst = tmp_path / "new_sub" / "out.bin"
    assert write_data_to_path(b"data", dst, force=True, make_backup=False) is True
    assert dst.read_bytes() == b"data"


def test_import_arbitrary_module_standalone(tmp_path: Path):
    module_path = tmp_path / "standalone_mod_for_test.py"
    module_path.write_text("VALUE = 42\ndef f(): return VALUE * 2\n", encoding="utf-8")
    module = import_arbitrary_module(module_path)
    try:
        assert module.VALUE == 42
        assert module.f() == 84
        assert module.__name__ == "standalone_mod_for_test"
    finally:
        sys.modules.pop("standalone_mod_for_test", None)


def test_import_arbitrary_module_in_package(tmp_path: Path):
    pkg = tmp_path / "pkg_for_test"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("PACKAGE_VALUE = 'pkg'\n", encoding="utf-8")
    (pkg / "leaf.py").write_text("from . import PACKAGE_VALUE\nLEAF = PACKAGE_VALUE + '_leaf'\n", encoding="utf-8")
    module = import_arbitrary_module(pkg / "leaf.py")
    try:
        assert module.LEAF == "pkg_leaf"
        assert module.__name__ == "pkg_for_test.leaf"
        assert "pkg_for_test" in sys.modules
    finally:
        sys.modules.pop("pkg_for_test.leaf", None)
        sys.modules.pop("pkg_for_test", None)


def test_import_arbitrary_module_failure_does_not_leak(tmp_path: Path):
    module_path = tmp_path / "broken_mod_for_test.py"
    module_path.write_text("raise RuntimeError('boom')\n", encoding="utf-8")
    with pytest.raises(RuntimeError):
        import_arbitrary_module(module_path)
    assert "broken_mod_for_test" not in sys.modules


# ===========================================================================
# utilities.inspection
# ===========================================================================


@dataclasses.dataclass
class _Simple:
    a: int = 1
    b: str = "x"


@dataclasses.dataclass
class _Nested:
    name: str = "n"
    child: _Simple = dataclasses.field(default_factory=_Simple)


def test_get_dataclass_repr():
    text = get_dataclass_repr(_Simple(1, "x"))
    assert "_Simple(" in text
    assert "a = 1" in text
    assert "b = 'x'" in text


def test_get_dataclass_repr_nested_and_recursive():
    text = get_dataclass_repr(_Nested())
    assert "_Nested(" in text
    assert "_Simple(" in text
    # Self-reference must not infinitely recurse.
    n = _Nested()
    n.child = n  # type: ignore[assignment]
    assert isinstance(get_dataclass_repr(n), str)


def test_get_dataclass_repr_rejects_non_dataclass():
    with pytest.raises(ValueError):
        get_dataclass_repr(object())


def test_compare_dataclasses_equal(capsys):
    compare_dataclasses(_Simple(1, "x"), _Simple(1, "x"))
    assert "Comparing instances of _Simple" in capsys.readouterr().out


def test_compare_dataclasses_type_mismatch(capsys):
    compare_dataclasses(_Simple(), _Nested())
    assert "not of the same type" in capsys.readouterr().out


def test_compare_dataclasses_rejects_non_dataclass():
    with pytest.raises(ValueError):
        compare_dataclasses(object(), _Simple())
    with pytest.raises(ValueError):
        compare_dataclasses(_Simple(), object())


def test_compare_dataclasses_unequal_default_args(capsys):
    compare_dataclasses(_Simple(1, "x"), _Simple(2, "y"))
    assert "!=" in capsys.readouterr().out


def test_compare_dataclasses_unequal_with_is_close_funcs(capsys):
    """Passing an explicit (even empty) `is_close_funcs` dict works around the default-arg bug."""
    compare_dataclasses(_Simple(1, "x"), _Simple(2, "y"), is_close_funcs={})
    assert "!=" in capsys.readouterr().out


def test_get_hex_repr():
    text = get_hex_repr(b"\x00\x01\x02\x03" * 4 + b"\xff" * 16)
    lines = text.split("\n")
    assert len(lines) == 2
    assert lines[0].startswith("     0 |      0x0: 00 01 02 03")
    assert "ff ff" in lines[1]
    # Without line numbers, just hex bytes.
    assert get_hex_repr(b"\x00" * 16, with_line_numbers=False).startswith("00 00")


def test_get_hex_repr_with_unicode():
    text = get_hex_repr(b"ABCD" * 4, with_unicode=True)
    assert "A B C D" in text


def test_write_hex_repr(tmp_path: Path):
    path = tmp_path / "hex.txt"
    write_hex_repr(b"\x01" * 16, path)
    assert "01 01" in path.read_text(encoding="utf-8")


def test_timer_logs_completion(caplog):
    with caplog.at_level(logging.INFO, logger="soulstruct.utilities.inspection"):
        with Timer("MyTask"):
            pass
    assert any("MyTask COMPLETED" in r.message for r in caplog.records)


def test_timer_logs_failure(caplog):
    with caplog.at_level(logging.ERROR, logger="soulstruct.utilities.inspection"):
        with pytest.raises(RuntimeError):
            with Timer("MyTask"):
                raise RuntimeError("boom")
    assert any("MyTask FAILED" in r.message for r in caplog.records)


def test_timer_enter_returns_timer():
    with Timer("MyTask") as t:
        assert isinstance(t, Timer)


def test_profile_function_returns_value_and_preserves_metadata(capsys):
    @profile_function(3)
    def double(x, y=1):
        """Doc."""
        return x * 2 + y

    assert double(21) == 43
    assert double(21, y=0) == 42
    assert double.__name__ == "double"
    assert double.__doc__ == "Doc."
    out = capsys.readouterr().out
    assert "Profiling function: double" in out
    assert "function calls" in out


def test_profile_function_propagates_exceptions():
    @profile_function(1)
    def boom():
        raise ValueError("boom")

    with pytest.raises(ValueError):
        boom()


def test_find_errant_prints(capsys):
    import builtins

    original = builtins.print
    with find_errant_prints():
        assert builtins.print is not original
        print("hello")
    assert builtins.print is original
    out = capsys.readouterr().out
    assert "FN:" in out and "hello" in out


def test_find_errant_prints_restores_on_exception():
    import builtins

    original = builtins.print
    try:
        with find_errant_prints():
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    try:
        assert builtins.print is original
    finally:
        builtins.print = original  # never leak the patch into other tests


# ===========================================================================
# utilities.binary (constrata shim)
# ===========================================================================


def test_binary_shim_exports_constrata_names():
    for name in ("BinaryStruct", "BinaryReader", "BinaryWriter", "byte", "uint32", "single", "varint", "RESERVED"):
        assert hasattr(binary_module, name), name


def test_binary_metadata_factories_registered():
    factories = binary_module.BinaryStruct.METADATA_FACTORIES
    assert set(factories) >= {"Vector2", "Vector3", "Vector4", "EulerDeg", "EulerRad"}
    meta = factories["Vector3"]()
    assert meta.length == 3
