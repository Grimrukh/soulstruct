import numpy as np

from soulstruct import FLVER, DSR_PATH
from soulstruct.base.models.flver.mesh_tools import MergedMesh


def main():
    flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m2000B2A10.flver.dcx")
    # flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m5060B2A10.flver.dcx")

    # For testing, throwing away submesh info and just using their FLVER material.
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

    submesh_layouts = list(submesh_layouts_dict.values())
    submesh_kwargs = [
        {
            "is_bind_pose": submesh.is_bind_pose,
            "default_bone_index": submesh.default_bone_index,
            "cull_back_faces": submesh.face_sets[0].cull_back_faces,
        }
        for submesh in flver.submeshes
    ]

    merged.split_mesh(flver.materials, submesh_layouts, submesh_kwargs)


if __name__ == '__main__':
    main()
