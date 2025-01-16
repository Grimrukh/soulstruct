"""Tools for manipulating FLVER models, e.g. for Blender import/export."""

from __future__ import annotations

__all__ = [
    "SplitMeshDef",
    "MergedMesh",
]

import logging
import multiprocessing
import typing as tp
from collections import defaultdict
from dataclasses import dataclass, field

from soulstruct.utilities.misc import setdefault_lambda

import numpy as np

from .material import Material
from .face_set import FaceSet
from .mesh import FLVERMesh
from .vertex_array import VertexArray
from .vertex_array_layout import VertexArrayLayout

if tp.TYPE_CHECKING:
    from .core import FLVER

_LOGGER = logging.getLogger("soulstruct")


class SplitMeshDef(tp.NamedTuple):
    material: Material
    layout: VertexArrayLayout
    is_bind_pose: bool  # required for correct bone index handling and sets `FLVERMesh.is_bind_pose`
    kwargs: dict[str, tp.Any]
    uv_layer_names: list[str] | None = None

    def get_validated_uv_layer_names(self, global_uv_layer_names: tp.Iterable[str], index: int) -> list[str]:
        uv_count = self.layout.get_uv_count()
        uv_layer_names = self.uv_layer_names
        if not uv_layer_names:
            # Default to 'UVMap{i}' for each UV layer.
            uv_layer_names = [f"UVMap{i}" for i in range(uv_count)]
        if len(uv_layer_names) != uv_count:
            raise ValueError(
                f"UV layer names for split mesh {index} do not match layout UV count: "
                f"{self.uv_layer_names} does not have {uv_count} elements."
            )
        if any(layer_name not in global_uv_layer_names for layer_name in uv_layer_names):
            raise ValueError(
                f"Not all UV layer names given for split mesh {index} ({uv_layer_names}) appear in the `MergedMesh` "
                f"global UV layer keys ({list(global_uv_layer_names)})."
            )
        return uv_layer_names

    @classmethod
    def get_defs_from_flver(cls, flver: FLVER) -> list[SplitMeshDef]:
        """Get a list of `SplitMeshDef` instances from a FLVER's meshes.

        Makes it easy to test merging and splitting `MergedMesh` from the same FLVER.
        """
        split_mesh_defs = []
        for mesh in flver.meshes:
            kwargs = {
                "default_bone_index": mesh.default_bone_index,
                "use_backface_culling": mesh.use_backface_culling,  # from FaceSet 0 in `FLVER`
                "uses_bounding_boxes": mesh.uses_bounding_boxes,
            }

            split_mesh_defs.append(
                cls(
                    material=mesh.material,
                    is_bind_pose=mesh.is_bind_pose,
                    layout=mesh.vertex_arrays[0].layout,
                    kwargs=kwargs,
                )
            )
        return split_mesh_defs


