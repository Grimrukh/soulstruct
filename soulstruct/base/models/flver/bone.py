from __future__ import annotations

__all__ = ["Bone"]

import typing as tp

from soulstruct.utilities.binary import BinaryStruct, BinaryObject
from soulstruct.utilities.maths import Vector3, Matrix3


class Bone(BinaryObject):

    STRUCT = BinaryStruct(
        ("translate", "3f"),
        ("__name__z", "i"),
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

    unpack = BinaryObject.default_unpack
    pack = BinaryObject.default_pack

    def get_parent(self, bones: list[Bone]) -> tp.Optional[Bone]:
        if self.parent_index != -1:
            return bones[self.parent_index]
        return None

    def get_all_parents(self, bones: list[Bone]) -> list[Bone]:
        """Get all parents, from the highest to this Bone."""
        parents = [self]
        bone = self
        while bone.parent_index != -1:
            bone = bones[bone.parent_index]
            parents.append(bone)
        return list(reversed(parents))

    def get_child(self, bones: list[Bone]) -> tp.Optional[Bone]:
        if self.child_index != -1:
            return bones[self.child_index]
        return None

    def get_next_sibling(self, bones: list[Bone]) -> tp.Optional[Bone]:
        if self.next_sibling_index != -1:
            return bones[self.next_sibling_index]
        return None

    def get_previous_sibling(self, bones: list[Bone]) -> tp.Optional[Bone]:
        if self.previous_sibling_index != -1:
            return bones[self.previous_sibling_index]
        return None

    def get_absolute_translate(self, bones: list[Bone]) -> Vector3:
        """Accumulates parents' translates and rotates."""
        absolute_translate = Vector3.zero()
        rotate = Matrix3.identity()
        for bone in self.get_all_parents(bones):
            absolute_translate += rotate @ bone.translate
            rotate @= Matrix3.from_euler_angles(bone.rotate, radians=True)
        return absolute_translate

    def get_vector_in_world_space(self, bones: list[Bone], v: Vector3) -> Vector3:
        """Accumulates parents' rotations and applies them all to given vector `v`."""
        rotate = Matrix3.identity()
        for bone in self.get_all_parents(bones):
            rotate @= Matrix3.from_euler_angles(bone.rotate, radians=True)
        return rotate @ v

    def __repr__(self):
        lines = [
            f"Bone(\n"
            f"  name = {repr(self.name)}",
            f"  translate = {self.translate}",
            f"  rotate = {self.rotate}",
        ]
        if self.scale != (1.0, 1.0, 1.0):
            lines.append(f"  scale = {self.scale}")
        lines.append(f"  parent_index = {self.parent_index}")
        if self.next_sibling_index != -1:
            lines.append(f"  next_sibling_index = {self.next_sibling_index}")
        if self.previous_sibling_index != -1:
            lines.append(f"  previous_sibling_index = {self.previous_sibling_index}")
        lines.append(f"  bounding_box_min = {self.bounding_box_min}")
        lines.append(f"  bounding_box_max = {self.bounding_box_max}")
        if self.unk_x3c != 0:
            lines.append(f"  unk_x3c = {self.unk_x3c}")
        lines.append(")")
        return "\n".join(lines)
