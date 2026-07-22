"""Tests for `soulstruct.base.text`: the `FMG` message format and the `MSGDirectory` manager."""
from __future__ import annotations

import logging
from pathlib import Path

import pytest

from soulstruct.base.text.fmg import FMG, FMGVersion, GAME_MAX_LINES


# ---------------------------------------------------------------------------
# FMG: pure unit tests
# ---------------------------------------------------------------------------


def test_fmg_version_enum():
    assert FMGVersion.V0 == 0  # Demon's Souls
    assert FMGVersion.V1 == 1  # DS1 / DS2
    assert FMGVersion.V2 == 2  # BB / DS3 / Sekiro / ER
    assert set(FMG.HEADER_VERSIONS) == {FMGVersion.V0, FMGVersion.V1, FMGVersion.V2}


def test_fmg_dict_interface():
    fmg = FMG(entries={3: "c", 1: "a"}, version=1)
    assert fmg[1] == "a"
    assert fmg.get(99) is None
    assert fmg.get(99, "x") == "x"
    fmg[2] = "b"
    assert fmg[2] == "b"
    assert fmg.setdefault(2, "zzz") == "b"
    assert fmg.setdefault(5, "e") == "e"
    assert sorted(fmg.keys()) == [1, 2, 3, 5]
    assert set(fmg.values()) == {"a", "b", "c", "e"}
    assert dict(fmg.items())[3] == "c"
    assert sorted(iter(fmg)) == [1, 2, 3, 5]
    assert fmg.pop(5) == "e"
    assert fmg.pop(1234) is None  # never raises
    assert "FMG Path" in repr(fmg)


def test_fmg_sort():
    fmg = FMG(entries={3: "c", 1: "a", 2: "b"}, version=1)
    fmg.sort()
    assert list(fmg.entries) == [1, 2, 3]


def test_fmg_update():
    fmg = FMG(entries={1: "a"}, version=1)
    fmg.update({2: "b"})
    assert fmg[2] == "b"
    fmg.update(FMG(entries={3: "c"}, version=1))
    assert fmg[3] == "c"
    with pytest.raises(TypeError):
        fmg.update("nope")


def test_fmg_remove_empty_strings_returns_copy():
    fmg = FMG(entries={1: "a", 2: "", 3: "c"}, version=1)
    trimmed = fmg.remove_empty_strings()
    assert trimmed is not fmg
    assert trimmed.entries == {1: "a", 3: "c"}
    assert fmg.entries == {1: "a", 2: "", 3: "c"}  # original untouched
    assert trimmed.version == fmg.version


def test_fmg_apply_line_limits_wraps():
    fmg = FMG(entries={1: "aaa bbb ccc ddd"}, version=1)
    wrapped = fmg.apply_line_limits(max_chars_per_line=7, max_lines=99)
    assert wrapped is not fmg
    assert wrapped[1] == "aaa bbb\nccc ddd"


def test_fmg_apply_line_limits_preserves_paragraphs():
    fmg = FMG(entries={1: "aaa bbb\n\nccc ddd"}, version=1)
    wrapped = fmg.apply_line_limits(max_chars_per_line=3, max_lines=99)
    assert wrapped[1] == "aaa\nbbb\n\nccc\nddd"


def test_fmg_apply_line_limits_leaves_manual_newlines():
    fmg = FMG(entries={1: "aaa bbb\nccc"}, version=1)
    wrapped = fmg.apply_line_limits(max_chars_per_line=3, max_lines=99)
    assert wrapped[1] == "aaa bbb\nccc"  # untouched: already contains a newline


def test_fmg_apply_line_limits_no_wrap():
    fmg = FMG(entries={1: "aaa bbb"}, version=1)
    assert fmg.apply_line_limits(max_chars_per_line=None, max_lines=99)[1] == "aaa bbb"


def test_fmg_apply_line_limits_warns_over_max(caplog):
    fmg = FMG(entries={1: "a b c d e f"}, version=1)
    with caplog.at_level(logging.WARNING):
        fmg.apply_line_limits(max_chars_per_line=1, max_lines=2)
    assert any("has" in r.message and "lines" in r.message for r in caplog.records)


def test_game_max_lines_table():
    assert GAME_MAX_LINES["darksouls1ptde"] == 11
    assert GAME_MAX_LINES["darksouls1r"] == 11


