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
    # flver = FLVER.from_path(DSR_PATH + "/map/m10_01_00_00/m3210B1A10.flver.dcx")
    # flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m2000B2A10.flver.dcx")
    flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m5060B2A10.flver.dcx")

    # TODO: For testing here, throwing away submesh info and just using their FLVER material.
    # Will of course need to create new indices into 'material' representations that include critical submesh fields.
    all_materials = []
    submesh_mat_indices = []
    for submesh in flver.submeshes:
        try:
            material_index = all_materials.index(submesh.material)
        except IndexError:
            material_index = len(all_materials)
            all_materials.append(submesh.material)
        submesh_mat_indices.append(material_index)

    merged = MergedMesh.from_flver(flver, submesh_mat_indices)
    print(f"Merged submeshes of FLVER '{flver.path.name}' successfully ({len(merged.vertex_data)} vertices).")

    # TODO: This seems general-purpose: getting layouts PER MATERIAL. We can detect if two different submesh arrays use
    #  different layouts for the same material, too.
    submesh_layouts_dict = {}
    for submesh, material_index in zip(flver.submeshes, submesh_mat_indices):
        layout = submesh.vertex_arrays[0].layout
        if material_index not in submesh_layouts_dict:
            submesh_layouts_dict[material_index] = layout
        else:
            assert layout == submesh_layouts_dict[material_index]

    print("Layouts are valid (same for all usages of each material).")

    submesh_info = []
    for submesh, material_index in zip(flver.submeshes, submesh_mat_indices):
        layout = submesh_layouts_dict[material_index]
        submesh_kwargs = {
            "is_bind_pose": submesh.is_bind_pose,
            "default_bone_index": submesh.default_bone_index,
            "use_backface_culling": submesh.use_backface_culling,
        }
        submesh_info.append((material_index, layout, submesh_kwargs))

    split_submeshes = merged.split_mesh(submesh_info)

    for s, (og_submesh, split_submesh) in enumerate(zip(flver.submeshes, split_submeshes)):

        og_faces = og_submesh.triangulate()
        print(f"\nOriginal submesh: {len(og_submesh.vertices)} vertices, {len(og_faces)} faces")
        for i in range(min(len(og_submesh.vertices), 5)):
            print(f"    Vertex {i}: {og_submesh.vertices[i]}")
        # for i in range(max(0, len(og_submesh.vertices) - 5), len(og_submesh.vertices)):
        #     print(f"    Vertex {i}: {og_submesh.vertices[i]}")
        for i in range(min(len(og_faces), 5)):
            print(f"    Face {i}: {og_faces[i]}")
        for i in range(max(0, len(og_faces) - 5), len(og_faces)):
            print(f"    Face {i}: {og_faces[i]}")
        for vertex_index in og_faces[0]:
            print(f"        Face 0 Vertex {vertex_index}: {og_submesh.vertices[vertex_index]}")

        split_faces = split_submesh.triangulate()
        print(f"Split submesh: {len(split_submesh.vertices)} vertices, {len(split_faces)} faces")
        for i in range(min(len(split_submesh.vertices), 5)):
            print(f"    Vertex {i}: {split_submesh.vertices[i]}")
        # for i in range(max(0, len(split_submesh.vertices) - 5), len(split_submesh.vertices)):
        #     print(f"    Vertex {i}: {split_submesh.vertices[i]}")
        for i in range(min(len(split_faces), 5)):
            print(f"    Face {i}: {split_faces[i]}")
        for i in range(max(0, len(split_faces) - 5), len(split_faces)):
            print(f"    Face {i}: {split_faces[i]}")
        for vertex_index in split_faces[0]:
            print(f"        Face 0 Vertex {vertex_index}: {split_submesh.vertices[vertex_index]}")


