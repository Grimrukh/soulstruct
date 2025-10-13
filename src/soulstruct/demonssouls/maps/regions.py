from __future__ import annotations

__all__ = [
    "MSBRegion",
    "RegionShape",
    "RegionShapeType",
    "PointShape",
    "CircleShape",
    "SphereShape",
    "CylinderShape",
    "RectShape",
    "BoxShape",
]

import logging
import typing as tp
from dataclasses import dataclass

from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.base.maps.msb.regions import *
from soulstruct.base.maps.msb.region_shapes import *
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import EulerDeg, Vector3
from .enums import MSBRegionSubtype

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList
    from soulstruct.base.maps.msb import MSBEntry

_LOGGER = logging.getLogger(__name__)


class RegionHeaderStruct(MSBHeaderStruct):
    name_offset: int
    _subtype_int: int  # always 0 in DeS
    supertype_index: int
    shape_type_int: int
    translate: Vector3
    rotate: EulerDeg
    null_struct_0_offset: int
    null_struct_1_offset: int
    shape_data_offset: int
    supertype_data_offset: int  # just `entity_id` in DeS
    subtype_data_offset: int = binary(asserted=0, init=False)  # no subtype data in DS1 Regions
    _pad1: bytes = binary_pad(4, init=False)  # extra pad in DeS compared to DS1

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBRegion],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        kwargs = super(RegionHeaderStruct, cls).reader_to_entry_kwargs(reader, entry_type, entry_offset)

        for i in (0, 1):
            # Check that null structs are 4 null bytes.
            null_struct_offset = kwargs.pop(f"null_struct_{i}_offset")
            reader.seek(entry_offset + null_struct_offset)
            zero = reader.read(4)
            if zero.strip(b"\0"):
                _LOGGER.warning(f"Null data entry in `{cls.__name__}` was not zero: {zero}.")

        # Read shape struct.
        shape_type_int = kwargs.pop("shape_type_int")
        try:
            shape_class = entry_type.SHAPE_CLASSES[shape_type_int]  # type: type[RegionShape]
        except KeyError:
            if shape_type_int == 6:
                raise ValueError("Composite Region shape type (6) is not supported in older games.")
            raise ValueError(f"Invalid MSB region shape type value: {shape_type_int}")
        reader.seek(entry_offset + kwargs.pop("shape_data_offset"))
        kwargs["shape"] = shape_class.from_msb_reader(reader)

        return kwargs

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBRegion,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        super(RegionHeaderStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)
        kwargs["shape_type_int"] = entry.shape_type_int
        kwargs["null_struct_0_offset"] = RESERVED
        kwargs["null_struct_1_offset"] = RESERVED
        kwargs.pop("subtype_index")  # not used by regions

    @classmethod
    def post_write(
        cls,
        entry: MSBRegion,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: [dict[str, IDList[MSBEntry]]],  # may be required by subclasses
    ):
        super(RegionHeaderStruct, cls).post_write(entry, writer, entry_offset, entry_lists)
        writer.fill("null_struct_0_offset", writer.position - entry_offset, obj=entry)
        writer.pad(4)
        writer.fill("null_struct_1_offset", writer.position - entry_offset, obj=entry)
        writer.pad(4)

        shape_offset = writer.position - entry_offset
        writer.fill("shape_data_offset", shape_offset, obj=entry)
        entry.shape.to_msb_writer(writer)


class RegionSupertypeData(MSBBinaryStruct):
    entity_id: int
    _pad1: bytes = binary_pad(12, init=False)  # not present in DS1


@dataclass(slots=True, eq=False, repr=False)
class MSBRegion(BaseMSBRegion):
    """Only DS1 region subtype -- not abstract."""

    HEADER_STRUCT = RegionHeaderStruct
    NAME_ENCODING = "shift_jis_2004"
    SUBTYPE_ENUM = MSBRegionSubtype.All
    STRUCTS = {
        # Shape data goes here (manual).
        "supertype_data": RegionSupertypeData,
        # Subtype data offset is always zero and ignored in header.
    }
