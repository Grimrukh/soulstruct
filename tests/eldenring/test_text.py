"""Tests for Elden Ring text (`soulstruct.eldenring.text`).

`MSGDirectory` loads `msg/<lang>/item.msgbnd.dcx` and `menu.msgbnd.dcx` simultaneously and exposes
each FMG through a `fmg_property("item"|"menu", entry_id)` class property named after a Soulstruct
'category' (e.g. `WeaponDescriptions`). The category name -> (binder, entry ID) mapping is duplicated
three ways -- `DEFAULT_ENTRY_STEMS`, the properties themselves, and `MAIN_CATEGORIES` /
`INTERNAL_CATEGORIES` -- so most of these tests check that those three agree.
"""
from __future__ import annotations

import pytest

from soulstruct.base.text.fmg import FMG
from soulstruct.eldenring.text import MSGDirectory
from soulstruct.eldenring.text.msgbnd import MSGBND


def _property_keys() -> dict[str, tuple[str, int]]:
    """Map each `MSGDirectory` category property name to its ('item'|'menu', entry_id) key."""
    keys = {}
    for name, value in vars(MSGDirectory).items():
        if not isinstance(value, property):
            continue
        cells = [cell.cell_contents for cell in value.fget.__closure__]
        msgbnd_name = next(c for c in cells if isinstance(c, str))
        entry_id = next(c for c in cells if isinstance(c, int))
        keys[name] = (msgbnd_name, entry_id)
    return keys


# ---------------------------------------------------------------------------
# Class configuration (pure unit)
# ---------------------------------------------------------------------------


def test_msgbnd_class_defaults():
    from soulstruct.containers import BinderVersion

    assert MSGBND.DEFAULT_ENTRY_ROOT == "N:\\GR\\data\\INTERROOT_win64\\msg\\engUS"
    assert MSGBND.IS_SPLIT_BXF is False
    bnd = MSGBND()
    assert bnd.version == BinderVersion.V4


def test_msg_directory_file_class():
    assert MSGDirectory.FILE_CLASS is MSGBND
    assert MSGDirectory.FILE_EXTENSION == ".msgbnd"


def test_every_property_has_a_default_entry_stem():
    keys = _property_keys()
    assert len(keys) > 40
    missing = {name: key for name, key in keys.items() if key not in MSGDirectory.DEFAULT_ENTRY_STEMS}
    assert not missing, f"Properties with no `DEFAULT_ENTRY_STEMS` entry: {missing}"


def test_every_default_entry_stem_has_a_property():
    keys = set(_property_keys().values())
    missing = [k for k in MSGDirectory.DEFAULT_ENTRY_STEMS if k not in keys]
    assert not missing, f"`DEFAULT_ENTRY_STEMS` entries with no property: {missing}"


def test_property_entry_ids_are_unique():
    keys = list(_property_keys().values())
    assert len(keys) == len(set(keys)), "Two `MSGDirectory` properties map to the same MSGBND entry."


def test_default_entry_stems_are_unique_per_binder():
    seen = {}
    for (msgbnd_name, entry_id), stem in MSGDirectory.DEFAULT_ENTRY_STEMS.items():
        key = (msgbnd_name, stem)
        assert key not in seen, f"Repeated entry stem {stem!r} in '{msgbnd_name}' MSGBND."
        seen[key] = entry_id


def test_main_and_internal_categories_do_not_overlap():
    assert not set(MSGDirectory.MAIN_CATEGORIES) & set(MSGDirectory.INTERNAL_CATEGORIES)


def test_all_categories_alias():
    assert MSGDirectory.ALL_CATEGORIES == MSGDirectory.MAIN_CATEGORIES + MSGDirectory.INTERNAL_CATEGORIES
    assert MSGDirectory.ALL_FMG_NAMES == MSGDirectory.ALL_CATEGORIES
    assert MSGDirectory.GET_ALL_CATEGORIES() == MSGDirectory.ALL_CATEGORIES


@pytest.mark.xfail(
    reason="BUG: `INTERNAL_CATEGORIES` lists 'SystemMessagesWin64' but the property is called "
           "'SystemMessageWin64' (already in `MAIN_CATEGORIES`), and the `MenuText` property "
           "(menu 200 / GR_MenuText) is missing from the category tuples entirely.",
    strict=False,
)
def test_categories_match_properties_exactly():
    props = set(_property_keys())
    cats = set(MSGDirectory.ALL_CATEGORIES)
    assert cats - props == set(), f"Categories with no property: {sorted(cats - props)}"
    assert props - cats == set(), f"Properties with no category: {sorted(props - cats)}"


