from __future__ import annotations

__all__ = [
    "BaseMSBRegion",
    "BaseMSBRegionPoint",
    "BaseMSBRegionCircle",
    "BaseMSBRegionCylinder",
    "BaseMSBRegionSphere",
    "BaseMSBRegionRect",
    "BaseMSBRegionBox",
    "BaseMSBRegionList",
]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.text import pad_chars

from .msb_entry import MSBEntry
from .msb_entry_list import BaseMSBEntryList
from .utils import MapFieldInfo

try:
    Self = tp.Self
except AttributeError:
    Self = "BaseMSBRegion"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class BaseMSBRegion(MSBEntry, abc.ABC):

    SUPERTYPE_DATA_STRUCT: tp.ClassVar = None
    UNKNOWN_DATA_SIZE: tp.ClassVar[int] = -1

    entity_id: int = -1
    translate: Vector3 = field(default_factory=lambda: Vector3.zero())
    rotate: Vector3 = field(default_factory=lambda: Vector3.zero())

    def __init__(self, source=None, **kwargs):
        self._region_index = None  # Final automatic assignment done on `MSB.pack()`.
        super().__init__(source=source, **kwargs)

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Regions do not have 'supertype data'. Just a header (with some supertype data) and optional subtype data."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)
        relative_subtype_data_offset = kwargs.pop("subtype_data_offset")
        if relative_subtype_data_offset > 0:
            reader.seek(entry_offset + relative_subtype_data_offset)
            kwargs |= cls.unpack_subtype_data(reader)
        return cls(**kwargs)

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)

        cls.check_null_field(reader, header.pop("unknown_offset_1"))
        cls.check_null_field(reader, header.pop("unknown_offset_2"))

        header_subtype_int = header.pop("subtype_int")
        if header_subtype_int != cls.SUBTYPE_INT:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")

        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        entity_id = reader.unpack_value("i", offset=entry_offset + header.pop("entity_id_offset"))

        return header.to_dict(ignore_underscore_prefix=True) | {"name": name, "entity_id": entity_id}

    @classmethod
    def unpack_supertype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        raise TypeError("MSB regions contain no supertype data.")

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, list[MSBEntry]]
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        self.pack_header(writer, supertype_index, subtype_index)
        self.pack_subtype_data(writer, entry_lists)
        writer.fill_with_position("entity_id_offset", self)
        writer.pack("i", self.entity_id)

    def pack_header(self, writer: BinaryWriter, supertype_index: int, subtype_index: int):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            _supertype_index=supertype_index,
            subtype_int=self.SUBTYPE_INT,
            _subtype_index=subtype_index,
            unknown_offset_1=RESERVED,
            unknown_offset_2=RESERVED,
            subtype_data_offset=RESERVED,
            entity_id_offset=RESERVED,
        )
        writer.fill_with_position("name_offset", self)
        writer.append(pad_chars(self.name, encoding=self.NAME_ENCODING, alignment=4))
        writer.fill_with_position("unknown_offset_1", self)
        writer.pad(4)
        writer.fill_with_position("unknown_offset_2", self)
        writer.pad(4)

    @classmethod
    def check_null_field(cls, reader: BinaryReader, offset_to_null: int):
        """Region headers have two unknown offsets to unused data, which should be null."""
        reader.seek(offset_to_null)
        zero = reader.read(cls.UNKNOWN_DATA_SIZE)
        if zero != b"\0" * cls.UNKNOWN_DATA_SIZE:
            _LOGGER.warning(f"Null data entry in `{cls.__name__}` was not zero: {zero}.")


class BaseMSBRegionPoint(BaseMSBRegion, abc.ABC):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way will the
    player be facing when they spawn?)."""

    REGION_TYPE_DATA_STRUCT = None

    FIELD_ORDER = (
        "entity_id",
        "translate",
        "rotate",
    )

    def unpack_type_data(self, msb_reader: BinaryReader):
        pass

    def pack_type_data(self):
        return b""


class BaseMSBRegionCircle(BaseMSBRegion, abc.ABC):
    """Almost never used (no volume)."""

    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("radius", "f"),
    )

    FIELD_INFO = BaseMSBRegion.FIELD_INFO | {
        "radius": MapFieldInfo(
            "Radius",
            float,
            1.0,
            "Radius (in xy-plane) of circular region.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "translate",
        "rotate",
        "radius",
    )

    radius: float


class BaseMSBRegionSphere(BaseMSBRegion, abc.ABC):
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("radius", "f"),
    )

    FIELD_INFO = BaseMSBRegion.FIELD_INFO | {
        "radius": MapFieldInfo(
            "Radius",
            float,
            1.0,
            "Radius of sphere-shaped region.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "translate",
        "rotate",
        "radius",
    )

    radius: float


class BaseMSBRegionCylinder(BaseMSBRegion, abc.ABC):
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("radius", "f"),
        ("height", "f"),
    )

    FIELD_INFO = BaseMSBRegion.FIELD_INFO | {
        "radius": MapFieldInfo(
            "Radius",
            float,
            1.0,
            "Radius (in xz-plane) of cylinder-shaped region.",
        ),
        "height": MapFieldInfo(
            "Height",
            float,
            1.0,
            "Height (along y-axis) of cylinder-shaped region.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "translate",
        "rotate",
        "radius",
        "height",
    )

    radius: float
    height: float


class BaseMSBRegionRect(BaseMSBRegion, abc.ABC):
    """Almost never used (no volume)."""
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("width", "f"),
        ("depth", "f"),
    )

    FIELD_INFO = BaseMSBRegion.FIELD_INFO | {
        "width": MapFieldInfo(
            "Width",
            float,
            1.0,
            "Width (along x-axis) of rectangle-shaped region.",
        ),
        "height": MapFieldInfo(
            "Height",
            float,
            1.0,
            "Height (along y-axis) of rectangle-shaped region.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "translate",
        "rotate",
        "width",
        "height",
    )

    width: float
    height: float


class BaseMSBRegionBox(BaseMSBRegion, abc.ABC):
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("width", "f"),
        ("depth", "f"),
        ("height", "f"),
    )

    FIELD_INFO = BaseMSBRegion.FIELD_INFO | {
        "width": MapFieldInfo(
            "Width",
            float,
            1.0,
            "Width (along x-axis) of box-shaped region.",
        ),
        "depth": MapFieldInfo(
            "Depth",
            float,
            1.0,
            "Depth (along z-axis) of box-shaped region.",
        ),
        "height": MapFieldInfo(
            "Height",
            float,
            1.0,
            "Height (along y-axis) of box-shaped region.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "translate",
        "rotate",
        "width",
        "depth",
        "height",
    )

    width: float
    depth: float
    height: float


class BaseMSBRegionList(BaseMSBEntryList, abc.ABC):

    @abc.abstractmethod
    def set_indices(self):
        pass
