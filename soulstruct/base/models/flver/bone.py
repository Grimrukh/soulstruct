from __future__ import annotations

__all__ = ["FLVERBone"]

from dataclasses import dataclass, field
import typing as tp

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Matrix3


@dataclass(slots=True)
class FLVERBoneStruct(BinaryStruct):

    translate: Vector3
    _name_offset: int
    rotate: Vector3  # Euler angles (radians)
    parent_index: short
    child_index: short
    scale: Vector3
    next_sibling_index: short
    previous_sibling_index: short
    bounding_box_min: Vector3
    unk_x3c: int  # seems to be 1 for root bones?
    bounding_box_max: Vector3
    _pad1: bytes = field(init=False, **BinaryPad(52))


@dataclass(slots=True)
class FLVERBone:
    """Bone in a FLVER model. Named to distinguish it from Havok bones in my `soulstruct-havok` package."""

    name: str
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: Vector3 = field(default_factory=Vector3.zero)  # Euler angles (radians)
    scale: Vector3 = field(default_factory=Vector3.one)
    bounding_box_min: Vector3 = field(default_factory=Vector3.zero)
    bounding_box_max: Vector3 = field(default_factory=Vector3.zero)
    # TODO: almost certainly flags. In DSR, seems to be 1 IFF bone is NOT in the main hierarchy. In Elden Ring, more
    #  flag values are used: 1 still means 'not in main hierarchy', but Dmypoly bones use 2, 'cXXXX_whatever' bones
    #  use 4, and main bones use either 8 (mostly) or 10 (unclear - combined with Dmypoly flag?). Definitely bitfield.
    unk_x3c: int = 0
    parent_index: int = -1
    child_index: int = -1  # NOTE: only indicates first child, but bone can have many children (can use siblings)
    next_sibling_index: int = -1
    previous_sibling_index: int = -1

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str) -> FLVERBone:
        bone_struct = FLVERBoneStruct.from_bytes(reader)
        name = reader.unpack_string(offset=bone_struct.pop("_name_offset"), encoding=encoding)
        flver_bone = bone_struct.to_object(cls, name=name)
        return flver_bone

    def to_flver_writer(self, writer: BinaryWriter):
        FLVERBoneStruct.object_to_writer(self, writer, _name_offset=None)

    def pack_name(self, writer: BinaryWriter, encoding: str):
        writer.fill_with_position("_name_offset", obj=self)
        writer.pack_z_string(self.name, encoding)

    def get_bone_index(self, bones: list[FLVERBone]) -> int:
        """Get index of this `FLVERBone` in given list from `FLVER`."""
        return bones.index(self)

    def get_parent(self, bones: list[FLVERBone]) -> tp.Optional[FLVERBone]:
        if self.parent_index != -1:
            return bones[self.parent_index]
        return None

    def get_all_parents(self, bones: list[FLVERBone], include_self=True) -> list[FLVERBone]:
        """Get all parents, from the highest to this `FLVERBone`."""
        parents = [self] if include_self else []
        bone = self
        while bone.parent_index != -1:
            bone = bones[bone.parent_index]
            parents.append(bone)
        return list(reversed(parents))

    def get_child(self, bones: list[FLVERBone]) -> tp.Optional[FLVERBone]:
        """Get the bone specified by `child_index`.

        Note that some bones have multiple children, which can only be detected by inspecting their parent.
        """
        if self.child_index != -1:
            return bones[self.child_index]
        return None

    def get_all_immediate_children(self, bones: list[FLVERBone]) -> list[FLVERBone]:
        """Get all immediate children of this `FLVERBone` by checking all bones' parent indices."""
        index = self.get_bone_index(bones)
        return [bone for bone in bones if bone.parent_index == index]

    def get_next_sibling(self, bones: list[FLVERBone]) -> tp.Optional[FLVERBone]:
        if self.next_sibling_index != -1:
            return bones[self.next_sibling_index]
        return None

    def get_previous_sibling(self, bones: list[FLVERBone]) -> tp.Optional[FLVERBone]:
        if self.previous_sibling_index != -1:
            return bones[self.previous_sibling_index]
        return None

    def get_local_transform(self) -> tuple[Vector3, Matrix3, Vector3]:
        """Return combined local transform of `FLVERBone`, converting rotation Euler to a 3x3 matrix."""
        rot_mat3 = Matrix3.from_euler_angles(self.rotate, radians=True, order="xzy")
        return self.translate.copy(), rot_mat3, self.scale.copy()

    def set_local_transform(self, transform: tuple[Vector3, Matrix3, Vector3]):
        """Set local transform of `FLVERBone`, converting rotation 3x3 matrix to Euler."""
        self.translate = transform[0].copy()
        self.rotate = transform[1].to_euler_angles(radians=True, order="xzy")
        self.scale = transform[2].copy()

    def get_armature_space_transform(self, bones: list[FLVERBone]) -> tuple[Vector3, Matrix3, Vector3]:
        """Accumulates parents' translates and rotates. Always uses bone's local scale (but copied).

        If all bones need to converted at once, the `FLVER.get_bone_armature_space_transforms()` method is more
        efficient, as it avoids recalculating the same parent transforms more than once.
        """
        absolute_translate = Vector3.zero()
        rotate = Matrix3.identity()
        for bone in self.get_all_parents(bones, include_self=True):
            absolute_translate += rotate @ bone.translate
            rotate @= Matrix3.from_euler_angles(bone.rotate, radians=True, order="xzy")
        return absolute_translate, rotate, self.scale.copy()

    def __repr__(self):
        lines = [
            f"FLVERBone(\n"
            f"  name = {repr(self.name)}",
            f"  translate = {self.translate}",
            f"  rotate = {self.rotate}",
        ]
        if not self.scale == Vector3.one():
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
