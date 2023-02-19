from __future__ import annotations

__all__ = ["BaseMSBRegion"]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.text import pad_chars

from .enums import BaseMSBRegionSubtype, MSBSupertype
from .msb_entry import MSBEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "BaseMSBRegion"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBRegion(MSBEntry, abc.ABC):

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.REGIONS

    # Further specify subtype enum type.
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBRegionSubtype]
    # Regions have no supertype data struct.
    SUPERTYPE_DATA_STRUCT: tp.ClassVar = None
    UNKNOWN_DATA_SIZE: tp.ClassVar[int]

    entity_id: int = -1
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: Vector3 = field(default_factory=Vector3.zero)

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Regions do not have 'supertype data'. Just a header (with some supertype data) and optional subtype data."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)
        relative_subtype_data_offset = kwargs.pop("subtype_data_offset")
        if relative_subtype_data_offset > 0:
            reader.seek(entry_offset + relative_subtype_data_offset)
            kwargs |= cls.unpack_subtype_data(reader)
        cls._SETATTR_CHECKS_DISABLED = True  # will be re-enabled in `__post_init__`
        return cls(**kwargs)

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        region_start = reader.position
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)

        cls.check_null_field(reader, region_start + header.pop("unknown_offset_1"))
        cls.check_null_field(reader, region_start + header.pop("unknown_offset_2"))

        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")

        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        entity_id = reader["i", entry_offset + header.pop("entity_id_offset")]

        return header.to_dict(ignore_underscore_prefix=True) | {"name": name, "entity_id": entity_id}

    @classmethod
    def unpack_supertype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        raise TypeError("MSB regions contain no supertype data.")

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, list[MSBEntry]]
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        entry_offset = writer.position
        self.pack_header(writer, entry_offset, supertype_index, subtype_index, entry_lists)
        subtype_data_offset = writer.position - entry_offset if self.SUBTYPE_DATA_STRUCT is not None else 0
        writer.fill("subtype_data_offset", subtype_data_offset, obj=self)
        self.pack_subtype_data(writer, entry_lists)
        writer.fill("entity_id_offset", writer.position - entry_offset, obj=self)
        writer.pack("i", self.entity_id)

    def pack_header(
        self,
        writer: BinaryWriter,
        entry_offset: int,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
    ):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            _supertype_index=supertype_index,
            _subtype_int=self.SUBTYPE_ENUM.value,
            # NOTE: No `_subtype_index` in Regions.
            unknown_offset_1=RESERVED,
            unknown_offset_2=RESERVED,
            subtype_data_offset=RESERVED,
            entity_id_offset=RESERVED,
        )
        writer.fill("name_offset", writer.position - entry_offset, obj=self)
        writer.append(pad_chars(self.name, encoding=self.NAME_ENCODING, alignment=4))
        writer.fill("unknown_offset_1", writer.position - entry_offset, obj=self)
        writer.pad(4)
        writer.fill("unknown_offset_2", writer.position - entry_offset, obj=self)
        writer.pad(4)

    @classmethod
    def check_null_field(cls, reader: BinaryReader, offset_to_null: int):
        """Region headers have two unknown offsets to unused data, which should be null."""
        reader.seek(offset_to_null)
        zero = reader.read(cls.UNKNOWN_DATA_SIZE)
        if zero != b"\0" * cls.UNKNOWN_DATA_SIZE:
            _LOGGER.warning(f"Null data entry in `{cls.__name__}` was not zero: {zero}.")
