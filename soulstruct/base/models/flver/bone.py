import io

from soulstruct.utilities import read_chars_from_buffer
from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject, BinaryWriter
from soulstruct.utilities.maths import Vector3


class Bone(BinaryObject):

    STRUCT = BinaryStruct(
        ("translate", "3f"),
        ("__name_offset", "i"),
        ("rotate", "3f"),
        ("parent_index", "h"),
        ("child_index", "h"),
        ("scale", "3f"),
        ("next_sibling_index", "h"),
        ("previous_sibling_index", "h"),
        ("bounding_box_min", "3f"),
        ("unk_x3c", "i"),
        ("bounding_box_max", "3f"),
        "52x",
    )

    translate: Vector3
    name: str
    rotate: Vector3
    parent_index: int
    child_index: int
    scale: Vector3
    next_sibling_index: int
    previous_sibling_index: int
    bounding_box_min: Vector3
    unk_x3c: int
    bounding_box_max: Vector3

    def unpack(self, buffer: io.BufferedIOBase, unicode=None):
        data = self.STRUCT.unpack(buffer)
        encoding = "utf-16-le" if unicode else "shift_jis_2004"
        self.name = read_chars_from_buffer(buffer, offset=data.pop("__name_offset"), encoding=encoding)
        self.set(**data)

    def pack_writer(self, writer: BinaryWriter, bone_index: int):
        writer.pack_struct(
            self.STRUCT,
            self,
            __name_offset=writer.Reserved(f"BoneNameOffset{bone_index}"),
        )
