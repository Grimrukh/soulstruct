"""Tests for the DSR `MSB` (map studio binary) and `MapStudioDirectory`.

DSR MSBs are byte-identical in format to PTDE MSBs (`soulstruct.darksouls1r.maps.MSB` subclasses the PTDE
class and only adds DSR-specific *methods*), so the interesting behaviour here is:

    - unpack -> pack byte stability, and unpack -> pack -> unpack entry equality;
    - JSON round-trip;
    - DSR-only helpers: `translate_entity_id_names()`, `get_nvmdump()`;
    - entry duplication / reference integrity;
    - `EnumModuleGenerator` output (the entity-ID enums module used by EVS scripts).
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import pytest

from soulstruct.base.maps.enum_module_generator import EnumModuleGenerator
from soulstruct.darksouls1r.maps import MSB, MapStudioDirectory, get_map
from soulstruct.darksouls1r.maps.constants import VANILLA_MSB_TRANSLATIONS
from soulstruct.utilities.maths import Vector3

MAP_STEM = "m10_00_00_00"


def assert_bytes_equal(actual: bytes, expected: bytes, context: str = "") -> None:
    """Local copy of the `conftest` helper (`tests/darksouls1r/` is a package, so `conftest` is not importable)."""
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


def assert_msb_entries_equal(first: MSB, second: MSB) -> None:
    """Compare every entry of every subtype list of two MSBs."""
    for subtype in MSB.get_subtype_list_names():
        source_entries = first[subtype]
        test_entries = second[subtype]
        assert len(source_entries) == len(test_entries), f"Entry count differs for subtype '{subtype}'."
        for i, (source, test) in enumerate(zip(source_entries, test_entries)):
            assert source == test, f"Entry {i} ('{source.name}') differs in subtype '{subtype}'."


@pytest.fixture
def msb_path(resource) -> Path:
    return resource(f"{MAP_STEM}.msb")


@pytest.fixture
def msb(msb_path) -> MSB:
    return MSB.from_path(msb_path)


# ---------------------------------------------------------------------------
# Basic structure
# ---------------------------------------------------------------------------


def test_msb_class_is_ptde_subclass():
    from soulstruct.darksouls1ptde.maps.msb import MSB as PTDE_MSB

    assert issubclass(MSB, PTDE_MSB)
    # DSR MSBs are NOT DCX-compressed, unlike most other DSR files.
    from soulstruct.dcx import DCXType

    assert MSB()._get_dcx_type() == DCXType.Null


def test_msb_read(msb):
    assert msb.get_map_stem() == MAP_STEM
    assert len(msb.navmeshes) == 41
    assert len(msb.collisions) > 0
    assert len(msb.characters) > 0
    assert msb.characters.find_entry_name("c1000_0000") is not None


def test_subtype_list_names_are_unique():
    names = MSB.get_subtype_list_names()
    assert len(names) == len(set(names))
    for name in names:
        assert isinstance(MSB()[name], object)


def test_msb_repack_is_idempotent(msb):
    """Soulstruct's MSB writer is NOT byte-identical to vanilla (it pads entry name strings to a tighter
    alignment, shrinking m10_00_00_00 by 1300 bytes), but repacking must be a fixed point."""
    once = bytes(msb)
    twice = bytes(MSB.from_bytes(once))
    assert_bytes_equal(twice, once, "MSB second repack")


def test_msb_repack_differs_from_vanilla_only_in_name_padding(msb, msb_path):
    """Guard-rail: repack must stay the same size or smaller, and reload identically."""
    packed = bytes(msb)
    vanilla = msb_path.read_bytes()
    assert len(packed) <= len(vanilla)
    assert_msb_entries_equal(msb, MSB.from_bytes(packed))


def test_msb_binary_roundtrip(msb, tmp_path):
    msb.write(tmp_path / "roundtrip.msb")
    reload = MSB.from_path(tmp_path / "roundtrip.msb")
    assert_msb_entries_equal(msb, reload)


def test_msb_model_and_part_references_resolve(msb):
    """Every part's `model` must be an actual model entry in the same MSB (not a dangling index)."""
    all_models = [m for subtype in MSB.get_subtype_list_names() if subtype.endswith("_models") for m in msb[subtype]]
    for subtype in ("map_pieces", "objects", "characters", "collisions", "navmeshes", "player_starts"):
        for part in msb[subtype]:
            if part.model is None:
                continue
            assert any(m is part.model for m in all_models), (
                f"Part '{part.name}' references a model not present in the MSB."
            )


