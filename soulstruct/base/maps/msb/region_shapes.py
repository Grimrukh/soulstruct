from __future__ import annotations

__all__ = [
    "RegionShapeType",
    "RegionShape",
    "PointShape",
    "CircleShape",
    "SphereShape",
    "CylinderShape",
    "RectShape",
    "BoxShape",
    "CompositeShape",
    "SHAPE_TYPE_CLASSES",
]

import abc
import typing as tp
from dataclasses import dataclass, field, fields
from enum import IntEnum

from soulstruct.base.maps.msb.utils import MSBBrokenEntryReference
from soulstruct.utilities.binary import *

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList
    from .regions import BaseMSBRegion
    from .core import MSBEntry


class RegionShapeType(IntEnum):
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5
    Composite = 6  # not supported by older games

    @classmethod
    def get_volume_types(cls) -> set[RegionShapeType]:
        return {cls.Sphere, cls.Cylinder, cls.Box}

    @classmethod
    def get_2d_types(cls) -> set[RegionShapeType]:
        """I have never seen these used even once in any FromSoftware game."""
        return {cls.Circle, cls.Rect}


@dataclass(slots=True)
class RegionShape(abc.ABC):
    """Shape structure for any `MSBRegion` entry."""
    SHAPE_TYPE: tp.ClassVar[RegionShapeType]
    SHAPE_FIELDS: tp.ClassVar[tuple[str]]
    SHAPE_DIMS: tp.ClassVar[str]  # up to three characters corresponding to internal 'XYZ' dimensions

    @classmethod
    @abc.abstractmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        """Straightforward for basic shapes, which are basically just 1-3 float structs."""
        ...

    @abc.abstractmethod
    def to_msb_writer(self, writer: BinaryWriter):
        """Straightforward for basic shapes, which are basically just 1-3 float structs."""
        ...

    @classmethod
    def from_json_dict(cls, json_dict: dict[str, str | float]):
        if "shape_type" in json_dict:
            if json_dict["shape_type"] != cls.SHAPE_TYPE.name.capitalize():
                raise ValueError(
                    f"JSON object shape type '{json_dict['shape_type']}' does not match this "
                    f"`RegionShape` class '{cls.__name__}' ({cls.SHAPE_TYPE.name})."
                )
        json_dict = {k: v for k, v in json_dict.items() if k != "shape_type"}
        # noinspection PyArgumentList
        return cls(**json_dict)

    def to_json_dict(self) -> dict[str, str | float]:
        return {
            "shape_type": self.SHAPE_TYPE.name,
            **{f.name: getattr(self, f.name) for f in fields(self)},
        }

    @abc.abstractmethod
    def get_three_dimensions(self) -> tuple[float, float, float]:
        """Get three dimensions for porting to other shape types."""

    @abc.abstractmethod
    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        """Set up to three dimensions from other shape types."""


@dataclass(slots=True)
class PointShape(RegionShape):
    """No shape attributes. Note that the MSB region's `rotate` attribute is still meaningful for many uses (e.g. what
    way the player will be facing when they spawn at or teleport to this point)."""

    SHAPE_TYPE = RegionShapeType.Point
    SHAPE_FIELDS = ()
    SHAPE_DIMS = ""

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        """No data in this shape."""
        return cls()

    def to_msb_writer(self, writer: BinaryWriter):
        """No data in this shape."""
        pass

    def get_three_dimensions(self) -> tuple[float, float, float]:
        return 1.0, 1.0, 1.0

    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        pass


@dataclass(slots=True)
class CircleShape(RegionShape):
    """Almost never used (no volume)."""

    SHAPE_TYPE = RegionShapeType.Circle
    SHAPE_FIELDS = ("radius",)
    SHAPE_DIMS = "R"

    radius: float = 1.0

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        radius = reader["f"]
        return cls(radius)

    def to_msb_writer(self, writer: BinaryWriter):
        writer.pack("f", self.radius)

    def get_three_dimensions(self) -> tuple[float, float, float]:
        return self.radius, self.radius, self.radius

    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        self.radius = dimensions[0]

    @property
    def R(self):
        return self.radius

    @R.setter
    def R(self, value):
        self.radius = value


@dataclass(slots=True)
class SphereShape(RegionShape):

    SHAPE_TYPE = RegionShapeType.Sphere
    SHAPE_FIELDS = ("radius",)
    SHAPE_DIMS = "R"

    radius: float = 1.0

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        radius = reader["f"]
        return cls(radius)

    def to_msb_writer(self, writer: BinaryWriter):
        writer.pack("f", self.radius)

    def get_three_dimensions(self) -> tuple[float, float, float]:
        return self.radius, self.radius, self.radius

    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        self.radius = dimensions[0]

    @property
    def R(self):
        return self.radius

    @R.setter
    def R(self, value):
        self.radius = value


