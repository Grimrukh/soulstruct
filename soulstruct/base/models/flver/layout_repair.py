"""Known layouts for certain MTDs."""
from __future__ import annotations

import logging
import typing as tp

from .vertex_array import *
from ..mtd import MTDInfo, MTDShaderCategory

if tp.TYPE_CHECKING:
    from .submesh import Submesh

_LOGGER = logging.getLogger(__name__)


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
        VertexTangent(VertexDataFormatEnum.FourBytesC, 0),  # not actually used by shader, I believe
        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),
    # Ditto.
    "M[D]_Edge.mtd": lambda: VertexArrayLayout([
        VertexPosition(VertexDataFormatEnum.Float3, 0),
        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
        VertexTangent(VertexDataFormatEnum.FourBytesC, 0),  # not actually used by shader, I believe
        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),

    # QLOC exported tangent AND bitangent data for this MTD, even though it has no bumpmap and only one texture, but
    # used the old (correct) layout.
    "A10_02_m9000_M[D].mtd": lambda: VertexArrayLayout([
        VertexPosition(VertexDataFormatEnum.Float3, 0),
        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
        VertexTangent(VertexDataFormatEnum.FourBytesC, 0),  # not actually used by shader, I believe
        VertexBitangent(VertexDataFormatEnum.FourBytesC, 0),  # not actually used by shader, I believe
        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        VertexUV(VertexDataFormatEnum.UV, 0),
    ]),

    # TODO: 'A19_Division[D]_Alp.mtd' in m0001B1A18 has 60-byte vertices but a 32-byte header?
    # TODO: 'A19_Fly[DSB]_edge.mtd' in m0001B1A18 has 60-byte vertices but a 32-byte header?

}


