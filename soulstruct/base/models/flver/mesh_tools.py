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
from .bounding_box import BoundingBox
from .material import Material
from .submesh import Submesh, FaceSet
from .vertex_array import *

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

    faces: np.ndarray  # integer array of `[loop0, loop1, loop2, material_index]` rows (uint32)

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
        submesh_material_indices: list[int],
        discard_degenerate_faces=False,
        discard_duplicate_faces=False,
        material_uv_layers: list[list[str]] = None,
    ):
        """Construct merged mesh data from all `flver` submeshes.

        The merged `faces` array contains a fourth column (`faces[:, 3]`) that records the 'material index' of each
        face, which is sourced directly from argument `submesh_material_indices` (which should have the same length as
        `flver.submeshes`) rather than using the original FLVER material index. This allows the definition of 'material'
        to be set to match the caller's purposes for the merged mesh, usually to preserve distinct submesh or face set
        properties (e.g. `is_bind_pose` or `cull_back_faces`) that may be different for submeshes that share the same
        FLVER material index.
        """
        if material_uv_layers:
            material_uv_layers = material_uv_layers
            all_uv_layer_names_set = set()
            for uv_layers in material_uv_layers:
                all_uv_layer_names_set |= set(uv_layers)
            uv_layers = sorted(all_uv_layer_names_set)
        else:
            material_uv_layers = [None] * len(flver.materials)
            uv_layers = None

        all_vertices, loop_data_dict = cls.build_stacked_loops(
            flver.submeshes, submesh_material_indices, material_uv_layers, uv_layers
        )

        unique_vertices, loop_vertex_indices = np.unique(all_vertices, return_inverse=True, axis=0)
        vertex_positions = np.column_stack([unique_vertices[c] for c in "xyz"])
        vertex_bone_weights = np.column_stack([unique_vertices[f"bw_{c}"] for c in "abcd"])
        vertex_bone_indices = np.column_stack([unique_vertices[f"bi_{c}"] for c in "abcd"])

        triangles_to_row_stack = []  # type: list[np.ndarray]
        loop_offset = 0
        for submesh, material_index in zip(flver.submeshes, submesh_material_indices):
            triangles = submesh.face_sets[0].triangulate(allow_primitive_restarts=False)  # `(n, 3)` array
            triangles += loop_offset
            # Add material index column (uniform for submesh, obviously).
            triangles = np.column_stack([triangles, np.full(len(triangles), material_index, dtype=np.uint32)])
            triangles_to_row_stack.append(triangles)
            loop_offset += len(submesh.vertex_arrays[0])

        # Initialize `faces` array with combined rows. If no faces are being discarded, this is final.
        faces = np.row_stack(triangles_to_row_stack)

        if discard_degenerate_faces or discard_duplicate_faces:
            existing_face_set = set()  # for duplicate face detection

            def include_row(triangle_row):
                """Boolean condition for each triangle's inclusion."""
                return cls.is_triangle_degenerate(
                    triangle_row, discard_degenerate_faces, discard_duplicate_faces, existing_face_set
                )

            faces = faces[include_row(faces)]

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
        material_indices: list[int],
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
        for submesh, material_index in zip(submeshes, material_indices):
            vertices = submesh.vertex_arrays[0].array
            field_names = vertices.dtype.names
            i = offset
            offset += len(vertices)
            j = offset
            uv_layers = material_uv_layers[material_index]

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

    def split_mesh(
        self,
        submesh_info: list[tuple[Material, VertexArrayLayout, dict[str, tp.Any]]],
        use_submesh_bone_indices=True,
        max_bones_per_submesh=38,
        unused_bone_indices_are_minus_one=False,
    ) -> list[Submesh]:
        """Splits merged mesh into FLVER submeshes.

        `submesh_info` must be a list of FLVER `Material` instances, appropriate layouts, and combined `Submesh/FaceSet`
        kwargs for each value that appears in `faces[3]`. The merged mesh will be split based on these values (and maybe
        further split by bone maximum if `use_submesh_bone_indices` is True) and the created `Submesh` and `FaceSet`
        instances will take their materials, layouts, and kwargs from this list.

        As with `MergedMesh.from_flver()`, the definition of 'material' here should comprise any reason that the mesh
        needs to be split, and `faces[3]` should be set accordingly. Two split submeshes may use the same FLVER material
        in `submesh_info`, for example, yet have different `is_bind_pose` values or `face_sets[0].cull_back_faces`, etc.

        `is_bind_pose` must appear in each submesh kwargs dictionary, as it is used to determine bone index style.
        TODO: Still not 100% sure if there are any FLVERs that use 'bind pose' for some submeshes but not others. From
         memory, I found a few cut content objects or something, but only checked the bool and not the indices.

        If `unused_bone_indices_are_minus_one` is True, it will be assumed that the bone indices in
        `self.vertex_bone_indices` have been set to -1 when unused, rather than the FLVER standard of zero (which can be
        confused with actual use of bone 0 and requires weight inspection to confirm). This makes mesh splitting easier
        when submesh bone indices are used (with maximums); all the -1 indices will be replaced with zeroes in the final
        split submesh arrays.
        """
        if use_submesh_bone_indices and max_bones_per_submesh < 3:
            raise ValueError("`max_bones_per_submesh` must be >= 3 (and realistically, should be much higher!).")

        submesh_materials = [material for material, _, _ in submesh_info]
        submesh_layouts = [layout for _, layout, _ in submesh_info]
        material_dtypes = [layout.get_dtypes()[1] for layout in submesh_layouts]  # decompressed dtypes
        submesh_kwargs = [kwargs for _, _, kwargs in submesh_info]

        # We construct a `dtype` that includes all fields from every material.
        # Order doesn't matter here, as materials will take the columns they need.
        combined_dtype_fields = []
        for dtype in material_dtypes:
            for field_name, field_info in dtype.fields.items():
                if (field_name, field_info[0]) not in combined_dtype_fields:
                    combined_dtype_fields.append((field_name, field_info[0]))
        combined_dtype = np.dtype(combined_dtype_fields)

        merged_loops = self.get_combined_loop_data(combined_dtype)

        # Stores tuples of `(material_index, loop_array, submesh_bone_indices)` for each submesh. Every three rows in
        # `loop_array` comprises a unique face, so face indices are implicit.
        # These are further subsplit by bone maximum if applicable. Loop arrays have not yet been reduced down to unique
        # rows only (happens afterward).
        # NOTE: Data will be EXTRACTED from `merged_loops` by index, making no assumptions about which submeshes share
        # loop data (which will never happen when `MergedMesh` is constructed from a single FLVER, but may in custom
        # data).
        split_submesh_info = []  # type: list[tuple[int, np.ndarray, tp.Optional[np.ndarray]]]

        merged_loop_views = {}  # minor optimization (construct each dtype-dependent view only once)
        for material_index, material_dtype in enumerate(material_dtypes):
            # Split `faces` and indexed `merged_loops` by material index (column 3).
            submesh_faces = self.faces[self.faces[:, 3] == material_index][:, :3]  # `(n, 3)` array
            submesh_loop_indices = submesh_faces.ravel()  # all loop indices used by faces in this submesh

            # Loop data access. This makes no assumptions about how 'loopy' the loop data in the `MergedMesh` is. If
            # loaded from a FLVER, many faces will already index the same 'loops', but this may not be the case for
            # custom data (like true loops from a Blender mesh). This array will always have length `(3 * n, 3)`, where
            # `n` is the face count; faces with overlapping loop indices will just have duplicate rows, all of which
            # will be reduced to unique rows below. The face indices at this stage are also implicit: [0, 1, 2, 3, ...]
            submesh_loops = merged_loop_views.setdefault(
                material_dtype.names, merged_loops[list(material_dtype.names)]
            )[submesh_loop_indices]  # every three rows corresponds to a single face (will have duplicates)

            if use_submesh_bone_indices:
                split_submesh_info += self.subsplit_faces(
                    material_index,
                    submesh_loops,
                    is_bind_pose=submesh_kwargs[material_index]["is_bind_pose"],
                    max_bones_per_submesh=max_bones_per_submesh,
                    unused_bone_indices_are_minus_one=unused_bone_indices_are_minus_one,
                )
            else:
                # Vertex bone indices are global and have no maximum count.
                split_submesh_info.append((material_index, submesh_loops, None))

        split_submeshes = []

        for material_index, submesh_loops, submesh_bone_indices in split_submesh_info:
            kwargs = submesh_kwargs[material_index]

            # Duplicate loop data is finally removed here, giving the true vertex data stored in the FLVER submesh.
            # However, since `np.unique()` automatically and unstoppably sorts the array, we need to use `return_index`
            # to UNSORT it, then `return_inverse` (after also unsorting) to get the final face vertex indices.
            submesh_vertices, first_indices, face_vertex_indices = np.unique(
                submesh_loops, return_index=True, return_inverse=True, axis=0
            )

            # TODO: Given all the extra sorting calls here, it's almost certainly worth using a custom `unique` function
            #  that doesn't sort to begin with?

            # Get the sorting indices for `first_indices`:
            sorting_indices = np.argsort(first_indices)
            # Apply those to `submesh_vertices` to unsort it:
            submesh_vertices = submesh_vertices[sorting_indices]
            # Get the inverse sorting indices:
            inverse_sorting_indices = np.argsort(sorting_indices)
            # Apply to `face_indices` to update them to index into the unsorted `submesh_vertices`:
            face_vertex_indices = inverse_sorting_indices[face_vertex_indices]

            vertex_array = VertexArray(array=submesh_vertices, layout=submesh_layouts[material_index])
            # TODO: Handle Sekiro+ bounding box with unknown.
            bounding_box = BoundingBox.from_vertex_positions(vertex_array.get_position(as_view=False))

            face_set = FaceSet.from_triangles(face_vertex_indices, cull_back_faces=kwargs["cull_back_faces"])
            material = submesh_materials[material_index]
            submesh = Submesh(
                face_sets=[face_set],
                material=material,
                vertex_arrays=[vertex_array],
                is_bind_pose=kwargs["is_bind_pose"],
                default_bone_index=kwargs["default_bone_index"],
                bone_indices=submesh_bone_indices,
                bounding_box=bounding_box,
            )

            split_submeshes.append(submesh)

        return split_submeshes

    @staticmethod
    def subsplit_faces(
        material_index: int,
        submesh_loops: np.ndarray,
        is_bind_pose: bool,
        max_bones_per_submesh: int,
        unused_bone_indices_are_minus_one: bool,
    ) -> list[tuple[int, np.ndarray, np.ndarray]]:
        """Takes arrays of split faces, loops, and bone indices and returns a tuple of arrays of subsplit faces, loops,
        and bone indices, which can be appended to the appropriate lists for each material rather than a single
        submesh."""
        subsplit_face_indices = [0]
        subsplit_bone_indices = []

        bone_indices = np.empty((len(submesh_loops), 4), dtype=np.int16)
        for i, c in enumerate("abcd"):
            bone_indices[:, i] = submesh_loops[f"bone_index_{c}"]

        if is_bind_pose:
            # Up to four unique bones per vertex, so we need to more carefully collect as we go.
            if not unused_bone_indices_are_minus_one:
                # Set all unused bone indices to -1, to distinguish them from true use of bone 0. Ideally, the
                # user can do this themselves while they are constructing their merged mesh (e.g. from Blender)
                # to save time here, as this requires two new array creations.
                bone_weights = np.empty((len(submesh_loops), 4), dtype=np.float32)
                for i, c in enumerate("abcd"):
                    bone_weights[:, i] = submesh_loops[f"bone_weight_{c}"]
                bone_indices[bone_weights == 0.0] = -1

        # Loops are still genuine loops, i.e. every three represent one triangle with 12 total bone indices.
        all_face_bone_indices = bone_indices.reshape((-1, 12))

        # Rather than filtering out values of -1, we make sure it's always in the set, and offset the check.
        # Slightly suboptimal for `is_bind_pose = False`, as every face should only have up to 3 bones, but
        # worth the complexity trade-off.
        max_bones = max_bones_per_submesh + 1
        unique_indices = {-1}
        for face_index, face_bone_indices in enumerate(all_face_bone_indices):
            unique_indices |= set(face_bone_indices)
            if len(unique_indices) > max_bones:
                # This row would exceed the limit. Start a new submesh.
                subsplit_face_indices.append(face_index)
                subsplit_bone_indices.append(np.array(sorted(unique_indices - {-1})))
                unique_indices = {-1} | set(face_bone_indices)

        # Finish final subsplit. Face indices for submeshes that don't need sub-splitting will just be `[0, n]`.
        subsplit_face_indices += [len(submesh_loops) // 3]
        subsplit_bone_indices.append(np.array(sorted(unique_indices - {-1})))

        all_subsplits = []
        for i, face_start in enumerate(subsplit_face_indices[:-1]):
            face_end = subsplit_face_indices[i + 1]
            loops_start, loops_end = face_start * 3, face_end * 3
            subsplit_loops = submesh_loops[loops_start:loops_end]

            subsplit_global_bone_indices = bone_indices[loops_start:loops_end, :]
            MergedMesh.make_bone_indices_local(subsplit_global_bone_indices, subsplit_bone_indices[i])
            subsplit_loops["bone_index_a"] = subsplit_global_bone_indices[:, 0]
            subsplit_loops["bone_index_b"] = subsplit_global_bone_indices[:, 1]
            subsplit_loops["bone_index_c"] = subsplit_global_bone_indices[:, 2]
            subsplit_loops["bone_index_d"] = subsplit_global_bone_indices[:, 3]

            all_subsplits.append((material_index, subsplit_loops, subsplit_bone_indices[i]))

        return all_subsplits

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

        uv_u_names = [n for n in names if n.startswith("uv_u_")]
        for uv_u_name in uv_u_names:
            uv_i = int(uv_u_name[-1])
            uvs = self.loop_uvs[uv_i]  # (loop_count, 2)
            combined_array[f"uv_u_{uv_i}"] = uvs[:, 0]
            combined_array[f"uv_v_{uv_i}"] = uvs[:, 1]
            # TODO: `uv_w`

        color_r_names = [n for n in names if n.startswith("color_r_")]
        for color_r_name in color_r_names:
            c_i = int(color_r_name[-1])
            colors = self.loop_vertex_colors[c_i]  # (loop_count, 4)
            combined_array[f"color_r_{c_i}"] = colors[:, 0]
            combined_array[f"color_g_{c_i}"] = colors[:, 1]
            combined_array[f"color_b_{c_i}"] = colors[:, 2]
            combined_array[f"color_a_{c_i}"] = colors[:, 3]

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

    @staticmethod
    def unique(array: np.ndarray, max_value=None):
        """More efficient `np.unique()` (for reasonable array lengths) that uses masking and does NOT sort."""
        max_value = max_value or np.max(array) + 1
        used = np.zeros(max_value, dtype=np.uint8)
        used[array] = 1
        return np.argwhere(used == 1)[:, 0]


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
