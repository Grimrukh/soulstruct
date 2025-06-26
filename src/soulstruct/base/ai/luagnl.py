from __future__ import annotations

__all__ = ["LuaGNL"]

from dataclasses import field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *


class LuaGNL(GameFile):
    """Global Name List file that lists all the functions declared in all the Lua scripts in the `LuaBND`.

    Literally just a list of offsets to null-terminated strings.

    Not actually required for AI to function (after Demon's Souls, at least).
    """

    byte_order: ByteOrder = ByteOrder.LittleEndian
    long_varints: bool = False
    names: list[str] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> LuaGNL:
        # We can only guess at byte order and varint size from the appearance of the first 1/2 string offsets.
        first_eight_bytes = reader.peek(8)
        reader.byte_order = ByteOrder.BigEndian if first_eight_bytes[0:2] == b"\0\0" else ByteOrder.LittleEndian
        zeroes = first_eight_bytes[2:4] if reader.byte_order == ByteOrder.BigEndian else first_eight_bytes[4:6]
        reader.long_varints = zeroes == b"\0\0"  # probable
        offset = reader["v"]
        encoding = cls.get_encoding(reader.byte_order, reader.long_varints)
        names = []
        while offset != 0:
            names.append(reader.unpack_string(offset=offset, encoding=encoding))
            offset = reader["v"]
        return cls(byte_order=reader.byte_order, long_varints=reader.long_varints, names=names)

    def to_writer(self) -> BinaryWriter:
        writer = BinaryWriter(
            byte_order=self.byte_order,
            long_varints=self.long_varints,
        )

        for i, name in self.names:
            writer.reserve(f"name_{i}", "v")
        writer.pad(8 if self.long_varints else 4)

        encoding = self.get_encoding(self.byte_order, self.long_varints)
        for i, name in self.names:
            writer.fill_with_position(f"name_{i}")
            writer.pack_z_string(name, encoding=encoding)
        writer.pad_align(16)
        return writer

    @staticmethod
    def get_encoding(byte_order: ByteOrder, long_varints: bool):
        if long_varints:
            return byte_order.get_utf_16_encoding()
        return "shift_jis_2004"
