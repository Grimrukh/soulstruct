"""Bloodborne text (`MSGDirectory` / `MSGBND` / `FMG`) tests.

No vanilla `item.msgbnd`/`menu.msgbnd` is committed, so the game-data test skips unless Bloodborne is
installed. Everything else is a pure-unit consistency check of the category <-> FMG-entry-ID mapping,
which is exactly where copy-paste errors from the DS1/DS3 packages show up.
"""
from __future__ import annotations

import pytest

from soulstruct.bloodborne.text import MSGBND, MSGDirectory
from soulstruct.base.text.fmg import FMG
from soulstruct.dcx import DCXType
from soulstruct.games import BLOODBORNE


def _fmg_properties() -> dict[str, tuple[str, int]]:
    """Map category name -> ('item'|'menu', entry_id) captured by `fmg_property`."""
    properties = {}
    for name, value in vars(MSGDirectory).items():
        if not isinstance(value, property) or value.fget is None or not value.fget.__closure__:
            continue
        cells = [cell.cell_contents for cell in value.fget.__closure__]
        source = next((c for c in cells if isinstance(c, str)), None)
        entry_id = next((c for c in cells if isinstance(c, int)), None)
        if source is not None and entry_id is not None:
            properties[name] = (source, entry_id)
    return properties


# ---------------------------------------------------------------------------
# MSGBND wiring
# ---------------------------------------------------------------------------


def test_msgbnd_defaults():
    assert MSGBND.IS_SPLIT_BXF is False
    assert MSGBND()._get_dcx_type() == DCXType.DCX_DFLT_10000_44_9
    assert MSGDirectory.FILE_CLASS is MSGBND
    assert MSGDirectory.FILE_EXTENSION == ".msgbnd"


def test_msgbnd_entry_root_uses_bloodborne_interroot():
    assert MSGBND.DEFAULT_ENTRY_ROOT.startswith(BLOODBORNE.interroot_prefix)


@pytest.mark.xfail(
    reason="`MSGBND.DEFAULT_ENTRY_ROOT` ends in '\\\\msg\\\\engUS\\\\64bit'. Bloodborne is PS4-only, so the "
           "'64bit' component (and the 'engUS' casing) look copied from the PC DS3 package; the game's own "
           "entry paths do not use a '64bit' folder.",
    strict=False,
)
def test_msgbnd_entry_root_has_no_pc_only_folder():
    assert "64bit" not in MSGBND.DEFAULT_ENTRY_ROOT, MSGBND.DEFAULT_ENTRY_ROOT


def test_fmg_dcx_type_is_null():
    """FMGs live inside the MSGBND and are not individually compressed."""
    assert MSGDirectory.FMG_DCX_TYPE == DCXType.Null


def test_no_base_patch_fmgs():
    """Unlike DS1, Bloodborne has no 'patch' FMG duplicates."""
    assert MSGDirectory.BASE_PATCH_FMGS == {}


# ---------------------------------------------------------------------------
# Category <-> FMG entry ID mapping
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    reason="`INTERNAL_CATEGORIES` lists 'FeatureNames', 'FeatureSummaries', 'FeatureDescriptions' and "
           "'ContextualHelp', copied from the DS1 package, but Bloodborne's `MSGDirectory` defines no "
           "`fmg_property` for any of them, so `getattr(text, category)` raises `AttributeError`.",
    strict=False,
)
def test_all_categories_have_properties():
    """Every name in MAIN/INTERNAL categories must be backed by an `fmg_property`."""
    properties = set(_fmg_properties())
    missing = sorted(set(MSGDirectory.GET_ALL_CATEGORIES()) - properties)
    assert not missing, f"Declared categories with no `fmg_property`: {missing}"


def test_all_properties_are_declared_categories():
    declared = set(MSGDirectory.GET_ALL_CATEGORIES())
    extra = sorted(set(_fmg_properties()) - declared)
    assert not extra, f"`fmg_property` attributes not listed in MAIN/INTERNAL categories: {extra}"


def test_categories_have_no_duplicates():
    all_categories = MSGDirectory.GET_ALL_CATEGORIES()
    assert len(set(all_categories)) == len(all_categories)
    assert not set(MSGDirectory.MAIN_CATEGORIES) & set(MSGDirectory.INTERNAL_CATEGORIES)


def test_every_property_entry_id_is_a_known_stem():
    """Each `fmg_property(source, entry_id)` must have a `DEFAULT_ENTRY_STEMS` entry, or FMG JSON I/O breaks."""
    unknown = [
        f"{name} -> {key}"
        for name, key in _fmg_properties().items()
        if key not in MSGDirectory.DEFAULT_ENTRY_STEMS
    ]
    assert not unknown, f"Categories with no `DEFAULT_ENTRY_STEMS` entry: {unknown}"