@pytest.mark.xfail(
    reason="BUG: `MSGDirectory.resolve_item_type` (base class, not overridden for ER) maps 'good'->'Good' "
           "and 'accessory'->'Ring', but Elden Ring's categories are 'Goods*' and 'Accessory*'. "
           "`get_item_fmgs`/`get_all_item_text`/`set_item_text` therefore only work for weapons and armor.",
    strict=False,
)
def test_resolve_item_type_matches_er_categories():
    cats = set(MSGDirectory.ALL_CATEGORIES)
    for item_type in ("weapon", "armor", "good", "accessory"):
        resolved = MSGDirectory.resolve_item_type(item_type)
        for suffix in ("Names", "Summaries", "Descriptions"):
            assert f"{resolved}{suffix}" in cats, f"'{item_type}' -> '{resolved}{suffix}' is not an ER category."


# ---------------------------------------------------------------------------
# Live game data
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def er_msg_directory(er_root):
    """`MSGDirectory` loaded from the installed game's English message folder."""
    msg_dir = er_root / "msg" / "engUS"
    if not msg_dir.is_dir():
        pytest.skip(f"No Elden Ring message directory at {msg_dir}.")
    return MSGDirectory.from_path(msg_dir)


@pytest.mark.slow
def test_load_live_msg_directory(er_msg_directory):
    assert set(er_msg_directory.files) == {"item", "menu"}
    assert len(er_msg_directory.fmgs) > 30
    for key, fmg in er_msg_directory.fmgs.items():
        assert isinstance(fmg, FMG), key


@pytest.mark.slow
def test_live_fmg_properties_resolve(er_msg_directory):
    """Every declared property must map to an FMG actually present in the vanilla MSGBNDs."""
    missing = []
    for name in _property_keys():
        try:
            getattr(er_msg_directory, name)
        except KeyError:
            missing.append(name)
    assert not missing, f"Properties that do not resolve against vanilla ER MSGBNDs: {missing}"


@pytest.mark.slow
def test_live_weapon_names_contain_known_string(er_msg_directory):
    names = er_msg_directory.WeaponNames
    assert len(names.entries) > 100
    assert any("Sword" in s for s in names.entries.values())


@pytest.mark.slow
def test_live_fmg_json_roundtrip(er_msg_directory, tmp_path):
    """FMG -> JSON -> FMG must preserve all entries."""
    fmg = er_msg_directory.WeaponNames
    json_path = tmp_path / "WeaponNames.json"
    fmg.write_json(json_path, encoding="utf-8")
    reloaded = FMG.from_json(json_path)
    assert reloaded.entries == fmg.entries


@pytest.mark.slow
def test_live_fmg_binary_roundtrip(er_msg_directory):
    """FMG unpack -> pack -> unpack must be stable."""
    fmg = er_msg_directory.WeaponNames
    packed = bytes(fmg)
    reloaded = FMG.from_bytes(packed)
    assert reloaded.entries == fmg.entries
    assert bytes(reloaded) == packed


@pytest.mark.slow
def test_live_msgbnd_regenerate_and_write(er_msg_directory, tmp_path):
    """`write()` regenerates both MSGBNDs from `fmgs` and must reload identically."""
    written = er_msg_directory.write(tmp_path)
    assert len(written) == 2
    reloaded = MSGDirectory.from_path(tmp_path)
    assert set(reloaded.fmgs) == set(er_msg_directory.fmgs)
    for key, fmg in er_msg_directory.fmgs.items():
        assert reloaded.fmgs[key].entries == fmg.entries, key


@pytest.mark.slow
def test_live_json_directory_roundtrip(er_msg_directory, tmp_path):
    """`write_json_directory()` -> `from_json_directory()` must preserve all FMGs."""
    er_msg_directory.write_json_directory(tmp_path)
    assert (tmp_path / "item_msgbnd_manifest.json").is_file()
    assert (tmp_path / "menu_msgbnd_manifest.json").is_file()
    reloaded = MSGDirectory.from_json_directory(tmp_path)
    assert set(reloaded.fmgs) == set(er_msg_directory.fmgs)
    for key, fmg in er_msg_directory.fmgs.items():
        assert reloaded.fmgs[key].entries == fmg.entries, key


@pytest.mark.slow
def test_live_get_item_fmgs_for_weapons(er_msg_directory):
    fmgs = er_msg_directory.get_item_fmgs("weapon")
    assert set(fmgs) == {"Names", "Summaries", "Descriptions"}


@pytest.mark.slow
@pytest.mark.xfail(
    reason="BUG: same `resolve_item_type` mismatch - 'good' resolves to category prefix 'Good', but ER "
           "uses 'Goods*'. Raises `KeyError`.",
    strict=False,
)
def test_live_get_item_fmgs_for_goods(er_msg_directory):
    fmgs = er_msg_directory.get_item_fmgs("good")
    assert set(fmgs) == {"Names", "Summaries", "Descriptions"}
