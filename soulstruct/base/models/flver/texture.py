from __future__ import annotations

__all__ = ["Texture"]

import logging
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector2
from soulstruct.base.models.base.texture import BaseTexture


_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class Texture(BaseTexture):

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):

        _path_offset: int
        _texture_type_offset: int
        scale: Vector2
        unk_x10: byte = field(**Binary(asserted=[0, 1, 2]))
        unk_x11: bool
        _pad1: bytes = field(init=False, **BinaryPad(2))
        unk_x14: float
        unk_x18: float
        unk_x1C: float

    scale: Vector2 = field(default_factory=Vector2.one)
    unk_x10: int = 1  # always 0 when `path` is empty, and *very rarely* 2 (for three total materials in DS1)
    unk_x11: bool = True  # seems exactly `bool(path)` in DS1
    unk_x14: float = 0.0
    unk_x18: float = 0.0
    unk_x1C: float = 0.0

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str):
        texture_struct = cls.STRUCT.from_bytes(reader)
        path = reader.unpack_string(offset=texture_struct.pop("_path_offset"), encoding=encoding)
        texture_type = reader.unpack_string(offset=texture_struct.pop("_texture_type_offset"), encoding=encoding)
        texture = texture_struct.to_object(cls, path=path, texture_type=texture_type)
        return texture

    def to_flver_writer(self, writer: BinaryWriter):
        self.STRUCT.object_to_writer(self, writer, _path_offset=None, _texture_type_offset=None)

    def pack_strings(self, writer: BinaryWriter, encoding: str):
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

    def __hash__(self) -> int:
        """Used mostly by `Material` hash."""
        return hash((
            self.path, self.texture_type, self.scale.x, self.scale.y, self.unk_x10, self.unk_x11, self.unk_x14,
            self.unk_x18, self.unk_x1C
        ))

    def __repr__(self):
        s = f"Texture(\"{self.path}\", \"{self.texture_type}\""
        if self.scale[0] != 1.0 or self.scale[1] != 1.0:
            s += f", scale={self.scale}"
        if self.unk_x10 != 1:
            s += f", unk_x10={self.unk_x10}"
        if not self.unk_x11:
            s += f", unk_x11={self.unk_x11}"
        if self.unk_x14 != 0.0:
            s += f", unk_x14={self.unk_x14}"
        if self.unk_x18 != 0.0:
            s += f", unk_x18={self.unk_x18}"
        if self.unk_x1C != 0.0:
            s += f", unk_x1C={self.unk_x1C}"
        s += ")"
        return s
