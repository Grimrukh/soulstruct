__all__ = ["BoundingBox", "BoundingBoxWithUnknown"]

from dataclasses import dataclass

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3


@dataclass(slots=True)
class BoundingBox(NewBinaryStruct):
    """Axis-aligned bounding box specified by `minimum` and `maximum` corners."""
    minimum: Vector3
    maximum: Vector3


@dataclass(slots=True)
class BoundingBoxWithUnknown(BoundingBox):
    """Used in Sekiro (and maybe afterward). Has an additional unknown `Vector3`."""
    unknown: Vector3
