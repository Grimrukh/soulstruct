"""Tests for the core `FLVER` class (`soulstruct.flver.core`) and its immediate components
(`FLVERMesh`, `FaceSet`, `Material`, `Texture`, `Dummy`, `FLVERBone`, `BoneTree`).

Almost everything here is a pure-unit test built on a tiny in-memory FLVER, so it runs with no
game data installed. A few tests use the committed DS1R/BB/DS2 binaries via the `resource` fixture
(those live in the per-game test modules; here we only use synthetic models).
"""
from __future__ import annotations

import math

import numpy as np
import pytest

from soulstruct.flver import (
    FLVER,
    FaceSet,
    FaceSetFlags,
    FLVERBone,
    FLVERMesh,
    FLVERVersion,
    GXItem,
    Material,
    Texture,
    VertexArray,
    VertexArrayLayout,
)
from soulstruct.flver.bone import FLVERBoneUsageFlags
from soulstruct.flver.bone_tools import BoneNode, BoneTree
from soulstruct.flver.dummy import ColorRGBA, Dummy
from soulstruct.flver.utilities import hash_material, hash_texture, hash_gx_item, get_all_texture_paths
from soulstruct.flver.vertex_array_layout import (
    VertexBoneIndices,
    VertexBoneWeights,
    VertexColor,
    VertexDataFormatEnum as FE,
    VertexNormal,
    VertexPosition,
    VertexUV,
)
from soulstruct.utilities.binary import BinaryReader, BinaryWriter, ByteOrder
from soulstruct.utilities.maths import AABB, EulerRad, Matrix3, Vector3


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------


QUAD_POSITIONS = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0]]
QUAD_TRIANGLES = np.array([[0, 1, 2], [1, 3, 2]], dtype=np.uint32)


def make_layout(byte_order=ByteOrder.LittleEndian, rigged=False) -> VertexArrayLayout:
    types = [VertexPosition(FE.Float3)]
    if rigged:
        types.append(VertexBoneWeights(FE.FourShortsToFloats))
    types += [
        VertexBoneIndices(FE.FourBytesB),
        VertexNormal(FE.FourBytesC),
        VertexColor(FE.FourBytesC),
        VertexUV(FE.UV),
    ]
    return VertexArrayLayout(types, byte_order=byte_order)


def make_vertex_array(layout: VertexArrayLayout, positions=None, bone_index=0) -> VertexArray:
    positions = QUAD_POSITIONS if positions is None else positions
    _, decompressed_dtype = layout.get_dtypes()
    array = np.zeros(len(positions), dtype=decompressed_dtype)
    array["position"] = positions
    array["bone_indices"] = bone_index
    array["normal"] = [[0.0, 0.0, 1.0]] * len(positions)
    array["normal_w"] = 127
    array["color_0"] = [[1.0, 1.0, 1.0, 1.0]] * len(positions)
    array["uv_0"] = [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]][:len(positions)]
    if "bone_weights" in decompressed_dtype.names:
        array["bone_weights"] = [[1.0, 0.0, 0.0, 0.0]] * len(positions)
    return VertexArray(array=array, layout=layout)


def make_material(name="mat", mat_def="m.mtd", texture_path="tex.tga") -> Material:
    return Material(
        name=name,
        mat_def_path=mat_def,
        textures=[Texture(path=texture_path, texture_type="g_Diffuse")],
    )


def make_mesh(
    layout: VertexArrayLayout = None,
    material: Material = None,
    positions=None,
    is_dynamic=False,
    bone_indices=(0,),
    rigged=False,
) -> FLVERMesh:
    layout = layout if layout is not None else make_layout(rigged=rigged)
    return FLVERMesh(
        is_dynamic=is_dynamic,
        material=material if material is not None else make_material(),
        default_bone_index=0,
        bone_indices=None if bone_indices is None else np.array(bone_indices, dtype=np.int32),
        vertex_arrays=[make_vertex_array(layout, positions)],
        face_sets=[FaceSet.from_triangles(QUAD_TRIANGLES)],
    )


def make_flver(
    version=FLVERVersion.DarkSouls_A,
    big_endian=False,
    meshes=None,
    bones=None,
    dummies=None,
) -> FLVER:
    flver = FLVER(
        version=version,
        big_endian=big_endian,
        meshes=meshes if meshes is not None else [make_mesh()],
        bones=bones if bones is not None else [FLVERBone(name="root")],
        dummies=dummies if dummies is not None else [],
    )
    flver.refresh_mesh_indices()
    flver.refresh_bounding_boxes()
    return flver


def write_read(flver: FLVER) -> FLVER:
    return FLVER.from_bytes(bytes(flver.to_writer().array))


# ---------------------------------------------------------------------------
# Basic construction / properties
# ---------------------------------------------------------------------------


def test_flver_convenience_properties():
    flver = make_flver(
        meshes=[make_mesh(), make_mesh()],
        bones=[FLVERBone(name="root"), FLVERBone(name="child", parent_bone_index=0)],
        dummies=[Dummy(reference_id=200)],
    )
    assert flver.mesh_count == 2
    assert flver.bone_count == 2
    assert flver.dummy_count == 1
    assert list(flver) == flver.meshes  # `__iter__` iterates meshes
    assert "2 meshes" in repr(flver)
    assert "FLVER(" in flver.to_string()
    assert flver.find_bone("child").parent_bone_index == 0
    with pytest.raises(KeyError):
        flver.find_bone("nope")


def test_refresh_mesh_indices():
    flver = make_flver(meshes=[make_mesh(), make_mesh(), make_mesh()])
    for mesh in flver.meshes:
        mesh.index = -1
    flver.refresh_mesh_indices()
    assert [mesh.index for mesh in flver.meshes] == [0, 1, 2]


def test_mesh_shortcut_properties():
    mesh = make_mesh()
    assert mesh.vertex_count == 4
    assert mesh.uv_count == 1
    assert mesh.vertex_color_count == 1
    assert mesh.use_backface_culling is True
    assert mesh.layout is mesh.vertex_arrays[0].layout
    assert mesh.vertices is mesh.vertex_arrays[0].array
    assert mesh.vertices_dtype == mesh.vertex_arrays[0].array.dtype
    assert mesh.can_use_0xffff_separators
    assert "FLVERMesh(" in repr(mesh)


def test_mesh_use_backface_culling_setter_and_mismatch():
    mesh = make_mesh()
    mesh.face_sets.append(FaceSet.from_triangles(QUAD_TRIANGLES, use_backface_culling=False))
    with pytest.raises(ValueError):
        _ = mesh.use_backface_culling
    mesh.use_backface_culling = True
    assert mesh.use_backface_culling is True


