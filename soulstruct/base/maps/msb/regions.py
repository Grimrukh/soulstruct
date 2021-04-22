from __future__ import annotations

__all__ = [
    "MSBRegion",
    "MSBRegionPoint",
    "MSBRegionCircle",
    "MSBRegionCylinder",
    "MSBRegionSphere",
    "MSBRegionRect",
    "MSBRegionBox",
    "MSBRegionList",
]

import abc
import typing as tp
import logging
import struct

from soulstruct.utilities.misc import partialmethod
from soulstruct.utilities.text import pad_chars
from soulstruct.utilities.binary import BinaryStruct, BinaryReader
from soulstruct.utilities.maths import Vector3

from .enums import MSBRegionSubtype
from .msb_entry import MSBEntryList, MSBEntryEntityCoordinates
from .utils import MapFieldInfo

_LOGGER = logging.getLogger(__name__)


class MSBRegion(MSBEntryEntityCoordinates, abc.ABC):

    ENTRY_SUBTYPE: MSBRegionSubtype = None
    REGION_STRUCT: BinaryStruct = None
    REGION_TYPE_DATA_STRUCT: BinaryStruct = None
    NAME_ENCODING = ""
    UNKNOWN_DATA_SIZE = -1

    FIELD_INFO = MSBEntryEntityCoordinates.FIELD_INFO | {
        "translate": MapFieldInfo(
            "Translate",
            Vector3,
            Vector3.zero(),
            "3D coordinates of the region's position. Note that this is the middle of the bottom face for box "
            "regions.",
        ),
        "rotate": MapFieldInfo(
            "Rotate",
            Vector3,
            Vector3.zero(),
            "Euler angles for region rotation around its local X, Y, and Z axes.",
        ),
    }

    translate: Vector3
    rotate: Vector3

    def __init__(self, source=None, **kwargs):
        self._region_index = None  # Final automatic assignment done on `MSB.pack()`.
        super().__init__(source=source, **kwargs)

    def unpack(self, msb_reader: BinaryReader):
        region_offset = msb_reader.position
        base_data = msb_reader.unpack_struct(self.REGION_STRUCT)
        self.name = msb_reader.unpack_string(
            offset=region_offset + base_data["name_offset"], encoding=self.NAME_ENCODING,
        )
        self._region_index = base_data["__region_index"]
        self.translate = Vector3(base_data["translate"])
        self.rotate = Vector3(base_data["rotate"])
        self.check_null_field(msb_reader, region_offset + base_data["unknown_offset_1"])
        self.check_null_field(msb_reader, region_offset + base_data["unknown_offset_2"])

        if base_data["type_data_offset"] != 0:
            msb_reader.seek(region_offset + base_data["type_data_offset"])
            self.unpack_type_data(msb_reader)

        msb_reader.seek(region_offset + base_data["entity_id_offset"])
        self.entity_id = msb_reader.unpack_value("i")

        return region_offset + base_data["entity_id_offset"]

    def pack(self, region_index=0):
        name_offset = self.REGION_STRUCT.size
        packed_name = pad_chars(self.get_name_to_pack(), encoding=self.NAME_ENCODING, pad_to_multiple_of=4)
        unknown_offset_1 = name_offset + len(packed_name)
        unknown_offset_2 = unknown_offset_1 + 4
        packed_type_data = self.pack_type_data()
        if packed_type_data:
            type_data_offset = unknown_offset_2 + 4
            entity_id_offset = type_data_offset + len(packed_type_data)
        else:
            type_data_offset = 0
            entity_id_offset = unknown_offset_2 + 4
        packed_base_data = self.REGION_STRUCT.pack(
            name_offset=name_offset,
            __region_index=region_index,
            region_type=self.ENTRY_SUBTYPE,
            translate=list(self.translate),
            rotate=list(self.rotate),
            unknown_offset_1=unknown_offset_1,
            unknown_offset_2=unknown_offset_2,
            type_data_offset=type_data_offset,
            entity_id_offset=entity_id_offset,
        )
        packed_entity_id = struct.pack("i", self.entity_id)
        return packed_base_data + packed_name + b"\0\0\0\0" * 2 + packed_type_data + packed_entity_id

    def unpack_type_data(self, msb_reader: BinaryReader):
        self.set(**msb_reader.unpack_struct(self.REGION_TYPE_DATA_STRUCT))

    def pack_type_data(self):
        return self.REGION_TYPE_DATA_STRUCT.pack(self)

    def set_indices(self, region_index):
        self._region_index = region_index

    @classmethod
    def check_null_field(cls, msb_reader: BinaryReader, offset_to_null):
        msb_reader.seek(offset_to_null)
        zero = msb_reader.read(cls.UNKNOWN_DATA_SIZE)
        if zero != b"\0" * cls.UNKNOWN_DATA_SIZE:
            _LOGGER.warning(f"Null data entry in `{cls.__name__}` was not zero: {zero}.")


