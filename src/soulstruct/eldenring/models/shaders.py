from __future__ import annotations

__all__ = [
    "ShaderProfile",
    "SamplerGroupRole",
    "MatDef",
]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum, auto

from soulstruct.base.models.matbin import MATBIN
from soulstruct.base.models.shaders import MatDef as _BaseMatDef, MatDefError, MatDefSampler
from soulstruct.flver.vertex_array_layout import *
from soulstruct.utilities.files import read_json, SOULSTRUCT_PATH
from soulstruct.utilities.maths import Vector2
from soulstruct.utilities.text import natural_keys

_LOGGER = logging.getLogger(__name__)


# region Shader Stem Parsing

@dataclass(slots=True)
class ShaderProfile:
    """Structured parsing of an ER shader stem like 'C[DetailBlend][S2]_cloth' or 'M[AMSN_V][Mb2][Ov_AN]_Edge'.

    Separates the stem into:
      - `category`: prefix letter(s) indicating asset type ('C', 'M', 'CS', 'P', etc.)
      - `base_type`: first bracket contents indicating the shader family ('DetailBlend', 'AMSN', 'Fur', etc.)
      - `tags`: additional bracket tags ('[S2]', '[Mb2]', '[Ov_AN]', '[3Mask]', etc.)
      - `suffixes`: underscore-separated trailing modifiers ('cloth', 'SSS', 'Glow', 'Alpha', 'Edge', etc.)
    """

    category: str = ""
    base_type: str = ""
    tags: list[str] = field(default_factory=list)
    suffixes: list[str] = field(default_factory=list)

    # Matches stems like: C[DetailBlend][S2]_cloth, M[AMSN_V][Mb2][Ov_AN]_Edge, CS[VA_Frame][Fur]_FurBlur
    # Group 1: category prefix (letters before first '[')
    # Group 2: first bracket contents (base_type)
    # Group 3: remaining bracket tags (zero or more '[...]')
    # Group 4: underscore-separated suffixes after last ']'
    _STEM_RE: tp.ClassVar[re.Pattern] = re.compile(
        r"^([A-Za-z]+)"          # category prefix
        r"\[([^\]]+)\]"          # first bracket = base type
        r"((?:\[[^\]]+\])*)"     # zero or more additional bracket tags
        r"(?:_(.+))?$"           # optional underscore-separated suffixes
    )

    # Shader families whose group-index-to-role mapping is defined in `FAMILY_GROUP_ROLES`.
    _KNOWN_FAMILIES: tp.ClassVar[frozenset[str]] = frozenset({
        "AMSN", "DetailBlend", "Fur", "Face", "Shell", "Crystal", "Hair", "Eye",
    })

    @classmethod
    def from_shader_stem(cls, stem: str) -> ShaderProfile:
        """Parse a shader stem string into its components. Returns a default (empty) profile for unrecognized stems."""
        m = cls._STEM_RE.match(stem)
        if not m:
            return cls()  # unrecognized (legacy GXFlver, test shaders, etc.)
        tags_str = m.group(3) or ""
        suffix_str = m.group(4) or ""
        return cls(
            category=m.group(1),
            base_type=m.group(2),
            tags=re.findall(r"\[([^\]]+)\]", tags_str),
            suffixes=suffix_str.split("_") if suffix_str else [],
        )

    @property
    def family(self) -> str:
        """Shader 'family' that determines group-to-role mapping.

        For multi-tag stems like `CS[VA_Frame][Fur]`, we want the last known family tag ('Fur').
        For `C[AMSN_V]`, we normalize to 'AMSN'.
        """
        # Check tags in reverse for a known family name.
        for tag in reversed(self.tags):
            if tag in self._KNOWN_FAMILIES:
                return tag
        if self.base_type in self._KNOWN_FAMILIES:
            return self.base_type
        # Normalize e.g. 'AMSN_V' -> 'AMSN'.
        for known in self._KNOWN_FAMILIES:
            if self.base_type.startswith(known):
                return known
        return self.base_type

    @property
    def multi_blend_count(self) -> int:
        """Returns N from `[MbN]` tag, or 1 if not a multi-blend shader."""
        for tag in self.tags:
            if m := re.match(r"Mb(\d+)", tag):
                return int(m.group(1))
        return 1

    @property
    def has_overlay(self) -> bool:
        return any(t.startswith("Ov_") for t in self.tags)

    @property
    def overlay_types(self) -> str:
        """Returns e.g. 'AN', 'N', 'detail_AN' from `[Ov_X]` tag, or empty string."""
        for tag in self.tags:
            if tag.startswith("Ov_"):
                return tag[3:]
        return ""

    @property
    def is_cloth(self) -> bool:
        return "cloth" in self.suffixes

    @property
    def is_sss(self) -> bool:
        return "SSS" in self.suffixes

    @property
    def is_alpha(self) -> bool:
        return "Alpha" in self.suffixes

    @property
    def is_edge(self) -> bool:
        return "Edge" in self.suffixes

    @property
    def has_emissive(self) -> bool:
        return "Emissive" in self.suffixes or "Glow" in self.suffixes

    @property
    def has_snow(self) -> bool:
        return "Snow" in self.tags

    @property
    def is_character(self) -> bool:
        return self.category in ("C", "CS", "P")

    @property
    def is_specific_character(self) -> bool:
        return re.match(r"c\d\d\d", self.family) is not None

    @property
    def is_map(self) -> bool:
        return self.category == "M"

    @property
    def is_recognized(self) -> bool:
        """True if the stem was successfully parsed (has a category and base_type)."""
        return bool(self.category and self.base_type)

    def __repr__(self) -> str:
        s = f"ShaderProfile('{self.category}[{self.base_type}]"
        for tag in self.tags:
            s += f"[{tag}]"
        if self.suffixes:
            s += "_" + "_".join(self.suffixes)
        s += f"' -> family={self.family!r})"
        return s


# endregion


# region Sampler Group Roles (still used by node tree builder for semantic dispatch)

class SamplerGroupRole(IntEnum):
    """Semantic role of a sampler group within its shader.

    Rather than classifying groups by their content (e.g. 'has Albedo+Metallic+Normal'), this enum describes the
    *purpose* each group serves in the rendering pipeline. The group-index-to-role mapping is shader-family-dependent
    and defined in `FAMILY_GROUP_ROLES`.
    """
    UNGROUPED = 0       # ungrouped samplers (blend masks, misc controls); group key "" in metaparam
    PRIMARY = auto()    # Main material (typically A+M+N, the base layer)
    SECONDARY = auto()  # Second material layer (multi-blend or [S2] skin layer)
    DETAIL = auto()     # Detail texture (tiled differently, usually Albedo+Normal)
    FUR_ALPHA = auto()  # Fur/cloth primary texture
    OVERLAY = auto()    # Overlay layer ([Ov_AN], [Ov_N], etc.)
    SUB_NORMALS = auto()  # Additional normal blending (Face/SSS shaders)
    BLEND_CONTROL = auto()  # Blend mask/edge textures (multi-blend shaders)
    EFFECT = auto()     # Fire, distortion, crystal refraction, etc.
    MISC = auto()       # Masks, vectors, standalone samplers with no clear role


# Mapping: family -> { group_index -> SamplerGroupRole }
# group_index 0 = ungrouped ("" key in metaparam JSON).
# Numbered groups use their integer from "group_N".
FAMILY_GROUP_ROLES: dict[str, dict[int, SamplerGroupRole]] = {
    "DetailBlend": {
        # C[DetailBlend], C[DetailBlend][S2], C[DetailBlend][Rich], C[DetailBlend]_SSS, etc.
        1: SamplerGroupRole.PRIMARY,     # AMN: main texture
        2: SamplerGroupRole.DETAIL,      # AN: detail 1
        3: SamplerGroupRole.DETAIL,      # AN: detail 2
        4: SamplerGroupRole.DETAIL,      # AN: detail 3
        5: SamplerGroupRole.SECONDARY,   # AMN: [S2] second skin layer
        7: SamplerGroupRole.DETAIL,      # AN: detail 4
        8: SamplerGroupRole.PRIMARY,     # AMN: secondary AMN (rarely populated)
        9: SamplerGroupRole.MISC,        # Mask1 (SSS), or standalone Albedo, or FurBlur trio (A/V/M1)
    },
    "Fur": {
        # C[Fur], C[Fur]_cloth, C[Fur]_FurBlur, C[Shell]_FurBlur, etc.
        1: SamplerGroupRole.FUR_ALPHA,   # AN: fur alpha and normal
        2: SamplerGroupRole.PRIMARY,     # AMN: base material
        3: SamplerGroupRole.DETAIL,      # AN: detail
        5: SamplerGroupRole.DETAIL,      # AN: Shell variant detail
        6: SamplerGroupRole.MISC,        # FurBlur: Mask1+Vector+Albedo
        7: SamplerGroupRole.MISC,        # FurBlur: additional Normal+Vector
    },
    "AMSN": {
        # C[AMSN], C[AMSN]_Glow, M[AMSN], M[AMSN]_Alpha, etc.
        # Multi-blend ([MbN]) and overlay ([Ov_*]) variants are handled separately in `get_group_role()`.
        1: SamplerGroupRole.PRIMARY,            # AN+: main texture
        2: SamplerGroupRole.PRIMARY,            # AN+: main texture (for foliage materials)
        6: SamplerGroupRole.BLEND_CONTROL,      # Mask1: for foliage materials
    },
    "Face": {
        # C[Face][S2]_SSS and similar
        1: SamplerGroupRole.PRIMARY,     # ANM3: Albedo+Normal+Mask3
        11: SamplerGroupRole.SUB_NORMALS,  # Three blended normals
        12: SamplerGroupRole.DETAIL,     # Detail (beard, etc.)
        13: SamplerGroupRole.DETAIL,     # Detail (overlay)
        18: SamplerGroupRole.MISC,       # Mask3 standalone
    },
    "Crystal": {
        # C[Crystal], C[Crystal]_Glow, C[Crystal_NoTransparent]
        1: SamplerGroupRole.PRIMARY,     # AMN or AMN+Emissive
        3: SamplerGroupRole.EFFECT,      # DistortionAlbedo
        4: SamplerGroupRole.MISC,        # Mask1
    },
    "Shell": {
        # C[Shell]_FurBlur
        1: SamplerGroupRole.FUR_ALPHA,   # Shell fur albedo (no normal)
        2: SamplerGroupRole.PRIMARY,     # AMN: base material
        5: SamplerGroupRole.DETAIL,      # AN: detail
        7: SamplerGroupRole.MISC,        # Mask1+Vector+Albedo
    },
    "Hair": {
        # C[Hair], C[Hair][ChrCustomize]
        1: SamplerGroupRole.PRIMARY,     # AMN: base material
        2: SamplerGroupRole.DETAIL,      # AN: detail
    },
    "Eye": {
        # C[Eye]_Glow, C[Eye][ChrCustomize]
        1: SamplerGroupRole.PRIMARY,     # AMN: base material
        3: SamplerGroupRole.EFFECT,      # Fire, glow, etc.
    },
}


