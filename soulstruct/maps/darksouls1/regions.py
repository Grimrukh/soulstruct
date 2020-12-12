import abc
from soulstruct.maps.base.regions import (
    MSBRegion as BaseMSBRegion,
    MSBRegionPoint as BaseMSBRegionPoint,
    MSBRegionCircle as BaseMSBRegionCircle,
    MSBRegionSphere as BaseMSBRegionSphere,
    MSBRegionCylinder as BaseMSBRegionCylinder,
    MSBRegionRect as BaseMSBRegionRect,
    MSBRegionBox as BaseMSBRegionBox,
    MSBRegionList as BaseMSBRegionList,
)
from soulstruct.maps.enums import MSBRegionSubtype
from soulstruct.utilities import BinaryStruct


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

    ENCODING = "shift-jis"
    UNKNOWN_DATA_SIZE = 4


class MSBRegionPoint(BaseMSBRegionPoint, MSBRegion):
    pass


class MSBRegionCircle(BaseMSBRegionCircle, MSBRegion):
    pass


class MSBRegionSphere(BaseMSBRegionSphere, MSBRegion):
    pass


class MSBRegionCylinder(BaseMSBRegionCylinder, MSBRegion):
    pass


class MSBRegionRect(BaseMSBRegionRect, MSBRegion):
    pass


class MSBRegionBox(BaseMSBRegionBox, MSBRegion):
    pass


class MSBRegionList(BaseMSBRegionList):
    REGION_SUBTYPE_CLASSES = {
        MSBRegionSubtype.Point: MSBRegionPoint,
        MSBRegionSubtype.Circle: MSBRegionCircle,
        MSBRegionSubtype.Sphere: MSBRegionSphere,
        MSBRegionSubtype.Cylinder: MSBRegionCylinder,
        MSBRegionSubtype.Rect: MSBRegionRect,
        MSBRegionSubtype.Box: MSBRegionBox,
    }
    REGION_SUBTYPE_OFFSET = 12


for _entry_subtype in MSBRegionSubtype:
    setattr(
        MSBRegionList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
