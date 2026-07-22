"""FLVER tests for Dark Souls: Remastered (FLVER2 version 0x2000C/0x2000D).

Rewritten from the old `unittest` module. The committed binaries `c5370.flver` (Gwyn) and
`m2200B0A10.flver.dcx` (Depths sewers map piece) are used, so these tests run without DSR
installed. Tests that need the full game directory use the `dsr_root` fixture and skip cleanly.
"""
from __future__ import annotations

import struct

import numpy as np
import pytest

from soulstruct.flver import FLVER, FLVERVersion
from soulstruct.flver.mesh_tools import MergedMesh
from soulstruct.utilities.maths import AABB


def binary_roundtrip(binary_file, tmp_path, name="_roundtrip"):
    """Local copy of the `conftest` helper (pytest `importlib` import mode blocks importing it)."""
    write_path = tmp_path / name
    binary_file.write(write_path)
    return type(binary_file).from_path(write_path)


CHR_NAME = "c5370.flver"
MAP_PIECE_NAME = "m2200B0A10.flver.dcx"


@pytest.fixture
def chr_flver(resource) -> FLVER:
    return FLVER.from_path(resource(CHR_NAME))


@pytest.fixture
def map_piece_flver(resource) -> FLVER:
    return FLVER.from_path(resource(MAP_PIECE_NAME))


# ---------------------------------------------------------------------------
# Read
# ---------------------------------------------------------------------------


def test_chr_read(chr_flver):
    assert chr_flver.version == FLVERVersion.DarkSouls_A
    assert not chr_flver.big_endian
    assert chr_flver.mesh_count == 22
    assert chr_flver.bone_count == 309
    assert chr_flver.dummy_count == 73
    assert all(not mesh.invalid_layout for mesh in chr_flver.meshes)
    for mesh in chr_flver.meshes:
        assert len(mesh.vertex_arrays) == 1
        assert mesh.vertex_count > 0
        assert mesh.material.mat_def_name.endswith(".mtd")


def test_chr_uses_triangle_strips(chr_flver):
    """DS1 characters store their faces as triangle strips with 0xFFFF restarts."""
    assert all(face_set.is_triangle_strip for mesh in chr_flver for face_set in mesh.face_sets)
    triangles = chr_flver.meshes[0].triangulate_flver2()
    assert triangles.ndim == 2 and triangles.shape[1] == 3
    assert triangles.max() < chr_flver.meshes[0].vertex_count


def test_chr_bones_are_a_valid_tree(chr_flver):
    tree = chr_flver.get_bone_tree()
    assert len(tree.bones) == chr_flver.bone_count
    assert len(tree.get_root_bones()) >= 1
    transforms = tree.get_bone_armature_space_transforms()
    assert len(transforms) == chr_flver.bone_count
    assert all(np.all(np.isfinite(t[0].data)) for t in transforms)


def test_map_piece_read(map_piece_flver):
    assert map_piece_flver.version == FLVERVersion.DarkSouls_A
    assert map_piece_flver.mesh_count == 17
    assert map_piece_flver.bone_count == 1
    assert map_piece_flver.dummy_count == 0
    # Map pieces are static and carry no bone weights.
    assert all(not mesh.is_dynamic for mesh in map_piece_flver.meshes)
    assert all(
        "bone_weights" not in array.field_names
        for mesh in map_piece_flver.meshes
        for array in mesh.vertex_arrays
    )


def test_map_piece_dcx_type_preserved(map_piece_flver, tmp_path):
    assert map_piece_flver.dcx_type is not None
    written = tmp_path / "m2200B0A10.flver.dcx"
    map_piece_flver.write(written)
    # The DCX header magic must be present (i.e. compression was applied on write).
    assert written.read_bytes()[:4] == b"DCX\0"


# ---------------------------------------------------------------------------
# Binary round-trips
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", [CHR_NAME, MAP_PIECE_NAME])
def test_flver_binary_roundtrip(resource, tmp_path, name):
    flver = FLVER.from_path(resource(name))
    reloaded = binary_roundtrip(flver, tmp_path, name=name)
    assert reloaded.version == flver.version
    assert reloaded.mesh_count == flver.mesh_count
    assert reloaded.bone_count == flver.bone_count
    assert reloaded.dummy_count == flver.dummy_count
    for original, new in zip(flver.meshes, reloaded.meshes):
        assert new.vertex_count == original.vertex_count
        assert new.vertices.dtype == original.vertices.dtype
        for field_name in original.vertices.dtype.names:
            np.testing.assert_allclose(
                original.vertices[field_name],
                new.vertices[field_name],
                atol=1e-5,
                err_msg=f"Vertex field '{field_name}' changed on rewrite.",
            )
        for original_fs, new_fs in zip(original.face_sets, new.face_sets):
            np.testing.assert_array_equal(original_fs.vertex_indices, new_fs.vertex_indices)
            assert new_fs.flags == original_fs.flags
            assert new_fs.is_triangle_strip == original_fs.is_triangle_strip


@pytest.mark.parametrize("name", [CHR_NAME, MAP_PIECE_NAME])
def test_flver_roundtrip_preserves_materials_and_bones(resource, tmp_path, name):
    flver = FLVER.from_path(resource(name))
    reloaded = binary_roundtrip(flver, tmp_path, name=name)
    for original, new in zip(flver.meshes, reloaded.meshes):
        assert new.material.name == original.material.name
        assert new.material.mat_def_path == original.material.mat_def_path
        assert [t.path for t in new.material.textures] == [t.path for t in original.material.textures]
        assert [t.texture_type for t in new.material.textures] == [
            t.texture_type for t in original.material.textures
        ]
    for original_bone, new_bone in zip(flver.bones, reloaded.bones):
        assert new_bone.name == original_bone.name
        assert new_bone.parent_bone_index == original_bone.parent_bone_index
        np.testing.assert_allclose(new_bone.translate, original_bone.translate)


