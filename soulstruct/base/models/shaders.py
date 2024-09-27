from __future__ import annotations

__all__ = [
    "MatDefError",
    "MatDef",
]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path

from soulstruct.exceptions import SoulstructError
from .base.vertex_array_layout import BaseVertexArrayLayout
from .matbin import MATBIN, MATBINBND
from .mtd import MTD, MTDBND
from soulstruct.utilities.maths import Vector2

_LOGGER = logging.getLogger("soulstruct")


class MatDefError(SoulstructError):
    """Raised when there is a fatal issue with parsing information from a material definition/shader."""
    pass


@dataclass(slots=True)
class MatDefSampler:

    name: str  # e.g. 'g_Diffuse'; real, game-specific name of sampler
    alias: str  # e.g. 'ALBEDO_0'; used for Blender node names, etc., to improve porting
    uv_layer: IntEnum | None  # game-specific UV layer enum (could be `None` for non-textured samplers)
    sampler_group: int = 0  # given explicitly in Elden Ring; inferred in earlier games
    uv_scale: Vector2 | None = None  # added from sampler group in later games
    default_texture_path: str = ""
    matbin_texture_path: str = ""  # only used in Elden Ring, where FLVERs only rarely override texture paths

    @property
    def uv_layer_name(self) -> str:
        return self.uv_layer.name if self.uv_layer is not None else ""

    @property
    def matbin_texture_stem(self) -> str:
        if self.matbin_texture_path:
            return Path(self.matbin_texture_path).stem  # remove last suffix only
        return ""  # no path

    def __repr__(self):
        s = f"Sampler({self.name} -> {self.alias}, UV '{self.uv_layer_name}'"
        if self.sampler_group > 0:
            s += f", Group {self.sampler_group}"
        if self.uv_scale is not None:
            s += f", Scale {self.uv_scale}"
        if self.default_texture_path:
            s += f", Default \"{self.default_texture_path}\""
        return s + ")"


