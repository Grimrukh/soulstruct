"""Binder flags, which indicate various things about the binder file (BND or BXF).

TODO: Determine which file types in which games use which magic values, so they can be initialized to defaults.
"""
from __future__ import annotations

__all__ = ["BinderFlags", "BinderEntryFlags"]

import typing as tp

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryReader, BinaryWriter


class BinderFlags(int):
    """Bit flags for binder file. Note that the bit order is 'big endian' here."""

    @property
    def is_big_endian(self):
        return self & 0b0000_0001  # 0x80

    @property
    def has_ids(self):
        return self & 0b0000_0010  # 0x40

    @property
    def has_names_1(self):
        return self & 0b0000_0100  # 0x20

    @property
    def has_names_2(self):
        return self & 0b0000_1000  # 0x10

    @property
    def has_names(self):
        """Looks for either 'names' flag. Unsure what the difference is."""
        return self & (0b0000_0100 | 0b0000_1000)

    @property
    def has_long_offsets(self):
        return self & 0b0001_0000  # 0x08

    @property
    def has_compression(self):
        return self & 0b0010_0000  # 0x04

    @property
    def has_flag_6(self):
        return self & 0b0100_0000  # 0x02

    @property
    def has_flag_7(self):
        return self & 0b1000_0000  # 0x01

    @classmethod
    def read(cls, reader: BinaryReader, bit_big_endian: bool) -> BinderFlags:
        """Read a byte, reverse it if necessary, and return flags integer."""
        flags = cls(reader.unpack_value("B"))
        if not bit_big_endian and not (flags.is_big_endian and not flags.has_flag_7):
            flags = cls(int(f"{flags:08b}"[::-1], 2))
        return flags

    def pack(self, writer: BinaryWriter, bit_big_endian: bool):
        if not bit_big_endian and not (self.is_big_endian and not self.has_flag_7):
            writer.pack("B", int(f"{self:08b}"[::-1], 2))
        else:
            writer.pack("B", self)

    def get_bnd_entry_header_size(self) -> int:
        """Calculate binder entry header size."""
        size = 16  # Base size.
        if self.has_ids:
            size += 4
        if self.has_names_1 or self.has_names_2:
            size += 4
        if self.has_compression:
            size += 8
        size += 8 if self.has_long_offsets else 4
        return size


class BinderEntryFlags(int):

    @property
    def is_compressed(self):
        return self & 0b0000_0001  # 0x80

    @property
    def has_flag_1(self):
        return self & 0b0000_0010  # 0x40

    @property
    def has_flag_2(self):
        return self & 0b0000_0100  # 0x20

    @property
    def has_flag_3(self):
        return self & 0b0000_1000  # 0x10

    @property
    def has_flag_4(self):
        return self & 0b0001_0000  # 0x08

    @property
    def has_flag_5(self):
        return self & 0b0010_0000  # 0x04

    @property
    def has_flag_6(self):
        return self & 0b0100_0000  # 0x02

    @property
    def has_flag_7(self):
        return self & 0b1000_0000  # 0x01

    @classmethod
    def read(cls, reader: BinaryReader, bit_big_endian: bool) -> BinderEntryFlags:
        """Read a byte, reverse it if necessary, and return flags integer."""
        flags = cls(reader.unpack_value("B"))
        if not bit_big_endian:
            flags = cls(int(f"{flags:08b}"[::-1], 2))
        return flags

    def pack(self, writer: BinaryWriter, bit_big_endian: bool):
        if not bit_big_endian:
            writer.pack("B", int(f"{self:08b}"[::-1], 2))
        else:
            writer.pack("B", self)
