"""Tests for `soulstruct.containers` -- Binder (BND/BXF v3 & v4), BinderEntry, and TPF.

Most tests build Binders in memory so they run without any game installation.
"""
from __future__ import annotations

import re
import zlib
from pathlib import Path

import pytest

from soulstruct.containers import Binder, BinderEntry, BinderEntryFlags, BinderFlags, BinderVersion
from soulstruct.containers.binder_hash import BinderHashTable
from soulstruct.containers.core import (
    BinderError,
    BinderVersion4Info,
    EntryNotFoundError,
    MultipleEntriesFoundError,
)
from soulstruct.containers.tpf import TPF, TPFPlatform, TPFTexture, TextureType
from soulstruct.dcx import DCXType


ROOT = "N:\\TEST\\data\\thing"


def _entry(entry_id: int, name: str, data: bytes = b"", flags: int = 0x2) -> BinderEntry:
    return BinderEntry(data=data, entry_id=entry_id, path=f"{ROOT}\\{name}", flags=flags)


def _populated(binder: Binder) -> Binder:
    binder.dcx_type = DCXType.Null
    binder.add_entry(_entry(0, "alpha.txt", b"alpha data"))
    binder.add_entry(_entry(1, "beta.txt", b"beta data, slightly longer"))
    binder.add_entry(_entry(2, "gamma.bin", bytes(range(256))))
    return binder


# ---------------------------------------------------------------------------
# BinderFlags
# ---------------------------------------------------------------------------


def test_binder_flags_bits():
    flags = BinderFlags(0b0010_1110)  # the near-universal value 46
    assert not flags.is_big_endian
    assert flags.has_ids
    assert flags.has_names_1
    assert flags.has_names_2
    assert flags.has_names
    assert not flags.has_long_offsets
    assert flags.has_compression


def test_binder_flags_entry_header_size():
    # 16 base + 4 (ids) + 4 (names) + 8 (compression) + 4 (short offset)
    assert BinderFlags(0b0010_1110).get_bnd_entry_header_size() == 36
    # No optional fields at all: 16 + 4 (short offset)
    assert BinderFlags(0).get_bnd_entry_header_size() == 20
    # Long offsets add 8 instead of 4.
    assert BinderFlags(0b0011_1110).get_bnd_entry_header_size() == 40


@pytest.mark.parametrize("value", [0, 0b0010_1110, 0b0111_0100, 0xFF])
@pytest.mark.parametrize("bit_big_endian", [True, False])
def test_binder_flags_byte_roundtrip(value: int, bit_big_endian: bool):
    flags = BinderFlags.from_byte(value, bit_big_endian)
    assert flags.to_byte(bit_big_endian) == value


# ---------------------------------------------------------------------------
# BinderEntry
# ---------------------------------------------------------------------------


def test_binder_entry_path_properties():
    entry = _entry(3, "some.file.name.tpf.dcx", b"xyz")
    assert entry.name == "some.file.name.tpf.dcx"
    assert entry.stem == "some"
    assert entry.suffix == ".dcx"
    assert entry.suffixes == [".file", ".name", ".tpf", ".dcx"]
    assert entry.data_size == 3
    assert entry.path_with_forward_slashes == f"{ROOT}/some.file.name.tpf.dcx".replace("\\", "/")
    assert entry.directory_with_forward_slashes == ROOT.replace("\\", "/")


def test_binder_entry_missing_path_raises():
    entry = BinderEntry(data=b"", entry_id=0, path=None)
    for attr in ("name", "stem", "suffix", "suffixes", "path_with_forward_slashes"):
        with pytest.raises(ValueError):
            getattr(entry, attr)


def test_binder_entry_set_path_name():
    entry = _entry(0, "old.txt")
    entry.set_path_name("new.txt")
    assert entry.name == "new.txt"
    assert entry.path == f"{ROOT}\\new.txt"


def test_binder_entry_uncompressed_data_passthrough():
    entry = _entry(0, "a.txt", b"plain")
    assert entry.get_uncompressed_data() == b"plain"
    assert bytes(entry) == b"plain"
    entry.set_uncompressed_data(b"other")
    assert entry.data == b"other"