def get_group_role(
    profile: ShaderProfile,
    group_index: int,
    group_sampler_names: list[str],
    is_first: bool,
) -> SamplerGroupRole:
    """Determine the semantic role of a sampler group from the parsed shader profile and group index.

    First, known special cases that extend family defaults are checked.
    Second, exact family is checked.
    Third, if family is unknown (e.g. a specific character 'C[cXXXX]'), group sampler names are checked for a guess.

    Finally, defaults to MISC.
    """
    if group_index == 0:
        if profile.multi_blend_count > 1:
            return SamplerGroupRole.BLEND_CONTROL
        return SamplerGroupRole.UNGROUPED

    family = profile.family

    # Multi-blend shaders ([MbN]):
    #   First AN group is PRIMARY, others are SECONDARY. N-only group is OVERLAY. Rest = MISC.
    if profile.multi_blend_count > 1:
        sampler_name_set = set(extract_map_type(name) for name in group_sampler_names)
        if group_index == 1:
            return SamplerGroupRole.PRIMARY
        elif sampler_name_set == {"Albedo", "Normal"}:
            return SamplerGroupRole.SECONDARY
        if profile.has_overlay and sampler_name_set == {"Normal"}:
            return SamplerGroupRole.OVERLAY
        return SamplerGroupRole.MISC

    if family == "AMSN":
        # First group is always PRIMARY (could be group index 2, not 1).
        if is_first:
            return SamplerGroupRole.PRIMARY
        # Overlays are groups 2/3.
        if profile.has_overlay:
            if group_index in (2, 3):
                return SamplerGroupRole.OVERLAY
            return SamplerGroupRole.MISC
        # TODO: Not sure if this is generalizable. Seen in foliage materials.
        if group_index == 6:
            return SamplerGroupRole.BLEND_CONTROL
        return SamplerGroupRole.MISC

    # Snow shaders: group_1 = PRIMARY, group_2 = SECONDARY (snow), group_3 = OVERLAY, rest = MISC.
    if profile.has_snow:
        if group_index == 1:
            return SamplerGroupRole.PRIMARY
        elif group_index == 2:
            return SamplerGroupRole.SECONDARY
        elif group_index == 3:
            return SamplerGroupRole.OVERLAY
        return SamplerGroupRole.MISC

    # Specific character shaders: rely on sampler group names to guess.
    # TODO: Can probably map each character-specific shader's groups to a list of roles.
    if profile.is_specific_character:
        sampler_name_set = set(extract_map_type(name) for name in group_sampler_names)
        if {"Albedo", "Metallic", "Normal"}.issubset(sampler_name_set):
            if is_first:
                return SamplerGroupRole.PRIMARY
            return SamplerGroupRole.SECONDARY
        if sampler_name_set == {"Albedo", "Normal"}:
            return SamplerGroupRole.DETAIL
        if len(sampler_name_set) == 1 and next(iter(sampler_name_set)) in {"Albedo", "Normal"}:
            # e.g. C[c2030]_Fabric has just-A and just-N detail samplers.
            return SamplerGroupRole.DETAIL
        return SamplerGroupRole.MISC

    # Standard family lookup.
    family_roles = FAMILY_GROUP_ROLES.get(family, {})
    return family_roles.get(group_index, SamplerGroupRole.MISC)


# endregion


# region Sampler Map Type Extraction

# Parses the map type from a full ER sampler name.
# Examples:
#   "C_DetailBlend__snp_Texture2D_7_AlbedoMap"                    -> "AlbedoMap"
#   "M_AMSN_Mb2__snp_Texture2D_1_GSBlendMap_AlbedoMap_0"          -> "AlbedoMap"
#   "C_Crystal__snp_Texture2D_2__DistortionDepth"                 -> "DistortionDepth"
#   "C_Face_S2__SSS_snp_Texture2D_2_Mask3Map"                     -> "Mask3Map"
_SAMPLER_MAP_TYPE_RE: re.Pattern = re.compile(
    r"^.+_snp_Texture2D_\d+_"    # stem + snp_Texture2D + index + underscore
    r"(?:GSBlendMap_)?"           # optional GSBlendMap_ prefix (multi-blend shaders)
    r"(?:RGB_)?"                  # optional RGB_ prefix (blend mask textures)
    r"_*(.+?)(?:_\d+)?$"         # capture map type, strip trailing slot index
)

# Canonical map type names extracted from sampler names.
_MAP_TYPE_CANONICAL: dict[str, str] = {
    "AlbedoMap": "Albedo",
    "NormalMap": "Normal",
    "MetallicMap": "Metallic",
    "ShininessMap": "Shininess",
    "EmissiveMap": "Emissive",
    "VectorMap": "Vector",
    "ReflectanceMap": "Reflectance",
    "Mask1Map": "Mask1",
    "Mask3Map": "Mask3",
    "3Mask": "3Mask",
    "DistortionDepth": "DistortionDepth",
    "BlendMaskTexture": "BlendMask",
    "BlendEdgeTexture": "BlendEdge",
    "UniqueOpacityMask": "UniqueOpacityMask",
    "BlendEdge": "BlendEdge",
    # Obscure types found in some shaders:
    "Normal": "Normal",  # e.g. 'eye_test' has '7_Normal' without 'Map'
    "Shadowmap": "Shadowmap",
    "DisplacementMap": "Displacement",
}

# Fallback regex patterns for specific complex sampler suffixes.
_MAP_TYPE_FALLBACK_RE: dict[str, re.Pattern] = {
    "Fire_Mask": re.compile(r".*__Fire___Mask$"),
    "Fire_Pattern": re.compile(r".*__Fire___Pattern$"),
    "Fire_LightEdge": re.compile(r".*__Fire___Light_Edge$"),
    "Fire_BlackEdge": re.compile(r".*__Fire___Black_Edge$"),
}


def extract_map_type(sampler_name: str) -> str:
    """Extract and canonicalize the map type from a full ER sampler name.

    Returns a short canonical name like 'Albedo', 'Normal', 'Metallic', etc., or the raw extracted suffix if
    not recognized.
    """
    m = _SAMPLER_MAP_TYPE_RE.match(sampler_name)
    if m:
        raw = m.group(1).lstrip("_")
        if raw in _MAP_TYPE_CANONICAL:
            return _MAP_TYPE_CANONICAL[raw]
        # Partial match: check if any canonical key is contained.
        for key, canonical in _MAP_TYPE_CANONICAL.items():
            if raw.endswith(key):
                return canonical
        return raw  # unrecognized but extracted

    # Fallback for complex/unusual names.
    for label, pattern in _MAP_TYPE_FALLBACK_RE.items():
        if pattern.match(sampler_name):
            return label

    return ""


# endregion


# region UV Slot and Group UV Mappings
#
# These two dictionaries are the primary authority for UV assignment in Elden Ring.
#
# SHADER_UV_SLOTS: Maps shader stems to tuples of UV semantic names.
#   - The index in the tuple = the local UV index in the FLVER vertex array.
#   - The length of the tuple = the number of UV maps the shader expects.
#   - UV maps not used by any sampler group (e.g. blend factors, wind) still appear.
#
# SHADER_GROUP_UV: Maps shader stems to {group_key: UV_semantic_name}.
#   - group_key is "group_N" or "" for ungrouped.
#   - Every UV semantic in the group dict MUST appear in the corresponding SHADER_UV_SLOTS tuple.
#
# Cloth variants (`_cloth` suffix) always share the same UV structure as their base.
# The lookup functions below strip `_cloth` automatically.
#
# Confidence levels:
#   HIGH   = Confirmed by group structure + FLVER UV counts + domain knowledge
#   MEDIUM = Inferred from group patterns and UV counts, not manually verified
#   LOW    = Speculative; unique shader with limited data

# Shorthand for readability:
_T0 = "UVTexture0"
_T1 = "UVTexture1"
_DT = "UVDetail"
_FA = "UVFurAlpha"
_SN = "UVSubNormals"
_BL = "UVBlend"
_EY = "UVEye4D"

