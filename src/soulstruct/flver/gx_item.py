from __future__ import annotations

__all__ = ["GXItem"]

import logging
import typing as tp
from dataclasses import dataclass

from soulstruct.utilities.binary import *
from .version import FLVERVersion

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class GXItem:
    """Item that sets various material rendering properties.

    Doesn't use `BinaryStruct` due to the way its header `size` and `data` interact.
    """
    # List of GXItems should end with a 'terminator' item that has one of these categories.
    TERMINATOR_CATEGORIES: tp.ClassVar[set[bytes]] = {b'\xff\xff\xff\x7f', b'\xff\xff\xff\xff'}
    HEADER_SIZE: tp.ClassVar[int] = 12  # category, index, size (all four bytes each)

    category: bytes  # typically ASCII, but not decoded as it may be one of the 'terminator' values above
    index: int  # index of `GXItem` 'subtype' (e.g. 100), NOT just its index in a FLVER list
    # `size` appears here in header (`len(data) + 12`).
    data: bytes  # packed 'argument' data; usage varies by category/index and is not managed here

    @classmethod
    def from_bytes(cls, reader: bytes | BinaryReader):
        if isinstance(reader, bytes):
            reader = BinaryReader(reader)
        category = reader.unpack_value("4s")
        index = reader.unpack_value("i")
        size = reader.unpack_value("i")  # total size of struct (12) and raw `data`
        data = reader.read(size - cls.HEADER_SIZE)
        return cls(category, index, data)

    def to_writer(self, writer: BinaryWriter):
        if len(self.category) != 4:
            raise ValueError(f"`GXItem.category` must be 4 bytes long, not {len(self.category)} bytes: {self.category}")
        writer.append(self.category)
        writer.pack("i", self.index)
        writer.pack("i", len(self.data) + self.HEADER_SIZE)
        writer.append(self.data)

    def __hash__(self):
        """For identifying unique lists of `GXItem`s."""
        return hash((self.category, self.index, self.data))

    @property
    def is_terminator(self):
        return self.category in self.TERMINATOR_CATEGORIES

    @classmethod
    def new_terminator(cls):
        """
        TODO: This is valid for Bloodborne, DS3, Sekiro, and Elden Ring.
         I think terminator items may have appeared somewhere (DS2? Other FLVERs?) with:
            category = b"\xff\xff\xff\xff"
            data     = b"\x00\x00\x00\x00"
         But I can't find those FLVERs. And this terminator may work in those FLVERs anyway.
        """
        return cls(b"\xff\xff\xff\x7f", 100, b"")

    @classmethod
    def read_list(cls, flver_reader: BinaryReader, flver_version: FLVERVersion) -> list[GXItem]:
        """Read a list of `GXItem` instances from FLVER, including the final terminator `GXItem` (which no `Material`
        should ever use).

        The `FLVER` instance will maintain the final terminator item for byte-perfect rewrites.
        """
        if flver_version <= FLVERVersion.DarkSouls2:
            # Only one `GXItem` with no terminator item. TODO: Definitely no terminator item?
            gx_item = cls.from_bytes(flver_reader)
            return [gx_item]

        # Keep unpacking `GXItem`s until we unpack one with a terminator category.
        # The terminator item is still appended to the list, as its exact category and data may vary.
        gx_items = []
        while True:
            gx_item = cls.from_bytes(flver_reader)
            gx_items.append(gx_item)
            if gx_item.is_terminator:
                # Warn user if contents of terminator `GXItem` are not as expected.
                if gx_item.index != 100:
                    _LOGGER.warning(f"List terminator `GXItem` should have `index == 100`, not: {gx_item.index}")
                if gx_item.data.strip(b"\0"):
                    _LOGGER.warning(f"List terminator `GXItem` has non-empty `data`: {gx_item.data}")
                break  # terminator item found
        return gx_items  # including terminator item
