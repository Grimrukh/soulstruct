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

from soulstruct.maps.base.regions import (
    MSBRegion as _BaseMSBRegion,
    MSBRegionPoint as _BaseMSBRegionPoint,
    MSBRegionCircle as _BaseMSBRegionCircle,
    MSBRegionSphere as _BaseMSBRegionSphere,
    MSBRegionCylinder as _BaseMSBRegionCylinder,
    MSBRegionRect as _BaseMSBRegionRect,
    MSBRegionBox as _BaseMSBRegionBox,
    MSBRegionList as _BaseMSBRegionList,
)
from soulstruct.maps.enums import MSBRegionSubtype
from soulstruct.utilities import BinaryStruct

from .msb_entry import MSBEntryList


class MSBRegion(_BaseMSBRegion, abc.ABC):

    REGION_STRUCT = BinaryStruct(
        ("name_offset", "q"),
        "4x",
        ("__region_index", "i"),
        ("region_type", "i"),
        ("translate", "3f"),
        ("rotate", "3f"),  # These are Euler angle rotations (and can therefore be gimbal-locked).
        "4x",
        ("unknown_offset_1", "q"),
        ("unknown_offset_2", "q"),
        ("type_data_offset", "q"),
        ("entity_id_offset", "q"),
    )

    NAME_ENCODING = "utf-16-le"
    UNKNOWN_DATA_SIZE = 2


class MSBRegionPoint(_BaseMSBRegionPoint, MSBRegion):
    pass


class MSBRegionCircle(_BaseMSBRegionCircle, MSBRegion):
    pass


class MSBRegionSphere(_BaseMSBRegionSphere, MSBRegion):
    pass


class MSBRegionCylinder(_BaseMSBRegionCylinder, MSBRegion):
    pass


class MSBRegionRect(_BaseMSBRegionRect, MSBRegion):
    pass


class MSBRegionBox(_BaseMSBRegionBox, MSBRegion):
    pass


class MSBRegionList(_BaseMSBRegionList, MSBEntryList):
    REGION_SUBTYPE_CLASSES = {
        MSBRegionSubtype.Point: MSBRegionPoint,
        MSBRegionSubtype.Circle: MSBRegionCircle,
        MSBRegionSubtype.Sphere: MSBRegionSphere,
        MSBRegionSubtype.Cylinder: MSBRegionCylinder,
        MSBRegionSubtype.Rect: MSBRegionRect,
        MSBRegionSubtype.Box: MSBRegionBox,
    }
    REGION_SUBTYPE_OFFSET = 16


for _entry_subtype in MSBRegionSubtype:
    setattr(
        MSBRegionList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
