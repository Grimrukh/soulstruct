from __future__ import annotations

__all__ = [
    "MSBRegionShapeType",
    "MSBRegionShape",
    "MSBRegionPoint",
    "MSBRegionCircle",
    "MSBRegionSphere",
    "MSBRegionCylinder",
    "MSBRegionRect",
    "MSBRegionBox",
    "MSBRegionComposite",
]

import abc
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.base.maps.msb.utils import MSBBrokenEntryReference
from soulstruct.utilities.binary import *

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList
    from .regions import BaseMSBRegion
    from .core import MSBEntry


class MSBRegionShapeType(IntEnum):
    """Correct for most games, up until `Composite` added."""
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5
    Composite = 6  # not supported by older games


class MSBRegionShape(abc.ABC):
    """Shape structure for any `MSBRegion` entry."""
    SHAPE_TYPE: tp.ClassVar[IntEnum]
    SHAPE_DATA_STRUCT: tp.ClassVar[type[BinaryStruct]]

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        """Straightforward for basic shapes, which are basically just 1-3 float structs."""
        return cls.SHAPE_DATA_STRUCT.reader_to_object(reader, cls)

    def to_msb_writer(self, writer: BinaryWriter):
        self.SHAPE_DATA_STRUCT.object_to_writer(self, writer)


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionPoint(MSBRegionShape):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way the player
    will be facing when they spawn at or teleport to this point)."""

    SHAPE_TYPE = MSBRegionShapeType.Point

    SHAPE_DATA_STRUCT: tp.ClassVar = None  # no data


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionCircle(MSBRegionShape):
    """Almost never used (no volume)."""

    SHAPE_TYPE = MSBRegionShapeType.Circle

    @dataclass(slots=True)
    class SHAPE_DATA_STRUCT(BinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionSphere(MSBRegionShape):

    SHAPE_TYPE = MSBRegionShapeType.Sphere

    @dataclass(slots=True)
    class SHAPE_DATA_STRUCT(BinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionCylinder(MSBRegionShape):

    SHAPE_TYPE = MSBRegionShapeType.Cylinder

    @dataclass(slots=True)
    class SHAPE_DATA_STRUCT(BinaryStruct):
        radius: float
        height: float

    radius: float = 1.0
    height: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionRect(MSBRegionShape):
    """Almost never used (no volume)."""

    SHAPE_TYPE = MSBRegionShapeType.Rect

    @dataclass(slots=True)
    class SHAPE_DATA_STRUCT(BinaryStruct):
        width: float
        height: float

    width: float = 1.0
    height: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBRegionBox(MSBRegionShape):

    SHAPE_TYPE = MSBRegionShapeType.Box

    @dataclass(slots=True)
    class SHAPE_DATA_STRUCT(BinaryStruct):
        width: float
        depth: float
        height: float

    width: float = 1.0
    depth: float = 1.0
    height: float = 1.0


@dataclass(slots=True)
class MSBRegionComposite(MSBRegionShape):

    SHAPE_TYPE = MSBRegionShapeType.Composite

    @dataclass(slots=True)
    class SHAPE_DATA_STRUCT(BinaryStruct):
        """MSB global region indices and unknown values for eight different regions. -1 indices indicate unused."""
        region_0_index: int
        region_0_unk: int
        region_1_index: int
        region_1_unk: int
        region_2_index: int
        region_2_unk: int
        region_3_index: int
        region_3_unk: int
        region_4_index: int
        region_4_unk: int
        region_5_index: int
        region_5_unk: int
        region_6_index: int
        region_6_unk: int
        region_7_index: int
        region_7_unk: int

    region_indices: list[int] = field(default_factory=lambda: [-1] * 8)
    region_unks: list[int] = field(default_factory=lambda: [0] * 8)

    regions: list[BaseMSBRegion | None] = field(default_factory=lambda: [None] * 8)

    def indices_to_regions(self, entry_lists: dict[str, IDList[MSBEntry]], owner_region_name: str):
        regions_list = entry_lists["POINT_PARAM_ST"]
        self.regions = []
        for i in range(8):
            index = self.region_indices[i]
            if index == -2:
                raise ValueError(
                    f"Composite shape region index '{i}' in MSB region '{owner_region_name}' is stale (-2). "
                    f"Cannot reference child Region.")
            if index == -1:
                region = None
            else:
                try:
                    region = regions_list[index]
                except IndexError:
                    region = MSBBrokenEntryReference("POINT_PARAM_ST", index)
            self.regions.append(region)

    def regions_to_indices(self, entry_lists: dict[str, IDList[MSBEntry]], owner_region_name: str):
        regions_list = entry_lists["POINT_PARAM_ST"]
        self.region_indices = []
        for i in range(8):
            region = self.regions[i]
            if region is None:
                index = -1
            else:
                try:
                    index = regions_list.index(region)  # by true instance ID in `IDList`
                except ValueError:
                    raise ValueError(
                        f"Composite shape region '{owner_region_name}' references region '{region.name}', but this "
                        f"region instance does not appear in given MSB regions."
                    )
            self.region_indices.append(index)

    def set_region(self, index: int, region: BaseMSBRegion, unk: int = 0):
        """Shortcut for setting composite sub-region of given index."""
        if not 0 <= index < 8:
            raise ValueError("Composite region index must be between 0 and 7.")
        self.regions[index] = region
        self.region_indices[index] = -2  # indicates stale
        self.region_unks[index] = unk