# Helper: all listed groups map to UVTexture0.
def _all_uv0(*groups: str) -> dict[str, str]:
    return {g: _T0 for g in groups}


SHADER_UV_SLOTS: dict[str, tuple[str, ...]] = {

    # ========================================================================
    # C[AMSN] family  (Confidence: HIGH)
    # 2 UVs. Only group_1 (AMN) uses UV0. UV1 is non-sampler (tangent space).
    # ========================================================================
    "C[AMSN]": (_T0, _T1),  # [2, 3] in FLVERs; using 2 (rare 3rd UV is outlier)
    "C[AMSN][PixelKill]": (_T0, _T1),
    "C[AMSN][PixelKill][ID1]": (_T0, _T1),
    "C[AMSN][VA_Loop]": (_T0, _T1, _T1, _T1, _T1, _T1),  # 6 UVs (VA adds 4)  # LOW
    "C[AMSN]_Alpha": (_T0, _T1),
    "C[AMSN]_Arts": (_T0, _T1),
    "C[AMSN]_Arts_Enchant": (_T0, _T1),
    "C[AMSN]_Burn": (_T0, _T1),
    "C[AMSN]_ClearCoat": (_T0, _T1),
    "C[AMSN]_ContactFade": (_T0, _T1),
    "C[AMSN]_Glow": (_T0, _T1),
    "C[AMSN]_GlowDepthFade_[Int]": (_T0, _T1),
    "C[AMSN]_Glow[Int]": (_T0, _T1),
    "C[AMSN]_Glow_[PixelKill]": (_T0, _T1),
    "C[AMSN]_Shadow": (_T0, _T1),

    # ========================================================================
    # C[DetailBlend] family  (Confidence: HIGH)
    # group_1 = PRIMARY on UV0, groups 2/3/4/7 = DETAIL on UV1, group_8 = PRIMARY on UV0.
    # [S2] adds group_5 = SECONDARY on UV2.
    # ========================================================================
    "C[DetailBlend]": (_T0, _DT),  # 2 UVs
    "C[DetailBlend][Rich]": (_T0, _DT),  # 2 UVs
    "C[DetailBlend]_SSS": (_T0, _DT),  # 2 UVs
    "C[DetailBlend]_FurBlur": (_T0, _DT),  # 2 UVs
    "C[DetailBlend]_ShellBlur": (_T0, _DT),  # 2 UVs
    "C[DetailBlend][S2]": (_T0, _DT, _T1),  # 3 UVs
    "C[DetailBlend][1_0_0_0][S2]_Glow[Int]": (_T0, _DT, _T1),  # 3 UVs
    "C[DetailBlend][VA_Morph]": (_T0, _DT, _T1, _T1, _T1),  # 5 UVs (VA adds 2)  # MEDIUM

    # ========================================================================
    # C[Fur] family  (Confidence: HIGH)
    # group_2 = PRIMARY on UV0, group_3 = DETAIL on UV1, group_1 = FUR_ALPHA on UV2.
    # ========================================================================
    "C[Fur]": (_T0, _DT, _FA),  # 3 UVs
    "C[Fur]_Albedo_FallOff": (_T0, _DT, _FA),
    "C[Fur]_Arts": (_T0, _DT, _FA),
    "C[Fur]_FurBlur": (_T0, _DT, _FA),
    "C[Fur]_FurBlur_Tr": (_T0, _DT, _FA),
    "C[Fur]_Glow": (_T0, _DT, _FA),
    "C[Fur]_Tr": (_T0, _DT, _FA),

    # ========================================================================
    # C[Hair] family  (Confidence: MEDIUM)
    # Only group_1 (AMN). Structurally like AMSN but with 3+ UVs.
    # UV1 likely anisotropy/detail, UV2 likely hair alpha (like fur).
    # ========================================================================
    "C[Hair]": (_T0, _DT, _FA),  # 3 UVs
    "C[Hair][ChrCustomize]": (_T0, _DT, _FA, _T1),  # 4 UVs; UV3 = customization layer

    # ========================================================================
    # C[Crystal] family  (Confidence: HIGH)
    # 2 UVs. All sampler groups share UV0. UV1 is non-sampler (refraction coords).
    # ========================================================================
    "C[Crystal]": (_T0, _T1),
    "C[Crystal]_Glow": (_T0, _T1),
    "C[Crystal]_Tr": (_T0, _T1),
    "C[Crystal_NoTransparent]": (_T0, _T1),
    "C[Crystal_NoTransparent]_Glow": (_T0, _T1),

    # ========================================================================
    # C[Face] family  (Confidence: HIGH)
    # group_1 = PRIMARY UV0, group_11 = SUB_NORMALS UV2, groups 12/13 = DETAIL UV1.
    # ========================================================================
    "C[Face][S2]_SSS": (_T0, _DT, _SN),  # 3 UVs

    # ========================================================================
    # C[Eye] family  (Confidence: HIGH)
    # 2 UVs. All groups share UV0.
    # ========================================================================
    "C[Eye]_Glow": (_T0, _T1),

    # ========================================================================
    # C[Shell] family  (Confidence: HIGH)
    # 2 UVs. Shell fur group and primary share UV0, detail on UV1.
    # FUR_ALPHA role collapses to UV0 when only 2 UVs available.
    # ========================================================================
    "C[Shell]": (_T0, _DT),
    "C[Shell]_FurBlur": (_T0, _DT),

    # ========================================================================
    # P[ChrCustomize] family  (Confidence: MEDIUM-HIGH)
    # ========================================================================
    "P[ChrCustomize][AMSN]_SSS": (_T0, _T1),  # 2 UVs
    "P[ChrCustomize][EyeAO]": (_T0,),  # 1 UV
    # TODO: Eye uses a third 4D UV. Will need to be split in Blender.
    "P[ChrCustomize][Eye]": (_T0, _T1, _EY),  # 3 UVs; special Eye UVs  # MEDIUM
    "P[ChrCustomize][FaceHair]": (_T0, _DT, _FA),  # 3 UVs; like Hair
    "P[ChrCustomize][Hair]": (_T0, _DT, _FA),  # 3 UVs; like Hair

    # ========================================================================
    # M[AMSN] / M[AMSN_V] map family  (Confidence: HIGH)
    # Base: 1 UV, all groups on UV0.
    # [MbN]: adds UVBlend for blend factor storage.
    # [Ov_*]: overlay groups still use UV0 (get their own UV scale via group param).
    # [Snow], [Snow_VtxMask]: snow mask may add a UV.
    # ========================================================================
    "M[AMSN]": (_T0,),
    "M[AMSN][Mb2]": (_T0, _BL),  # 2 UVs; UV1 = blend factors
    "M[AMSN][Mb2][Ov_AN]": (_T0, _BL),  # 2 UVs
    "M[AMSN][Mb3]": (_T0, _BL),  # 2 UVs
    "M[AMSN][Mb3][Ov_AN]": (_T0, _BL),  # 2 UVs
    "M[AMSN][Snow]": (_T0,),
    "M[AMSN][Ov_N]_Skin_PaintDecal": (_T0, _T1),  # 2 UVs; UV1 = decal  # MEDIUM
    "M[AMSN_V]": (_T0,),
    "M[AMSN_V][Mb2]": (_T0, _BL),
    "M[AMSN_V][Mb2][Ov_AN]": (_T0, _BL),
    "M[AMSN_V][Mb2][Ov_N]": (_T0, _BL),
    "M[AMSN_V][Mb3]": (_T0, _BL),
    "M[AMSN_V][Mb3][Ov_N2_T]": (_T0, _BL),
    "M[AMSN_V][Mb3][Ov_AN]": (_T0, _BL),
    "M[AMSN_V][Mb3][Ov_N]": (_T0, _BL),
    "M[AMSN_V][Mb3][3Mask][Ov_N]": (_T0, _BL),
    "M[AMSN_V][Mb3][VC][3Mask][Ov_N][Cover]": (_T0, _T1, _BL),  # 3 UVs  # MEDIUM
    "M[AMSN_V][Ov_N]": (_T0,),
    "M[AMSN_V][Ov_N][Mb3_ColorAdjust][3Mask_ch18]": (_T0, _BL),  # 2 UVs
    "M[AMSN_V][Ov_N][Mb3_ColorAdjust][3Mask_ch18][Snow_VtxMask_ch19]": (_T0, _BL, _T1),  # 3 UVs  # MEDIUM
    "M[AMSN_V][Ov_N][Snow]": (_T0,),
    "M[AMSN_V][Ov_N][Snow]_Edge": (_T0,),
    "M[AMSN_V][Ov_N][Snow_VtxMask]": (_T0, _BL),  # 2 UVs; UV1 = snow mask
    "M[AMSN_V][Ov_N]_Edge": (_T0,),
    "M[AMSN_V][Ov_N]_Skin": (_T0,),
    "M[AMSN_V][Snow]": (_T0,),
    "M[AMSN_V][Snow_VtxMask]": (_T0, _BL),
    "M[AMSN_V][Snow_VtxMask]_Edge": (_T0, _BL),  # [1, 2] in FLVERs; using 2
    "M[AMSN_V]_Edge": (_T0,),
    "M[AMSN_V]_Grass": (_T0, _T1),  # 2 UVs; UV1 = grass wind  # MEDIUM
    "M[AMSN_V]_Grass2": (_T0, _T1, _T1, _T1),  # 4 UVs; grass animation  # LOW
    "M[AMSN_V]_Grass2_LOD1": (_T0, _T1, _T1),  # 3 UVs  # LOW
    "M[AMSN_V]_Grass2_test": (_T0, _T1, _T1),  # 3 UVs  # LOW
    "M[AMSN_V]_TestGrass": (_T0, _T1),  # 2 UVs
    "M[AMSN_V]_Vesitation": (_T0, _T1, _T1, _T1),  # 4 UVs  # LOW

    # ========================================================================
    # M[A] / M[Flower] / M[GhostTree]  (Confidence: MEDIUM)
    # ========================================================================
    "M[A]": (_T0,),
    "M[A]_Grass": (_T0, _T1),
    "M[Flower_m10]": (_T0, _T1, _T1, _T1),  # 4 UVs; flower animation  # LOW
    "M[GhostTree]": (_T0, _T1, _T1),  # 3 UVs  # LOW

    # ========================================================================
    # GXFlver legacy  (Confidence: MEDIUM)
    # DS3-era shaders with no metaparam groups.
    # ========================================================================
    "GXFlver_ColDif": (_T0,),
    "GXFlver_ColDifSpcBumpIbl": (_T0,),
    "GXFlver_Grass": (_T0, _T1),
    "GXFlver_GrassSpcBump": (_T0, _T1),

    # ========================================================================
    # CS[...] cutscene/VA variants  (Confidence: LOW)
    # High UV counts due to vertex animation frames.
    # ========================================================================
    "CS[VA_Frame][DetailBlend][S2][Rich]": (_T0, _DT, _T1, _T1, _T1, _T1),  # 6 UVs
    "CS[VA_Frame][Fur]_FurBlur": (_T0, _DT, _FA, _T1, _T1, _T1),  # 6 UVs
    "CS[c8901][Fur]_Burn": (_T0, _DT, _FA, _T1),  # 4 UVs
    "CS[c8901][VA_Frame][Fur]_Burn": (_T0, _DT, _FA, _T1, _T1, _T1, _T1),  # 7 UVs
    "CS[c8901][VA_Frame]_Burn": (_T0, _DT, _T1, _T1, _T1, _T1, _T1, _T1),  # 8 UVs
    "CS[c8901]_Burn": (_T0, _DT, _T1, _T1, _T1),  # 5 UVs

    # ========================================================================
    # C[cNNNN] character-specific: DetailBlend-like  (Confidence: MEDIUM)
    # These have groups 1(AMN) + detail AN groups (2/3/4/7) indicating DetailBlend structure.
    # ========================================================================
    "C[c2030]_Fabric": (_T0, _T1, _DT),  # 3 UVs; groups 1,2,4,5,7,8,9 → DB[S2]-like  # CONFIRMED
    "C[c4460]_Oil": (_T0, _DT),  # 2 UVs; groups 1,2,4
    "C[c4480]_Flower_1": (_T0, _DT),  # 2 UVs; full DetailBlend group set
    "C[c4520]_Dragon": (_T0, _DT, _T1),  # 3 UVs; groups 1,2,4,7 + extra 10,14
    "C[c4720]_Beast": (_T0, _DT, _T1, _T1),  # 4 UVs; DB + extra effect groups  # LOW
    "C[c4950]_Ghost": (_T0, _DT),  # 2 UVs; full DetailBlend set + emissive group
    "C[c3200]_Costume": (_T0, _DT, _T1),  # 3 UVs; groups 1,2,9

    # ========================================================================
    # C[cNNNN] character-specific: Fur-like  (Confidence: MEDIUM)
    # ========================================================================
    "C[c2120]_Clone_Butterfly": (_T0, _DT, _FA),  # 3 UVs; groups 1(AN),2(AMN)
    "C[c2500]_Fade_Fur": (_T0, _DT, _FA),  # 3 UVs; Fur + emissive
    "C[c3200]_Fur": (_T0, _DT, _FA, _T1),  # 4 UVs; Fur + extra group_6
    "C[c3200]_Shell": (_T0, _DT, _FA),  # 3 UVs; Shell-like  # LOW
    "C[c4503]_Freeze_Fur": (_T0, _T1, _DT),  # 3 UVs; AMSN + freeze + detail  # MEDIUM
    "C[c5130]_Hair": (_T0, _DT, _FA),  # 3 UVs; groups 1(AN),2(AMN),5
    "C[c5220]_Mipuella_Hair": (_T0, _DT, _FA),  # 3 UVs; groups 1(AND),2(AMN)
    "C[c5330]_Trina_Hair": (_T0, _DT, _FA, _T1),  # 4 UVs; Fur + extra mask

    # ========================================================================
    # C[cNNNN] character-specific: Crystal-like  (Confidence: MEDIUM)
    # Have DistortionDepth groups. All samplers on UV0.
    # ========================================================================
    "C[c3300]_Mercury": (_T0, _T1),  # 2 UVs
    "C[c4190]_Crystal": (_T0, _T1),  # 2 UVs
    "C[c4190]_Est": (_T0, _T1),  # 2 UVs
    "C[c4620]_Galaxy": (_T0, _T1),  # 2 UVs
    "C[c5050]_Crystal_Blend": (_T0, _T1, _T1),  # 3 UVs  # LOW
    "C[c5200]_Sun": (_T0, _T1),  # 2 UVs
    "C[c4180]_Glow": (_T0, _T1),  # 2 UVs; Crystal-like + effects

    # ========================================================================
    # C[cNNNN] character-specific: AMSN-like (simple)  (Confidence: MEDIUM-HIGH)
    # Primarily group_1 with AMN. Extra groups share UV0.
    # ========================================================================
    "C[c2120]_Arts_Petal": (_T0, _T1),  # 2 UVs; group_1 only
    "C[c2120]_Clone_Blade": (_T0, _T1),  # 2 UVs
    "C[c2200]_Rune": (_T0, _T1),  # 2 UVs
    "C[c2500]_Fade": (_T0, _T1),  # 2 UVs; like AMSN_Arts
    "C[c3320]_Triplanar": (_T0, _T1),  # 2 UVs
    "C[c4150]_Eye": (_T0, _T1),  # 2 UVs
    "C[c4280]_Honey": (_T0, _T1),  # 2 UVs; ClearCoat-like
    "C[c4450]_AreaMatchBlend": (_T0, _T1),  # 2 UVs; many groups all UV0
    "C[c4450]_Shell": (_T0, _T1),  # 2 UVs; Shell-like but only 2 UVs
    "C[c4503]_Freeze": (_T0, _T1),  # 2 UVs
    "C[c4503]_Freeze_ContactFade": (_T0, _T1),  # 2 UVs
    "C[c4620]_ClearCoat": (_T0, _T1),  # 2 UVs
    "C[c4640]_Body": (_T0, _T1),  # 2 UVs; complex groups all UV0
    "C[c4640]_Tentacles": (_T0, _T1),  # 2 UVs
    "C[c4650]_Freeze_ContactFade": (_T0, _T1),  # 2 UVs
    "C[c4710]_Eye": (_T0, _T1),  # 2 UVs
    "C[c4720]_Beast_Light": (_T0, _T1),  # 2 UVs
    "C[c4760]_Eye": (_T0, _T1),  # 2 UVs
    "C[c5030]_Wing": (_T0, _T1),  # 2 UVs
    "C[c5051]_Fire": (_T0, _T1),  # 2 UVs
    "C[c5110]_Weapon": (_T0, _T1),  # 2 UVs
    "C[c5130]_Eye": (_T0, _T1),  # 2 UVs (like Eye_Glow)
    "C[c5131]_Eye": (_T0, _T1),  # 2 UVs
    "C[c5132]_Dark": (_T0, _T1),  # 2 UVs
    "C[c5170]_Burn": (_T0, _T1),  # 2 UVs (like AMSN_Burn)
    "C[c5210]_Eye": (_T0, _T1),  # 2 UVs
    "C[c5270]_Jelly": (_T0, _T1),  # 2 UVs
    "C[c3350]_Crystal": (_T0, _T1),  # 2 UVs; Crystal-like
    "C[c3400]_Fade": (_T0, _T1),  # 2 UVs
    "C[c4180]_Innner": (_T0,),  # 1 UV
    "C[c4980]_Lwing": (_T0,),  # 1 UV
    "C[c2190]_Smoke": (_T0,),  # 1 UV

    # ========================================================================
    # C[cNNNN] character-specific: unique/complex  (Confidence: LOW)
    # ========================================================================
    "C[c2050]_Ghost": (_T0, _T1, _T1),  # 3 UVs; single group_3
    "C[c2070]_GlowMud": (_T0, _T1, _T1, _T1),  # 4 UVs; complex groups
    "C[c2120]_Clone_BodyGlow": (_T0, _T1, _T1),  # 3 UVs; groups 1,2,3
    "C[c2180]_Eye": (_T0, _T1, _T1),  # 3 UVs
    "C[c2190]_Hair_ColorBlend": (_T0, _DT, _FA, _T1),  # 4 UVs; Hair-like  # MEDIUM
    "C[c2190]_Rune": (_T0, _T1, _T1),  # 3 UVs; ungrouped only
    "C[c2191]_Fog": (_T0, _T1),  # 2 UVs; single group_4
    "C[c2200]_Body": (_T0, _T1, _T1, _T1),  # 4 UVs; complex
    "C[c4190]_Rune": (_T0, _T1, _T1),  # 3 UVs; single group_1
    "C[c4760]_Rope": (_T0, _T1, _T1, _T1),  # 4 UVs; groups 1,3
    "C[c5020]_Oil": (_T0, _T1, _T1, _T1),  # 4 UVs; unique oil shader
    "C[c5051]_Robe": (_T0, _T1, _T1),  # 3 UVs; groups 1,2
    "C[c5060]_Body": (_T0, _DT, _T1),  # 3 UVs; groups 1(AMN),2(AN),6(AN) → DB-like
    "C[c5070]_Fire": (_T0, _T1, _T1),  # 3 UVs; fire effects
    "C[c5110]_Glow": (_T0, _T1, _T1, _T1),  # 4 UVs; Crystal-like + effects
    "C[c5120]_Phantom_Wing": (_T0, _T1, _T1),  # 3 UVs
    "C[c5130]_Fade": (_T0, _T1, _T1, _T1),  # 4 UVs
    "C[c5132]_TexScroll": (_T0, _T1, _T1, _T1),  # 4 UVs
    "C[c5220]_Mipuella": (_T0, _DT, _T1),  # 3 UVs; groups 1(AMN),2(AN),6(AN) → DB-like
    "C[c5500]_Magma": (_T0, _T1, _T1),  # 3 UVs; groups 1,2
    "C[c5500]_Magma_VtxAni": (_T0, _T1, _T1, _T1, _T1, _T1),  # 6 UVs; + VA
    "C[c5590]_Oil": (_T0, _T1, _T1),  # 3 UVs
    "C[c3320]_VA_Frame": (_T0, _T1, _T1, _T1, _T1),  # 5 UVs; VA variant

    # ========================================================================
    # Misc / test shaders  (Confidence: LOW)
    # ========================================================================
    "Fujir_2UV_Fur_Test2": (_T0, _T1, _T1),  # 3 UVs; test shader
    "Fujir_MaterialBasedBlendShader_Metalic_Test3": (_T0, _T1),  # 2 UVs
    "Fujir_MaterialBasedBlendShader_Metalic_Test3_BGUV2": (_T0, _T1, _T1),  # 3 UVs
    "Wyburn_Rune": (_T0, _T1),  # 2 UVs; ungrouped
}


