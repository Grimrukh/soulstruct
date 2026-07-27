from __future__ import annotations

__all__ = ["FaceSetFlags", "FaceSet"]

import logging
from dataclasses import dataclass, field
from enum import IntEnum

import numpy as np

from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger(__name__)


class FaceSetFlags(IntEnum):

    LodLevel1 = 0b0000_0001
    LodLevel2 = 0b0000_0010
    EdgeCompressed = 0b0100_0000
    MotionBlur = 0b1000_0000

    def has_flag(self, flag_int: int):
        return flag_int & self.value


@dataclass(slots=True)
class FaceSet:

    class STRUCT(BinaryStruct):

        _pad1: bytes = binary_pad(3, init=False)
        flags: byte
        is_triangle_strip: bool
        use_backface_culling: bool
        unk_x06: short
        _vertex_indices_count: int
        _vertex_indices_offset: int
        # NOTE: Fields stop here for FLVER versions < 0x20005, which are not supported by Soulstruct.
        _vertex_indices_length: int  # len(self.vertex_indices) * vertex_index_bit_size // 8
        _pad2: bytes = binary_pad(4, init=False)
        _vertex_index_bit_size: int = binary(asserted=[0, 16, 32])  # 0 means size is set by FLVER header
        _pad3: bytes = binary_pad(4, init=False)

    flags: int  # seems to indicate LoD level
    is_triangle_strip: bool
    use_backface_culling: bool
    unk_x06: int

    # Vertex indices could be in triangle strip format (1D) or simply an `(n, 3)` array of triangles. Number of
    # dimensions must match setting of `is_triangle_strip` upon export.
    # Note that the `dtype` is always `uint32`, even if FLVER read/written vertex size is 16, for simplicity. It is
    # cast to the correct `dtype` before packing.
    vertex_indices: np.ndarray = field(default_factory=lambda: np.empty(0, dtype=np.uint32))

    @classmethod
    def from_flver_reader(
        cls, reader: BinaryReader, header_vertex_index_bit_size: int, vertex_data_offset: int
    ) -> FaceSet:
        face_set_struct = cls.STRUCT.from_bytes(reader)

        # NOTE: We don't use the `_vertex_indices_length` field, since length is computable from size * count, but the
        # game DOES use it and WILL crash if it's not set correctly.

        vertex_index_bit_size = face_set_struct.pop("_vertex_index_bit_size")
        if vertex_index_bit_size == 0:
            # Use global FLVER size.
            vertex_index_bit_size = header_vertex_index_bit_size

        if vertex_index_bit_size == 8:
            raise NotImplementedError("Soulstruct cannot read edge-compressed FLVER face sets.")
        elif vertex_index_bit_size not in {16, 32}:
            raise ValueError(f"Unsupported face set index size: {vertex_index_bit_size}")

        vertex_indices_count = face_set_struct.pop("_vertex_indices_count")
        vertex_indices_offset = face_set_struct.pop("_vertex_indices_offset")

        vertex_indices_data = reader.read(
            vertex_indices_count * vertex_index_bit_size // 8,
            offset=vertex_data_offset + vertex_indices_offset,
        )

        # TODO: No byte order?
        vertex_indices = np.frombuffer(
            vertex_indices_data, dtype=np.uint16 if vertex_index_bit_size == 16 else np.uint32
        )

        # We always store indices as 32-bit.
        if vertex_index_bit_size == 16:
            vertex_indices = vertex_indices.astype(np.uint32)

        # NOTE: This method is not called for `FLVER0` (FaceSet is constructed manually as a container only) so
        # we know we will only have triangles.
        if not face_set_struct.is_triangle_strip:
            # Reshape indices into 2D array (every row of three indices is a separate triangle).
            vertex_indices = vertex_indices.reshape((-1, 3))

        return face_set_struct.to_object(cls, vertex_indices=vertex_indices)

    def to_flver_writer(self, writer: BinaryWriter, vertex_index_bit_size: int, write_index_size: bool):
        if self.is_triangle_strip and self.vertex_indices.ndim != 1:
            raise ValueError(
                f"Cannot write triangle strip FaceSet with {self.vertex_indices.ndim}-dimensional vertex indices. "
                f"Must be 1D."
            )
        elif not self.is_triangle_strip and self.vertex_indices.ndim != 2:
            raise ValueError(
                f"Cannot write non-strip triangles FaceSet {self.vertex_indices.ndim}-dimensional vertex indices. "
                f"Must be 2D."
            )

        vertex_indices_count = self.vertex_indices.size
        self.STRUCT.object_to_writer(
            self,
            writer,
            _vertex_indices_count=vertex_indices_count,
            _vertex_indices_offset=None,  # reserved
            _vertex_indices_length=vertex_indices_count * vertex_index_bit_size // 8,
            _vertex_index_bit_size=vertex_index_bit_size if write_index_size else 0,
        )

    def pack_vertex_indices(self, writer: BinaryWriter, vertex_index_bit_size: int, vertex_indices_offset: int):
        writer.fill("_vertex_indices_offset", vertex_indices_offset, obj=self)
        if vertex_index_bit_size == 16:
            vertex_indices = self.vertex_indices.astype(np.uint16)
        elif vertex_index_bit_size == 32:
            if self.vertex_indices.dtype != np.uint32:
                vertex_indices = self.vertex_indices.astype(np.uint32)
            else:
                vertex_indices = self.vertex_indices
        else:
            raise NotImplementedError(f"Unsupported vertex index size for `pack()`: {vertex_index_bit_size}")
        # TODO: byte order issue?
        packed_vertex_indices = vertex_indices.tobytes()
        writer.append(packed_vertex_indices)

    def get_face_counts(self, uses_0xffff_separators: bool) -> tuple[int, int]:
        """Returns two counts of faces: 'true' and 'total'.

        Both counts are always the same for non-strip vertex indices. For strips, the 'true' count is zero if this
        face set has the `MotionBlur` flag set and otherwise excludes degenerate (point/line) faces.
        """
        if not self.is_triangle_strip:
            if self.has_flag(FaceSetFlags.MotionBlur):
                # We don't include motion blur face sets towards the true face count.
                return 0, len(self.vertex_indices)
            # True and total face counts are the same.
            return len(self.vertex_indices), len(self.vertex_indices)

        indices = np.asarray(self.vertex_indices)
        if len(indices) < 3:
            return 0, 0

        triplets = np.lib.stride_tricks.sliding_window_view(indices, 3)

        if uses_0xffff_separators:
            valid_mask = ~np.any(triplets == 0xFFFF, axis=1)
        else:
            valid_mask = np.ones(len(triplets), dtype=bool)

        total_face_count = int(np.count_nonzero(valid_mask))

        is_motion_blur = self.has_flag(FaceSetFlags.MotionBlur)  # hoisted out of the loop
        if is_motion_blur:
            true_face_count = 0
        else:
            a, b, c = triplets[:, 0], triplets[:, 1], triplets[:, 2]
            non_degenerate = (a != b) & (b != c) & (a != c)
            true_face_count = int(np.count_nonzero(valid_mask & non_degenerate))

        return true_face_count, total_face_count

    def needs_32bit_indices(self) -> bool:
        """Check if vertices can be written as unsigned shorts (16-bit), which is only possible if they are all less
        than or equal to 2 ** 16 - 1. Returns `False` if so.

        We need to check this when writing both the FaceSet headers and the vertices themselves, hence this method.
        """
        if (self.vertex_indices > 2 ** 16 - 1).any():
            # Indices go too high to use an unsigned short.
            return True
        # Can use unsigned shorts.
        return False

    def has_flag(self, flag: FaceSetFlags):
        return flag.has_flag(self.flags)

    def triangulate(
        self,
        uses_0xffff_separators: bool,
        include_degenerate_faces=False,
        flver0_vertices: np.ndarray | None = None,
    ) -> np.ndarray:
        """Convert triangle strip to 2D triangle array (i.e. every row/triangle is a separate vertex index triplet).

        Simply copies `self.vertex_indices` if `self.is_triangle_strip=False` already. Otherwise, processes the triangle
        strip. In this case, if `uses_0xffff_separators=True`, a vertex index of 0xFFFF will reset `flip` to False.
        Only use this if the number of vertices in the mesh is less than 0xFFFF (otherwise the primitive command is
        ambiguous). TODO: Surely can automate that detection.

        When unwinding a triangle strip, also excludes degenerate faces (where two or more vertex indices are identical)
        by default. Otherwise, they may be included.
        """
        if not self.is_triangle_strip:
            if self.vertex_indices.ndim != 2:
                raise ValueError("Non-triangle-strip `FaceSet.vertex_indices` must be a 2D array.")
            return self.vertex_indices.copy()

        if self.vertex_indices.ndim != 1:
            raise ValueError("Triangle-strip `FaceSet.vertex_indices` must be a 1D array.")

        if flver0_vertices is not None:
            # Sub-call with modified (slower) method including TK's manual normal inspection.
            return self._triangulate_flver0(flver0_vertices)

        indices = self.vertex_indices
        n = len(indices) - 2
        if n <= 0:
            return np.empty((0, 3), dtype=indices.dtype)

        triplets = np.lib.stride_tricks.sliding_window_view(indices, 3)  # (n, 3)
        a, b, c = triplets[:, 0], triplets[:, 1], triplets[:, 2]

        if uses_0xffff_separators:
            poisoned = np.any(triplets == 0xFFFF, axis=1)
        else:
            poisoned = np.zeros(n, dtype=bool)

        # `flip` toggles every window, but resets to False whenever a window is poisoned (matches
        # the sequential loop's `flip = False; continue` on separator hit). This is a "distance
        # since last reset, mod 2" recurrence, so we can resolve it with searchsorted instead of
        # a Python loop.
        reset_positions = np.nonzero(poisoned)[0]
        idx = np.arange(n)
        if reset_positions.size == 0:
            # No separators: `flip` simply toggles every window.
            last_reset = np.full(n, -1)
        else:
            insert_pos = np.searchsorted(reset_positions, idx, side="left")
            safe_idx = np.clip(insert_pos - 1, 0, None)
            last_reset = np.where(insert_pos > 0, reset_positions[safe_idx], -1)
        flip = (idx - last_reset - 1) % 2 == 1

        non_degenerate = (a != b) & (b != c) & (a != c)
        keep = ~poisoned & (include_degenerate_faces | non_degenerate)

        triangles = np.where(flip[:, None], triplets[:, ::-1], triplets)
        return triangles[keep].copy()

    def _triangulate_flver0(self, vertices: np.ndarray) -> np.ndarray:
        """Triangulate a triangle strip with manual normal inspection for `FLVER0`."""
        indices = self.vertex_indices
        n = len(indices) - 2
        if n <= 0:
            return np.empty((0, 3), dtype=indices.dtype)

        triplets = np.lib.stride_tricks.sliding_window_view(indices, 3)  # (n, 3)
        a, b, c = triplets[:, 0], triplets[:, 1], triplets[:, 2]

        poisoned = np.any(triplets == 0xFFFF, axis=1)
        non_degenerate = (a != b) & (b != c) & (a != c)

        # Vectorised normal/angle computation for *every* window up. We compute it once for all
        # windows, regardless of whether it ends up being used.
        v0, v1, v2 = vertices[a], vertices[b], vertices[c]
        vertex_normal = (v0["normal"] + v1["normal"] + v2["normal"]) / 3
        face_normal = np.cross(v1["position"] - v0["position"], v2["position"] - v0["position"])
        norm_product = np.linalg.norm(face_normal, axis=1) * np.linalg.norm(vertex_normal, axis=1)
        with np.errstate(invalid="ignore", divide="ignore"):
            angle = np.einsum("ij,ij->i", face_normal, vertex_normal) / norm_product
        angle_flip = angle >= 0

        # `flip` here does NOT reset on a poison (unlike `triangulate`) -- a poison only arms
        # `check_normals`, and the *next* non-degenerate window then overrides `flip` from the
        # precomputed angle before resuming normal toggling. This is at least just bookkeeping
        # and not math/vertex access.
        triangle_list = []
        flip = False
        check_normals = False
        for i in range(n):
            if poisoned[i]:
                check_normals = True
                continue
            if non_degenerate[i]:
                if check_normals:
                    flip = bool(angle_flip[i])
                    check_normals = False
                triangle_list.append(triplets[i, ::-1] if flip else triplets[i])
            flip = not flip

        if not triangle_list:
            return np.empty((0, 3), dtype=indices.dtype)
        return np.array(triangle_list)

    def get_connected_vertex_indices(self, vertex_index: int) -> set[int]:
        """Find all vertices connected to the given `vertex_index`, including `vertex_index` itself."""
        triangles = self.triangulate(uses_0xffff_separators=False, include_degenerate_faces=False)
        connected_vertices = {vertex_index}

        # Iterate over `triangles`, 3 at a time, and add any triangle that shares a vertex with `connected`.
        # Keeps repeating this until the number of connected vertices stops increasing.
        previous_connection_count = len(connected_vertices)
        while True:
            for triangle in triangles:
                if any(v in connected_vertices for v in triangle):
                    connected_vertices.update(triangle)
            new_connection_count = len(connected_vertices)
            if new_connection_count == previous_connection_count:
                break
            previous_connection_count = new_connection_count
        return connected_vertices

    @classmethod
    def from_triangles(cls, triangles: np.ndarray | list[tuple[int, int, int], ...], use_backface_culling=True):
        """Create a `FaceSet` with `triangle_strip=False` from a list of vertex indices triplets.

        Given `triangles` can be a 1D or 2D array or a list of triplets. If 1D, it will be reshaped to 2D.

        A new array will be created in all cases to ensure it has `uint32` type.

        TODO: Currently sets `flags=0` and `unk_x06=0`, which is correct so far in my usage.
        """
        if isinstance(triangles, np.ndarray):
            if triangles.ndim == 2:
                vertex_indices = triangles.astype(np.uint32)
            elif triangles.ndim == 1:
                vertex_indices = triangles.reshape((-1, 3)).astype(np.uint32)
            else:
                raise ValueError("Triangle array must be 1D or 2D.")
        else:
            # Flatten and combine into 1D `uint32` array, then reshape to 2D.
            vertex_indices = np.array([i for tri in triangles for i in tri], dtype=np.uint32).reshape((-1, 3))

        return cls(
            flags=0,
            unk_x06=0,
            is_triangle_strip=False,
            use_backface_culling=use_backface_culling,
            vertex_indices=vertex_indices,
        )

    def __repr__(self):
        if self.is_triangle_strip:
            vertex_indices_str = f"<{self.vertex_indices.size}-index strip>"
        else:
            vertex_indices_str = f"<{self.vertex_indices.shape[0]} triangles>"
        if self.flags == 0 and self.unk_x06 == 0:
            return f"FaceSet({vertex_indices_str}, use_backface_culling = {self.use_backface_culling})"
        return (
            f"FaceSet(\n"
            f"  flags = 0b{self.flags:032b}  # {self.flags}\n"
            f"  triangle_strip = {self.is_triangle_strip}\n"
            f"  use_backface_culling = {self.use_backface_culling}\n"
            f"  unk_x06 = {self.unk_x06}\n"
            f"  vertex_indices = {vertex_indices_str}\n"
            f")"
        )
