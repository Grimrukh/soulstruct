"""Known layouts for certain MTDs."""
from __future__ import annotations

import logging
import typing as tp

from .vertex import BufferLayout, LayoutMember, MemberFormat, MemberType, VertexBuffer
from ..mtd import MTDInfo

if tp.TYPE_CHECKING:
    from .material import Material
    from .mesh import Mesh

_LOGGER = logging.getLogger(__name__)


class BufferLayoutFactory:

    member_unkx_00: int

    def __init__(self, unkx_00: int):
        self.member_unkx_00 = unkx_00

    def member(self, member_type: MemberType, member_format: MemberFormat, index=0):
        return LayoutMember(
            member_type=member_type,
            member_format=member_format,
            index=index,
            unk_x00=self.member_unkx_00,
        )

    def get_ds1_map_buffer_layout(self, mtd_info: MTDInfo) -> BufferLayout:
        members = [  # always present
            self.member(MemberType.Position, MemberFormat.Float3),
            self.member(MemberType.BoneIndices, MemberFormat.Byte4B),
            self.member(MemberType.Normal, MemberFormat.Byte4C),
            # Tangent/Bitangent will be inserted here if needed.
            self.member(MemberType.VertexColor, MemberFormat.Byte4C),
            # UV/UVPair will be appended here if needed.
        ]

        if not mtd_info.no_tangents:
            members.insert(3, self.member(MemberType.Tangent, MemberFormat.Byte4C))
            if mtd_info.has_two_slots:  # still has Bitangent
                # TODO: Why is Bitangent needed for double slots? Does it actually hold a second tangent or something?
                members.insert(4, self.member(MemberType.Bitangent, MemberFormat.Byte4C))
        elif mtd_info.has_two_slots:  # has Bitangent but not Tangent (probably never happens)
            members.insert(3, self.member(MemberType.Bitangent, MemberFormat.Byte4C))

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
                members.append(self.member(MemberType.UV, MemberFormat.UV, index=uv_member_index))
                uv_count -= 1
                uv_member_index += 1
            else:  # must be a non-zero even number remaining
                # Use a UVPair member.
                members.append(self.member(MemberType.UV, MemberFormat.UVPair, index=uv_member_index))
                uv_count -= 2
                uv_member_index += 1

        return BufferLayout(members)

    def get_ds1_chr_buffer_layout(self, mtd_info: MTDInfo) -> BufferLayout:
        """Default buffer layout for character (and probably object) materials in DS1R."""
        members = [
            self.member(MemberType.Position, MemberFormat.Float3),
            self.member(MemberType.BoneIndices, MemberFormat.Byte4B),
            self.member(MemberType.BoneWeights, MemberFormat.Short4ToFloat4A),
            self.member(MemberType.Normal, MemberFormat.Byte4C),
            self.member(MemberType.Tangent, MemberFormat.Byte4C),
            self.member(MemberType.VertexColor, MemberFormat.Byte4C),
        ]
        if mtd_info.has_two_slots:  # has Bitangent and UVPair
            members.insert(5, self.member(MemberType.Bitangent, MemberFormat.Byte4C))
            members.append(self.member(MemberType.UV, MemberFormat.UVPair))
        else:  # one UV
            members.append(self.member(MemberType.UV, MemberFormat.UV))

        return BufferLayout(members)


def guess_mtd_layout(mtd_name: str, member_unk_00: int, is_chr: bool) -> BufferLayout:
    """Guesses the vertex buffer layout for a given MTD name. Returns `None` if no guess is possible."""
    mtd_info = MTDInfo.from_mtd_name(mtd_name)
    layout_factory = BufferLayoutFactory(member_unk_00)
    if is_chr:
        return layout_factory.get_ds1_chr_buffer_layout(mtd_info)
    return layout_factory.get_ds1_map_buffer_layout(mtd_info)


def check_ds1_layouts(
    buffer_layouts: list[BufferLayout],
    vertex_buffers: dict[int, VertexBuffer],
    meshes: list[Mesh],
    materials: list[Material],
):
    """
    QLOC really botched some of the FLVERs in DS1R, so we need to know the layouts of the broken ones and manually use
    them instead of whatever is written in the FLVER file. Example map pieces:
        m2120B2A10.flver.dcx
        m8000B2A10.flver.dcx
    """

    for i, mesh in enumerate(meshes):
        material = materials[mesh.material_index]
        buffers = [vertex_buffers[i] for i in mesh._vertex_buffer_indices]
        for buffer in buffers:
            layout = buffer_layouts[buffer.layout_index]
            if buffer._struct.vertex_size != layout.get_total_size():
                # BAD LAYOUT.

                # Try to guess the layout from the MTD name.
                member_unk_00 = layout.members[0].unk_x00
                is_chr = mesh.is_bind_pose
                guessed_layout = guess_mtd_layout(material.mtd_name, member_unk_00, is_chr)
                buffer.layout_index = len(buffer_layouts)
                buffer_layouts.append(guessed_layout)  # new buffer layout (we don't want to replace original!)
                _LOGGER.info(f"Fixing bad vertex buffer layout for mesh {i} (MTD {material.mtd_name}).")
                # Mesh should now be able to read vertex buffer correctly.
