"""Additional complex Composite shape used by Elden Ring regions."""
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

import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.base.maps.msb.region_shapes import *
from soulstruct.base.maps.msb.utils import MSBBrokenEntryReference
from soulstruct.utilities.binary import BinaryStruct
from soulstruct.utilities.misc import IDList

if tp.TYPE_CHECKING:
    from .regions import MSBRegion


class MSBRegionShapeType(IntEnum):
    """Adds `Composite` value."""
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 3
    Rect = 4
    Box = 5
    Composite = 6
