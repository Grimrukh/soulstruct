"""FLVER tests for Bloodborne (FLVER2 version 0x20014).

Rewritten from the old `unittest`-ish module, which read `c2800.flver`, wrote it into the repo
tree, and drew a matplotlib skeleton. The intent (read -> write -> read, plus bone resolution) is
preserved here with real assertions and `tmp_path` output. Bloodborne is not installed on most
machines, so everything runs off the committed `c2800.flver` binary.
"""
from __future__ import annotations

import struct

import numpy as np
import pytest

from soulstruct.flver import FLVER, FaceSetFlags, FLVERVersion
from soulstruct.flver.mesh_tools import MergedMesh
from soulstruct.utilities.maths import AABB


CHR_NAME = "c2800.flver"


def binary_roundtrip(binary_file, tmp_path, name="_roundtrip"):
    """Local copy of the `conftest` helper (pytest `importlib` import mode blocks importing it)."""
    write_path = tmp_path / name
    binary_file.write(write_path)
    return type(binary_file).from_path(write_path)


@pytest.fixture
def bb_chr(resource) -> FLVER:
    return FLVER.from_path(resource(CHR_NAME))


# ---------------------------------------------------------------------------
# Read
# ---------------------------------------------------------------------------


def test_chr_read(bb_chr):
    assert bb_chr.version == FLVERVersion.Bloodborne_DS3_B
    assert not bb_chr.big_endian
    assert bb_chr.mesh_count == 6
    assert bb_chr.bone_count == 106
    assert bb_chr.dummy_count == 68
    assert all(not mesh.invalid_layout for mesh in bb_chr.meshes)


def test_chr_uses_non_strip_face_sets_with_lods(bb_chr):
    """Bloodborne meshes store plain triangles, with LOD and motion-blur face set variants."""
    all_face_sets = [fs for mesh in bb_chr for fs in mesh.face_sets]
    assert all(not fs.is_triangle_strip for fs in all_face_sets)
    flags = {fs.flags for fs in all_face_sets}
    assert flags == {0, 1, 2, 128, 129, 130}
    assert any(fs.has_flag(FaceSetFlags.MotionBlur) for fs in all_face_sets)
    assert any(fs.has_flag(FaceSetFlags.LodLevel1) for fs in all_face_sets)


def test_chr_layout_includes_bone_weights_and_two_uv_formats(bb_chr):
    field_names = set()
    for mesh in bb_chr:
        field_names |= mesh.unique_field_names
    assert "bone_weights" in field_names
    assert "bone_indices" in field_names
    assert "tangent_0" in field_names
    assert any(name.startswith("uv_") for name in field_names)
    assert all(mesh.is_dynamic for mesh in bb_chr)


def test_chr_bone_resolution(bb_chr):
    """Replaces the old `draw_skeleton()` helper: resolve every bone into armature space."""
    tree = bb_chr.get_bone_tree()
    transforms = tree.get_bone_armature_space_transforms()
    assert len(transforms) == bb_chr.bone_count
    translates = np.array([t[0].data for t in transforms])
    assert np.all(np.isfinite(translates))
    # A humanoid skeleton spans a plausible range around the origin.
    assert translates.max() < 100.0 and translates.min() > -100.0
    # Root bone(s) resolve to their own local translate.
    for root in tree.get_root_bones():
        index = tree.get_bone_index(root)
        np.testing.assert_allclose(transforms[index][0], root.translate)


def test_chr_dummies_reference_bones(bb_chr):
    for dummy in bb_chr.dummies:
        assert -1 <= dummy.parent_bone_index < bb_chr.bone_count
        assert -1 <= dummy.attach_bone_index < bb_chr.bone_count


# ---------------------------------------------------------------------------
# Binary round-trip
# ---------------------------------------------------------------------------


def test_chr_binary_roundtrip(bb_chr, tmp_path):
    reloaded = binary_roundtrip(bb_chr, tmp_path, name=CHR_NAME)
    assert reloaded.version == bb_chr.version
    assert reloaded.mesh_count == bb_chr.mesh_count
    assert reloaded.bone_count == bb_chr.bone_count
    assert reloaded.dummy_count == bb_chr.dummy_count
    for original, new in zip(bb_chr.meshes, reloaded.meshes):
        assert new.vertex_count == original.vertex_count
        assert new.vertices.dtype == original.vertices.dtype
        for field_name in original.vertices.dtype.names:
            np.testing.assert_allclose(
                original.vertices[field_name], new.vertices[field_name], atol=1e-5,
                err_msg=f"Vertex field '{field_name}' changed on rewrite.",
            )
        assert [fs.flags for fs in new.face_sets] == [fs.flags for fs in original.face_sets]
        for original_fs, new_fs in zip(original.face_sets, new.face_sets):
            np.testing.assert_array_equal(original_fs.vertex_indices, new_fs.vertex_indices)


