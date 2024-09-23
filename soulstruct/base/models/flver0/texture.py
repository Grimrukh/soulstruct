from __future__ import annotations

__all__ = ["Texture"]

from dataclasses import dataclass, field

from soulstruct.base.models.base.texture import BaseTexture
from soulstruct.utilities.binary import *


@dataclass(slots=True)
class Texture(BaseTexture):

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):
        _path_offset: int
        _texture_type_offset: int
        _pad0: bytes = field(init=False, **BinaryPad(8))

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str):
        texture_struct = cls.STRUCT.from_bytes(reader)
        path = reader.unpack_string(offset=texture_struct.pop("_path_offset"), encoding=encoding)
        texture_type_offset = texture_struct.pop("_texture_type_offset")
        if texture_type_offset > 0:
            texture_type = reader.unpack_string(offset=texture_type_offset, encoding=encoding)
        else:
            texture_type = None
        return cls(path=path, texture_type=texture_type)

    def to_flver_writer(self, writer: BinaryWriter):
        """String offsets reserved."""
        self.STRUCT.object_to_writer(self, writer, _path_offset=None, _texture_type_offset=None)

    def pack_strings(self, writer: BinaryWriter, encoding: str):
        writer.fill_with_position("_path_offset", obj=self)
        writer.pack_z_string(self.path, encoding=encoding)
        if self.texture_type is not None:
            writer.fill_with_position("_texture_type_offset", obj=self)
            writer.pack_z_string(self.texture_type, encoding=encoding)
        else:
            writer.fill("_texture_type_offset", 0, obj=self)

    def __hash__(self) -> int:
        """Used mostly by `Material` hash."""
        return hash((self.path, self.texture_type))
