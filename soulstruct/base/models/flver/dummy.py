"""NOTE: This file is Python 3.9 compatible for Blender 3.X use."""

__all__ = ["Dummy"]

from soulstruct.base.models.color import ColorRGBA8
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader, BinaryWriter
from soulstruct.utilities.maths import Vector3


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
    color: ColorRGBA8
    forward: Vector3
    reference_id: int
    parent_bone_index: int
    upward: Vector3
    attach_bone_index: int
    flag_1: bool
    use_upward_vector: bool
    unk_x30: int
    unk_x34: int

    def unpack(self, reader: BinaryReader, color_is_argb=None):
        if color_is_argb is None:
            raise ValueError("`color_is_argb` (bool) must be given to `Dummy.unpack()`.")
        data = reader.unpack_struct(self.STRUCT)
        if color_is_argb:
            alpha, red, green, blue = data.pop("__color")
        else:
            blue, green, red, alpha = data.pop("__color")
        self.color = ColorRGBA8(red, green, blue, alpha)
        self.set(**data)

    def pack(self, writer: BinaryWriter, color_is_argb: bool):
        """Nothing to reserve."""
        if color_is_argb:
            color = (self.color.alpha, self.color.red, self.color.green, self.color.blue)
        else:
            color = (self.color.blue, self.color.green, self.color.red, self.color.alpha)
        writer.pack_struct(self.STRUCT, self, __color=color)

    def __repr__(self) -> str:
        return (
            f"Dummy(\n"
            f"    position={self.position}\n"
            f"    color={self.color}\n"
            f"    forward={self.forward}\n"
            f"    reference_id={self.reference_id}\n"
            f"    parent_bone_index={self.parent_bone_index}\n"
            f"    upward={self.upward}\n"
            f"    attach_bone_index={self.attach_bone_index}\n"
            f"    flag_1={self.flag_1}\n"
            f"    use_upward_vector={self.use_upward_vector}\n"
            f"    unk_x30={self.unk_x30}\n"
            f"    unk_x34={self.unk_x34}\n"
            f")"
        )
