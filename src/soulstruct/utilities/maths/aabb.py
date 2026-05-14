"""3D axis-aligned bounding box (AABB) class, storing min/max Vector3."""
from __future__ import annotations

__all__ = ["AABB"]

from dataclasses import dataclass

from .vector import Vector3


@dataclass(slots=True)
class AABB:

    min: Vector3
    max: Vector3

    @classmethod
    def invalid(cls) -> AABB:
        """Create an invalid AABB with min > max, using the max/min single-precision float values."""
        return cls(Vector3.single_max(), Vector3.single_min())

    def __repr__(self) -> str:
        return f"AABB(min={self.min}, max={self.max})"