def inspect_c5280():
    """
    Trying to figure out why some faces in Quelaag's hair are inverted.

    Documenting Blender materials and their merged submeshes. Backface culling enabled unless (NBC) shown.
        BL 0: Submesh 0-3: Spider body
        BL 1: Submesh 4: Spider eyes
        BL 2: Submesh 5-9: Spider hair (NBC)
        BL 3: Submesh 10-12: Human body
        BL 4: Submesh 13: Human eyelashes (NBC)
        BL 5: Submesh 14: Human eyes
        BL 6: Submesh 15: Human hair, top
        BL 7: Submesh 16: Human hair, long
        BL 8: Submesh 17: Human hair, ponytail
        BL 9: Submesh 18: Human armband
        BL 10: Submesh 19: Sword
        BL 11: Submesh 20: Sword handle (NBC)

    BL 6, hair top, has some inverted faces.

    My first suspicion is about the whopping 1045 "duplicate" faces that were removed by the importer (not in the merged
    mesh, but by catching Blender `BMFace` creations that use the same three vertices). The skipped duplicate faces may
    have been inverted. On the other hand:
        - the only mesh that could possible have these faces already with ANY normals is Blender material 7, which comes
        AFTER the problematic Blender material (6) / submesh (15).

    AH. I think I get it now. The "inverted" faces I'm seeing are REAL; they SHOULD appear, because they are actually
    visible just under Quelaag's fringe. Both sides of her hair are visible at this point, but as the meshes use
    backface culling (for some reason), there must be duplicate faces - possibly with different UVs? - on either side
    of the same vertices.

    So the answer, awkwardly, is that to properly import these "manual back face" models with duplicate faces using
    inverted normals, we do need "duplicate faces" in Blender. That means duplicate vertices.

    The issue here, of course, is that we don't just want to duplicate all three vertices every time we encounter a
    "duplicate face"; it's likely part of a "duplicate" connected mesh segment that should share those duplicate
    vertices.

    The answer may be to include NORMALS in the data used to reduce all vertices to "unique" vertices only in
    `MergedMesh`... except this would almost certainly lead to an excessive number of duplicate vertices that in fact
    should just use custom split normals per-loop in Blender, as I'm doing currently.

    What I would really want to do is get the "face normal" when merging the submeshes and deciding which vertices to
    merge and which to keep separate. This would basically involve doing what I used to do in Blender: iterating over
    all the faces, making a 'vertex hash' that includes the faces' FLVER vertex data AND the mean face normal, and then
    using that hash to retrieve or hash a vertex.

    But I think I can do something a bit better: when merging vertices, do NOT merge vertices whose normals are, say,
    90 degrees or greater apart. This should definitely avoid merging the vertices belonging to faces that are simply
    inverted (~180 degrees apart), but also avoid merging vertices with more subtle per-loop normal differences. (I
    could possible set the threshold even higher, at ~170 degrees, to preserve very sharp outcrops or points on meshes.)

    Doesn't look like there's anyway way to do that that doesn't involve sorting all FLVER vertices, iterating over
    them, and comparing every adjacent pair with a dot product. So maybe the 'face-based' approach would be better and
    not much slower, if at all?

    I should also consider that DIFFERENT MATERIALS should ALWAYS support duplicate faces, as they will genuinely
    appear different. Simply cutting a face out of a submesh because of activity in a different submesh is going to lead
    to an incomplete mesh (rare as it probably is when the faces are NOT inverted).

    Heck, even WITHIN a submesh, they should be supported if they have different UV data, or vertex color, or whatever
    (there aren't many other fields to NOT consider!). Two sides of a planar wall could easily have the same material
    with different texture mapping or transparency, right?

    So... am I giving up on the idea of merging ANY vertices at all? No, that's stupid; having the different materials
    actually share vertices and edges is 90% of the benefit of merging them. It's just OVERLAPPING duplicate faces I
    need to handle.

    Let's imagine a per-face approach:
        - combine all vertices in all submeshes but do NOT reduce them yet
        - instead, keep a dictionary mapping vertex (position, bone_weights, bone_indices) to full vertex row
            - these represent the ordered, 'created' merged vertices
        - also create a 'vertex variant' dictionary mapping the same hashes to inner dictionaries that map normals to
            vertex rows
        - iterate over faces in submesh
        - for each vertex in face:
            - hash vertex by (position, bone_indices, bone_weights)
            - try to retrieve vertex hash
                - if missing, add it to the dictionary (first-time Blender vertex) and use its index
                - if present, compare dot product of normals for each value in the 'vertex variant' subdict:
                    - if dot product is < -0.9, the existing Blender vertex is NOT suitable; normals change too much
                    - create a new 'vertex variant' normal key under this (position, bone_indices, bone_weights) key
            - if ALL THREE vertex hashes are already present, and the normals are all 'mergeable', then:
                - we need to check a third dictionary that tells us which material index added the duplicate face
                - if it's different, create new vertices anyway (different materials with identical face positions)
                - if it's the same, we seem to have a genuine "duplicate" same-material face that should be ignored
        - Blender vertex list and properly indexed face list are now ready!

    Note that the above algorithm does not really care when it encounters packed FLVER faces that seem to use vertices
    with wildly varying normals (e.g. one of the vertex normals is inverted from the other two).
    """

    flver = FLVER.from_binder_path(DSR_PATH + "/chr/c5280.chrbnd.dcx", 200)
    for i, submesh in enumerate(flver.submeshes):
        print(i, submesh.face_sets[0].use_backface_culling, submesh.material.textures[0].stem)


if __name__ == '__main__':
    test_merge_and_split()
    # inspect_c5280()
