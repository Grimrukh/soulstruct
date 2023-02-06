
__all__ = ["MapFieldInfo"]

from soulstruct.utilities.maths import Matrix3, Vector3, resolve_rotation

from .msb_entry import MSBEntry


def MapFieldInfo(display_name: str, description: str) -> dict[str, dict[str, str]]:
    """Convenience generator for use with ** in `field()`."""
    return {"metadata": {"display_name": display_name, "description": description}}


def rotate_entry(
    entry: MSBEntry, rotation: Matrix3 | Vector3 | list | tuple | int | float, pivot_point=(0, 0, 0), radians=False,
):
    """Modify entity `translate` and `rotate` by rotating entry around some `pivot_point` in world coordinates.

    Default `pivot_point` is the world origin (0, 0, 0). Default rotation units are degrees.
    """
    rotation = resolve_rotation(rotation, radians)
    pivot_point = Vector3(*pivot_point)
    entry.rotate = (rotation @ Matrix3.from_euler_angles(entry.rotate)).to_euler_angles()
    entry.translate = (rotation @ (entry.translate - pivot_point)) + pivot_point
