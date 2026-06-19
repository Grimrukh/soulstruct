from __future__ import annotations

__all__ = [
    "MatDef",
]

import logging
import re
import typing as tp
from dataclasses import dataclass
from enum import IntEnum

from soulstruct.base.models import MTD
from soulstruct.base.models.shaders import MatDef as _BaseMatDef
from soulstruct.flver.vertex_array_layout import *
from soulstruct.utilities.binary import ByteOrder

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MatDef(_BaseMatDef):
    """TODO: So far mostly identical to Dark Souls 1, but I'm sure there are a few differences to find."""

    class UVLayer(IntEnum):
        """Up to four of these are used by each shader in DeS, in the order they appear here."""
        UVTexture0 = 0
        UVTexture1 = 1
        UVLightmap = 2
        UVData_WindA = 3  # used mostly by Foliage and occasionally by Ivy
        UVData_WindB = 4  # used mostly by Ivy and always zero for Foliage

    SAMPLER_ALIASES: tp.ClassVar[dict[str, str]] = {
        "g_Diffuse": "DSB 0 Diffuse",
        "g_Specular": "DSB 0 Specular",
        "g_Bumpmap": "DSB 0 Normal",
        "g_Diffuse_2": "DSB 1 Diffuse",
        "g_Specular_2": "DSB 1 Specular",
        "g_Bumpmap_2": "DSB 1 Normal",
        "g_Height": "Displacement",
        "g_Lightmap": "Lightmap",
        "g_DetailBumpmap": "Detail 0 Normal",
    }

    SAMPLER_GAME_NAMES: tp.ClassVar[dict[str, str]] = {v: k for k, v in SAMPLER_ALIASES.items()}

    # Class regex patterns for MTD name parsing.
    NAME_TAG_RE: tp.ClassVar[dict[str, re.Pattern]] = {
        "Diffuse": re.compile(r".*\[.*D.*\].*"),
        "Specular": re.compile(r".*\[.*S.*\].*"),
        # No "Shininess" samplers in DeS.
        "Normal": re.compile(r".*\[.*B.*\].*"),
        "Translucent": re.compile(r".*\[.*T.*\].*"),
        "Multi": re.compile(r".*\[.*M.*\].*"),  # two blended texture slots (ALBEDO, SPECULAR, and/or NORMAL)
        "Displacement": re.compile(r".*\[.*H.*\].*"),
        "Lightmap": re.compile(r".*\[.*L.*\].*"),
        "NormalToAlpha": re.compile(r".*\[(Dn|.*N.*)\].*"),  # DSB 0 Diffuse only
        "Water": re.compile(r".*\[We\].*"),  # DSB 0 Normal only

        "Alpha": re.compile(r".*_Alp.*"),
        "Edge": re.compile(r".*_Edge.*"),
    }

    # TODO: DeS has its own wind shaders...
    EXTRA_SHADER_UV_LAYERS: tp.ClassVar[dict[str, list[UVLayer]]] = {
        # NOTE: These are used differently by Foliage and Ivy. Foliage uses mostly A, and Ivy mostly B (both of which
        # will appear to stretch the texture from one edge to the opposite).
        "Foliage": [UVLayer.UVData_WindA, UVLayer.UVData_WindB],
        "Ivy": [UVLayer.UVData_WindA, UVLayer.UVData_WindB],
    }

    # TODO: These are all PTDE stems.
    KNOWN_SHADER_MTD_STEMS: tp.ClassVar[dict[str, list[str | re.Pattern]]] = {
        "Water": [
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
        "Snow": [
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
        "Foliage": [
            re.compile(r"^M_2Foliage.*"),
        ],
        "Ivy": [
            re.compile(r"^M_3Ivy.*"),
        ],
        "NormalToAlpha": [
            "M_Tree[D]_Edge",
        ],
    }

    # Some older materials have a second albedo texture ('g_Diffuse_2') that still uses UV layer 0.
    HAS_DUPLICATE_ALBEDO_STEMS: tp.ClassVar[set[str]] = {
        "Cs_ShadowMan_skin",
        "Cs_Ghost_Param_Wander",
        "Ps_Wander_Ghost",
    }

    @classmethod
    def from_mtd(cls, mtd: MTD):
        matdef = tp.cast(tp.Self, super(MatDef, cls).from_mtd(mtd))

        # Special known cases of a reused diffuse UV layer, which we redirect to the first diffuse UV.
        if matdef.stem in cls.HAS_DUPLICATE_ALBEDO_STEMS:
            dsb_0_sampler = matdef.get_sampler_with_alias("DSB 0 Diffuse")
            dsb_1_sampler = matdef.get_sampler_with_alias("DSB 1 Diffuse")
            if dsb_1_sampler is None:
                _LOGGER.warning(
                    f"MatDef '{matdef.name}' does not have expected 'DSB 1 Diffuse' sampler."
                )
            else:
                dsb_1_sampler.uv_layer = dsb_0_sampler.uv_layer

        return matdef

    @classmethod
    def from_mtd_name(cls, mtd_name: str):
        matdef = tp.cast(tp.Self, super(MatDef, cls).from_mtd_name(mtd_name))

        if matdef.get_sampler_with_alias("DSB 0 Normal"):
            # Add useless "Detail 0 Normal" sampler for completion.
            # TODO: Some DeS shaders, even with 'g_Bumpmap', do not have this. I have no way to detect from the name.
            #  Currently assuming that it doesn't matter at all if FLVERs have an (empty) texture definition for it.
            matdef.add_sampler(alias="Detail 0 Normal", uv_layer=cls.UVLayer.UVTexture0)

        return matdef

    def get_vertex_array_layout(self, is_dynamic: bool) -> VertexArrayLayout:
        """Unified method for determining the correct vertex array layout for FLVER meshes using this material.

        The only external input required is `is_dynamic` from the FLVER mesh, which simply indicates whether vertex
        bone weights are present (bone indices are always present in DeS -- later games switch to using `NormalW`).
        """

        # Guaranteed start:
        data_types: list[VERTEX_DATA_TYPING] = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesD, 0),
        ]

        # Bone weights for dynamic meshes:
        if is_dynamic:
            data_types.append(VertexBoneWeights(VertexDataFormatEnum.FourShortsToFloats, 0))

        # Guaranteed:
        data_types.append(VertexNormal(VertexDataFormatEnum.FourBytesA, 0))

        if self.get_sampler_with_alias("DSB 0 Normal"):
            # Uses tangent vertex data.
            data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesA, 0))
        if self.get_sampler_with_alias("DSB 1 Normal"):
            # Uses bitangent vertex data for second texture group normal.
            data_types.append(VertexBitangent(VertexDataFormatEnum.FourBytesA, 0))
            if not self.get_sampler_with_alias("DSB 0 Normal"):
                # No known cases of this, so I want to hear about it.
                _LOGGER.warning(
                    f"Material MTD '{self.name}' has 'DSB 1 Normal' but no 'DSB 0 Normal'. This is "
                    f"unusual and may lead to incorrect exported FLVER data."
                )

        # Guaranteed:
        data_types.append(VertexColor(VertexDataFormatEnum.FourBytesA, 0))

        # UVs:
        uv_member_index = 0
        uv_count = len(self.get_used_uv_layers())
        while uv_count > 0:
            # For odd counts, single UV member is added first.
            if uv_count % 2:
                data_types.append(VertexUV(VertexDataFormatEnum.UV, uv_member_index))
                uv_count -= 1
                uv_member_index += 1
            else:  # must be a non-zero even number remaining
                data_types.append(VertexUV(VertexDataFormatEnum.UVPair, uv_member_index))
                uv_count -= 2
                uv_member_index += 1


        return VertexArrayLayout(data_types, byte_order=ByteOrder.BigEndian)