SHADER_GROUP_UV: dict[str, dict[str, str]] = {

    # ========================================================================
    # C[AMSN] family  (Confidence: HIGH)
    # ========================================================================
    "C[AMSN]": {"group_1": _T0},
    "C[AMSN][PixelKill]": {"group_1": _T0},
    "C[AMSN][PixelKill][ID1]": {"group_1": _T0},
    "C[AMSN][VA_Loop]": {"group_1": _T0, "group_2": _T0},
    "C[AMSN]_Alpha": {"group_1": _T0},
    "C[AMSN]_Arts": {"group_1": _T0, "group_2": _T0},
    "C[AMSN]_Arts_Enchant": {"group_1": _T0, "group_2": _T0},
    "C[AMSN]_Burn": _all_uv0("group_1", "group_2", "group_11", "group_12"),
    "C[AMSN]_ClearCoat": {"group_1": _T0, "group_2": _T0},
    "C[AMSN]_ContactFade": {"group_1": _T0},
    "C[AMSN]_Glow": {"group_1": _T0},
    "C[AMSN]_GlowDepthFade_[Int]": {"group_1": _T0},
    "C[AMSN]_Glow[Int]": {"group_1": _T0},
    "C[AMSN]_Glow_[PixelKill]": {"group_1": _T0},
    "C[AMSN]_Shadow": {"group_1": _T0},

    # ========================================================================
    # C[DetailBlend] family  (Confidence: HIGH)
    # ========================================================================
    "C[DetailBlend]": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_7": _DT, "group_8": _T0,
    },
    "C[DetailBlend][Rich]": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_7": _DT, "group_8": _T0,
    },
    "C[DetailBlend]_SSS": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_7": _DT, "group_9": _T0,
    },
    "C[DetailBlend]_FurBlur": {
        "group_1": _T0, "group_2": _DT, "group_4": _DT,
        "group_7": _DT, "group_8": _T0, "group_9": _T0,
    },
    "C[DetailBlend]_ShellBlur": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_7": _DT, "group_8": _T0, "group_9": _T0,
    },
    "C[DetailBlend][S2]": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_5": _T1, "group_7": _DT, "group_8": _T0,
    },
    "C[DetailBlend][1_0_0_0][S2]_Glow[Int]": {
        "group_1": _T0, "group_2": _DT, "group_5": _T1,
    },
    "C[DetailBlend][VA_Morph]": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_7": _DT, "group_8": _T0, "group_9": _T1,
    },

    # ========================================================================
    # C[Fur] family  (Confidence: HIGH)
    # ========================================================================
    "C[Fur]": {"group_1": _FA, "group_2": _T0, "group_3": _DT},
    "C[Fur]_Albedo_FallOff": {"group_1": _FA, "group_2": _T0, "group_3": _DT},
    "C[Fur]_Arts": {"group_1": _FA, "group_2": _T0, "group_3": _DT, "group_5": _T0},
    "C[Fur]_FurBlur": {"group_1": _FA, "group_2": _T0, "group_3": _DT, "group_6": _T0},
    "C[Fur]_FurBlur_Tr": {"group_1": _FA, "group_2": _T0, "group_3": _DT, "group_6": _T0},
    "C[Fur]_Glow": {"group_1": _FA, "group_2": _T0, "group_6": _T0},
    "C[Fur]_Tr": {"group_1": _FA, "group_2": _T0, "group_3": _DT},

    # ========================================================================
    # C[Hair] family  (Confidence: MEDIUM)
    # ========================================================================
    "C[Hair]": {"group_1": _T0},
    "C[Hair][ChrCustomize]": {"group_1": _T0},

    # ========================================================================
    # C[Crystal] family  (Confidence: HIGH)
    # ========================================================================
    "C[Crystal]": _all_uv0("group_1", "group_3", "group_4"),
    "C[Crystal]_Glow": _all_uv0("group_1", "group_3", "group_4"),
    "C[Crystal]_Tr": _all_uv0("group_1", "group_3", "group_4"),
    "C[Crystal_NoTransparent]": _all_uv0("group_1", "group_3"),
    "C[Crystal_NoTransparent]_Glow": _all_uv0("group_1", "group_3"),

    # ========================================================================
    # C[Face] family  (Confidence: HIGH)
    # ========================================================================
    "C[Face][S2]_SSS": {
        "group_1": _T0, "group_11": _SN, "group_12": _DT, "group_13": _DT, "group_18": _T0,
    },

    # ========================================================================
    # C[Eye] family  (Confidence: HIGH)
    # ========================================================================
    "C[Eye]_Glow": {"group_1": _T0, "group_3": _T0},

    # ========================================================================
    # C[Shell] family  (Confidence: HIGH)
    # FUR_ALPHA collapses to UV0 with only 2 UVs.
    # ========================================================================
    "C[Shell]": {"group_1": _T0, "group_2": _T0, "group_5": _DT},
    "C[Shell]_FurBlur": {"group_1": _T0, "group_2": _T0, "group_5": _DT, "group_7": _T0},

    # ========================================================================
    # P[ChrCustomize] family  (Confidence: MEDIUM-HIGH)
    # ========================================================================
    "P[ChrCustomize][AMSN]_SSS": {"group_1": _T0},
    "P[ChrCustomize][EyeAO]": {"": _T0},
    "P[ChrCustomize][Eye]": {"group_3": _T0},
    "P[ChrCustomize][FaceHair]": {"group_1": _T0},
    "P[ChrCustomize][Hair]": {"group_1": _T0},

    # ========================================================================
    # M[AMSN] / M[AMSN_V] map family  (Confidence: HIGH)
    # All sampler groups use UV0. Extra UVs (blend, snow) are non-sampler.
    # ========================================================================
    "M[AMSN]": {"group_1": _T0},
    "M[AMSN][Mb2][Ov_AN]": _all_uv0("group_1", "group_2", "group_3", ""),
    "M[AMSN][Mb3][Ov_AN]": _all_uv0("group_1", "group_2", "group_3", "group_4", ""),
    "M[AMSN][Snow]": _all_uv0("group_1", "group_2"),
    "M[AMSN][Ov_N]_Skin_PaintDecal": {"group_1": _T0, "group_2": _T0},
    "M[AMSN_V]": {"group_1": _T0},
    "M[AMSN_V][Mb2][Ov_AN]": _all_uv0("group_1", "group_2", "group_3", ""),
    "M[AMSN_V][Mb2][Ov_N]": _all_uv0("group_1", "group_2", "group_3", ""),
    "M[AMSN_V][Mb3][VC][3Mask][Ov_N][Cover]": _all_uv0("group_1", "group_2", "group_3", "group_5", "group_6"),
    "M[AMSN_V][Ov_N]": {"group_1": _T0},
    "M[AMSN_V][Ov_N][Mb3_ColorAdjust][3Mask_ch18]": _all_uv0(
        "group_1", "group_2", "group_3", "group_5", "group_6", "group_7",
    ),
    "M[AMSN_V][Ov_N][Mb3_ColorAdjust][3Mask_ch18][Snow_VtxMask_ch19]": _all_uv0(
        "group_1", "group_2", "group_3", "group_5", "group_6", "group_7", "group_8",
    ),
    "M[AMSN_V][Ov_N][Snow]": _all_uv0("group_1", "group_2", "group_3"),
    "M[AMSN_V][Ov_N][Snow]_Edge": _all_uv0("group_1", "group_2", "group_3"),
    "M[AMSN_V][Ov_N][Snow_VtxMask]": _all_uv0("group_1", "group_2", ""),
    "M[AMSN_V][Ov_N]_Edge": {"group_1": _T0, "": _T0},
    "M[AMSN_V][Ov_N]_Skin": {"group_1": _T0},
    "M[AMSN_V][Snow]": _all_uv0("group_1", "group_2"),
    "M[AMSN_V][Snow_VtxMask]": _all_uv0("group_1", "group_2", ""),
    "M[AMSN_V][Snow_VtxMask]_Edge": _all_uv0("group_1", "group_2", ""),
    "M[AMSN_V]_Edge": {"group_1": _T0},
    "M[AMSN_V]_Grass": {"group_1": _T0},
    "M[AMSN_V]_Grass2": _all_uv0("group_2", "group_6"),
    "M[AMSN_V]_Grass2_LOD1": _all_uv0("group_2", "group_5"),
    "M[AMSN_V]_Grass2_test": {"group_2": _T0},
    "M[AMSN_V]_TestGrass": {"group_2": _T0},
    "M[AMSN_V]_Vesitation": {"group_2": _T0},

    # ========================================================================
    # M[A] / M[Flower] / M[GhostTree]  (Confidence: MEDIUM)
    # ========================================================================
    "M[A]": {"": _T0},
    "M[A]_Grass": {"": _T0},
    "M[Flower_m10]": _all_uv0("group_2", "group_7"),
    "M[GhostTree]": _all_uv0("group_1", "group_7"),

    # ========================================================================
    # GXFlver legacy  (Confidence: MEDIUM)
    # No metaparam groups. All samplers ungrouped on UV0.
    # ========================================================================
    "GXFlver_ColDif": {"": _T0},
    "GXFlver_ColDifSpcBumpIbl": {"": _T0},
    "GXFlver_Grass": {"": _T0},
    "GXFlver_GrassSpcBump": {"": _T0},

    # ========================================================================
    # CS[...] cutscene/VA variants  (Confidence: LOW)
    # Same group UV as their base family; VA UVs are non-sampler.
    # ========================================================================
    "CS[VA_Frame][DetailBlend][S2][Rich]": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_5": _T1, "group_7": _DT, "group_8": _T0, "group_9": _T0, "group_10": _T0,
    },
    "CS[VA_Frame][Fur]_FurBlur": {
        "group_1": _FA, "group_2": _T0, "group_3": _DT, "group_6": _T0, "group_7": _T0,
    },
    "CS[c8901][Fur]_Burn": {"group_1": _FA, "group_2": _T0, "group_5": _T0},
    "CS[c8901][VA_Frame][Fur]_Burn": {"group_1": _FA, "group_2": _T0, "group_5": _T0, "group_6": _T0},
    "CS[c8901][VA_Frame]_Burn": {
        "group_1": _T0, "group_2": _DT, "group_4": _DT, "group_7": _DT,
        "group_10": _T0, "group_11": _T0, "group_12": _T0,
    },
    "CS[c8901]_Burn": {
        "group_1": _T0, "group_2": _DT, "group_4": _DT, "group_7": _DT,
        "group_10": _T0, "group_11": _T0,
    },

    # ========================================================================
    # C[cNNNN] character-specific: DetailBlend-like  (Confidence: MEDIUM)
    # ========================================================================
    "C[c2030]_Fabric": {
        "group_1": _T0, "group_2": _DT, "group_4": _DT, "group_5": _T1,
        "group_7": _DT, "group_8": _DT, "group_9": _DT,
    },
    "C[c4460]_Oil": {"group_1": _T0, "group_2": _DT, "group_4": _DT},
    "C[c4480]_Flower_1": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_7": _DT, "group_9": _T0, "group_11": _T0,
    },
    "C[c4520]_Dragon": {
        "group_1": _T0, "group_2": _DT, "group_4": _DT, "group_7": _DT,
        "group_10": _T1, "group_14": _T0,
    },
    "C[c4720]_Beast": {
        "group_1": _T0, "group_2": _DT, "group_4": _DT, "group_7": _DT,
        "group_12": _T1, "group_13": _T1,
    },
    "C[c4950]_Ghost": {
        "group_1": _T0, "group_2": _DT, "group_3": _DT, "group_4": _DT,
        "group_7": _DT, "group_8": _T0, "group_9": _T0,
    },
    "C[c3200]_Costume": {"group_1": _T0, "group_2": _DT, "group_9": _T0},

    # ========================================================================
    # C[cNNNN] character-specific: Fur-like  (Confidence: MEDIUM)
    # ========================================================================
    "C[c2120]_Clone_Butterfly": {"group_1": _FA, "group_2": _T0},
    "C[c2500]_Fade_Fur": {"group_1": _FA, "group_2": _T0, "group_3": _DT, "group_5": _T0},
    "C[c3200]_Fur": {"group_1": _FA, "group_2": _T0, "group_6": _T0},
    "C[c3200]_Shell": {"group_1": _T0, "group_2": _T0, "group_6": _T0},
    "C[c4503]_Freeze_Fur": {"group_1": _T0, "group_2": _T0, "group_6": _DT},
    "C[c5130]_Hair": {"group_1": _FA, "group_2": _T0, "group_5": _T0},
    "C[c5220]_Mipuella_Hair": {"group_1": _FA, "group_2": _T0},
    "C[c5330]_Trina_Hair": {"group_1": _FA, "group_2": _T0, "group_6": _T0},

    # ========================================================================
    # C[cNNNN] character-specific: Crystal-like  (Confidence: MEDIUM)
    # ========================================================================
    "C[c3300]_Mercury": _all_uv0("group_1", "group_3"),
    "C[c4190]_Crystal": _all_uv0("group_1", "group_3"),
    "C[c4190]_Est": _all_uv0("group_1", "group_3"),
    "C[c4620]_Galaxy": _all_uv0("group_1", "group_3"),
    "C[c5050]_Crystal_Blend": _all_uv0("group_1", "group_3", "group_8"),
    "C[c5200]_Sun": _all_uv0("group_1", "group_3", "group_4"),
    "C[c4180]_Glow": _all_uv0("group_1", "group_2", "group_3", "group_4"),

    # ========================================================================
    # C[cNNNN] character-specific: AMSN-like  (Confidence: MEDIUM-HIGH)
    # ========================================================================
    "C[c2120]_Arts_Petal": {"group_1": _T0},
    "C[c2120]_Clone_Blade": _all_uv0("group_1", "group_2"),
    "C[c2200]_Rune": _all_uv0("group_1", "group_2", "group_3"),
    "C[c2500]_Fade": _all_uv0("group_1", "group_2"),
    "C[c3320]_Triplanar": {"group_1": _T0},
    "C[c4150]_Eye": _all_uv0("group_1", "group_3"),
    "C[c4280]_Honey": _all_uv0("group_1", "group_2", "group_6"),
    "C[c4450]_AreaMatchBlend": _all_uv0("group_1", "group_3", "group_4", "group_5", "group_6", "group_7"),
    "C[c4450]_Shell": _all_uv0("group_1", "group_2"),
    "C[c4503]_Freeze": _all_uv0("group_1", "group_2", "group_3", "group_5", "group_6"),
    "C[c4503]_Freeze_ContactFade": _all_uv0("group_1", "group_2"),
    "C[c4620]_ClearCoat": _all_uv0("group_1", "group_2"),
    "C[c4640]_Body": _all_uv0("group_1", "group_3", "group_4", "group_5"),
    "C[c4640]_Tentacles": _all_uv0("group_1", "group_3", "group_4"),
    "C[c4650]_Freeze_ContactFade": _all_uv0("group_1", "group_2"),
    "C[c4710]_Eye": _all_uv0("group_1", "group_3"),
    "C[c4720]_Beast_Light": {"group_1": _T0},
    "C[c4760]_Eye": _all_uv0("group_1", "group_2", "group_4", "group_5"),
    "C[c5030]_Wing": _all_uv0("group_1", "group_3"),
    "C[c5051]_Fire": {"group_1": _T0},
    "C[c5110]_Weapon": {"group_1": _T0},
    "C[c5130]_Eye": _all_uv0("group_1", "group_3"),
    "C[c5131]_Eye": _all_uv0("group_1", "group_3"),
    "C[c5132]_Dark": {"group_1": _T0},
    "C[c5170]_Burn": _all_uv0("group_1", "group_2", "group_11", "group_12"),
    "C[c5210]_Eye": _all_uv0("group_1", "group_3"),
    "C[c5270]_Jelly": _all_uv0("group_1", "group_2"),
    "C[c3350]_Crystal": _all_uv0("group_2", "group_4", "group_6", "group_10"),
    "C[c3400]_Fade": _all_uv0("group_1", "group_2", "group_3", "group_5"),
    "C[c4180]_Innner": {"group_1": _T0},
    "C[c4980]_Lwing": {"group_1": _T0},
    "C[c2190]_Smoke": _all_uv0("group_1", "group_2"),

    # ========================================================================
    # C[cNNNN] character-specific: unique/complex  (Confidence: LOW)
    # ========================================================================
    "C[c2050]_Ghost": {"group_3": _T0},
    "C[c2070]_GlowMud": _all_uv0("group_1", "group_2", "group_3", "group_4"),
    "C[c2120]_Clone_BodyGlow": _all_uv0("group_1", "group_2", "group_3"),
    "C[c2180]_Eye": _all_uv0("group_1", "group_3"),
    "C[c2190]_Hair_ColorBlend": {"group_1": _T0, "group_3": _T0},
    "C[c2190]_Rune": {"": _T0},
    "C[c2191]_Fog": {"group_4": _T0},
    "C[c2200]_Body": _all_uv0("group_1", "group_2", "group_3", "group_4", "group_5"),
    "C[c4190]_Rune": {"group_1": _T0},
    "C[c4760]_Rope": _all_uv0("group_1", "group_3"),
    "C[c5020]_Oil": _all_uv0("group_1", "group_3", "group_5", "group_6"),
    "C[c5051]_Robe": _all_uv0("group_1", "group_2"),
    "C[c5060]_Body": {"group_1": _T0, "group_2": _DT, "group_6": _DT},
    "C[c5070]_Fire": _all_uv0("group_1", "group_2", "group_3"),
    "C[c5110]_Glow": _all_uv0("group_1", "group_2", "group_3", "group_4", "group_5"),
    "C[c5120]_Phantom_Wing": _all_uv0("group_1", "group_2", "group_5"),
    "C[c5130]_Fade": _all_uv0("group_1", "group_3", "group_4", "group_7", "group_8"),
    "C[c5132]_TexScroll": _all_uv0("group_1", "group_2"),
    "C[c5220]_Mipuella": {"group_1": _T0, "group_2": _DT, "group_6": _DT},
    "C[c5500]_Magma": _all_uv0("group_1", "group_2"),
    "C[c5500]_Magma_VtxAni": _all_uv0("group_1", "group_2", "group_3"),
    "C[c5590]_Oil": _all_uv0("group_1", "group_3", "group_5", "group_6"),
    "C[c3320]_VA_Frame": _all_uv0("group_1", "group_2"),

    # ========================================================================
    # Misc / test shaders  (Confidence: LOW)
    # ========================================================================
    "Fujir_2UV_Fur_Test2": {"": _T0},
    "Fujir_MaterialBasedBlendShader_Metalic_Test3": {"": _T0},
    "Fujir_MaterialBasedBlendShader_Metalic_Test3_BGUV2": {"": _T0},
    "Wyburn_Rune": {"": _T0},
}


