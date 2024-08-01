from __future__ import annotations

__all__ = ["FLVERBone"]

import typing as tp
from dataclasses import dataclass, field, fields
from enum import IntEnum

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Matrix3
from soulstruct.utilities.misc import IDList


@dataclass(slots=True)
class FLVERBoneStruct(BinaryStruct):

    translate: Vector3
    _name_offset: int
    rotate: Vector3  # Euler angles (radians)
    _parent_bone_index: short
    _child_bone_index: short
    scale: Vector3
    _next_sibling_bone_index: short
    _previous_sibling_bone_index: short
    bounding_box_min: Vector3
    usage_flags: int
    bounding_box_max: Vector3
    _pad1: bytes = field(init=False, **BinaryPad(52))


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

    name: str
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: Vector3 = field(default_factory=Vector3.zero)  # Euler angles (radians)
    scale: Vector3 = field(default_factory=Vector3.one)
    # Mesh vertices weighted to this bone will only be drawn if this bounding box is in the camera's current view.
    # NOTE: units are in local bone space for character
    bounding_box_min: Vector3 = field(default_factory=Vector3.single_max)
    bounding_box_max: Vector3 = field(default_factory=Vector3.single_min)
    usage_flags: int = 0

    # Bone indices, which are only re-referenced just prior to pickling (in `FLVER.__getstate__()`) or FLVER export.
    # This is necessary to avoid pickling recursion limit issues with large skeletons.
    _parent_bone_index: int = -1
    _child_bone_index: int = -1
    _next_sibling_bone_index: int = -1
    _previous_sibling_bone_index: int = -1

    # Deferenced connected bones from above indices.
    parent_bone: FLVERBone | None = None
    child_bone: FLVERBone | None = None  # bone can have many children; this is the 'first' (with no previous sibling)
    next_sibling_bone: FLVERBone | None = None
    previous_sibling_bone: FLVERBone | None = None

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str) -> FLVERBone:
        """Returns `FLVERBone` instance without dereferenced connected bones."""
        bone_struct = FLVERBoneStruct.from_bytes(reader)
        name = reader.unpack_string(offset=bone_struct.pop("_name_offset"), encoding=encoding)
        flver_bone = bone_struct.to_object(cls, name=name)  # connected bone indices included
        return flver_bone

    def __getstate__(self) -> tuple[None, dict[str, tp.Any]]:
        """We don't pickle direct bone references. `FLVER.__setstate__()` will dereference them again.

        Return signature is standard for classes with `__slots__` and no `__dict__`.
        """
        return None, {f.name: getattr(self, f.name) for f in fields(self) if not f.name.endswith("_bone")}

    def set_bones(self, bones: IDList[FLVERBone]):
        for connection_name in ("parent", "child", "next_sibling", "previous_sibling"):
            index = getattr(self, f"_{connection_name}_bone_index")
            if index < 0:
                bone = None
            else:
                try:
                    bone = bones[index]
                except IndexError:
                    raise ValueError(f"Bone index {index} on '{self.name}' exceeds length of loaded `FLVER` bone list.")
            setattr(self, f"{connection_name}_bone", bone)

    def set_bone_indices(self, bones: IDList[FLVERBone]):
        for connection_name in ("parent", "child", "next_sibling", "previous_sibling"):
            bone = getattr(self, f"{connection_name}_bone")
            setattr(self, f"_{connection_name}_bone_index", -1 if bone is None else bone.get_bone_index(bones))

    def to_flver_writer(self, writer: BinaryWriter, bones: list[FLVERBone]):
        """Write this `FLVERBone` into FLVER `writer`.

        Full list of FLVER `bones` is required to get the indices of referenced bones (parent, child, siblings).
        """
        
        def get_index(bone_attr: str):
            bone = getattr(self, bone_attr)
            return -1 if bone is None else bone.get_bone_index(bones)
        
        FLVERBoneStruct.object_to_writer(
            self,
            writer,
            _name_offset=None,
            _parent_bone_index=get_index("parent_bone"),
            _child_bone_index=get_index("child_bone"),
            _next_sibling_bone_index=get_index("next_sibling_bone"),
            _prev_sibling_bone_index=get_index("previous_sibling_bone"),
        )

    def pack_name(self, writer: BinaryWriter, encoding: str):
        writer.fill_with_position("_name_offset", obj=self)
        writer.pack_z_string(self.name, encoding)

    def get_bone_index(self, bones: IDList[FLVERBone]) -> int:
        """Get index of this `FLVERBone` in given `IDList` (usually from `FLVER`).

        As FLVERs can include bones that are 100% identical in their name and data, `bones` has to be an `IDList`.
        """
        index = bones.index(self)
        if index == -1:
            raise ValueError(f"`FLVERBone` {self.name} is not in given `bones` list. Cannot set index.")
        return index

    def get_root_parent(self) -> FLVERBone:
        """Get the highest parent of this bone (may be itself)."""
        bone = self
        while bone.parent_bone is not None:
            bone = bone.parent_bone
        return bone

    def get_all_parents(self, include_self=True) -> list[FLVERBone]:
        """Get all parents, starting from the highest (root) and ending either in this bone or its parent."""
        parents = [self] if include_self else []
        bone = self
        while bone.parent_bone is not None:
            bone = bone.parent_bone
            parents.append(bone)
        return list(reversed(parents))

    def get_all_immediate_children(self) -> list[FLVERBone]:
        """Get all immediate children of this `FLVERBone` by using first child and its siblings."""
        if self.child_bone is None:
            return []
        children = [self.child_bone]
        bone = self.child_bone
        while bone.next_sibling_bone is not None:
            bone = bone.next_sibling_bone
            if bone.parent_bone is not self:
                raise ValueError(f"Bone {self.name} has a child sibling bone whose parent is not itself.")
            children.append(bone)
        return children

    def get_local_transform(self) -> tuple[Vector3, Matrix3, Vector3]:
        """Return combined local transform of `FLVERBone`, converting rotation Euler to a 3x3 matrix."""
        rot_mat3 = Matrix3.from_euler_angles(self.rotate, radians=True, order="xzy")
        return self.translate.copy(), rot_mat3, self.scale.copy()

    def set_local_transform(self, transform: tuple[Vector3, Matrix3, Vector3]):
        """Set local transform of `FLVERBone`, converting rotation 3x3 matrix to Euler."""
        self.translate = transform[0].copy()
        self.rotate = transform[1].to_euler_angles(radians=True, order="xzy")
        self.scale = transform[2].copy()

    def get_armature_space_transform(self) -> tuple[Vector3, Matrix3, Vector3]:
        """Accumulates parents' translates and rotates. Always uses bone's local scale (but copied).

        If all bones need to converted at once, the `FLVER.get_bone_armature_space_transforms()` method is more
        efficient, as it avoids recalculating the same parent transforms more than once.
        """
        absolute_translate = Vector3.zero()
        rotate = Matrix3.identity()
        for bone in self.get_all_parents(include_self=True):
            absolute_translate += rotate @ bone.translate
            rotate @= Matrix3.from_euler_angles(bone.rotate, radians=True, order="xzy")
        return absolute_translate, rotate, self.scale.copy()

    @property
    def is_default_origin(self):
        """Checks whether this bone has only default (non-auto-generated) data."""
        zero = Vector3.zero()
        one = Vector3.one()
        return (
            self.translate == zero
            and self.rotate == zero
            and self.scale == one
            and self.usage_flags == 0
        )

    def __repr__(self):
        lines = [
            f"FLVERBone(\n"
            f"  name = {repr(self.name)}",
            f"  translate = {self.translate}",
            f"  rotate = {self.rotate}",
        ]
        if not self.scale == Vector3.one():
            lines.append(f"  scale = {self.scale}")
        if self.parent_bone:
            lines.append(f"  parent_bone = '{self.parent_bone.name}'")
        if self.child_bone:
            lines.append(f"  child_bone = '{self.child_bone.name}'")
        if self.previous_sibling_bone:
            lines.append(f"  previous_sibling_bone = '{self.previous_sibling_bone.name}'")
        if self.next_sibling_bone:
            lines.append(f"  next_sibling_bone = '{self.next_sibling_bone.name}'")

        lines.append(f"  bounding_box_min = {self.bounding_box_min}")
        lines.append(f"  bounding_box_max = {self.bounding_box_max}")
        if self.usage_flags != 0:
            flags = " | ".join(
                [flag.name for flag in FLVERBoneUsageFlags if self.usage_flags & flag]
            )
            lines.append(f"  usage_flags = {self.usage_flags} ({flags})")
        lines.append(")")
        return "\n".join(lines)
