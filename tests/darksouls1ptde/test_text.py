"""Tests for DS1 PTDE text (FMG / MSGBND / MSGDirectory).

DS1 uses the oldest FMG version (`version == 1`, big-endian-free, 32-bit offsets) and, uniquely for
PTDE, keeps ALL 'patch' (DLC) FMGs in `menu.msgbnd` -- in DSR the item patch FMGs moved into
`item.msgbnd.dcx`. PTDE MSGBNDs are also uncompressed.
"""
from __future__ import annotations

import logging

import pytest

from soulstruct.darksouls1ptde.text import FMG, MSGDirectory
from soulstruct.darksouls1ptde.text.msgbnd import MSGBND
from soulstruct.dcx import DCXType


# ---------------------------------------------------------------------------
# Pure-unit: class table consistency
# ---------------------------------------------------------------------------


def test_msgbnd_is_uncompressed():
    from soulstruct.games import DARK_SOULS_PTDE

    assert DARK_SOULS_PTDE.default_dcx_type == DCXType.Null
    assert MSGBND()._get_dcx_type() == DCXType.Null
    assert MSGDirectory.FILE_CLASS is MSGBND
    assert MSGDirectory.FMG_DCX_TYPE == DCXType.Null


def test_default_entry_stems_are_unique():
    stems = list(MSGDirectory.DEFAULT_ENTRY_STEMS.values())
    assert len(stems) == len(set(stems)), "Duplicate FMG entry stem in `DEFAULT_ENTRY_STEMS`."
    keys = list(MSGDirectory.DEFAULT_ENTRY_STEMS)
    assert len(keys) == len(set(keys))
    for msgbnd_name, entry_id in keys:
        assert msgbnd_name in {"item", "menu"}
        assert isinstance(entry_id, int)


def test_base_patch_fmgs_reference_known_entries():
    for base_key, patch_key in MSGDirectory.BASE_PATCH_FMGS.items():
        assert base_key in MSGDirectory.DEFAULT_ENTRY_STEMS, f"Unknown base FMG: {base_key}"
        assert patch_key in MSGDirectory.DEFAULT_ENTRY_STEMS, f"Unknown patch FMG: {patch_key}"
        assert base_key != patch_key


def test_all_ptde_patch_fmgs_live_in_menu_msgbnd():
    """PTDE quirk (differs from DSR): every patch FMG is in `menu.msgbnd`."""
    for base_key, (patch_msgbnd, _) in MSGDirectory.BASE_PATCH_FMGS.items():
        assert patch_msgbnd == "menu", f"{base_key} patch should be in `menu.msgbnd` for PTDE."


def test_base_patch_map_is_injective():
    patch_keys = list(MSGDirectory.BASE_PATCH_FMGS.values())
    assert len(patch_keys) == len(set(patch_keys)), "Two base FMGs share a patch FMG."


def test_every_category_has_an_fmg_property():
    for category in MSGDirectory.GET_ALL_CATEGORIES():
        assert isinstance(getattr(MSGDirectory, category, None), property), (
            f"`MSGDirectory.{category}` property missing (declared in MAIN/INTERNAL_CATEGORIES)."
        )


def test_categories_do_not_overlap():
    main = set(MSGDirectory.MAIN_CATEGORIES)
    internal = set(MSGDirectory.INTERNAL_CATEGORIES)
    assert not (main & internal), f"Categories in both MAIN and INTERNAL: {main & internal}"
    assert len(MSGDirectory.MAIN_CATEGORIES) == len(main)
    assert len(MSGDirectory.INTERNAL_CATEGORIES) == len(internal)


