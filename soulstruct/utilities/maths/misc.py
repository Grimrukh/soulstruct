from __future__ import annotations

__all__ = [
    "shift_msb_coordinates",
    "shift",
    "resolve_rotation",
    "get_distance",
]

import math
import typing as tp

if tp.TYPE_CHECKING:
    from .matrix import Matrix3
    from .vector import Vector3


def shift_msb_coordinates(distance: float, translate=(0.0, 0.0, 0.0), ry=0.0):
    """Shift an MSB entity forward (if `distance > 0` or backward (if `distance < 0`)."""
    ry_rad = math.radians(ry)
    delta_x = -distance * math.sin(ry_rad)
    delta_z = -distance * math.cos(ry_rad)
    return translate[0] + delta_x, translate[1], translate[2] + delta_z


def shift(rel_x, rel_z, origin=(0, 0), rotation=0):
    rot_rad = math.radians(rotation)
    r, th = math.hypot(rel_x, rel_z), math.atan2(rel_z, rel_x)
    th += rot_rad
    dx, dz = r * -math.sin(th), r * -math.cos(th)
    return origin[0] + dx, origin[1] + dz


def resolve_rotation(rotation: Matrix3 | Vector3 | list | tuple | int | float, radians=False) -> Matrix3:
    """Return a rotation `Matrix3` from various shortcut input types (e.g. single value or Euler angle vector)."""
    if isinstance(rotation, (int, float)):
        # Single rotation value is a shortcut for Y rotation (i.e. around vertical in-game axis).
        return Matrix3.from_euler_angles(0.0, rotation, 0.0, radians=radians)
    elif isinstance(rotation, (Vector3, list, tuple)):
        return Matrix3.from_euler_angles(rotation, radians=radians)
    elif isinstance(rotation, Matrix3):
        return rotation
    raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")


def get_distance(x1: Vector3, x2: Vector3, squared=False):
    if not isinstance(x1, Vector3):
        x1 = Vector3(x1)
    if not isinstance(x2, Vector3):
        x2 = Vector3(x2)
    squared_distance = (x2.x - x1.x) ** 2 + (x2.y - x1.y) ** 2 + (x2.z - x1.z) ** 2
    if squared:
        return squared_distance
    return math.sqrt(squared_distance)