def test_binder_entry_zlib_compression_flag():
    """`BinderEntryFlags.Compressed` (bit 0) makes `data` a zlib stream."""
    entry = BinderEntry(data=b"", entry_id=0, path=f"{ROOT}\\c.txt", flags=0x3)
    assert BinderEntryFlags.is_compressed(entry.flags)
    payload = b"compress me" * 100
    entry.set_uncompressed_data(payload)
    assert entry.data != payload
    assert zlib.decompress(entry.data) == payload
    assert entry.get_uncompressed_data() == payload


def test_binder_entry_copy_is_independent():
    entry = _entry(0, "a.txt", b"data")
    clone = entry.copy()
    clone.entry_id = 99
    clone.data = b"changed"
    assert entry.entry_id == 0
    assert entry.data == b"data"


def test_binder_entry_flags_bit_reversal():
    assert BinderEntryFlags.from_byte(0b1000_0000, bit_big_endian=True) == 0b1000_0000
    assert BinderEntryFlags.from_byte(0b1000_0000, bit_big_endian=False) == 0b0000_0001
    assert BinderEntryFlags.to_byte(0b0000_0001, bit_big_endian=False) == 0b1000_0000


@pytest.mark.xfail(
    reason="BUG: `BinderEntry.get_header()` sets `uncompressed_size=self.data_size` (the COMPRESSED size) "
           "when the binder has the compression flag, and computes the true uncompressed size only in the "
           "`else` branch, where the value is never written. The ternary is inverted.",
    strict=False,
)
def test_binder_entry_header_uncompressed_size():
    payload = b"compress me" * 100
    entry = BinderEntry(data=b"", entry_id=0, path=f"{ROOT}\\c.txt", flags=0x3)
    entry.set_uncompressed_data(payload)
    header = entry.get_header(BinderFlags(0b0010_1110))  # has_compression
    assert header.compressed_size == len(entry.data)
    assert header.uncompressed_size == len(payload)


# ---------------------------------------------------------------------------
# Binder construction & round-trips
# ---------------------------------------------------------------------------


def test_empty_binder_constructors():
    bnd3 = Binder.empty_bnd3()
    assert bnd3.version == BinderVersion.V3 and bnd3.v4_info is None and not bnd3.is_split_bxf
    bnd4 = Binder.empty_bnd4()
    assert bnd4.version == BinderVersion.V4 and isinstance(bnd4.v4_info, BinderVersion4Info)
    bxf3 = Binder.empty_bxf3()
    assert bxf3.is_split_bxf and bxf3.version == BinderVersion.V3
    bxf4 = Binder.empty_bxf4()
    assert bxf4.is_split_bxf and bxf4.version == BinderVersion.V4


def test_binder_len_iter_bool():
    binder = _populated(Binder.empty_bnd4())
    assert len(binder) == 3
    assert [e.entry_id for e in binder] == [0, 1, 2]
    assert bool(Binder.empty_bnd4()) is True  # empty binder is still truthy
    assert binder.entry_count == 3
    assert binder.highest_entry_id == 2
    assert binder.get_entry_ids() == [0, 1, 2]
    assert binder.get_entry_names() == ["alpha.txt", "beta.txt", "gamma.bin"]


@pytest.mark.parametrize("version", [BinderVersion.V3, BinderVersion.V4], ids=["BND3", "BND4"])
def test_bnd_binary_roundtrip(version: BinderVersion):
    """unpack -> pack -> unpack must preserve every entry exactly."""
    binder = _populated(Binder.empty_bnd3() if version == BinderVersion.V3 else Binder.empty_bnd4())
    data = bytes(binder)
    assert data[:4] == (b"BND3" if version == BinderVersion.V3 else b"BND4")

    reloaded = Binder.from_bytes(data)
    assert reloaded.version == version
    assert reloaded.signature == binder.signature
    assert int(reloaded.flags) == int(binder.flags)
    assert len(reloaded.entries) == 3
    for original, new in zip(binder.entries, reloaded.entries):
        assert (new.entry_id, new.path, new.data, new.flags) == (
            original.entry_id, original.path, original.data, original.flags
        )

    # Second round-trip must be byte-identical to the first (stability).
    assert bytes(reloaded) == data


def test_bnd4_hash_table_is_rebuilt_when_paths_change():
    binder = _populated(Binder.empty_bnd4(hash_table_type=4))
    first = bytes(binder)
    reloaded = Binder.from_bytes(first)
    assert reloaded.v4_info.most_recent_hash_table  # captured from header
    reloaded.entries[0].set_path_name("renamed.txt")
    second = bytes(reloaded)
    assert second != first
    again = Binder.from_bytes(second)
    assert again.entries[0].name == "renamed.txt"


