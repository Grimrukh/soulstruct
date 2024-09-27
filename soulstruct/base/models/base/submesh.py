from __future__ import annotations

__all__ = ["BaseSubmesh"]

import typing as tp
from dataclasses import dataclass

import numpy as np

from soulstruct.base.models.base.vertex_array import BaseVertexArray
from .face_set import FaceSet
from .material import BaseMaterial
from .vertex_array_layout import BaseVertexArrayLayout

MATERIAL_T = tp.TypeVar("MATERIAL_T", bound=BaseMaterial)
LAYOUT_T = tp.TypeVar("LAYOUT_T", bound=BaseVertexArrayLayout)
ARRAY_T = tp.TypeVar("ARRAY_T", bound=BaseVertexArray)


@dataclass(slots=True)
class BaseSubmesh(tp.Generic[MATERIAL_T, LAYOUT_T, ARRAY_T]):
    """FLVER0 submesh, which has only one built-in 'face set' and is simplified in other ways.

    To unify these classes in Python, we actually use a single `FaceSet` here to store the vertex indices and other
    settings. We don't permit the `flags` or `unk_x06` fields to be set, as they are not used in `FLVER0`.
    """

    material: MATERIAL_T
    default_bone_index: int
    bone_indices: np.ndarray | None
    vertex_arrays: list[ARRAY_T]  # only ever has one element
    face_sets: list[FaceSet]

    # Set by `BaseFLVER` on initial creation, for convenience. Can be updated with `flver.refresh_submesh_indices()`.
    index: int = -1
    # Enabled by Soulstruct when a bad layout was (attempted to be) fixed.
    layout_fixed: bool = False
    # Enabled by Soulstruct when trying to read a vertex array from a FLVER (usually DS1R) with the wrong layout.
    invalid_layout: bool = False

    @property
    def vertices(self) -> np.ndarray:
        """Shortcut for accessing the data of the first vertex array (generally the only array)."""
        return self.vertex_arrays[0].array

    @property
    def vertices_dtype(self) -> np.dtype:
        return self.vertices.dtype

    @property
    def layout(self) -> LAYOUT_T:
        """Shortcut for accessing the layout of the first vertex array (generally the only array)."""
        return self.vertex_arrays[0].layout

    @property
    def use_backface_culling(self) -> bool:
        if not self.face_sets:
            raise ValueError("Submesh has no face sets to check `use_backface_culling`.")
        cull = self.face_sets[0].use_backface_culling
        if any(face_set.use_backface_culling != cull for face_set in self.face_sets):
            raise ValueError("Submesh has multiple face sets with different `use_backface_culling` values.")
        return cull

    @use_backface_culling.setter
    def use_backface_culling(self, value: bool):
        for face_set in self.face_sets:
            face_set.use_backface_culling = value

    def validate_unique_data_types(self):
        """Check that per-mesh unique `MemberType`s do not occur more than once among all members of all arrays."""
        existing_types = set()
        for vertex_array in self.vertex_arrays:
            for data_type in vertex_array.layout:
                if data_type.unique:
                    name = data_type.__class__.__name__
                    if name in existing_types:
                        raise ValueError(
                            f"Unique vertex data type `{name} found more than once across all vertex arrays of Submesh."
                        )
                    existing_types.add(name)

    def triangulate(self, include_degenerate_faces=False) -> np.ndarray:
        """Shortcut for triangulating first face set."""
        uses_0xffff_separators = len(self.vertices) < 0xFFFF
        return self.face_sets[0].triangulate(uses_0xffff_separators, include_degenerate_faces)

    def to_obj(self, name="Submesh", vertex_offset=0, vertex_array=0) -> str:
        """Convert mesh vertices, normals, UVs, and faces to an OBJ string.

        Use `vertex_offset` to offset all vertex indices in face definitions (e.g. if other meshes' vertices have
        been defined in the same file).
        """
        lines = [f"o {name}"]

        # Check if vertices record array has 'uv_u_1' field:
        vertex = self.vertices[0]
        if "uv_u_1" in vertex:
            raise NotImplementedError("Cannot convert mesh to OBJ because one or more vertices has multiple UVs.")
        array = self.vertex_arrays[0]

        for position in array[[f"position_{c}" for c in "xyz"]]:
            pos_str = " ".join(str(x) for x in position)
            lines.append(f"v {pos_str}")
        for normal in array[[f"normal_{c}" for c in "abcd"]]:
            normal_str = " ".join(str(x) for x in normal)
            lines.append(f"vn {normal_str}")
        for uv in array[["uv_u_0", "uv_v_0"]]:
            uv_str = " ".join(str(x) for x in uv)
            lines.append(f"vt {uv_str}")
        for i, face_set in enumerate(self.face_sets):
            lines.append(f"# Face Set {i}")
            triangles = face_set.triangulate(uses_0xffff_separators=len(self.vertex_arrays[vertex_array]) <= 0xFFFF)
            for j in range(0, len(triangles), 3):
                # TODO: Are these UV/normal assignments correct, given that each vertex has one?
                face = " ".join("/".join([str(v + vertex_offset + 1)] * 3) for v in triangles[j:j + 3])
                lines.append(f"f {face}")
        return "\n".join(lines)

    def sort_bone_indices(self):
        """Sort `bone_indices` in-place, if defined, and re-index all vertex data to match."""

        if self.bone_indices is None:
            return  # this submesh has global vertex bone indices

        sorted_indices = np.argsort(self.bone_indices)
        # Sort now, and use `sorted_indices` to remap vertex data below.
        self.bone_indices = self.bone_indices[sorted_indices]

        for vertex_array in self.vertex_arrays:
            try:
                bone_indices = vertex_array["bone_indices"]
            except ValueError:  # no bone indices
                continue

            # Check map piece 'pose' case, where weights are missing:
            try:
                bone_weights = vertex_array["bone_weights"]
            except ValueError:  # no weights
                # Map Piece case: all four indices should be the same number (all used) and can be safely re-indexed.
                vertex_array["bone_indices"] = sorted_indices[bone_indices]
            else:
                # Rigged case: at least one bone weight is non-zero, and we need to check which ones in order to
                # distinguish use of bone 0 from an unused bone index, unfortunately.

                # Get indices of all vertices with non-zero bone weights.
                used_indices = np.nonzero(bone_weights)[0]  # (n, 4) mask array
                vertex_array["bone_indices"][used_indices] = sorted_indices[bone_indices[used_indices]]

    def local_to_global_bone_indices(self):
        """Transforms `vertex_array` in-place by replacing all vertex bone indices with the global bone index in
        `mesh.bone_indices` that the vertex indexes, then clearing `self.bone_indices`.

        Will raise a `ValueError` if `mesh.bone_indices` is already None (implying vertex bone indices are already
        global).
        """
        if self.bone_indices is None:
            raise ValueError(
                "Cannot convert local vertex bone indices to global because `mesh.bone_indices` is None, suggesting "
                "that the vertex bone indices are already global FLVER bone indices."
            )
        for vertex_array in self.vertex_arrays:
            if not vertex_array.has_field("bone_indices"):
                continue
            # Simple re-index into global indices.
            vertex_array.array["bone_indices"] = self.bone_indices[vertex_array.array["bone_indices"]]
        self.bone_indices = None
