__all__ = [
    "MSBRegion",
    "MSBRegionPoint",
    "MSBRegionCircle",
    "MSBRegionSphere",
    "MSBRegionCylinder",
    "MSBRegionRect",
    "MSBRegionBox",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.regions import *
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import MSBRegionSubtype


@dataclass(slots=True)
class RegionHeader(NewBinaryStruct):
    name_offset: int
    _pad1: bytes = field(init=False, **BinaryPad(4))
    _region_index: int
    region_type: int
    translate: Vector3
    rotate: Vector3  # Euler angles in radians
    _pad2: bytes = field(init=False, **BinaryPad(4))
    unknown_offset_1: int
    unknown_offset_2: int
    subtype_data_offset: int
    entity_id_offset: int


@dataclass(slots=True)
class MSBRegion(BaseMSBRegion, abc.ABC):

    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[tp.Type[NewBinaryStruct]] = RegionHeader
    NAME_ENCODING = "shift_jis_2004"
    UNKNOWN_DATA_SIZE = 4


@dataclass(slots=True)
class MSBRegionPoint(BaseMSBRegion):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way the player
    will be facing when they spawn at or teleport to this point)."""

    SUBTYPE_ENUM = MSBRegionSubtype.Point

    SUBTYPE_DATA_STRUCT: tp.ClassVar = None


@dataclass(slots=True)
class MSBRegionCircle(BaseMSBRegion):
    """Almost never used (no volume)."""

    SUBTYPE_ENUM = MSBRegionSubtype.Circle

    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True)
class MSBRegionSphere(BaseMSBRegion):

    SUBTYPE_ENUM = MSBRegionSubtype.Sphere

    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True)
class MSBRegionCylinder(BaseMSBRegion):

    SUBTYPE_ENUM = MSBRegionSubtype.Cylinder

    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        radius: float
        height: float

    radius: float = 1.0
    height: float = 1.0


@dataclass(slots=True)
class MSBRegionRect(BaseMSBRegion):
    """Almost never used (no volume)."""

    SUBTYPE_ENUM = MSBRegionSubtype.Rect

    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        width: float
        height: float

    width: float = 1.0
    height: float = 1.0


@dataclass(slots=True)
class MSBRegionBox(BaseMSBRegion):

    SUBTYPE_ENUM = MSBRegionSubtype.Box

    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        width: float
        depth: float
        height: float

    width: float = 1.0
    depth: float = 1.0
    height: float = 1.0
