
__all__ = [
    "EventsIndicesData",
    "EventsNamesData",
    "BaseMSBEvent",
    "BaseMSBEventList",
]

import abc
import typing as tp
from collections import namedtuple

from soulstruct.utilities.text import pad_chars
from soulstruct.utilities.binary import BinaryStruct, BinaryReader

from .enums import BaseMSBEventSubtype
from .msb_entry import MSBEntryEntity
from .msb_entry_list import BaseMSBEntryList


EventsIndicesData = namedtuple(
    "EventsIndicesData",
    [
        "event_index",
        "local_event_index",
        "region_indices",
        "part_indices",
    ],
)

EventsNamesData = namedtuple(
    "EventsNamesData",
    [
        "region_names",
        "part_names",
    ],
)


class BaseMSBEvent(MSBEntryEntity, abc.ABC):
    """Parent class for MSB events, which describe various things that occur in maps (often attached to Regions)."""

    ENTRY_SUBTYPE: BaseMSBEventSubtype = None
    EVENT_HEADER_STRUCT: BinaryStruct = None
    EVENT_BASE_DATA_STRUCT: BinaryStruct = None
    EVENT_TYPE_DATA_STRUCT: BinaryStruct = None
    NAME_ENCODING = ""

    REFERENCE_FIELDS = {"parts": ["base_part_name"], "regions": ["base_region_name"]}

    base_part_name: tp.Optional[str]
    base_region_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._event_index = None  # global index
        self._local_event_index = None  # local type index
        self._base_part_index = None
        self._base_part_name = None
        self._base_region_index = None
        self._base_region_name = None
        super().__init__(source=source, **kwargs)

    def unpack(self, msb_reader: BinaryReader):
        event_offset = msb_reader.position
        header = msb_reader.unpack_struct(self.EVENT_HEADER_STRUCT)
        if header["__event_type"] != self.ENTRY_SUBTYPE:
            raise ValueError(f"Unexpected MSB event type value {header['__event_type']} for {self.__class__.__name__}.")
        msb_reader.seek(event_offset + header["__base_data_offset"])
        base_data = msb_reader.unpack_struct(self.EVENT_BASE_DATA_STRUCT)
        name_offset = event_offset + header["__name_offset"]
        self.name = msb_reader.unpack_string(offset=name_offset, encoding=self.NAME_ENCODING)
        self.set(**header)
        self.set(**base_data)
        msb_reader.seek(event_offset + header["__type_data_offset"])
        self.unpack_type_data(msb_reader)

    @property
    def base_part_name(self):
        return self._base_part_name

    @base_part_name.setter
    def base_part_name(self, value: tp.Union[None, str]):
        if isinstance(value, str):
            self._base_part_name = value if value else None
        elif value is None:
            self._base_part_name = None
        else:
            raise TypeError(f"`base_part_name` must be a string or `None`, not {value}.")

    @property
    def base_region_name(self):
        return self._base_region_name

    @base_region_name.setter
    def base_region_name(self, value: tp.Union[None, str]):
        if isinstance(value, str):
            self._base_region_name = value if value else None
        elif value is None:
            self._base_region_name = None
        else:
            raise TypeError(f"`base_region_name` must be a string or `None`, not {value}.")

    def set_indices(self, indices: EventsIndicesData):
        self._event_index = indices.event_index
        self._local_event_index = indices.local_event_index
        self._base_part_index = indices.part_indices[self._base_part_name] if self._base_part_name else -1
        self._base_region_index = indices.region_indices[self._base_region_name] if self._base_region_name else -1

    def set_names(self, names: EventsNamesData):
        self._base_part_name = names.part_names[self._base_part_index] if self._base_part_index != -1 else None
        self._base_region_name = names.region_names[self._base_region_index] if self._base_region_index != -1 else None

    def pack(self):
        name_offset = self.EVENT_HEADER_STRUCT.size
        packed_name = pad_chars(self.get_name_to_pack(), encoding=self.NAME_ENCODING, pad_to_multiple_of=4)
        base_data_offset = name_offset + len(packed_name)
        packed_base_data = self.EVENT_BASE_DATA_STRUCT.pack(self)
        type_data_offset = base_data_offset + len(packed_base_data)
        packed_type_data = self.pack_type_data()
        packed_header = self.EVENT_HEADER_STRUCT.pack(
            __name_offset=name_offset,
            _event_index=self._event_index,
            __event_type=self.ENTRY_SUBTYPE,
            _local_event_index=self._local_event_index,
            __base_data_offset=base_data_offset,
            __type_data_offset=type_data_offset,
        )
        return packed_header + packed_name + packed_base_data + packed_type_data

    def unpack_type_data(self, msb_reader: BinaryReader):
        self.set(**msb_reader.unpack_struct(self.EVENT_TYPE_DATA_STRUCT, exclude_asserted=True))

    def pack_type_data(self):
        return self.EVENT_TYPE_DATA_STRUCT.pack(self)


class BaseMSBEventList(BaseMSBEntryList, abc.ABC):

    @abc.abstractmethod
    def set_indices(self, region_indices, part_indices):
        pass

    @abc.abstractmethod
    def set_names(self, region_names, part_names):
        pass
