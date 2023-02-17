"""Collects all game headers for MSB entry superlists (parts, events, regions, models) in one place.

Provides a dictionary that maps game submodule name (from `GameFile.get_game()`) to the appropriate class.
"""
__all__ = ["MSBEntrySuperlistHeader", "MSB_ENTRY_SUPERLIST_HEADERS"]

import abc
from dataclasses import dataclass, field

from soulstruct.utilities.binary import *


# TODO: move to game subclasses, changed my mind

@dataclass(slots=True)
class MSBEntrySuperlistHeader_PTDE(BinaryStruct):
    # TODO: apparently big-endian if this is > 0xFFFF, but I've only seen zero in DS1.
    _big_endian_check: int = field(init=False, **Binary(asserted=0))
    name_offset: int
    entry_offset_count: int

    def is_big_endian(self) -> bool:
        return self.big_endian_check > 0xFFFF


@dataclass(slots=True)
class MSBEntrySuperlistHeader_BB(BinaryStruct):
    _version: int = field(init=False, **Binary(asserted=3))
    entry_offset_count: int
    name_offset: long

    def is_big_endian(self) -> bool:
        return False


MSB_ENTRY_SUPERLIST_HEADERS = {
    "darksouls1ptde": MSBEntrySuperlistHeader_PTDE,
    "darksouls1r": MSBEntrySuperlistHeader_PTDE,  # identical
    "bloodborne": MSBEntrySuperlistHeader_BB,
    # TODO: other games
}