def test_bnd4_no_hash_table():
    binder = _populated(Binder.empty_bnd4(hash_table_type=0))
    reloaded = Binder.from_bytes(bytes(binder))
    assert reloaded.v4_info.hash_table_type == 0
    assert len(reloaded.entries) == 3


def test_bxf3_split_roundtrip():
    binder = _populated(Binder.empty_bxf3())
    packed_bhd, packed_bdt = binder.get_split_bytes()
    assert packed_bhd[:4] == b"BHF3"
    assert packed_bdt[:4] == b"BDF3"
    reloaded = Binder.from_bytes(packed_bhd, packed_bdt)
    assert reloaded.is_split_bxf
    assert [(e.entry_id, e.path, e.data) for e in reloaded.entries] == [
        (e.entry_id, e.path, e.data) for e in binder.entries
    ]


def test_bxf4_split_roundtrip():
    binder = _populated(Binder.empty_bxf4())
    packed_bhd, packed_bdt = binder.get_split_bytes()
    assert packed_bhd[:4] == b"BHF4"
    assert packed_bdt[:4] == b"BDT4"
    reloaded = Binder.from_bytes(packed_bhd, packed_bdt)
    assert len(reloaded.entries) == 3


def test_bnd_write_and_from_path(tmp_path: Path):
    binder = _populated(Binder.empty_bnd4())
    out = tmp_path / "test.testbnd"
    written = binder.write(out)
    assert written == [out]
    assert out.is_file()
    reloaded = Binder.from_path(out)
    assert reloaded.path == out
    assert len(reloaded.entries) == 3


def test_bnd_write_with_dcx(tmp_path: Path):
    binder = _populated(Binder.empty_bnd4())
    binder.dcx_type = DCXType.DCX_DFLT_10000_44_9
    out = tmp_path / "test.testbnd"
    binder.write(out)
    dcx_path = tmp_path / "test.testbnd.dcx"
    assert dcx_path.is_file(), "DCX extension should be appended automatically."
    reloaded = Binder.from_path(dcx_path)
    assert reloaded.dcx_type == DCXType.DCX_DFLT_10000_44_9
    assert len(reloaded.entries) == 3


def test_split_bxf_write_and_autodetect_bdt(tmp_path: Path):
    binder = _populated(Binder.empty_bxf3())
    bhd_path = tmp_path / "textures.tpfbhd"
    written = binder.write(bhd_path)
    assert (tmp_path / "textures.tpfbdt").is_file()
    assert len(written) == 2
    # `from_path` should find the BDT next to the BHD automatically.
    reloaded = Binder.from_path(bhd_path)
    assert reloaded.is_split_bxf
    assert len(reloaded.entries) == 3


def test_write_split_into_binder_entries():
    binder = _populated(Binder.empty_bxf3())
    bhd_entry = _entry(10, "x.tpfbhd")
    bdt_entry = _entry(11, "x.tpfbdt")
    binder.write_split(bhd_entry, bdt_entry)
    assert bhd_entry.data[:4] == b"BHF3"
    assert bdt_entry.data[:4] == b"BDF3"


def test_bnd_bytes_rejects_split():
    binder = Binder.empty_bxf3()
    with pytest.raises(TypeError):
        bytes(binder)


def test_from_path_rejects_bdt_path_for_bnd(tmp_path: Path):
    binder = _populated(Binder.empty_bnd4())
    out = tmp_path / "plain.testbnd"
    binder.write(out)
    with pytest.raises(ValueError, match="Cannot pass in `bdt_path`"):
        Binder.from_path(out, bdt_path=tmp_path / "nope.bdt")


def test_is_split_bxf_class_constraints():
    """`IS_SPLIT_BXF` class var lets subclasses forbid one of the two layouts."""

    class BNDOnly(Binder):
        IS_SPLIT_BXF = False

    class BXFOnly(Binder):
        IS_SPLIT_BXF = True

    with pytest.raises(ValueError):
        BNDOnly.empty_bxf3()
    with pytest.raises(ValueError):
        BXFOnly.empty_bnd3()


def test_from_path_rejects_non_binder(tmp_path: Path):
    bad = tmp_path / "bad.bin"
    bad.write_bytes(b"NOPE" + b"\0" * 100)
    with pytest.raises(ValueError):
        Binder.from_path(bad)


