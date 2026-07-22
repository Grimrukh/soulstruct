"""Tests for DSR `MSGDirectory` (`msg/<LANGUAGE>/item.msgbnd.dcx` + `menu.msgbnd.dcx`).

DSR text differs from PTDE in two important ways, both encoded in `darksouls1r/text/msg_directory.py`:

    - The item 'patch' (DLC) FMGs live inside `item.msgbnd` rather than `menu.msgbnd`.
    - Patch entries have the *same* Binder entry paths as their base counterparts (a QLOC oversight),
      which is why `MSGBND` needs `use_id_prefix` handling when unpacking to a directory.

`MSGDirectory.fmgs` maps `("item"|"menu", entry_id)` to `FMG`; the many `fmg_property` attributes
(`WeaponNames`, `WeaponNamesPatch`, ...) are the public accessors.
"""
from __future__ import annotations

import pytest

from soulstruct.dcx import DCXType
from soulstruct.darksouls1r.text import FMG, MSGDirectory
from soulstruct.darksouls1r.text.msgbnd import MSGBND
from soulstruct.games import DARK_SOULS_DSR


@pytest.fixture(scope="module")
def dsr_text():
    from pathlib import Path

    from soulstruct.config import Config

    root = Config.DSR_PATH
    if not root or not Path(root).is_dir():
        pytest.skip("Dark Souls: Remastered directory not found.")
    path = Path(root) / "msg/ENGLISH"
    if not path.is_dir():
        pytest.skip(f"Missing DSR text directory: {path}")
    return MSGDirectory.from_path(path)


# ---------------------------------------------------------------------------
# Class configuration (pure unit, no game data)
# ---------------------------------------------------------------------------


def test_msgbnd_class_config():
    assert MSGBND.DEFAULT_ENTRY_ROOT.endswith("\\Msg\\Data_ENGLISH")
    assert MSGBND()._get_dcx_type() == DARK_SOULS_DSR.default_dcx_type
    assert MSGBND()._get_dcx_type() != DCXType.Null, "DSR MSGBNDs are DCX-compressed (unlike PTDE)."
    assert MSGDirectory.FILE_CLASS is MSGBND


def test_categories_are_unique_and_disjoint():
    main = MSGDirectory.MAIN_CATEGORIES
    internal = MSGDirectory.INTERNAL_CATEGORIES
    assert len(set(main)) == len(main)
    assert len(set(internal)) == len(internal)
    assert not set(main) & set(internal), "A category must not be both MAIN and INTERNAL."
    assert set(MSGDirectory.GET_ALL_CATEGORIES()) == set(main) | set(internal)


def test_all_categories_have_fmg_properties():
    missing = [c for c in MSGDirectory.GET_ALL_CATEGORIES() if not isinstance(getattr(MSGDirectory, c, None), property)]
    assert not missing, f"Categories with no `fmg_property`: {missing}"


def test_dsr_item_patch_fmgs_live_in_item_binder():
    """The key DSR-vs-PTDE difference: item patch FMGs are in `item.msgbnd`, not `menu.msgbnd`."""
    for base, patch in MSGDirectory.BASE_PATCH_FMGS.items():
        assert base[0] == patch[0], f"Base {base} and patch {patch} must live in the same MSGBND for DSR."
    item_patches = [p for b, p in MSGDirectory.BASE_PATCH_FMGS.items() if b[0] == "item"]
    assert item_patches and all(source == "item" for source, _ in item_patches)


def test_base_patch_mapping_is_injective_and_declared():
    stems = MSGDirectory.DEFAULT_ENTRY_STEMS
    patches = list(MSGDirectory.BASE_PATCH_FMGS.values())
    assert len(set(patches)) == len(patches), "Two base FMGs map to the same patch FMG."
    for base, patch in MSGDirectory.BASE_PATCH_FMGS.items():
        assert base in stems, f"Base FMG {base} has no `DEFAULT_ENTRY_STEMS` entry."
        assert patch in stems, f"Patch FMG {patch} has no `DEFAULT_ENTRY_STEMS` entry."
        assert stems[base] == stems[patch], (
            f"Base {base} and patch {patch} must share an entry stem (they share a Binder path in DSR)."
        )


