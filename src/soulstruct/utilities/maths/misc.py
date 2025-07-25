from __future__ import annotations

__all__ = [
    "ROTATION_TYPING",
    "local_translate",
    "resolve_rotation",
    "get_distance",
]

import math
import typing as tp

from .matrix import Matrix3
from .vector import Vector3


# Valid rotation types for `resolve_rotation()` (`None` also allowed, which returns identity matrix).
ROTATION_TYPING = tp.Union[Matrix3 | Vector3 | list | tuple | int | float]


def local_translate(
    pos: Vector3, rot: ROTATION_TYPING, distance: float, local_axis: Vector3 = None, radians=False
) -> Vector3:
    """Slide given world-sapce `pos` vector by `distance` along `local_axis` vector, which defaults to -Z axis.

    `rot` is a rotation (in degrees by default) used to convert `axis` to world space.
    """
    rot_matrix = resolve_rotation(rot, radians=radians)
    if local_axis is None:
        local_axis = Vector3((0.0, 0.0, -1.0))  # standard 'forward-facing' direction of MSB entities
    if not isinstance(local_axis, Vector3):
        local_axis = Vector3(local_axis)
    local_axis = local_axis.normalize()
    if not isinstance(pos, Vector3):
        pos = Vector3(pos)
    if distance == 0.0:
        return pos
    # Rotate the axis vector by the rotation matrix and scale it by `distance`, then add it to `pos`.
    return pos + distance * (rot_matrix @ local_axis)


def resolve_rotation(rotation: ROTATION_TYPING | None, radians=False) -> Matrix3:
    """Return a rotation `Matrix3` from various shortcut input types (e.g. single value or Euler angle vector).

    `None` is returned as the identity matrix.
    """
    if rotation is None:
        return Matrix3.identity()
    elif isinstance(rotation, (int, float)):
        # Single rotation value is a shortcut for Y rotation (i.e. around vertical in-game axis).
        return Matrix3.from_euler_angles((0.0, rotation, 0.0), radians=radians)
    elif isinstance(rotation, (Vector3, list, tuple)):
        return Matrix3.from_euler_angles(rotation, radians=radians)
    elif isinstance(rotation, Matrix3):
        return rotation
    raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")


def get_distance(x1: Vector3, x2: Vector3, squared=False):
    """Get distance (or `squared` distance) between two `Vector3`-like objects."""
    if not isinstance(x1, Vector3):
        x1 = Vector3(x1)
    if not isinstance(x2, Vector3):
        x2 = Vector3(x2)
    squared_distance = (x2.x - x1.x) ** 2 + (x2.y - x1.y) ** 2 + (x2.z - x1.z) ** 2
    if squared:
        return squared_distance
    return math.sqrt(squared_distance)