@dataclass(slots=True)
class MatDef(abc.ABC):
    """Various summarized properties that tell Soulstruct how to generate FLVER vertex array layouts and Blender
    shader node trees for optimal FLVER visualization.

    Probably its most important function is parsing the tightly-packed FLVER vertex UV arrays and properly matching them
    up across all the materials in the FLVER, using the `UVLayer` class enum below (overridden by subclasses). The
    integer values of this enum correspond to the `uv_index` property of samplers in the MTD files (except they are
    zero-indexed here).

    In Elden Ring, these UV indices are MUCH harder to find; they exist in the 'metadata' of 'sampler groups', which I
    have pre-loaded for all known MATBINs into a bundled JSON with Meow's help.

    The other function of this class is to map each known sampler name in each game to a game-agnostic 'alias' like
    `ALBEDO_0` (which appears as 'g_Diffuse' in DS1, 'g_DiffuseTexture' in BB, etc.). This makes it easier to port
    FLVER materials across games and determines how they are held in my Blender add-on.
    """

    class UVLayer(IntEnum):
        """Most basic version of UV layers; overridden in most subclasses.

        Note that different FLVER types (Characters, Map Pieces, etc.) may conflict in their usage of these, and the
        names of the re-used values may be a bit verbose like 'UVBloodOrLightmap' to indicate that.
        """
        UVTexture0 = 0
        UVTexture1 = 1
        UVLightmap = 2

    # Game-specific subclasses can define their UV layer labels.
    UVLayer: tp.ClassVar[type[IntEnum]]

    # Game-specific mapping of shader categories to `MatDef` names known to use that category, which aids in creating
    # `MatDef`s from material definition names alone when files are unavailable.
    KNOWN_SHADER_MTD_STEMS: tp.ClassVar[dict[str, list[str | re.Pattern]]] = {}
    # Game-specific mapping of game-specific `shader_category` values to lists of extra `UVLayer` members.
    EXTRA_SHADER_UV_LAYERS: tp.ClassVar[dict[str, list[UVLayer]]] = {}
    # Earlier games can easily have their sampler names mapped to global aliases.
    # Later games may not use this, as they have more complex sampler groups that need shaders to determine function.
    SAMPLER_ALIASES: tp.ClassVar[dict[str, str]]
    # Maps aliases back to game-specific sampler names.
    SAMPLER_GAME_NAMES: tp.ClassVar[dict[str, str]]
    # Detects [T] style tags in MTD names.
    NAME_TAG_RE: tp.ClassVar[dict[str, re.Pattern]]
    # Detects '_Label' style suffixes in MTD names.
    NAME_SUFFIX_RE: tp.ClassVar[dict[str, re.Pattern]]
    # True if this game uses `MATBIN` material definition files rather than old `MTD`.
    USES_MATBIN: tp.ClassVar[bool] = False

    # Stem of shader name, if available.
    shader_stem: str = ""
    # Category of shader, if detectable.
    shader_category: str | None = None
    # List of samplers used by this material, and their information.
    samplers: list[MatDefSampler] = field(default_factory=list)

    # MTD used to generate this `MatDef`, if available (older games).
    mtd: MTD | None = None
    # MATBIN used to generate this `MatDef`, if available (newer games).
    matbin: MATBIN | None = None
    # Name of MTD or MATBIN file used to generate this `MatDef`, if available.
    name: str = ""

    # NOTE: `matbin` field only defined by Elden Ring subclass, which does not use `MTD` at all.

    # Unknown value to write to generated `VertexArrayLayout` elements.
    type_unk_x00: int = 0

    # If true, this material should use alpha blending (true material transparency).
    alpha: bool = False
    # If true, this material should use thresholded alpha clipping (e.g. plant textures).
    edge: bool = False

    def __post_init__(self):
        if self.shader_stem and not self.shader_category:
            self.shader_category = self.get_shader_category(self.shader_stem)

    @classmethod
    def get_shader_category(cls, shader_stem: str) -> str:
        """Subclasses can specify how they determine categories from full stems. Default is equal, so every unique
        stem is a category."""
        return shader_stem

    @classmethod
    def from_mtd(cls, mtd: MTD):
        """Extract critical MTD information (mainly for generating FLVER vertex array layouts) directly from MTD."""
        matdef = cls(
            shader_stem=mtd.shader_name.split(".")[0],
            mtd=mtd,
            name=mtd.path.name if mtd.path else "",
        )

        for sampler in mtd.samplers:
            uv_index = sampler.uv_index - 1  # 1-indexed -> 0-indexed
            matdef.samplers.append(
                MatDefSampler(
                    name=sampler.sampler_type,
                    alias=cls.SAMPLER_ALIASES.get(sampler.sampler_type, ""),
                    uv_layer=cls.UVLayer(uv_index),
                )
            )

        blend_mode = mtd.get_param("g_BlendMode", default=0)
        if blend_mode == 1:
            matdef.edge = True
        elif blend_mode == 2:
            matdef.alpha = True

        return matdef

    @classmethod
    def from_mtd_name(cls, mtd_name: str):
        """Guess as much information about the shader as possible purely from its name.

        Obviously, getting the texture names right is the most important part, but we can also guess whether the shader
        uses a lightmap (L), two texture slots (M), or has extra features like alpha (Alp/Edge).
        """
        mtd_stem = Path(mtd_name).stem
        matdef = cls(shader_stem=mtd_stem, name=mtd_name)

        # Find category.
        for category, patterns in cls.KNOWN_SHADER_MTD_STEMS.items():
            for pattern in patterns:
                if isinstance(pattern, re.Pattern) and pattern.match(mtd_stem):
                    matdef.shader_category = category
                    break
                elif isinstance(pattern, str) and pattern == mtd_stem:
                    matdef.shader_category = category
                    break
            else:
                continue
            break
        else:
            # Failed to find category.
            matdef.shader_category = ""

        # Detect used sampler names.
        if (
            matdef.has_name_tag("NormalToAlpha")
            or mtd_stem in cls.KNOWN_SHADER_MTD_STEMS.get("NormalToAlpha", {})
        ):
            # Unshaded skyboxes, mist, some trees, etc.
            matdef.shader_category = "NormalToAlpha"
            matdef.add_sampler(alias="Main 0 Albedo", uv_layer=cls.UVLayer.UVTexture0)
        elif (
            matdef.has_name_tag("wet")
            or mtd_stem in cls.KNOWN_SHADER_MTD_STEMS.get("Water", {})
        ):
            # Water shaders with normals only.
            matdef.shader_category = "Water"
            matdef.add_sampler(alias="Main 0 Normal", uv_layer=cls.UVLayer.UVTexture0)
        else:
            # Check for all other standard sampler types.
            for texture_tag, alias in (
                ("Albedo", "Main 0 Albedo"),
                ("Specular", "Main 0 Specular"),
                ("Shininess", "Main 0 Shininess"),
                ("Normal", "Main 0 Normal"),
                ("Displacement", "Displacement"),
            ):
                if texture_tag in cls.NAME_TAG_RE and matdef.has_name_tag(texture_tag):
                    matdef.add_sampler(alias=alias, uv_layer=cls.UVLayer.UVTexture0)

        if not matdef.samplers:
            _LOGGER.warning(
                f"Unusual MTD name '{mtd_name}' could not be parsed for any samplers. You may need to define it in "
                f"your own custom MTD/MTDBND."
            )

        if matdef.has_name_tag("Multi"):
            # For each 'Main 0' alias sampler, create 'Main 1' alias sampler.
            for sampler in matdef.samplers:
                if sampler.alias.startswith("Main 0"):
                    secondary_alias = sampler.alias.replace("Main 0", "Main 1")
                    matdef.add_sampler(alias=secondary_alias, uv_layer=cls.UVLayer.UVTexture1)

        if matdef.has_name_tag("Lightmap"):
            matdef.add_sampler(alias="Lightmap", uv_layer=cls.UVLayer.UVLightmap)

        matdef.alpha = matdef.has_name_suffix("Alpha")
        matdef.edge = matdef.has_name_suffix("Edge")

        return matdef

    @classmethod
    def from_mtdbnd_or_name(cls, mtd_name: str, mtdbnd: MTDBND = None):
        """Get DS1 material info for a FLVER material, which is needed to determine which material uses which UV
        layers from Blender, and for layout generation.
        """
        if not mtdbnd:
            return cls.from_mtd_name(mtd_name)

        # Use real MTD file if available (much less guesswork).
        try:
            mtd = mtdbnd.get_mtd(mtd_name)
        except KeyError:
            _LOGGER.warning(f"Could not find MTD '{mtd_name}' in MTDBND. Guessing info from name...")
            return cls.from_mtd_name(mtd_name)
        return cls.from_mtd(mtd)

    @classmethod
    def from_matbin(cls, matbin: MATBIN):
        raise MatDefError(f"`MatDef` subclass '{cls.__name__}' does not define `from_matbin()`.")

    @classmethod
    def from_matbin_name(cls, matbin_name: str):
        raise MatDefError(f"`MatDef` subclass '{cls.__name__}' does not define `from_matbin_name()`.")

    @classmethod
    def from_matbinbnd_or_name(cls, matbin_name: str, matbinbnd: MATBINBND = None):
        """Look up `matbin_name` in `matbinbnd` if it is given and the MATBIN exists. Otherwise, try to parse directly
        from name (which is highly difficult for MATBINs!).
        """
        if not matbinbnd:
            return cls.from_matbin_name(matbin_name)

        # Use real MATBIN file if available (much less guesswork).
        try:
            matbin = matbinbnd.get_matbin(matbin_name)
        except KeyError:
            _LOGGER.warning(f"Could not find MATBIN '{matbin_name}' in MATBINBND. Guessing info from name...")
            return cls.from_matbin_name(matbin_name)
        return cls.from_matbin(matbin)

    def get_used_uv_layers(self) -> list[IntEnum]:
        """Value-sorted list of unique UV layer enums used by all samplers and any additional, otherwise undetectable
        shader function (e.g. foliage wind animation) specified in `cls.EXTRA_SHADER_UV_LAYERS`."""
        all_uv_layers = set(sampler.uv_layer for sampler in self.samplers) - {None}
        for extra_uv_layer in self.EXTRA_SHADER_UV_LAYERS.get(self.shader_category, []):
            all_uv_layers.add(extra_uv_layer)
        return sorted(all_uv_layers, key=lambda x: x.value)

    # region Abstract Methods/Properties

    @abc.abstractmethod
    def get_map_piece_layout(self) -> BaseVertexArrayLayout:
        ...

    @abc.abstractmethod
    def get_character_layout(self) -> BaseVertexArrayLayout:
        ...

    # endregion

    def has_name_tag(self, tag: str) -> bool:
        if not self.NAME_TAG_RE:
            raise ValueError(f"Cannot check MATDEF name for tag '{tag}' without `NAME_TAG_RE` defined in subclass.")
        if tag not in self.NAME_TAG_RE:
            raise KeyError(f"Tag '{tag}' not found in `NAME_TAG_RE` for this shader subclass.")
        if not self.name:
            raise ValueError(f"Cannot check MATDEF name for tag '{tag}' without `name` assigned to `MATDEF`.")
        return self.NAME_TAG_RE[tag].match(self.name) is not None

    def has_name_suffix(self, suffix: str) -> bool:
        if not self.NAME_SUFFIX_RE:
            raise ValueError(
                f"Cannot check MATDEF name for suffix '{suffix}' without `NAME_SUFFIX_RE` defined in subclass.")
        if suffix not in self.NAME_SUFFIX_RE:
            raise KeyError(f"Tag '{suffix}' not found in `NAME_SUFFIX_RE` for this shader subclass.")
        if not self.name:
            raise ValueError(
                f"Cannot check MATDEF name for suffix '{suffix}' without MATDEF name assigned to `MATDEF`."
            )
        return self.NAME_SUFFIX_RE[suffix].match(self.name) is not None

    def add_sampler(
        self,
        name="",
        alias="",
        uv_layer: UVLayer | None = None,
        sampler_group=0,
        uv_scale: Vector2 | None = None,
        default_texture_path="",
        matbin_texture_path="",
    ):
        if not name and not alias:
            raise ValueError("Sampler must have either a game name or an alias.")
        if not name:
            try:
                name = self.SAMPLER_GAME_NAMES[alias]
            except KeyError:
                raise ValueError(f"Could not find game name for sampler alias '{alias}'.")
        if not alias:
            try:
                alias = self.SAMPLER_ALIASES[name]
            except KeyError:
                raise ValueError(f"Could not find sampler alias for game name '{name}'.")
        self.samplers.append(
            MatDefSampler(
                name=name,
                alias=alias,
                uv_layer=uv_layer,
                sampler_group=sampler_group,
                uv_scale=uv_scale,
                default_texture_path=default_texture_path,
                matbin_texture_path=matbin_texture_path,
            )
        )

    def get_sampler_with_alias(self, sampler_alias: str) -> MatDefSampler | None:
        for sampler in self.samplers:
            if sampler.alias == sampler_alias:
                return sampler
        return None

    def get_samplers_field(self, field_name: str) -> dict[str, tp.Any]:
        """Get a dictionary mapping sampler names to the value of the given field name for each sampler."""
        return {sampler.name: getattr(sampler, field_name) for sampler in self.samplers}

    def get_matching_samplers(self, pattern: re.Pattern, match_alias=False) -> list[tuple[re.Match, MatDefSampler]]:
        return [
            (match, sampler)
            for sampler in self.samplers
            if (match := pattern.match(sampler.alias if match_alias else sampler.name))
        ]