@pytest.mark.xfail(
    reason="M9: `if lines in ['', ' ']` compares a *list* to strings, so the empty/space "
           "short-circuit in `apply_line_limits()` is unreachable.",
    strict=False,
)
def test_fmg_apply_line_limits_space_string_untouched():
    fmg = FMG(entries={1: " "}, version=1)
    assert fmg.apply_line_limits(max_chars_per_line=5, max_lines=99)[1] == " "


@pytest.mark.xfail(
    reason="M8: `FMG.replace_substring_in_all()` iterates `self.entries` (keys) and unpacks pairs.",
    strict=False,
)
def test_fmg_replace_substring_in_all():
    fmg = FMG(entries={1: "abc", 2: "aaa"}, version=1)
    result = fmg.replace_substring_in_all("a", "z")
    assert result.entries == {1: "zbc", 2: "zzz"}


def test_fmg_find_and_replace(capsys):
    fmg = FMG(entries={1: "hello world", 2: "nothing"}, version=1)
    fmg.find("world", replace_with="there")
    out = capsys.readouterr().out
    assert "hello world" in out
    assert fmg[1] == "hello there"
    fmg.find("zzzz")
    assert "Could not find" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# FMG: binary round-trips
# ---------------------------------------------------------------------------


SAMPLE_ENTRIES = {
    1: "hello",
    2: "",  # empty string -> offset 0
    3: "world",
    10: "日本語",  # non-ASCII (UTF-16 in the file)
    11: "multi\nline\ntext",
}


@pytest.mark.parametrize("version", [1, 2])
def test_fmg_binary_roundtrip(version):
    fmg = FMG(entries=dict(SAMPLE_ENTRIES), version=version)
    data = bytes(fmg)
    reloaded = FMG.from_bytes(data)
    assert reloaded.entries == SAMPLE_ENTRIES
    assert reloaded.version == version
    assert bytes(reloaded) == data  # byte-stable


@pytest.mark.parametrize("version", [1, 2])
def test_fmg_empty_roundtrip(version):
    fmg = FMG(entries={}, version=version)
    reloaded = FMG.from_bytes(bytes(fmg))
    assert reloaded.entries == {}


@pytest.mark.parametrize("version", [1, 2])
def test_fmg_single_entry_roundtrip(version):
    fmg = FMG(entries={7: "x"}, version=version)
    assert FMG.from_bytes(bytes(fmg)).entries == {7: "x"}


@pytest.mark.parametrize("version", [1, 2])
def test_fmg_ranges_are_rebuilt(version):
    """Contiguous IDs are merged into ranges; a gap starts a new range."""
    fmg = FMG(entries={1: "a", 2: "b", 3: "c", 100: "d", 101: "e"}, version=version)
    reloaded = FMG.from_bytes(bytes(fmg))
    assert reloaded.entries == fmg.entries
    # Two ranges of 3 and 2 entries -> smaller than five singleton ranges would be.
    contiguous = FMG(entries={i: "a" for i in range(1, 6)}, version=version)
    scattered = FMG(entries={i * 10: "a" for i in range(1, 6)}, version=version)
    assert len(bytes(contiguous)) < len(bytes(scattered))


def test_fmg_negative_and_large_ids_roundtrip():
    fmg = FMG(entries={-5: "neg", 0: "zero", 2 ** 30: "big"}, version=1)
    assert FMG.from_bytes(bytes(fmg)).entries == fmg.entries


def test_fmg_duplicate_strings_roundtrip():
    fmg = FMG(entries={1: "same", 2: "same", 3: "same"}, version=1)
    assert FMG.from_bytes(bytes(fmg)).entries == fmg.entries


def test_fmg_sorts_on_write():
    fmg = FMG(entries={5: "e", 1: "a"}, version=1)
    reloaded = FMG.from_bytes(bytes(fmg))
    assert list(reloaded.entries) == [1, 5]


@pytest.mark.xfail(
    reason="H11: `FMGHeaderV0._minus_one` is declared as an unsigned `byte` with `asserted=-1`, so "
           "packing any Demon's Souls (V0) FMG raises `struct.error`.",
    strict=False,
)
def test_fmg_v0_binary_roundtrip():
    fmg = FMG(entries=dict(SAMPLE_ENTRIES), version=0)
    reloaded = FMG.from_bytes(bytes(fmg))
    assert reloaded.entries == SAMPLE_ENTRIES