def _normalize_stem(stem: str) -> str:
    """Strip `_cloth` suffix for lookup, since cloth variants always share UV structure with their base."""
    if stem.endswith("_cloth"):
        return stem[:-6]
    return stem


def get_shader_uv_slots(shader_stem: str) -> tuple[str, ...] | None:
    """Look up the ordered UV semantic tuple for a shader stem.

    Returns None if not found (caller should fall back to heuristics).
    """
    norm = _normalize_stem(shader_stem)
    return SHADER_UV_SLOTS.get(norm)


def get_shader_group_uv(shader_stem: str) -> dict[str, str] | None:
    """Look up the group-to-UV-semantic mapping for a shader stem.

    Returns None if not found (caller should fall back to heuristics).
    """
    norm = _normalize_stem(shader_stem)
    return SHADER_GROUP_UV.get(norm)


def _fallback_uv_for_role(role: SamplerGroupRole, profile: ShaderProfile) -> str:
    """Heuristic fallback UV assignment when explicit mapping is unavailable."""
    if profile.is_map:
        return _T0  # map shaders: all groups use UV0

    _ROLE_TO_UV = {
        SamplerGroupRole.UNGROUPED: _T0,
        SamplerGroupRole.PRIMARY: _T0,
        SamplerGroupRole.SECONDARY: _T0,
        SamplerGroupRole.DETAIL: _DT,
        SamplerGroupRole.FUR_ALPHA: _FA,
        SamplerGroupRole.OVERLAY: _DT,
        SamplerGroupRole.SUB_NORMALS: _SN,
        SamplerGroupRole.BLEND_CONTROL: _T0,
        SamplerGroupRole.EFFECT: _T0,
        SamplerGroupRole.MISC: _T0,
    }
    return _ROLE_TO_UV.get(role, _T0)


