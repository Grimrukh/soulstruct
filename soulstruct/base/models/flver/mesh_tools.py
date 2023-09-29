"""Tools for manipulating FLVER models, e.g. for Blender import/export."""
from __future__ import annotations

__all__ = [
    "MergedMesh",
]

import logging
import typing as tp
from dataclasses import dataclass, field

import numpy as np

from .core import FLVER
from .submesh import Submesh, FaceSet

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MergedMesh:
    """Holds data for a single merged FLVER mesh created from all its submeshes. Optimized for Blender meshes.

    The merging operation identifes all unique vertices across all submeshes - as defined by their position, bone
    weights, and bone indices - and creates reduced 'vertex arrays' of these data for the entire mesh. Other data
    defined by FLVER vertices are moved to 'loop arrays', as well as the indices of the new reduced vertices they use.
    Each face indexes the loops it uses, as well as the material and vertex buffer layout it uses from the FLVER
    (unchanged indices from the submesh).

    NOTE: Bone indices will be remapped to global bone indices from `submesh.bone_indices` if present. The submesh will
    not be modified and `submesh.bone_indices` will not be cleared.

    Also has the options to discard degenerate (line/point) faces and/or duplicate faces (same three vertex indices in
    any order) as they are encountered. Neither is done by default, as it may be faster for your 3D software (e.g.
    Blender) to handle any issues or exceptions caused by such faces as they arise. Both types of problematic faces
    appear frequently in vanilla FLVER files, likely as an artifact of FromSoft's own mesh-splitting algorithm, and are
    almost certainly fine to remove.

    TODO: Currently optimized for DS1, but likely works for other games (if `FLVER` class is supported for them). Also
     only acts on the first vertex array in each submesh, as I haven't encountered any multi-buffer FLVERs yet.
    """
    vertex_positions: np.ndarray  # three columns for 'x', 'y', and 'z' (float32)
    vertex_bone_weights: np.ndarray  # four columns for 'a', 'b', 'c', and 'd' (float32)
    vertex_bone_indices: np.ndarray  # four columns for 'a', 'b', 'c', and 'd' (uint16)

    loop_vertex_indices: np.ndarray  # 1D array for 'vertex_index' (uint32)

    loop_normals: np.ndarray  # three columns for 'x', 'y', and 'z' (float32)
    loop_normals_w: np.ndarray  # one column for 'w' (uint8)
    loop_tangents: np.ndarray  # four columns for 'x', 'y', 'z', and `w` (float32)
    loop_bitangents: np.ndarray  # four columns for 'x', 'y', and 'z' (float32)
    loop_vertex_colors: list[np.ndarray]  # four columns per array for 'r', 'g', 'b', and 'a' (uint8)
    # If `uv_layer_names` is given, this list will have the same length as `uv_layer_names` and each UV array will
    # correspond to the UV layer with the same index. Otherwise, this list will have the same length as the maximum
    # number of UV layers used by any submesh, which may cause layer clashes (e.g. one submesh's second texture UV may
    # appear in the same array as another submesh's lightmap UV or wind UV).
    loop_uvs: list[np.ndarray]  # two columns per array for 'u' and 'v' (float32)  # TODO: currently ignoring `uv_w`

    faces: np.ndarray  # integer array of `[loop0, loop1, loop2, material_index, layout_index]` rows (uint32)

    # Stored for posterity and convenient access to materials and layouts.
    flver: FLVER | None = None

    # UV layer names used by each material to assign UV data index.
    material_uv_layers: list[list[str]] | list[None] = field(default_factory=list)

    # All unique, sorted UV layer names used by any material (or None if material UVs not given).
    uv_layers: list[str] | None = None

    @classmethod
    def from_flver(
        cls,
        flver: FLVER,
        discard_degenerate_faces=False,
        discard_duplicate_faces=False,
        material_uv_layers: list[list[str]] = None,
    ):
        """Construct merged mesh data from all `flver` submeshes."""
        if material_uv_layers:
            material_uv_layers = material_uv_layers
            all_uv_layer_names_set = set()
            for uv_layers in material_uv_layers:
                all_uv_layer_names_set |= set(uv_layers)
            uv_layers = sorted(all_uv_layer_names_set)
        else:
            material_uv_layers = [None] * len(flver.materials)
            uv_layers = None

        all_vertices, loop_data_dict = cls.build_stacked_loops(flver.submeshes, material_uv_layers, uv_layers)
        unique_vertices, loop_vertex_indices = np.unique(all_vertices, return_inverse=True, axis=0)
        vertex_positions = np.column_stack([unique_vertices[c] for c in "xyz"])
        vertex_bone_weights = np.column_stack([unique_vertices[f"bw_{c}"] for c in "abcd"])
        vertex_bone_indices = np.column_stack([unique_vertices[f"bi_{c}"] for c in "abcd"])

        # TODO: Do I really need to store the layout index? All the data has already been unpacked.
        #  Also, it should really be *materials* that specify layouts, not submeshes...

        submesh_face_info = []
        loop_offset = 0
        for submesh in flver.submeshes:
            triangles = submesh.face_sets[0].get_triangles(
                allow_primitive_restarts=False, vertex_index_offset=loop_offset
            )
            submesh_face_info.append((triangles, submesh.material_index, submesh.vertex_buffers[0].layout_index))
            loop_offset += len(submesh.vertex_arrays[0])

        # Minor optimization: can fill face array of known length directly if no faces are being discarded.
        if not discard_degenerate_faces and not discard_duplicate_faces:
            face_count = sum(len(info[0]) for info in submesh_face_info)
            faces = np.empty((face_count, 5), dtype=np.uint32)  # will be fully initialized
        else:
            faces = None  # created below

        # Only used if faces could be discarded.
        valid_face_list = []
        # Only used if `discard_duplicate_faces` is True.
        existing_face_set = set()

        face_index = 0
        for triangles, material_index, layout_index in submesh_face_info:
            for triangle in triangles:
                triangle_row = [*triangle, material_index, layout_index]
                if discard_degenerate_faces or discard_duplicate_faces:
                    if cls.is_triangle_degenerate(
                        triangle, discard_degenerate_faces, discard_duplicate_faces, existing_face_set
                    ):
                        continue
                    valid_face_list.append(triangle_row)
                else:
                    # Can fill array directly.
                    faces[face_index] = triangle_row
                    face_index += 1

        if discard_degenerate_faces or discard_duplicate_faces:
            faces = np.array(valid_face_list, dtype=np.uint32)

        return cls(
            vertex_positions=vertex_positions,
            vertex_bone_weights=vertex_bone_weights,
            vertex_bone_indices=vertex_bone_indices,
            loop_vertex_indices=loop_vertex_indices,
            **loop_data_dict,
            faces=faces,
            flver=flver,
            material_uv_layers=material_uv_layers,
            uv_layers=uv_layers,
        )

    @classmethod
    def build_stacked_loops(
        cls,
        submeshes: list[Submesh],
        material_uv_layers: list[list[str]],
        all_uv_layers: list[str] | None,
    ) -> tuple[np.ndarray, dict[str, np.ndarray]]:
        """Row-stack all submesh vertices' position and bone data in a single structured array for reduction."""
        dtype = [
            ("x", np.float32), ("y", np.float32), ("z", np.float32),
            ("bw_a", np.float32), ("bw_b", np.float32), ("bw_c", np.float32), ("bw_d", np.float32),
            ("bi_a", np.uint16), ("bi_b", np.uint16), ("bi_c", np.uint16), ("bi_d", np.uint16),
        ]
        total_vertex_count = sum(len(mesh.vertices) for mesh in submeshes)

        # Structured array for mixed dtypes.
        all_vertices = np.empty(total_vertex_count, dtype=dtype)  # will be fully initialized

        # These four arrays will be fully initialized.
        loop_normals = np.empty((total_vertex_count, 3), dtype=np.float32)
        loop_normals_w = np.empty((total_vertex_count, 1), dtype=np.uint8)
        loop_tangents = np.empty((total_vertex_count, 4), dtype=np.float32)
        loop_bitangents = np.empty((total_vertex_count, 4), dtype=np.float32)

        loop_vertex_colors_dict = {}  # new arrays added as new color indices are encountered
        loops_uvs_dict = {}  # new arrays added as new UV indices are encountered

        offset = 0
        for submesh in submeshes:
            vertices = submesh.vertex_arrays[0]
            field_names = vertices.dtype.names
            i = offset
            offset += len(vertices)
            j = offset
            uv_layers = material_uv_layers[submesh.material_index]

            if "position_x" in field_names:
                for c in "xyz":
                    all_vertices[c][i:j] = vertices[f"position_{c}"]
            else:
                _LOGGER.warning("Submesh vertices have no 'position' data. This is extremely unusual. Using zeroes.")
                # Zeroes already present in empty array.

            if "bone_weight_a" in field_names:
                for c in "abcd":
                    all_vertices[f"bw_{c}"][i:j] = vertices[f"bone_weight_{c}"]
            else:  # no bone weights (very common in map piece FLVERs)
                for c in "abcd":
                    all_vertices[f"bw_{c}"][i:j] = 0.0
                pass

            if "bone_index_a" in field_names:
                for c in "abcd":
                    if submesh.bone_indices is not None:
                        # Remap local to global bone indices (without modifying FLVER).
                        local_bone_indices = vertices[f"bone_index_{c}"]
                        all_vertices[f"bi_{c}"][i:j] = submesh.bone_indices[local_bone_indices]
                    else:
                        all_vertices[f"bi_{c}"][i:j] = vertices[f"bone_index_{c}"]
            else:
                _LOGGER.warning("Submesh vertices have no 'bone index' data. This is extremely unusual. Using zeroes.")
                # Zeroes already present in empty array.

            if "normal_x" in field_names:
                loop_normals[i:j, 0] = vertices["normal_x"]
                loop_normals[i:j, 1] = vertices["normal_y"]
                loop_normals[i:j, 2] = vertices["normal_z"]
            else:
                # Default to upward (Y) vector.
                loop_normals[i:j, 0] = 0.0
                loop_normals[i:j, 1] = 1.0
                loop_normals[i:j, 2] = 0.0

            if "normal_w" in field_names:
                loop_normals_w[i:j, 0] = vertices["normal_w"]
            else:
                # Default to 127.
                loop_normals_w[i:j, 0] = 127

            if "tangent_x" in field_names:
                loop_tangents[i:j, 0] = vertices["tangent_x"]
                loop_tangents[i:j, 1] = vertices["tangent_y"]
                loop_tangents[i:j, 2] = vertices["tangent_z"]
                loop_tangents[i:j, 3] = vertices["tangent_w"]
            else:
                # Default to rightward (X) vector.
                loop_tangents[i:j, 0] = 1.0
                loop_tangents[i:j, 1] = 0.0
                loop_tangents[i:j, 2] = 0.0
                loop_tangents[i:j, 3] = 1.0

            if "bitangent_x" in field_names:
                loop_bitangents[i:j, 0] = vertices["bitangent_x"]
                loop_bitangents[i:j, 1] = vertices["bitangent_y"]
                loop_bitangents[i:j, 2] = vertices["bitangent_z"]
                loop_bitangents[i:j, 3] = vertices["bitangent_w"]
            else:
                # Default to forward (Z) vector.
                loop_bitangents[i:j, 0] = 0.0
                loop_bitangents[i:j, 1] = 0.0
                loop_bitangents[i:j, 2] = 1.0
                loop_bitangents[i:j, 3] = 1.0

            # Color and UV arrays are only created as used. They are created with `np.zeros()` so any vertices that
            # don't use a given color or UV index will be zeroes.
            for name in field_names:
                if name.startswith("color_r_"):
                    c_i = int(name[-1])
                    color_array = loop_vertex_colors_dict.setdefault(
                        c_i, np.zeros((total_vertex_count, 4), dtype=np.uint8)
                    )
                    color_array[i:j, 0] = vertices[f"color_r_{c_i}"]
                    color_array[i:j, 1] = vertices[f"color_g_{c_i}"]
                    color_array[i:j, 2] = vertices[f"color_b_{c_i}"]
                    color_array[i:j, 3] = vertices[f"color_a_{c_i}"]
                elif name.startswith("uv_u_"):
                    # TODO: `uv_w` dropped for now.
                    uv_i = int(name[-1])
                    if all_uv_layers:
                        # Get FLVER-wide index of this UV from its known layer name in the material.
                        uv_i = all_uv_layers.index(uv_layers[uv_i])
                    uv_array = loops_uvs_dict.setdefault(uv_i, np.zeros((total_vertex_count, 2), dtype=np.float32))
                    uv_array[i:j, 0] = vertices[f"uv_u_{uv_i}"]
                    uv_array[i:j, 1] = vertices[f"uv_v_{uv_i}"]

        # Could be empty lists.
        loop_vertex_colors = [loop_vertex_colors_dict[i] for i in sorted(loop_vertex_colors_dict)]
        loop_uvs = [loops_uvs_dict[i] for i in sorted(loops_uvs_dict)]

        return all_vertices, dict(
            loop_normals=loop_normals,
            loop_normals_w=loop_normals_w,
            loop_tangents=loop_tangents,
            loop_bitangents=loop_bitangents,
            loop_vertex_colors=loop_vertex_colors,
            loop_uvs=loop_uvs,
        )

    @staticmethod
    def is_triangle_degenerate(
        triangle_vertex_indices: tuple[int, int, int],
        discard_degenerate_faces=False,
        discard_duplicate_faces=False,
        existing_face_set: set = None,
    ):
        """Returns True if triangle has two or more identical vertex indices or already exists in some vertex order."""
        if discard_degenerate_faces:
            if len(set(triangle_vertex_indices)) < 3:
                return True  # face with duplicate vertices
        if discard_duplicate_faces:
            if (triangle_tuple := tuple(sorted(triangle_vertex_indices))) in existing_face_set:
                return True  # face with same three vertices in any order
            existing_face_set.add(triangle_tuple)
        return False

    def swap_vertex_yz(self, tangents=True, bitangents=True):
        """Transform mesh in-place from game to Blender coordinates (or back) by swapping Y and Z columns of the
        relevant columns.

        As a minor optimization for Blender import, has the option to ignore tangents or bitangents.
        """
        self.vertex_positions[:, [1, 2]] = self.vertex_positions[:, [2, 1]]
        self.loop_normals[:, [1, 2]] = self.loop_normals[:, [2, 1]]
        if tangents:
            self.loop_tangents[:, [1, 2]] = self.loop_tangents[:, [2, 1]]
        if bitangents:
            self.loop_bitangents[:, [1, 2]] = self.loop_bitangents[:, [2, 1]]

    def invert_vertex_uv(self, invert_u=False, invert_v=True):
        """Transform loop UV data in place by subtracting UV coordinates from 1.

        Inverts only V by default, as this is standard for Blender.

        TODO: `uv_w` support.
        """
        for loop_uv_array in self.loop_uvs:
            if invert_u:
                loop_uv_array[:, 0] = 1.0 - loop_uv_array[:, 0]
            if invert_v:
                loop_uv_array[:, 1] = 1.0 - loop_uv_array[:, 1]

    def normalize_normals(self):
        """Transform loop normal data in place by normalizing them.

        As normals are typically compressed in FLVER vertex buffers, the decompressed normals are not normalized by
        default. They are not normalized automatically by Soulstruct because this is lossy. However, Blender expects
        normalized vectors for its normal data, so this method is provided to normalize them in-place.
        """
        self.loop_normals /= np.linalg.norm(self.loop_normals, axis=1, keepdims=True)

    def reassign_face_materials(self, new_indices: np.ndarray):
        """Reassign all face materials by using their current index to index into `new_indices`."""
        self.faces[:, 3] = new_indices[self.faces[:, 3]]

    def split_mesh(
        self,
        material_vertex_array_dtypes: dict[int, np.dtype],
        material_submesh_props: dict[int, dict[str, tp.Any]],
        use_submesh_bone_indices=True,
        max_bones_per_submesh=38,
        remapped_material_indices: dict[int, int] = None,
        unused_bone_indices_are_minus_one=False,
    ) -> list[Submesh]:
        """Splits merged mesh into FLVER submeshes.

        Requires `material_vertex_array_dtypes`, which maps the material indices that appear in the merged `faces` to
        dtypes for the vertex arrays their loops/vertices will be written into, and `material_submesh_props`, which
        specifies field values on the submesh to be created for each face material index (e.g. read from Blender
        materials). The latter MUST contain `is_bind_pose` at the very least, as it is needed to efficiently determine
        how to check used bone indices.

        If `remapped_material_indices` is given, split submeshes' material indices will be remapped to these (e.g. in
        case Blender materials have been merged into fewer final FLVER materials).

        If `unused_bone_indices_are_minus_one` is True, it will be assumed that the bone indices in
        `vertex_bone_indices` have been set to -1 when unused, rather than the FLVER standard of zero (which can be
        confused with actual use of bone 0 and requires weight inspection to confirm). This makes mesh splitting easier
        when submesh bone indices are used (with maximums); all the -1 indices will be replaced with zeroes in the final
        split submesh arrays.
        """
        if use_submesh_bone_indices and max_bones_per_submesh < 3:
            raise ValueError("`max_bones_per_submesh` must be >= 3 (and realistically, much higher!).")

        # Maps faces' material indices to lists of split submeshes (usually only one, but possibly more due to local
        # bone max limitations) and under-construction vertex array (as a list of lists).
        submeshes = {}  # type: dict[int, list[Submesh]]

        is_bind_pose = [props["is_bind_pose"] for props in material_submesh_props.values()]
        submesh_bone_counts = [0] * len(material_submesh_props)

        # Order doesn't matter here, as materials will take the columns they need.
        combined_dtype_dict = {}
        for dtype in material_vertex_array_dtypes.values():
            combined_dtype_dict.update(dtype.fields)
        combined_dtype = np.dtype(list(combined_dtype_dict.items()))

        merged_loops = self.get_combined_loop_data(combined_dtype)

        # TODO: Trying a different approach that is more straightforward.
        #  - `faces` is an array of face data rows. The first three columns are loop indices, which are still valid for
        #  our `merged_loops` array above.
        #  - First, we split `faces` by material index. By resetting the first loop index of all faces to zero (by
        #  subtracting the total length of all prior split face arrays), we essentially get every `FaceSet` immediately.
        #  - The only thing not handled at this point is bone maximums per submesh. But it's easier to grok now:
        #       - For each submesh, make a copy of the `bone_index` columns to work with (they're global, remember).
        #       - If we're in 'bind pose' mode (characters):
        #           - Set all bone indices where weight is zero to -1, to distinguish them from true use of bone 0.
        #           - We can then iterate over the rows in this 'used_bone_indices' array (our one 'array row iter').
        #           - We collect the bones used by the submesh, as currently. When this exceeds the max, we start a new
        #           submesh for that face material index, starting with that row. (We do NOT return to finished meshes.)

        # Split `faces` and indexed `merged_loops` by material index (column 3).
        split_material_indices = []
        split_faces = []
        split_loops = []  # theoretically could be re-used by different materials, but `MergedMesh` will never do that
        loop_offset = 0
        merged_loop_views = {}
        for material_index, material_dtype in material_vertex_array_dtypes.items():
            submesh_faces = self.faces[self.faces[:, 3] == material_index]
            submesh_loop_indices = submesh_faces[:, :3].ravel()  # all loop indices used by faces in this submesh
            # Minor optimization: cached views of the merged loops for identical dtypes (common).
            submesh_loops = merged_loop_views.setdefault(
                material_dtype.names, merged_loops[material_dtype.names]
            )[submesh_loop_indices]  # every three rows corresponds to a single face

            submesh_faces[:, :3] -= loop_offset  # loop indices will refer to this split submesh

            split_material_indices.append(material_index)
            split_faces.append(submesh_faces)
            split_loops.append(submesh_loops)
            loop_offset += len(submesh_loops)

        final_material_indices = []
        final_split_faces = []
        final_split_loops = []
        if use_submesh_bone_indices:
            # The actual difficult part: splitting submeshes by bone maximums. This is done differently depending on
            # `is_bind_pose=True` for this material index and whether unused bone indices are already set to -1.
            for material_index, submesh_faces, submesh_loops in zip(split_material_indices, split_faces, split_loops):

                new_subsplit_rows = []  # will contain row indices where new submeshes need to start (may be empty)
                if is_bind_pose[material_index]:
                    # Up to four unique bones per vertex, so we need to more carefully collect as we go.
                    bone_indices = np.array(submesh_loops[[f"bone_index_{c}" for c in "abcd"]], dtype=np.int16)
                    if not unused_bone_indices_are_minus_one:
                        # Set all unused bone indices to -1, to distinguish them from true use of bone 0. Ideally, the
                        # user can do this themselves while they are constructing their merged mesh (e.g. from Blender)
                        # to save time here, as this requires two new array creations.
                        bone_weights = np.array(submesh_loops[[f"bone_weight_{c}" for c in "abcd"]], dtype=np.float32)
                        bone_indices[bone_weights == 0.0] = -1

                    # Loops are still genuine loops, i.e. every three represent one triangle with 12 total bone indices.
                    bone_indices = bone_indices.reshape((-1, 12))

                    # Rather than filtering out values of -1, we make sure it's always in the set, and offset the check.
                    max_bones = max_bones_per_submesh + 1
                    unique_indices = {-1}
                    for i, row in enumerate(bone_indices):
                        unique_indices |= set(row)
                        if len(unique_indices) > max_bones:
                            # This row would exceed the limit. Start a new submesh.
                            new_subsplit_rows.append(i)
                            unique_indices = {-1} | set(row)
                else:
                    # Only one (and exactly one) index per vertex, so we only need to check the first bone index.
                    # -1 should not appear anywhere in here.
                    unique_indices = set()
                    for i, index in enumerate(submesh_loops["bone_index_a"]):
                        unique_indices.add(index)
                        if len(unique_indices) > max_bones_per_submesh:
                            # This row would exceed the limit. Start a new submesh.
                            new_subsplit_rows.append(i)
                            unique_indices = {index}

                if new_subsplit_rows:
                    # Multiple submeshes required to support all the bones in this single face material index.
                    new_subsplit_rows = [0] + new_subsplit_rows
                    for i in new_subsplit_rows[:-1]:
                        j = new_subsplit_rows[i + 1]
                        subsplit_faces = submesh_faces[i:j, :]
                        loops_start, loops_end = i * 3, j * 3
                        subsplit_loops = submesh_loops[loops_start:loops_end]

                        final_split_faces.append(subsplit_faces)
                        final_split_loops.append(subsplit_loops)
                    # Final split mesh: from last subsplit row to end.
                    subsplit_faces = submesh_faces[new_subsplit_rows[-1]:, :]
                    loops_start = new_subsplit_rows[-1] * 3
                    subsplit_loops = submesh_loops[loops_start:]
                    # TODO: Collect subsplit mesh bone indices!
                    final_material_indices.append(material_index)  # same for all bone splits
                    final_split_faces.append(subsplit_faces)
                    final_split_loops.append(subsplit_loops)
                else:
                    # No subsplits needed for this material index.
                    # TODO: Still need to set `mesh.bone_indices` though.
                    final_material_indices.append(material_index)
                    final_split_faces.append(submesh_faces)
                    final_split_loops.append(submesh_loops)
        else:
            # No subsplits needed.
            final_material_indices = split_material_indices
            final_split_faces = split_faces
            final_split_loops = split_loops

        for material_index, submesh_faces, submesh_loops in zip(
            final_material_indices, final_split_faces, final_split_loops
        ):
            submesh_loops, reduced_indices = np.unique(submesh_loops, return_inverse=True, axis=0)
            submesh_faces[:, :3] = reduced_indices[submesh_faces[:, :3]]  # replace loop indices with reduced indices
            # TODO: Set `cull_back_faces` properly.
            face_set = FaceSet.from_triangles(submesh_faces[:, :3])
            # TODO: **material_submesh_props[material_index]?
            #  also need to create VertexBuffer or (preferably) make it an artifact of packing/unpacking Submesh (only
            #  the layout index remains relevant for each Submesh vertex array).
            # TODO: expanding on that cleanup: rather than saving a `BufferLayout`, FLVER could just store the dtype and
            #  the names of the codecs used for each one. Field name + codec name allows full regen of layout members.
            #  Then each Submesh vertex array contains EVERYTHING needed in its dtype + codec names, which could be in
            #  a handy `FLVERVertexArray` wrapper class (can redirect `submesh.vertices` to the actual wrapped array).
            material_index = remapped_material_indices.get(material_index, material_index)
            submesh = Submesh(face_sets=[face_set], material_index=material_index)

            if use_submesh_bone_indices:
                # Truncate all -1 values from end of submesh bone indices.
                submesh.bone_indices = submesh.bone_indices[submesh.bone_indices != -1]

                flver_submeshes.append(submesh)

        return flver_submeshes

    def get_combined_loop_data(self, combined_dtype: np.dtype):
        """Combine the appropriate loop data, in the given order, into a single structured array for indexing by loop
        row ('FLVER vertex row') or field name (so materials can use their subset dtypes).

        The returned array, therefore, is essentially a merged version of the complete `submesh.vertices` arrays for
        all submeshes using a 'maximal' dtype (including whichever colors happen to be present).

        Note that the order of fields in `combined_dtype` likely won't matter if materials are using their own subset
        dtypes anyway.
        """
        loop_count = len(self.loop_vertex_indices)
        combined_array = np.empty(loop_count, dtype=combined_dtype)  # will be fully initialized

        names = set(combined_dtype.names)  # order is unimportant for initialization

        if "position_x" in names:
            positions = self.vertex_positions[self.loop_vertex_indices]  # (loop_count, 3)
            combined_array["position_x"] = positions[:, 0]
            combined_array["position_y"] = positions[:, 1]
            combined_array["position_z"] = positions[:, 2]
        if "bone_weight_a" in names:
            bone_weights = self.vertex_bone_weights[self.loop_vertex_indices]  # (loop_count, 4)
            combined_array["bone_weight_a"] = bone_weights[:, 0]
            combined_array["bone_weight_b"] = bone_weights[:, 1]
            combined_array["bone_weight_c"] = bone_weights[:, 2]
            combined_array["bone_weight_d"] = bone_weights[:, 3]
        if "bone_index_a" in names:
            bone_indices = self.vertex_bone_indices[self.loop_vertex_indices]  # (loop_count, 4)
            combined_array["bone_index_a"] = bone_indices[:, 0]
            combined_array["bone_index_b"] = bone_indices[:, 1]
            combined_array["bone_index_c"] = bone_indices[:, 2]
            combined_array["bone_index_d"] = bone_indices[:, 3]
        if "normal_x" in names:
            combined_array["normal_x"] = self.loop_normals[:, 0]
            combined_array["normal_y"] = self.loop_normals[:, 1]
            combined_array["normal_z"] = self.loop_normals[:, 2]
        if "normal_w" in names:
            combined_array["normal_w"] = self.loop_normals_w[:, 0]
        if "tangent_x" in names:
            combined_array["tangent_x"] = self.loop_tangents[:, 0]
            combined_array["tangent_y"] = self.loop_tangents[:, 1]
            combined_array["tangent_z"] = self.loop_tangents[:, 2]
            combined_array["tangent_w"] = self.loop_tangents[:, 3]
        if "bitangent_x" in names:
            combined_array["bitangent_x"] = self.loop_bitangents[:, 0]
            combined_array["bitangent_y"] = self.loop_bitangents[:, 1]
            combined_array["bitangent_z"] = self.loop_bitangents[:, 2]
            combined_array["bitangent_w"] = self.loop_bitangents[:, 3]

        color_r_names = [n for n in names if n.startswith("color_r_")]
        for color_r_name in color_r_names:
            c_i = int(color_r_name[-1])
            colors = self.loop_vertex_colors[c_i]  # (loop_count, 4)
            combined_array[f"color_r_{c_i}"] = colors[:, 0]
            combined_array[f"color_g_{c_i}"] = colors[:, 1]
            combined_array[f"color_b_{c_i}"] = colors[:, 2]
            combined_array[f"color_a_{c_i}"] = colors[:, 3]

        uv_u_names = [n for n in names if n.startswith("uv_u_")]
        for uv_u_name in uv_u_names:
            uv_i = int(uv_u_name[-1])
            uvs = self.loop_uvs[uv_i]  # (loop_count, 2)
            combined_array["uv_u"] = uvs[:, 0]
            combined_array["uv_v"] = uvs[:, 1]
            # TODO: `uv_w`

        return combined_array

    @staticmethod
    def get_empty_subarray_dict(names: tp.Sequence[str]) -> dict[str, list[np.ndarray]]:
        """Create a dictionary with empty lists for each vertex array field name (combining sub-dimensions)."""

        subarrays = {}

        for field_name in names:
            if field_name == "position_x":
                subarrays["position"] = []
            elif field_name == "bone_weight_a":
                subarrays["bone_weights"] = []
            elif field_name == "bone_index_a":
                subarrays["bone_indices"] = []
            elif field_name == "normal_x":
                subarrays["normal"] = []
            elif field_name == "normal_w":
                subarrays["normal_w"] = []
            elif field_name == "tangent_x":
                subarrays["tangent"] = []
            elif field_name == "bitangent_x":
                subarrays["bitangent"] = []
            elif field_name.startswith("color_r_"):
                c_i = int(field_name[-1])
                subarrays[f"color_{c_i}"] = []
            elif field_name.startswith("uv_u_"):
                uv_i = int(field_name[-1])
                subarrays[f"uv_{uv_i}"] = []

        return subarrays

    @staticmethod
    def make_bone_indices_local(bone_indices: np.ndarray, submesh_bone_indices: np.ndarray):
        lo = min(bone_indices.min(), submesh_bone_indices.min())
        hi = max(bone_indices.max(), submesh_bone_indices.max())
        lut = np.zeros(hi - lo + 1, dtype=np.int64)
        lut[submesh_bone_indices - lo] = np.arange(len(submesh_bone_indices))
        return lut[bone_indices - lo]


@dataclass(slots=True)
class SplitSubmesh:
    """Holds data for submeshes under construction."""
    submesh: Submesh

    # Each value added to this (dtype-dependent) will be row-stacked, then the results column-stacked.
    vertex_subarrays: dict[str, list[np.ndarray]]

    # Used to offset face vertex indices
    vertex_count: int

    # Triangles for `FaceSet`.
    face_vertex_indices: list[int]

    @classmethod
    def from_props(cls, **submesh_kwargs):
        """Create a `SplitSubmesh` from a `Submesh`'s properties."""
        return cls(
            submesh=Submesh(**submesh_kwargs),
            vertex_subarrays={},
            vertex_count=0,
            face_vertex_indices=[],
        )
