from soulstruct import FLVER, DSR_PATH
from soulstruct.base.models.flver.mesh_tools import MergedMesh


def test_flver_rewrite():
    # flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m2000B2A10.flver.dcx")
    flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m5060B2A10.flver.dcx")

    flver.write("test.flver.dcx")
    re_flver = FLVER.from_path("test.flver.dcx")
    print("FLVER read, written, and re-read successfully? First five vertices of submesh 0 compared below.")
    print(flver.submeshes[0].vertex_arrays[0].array[:5])
    print(re_flver.submeshes[0].vertex_arrays[0].array[:5])


def test_merge_and_split():
    flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m2000B2A10.flver.dcx")

    # TODO: For testing here, throwing away submesh info and just using their FLVER material.
    # Will of course need to create new indices into 'material' representations that include critical submesh fields.
    default_submesh_materials = [flver.materials.index(submesh.material) for submesh in flver.submeshes]

    merged = MergedMesh.from_flver(flver, default_submesh_materials)
    print(f"Merged submeshes of FLVER '{flver.path.name}' successfully ({len(merged.vertex_positions)} vertices).")

    # Test splitter. We need to get data per-submesh. Again, would normally use 'extended material' definitions here.
    materials = flver.materials

    # TODO: This seems general-purpose: getting layouts PER MATERIAL. We can detect if two different submesh arrays use
    #  different layouts for the same material, too.
    submesh_layouts_dict = {}
    for submesh in flver.submeshes:
        material_index = materials.index(submesh.material)
        layout = submesh.vertex_arrays[0].layout
        if material_index not in submesh_layouts_dict:
            submesh_layouts_dict[material_index] = layout
        else:
            assert layout == submesh_layouts_dict[material_index]

    print("Layouts are valid (same for all usages of each material).")

    submesh_info = []
    for submesh in flver.submeshes:
        material_index = materials.index(submesh.material)
        layout = submesh_layouts_dict[material_index]
        submesh_kwargs = {
            "is_bind_pose": submesh.is_bind_pose,
            "default_bone_index": submesh.default_bone_index,
            "cull_back_faces": submesh.cull_back_faces,
        }
        submesh_info.append((material_index, layout, submesh_kwargs))

    split_submeshes = merged.split_mesh(submesh_info)

    for og_submesh, split_submesh in zip(flver.submeshes, split_submeshes):
        og_faces = og_submesh.face_sets[0].triangulate(False)
        print(f"\nOriginal submesh: {len(og_submesh.vertices)} vertices, {len(og_faces)} faces")
        for i in range(5):
            print(f"    Vertex {i}: {og_submesh.vertices[i]}")
        for i in range(5):
            print(f"    Face {i}: {og_faces[i]}")

        split_faces = split_submesh.face_sets[0].triangulate(False)
        print(f"Split submesh: {len(split_submesh.vertices)} vertices, {len(split_faces)} faces")
        for i in range(5):
            print(f"    Vertex {i}: {split_submesh.vertices[i]}")
        for i in range(5):
            print(f"    Face {i}: {split_faces[i]}")

    # for submesh in flver.submeshes:
    #     print(f"Original submesh:")
    #     print(f"    {len(submesh.vertex_arrays[0].array)}, {len(submesh.face_sets[0].triangulate(False))}")


if __name__ == '__main__':
    test_merge_and_split()
