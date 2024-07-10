from __future__ import annotations

__all__ = [
    "MatDef",
]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path

from soulstruct.base.models.matbin import MATBIN, MATBINBND
from soulstruct.base.models.flver.vertex_array import *
from soulstruct.base.models.flver.shaders import MatDef as BaseMatDef, MatDefError
from soulstruct.containers import Binder, BinderEntry, EntryNotFoundError
from soulstruct.utilities.binary import BinaryReader
from soulstruct.utilities.files import read_json, write_json, PACKAGE_PATH
from soulstruct.utilities.future import StrEnum
from soulstruct.utilities.maths import Vector2
from soulstruct.utilities.text import natural_keys

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True, repr=False)
class MatDef(BaseMatDef):
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
        shader data are so important.
    """

    class ShaderCategory(StrEnum):
        # TODO: Pretty meaningless at the moment.
        C = "C"  # character
        M = "M"  # map

    class UVLayer(IntEnum):
        UVTexture0 = 0  # TODO: may as well be `UVMain0`
        UVBlend01 = 1
        UVTexture1 = 2  # TODO: may as well be `UVOverlay` or `UVDetail`
        UVFur = 3

    METAPARAMS: tp.ClassVar[dict[str, dict[str, list[tuple[str, str]]]]] = read_json(
        PACKAGE_PATH("eldenring/models/resources/er_shader_sampler_groups.json")
    )

    NAME_TAG_RE: tp.ClassVar[str, re.Pattern] = {
        "Albedo": re.compile(r".*\[.*A.*\].*"),
        "Specular": re.compile(r".*\[.*M.*\].*"),
        "Shininess": re.compile(r".*\[.*S.*\].*"),  # rarely used
        "Normal": re.compile(r".*\[.*N.*\].*"),
        "Vector": re.compile(r".*\[.*V.*\].*"),  # TODO: not sure what this does
        "Overlay": re.compile(r".*\[Ov_.*\].*"),  # don't mistake for a zero! e.g. '[Ov_N]'  # TODO: purpose?
        "Far": re.compile(r".*\[Far_.*\].*"),  # e.g. '[Far_AN]'
        "Multi": re.compile(r".*\[Mb(\d+).*\].*"),  # e.g. '[Mb2]', note count in capture group 1
        "Mask": re.compile(r".*\[(\d+)Mask.*\].*"),
    }

    NAME_SUFFIX_RE: tp.ClassVar[dict[str, re.Pattern]] = {
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
        "Specular": re.compile(r".*_MetallicMap(_\d+|$)", re.IGNORECASE),
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

    # Some shaders' sampler names end with some useless digit suffix after their map type above.
    SAMPLER_SUFFIX_RE: tp.ClassVar[re.Pattern] = re.compile(r".*_(\w+)(_\d+)?$")

    class SamplerGroupType(IntEnum):
        Main = 0  # has at least Albedo, Specular, Normal - may have others (Emissive, Shininess, ...)
        Detail = 1  # has Albedo and Normal only
        AlbedoOnly = 2  # duh
        NormalOnly = 3  # duh
        Other = 4  # e.g. Mask, Vector, ...

    # Metaparam dictionary, currently required to determine sampler groups for Elden Ring.
    metaparam: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    # Simiplified MATBIN params with useless parts of their prefixes removed, and natural key sorting.
    matbin_params: dict[str, tp.Any] = field(default_factory=dict)

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

        matbin_param_prefix = matbin.shader_stem.replace("[", "_").replace("]", "_") + "_snp_0_"
        matbin_params = {
            param.name.removeprefix(matbin_param_prefix): param.value
            for param in matbin.params
        }
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
            matdef.edge = True  # TODO: not yet seen in ER?
        elif blend_mode == 2:
            matdef.alpha = True

        grouped_sampler_names = {}  # type: dict[str, list[str]]
        sampler_default_texture_paths = {}  # type: dict[str, str]
        for group_name, samplers in metaparam.items():
            # NOTE: Will catch empty group name (ungrouped) as well. These will use UV layer 0 and default scale.
            grouped_sampler_names[group_name] = []
            for sampler_name, default_texture_path in samplers:
                grouped_sampler_names[group_name].append(sampler_name)
                sampler_default_texture_paths[sampler_name] = default_texture_path

        # TODO: Not using 'Multi' label, currently. Just counting main groups from sampler usage.
        #  This may indicate more UV layers, though.
        # main_group_count = 1
        # if multi_match := cls.NAME_TAG_RE["Multi"].match(matbin.shader_stem):
        #     main_group_count = int(multi_match.group(1))

        groups_found = {
            cls.SamplerGroupType.Main: 0,
            cls.SamplerGroupType.Detail: 0,
            cls.SamplerGroupType.AlbedoOnly: 0,
            cls.SamplerGroupType.NormalOnly: 0,
            cls.SamplerGroupType.Other: 0,
        }

        if len(grouped_sampler_names) == 1 and "" in grouped_sampler_names:
            # All ungrouped. We try to guess groups, by iterating over samplers and starting a new group whenever a
            # repeat of any sampler map type is found.
            grouped_sampler_names = cls.guess_sampler_groups(grouped_sampler_names[""])

        group_types = {}
        for group_name, group_sampler_names in grouped_sampler_names.items():
            # Detect group type from sampler content.
            group_type = cls.SamplerGroupType.Other
            group_size = len(group_sampler_names)
            group_suffixes = []
            for sampler_name in group_sampler_names:
                if match := cls.SAMPLER_SUFFIX_RE.match(sampler_name):
                    group_suffixes.append(match.group(1))
                else:
                    group_suffixes.append("")

            if group_size >= 3 and all(f"{s}Map" in group_suffixes for s in ("Albedo", "Metallic", "Normal")):
                group_type = cls.SamplerGroupType.Main
            elif len(group_sampler_names) == 2 and all(f"{s}Map" in group_suffixes for s in ("Albedo", "Normal")):
                group_type = cls.SamplerGroupType.Detail
            elif len(group_sampler_names) == 1:
                if "AlbedoMap" in group_suffixes:
                    group_type = cls.SamplerGroupType.AlbedoOnly
                elif "NormalMap" in group_suffixes:
                    group_type = cls.SamplerGroupType.NormalOnly

            group_types[group_name] = group_type

        for group_name in sorted(grouped_sampler_names):

            # NOTE: We don't need Meow's hack to detect fur shaders. That hack is needed because C[Fur] shaders use
            #   "group_2" as the first main texture (UV layer 0) rather than "group_1", which is instead just albedo and
            #   normal maps used for fur. My algorithm will detect that thanks to sampler groups being ordered in the
            #   metaparam.

            # Get group index (from name) and UV scale.
            # NOTE: May obviously be wrong for guessed groups with no metaparam groups at all.
            group_sampler_names = grouped_sampler_names[group_name]
            group_index = int(group_name.split("_")[1])  # e.g. 'group_3' -> 3
            group_uv_param = f"{group_name}_CommonUV-UVParam"
            uv_scale = Vector2(matbin.get_param(group_uv_param, default=(1.0, 1.0)))
            group_type = group_types[group_name]
            group_type_index = groups_found[group_type]

            if group_type == cls.SamplerGroupType.Detail and group_index == 1:
                # Fur shaders have a 'detail' (AN) group first, and use a special additional UV layer.
                group_uv_layer = cls.UVLayer.UVFur
            elif group_type == cls.SamplerGroupType.Main and group_type_index == 0:
                # TODO: Big current assumption: only Main 0 group uses `UVTexture0` layer. Maybe Main 1 also does?
                group_uv_layer = cls.UVLayer.UVTexture0
            else:
                # TODO: Also big assumption.
                group_uv_layer = cls.UVLayer.UVTexture1

            for sampler_name in group_sampler_names:

                if cls.SAMPLER_NAME_RE["Mask1"].match(sampler_name):
                    uv_layer = cls.UVLayer.UVBlend01
                    alias = "Blend 01"
                elif cls.SAMPLER_NAME_RE["Mask3"].match(sampler_name):
                    uv_layer = cls.UVLayer.UVTexture0  # explicit
                    alias = "Blend 3"
                else:
                    uv_layer = group_uv_layer

                    # Alias just comes from sampler map type, if recognized.
                    alias = f"{group_type.name} {group_type_index}"
                    for sampler_map in (
                        "Albedo", "Specular", "Shininess", "Normal", "Vector", "Reflectance", "Emissive"
                    ):
                        if cls.SAMPLER_NAME_RE[sampler_map].match(sampler_name):
                            alias += f" {sampler_map}"
                            break
                    else:
                        # Unknown sampler map type. No alias used.
                        alias = ""

                matdef.add_sampler(
                    name=sampler_name,
                    alias=alias or sampler_name,  # fallback
                    uv_layer=uv_layer,
                    sampler_group=group_index,
                    uv_scale=uv_scale,
                    default_texture_path=sampler_default_texture_paths[sampler_name],
                    matbin_texture_path=matbin.get_sampler_path(sampler_name),
                )

            groups_found[group_type] += 1

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

    @property
    def is_water(self):
        return "[Water]" in self.shader_stem

    @property
    def is_snow(self):
        return "[Snow]" in self.shader_stem

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
        ]

        sampler_names = set(sampler.name for sampler in self.samplers)

        if "Main 0 Normal" in sampler_names:
            data_types.insert(3, VertexTangent(VertexDataFormatEnum.FourBytesC, 0))
            if any(s in sampler_names for s in ("Main 1 Normal", "Detail 0 Normal", "NormalOnly 0 Normal")):
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

    def get_character_layout(self) -> VertexArrayLayout:
        """Get a standard vertex array layout for character (and probably object) materials in ER."""
        # TODO: Need to detect number of tangents (UV count? Replaces bitangent?) and vertex color count.
        data_types = [
            VertexPosition(VertexDataFormatEnum.Float3, 0),
            VertexNormal(VertexDataFormatEnum.FourBytesB, 0),
            VertexTangent(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneIndices(VertexDataFormatEnum.FourBytesB, 0),
            VertexBoneWeights(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
            VertexColor(VertexDataFormatEnum.FourBytesC, 0),
        ]
        if len(self.get_used_uv_layers()) > 1:  # has UVPair
            data_types.append(VertexUV(VertexDataFormatEnum.UVPair, 0))
        else:  # one UV
            data_types.append(VertexUV(VertexDataFormatEnum.UV, 0))

        for data_type in data_types:
            data_type.unk_x00 = self.type_unk_x00

        return VertexArrayLayout(data_types)

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


def generate_metaparam(elden_ring_path: Path):
    matbinbnd = MATBINBND.from_bundled("ELDEN_RING")
    shaderbdlebnd_path = Path(elden_ring_path, "shader/shaderbdle.shaderbdlebnd.dcx")
    shaderbdlebnd_dlc01_path = Path(elden_ring_path, "shader/shaderbdle_dlc01.shaderbdlebnd.dcx")
    shaderbdlebnd_dlc02_path = Path(elden_ring_path, "shader/shaderbdle_dlc02.shaderbdlebnd.dcx")

    shaderbdlebnd = Binder.from_path(shaderbdlebnd_path)
    shaderbdlebnd_dlc01 = Binder.from_path(shaderbdlebnd_dlc01_path)
    shaderbdlebnd_dlc02 = Binder.from_path(shaderbdlebnd_dlc02_path)

    entries_by_name = shaderbdlebnd.get_entries_by_name()
    for entry in shaderbdlebnd_dlc01.entries:
        if entry.name in entries_by_name:
            # Replace base game entry with DLC entry.
            shaderbdlebnd.remove_entry_name(entry.name)
        shaderbdlebnd.entries.append(entry)
    for entry in shaderbdlebnd_dlc02.entries:
        if entry.name in entries_by_name:
            # Replace base game entry with DLC entry.
            shaderbdlebnd.remove_entry_name(entry.name)
        shaderbdlebnd.entries.append(entry)

    all_shader_sampler_groups = {}

    for matbin_entry in matbinbnd.entries:
        matbin = MATBIN.from_binder_entry(matbin_entry)
        shader_stem = matbin.shader_name.split(".")[0]
        if shader_stem in all_shader_sampler_groups:
            continue  # done from previous MATBIN

        print(f"Finding metaparam for shader {shader_stem}...")
        try:
            shaderbdle_entry = shaderbdlebnd.find_entry_name(f"{shader_stem}.shaderbdle")
        except EntryNotFoundError:
            print(f"  No shaderbdle entry found for {shader_stem}.")
            all_shader_sampler_groups[shader_stem] = []  # don't look again
            continue

        shaderbdle = Binder.from_binder_entry(shaderbdle_entry)
        metaparam_entry = shaderbdle.find_entry_name(f"{shader_stem}.metaparam")

        shader_sampler_groups = read_metaparam(metaparam_entry)
        # Sort group keys.
        shader_sampler_groups = {
            group_name: shader_sampler_groups[group_name] for group_name in sorted(shader_sampler_groups)
        }
        all_shader_sampler_groups[shader_stem] = shader_sampler_groups

    write_json("resources/er_shader_sampler_groups.json", all_shader_sampler_groups, indent=4)


def read_metaparam(metaparam_entry: BinderEntry) -> dict[str, list[tuple[str, str]]]:
    """Read metaparam data as a dictionary mapping sampler group names to lists of sampler names with their default
    texture paths ('SYSTEX' stuff usually).

    Note that an empty group name key may exist.
    """
    metaparam = BinaryReader(metaparam_entry.get_uncompressed_data())

    shader_dict = {}
    metaparam.seek(0xC)
    sampler_count = metaparam.unpack_value("i")
    for i in range(sampler_count):
        metaparam.seek(0x98 + (0x30 * i))
        sampler_name_offset = metaparam.unpack_value("q")
        metaparam.seek(8, 1)
        default_texture_path_offset = metaparam.unpack_value("q")
        sampler_group_name_offset = metaparam.unpack_value("q")

        sampler_name = metaparam.unpack_string(sampler_name_offset, encoding="utf-16-le")
        default_texture_path = metaparam.unpack_string(default_texture_path_offset, encoding="utf-16-le")
        group_name = metaparam.unpack_string(sampler_group_name_offset, encoding="utf-16-le")  # could be empty

        shader_dict.setdefault(group_name, []).append((sampler_name, default_texture_path))

    return shader_dict


if __name__ == '__main__':
    generate_metaparam(Path(r"C:\Steam\steamapps\common\ELDEN RING (Modding 1.12)\Game"))
