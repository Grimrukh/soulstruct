from __future__ import annotations

__all__ = [
    "FLVERBoneUsageFlags",
    "FLVERBone",
]

from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import AABB, EulerRad, Vector3


class FLVERBoneUsageFlags(IntEnum):
    """Bit flags used in `FLVERBone.usage_flags`, which indicate whether/how the bone is used in the FLVER."""

    # Used bones have no flags (0).
    UNUSED = 0b0001  # 1
    # TODO: Flags below only started being used at some point after DS1.
    DUMMY = 0b0010  # 2
    cXXXX = 0b0100  # 4  # TODO: references another skeleton...?
    MESH = 0b1000  # 8


@dataclass(slots=True)
class FLVERBone:
    """Bone in a FLVER model. Named to distinguish it from Havok `Bone` in my `soulstruct-havok` package."""

    class STRUCT(BinaryStruct):
        translate: Vector3
        _name_offset: int
        rotate: EulerRad
        parent_bone_index: short
        child_bone_index: short
        scale: Vector3
        next_sibling_bone_index: short
        previous_sibling_bone_index: short
        bounding_box_min: Vector3
        usage_flags: int
        bounding_box_max: Vector3
        _pad1: bytes = binary_pad(52, init=False)

    name: str
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: EulerRad = field(default_factory=EulerRad.zero)
    scale: Vector3 = field(default_factory=Vector3.one)
    # Mesh vertices weighted to this bone will only be drawn if this bounding box is in the camera's current view.
    # NOTE: units are in local bone space for character
    bounding_box: AABB = field(default_factory=AABB.invalid)
    usage_flags: int = 0
    parent_bone_index: int = -1
    child_bone_index: int = -1  # first child (has no previous sibling)
    next_sibling_bone_index: int = -1
    previous_sibling_bone_index: int = -1

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str) -> FLVERBone:
        """Returns `FLVERBone` instance without dereferenced connected bones."""
        bone_struct = cls.STRUCT.from_bytes(reader)
        name = reader.unpack_string(offset=bone_struct.pop("_name_offset"), encoding=encoding)
        flver_bone = bone_struct.to_object(cls, name=name)  # connected bone indices included
        return flver_bone

    def to_flver_writer(self, writer: BinaryWriter):
        """Write this `FLVERBone` into FLVER `writer`.

        Full list of FLVER `bones` is required to get the indices of referenced bones (parent, child, siblings).
        """

        self.STRUCT.object_to_writer(
            self,
            writer,
            _name_offset=None,
            bounding_box_min=self.bounding_box.min,
            bounding_box_max=self.bounding_box.max,
        )

    def pack_name(self, writer: BinaryWriter, encoding: str):
        writer.fill_with_position("_name_offset", obj=self)
        writer.pack_z_string(self.name, encoding)

    def __eq__(self, other: FLVERBone):
        """Checks the names of connected bones if set, or their indices if not."""
        if not isinstance(other, FLVERBone):
            return False
        if not all(
            [
                self.name == other.name,
                self.translate == other.translate,
                self.rotate == other.rotate,
                self.scale == other.scale,
                self.bounding_box == other.bounding_box,
                self.usage_flags == other.usage_flags,
            ]
        ):
            return False
        for connection_name in ("parent", "child", "next_sibling", "previous_sibling"):
            ref_bone = getattr(self, f"{connection_name}_bone")
            other_ref_bone = getattr(other, f"{connection_name}_bone")
            if ref_bone is None and other_ref_bone is None:
                if getattr(self, f"_{connection_name}_bone_index") != getattr(other, f"_{connection_name}_bone_index"):
                    return False
            elif ref_bone is None or other_ref_bone is None:
                return False
            elif ref_bone.name != other_ref_bone.name:
                return False
        return True

    def __repr__(self):
        lines = [
            f"FLVERBone(\n"
            f"  name = {repr(self.name)}",
            f"  translate = {self.translate}",
            f"  rotate = {self.rotate}",
        ]
        if not self.scale == Vector3.one():
            lines.append(f"  scale = {self.scale}")
        if self.parent_bone_index != -1:
            lines.append(f"  parent_bone_index = {self.parent_bone_index}'")
        if self.child_bone_index != -1:
            lines.append(f"  child_bone_index = {self.child_bone_index}'")
        if self.previous_sibling_bone_index != -1:
            lines.append(f"  previous_sibling_bone_index = {self.previous_sibling_bone_index}'")
        if self.next_sibling_bone_index != -1:
            lines.append(f"  next_sibling_bone_index = {self.next_sibling_bone_index}'")

        lines.append(f"  bounding_box = {self.bounding_box}")
        if self.usage_flags != 0:
            flags = " | ".join(
                [flag.name for flag in FLVERBoneUsageFlags if self.usage_flags & flag]
            )
            lines.append(f"  usage_flags = {self.usage_flags} ({flags})")
        lines.append(")")
        return "\n".join(lines)
