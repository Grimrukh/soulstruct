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
from soulstruct.utilities.binary_struct import BinaryStruct

from .msb_entry import MSBEntryList


class MSBRegion(_BaseMSBRegion, abc.ABC):

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

    Points: tp.Sequence[MSBRegionPoint]
    Circles: tp.Sequence[MSBRegionCircle]
    Spheres: tp.Sequence[MSBRegionSphere]
    Cylinders: tp.Sequence[MSBRegionCylinder]
    Rectangles: tp.Sequence[MSBRegionRect]
    Boxes: tp.Sequence[MSBRegionBox]

    new_point: tp.Callable[..., MSBRegionPoint]
    new_circle: tp.Callable[..., MSBRegionCircle]
    new_sphere: tp.Callable[..., MSBRegionSphere]
    new_cylinder: tp.Callable[..., MSBRegionCylinder]
    new_rect: tp.Callable[..., MSBRegionRect]
    new_box: tp.Callable[..., MSBRegionBox]