# ---------------------------------------------------------------------------
# Entry lookup / `__getitem__`
# ---------------------------------------------------------------------------


def test_getitem_by_id_name_path_and_regex():
    binder = _populated(Binder.empty_bnd4())
    assert binder[1].name == "beta.txt"
    assert binder["gamma.bin"].entry_id == 2
    assert binder[Path(f"{ROOT}\\alpha.txt")].entry_id == 0
    # A `str` containing a separator is treated as a full path.
    assert binder[f"{ROOT}\\alpha.txt"].entry_id == 0
    assert binder[re.compile(r"beta\..*")].entry_id == 1


def test_getitem_bad_type():
    binder = _populated(Binder.empty_bnd4())
    with pytest.raises(TypeError):
        binder[3.5]


def test_find_entry_methods():
    binder = _populated(Binder.empty_bnd4())
    assert binder.find_entry_by_id(0).name == "alpha.txt"
    assert binder.find_entry_by_name("beta.txt").entry_id == 1
    assert binder.find_entry_by_stem("gamma").entry_id == 2
    assert binder.find_entry_by_path(f"{ROOT}\\alpha.txt").entry_id == 0
    assert binder.find_entry_by_name_regex(r"alpha").entry_id == 0
    assert len(binder.find_entries_by_name_regex(r".*\.txt")) == 2
    assert len(binder.find_entries_by_path_regex(r"N:\\TEST")) == 3


def test_find_entry_not_found_raises_entry_not_found_error(tmp_path: Path):
    """`EntryNotFoundError` is a `KeyError` subclass, so `binder[...]` behaves like a mapping."""
    binder = _populated(Binder.empty_bnd4())
    binder.path = tmp_path / "dummy.bnd"  # needed; see `test_entry_not_found_without_path`
    with pytest.raises(EntryNotFoundError):
        binder[999]
    with pytest.raises(KeyError):
        binder["nope.txt"]


def test_entry_not_found_without_path():
    binder = _populated(Binder.empty_bnd4())
    assert binder.path is None
    with pytest.raises(EntryNotFoundError):
        binder[999]


def test_duplicate_names_raise_multiple_entries_found():
    binder = Binder.empty_bnd4()
    binder.add_entry(_entry(0, "same.txt", b"a"))
    binder.add_entry(_entry(1, "same.txt", b"b"))
    with pytest.raises(MultipleEntriesFoundError):
        binder["same.txt"]
    with pytest.raises(MultipleEntriesFoundError):
        binder.get_entries_by_name()


def test_get_entries_by_id_and_path():
    binder = _populated(Binder.empty_bnd4())
    assert set(binder.get_entries_by_id()) == {0, 1, 2}
    assert set(binder.get_entries_by_path()) == {f"{ROOT}\\{n}" for n in ("alpha.txt", "beta.txt", "gamma.bin")}


def test_get_entries_by_id_duplicate_raises():
    binder = Binder.empty_bnd4()
    binder.add_entry(_entry(0, "a.txt"))
    binder.add_entry(_entry(0, "b.txt"), ignore_id_conflict=True)
    with pytest.raises(BinderError):
        binder.get_entries_by_id()


def test_looks_like_entry_path():
    assert Binder.looks_like_entry_path(Path("a"))
    assert Binder.looks_like_entry_path("a/b")
    assert Binder.looks_like_entry_path("a\\b")
    assert not Binder.looks_like_entry_path("a.txt")
    assert not Binder.looks_like_entry_path(3)


# ---------------------------------------------------------------------------
# Entry management
# ---------------------------------------------------------------------------


def test_add_entry_rejects_same_instance():
    binder = Binder.empty_bnd4()
    entry = _entry(0, "a.txt")
    binder.add_entry(entry)
    with pytest.raises(BinderError):
        binder.add_entry(entry)


def test_remove_entry_methods():
    binder = _populated(Binder.empty_bnd4())
    binder.remove_entry_id(0)
    assert len(binder) == 2
    binder.remove_entry_name("beta.txt")
    assert len(binder) == 1
    binder.remove_entry_path(f"{ROOT}\\gamma.bin")
    assert len(binder) == 0
    with pytest.raises(KeyError):
        binder.remove_entry(_entry(5, "ghost.txt"))


