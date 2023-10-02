__all__ = ["BoundingBox", "BoundingBoxWithUnknown"]

from dataclasses import dataclass

import numpy as np

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3


@dataclass(slots=True)
class BoundingBox(BinaryStruct):
    """Axis-aligned bounding box specified by `minimum` and `maximum` corners."""
    minimum: Vector3
    maximum: Vector3

    @classmethod
    def from_vertex_positions(cls, positions: np.ndarray):
        return cls(
            minimum=Vector3(positions.min(axis=0)),
            maximum=Vector3(positions.max(axis=0)),
        )


@dataclass(slots=True)
class BoundingBoxWithUnknown(BoundingBox):
    """Used in Sekiro (and maybe afterward). Has an additional unknown `Vector3`."""
    unknown: Vector3
