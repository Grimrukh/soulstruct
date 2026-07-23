"""Tests for `soulstruct.flver.mesh_tools` (`MergedMesh`, `MergedMeshLoops`, `SplitMeshDef`).

All tests here are pure-unit tests built on tiny in-memory FLVERs, so they run without game data.
Game-file merge/split round-trips live in `tests/flver/test_mesh_splitter.py`.
"""
from __future__ import annotations

import numpy as np
import pytest

from soulstruct.flver import (
    FLVER,
    FaceSet,
    FLVERBone,
    FLVERMesh,
    FLVERVersion,
    Material,
    Texture,
    VertexArray,
    VertexArrayLayout,
)
from soulstruct.flver.mesh_tools import MergedMesh, MergedMeshLoops, SplitMeshDef
from soulstruct.flver.vertex_array_layout import (
    VertexBoneIndices,
    VertexBoneWeights,
    VertexColor,
    VertexDataFormatEnum as FE,
    VertexNormal,
    VertexPosition,
    VertexTangent,
    VertexUV,
)
from soulstruct.utilities.binary import ByteOrder


# ---------------------------------------------------------------------------
# Builders (duplicated from `test_flver_core` to avoid cross-module test imports)
# ---------------------------------------------------------------------------


QUAD_POSITIONS = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0]]
QUAD_TRIANGLES = np.array([[0, 1, 2], [1, 3, 2]], dtype=np.uint32)


def make_layout(rigged=False, with_tangent=True) -> VertexArrayLayout:
    types = [VertexPosition(FE.Float3)]
    if rigged:
        types.append(VertexBoneWeights(FE.FourShortsToFloats))
    types.append(VertexBoneIndices(FE.FourBytesB))
    types.append(VertexNormal(FE.FourBytesC))
    if with_tangent:
        types.append(VertexTangent(FE.FourBytesC, 0))
    types += [VertexColor(FE.FourBytesC), VertexUV(FE.UV)]
    return VertexArrayLayout(types, byte_order=ByteOrder.LittleEndian)