def test_mesh_multi_array_shortcuts_raise():
    mesh = make_mesh()
    mesh.vertex_arrays.append(mesh.vertex_arrays[0])
    for prop in ("vertices", "vertices_dtype", "layout"):
        with pytest.raises(ValueError):
            getattr(mesh, prop)


def test_vertex_array_wrapper_api():
    layout = make_layout()
    va = make_vertex_array(layout)
    assert len(va) == 4
    assert va.has_field("position")
    assert not va.has_field("bone_weights")
    assert va.dtype == va.array.dtype
    va["position"] = np.zeros((4, 3), dtype=np.float32)
    assert np.all(va["position"] == 0.0)
    assert not va.guess_has_normal_w_bone_indices  # has real `bone_indices`


def test_guess_has_normal_w_bone_indices():
    layout = VertexArrayLayout([VertexPosition(FE.Float3), VertexNormal(FE.FourBytesC)])
    _, dtype = layout.get_dtypes()
    array = np.zeros(3, dtype=dtype)
    array["normal_w"] = 127
    va = VertexArray(array=array, layout=layout)
    assert not va.guess_has_normal_w_bone_indices
    array["normal_w"][1] = 5
    assert va.guess_has_normal_w_bone_indices


# ---------------------------------------------------------------------------
# Binary round-trips (synthetic models, no game data needed)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "version",
    [
        FLVERVersion.DarkSouls_A,
        FLVERVersion.DarkSouls_B,
        FLVERVersion.DarkSouls2,
        FLVERVersion.Bloodborne_DS3_A,
        FLVERVersion.Bloodborne_DS3_B,
        FLVERVersion.Sekiro_EldenRing,
    ],
)
def test_flver2_write_read_roundtrip(version):
    flver = make_flver(version=version, dummies=[Dummy(reference_id=220)])
    reloaded = write_read(flver)
    assert reloaded.version == version
    assert reloaded.mesh_count == flver.mesh_count
    assert reloaded.bone_count == flver.bone_count
    assert reloaded.dummy_count == flver.dummy_count
    assert reloaded.bones[0].name == "root"
    assert reloaded.meshes[0].material.name == "mat"
    assert reloaded.meshes[0].material.textures[0].path == "tex.tga"
    np.testing.assert_allclose(reloaded.meshes[0].vertices["position"], QUAD_POSITIONS)
    np.testing.assert_array_equal(
        reloaded.meshes[0].face_sets[0].vertex_indices, QUAD_TRIANGLES
    )


@pytest.mark.parametrize("big_endian", [True, False])
def test_flver0_write_read_roundtrip(big_endian):
    """FLVER0 (Demon's Souls) round-trip, exercised without any DeS game data."""
    layout = make_layout(byte_order=ByteOrder.BigEndian if big_endian else ByteOrder.LittleEndian)
    mesh = make_mesh(layout=layout)
    flver = make_flver(version=FLVERVersion.DemonsSouls, big_endian=big_endian, meshes=[mesh])
    reloaded = write_read(flver)
    assert reloaded.version == FLVERVersion.DemonsSouls
    assert reloaded.big_endian == big_endian
    np.testing.assert_allclose(reloaded.meshes[0].vertices["position"], QUAD_POSITIONS)
    np.testing.assert_array_equal(reloaded.meshes[0].face_sets[0].vertex_indices, QUAD_TRIANGLES)
    # FLVER0 mesh bone index arrays are padded out to 28 entries with -1.
    assert len(reloaded.meshes[0].bone_indices) == FLVERMesh.FLVER0_MAX_BONE_COUNT
    assert reloaded.meshes[0].bone_indices[0] == 0


def test_flver0_preserves_bounding_box():
    flver = make_flver(version=FLVERVersion.DemonsSouls, big_endian=True)
    expected = flver.bounding_box
    reloaded = write_read(flver)
    np.testing.assert_allclose(reloaded.bounding_box.min, expected.min)
    np.testing.assert_allclose(reloaded.bounding_box.max, expected.max)


@pytest.mark.xfail(
    reason=(
        "BUG: `FLVER._from_flver2_reader` returns `header.to_object(cls, ...)` without mapping "
        "`bounding_box_min`/`bounding_box_max` to the `bounding_box` field, so the FLVER-wide "
        "bounding box is dropped on read and an invalid (inverted-infinite) AABB is written back."
    ),
    strict=False,
)
def test_flver2_preserves_bounding_box():
    flver = make_flver(version=FLVERVersion.DarkSouls_A)
    expected = flver.bounding_box
    reloaded = write_read(flver)
    np.testing.assert_allclose(reloaded.bounding_box.min, expected.min)
    np.testing.assert_allclose(reloaded.bounding_box.max, expected.max)


def test_flver2_roundtrip_deduplicates_identical_materials_and_layouts():
    """Two meshes with equal (but distinct) materials must pack to a single FLVER material."""
    layout = make_layout()
    meshes = [
        make_mesh(layout=layout, material=make_material()),
        make_mesh(layout=make_layout(), material=make_material()),
    ]
    flver = make_flver(meshes=meshes)
    data = bytes(flver.to_writer().array)
    header = FLVER.STRUCT2.from_bytes(BinaryReader(data))
    assert header.material_count == 1
    assert header.array_layout_count == 1
    assert header.mesh_count == 2
    reloaded = FLVER.from_bytes(data)
    assert reloaded.meshes[0].material == reloaded.meshes[1].material


def test_flver2_roundtrip_keeps_distinct_materials_separate():
    meshes = [
        make_mesh(material=make_material(name="a")),
        make_mesh(material=make_material(name="b")),
    ]
    flver = make_flver(meshes=meshes)
    header = FLVER.STRUCT2.from_bytes(BinaryReader(bytes(flver.to_writer().array)))
    assert header.material_count == 2


def test_flver2_gx_items_roundtrip_with_appended_terminator():
    material = make_material()
    material.gx_items = [GXItem(b"GX00", 100, b"\x01\x02\x03\x04")]
    flver = make_flver(version=FLVERVersion.Bloodborne_DS3_B, meshes=[make_mesh(material=material)])
    reloaded = write_read(flver)
    gx_items = reloaded.meshes[0].material.gx_items
    assert len(gx_items) == 2  # terminator appended automatically on write
    assert gx_items[0].category == b"GX00"
    assert gx_items[0].data == b"\x01\x02\x03\x04"
    assert gx_items[1].is_terminator
    assert reloaded.meshes[0].material.get_non_terminator_gx_items() == [gx_items[0]]


