from __future__ import annotations

import copy
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.maths import *
from soulstruct.utilities.misc import IDList

if tp.TYPE_CHECKING:
    from soulstruct.flver import FLVER


@dataclass(slots=True)
class BoneNode:
    """Reference-based FLVER bone representation for easy tree manipulation/navigation."""

    name: str
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: EulerRad = field(default_factory=EulerRad.zero)
    scale: Vector3 = field(default_factory=Vector3.one)
    bounding_box: AABB = field(default_factory=AABB.invalid)
    usage_flags: int = 0
    parent_bone: BoneNode | None = None
    child_bone: BoneNode | None = None
    next_sibling_bone: BoneNode | None = None
    previous_sibling_bone: BoneNode | None = None

    def get_bone_index(self, bones: IDList[BoneNode]) -> int:
        try:
            index = bones.index(self)
        except IndexError:
            raise ValueError(f"Bone {self.name} is not in given BoneTree list. Cannot get index.")
        return index

    def get_root_parent(self) -> BoneNode:
        """Get the highest parent of this bone (could be itself)."""
        bone = self
        while bone.parent_bone is not None:
            bone = bone.parent_bone
        return bone

    def get_all_parents(self, include_self=True) -> list[BoneNode]:
        """Get all parents, starting from the highest (root) and ending either in this bone or its parent."""
        parents = [self] if include_self else []
        bone = self
        while bone.parent_bone is not None:
            bone = bone.parent_bone
            parents.append(bone)
        return list(reversed(parents))

    def get_all_immediate_children(self) -> list[BoneNode]:
        """Get all immediate children of this `BoneNode` by using first child and its siblings."""
        if self.child_bone is None:
            return []
        children = [self.child_bone]
        bone = self.child_bone
        while bone.next_sibling_bone is not None:
            bone = bone.next_sibling_bone
            if bone.parent_bone is not self:
                raise ValueError(f"BoneNode {self.name} has a child sibling bone whose parent is not itself.")
            children.append(bone)
        return children

    def get_local_transform(self) -> tuple[Vector3, Matrix3, Vector3]:
        """Return combined local transform of `FLVERBone`, converting rotation Euler to a 3x3 matrix."""
        rot_mat3 = Matrix3.from_euler_angles_rad(self.rotate, order="xzy")
        return copy.copy(self.translate), rot_mat3, self.scale.copy()

    def set_local_transform(self, transform: tuple[Vector3, Matrix3, Vector3]):
        """Set local transform of `FLVERBone`, converting rotation 3x3 matrix to Euler."""
        self.translate = transform[0].copy()
        self.rotate = transform[1].to_euler_angles_rad(order="xzy")
        self.scale = transform[2].copy()

    def get_armature_space_transform(self) -> tuple[Vector3, Matrix3, Vector3]:
        """Accumulates parents' translates and rotates. Always uses bone's local scale (but copied).

        If all bones need to converted at once, the `FLVER.get_bone_armature_space_transforms()` method is more
        efficient, as it avoids recalculating the same parent transforms more than once.
        """
        absolute_translate = Vector3.zero()
        m_rotate = Matrix3.identity()
        for bone in self.get_all_parents(include_self=True):
            absolute_translate += m_rotate @ bone.translate
            m_rotate @= Matrix3.from_euler_angles_rad(bone.rotate)
        return absolute_translate, m_rotate, self.scale.copy()