def test_msb_collision_environment_event_backrefs(msb):
    """Collision `environment_event` references must point at real `environments` entries."""
    for collision in msb.collisions:
        event = getattr(collision, "environment_event", None)
        if event is not None:
            assert any(e is event for e in msb.environments)


# ---------------------------------------------------------------------------
# Entry editing
# ---------------------------------------------------------------------------


def test_duplicate_character_and_treasure(msb, tmp_path):
    source_chr = msb.characters.find_entry_name("c1000_0000")
    new_chr = msb.characters.duplicate(
        source_chr, name="c1000_0000_COPY", entity_id=1000999, translate=Vector3([1.0, 2.0, 3.0])
    )
    new_treasure = msb.treasures.duplicate(0, name="TREASURE_0_COPY")

    assert new_chr.name == "c1000_0000_COPY"
    assert new_chr.entity_id == 1000999
    assert new_chr.translate == Vector3([1.0, 2.0, 3.0])
    assert new_chr.model is source_chr.model, "Duplicated part must share the source's model entry."
    assert new_treasure.name == "TREASURE_0_COPY"

    msb.write(tmp_path / "edited.msb")
    reload = MSB.from_path(tmp_path / "edited.msb")
    assert_msb_entries_equal(msb, reload)

    reloaded_chr = reload.characters.find_entry_name("c1000_0000_COPY")
    assert reloaded_chr.entity_id == 1000999
    assert reloaded_chr.translate == Vector3([1.0, 2.0, 3.0])
    assert reload.treasures.find_entry_name("TREASURE_0_COPY") is not None


def test_find_entry_name_raises_for_missing(msb):
    with pytest.raises(Exception):
        msb.characters.find_entry_name("c9999_9999_DOES_NOT_EXIST")


# ---------------------------------------------------------------------------
# DSR-specific methods
# ---------------------------------------------------------------------------


def test_translate_entity_id_names(msb):
    """Only regions/events get translated; parts and models keep their (already-English) names."""
    part_names_before = [p.name for p in msb.characters]
    msb.translate_entity_id_names()
    assert [p.name for p in msb.characters] == part_names_before

    depths_region_names = {r.name for r in msb.regions}
    assert "GapingDragonMusic" in depths_region_names
    assert "GapingDragonFogPrompt" in depths_region_names

    for region in msb.regions:
        if region.entity_id in VANILLA_MSB_TRANSLATIONS:
            assert region.name == VANILLA_MSB_TRANSLATIONS[region.entity_id]


def test_translate_entity_id_names_is_idempotent(msb):
    msb.translate_entity_id_names()
    first = [r.name for r in msb.regions]
    msb.translate_entity_id_names()
    assert [r.name for r in msb.regions] == first


def test_translate_does_not_introduce_new_subtype_name_clashes(msb):
    """Translation must not make two entries in the SAME subtype list share a name."""

    def subtype_duplicates(m: MSB) -> dict[str, list[str]]:
        out = {}
        for subtype in MSB.get_subtype_list_names():
            counts = Counter(e.name for e in m[subtype])
            dups = sorted(n for n, c in counts.items() if c > 1)
            if dups:
                out[subtype] = dups
        return out

    before = subtype_duplicates(msb)
    msb.translate_entity_id_names()
    after = subtype_duplicates(msb)
    for subtype, names in after.items():
        new = set(names) - set(before.get(subtype, []))
        assert not new, f"Translation created new duplicate names in '{subtype}': {sorted(new)}"


def test_get_nvmdump(msb):
    dump = msb.get_nvmdump(MAP_STEM)
    lines = dump.splitlines()
    assert dump.endswith("\n"), "Vanilla NVMDUMP files end with a newline."
    # 4 lines per navmesh + 2 lines per map offset.
    assert len(lines) == 4 * len(msb.navmeshes) + 2 * len(msb.map_offsets)
    assert lines[0] == f"Nvm[0].Name: {msb.navmeshes[0].name}"
    assert lines[1].startswith(f"Nvm[0].FilePath: N:\\FRPG\\data\\Model\\map\\{MAP_STEM}\\navimesh\\")
    assert lines[1].endswith("A10.SIB")


def test_get_nvmdump_auto_detects_map_stem(msb):
    assert msb.get_nvmdump() == msb.get_nvmdump(MAP_STEM)


def test_get_nvmdump_requires_map_stem_when_unknown(msb):
    msb.path = None
    with pytest.raises(ValueError):
        msb.get_nvmdump()


# ---------------------------------------------------------------------------
# Entity enums module generation
# ---------------------------------------------------------------------------