def make_vertex_array(layout: VertexArrayLayout, positions=None, bone_index=0) -> VertexArray:
    positions = QUAD_POSITIONS if positions is None else positions
    _, dtype = layout.get_dtypes()
    array = np.zeros(len(positions), dtype=dtype)
    array["position"] = positions
    array["bone_indices"] = bone_index
    array["normal"] = [[0.0, 0.0, 1.0]] * len(positions)
    array["normal_w"] = 127
    if "tangent_0" in dtype.names:
        array["tangent_0"] = [[1.0, 0.0, 0.0, 1.0]] * len(positions)
    array["color_0"] = [[1.0, 1.0, 1.0, 1.0]] * len(positions)
    base_uvs = [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    array["uv_0"] = [base_uvs[i % 4] for i in range(len(positions))]
    if "bone_weights" in dtype.names:
        array["bone_weights"] = [[1.0, 0.0, 0.0, 0.0]] * len(positions)
    return VertexArray(array=array, layout=layout)


def make_material(name="mat") -> Material:
    return Material(name=name, mat_def_path="m.mtd", textures=[Texture(path="t.tga", texture_type="g_Diffuse")])


def make_mesh(layout=None, material=None, positions=None, is_dynamic=False, bone_indices=(0,), rigged=False):
    layout = layout if layout is not None else make_layout(rigged=rigged)
    return FLVERMesh(
        is_dynamic=is_dynamic,
        material=material if material is not None else make_material(),
        default_bone_index=0,
        bone_indices=None if bone_indices is None else np.array(bone_indices, dtype=np.int32),
        vertex_arrays=[make_vertex_array(layout, positions)],
        face_sets=[FaceSet.from_triangles(QUAD_TRIANGLES)],
    )


def make_flver(meshes=None, bones=None, version=FLVERVersion.DarkSouls_A) -> FLVER:
    flver = FLVER(
        version=version,
        meshes=meshes if meshes is not None else [make_mesh()],
        bones=bones if bones is not None else [FLVERBone(name="root")],
    )
    flver.refresh_mesh_indices()
    flver.refresh_bounding_boxes()
    return flver


def make_split_defs(flver: FLVER) -> list[SplitMeshDef]:
    """`SplitMeshDef.get_defs_from_flver()`. `split_mesh()` now correctly sources `is_dynamic` from the

    `SplitMeshDef.is_dynamic` field itself (see finding #17), so no `kwargs` workaround is needed anymore.
    """
    return SplitMeshDef.get_defs_from_flver(flver)


# ---------------------------------------------------------------------------
# MergedMesh construction
# ---------------------------------------------------------------------------


def test_merged_mesh_from_single_mesh_flver():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    assert merged.flver is flver
    assert merged.vertices_merged is True
    assert merged.vertex_count == 4
    assert merged.faces.shape == (2, 4)
    np.testing.assert_array_equal(merged.faces[:, 3], [0, 0])
    np.testing.assert_array_equal(merged.loop_vertex_indices, [0, 1, 2, 3])
    np.testing.assert_allclose(merged.positions, QUAD_POSITIONS)
    assert merged.loop_normals.shape == (4, 3)
    assert len(merged.loop_tangents) == 1
    assert merged.loop_bitangents is None
    assert list(merged.loop_uvs) == ["UVMap0"]
    assert merged.loop_uvs["UVMap0"].shape == (4, 2)
    assert len(merged.loop_vertex_colors) == 1
    assert merged.loop_normals_w is not None


def test_merged_mesh_default_material_indices_are_per_mesh():
    flver = make_flver(meshes=[make_mesh(), make_mesh(), make_mesh()])
    merged = MergedMesh.from_flver(flver)
    assert sorted(set(merged.faces[:, 3].tolist())) == [0, 1, 2]


def test_merged_mesh_explicit_material_indices():
    flver = make_flver(meshes=[make_mesh(), make_mesh(), make_mesh()])
    merged = MergedMesh.from_flver(flver, mesh_material_indices=[0, 0, 1])
    assert sorted(set(merged.faces[:, 3].tolist())) == [0, 1]


def test_merged_mesh_without_merging_keeps_loops_one_to_one():
    flver = make_flver(meshes=[make_mesh(), make_mesh()])
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    assert merged.vertices_merged is False
    assert merged.vertex_count == 8
    np.testing.assert_array_equal(merged.loop_vertex_indices, np.arange(8))
    # Second mesh's face loop indices are offset by the first mesh's vertex count.
    np.testing.assert_array_equal(merged.faces[2:, :3], QUAD_TRIANGLES + 4)


def test_merged_mesh_uv_layer_names():
    flver = make_flver(meshes=[make_mesh(), make_mesh()])
    merged = MergedMesh.from_flver(
        flver, mesh_material_indices=[0, 1], material_uv_layer_names=[["UVTexture0"], ["UVTexture0"]]
    )
    assert list(merged.loop_uvs) == ["UVTexture0"]


def test_merged_mesh_skips_meshes_with_nan_positions():
    bad_mesh = make_mesh()
    bad_mesh.vertices["position"][0] = np.nan
    flver = make_flver(meshes=[make_mesh(), bad_mesh])
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    assert merged.vertex_count == 4  # only the good mesh


def test_merged_mesh_requires_meshes():
    flver = FLVER(version=FLVERVersion.DarkSouls_A)
    with pytest.raises(ValueError, match="no meshes"):
        MergedMesh.from_flver(flver)


def test_merged_mesh_remaps_local_bone_indices_to_global():
    mesh = make_mesh(bone_indices=(4, 9))
    mesh.vertices["bone_indices"] = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0]]
    flver = make_flver(meshes=[mesh], bones=[FLVERBone(name=f"b{i}") for i in range(10)])
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    np.testing.assert_array_equal(merged.bone_indices[:, 0], [4, 9, 4, 9])
    # FLVER itself is not modified.
    assert mesh.bone_indices is not None
    np.testing.assert_array_equal(mesh.vertices["bone_indices"][:, 0], [0, 1, 0, 1])


def test_merged_mesh_bone_weights_are_initialized_when_absent_from_layout():
    flver = make_flver(meshes=[make_mesh(), make_mesh()])
    merged = MergedMesh.from_flver(flver, merge_vertices=False)
    assert "bone_weights" not in flver.meshes[0].vertex_arrays[0].field_names
    assert np.all(merged.bone_weights == 0.0)


def test_merged_mesh_merges_identical_vertices_across_meshes():
    """Two meshes with identical vertex data must share vertices once merged."""
    flver = make_flver(meshes=[make_mesh(rigged=True), make_mesh(rigged=True)])
    merged = MergedMesh.from_flver(flver)
    assert merged.vertex_count == 4  # 8 FLVER vertices -> 4 unique
    np.testing.assert_array_equal(merged.loop_vertex_indices, [0, 1, 2, 3, 0, 1, 2, 3])


