__all__ = ["MSBEntryList"]

import abc

from soulstruct.base.maps.msb.msb_entry import MSBEntryList as _BaseMSBEntryList
from soulstruct.utilities.binary import BinaryStruct


class MSBEntryList(_BaseMSBEntryList, abc.ABC):

    MAP_ENTITY_LIST_HEADER = BinaryStruct(
        ("version", "i", 3),
        ("entry_offset_count", "i"),
        ("name_offset", "q"),
    )
    MAP_ENTITY_ENTRY_OFFSET = BinaryStruct(
        ("entry_offset", "q"),
    )
    MAP_ENTITY_LIST_TAIL = BinaryStruct(
        ("next_entry_list_offset", "q"),
    )
    NAME_ENCODING = "utf-16-le"