@dataclass(slots=True)
class MergedMesh:
    """Holds data for a single merged FLVER mesh created from all its meshes. Optimized for Blender meshes.

    The merging operation identifes all unique vertices across all meshes - as defined by their position, bone
    weights, and bone indices - and creates reduced 'vertex arrays' of these data for the entire mesh. Other data
    defined by FLVER vertices are moved to 'loop arrays', as well as the indices of the new reduced vertices they use.
    Each face indexes the loops it uses, as well as the material and vertex buffer layout it uses from the FLVER
    (unchanged indices from the mesh).

    NOTE: Bone indices will be remapped to global bone indices from `mesh.bone_indices` if present. The mesh will
    not be modified and `mesh.bone_indices` will not be cleared.

    Also has the options to discard degenerate (line/point) faces and/or duplicate faces (same three vertex indices in
    any order) as they are encountered. Neither is done by default, as it may be faster for your 3D software (e.g.
    Blender) to handle any issues or exceptions caused by such faces as they arise. Both types of problematic faces
    appear frequently in vanilla FLVER files, likely as an artifact of FromSoft's own mesh-splitting algorithm, and are
    almost certainly fine to remove.

    TODO: Currently optimized for DS1, but likely works for other games (if `FLVER` class is supported for them). Also
     only acts on the first vertex array in each mesh, as I haven't encountered any multi-buffer FLVERs yet.
    """

    vertex_data: np.ndarray  # holds `position`, `bone_weights`, and `bone_indices` fields

    loop_vertex_indices: np.ndarray  # 1D array indexing into `vertex_data` (uint32)
    vertices_merged: bool  # enabled to mark when vertices are merged (making `loop_vertex_indices` trivial)

    loop_normals: np.ndarray | None  # three columns for 'x', 'y', and 'z' (float32)
    loop_normals_w: np.ndarray | None  # one column for 'w' (uint8)
    loop_tangents: list[np.ndarray]  # four columns per array for 'x', 'y', 'z', and `w` (float32)
    loop_bitangents: np.ndarray | None  # four columns for 'x', 'y', and 'z' (float32)
    loop_vertex_colors: list[np.ndarray]  # four columns per array for 'r', 'g', 'b', and 'a' (float32)
    # Maps UV layer names (which default to just 'UVMap{i}') to UV data arrays. UV layer names per merged mesh material
    # need to be passed in. Column count may vary from 2D (almost always the case) to 4D.
    loop_uvs: dict[str, np.ndarray]  # 2-4 columns per array for 'u', 'v', etc. (float32) (depending on max UV dim)

    faces: np.ndarray  # integer array of `[loop0, loop1, loop2, material_index]` rows (uint32)

    # Stored for posterity and convenient access to materials and layouts.
    flver: FLVER | None = None

    # UV layer names used by each material to assign UV data index.
    material_uv_layers: list[list[str]] | list[None] = field(default_factory=list)

    @classmethod
    def from_flver(
        cls,
        flver: FLVER,
        mesh_material_indices: tp.Sequence[int] = None,
        material_uv_layer_names: tp.Sequence[tp.Sequence[str]] = None,
        merge_vertices=True,
    ):
        """Construct merged mesh data from all `flver` meshes.

        The merged `faces` array contains a fourth column (`faces[:, 3]`) that records the 'material index' of each
        face, which is sourced directly from argument `mesh_material_indices` (which should have the same length as
        `flver.meshes`) rather than using the original FLVER material index. This allows the definition of 'material'
        in the `MergedMesh` to be set to match the caller's purposes, usually to preserve distinct combinations of
        mesh AND face set properties (e.g. `is_bind_pose` or `use_backface_culling`) that may be different for
        meshes that share the same FLVER material index.

        If `material_uv_layer_names` is given, it should be a list of list of UV layer names that correspond to the UV
        subarrays in the mesh's vertex buffer. This ensures that the UV maps across the entire merged FLVER are as
        compatible as possible, e.g. second texture UVs go into one map, lightmap UVs go into one map, etc. If not
        given, UV data will be assigned to default 'UVMap{i}' names created directly from the vertex array indices,
        which may lead to clashes in UV usage and consequently a more difficult 3D workflow (though no lost information,
        theoretically).

        If `merge_vertices = False`, the `MergedMesh` will be created without any vertex merging. This is useful for
        importing FLVERs more quickly and faithfully, but makes the models a lot more painful to edit, as adjacent faces
        with different materials -- even those that are clearly intended to represent a contiguous surface -- will not
        share their vertices or edges.
        """
        if not flver.meshes:
            raise ValueError("FLVER has no meshes. Cannot create `MergedMesh`.")

        if not mesh_material_indices:
            # By default, every mesh will be considered a separate 'material' in the `MergedMesh`.
            mesh_material_indices = list(range(len(flver.meshes)))

        valid_meshes = []
        valid_mesh_material_indices = []
        for i, mesh in enumerate(flver.meshes):
            if any(
                "position" in vertex_array.array.dtype.names
                and np.isnan(vertex_array.array["position"]).any()
                for vertex_array in mesh.vertex_arrays
            ):
                _LOGGER.warning(
                    f"Mesh {i} in FLVER with path '{flver.path_name}' has NaN vertex position data and will be "
                    f"ignored by `MergedMesh`."
                )
                continue

            valid_meshes.append(mesh)
            valid_mesh_material_indices.append(mesh_material_indices[i])

        all_vertices, loop_data_dict = cls.build_stacked_loops(
            valid_meshes, valid_mesh_material_indices, material_uv_layer_names, flver_name=flver.path_name
        )

        if merge_vertices:
            vertex_data, loop_vertex_indices, faces = cls.get_merged_vertices(
                meshes=valid_meshes,
                all_vertices=all_vertices,
                mesh_material_indices=valid_mesh_material_indices,
                loop_normals=loop_data_dict["loop_normals"],
                is_flver0=flver.version.is_flver0(),
            )
        else:
            # Vertices not reduced. We just need to stack faces, add materials, and offset their loop/vertex indices.
            total_vertex_count = all_vertices.shape[0]
            vertex_data = all_vertices
            loop_vertex_indices = np.arange(total_vertex_count, dtype=np.uint32)
            faces = cls.get_stacked_faces(
                valid_meshes,
                valid_mesh_material_indices,
                is_flver0=flver.version.is_flver0(),
            )

        return cls(
            vertex_data=vertex_data,
            loop_vertex_indices=loop_vertex_indices,
            vertices_merged=merge_vertices,
            **loop_data_dict,
            faces=faces,
            flver=flver,
        )

    @classmethod
    def from_flver_batch(
        cls,
        flvers: list[FLVER],
        merged_mesh_args: list[tuple[tuple[int, ...], tuple[tuple[str, ...], ...], bool]],
        processes: int = None,
    ) -> list[tp.Self | None]:
        """Use multiprocessing to create `MergedMesh` instances from given `FLVER` instances and args in parallel.

        Failed conversions will put `None` into list rather than `MergedMesh`.
        """
        mp_args = [
            (flver, *args) for flver, args in zip(flvers, merged_mesh_args, strict=True)
        ]

        with multiprocessing.Pool(processes=processes) as pool:
            merged_meshes = pool.starmap(_from_flver_mp, mp_args)  # blocks here until all done

        return merged_meshes

    @classmethod
    def build_stacked_loops(
        cls,
        meshes: list[FLVERMesh],
        material_indices: list[int],
        material_uv_layer_names: list[list[str]] | None,
        flver_name: str,
    ) -> tuple[np.ndarray, dict[str, np.ndarray | list[np.ndarray] | None]]:
        """Row-stack all mesh vertices' position and bone data in a single structured array for later reduction (true
        'vertex' information rather than loop information) and return it along with a dictionary of loop data arrays or
        lists of arrays.

        Uses `material_indices` and `material_uv_layer_names` to assign UV data to the correct UV layer names.

        Does nothing about faces. This processes FLVER vertices only.
        """
        # TODO: None of these fields are guaranteed in later games.
        dtype = [
            ("position", "f", 3),  # TODO: support 4D position
            ("bone_weights", "f", 4),
            ("bone_indices", "i", 4),
        ]
        total_vertex_count = sum(len(mesh.vertices) for mesh in meshes)

        all_field_names = set()
        for mesh in meshes:
            all_field_names.update(mesh.vertex_arrays[0].array.dtype.names)

        # Structured array for mixed dtypes.
        all_vertices = np.empty(total_vertex_count, dtype=dtype)  # will be fully initialized

        # These four arrays will be fully initialized.
        if "normal" in all_field_names:
            loop_normals = np.empty((total_vertex_count, 3), dtype=np.float32)
        else:
            loop_normals = None
        if "normal_w" in all_field_names:
            loop_normals_w = np.empty((total_vertex_count, 1), dtype=np.uint8)  # still 2D!
        else:
            loop_normals_w = None
        if "bitangent" in all_field_names:
            loop_bitangents = np.empty((total_vertex_count, 4), dtype=np.float32)
        else:
            loop_bitangents = None

        loop_tangents_dict = {}  # new arrays added as new tangent indices are encountered
        loop_vertex_colors_dict = {}  # new arrays added as new color indices are encountered
        loop_uvs = {}  # type: dict[str, np.ndarray]  # new arrays added as new global UV layer names used

        offset = 0
        for mesh, material_index in zip(meshes, material_indices):
            vertices = mesh.vertex_arrays[0].array
            field_names = vertices.dtype.names
            i = offset
            offset += len(vertices)
            j = offset

            mesh_vertices = all_vertices[i:j]

            if "position" in field_names:
                mesh_vertices["position"] = vertices["position"]
            else:
                _LOGGER.warning(
                    f"Mesh vertices have no 'position' data. This is unusual. Using zeroes. (FLVER {flver_name})"
                )
                mesh_vertices["position"] = 0.0

            if "bone_weights" in field_names:
                mesh_vertices["bone_weights"] = vertices["bone_weights"]
            else:  # no bone weights (standard in map piece FLVERs)
                mesh_vertices["bone_weights"] = 0.0

            if "bone_indices" in field_names:
                bone_indices = np.array(vertices["bone_indices"])  # copy to avoid modifying FLVER
                # Some FLVER files may use 255 to mark unused bone indices, rather than the standard game value of 0
                # (with zero bone weight indicating it is unused). For ease of remapping indices, we remap 255 to 0.
                bone_indices[bone_indices == 255] = 0
                if mesh.bone_indices is not None:
                    # Remap local to global bone indices (without modifying FLVER).
                    bone_indices = mesh.bone_indices[bone_indices]
                mesh_vertices["bone_indices"] = bone_indices
            else:
                # This is unusual in DS1, but not beyond that.
                mesh_vertices["bone_indices"] = 0

            if "normal" in field_names:
                loop_normals[i:j] = vertices["normal"]
            elif loop_normals is not None:
                # Default to upward (Y) vector.
                loop_normals[i:j] = [0.0, 1.0, 0.0]

            if "normal_w" in field_names:
                loop_normals_w[i:j] = vertices["normal_w"]
            elif loop_normals_w is not None:
                # Default to 127.
                loop_normals_w[i:j] = 127

            if "bitangent" in field_names:
                loop_bitangents[i:j] = vertices["bitangent"]
            elif loop_bitangents is not None:
                # Default to forward (Z) vector.
                loop_bitangents[i:j] = [0.0, 0.0, 1.0, 1.0]

            # Tangent, color, and UV arrays are only created as used. They are created with `np.zeros()` so any vertices
            # that don't use a given tangent, color, or UV index will be zeroes.
            for name in field_names:
                if name.startswith("tangent_"):
                    # TODO: Might want to default to, say, a rightward unit vector rather than zeroes.
                    t_i = int(name[-1])
                    tangent_array = setdefault_lambda(
                        loop_tangents_dict, t_i, lambda: np.zeros((total_vertex_count, 4), dtype=np.float32)
                    )
                    tangent_array[i:j] = vertices[f"tangent_{t_i}"]
                elif name.startswith("color_"):
                    c_i = int(name[-1])
                    color_array = setdefault_lambda(
                        loop_vertex_colors_dict, c_i, lambda: np.zeros((total_vertex_count, 4), dtype=np.float32)
                    )
                    color_array[i:j] = vertices[f"color_{c_i}"]
                elif name.startswith("uv_"):
                    uv_i = int(name.removeprefix("uv_"))
                    uv_layer_name = f"UVMap{uv_i}"  # default
                    if material_uv_layer_names:
                        try:
                            # Real UV names are generally 'UVTexture{i}', 'UVFur', 'UVData_WindMain', etc.
                            uv_layer_name = material_uv_layer_names[material_index][uv_i]
                        except IndexError:
                            _LOGGER.warning(
                                f"No UV layer name for material index {material_index} (UV {uv_i}, FLVER {flver_name})."
                            )
                    uv_dim = vertices[name].shape[1]
                    if uv_layer_name in loop_uvs:
                        # UV layer array already created. However, we need to check its size.
                        uv_array = loop_uvs[uv_layer_name]
                        if uv_array.shape[1] < uv_dim:
                            old_uv_dim = uv_array.shape[1]
                            _LOGGER.warning(
                                f"UV array for layer '{uv_layer_name}' in MergedMesh required a dimension upgrade from "
                                f"{old_uv_dim} to {uv_dim}. This is unusual, as named layer dimensions should be "
                                f"consistent across their usage in FLVER meshes. (FLVER {flver_name})"
                            )
                            new_uv_array = np.zeros((total_vertex_count, uv_dim), dtype=np.float32)
                            # Copy old array into new array. No need to copy past row `i`.
                            new_uv_array[:i, :old_uv_dim] = uv_array
                            uv_array = loop_uvs[uv_layer_name] = new_uv_array
                    else:
                        # First use of this UV layer name. Create loop array.
                        new_uv_array = np.zeros((total_vertex_count, uv_dim), dtype=np.float32)
                        uv_array = loop_uvs[uv_layer_name] = new_uv_array

                    # Write rows into (possibly just created or column-upgraded) UV array.
                    uv_array[i:j] = vertices[name]

        # Could be empty lists.
        loop_tangents = [loop_tangents_dict[i] for i in sorted(loop_tangents_dict)]
        loop_vertex_colors = [loop_vertex_colors_dict[i] for i in sorted(loop_vertex_colors_dict)]
        # NOTE: We don't sort `loop_uvs`. Their order shouldn't matter; the user can determine it, if needed.

        return all_vertices, dict(
            loop_normals=loop_normals,
            loop_normals_w=loop_normals_w,
            loop_tangents=loop_tangents,
            loop_bitangents=loop_bitangents,
            loop_vertex_colors=loop_vertex_colors,
            loop_uvs=loop_uvs,
        )

    @classmethod
    def get_stacked_faces(
        cls,
        meshes: list[FLVERMesh],
        mesh_material_indices: list[int],
        is_flver0: bool,
    ) -> np.ndarray:
        """Simply stacks vertices and loops and adjusts loop indices into faces. No merging.

        Faster, but makes models painful to edit. Returned vertex data and loop indices will have the same first
        dimension, since loops and vertices remain 1:1 as in the FLVER.
        """

        # Loops are 1:1 with vertices and so this is literally just `arange` of the total FLVER vertex count.

        # List of final faces: `(loop0, loop1, loop2)`, which naturally excludes duplicates. Material index added later.
        all_mesh_faces = []  # type: list[np.ndarray]
        loop_offset = 0
        for i, (mesh, material_index) in enumerate(zip(meshes, mesh_material_indices)):

            # We just need to triangulate the face set and add the material index column.
            triangles = mesh.triangulate_flver0() if is_flver0 else mesh.triangulate_flver2()  # `(n, 3)` array
            triangles += loop_offset
            mesh_faces = np.column_stack([triangles, np.full(triangles.shape[0], material_index, dtype=np.uint32)])
            all_mesh_faces.append(mesh_faces)
            loop_offset += mesh.vertices.shape[0]

        faces = np.row_stack(all_mesh_faces)
        return faces

    @classmethod
    def get_merged_vertices(
        cls,
        meshes: list[FLVERMesh],
        all_vertices: np.ndarray,
        mesh_material_indices: list[int],
        loop_normals: np.ndarray | None,
        is_flver0: bool,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """FLVER models are optimized for rendering, and so they often have many duplicate vertices across FLVER meshes,
        particularly along edges between faces that have different materials. This function attempts to restore the mesh
        to a state more suited for modelling by merging identical vertices in `all_vertices` where appropriate.

        Returns vertex data (position and bone indices/weights), a 1D array mapping the original FLVER vertices (now
        called 'loops') to that vertex data, and a 4-column array of face data (index triplets into loop data and
        a 'material index' column). All FLVER mesh faces are triangles (and not strips).

        The definition of 'identical vertices' is where the real difficulty lies here. Cases to consider:

            1. Two faces with different materials share one or two vertices with identical positions and bone weights.
            The shared vertices should definitely be merged. This is the easiest and most common case.

            2. Two faces with the same material share all three vertices and have vertex normals with SIMILAR
            ORIENTATION (separated by less than 90 degrees). These are genuine 'duplicate' faces and one of them should
            be deleted (the second one). There's no way for the game to render only one of these at a time, so they are
            likely an artifact of From's FLVER export process.

            3. Two faces with the same material share all three vertices and have vertex normals with DIFFERENT
            ORIENTATION (separated by 90 degrees or more). These are NOT 'duplicate' faces because they are likely to be
            rendered from different sides. We should NOT merge these vertices, as Blender does not support two faces
            (which we do want here) sharing the exact same vertices. TODO: This was true when using BMesh, at least.

            4. Two faces with different materials share all three vertices. If the materials have mask prefixes (in
            particular, DIFFERENT mask prefixes) like '#00#' and '#01#', then this is likely a genuine case of two faces
            that are used exclusively by different GameParam mask configurations (e.g. two copies of a face mesh with
            different skin materials). We should NOT merge these vertices, regardless of normals. However, if the two
            meshes have the same mask prefix, then they will always be rendered simultaneously and we are basically in
            the same situation as (3), in which case we should check the normals again.

        In practice, we can simplify these by simply ensuring that faces with different material display masks are NEVER
        merged, which is probably desirable anyway.

        To classify these different cases, we unfortunately need to iterate over faces, rather than just vertices, and
        manually compare vertex normals (averaged over their loop normals) with `np.dot`. We also check the display mask
        mask of each material.
        """

        # Maps raw vertex bytes (as a hash) and material display mask (could be `None`) to vertex index and the
        # normal of the first face with that display mask found that uses it. Two variant dicts; the second
        # is only used if a face has a near-inverted normal from the vertices retrieved from the first variant. (No more
        # than two vertex variants can exist, as no other face normal could possibly be different enough from BOTH of
        # the previous faces.)
        vertex_indices_normals = {}  # type: dict[tuple[int | None, bytes], tuple[int, np.ndarray]]
        inv_vertex_indices = {}  # type: dict[tuple[int | None, bytes], int]  # normal not needed here

        # Actual vertex indices (subset of row indices) to extract from `all_vertices`.
        reduced_vertex_indices = []  # type: list[int]

        vertex_count = 0  # rather than continually calling `len(reduced_vertex_indices)`

        # List of final faces: `(loop0, loop1, loop2)`, which naturally excludes duplicates. Material index added later.
        all_mesh_faces = []  # type: list[np.ndarray]

        # Array of loop vertex indices. Same length as other loop data, as face loop indices are not modified (beyond
        # offsetting them for each merged mesh).
        loop_vertex_indices = np.empty(all_vertices.shape[0], dtype=np.uint32)

        loop_offset = 0
        for i, (mesh, material_index) in enumerate(zip(meshes, mesh_material_indices)):

            display_mask = mesh.material.display_mask  # type: int | None

            triangles = mesh.triangulate_flver0() if is_flver0 else mesh.triangulate_flver2()  # `(n, 3)` array
            triangles += loop_offset
            resolved_loop_indices = set()

            for triangle in triangles:
                for loop_index in triangle:
                    # We inspect each FLVER loop index as it appears, and figure out if we can redirect it to an
                    # existing 'true vertex'. Otherwise, we create a new 'true vertex' for it.

                    if loop_index in resolved_loop_indices:
                        # This loop has already been handled by a previous FLVER face that uses it.
                        continue
                    resolved_loop_indices.add(loop_index)

                    triangle_vert = all_vertices[loop_index]
                    vertex_hash = triangle_vert.tobytes()  # "hash" of position, bone indices, and bone weights
                    vert_normal = loop_normals[loop_index] if loop_normals is not None else None

                    # Check for an existing vertex with the same display mask and same hashed (position, bone_weights,
                    # bone_indices) data.
                    try:
                        existing_vertex_index, existing_normal = vertex_indices_normals[display_mask, vertex_hash]
                    except KeyError:
                        # First time this vertex has been encountered in this display mask.
                        vertex_index = vertex_count
                        vertex_indices_normals[display_mask, vertex_hash] = (vertex_index, vert_normal)
                        loop_vertex_indices[loop_index] = vertex_index
                        reduced_vertex_indices.append(loop_index)
                        vertex_count += 1
                        continue

                    # Compare normals to see if this vertex is suitable.
                    if vert_normal is not None and np.dot(vert_normal, existing_normal) < -0.9:
                        # This face is inverted from the existing vertex. Use the inv dict (whether existing or new).
                        try:
                            existing_inv_vertex_index = inv_vertex_indices[display_mask, vertex_hash]
                        except KeyError:
                            # First time this inverted vertex has been encountered.
                            vertex_index = vertex_count
                            inv_vertex_indices[display_mask, vertex_hash] = vertex_index
                            reduced_vertex_indices.append(loop_index)
                            loop_vertex_indices[loop_index] = vertex_index
                            vertex_count += 1
                            continue

                        # Use existing inverted vertex. We do NOT check for normals here; if it turns out that another
                        # face has already used the exact same three inverted vertices, it will be treated as a true
                        # 'duplicate face' and handled accordingly (e.g. simply discarded in Blender).
                        loop_vertex_indices[loop_index] = existing_inv_vertex_index
                        continue

                    # Existing vertex is suitable (normal is sufficiently close). Again, if it turns out that multiple
                    # faces use the exact same three vertices, they will be treated as a true 'duplicate face'.
                    loop_vertex_indices[loop_index] = existing_vertex_index

            # Check for any unused FLVER vertices (now loops).
            all_loop_indices = set(range(loop_offset, loop_offset + len(mesh.vertices)))
            unresolved_loop_indices = all_loop_indices - resolved_loop_indices
            if unresolved_loop_indices:
                _LOGGER.warning(f"FLVER mesh {i} has {len(unresolved_loop_indices)} vertices never used by a face.")
                for loop_index in unresolved_loop_indices:
                    loop_vertex_indices[loop_index] = 2 ** 32 - 1  # mark as unused (-1)

            mesh_faces = np.column_stack(
                [triangles, np.full(triangles.shape[0], material_index, dtype=np.uint32)]
            )
            all_mesh_faces.append(mesh_faces)

            loop_offset += len(mesh.vertex_arrays[0])

        vertex_data = all_vertices[reduced_vertex_indices]
        faces = np.row_stack(all_mesh_faces)
        return vertex_data, loop_vertex_indices, faces

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
        self.vertex_data["position"] = self.vertex_data["position"][:, [0, 2, 1]]
        if self.loop_normals is not None:
            self.loop_normals = self.loop_normals[:, [0, 2, 1]]
        if tangents:
            for i, tangent_array in enumerate(self.loop_tangents):
                self.loop_tangents[i] = tangent_array[:, [0, 2, 1, 3]]
        if bitangents and self.loop_bitangents is not None:
            self.loop_bitangents = self.loop_bitangents[:, [0, 2, 1, 3]]

    def invert_vertex_uv(self, invert_u=False, invert_v=True, invert_w=False, invert_3=False):
        """Transform loop UV data in place by subtracting UV coordinates from 1.

        Inverts only V by default, as this is standard for Blender.

        TODO: Should later indices be inverted in Blender?
        """
        for loop_uv_array in self.loop_uvs.values():
            if invert_u:
                loop_uv_array[:, 0] = 1.0 - loop_uv_array[:, 0]
            if invert_v:
                loop_uv_array[:, 1] = 1.0 - loop_uv_array[:, 1]
            if invert_w:
                # Does not check shape. User should know UV dimensionality.
                loop_uv_array[:, 2] = 1.0 - loop_uv_array[:, 2]
            if invert_3:
                # Does not check shape. User should know UV dimensionality.
                loop_uv_array[:, 3] = 1.0 - loop_uv_array[:, 3]

    def normalize_normals(self):
        """Transform loop normal data in place by normalizing them.

        As normals are typically compressed in FLVER vertex buffers, the decompressed normals are not normalized by
        Soulstruct automatically, because this is lossy. However, Blender expects normalized vectors for its normal
        data, so this method is provided to normalize them in-place.
        """
        if self.loop_normals is None:
            return
        self.loop_normals /= np.linalg.norm(self.loop_normals, axis=1, keepdims=True)

    def normalize_tangents(self):
        """Ditto for tangents. See above."""
        for i in range(len(self.loop_tangents)):
            self.loop_tangents[i] /= np.linalg.norm(self.loop_tangents[i], axis=1, keepdims=True)

    def round_normals(self, decimals=3):
        """Round loop normal data in place to a given number of decimal places.

        Normal data exported from a program like Blender is probably much higher-resolution than the compressed normals
        written to most FLVER files (e.g., only 255 values per coordinate). This will cause loops to be considered
        "unique" too aggressively when splitting meshes and creating vertex arrays. Rounding the normals to a lower
        resolution can help to mitigate this issue.
        """
        if self.loop_normals is None:
            return
        self.loop_normals = np.round(self.loop_normals, decimals=decimals)

    def round_tangents(self, decimals=3):
        """Ditto for tangents. See above."""
        for i in range(len(self.loop_tangents)):
            self.loop_tangents[i] = np.round(self.loop_tangents[i], decimals=decimals)

    def round_uvs(self, decimals=5):
        """UVs will likely need less rounding (and less often), but it may still cause issues if tiny differences in
        UVs that will disappear under FLVER compression anyway were inflating the vertex counts of meshes.

        Note that the default value of `decimals` is higher here, as these are usually compressed to 16-bit, not 8-bit.
        """
        for key, loop_uv_array in self.loop_uvs.items():
            self.loop_uvs[key] = np.round(loop_uv_array, decimals=decimals)

    def split_mesh(
        self,
        split_mesh_defs: list[SplitMeshDef],
        use_mesh_bone_indices=True,
        max_bones_per_mesh=38,
        unused_bone_indices_are_minus_one=False,
        normal_tangent_dot_threshold=1.0,
        max_mesh_vertex_count=0,
        is_flver0=False,
    ) -> list[FLVERMesh]:
        """Splits merged mesh into FLVER meshes.

        `split_mesh_defs` must be a list of FLVER `Material` instances, appropriate layouts, and combined
        `Mesh/FaceSet` kwargs for each value that appears in `faces[:, 3]`. The merged mesh will be split based on
        these values (and maybe further split by bone maximum if `use_mesh_bone_indices == True`) and the created
        `Mesh` and `FaceSet` instances will take their materials, layouts, and miscellaneous kwargs from this list.

        If `uv_layer_names` is given for a `split_mesh_defs` element, it should be a list of list of UV layer
        names that indicate which keys in `MergedMesh.loop_uvs` are used by each corresponding mesh. This will
        ensure that each FLVER mesh vertex buffer can tightly pack only the global arrays that it uses: for
        example, a lightmapped one-texture mesh material may have UV layer names `['UVTexture0', 'UVLightmap']`,
        which will become its `uv_0` and `uv_1` vertex buffer fields, respectively. If `mesh_uv_layer_names` is
        not given, each mesh will simply look up UV keys 'UVMap{i}' in `MergedMesh.loop_uvs` for `i < n`,
        where `n` is the number of UVs it uses (determined by its given layout). This is fine, assuming that the
        `MergedMesh` was also constructed this way, with no UV layer names given.

        As with `MergedMesh.from_flver()`, the definition of 'material' here should comprise any reason that the mesh
        needs to be split, and `faces[3]` should be set accordingly. Two split meshes may use the same FLVER
        material in `split_mesh_defs`, for example, yet have different `is_bind_pose` values or `face_sets[
        0].use_backface_culling` etc. The `FLVER` class will efficiently remove any duplicate FLVER materials or
        layouts when packed.

        If a mesh material index has no faces, it will be ignored.

        `is_rigged` must appear in each mesh kwargs dictionary, as it is used to determine bone index style. For
        modern `FLVER` format, it will also be used to set
        TODO: Still not 100% sure if there are any FLVERs that use 'bind pose' for some meshes but not others. From
         memory, I found a few cut content objects or something, but only checked the bool and not the indices.

        If `unused_bone_indices_are_minus_one` is True, it will be assumed that the bone indices in
        `self.vertex_bone_indices` have been set to -1 when unused, rather than the FLVER standard of zero (which can be
        confused with actual use of bone 0 and requires weight inspection to confirm). This makes mesh splitting easier
        when mesh bone indices are used (with maximums); all the -1 indices will be replaced with zeroes in the final
        split mesh arrays.

        If `normal_tangent_dot_threshold` is less than 1.0, mesh loops will be considered equivalent if their
        normal and tangent (and bitangent) vectors' respective dot products are greater than this value. Note that this
        incurs a small performance penalty. Vertex POSITION must always be identical for two loops to be considered
        equivalent.

        If `max_mesh_vertex_count` is >0, an error will be raised if any mesh has more than this number of
        vertices. This is useful for ensuring that meshes are not too large for the game to handle, as earlier games
        restrict face vertex indices to being 16-bit.
        """
        if use_mesh_bone_indices and max_bones_per_mesh < 3:
            raise ValueError("`max_bones_per_mesh` must be >= 3 (and realistically should be much higher).")

        # Split each `SplitMeshDef` into its component information for efficiency.
        mesh_materials = [mesh_def.material for mesh_def in split_mesh_defs]
        mesh_layouts = [mesh_def.layout for mesh_def in split_mesh_defs]
        mesh_is_bind_pose = [mesh_def.is_bind_pose for mesh_def in split_mesh_defs]
        mesh_kwargs = [mesh_def.kwargs for mesh_def in split_mesh_defs]
        mesh_uv_layer_names = [
            mesh_def.get_validated_uv_layer_names(self.loop_uvs, i)
            for i, mesh_def in enumerate(split_mesh_defs)
        ]

        # Check `face_set_count` is within range for all mesh kwargs.
        for i, kwargs in enumerate(mesh_kwargs):
            if "face_set_count" in kwargs:
                if not 1 <= kwargs["face_set_count"] <= 3:
                    raise ValueError(f"Mesh {i} `face_set_count` must be between 1 and 3 (inclusive) for splitting.")

        # We construct two material dtypes: one that uses global UV layer names, and the true one that uses tightly
        # packed 'uv_{i}' UV names. These names are the only difference, so we can just reassign the dtype at the end.
        global_uv_material_dtypes = []
        true_material_dtypes = []
        for layout, uv_layer_names in zip(mesh_layouts, mesh_uv_layer_names):
            true_dtype = layout.get_dtypes()[1]  # decompressed fields
            global_dtype_fields = []
            for field_name, (field_fmt, field_index) in true_dtype.fields.items():
                if field_name.startswith("uv_"):
                    local_uv_index = int(field_name.removeprefix("uv_"))
                    global_uv_layer_name = uv_layer_names[local_uv_index]
                    global_dtype_fields.append((global_uv_layer_name, field_fmt))
                else:
                    global_dtype_fields.append((field_name, field_fmt))
            global_dtype = np.dtype(global_dtype_fields)
            global_uv_material_dtypes.append(global_dtype)
            true_material_dtypes.append(true_dtype)

        # We construct a `dtype` that includes all fields from every material.
        # Order doesn't matter here, as materials will retrieve the combined columns they need by name, not index.
        combined_dtype_fields = []
        for dtype in global_uv_material_dtypes:
            for field_name, (field_fmt, field_index) in dtype.fields.items():
                if (field_name, field_fmt) not in combined_dtype_fields:
                    combined_dtype_fields.append((field_name, field_fmt))
        combined_dtype = np.dtype(combined_dtype_fields)

        # First, construct a big merged array of all FLVER-style loops (i.e. containing vertex AND loop data per row
        # rather than being true face corners). Vertex data (position and bones) will repeat in every loop that uses it.
        # Note that UV layers still have their global names; final split meshes will rename them `uv_0`, `uv_1`, etc.
        merged_loops = self.get_combined_loop_data(combined_dtype)

        # Stores tuples of `(material_index, loop_array, mesh_bone_indices)` for each mesh. Every three rows in
        # `loop_array` comprises a unique face, so face indices are implicit.
        # These are further subsplit by bone maximum if applicable. Loop arrays have not yet been reduced down to unique
        # rows only (happens afterward).
        # NOTE: Data will be EXTRACTED from `merged_loops` by index, making no assumptions about which meshes share
        # loop data (which will never happen when `MergedMesh` is constructed from a single FLVER, but may in custom
        # data).
        split_mesh_info = []  # type: list[tuple[int, np.ndarray, tp.Optional[np.ndarray]]]

        merged_loop_views = {}  # minor optimization (construct each dtype-dependent view only once)
        for material_index, global_uv_material_dtype in enumerate(global_uv_material_dtypes):

            # Split `faces` and indexed `merged_loops` by material index (column 3).
            mesh_faces = self.faces[self.faces[:, 3] == material_index][:, :3]  # `(n, 3)` array
            if len(mesh_faces) == 0:
                # This is an unused material index. Do not create any meshes.
                continue
            mesh_loop_indices = mesh_faces.ravel()  # all loop indices used by faces in this mesh

            # Loop data access. This makes no assumptions about how 'loopy' the loop data in the `MergedMesh` is. If
            # loaded from a FLVER, many faces will already index the same 'loops', but this may not be the case for
            # custom data (like true loops from a Blender mesh). This array will always have length `(3 * n, 3)`, where
            # `n` is the face count; faces with overlapping loop indices will just have duplicate rows, all of which
            # will be reduced to unique rows below. The face indices at this stage are also implicit: [0, 1, 2, 3, ...]
            if global_uv_material_dtype.names not in merged_loop_views:
                # No point extracting the same view multiple times.
                merged_loop_views[global_uv_material_dtype.names] = merged_loops[list(global_uv_material_dtype.names)]
            dtype_view = merged_loop_views[global_uv_material_dtype.names]

            # Every three rows corresponds to a single face (will have many duplicates that are removed below).
            mesh_loops = dtype_view[mesh_loop_indices]

            # Not all FLVER materials/meshes use bone indices. (Some use `normal_w` as a single bone index.)
            # TODO: Can `normal_w` bone indices still be local? I suspect (and currently assume) not.
            uses_vertex_bone_indices = "bone_indices" in global_uv_material_dtype.names

            if uses_vertex_bone_indices and use_mesh_bone_indices:
                # We may need to split this mesh due to max bone count.
                split_mesh_info += self.subsplit_faces(
                    material_index,
                    mesh_loops,
                    is_rigged=mesh_is_bind_pose[material_index],
                    max_bones_per_mesh=max_bones_per_mesh,
                    unused_bone_indices_are_minus_one=unused_bone_indices_are_minus_one,
                )
            else:
                # Vertex bone indices are global and have no maximum count (or are missing altogether).
                split_mesh_info.append((material_index, mesh_loops, None))

        split_meshes = []

        for material_index, mesh_loops, mesh_bone_indices in split_mesh_info:
            kwargs = mesh_kwargs[material_index].copy()  # may be used by multiple subsplit meshes

            # Duplicate loop data is finally removed here, giving the true vertex data stored in the FLVER mesh.

            if normal_tangent_dot_threshold >= 1.0:
                # Use `np.unique` to remove EXACT duplicate vertices only.
                mesh_vertices, face_vertex_indices = self.loops_to_flver_vertices_exact(mesh_loops)
            else:
                # Iterate over all loops and compare their normals and tangents to determine if they are 'unique'.
                mesh_vertices, face_vertex_indices = self.loops_to_flver_vertices_approx(
                    mesh_loops, normal_tangent_dot_threshold
                )

            if 0 < max_mesh_vertex_count < len(mesh_vertices):
                raise ValueError(
                    f"Mesh {material_index} has {len(mesh_vertices)} vertices, which is greater than the "
                    f"maximum of {max_mesh_vertex_count}. You need to simplify this mesh (material name "
                    f"{mesh_materials[material_index].name}) or try lowering `normal_tangent_dot_max` to merge "
                    f"vertices with similar normals/tangents more aggressively (current value = "
                    f"{normal_tangent_dot_threshold})."
                )

            if mesh_bone_indices is not None and unused_bone_indices_are_minus_one:
                # Replace -1 unused bone indices with 0 for FLVER.
                bone_indices = mesh_vertices["bone_indices"]
                bone_indices[bone_indices == -1] = 0

            # Reassign true dtype to vertex array (with local 'uv_{i}' names instead of merged global UV layer names).
            mesh_vertices = mesh_vertices.astype(true_material_dtypes[material_index], copy=False)

            vertex_array = VertexArray(array=mesh_vertices, layout=mesh_layouts[material_index])

            face_set_count = kwargs.pop("face_set_count", 1)
            face_set = FaceSet.from_triangles(
                face_vertex_indices, use_backface_culling=kwargs.pop("use_backface_culling")
            )
            material = mesh_materials[material_index]
            mesh = FLVERMesh(
                face_sets=[face_set],
                material=material,
                vertex_arrays=[vertex_array],
                bone_indices=mesh_bone_indices,
                **kwargs,  # e.g. 'default_bone_index', 'uses_bounding_boxes', 'is_bind_pose'
            )
            if not is_flver0:
                # No point refreshing bounding boxes for FLVER0 versions.
                mesh.refresh_bounding_boxes()

            if face_set_count > 1:  # already validated as 2 or 3 only
                # Duplicate default face set (0) to LOD levels 1 and/or 2, setting `FaceSet.flags` appropriately.
                base_face_set = mesh.face_sets[0]
                for i in range(1, face_set_count):
                    face_set = FaceSet(
                        flags=i,  # 1 or 2
                        is_triangle_strip=base_face_set.is_triangle_strip,  # False
                        use_backface_culling=base_face_set.use_backface_culling,
                        unk_x06=base_face_set.unk_x06,
                        vertex_indices=base_face_set.vertex_indices,  # don't bother copying array
                    )
                    mesh.face_sets.append(face_set)

            split_meshes.append(mesh)

        return split_meshes

    @staticmethod
    def loops_to_flver_vertices_exact(mesh_loops: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Get unique loops (to become FLVER 'vertices') and face vertex indices (to become FLVER 'faces').

        `mesh_loops` input must be true loops, in the sense that every three rows defines one face.

        Requires exact uniqueness, which can inflate FLVER vertex counts due to tiny differences in normal/tangent
        vectors or any other data, especially when that data is compressed to 8 or 16 bits in the FLVER anyway.

        Note that `np.unique` automatically sorts the array, so we need to use `return_index` to de-sort it, then use
        `return_inverse` (after also de-sorting it) to get the final face vertex indices.
        """

        # Since `np.unique()` automatically and unstoppably sorts the array, we need to use `return_index`
        # to UNSORT it, then `return_inverse` (after also unsorting) to get the final face vertex indices.
        mesh_vertices, first_indices, face_vertex_indices = np.unique(
            mesh_loops, return_index=True, return_inverse=True, axis=0
        )
        # Get the sorting indices for `first_indices`. The elements in this are the indices of elements that would
        # produce a sorted version of `first_indices`:
        sorting_indices = np.argsort(first_indices)
        # Apply those to `mesh_vertices` (sorted output of `np.unique` above) to unsort it:
        mesh_vertices = mesh_vertices[sorting_indices]
        # Get the inverse sorting indices, i.e. the indices of elements in `first_indices`:
        inverse_sorting_indices = np.argsort(sorting_indices)
        # Apply to `face_vertex_indices` to update them to index into the unsorted `mesh_vertices`:
        face_vertex_indices = inverse_sorting_indices[face_vertex_indices]

        return mesh_vertices, face_vertex_indices

    @staticmethod
    def loops_to_flver_vertices_approx(
        mesh_loops: np.ndarray, max_dot_product=0.9999
    ) -> tuple[np.ndarray, np.ndarray]:
        """Get unique loops (to become FLVER 'vertices') and face vertex indices (to become FLVER 'faces'), but consider
        any normal or tangent vectors (NOT vertex position) to be identical if their dot product is greater than
        `max_dot_product`.
        """
        mesh_vertices = []
        mesh_vertices_dict = {}  # type: dict[int, int]  # maps vertex hashes to indices
        mesh_vertices_by_position = defaultdict(lambda: [])  # type: defaultdict[tuple, list[tuple[tp.Any, int]]]
        face_vertex_indices = []

        vector_fields = [f for f in mesh_loops.dtype.names if f.startswith(("normal", "tangent_", "bitangent"))]
        non_vector_fields = [f for f in mesh_loops.dtype.names if f not in vector_fields and f != "position"]

        for loop in mesh_loops:

            vertex_hash = loop.tobytes()
            if vertex_hash in mesh_vertices_dict:
                # Exact vertex already exists. Reuse it.
                face_vertex_indices.append(mesh_vertices_dict[vertex_hash])
                continue

            # Check if a similar vertex (in normal and tangents) already exists.
            pos = tuple(loop["position"])
            found_similar = False
            if pos in mesh_vertices_by_position:
                for existing_vertex, existing_vertex_i in mesh_vertices_by_position[pos]:
                    if non_vector_fields and not np.all(loop[non_vector_fields] == existing_vertex[non_vector_fields]):
                        # Not an exact match.
                        break
                    if vector_fields and not all(
                        np.dot(loop[f], existing_vertex[f]) > max_dot_product for f in vector_fields
                    ):
                        # Not an approximate match.
                        break
                    # All vectors are similar enough and other fields match. Re-use this vertex.
                    mesh_vertices_dict[vertex_hash] = existing_vertex_i
                    face_vertex_indices.append(existing_vertex_i)
                    found_similar = True
                    break
                if found_similar:
                    continue

            # New vertex found. Not similar to any previous vertices.
            vertex_index = len(mesh_vertices)
            mesh_vertices.append(loop)
            mesh_vertices_dict[vertex_hash] = vertex_index
            mesh_vertices_by_position[pos].append((loop, vertex_index))
            face_vertex_indices.append(vertex_index)

        mesh_vertices_array = np.array(mesh_vertices, dtype=mesh_loops.dtype)
        face_vertex_indices_array = np.array(face_vertex_indices, dtype=np.uint32)
        return mesh_vertices_array, face_vertex_indices_array

    @classmethod
    def subsplit_faces(
        cls,
        material_index: int,
        mesh_loops: np.ndarray,
        is_rigged: bool,
        max_bones_per_mesh: int,
        unused_bone_indices_are_minus_one: bool,
    ) -> list[tuple[int, np.ndarray, np.ndarray]]:
        """Takes arrays of split faces, loops, and bone indices and returns a tuple of arrays of subsplit faces, loops,
        and bone indices, which can be appended to the appropriate lists for each material rather than a single
        mesh."""
        subsplit_face_indices = [0]
        subsplit_bone_indices = []

        bone_indices = mesh_loops["bone_indices"]  # copied below if modified

        if is_rigged:
            # Up to four unique bones per vertex, so we need to more carefully collect as we go.
            if not unused_bone_indices_are_minus_one:
                # Set all unused bone indices to -1, to distinguish them from true use of bone 0. Ideally, the
                # user can do this themselves while they are constructing their merged mesh (e.g. from Blender)
                # to save time here, as this requires two new array creations.
                bone_weights = mesh_loops["bone_weights"]
                bone_indices = bone_indices.copy()  # NOT modified in-place
                bone_indices[bone_weights == 0.0] = -1

        # Loops are still genuine loops, i.e. every three represent one triangle with 12 total bone indices.
        all_face_bone_indices = bone_indices.reshape((-1, 12))

        # Rather than filtering out values of -1, we make sure it's always in the set, and offset the check.
        # Slightly suboptimal for `is_rigged = False`, as every face should only have up to 3 bones, but
        # worth the complexity trade-off.
        max_bones = max_bones_per_mesh + 1
        unique_indices = {-1}
        for face_index, face_bone_indices in enumerate(all_face_bone_indices):
            new_indices = unique_indices | set(face_bone_indices)
            if len(new_indices) > max_bones:
                # This row would exceed the limit. Start a new mesh.
                subsplit_face_indices.append(face_index)
                subsplit_bone_indices.append(np.array(sorted(unique_indices - {-1})))
                unique_indices = {-1} | set(face_bone_indices)
            else:
                # Can continue.
                unique_indices = new_indices

        # Finish final subsplit. Face indices for meshes that don't need sub-splitting will just be `[0, n]`.
        subsplit_face_indices += [len(mesh_loops) // 3]
        subsplit_bone_indices.append(np.array(sorted(unique_indices - {-1})))

        all_subsplits = []
        for i, face_start in enumerate(subsplit_face_indices[:-1]):
            face_end = subsplit_face_indices[i + 1]
            loops_start, loops_end = face_start * 3, face_end * 3
            subsplit_loops = mesh_loops[loops_start:loops_end]

            subsplit_global_bone_indices = bone_indices[loops_start:loops_end, :]
            subsplit_loops["bone_indices"] = cls.make_bone_indices_local(
                subsplit_global_bone_indices, subsplit_bone_indices[i]
            )

            all_subsplits.append((material_index, subsplit_loops, subsplit_bone_indices[i]))

        return all_subsplits

    def get_combined_loop_data(self, combined_dtype: np.dtype):
        """Combine the appropriate loop data, in the given order, into a single structured array for indexing by loop
        row ('FLVER vertex row') or field name (so mesh materials can retrieve only the fields they need).

        The returned array, therefore, is essentially a merged version of the complete FLVER `mesh.vertices` arrays
        for all meshes using a 'maximal' dtype.

        The only exception is the UV data arrays, whose fields still have their global names (e.g. 'UVTexture0' or
        'UVMap1'). The final split meshes will simply rename the fields they actually use and discard the remainder.

        Note that the order of fields in `combined_dtype` likely won't matter if materials are using their own subset
        dtypes anyway.
        """
        loop_count = len(self.loop_vertex_indices)
        combined_array = np.empty(loop_count, dtype=combined_dtype)  # will be fully initialized

        names = set(combined_dtype.names)  # order is unimportant for initialization

        if "position" in names:
            positions = self.vertex_data["position"][self.loop_vertex_indices]  # (loop_count, 3)
            combined_array["position"] = positions
        if "bone_weights" in names:
            bone_weights = self.vertex_data["bone_weights"][self.loop_vertex_indices]  # (loop_count, 4)
            combined_array["bone_weights"] = bone_weights
        if "bone_indices" in names:
            bone_indices = self.vertex_data["bone_indices"][self.loop_vertex_indices]  # (loop_count, 4)
            combined_array["bone_indices"] = bone_indices
        if "normal" in names:
            if self.loop_normals is None:
                raise ValueError("`MergedMesh.loop_normals` is None, but 'normal' appears in full FLVER dtype.")
            combined_array["normal"] = self.loop_normals
        if "normal_w" in names:
            if self.loop_normals_w is None:
                raise ValueError("`MergedMesh.loop_normals_w` is None, but 'normal_w' appears in full FLVER dtype.")
            combined_array["normal_w"] = self.loop_normals_w
        if "bitangent" in names:
            if self.loop_bitangents is None:
                raise ValueError("`MergedMesh.loop_bitangents` is None, but 'bitangent' appears in full FLVER dtype.")
            combined_array["bitangent"] = self.loop_bitangents

        tangent_names = [n for n in names if n.startswith("tangent_")]
        for tangent_name in tangent_names:
            t_i = int(tangent_name[-1])
            combined_array[f"tangent_{t_i}"] = self.loop_tangents[t_i]  # (loop_count, 4)

        # Combined array still uses global UV layer names.
        for uv_layer_name in self.loop_uvs:
            combined_array[uv_layer_name] = self.loop_uvs[uv_layer_name]

        color_names = [n for n in names if n.startswith("color_")]
        for color_name in color_names:
            c_i = int(color_name[-1])
            combined_array[f"color_{c_i}"] = self.loop_vertex_colors[c_i]  # (loop_count, 4)

        return combined_array

    @staticmethod
    def make_bone_indices_local(bone_indices: np.ndarray, mesh_bone_indices: np.ndarray):
        lo = min(bone_indices.min(), mesh_bone_indices.min())
        hi = max(bone_indices.max(), mesh_bone_indices.max())
        lut = np.zeros(hi - lo + 1, dtype=np.int64)
        lut[mesh_bone_indices - lo] = np.arange(len(mesh_bone_indices))
        return lut[bone_indices - lo]

    @staticmethod
    def unique(array: np.ndarray, max_value=None):
        """More efficient `np.unique()` (for reasonable array lengths) that uses masking and does NOT sort."""
        max_value = max_value or np.max(array) + 1
        used = np.zeros(max_value, dtype=np.uint8)
        used[array] = 1
        return np.argwhere(used == 1)[:, 0]


def _from_flver_mp(
    flver: FLVER,
    mesh_material_indices: list[int],
    material_uv_layer_names: list[list[str]],
    merge_vertices: bool,
) -> MergedMesh | None:
    if not flver.meshes:
        _LOGGER.info(f"FLVER '{flver.path_name}' has no meshes. No MergedMesh created.")
        return None
    try:
        return MergedMesh.from_flver(flver, mesh_material_indices, material_uv_layer_names, merge_vertices)
    except Exception as ex:
        _LOGGER.error(f"Failed to load FLVER '{flver.path_name}' as MergedMesh: {ex}")
        return None