def test_flver_from_path_and_write_path(tmp_path):
    flver = make_flver()
    path = tmp_path / "test.flver"
    flver.write(path)
    reloaded = FLVER.from_path(path)
    assert reloaded.mesh_count == 1
    assert reloaded.path == path


def test_multiple_face_sets_roundtrip():
    """LOD face sets (flags 1 and 2) survive a write/read cycle."""
    mesh = make_mesh()
    for flags in (1, 2):
        mesh.face_sets.append(
            FaceSet(
                flags=flags,
                is_triangle_strip=False,
                use_backface_culling=True,
                unk_x06=0,
                vertex_indices=QUAD_TRIANGLES.copy(),
            )
        )
    flver = make_flver(version=FLVERVersion.Bloodborne_DS3_B, meshes=[mesh])
    reloaded = write_read(flver)
    assert [fs.flags for fs in reloaded.meshes[0].face_sets] == [0, 1, 2]


# ---------------------------------------------------------------------------
# Bounding boxes
# ---------------------------------------------------------------------------


def test_refresh_bounding_boxes():
    mesh = make_mesh(positions=[[-1.0, -2.0, -3.0], [4.0, 5.0, 6.0], [0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
    flver = make_flver(meshes=[mesh])
    flver.refresh_bounding_boxes()
    np.testing.assert_allclose(flver.bounding_box.min, [-1.0, -2.0, -3.0])
    np.testing.assert_allclose(flver.bounding_box.max, [4.0, 5.0, 6.0])
    np.testing.assert_allclose(mesh.bounding_box.min, [-1.0, -2.0, -3.0])
    np.testing.assert_allclose(mesh.bounding_box.max, [4.0, 5.0, 6.0])


def test_refresh_bounding_boxes_on_empty_flver():
    flver = FLVER(version=FLVERVersion.DarkSouls_A)
    flver.refresh_bounding_boxes()
    assert flver.bounding_box == AABB.invalid()


def test_mesh_refresh_bounding_boxes_respects_uses_bounding_boxes():
    mesh = make_mesh()
    mesh.uses_bounding_boxes = False
    mesh.bounding_box = AABB.invalid()
    mesh.refresh_bounding_boxes()
    assert mesh.bounding_box == AABB.invalid()


def test_refresh_bone_bounding_boxes_world_space():
    mesh = make_mesh(positions=[[0.0, 0.0, 0.0], [2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 4.0]])
    flver = make_flver(meshes=[mesh], bones=[FLVERBone(name="root")])
    flver.refresh_bone_bounding_boxes(in_local_space=False)
    np.testing.assert_allclose(flver.bones[0].bounding_box.min, [0.0, 0.0, 0.0])
    np.testing.assert_allclose(flver.bones[0].bounding_box.max, [2.0, 3.0, 4.0])


def test_refresh_bone_bounding_boxes_local_space_subtracts_bone_translate():
    mesh = make_mesh(positions=[[10.0, 0.0, 0.0], [12.0, 0.0, 0.0], [10.0, 3.0, 0.0], [10.0, 0.0, 4.0]])
    bone = FLVERBone(name="root", translate=Vector3((10.0, 0.0, 0.0)))
    flver = make_flver(meshes=[mesh], bones=[bone])
    flver.refresh_bone_bounding_boxes(in_local_space=True)
    np.testing.assert_allclose(flver.bones[0].bounding_box.min, [0.0, 0.0, 0.0], atol=1e-6)
    np.testing.assert_allclose(flver.bones[0].bounding_box.max, [2.0, 3.0, 4.0], atol=1e-6)


# ---------------------------------------------------------------------------
# Transform utilities
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    reason=(
        "BUG: `FLVER.scale_all_translations` indexes `position[0]`, `position[1]`, `position[2]` "
        "which are the first three VERTEX ROWS, not the X/Y/Z columns. Only the first three "
        "vertices are scaled, each by a single (wrong) axis factor."
    ),
    strict=False,
)
def test_scale_all_translations_scales_every_vertex():
    flver = make_flver(dummies=[Dummy(translate=Vector3((1.0, 2.0, 3.0)))])
    flver.bones[0].translate = Vector3((1.0, 1.0, 1.0))
    flver.scale_all_translations(2.0)
    np.testing.assert_allclose(flver.bones[0].translate, [2.0, 2.0, 2.0])
    np.testing.assert_allclose(flver.dummies[0].translate, [2.0, 4.0, 6.0])
    np.testing.assert_allclose(
        flver.meshes[0].vertices["position"], np.array(QUAD_POSITIONS) * 2.0
    )


def test_scale_all_translations_does_scale_bones_and_dummies():
    """The bone/dummy half of `scale_all_translations` works even though the vertex half does not."""
    flver = make_flver(dummies=[Dummy(translate=Vector3((1.0, 2.0, 3.0)))])
    flver.bones[0].translate = Vector3((1.0, 1.0, 1.0))
    flver.scale_all_translations(3.0)
    np.testing.assert_allclose(flver.bones[0].translate, [3.0, 3.0, 3.0])
    np.testing.assert_allclose(flver.dummies[0].translate, [3.0, 6.0, 9.0])


def test_debone_map_piece_bakes_bone_translation_into_vertices():
    bone = FLVERBone(name="offset_bone", translate=Vector3((10.0, 20.0, 30.0)))
    mesh = make_mesh(bone_indices=(0,))
    flver = make_flver(meshes=[mesh], bones=[bone])
    flver.debone_map_piece(default_bone_name="m0000B0A10")
    assert len(flver.bones) == 1
    assert flver.bones[0].name == "m0000B0A10"
    expected = np.array(QUAD_POSITIONS) + np.array([10.0, 20.0, 30.0])
    np.testing.assert_allclose(mesh.vertices["position"], expected, atol=1e-5)
    assert np.all(mesh.vertices["bone_indices"] == 0)


def test_debone_map_piece_rejects_dynamic_meshes():
    flver = make_flver(meshes=[make_mesh(is_dynamic=True, rigged=True)])
    with pytest.raises(ValueError, match="is_dynamic"):
        flver.debone_map_piece(default_bone_name="x")


def test_sort_mesh_bone_indices_remaps_vertex_indices():
    layout = make_layout()
    mesh = make_mesh(layout=layout, bone_indices=(5, 2, 9))
    mesh.vertices["bone_indices"] = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [0, 0, 0, 0]]
    flver = make_flver(meshes=[mesh], bones=[FLVERBone(name=f"b{i}") for i in range(10)])
    flver.sort_mesh_bone_indices()
    np.testing.assert_array_equal(mesh.bone_indices, [2, 5, 9])
    # Vertex 0 used local 0 (global bone 5), which is now local index 1.
    np.testing.assert_array_equal(mesh.vertices["bone_indices"][:, 0], [1, 0, 2, 1])


def test_local_to_global_bone_indices():
    mesh = make_mesh(bone_indices=(3, 7))
    mesh.vertices["bone_indices"] = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0]]
    mesh.local_to_global_bone_indices()
    assert mesh.bone_indices is None
    np.testing.assert_array_equal(mesh.vertices["bone_indices"][:, 0], [3, 7, 3, 7])
    with pytest.raises(ValueError):
        mesh.local_to_global_bone_indices()  # already global


