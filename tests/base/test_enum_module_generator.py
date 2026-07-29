"""Tests for `soulstruct.base.maps.enum_module_generator.EnumModuleGenerator`.

The generator turns an `MSB`'s entity IDs into a `{map_stem}_enums.py` module of `IntEnum`
subclasses that EVS scripts import. The critical property is simply that the emitted module is
valid, *importable* Python -- a broken module silently breaks every EVS script for that map.
"""
from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

import pytest

from soulstruct.base.maps.enum_module_generator import EnumModuleGenerator
from soulstruct.darksouls1ptde.maps.msb import MSB as PTDE_MSB


PTDE_MSB_RELPATH = ("darksouls1ptde", "resources", "m10_00_00_00.msb")
MAP_STEM = "m10_00_00_00"

_module_counter = 0


def import_module_file(path: Path):
    """Import a generated enums module by path, with a unique module name each time."""
    global _module_counter
    _module_counter += 1
    name = f"_generated_enums_{_module_counter}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(name, None)
    return module


def build_msb(**_) -> PTDE_MSB:
    """Small synthetic MSB with entity IDs across several supertypes."""
    msb = PTDE_MSB()
    char_model = msb.character_models.new(name="c1000")
    col_model = msb.collision_models.new(name="h0000B0")
    obj_model = msb.object_models.new(name="o0000")
    collision = msb.collisions.new(name="h0000B0_0000", model=col_model, entity_id=1003200)
    msb.characters.new(name="c1000_0000", model=char_model, entity_id=1000000, draw_parent=collision)
    msb.characters.new(name="c1000_0001", model=char_model, entity_id=1000001, draw_parent=collision)
    msb.characters.new(name="c1000_0002", model=char_model, entity_id=-1)  # no ID -> omitted
    msb.objects.new(name="o0000_0000", model=obj_model, entity_id=1001000)
    region = msb.regions.new(name="StartPoint", entity_id=1002000)
    msb.sounds.new(name="Sound0", entity_id=1003800, attached_region=region)
    return msb


@pytest.fixture
def msb() -> PTDE_MSB:
    return build_msb()


@pytest.fixture(scope="module")
def ptde_msb_path(tests_dir):
    path = tests_dir.joinpath(*PTDE_MSB_RELPATH)
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


def generate(msb: PTDE_MSB, tmp_path: Path, name="m10_00_00_00_enums.py", **kwargs) -> Path:
    out_path = tmp_path / name
    EnumModuleGenerator(msb, map_stem=MAP_STEM).write_enums_module(out_path, **kwargs)
    return out_path


# ---------------------------------------------------------------------------
# Basic generation
# ---------------------------------------------------------------------------


def test_generated_module_is_valid_python(msb, tmp_path):
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text(encoding="utf-8")
    ast.parse(text)  # raises SyntaxError if invalid


def test_generated_module_is_importable_and_has_expected_enums(msb, tmp_path):
    module = import_module_file(generate(msb, tmp_path, separate_region_points_volumes=True))
    assert module.Characters.c1000_0000 == 1000000
    assert module.Characters.c1000_0001 == 1000001
    assert not hasattr(module.Characters, "c1000_0002")  # entity ID -1 omitted
    assert module.Objects.o0000_0000 == 1001000
    assert module.Collisions.h0000B0_0000 == 1003200
    assert module.Sounds.Sound0 == 1003800
    assert module.RegionPoints.StartPoint == 1002000


def test_generated_module_imports_game_types(msb, tmp_path):
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text(encoding="utf-8")
    assert text.startswith("from soulstruct.darksouls1ptde.game_types import *")
    assert text.endswith("\n")


def test_empty_subtype_lists_are_skipped(msb, tmp_path):
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text(encoding="utf-8")
    assert "class MapPieces" not in text  # no map pieces in the synthetic MSB
    assert "class PlayerStarts" not in text


def test_output_directory_is_created(msb, tmp_path):
    out_path = tmp_path / "nested" / "dir" / "m10_enums.py"
    EnumModuleGenerator(msb, map_stem=MAP_STEM).write_enums_module(
        out_path, separate_region_points_volumes=True
    )
    assert out_path.is_file()


def test_default_options_produce_valid_python(msb, tmp_path):
    text = generate(msb, tmp_path).read_text(encoding="utf-8")
    ast.parse(text)


# ---------------------------------------------------------------------------
# Entity ID ranges
# ---------------------------------------------------------------------------


def test_entity_id_ranges_are_applied_for_ds1_map_stem(msb, tmp_path):
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text(encoding="utf-8")
    # DS1 7-digit base for m10_00_00_00 is 1000000; `Object` range is base+1000 .. base+1899.
    assert "class Objects(Object, first_value=1001000, last_value=1001899):" in text
    assert "class Characters(Character, first_value=1000000, last_value=1000899):" in text


