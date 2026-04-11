from __future__ import annotations

__all__ = [
    "SamplerGroupType",
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


class SamplerGroupType(IntEnum):
    """Categories of sampler groups (which share a UV layer/scaling), based on present sampler types."""

    AMN = auto()  # Albedo/Metallic/Normal; may also have other samplers (Emissive, Shininess, ...)
    AlbedoNormal = auto()  # usually Detail, sometimes Fur/Cloth
    AlbedoNormalMask3 = auto()  # first group in SSS shaders?
    ThreeNormals = auto()  # appears in SSS shaders

    DistortionAlbedo = auto()

    # Single-map sampler groups:
    AlbedoOnly = auto()
    NormalOnly = auto()
    Mask1Only = auto()
    Mask3Only = auto()

    Unknown = auto()  # e.g. Mask, Vector, ...

    @classmethod
    def from_sampler_suffixes(cls, suffixes: tp.Sequence[str]):
        size = len(suffixes)
        if size == 1:
            if "AlbedoMap" in suffixes:
                return cls.AlbedoOnly
            if "NormalMap" in suffixes:
                return cls.NormalOnly
        elif size == 2:
            if "AlbedoMap" in suffixes and "NormalMap" in suffixes:
                return cls.AlbedoNormal  # could also be Fur
            if "AlbedoMap" in suffixes and "DistortionDepth" in suffixes:
                return cls.DistortionAlbedo
        elif size >= 3:
            if all(f"{s}Map" in suffixes for s in ("Albedo", "Metallic", "Normal")):
                return cls.AMN
            if all(f"{s}Map" in suffixes for s in ("Albedo", "Normal", "Mask3")):
                return cls.AlbedoNormalMask3
            if size == 3 and set(suffixes) == {"NormalMap"}:
                return cls.ThreeNormals

        return cls.Unknown


@dataclass(slots=True, repr=False)
class MatDef(_BaseMatDef):
    """Elden Ring materials/shaders are a lot more complicated to parse, for the following reasons:

    - FLVERs almost never specify texture names. Instead, their materials are fully deferred to a `MATBIN` file, which
    contains the texture names and are basically 1:1 with specific character materials (as evident from the character
    model IDs baked into their names).
    - Sampler UVs are sorted into groups, but these groups are only available in shader metadata files (dumped to JSON
    here). These groups are required because each can be scaled (and frequently is) in MATBIN params.
    - Sampler names use this template:
        f"{shader_stem.replace('[', '_').replace(']', '_')}_snp_Texture2D_{sampler_index}_{map_type}(_{slot_index})"
        - `slot_index` (presumably) only appears for a few shaders.
        - `sampler_index` may as well be randomly ordered, unfortunately, which is why metaparam sampler groups from the
        shader data are so important to identify UV layers and UV scaling.
    """

    class UVLayer(IntEnum):
        UVTexture0 = auto()
        UVTexture1 = auto()
        UVDetail = auto()
        UVFurCloth = auto()
        UVSubNormals = auto()  # e.g. skin normals
        UVEye2D = auto()  # 2D second UV layer found only on 'P[ChrCustomize][Eye]' so far
        UVEye4D = auto()  # 4D third UV layer found only on 'P[ChrCustomize][Eye]' so far

        @classmethod
        def guess(cls, group_index: int, group_type: SamplerGroupType, type_index: int):
            """Guess `UVLayer` from UV group context and sampler type index."""

            # Albedo/Normal groups are either Detail or the primary Fur/Cloth texture.
            if group_type == SamplerGroupType.AlbedoNormal:
                if group_index == 1:
                    # Fur/Cloth shaders have a detail-like (AN) group first, which uses a special additional UV layer.
                    # Fortunately, we can detect it since it's always sampler "group_1". (So far...)
                    return cls.UVFurCloth

                # All other observed AlbedoNormal sampler groups are detail.
                return cls.UVDetail

            if group_type in {SamplerGroupType.AMN, SamplerGroupType.AlbedoNormalMask3}:
                if type_index == 0:
                    return cls.UVTexture0
                # TODO: Carefully ignoring group 8 in 'C[DetailBlend], an AMN group that I've NEVER seen used and does
                #  NOT bring an extra UVTexture layer to the table.
                if group_index in {1, 5}:
                    return cls.UVTexture1

            if group_type == SamplerGroupType.ThreeNormals:
                # TODO: Testing.
                return cls.UVSubNormals

            if group_type in {
                SamplerGroupType.AlbedoOnly, SamplerGroupType.NormalOnly, SamplerGroupType.DistortionAlbedo
            }:
                # Only observed with detail UV.
                return cls.UVDetail

            # TODO: Also big assumption.
            return cls.UVTexture0

    METAPARAMS: tp.ClassVar[dict[str, dict[str, list[tuple[str, str]]]]] = read_json(
        SOULSTRUCT_PATH("eldenring/models/resources/er_shader_sampler_groups.json")
    )

    NAME_TAG_RE: tp.ClassVar[dict[str, re.Pattern]] = {
        "Albedo": re.compile(r".*\[.*A.*\].*"),
        "Metallic": re.compile(r".*\[.*M.*\].*"),
        "Shininess": re.compile(r".*\[.*S.*\].*"),  # rarely used
        "Normal": re.compile(r".*\[.*N.*\].*"),
        "Vector": re.compile(r".*\[.*V.*\].*"),  # TODO: not sure what this does
        "Overlay": re.compile(r".*\[Ov_.*\].*"),  # don't mistake 'O' for '0'! e.g. '[Ov_N]'  # TODO: purpose?
        "Far": re.compile(r".*\[Far_.*\].*"),  # e.g. '[Far_AN]'
        "Multi": re.compile(r".*\[Mb(\d+).*\].*"),  # e.g. '[Mb2]', note count in capture group 1
        "Mask": re.compile(r".*\[(\d+)Mask.*\].*"),

        "Alpha": re.compile(r".*_Alpha(_.*|$)", re.IGNORECASE),
        "Edge": re.compile(r".*_Edge(_.*|$)", re.IGNORECASE),
        "Emissive_Glow": re.compile(r".*_Emissive_Glow(_.*|$)", re.IGNORECASE),
        "Grass": re.compile(r".*_Grass(_.*|$)", re.IGNORECASE),
        "Grass2": re.compile(r".*_Grass2(_.*|$)", re.IGNORECASE),
        "Grass2_LOD1": re.compile(r".*_Grass2_LOD1(_.*|$)", re.IGNORECASE),
        "MeshDecalBlend": re.compile(r".*_MeshDecalBlend(_.*|$)", re.IGNORECASE),
        "Skin_PaintDecal": re.compile(r".*_Skin_PaintDecal(_.*|$)", re.IGNORECASE),
        "Vesitation": re.compile(r".*_Vesitation(_.*|$)", re.IGNORECASE),
        "NoLight": re.compile(r".*_NoLight.*", re.IGNORECASE),  # note: can be followed by non-underscore
        # TODO: More, I think. But no Blender usage yet.
    }

    SAMPLER_NAME_RE: tp.ClassVar[dict[str, re.Pattern]] = {
        "Albedo": re.compile(r".*_AlbedoMap(_\d+|$)", re.IGNORECASE),
        "Metallic": re.compile(r".*_MetallicMap(_\d+|$)", re.IGNORECASE),
        "Shininess": re.compile(r".*_ShininessMap(_\d+|$)", re.IGNORECASE),  # rarely used
        "Normal": re.compile(r".*_NormalMap(_\d+|$)", re.IGNORECASE),
        "Vector": re.compile(r".*_VectorMap(_\d+|$)", re.IGNORECASE),
        "Reflectance": re.compile(r".*_ReflectanceMap(_\d+|$)", re.IGNORECASE),
        "Emissive": re.compile(r".*_EmissiveMap(_\d+|$)", re.IGNORECASE),

        "DistortionDepth": re.compile(r".*_DistortionDepth(_\d+|$)", re.IGNORECASE),

        "Mask1": re.compile(r".*_Mask1Map(_\d+|$)", re.IGNORECASE),
        "Mask3": re.compile(r".*_Mask3Map(_\d+|$)", re.IGNORECASE),

        "3Mask": re.compile(r".*_3Mask(_\d+|$)", re.IGNORECASE),
        "UniqueOpacityMask": re.compile(r".*_UniqueOpacityMask(_\d+|$)", re.IGNORECASE),

        "BlendMaskTexture": re.compile(r".*_BlendMaskTexture(_\d+|$)", re.IGNORECASE),
        "BlendEdgeTexture": re.compile(r".*_BlendEdgeTexture(_\d+|$)", re.IGNORECASE),
        # Not ending:
        "GSBlendMap": re.compile(r".*_GSBlendMap_.*", re.IGNORECASE),  # TODO: just implied by [Mn#] tag?

        # IGNORING: 'Shadowmap' (test only?), 'Extra__Base'
    }

    EXTRA_SHADER_UV_LAYERS: tp.ClassVar[dict[str, list[UVLayer]]] = {
        "P[ChrCustomize][Eye]": [UVLayer.UVEye2D, UVLayer.UVEye4D],
    }

    # Some shaders' sampler names end with some useless digit suffix after their map type above.
    SAMPLER_SUFFIX_RE: tp.ClassVar[re.Pattern] = re.compile(r".*_(\w+)(_\d+)?$")

    USES_MATBIN: tp.ClassVar[bool] = True

    # Metaparam dictionary, currently required to determine sampler groups for Elden Ring.
    metaparam: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    # Simplified MATBIN params with useless parts of their prefixes removed, and natural key sorting.
    matbin_params: dict[str, tp.Any] = field(default_factory=dict)

    # Is this a cloth shader?
    cloth: bool = False
    # Is this a fur shader?
    fur: bool = False

    # TODO: Noting down my suspicions about MATBIN param usage (float, color) for 'C[DetailBlend]'.
    """
    - 'color' arrays have five floats. I suspect these are RGBA 'tints' for each Albedo map, and I suspect the fifth
      float is SPECULAR ROUGHNESS MULTIPLIER, since it seems low for metal textures (e.g. 0.6) and high for leather 
      (e.g. 10)... sometimes.
    """

    @classmethod
    def from_matbin(cls, matbin: MATBIN):
        """Extract critical material information directly from MATBIN.

        TODO: Focusing on characters first, as they use relatively few shaders ('C[DetailBlend]', 'C[Fur]', etc.).
        """
        metaparam = cls.METAPARAMS.get(matbin.shader_stem, None)
        if not metaparam:
            raise MatDefError(
                f"No shader metaparam information known to Soulstruct for Elden Ring shader '{matbin.shader_name}'. "
                f"Cannot parse material definition, as sampler groups cannot be determined from their names alone."
            )

        matbin_name = matbin.path.name if matbin.path is not None else ""

        matbin_params = {param.name: param.value for param in matbin.params}
        matbin_params = {k: matbin_params[k] for k in sorted(matbin_params, key=natural_keys)}

        matdef = cls(
            name=matbin_name,
            shader_stem=matbin.shader_stem,
            metaparam=metaparam,
            matbin=matbin,
            matbin_params=matbin_params,
        )

        # Still here in MATBIN, like in MTD.
        blend_mode = matbin.get_param("g_BlendMode", default=0)
        if blend_mode == 1:
            matdef.edge = True  # TODO: not yet seen in ER? Need to check MPs.
        elif blend_mode == 2:
            matdef.alpha = True

        # Very important Elden Ring material class. This is more reliable than checking if '_cloth' is in shader stem.
        matdef.cloth = matbin.get_param("GXFT_Cloth", False)
        matdef.fur = "[Fur]" in matbin.shader_stem

        grouped_sampler_names = {}  # type: dict[str, list[str]]
        sampler_default_texture_paths = {}  # type: dict[str, str]
        found_metaparam_samplers = set()
        for group_name, samplers in metaparam.items():
            # NOTE: Will catch empty group name (ungrouped) as well. These will use UV layer 0 and default scale.
            grouped_sampler_names[group_name] = []
            for sampler_name, default_texture_path in samplers:
                grouped_sampler_names[group_name].append(sampler_name)
                sampler_default_texture_paths[sampler_name] = default_texture_path
                found_metaparam_samplers.add(sampler_name)

        # Some samplers, such as '5_DisplacementMap', do not appear at all in shader metaparam. We leave them ungrouped.
        for sampler in matbin.samplers:
            if sampler.sampler_type not in found_metaparam_samplers:
                grouped_sampler_names.setdefault("", []).append(sampler.sampler_type)
                sampler_default_texture_paths[sampler.sampler_type] = sampler.path

        # TODO: Not using 'Multi' label, currently. Just counting main groups from sampler usage.
        #  This may indicate more UV layers, though.
        # main_group_count = 1
        # if multi_match := cls.NAME_TAG_RE["Multi"].match(matbin.shader_stem):
        #     main_group_count = int(multi_match.group(1))

        group_type_indices = {group_enum: 0 for group_enum in SamplerGroupType}

        if len(grouped_sampler_names) == 1 and "" in grouped_sampler_names:
            # All ungrouped. We try to guess groups, by iterating over samplers and starting a new group whenever a
            # repeat of any sampler map type is found.
            grouped_sampler_names = cls.guess_sampler_groups(grouped_sampler_names[""])

        group_types = {}
        for group_name, group_sampler_names in grouped_sampler_names.items():
            # Detect group type from sampler content.
            suffixes = []
            for sampler_name in group_sampler_names:
                if match := cls.SAMPLER_SUFFIX_RE.match(sampler_name):
                    suffixes.append(match.group(1))
                else:
                    suffixes.append("")
            group_type = SamplerGroupType.from_sampler_suffixes(suffixes)
            group_types[group_name] = group_type

        # We sort groups by name to ensure consistent order, but place ungrouped samplers LAST.
        sorted_group_names = sorted(grouped_sampler_names)
        if "" in sorted_group_names:
            sorted_group_names.remove("")
            sorted_group_names.append("")

        for group_name in sorted_group_names:

            # Get group index (from name) and UV scale.
            # NOTE: May obviously be wrong for guessed groups with no metaparam groups at all.
            group_sampler_names = grouped_sampler_names[group_name]
            if group_name:
                group_index = int(group_name.split("_")[1])  # e.g. 'group_3' -> 3
                group_uv_param = f"{group_name}_CommonUV-UVParam"
                uv_scale = Vector2(matbin.get_param(group_uv_param, default=(1.0, 1.0)))
            else:
                group_index = 0  # ungrouped (real groups are always 1+)
                uv_scale = None  # unscaled

            group_type = group_types[group_name]
            group_type_index = group_type_indices[group_type]

            group_uv_layer = cls.UVLayer.guess(group_index, group_type, group_type_index)

            sampler_counts_in_group = {}
            primed_first_sampler_types = {}  # type: dict[str, MatDefSampler]

            for i, sampler_name in enumerate(group_sampler_names):

                # TODO: 'Mask1Map' does not seem to use its own UV layer. Just goes with its group.
                if cls.SAMPLER_NAME_RE["Mask3"].match(sampler_name):
                    sampler_type = "Mask3"
                    uv_layer = cls.UVLayer.UVTexture0  # explicit
                    alias = f"{group_type.name} {group_type_index} Mask3"
                else:
                    uv_layer = group_uv_layer

                    # Alias just comes from sampler map type, if recognized.
                    alias = f"{group_type.name} {group_type_index}"
                    for sampler_type in (
                        "Albedo", "Metallic", "Shininess", "Normal",
                        "Vector", "Reflectance", "Emissive", "Mask1",
                    ):
                        if cls.SAMPLER_NAME_RE[sampler_type].match(sampler_name):
                            alias += f" {sampler_type}"
                            break
                    else:
                        # Unknown sampler map type. No alias used.
                        sampler_type = ""
                        alias = ""

                prime_first = False
                if sampler_type:
                    if sampler_type not in sampler_counts_in_group:
                        prime_first = True
                        sampler_counts_in_group[sampler_type] = 1
                    else:
                        count = sampler_counts_in_group[sampler_type]
                        alias += f"_{count}"
                        if sampler_type in primed_first_sampler_types:
                            # Retroactively add '_0' suffix to first sampler.
                            primed_first_sampler_types[sampler_type].alias += "_0"
                            primed_first_sampler_types.pop(sampler_type)
                        sampler_counts_in_group[sampler_type] += 1

                sampler = matdef.add_sampler(
                    name=sampler_name,
                    alias=alias or sampler_name,  # fallback
                    uv_layer=uv_layer,
                    sampler_group=group_index,
                    uv_scale=uv_scale,
                    default_texture_path=sampler_default_texture_paths[sampler_name],
                    matbin_texture_path=matbin.get_sampler_path(sampler_name),
                )

                if prime_first:
                    primed_first_sampler_types[sampler_type] = sampler

            group_type_indices[group_type] += 1

        return matdef

    @staticmethod
    def guess_sampler_groups(ungrouped_sampler_names: list[str]):
        """Parse ordered samplers in `ungrouped_sampler_names` and try to assign them to groups based on repeated map
        types encountered.
        """
        current_group_index = 1
        current_group_sampler_names = []
        current_group_sampler_suffixes = set()
        new_grouped_sampler_names = {}
        for sampler_name in ungrouped_sampler_names:
            suffix = sampler_name.split("_")[-1]
            if suffix.isdigit():
                # Get NEXT suffix back.
                suffix = sampler_name.split("_")[-2]

            if suffix in current_group_sampler_suffixes:
                # New group found!
                new_grouped_sampler_names[f"group_{current_group_index}"] = current_group_sampler_names
                current_group_index += 1
                current_group_sampler_names.clear()
                current_group_sampler_suffixes.clear()
            #  TODO: This is where false negatives for new groups may easily occur.

            current_group_sampler_names.append(sampler_name)
            current_group_sampler_suffixes.add(suffix)

        # Finish final current group.
        new_grouped_sampler_names[f"group_{current_group_index}"] = current_group_sampler_names
        return new_grouped_sampler_names

    @classmethod
    def from_matbin_name(cls, matbin_name: str):
        """Too much required metadata for this, currently."""
        raise MatDefError("Cannot yet parse Elden Ring material from MATBIN name. `MATBIN` instance must be given.")

    def get_uv_group_sampler_paths(
        self, matbin: MATBIN = None, ignore_empty_paths=True
    ) -> dict[int, dict[str, tuple[str, UVLayer]]]:
        """Build a dictionary mapping metaparam UV group indices to dictionaries mapping sampler names to paths.

        By default, ignores sampler names with no paths.
        """
        matbin = matbin or self.matbin
        if matbin is None:
            raise ValueError("Cannot get UV layer sampler paths without a MATBIN instance.")
        layer_sampler_paths = {}
        for sampler in self.samplers:
            path = matbin.get_sampler_path(sampler.name)  # will raise `KeyError` if missing
            if ignore_empty_paths and not path:
                continue
            layer_sampler_paths.setdefault(sampler.sampler_group, {})[sampler.name] = (path, sampler.uv_layer)
        return layer_sampler_paths

    def get_map_piece_layout(self) -> VertexArrayLayout:
        """Get a standard ER map piece layout.

        TODO: Not finished yet.
        """

        data_types = [  # always present
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesC, 0),
            # Tangent/Bitangent will be inserted here if needed.
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
            # UV/UVPair will be inserted here if needed.
        ]  # type: list[VERTEX_DATA_TYPING]

        sampler_names = set(sampler.name for sampler in self.samplers)

        if "AMN 0 Normal" in sampler_names:
            # Tangent array required.
            data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesC, 0))
            if any(s in sampler_names for s in (
                    "AMN 1 Normal", "Detail 0 Normal", "NormalOnly 0 Normal"
            )):
                # Additional tangent array required.
                data_types.insert(4, VertexTangent(VertexDataFormatEnum.FourBytesC, 0))

        # Calculate total UV map count and use a combination of UVPair and UV format members below.
        uv_count = len(self.get_used_uv_layers())

        if uv_count > 4:
            # TODO: Might be an unnecessary assertion. True for DS1, for sure.
            raise ValueError(f"Cannot have more than 4 UV maps in a vertex array (got {uv_count}).")

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

        return VertexArrayLayout(data_types)

    def get_non_map_piece_layout(self, is_dynamic_mesh: bool = True) -> VertexArrayLayout:
        """Get a standard vertex array layout for character (and probably object) materials in ER."""

        data_types = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
            VertexTangent(VertexDataFormatEnum.FourBytesB, 0),  # calculated from `UVTexture0` (or empty)
        ]  # type: list[VERTEX_DATA_TYPING]

        uv_layers = self.get_used_uv_layers()
        if not uv_layers:
            # No bone indices, weights, color, or UVs!
            # TODO: Only seen for shader "C[Fur]_cloth" so far.
            layout = VertexArrayLayout(data_types)
            layout.set_unk_x00(self.type_unk_x00)
            return layout
        elif self.UVLayer.UVFurCloth in uv_layers:
            # TODO: This goes in vertex array 1.
            # Extra Tangent array calculated from `UVFurCloth`, with index 4, and continue with other data below.
            data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesB, instance_index=4))
        # TODO: Need to look at other materials.

        data_types += [
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneWeights(VertexDataFormatEnum.FourBytesC, 0),
            # One or two Color arrays added below.
        ]

        if self.shader_stem == "P[ChrCustomize][Eye]":
            # Standard 1-indexed color:
            data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=1))
            # TODO: Three UVs, and the third is 4D (FourShortsToFloatsB). Any other shaders do this?
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
            data_types.append(VertexUV(VertexDataFormatEnum.FourShortsToFloatsB, 1))
        else:
            # Generic UV detection.
            uv_count = len(uv_layers)

            if uv_count > 4:
                # TODO: Might be an unnecessary assertion. True for DS1, for sure.
                raise ValueError(f"Cannot have more than 4 UV maps in a vertex array (got {uv_count}).")

            if uv_count >= 3:
                # TODO: Best detection so far for extra color...
                data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=0))
                data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=1))
            else:
                # Single color only, but weirdly has instance index 1.
                data_types.append(VertexColor(VertexDataFormatEnum.FourBytesC, instance_index=1))

            uv_instance_index = 0
            while uv_count > 0:  # extra UVs
                # `UVPair` is added first.
                if uv_count >= 2:
                    data_types.append(VertexUV(VertexDataFormatEnum.UVPair, uv_instance_index))
                    uv_count -= 2
                    uv_instance_index += 1
                else:
                    # Last UV.
                    data_types.append(VertexUV(VertexDataFormatEnum.UV, uv_instance_index))
                    uv_count -= 1
                    uv_instance_index += 1

        layout = VertexArrayLayout(data_types)
        layout.set_unk_x00(self.type_unk_x00)
        return layout

    def __repr__(self):
        lines = [
            "MatDef(",
            f"    shader_stem='{self.shader_stem}',",
            f"    samplers=[",
        ]

        for sampler in self.samplers:
            lines.append(f"        {sampler}")
        lines.append("    ],")

        if self.type_unk_x00 != 0:
            lines.append(f"    type_unk_x00={self.type_unk_x00},")
        if self.alpha:
            lines.append(f"    alpha={self.alpha},")
        if self.edge:
            lines.append(f"    edge={self.edge},")
        # if self.metaparam:
        #     lines.append(f"    metaparam={self.metaparam},")
        lines.append(")")
        return "\n".join(lines)
