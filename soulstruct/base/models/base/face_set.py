from __future__ import annotations

__all__ = ["FaceSetFlags", "FaceSet"]

import logging
from dataclasses import dataclass, field
from enum import IntEnum

import numpy as np

from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger("soulstruct")


class FaceSetFlags(IntEnum):

    LodLevel1 = 0b0000_0001
    LodLevel2 = 0b0000_0010
    EdgeCompressed = 0b0100_0000
    MotionBlur = 0b1000_0000

    def has_flag(self, flag_int: int):
        return flag_int & self.value


@dataclass(slots=True)
class FaceSet:

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):

        _pad1: bytes = field(init=False, **BinaryPad(3))
        flags: byte
        is_triangle_strip: bool
        use_backface_culling: bool
        unk_x06: short
        _vertex_indices_count: int
        _vertex_indices_offset: int
        # NOTE: Fields stop here for FLVER versions < 0x20005, which are not supported by Soulstruct.
        _vertex_indices_length: int  # len(self.vertex_indices) * vertex_index_bit_size // 8
        _pad2: bytes = field(init=False, **BinaryPad(4))
        _vertex_index_bit_size: int = field(**Binary(asserted=[0, 16, 32]))  # 0 means size is set by FLVER header
        _pad3: bytes = field(init=False, **BinaryPad(4))

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
        if self.is_triangle_strip:
            true_face_count = 0
            total_face_count = 0
            for i in range(len(self.vertex_indices) - 2):
                triplet = self.vertex_indices[i:i + 3]
                if not uses_0xffff_separators or 0xFFFF not in triplet:
                    total_face_count += 1
                    if not self.has_flag(FaceSetFlags.MotionBlur) and len(set(triplet)) == 3:
                        # Vertices are not MotionBlur and not degenerate.
                        true_face_count += 1
            return true_face_count, total_face_count

        # True and total face counts are the same.
        return len(self.vertex_indices), len(self.vertex_indices)

    def needs_32bit_indices(self) -> bool:
        """Check if vertices can be written as unsigned shorts (16-bit), which is only possible if they are all less
        than or equal to 2 ** 16. Returns `False` if so.

        We need to check this when writing both the FaceSet headers and the vertices themselves, hence this method.
        """
        if (self.vertex_indices > 2 ** 16).any():
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
        vertices: np.ndarray | None = None,
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

        if vertices is not None:
            # Sub-call with modified (slower) method including TK's manual normal inspection.
            return self._triangulate_flver0(vertices)

        triangle_list = []  # can't predict array length due to primitive restarts
        flip = False
        for i in range(len(self.vertex_indices) - 2):
            triplet = self.vertex_indices[i:i + 3]
            if uses_0xffff_separators and 0xFFFF in triplet:
                flip = False  # restart the strip and ignore this triplet
                continue
            if include_degenerate_faces or len(set(triplet)) == 3:
                triangle_list.append([triplet[2], triplet[1], triplet[0]] if flip else triplet)
            flip = not flip
        return np.array(triangle_list)

    def _triangulate_flver0(self, vertices: np.ndarray) -> np.ndarray:
        """Triangulate a triangle strip with manual normal inspection for `FLVER0`."""
        triangle_list = []
        flip = False
        check_normals = False
        for i in range(len(self.vertex_indices) - 2):
            triplet = self.vertex_indices[i:i + 3]
            if 0xFFFF in triplet:
                check_normals = True
                continue
            if len(set(triplet)) == 3:
                if check_normals:
                    # TODO: Numpify.
                    v0 = vertices[triplet[0]]
                    v1 = vertices[triplet[1]]
                    v2 = vertices[triplet[2]]
                    n0 = v0["normal"]
                    n1 = v1["normal"]
                    n2 = v2["normal"]
                    vertex_normal = (n0 + n1 + n2) / 3
                    face_normal = np.cross(v1["position"] - v0["position"], v2["position"] - v0["position"])
                    norm_product = np.linalg.norm(face_normal) * np.linalg.norm(vertex_normal)
                    angle = np.dot(face_normal, vertex_normal) / norm_product
                    flip = angle >= 0
                    check_normals = False
                triangle_list.append([triplet[2], triplet[1], triplet[0]] if flip else triplet)
            flip = not flip
        return np.array(triangle_list)

    def get_connected_vertex_indices(self, vertex_index: int) -> set[int]:
        """Find all vertices connected to the given `vertex_index`, including `vertex_index` itself."""
        triangles = self.triangulate(uses_0xffff_separators=False, include_degenerate_faces=False)
        connected_vertices = {vertex_index}

        # Iterate over `triangles`, 3 at a time, and add any triangle that shares a vertex with `connected`.
        # Keeps repeating this until the number of connected vertices stops increasing.
        previous_connection_count = len(connected_vertices)
        while True:
            for i in range(0, len(triangles), 3):
                if any(v in connected_vertices for v in triangles[i:i + 3]):
                    connected_vertices.update(triangles[i:i + 3])
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
            # Flatten and combine into 1D `uint32` array.
            vertex_indices = np.array([i for tri in triangles for i in tri], dtype=np.uint32)

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