# ---------------------------------------------------------------------------
# FMG: JSON round-trips
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("version", [1, 2])
def test_fmg_json_roundtrip(version, tmp_path):
    fmg = FMG(entries=dict(SAMPLE_ENTRIES), version=version)
    fmg.write_json(tmp_path / "fmg.json", encoding="utf-8")
    reloaded = FMG.from_json(tmp_path / "fmg.json")
    assert reloaded.entries == SAMPLE_ENTRIES  # int keys restored from JSON strings
    assert all(isinstance(k, int) for k in reloaded.entries)
    assert bytes(reloaded) == bytes(fmg)


def test_fmg_to_dict_sorts():
    fmg = FMG(entries={5: "e", 1: "a"}, version=1)
    d = fmg.to_dict()
    assert list(d["entries"]) == [1, 5]


# ---------------------------------------------------------------------------
# MSGDirectory (live PTDE install)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def ptde_msg_directory():
    from soulstruct.config import Config
    from soulstruct.darksouls1ptde.text import MSGDirectory

    root = Config.PTDE_PATH
    if not root or not (Path(root) / "msg" / "ENGLISH").is_dir():
        pytest.skip("PTDE `msg/ENGLISH` directory not found (set Config.PTDE_PATH to run).")
    logging.disable(logging.WARNING)
    try:
        return MSGDirectory.from_path(Path(root) / "msg" / "ENGLISH")
    finally:
        logging.disable(logging.NOTSET)


def test_msg_directory_loads(ptde_msg_directory):
    msg = ptde_msg_directory
    assert set(msg.files) == {"item", "menu"}
    assert len(msg.fmgs) > 30
    assert all(isinstance(k, tuple) and k[0] in ("item", "menu") for k in msg.fmgs)


def test_msg_directory_category_properties(ptde_msg_directory):
    msg = ptde_msg_directory
    categories = msg.get_matching_fmgs()
    assert "WeaponNames" in categories
    assert msg["WeaponNames"] is categories["WeaponNames"]
    with pytest.raises(AttributeError):
        _ = msg["NotACategory"]
    assert set(msg.GET_ALL_CATEGORIES()) >= set(msg.MAIN_CATEGORIES)


def test_msg_directory_regex_filter(ptde_msg_directory):
    """NOTE: `get_matching_fmgs` uses `re.match`, i.e. a *prefix* match (see H16)."""
    names = ptde_msg_directory.get_matching_fmgs(r".*Descriptions")
    assert names
    assert all("Descriptions" in n for n in names)
    # Prefix matching also pulls in the DLC "Patch" variants.
    assert any(n.endswith("DescriptionsPatch") for n in names)


def test_msg_directory_merge_base_and_patch(ptde_msg_directory):
    msg = ptde_msg_directory
    assert msg.BASE_PATCH_FMGS, "DS1 defines base->patch FMG pairs"
    base_key, patch_key = next(iter(msg.BASE_PATCH_FMGS.items()))
    msg.fmgs[patch_key][987654] = "patched"
    msg.merge_base_and_patch()
    assert msg.fmgs[base_key][987654] == "patched"
    assert msg.fmgs[patch_key][987654] == "patched"
    msg.fmgs[base_key].pop(987654)
    msg.fmgs[patch_key].pop(987654)


def test_msg_directory_all_fmgs_roundtrip(ptde_msg_directory):
    for key, fmg in ptde_msg_directory.fmgs.items():
        data = bytes(fmg)
        reloaded = FMG.from_bytes(data)
        assert reloaded.entries == fmg.entries, key
        assert bytes(reloaded) == data, key


@pytest.mark.xfail(
    reason="H16: `get_item_fmgs()` filters categories with `re.match` (a prefix match), so DS1's "
           "'...Patch' categories also match and the len==3 check always fails.",
    strict=False,
)
def test_msg_directory_item_text_helpers(ptde_msg_directory):
    msg = ptde_msg_directory
    names = msg.get_item_fmgs("weapon")
    assert set(names) == {"Names", "Summaries", "Descriptions"}
    some_id = next(iter(sorted(names["Names"].keys())))
    text = msg.get_all_item_text(some_id, "weapon")
    assert "name" in text and text["name"] == names["Names"][some_id]
    assert msg.get_all_item_text(-999999, "weapon") == {}