# ---------------------------------------------------------------------------
# Bones / BoneTree
# ---------------------------------------------------------------------------


def test_bone_tree_hierarchy_and_armature_transforms():
    """Parent rotated 90 deg about Y; child translated +X locally must end up at -Z in armature space."""
    parent = FLVERBone(name="parent", rotate=EulerRad((0.0, math.pi / 2, 0.0)), child_bone_index=1)
    child = FLVERBone(name="child", translate=Vector3((1.0, 0.0, 0.0)), parent_bone_index=0)
    flver = make_flver(bones=[parent, child])
    tree = flver.get_bone_tree()
    assert [b.name for b in tree.bones] == ["parent", "child"]
    assert tree[1].parent_bone is tree[0]
    assert tree.get_root_bones() == [tree[0]]

    transforms = tree.get_bone_armature_space_transforms()
    np.testing.assert_allclose(transforms[0][0], [0.0, 0.0, 0.0], atol=1e-6)
    np.testing.assert_allclose(transforms[1][0], [0.0, 0.0, -1.0], atol=1e-6)

    # Single-bone accessor must agree with the batch version.
    node_translate, _, _ = tree[1].get_armature_space_transform()
    np.testing.assert_allclose(node_translate, transforms[1][0], atol=1e-6)


def test_bone_tree_armature_transform_roundtrip():
    bones = [
        FLVERBone(name="root", translate=Vector3((1.0, 2.0, 3.0))),
        FLVERBone(name="a", translate=Vector3((0.0, 1.0, 0.0)), rotate=EulerRad((0.3, 0.2, 0.1)), parent_bone_index=0),
        FLVERBone(name="b", translate=Vector3((0.0, 0.0, 2.0)), parent_bone_index=1),
    ]
    flver = make_flver(bones=bones)
    tree = flver.get_bone_tree()
    tree.set_bone_children_siblings()  # REQUIRED: batch transforms walk DOWN via child/sibling refs
    arma = tree.get_bone_armature_space_transforms()
    tree.set_bone_armature_space_transforms(arma)
    arma_again = tree.get_bone_armature_space_transforms()
    for (t0, r0, s0), (t1, r1, s1) in zip(arma, arma_again):
        np.testing.assert_allclose(t0, t1, atol=1e-6)
        np.testing.assert_allclose(r0.data, r1.data, atol=1e-6)
        np.testing.assert_allclose(s0, s1, atol=1e-6)


def test_bone_tree_set_children_siblings():
    bones = [
        FLVERBone(name="root"),
        FLVERBone(name="a", parent_bone_index=0),
        FLVERBone(name="b", parent_bone_index=0),
        FLVERBone(name="c", parent_bone_index=1),
    ]
    tree = make_flver(bones=bones).get_bone_tree()
    tree.set_bone_children_siblings()
    root, a, b, c = tree.bones
    assert root.child_bone is a
    assert a.next_sibling_bone is b
    assert b.previous_sibling_bone is a
    assert a.child_bone is c
    assert root.get_all_immediate_children() == [a, b]
    assert c.get_root_parent() is root
    assert [n.name for n in c.get_all_parents()] == ["root", "a", "c"]


def test_set_bone_tree_writes_indices_back():
    bones = [FLVERBone(name="root"), FLVERBone(name="a", parent_bone_index=0)]
    flver = make_flver(bones=bones)
    tree = flver.get_bone_tree()
    tree.set_bone_children_siblings()
    flver.set_bone_tree(tree)
    assert flver.bones[1].parent_bone_index == 0
    assert flver.bones[0].child_bone_index == 1
    assert flver.bones[0].parent_bone_index == -1


@pytest.mark.xfail(
    reason=(
        "TRAP: `BoneTree.get_bone_armature_space_transforms()` walks DOWN the hierarchy using "
        "`child_bone`/`next_sibling_bone` references, while `BoneNode.get_armature_space_transform()` "
        "walks UP using `parent_bone`. If only parent references are set (a natural way to build a "
        "tree by hand), the batch method silently returns LOCAL transforms for every non-root bone "
        "instead of raising. Call `set_bone_children_siblings()` first."
    ),
    strict=False,
)
def test_batch_and_single_armature_transforms_agree_with_only_parent_refs():
    parent = FLVERBone(name="parent", rotate=EulerRad((0.0, math.pi / 2, 0.0)))
    child = FLVERBone(name="child", translate=Vector3((1.0, 0.0, 0.0)), parent_bone_index=0)
    tree = make_flver(bones=[parent, child]).get_bone_tree()
    batch = tree.get_bone_armature_space_transforms()[1][0]
    single = tree[1].get_armature_space_transform()[0]
    np.testing.assert_allclose(batch, single, atol=1e-6)


def test_bone_tree_nearest_nub_bone():
    bones = [
        FLVERBone(name="R Finger0"),
        FLVERBone(name="R Finger02", parent_bone_index=0),
        FLVERBone(name="R Finger0Nub", parent_bone_index=0),
    ]
    tree = make_flver(bones=bones).get_bone_tree()
    nub = tree.get_nearest_nub_bone(tree[1])
    assert nub is not None and nub.name == "R Finger0Nub"


def test_bone_usage_flags():
    bone = FLVERBone(name="x", usage_flags=FLVERBoneUsageFlags.UNUSED | FLVERBoneUsageFlags.MESH)
    assert bone.usage_flags & FLVERBoneUsageFlags.UNUSED
    assert "UNUSED" in repr(bone)


