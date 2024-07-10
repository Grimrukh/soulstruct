from __future__ import annotations

__all__ = [
    "MatDef",
]

import logging
import re
import typing as tp
from dataclasses import dataclass
from enum import IntEnum

from soulstruct.base.models.flver.shaders import MatDef as MatDef
from soulstruct.base.models.flver.vertex_array import *
from soulstruct.utilities.future import StrEnum

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MatDef(MatDef):

    class ShaderCategory(StrEnum):
        """Categories of DS1 MTD shaders."""
        PHN = "FRPG_Phn"
        SFX = "FRPG_Sfx"
        NORMAL_TO_ALPHA = "FRPG_NormalToAlpha"  # used by mist, light shafts, and special 'M_Tree[D]_Edge.mtd'
        WATER = "FRPG_Water"  # any wet surface with normals only and splash effects
        SNOW = "FRPG_Snow"  # has 'g_SnowColor', 'g_SnowHeight', and other 'g_Snow*' params (also used for tar/swamp)
        FOLIAGE = "FRPG_Foliage"  # has 'g_Wind*' params and two extra UV slots for wind animation control
        IVY = "FRPG_Ivy"  # has 'g_Wind*' params and two extra UV slots for wind animation control

    class UVLayer(IntEnum):
        UVTexture0 = 0
        UVTexture1 = 1
        UVLightmap = 2
        UVWindData0 = 3
        UVWindData1 = 4

    SAMPLER_ALIASES: tp.ClassVar[dict[str, str]] = {
        "g_Diffuse": "Main 0 Albedo",
        "g_Specular": "Main 0 Specular",
        "g_Bumpmap": "Main 0 Normal",
        "g_Diffuse_2": "Main 1 Albedo",
        "g_Specular_2": "Main 1 Specular",
        "g_Bumpmap_2": "Main 1 Normal",
        "g_Height": "Displacement",
        "g_Lightmap": "Lightmap",
        "g_DetailBumpmap": "Detail 0 Normal",
    }

    SAMPLER_GAME_NAMES: tp.ClassVar[dict[str, str]] = {v: k for k, v in SAMPLER_ALIASES.items()}

    @property
    def is_water(self):
        return self.shader_category == self.ShaderCategory.WATER

    @property
    def is_snow(self):
        return self.shader_category == self.ShaderCategory.SNOW

    # Class regex patterns for MTD name parsing.
    NAME_TAG_RE: tp.ClassVar[str, re.Pattern] = {
        "Albedo": re.compile(r".*\[.*D.*\].*"),
        "Specular": re.compile(r".*\[.*S.*\].*"),
        # No "Shininess" samplers in DS1.
        "Normal": re.compile(r".*\[.*B.*\].*"),
        "Translucent": re.compile(r".*\[.*T.*\].*"),
        "Multi": re.compile(r".*\[.*M.*\].*"),  # two blended texture slots (ALBEDO, SPECULAR, and/or NORMAL)
        "Displacement": re.compile(r".*\[.*H.*\].*"),
        "Lightmap": re.compile(r".*\[.*L.*\].*"),
        "NormalToAlpha": re.compile(r".*\[(Dn|.*N.*)\].*"),  # Main 0 Albedo only
        "Water": re.compile(r".*\[We\].*"),  # Main 0 Normal only
    }

    NAME_SUFFIX_RE: tp.ClassVar[str, re.Pattern] = {
        "Alpha": re.compile(r".*_Alp.*"),
        "Edge": re.compile(r".*_Edge.*"),
    }

    EXTRA_SHADER_UV_LAYERS: tp.ClassVar[dict[str, list[UVLayer]]] = {
        ShaderCategory.FOLIAGE: [UVLayer.UVWindData0, UVLayer.UVWindData1],
        ShaderCategory.IVY: [UVLayer.UVWindData0, UVLayer.UVWindData1],
    }

    KNOWN_SHADER_MTD_STEMS: tp.ClassVar[dict[str, list[str | re.Pattern]]] = {
        ShaderCategory.WATER: [
            "M_5Water[B]",  # FRPG_Water_Reflect
            "A10_00_Water_drainage",  # FRPG_Water_Reflect
            "A10_01_Water[B]",  # FRPG_Water_Reflect
            "A11_Water[W]",  # FRPG_Water_Reflect
            "A12_Little River",  # FRPG_Water_Reflect
            "A12_River",  # FRPG_Water_Reflect
            "A12_River_No reflect",  # FRPG_Water_Reflect
            "A12_Water",  # FRPG_Water_Reflect
            "A12_Water_lake",  # FRPG_Water_Reflect
            "A14Water[B]",  # FRPG_Water_Reflect
            "S[DB]_Alp_water",  # FRPG_WaterWaveSfx
            "A12_DarkRiver",  # FRPG_Water_Reflect
            "A12_DarkWater",  # FRPG_Water_Reflect
            "A12_NewWater",  # FRPG_Water_Reflect
            "A12_Water_boss",  # FRPG_Water_Reflect
        ],
        ShaderCategory.SNOW: [
            "M_8Snow",  # FRPG_Snow
            "A10_slime[D][L]",  # FRPG_Snow_Lit
            "A11_Snow",  # FRPG_Snow
            "A11_Snow[L]",  # FRPG_Snow_Lit
            "A11_Snow_stair",  # FRPG_Snow
            "A11_Snow_stair[L]",  # FRPG_Snow_Lit
            "A14_numa",  # FRPG_Snow (Blighttown swamp)
            "A14_numa2",  # FRPG_Snow (Blighttown swamp)
            "A15_Tar",  # FRPG_Snow
            "A18_ash",  # FRPG_Snow
            "A19_Snow",  # FRPG_Snow
            "A19_Snow[L]",  # FRPG_Snow_Lit
        ],
        ShaderCategory.FOLIAGE: [
            re.compile(r"^M_2Foliage.*"),
        ],
        ShaderCategory.IVY: [
            re.compile(r"^M_3Ivy.*"),
        ],
        ShaderCategory.NORMAL_TO_ALPHA: [
            "M_Tree[D]_Edge",
        ],
    }

    # Subset of `SNOW_STEMS` that use a 'FRPG_Snow*' SPX shader and also have a 'g_SnowMetalMask' param and an extra
    # 'g_Bumpmap_3' texture type.
    SNOW_METAL_MASK_STEMS: tp.ClassVar[set[str]] = {
        "A10_slime[D][L]",  # FRPG_Snow_Lit
        "A11_Snow",  # FRPG_Snow
        "A11_Snow[L]",  # FRPG_Snow_Lit
        "A11_Snow_stair",  # FRPG_Snow
        "A11_Snow_stair[L]",  # FRPG_Snow_Lit
        "A14_numa",  # FRPG_Snow (Blighttown swamp)
        "A14_numa2",  # FRPG_Snow (Blighttown swamp)
        "A15_Tar",  # FRPG_Snow
        "A19_Snow",  # FRPG_Snow
        "A19_Snow[L]",  # FRPG_Snow_Lit
    }

    # TODO: Some shaders simply don't use the always-empty 'g_DetailBumpmap', but I can find no reliable way to detect
    #  this from their MTD names alone. I may have to guess that they do unless the MTD file is provided.

    shader_category: ShaderCategory | None = ShaderCategory.PHN

    @classmethod
    def from_mtd_name(cls, mtd_name: str):
        matdef = super().from_mtd_name(mtd_name)

        if matdef.get_sampler_with_alias("Main 0 Normal"):
            # Add useless "Detail 0 Normal" sampler for completion.
            # TODO: Some DS1 shaders, even with 'g_Bumpmap', do not have this. I have no way to detect from the name.
            #  Currently assuming that it doesn't matter at all if FLVERs have an (empty) texture definition for it.
            matdef.add_sampler(alias="Detail 0 Normal", uv_layer=cls.UVLayer.UVTexture0)

        return matdef

    def get_map_piece_layout(self) -> VertexArrayLayout:
        """Get a standard DS1 map piece layout with the given number of UV layers."""

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
        """Get a standard vertex array layout for character (and probably object) materials in DS1."""
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
            raise ValueError(f"Invalid UV count for DS1 character layout: {uv_count}. Must be 1 or 2.")

        for data_type in data_types:
            data_type.unk_x00 = 0  # DS1

        return VertexArrayLayout(data_types)
