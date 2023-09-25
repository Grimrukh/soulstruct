"""Tools for manipulating FLVER models, e.g. for Blender import/export."""
from __future__ import annotations

__all__ = [
    "MergedMesh",
]

import logging
from dataclasses import dataclass

import numpy as np

from .core import FLVER
from .submesh import Submesh

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True, init=False)
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
    flver: FLVER  # stored for posterity and convenient access to materials and layouts
    material_uv_layers: list[list[str]] | list[None]  # UV layer names used by each material to assign UV data index
    uv_layers: list[str] | None  # all unique UV layer names used by any material (or None if material UVs not given)

    vertex_positions: np.ndarray  # three columns for 'x', 'y', and 'z' (float32)
    vertex_bone_weights: np.ndarray  # four columns for 'a', 'b', 'c', and 'd' (float32)
    vertex_bone_indices: np.ndarray  # four columns for 'a', 'b', 'c', and 'd' (uint16)

    loop_vertex_indices: np.ndarray  # one column for 'vertex_index' (uint32)
    loop_normals: np.ndarray  # three columns for 'x', 'y', and 'z' (float32)
    loop_normals_w: np.ndarray  # one column for 'w' (uint8)
    loop_tangents: np.ndarray  # three columns for 'x', 'y', and 'z' (float32)
    loop_bitangents: np.ndarray  # three columns for 'x', 'y', and 'z' (float32)
    loop_vertex_colors: list[np.ndarray]  # four columns per array for 'r', 'g', 'b', and 'a' (uint8)

    # If `uv_layer_names` is given, this list will have the same length as `uv_layer_names` and each UV array will
    # correspond to the UV layer with the same index. Otherwise, this list will have the same length as the maximum
    # number of UV layers used by any submesh, which may cause layer clashes (e.g. one submesh's second texture UV may
    # appear in the same array as another submesh's lightmap UV or wind UV).
    loop_uvs: list[np.ndarray]  # two columns per array for 'u' and 'v' (float32)  # TODO: currently ignoring `uv_w`

    faces: np.ndarray  # integer array of `[loop0, loop1, loop2, material_index, layout_index]` rows (uint32)

    def __init__(
        self,
        flver: FLVER,
        discard_degenerate_faces=False,
        discard_duplicate_faces=False,
        material_uv_layers: list[list[str]] = None,
    ):
        """Construct merged mesh data from all `flver` submeshes."""
        self.flver = flver

        if material_uv_layers:
            self.material_uv_layers = material_uv_layers
            all_uv_layer_names_set = set()
            for uv_layers in self.material_uv_layers:
                all_uv_layer_names_set |= set(uv_layers)
            self.uv_layers = sorted(all_uv_layer_names_set)
        else:
            self.material_uv_layers = [None] * len(flver.materials)
            self.uv_layers = None

        all_vertices = self.build_stacked_loops(flver.submeshes)
        unique_vertices, self.loop_vertex_indices = np.unique(all_vertices, return_inverse=True, axis=0)
        self.vertex_positions = np.column_stack([unique_vertices[c] for c in "xyz"])
        self.vertex_bone_weights = np.column_stack([unique_vertices[f"bw_{c}"] for c in "abcd"])
        self.vertex_bone_indices = np.column_stack([unique_vertices[f"bi_{c}"] for c in "abcd"])

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
            self.faces = np.empty((face_count, 5), dtype=np.uint32)  # will be fully initialized

        # Only used if faces could be discarded.
        valid_face_list = []
        # Only used if `discard_duplicate_faces` is True.
        existing_face_set = set()

        face_index = 0
        for triangles, material_index, layout_index in submesh_face_info:
            for triangle in triangles:
                triangle_row = [*triangle, material_index, layout_index]
                if discard_degenerate_faces or discard_duplicate_faces:
                    if self.is_triangle_degenerate(
                        triangle, discard_degenerate_faces, discard_duplicate_faces, existing_face_set
                    ):
                        continue
                    valid_face_list.append(triangle_row)
                else:
                    # Can fill array directly.
                    self.faces[face_index] = triangle_row
                    face_index += 1

        if discard_degenerate_faces or discard_duplicate_faces:
            self.faces = np.array(valid_face_list, dtype=np.uint32)

    def build_stacked_loops(self, submeshes: list[Submesh]):
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
        self.loop_normals = np.empty((total_vertex_count, 3), dtype=np.float32)
        self.loop_normals_w = np.empty((total_vertex_count, 1), dtype=np.uint8)
        self.loop_tangents = np.empty((total_vertex_count, 4), dtype=np.float32)
        self.loop_bitangents = np.empty((total_vertex_count, 4), dtype=np.float32)
        loop_vertex_colors_dict = {}  # new arrays added as new color indices are encountered
        loops_uvs_dict = {}  # new arrays added as new UV indices are encountered

        offset = 0
        for submesh in submeshes:
            vertices = submesh.vertex_arrays[0]
            field_names = vertices.dtype.names
            i = offset
            offset += len(vertices)
            j = offset
            material_uv_layers = self.material_uv_layers[submesh.material_index]

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
                self.loop_normals[i:j, 0] = vertices["normal_x"]
                self.loop_normals[i:j, 1] = vertices["normal_y"]
                self.loop_normals[i:j, 2] = vertices["normal_z"]
            else:
                # Default to upward (Y) vector.
                self.loop_normals[i:j, 0] = 0.0
                self.loop_normals[i:j, 1] = 1.0
                self.loop_normals[i:j, 2] = 0.0

            if "normal_w" in field_names:
                self.loop_normals_w[i:j, 0] = vertices["normal_w"]
            else:
                # Default to 127.
                self.loop_normals_w[i:j, 0] = 127

            if "tangent_x" in field_names:
                self.loop_tangents[i:j, 0] = vertices["tangent_x"]
                self.loop_tangents[i:j, 1] = vertices["tangent_y"]
                self.loop_tangents[i:j, 2] = vertices["tangent_z"]
                self.loop_tangents[i:j, 3] = vertices["tangent_w"]
            else:
                # Default to rightward (X) vector.
                self.loop_tangents[i:j, 0] = 1.0
                self.loop_tangents[i:j, 1] = 0.0
                self.loop_tangents[i:j, 2] = 0.0
                self.loop_tangents[i:j, 3] = 1.0

            if "bitangent_x" in field_names:
                self.loop_bitangents[i:j, 0] = vertices["bitangent_x"]
                self.loop_bitangents[i:j, 1] = vertices["bitangent_y"]
                self.loop_bitangents[i:j, 2] = vertices["bitangent_z"]
                self.loop_bitangents[i:j, 3] = vertices["bitangent_w"]
            else:
                # Default to forward (Z) vector.
                self.loop_bitangents[i:j, 0] = 0.0
                self.loop_bitangents[i:j, 1] = 0.0
                self.loop_bitangents[i:j, 2] = 1.0
                self.loop_bitangents[i:j, 3] = 1.0

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
                    if material_uv_layers:
                        # Get FLVER-wide index of this UV from its known layer name in the material.
                        uv_i = self.uv_layers.index(material_uv_layers[uv_i])
                    uv_array = loops_uvs_dict.setdefault(uv_i, np.zeros((total_vertex_count, 2), dtype=np.float32))
                    uv_array[i:j, 0] = vertices[f"uv_u_{uv_i}"]
                    uv_array[i:j, 1] = vertices[f"uv_v_{uv_i}"]

        # Could be empty lists.
        self.loop_vertex_colors = [loop_vertex_colors_dict[i] for i in sorted(loop_vertex_colors_dict)]
        self.loop_uvs = [loops_uvs_dict[i] for i in sorted(loops_uvs_dict)]

        return all_vertices

    def is_triangle_degenerate(
        self,
        triangle: tuple[int, int, int],
        discard_degenerate_faces=False,
        discard_duplicate_faces=False,
        existing_face_set: set = None,
    ):
        """Returns True if triangle has two or more identical vertex indices or already exists in some vertex order."""
        vertex_indices = self.loop_vertex_indices[triangle]
        if discard_degenerate_faces:
            if len(set(vertex_indices)) < 3:
                return True  # face with duplicate vertices
        if discard_duplicate_faces:
            if (triangle_tuple := tuple(sorted(vertex_indices))) in existing_face_set:
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
