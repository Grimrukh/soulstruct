__all__ = ["MSBEntryList"]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.msb_entry import MSBEntry
from soulstruct.base.maps.msb.msb_entry_list import BaseMSBEntryList
from soulstruct.utilities.binary import *


MSBEntryType = tp.TypeVar("MSBEntryType", bound=MSBEntry)


@dataclass(slots=True)
class MSBEntryList(BaseMSBEntryList, abc.ABC, tp.Generic[MSBEntryType]):

    @dataclass(slots=True)
    class MAP_ENTITY_LIST_HEADER(NewBinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(4))
        name_offset: int
        entry_offset_count: int

    VARINT_SIZE = 4
    NAME_ENCODING = "utf-8"
