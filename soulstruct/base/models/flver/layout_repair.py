"""Known layouts for certain MTDs."""
from __future__ import annotations

import logging
import typing as tp

from .vertex_array import *
from ..mtd import MTDInfo

if tp.TYPE_CHECKING:
    from .submesh import Submesh

_LOGGER = logging.getLogger(__name__)


class VertexDataLayoutFactory:

    type_unk_x00: int

    def __init__(self, unk_x00: int):
        self.type_unk_x00 = unk_x00

    def get_ds1_map_buffer_layout(self, mtd_info: MTDInfo) -> VertexDataLayout:
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

        if mtd_info.is_foliage:
            # Foliage shaders have two extra UV slots for wind animation control.
            uv_count += 2

        if uv_count > 4:
            # TODO: Might be an unnecessary assertion. True for DS1, for sure.
            raise ValueError(f"Cannot have more than 4 UV maps in a vertex buffer (got {uv_count}).")

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

        return VertexDataLayout(data_types)

    def get_ds1_chr_buffer_layout(self, mtd_info: MTDInfo) -> VertexDataLayout:
        """Default buffer layout for character (and probably object) materials in DS1R."""
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

        return VertexDataLayout(data_types)


def guess_mtd_layout(mtd_name: str, member_unk_00: int, is_chr: bool) -> VertexDataLayout:
    """Guesses the vertex buffer layout for a given MTD name. Returns `None` if no guess is possible."""
    mtd_info = MTDInfo.from_mtd_name(mtd_name)
    layout_factory = VertexDataLayoutFactory(member_unk_00)
    if is_chr:
        return layout_factory.get_ds1_chr_buffer_layout(mtd_info)
    return layout_factory.get_ds1_map_buffer_layout(mtd_info)


def check_ds1_layouts(
    buffer_layouts: list[VertexDataLayout],
    buffer_structs: list[VertexBufferStruct],
    submeshes: list[Submesh],
):
    """
    QLOC really botched some of the FLVERs in DS1R, so we need to know the layouts of the broken ones and manually use
    them instead of whatever is written in the FLVER file. Example map pieces:
        m2120B2A10.flver.dcx
        m8000B2A10.flver.dcx

    Note that this should be called BEFORE submesh vertex buffers/arrays are dereferenced.
    """

    for i, submesh in enumerate(submeshes):
        mtd_name = submesh.material.mtd_name
        # noinspection PyProtectedMember
        for buffer_index in submesh._vertex_buffer_indices:
            buffer = buffer_structs[buffer_index]
            layout = buffer_layouts[buffer.layout_index]

            if buffer.vertex_size != layout.get_total_data_size():
                # BAD LAYOUT. Try to guess the layout from the MTD name.
                member_unk_00 = layout[0].unk_x00
                is_chr = submesh.is_bind_pose
                guessed_layout = guess_mtd_layout(mtd_name, member_unk_00, is_chr)
                buffer.layout_index = len(buffer_layouts)
                buffer_layouts.append(guessed_layout)  # new buffer layout (we don't want to replace original!)
                _LOGGER.info(f"Attempting to fix bad vertex data layout for submesh {i} (MTD {mtd_name}).")
                # Mesh should now be able to read vertex buffer correctly.
