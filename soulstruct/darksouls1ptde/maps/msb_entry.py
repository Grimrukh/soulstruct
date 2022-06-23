__all__ = ["MSBEntryList"]

import abc
import typing as tp

from soulstruct.base.maps.msb.msb_entry import MSBEntry
from soulstruct.base.maps.msb.msb_entry_list import BaseMSBEntryList
from soulstruct.utilities.binary import BinaryStruct


MSBEntryType = tp.TypeVar("MSBEntryType", bound=MSBEntry)


class MSBEntryList(BaseMSBEntryList, abc.ABC, tp.Generic[MSBEntryType]):

    MAP_ENTITY_LIST_HEADER = BinaryStruct(
        "4x",
        ("name_offset", "i"),
        ("entry_offset_count", "i"),
    )
    MAP_ENTITY_ENTRY_OFFSET = BinaryStruct(
        ("entry_offset", "i"),
    )
    MAP_ENTITY_LIST_TAIL = BinaryStruct(
        ("next_entry_list_offset", "i"),
    )
    NAME_ENCODING = "utf-8"