def test_chr_roundtrip_preserves_dummies(bb_chr, tmp_path):
    reloaded = binary_roundtrip(bb_chr, tmp_path, name=CHR_NAME)
    for original, new in zip(bb_chr.dummies, reloaded.dummies):
        assert new.reference_id == original.reference_id
        assert new.parent_bone_index == original.parent_bone_index
        assert new.attach_bone_index == original.attach_bone_index
        np.testing.assert_allclose(new.translate, original.translate)


@pytest.mark.xfail(
    reason=(
        "BUG: `Dummy` colour bytes are reversed on write for every version except DS2 but reversed "
        "on read only FOR DS2, so dummy colours are byte-flipped by any read->write cycle. (All 68 "
        "c2800 dummies happen to be pure white, so this file cannot detect it; kept as an explicit "
        "check in case a future test binary has coloured dummies.)"
    ),
    strict=False,
)
def test_chr_roundtrip_preserves_dummy_colors(bb_chr, tmp_path):
    bb_chr.dummies[0].color[0] = 1
    bb_chr.dummies[0].color[3] = 4
    expected = tuple(bb_chr.dummies[0].color)
    reloaded = binary_roundtrip(bb_chr, tmp_path, name=CHR_NAME)
    assert tuple(reloaded.dummies[0].color) == expected


@pytest.mark.xfail(
    reason=(
        "BUG: `FaceSet.get_face_counts` never excludes MotionBlur face sets when the indices are "
        "plain triangles (not a strip), so the FLVER header's `true_face_count` is written as the "
        "TOTAL face count. Vanilla c2800 stores 30630 (all faces in non-MotionBlur face sets); "
        "Soulstruct writes 65420."
    ),
    strict=False,
)
def test_chr_roundtrip_preserves_header_true_face_count(bb_chr, resource, tmp_path):
    original_bytes = resource(CHR_NAME).read_bytes()
    vanilla_true, vanilla_total = struct.unpack_from("<2i", original_bytes, 0x40)
    assert (vanilla_true, vanilla_total) == (30630, 65420)  # sanity check on the vanilla file
    written = tmp_path / "rewrite.flver"
    bb_chr.write(written)
    new_true, new_total = struct.unpack_from("<2i", written.read_bytes(), 0x40)
    assert new_total == vanilla_total
    assert new_true == vanilla_true


def test_chr_header_face_counts_are_computable(bb_chr, tmp_path):
    """Total face count IS correct even though `true_face_count` is not (see xfail above)."""
    written = tmp_path / "rewrite.flver"
    bb_chr.write(written)
    _, new_total = struct.unpack_from("<2i", written.read_bytes(), 0x40)
    assert new_total == sum(len(fs.vertex_indices) for mesh in bb_chr for fs in mesh.face_sets)


# ---------------------------------------------------------------------------
# MergedMesh
# ---------------------------------------------------------------------------


def test_merged_mesh_from_bloodborne_character(bb_chr):
    merged = MergedMesh.from_flver(bb_chr, merge_vertices=False)
    total = sum(mesh.vertex_count for mesh in bb_chr.meshes)
    assert merged.vertex_count == total
    assert np.all(np.isfinite(merged.positions))
    assert np.all(np.isfinite(merged.bone_weights))  # BB characters DO store bone weights
    assert merged.loop_normals.shape == (total, 3)
    assert len(merged.loop_tangents) >= 1


def test_bloodborne_bounding_boxes_refresh(bb_chr):
    bb_chr.refresh_bounding_boxes()
    assert bb_chr.bounding_box != AABB.invalid()
    for mesh in bb_chr.meshes:
        assert mesh.uses_bounding_boxes
        assert np.all(np.asarray(mesh.bounding_box.min.data) <= np.asarray(mesh.bounding_box.max.data))


# ---------------------------------------------------------------------------
# Bloodborne game directory (skipped: BB is a console-only game)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_bb_character_from_binder(bb_root):
    path = bb_root / "chr/c2800.chrbnd.dcx"
    if not path.is_file():
        pytest.skip(f"Bloodborne CHRBND not found: {path}")
    flver = FLVER.from_binder_path(path)
    assert flver.version == FLVERVersion.Bloodborne_DS3_B
    assert flver.mesh_count > 0