@dataclass(slots=True)
class CylinderShape(RegionShape):

    SHAPE_TYPE = RegionShapeType.Cylinder
    SHAPE_FIELDS = ("radius", "height")
    SHAPE_DIMS = "RH"

    radius: float = 1.0
    height: float = 1.0

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        radius = reader["f"]
        height = reader["f"]
        return cls(radius, height)

    def to_msb_writer(self, writer: BinaryWriter):
        writer.pack("f", self.radius)
        writer.pack("f", self.height)

    def get_three_dimensions(self) -> tuple[float, float, float]:
        return self.radius, self.height, self.radius

    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        self.radius, self.height = dimensions[0], dimensions[1]

    @property
    def R(self):
        return self.radius

    @R.setter
    def R(self, value):
        self.radius = value

    @property
    def H(self):
        return self.height

    @H.setter
    def H(self, value):
        self.height = value


@dataclass(slots=True)
class RectShape(RegionShape):
    """Almost never used (no volume)."""

    SHAPE_TYPE = RegionShapeType.Rect
    SHAPE_FIELDS = ("width", "depth")
    SHAPE_DIMS = "W D"

    width: float = 1.0
    depth: float = 1.0

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        width = reader["f"]
        depth = reader["f"]
        return cls(width, depth)

    def to_msb_writer(self, writer: BinaryWriter):
        writer.pack("f", self.width)
        writer.pack("f", self.depth)

    def get_three_dimensions(self) -> tuple[float, float, float]:
        return self.width, self.width, self.depth

    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        self.width, self.depth = dimensions[0], dimensions[2]

    @property
    def W(self):
        return self.width

    @W.setter
    def W(self, value):
        self.width = value

    @property
    def D(self):
        return self.depth

    @D.setter
    def D(self, value):
        self.depth = value


@dataclass(slots=True)
class BoxShape(RegionShape):

    SHAPE_TYPE = RegionShapeType.Box
    SHAPE_FIELDS = ("width", "depth", "height")
    SHAPE_DIMS = "WHD"

    width: float = 1.0  # game X
    depth: float = 1.0  # game Z
    height: float = 1.0  # game Y

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        """NOTE: These dimensions are indeed in XZY order, not XYZ."""
        width = reader["f"]
        depth = reader["f"]
        height = reader["f"]
        return cls(width, depth, height)

    def to_msb_writer(self, writer: BinaryWriter):
        """NOTE: These dimensions are indeed in XZY order, not XYZ."""
        writer.pack("f", self.width)
        writer.pack("f", self.depth)
        writer.pack("f", self.height)

    def get_three_dimensions(self) -> tuple[float, float, float]:
        return self.width, self.height, self.depth

    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        self.width, self.height, self.depth = dimensions[0], dimensions[1], dimensions[2]

    @property
    def W(self):
        return self.width

    @W.setter
    def W(self, value: float):
        self.width = value

    @property
    def H(self):
        return self.height

    @H.setter
    def H(self, value: float):
        self.height = value

    @property
    def D(self):
        return self.depth

    @D.setter
    def D(self, value: float):
        self.depth = value


@dataclass(slots=True)
class CompositeShape(RegionShape):

    SHAPE_TYPE = RegionShapeType.Composite
    SHAPE_FIELDS = ()
    SHAPE_DIMS = ""

    region_indices: list[int] = field(default_factory=lambda: [-1] * 8)
    region_unks: list[int] = field(default_factory=lambda: [0] * 8)  # TODO: is this the right default?

    regions: list[BaseMSBRegion | None] = field(default_factory=lambda: [None] * 8)

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> tp.Self:
        """Eight pairs of region index and unknown value. -1 index indicates unused child region."""
        region_indices = []
        region_unks = []
        for i in range(8):
            region_indices.append(reader["i"])
            region_unks.append(reader["i"])
        return cls(region_indices, region_unks)

    def to_msb_writer(self, writer: BinaryWriter):
        """Eight pairs of region index and unknown value. -1 index indicates unused child region."""
        for i in range(8):
            writer.pack("i", self.region_indices[i])
            writer.pack("i", self.region_unks[i])

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

    def get_three_dimensions(self) -> tuple[float, float, float]:
        """Not compatible."""
        raise ValueError("Composite shapes do not have dimensions to get.")

    def set_three_dimensions(self, dimensions: tuple[float, float, float]):
        """Not compatible."""
        raise ValueError("Composite shapes do not have dimensions to set.")


# For JSON mostly.
SHAPE_TYPE_CLASSES = {
    RegionShapeType.Point: PointShape,
    RegionShapeType.Circle: CircleShape,
    RegionShapeType.Sphere: SphereShape,
    RegionShapeType.Cylinder: CylinderShape,
    RegionShapeType.Rect: RectShape,
    RegionShapeType.Box: BoxShape,
    RegionShapeType.Composite: CompositeShape,
}
