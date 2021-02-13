__all__ = ["MSBEntryList"]

import abc

from soulstruct.base.maps.msb.msb_entry import MSBEntryList as _BaseMSBEntryList
from soulstruct.utilities.binary_struct import BinaryStruct


class MSBEntryList(_BaseMSBEntryList, abc.ABC):

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