def test_no_base_fmg_is_also_a_patch_fmg():
    bases = set(MSGDirectory.BASE_PATCH_FMGS)
    patches = set(MSGDirectory.BASE_PATCH_FMGS.values())
    assert not bases & patches


# ---------------------------------------------------------------------------
# Live DSR text
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_read_dsr_text(dsr_text):
    assert sorted(dsr_text.files) == ["item", "menu"]
    assert isinstance(dsr_text.WeaponNames, FMG)
    assert dsr_text.WeaponNames[100000]  # Dagger
    assert dsr_text.NPCNames.entries


@pytest.mark.game_data
def test_every_declared_fmg_is_present(dsr_text):
    missing = [key for key in MSGDirectory.DEFAULT_ENTRY_STEMS if key not in dsr_text.fmgs]
    assert not missing, f"FMGs declared in `DEFAULT_ENTRY_STEMS` but absent from vanilla DSR: {missing}"


@pytest.mark.game_data
def test_dsr_base_and_patch_fmgs_are_already_in_sync(dsr_text):
    """Unlike PTDE, vanilla DSR ships identical base and patch FMGs."""
    for base, patch in MSGDirectory.BASE_PATCH_FMGS.items():
        assert dsr_text.fmgs[base].entries == dsr_text.fmgs[patch].entries, (
            f"Base {base} and patch {patch} FMGs differ in vanilla DSR."
        )


@pytest.mark.game_data
def test_msg_directory_binary_roundtrip(dsr_text, tmp_path):
    dsr_text.write(tmp_path / "msg")
    written = sorted(p.name for p in (tmp_path / "msg").iterdir())
    assert written == ["item.msgbnd.dcx", "menu.msgbnd.dcx"], f"Unexpected written files: {written}"

    reload = MSGDirectory.from_path(tmp_path / "msg")
    assert sorted(reload.fmgs) == sorted(dsr_text.fmgs)
    for key, fmg in dsr_text.fmgs.items():
        assert fmg.entries == reload.fmgs[key].entries, f"FMG {key} changed after binary round-trip."


@pytest.mark.game_data
def test_msg_directory_json_roundtrip(dsr_text, tmp_path):
    dsr_text.write_json_directory(tmp_path / "msg_json")
    assert (tmp_path / "msg_json" / "item_msgbnd_manifest.json").is_file()
    assert (tmp_path / "msg_json" / "menu_msgbnd_manifest.json").is_file()

    reload = MSGDirectory.from_json_directory(tmp_path / "msg_json")
    assert sorted(reload.fmgs) == sorted(dsr_text.fmgs)
    for key, fmg in dsr_text.fmgs.items():
        assert fmg.entries == reload.fmgs[key].entries, f"FMG {key} changed after JSON round-trip."


@pytest.mark.game_data
def test_text_edit_survives_roundtrip(dsr_text, tmp_path):
    from soulstruct.config import Config
    from pathlib import Path

    # Work on a fresh instance so the module-scoped fixture is not mutated.
    text = MSGDirectory.from_path(Path(Config.DSR_PATH) / "msg/ENGLISH")
    text.WeaponNames[100000] = "Test Dagger"
    text.write(tmp_path / "msg")
    reload = MSGDirectory.from_path(tmp_path / "msg")
    assert reload.WeaponNames[100000] == "Test Dagger"


@pytest.mark.game_data
def test_from_path_requires_both_binders(tmp_path):
    (tmp_path / "empty").mkdir()
    with pytest.raises(FileNotFoundError):
        MSGDirectory.from_path(tmp_path / "empty")


def test_from_path_rejects_missing_directory(tmp_path):
    with pytest.raises(NotADirectoryError):
        MSGDirectory.from_path(tmp_path / "does_not_exist")