def test_merged_mesh_does_not_merge_across_display_masks():
    flver = make_flver(
        meshes=[
            make_mesh(material=make_material(name="#00# a"), rigged=True),
            make_mesh(material=make_material(name="#01# b"), rigged=True),
        ]
    )
    merged = MergedMesh.from_flver(flver)
    assert merged.vertex_count == 8


def test_merged_mesh_marks_unused_vertices():
    """Vertices not referenced by any face are marked with 2**32 - 1 in `loop_vertex_indices`."""
    mesh = make_mesh(positions=QUAD_POSITIONS + [[9.0, 9.0, 9.0]])
    flver = make_flver(meshes=[mesh])
    merged = MergedMesh.from_flver(flver)
    assert merged.loop_vertex_indices[4] == 2 ** 32 - 1


def test_get_stacked_faces_offsets_loop_indices():
    flver = make_flver(meshes=[make_mesh(), make_mesh()])
    faces = MergedMesh.get_stacked_faces(flver.meshes, [0, 1], is_flver0=False)
    assert faces.shape == (4, 4)
    np.testing.assert_array_equal(faces[:2, :3], QUAD_TRIANGLES)
    np.testing.assert_array_equal(faces[2:, :3], QUAD_TRIANGLES + 4)
    np.testing.assert_array_equal(faces[:, 3], [0, 0, 1, 1])


# ---------------------------------------------------------------------------
# MergedMeshLoops
# ---------------------------------------------------------------------------


def test_merged_mesh_loops_get_empty():
    loops = MergedMeshLoops.get_empty(
        {"normal", "normal_w", "tangent_0", "tangent_1", "bitangent", "color_0", "cloth_tangent"}, size=5
    )
    assert loops.normals.shape == (5, 3)
    assert loops.normals_w.shape == (5, 1)
    assert len(loops.tangents) == 2
    assert loops.bitangents.shape == (5, 4)
    assert len(loops.vertex_colors) == 1
    assert loops.cloth_tangents.shape == (5, 4)
    assert loops.cloth_bitangents is None
    assert loops.uvs == {}


def test_merged_mesh_loops_get_empty_rejects_unknown_field():
    with pytest.raises(ValueError, match="Unknown field"):
        MergedMeshLoops.get_empty({"bogus"}, size=1)


def test_merged_mesh_loops_ignores_uv_fields():
    """UV arrays must be built lazily by the caller (they need global layer names)."""
    loops = MergedMeshLoops.get_empty({"uv_0", "uv_1"}, size=3)
    assert loops.uvs == {}


# ---------------------------------------------------------------------------
# In-place transform helpers
# ---------------------------------------------------------------------------


def test_swap_vertex_yz():
    merged = MergedMesh.from_flver(make_flver())
    merged.loop_data.bitangents = np.array([[1.0, 2.0, 3.0, 4.0]] * 4, dtype=np.float32)
    merged.loop_data.tangents = [np.array([[1.0, 2.0, 3.0, 4.0]] * 4, dtype=np.float32)]
    merged.loop_data.normals = np.array([[1.0, 2.0, 3.0]] * 4, dtype=np.float32)
    merged.swap_vertex_yz()
    np.testing.assert_allclose(merged.positions[1], [1.0, 0.0, 0.0])  # (1,0,0) -> (1,0,0)
    np.testing.assert_allclose(merged.positions[2], [0.0, 0.0, 1.0])  # (0,1,0) -> (0,0,1)
    np.testing.assert_allclose(merged.loop_normals[0], [1.0, 3.0, 2.0])
    np.testing.assert_allclose(merged.loop_tangents[0][0], [1.0, 3.0, 2.0, 4.0])
    np.testing.assert_allclose(merged.loop_bitangents[0], [1.0, 3.0, 2.0, 4.0])


def test_invert_vertex_uv():
    merged = MergedMesh.from_flver(make_flver())
    original = merged.loop_uvs["UVMap0"].copy()
    merged.invert_vertex_uv()
    np.testing.assert_allclose(merged.loop_uvs["UVMap0"][:, 0], original[:, 0])
    np.testing.assert_allclose(merged.loop_uvs["UVMap0"][:, 1], 1.0 - original[:, 1])
    merged.invert_vertex_uv(invert_u=True, invert_v=False)
    np.testing.assert_allclose(merged.loop_uvs["UVMap0"][:, 0], 1.0 - original[:, 0])