class VertexArrayLayoutFactory:

    type_unk_x00: int

    def __init__(self, unk_x00: int):
        self.type_unk_x00 = unk_x00

    def get_ds1_map_array_layout(self, mtd_info: MTDInfo) -> VertexArrayLayout:
        data_types = [  # always present
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
            # Tangent/Bitangent will be inserted here if needed.
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
            # UV/UVPair will be inserted here if needed.
        ]

        if mtd_info.has_tangent:
            data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesC, 0))
            if mtd_info.has_two_slots:  # still has Bitangent
                # TODO: Why is Bitangent needed for double slots? Does it actually hold a second tangent or something?
                data_types.insert(4, VertexBitangent(VertexDataFormatEnum.FourBytesC, 0))
        elif mtd_info.has_two_slots:  # has Bitangent but not Tangent (probably never happens)
            data_types.insert(3, VertexBitangent(VertexDataFormatEnum.FourBytesC, 0))

        # Calculate total UV map count and use a combination of UVPair and UV format members below.
        uv_count = 1 + int(mtd_info.has_two_slots) + int(mtd_info.has_lightmap)

        if mtd_info.shader_category in {MTDShaderCategory.FOLIAGE, MTDShaderCategory.IVY}:
            # Foliage shaders have two extra UV slots for wind animation control.
            uv_count += 2

        if uv_count > 4:
            # TODO: Might be an unnecessary assertion. True for DS1, for sure.
            raise ValueError(f"Cannot have more than 4 UV maps in a vertex array (got {uv_count}).")

        uv_member_index = 0
        while uv_count > 0:  # extra UVs
            # For odd counts, single UV member is added first.
            if uv_count % 2:
                data_types.append(VertexUV(VertexDataFormatEnum.UV, uv_member_index))
                uv_count -= 1
                uv_member_index += 1
            else:  # must be a non-zero even number remaining
                # Use a UVPair member.
                data_types.append(VertexUV(VertexDataFormatEnum.UVPair, uv_member_index))
                uv_count -= 2
                uv_member_index += 1

        for data_type in data_types:
            data_type.unk_x00 = self.type_unk_x00

        return VertexArrayLayout(data_types)

    def get_ds1_chr_array_layout(self, mtd_info: MTDInfo) -> VertexArrayLayout:
        """Default array layout for character (and probably object) materials in DS1R."""
        data_types = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneWeights(VertexDataFormatEnum.FourShortsToFloats, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
            VertexTangent(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        ]
        if mtd_info.has_two_slots:  # has Bitangent and UVPair
            data_types.insert(5, VertexBitangent(VertexDataFormatEnum.FourBytesC, 0))
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
        else:  # one UV
            data_types.append(VertexUV(VertexDataFormatEnum.UV, 0))

        for data_type in data_types:
            data_type.unk_x00 = self.type_unk_x00

        return VertexArrayLayout(data_types)


def guess_mtd_layout(mtd_name: str, member_unk_00: int, is_chr: bool) -> VertexArrayLayout:
    """Guesses the vertex array layout for a given MTD name. Returns `None` if no guess is possible."""
    mtd_info = MTDInfo.from_mtd_name(mtd_name)
    layout_factory = VertexArrayLayoutFactory(member_unk_00)
    if is_chr:
        return layout_factory.get_ds1_chr_array_layout(mtd_info)
    return layout_factory.get_ds1_map_array_layout(mtd_info)


def check_ds1_layouts(
    array_layouts: list[VertexArrayLayout],
    array_headers: list[VertexArrayHeaderStruct],
    submeshes: list[Submesh],
):
    """
    QLOC really botched some of the FLVERs in DS1R, so we need to know the layouts of the broken ones and manually use
    them instead of whatever is written in the FLVER file. Example map pieces:
        m2120B2A10.flver.dcx
        m8000B2A10.flver.dcx

    Note that this should be called BEFORE submesh vertex arrays/arrays are dereferenced.
    """

    for i, submesh in enumerate(submeshes):
        mtd_name = submesh.material.mtd_name
        # noinspection PyProtectedMember
        for array_index in submesh._vertex_array_indices:
            header = array_headers[array_index]
            layout = array_layouts[header.layout_index]

            if header.vertex_size != (layout_size := layout.get_total_data_size()):
                # BAD LAYOUT. Try to guess the layout from the MTD name.
                _LOGGER.info(
                    f"Attempting to fix bad vertex data layout for submesh {i}.\n"
                    f"    MTD: {mtd_name})\n"
                    f"    Layout size {layout_size} vs. header vertex size {header.vertex_size}"
                )

                if mtd_name in OTHER_CORRECTED_QLOC_LAYOUTS:
                    guessed_layout = OTHER_CORRECTED_QLOC_LAYOUTS[mtd_name]()
                    _LOGGER.info(f"Known layout: {guessed_layout}")
                elif mtd_name in CORRECTED_UNSHADED_QLOC_LAYOUTS:
                    guessed_layout = VertexArrayLayout([
                        VertexPosition(VertexDataFormatEnum.Float3, 0),
                        VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
                        VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
                        VertexColor(VertexDataFormatEnum.FourBytesC, 0),
                        VertexUV(VertexDataFormatEnum.UV, 0),
                    ])
                else:
                    member_unk_00 = layout[0].unk_x00
                    is_chr = submesh.is_bind_pose
                    guessed_layout = guess_mtd_layout(mtd_name, member_unk_00, is_chr)
                    _LOGGER.info(f"Guessed layout: {guessed_layout}")

                guessed_layout_size = guessed_layout.get_total_data_size()
                if guessed_layout_size != header.vertex_size:
                    _LOGGER.error(
                        f"Attempted to repair FLVER layout, but predicted layout size {guessed_layout_size} still does "
                        f"not match header vertex size {header.vertex_size}."
                    )
                else:
                    # New layout works. We do NOT replace the original, as it may be used correctly by other submeshes.
                    header.layout_index = len(array_layouts)
                    array_layouts.append(guessed_layout)

                    # Mesh should now be able to read vertex array correctly...?
                    submesh.layout_fixed = True

    return True
