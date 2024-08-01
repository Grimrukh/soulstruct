from __future__ import annotations

__all__ = [
    "MatDef",
]

import logging
import re
import typing as tp
from dataclasses import dataclass
from enum import IntEnum

from soulstruct.base.models.shaders import MatDef as _BaseMatDef
from soulstruct.base.models.flver.vertex_array import *

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MatDef(_BaseMatDef):

    class UVLayer(IntEnum):
        # TODO: Same as DS1?
        UVTexture0 = 0
        UVTexture1 = 1
        UVLightmap = 2
        UVWindData0 = 3
        UVWindData1 = 4

    SAMPLER_ALIASES: tp.ClassVar[dict[str, str]] = {
        "g_DiffuseTexture": "Main 0 Albedo",  # A
        "g_SpecularTexture": "Main 0 Specular",  # R
        "g_ShininessTexture": "Main 0 Shininess",  # S
        "g_BumpmapTexture": "Main 0 Normal",  # N
        "g_DiffuseTexture2": "Main 1 Albedo",  # NOTE: no underscore before '2' suffix in Bloodborne
        "g_SpecularTexture2": "Main 1 Specular",
        "g_ShininessTexture2": "Main 1 Shininess",
        "g_Bumpmap2": "Main 1 Normal",
        "g_BlendMaskTexture": "Blend 01",
        "g_DisplacementTexture": "Displacement",
        "g_LightmapTexture": "Lightmap",
        "g_DetailBumpmapTexture": "Detail 0 Normal",  # TODO: confirm (if even used)
    }

    SAMPLER_GAME_NAMES: tp.ClassVar[dict[str, str]] = {v: k for k, v in SAMPLER_ALIASES.items()}

    # Class regex patterns for MTD name parsing.
    NAME_BOOL_RE: tp.ClassVar[str, re.Pattern] = {
        "albedo": re.compile(r".*\[.*A.*\].*"),
        "metallic": re.compile(r".*\[.*R.*\].*"),
        "shininess": re.compile(r".*\[.*S.*\].*"),
        "normal": re.compile(r".*\[.*N.*\].*"),
        # "translucent": re.compile(r".*\[.*T.*\].*"),
        "multi": re.compile(r".*_m(_.*|$)"),  # two blended texture slots (ALBEDO, SPECULAR, and/or NORMAL)
        "displacement": re.compile(r".*\[.*H.*\].*"),
        "lightmap": re.compile(r".*_l(_.*|$)"),
        "unshaded": re.compile(r".*\[.*N.*\].*"),
        "normal_to_alpha": re.compile(r".*\[Dn\].*"),  # ALBEDO_0 only
        "wet": re.compile(r".*\[We\].*"),  # NORMAL_0 only
        "alpha": re.compile(r".*_Alp.*"),
        "edge": re.compile(r".*_Edge.*"),
    }

    KNOWN_SHADER_STEMS: tp.ClassVar[dict[str, list[str | re.Pattern]]] = {
        # TODO
    }

    @classmethod
    def get_shader_category(cls, shader_stem: str) -> str:
        """99% of Bloodborne shaders start with 'GXFlver'."""
        return shader_stem.removeprefix("GXFlver_").split("_")[0]

    def get_map_piece_layout(self) -> VertexArrayLayout:
        """Get a standard BB map piece layout with the given number of UV layers.

        TODO: Copied from DS1 currently.
        """

        data_types = [  # always present
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
            # Tangent/Bitangent will be inserted here if needed.
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
            # UV/UVPair will be inserted here if needed.
        ]

        texture_group_count = 0
        if self.get_sampler_with_alias("Main 0 Albedo"):
            texture_group_count += 1
        if self.get_sampler_with_alias("Main 1 Albedo"):
            texture_group_count += 1

        if self.get_sampler_with_alias("Main 0 Normal"):
            # Uses tangent vertex data.
            data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesC, 0))
            if self.get_sampler_with_alias("Main 1 Normal"):
                # Uses bitangent vertex data for second texture group normal.
                data_types.insert(4, VertexBitangent(VertexDataFormatEnum.FourBytesC, 0))
        elif self.get_sampler_with_alias("Main 1 Albedo"):
            # Uses bitangent only. NOTE: I highly doubt any game shaders do this.
            data_types.insert(3, VertexBitangent(VertexDataFormatEnum.FourBytesC, 0))

        uv_member_index = 0
        uv_count = len(self.get_used_uv_layers())
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

    def get_character_layout(self) -> VertexArrayLayout:
        """Get a standard vertex array layout for character (and probably object) materials in BB.

        TODO: Copied from DS1 currently.
        """
        data_types = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneWeights(VertexDataFormatEnum.FourShortsToFloats, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
            VertexTangent(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        ]

        uv_count = len(self.get_used_uv_layers())
        if uv_count == 2:  # has Bitangent and UVPair
            data_types.insert(5, VertexBitangent(VertexDataFormatEnum.FourBytesC, 0))
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
        elif uv_count == 1:  # one UV
            data_types.append(VertexUV(VertexDataFormatEnum.UV, 0))
        else:
            raise ValueError(f"Invalid UV count for BB character layout: {uv_count}. Must be 1 or 2.")

        for data_type in data_types:
            data_type.unk_x00 = 0  # TODO: BB?

        return VertexArrayLayout(data_types)
