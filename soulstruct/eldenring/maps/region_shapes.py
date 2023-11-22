"""Shape structs used, modularly, by Elden Ring regions.

TODO: Can move this into `base` submodule and use in all games (in earlier games, 'region subtype' is just shape type).
"""
from __future__ import annotations

__all__ = [
    "RegionShapeType",
    "BaseShape",
    "PointShape",
    "CircleShape",
    "SphereShape",
    "CylinderShape",
    "RectShape",
    "BoxShape",
    "CompositeShape",
    "SHAPE_TYPES",
]

import abc
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.base.maps.msb.utils import MSBBrokenEntryReference
from soulstruct.utilities.binary import BinaryStruct, BinaryReader, BinaryWriter

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.msb import MSBEntry
    from soulstruct.base.maps.msb.regions import BaseMSBRegion


class RegionShapeType(IntEnum):
    """The shape of a region (e.g. point, circle, box, etc.)."""
    Invalid = -1  # not permitted
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5
    Composite = 6


@dataclass(slots=True)
class BaseShape(abc.ABC):
    """Base class for all region shapes."""

    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Invalid
    DATA_STRUCT: tp.ClassVar[type[BinaryStruct]] = None

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader):
        if cls.DATA_STRUCT is not None:
            shape_data = cls.DATA_STRUCT.from_bytes(reader)
            # noinspection PyArgumentList
            return cls(**shape_data.to_dict())
        return cls()  # e.g. `PointShape`

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        """Base region and most subclasses have nothing to set."""
        pass

    def to_msb_writer(self, writer: BinaryWriter):
        """Write data, if any."""
        if self.DATA_STRUCT is not None:
            self.DATA_STRUCT.object_to_writer(self, writer)


@dataclass(slots=True)
class PointShape(BaseShape):
    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Point

    # No data.


@dataclass(slots=True)
class CircleShape(BaseShape):
    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Circle

    @dataclass(slots=True)
    class DATA_STRUCT(BinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True)
class SphereShape(BaseShape):
    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Sphere

    @dataclass(slots=True)
    class DATA_STRUCT(BinaryStruct):
        radius: float

    radius: float = 1.0


@dataclass(slots=True)
class CylinderShape(BaseShape):
    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Cylinder

    @dataclass(slots=True)
    class DATA_STRUCT(BinaryStruct):
        radius: float
        height: float

    radius: float = 1.0
    height: float = 1.0


@dataclass(slots=True)
class RectShape(BaseShape):
    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Rect

    @dataclass(slots=True)
    class DATA_STRUCT(BinaryStruct):
        width: float
        height: float

    width: float = 1.0
    height: float = 1.0


@dataclass(slots=True)
class BoxShape(BaseShape):
    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Box

    @dataclass(slots=True)
    class DATA_STRUCT(BinaryStruct):
        width: float
        height: float
        depth: float

    width: float = 1.0
    height: float = 1.0
    depth: float = 1.0


@dataclass(slots=True)
class CompositeShape(BaseShape):

    @dataclass(slots=True)
    class CompositeChild:
        """Composite shapes store up to eight references to other MSB regions."""

        _region_index: int | None
        region: BaseMSBRegion | None
        unk_x04: int

        @classmethod
        def from_msb_reader(cls, reader: BinaryReader):
            _region_index, unk_x04 = reader.unpack("ii")
            return cls(_region_index=_region_index, region=None, unk_x04=unk_x04)

        # TODO: Write method.

        def index_to_region(self, regions: list[BaseMSBRegion]):
            """Consume `_region_index` and set `region` to the corresponding entry in `regions` supertype list."""
            index = self._region_index
            try:
                entry = regions[index] if index != -1 else None
            except IndexError:
                entry = MSBBrokenEntryReference("POINT_PARAM_ST", index)
            self.region = entry
            self._region_index = None

    SHAPE_TYPE: tp.ClassVar[RegionShapeType] = RegionShapeType.Composite

    children: list[CompositeChild] = field(default_factory=lambda: [None] * 8)

    @classmethod
    def from_msb_reader(cls, reader):
        children = []
        for i in range(8):
            child = cls.CompositeChild.from_msb_reader(reader)
            children.append(child)

        return cls(children=children)

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        for child in self.children:
            # noinspection PyTypeChecker
            child.index_to_region(entry_lists["POINT_PARAM_ST"])


SHAPE_TYPES = {
    RegionShapeType.Point: PointShape,
    RegionShapeType.Circle: CircleShape,
    RegionShapeType.Sphere: SphereShape,
    RegionShapeType.Cylinder: CylinderShape,
    RegionShapeType.Rect: RectShape,
    RegionShapeType.Box: BoxShape,
    RegionShapeType.Composite: CompositeShape,
}
