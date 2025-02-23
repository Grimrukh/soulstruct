__all__ = [
    "MatDef"
]

import typing as tp
from dataclasses import dataclass
from pathlib import Path

from soulstruct.base.models.mtd import MTD
from soulstruct.darksouls1ptde.models.shaders import MatDef as _PTDE_MatDef
from soulstruct.utilities.maths import Vector2


@dataclass(slots=True)
class MatDef(_PTDE_MatDef):
    """Identical to PTDE except for the possibility of a tertiary normal map in some snow shaders."""

    # DSR snow shaders may have an extra normal texture.
    SAMPLER_ALIASES: tp.ClassVar[dict[str, str]] = _PTDE_MatDef.SAMPLER_ALIASES | {
        "g_Bumpmap_3": "Main 2 Normal",
    }

    SAMPLER_GAME_NAMES: tp.ClassVar[dict[str, str]] = {v: k for k, v in SAMPLER_ALIASES.items()}

    @classmethod
    def from_mtd(cls, mtd: MTD):
        """Extract critical MTD information (mainly for generating FLVER vertex array layouts) directly from MTD.

        NOTES:
            - There are only a couple dozen different shaders (SPX) used by all MTDs.
            - All FLVER vertex arrays have normals, at least one vertex color.
        """
        matdef = super(MatDef, cls).from_mtd(mtd)
        detail_samp = matdef.get_sampler_with_alias("Detail 0 Normal")
        if detail_samp is not None:
            detail_samp.uv_scale = Vector2(mtd.get_param("g_DetailBump_UVScale", default=[1.0, 1.0]))

        if matdef.shader_category == "Snow":
            # In DS1R, some snow shaders (those with "Snow Metal Mask" MTD param) have a THIRD normal texture. I believe
            # QLOC changed `g_Bumpmap_2` to use the first UV index in the shader so that the new `g_Bumpmap_3` could
            # use the second UV index) WITHOUT changing the sampler's UV index in the MTD. We update it here.
            if mtd.has_param("g_SnowMetalMask"):
                snow_normal_2 = matdef.get_sampler_with_alias("Main 2 Normal")
                snow_normal_2.uv_layer = cls.UVLayer.UVTexture1
                snow_normal_1 = matdef.get_sampler_with_alias("Main 1 Normal")
                snow_normal_1.uv_layer = cls.UVLayer.UVTexture0

        return matdef

    @classmethod
    def from_mtd_name(cls, mtd_name: str):
        mtd_stem = Path(mtd_name).stem
        matdef = super(MatDef, cls).from_mtd_name(mtd_name)
        if matdef.shader_category == "Snow" and mtd_stem in cls.SNOW_METAL_MASK_STEMS:
            matdef.add_sampler(alias="Main 2 Normal", uv_layer=cls.UVLayer.UVTexture1)
            snow_normal_1 = matdef.get_sampler_with_alias("Main 1 Normal")
            snow_normal_1.uv_layer = cls.UVLayer.UVTexture0
        return matdef
