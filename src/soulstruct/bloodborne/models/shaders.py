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

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MatDef(_BaseMatDef):

    class UVLayer(IntEnum):
        UVTexture0 = 0
        UVTexture1 = 1
        UVBloodMaskOrLightmap = 2  # lightmap ('DOLTexture') for maps, blood mask for characters
        UVBlendMask = 3
        UVData_WindA = 4
        # TODO: other data UVs?

    SAMPLER_ALIASES: tp.ClassVar[dict[str, str]] = {
        "g_DiffuseTexture": "DSB 0 Diffuse",  # A
        "g_SpecularTexture": "DSB 0 Specular",  # R
        "g_ShininessTexture": "DSB 0 Shininess",  # S
        "g_BumpmapTexture": "DSB 0 Normal",  # N
        "g_DiffuseTexture2": "DSB 1 Diffuse",  # NOTE: no underscore before '2' suffix in Bloodborne
        "g_SpecularTexture2": "DSB 1 Specular",
        "g_ShininessTexture2": "DSB 1 Shininess",
        "g_Bumpmap2": "DSB 1 Normal",
        "g_BlendMaskTexture": "Blend 01",
        "g_DisplacementTexture": "Displacement",
        "g_DOLTexture1": "Lightmap 0",  # NOTE: does end with '1', unlike primaries above
        "g_DOLTexture2": "Lightmap 1",
        "g_DetailBumpmapTexture": "Detail 0 Normal",  # TODO: confirm (if even used)
    }

    SAMPLER_GAME_NAMES: tp.ClassVar[dict[str, str]] = {v: k for k, v in SAMPLER_ALIASES.items()}

    # Class regex patterns for MTD name parsing.
    NAME_TAG_RE: tp.ClassVar[dict[str, re.Pattern]] = {
        "Diffuse": re.compile(r".*\[.*A.*\].*"),
        "Metallic": re.compile(r".*\[.*R.*\].*"),
        "Shininess": re.compile(r".*\[.*S.*\].*"),
        "Normal": re.compile(r".*\[.*N.*\].*"),
        # "translucent": re.compile(r".*\[.*T.*\].*"),
        "Displacement": re.compile(r".*\[.*H.*\].*"),
        "NormalToAlpha": re.compile(r".*\[Dn\].*"),  # 'DSB 0 Diffuse' only
        "Water": re.compile(r".*\[We\].*"),  # 'DSB 0 Normal' only

        "Multi": re.compile(r".*_m(_.*|$)"),  # two blended texture slots (Diffuse, Metallic, and/or Normal)
        "Alpha": re.compile(r".*_Alp.*"),
        "Edge": re.compile(r".*_e(_.*|$).*"),
        "Blend": re.compile(r".*_blend(_.*|$)"),  # has Blend 01 texture
        "Env": re.compile(r".*_env(_.*|$)"),
        "Lightmap": re.compile(r".*_l(_.*|$)"),
        "Emission": re.compile(r".*_em(_.*|$).*"),
        "Glow": re.compile(r".*_Glow(_.*|$).*"),
        "SSS": re.compile(r".*_SSS(_.*|$).*"),
        "PDEnhanced": re.compile(r".*_PDEnhanced(_.*|$).*"),
        "Tr": re.compile(r".*_Tr(_.*|$).*"),
        "Phantom": re.compile(r".*_Phantom(_.*|$).*"),
    }

    EXTRA_SHADER_UV_LAYERS: tp.ClassVar[dict[str, list[UVLayer]]] = {
        "Grass": [UVLayer.UVData_WindA],
    }

    KNOWN_SHADER_STEMS: tp.ClassVar[dict[str, list[str | re.Pattern]]] = {
        # TODO
    }

    is_cloth: bool = False

    @classmethod
    def from_mtd(cls, mtd: MTD):
        """Check if this is a Cloth material and set `is_cloth` attribute accordingly."""
        matdef = tp.cast(tp.Self, super(MatDef, cls).from_mtd(mtd))
        if mtd.get_param("g_GX_MaterialType", default=0) == 2:
            matdef.is_cloth = True
        return matdef

    @classmethod
    def from_mtd_name(cls, mtd_name: str):
        matdef = tp.cast(tp.Self, super(MatDef, cls).from_mtd_name(mtd_name))
        if "_Cloth" in mtd_name:
            matdef.is_cloth = True
        return matdef

    def get_used_uv_layers(self) -> list[IntEnum]:
        """Need to handle 'Cloth' case, which has no UVs (or colors, or bone indices/weights).

        There doesn't seem to be any distinguishing property for these.
        """
        if self.is_cloth:
            # No UV layers used, despite presence of textures.
            return []

        # Standard call:
        return super(MatDef, self).get_used_uv_layers()

    def get_vertex_array_layout(self, is_dynamic: bool) -> VertexArrayLayout:
        """Unified method for determining the correct vertex array layout for FLVER meshes using this material.

        `is_dynamic` distinguishes static meshes (False) from dynamic (rigged) meshes (True). Static meshes
        encode the single bone index in `normal_w` and have no explicit bone index/weight arrays, while dynamic
        meshes carry full `BoneIndices` and `BoneWeights` arrays (except the cloth and diffuse-only special cases
        below).
        """
        if not is_dynamic:
            # Static: `normal_w` used as bone index; no explicit bone index/weight arrays.
            data_types: list[VERTEX_DATA_TYPING] = [
                VertexPosition(VertexDataFormatEnum.Float3, 0),
                VertexNormal(VertexDataFormatEnum.FourBytesB, 0),  # `normal_w` component used as bone index
            ]

            if self.get_sampler_with_alias("DSB 0 Normal"):
                # Uses tangent vertex data.
                data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesB, 0))
                if self.get_sampler_with_alias("DSB 1 Normal"):
                    # Uses second tangent for second texture group normal.
                    data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesB, 1))
            elif self.get_sampler_with_alias("DSB 1 Normal"):
                # Still uses one tangent field. NOTE: I highly doubt any game shaders do this.
                data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesB, 0))

            data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, 0))

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

            return VertexArrayLayout(data_types)

        # Dynamic (character/object) mesh:

        if self.is_cloth:
            # Single tangent only; no bones, no color, no UVs.
            return VertexArrayLayout([
                VertexPosition(VertexDataFormatEnum.Float3, 0),
                VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
                VertexTangent(VertexDataFormatEnum.FourBytesB, 0),
            ])

        if len(self.samplers) == 1 and self.samplers[0].alias == "DSB 0 Diffuse":
            # Diffuse-only, no normals (e.g. 'C_1040_Phantom', 'C[A]_NoLight').
            return VertexArrayLayout([
                VertexPosition(VertexDataFormatEnum.Float3, 0),
                VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
                VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
                VertexBoneWeights(VertexDataFormatEnum.FourBytesC, 0),
                VertexColor(VertexDataFormatEnum.FourBytesC, 1),  # note index 1
                VertexUV(VertexDataFormatEnum.UV, 1),
            ])

        # Standard character layout: number of tangent arrays matches number of UV layers.
        uv_count = len(self.get_used_uv_layers())
        data_types: list[VERTEX_DATA_TYPING] = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
            VertexTangent(VertexDataFormatEnum.FourBytesB, 0),
        ]
        if uv_count >= 2:
            data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesB, 1))
        if uv_count >= 3:
            data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesB, 2))

        data_types += [
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneWeights(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 1),  # note index 1
        ]

        if uv_count == 3:
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
            data_types.append(VertexUV(VertexDataFormatEnum.UV, 1))
        elif uv_count == 2:
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
        elif uv_count == 1:
            # No blood mask. Pretty rare (e.g. 'C_Phantom.mtd').
            data_types.append(VertexUV(VertexDataFormatEnum.UV, 0))
        else:
            raise ValueError(f"Invalid UV count for Bloodborne character layout: {uv_count}. Must be 1, 2, or 3.")


        return VertexArrayLayout(data_types)