class MSBRegionPoint(MSBRegion, abc.ABC):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way will the
    player be facing when they spawn?)."""

    ENTRY_SUBTYPE = MSBRegionSubtype.Point
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


class MSBRegionCircle(MSBRegion, abc.ABC):
    """Almost never used (no volume)."""

    ENTRY_SUBTYPE = MSBRegionSubtype.Circle
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("radius", "f"),
    )

    FIELD_INFO = MSBRegion.FIELD_INFO | {
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


class MSBRegionSphere(MSBRegion, abc.ABC):
    ENTRY_SUBTYPE = MSBRegionSubtype.Sphere
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("radius", "f"),
    )

    FIELD_INFO = MSBRegion.FIELD_INFO | {
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


class MSBRegionCylinder(MSBRegion, abc.ABC):
    ENTRY_SUBTYPE = MSBRegionSubtype.Cylinder
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("radius", "f"),
        ("height", "f"),
    )

    FIELD_INFO = MSBRegion.FIELD_INFO | {
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


class MSBRegionRect(MSBRegion, abc.ABC):
    """Almost never used (no volume)."""

    ENTRY_SUBTYPE = MSBRegionSubtype.Rect
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("width", "f"),
        ("depth", "f"),
    )

    FIELD_INFO = MSBRegion.FIELD_INFO | {
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


class MSBRegionBox(MSBRegion, abc.ABC):
    ENTRY_SUBTYPE = MSBRegionSubtype.Box
    REGION_TYPE_DATA_STRUCT = BinaryStruct(
        ("width", "f"),
        ("depth", "f"),
        ("height", "f"),
    )

    FIELD_INFO = MSBRegion.FIELD_INFO | {
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


class MSBRegionList(MSBEntryList[MSBRegion], abc.ABC):
    ENTRY_LIST_NAME = "Regions"
    ENTRY_SUBTYPE_ENUM = MSBRegionSubtype
    SUBTYPE_CLASSES = {}  # type: dict[MSBRegionSubtype, tp.Type[MSBRegion]]
    SUBTYPE_OFFSET = -1  # type: int

    _entries: list[MSBRegion]

    Points: tp.Sequence[MSBRegionPoint]
    Circles: tp.Sequence[MSBRegionCircle]
    Spheres: tp.Sequence[MSBRegionSphere]
    Cylinders: tp.Sequence[MSBRegionCylinder]
    Rectangles: tp.Sequence[MSBRegionRect]
    Boxes: tp.Sequence[MSBRegionBox]

    new_point: tp.Callable[..., MSBRegionPoint] = partialmethod(MSBEntryList.new, MSBRegionSubtype.Point)
    new_circle: tp.Callable[..., MSBRegionCircle] = partialmethod(MSBEntryList.new, MSBRegionSubtype.Circle)
    new_sphere: tp.Callable[..., MSBRegionSphere] = partialmethod(MSBEntryList.new, MSBRegionSubtype.Sphere)
    new_cylinder: tp.Callable[..., MSBRegionCylinder] = partialmethod(MSBEntryList.new, MSBRegionSubtype.Cylinder)
    new_rect: tp.Callable[..., MSBRegionRect] = partialmethod(MSBEntryList.new, MSBRegionSubtype.Rect)
    new_box: tp.Callable[..., MSBRegionBox] = partialmethod(MSBEntryList.new, MSBRegionSubtype.Box)

    def pack_entry(self, index: int, entry: MSBRegion):
        return entry.pack(index)

    def set_indices(self):
        """Global region index only."""
        for i, entry in enumerate(self._entries):
            entry.set_indices(region_index=i)


for _entry_subtype in MSBRegionList.ENTRY_SUBTYPE_ENUM:
    setattr(
        MSBRegionList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
