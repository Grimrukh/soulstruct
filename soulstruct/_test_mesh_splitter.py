import numpy as np

from soulstruct import FLVER, DSR_PATH
from soulstruct.base.models.flver.mesh_tools import MergedMesh


def main():
    flver = FLVER.from_path(DSR_PATH + "/map/m10_02_00_00/m2000B2A10.flver.dcx")

    merged = MergedMesh.from_flver(flver)

    # Create material dtypes. In this test case, material index is still FLVER material index.
    dtypes = {}
    props = {}
    for submesh in flver.submeshes:

        if submesh.material_index not in dtypes:
            layout = submesh.get_buffer_layout(flver)
            dtypes[submesh.material_index] = layout.get_dtype()

        props[submesh.material_index] = {
            "is_bind_pose": submesh.is_bind_pose,
        }

    submeshes = merged.split_mesh(dtypes, props)

    for submesh in submeshes:
        print(submesh)


if __name__ == '__main__':
    main()