def test_enum_module_generator_writes_file(msb, tmp_path):
    emg = EnumModuleGenerator(msb, MAP_STEM)
    out = tmp_path / f"{MAP_STEM}_enums.py"
    emg.write_enums_module(out)
    text = out.read_text(encoding="utf-8")
    assert "from soulstruct.darksouls1r.game_types import *" in text
    assert "class Objects(Object" in text
    assert "class Characters(Character" in text


def test_generated_enums_module_is_importable(msb, tmp_path):
    import importlib.util

    emg = EnumModuleGenerator(msb, MAP_STEM)
    out = tmp_path / f"{MAP_STEM}_enums.py"
    emg.write_enums_module(out)

    spec = importlib.util.spec_from_file_location(f"{MAP_STEM}_enums", out)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(module, "Objects")


def test_generated_enums_module_is_importable_with_split_regions(msb, tmp_path):
    """The `separate_region_points_volumes=True` path DOES produce a valid module."""
    import importlib.util

    emg = EnumModuleGenerator(msb, MAP_STEM)
    out = tmp_path / f"{MAP_STEM}_enums.py"
    emg.write_enums_module(out, separate_region_points_volumes=True)

    spec = importlib.util.spec_from_file_location(f"{MAP_STEM}_split_enums", out)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(module, "Objects")
    assert hasattr(module, "Characters")


# ---------------------------------------------------------------------------
# JSON
# ---------------------------------------------------------------------------


def test_msb_json_roundtrip(msb, tmp_path):
    msb.write_json(tmp_path / "msb.json")
    reload = MSB.from_json(tmp_path / "msb.json")
    assert_msb_entries_equal(msb, reload)


def test_msb_to_dict_is_json_serialisable(msb, tmp_path):
    """Even though reading it back is broken, writing must at least succeed and be stable."""
    msb.write_json(tmp_path / "a.json")
    msb.write_json(tmp_path / "b.json")
    assert (tmp_path / "a.json").read_text(encoding="utf-8") == (tmp_path / "b.json").read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# `MapStudioDirectory` (requires DSR install)
# ---------------------------------------------------------------------------


def test_map_studio_directory_class_config():
    assert MapStudioDirectory.FILE_CLASS is MSB
    # `COMMON` has no MSB and must be excluded.
    assert all(m.msb_file_stem for m in MapStudioDirectory.ALL_MAPS)
    assert "m12_00_00_00" in MapStudioDirectory.QUIETLY_IGNORED_FILE_STEMS
    assert MapStudioDirectory.GET_MAP("m10_00_00_00") is get_map("m10_00_00_00")


@pytest.mark.slow
@pytest.mark.game_data
def test_map_studio_directory_roundtrip(dsr_root, tmp_path):
    msd = MapStudioDirectory.from_path(dsr_root / "map/MapStudio")
    assert len(msd.files) == len(MapStudioDirectory.ALL_MAPS)

    msd.write(tmp_path / "MapStudio")
    reload = MapStudioDirectory.from_path(tmp_path / "MapStudio")
    assert sorted(reload.files) == sorted(msd.files)
    for stem, source_msb in msd.files.items():
        assert_msb_entries_equal(source_msb, reload.files[stem])

    # Named map properties must work.
    assert msd.Depths is msd.files["m10_00_00_00"]
    assert msd.DarkrootGarden is msd.files["m12_00_00_01"]


@pytest.mark.slow
@pytest.mark.game_data
def test_all_vanilla_msbs_roundtrip(dsr_root):
    """Every real DSR MSB must unpack -> pack -> unpack with identical entries and idempotent bytes."""
    checked = 0
    for msb_file in sorted((dsr_root / "map/MapStudio").glob("m*.msb")):
        if msb_file.stem.startswith("m99") or msb_file.stem == "m12_00_00_00":
            continue  # DSR test maps / unused pre-DLC Darkroot MSB
        game_msb = MSB.from_path(msb_file)
        packed = bytes(game_msb)
        reload = MSB.from_bytes(packed)
        assert_msb_entries_equal(game_msb, reload)
        assert_bytes_equal(bytes(reload), packed, f"{msb_file.name} second repack")
        checked += 1
    assert checked >= 17


@pytest.mark.slow
@pytest.mark.game_data
def test_dsr_test_maps_cannot_be_read(dsr_root):
    """Documents a known limitation: DSR's `m99_*` test-map MSBs use `MSBCollision` values Soulstruct
    asserts against, which is why `MapStudioDirectory.QUIETLY_IGNORED_FILE_STEMS` excludes them."""
    path = dsr_root / "map/MapStudio/m99_80_10_00.msb"
    if not path.is_file():
        pytest.skip(f"Missing DSR test map: {path}")
    with pytest.raises(Exception):
        MSB.from_path(path)