@pytest.mark.xfail(
    reason="MSGBND entry ('item', 29) -- '魔法うんちく' (spell descriptions) -- has a "
           "`DEFAULT_ENTRY_STEMS` entry but no `fmg_property`, because `SpellDescriptions` wrongly points at "
           "entry 27. That FMG is unreachable and `write_json_directory()` would raise `IndexError` on it.",
    strict=False,
)
def test_every_default_entry_stem_has_a_category():
    """Each MSGBND entry must map to exactly one Soulstruct category name.

    `write_json_directory()` does a reverse lookup (`[key for key, fmg in ... if fmg is fmg][0]`), so an
    unmapped entry ID would raise `IndexError` at write time.
    """
    used_keys = set(_fmg_properties().values())
    unmapped = sorted(key for key in MSGDirectory.DEFAULT_ENTRY_STEMS if key not in used_keys)
    assert not unmapped, f"MSGBND entry IDs with no Soulstruct category: {unmapped}"


@pytest.mark.xfail(
    reason="`SpellDescriptions = fmg_property(\"item\", 27)` duplicates `AccessoryDescriptions`. Entry 27 is "
           "'アクセサリうんちく' (accessory description); spell descriptions are entry 29 ('魔法うんちく'), which "
           "DS1 maps correctly. Two categories therefore alias one FMG and entry 29 is unreachable.",
    strict=False,
)
def test_no_two_categories_share_an_fmg_entry():
    properties = _fmg_properties()
    seen: dict[tuple[str, int], str] = {}
    collisions = []
    for name, key in sorted(properties.items()):
        if key in seen:
            collisions.append(f"{seen[key]} and {name} both map to {key}")
        else:
            seen[key] = name
    assert not collisions, collisions


def test_known_bloodborne_categories_map_to_expected_entries():
    """Spot-check Bloodborne-specific 'Blood Gem' FMGs (menu 31-35), which DS1/DS3 do not have."""
    properties = _fmg_properties()
    assert properties["BloodGemNames"] == ("menu", 31)
    assert properties["BloodGemSummaries"] == ("menu", 32)
    assert properties["BloodGemDescriptions"] == ("menu", 33)
    assert properties["BloodGemPrefixes"] == ("menu", 34)
    assert properties["BloodGemEffects"] == ("menu", 35)


def test_item_entries_use_item_msgbnd_and_menu_entries_use_menu():
    for name, (source, entry_id) in _fmg_properties().items():
        assert source in {"item", "menu"}, f"{name} has unknown MSGBND source '{source}'."


# ---------------------------------------------------------------------------
# FMG round-trip (pure unit)
# ---------------------------------------------------------------------------


def test_fmg_json_roundtrip(tmp_path):
    """FMG JSON round-trip using a synthetic Bloodborne-style FMG."""
    fmg = FMG(entries={100: "Saw Cleaver", 200: "Hunter Axe", 300: ""})
    fmg.dcx_type = MSGDirectory.FMG_DCX_TYPE
    json_path = tmp_path / "WeaponNames.json"
    fmg.write_json(json_path, encoding="utf-8")
    reloaded = FMG.from_json(json_path)
    assert reloaded.entries == fmg.entries


def test_fmg_binary_roundtrip(tmp_path):
    fmg = FMG(entries={100: "Saw Cleaver", 200: "Hunter Axe"})
    fmg.dcx_type = DCXType.Null
    packed = bytes(fmg)
    reloaded = FMG.from_bytes(packed)
    assert reloaded.entries == fmg.entries
    assert bytes(reloaded) == packed


# ---------------------------------------------------------------------------
# Game data (skipped unless Bloodborne is installed)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
@pytest.mark.slow
def test_vanilla_msg_directory(bb_root, tmp_path):
    msg_dir = bb_root / "msg/engus"
    if not msg_dir.is_dir():
        pytest.skip(f"Missing Bloodborne msg directory: {msg_dir}")
    text = MSGDirectory.from_path(msg_dir)
    assert text.WeaponNames
    # Every declared category must resolve on a real vanilla install.
    for category in MSGDirectory.GET_ALL_CATEGORIES():
        assert getattr(text, category) is not None, f"Category '{category}' missing from vanilla MSGBNDs."
    text.write_json_directory(tmp_path / "text_json")
    reloaded = MSGDirectory.from_json_directory(tmp_path / "text_json")
    assert reloaded.WeaponNames.entries == text.WeaponNames.entries