def test_clear_and_auto_enumerate():
    binder = _populated(Binder.empty_bnd4())
    binder.auto_enumerate_entries(sort_key=lambda e: e.name)
    assert [e.name for e in binder] == ["alpha.txt", "beta.txt", "gamma.bin"]
    assert binder.get_entry_ids() == [0, 1, 2]
    binder.clear_entries()
    assert len(binder) == 0


def test_add_or_replace_entry_with_name():
    binder = _populated(Binder.empty_bnd4())
    binder.add_or_replace_entry_with_name(_entry(0, "alpha.txt", b"NEW"))
    assert len(binder) == 3
    assert binder["alpha.txt"].data == b"NEW"


def test_add_or_replace_entry_with_id():
    binder = Binder.empty_bnd4()
    binder.add_entry(_entry(5, "a.txt", b"OLD"))
    binder.add_or_replace_entry_with_id(_entry(5, "a.txt", b"NEW"))
    assert len(binder) == 1
    assert binder.find_entry_by_id(5).data == b"NEW"


def test_or_operator_merges_by_name():
    binder = _populated(Binder.empty_bnd4())
    other = [_entry(0, "alpha.txt", b"REPLACED"), _entry(9, "delta.txt", b"NEW")]
    binder | other
    assert len(binder) == 4
    assert binder["alpha.txt"].data == b"REPLACED"
    assert binder["delta.txt"].entry_id == 9
    with pytest.raises(TypeError):
        binder | "not a binder"


def test_get_first_new_entry_id_in_range():
    binder = _populated(Binder.empty_bnd4())
    assert binder.get_first_new_entry_id_in_range(0, 10) == 3
    with pytest.raises(EntryNotFoundError):
        binder.get_first_new_entry_id_in_range(0, 3)


def test_get_default_entry_path_requires_root():
    with pytest.raises(BinderError):
        Binder.get_default_entry_path("a.txt")

    class RootedBinder(Binder):
        DEFAULT_ENTRY_ROOT = "N:\\ROOT"

    assert RootedBinder.get_default_entry_path("a.txt") == "N:\\ROOT\\a.txt"


def test_set_default_entry_returns_existing():
    binder = _populated(Binder.empty_bnd4())
    entry = binder.set_default_entry("alpha.txt")
    assert entry.data == b"alpha data"
    assert len(binder) == 3


def test_set_default_entry_creates_new(tmp_path: Path):
    binder = _populated(Binder.empty_bnd4())
    binder.path = tmp_path / "dummy.bnd"  # required: see `test_entry_not_found_without_path`
    entry = binder.set_default_entry(7, new_path=f"{ROOT}\\new.txt")
    assert entry.entry_id == 7
    assert entry.data == b""
    assert len(binder) == 4
    entry.set_uncompressed_data(b"filled in")
    assert binder[7].data == b"filled in"


def test_set_default_entry_on_empty_binder():
    class RootedBinder(Binder):
        DEFAULT_ENTRY_ROOT = "N:\\ROOT"

    binder = RootedBinder.empty_bnd4()
    entry = binder.set_default_entry("first.txt")
    assert entry.entry_id == 0


# ---------------------------------------------------------------------------
# Repr / manifest / unpacked directories
# ---------------------------------------------------------------------------


def test_binder_repr_with_entries():
    binder = _populated(Binder.empty_bnd4())
    assert "BinderEntry(0" in repr(binder)


def test_binder_repr_when_empty():
    assert isinstance(repr(Binder.empty_bnd4()), str)


def test_manifest_header_roundtrip():
    binder = _populated(Binder.empty_bnd4())
    manifest = binder.get_manifest_header()
    assert manifest["binder_type"] == "BND4"
    assert manifest["dcx_type"] == "Null"
    kwargs = Binder.process_manifest_header(manifest)
    assert kwargs["version"] == BinderVersion.V4
    assert kwargs["is_split_bxf"] is False
    assert kwargs["v4_info"].hash_table_type == 4


def test_manifest_header_bxf3():
    binder = _populated(Binder.empty_bxf3())
    manifest = binder.get_manifest_header()
    assert manifest["binder_type"] == "BXF3"
    kwargs = Binder.process_manifest_header(manifest)
    assert kwargs["is_split_bxf"] is True
    assert kwargs["version"] == BinderVersion.V3


def test_process_manifest_header_missing_key():
    with pytest.raises(BinderError):
        Binder.process_manifest_header({"binder_type": "BND4"})


