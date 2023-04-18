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
class RegionHeader(BinaryStruct):
    name_offset: int
    _pad1: bytes = field(init=False, **BinaryPad(4))
    _supertype_index: int
    _subtype_int: int
    translate: Vector3
    rotate: Vector3  # Euler angles in radians
    unknown_offset_1: int
    unknown_offset_2: int
    subtype_data_offset: int
    entity_id_offset: int
    _pad2: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBRegion(BaseMSBRegion, abc.ABC):

    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[tp.Type[BinaryStruct]] = RegionHeader
    NAME_ENCODING = "shift_jis_2004"
    UNKNOWN_DATA_SIZE = 4


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionPoint(MSBRegion):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way the player
    will be facing when they spawn at or teleport to this point)."""

    SUBTYPE_ENUM = MSBRegionSubtype.Point

    SUBTYPE_DATA_STRUCT: tp.ClassVar = None


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionCircle(MSBRegion):
    """Almost never used (no volume)."""

    SUBTYPE_ENUM = MSBRegionSubtype.Circle

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionSphere(MSBRegion):

    SUBTYPE_ENUM = MSBRegionSubtype.Sphere

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionCylinder(MSBRegion):

    SUBTYPE_ENUM = MSBRegionSubtype.Cylinder

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        radius: float
        height: float

    radius: float = 1.0
    height: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionRect(MSBRegion):
    """Almost never used (no volume)."""

    SUBTYPE_ENUM = MSBRegionSubtype.Rect

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        width: float
        height: float

    width: float = 1.0
    height: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionBox(MSBRegion):

    SUBTYPE_ENUM = MSBRegionSubtype.Box

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        width: float
        depth: float
        height: float

    width: float = 1.0
    depth: float = 1.0
    height: float = 1.0