@pytest.mark.xfail(
    reason=(
        "BUG: the FLVER-wide bounding box in the FLVER2 header is dropped by "
        "`FLVER._from_flver2_reader` (it never maps `bounding_box_min`/`bounding_box_max` onto the "
        "`bounding_box` field), so a plain read->write cycle replaces the real box with the "
        "'invalid' inverted-infinite AABB."
    ),
    strict=False,
)
@pytest.mark.parametrize("name", [CHR_NAME, MAP_PIECE_NAME])
def test_flver_roundtrip_preserves_header_bounding_box(resource, tmp_path, name):
    flver = FLVER.from_path(resource(name))
    assert flver.bounding_box != AABB.invalid()
    reloaded = binary_roundtrip(flver, tmp_path, name=name)
    np.testing.assert_allclose(reloaded.bounding_box.min, flver.bounding_box.min)
    np.testing.assert_allclose(reloaded.bounding_box.max, flver.bounding_box.max)


def test_flver_roundtrip_after_explicit_bounding_box_refresh(chr_flver, tmp_path):
    """Work-around for the header bounding-box bug: call `refresh_bounding_boxes()` before writing."""
    chr_flver.refresh_bounding_boxes()
    expected = chr_flver.bounding_box
    written = tmp_path / "refreshed.flver"
    chr_flver.write(written)
    header = struct.unpack_from("<6f", written.read_bytes(), 0x28)
    np.testing.assert_allclose(header[:3], expected.min, rtol=1e-5)
    np.testing.assert_allclose(header[3:], expected.max, rtol=1e-5)


# ---------------------------------------------------------------------------
# Bounding boxes / geometry utilities
# ---------------------------------------------------------------------------


def test_refresh_bounding_boxes_covers_all_vertices(chr_flver):
    chr_flver.refresh_bounding_boxes()
    all_positions = np.vstack([mesh.vertices["position"] for mesh in chr_flver.meshes])
    np.testing.assert_allclose(chr_flver.bounding_box.min, all_positions.min(axis=0))
    np.testing.assert_allclose(chr_flver.bounding_box.max, all_positions.max(axis=0))


def test_refresh_bone_bounding_boxes(chr_flver):
    chr_flver.refresh_bone_bounding_boxes(in_local_space=True)
    used = [b for b in chr_flver.bones if b.bounding_box != AABB.invalid()]
    assert used, "No bone bounding boxes were refreshed."
    for bone in used:
        assert np.all(np.asarray(bone.bounding_box.min.data) <= np.asarray(bone.bounding_box.max.data))


# ---------------------------------------------------------------------------
# MergedMesh
# ---------------------------------------------------------------------------


def test_merged_mesh_from_character(chr_flver):
    merged = MergedMesh.from_flver(chr_flver, merge_vertices=False)
    total = sum(mesh.vertex_count for mesh in chr_flver.meshes)
    assert merged.vertex_count == total
    assert merged.faces.shape[1] == 4
    assert merged.loop_normals.shape == (total, 3)
    assert merged.loop_uvs  # at least one UV layer
    assert np.all(np.isfinite(merged.positions))


@pytest.mark.xfail(
    reason=(
        "BUG: `MergedMesh.build_stacked_loops` allocates the merged vertex array with `np.empty` and "
        "never initializes fields absent from every mesh layout. DS1 map pieces have no "
        "`bone_weights`, so the merged `bone_weights` column is uninitialized memory (observed as "
        "NaN here). It is also part of the vertex hash used for merging, so vertex merging becomes "
        "non-deterministic."
    ),
    strict=False,
)
def test_merged_map_piece_bone_weights_are_zeroed(map_piece_flver):
    merged = MergedMesh.from_flver(map_piece_flver, merge_vertices=False)
    assert np.all(np.isfinite(merged.bone_weights))
    assert np.all(merged.bone_weights == 0.0)


def test_merged_mesh_cached_on_flver(map_piece_flver):
    merged = map_piece_flver.update_cached_merged_mesh(merge_vertices=False)
    assert map_piece_flver.get_cached_merged_mesh() is merged
    map_piece_flver.clear_cached_merged_mesh()
    assert not map_piece_flver.has_cached_merged_mesh()


# ---------------------------------------------------------------------------
# DSR game directory (skipped when DSR is not installed)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_dsr_character_from_binder(dsr_root):
    path = dsr_root / "chr/c2230.chrbnd.dcx"
    if not path.is_file():
        pytest.skip(f"DSR CHRBND not found: {path}")
    flver = FLVER.from_binder_path(path)
    assert flver.version == FLVERVersion.DarkSouls_A
    assert flver.mesh_count > 0
    assert flver.bone_count > 0


@pytest.mark.game_data
@pytest.mark.slow
def test_dsr_map_pieces_read_without_invalid_layouts(dsr_root):
    """QLOC botched several DS1R map-piece layouts; `layout_repair` should fix them on read."""
    map_dir = dsr_root / "map/m10_01_00_00"
    if not map_dir.is_dir():
        pytest.skip(f"DSR map directory not found: {map_dir}")
    paths = sorted(map_dir.glob("*.flver.dcx"))[:15]
    if not paths:
        pytest.skip("No DSR map piece FLVERs found.")
    unrepaired = [
        path.name for path in paths
        if any(mesh.invalid_layout for mesh in FLVER.from_path(path).meshes)
    ]
    assert not unrepaired, f"FLVERs with unrepairable vertex layouts: {unrepaired}"
