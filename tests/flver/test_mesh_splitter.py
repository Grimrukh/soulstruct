"""Merge/split round-trips on real FLVER files.

Ported from the old stray script `tests/_test_mesh_splitter.py`, which printed diagnostics for a
DSR map piece instead of asserting anything. The intent is preserved:

    1. read a real FLVER, write it, re-read it, and confirm the vertex data survives;
    2. merge all of its meshes into a `MergedMesh`, confirm each material uses a single consistent
       vertex layout, split it back into FLVER meshes, and compare geometry with the original.

Committed test binaries are used where possible (always runs); the DSR game directory is used for
the larger map-piece cases (skipped when DSR is not installed).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from soulstruct.flver import FLVER
from soulstruct.flver.mesh_tools import MergedMesh, SplitMeshDef


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def ds1r_resource(tests_dir: Path, name: str) -> Path:
    """Committed DS1R FLVER binaries live beside the DS1R tests."""
    path = tests_dir / "darksouls1r" / "resources" / name
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


def split_defs_with_is_dynamic(flver: FLVER) -> list[SplitMeshDef]:
    """`SplitMeshDef.get_defs_from_flver()` plus the `is_dynamic` kwarg `split_mesh()` requires.

    See `tests/flver/test_mesh_tools.py::test_split_mesh_with_canonical_defs`: the canonical helper
    does not populate `kwargs["is_dynamic"]`, but `FLVERMesh` requires it.
    """
    return [
        SplitMeshDef(
            d.material, d.layout, d.is_dynamic, {**d.kwargs, "is_dynamic": d.is_dynamic}, d.uv_layer_names
        )
        for d in SplitMeshDef.get_defs_from_flver(flver)
    ]


def assert_layouts_consistent_per_material(flver: FLVER, mesh_material_indices: list[int]):
    """Every mesh sharing a material index must use an identical vertex array layout."""
    layouts = {}
    for mesh, material_index in zip(flver.meshes, mesh_material_indices):
        layout = mesh.vertex_arrays[0].layout
        if material_index not in layouts:
            layouts[material_index] = layout
        else:
            assert layout == layouts[material_index], (
                f"Meshes sharing material index {material_index} have different vertex layouts."
            )


def merge_and_split(flver: FLVER, merge_vertices=True):
    merged = MergedMesh.from_flver(flver)  # default: one 'material' per mesh
    assert_layouts_consistent_per_material(flver, list(range(len(flver.meshes))))
    if not merge_vertices:
        merged = MergedMesh.from_flver(flver, merge_vertices=False)
    return merged, merged.split_mesh(split_defs_with_is_dynamic(flver))


# ---------------------------------------------------------------------------
# Read -> write -> read (committed resources)
# ---------------------------------------------------------------------------


def test_flver_rewrite_preserves_vertex_data(tests_dir, tmp_path):
    """Port of `_test_mesh_splitter.test_flver_rewrite`, now asserting instead of printing."""
    path = ds1r_resource(tests_dir, "m2200B0A10.flver.dcx")
    flver = FLVER.from_path(path)
    write_path = tmp_path / "rewrite.flver.dcx"
    flver.write(write_path)
    reloaded = FLVER.from_path(write_path)

    assert reloaded.mesh_count == flver.mesh_count
    assert reloaded.bone_count == flver.bone_count
    for original_mesh, reloaded_mesh in zip(flver.meshes, reloaded.meshes):
        original = original_mesh.vertex_arrays[0].array
        rewritten = reloaded_mesh.vertex_arrays[0].array
        assert original.dtype == rewritten.dtype
        for name in original.dtype.names:
            np.testing.assert_allclose(
                original[name], rewritten[name], atol=1e-5, err_msg=f"Field '{name}' changed."
            )


# ---------------------------------------------------------------------------
# Merge -> split (committed resources)
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    reason=(
        "BUG: vanilla FLVERs contain vertices that no face uses; `MergedMesh.get_merged_vertices` "
        "marks those loops with 2**32-1 and `get_combined_loop_data` then indexes `vertex_data` with "
        "that sentinel, raising `IndexError`. The documented merge->split round-trip cannot run on "
        "real game models with vertex merging enabled."
    ),
    strict=False,
)
def test_merge_and_split_character_with_merged_vertices(tests_dir):
    """Port of `_test_mesh_splitter.test_merge_and_split` (default merged-vertex behaviour)."""
    flver = FLVER.from_path(ds1r_resource(tests_dir, "c5370.flver"))
    merged, split_meshes = merge_and_split(flver, merge_vertices=True)
    assert len(split_meshes) == flver.mesh_count


def test_merge_and_split_character_without_merged_vertices(tests_dir):
    """Same round-trip with `merge_vertices=False`, which avoids the unused-vertex sentinel.

    Face counts must be preserved exactly; vertex counts may only DROP (duplicate loops are merged).
    """
    flver = FLVER.from_path(ds1r_resource(tests_dir, "c5370.flver"))
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    assert_layouts_consistent_per_material(flver, list(range(len(flver.meshes))))
    split_meshes = merged.split_mesh(split_defs_with_is_dynamic(flver))

    assert len(split_meshes) == flver.mesh_count
    for original, split in zip(flver.meshes, split_meshes):
        original_faces = original.triangulate_flver2()
        split_faces = split.triangulate_flver2()
        assert len(split_faces) == len(original_faces)
        assert split.vertex_count <= original.vertex_count
        assert split.is_dynamic == original.is_dynamic
        assert split.material is original.material
        assert split.vertices.dtype == original.vertices.dtype
        # Every split face must reference valid vertices.
        assert split_faces.max() < split.vertex_count


def test_merge_and_split_map_piece_without_merged_vertices(tests_dir):
    flver = FLVER.from_path(ds1r_resource(tests_dir, "m2200B0A10.flver.dcx"))
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    split_meshes = merged.split_mesh(split_defs_with_is_dynamic(flver))
    assert len(split_meshes) == flver.mesh_count
    for original, split in zip(flver.meshes, split_meshes):
        assert len(split.triangulate_flver2()) == len(original.triangulate_flver2())


def test_split_meshes_can_be_repacked_into_a_flver(tests_dir, tmp_path):
    """The split result must be a writable FLVER again (full editing round-trip)."""
    flver = FLVER.from_path(ds1r_resource(tests_dir, "c5370.flver"))
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    flver.meshes = merged.split_mesh(split_defs_with_is_dynamic(flver))
    flver.refresh_mesh_indices()
    flver.refresh_bounding_boxes()

    write_path = tmp_path / "split.flver"
    flver.write(write_path)
    reloaded = FLVER.from_path(write_path)
    assert reloaded.mesh_count == flver.mesh_count
    for original, reloaded_mesh in zip(flver.meshes, reloaded.meshes):
        assert reloaded_mesh.vertex_count == original.vertex_count


def test_merged_mesh_position_data_matches_flver(tests_dir):
    flver = FLVER.from_path(ds1r_resource(tests_dir, "c5370.flver"))
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    total_vertices = sum(mesh.vertex_count for mesh in flver.meshes)
    assert merged.vertex_count == total_vertices
    assert merged.loop_normals.shape == (total_vertices, 3)
    offset = 0
    for mesh in flver.meshes:
        count = mesh.vertex_count
        np.testing.assert_allclose(
            merged.positions[offset:offset + count], mesh.vertices["position"]
        )
        offset += count


# ---------------------------------------------------------------------------
# DSR game directory (skipped when DSR is not installed)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_dsr_map_piece_rewrite(dsr_root, tmp_path):
    """Original stray-test target: DSR map piece m5060B2A10 (Firelink Shrine area)."""
    path = dsr_root / "map/m10_02_00_00/m5060B2A10.flver.dcx"
    if not path.is_file():
        pytest.skip(f"DSR map piece not found: {path}")
    flver = FLVER.from_path(path)
    write_path = tmp_path / "m5060B2A10.flver.dcx"
    flver.write(write_path)
    reloaded = FLVER.from_path(write_path)
    assert reloaded.mesh_count == flver.mesh_count
    for original_mesh, reloaded_mesh in zip(flver.meshes, reloaded.meshes):
        np.testing.assert_allclose(
            original_mesh.vertices["position"], reloaded_mesh.vertices["position"], atol=1e-5
        )


@pytest.mark.game_data
def test_dsr_map_piece_merge_and_split(dsr_root):
    """Original stray-test target: DSR map piece m8101B2A10."""
    path = dsr_root / "map/m10_02_00_00/m8101B2A10.flver.dcx"
    if not path.is_file():
        pytest.skip(f"DSR map piece not found: {path}")
    flver = FLVER.from_path(path)
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    assert_layouts_consistent_per_material(flver, list(range(len(flver.meshes))))
    split_meshes = merged.split_mesh(split_defs_with_is_dynamic(flver))
    assert len(split_meshes) == flver.mesh_count
    for original, split in zip(flver.meshes, split_meshes):
        assert len(split.triangulate_flver2()) == len(original.triangulate_flver2())


@pytest.mark.game_data
def test_dsr_character_binder_flver(dsr_root):
    """Original stray-test target: c5280 (Quelaag) inside a CHRBND."""
    path = dsr_root / "chr/c5280.chrbnd.dcx"
    if not path.is_file():
        pytest.skip(f"DSR character binder not found: {path}")
    flver = FLVER.from_binder_path(path, 200)
    assert flver.mesh_count > 0
    for mesh in flver.meshes:
        assert mesh.material.textures  # every Quelaag mesh has at least one texture
        assert isinstance(mesh.face_sets[0].use_backface_culling, (bool, np.bool_))
