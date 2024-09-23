from __future__ import annotations

__all__ = ["BaseTexture"]

import logging
from dataclasses import dataclass
from pathlib import Path

from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class BaseTexture:

    path: str = ""
    texture_type: str = ""  # MTD or MATBIN sampler name (e.g. 'g_Diffuse', 'C_DetailBlend__snp_Texture2D_7_AlbedoMap')

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str):
        raise NotImplementedError

    def to_flver_writer(self, writer: BinaryWriter):
        raise NotImplementedError

    def __hash__(self) -> int:
        """Used mostly by `Material` hash."""
        raise NotImplementedError

    def pack_strings(self, writer: BinaryWriter, encoding: str):
        """Shared by FLVER versions."""
        writer.fill_with_position("_path_offset", obj=self)
        writer.pack_z_string(self.path, encoding=encoding)
        writer.fill_with_position("_texture_type_offset", obj=self)
        writer.pack_z_string(self.texture_type, encoding=encoding)

    def set_name(self, name: str):
        """Set `path` to '{name}.tga'.

        Any existing '.tga' or '.tpf' extension in `name` will be removed and replaced with '.tga'.
        """
        name = name.removesuffix(".tga").removesuffix(".tpf") + ".tga"
        self.path = str(Path(self.path).with_name(name))

    @property
    def path_parent(self) -> str:
        """Directory part of FLVER texture path, as a string. Includes (exactly one) trailing backslash."""
        return str(Path(self.path).parent).rstrip("\\") + "\\"

    @property
    def name(self) -> str:
        return Path(self.path).name if self.path else ""

    @property
    def stem(self) -> str:
        """Typically just removes '.tga' extension from FLVER texture path."""
        return Path(self.path).stem if self.path else ""

    def __repr__(self):
        return f"Texture(\"{self.path}\", \"{self.texture_type}\")"