def test_every_fmg_property_targets_a_known_entry():
    """Every `fmg_property` on the class must point at a `DEFAULT_ENTRY_STEMS` key."""
    import inspect

    targets = set()
    for name, value in vars(MSGDirectory).items():
        if not isinstance(value, property) or value.fget is None:
            continue
        closure = inspect.getclosurevars(value.fget).nonlocals
        if "msgbnd_name" in closure and "bnd_index" in closure:
            key = (closure["msgbnd_name"], closure["bnd_index"])
            assert key in MSGDirectory.DEFAULT_ENTRY_STEMS, (
                f"`MSGDirectory.{name}` targets unknown FMG {key}."
            )
            targets.add(key)
    assert targets, "No `fmg_property` getters found (test is broken)."
    # Every declared FMG entry should be reachable through some property.
    unreachable = set(MSGDirectory.DEFAULT_ENTRY_STEMS) - targets
    assert not unreachable, f"FMG entries with no `fmg_property`: {sorted(unreachable)}"


def test_patch_properties_follow_naming_convention():
    for base_key, patch_key in MSGDirectory.BASE_PATCH_FMGS.items():
        # Find the property name for the base FMG, then assert `<Name>Patch` exists.
        import inspect

        base_name = None
        for name, value in vars(MSGDirectory).items():
            if not isinstance(value, property) or value.fget is None:
                continue
            closure = inspect.getclosurevars(value.fget).nonlocals
            if (closure.get("msgbnd_name"), closure.get("bnd_index")) == base_key:
                base_name = name
                break
        assert base_name is not None, f"No property for base FMG {base_key}."
        assert hasattr(MSGDirectory, f"{base_name}Patch"), (
            f"`MSGDirectory.{base_name}Patch` missing for base FMG {base_key}."
        )


# ---------------------------------------------------------------------------
# Vanilla game data
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def msg_dir(ptde_root):
    path = ptde_root / "msg" / "ENGLISH"
    if not path.is_dir():
        pytest.skip(f"Missing PTDE msg/ENGLISH directory: {path}")
    return path


@pytest.fixture(scope="module")
def msg_directory(msg_dir) -> MSGDirectory:
    return MSGDirectory.from_path(msg_dir)


def test_vanilla_msgbnds_are_not_dcx(msg_dir):
    assert (msg_dir / "item.msgbnd").is_file()
    assert (msg_dir / "menu.msgbnd").is_file()
    assert not (msg_dir / "item.msgbnd.dcx").is_file(), "PTDE MSGBNDs must not be DCX."


def test_msg_directory_loads_all_declared_fmgs(msg_directory):
    assert set(msg_directory.fmgs) == set(MSGDirectory.DEFAULT_ENTRY_STEMS)
    for key, fmg in msg_directory.fmgs.items():
        assert isinstance(fmg, FMG), f"{key} is not an FMG."


def test_ds1_fmg_uses_old_version(msg_directory):
    """DS1 uses FMG version 1 (later games use 2, Elden Ring uses 3)."""
    for key, fmg in msg_directory.fmgs.items():
        assert fmg.version == 1, f"{key}: expected FMG version 1, got {fmg.version}."


def test_msg_directory_category_properties(msg_directory):
    weapon_names = msg_directory.WeaponNames
    assert weapon_names is msg_directory.fmgs[("item", 11)]
    # Dagger is weapon 100000 in vanilla DS1.
    assert weapon_names.entries.get(100000), "WeaponNames should contain the Dagger (ID 100000)."
    assert msg_directory.WeaponNamesPatch is msg_directory.fmgs[("menu", 115)]
    assert msg_directory["WeaponNames"] is weapon_names


