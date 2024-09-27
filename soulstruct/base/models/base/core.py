from __future__ import annotations

__all__ = ["BaseFLVER"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from soulstruct.base.game_file import GameFile
from soulstruct.containers import Binder, TPF
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Vector4, Matrix3, SINGLE_MIN, SINGLE_MAX
from soulstruct.utilities.misc import IDList

from .bone import FLVERBone
from .dummy import Dummy
from .mesh_tools import BaseMergedMesh
from .submesh import BaseSubmesh
from .version import FLVERVersion

_LOGGER = logging.getLogger("soulstruct")

SUBMESH_T = tp.TypeVar("SUBMESH_T", bound=BaseSubmesh)


@dataclass(slots=True)
class BaseFLVER(GameFile, tp.Generic[SUBMESH_T]):
    """Base class for older `FLVER0` and newer `FLVER` models. This class is not intended to be used directly."""

    EXT: tp.ClassVar = ".flver"
    PATTERN: tp.ClassVar = re.compile(r".*\.flver(\.dcx)?$")

    big_endian: bool = False
    version: FLVERVersion = FLVERVersion.DarkSouls_A
    unicode: bool = True

    bounding_box_min: Vector3 = field(default_factory=Vector3.single_max)
    bounding_box_max: Vector3 = field(default_factory=Vector3.single_min)

    dummies: list[Dummy] = field(default_factory=list)
    bones: IDList[FLVERBone] = field(default_factory=IDList)
    submeshes: list[SUBMESH_T] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        raise NotImplementedError

    @classmethod
    def from_binder_path(cls, binder_path: str | Path, entry_id_or_name: int | str = None, from_bak=False) -> tp.Self:
        """If not `entry_id_or_name` is given, will search for a lone '.flver{.dcx}' entry in the binder. In this case,
        will raise an exception if no FLVER files or multiple FLVER files exist in the BND.
        """
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)
        if entry_id_or_name is None:
            flver_entry = binder.find_entry_matching_name(r".*\.flver(\.dcx)?$")
            return cls.from_bytes(flver_entry)
        return cls.from_bytes(binder[entry_id_or_name])

    @classmethod
    def multiple_from_binder_path(
        cls, binder_path: Path | str, entry_ids_or_names: tp.Sequence[int | str] = None, from_bak=False
    ) -> list[tp.Self]:
        """If not `entry_ids_or_names` is given, will search for ALL '.flver{.dcx}' entries in the binder and return a
        list of loaded FLVERs. Will raise an exception if no FLVER files are found."""
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)
        if entry_ids_or_names is None:
            flver_entries = binder.find_entries_matching_name(r".*\.flver(\.dcx)?$")
            return [cls.from_bytes(entry) for entry in flver_entries]
        return [cls.from_bytes(binder[entry_id_or_name]) for entry_id_or_name in entry_ids_or_names]

    def to_writer(self) -> BinaryWriter:
        raise NotImplementedError

    def to_string(self) -> str:
        if self.bones:
            bones = "[\n    " + "\n    ".join(repr(self.bones)[1:-1].split("\n")) + "\n  ]"
        else:
            bones = "[]"
        if self.dummies:
            dummies = "[\n    " + "\n    ".join(repr(self.dummies)[1:-1].split("\n")) + "\n  ]"
        else:
            dummies = "[]"
        if self.submeshes:
            submeshes = "[\n    " + "\n    ".join(repr(self.submeshes)[1:-1].split("\n")) + "\n  ]"
        else:
            submeshes = "[]"
        return (
            f"FLVER(\n"
            f"  bones = {bones}\n"
            f"  dummies = {dummies}\n"
            f"  submeshes = {submeshes}\n"
            ")"
        )

    def __setstate__(self, state: tuple[None, dict[str, tp.Any]]):
        """Dereference bone connections after restoring state."""
        _, slot_dict = state
        for field_name, field_value in slot_dict.items():
            setattr(self, field_name, field_value)
        for bone in self.bones:
            bone.set_bones(self.bones)

    def __repr__(self) -> str:
        return (
            f"{self.cls_name}({self.version.name}, {len(self.submeshes)} submeshes, "
            f"{len(self.bones)} bones, {len(self.dummies)} dummies)"
        )

    def refresh_submesh_indices(self):
        for i, submesh in enumerate(self.submeshes):
            submesh.index = i

    def to_merged_mesh(
        self,
        submesh_material_indices: tp.Sequence[int] = None,
        material_uv_layer_names: tp.Sequence[tp.Sequence[str]] = None,
        merge_vertices=True,
    ) -> BaseMergedMesh:
        """Return a `BaseMergedMesh` object that combines all submeshes of this FLVER into a single mesh."""
        raise NotImplementedError

    def draw(self, auto_show=False, show_mesh_face_sets=(), show_origin=False, axes=None, **kwargs):
        import matplotlib.pyplot as plt
        if show_mesh_face_sets == "all":
            show_mesh_face_sets = tuple(range(len(self.submeshes)))
        if axes is None:
            axes = plt.figure().add_subplot(111, projection="3d")
        for i, mesh in enumerate(self.submeshes):
            mesh.draw(
                show_origin=show_origin and mesh is self.submeshes[-1],
                show_face_sets=show_mesh_face_sets,
                auto_show=False,
                axes=axes,
                **kwargs,
            )
        for bone in self.bones:
            bone_position, _, _ = bone.get_armature_space_transform()
            axes.scatter(*bone_position.to_xzy(), color="blue", s=10)
        if auto_show:
            plt.show()

    def scale_all_translations(self, scale_factor: float | Vector3 | Vector4):
        """Modifies the FLVER in place by scaling all dummies, bones, and vertex positions by `factor`.

        NOTE: As a reminder, FLVER files are for APPEARANCE ONLY (and dummies for TAE events). You will have to scale
        the corresponding HKX files (map collision, character skeletons/ragdolls, etc.) before gameplay will really be
        affected.
        """
        if isinstance(scale_factor, Vector4):
            scale_factor = Vector3((scale_factor.x, scale_factor.y, scale_factor.z))
        for dummy in self.dummies:
            dummy.translate *= scale_factor
        for bone in self.bones:
            bone.translate *= scale_factor
        if isinstance(scale_factor, (int, float)):
            scale_factor = Vector3((scale_factor, scale_factor, scale_factor))
        for submesh in self.submeshes:
            for vertex_array in submesh.vertex_arrays:
                # Scale all three position columns.
                position = vertex_array["position"]
                # TODO: Should be able to broadcast this in one line.
                position[0] *= scale_factor.x
                position[1] *= scale_factor.y
                position[2] *= scale_factor.z

    # region Materials/Textures

    def replace_tpf_name(self, old_name: str, new_name: str):
        """Iterate over all `Material` textures and replace all '{old_name}.tga' names with '{new_name}.tga'."""
        for submesh in self.submeshes:
            for texture in submesh.material.textures:
                # TODO: To be safe, probably make sure we're only replacing the file name of the path.
                texture.path = texture.path.replace(old_name, new_name)

    def get_all_texture_paths(self) -> set[Path]:
        """Get set of all texture paths from all materials, which typically end in '.tga' or '.tif'.

        Ignores textures with empty `path`.
        """
        return {
            Path(texture.path)
            for submesh in self.submeshes
            for texture in submesh.material.textures if texture.path
        }

    def get_tpfbhd_directory_path(self) -> Path:
        """Looks for folder containing TPFBHD files adjacent to FLVER's directory.

        Only works for map pieces right now, and requires them to be loaded from their native location (e.g.
        `{data}/map/m10_00_00_00`).
        """
        if not self.path:
            raise ValueError(f"Cannot automatically find `tpfbhd` directory (FLVER path is unknown).")
        flver_parent = self.path.parent
        map_directory_match = re.match(r"^(m\d\d)_\d\d_\d\d_\d\d$", flver_parent.name)
        if not map_directory_match:
            raise ValueError(f"FLVER is not located in a map folder (`mAA_BB_CC_DD`).")
        tpfbhd_directory = flver_parent / f"../{map_directory_match.group(1)}"
        if not tpfbhd_directory.is_dir():
            raise FileNotFoundError(f"Required TPFBHD directory does not exist: {tpfbhd_directory}")
        return tpfbhd_directory

    def find_all_tpfs(self, tpfbhd_directory: None | str | Path = None) -> dict[Path, TPF]:
        if tpfbhd_directory is None:
            tpfbhd_directory = self.get_tpfbhd_directory_path()
        else:
            tpfbhd_directory = Path(tpfbhd_directory)
        tpf_paths = [(p, re.compile(rf"{p.stem}\.tpf(\.dcx)?$")) for p in self.get_all_texture_paths()]
        tpf_sources = {}
        for bhd_path in tpfbhd_directory.glob("*.tpfbhd"):
            bxf = Binder.from_path(bhd_path)
            for entry in bxf.entries:
                for tpf_path, tpf_re in reversed(tpf_paths):
                    if tpf_re.match(entry.name):
                        tpf_paths.remove((tpf_path, tpf_re))
                        tpf_sources[tpf_path] = TPF.from_bytes(entry.data)
                        break
                if not tpf_paths:
                    break
            if not tpf_paths:
                break
        return tpf_sources

    # endregion

    # region Bones

    def guess_rigged(self) -> bool:
        """Guess whether this FLVER is rigged -- that is, if it is a Character, Object, Equipment, etc. rather than
        a Map Piece. This is important for handling proper usage of bones, as 'unrigged' or 'static' Map Piece FLVERs
        use them simply as transforms for certain groups of vertices (e.g. individual plants), which 3D software will
        probably want to handle by 'pre-posing' the Map Piece mesh with those bones.

        Conditions indicating NOT rigged:
            - At least one vertex array layout is missing `bone_weights` data.
        """
        for submesh in self.submeshes:
            if not submesh.vertex_arrays[0].has_field("bone_weights"):
                return False
        return True

    def sort_submesh_bone_indices(self):
        """Sort local `bone_indices` of each submesh, if used."""
        for submesh in self.submeshes:
            submesh.sort_bone_indices()

    def refresh_bone_bounding_boxes(self, in_local_space=True, only_bones: tp.Container[int] = ()):
        """Refresh the bounding box of each bone by finding every vertex in every submesh weighted to it.

        As you'd expect, this is a little expensive, though less so with `NumPy`, thankfully. Optionally allows
        restriction to only certain bones, in case you KNOW which bones need refreshing and don't want to waste time on
        the others.

        Note that rigged FLVERs (characters, objects) seem to always use `in_local_space=True`, while map pieces do not.
        """

        if in_local_space:
            # Get the inverse transforms required to convert each bone's vertex positions to local bone space.
            bone_arma_translate_inv_rotates = [
                (translate, rotate.inverse())
                for translate, rotate, _ in self.get_bone_armature_space_transforms()
            ]
        else:
            # Unused.
            bone_arma_translate_inv_rotates = []

        refresh_bone_indices = [i for i, bone in enumerate(self.bones) if not only_bones or i in only_bones]

        # 3D arrays that track min/max vertex positions for each bone and axis.
        bone_mins = SINGLE_MAX * np.ones((len(self.bones), 3))
        bone_maxs = SINGLE_MIN * np.ones((len(self.bones), 3))

        # We need to check all bone indices in every vertex array in every submesh.
        for submesh in self.submeshes:

            for vertex_array in submesh.vertex_arrays:

                used_bone_vertex_indices = {}  # tracks vertex indices used by each bone
                if vertex_array.has_normal_w_bone_indices:
                    # Already global, but confirmed below.
                    bone_indices = vertex_array["normal_w"]
                else:
                    try:
                        bone_indices = vertex_array["bone_indices"]
                    except ValueError:
                        continue  # submesh vertex array has no bone indices (weird)

                if submesh.bone_indices is not None:
                    # Remap bone indices to global indices.
                    bone_indices = submesh.bone_indices[bone_indices]

                try:
                    bone_weights = vertex_array["bone_weights"]
                except ValueError:
                    # No bone weights (map piece 'pose' mode). We only need to look at first bone index (always used).
                    for bone_index in refresh_bone_indices:
                        used_bone_vertex_indices[bone_index] = bone_indices[:, 0] == bone_index
                else:
                    # Only check bone indices where weight is non-zero.
                    for bone_index in refresh_bone_indices:
                        used = ((bone_indices == bone_index) & (bone_weights > 0.0)).any(axis=1)
                        used_bone_vertex_indices[bone_index] = used

                position = vertex_array["position"]

                for bone_index, vertex_indices in used_bone_vertex_indices.items():
                    if not np.any(vertex_indices):
                        continue  # bone unused by this submesh array

                    # Get vertex positions for this bone.
                    # TODO: "IndexError: boolean index did not match indexed array along dimension 1; dimension is 3
                    #  but corresponding boolean dimension is 4."
                    bone_vertex_positions = position[vertex_indices]

                    if in_local_space:
                        # Transform vertex positions into bone local space (typical for characters).
                        arma_translate, inv_arma_rotate = bone_arma_translate_inv_rotates[bone_index]
                        bone_vertex_positions -= arma_translate.data
                        bone_vertex_positions = bone_vertex_positions @ inv_arma_rotate.data.T

                    # Get bounds for this vertex array.
                    bone_vertex_mins = np.min(bone_vertex_positions, axis=0)
                    bone_vertex_maxs = np.max(bone_vertex_positions, axis=0)

                    # Update FLVER-wide bounds across all submeshes and vertex arrays.
                    bone_mins[bone_index] = np.min((bone_mins[bone_index], bone_vertex_mins), axis=0)
                    bone_maxs[bone_index] = np.max((bone_maxs[bone_index], bone_vertex_maxs), axis=0)

        # Update bone bounding boxes.
        for bone_index in refresh_bone_indices:
            # print(f"BEFORE: {bone.name}: {bone.bounding_box_min} -> {bone.bounding_box_max}")
            bone = self.bones[bone_index]
            bone.bounding_box_min = Vector3(bone_mins[bone_index])
            bone.bounding_box_max = Vector3(bone_maxs[bone_index])
            # print(f"    --> {bone.name}: {bone.bounding_box_min} -> {bone.bounding_box_max}")

    def refresh_bounding_boxes(self):
        """Refresh global bounding box of FLVER from minimum and maximum positions of all submesh vertices, along with
        the submesh-specific bounding boxes if used.

        TODO: Should probably call this automatically on FLVER write.
        """
        if not self.submeshes:
            # Empty FLVER.
            _LOGGER.warning(f"FLVER '{self.path}' has no submeshes. Setting maximal bounding box.")
            self.bounding_box_min = Vector3((SINGLE_MAX, SINGLE_MAX, SINGLE_MAX))
            self.bounding_box_max = Vector3((SINGLE_MIN, SINGLE_MIN, SINGLE_MIN))
            return

        submesh_mins = np.empty((len(self.submeshes), 3))
        submesh_maxs = np.empty((len(self.submeshes), 3))

        for i, submesh in enumerate(self.submeshes):
            submesh_min = np.array([SINGLE_MAX] * 3)
            submesh_max = np.array([SINGLE_MIN] * 3)
            for vertex_array in submesh.vertex_arrays:
                position = vertex_array["position"]
                submesh_min = np.minimum(submesh_min, position.min(axis=0))
                submesh_max = np.maximum(submesh_max, position.max(axis=0))

            # NOTE: Lazy check for `FLVER0` vs. `FLVER`.
            if getattr(submesh, "uses_bounding_box", False):
                submesh.bounding_box_min = Vector3(submesh_min)
                submesh.bounding_box_max = Vector3(submesh_max)
                # TODO: Don't know how to set `bounding_box_unknown` in Sekiro+.

            submesh_mins[i, :] = submesh_min
            submesh_maxs[i, :] = submesh_max

        # Update FLVER-wide bounding box.
        self.bounding_box_min = Vector3(submesh_mins.min(axis=0))
        self.bounding_box_max = Vector3(submesh_maxs.max(axis=0))

    def get_root_bones(self) -> list[FLVERBone]:
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

        def local_to_parent_space(bone: FLVERBone, parent_transform: tuple[Vector3, Matrix3, Vector3]):
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

    def check_if_all_zero_bone_weights(self) -> bool:
        """Reliable (so far) indicator of map piece FLVER, as opposed to character/object FLVER.

        Map pieces sometimes use bone indices as an offset for certain submeshes (or even a subset of a mesh's
        vertices), but never use bone weights (in DS1 at least).

        This method checks every vertex and is therefore reasonably expensive to compute, so do it sparingly.
        """
        for m in self.submeshes:
            for v in m.vertices:
                if any(v.bone_weights):
                    return False
        return True

    def debone_map_piece(self, default_bone_name="", refresh_bone_bounding_boxes=True):
        """Remove all bones from a Map Piece FLVER by baking the bones into the vertices that use them and setting all
        submeshes and vertices to use only the default bone (index 0).

        Some of From's older map pieces, like Sunlight Altar and Andre's building in DS1 m10_01_00_00, use bones even
        just to place certain walls of buildings, which is extremly weird and annoying for editing. This function bakes
        all bone transforms into the vertices that use them, then removes all bones except the default bone (0), which
        is moved to the origin and named after the FLVER model (standard practice).

        If `default_bone_name` is not given, we will try to get it from the minimal stem of `self.path`. If that fails,
        we will use 'FLVER' and issue a warning.

        NOTE: Not intended for use with map pieces that use bones to place individual trees and shrubs whose mesh data
        is centered at the origin, which is an actual good way to use bones in a Map Piece!
        """
        if any(submesh.is_bind_pose for submesh in self.submeshes):
            raise ValueError("Cannot debone FLVER models with any `is_bind_pose` submeshes (i.e. must be Map Piece).")

        if not default_bone_name:
            if self.path:
                # NOTE: Map Piece default bone names are sometimes FLVER model stems (with 'AXX' suffix, etc.) and
                # sometimes the reduced model name that appears in MSB Map Piece models (without suffix/map). We use
                # the full model name here, since this is going in the model file.
                default_bone_name = self.path_minimal_stem
            else:
                default_bone_name = "FLVER"
                _LOGGER.warning(f"Could not get default bone name from FLVER path. Using bone name 'FLVER'.")

        if len(self.bones) == 1:
            if (
                self.bones[0].translate == Vector3.zero()
                and self.bones[0].rotate == Vector3.zero()
                and self.bones[0].scale == Vector3.one()
            ):
                print(f"FLVER {self.path.name} is already deboned (only has one bone at the origin).")
                return

        bone_transforms = {}
        for i, bone in enumerate(self.bones):
            bone_transforms[i] = (bone.translate, Matrix3.from_euler_angles(bone.rotate, radians=True), bone.scale)

        for submesh in self.submeshes:
            for vertex_array in submesh.vertex_arrays:
                if not vertex_array.has_field("bone_indices"):
                    if vertex_array.has_normal_w_bone_indices:
                        # These are always global, but that will be confirmed below.
                        local_bone_indices = vertex_array["normal_w"][:, 0]
                        using_normal_w = True
                    else:
                        # Submesh has no bone indices at all. (Weird.)
                        continue
                else:
                    local_bone_indices = vertex_array["bone_indices"][:, 0]  # only first index needed
                    using_normal_w = False

                array = vertex_array.array
                if submesh.bone_indices is not None:
                    global_bone_indices = submesh.bone_indices[local_bone_indices].tolist()
                else:
                    global_bone_indices = local_bone_indices.tolist()
                if len(np.unique(global_bone_indices)) == 1:
                    # All vertices use the same bone. No need to iterate over rows; just transform all positions.
                    t, r, s = bone_transforms[global_bone_indices[0]]
                    # Scale, then rotate, then translate.
                    array["position"] = (s.data * array["position"]) @ r.data.T + t.data
                    for array_field in array.dtype.names:
                        if array_field in ("normal", "bitangent") or array_field.startswith("tangent"):
                            # Just rotate unit vector. Don't bother normalizing; FLVER compression will dwarf errors.
                            array[array_field][:, :3] = array[array_field][:, :3] @ r.data.T
                else:
                    # Multiple bones used. Iterate over rows. TODO: Probably a faster way to do this.
                    for i in range(len(array)):
                        t, r, s = bone_transforms[global_bone_indices[i]]
                        # Scale, then rotate, then translate.
                        array["position"][i] = r.data @ (s.data * array["position"][i]) + t.data
                        for array_field in array.dtype.names:
                            if array_field in ("normal", "bitangent") or array_field.startswith("tangent"):
                                array[array_field][i][:3] = r.data @ array[array_field][i][:3]  # rotating a single row

                # Now set all bone indices to zero.
                if using_normal_w:
                    array["normal_w"][:, :] = 0
                else:
                    array["bone_indices"][:, :] = 0

            if submesh.bone_indices is not None:
                # Set submesh local bones to [0]. (NOTE: `FLVER0` pack will pad to 28 indices with -1.)
                submesh.bone_indices = np.array([0])

        # All bones baked into all submeshes. Remove all but the default bone (0).
        self.bones.clear()
        self.bones.append(FLVERBone(name=default_bone_name))

        if refresh_bone_bounding_boxes:
            self.refresh_bone_bounding_boxes(in_local_space=False)
        self.refresh_bounding_boxes()

    # endregion

    # region Other Formats

    def to_obj(self, name="FLVER", submeshes=()) -> str:
        if isinstance(submeshes, int):
            submeshes = [submeshes]
        vertex_offset = 0
        mesh_objs = []
        for i, mesh in enumerate(self.submeshes):
            if submeshes and i not in submeshes:
                continue  # skip this mesh
            mesh_objs.append(mesh.to_obj(name=f"{name} Submesh {i}", vertex_offset=vertex_offset))
            vertex_offset += len(mesh.vertices)
        return "\n\n".join(mesh_objs)

    def write_obj(self, obj_path: Path | str = None, obj_name="", make_dirs=True, submeshes=()):
        if obj_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            obj_path = self.path
            if obj_path.suffix == ".dcx":
                obj_path = obj_path.with_name(obj_path.stem)
            obj_path = obj_path.with_suffix(".obj")
        else:
            obj_path = Path(obj_path)
            if obj_path.suffix != ".obj":
                obj_path = obj_path.with_suffix(".obj")
        if make_dirs:
            obj_path.parent.mkdir(parents=True, exist_ok=True)
        if not obj_name:
            obj_name = obj_path.stem
        obj_str = self.to_obj(name=obj_name, submeshes=submeshes)
        with obj_path.open("w") as f:
            f.write(obj_str)

    # endregion
