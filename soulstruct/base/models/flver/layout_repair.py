"""Known layouts for certain MTDs."""
from __future__ import annotations

import logging
import typing as tp

from .vertex_array_layout import *

if tp.TYPE_CHECKING:
    from .mesh import FLVERMesh
    from .vertex_array import VertexArray

_LOGGER = logging.getLogger("soulstruct")


# List of MTD names for which QLOC incorrectly listed tangents in the exported in DS1R.
CORRECTED_UNSHADED_QLOC_LAYOUTS = {
    "A10_lightshaft[Dn]_Add.mtd",
    "A10_BG_shaft[Dn]_Add_LS.mtd",
    "A10_mist_02[Dn]_Alp.mtd",
    "M_Sky[Dn].mtd",
    "M_Tree[D]_Edge.mtd",
    "S[NL].mtd",
}


# Hard-coded MTD layouts in DS1R that are known to have array-incompatible layouts in FLVER data.
OTHER_CORRECTED_QLOC_LAYOUTS = {

    # QLOC probably saw that `g_LightingType == 3` and so included vertex tangents, even though the MTD has no bumpmap.
    # The layout has no tangents, but the vertex data does.
    "M[D].mtd": lambda: VertexArrayLayout([
        VertexPosition(VertexDataFormatEnum.Float3, 0),
        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
        VertexIgnore(4),  # useless `VertexTangent`
        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),
    # Ditto.
    "M[D]_Edge.mtd": lambda: VertexArrayLayout([
        VertexPosition(VertexDataFormatEnum.Float3, 0),
        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
        VertexIgnore(4),  # useless `VertexTangent`
        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),

    # QLOC exported tangent AND bitangent data for this MTD, even though it has no bumpmap and only one texture, but
    # used the old (correct) layout.
    "A10_02_m9000_M[D].mtd": lambda: VertexArrayLayout([
        VertexPosition(VertexDataFormatEnum.Float3, 0),
        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
        VertexIgnore(8),  # useless `VertexTangent` and `VertexBitangent`
        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),

    # Used for a couple of patches in the Asylum starting cell (m0001B1A18) that aren't really visible anyway.
    # In PTDE, this is just a straightforward no-tangent layout with five members.
    "A19_Division[D]_Alp.mtd": lambda: VertexArrayLayout([
        VertexPosition(VertexDataFormatEnum.Float3, 0),
        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
        # NOTE: We have eight four-byte members that shouldn't be in the vertex data. The first looks like the tangent
        # as expected. Then we have six four-byte sets that are ALMOST always (0, 0, 0, 255). Then we have what looks
        # like a possible bitangent, except it's not normalized. We ignore all of these.
        VertexIgnore(32),  # useless `VertexTangent`, six useless sets, useless `VertexBitangent`
        VertexColor(VertexDataFormatEnum.FourBytesC, 6),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),
    # Used once in DS1, for the swarm of flies in the Asylum starting cell (m0001B1A18).
    # In PTDE, this is just a straightforward no-tangent layout with five members (and the flies actually show).
    "A19_Fly[DSB]_edge.mtd": lambda: VertexArrayLayout([
        VertexPosition(VertexDataFormatEnum.Float3, 0),
        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
        VertexIgnore(32),  # useless `VertexTangent`, six useless sets, useless `VertexBitangent`
        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),

}


def check_ds1_layouts(
    array_layouts: list[VertexArrayLayout],
    array_headers: list[VertexArray.HEADER2],
    flver_meshes: list[FLVERMesh],
):
    """
    QLOC really botched some of the FLVERs in DS1R, so we need to know the layouts of the broken ones and manually use
    them instead of whatever is written in the FLVER file. Example map pieces:
        m2120B2A10.flver.dcx
        m8000B2A10.flver.dcx

    Note that this should be called BEFORE mesh vertex arrays/arrays are dereferenced.
    """

    for i, mesh in enumerate(flver_meshes):
        mtd_name = mesh.material.mat_def_name
        if not mtd_name.endswith(".mtd"):
            continue  # definitely not DS1

        # noinspection PyProtectedMember
        for array_index in mesh._vertex_array_indices:
            header = array_headers[array_index]
            layout = array_layouts[header.layout_index]
            layout_size = layout.get_total_data_size(include_ignored=True)

            if header.vertex_size != layout_size:
                # BAD LAYOUT. Try to guess the layout from the MTD name.
                _LOGGER.info(
                    f"Attempting to fix bad vertex data layout for FLVER mesh {i} (MTD '{mtd_name}', "
                    f"layout size {layout_size} != header vertex size {header.vertex_size})."
                )

                if mtd_name in OTHER_CORRECTED_QLOC_LAYOUTS:
                    guessed_layout = OTHER_CORRECTED_QLOC_LAYOUTS[mtd_name]()
                    # _LOGGER.info(f"Known layout: {guessed_layout}")
                elif mtd_name in CORRECTED_UNSHADED_QLOC_LAYOUTS:
                    guessed_layout = VertexArrayLayout([
                        VertexPosition(VertexDataFormatEnum.Float3, 0),
                        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
                        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
                        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
                        VertexUV(VertexDataFormatEnum.UV, 0),
                    ])
                else:
                    _LOGGER.warning(f"Attempt failed. No corrected DS1R layout known for MTD {mtd_name}.")
                    continue

                guessed_layout_size = guessed_layout.get_total_data_size(include_ignored=True)
                if guessed_layout_size != header.vertex_size:
                    _LOGGER.error(
                        f"Attempted to repair FLVER layout, but predicted layout size {guessed_layout_size} still does "
                        f"not match header vertex size {header.vertex_size}."
                    )
                else:
                    # New layout works. We do NOT replace the original, as it may be used correctly by other meshes.
                    _LOGGER.info(
                        f"Successfully repaired layout for FLVER mesh {i} with MTD '{mtd_name}'. "
                        f"Size: {layout_size} -> {guessed_layout_size}"
                    )
                    header.layout_index = len(array_layouts)
                    array_layouts.append(guessed_layout)

                    # Mesh should now be able to read vertex array correctly...?
                    mesh.layout_fixed = True