def test_bone_binary_roundtrip():
    bone = FLVERBone(
        name="test_bone",
        translate=Vector3((1.0, 2.0, 3.0)),
        rotate=EulerRad((0.1, 0.2, 0.3)),
        scale=Vector3((1.0, 1.0, 1.0)),
        bounding_box=AABB(Vector3((-1.0, -1.0, -1.0)), Vector3((1.0, 1.0, 1.0))),
        usage_flags=1,
        parent_bone_index=4,
    )
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    bone.to_flver_writer(writer)
    bone.pack_name(writer, encoding="utf-16-le")
    reader = BinaryReader(bytes(writer.array), byte_order=ByteOrder.LittleEndian)
    reloaded = FLVERBone.from_flver_reader(reader, encoding="utf-16-le")
    assert reloaded.name == "test_bone"
    assert reloaded.parent_bone_index == 4
    assert reloaded.usage_flags == 1
    np.testing.assert_allclose(reloaded.translate, [1.0, 2.0, 3.0])


@pytest.mark.xfail(
    reason=(
        "BUG: `FLVERBone.__eq__` reads `self.parent_bone` / `self._parent_bone_index`, which do not "
        "exist on the slots dataclass (fields are named `parent_bone_index`). Comparing two otherwise "
        "equal bones raises `AttributeError`."
    ),
    strict=False,
)
def test_flver_bone_equality():
    a = FLVERBone(name="x", translate=Vector3((1.0, 0.0, 0.0)))
    b = FLVERBone(name="x", translate=Vector3((1.0, 0.0, 0.0)))
    assert a == b


def test_flver_bone_inequality_short_circuits_on_name():
    """Comparison of bones with different names returns `False` before the broken branch is hit."""
    assert FLVERBone(name="x") != FLVERBone(name="y")


# ---------------------------------------------------------------------------
# Dummies
# ---------------------------------------------------------------------------


def test_dummy_binary_roundtrip_fields():
    dummy = Dummy(
        translate=Vector3((1.0, 2.0, 3.0)),
        forward=Vector3((0.0, 0.0, 1.0)),
        upward=Vector3((0.0, 1.0, 0.0)),
        reference_id=220,
        parent_bone_index=3,
        attach_bone_index=7,
        follows_attach_bone=False,
        use_upward_vector=True,
    )
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    dummy.to_flver_writer(writer, FLVERVersion.DarkSouls_A)
    reader = BinaryReader(bytes(writer.array), byte_order=ByteOrder.LittleEndian)
    reloaded = Dummy.from_flver_reader(reader, FLVERVersion.DarkSouls_A)
    assert reloaded.reference_id == 220
    assert reloaded.parent_bone_index == 3
    assert reloaded.attach_bone_index == 7
    assert reloaded.follows_attach_bone is False
    np.testing.assert_allclose(reloaded.translate, [1.0, 2.0, 3.0])


@pytest.mark.parametrize("version", [FLVERVersion.DarkSouls_A, FLVERVersion.DarkSouls2])
@pytest.mark.xfail(
    reason=(
        "BUG: `Dummy.from_flver_reader` reverses the packed colour bytes for DS2 only, but "
        "`Dummy.to_flver_writer` reverses them for every version EXCEPT DS2. Both branches are "
        "inverted, so a non-symmetric dummy colour is byte-reversed on every write."
    ),
    strict=False,
)
def test_dummy_color_roundtrip(version):
    dummy = Dummy(color=ColorRGBA(1, 2, 3, 4))
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    dummy.to_flver_writer(writer, version)
    reader = BinaryReader(bytes(writer.array), byte_order=ByteOrder.LittleEndian)
    reloaded = Dummy.from_flver_reader(reader, version)
    assert tuple(reloaded.color) == (1, 2, 3, 4)


def test_color_rgba_api():
    color = ColorRGBA(10, 20, 30)
    assert color.a == 255
    assert list(color) == [10, 20, 30, 255]
    assert len(color) == 4
    assert color[1] == 20
    color[1] = 21
    assert color.g == 21
    with pytest.raises(IndexError):
        _ = color[4]
    with pytest.raises(ValueError):
        ColorRGBA(300, 0, 0)
    assert tuple(ColorRGBA.default()) == (255, 255, 255, 255)


# ---------------------------------------------------------------------------
# FaceSet
# ---------------------------------------------------------------------------


def test_face_set_from_triangles_2d_array():
    face_set = FaceSet.from_triangles(QUAD_TRIANGLES)
    assert face_set.vertex_indices.ndim == 2
    assert face_set.vertex_indices.dtype == np.uint32
    assert not face_set.is_triangle_strip


def test_face_set_from_triangles_1d_array_is_reshaped():
    face_set = FaceSet.from_triangles(np.array([0, 1, 2, 1, 3, 2], dtype=np.uint32))
    assert face_set.vertex_indices.shape == (2, 3)


@pytest.mark.xfail(
    reason=(
        "BUG: `FaceSet.from_triangles` builds a flat 1D array when given a list/sequence of triplets "
        "instead of an ndarray, but leaves `is_triangle_strip=False`. The resulting FaceSet cannot be "
        "triangulated or written (both require 2D indices)."
    ),
    strict=False,
)
def test_face_set_from_triangles_list_of_triplets():
    face_set = FaceSet.from_triangles([(0, 1, 2), (1, 3, 2)])
    assert face_set.vertex_indices.shape == (2, 3)
    np.testing.assert_array_equal(face_set.triangulate(uses_0xffff_separators=False), QUAD_TRIANGLES)


def test_face_set_triangulate_non_strip_copies():
    face_set = FaceSet.from_triangles(QUAD_TRIANGLES)
    triangles = face_set.triangulate(uses_0xffff_separators=False)
    np.testing.assert_array_equal(triangles, QUAD_TRIANGLES)
    assert triangles is not face_set.vertex_indices


def test_face_set_triangulate_strip_alternates_winding():
    face_set = FaceSet(
        flags=0,
        is_triangle_strip=True,
        use_backface_culling=True,
        unk_x06=0,
        vertex_indices=np.array([0, 1, 2, 3, 4], dtype=np.uint32),
    )
    triangles = face_set.triangulate(uses_0xffff_separators=False)
    np.testing.assert_array_equal(
        triangles, [[0, 1, 2], [3, 2, 1], [2, 3, 4]]
    )


def test_face_set_triangulate_strip_restart_separator():
    face_set = FaceSet(
        flags=0,
        is_triangle_strip=True,
        use_backface_culling=True,
        unk_x06=0,
        vertex_indices=np.array([0, 1, 2, 0xFFFF, 3, 4, 5], dtype=np.uint32),
    )
    triangles = face_set.triangulate(uses_0xffff_separators=True)
    np.testing.assert_array_equal(triangles, [[0, 1, 2], [3, 4, 5]])