# endregion


@dataclass(slots=True, repr=False)
class MatDef(_BaseMatDef):
    """Elden Ring material definition parser.

    Uses SHADER_UV_SLOTS and SHADER_GROUP_UV dictionaries to determine which UV layer each sampler uses, falling back
    to role-based heuristics for unknown shaders.
    """

    class UVLayer(IntEnum):
        UVTexture0 = auto()
        UVTexture1 = auto()
        UVDetail = auto()
        UVFurAlpha = auto()
        UVSubNormals = auto()
        UVBlend = auto()
        UVEye2D = auto()
        UVEye4D = auto()

    METAPARAMS: tp.ClassVar[dict[str, dict[str, list[tuple[str, str]]]]] = read_json(
        SOULSTRUCT_PATH("eldenring/models/resources/er_shader_sampler_groups.json")
    )

    NAME_TAG_RE: tp.ClassVar[dict[str, re.Pattern]] = {
        "Multi": re.compile(r".*\[Mb(\d+).*\].*"),
        "Alpha": re.compile(r".*_Alpha(_.*|$)", re.IGNORECASE),
        "Edge": re.compile(r".*_Edge(_.*|$)", re.IGNORECASE),
    }

    EXTRA_SHADER_UV_LAYERS: tp.ClassVar[dict[str, list[UVLayer]]] = {
        "P[ChrCustomize][Eye]": [UVLayer.UVEye2D, UVLayer.UVEye4D],
    }

    USES_MATBIN: tp.ClassVar[bool] = True

    # --- Instance fields ---
    profile: ShaderProfile = field(default_factory=ShaderProfile)
    metaparam: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    matbin_params: dict[str, tp.Any] = field(default_factory=dict)
    cloth: bool = False
    fur: bool = False

    @classmethod
    def from_matbin(cls, matbin: MATBIN) -> tp.Self:
        """Extract material definition from a MATBIN using shader metaparam JSON and explicit UV slot dictionaries."""
        metaparam = cls.METAPARAMS.get(matbin.shader_stem, None)
        if not metaparam:
            raise MatDefError(
                f"No shader metaparam information known to Soulstruct for Elden Ring shader '{matbin.shader_name}'. "
                f"Cannot parse material definition, as sampler groups cannot be determined from their names alone."
            )

        matbin_name = matbin.path.name if matbin.path is not None else ""
        profile = ShaderProfile.from_shader_stem(matbin.shader_stem)

        matbin_params = {param.name: param.value for param in matbin.params}
        matbin_params = {k: matbin_params[k] for k in sorted(matbin_params, key=natural_keys)}

        matdef = cls(
            name=matbin_name,
            shader_stem=matbin.shader_stem,
            profile=profile,
            metaparam=metaparam,
            matbin=matbin,
            matbin_params=matbin_params,
        )  # type: MatDef

        # Detect blend mode (same param as MTD-based games).
        blend_mode = matbin.get_param("g_BlendMode", default=0)
        if blend_mode == 1:
            matdef.edge = True
        elif blend_mode == 2:
            matdef.alpha = True

        # Also check profile suffixes for Alpha/Edge (some shaders encode it in the stem rather than BlendMode).
        if profile.is_alpha:
            matdef.alpha = True
        if profile.is_edge:
            matdef.edge = True

        # Cloth is a MATBIN param, generally accompanied by '_cloth' string in shader stem.
        matdef.cloth = matbin.get_param("GXFT_Cloth", False)

        # Look up explicit UV mappings; fall back to role-based heuristics if unavailable.
        group_uv_map = get_shader_group_uv(matbin.shader_stem)

        # Collect sampler groups from metaparam.
        grouped_sampler_names, sampler_default_paths = cls._collect_metaparam_samplers(metaparam, matbin)
        # If all samplers are ungrouped (single "" key), attempt heuristic grouping.
        if len(grouped_sampler_names) == 1 and "" in grouped_sampler_names:
            grouped_sampler_names = cls._guess_sampler_groups(grouped_sampler_names[""])

        # Sort group names: numbered groups in natural order, ungrouped ("") last.
        sorted_names = cls._sorted_group_names(grouped_sampler_names)

        # Track how many groups of each role we've seen (for alias disambiguation).
        role_counts: dict[SamplerGroupRole, int] = {role: 0 for role in SamplerGroupRole}

        is_first = True
        for group_name in sorted_names:
            group_sampler_names = grouped_sampler_names[group_name]

            # Parse group index and UV scale from MATBIN params.
            if group_name:
                group_index = int(group_name.split("_")[1])  # e.g. 'group_3' -> 3
                uv_param = f"{group_name}_CommonUV-UVParam"
                uv_scale = Vector2(matbin.get_param(uv_param, default=(1.0, 1.0)))
            else:
                group_index = 0
                uv_scale = None

            # Determine role (for aliases and node tree builder).
            role = get_group_role(profile, group_index, group_sampler_names, is_first=is_first)
            role_index = role_counts[role]
            is_first = False

            # Determine UV layer from explicit dict, or fall back to role-based heuristic.
            if group_uv_map is not None:
                uv_layer_name = group_uv_map.get(group_name, _T0)
            else:
                uv_layer_name = _fallback_uv_for_role(role, profile)
            uv_layer = cls.UVLayer[uv_layer_name]

            # Track per-map-type counts within this group for alias disambiguation.
            type_counts_in_group: dict[str, int] = {}
            # Store first sampler of each type in case we need to retroactively add '_0' suffix.
            first_of_type: dict[str, MatDefSampler] = {}

            for sampler_name in group_sampler_names:
                map_type = extract_map_type(sampler_name)

                # Mask3 always uses UVTexture0 regardless of group assignment.
                if map_type == "Mask3":
                    sampler_uv_layer = cls.UVLayer.UVTexture0
                else:
                    sampler_uv_layer = uv_layer

                # Build alias: "{RoleName} {role_index} {MapType}"
                if map_type:
                    alias = f"{role.name} {role_index} {map_type}"
                else:
                    alias = ""  # will fall back to raw sampler name

                # Disambiguate if multiple samplers of the same map type exist in this group.
                prime_first = False
                if map_type:
                    if map_type not in type_counts_in_group:
                        prime_first = True
                        type_counts_in_group[map_type] = 1
                    else:
                        count = type_counts_in_group[map_type]
                        alias += f"_{count}"
                        if map_type in first_of_type:
                            # Retroactively add '_0' to the first sampler's alias.
                            first_of_type[map_type].alias += "_0"
                            first_of_type.pop(map_type)
                        type_counts_in_group[map_type] += 1

                sampler = matdef.add_sampler(
                    name=sampler_name,
                    alias=alias or sampler_name,  # fallback to raw name
                    uv_layer=sampler_uv_layer,
                    sampler_group=group_index,
                    uv_scale=uv_scale,
                    default_texture_path=sampler_default_paths[sampler_name],
                    matbin_texture_path=matbin.get_sampler_path(sampler_name),
                )

                if prime_first:
                    first_of_type[map_type] = sampler

            role_counts[role] += 1

        return matdef

    @classmethod
    def from_matbin_name(cls, matbin_name: str):
        """Too much required metadata for this, currently."""
        raise MatDefError(
            "Cannot yet parse Elden Ring material from MATBIN name alone. `MATBIN` instance must be given."
        )

    def get_uv_slot_tuple(self) -> tuple[UVLayer, ...]:
        """Get the authoritative ordered UV slot tuple for this shader.

        Prefers the explicit SHADER_UV_SLOTS dictionary. Falls back to sorted used UV layers + extras.
        """
        slots = get_shader_uv_slots(self.shader_stem)
        if slots is not None:
            return tuple(self.UVLayer[name] for name in slots)
        # Fallback: use UV layers found on samplers + any extras.
        return tuple(self.get_used_uv_layers())

    # region Private Helpers

    @staticmethod
    def _collect_metaparam_samplers(
        metaparam: dict[str, list[tuple[str, str]]],
        matbin: MATBIN,
    ) -> tuple[dict[str, list[str]], dict[str, str]]:
        """Collect grouped sampler names and default texture paths from metaparam and MATBIN.

        Returns (grouped_sampler_names, sampler_default_paths).
        """
        grouped_sampler_names: dict[str, list[str]] = {}
        sampler_default_paths: dict[str, str] = {}
        found_metaparam_samplers: set[str] = set()

        for group_name, samplers in metaparam.items():
            grouped_sampler_names[group_name] = []
            for sampler_name, default_texture_path in samplers:
                grouped_sampler_names[group_name].append(sampler_name)
                sampler_default_paths[sampler_name] = default_texture_path
                found_metaparam_samplers.add(sampler_name)

        # Samplers in MATBIN but not in metaparam go into the ungrouped ("") bucket.
        for sampler in matbin.samplers:
            if sampler.sampler_type not in found_metaparam_samplers:
                grouped_sampler_names.setdefault("", []).append(sampler.sampler_type)
                sampler_default_paths[sampler.sampler_type] = sampler.path

        return grouped_sampler_names, sampler_default_paths

    @staticmethod
    def _sorted_group_names(grouped_sampler_names: dict[str, list[str]]) -> list[str]:
        """Sort group names: numbered groups in natural order, ungrouped ('') last."""
        names = sorted(grouped_sampler_names, key=natural_keys)
        if "" in names:
            names.remove("")
            names.append("")
        return names

    @staticmethod
    def _guess_sampler_groups(ungrouped_sampler_names: list[str]) -> dict[str, list[str]]:
        """Heuristic grouping for shaders with no metaparam groups.

        Iterates over samplers and starts a new group whenever a repeated map type suffix is encountered.
        """
        current_group_index = 1
        current_group_names: list[str] = []
        current_suffixes: set[str] = set()
        new_groups: dict[str, list[str]] = {}

        for sampler_name in ungrouped_sampler_names:
            suffix = sampler_name.split("_")[-1]
            if suffix.isdigit():
                suffix = sampler_name.split("_")[-2]

            if suffix in current_suffixes:
                # Repeated suffix means new group.
                new_groups[f"group_{current_group_index}"] = current_group_names
                current_group_index += 1
                current_group_names = []
                current_suffixes = set()

            current_group_names.append(sampler_name)
            current_suffixes.add(suffix)

        # Finish final group.
        new_groups[f"group_{current_group_index}"] = current_group_names
        return new_groups

    # endregion

    # region UV / Sampler Queries

    def get_samplers_by_role(self, role: SamplerGroupRole) -> list[MatDefSampler]:
        """Get all samplers whose alias starts with the given role name."""
        prefix = f"{role.name} "
        return [s for s in self.samplers if s.alias.startswith(prefix)]

    def get_uv_group_sampler_paths(
        self, matbin: MATBIN = None, ignore_empty_paths=True
    ) -> dict[int, dict[str, tuple[str, UVLayer]]]:
        """Build a dictionary mapping metaparam UV group indices to dictionaries mapping sampler names to paths."""
        matbin = matbin or self.matbin
        if matbin is None:
            raise ValueError("Cannot get UV layer sampler paths without a MATBIN instance.")
        layer_sampler_paths = {}
        for sampler in self.samplers:
            path = matbin.get_sampler_path(sampler.name)
            if ignore_empty_paths and not path:
                continue
            layer_sampler_paths.setdefault(sampler.sampler_group, {})[sampler.name] = (path, sampler.uv_layer)
        return layer_sampler_paths

    # endregion

    # region Vertex Array Layout Generation

    def get_map_piece_layout(self) -> VertexArrayLayout:
        """Get a standard ER map piece layout."""
        data_types = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        ]  # type: list[VERTEX_DATA_TYPING]

        primary_samplers = self.get_samplers_by_role(SamplerGroupRole.PRIMARY)
        has_primary_normal = any("Normal" in s.alias for s in primary_samplers)
        has_detail_or_secondary_normal = any(
            "Normal" in s.alias
            for s in self.get_samplers_by_role(SamplerGroupRole.DETAIL)
            + self.get_samplers_by_role(SamplerGroupRole.SECONDARY)
        )

        if has_primary_normal:
            data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesC, 0))
            if has_detail_or_secondary_normal:
                data_types.insert(4, VertexTangent(VertexDataFormatEnum.FourBytesC, 0))

        uv_count = len(self.get_uv_slot_tuple())
        if uv_count > 4:
            raise ValueError(f"Cannot have more than 4 UV maps in a vertex array (got {uv_count}).")

        uv_member_index = 0
        while uv_count > 0:
            if uv_count % 2:
                data_types.append(VertexUV(VertexDataFormatEnum.UV, uv_member_index))
                uv_count -= 1
                uv_member_index += 1
            else:
                data_types.append(VertexUV(VertexDataFormatEnum.UVPair, uv_member_index))
                uv_count -= 2
                uv_member_index += 1

        for data_type in data_types:
            data_type.unk_x00 = self.type_unk_x00

        return VertexArrayLayout(data_types)

    def get_non_map_piece_layout(self, is_dynamic_mesh: bool = True) -> VertexArrayLayout:
        """Get a standard vertex array layout for character (and probably object) materials in ER."""
        data_types = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
            VertexTangent(VertexDataFormatEnum.FourBytesB, 0),
        ]  # type: list[VERTEX_DATA_TYPING]

        uv_slot_tuple = self.get_uv_slot_tuple()
        if not uv_slot_tuple:
            # No bone indices, weights, color, or UVs!
            # Only seen for shader "C[Fur]_cloth" so far.
            layout = VertexArrayLayout(data_types)
            layout.set_unk_x00(self.type_unk_x00)
            return layout
        elif self.UVLayer.UVFurAlpha in uv_slot_tuple:
            data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesB, instance_index=4))

        data_types += [
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneWeights(VertexDataFormatEnum.FourBytesC, 0),
        ]

        if self.shader_stem == "P[ChrCustomize][Eye]":
            data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=1))
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
            data_types.append(VertexUV(VertexDataFormatEnum.FourShortsToFloatsB, 1))
        else:
            uv_count = len(uv_slot_tuple)
            if uv_count > 4:
                raise ValueError(f"Cannot have more than 4 UV maps in a vertex array (got {uv_count}).")

            if uv_count >= 3:
                data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=0))
                data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=1))
            else:
                data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=1))

            uv_instance_index = 0
            while uv_count > 0:
                if uv_count >= 2:
                    data_types.append(VertexUV(VertexDataFormatEnum.UVPair, uv_instance_index))
                    uv_count -= 2
                    uv_instance_index += 1
                else:
                    data_types.append(VertexUV(VertexDataFormatEnum.UV, uv_instance_index))
                    uv_count -= 1
                    uv_instance_index += 1

        layout = VertexArrayLayout(data_types)
        layout.set_unk_x00(self.type_unk_x00)
        return layout

    # endregion

    def __repr__(self):
        lines = [
            "MatDef(",
            f"    shader_stem='{self.shader_stem}',",
            f"    profile={self.profile},",
            f"    samplers=[",
        ]

        for sampler in self.samplers:
            lines.append(f"        {sampler}")
        lines.append("    ],")
        uv_slots = get_shader_uv_slots(self.shader_stem)
        if uv_slots:
            lines.append(f"    uv_slots={uv_slots},")
        if self.type_unk_x00 != 0:
            lines.append(f"    type_unk_x00={self.type_unk_x00},")
        if self.alpha:
            lines.append(f"    alpha={self.alpha},")
        if self.edge:
            lines.append(f"    edge={self.edge},")
        lines.append(")")
        return "\n".join(lines)