def test_process_manifest_header_bad_binder_type():
    manifest = _populated(Binder.empty_bnd4()).get_manifest_header()
    manifest["binder_type"] = "XXX4"
    with pytest.raises(ValueError):
        Binder.process_manifest_header(manifest)


def test_manifest_header_with_default_dcx_type():
    binder = Binder.empty_bnd4()
    binder.add_entry(_entry(0, "a.txt", b"x"))
    assert binder.dcx_type is None
    binder.get_manifest_header()


def test_unpacked_directory_roundtrip(tmp_path: Path):
    binder = _populated(Binder.empty_bnd4())
    directory = tmp_path / "test.testbnd.unpacked"
    binder.write_unpacked_directory(directory)
    assert (directory / "binder_manifest.json").is_file()
    reloaded = Binder.from_unpacked_path(directory)
    assert reloaded.version == BinderVersion.V4
    assert len(reloaded.entries) == 3
    assert [(e.entry_id, e.path, e.data) for e in reloaded.entries] == [
        (e.entry_id, e.path, e.data) for e in binder.entries
    ]
    # `.unpacked` suffix is stripped from the recovered `path`.
    assert reloaded.path.name == "test.testbnd"


def test_unpacked_directory_from_manifest_json(tmp_path: Path):
    binder = _populated(Binder.empty_bnd3())
    directory = tmp_path / "unpacked_bnd3"
    binder.write_unpacked_directory(directory)
    reloaded = Binder.from_unpacked_path(directory / Binder.MANIFEST_NAME)
    assert reloaded.version == BinderVersion.V3
    assert len(reloaded.entries) == 3


def test_from_unpacked_path_bad_source(tmp_path: Path):
    bad = tmp_path / "not_a_manifest.json"
    bad.write_text("{}")
    with pytest.raises(ValueError):
        Binder.from_unpacked_path(bad)


def test_to_dict_not_supported():
    with pytest.raises(TypeError):
        Binder.empty_bnd4().to_dict()


# ---------------------------------------------------------------------------
# Hash table
# ---------------------------------------------------------------------------


def test_path_hash_is_separator_and_root_agnostic():
    a = BinderHashTable.path_hash("N:\\a\\b.txt")
    b = BinderHashTable.path_hash("N:/a/b.txt")
    assert a == b
    assert BinderHashTable.path_hash("a/b.txt") == BinderHashTable.path_hash("/a/b.txt")


def test_is_prime():
    def _naive_is_prime(n: int) -> bool:
        if n < 2:
            return False
        return all(n % i for i in range(2, int(n ** 0.5) + 1))

    for n in range(0, 500):
        assert BinderHashTable.is_prime(n) == _naive_is_prime(n), n


def test_build_hash_table_is_deterministic():
    entries = [_entry(i, f"file_{i}.txt") for i in range(50)]
    assert BinderHashTable.build_hash_table(entries) == BinderHashTable.build_hash_table(entries)
    # Changing a path changes the table.
    entries[0].set_path_name("renamed.txt")
    assert BinderHashTable.build_hash_table(entries) != BinderHashTable.build_hash_table(
        [_entry(i, f"file_{i}.txt") for i in range(50)]
    )


# ---------------------------------------------------------------------------
# Real binder files
# ---------------------------------------------------------------------------


def test_ptde_uncompressed_bnd3(tests_dir: Path, tmp_path: Path):
    path = tests_dir / "darksouls1ptde" / "resources" / "GameParam.parambnd"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    binder = Binder.from_path(path)
    assert binder.version == BinderVersion.V3
    assert binder.dcx_type == DCXType.Null
    assert binder.signature == "07D7R6"
    assert len(binder.entries) == 38
    assert binder["EquipParamWeapon.param"].entry_id == 0

    out = tmp_path / "GameParam.parambnd"
    binder.write(out)
    reloaded = Binder.from_path(out)
    assert len(reloaded.entries) == len(binder.entries)
    for a, b in zip(binder.entries, reloaded.entries):
        assert (a.entry_id, a.path, a.data) == (b.entry_id, b.path, b.data)
    # Repacking the reloaded binder is byte-stable.
    assert bytes(reloaded) == bytes(binder)


def test_ptde_bnd3_byte_perfect(tests_dir: Path):
    path = tests_dir / "darksouls1ptde" / "resources" / "GameParam.parambnd"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    binder = Binder.from_path(path)
    assert bytes(binder) == path.read_bytes()