def test_entity_id_ranges_can_be_disabled(msb, tmp_path):
    text = generate(
        msb, tmp_path, separate_region_points_volumes=True, use_entity_id_ranges=False
    ).read_text(encoding="utf-8")
    assert "first_value" not in text
    assert "class Objects(Object):" in text


def test_unusual_map_stem_disables_ranges_with_warning(msb, tmp_path, caplog):
    out_path = tmp_path / "weird_enums.py"
    EnumModuleGenerator(msb, map_stem="not_a_map").write_enums_module(
        out_path, separate_region_points_volumes=True
    )
    text = out_path.read_text(encoding="utf-8")
    assert "first_value" not in text
    ast.parse(text)


# ---------------------------------------------------------------------------
# Sorting, comments, appending
# ---------------------------------------------------------------------------


def test_sort_by_id(tmp_path):
    msb = PTDE_MSB()
    model = msb.character_models.new(name="c1000")
    msb.characters.new(name="Zebra", model=model, entity_id=1000005)
    msb.characters.new(name="Alpha", model=model, entity_id=1000001)
    unsorted_text = generate(msb, tmp_path, "a_enums.py", separate_region_points_volumes=True).read_text("utf-8")
    sorted_text = generate(
        msb, tmp_path, "b_enums.py", separate_region_points_volumes=True, sort_by_id=True
    ).read_text("utf-8")
    assert unsorted_text.index("Zebra") < unsorted_text.index("Alpha")
    assert sorted_text.index("Alpha") < sorted_text.index("Zebra")


def test_comment_func_is_applied(msb, tmp_path):
    def comment_func(class_name: str, entry_name: str) -> str:
        return f"{class_name}!{entry_name}" if entry_name == "c1000_0000" else ""

    text = generate(
        msb, tmp_path, separate_region_points_volumes=True, comment_func=comment_func
    ).read_text("utf-8")
    assert "c1000_0000 = 1000000  # Character!c1000_0000" in text
    ast.parse(text)


def test_entry_description_becomes_comment(tmp_path):
    msb = PTDE_MSB()
    model = msb.character_models.new(name="c1000")
    msb.characters.new(name="Guy", model=model, entity_id=1000001, description="A guy.")
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text("utf-8")
    assert "Guy = 1000001  # A guy." in text
    ast.parse(text)


def test_append_to_module_preserves_existing_text_and_adds_import(msb, tmp_path):
    existing = "# my custom header\n\n\nclass MyThing:\n    pass\n"
    out_path = tmp_path / "appended_enums.py"
    EnumModuleGenerator(msb, map_stem=MAP_STEM).write_enums_module(
        out_path, append_to_module=existing, separate_region_points_volumes=True
    )
    text = out_path.read_text("utf-8")
    assert "# my custom header" in text
    assert "class MyThing:" in text
    assert "from soulstruct.darksouls1ptde.game_types import *" in text
    assert text.index("from soulstruct.darksouls1ptde.game_types import *") < text.index("class MyThing:")
    ast.parse(text)


def test_append_to_module_does_not_duplicate_import(msb, tmp_path):
    existing = "from soulstruct.darksouls1ptde.game_types import *\n\n\nclass MyThing:\n    pass\n"
    out_path = tmp_path / "appended2_enums.py"
    EnumModuleGenerator(msb, map_stem=MAP_STEM).write_enums_module(
        out_path, append_to_module=existing, separate_region_points_volumes=True
    )
    text = out_path.read_text("utf-8")
    assert text.count("from soulstruct.darksouls1ptde.game_types import *") == 1


# ---------------------------------------------------------------------------
# Awkward entry names
# ---------------------------------------------------------------------------


def test_invalid_python_name_is_commented_out(tmp_path):
    msb = PTDE_MSB()
    model = msb.character_models.new(name="c1000")
    msb.characters.new(name="has a space", model=model, entity_id=1000001)
    msb.characters.new(name="ok_name", model=model, entity_id=1000002)
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text("utf-8")
    assert "# has a space = 1000001" in text
    assert "ok_name = 1000002" in text
    ast.parse(text)


def test_non_ascii_name_is_commented_out(tmp_path):
    msb = PTDE_MSB()
    model = msb.character_models.new(name="c1000")
    msb.characters.new(name="松明01", model=model, entity_id=1000001)
    msb.characters.new(name="ok_name", model=model, entity_id=1000002)
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text("utf-8")
    assert "# 松明01 = 1000001" in text
    assert "ok_name = 1000002" in text
    ast.parse(text)


def test_repeated_entity_id_uses_first_entry_only(tmp_path):
    msb = PTDE_MSB()
    model = msb.character_models.new(name="c1000")
    msb.characters.new(name="first", model=model, entity_id=1000001)
    msb.characters.new(name="second", model=model, entity_id=1000001)
    module = import_module_file(generate(msb, tmp_path, separate_region_points_volumes=True))
    assert module.Characters.first == 1000001
    assert not hasattr(module.Characters, "second")