class BoneTree:
    """Dereferenced bone tree, converted to/from FLVER bone reference indices."""

    bones: IDList[BoneNode]

    def __init__(self, flver: FLVER | None = None) -> None:
        self.bones = IDList()

        if flver is None:
            return  # empty tree

        for bone in flver.bones:
            bone_node = BoneNode(
                name=bone.name,
                translate=Vector3(bone.translate),
                rotate=EulerRad(bone.rotate),
                scale=Vector3(bone.scale),
                bounding_box=AABB(bone.bounding_box.min, bone.bounding_box.max),
                usage_flags=bone.usage_flags,
            )
            self.bones.append(bone_node)

        # Dereference.

        def _get_bone(_index: int):
            return None if _index == -1 else self.bones[_index]

        for i, bone in enumerate(flver.bones):
            bone_node = self.bones[i]
            bone_node.parent_bone = _get_bone(bone.parent_bone_index)
            bone_node.child_bone = _get_bone(bone.child_bone_index)
            bone_node.next_sibling_bone = _get_bone(bone.next_sibling_bone_index)
            bone_node.previous_sibling_bone = _get_bone(bone.previous_sibling_bone_index)

    def __getitem__(self, bone_index: int) -> BoneNode:
        return self.bones[bone_index]

    def append(self, bone_node: BoneNode):
        """Append a new bone to this tree, created by the caller.

        Will raise a ValueError if the bone is already in the tree (`IDList` management).
        """
        self.bones.append(bone_node)

    def get_bone_index(self, bone_node: BoneNode | None) -> int:
        if bone_node is None:
            return -1
        return bone_node.get_bone_index(self.bones)

    def get_root_bones(self) -> list[BoneNode]:
        """Return all bones with no parent."""
        return [bone for bone in self.bones if bone.parent_bone is None]

    def set_bone_children_siblings(self):
        """Iterate through the `bones` hierarchy and use set `parent_bone` (the most important reference) to set
        `child_bone` (first bone using this bone as parent) and sibling bones (ordered bones with the same parent).
        """

        # Clear old references.
        for bone in self.bones:
            bone.child_bone = None
            bone.previous_sibling_bone = None
            bone.next_sibling_bone = None

        root_bones = []
        for bone in self.bones:

            if bone.parent_bone is None:
                # Root bone. Assign siblings.
                if root_bones:
                    # Next sibling.
                    root_bones[-1].next_sibling_bone = bone
                    bone.previous_sibling_bone = root_bones[-1]
                root_bones.append(bone)

            children = []
            for other_bone in self.bones:
                if other_bone.parent_bone is bone:
                    if not children:
                        # First child found.
                        bone.child_bone = other_bone
                    else:
                        # Next sibling.
                        children[-1].next_sibling_bone = other_bone
                        other_bone.previous_sibling_bone = children[-1]
                    children.append(other_bone)

    def get_bone_armature_space_transforms(self) -> list[tuple[Vector3, Matrix3, Vector3]]:
        """Compute the FLVER armature space transforms of all bones at once by moving downward through the hierarchy.

        Note that bone scale is not inherited. All scale values are local.

        Also note that we can't cache this because any/all parent bone transforms could change. It's inexpensive anyway.
        """
        root_bones = self.get_root_bones()
        # Start with local transforms. They will be changed to armature space transforms one at a time, recursively.
        armature_space_transforms = [bone.get_local_transform() for bone in self.bones]
        done_indices = set()

        def local_to_parent_space(bone: BoneNode, parent_transform: tuple[Vector3, Matrix3, Vector3]):
            index = bone.get_bone_index(self.bones)
            if index in done_indices:
                raise ValueError(f"Bone '{bone.name}' is a child of multiple bones.")
            done_indices.add(index)
            local_translate, local_rotate_matrix, local_scale = armature_space_transforms[index]
            parent_translate, parent_rotate_matrix, _ = parent_transform
            bone_armature_transform = (
                parent_translate + parent_rotate_matrix @ local_translate,
                parent_rotate_matrix @ local_rotate_matrix,
                local_scale,  # scale not inherited
            )
            armature_space_transforms[index] = bone_armature_transform
            for child_bone in bone.get_all_immediate_children():
                local_to_parent_space(child_bone, bone_armature_transform)

        for root_bone in root_bones:
            local_to_parent_space(root_bone, (Vector3.zero(), Matrix3.identity(), Vector3.one()))

        return armature_space_transforms

    def set_bone_armature_space_transforms(self, armature_space_transforms: list[tuple[Vector3, Matrix3, Vector3]]):
        """Use given `armature_space_transforms` to set the local transforms of each `FLVERBone`, by applying the
        inverse of each parent's armature space transform (conveniently available).

        NOTE: Bone scale is NOT inherited. All scale vectors in `armature_space_transforms` will be treated as local
        bone scale vectors.
        """

        if (arma_count := len(armature_space_transforms)) != len(self.bones):
            raise ValueError(f"Expected {len(self.bones)} armature space transforms, but got {arma_count}.")

        parent_inv_rots = {}  # type: dict[int, Matrix3]

        for bone_index, bone in enumerate(self.bones):
            arma_transform = armature_space_transforms[bone_index]
            parent_bone = bone.parent_bone
            if parent_bone is None:
                # Root bone: armature space transform is local transform.
                bone.set_local_transform(arma_transform)
                continue

            parent_index = parent_bone.get_bone_index(self.bones)

            # Get parent transform and apply inverse to this bone's armature space transform.
            arma_translate, arma_rotate_matrix, arma_scale = arma_transform
            parent_arma_translate, parent_arma_rotate_matrix, _ = armature_space_transforms[parent_index]
            parent_arma_inv_rotate = parent_inv_rots.setdefault(parent_index, parent_arma_rotate_matrix.inverse())

            bone.set_local_transform(
                (
                    parent_arma_inv_rotate @ (arma_translate - parent_arma_translate),
                    parent_arma_inv_rotate @ arma_rotate_matrix,
                    arma_scale,  # scale not inherited
                )
            )

    def get_nearest_nub_bone(
        self, bone: BoneNode, bones_by_name: dict[str, BoneNode] | None = None
    ) -> BoneNode | None:
        """Recursively search up tree for a matching '*Nub' bone name.

        e.g. bone 'R Finger02' with parent 'R Finger0' might use 'R Finger0Nub'.
        """
        if bones_by_name is None:
            bones_by_name = {bone.name: bone for bone in self.bones}
        nub_name = f"{bone.name}Nub"
        if nub_name in bones_by_name:
            return bones_by_name[nub_name]
        elif bone.parent_bone is not None:
            return self.get_nearest_nub_bone(bone.parent_bone, bones_by_name)
        return None  # no Nub bone found
