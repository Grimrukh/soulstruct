__all__ = ["BoundingBox", "BoundingBoxWithUnknown"]

from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject
from soulstruct.utilities.maths import Vector3


class BoundingBox(BinaryObject):
    """Axis-aligned bounding box specified by `minimum` and `maximum` corners."""

    STRUCT = BinaryStruct(
        ("minimum", "3f"),
        ("maximum", "3f"),
    )

    minimum: Vector3
    maximum: Vector3

    def __repr__(self):
        return f"BoundingBox(minimum={tuple(self.minimum)}, maximum={tuple(self.maximum)})"


class BoundingBoxWithUnknown(BoundingBox):
    """Used in Sekiro. Has an additional unknown `Vector3`."""

    STRUCT = BinaryStruct(
        ("minimum", "3f"),
        ("maximum", "3f"),
        ("unknown", "3f"),
    )

    minimum: Vector3
    maximum: Vector3
    unknown: Vector3

    def __repr__(self):
        return (
            f"BoundingBoxWithUnknown("
            f"minimum={tuple(self.minimum)}, maximum={tuple(self.maximum)}, unknown={tuple(self.unknown)}"
            f")"
        )