def test_normalize_normals():
    merged = MergedMesh.from_flver(make_flver())
    merged.loop_data.normals = np.array([[0.0, 0.0, 2.0], [3.0, 4.0, 0.0]], dtype=np.float32)
    merged.normalize_normals()
    np.testing.assert_allclose(merged.loop_normals[0], [0.0, 0.0, 1.0])
    np.testing.assert_allclose(merged.loop_normals[1], [0.6, 0.8, 0.0])


@pytest.mark.xfail(
    reason=(
        "BUG: `MergedMesh.normalize_tangents` divides all FOUR tangent columns by the 4D norm. The "
        "W component is a bitangent-sign flag (+/-1), not part of the vector, so a unit tangent "
        "[1, 0, 0, 1] is scaled to [0.707, 0, 0, 0.707] instead of being left alone. Compare "
        "`normalize_normals`, which correctly operates on a 3-column array."
    ),
    strict=False,
)
def test_normalize_tangents_only_normalizes_xyz():
    merged = MergedMesh.from_flver(make_flver())
    merged.loop_data.tangents = [np.array([[2.0, 0.0, 0.0, 1.0], [0.0, 3.0, 0.0, -1.0]], dtype=np.float32)]
    merged.normalize_tangents()
    np.testing.assert_allclose(merged.loop_tangents[0][0], [1.0, 0.0, 0.0, 1.0])
    np.testing.assert_allclose(merged.loop_tangents[0][1], [0.0, 1.0, 0.0, -1.0])


def test_round_helpers():
    merged = MergedMesh.from_flver(make_flver())
    merged.loop_data.normals = np.array([[0.123456, 0.654321, 0.5]], dtype=np.float32)
    merged.loop_data.tangents = [np.array([[0.123456, 0.0, 0.0, 1.0]], dtype=np.float32)]
    merged.loop_data.uvs["UVMap0"] = np.array([[0.1234567, 0.7654321]], dtype=np.float32)
    merged.round_normals(decimals=2)
    merged.round_tangents(decimals=2)
    merged.round_uvs(decimals=3)
    np.testing.assert_allclose(merged.loop_normals[0], [0.12, 0.65, 0.5], atol=1e-6)
    np.testing.assert_allclose(merged.loop_tangents[0][0], [0.12, 0.0, 0.0, 1.0], atol=1e-6)
    np.testing.assert_allclose(merged.loop_uvs["UVMap0"][0], [0.123, 0.765], atol=1e-6)


def test_normalize_normals_is_a_no_op_without_normals():
    merged = MergedMesh.from_flver(make_flver())
    merged.loop_data.normals = None
    merged.normalize_normals()  # must not raise
    merged.round_normals()


# ---------------------------------------------------------------------------
# Loop reduction
# ---------------------------------------------------------------------------


def _loop_array(rows) -> np.ndarray:
    dtype = np.dtype([("position", "f4", (3,)), ("normal", "f4", (3,))])
    array = np.zeros(len(rows), dtype=dtype)
    for i, (pos, normal) in enumerate(rows):
        array[i]["position"] = pos
        array[i]["normal"] = normal
    return array