@pytest.mark.xfail(
    reason=(
        "Two entries in the same subtype list sharing a NAME but not an entity ID emit two enum "
        "members with the same name; `EnumMeta` then raises `TypeError: <name> already defined`, "
        "so the generated module cannot be imported. MSB names are not guaranteed unique."
    ),
    strict=False,
)
def test_repeated_entry_name_still_produces_importable_module(tmp_path):
    msb = PTDE_MSB()
    model = msb.character_models.new(name="c1000")
    msb.characters.new(name="same_name", model=model, entity_id=1000001)
    msb.characters.new(name="same_name", model=model, entity_id=1000002)
    import_module_file(generate(msb, tmp_path, separate_region_points_volumes=True))


@pytest.mark.xfail(
    reason=(
        "An entry `description` containing a newline is emitted verbatim as a trailing `# ...` "
        "comment, breaking the generated module."
    ),
    strict=False,
)
def test_multiline_description_does_not_break_module(tmp_path):
    msb = PTDE_MSB()
    model = msb.character_models.new(name="c1000")
    msb.characters.new(name="Guy", model=model, entity_id=1000001, description="Line one\nLine two")
    text = generate(msb, tmp_path, separate_region_points_volumes=True).read_text("utf-8")
    ast.parse(text)


# ---------------------------------------------------------------------------
# Constructor behaviour
# ---------------------------------------------------------------------------


def test_map_stem_defaults_to_msb_path_stem(ptde_msb_path, tmp_path):
    msb = PTDE_MSB.from_path(ptde_msb_path)
    generator = EnumModuleGenerator(msb)
    assert generator.map_stem == MAP_STEM
    assert generator.path == ptde_msb_path


def test_output_path_defaults_to_msb_directory(ptde_msb_path, tmp_path):
    """`write_enums_module(None)` writes next to the MSB, so copy the MSB into `tmp_path` first."""
    msb = PTDE_MSB.from_path(ptde_msb_path)
    msb.path = tmp_path / f"{MAP_STEM}.msb"
    generator = EnumModuleGenerator(msb)
    generator.write_enums_module(separate_region_points_volumes=True)
    assert (tmp_path / f"{MAP_STEM}_enums.py").is_file()


def test_pathless_msb_without_map_stem_raises_value_error(msb):
    with pytest.raises(ValueError):
        EnumModuleGenerator(msb)


# ---------------------------------------------------------------------------
# Real MSB
# ---------------------------------------------------------------------------


def test_real_ptde_msb_generates_importable_module(ptde_msb_path, tmp_path):
    msb = PTDE_MSB.from_path(ptde_msb_path)
    out_path = tmp_path / f"{MAP_STEM}_enums.py"
    EnumModuleGenerator(msb).write_enums_module(out_path, separate_region_points_volumes=True)
    module = import_module_file(out_path)
    assert module.Characters
    assert module.RegionPoints
    # Spot-check that a real entity ID survived.
    assert any(v >= 1000000 for v in module.Characters.__members__.values())


def test_real_ptde_msb_region_split_matches_shapes(ptde_msb_path, tmp_path):
    from soulstruct.base.maps.msb.region_shapes import RegionShapeType

    msb = PTDE_MSB.from_path(ptde_msb_path)
    out_path = tmp_path / f"{MAP_STEM}_enums.py"
    EnumModuleGenerator(msb).write_enums_module(out_path, separate_region_points_volumes=True)
    module = import_module_file(out_path)
    volume_types = RegionShapeType.get_volume_types()
    point_names = set(module.RegionPoints.__members__)
    volume_names = set(module.RegionVolumes.__members__)
    # NOTE: vanilla DS1 region names are mostly non-ASCII or contain spaces, so they are emitted as
    # comments only; both classes can legitimately end up with zero members.
    assert not (point_names & volume_names)
    regions_by_name = {region.name: region for region in msb.regions}
    for name in point_names:
        assert regions_by_name[name].shape.SHAPE_TYPE == RegionShapeType.Point
    for name in volume_names:
        assert regions_by_name[name].shape.SHAPE_TYPE in volume_types


def test_region_split_on_synthetic_msb(tmp_path):
    from soulstruct.base.maps.msb.region_shapes import BoxShape, PointShape

    msb = PTDE_MSB()
    msb.regions.new(name="MyPoint", entity_id=1002000, shape=PointShape())
    msb.regions.new(name="MyBox", entity_id=1002001, shape=BoxShape(1.0, 2.0, 3.0))
    module = import_module_file(generate(msb, tmp_path, separate_region_points_volumes=True))
    assert set(module.RegionPoints.__members__) == {"MyPoint"}
    assert set(module.RegionVolumes.__members__) == {"MyBox"}