def test_msg_directory_binary_round_trip(msg_directory, tmp_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        msg_directory.write(tmp_path)
        reloaded = MSGDirectory.from_path(tmp_path)
    assert set(reloaded.fmgs) == set(msg_directory.fmgs)
    for key, fmg in msg_directory.fmgs.items():
        assert reloaded.fmgs[key].entries == fmg.entries, f"{key}: FMG entries changed."
        assert reloaded.fmgs[key].version == fmg.version


def test_msgbnd_entry_paths_survive_regeneration(msg_directory, caplog):
    """`regenerate_binders()` must not invent new entries or rewrite existing entry paths."""
    before = {
        name: [(entry.entry_id, entry.path) for entry in binder.entries]
        for name, binder in msg_directory.files.items()
    }
    with caplog.at_level(logging.CRITICAL):
        msg_directory.regenerate_binders()
    after = {
        name: [(entry.entry_id, entry.path) for entry in binder.entries]
        for name, binder in msg_directory.files.items()
    }
    assert before == after


@pytest.mark.xfail(
    reason=(
        "`MSGBND.DEFAULT_ENTRY_ROOT` is "
        "'N:\\FRPG\\data\\INTERROOT_win32\\Msb\\Data_ENGLISH\\win32', but vanilla PTDE FMG entries "
        "live at 'N:\\FRPG\\data\\Msg\\Data_ENGLISH\\win32' ('Msg', and no INTERROOT component). "
        "Only newly-added FMG entries are affected, but they would be written to a bogus path."
    ),
    strict=False,
)
def test_msgbnd_default_entry_root_matches_vanilla(msg_directory):
    roots = {
        entry.path.rsplit("\\", 1)[0]
        for binder in msg_directory.files.values()
        for entry in binder.entries
    }
    assert len(roots) == 1, f"Mixed FMG entry roots: {roots}"
    assert MSGBND.DEFAULT_ENTRY_ROOT == next(iter(roots))


def test_msg_directory_json_round_trip(msg_directory, tmp_path, caplog):
    with caplog.at_level(logging.CRITICAL):
        msg_directory.write_json_directory(tmp_path / "json")
        reloaded = MSGDirectory.from_json_directory(tmp_path / "json")
    assert set(reloaded.fmgs) == set(msg_directory.fmgs)
    for key, fmg in msg_directory.fmgs.items():
        assert reloaded.fmgs[key].entries == fmg.entries, f"{key}: FMG entries changed via JSON."


def test_fmg_binary_round_trip(msg_directory, tmp_path):
    fmg = msg_directory.WeaponNames
    path = tmp_path / "weapon_names.fmg"
    fmg.write(path)
    reloaded = FMG.from_path(path)
    assert reloaded.entries == fmg.entries
    assert reloaded.version == fmg.version
    assert bytes(reloaded) == bytes(fmg)


def test_get_matching_fmgs_is_unanchored(msg_directory):
    """Documents the root cause of the `get_item_fmgs` bug below: `re.match` is not anchored at the
    end, so 'Weapon(Names|Summaries|Descriptions)' also matches the three `...Patch` properties."""
    import re

    matches = msg_directory.get_matching_fmgs(re.compile(r"Weapon(Names|Summaries|Descriptions)"))
    assert set(matches) == {
        "WeaponNames", "WeaponSummaries", "WeaponDescriptions",
        "WeaponNamesPatch", "WeaponSummariesPatch", "WeaponDescriptionsPatch",
    }


@pytest.mark.xfail(
    reason=(
        "`MSGDirectory.get_item_fmgs()` builds an unanchored regex "
        "'{type}(Names|Summaries|Descriptions)' and requires exactly 3 matches, but the '...Patch' "
        "properties also match, giving 6 -> `KeyError`. This breaks `get_all_item_text`, "
        "`set_item_text` and `delete_item_text` for every item type."
    ),
    strict=False,
)
def test_get_all_item_text(msg_directory):
    text = msg_directory.get_all_item_text(100000, item_type="weapon")
    assert set(text) >= {"Name", "Summary", "Description"}
    assert text["Name"]


@pytest.mark.xfail(
    reason=(
        "`MSGDirectory.replace_substring_in_all()` iterates `for string_id, string in fmg.entries`, "
        "unpacking dict KEYS (ints) -> `TypeError: cannot unpack non-iterable int object`."
    ),
    strict=False,
)
def test_replace_substring_in_all(msg_directory):
    msg_directory.replace_substring_in_all("WeaponNames", "Sword", "Blade")
