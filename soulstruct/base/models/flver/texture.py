from __future__ import annotations

__all__ = ["Texture"]

import logging
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector2

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class Texture:

    class STRUCT0(BinaryStruct):
        _path_offset: int
        _texture_type_offset: int
        _pad0: bytes = binary_pad(8, init=False)

    class STRUCT2(BinaryStruct):
        _path_offset: int
        _texture_type_offset: int
        scale: Vector2
        f2_unk_x10: byte = binary(asserted=[0, 1, 2])
        f2_unk_x11: bool
        _pad1: bytes = binary_pad(2, init=False)
        f2_unk_x14: float
        f2_unk_x18: float
        f2_unk_x1c: float

    path: str = ""
    # MTD or MATBIN sampler name (e.g. 'g_Diffuse', 'C_DetailBlend__snp_Texture2D_7_AlbedoMap').
    # Can be `None` in old FLVER0 versions.
    texture_type: str | None = ""

    # Written to FLVER2 versions only:
    scale: Vector2 = field(default_factory=Vector2.one)
    f2_unk_x10: int = 1  # always 0 when `path` is empty, and *very rarely* 2 (for three total materials in DS1)
    f2_unk_x11: bool = True  # seems exactly `bool(path)` in DS1
    f2_unk_x14: float = 0.0
    f2_unk_x18: float = 0.0
    f2_unk_x1c: float = 0.0

    @classmethod
    def from_flver0_reader(cls, reader: BinaryReader, encoding: str):
        texture_struct = cls.STRUCT0.from_bytes(reader)
        path = reader.unpack_string(offset=texture_struct.pop("_path_offset"), encoding=encoding)
        texture_type_offset = texture_struct.pop("_texture_type_offset")
        if texture_type_offset > 0:
            texture_type = reader.unpack_string(offset=texture_type_offset, encoding=encoding)
        else:
            texture_type = None
        return cls(path=path, texture_type=texture_type)

    @classmethod
    def from_flver2_reader(cls, reader: BinaryReader, encoding: str):
        texture_struct = cls.STRUCT2.from_bytes(reader)
        path = reader.unpack_string(offset=texture_struct.pop("_path_offset"), encoding=encoding)
        texture_type = reader.unpack_string(offset=texture_struct.pop("_texture_type_offset"), encoding=encoding)
        texture = texture_struct.to_object(cls, path=path, texture_type=texture_type)
        return texture

    def to_flver0_writer(self, writer: BinaryWriter):
        """String offsets reserved."""
        self.STRUCT0.object_to_writer(self, writer, _path_offset=None, _texture_type_offset=None)

    def to_flver2_writer(self, writer: BinaryWriter):
        self.STRUCT2.object_to_writer(self, writer, _path_offset=None, _texture_type_offset=None)

    def pack_strings(self, writer: BinaryWriter, encoding: str, texture_type_optional=False):
        """Shared by FLVER versions."""
        writer.fill_with_position("_path_offset", obj=self)
        writer.pack_z_string(self.path, encoding=encoding)
        if self.texture_type is not None:
            writer.fill_with_position("_texture_type_offset", obj=self)
            writer.pack_z_string(self.texture_type, encoding=encoding)
        elif not texture_type_optional:
            raise ValueError(f"Texture {self} has `texture_type == None`, which is not invalid for this FLVER version.")
        else:
            # Only possible in FLVER0 versions.
            writer.fill("_texture_type_offset", 0, obj=self)

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
            self.path, self.texture_type, self.scale.x, self.scale.y, self.f2_unk_x10, self.f2_unk_x11,
            self.f2_unk_x14, self.f2_unk_x18, self.f2_unk_x1c
        ))

    def __repr__(self):
        s = f"Texture(\"{self.path}\", \"{self.texture_type}\""
        if self.scale[0] != 1.0 or self.scale[1] != 1.0:
            s += f", scale={self.scale}"
        if self.f2_unk_x10 != 1:
            s += f", f2_unk_x10={self.f2_unk_x10}"
        if not self.f2_unk_x11:
            s += f", f2_unk_x11={self.f2_unk_x11}"
        if self.f2_unk_x14 != 0.0:
            s += f", f2_unk_x14={self.f2_unk_x14}"
        if self.f2_unk_x18 != 0.0:
            s += f", f2_unk_x18={self.f2_unk_x18}"
        if self.f2_unk_x1c != 0.0:
            s += f", f2_unk_x1c={self.f2_unk_x1c}"
        s += ")"
        return s