def test_face_set_triangulate_strip_drops_degenerate_faces_by_default():
    face_set = FaceSet(
        flags=0,
        is_triangle_strip=True,
        use_backface_culling=True,
        unk_x06=0,
        vertex_indices=np.array([0, 0, 1, 2], dtype=np.uint32),
    )
    assert len(face_set.triangulate(uses_0xffff_separators=False)) == 1
    assert len(face_set.triangulate(uses_0xffff_separators=False, include_degenerate_faces=True)) == 2


def test_face_set_triangulate_dimension_checks():
    strip = FaceSet(
        flags=0, is_triangle_strip=True, use_backface_culling=True, unk_x06=0,
        vertex_indices=QUAD_TRIANGLES.copy(),
    )
    with pytest.raises(ValueError):
        strip.triangulate(uses_0xffff_separators=False)


def test_face_set_needs_32bit_indices():
    small = FaceSet.from_triangles(QUAD_TRIANGLES)
    assert not small.needs_32bit_indices()
    big = FaceSet.from_triangles(np.array([[0, 1, 70000]], dtype=np.uint32))
    assert big.needs_32bit_indices()


def test_face_set_flags():
    face_set = FaceSet.from_triangles(QUAD_TRIANGLES)
    face_set.flags = int(FaceSetFlags.LodLevel1) | int(FaceSetFlags.MotionBlur)
    assert face_set.has_flag(FaceSetFlags.LodLevel1)
    assert face_set.has_flag(FaceSetFlags.MotionBlur)
    assert not face_set.has_flag(FaceSetFlags.LodLevel2)


def test_face_set_get_face_counts_non_strip():
    face_set = FaceSet.from_triangles(QUAD_TRIANGLES)
    assert face_set.get_face_counts(uses_0xffff_separators=True) == (2, 2)


@pytest.mark.xfail(
    reason=(
        "BUG: `FaceSet.get_face_counts` only excludes MotionBlur face sets in the triangle-strip "
        "branch. For non-strip face sets (all modern games) it returns `(len, len)` unconditionally, "
        "so the FLVER header's `true_face_count` is inflated. Verified against vanilla Bloodborne "
        "c2800.flver: Soulstruct writes 65420 where the vanilla header holds 30630 (= all faces in "
        "face sets without the MotionBlur flag)."
    ),
    strict=False,
)
def test_face_set_get_face_counts_excludes_motion_blur_when_not_a_strip():
    face_set = FaceSet.from_triangles(QUAD_TRIANGLES)
    face_set.flags = int(FaceSetFlags.MotionBlur)
    true_count, total_count = face_set.get_face_counts(uses_0xffff_separators=True)
    assert true_count == 0
    assert total_count == 2


def test_face_set_binary_roundtrip():
    face_set = FaceSet.from_triangles(QUAD_TRIANGLES)
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    face_set.to_flver_writer(writer, vertex_index_bit_size=16, write_index_size=True)
    face_set.pack_vertex_indices(writer, vertex_index_bit_size=16, vertex_indices_offset=writer.position)
    reader = BinaryReader(bytes(writer.array), byte_order=ByteOrder.LittleEndian)
    reloaded = FaceSet.from_flver_reader(reader, header_vertex_index_bit_size=0, vertex_data_offset=0)
    np.testing.assert_array_equal(reloaded.vertex_indices, QUAD_TRIANGLES)
    assert reloaded.vertex_indices.dtype == np.uint32


@pytest.mark.xfail(
    reason=(
        "BUG: `FaceSet.get_connected_vertex_indices` iterates `range(0, len(triangles), 3)` over the "
        "already-2D `(n, 3)` output of `triangulate()`, so it treats three ROWS as one triangle and "
        "returns the wrong connected set."
    ),
    strict=False,
)
def test_face_set_get_connected_vertex_indices():
    # Two disjoint triangles: {0,1,2} and {3,4,5}.
    face_set = FaceSet.from_triangles(np.array([[0, 1, 2], [3, 4, 5]], dtype=np.uint32))
    assert face_set.get_connected_vertex_indices(0) == {0, 1, 2}


# ---------------------------------------------------------------------------
# Material / Texture
# ---------------------------------------------------------------------------


def test_material_display_mask_parsing_and_setting():
    material = Material(name="#01# body")
    assert material.display_mask == 1
    assert material.name_without_display_mask == "body"
    material.display_mask = 12
    assert material.name == "#12# body"
    assert material.display_mask == 12

    plain = Material(name="plain")
    assert plain.display_mask is None
    assert plain.name_without_display_mask == "plain"
    plain.display_mask = 3
    assert plain.name == "#03# plain"

    with pytest.raises(ValueError):
        plain.display_mask = 99


def test_material_mat_def_name_and_stem():
    material = Material(mat_def_path=r"N:\FRPG\data\Material\m.mtd")
    assert material.mat_def_name == "m.mtd"
    assert material.mat_def_stem == "m"
    material.mat_def_name = "other"
    assert material.mat_def_name == "other.mtd"
    material.mat_def_name = "third.matxml"
    assert material.mat_def_name == "third.matxml"
    with pytest.raises(ValueError):
        material.mat_def_name = "bad.png"


def test_material_texture_helpers():
    material = Material(
        textures=[
            Texture(path=r"N:\map\tex\a.tga", texture_type="g_Diffuse"),
            Texture(path=r"N:\map\tex\b.tga", texture_type="g_Bumpmap"),
        ]
    )
    assert set(material.get_texture_dict()) == {"g_Diffuse", "g_Bumpmap"}
    assert material.find_texture_type("g_Diffuse").stem == "a"
    assert material.find_texture_type("g_Missing") is None
    assert material.get_shared_texture_path_prefix() == "N:\\map\\tex\\"
    material.replace_in_all_texture_names("a.tga", "c.tga")
    assert material.textures[0].name == "c.tga"

    material.textures.append(Texture(path="dupe.tga", texture_type="g_Diffuse"))
    with pytest.raises(KeyError):
        material.get_texture_dict()


def test_texture_name_helpers():
    texture = Texture(path=r"N:\map\tex\a.tga", texture_type="g_Diffuse")
    assert texture.name == "a.tga"
    assert texture.stem == "a"
    assert texture.path_parent == "N:\\map\\tex\\"
    texture.set_name("b.tpf")
    assert texture.name == "b.tga"
    empty = Texture()
    assert empty.name == "" and empty.stem == ""