def test_loops_to_flver_vertices_exact_preserves_first_appearance_order():
    loops = _loop_array([
        ([2.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
        ([1.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
        ([2.0, 0.0, 0.0], [0.0, 0.0, 1.0]),  # duplicate of row 0
        ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
    ])
    vertices, face_vertex_indices = MergedMesh.loops_to_flver_vertices_exact(loops)
    assert len(vertices) == 3
    # Unsorted: order of first appearance is preserved (np.unique sorts, this must undo it).
    np.testing.assert_allclose(vertices["position"][:, 0], [2.0, 1.0, 0.0])
    np.testing.assert_array_equal(face_vertex_indices, [0, 1, 0, 2])
    # Reconstructing loops from vertices via indices must return the original data.
    np.testing.assert_allclose(vertices[face_vertex_indices]["position"], loops["position"])


def test_loops_to_flver_vertices_exact_keeps_differing_normals_apart():
    loops = _loop_array([
        ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
        ([0.0, 0.0, 0.0], [0.0, 0.0, -1.0]),
    ])
    vertices, indices = MergedMesh.loops_to_flver_vertices_exact(loops)
    assert len(vertices) == 2
    np.testing.assert_array_equal(indices, [0, 1])


def test_loops_to_flver_vertices_approx_merges_similar_normals():
    loops = _loop_array([
        ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
        ([0.0, 0.0, 0.0], [0.001, 0.0, 0.999999]),  # nearly identical normal
        ([0.0, 0.0, 0.0], [0.0, 0.0, -1.0]),        # inverted normal
    ])
    vertices, indices = MergedMesh.loops_to_flver_vertices_approx(loops, max_dot_product=0.99)
    assert len(vertices) == 2
    np.testing.assert_array_equal(indices, [0, 0, 1])


def test_loops_to_flver_vertices_approx_never_merges_different_positions():
    loops = _loop_array([
        ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
        ([0.0, 0.0, 0.001], [0.0, 0.0, 1.0]),
    ])
    vertices, indices = MergedMesh.loops_to_flver_vertices_approx(loops, max_dot_product=0.0)
    assert len(vertices) == 2
    np.testing.assert_array_equal(indices, [0, 1])


def test_loops_to_flver_vertices_approx_exact_duplicates_are_reused():
    loops = _loop_array([
        ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
        ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
    ])
    vertices, indices = MergedMesh.loops_to_flver_vertices_approx(loops)
    assert len(vertices) == 1
    np.testing.assert_array_equal(indices, [0, 0])


# ---------------------------------------------------------------------------
# Bone index helpers / sub-splitting
# ---------------------------------------------------------------------------


def test_make_bone_indices_local():
    global_indices = np.array([[10, 20, 10, 30], [30, 30, 20, 10]])
    mesh_bone_indices = np.array([10, 20, 30])
    local = MergedMesh.make_bone_indices_local(global_indices, mesh_bone_indices)
    np.testing.assert_array_equal(local, [[0, 1, 0, 2], [2, 2, 1, 0]])


def test_subsplit_faces_no_split_needed():
    dtype = np.dtype([("bone_indices", "i4", (4,)), ("bone_weights", "f4", (4,))])
    loops = np.zeros(6, dtype=dtype)  # two faces
    loops["bone_indices"] = [[0, 1, 2, 3]] * 6
    loops["bone_weights"] = [[0.25, 0.25, 0.25, 0.25]] * 6
    subsplits = MergedMesh.subsplit_faces(
        0, loops, is_dynamic=True, max_bones_per_mesh=38, unused_bone_indices_are_minus_one=False
    )
    assert len(subsplits) == 1
    material_index, subsplit_loops, bone_indices = subsplits[0]
    assert material_index == 0
    assert len(subsplit_loops) == 6
    np.testing.assert_array_equal(bone_indices, [0, 1, 2, 3])
    # Vertex bone indices are now LOCAL indices into `bone_indices`.
    np.testing.assert_array_equal(subsplit_loops["bone_indices"][0], [0, 1, 2, 3])


def test_subsplit_faces_splits_on_bone_limit():
    dtype = np.dtype([("bone_indices", "i4", (4,)), ("bone_weights", "f4", (4,))])
    loops = np.zeros(9, dtype=dtype)  # three faces, 12 bone slots each
    loops["bone_weights"] = 0.25
    # Face 0 uses bones 0-11, face 1 uses 12-23, face 2 uses 24-35.
    loops["bone_indices"] = np.arange(36).reshape((9, 4))
    subsplits = MergedMesh.subsplit_faces(
        0, loops, is_dynamic=True, max_bones_per_mesh=12, unused_bone_indices_are_minus_one=True
    )
    assert len(subsplits) == 3
    for _, subsplit_loops, bone_indices in subsplits:
        assert len(subsplit_loops) == 3  # one face each
        assert len(bone_indices) == 12


def test_subsplit_faces_rejects_tiny_bone_limit():
    dtype = np.dtype([("bone_indices", "i4", (4,)), ("bone_weights", "f4", (4,))])
    loops = np.zeros(3, dtype=dtype)
    with pytest.raises(ValueError, match="max_bones_per_mesh"):
        MergedMesh.subsplit_faces(
            0, loops, is_dynamic=True, max_bones_per_mesh=4, unused_bone_indices_are_minus_one=True
        )


def test_split_mesh_rejects_bone_limit_below_three():
    merged = MergedMesh.from_flver(make_flver())
    with pytest.raises(ValueError, match="max_bones_per_mesh"):
        merged.split_mesh(make_split_defs(merged.flver), max_bones_per_mesh=2)


# ---------------------------------------------------------------------------
# `SplitMeshDef`
# ---------------------------------------------------------------------------


def test_split_mesh_def_from_flver():
    flver = make_flver(meshes=[make_mesh(), make_mesh(is_dynamic=True, rigged=True)])
    defs = SplitMeshDef.get_defs_from_flver(flver)
    assert len(defs) == 2
    assert defs[0].is_dynamic is False
    assert defs[1].is_dynamic is True
    assert defs[0].kwargs["default_bone_index"] == 0
    assert defs[0].kwargs["use_backface_culling"] is True
    assert defs[0].kwargs["uses_bounding_boxes"] is True
    assert "is_dynamic" not in defs[0].kwargs  # see `test_split_mesh_with_canonical_defs`


def test_split_mesh_def_uv_layer_name_validation():
    layout = make_layout()
    mesh_def = SplitMeshDef(make_material(), layout, False, {}, uv_layer_names=["UVTexture0"])
    assert mesh_def.get_validated_uv_layer_names({"UVTexture0": None}, 0) == ["UVTexture0"]
    # Default names when none given:
    default_def = SplitMeshDef(make_material(), layout, False, {})
    assert default_def.get_validated_uv_layer_names({"UVMap0": None}, 0) == ["UVMap0"]
    # Wrong count:
    bad_count = SplitMeshDef(make_material(), layout, False, {}, uv_layer_names=["a", "b"])
    with pytest.raises(ValueError, match="do not match layout UV count"):
        bad_count.get_validated_uv_layer_names({"a": None, "b": None}, 0)
    # Name not present in merged mesh:
    missing = SplitMeshDef(make_material(), layout, False, {}, uv_layer_names=["Nope"])
    with pytest.raises(ValueError, match="Not all UV layer names"):
        missing.get_validated_uv_layer_names({"UVMap0": None}, 0)


# ---------------------------------------------------------------------------
# Merge -> split round-trips
# ---------------------------------------------------------------------------


def test_split_mesh_with_canonical_defs():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    split_meshes = merged.split_mesh(SplitMeshDef.get_defs_from_flver(flver))
    assert len(split_meshes) == 1


def test_split_mesh_with_unused_vertices():
    mesh = make_mesh(positions=QUAD_POSITIONS + [[9.0, 9.0, 9.0]])
    flver = make_flver(meshes=[mesh])
    merged = MergedMesh.from_flver(flver)
    split_meshes = merged.split_mesh(make_split_defs(flver))
    assert len(split_meshes) == 1


def test_merge_split_roundtrip_preserves_geometry():
    """Merge -> split round-trip (with the `is_dynamic` workaround) must preserve faces and vertices."""
    flver = make_flver(meshes=[make_mesh(material=make_material("a")), make_mesh(material=make_material("b"))])
    merged = MergedMesh.from_flver(flver)
    split_meshes = merged.split_mesh(make_split_defs(flver))
    assert len(split_meshes) == 2
    for original, split in zip(flver.meshes, split_meshes):
        assert split.vertex_count == original.vertex_count
        assert split.is_dynamic == original.is_dynamic
        assert split.material is original.material
        assert len(split.triangulate_flver2()) == len(original.triangulate_flver2())
        # Sort positions for comparison: split vertex order follows first-face-corner appearance.
        np.testing.assert_allclose(
            np.sort(split.vertices["position"], axis=0),
            np.sort(original.vertices["position"], axis=0),
        )


def test_merge_split_roundtrip_can_be_repacked():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    flver.meshes = merged.split_mesh(make_split_defs(flver))
    flver.refresh_bounding_boxes()
    reloaded = FLVER.from_bytes(bytes(flver.to_writer().array))
    assert reloaded.mesh_count == 1
    assert reloaded.meshes[0].vertex_count == 4


def test_split_mesh_ignores_unused_material_indices():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    defs = make_split_defs(flver)
    defs.append(defs[0])  # material index 1 has no faces
    split_meshes = merged.split_mesh(defs)
    assert len(split_meshes) == 1


def test_split_mesh_max_vertex_count():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    with pytest.raises(ValueError, match="maximum of 2"):
        merged.split_mesh(make_split_defs(flver), max_mesh_vertex_count=2)


def test_split_mesh_face_set_count_duplicates_lods():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    defs = make_split_defs(flver)
    defs[0].kwargs["face_set_count"] = 3
    split_meshes = merged.split_mesh(defs)
    assert [fs.flags for fs in split_meshes[0].face_sets] == [0, 1, 2]


def test_split_mesh_face_set_count_validation():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    defs = make_split_defs(flver)
    defs[0].kwargs["face_set_count"] = 4
    with pytest.raises(ValueError, match="face_set_count"):
        merged.split_mesh(defs)


def test_split_mesh_approx_threshold_merges_loops():
    """A dot-product threshold below 1.0 uses the slower approximate loop reduction path."""
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    split_meshes = merged.split_mesh(make_split_defs(flver), normal_tangent_dot_threshold=0.99)
    assert split_meshes[0].vertex_count == 4


def test_get_combined_loop_data_fields():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    dtype = np.dtype([
        ("position", "f4", (3,)),
        ("normal", "f4", (3,)),
        ("UVMap0", "f4", (2,)),
        ("color_0", "f4", (4,)),
    ])
    combined = merged.get_combined_loop_data(dtype)
    assert len(combined) == 4
    np.testing.assert_allclose(combined["position"], QUAD_POSITIONS)
    np.testing.assert_allclose(combined["color_0"], 1.0)


def test_get_combined_loop_data_requires_normals():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    merged.loop_data.normals = None
    with pytest.raises(ValueError, match="normals` is None"):
        merged.get_combined_loop_data(np.dtype([("normal", "f4", (3,))]))


def test_get_combined_loop_data_derives_normal_w_from_bone_indices():
    """Newer games store the single static-mesh bone index in `normal_w`."""
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    merged.vertex_data["bone_indices"] = 3
    merged.loop_data.normals_w = None
    # NOTE: every key in `loop_data.uvs` must appear in the dtype (see next test).
    combined = merged.get_combined_loop_data(np.dtype([("normal_w", "u1", (1,)), ("UVMap0", "f4", (2,))]))
    assert np.all(combined["normal_w"] == 3)


@pytest.mark.xfail(
    reason=(
        "BUG: `MergedMesh.get_combined_loop_data` writes EVERY key of `loop_data.uvs` into the "
        "combined array without checking whether the field exists in the requested dtype, so a "
        "merged mesh that carries a UV layer no split material uses raises "
        "`ValueError: no field of name ...` instead of ignoring it."
    ),
    strict=False,
)
def test_get_combined_loop_data_ignores_unused_uv_layers():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    merged.loop_data.uvs["UVUnused"] = np.zeros((4, 2), dtype=np.float32)
    combined = merged.get_combined_loop_data(np.dtype([("UVMap0", "f4", (2,))]))
    assert combined.dtype.names == ("UVMap0",)


@pytest.mark.xfail(
    reason=(
        "Same root cause as `test_get_combined_loop_data_ignores_unused_uv_layers`: an extra UV "
        "layer in the merged mesh that no `SplitMeshDef` layout consumes breaks `split_mesh()`."
    ),
    strict=False,
)
def test_split_mesh_with_extra_unused_uv_layer():
    flver = make_flver()
    merged = MergedMesh.from_flver(flver)
    merged.loop_data.uvs["UVLightmap"] = np.zeros((4, 2), dtype=np.float32)
    split_meshes = merged.split_mesh(make_split_defs(flver))
    assert len(split_meshes) == 1


# ---------------------------------------------------------------------------
# Static helpers
# ---------------------------------------------------------------------------


def test_is_triangle_degenerate():
    assert MergedMesh.is_triangle_degenerate((0, 0, 1), discard_degenerate_faces=True)
    assert not MergedMesh.is_triangle_degenerate((0, 1, 2), discard_degenerate_faces=True)
    assert not MergedMesh.is_triangle_degenerate((0, 0, 1))  # not discarding

    existing = set()
    assert not MergedMesh.is_triangle_degenerate(
        (0, 1, 2), discard_duplicate_faces=True, existing_face_set=existing
    )
    assert MergedMesh.is_triangle_degenerate(
        (2, 1, 0), discard_duplicate_faces=True, existing_face_set=existing
    )
    with pytest.raises(ValueError, match="existing_face_set"):
        MergedMesh.is_triangle_degenerate((0, 1, 2), discard_duplicate_faces=True)


def test_merged_mesh_unique_helper_does_not_sort_output_values():
    array = np.array([5, 1, 5, 3, 1])
    result = MergedMesh.unique(array)
    np.testing.assert_array_equal(np.sort(result), [1, 3, 5])