def test_dsr_dcx_bnd3(tests_dir: Path, tmp_path: Path):
    path = tests_dir / "darksouls1r" / "resources" / "GameParam.parambnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    binder = Binder.from_path(path)
    assert binder.version == BinderVersion.V3
    assert binder.dcx_type == DCXType.DCX_DFLT_10000_24_9
    assert len(binder.entries) == 41

    out = tmp_path / "GameParam.parambnd"  # `.dcx` appended automatically
    written = binder.write(out)
    assert written == [tmp_path / "GameParam.parambnd.dcx"]
    reloaded = Binder.from_path(tmp_path / "GameParam.parambnd.dcx")
    assert reloaded.dcx_type == DCXType.DCX_DFLT_10000_24_9
    for a, b in zip(binder.entries, reloaded.entries):
        assert (a.entry_id, a.path, a.data) == (b.entry_id, b.path, b.data)


def test_bloodborne_bnd4(tests_dir: Path):
    path = tests_dir / "bloodborne" / "resources" / "gameparam.parambnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    binder = Binder.from_path(path)
    assert binder.version == BinderVersion.V4
    assert binder.dcx_type == DCXType.DCX_DFLT_10000_44_9
    assert binder.v4_info is not None
    reloaded = Binder.from_bytes(bytes(binder))
    assert len(reloaded.entries) == len(binder.entries)
    for a, b in zip(binder.entries, reloaded.entries):
        assert (a.entry_id, a.path, a.data) == (b.entry_id, b.path, b.data)


def test_dsr_talkesdbnd_unpacked_directory_roundtrip(tests_dir: Path, tmp_path: Path):
    path = tests_dir / "darksouls1r" / "resources" / "m10_00_00_00.talkesdbnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    binder = Binder.from_path(path)
    directory = tmp_path / "unpacked"
    binder.write_unpacked_directory(directory)
    reloaded = Binder.from_unpacked_path(directory)
    assert reloaded.dcx_type == binder.dcx_type
    assert [(e.entry_id, e.path, e.data) for e in reloaded.entries] == [
        (e.entry_id, e.path, e.data) for e in binder.entries
    ]


@pytest.mark.game_data
def test_dsr_real_bxf3(dsr_root: Path, tmp_path: Path):
    """Real split BHD/BDT pair (map texture binder)."""
    bhd_path = dsr_root / "map" / "m10" / "m10_0000.tpfbhd"
    if not bhd_path.is_file():
        pytest.skip(f"Missing DSR file: {bhd_path}")
    binder = Binder.from_path(bhd_path)
    assert binder.is_split_bxf
    assert binder.version == BinderVersion.V3
    packed_bhd, packed_bdt = binder.get_split_bytes()
    # BHD headers are byte-perfect for BXF3.
    assert packed_bhd == bhd_path.read_bytes()
    reloaded = Binder.from_bytes(packed_bhd, packed_bdt)
    assert len(reloaded.entries) == len(binder.entries)


@pytest.mark.game_data
def test_elden_ring_bnd4_krak(er_root: Path):
    path = er_root / "msg" / "engus" / "ngword.msgbnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing Elden Ring file: {path}")
    binder = Binder.from_path(path)
    assert binder.version == BinderVersion.V4
    assert binder.dcx_type == DCXType.DCX_KRAK
    assert binder.v4_info.unicode
    reloaded = Binder.from_bytes(bytes(binder))
    for a, b in zip(binder.entries, reloaded.entries):
        assert (a.entry_id, a.path, a.data) == (b.entry_id, b.path, b.data)


# ---------------------------------------------------------------------------
# TPF
# ---------------------------------------------------------------------------


def _dummy_dds() -> bytes:
    """Minimal 128-byte DDS header + a little data (not a valid image, but structurally parseable)."""
    return b"DDS " + b"\x7c\x00\x00\x00" + b"\0" * 120 + b"\xAB" * 64


def test_tpf_empty_roundtrip():
    tpf = TPF(dcx_type=DCXType.Null)
    data = bytes(tpf)
    assert data[:4] == b"TPF\0"
    reloaded = TPF.from_bytes(data)
    assert len(reloaded.textures) == 0
    assert reloaded.platform == TPFPlatform.PC