def test_material_get_mesh_users():
    material = make_material()
    flver = make_flver(meshes=[make_mesh(material=material), make_mesh(material=make_material(name="other"))])
    users = material.get_mesh_users(flver)
    assert len(users) == 1
    assert users[0] is flver.meshes[0]


def test_material_non_terminator_gx_items_rejects_misplaced_terminator():
    material = make_material()
    material.gx_items = [GXItem.new_terminator(), GXItem(b"GX00", 100, b"")]
    with pytest.raises(ValueError):
        material.get_non_terminator_gx_items()


def test_gx_item_binary_roundtrip():
    item = GXItem(b"GX00", 102, b"\x01\x02\x03\x04")
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    item.to_writer(writer)
    reloaded = GXItem.from_bytes(bytes(writer.array))
    assert reloaded == item
    assert not reloaded.is_terminator
    assert GXItem.new_terminator().is_terminator
    with pytest.raises(ValueError):
        GXItem(b"XX", 0, b"").to_writer(BinaryWriter())


def test_hash_helpers_are_stable_and_discriminating():
    a = make_material()
    b = make_material()
    assert hash_material(a) == hash_material(b)
    b.name = "different"
    assert hash_material(a) != hash_material(b)
    assert hash_texture(a.textures[0]) == hash_texture(make_material().textures[0])
    assert hash_gx_item(GXItem(b"GX00", 1, b"a")) == hash_gx_item(GXItem(b"GX00", 1, b"a"))


@pytest.mark.xfail(
    reason=(
        "BUG/doc mismatch: `get_all_texture_paths` docstring says it ignores textures with an empty "
        "`path`, but it has no such filter, so `Path('')` (i.e. `Path('.')`) is returned."
    ),
    strict=False,
)
def test_get_all_texture_paths_ignores_empty_paths():
    material = make_material()
    material.textures.append(Texture(path="", texture_type="g_Bumpmap"))
    flver = make_flver(meshes=[make_mesh(material=material)])
    paths = get_all_texture_paths(flver)
    assert len(paths) == 1


def test_texture_type_none_requires_optional_flag():
    texture = Texture(path="a.tga", texture_type=None)
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    texture.to_flver0_writer(writer)
    with pytest.raises(ValueError, match="texture_type == None"):
        texture.pack_strings(writer, encoding="utf-16-le")


def test_texture_type_none_written_when_optional():
    texture = Texture(path="a.tga", texture_type=None)
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    texture.to_flver0_writer(writer)
    texture.pack_strings(writer, encoding="utf-16-le", texture_type_optional=True)
    data = bytes(writer.array)
    reader = BinaryReader(data, byte_order=ByteOrder.LittleEndian)
    reloaded = Texture.from_flver0_reader(reader, encoding="utf-16-le")
    assert reloaded.path == "a.tga"
    assert reloaded.texture_type is None


@pytest.mark.xfail(
    reason=(
        "BUG: `Material.pack_flver0_data` calls `texture.pack_strings()` without "
        "`texture_type_optional=True`, so a FLVER0 texture that legitimately has no texture type "
        "(offset 0 in the file) cannot be written back out."
    ),
    strict=False,
)
def test_flver0_roundtrip_with_null_texture_type():
    material = Material(name="m", mat_def_path="m.mtd", textures=[Texture(path="a.tga", texture_type=None)])
    flver = make_flver(
        version=FLVERVersion.DemonsSouls, big_endian=True, meshes=[make_mesh(material=material)]
    )
    reloaded = write_read(flver)
    assert reloaded.meshes[0].material.textures[0].texture_type is None


# ---------------------------------------------------------------------------
# Validation / error paths
# ---------------------------------------------------------------------------


def test_flver0_write_rejects_multiple_vertex_arrays():
    mesh = make_mesh()
    mesh.vertex_arrays.append(mesh.vertex_arrays[0])
    flver = make_flver(version=FLVERVersion.DemonsSouls, big_endian=True, meshes=[mesh])
    with pytest.raises(ValueError, match="exactly one VertexArray"):
        flver.to_writer()


def test_flver0_write_rejects_too_many_bone_indices():
    mesh = make_mesh(bone_indices=tuple(range(29)))
    flver = make_flver(version=FLVERVersion.DemonsSouls, big_endian=True, meshes=[mesh])
    with pytest.raises(ValueError, match="bone indices"):
        flver.to_writer()


def test_validate_unique_data_types():
    layout = make_layout()
    mesh = make_mesh(layout=layout)
    mesh.validate_unique_data_types()  # single array, fine
    mesh.vertex_arrays.append(make_vertex_array(make_layout()))
    with pytest.raises(ValueError, match="Unique vertex data type"):
        mesh.validate_unique_data_types()


def test_unrecognized_version_rejected():
    data = bytearray(bytes(make_flver().to_writer().array))
    data[8:12] = (0x99999).to_bytes(4, "little")
    with pytest.raises(ValueError, match="Unrecognized FLVER version"):
        FLVER.from_bytes(bytes(data))


def test_flver_version_helpers():
    assert FLVERVersion.DemonsSouls.is_flver0()
    assert not FLVERVersion.DarkSouls_A.is_flver0()
    assert FLVERVersion.Bloodborne_DS3_A.use_normal_w_bones()
    assert not FLVERVersion.DarkSouls_A.use_normal_w_bones()
    assert FLVERVersion.default() is FLVERVersion.Null


# ---------------------------------------------------------------------------
# OBJ export
# ---------------------------------------------------------------------------


def test_to_obj_contains_vertices_normals_and_uvs():
    flver = make_flver()
    obj = flver.to_obj(name="TestModel")
    assert "o TestModel Mesh 0" in obj
    assert obj.count("\nv ") == 4
    assert obj.count("\nvn ") == 4
    assert obj.count("\nvt ") == 4


@pytest.mark.xfail(
    reason=(
        "BUG: `FLVERMesh.to_obj` iterates `range(0, len(triangles), 3)` and slices `triangles[j:j+3]`, "
        "but `FaceSet.triangulate()` returns an `(n, 3)` 2D array. Each 'vertex index' is therefore a "
        "whole row, and the emitted OBJ face lines look like `f [1 2 3]/[1 2 3]/[1 2 3] ...`."
    ),
    strict=False,
)
def test_to_obj_face_lines_are_valid():
    flver = make_flver()
    obj = flver.to_obj(name="TestModel")
    face_lines = [line for line in obj.splitlines() if line.startswith("f ")]
    assert len(face_lines) == 2
    for line in face_lines:
        assert "[" not in line
        assert len(line.split()) == 4  # 'f' plus three vertex triplets


