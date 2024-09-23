from __future__ import annotations

__all__ = ["BaseMaterial"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.binary import *
from .texture import BaseTexture
from .version import FLVERVersion

_LOGGER = logging.getLogger("soulstruct")

TEXTURE_T = tp.TypeVar("TEXTURE_T", bound=BaseTexture)


@dataclass(slots=True)
class BaseMaterial(tp.Generic[TEXTURE_T]):
    """Information about a FLVER material used by any number of submeshes.

    NOTE: The `name` of the material is usually junk, but if it is formatted as a number between two hashes, e.g.
    '#01#', then any submesh using the materia will ONLY be rendered if the corresponding 'Model Display Mask' bit flag
    in `NPC_PARAM` is enabled. We carefully preserve these names and have properties that wrap name getting/setting
    based on a desired mask value. Multiple `Material` instances may use the same display mask value, but typically only
    one of them will.
    """

    # Exactly one or two digits required between hashes (two usually used), with optional trimmable spaces. Any suffix.
    DISPLAY_MASK_RE: tp.ClassVar[re.Pattern] = re.compile(r"^# *(\d|\d\d) *# *(.*)$")

    name: str = ""
    mat_def_path: str = ""  # could be a '.mtd' (MTD) file name or '.matxml' (MATBIN) file name
    textures: list[TEXTURE_T] = field(default_factory=list)

    # Held temporarily before FLVER textures are assigned.
    _texture_count: int | None = None
    _first_texture_index: int | None = None

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str, version: FLVERVersion):
        raise NotImplementedError

    def to_flver_writer(self, writer: BinaryWriter):
        raise NotImplementedError

    def pack_strings(self, flver_writer: BinaryWriter, encoding: str):
        flver_writer.fill_with_position("_name_offset", obj=self)
        flver_writer.pack_z_string(self.name, encoding=encoding)
        flver_writer.fill_with_position("_mat_def_path_offset", obj=self)
        flver_writer.pack_z_string(self.mat_def_path, encoding=encoding)

    def get_texture_dict(self) -> dict[str, TEXTURE_T]:
        """Get a dictionary mapping texture types to like 'g_Diffuse' to `Texture` instances.

        Will raise a `KeyError` if any texture type is repeated.
        """
        textures = {}
        for texture in self.textures:
            if texture.texture_type in textures:
                raise KeyError(f"Texture type {texture.texture_type} appeared more than once in Material {self.name}.")
            textures[texture.texture_type] = texture
        return textures

    def find_texture_type(self, texture_type: str) -> TEXTURE_T | None:
        for texture in self.textures:
            if texture.texture_type == texture_type:
                return texture
        return None

    def get_shared_texture_path_prefix(self, exclude_names=True, exclude_empty_paths=True) -> str:
        shared_texture_prefix = ""
        for texture in self.textures:
            if exclude_empty_paths and not texture.path:
                continue  # empty paths do not count
            path_part = texture.path_parent if exclude_names else texture.path
            if shared_texture_prefix == "":
                shared_texture_prefix = path_part
                continue
            for i, (a, b) in enumerate(zip(shared_texture_prefix, path_part)):
                if a != b:
                    shared_texture_prefix = shared_texture_prefix[:i]
                    break
        return shared_texture_prefix

    @property
    def mat_def_stem(self) -> str:
        return Path(self.mat_def_path).stem

    @property
    def mat_def_name(self) -> str:
        """Extension can vary: '.mtd' or '.matxml'."""
        return Path(self.mat_def_path).name

    @mat_def_name.setter
    def mat_def_name(self, name: str):
        """Replaces name component of current `mat_def_path`. If extension is missing, current suffix will be used."""
        if name.endswith(".mtd") or name.endswith(".matxml"):
            # Use name as-is.
            pass
        elif "." in name:
            raise ValueError(f"Material definition name {name} should have no suffix, or '.mtd' or '.matxml'.")
        else:
            # Keep current suffix.
            new_suffix = Path(self.mat_def_path).suffix
            name += new_suffix
        self.mat_def_path = str(Path(self.mat_def_path).with_name(name))

    @property
    def display_mask(self) -> int | None:
        """Parse `name` of material to check if it is a display mask material, and return the mask value if so.

        Returns `None` if the material is not a display mask material, which means it will always be rendered.
        """
        if match := self.DISPLAY_MASK_RE.match(self.name):
            return int(match.group(1))
        return None

    @display_mask.setter
    def display_mask(self, value: int):
        """Sets `name` to the appropriate formatted, hash-enclosed string: `#{value:02d}#`.

        Since suffixes in mask names are supported, any existing suffix will be copied. If the name is not currently a
        mask name, the existing name will be moved to a suffix.
        """
        if value is None:
            raise ValueError("Model display mask value cannot be `None`. Just change the name to a non-mask name.")
        if not 0 <= value < 32:
            # TODO: Earlier games only allow 16 masks, not 32.
            raise ValueError(f"Model display mask value must be between 0 and 31, not {value}.")
        if match := self.DISPLAY_MASK_RE.match(self.name):
            self.name = f"#{value:02d}# {match.group(2)}"  # keep existing mask name suffix
        else:
            self.name = f"#{value:02d}# {self.name}"  # no existing mask name suffix

    @property
    def name_without_display_mask(self) -> str:
        """Return material name after display mask prefix, if present.

        May be empty if there's nothing after the mask.
        """
        if match := self.DISPLAY_MASK_RE.match(self.name):
            return match.group(2)
        return self.name

    def replace_in_all_texture_names(self, old_string: str, new_string: str):
        """Replace all occurrences of `old_string` in all texture names (at end of paths) with `new_string`."""
        for tex in self.textures:
            if tex.path:
                tex_path = Path(tex.path)
                tex_name = tex_path.name.replace(old_string, new_string)
                tex.path = str(tex_path.with_name(tex_name))

    def __hash__(self) -> int:
        raise NotImplementedError

    def __eq__(self, other: tp.Self):
        """Check for equality by hash."""
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)
