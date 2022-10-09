__all__ = [
    "MSBRegion",
    "MSBRegionPoint",
    "MSBRegionCircle",
    "MSBRegionSphere",
    "MSBRegionCylinder",
    "MSBRegionRect",
    "MSBRegionBox",
    "MSBRegionList",
]

import abc
import typing as tp

from soulstruct.base.maps.msb.msb_entry_list import GenericMSBEntryList
from soulstruct.base.maps.msb.regions import *
from soulstruct.utilities.binary import BinaryStruct
from soulstruct.utilities.misc import partialmethod

from .enums import MSBRegionSubtype
from .msb_entry import MSBEntryList


class MSBRegion(BaseMSBRegion, abc.ABC):

    REGION_STRUCT = BinaryStruct(
        ("name_offset", "i"),
        "4x",
        ("__region_index", "i"),
        ("region_type", "i"),
        ("translate", "3f"),
        ("rotate", "3f"),  # These are Euler angle rotations (and can therefore be gimbal-locked).
        ("unknown_offset_1", "i"),
        ("unknown_offset_2", "i"),
        ("type_data_offset", "i"),
        ("entity_id_offset", "i"),
        "4x",
    )

    NAME_ENCODING = "shift_jis_2004"
    UNKNOWN_DATA_SIZE = 4


class MSBRegionPoint(BaseMSBRegionPoint, MSBRegion):
    ENTRY_SUBTYPE = MSBRegionSubtype.Point


class MSBRegionCircle(BaseMSBRegionCircle, MSBRegion):
    ENTRY_SUBTYPE = MSBRegionSubtype.Circle


class MSBRegionSphere(BaseMSBRegionSphere, MSBRegion):
    ENTRY_SUBTYPE = MSBRegionSubtype.Sphere


class MSBRegionCylinder(BaseMSBRegionCylinder, MSBRegion):
    ENTRY_SUBTYPE = MSBRegionSubtype.Cylinder


class MSBRegionRect(BaseMSBRegionRect, MSBRegion):
    ENTRY_SUBTYPE = MSBRegionSubtype.Rect


class MSBRegionBox(BaseMSBRegionBox, MSBRegion):
    ENTRY_SUBTYPE = MSBRegionSubtype.Box


class MSBRegionList(MSBEntryList[MSBRegion]):
    INTERNAL_NAME = "POINT_PARAM_ST"
    ENTRY_LIST_NAME = "Regions"
    ENTRY_SUBTYPE_ENUM = MSBRegionSubtype

    SUBTYPE_CLASSES = {
        MSBRegionSubtype.Point: MSBRegionPoint,
        MSBRegionSubtype.Circle: MSBRegionCircle,
        MSBRegionSubtype.Sphere: MSBRegionSphere,
        MSBRegionSubtype.Cylinder: MSBRegionCylinder,
        MSBRegionSubtype.Rect: MSBRegionRect,
        MSBRegionSubtype.Box: MSBRegionBox,
    }
    SUBTYPE_OFFSET = 12

    _entries: list[MSBRegion]

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

    _entries: list[MSBRegion]

    @property
    def Points(self) -> GenericMSBEntryList[MSBRegionPoint]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBRegionPoint)])

    @property
    def Circles(self) -> GenericMSBEntryList[MSBRegionPoint]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBRegionCircle)])

    @property
    def Spheres(self) -> GenericMSBEntryList[MSBRegionPoint]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBRegionSphere)])

    @property
    def Cylinders(self) -> GenericMSBEntryList[MSBRegionPoint]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBRegionCylinder)])

    @property
    def Rectangles(self) -> GenericMSBEntryList[MSBRegionPoint]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBRegionRect)])

    @property
    def Boxes(self) -> GenericMSBEntryList[MSBRegionPoint]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBRegionBox)])
