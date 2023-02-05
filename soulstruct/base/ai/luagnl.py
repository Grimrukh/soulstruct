from __future__ import annotations

__all__ = ["LuaGNL"]

from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *


@dataclass(slots=True)
class LuaGNL(GameFile):
    """Global Name List file that lists all the functions declared in all the Lua scripts in the `LuaBND`.

    Literally just a list of offsets to null-terminated strings.

    Not actually required for AI to function (after Demon's Souls, at least).
    """

    byte_order: ByteOrder = ByteOrder.LittleEndian
    varint_size: int = 4
    names: list[str] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> LuaGNL:
        # We can only guess at byte order and varint size from the appearance of the first 1/2 string offsets.
        first_eight_bytes = reader.peek(8)
        reader.default_byte_order = ByteOrder.BigEndian if first_eight_bytes[0:2] == b"\0\0" else ByteOrder.LittleEndian
        zeroes = first_eight_bytes[2:4] if reader.default_byte_order == ByteOrder.BigEndian else first_eight_bytes[4:6]
        reader.varint_size = 8 if zeroes == b"\0\0" else 4  # probable
        offset = reader.unpack_value("v")
        encoding = cls.get_encoding(reader.default_byte_order, reader.varint_size)
        names = []
        while offset != 0:
            names.append(reader.unpack_string(offset=offset, encoding=encoding))
            offset = reader.unpack_value("v")
        return cls(reader.default_byte_order, reader.varint_size, names)

    def to_writer(self) -> BinaryWriter:
        writer = BinaryWriter(
            byte_order=self.byte_order,
            varint_size=self.varint_size,
        )

        for i, name in self.names:
            writer.reserve(f"name_{i}", "v")
        writer.pad(self.varint_size)

        encoding = self.get_encoding(self.byte_order, self.varint_size)
        for i, name in self.names:
            writer.fill_with_position(f"name_{i}")
            writer.pack_z_string(name, encoding=encoding)
        writer.pad_align(16)
        return writer

    @staticmethod
    def get_encoding(byte_order: ByteOrder, varint_size: int):
        if varint_size == 8:
            return f"utf-16-{'be' if byte_order == ByteOrder.BigEndian else 'le'}"
        return "shift_jis_2004"
