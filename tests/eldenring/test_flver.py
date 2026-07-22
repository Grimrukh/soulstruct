"""FLVER tests for Elden Ring (FLVER2 version 0x2001A, shared with Sekiro).

The old module was a stub that tried to read an EMEVD file as a FLVER. There are no committed
Elden Ring FLVER binaries (they only exist inside game Binders), so every test here pulls a
model out of the live `er_root` and skips cleanly when Elden Ring is not installed.

Elden Ring specifics exercised here:
    - `FLVERVersion.Sekiro_EldenRing`, whose mesh bounding boxes carry a third 'unknown' vector;
    - MATBIN material definitions ('.matxml' suffix in FLVER material paths);
    - multi-vertex-array cloth meshes (3 arrays), where array[0] == array[2].
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from soulstruct.flver import FLVER, FLVERVersion
from soulstruct.flver.mesh_tools import MergedMesh


# Small armour part Binder: a single FLVER with ~4k vertices (fast to load).
PARTS_BINDER = "parts/am_f_1540.partsbnd.dcx"


def binary_roundtrip(binary_file, tmp_path, name="_roundtrip"):
    """Local copy of the `conftest` helper (pytest `importlib` import mode blocks importing it)."""
    write_path = tmp_path / name
    binary_file.write(write_path)
    return type(binary_file).from_path(write_path)


def er_binder_path(er_root: Path, relative: str) -> Path:
    path = er_root / relative
    if not path.is_file():
        pytest.skip(f"Elden Ring Binder not found: {path}")
    return path


@pytest.fixture(scope="module")
def er_part_flver(er_root) -> FLVER:
    return FLVER.from_binder_path(er_binder_path(er_root, PARTS_BINDER))


pytestmark = pytest.mark.game_data


# ---------------------------------------------------------------------------
# Read
# ---------------------------------------------------------------------------


def test_part_flver_read(er_part_flver):
    assert er_part_flver.version == FLVERVersion.Sekiro_EldenRing
    assert not er_part_flver.big_endian
    assert er_part_flver.mesh_count >= 1
    assert er_part_flver.bone_count > 0
    assert all(not mesh.invalid_layout for mesh in er_part_flver.meshes)
    for mesh in er_part_flver.meshes:
        assert mesh.vertex_count > 0
        assert mesh.uses_bounding_boxes


def test_part_flver_uses_matbin_material_paths(er_part_flver):
    for mesh in er_part_flver.meshes:
        assert mesh.material.mat_def_path
        # Elden Ring FLVERs reference '.matxml' (MATBIN) material definitions.
        assert mesh.material.mat_def_name.endswith((".matxml", ".mtd"))


def test_part_flver_mesh_bounding_box_unknown_is_present(er_part_flver):
    """Sekiro/ER mesh bounding boxes have a third vector after min/max."""
    for mesh in er_part_flver.meshes:
        assert mesh.bounding_box_unknown is not None
        assert np.all(np.isfinite(np.asarray(mesh.bounding_box_unknown.data)))


def test_part_flver_gx_items_are_terminated(er_part_flver):
    for mesh in er_part_flver.meshes:
        if mesh.material.gx_items:
            assert mesh.material.gx_items[-1].is_terminator


def test_part_flver_bone_tree(er_part_flver):
    tree = er_part_flver.get_bone_tree()
    assert len(tree.bones) == er_part_flver.bone_count
    transforms = tree.get_bone_armature_space_transforms()
    assert all(np.all(np.isfinite(t[0].data)) for t in transforms)


# ---------------------------------------------------------------------------
# Binary round-trip
# ---------------------------------------------------------------------------


def test_part_flver_binary_roundtrip(er_part_flver, tmp_path):
    reloaded = binary_roundtrip(er_part_flver, tmp_path, name="am_f_1540.flver")
    assert reloaded.version == er_part_flver.version
    assert reloaded.mesh_count == er_part_flver.mesh_count
    assert reloaded.bone_count == er_part_flver.bone_count
    assert reloaded.dummy_count == er_part_flver.dummy_count
    for original, new in zip(er_part_flver.meshes, reloaded.meshes):
        assert new.vertex_count == original.vertex_count
        assert len(new.vertex_arrays) == len(original.vertex_arrays)
        for original_array, new_array in zip(original.vertex_arrays, new.vertex_arrays):
            assert new_array.dtype == original_array.dtype
            for field_name in original_array.dtype.names:
                np.testing.assert_allclose(
                    original_array[field_name], new_array[field_name], atol=1e-5,
                    err_msg=f"Vertex field '{field_name}' changed on rewrite.",
                )
        for original_fs, new_fs in zip(original.face_sets, new.face_sets):
            np.testing.assert_array_equal(original_fs.vertex_indices, new_fs.vertex_indices)


def test_part_flver_roundtrip_preserves_materials(er_part_flver, tmp_path):
    reloaded = binary_roundtrip(er_part_flver, tmp_path, name="am_f_1540.flver")
    for original, new in zip(er_part_flver.meshes, reloaded.meshes):
        assert new.material.name == original.material.name
        assert new.material.mat_def_path == original.material.mat_def_path
        assert [t.texture_type for t in new.material.textures] == [
            t.texture_type for t in original.material.textures
        ]
        assert len(new.material.gx_items) == len(original.material.gx_items)


def test_part_flver_roundtrip_preserves_mesh_bounding_boxes(er_part_flver, tmp_path):
    reloaded = binary_roundtrip(er_part_flver, tmp_path, name="am_f_1540.flver")
    for original, new in zip(er_part_flver.meshes, reloaded.meshes):
        np.testing.assert_allclose(new.bounding_box.min, original.bounding_box.min)
        np.testing.assert_allclose(new.bounding_box.max, original.bounding_box.max)
        np.testing.assert_allclose(new.bounding_box_unknown, original.bounding_box_unknown)


# ---------------------------------------------------------------------------
# MergedMesh
# ---------------------------------------------------------------------------


def test_merged_mesh_from_elden_ring_part(er_part_flver):
    merged = MergedMesh.from_flver(er_part_flver, merge_vertices=False)
    total = sum(mesh.vertex_count for mesh in er_part_flver.meshes)
    assert merged.vertex_count == total
    assert np.all(np.isfinite(merged.positions))
    assert merged.loop_normals.shape == (total, 3)
    assert merged.loop_uvs


# ---------------------------------------------------------------------------
# Larger models (slow)
# ---------------------------------------------------------------------------


@pytest.mark.slow
def test_elden_ring_character_flver(er_root):
    """A full ER character (c3200 = Godrick soldier-type) exercises larger bone/mesh counts."""
    path = er_root / "chr/c3200.chrbnd.dcx"
    if not path.is_file():
        pytest.skip(f"Elden Ring CHRBND not found: {path}")
    flver = FLVER.from_binder_path(path)
    assert flver.version == FLVERVersion.Sekiro_EldenRing
    assert flver.mesh_count > 0
    assert flver.bone_count > 0
    assert all(not mesh.invalid_layout for mesh in flver.meshes)


@pytest.mark.slow
def test_elden_ring_multi_array_cloth_mesh(er_root):
    """ER cloth meshes use three vertex arrays where array[0] == array[2] (special-cased in
    `MergedMesh.build_stacked_loops` as `cloth_tangent`/`cloth_bitangent`)."""
    path = er_root / "chr/c0000.chrbnd.dcx"
    if not path.is_file():
        pytest.skip(f"Elden Ring CHRBND not found: {path}")
    flver = FLVER.from_binder_path(path)
    multi_array_meshes = [mesh for mesh in flver.meshes if len(mesh.vertex_arrays) == 3]
    if not multi_array_meshes:
        pytest.skip("No 3-array cloth meshes in this FLVER.")
    for mesh in multi_array_meshes:
        assert np.all(mesh.vertex_arrays[0].array == mesh.vertex_arrays[2].array)
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    assert merged.loop_cloth_tangents is not None
    assert merged.loop_cloth_bitangents is not None
