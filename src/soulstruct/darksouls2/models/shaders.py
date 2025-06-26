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
    # TODO: Currently mostly just copied from Bloodborne.

    class UVLayer(IntEnum):
        UVTexture0 = 0
        UVTexture1 = 1
        UVBloodMaskOrLightmap = 2  # lightmap ('DOLTexture') for Map Pieces, blood mask for characters
        UVBlendMask = 3
        UVData_WindA = 4
        # TODO: other data UVs?

    SAMPLER_ALIASES: tp.ClassVar[dict[str, str]] = {
        "g_DiffuseTexture": "Main 0 Albedo",  # D
        "g_SpecularTexture": "Main 0 Specular",  # S
        "g_BumpmapTexture": "Main 0 Normal",  # B
        "g_DiffuseTexture2": "Main 1 Albedo",  # TODO: underscore before '2' suffix?
        "g_SpecularTexture2": "Main 1 Specular",
        "g_Bumpmap2": "Main 1 Normal",
        "g_BlendMaskTexture": "Blend 01",
        "g_DisplacementTexture": "Displacement",
        "g_DOLTexture1": "Lightmap 0",  # NOTE: does end with '1', unlike primaries above
        "g_DOLTexture2": "Lightmap 1",
        "g_DetailBumpmapTexture": "Detail 0 Normal",
    }

    SAMPLER_GAME_NAMES: tp.ClassVar[dict[str, str]] = {v: k for k, v in SAMPLER_ALIASES.items()}

    # Class regex patterns for MTD name parsing.
    NAME_TAG_RE: tp.ClassVar[dict[str, re.Pattern]] = {
        "Albedo": re.compile(r".*\[.*D.*\].*"),
        "Metallic": re.compile(r".*\[.*S.*\].*"),
        "Shininess": re.compile(r".*\[.*B.*\].*"),
        "Normal": re.compile(r".*\[.*N.*\].*"),
        # "translucent": re.compile(r".*\[.*T.*\].*"),
        "Displacement": re.compile(r".*\[.*H.*\].*"),
        "NormalToAlpha": re.compile(r".*\[Dn\].*"),  # 'Main 0 Albedo' only
        "Water": re.compile(r".*\[We\].*"),  # 'Main 0 Normal' only

        # TODO: [Ibl] tag? Very common. Also look for 'Cloth' prefix.
        "Multi": re.compile(r".*_m(_.*|$)"),  # two blended texture slots (Albedo, Metallic, and/or Normal)
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
        # "Grass": [UVLayer.UVData_WindA],
    }

    KNOWN_SHADER_STEMS: tp.ClassVar[dict[str, list[str | re.Pattern]]] = {
        # TODO
    }

    is_cloth: bool = False

    @classmethod
    def from_mtd(cls, mtd: MTD):
        """Check if this is a Cloth material and set `is_cloth` attribute accordingly."""
        matdef = super(MatDef, cls).from_mtd(mtd)
        if mtd.get_param("g_GX_MaterialType", default=0) == 2:  # TODO: confirm
            matdef.is_cloth = True
        return matdef

    @classmethod
    def from_mtd_name(cls, mtd_name: str):
        matdef = super(MatDef, cls).from_mtd_name(mtd_name)
        if mtd_name.startswith("Cloth"):
            matdef.is_cloth = True
        return matdef

    @classmethod
    def _get_shader_category(cls, shader_stem: str) -> str:
        """99% of DS2 shaders start with 'GXFlver'."""
        return shader_stem.removeprefix("GXFlver_").split("_")[0]

    def get_used_uv_layers(self) -> list[IntEnum]:
        """Need to handle 'Cloth' case, which has no UVs (or colors, or bone indices/weights).

        There doesn't seem to be any distinguishing property for these.
        """
        if self.is_cloth:
            # No UV layers used, despite presence of textures.
            return []

        # Standard call:
        return super(MatDef, self).get_used_uv_layers()

    def get_map_piece_layout(self) -> VertexArrayLayout:
        """Get a standard DS2 map piece layout with the given number of UV layers.

        DS2 Map Pieces use `normal_w` component as a single bone index and do not have standard four-element bone
        indices or weights.

        NOTE: Every material seems to use two colors.
        """

        data_types = [  # always present
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesB, 0),  # `normal_w` component used as bone index
            # Tangent fields will be inserted here if needed.
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 1),
            # UV/UVPair fields will be appended here if needed.
        ]  # type: list[VertexDataType]

        if self.get_sampler_with_alias("Main 0 Normal"):
            # Uses tangent vertex data.
            data_types.insert(2, VertexTangent(VertexDataFormatEnum.FourBytesB, 0))
            if self.get_sampler_with_alias("Main 1 Normal"):
                # Uses second tangent vertex data for second texture group normal.
                data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesB, 1))
        elif self.get_sampler_with_alias("Main 1 Normal"):
            # Still uses one tangent field. NOTE: I highly doubt any game shaders do this.
            data_types.insert(2, VertexTangent(VertexDataFormatEnum.FourBytesB, 0))

        uv_member_index = 0
        uv_count = len(self.get_used_uv_layers())
        while uv_count > 0:
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

    def get_non_map_piece_layout(self) -> VertexArrayLayout:
        """Get a standard vertex array layout for character (and probably object) materials in DS2.

        NOTE: Every material seems to use two colors.
        """

        if len(self.samplers) == 1 and self.samplers[0].alias == "Main 0 Albedo":
            # Diffuse-only, with no normals.
            layout = VertexArrayLayout([
                VertexPosition(VertexDataFormatEnum.Float3, 0),
                VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
                VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
                VertexBoneWeights(VertexDataFormatEnum.FourBytesC, 0),
                VertexColor(VertexDataFormatEnum.FourBytesC, 0),
                VertexColor(VertexDataFormatEnum.FourBytesC, 1),
                VertexUV(VertexDataFormatEnum.UV, 1),
            ])
            layout.set_unk_x00(self.type_unk_x00)
            return layout

        data_types = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
            VertexTangent(VertexDataFormatEnum.FourBytesB, 0),
        ]  # type: list[VertexDataType]

        if self.is_cloth:
            # Single tangent, but with no bones, color, or UVs.
            layout = VertexArrayLayout(data_types)
            layout.set_unk_x00(self.type_unk_x00)
            return layout

        # Number of tangent arrays always matches number of UV layers for characters.
        # First tangent already added above.
        uv_count = len(self.get_used_uv_layers())
        if uv_count >= 2:
            data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesB, 1))
        if uv_count >= 3:
            data_types.append(VertexTangent(VertexDataFormatEnum.FourBytesB, 2))

        # Bone indices, bone weights, and color (1) are always present.
        data_types += [
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneWeights(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 1),  # note index 1
        ]

        # Add appropriate number of UV fields.
        if uv_count == 3:
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
            data_types.append(VertexUV(VertexDataFormatEnum.UV, 1))
        elif uv_count == 2:
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
        elif uv_count == 1:
            # No blood mask. Pretty rare (e.g. 'C_Phantom.mtd').
            data_types.append(VertexUV(VertexDataFormatEnum.UV, 0))
        else:
            raise ValueError(f"Invalid UV count for DS2 character layout: {uv_count}. Must be 1, 2, or 3.")

        for data_type in data_types:
            data_type.unk_x00 = self.type_unk_x00

        return VertexArrayLayout(data_types)