def test_write_obj(tmp_path):
    flver = make_flver()
    path = tmp_path / "model.obj"
    flver.write_obj(path)
    assert path.is_file()
    assert path.read_text().startswith("o model")


@pytest.mark.xfail(
    reason=(
        "BUG: `FLVERMesh.to_obj` does `if name is None: name = f'{name}{self.index}'`, which "
        "formats the literal `None`, producing an object name like 'None0'."
    ),
    strict=False,
)
def test_mesh_to_obj_default_name():
    mesh = make_mesh()
    mesh.index = 3
    assert "None" not in mesh.to_obj().splitlines()[0]


# ---------------------------------------------------------------------------
# Merged mesh cache API
# ---------------------------------------------------------------------------


"""Material definition files referenced by `Material.mat_def_path` (`soulstruct.base.models`)."""


def test_mtd_param_api():
    from soulstruct.base.models.mtd import MTD, MTDParam, MTDParamType, MTDSampler

    mtd = MTD(
        shader_path=r"N:\shader\FRPG_Phn.spx",
        description="test",
        params=[MTDParam("g_BlendMode", MTDParamType.Int, 2), MTDParam("g_Scale", MTDParamType.Float2, (1.0, 2.0))],
        samplers=[MTDSampler("g_Diffuse", uv_index=1), MTDSampler("g_Bumpmap", uv_index=2)],
    )
    assert mtd.shader_name == "FRPG_Phn.spx"
    assert mtd.shader_stem == "FRPG_Phn"
    assert mtd.has_param("g_BlendMode")
    assert mtd.get_param("g_BlendMode") == 2
    assert mtd.get_param("g_Missing", 7) == 7
    with pytest.raises(KeyError):
        mtd.get_param("g_Missing")
    assert mtd.has_sampler_type("g_Bumpmap")
    assert mtd.get_sampler_type_uv_index("g_Bumpmap") == 2
    with pytest.raises(KeyError):
        mtd.get_sampler_type_uv_index("g_Nope")


def test_mtd_param_type_validation():
    from soulstruct.base.models.mtd import MTDParam, MTDParamType

    assert MTDParamType.Float4.get_value_count() == 4
    assert MTDParamType.Bool.get_value_count() == 1
    assert MTDParam("x", MTDParamType.Int).value == 0
    assert MTDParam("x", MTDParamType.Float3).value == (0.0, 0.0, 0.0)
    with pytest.raises(ValueError):
        MTDParam("x", MTDParamType.Int, "not an int")
    with pytest.raises(ValueError):
        MTDParam("x", MTDParamType.Float2, (1.0, 2.0, 3.0))


@pytest.mark.xfail(
    reason=(
        "BUG: `MTD.to_writer()` (and `MTDParam.to_mtd_writer`) unpack `write_block()` as a 2-tuple "
        "(`file_block, file_block_offset = write_block(...)`) but that function returns a single "
        "int, and then call `block.fill(...)` on an `MTDBlock` NamedTuple that has no `fill` method. "
        "MTD writing is completely broken: `TypeError: cannot unpack non-iterable int object`."
    ),
    strict=False,
)
def test_mtd_write():
    from soulstruct.base.models.mtd import MTD, MTDParam, MTDParamType

    mtd = MTD(shader_path="a.spx", description="d", params=[MTDParam("g_X", MTDParamType.Float, 1.0)])
    data = bytes(mtd.to_writer().array)
    assert data


def test_matbin_param_api():
    from soulstruct.base.models.matbin import MATBIN, MATBINParam, MATBINParamType, MATBINSampler

    matbin = MATBIN(
        shader_path=r"N:\shader\M[A].spx",
        source_path=r"N:\material\M[A].matxml",
        params=[MATBINParam("g_Alpha", MATBINParamType.Float, 0.5)],
        samplers=[MATBINSampler(sampler_type="AlbedoMap", path=r"N:\tex\a.tif")],
    )
    assert matbin.shader_stem == "M[A]"
    assert matbin.source_name == "M[A].matxml"
    assert matbin.has_param("g_Alpha")
    assert matbin.get_param("g_Alpha") == 0.5
    assert matbin.get_param("g_Missing", 1.0) == 1.0
    with pytest.raises(KeyError):
        matbin.get_param("g_Missing")
    assert matbin.has_sampler_type("AlbedoMap")
    assert matbin.get_sampler_stem("AlbedoMap") == "a"
    assert matbin.get_all_sampler_stems() == {"AlbedoMap": "a"}
    with pytest.raises(KeyError):
        matbin.get_sampler_path("Nope")


@pytest.mark.xfail(
    reason=(
        "BUG: `MATBINSampler.unk_x14` uses `field(default_factory=lambda: Vector2.zero)` -- note the "
        "MISSING call parentheses -- so the default value is the bound classmethod itself and "
        "`MATBIN.to_writer()` dies with `TypeError: 'method' object is not iterable`."
    ),
    strict=False,
)
def test_matbin_sampler_default_unk_x14():
    from soulstruct.base.models.matbin import MATBIN, MATBINSampler

    matbin = MATBIN(shader_path="a.spx", source_path="b.matxml", samplers=[MATBINSampler(sampler_type="S")])
    assert bytes(matbin.to_writer().array)


def test_matbin_binary_roundtrip():
    from soulstruct.base.models.matbin import MATBIN, MATBINParam, MATBINParamType, MATBINSampler
    from soulstruct.utilities.maths import Vector2

    matbin = MATBIN(
        shader_path="X.spx",
        source_path="Y.matxml",
        key=1,
        params=[MATBINParam("AAA", MATBINParamType.Int, 5)],
        samplers=[MATBINSampler(sampler_type="S1", path="tex.tif", unk_x14=Vector2.zero())],
    )
    reloaded = MATBIN.from_bytes(bytes(matbin.to_writer().array))
    assert reloaded.shader_path == "X.spx"
    assert reloaded.get_param("AAA") == 5
    assert reloaded.get_sampler_path("S1") == "tex.tif"


def test_merged_mesh_cache_api():
    flver = make_flver()
    assert not flver.has_cached_merged_mesh()
    with pytest.raises(ValueError):
        flver.get_cached_merged_mesh()
    merged = flver.update_cached_merged_mesh()
    assert flver.has_cached_merged_mesh()
    assert flver.get_cached_merged_mesh() is merged
    flver.clear_cached_merged_mesh()
    assert not flver.has_cached_merged_mesh()
