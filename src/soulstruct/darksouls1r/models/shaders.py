__all__ = [
    "MatDef"
]

import typing as tp
from dataclasses import dataclass
from pathlib import Path

from soulstruct.base.models.mtd import MTD
from soulstruct.darksouls1ptde.models.shaders import MatDef as _PTDE_MatDef
from soulstruct.flver.vertex_array_layout import VertexArrayLayout, VertexBitangent


@dataclass(slots=True)
class MatDef(_PTDE_MatDef):
    """Identical to PTDE except for the possibility of a third normal sampler in some snow shaders."""

    # These DSR MTDs use a 'FRPG_Snow*' SPX shader with a 'g_SnowMetalMask' param and custom bumpmaps.
    SNOW_METAL_MASK_STEMS: tp.ClassVar[set[str]] = {
        "A10_slime[D][L]",  # FRPG_Snow_Lit (Depths slime)
        "A11_Snow",  # FRPG_Snow
        "A11_Snow[L]",  # FRPG_Snow_Lit
        "A11_Snow_stair",  # FRPG_Snow
        "A11_Snow_stair[L]",  # FRPG_Snow_Lit
        "A14_numa",  # FRPG_Snow (Blighttown swamp)
        "A14_numa2",  # FRPG_Snow (Blighttown swamp)
        "A15_Tar",  # FRPG_Snow (Sen's Fortress tar)
        "A19_Snow",  # FRPG_Snow
        "A19_Snow[L]",  # FRPG_Snow_Lit
    }

    @classmethod
    def from_mtd(cls, mtd: MTD) -> tp.Self:
        """Extract critical MTD information (mainly for generating FLVER vertex array layouts) directly from MTD.

        In DSR, we have to handle the possibility of a tertiary normal map in snow shaders that use "g_SnowMetalMask".
        """
        matdef = super(MatDef, cls).from_mtd(mtd)

        if "Snow" in matdef.shader_stem:
            # In DS1R, some snow shaders (those with "Snow Metal Mask" MTD param) have a very unusual setup using
            # three normal samplers (g_Bumpmap*).
            # The first contains a snow height map that is layered on top of itself at different scales. The second
            # contains a detailed normal map. The third contains the standard normal map for the ground under the snow.
            # There may also be a lightmap.
            # The sampler UV indices in the MTD are wrong -- all three normal samplers use the first UV slot (0) and
            # the lightmap, if present, uses the second UV slot (1).
            if mtd.has_param("g_SnowMetalMask"):
                snow_detail_normal = matdef.get_sampler_with_alias("DSB 1 Normal")  # g_Bumpmap_2
                dsb_normal = matdef.get_sampler_with_alias("DSB 2 Normal")  # g_Bumpmap_3

                if not snow_detail_normal or not dsb_normal:
                    raise ValueError(
                        f"DSR Snow material with g_SnowMetalMask does not have expected Normal samplers.\n"
                        f"All samplers: {', '.join(sampler.alias for sampler in matdef.samplers)}"
                    )
                snow_detail_normal.uv_layer = cls.UVLayer.UVTexture0  # *NOT* UVTexture1 as the MTD indicates
                dsb_normal.uv_layer = cls.UVLayer.UVTexture0  # explicit for clarity
                if lightmap := matdef.get_sampler_with_alias("Lightmap"):
                    lightmap.uv_layer = cls.UVLayer.UVLightmap  # explicit for clarity

        return matdef

    @classmethod
    def from_mtd_name(cls, mtd_name: str) -> tp.Self:
        mtd_stem = Path(mtd_name).stem
        matdef = super(MatDef, cls).from_mtd_name(mtd_name)

        if "Snow" in matdef.shader_stem and mtd_stem in cls.SNOW_METAL_MASK_STEMS:
            # Repair guessing of DSR snow shader.

            snow_height = matdef.get_sampler_with_alias("DSB 0 Normal")
            snow_height.uv_layer = cls.UVLayer.UVTexture0

            snow_detail_normal = matdef.get_sampler_with_alias("DSB 1 Normal")
            snow_detail_normal.uv_layer = cls.UVLayer.UVTexture0

            # Add third normal sampler, which the standard PTDE from-name method won't guess.
            # This sampler actually contains the standard normal map for the ground under the snow.
            matdef.add_sampler(alias="DSB 2 Normal", uv_layer=cls.UVLayer.UVTexture0)

            if lightmap := matdef.get_sampler_with_alias("Lightmap"):  # for [L] MTDs
                lightmap.uv_layer = cls.UVLayer.UVLightmap

        return matdef

    def get_vertex_array_layout(self, is_dynamic: bool) -> VertexArrayLayout:
        layout = super(MatDef, self).get_vertex_array_layout(is_dynamic)

        # Handle three-bumpmap DSR snow shaders.
        # These are the same, except we remove the Bitangent data (they don't use a real second normal texture).
        if "Snow" in self.shader_stem and self.get_sampler_with_alias("DSB 2 Normal"):
            layout = VertexArrayLayout(
                [d for d in layout.read_types if not isinstance(d, VertexBitangent)]
            )

        return layout
