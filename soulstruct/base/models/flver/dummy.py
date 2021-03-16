import io

from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject
from soulstruct.utilities.maths import Vector3

from .color import Color


class Dummy(BinaryObject):

    STRUCT = BinaryStruct(
        ("position", "3f"),
        ("__color", "4B"),
        ("forward", "3f"),
        ("reference_id", "h"),
        ("parent_bone_index", "h"),
        ("upward", "3f"),
        ("attach_bone_index", "h"),
        ("flag_1", "?"),
        ("use_upward_vector", "?"),
        ("unk_x30", "i"),
        ("unk_x34", "i"),
        "8x",
    )

    position: Vector3
    color: Color
    forward: Vector3
    reference_id: int
    parent_bone_index: int
    upward: Vector3
    attach_bone_index: int
    flag_1: bool
    use_upward_vector: bool
    unk_x30: int
    unk_x34: int

    def unpack(self, buffer: io.BufferedIOBase, color_is_argb=None):
        if color_is_argb is None:
            raise ValueError("`color_is_argb` (bool) must be given to `Dummy.unpack()`.")
        data = self.STRUCT.unpack(buffer)
        color = data.pop("__color")
        self.color = (Color.from_argb if color_is_argb else Color.from_bgra)(*color)
        self.set(**data)
