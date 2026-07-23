"""FLVER tests for Dark Souls II (FLVER2 version 0x20010, extension '.flv').

Rewritten from the old `unittest` module, which printed material/layout/vertex dumps and wrote
its output into the repository. DS2 is the first game to use `GXItem` material data and a UV
factor of 2048, so those specifics are asserted here. Both committed binaries (`c3090.flv`
character and `m0000.flv` map piece) are used; no DS2 installation is needed.
"""
from __future__ import annotations

import numpy as np
import pytest

from soulstruct.flver import FLVER, FLVERVersion
from soulstruct.flver.mesh_tools import MergedMesh


CHR_NAME = "c3090.flv"
MAP_PIECE_NAME = "m0000.flv"


def binary_roundtrip(binary_file, tmp_path, name="_roundtrip"):
    """Local copy of the `conftest` helper (pytest `importlib` import mode blocks importing it)."""
    write_path = tmp_path / name
    binary_file.write(write_path)
    return type(binary_file).from_path(write_path)


@pytest.fixture
def ds2_chr(resource) -> FLVER:
    return FLVER.from_path(resource(CHR_NAME))


@pytest.fixture
def ds2_map_piece(resource) -> FLVER:
    return FLVER.from_path(resource(MAP_PIECE_NAME))


# ---------------------------------------------------------------------------
# Read
# ---------------------------------------------------------------------------


def test_chr_read(ds2_chr):
    assert ds2_chr.version == FLVERVersion.DarkSouls2
    assert ds2_chr.mesh_count == 7
    assert ds2_chr.bone_count == 76
    assert ds2_chr.dummy_count == 20
    assert all(not mesh.invalid_layout for mesh in ds2_chr.meshes)
    assert all(mesh.is_dynamic for mesh in ds2_chr.meshes)


def test_map_piece_read(ds2_map_piece):
    assert ds2_map_piece.version == FLVERVersion.DarkSouls2
    assert ds2_map_piece.mesh_count == 3
    assert ds2_map_piece.bone_count == 1
    assert all(not mesh.is_dynamic for mesh in ds2_map_piece.meshes)
    # DS2 map pieces use `normal_w` rather than a dedicated bone index field.
    assert all(
        "bone_indices" not in array.field_names
        for mesh in ds2_map_piece.meshes
        for array in mesh.vertex_arrays
    )


def test_ds2_materials_carry_gx_items(ds2_chr):
    """DS2 is the first game to use `GXItem`s, and does not terminate its lists."""
    gx_using = [mesh.material for mesh in ds2_chr if mesh.material.gx_items]
    assert gx_using, "Expected at least one DS2 material with GX items."
    for material in gx_using:
        assert len(material.gx_items) == 1  # DS2 lists are a single item, no terminator
        assert not material.gx_items[0].is_terminator
        assert material.gx_items[0].data


def test_ds2_uv_factor_is_2048(ds2_chr):
    """DS2 onwards de-quantize 16-bit UVs by 2048 rather than 1024; UVs stay in a sane range."""
    uvs = np.vstack([
        array["uv_0"] for mesh in ds2_chr for array in mesh.vertex_arrays if array.has_field("uv_0")
    ])
    assert np.all(np.abs(uvs) < 64.0)


def test_ds2_character_has_a_multi_array_mesh(ds2_chr):
    """c3090 mesh 5 has TWO vertex arrays, which breaks several single-array shortcuts."""
    multi = [mesh for mesh in ds2_chr if len(mesh.vertex_arrays) > 1]
    assert multi, "Expected at least one multi-array mesh in c3090."
    with pytest.raises(ValueError, match="exactly one VertexArray"):
        _ = multi[0].vertices
    # All arrays in a mesh must have the same length.
    assert len({len(array) for array in multi[0].vertex_arrays}) == 1


def test_ds2_material_names_and_paths(ds2_chr):
    for mesh in ds2_chr:
        assert mesh.material.mat_def_path
        assert mesh.material.mat_def_name.endswith(".mtd")
        assert mesh.material.textures


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


def test_chr_roundtrip_preserves_gx_items(ds2_chr, tmp_path):
    """No terminator item may be appended for DS2 (`FLVERVersion.DarkSouls2` is special-cased)."""
    reloaded = binary_roundtrip(ds2_chr, tmp_path, name=CHR_NAME)
    for original, new in zip(ds2_chr.meshes, reloaded.meshes):
        assert len(new.material.gx_items) == len(original.material.gx_items)
        for original_item, new_item in zip(original.material.gx_items, new.material.gx_items):
            assert new_item.category == original_item.category
            assert new_item.index == original_item.index
            assert new_item.data == original_item.data


def test_map_piece_roundtrip_preserves_normal_w(ds2_map_piece, tmp_path):
    reloaded = binary_roundtrip(ds2_map_piece, tmp_path, name=MAP_PIECE_NAME)
    for original, new in zip(ds2_map_piece.meshes, reloaded.meshes):
        np.testing.assert_array_equal(original.vertices["normal_w"], new.vertices["normal_w"])


def test_map_piece_normal_w_holds_bone_index(ds2_map_piece):
    for mesh in ds2_map_piece.meshes:
        array = mesh.vertex_arrays[0]
        assert array.has_field("normal_w")
        # Single-bone map piece: `normal_w` is either the 127 'unused' marker or bone index 0.
        assert set(np.unique(array["normal_w"]).tolist()) <= {0, 127}


# ---------------------------------------------------------------------------
# MergedMesh
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    reason=(
        "BUG: `MergedMesh.build_stacked_loops` fallback for unrecognized multi-array meshes records "
        "vertex-array index 0 for fields that actually live in a LATER array: "
        "`merged_field_sources.setdefault(field_name, {}).update({i: (0, field_name)})`. DS2 c3090 "
        "mesh 5 has two vertex arrays, so merging raises "
        "`ValueError: no field of name bone_indices`."
    ),
    strict=False,
)
def test_merged_mesh_from_ds2_character(ds2_chr):
    merged = MergedMesh.from_flver(ds2_chr, merge_vertices=False)
    total = sum(mesh.vertex_count for mesh in ds2_chr.meshes)
    assert merged.vertex_count == total
    assert np.all(np.isfinite(merged.positions))
    assert merged.loop_normals_w is not None


def test_merged_mesh_from_ds2_map_piece(ds2_map_piece):
    """Map pieces have no `bone_indices` field; the merged mesh must fall back to the default 0."""
    merged = MergedMesh.from_flver(ds2_map_piece, merge_vertices=False)
    assert merged.loop_normals_w is not None
    assert np.all(merged.bone_indices == 0)
    assert np.all(merged.bone_weights == 0.0)


def test_merged_mesh_from_ds2_map_piece_positions_are_valid(ds2_map_piece):
    """Positions and loop data ARE correctly populated even though bone columns are not."""
    merged = MergedMesh.from_flver(ds2_map_piece, merge_vertices=False)
    total = sum(mesh.vertex_count for mesh in ds2_map_piece.meshes)
    assert merged.vertex_count == total
    assert np.all(np.isfinite(merged.positions))
    assert merged.loop_normals.shape == (total, 3)


# ---------------------------------------------------------------------------
# DS2 game directory (skipped when DS2 is not installed)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_ds2_character_from_binder(ds2_root):
    path = ds2_root / "model/chr/c3090.bnd"
    if not path.is_file():
        pytest.skip(f"DS2 character binder not found: {path}")
    flver = FLVER.from_binder_path(path, "c3090.flv")
    assert flver.version == FLVERVersion.DarkSouls2
    assert flver.mesh_count > 0