@pytest.mark.parametrize(
    "given, expected",
    [
        ("good", "Good"), ("consumable", "Good"),
        ("ring", "Ring"), ("accessory", "Ring"),
        ("weapon", "Weapon"), ("shield", "Weapon"),
        ("armor", "Armor"), ("armour", "Armor"), ("protector", "Armor"),
    ],
)
def test_msg_directory_resolve_item_type(given, expected):
    from soulstruct.base.text.msg_directory import MSGDirectory

    assert MSGDirectory.resolve_item_type(given) == expected


@pytest.mark.parametrize("given", ["equipment", "item", "bogus"])
def test_msg_directory_resolve_item_type_rejects(given):
    from soulstruct.base.text.msg_directory import MSGDirectory

    with pytest.raises(ValueError):
        MSGDirectory.resolve_item_type(given)


@pytest.mark.xfail(
    reason="H16: `get_item_fmgs()` uses `re.match` (prefix), which also matches '...Patch' categories.",
    strict=False,
)
def test_msg_directory_set_and_delete_item_text(ptde_msg_directory):
    msg = ptde_msg_directory
    new_id = 990001
    msg.set_item_text(new_id, "weapon", "N", "S", "D")
    assert msg.get_all_item_text(new_id, "weapon") == {"name": "N", "summary": "S", "description": "D"}
    with pytest.raises(ValueError):
        msg.set_item_text(new_id, "weapon", "N2", "S2", "D2", allow_override=False)
    msg.delete_item_text(new_id, "weapon")
    assert msg.get_all_item_text(new_id, "weapon") == {}


def test_msg_directory_get_range(ptde_msg_directory):
    pairs = ptde_msg_directory.get_range("WeaponNames", 0, 3)
    assert len(pairs) == 3
    assert all(isinstance(i, int) and isinstance(s, str) for i, s in pairs)


def test_msg_directory_update_from_csv(ptde_msg_directory, tmp_path):
    csv_path = tmp_path / "text.csv"
    csv_path.write_text(
        "category,id,text\nWeaponNames,990002,Test\\nWeapon\n", encoding="utf-8"
    )
    ptde_msg_directory.update_from_csv(csv_path, 0, 1, 2)
    assert ptde_msg_directory["WeaponNames"][990002] == "Test\nWeapon"
    ptde_msg_directory["WeaponNames"].pop(990002)


@pytest.mark.slow
def test_msg_directory_json_directory_roundtrip(ptde_msg_directory, tmp_path):
    from soulstruct.darksouls1ptde.text import MSGDirectory

    ptde_msg_directory.write_json_directory(tmp_path)
    assert (tmp_path / "item_msgbnd_manifest.json").is_file()
    assert (tmp_path / "menu_msgbnd_manifest.json").is_file()
    logging.disable(logging.WARNING)
    try:
        reloaded = MSGDirectory.from_json_directory(tmp_path)
    finally:
        logging.disable(logging.NOTSET)
    assert set(reloaded.fmgs) == set(ptde_msg_directory.fmgs)
    for key, fmg in ptde_msg_directory.fmgs.items():
        assert reloaded.fmgs[key].entries == fmg.entries, key


@pytest.mark.slow
def test_msg_directory_write_and_reload(ptde_msg_directory, tmp_path):
    from soulstruct.darksouls1ptde.text import MSGDirectory

    logging.disable(logging.WARNING)
    try:
        ptde_msg_directory.write(tmp_path)
        reloaded = MSGDirectory.from_path(tmp_path)
    finally:
        logging.disable(logging.NOTSET)
    assert set(reloaded.fmgs) == set(ptde_msg_directory.fmgs)
    for key, fmg in ptde_msg_directory.fmgs.items():
        assert reloaded.fmgs[key].entries == fmg.entries, key


@pytest.mark.xfail(
    reason="M8: `MSGDirectory.replace_substring_in_all()` iterates `fmg.entries` (keys) and unpacks pairs.",
    strict=False,
)
def test_msg_directory_replace_substring_in_all(ptde_msg_directory):
    ptde_msg_directory.replace_substring_in_all(r"WeaponNames", "zzzz-nonexistent", "y")