def test_tpf_len_iter_repr():
    tpf = TPF(dcx_type=DCXType.Null, textures=[TPFTexture(stem="a"), TPFTexture(stem="b")])
    assert len(tpf) == 2
    assert [t.stem for t in tpf] == ["a", "b"]
    assert "2 textures" in repr(tpf)
    assert tpf.find_texture_stem("A").stem == "a"
    with pytest.raises(ValueError):
        tpf.find_texture_stem("A", case_sensitive=True)


def test_tpf_platform_byte_order():
    assert TPFPlatform.PC.get_byte_order().name == "LittleEndian"
    assert TPFPlatform.PS3.get_byte_order().name == "BigEndian"
    assert TPFPlatform.Xbox360.get_byte_order().name == "BigEndian"
    assert TPFPlatform.PS4.get_byte_order().name == "LittleEndian"


def test_tpf_texture_format_info():
    assert TPFTexture.get_texture_format_info(0) == (b"DXT1", 8, True)
    assert TPFTexture.get_texture_format_info(5) == (b"DXT5", 16, True)
    assert TPFTexture.get_texture_format_info(102) == (b"DX10", 16, True)
    with pytest.raises(ValueError):
        TPFTexture.get_texture_format_info(9999)


def test_real_tpf_roundtrip(tests_dir: Path, tmp_path: Path):
    path = tests_dir / "darksouls1r" / "resources" / "m10_00_arch_01.tpf.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    tpf = TPF.from_path(path)
    assert tpf.dcx_type == DCXType.DCX_DFLT_10000_24_9
    assert tpf.platform == TPFPlatform.PC
    assert len(tpf.textures) == 1
    assert tpf.textures[0].stem == "m10_00_arch_01"
    assert tpf.textures[0].data[:4] == b"DDS "

    out = tmp_path / "out.tpf"
    tpf.write(out)
    reloaded = TPF.from_path(tmp_path / "out.tpf.dcx")
    assert [t.stem for t in reloaded.textures] == [t.stem for t in tpf.textures]
    assert [t.data for t in reloaded.textures] == [t.data for t in tpf.textures]
    # Second write is byte-stable.
    assert bytes(reloaded) == bytes(TPF.from_bytes(bytes(reloaded)))


@pytest.mark.xfail(
    reason="BUG: `TPFTexture.to_tpf_writer()` recomputes `mipmap_count` (and `texture_type`) from the DDS "
           "header for PC TPFs instead of preserving the value stored in the TPF. Vanilla files that store 0 "
           "('all mipmaps') are silently rewritten with the real count, so the first pack is not faithful.",
    strict=False,
)
def test_tpf_preserves_mipmap_count(tests_dir: Path):
    path = tests_dir / "darksouls1r" / "resources" / "m10_00_arch_01.tpf.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    tpf = TPF.from_path(path)
    original_mipmap_counts = [t.mipmap_count for t in tpf.textures]
    reloaded = TPF.from_bytes(bytes(tpf))
    assert [t.mipmap_count for t in reloaded.textures] == original_mipmap_counts


def test_tpf_unpacked_directory_roundtrip(tests_dir: Path, tmp_path: Path):
    path = tests_dir / "darksouls1r" / "resources" / "m10_00_arch_01.tpf.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    tpf = TPF.from_path(path)
    directory = tmp_path / "tpf.unpacked"
    tpf.write_unpacked_directory(directory)
    assert (directory / "tpf_manifest.json").is_file()
    reloaded = TPF.from_unpacked_path(directory)
    assert reloaded.dcx_type == tpf.dcx_type
    assert [t.stem for t in reloaded.textures] == [t.stem for t in tpf.textures]
    assert [t.data for t in reloaded.textures] == [t.data for t in tpf.textures]


def test_tpf_unpacked_directory_preserves_console_info(tmp_path: Path):
    texture = TPFTexture(
        stem="console_tex",
        format=0,
        texture_type=TextureType.Texture,
        mipmap_count=1,
        texture_flags=0,
        data=_dummy_dds(),
        console_info=TPFTexture.ConsoleInfo(width=64, height=64, texture_count=1, unk1=0, unk2=0xD),
    )
    tpf = TPF(dcx_type=DCXType.Null, platform=TPFPlatform.PS4, textures=[texture])
    directory = tmp_path / "console.tpf.unpacked"
    tpf.write_unpacked_directory(directory)
    reloaded = TPF.from_unpacked_path(directory)
    assert reloaded.textures[0].console_info is not None
    assert reloaded.textures[0].console_info.width == 64


def test_tpf_json_header_with_default_dcx_type():
    TPF().get_json_header()
