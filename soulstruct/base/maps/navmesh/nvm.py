from __future__ import annotations

__all__ = ["NVMTriangle", "NavmeshFlag", "NVMBox", "NVMEventEntity", "NVM"]

import logging
import typing as tp
from collections import deque
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.darksouls1r.events.enums import NavmeshFlag
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Matrix3

import numpy as np

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class NVMTriangle:
    """A single triangle face in a `NVM` mesh.

    Has flags that indicate whether the triangle is walkable, has any breakable obstacles on it, etc.

    TODO: Should probably just hold these in an 8-column NumPy array.
    """

    vertex_indices: tuple[int, int, int]
    connected_indices: tuple[int, int, int]  # indices of surrounding triangles along the 1-2, 2-3, and 1-3 edges
    obstacle_count: int  # number of breakable objects on this triangle (implies `NavmeshFlag.Obstacle` flag)
    flags: int  # used by AI to check if this triangle can be navigated by a given character

    @classmethod
    def from_nvm_reader(cls, reader: BinaryReader) -> NVMTriangle:
        vertex_indices = reader.unpack("3i")
        connected_indices = reader.unpack("3i")
        obstacles_and_flags = reader.unpack("I")[0]
        if obstacles_and_flags & 3 != 0:
            raise ValueError(f"Lowest two bits of NVMTriangle obstacle/flag int != 0: {obstacles_and_flags:010b}")
        obstacle_count = (obstacles_and_flags >> 2) & 0x3FFF
        all_flags = cls.reverse_flags_bits(obstacles_and_flags >> 16)
        # noinspection PyTypeChecker
        return NVMTriangle(vertex_indices, connected_indices, obstacle_count, all_flags)

    def to_nvm_writer(self, writer: BinaryWriter):
        writer.pack("6i", *self.vertex_indices, *self.connected_indices)
        obstacles_and_flags = (self.obstacle_count << 2) | (self.reverse_flags_bits(self.flags) << 16)
        writer.pack("I", obstacles_and_flags)

    def has_flag(self, navmesh_type: NavmeshFlag):
        return self.flags & navmesh_type == navmesh_type

    def get_centroid(self, vertices: list[Vector3]) -> Vector3:
        """Return centroid point of triangle (just average of vertices)."""
        v1, v2, v3 = (vertices[i] for i in self.vertex_indices)
        x = sum(v.x for v in (v1, v2, v3)) / 3.0
        y = sum(v.y for v in (v1, v2, v3)) / 3.0
        z = sum(v.z for v in (v1, v2, v3)) / 3.0
        return Vector3([x, y, z])

    @staticmethod
    def reverse_flags_bits(n):
        return int(f"{{0:016b}}".format(n)[::-1], 2)

    @property
    def flag(self) -> NavmeshFlag:
        """Try to access the triangle flags as a single `NavmeshFlag` enum.

        Will raise `ValueError` if multiple flags are set (which does happen).
        """
        try:
            return NavmeshFlag(self.flags)
        except ValueError:  # unexpected multiple flags
            raise ValueError(f"`NVMTriangle` has multiple flags: {self.flags:016b}")

    @flag.setter
    def flag(self, flag: NavmeshFlag):
        """Set the triangle flags to a single value."""
        self.flags = flag.value

    def __repr__(self):
        try:
            flag = self.flag
            if flag == NavmeshFlag.Default:
                return (
                    f"NVMTriangle({self.vertex_indices}, "
                    f"connected_indices={self.connected_indices}, "
                    f"obstacle_count={self.obstacle_count})"
                )
            return (
                f"NVMTriangle({self.vertex_indices}, "
                f"connected_indices={self.connected_indices}, "
                f"obstacle_count={self.obstacle_count}, "
                f"flag=<NavmeshFlag.{flag.name}>)"
            )
        except ValueError:
            return (
                f"NVMTriangle({self.vertex_indices}, "
                f"connected_indices={self.connected_indices}, "
                f"obstacle_count={self.obstacle_count}, "
                f"all_flags={self.flags})"
            )


@dataclass(slots=True)
class NVMBox:
    """AABB in a quaternary tree structure that covers the navmesh."""

    start_corner: Vector3
    end_corner: Vector3
    triangle_indices: list[int]  # list of triangles contained in this box (only used for leaf box nodes)
    child_boxes: list[NVMBox]  # four child boxes that subdivide this one (empty for leaf box nodes)

    @classmethod
    def from_nvm_reader(cls, reader: BinaryReader) -> NVMBox:
        start_corner = Vector3(reader.unpack("3f"))
        triangle_count = reader["i"]
        end_corner = Vector3(reader.unpack("3f"))
        triangles_offset = reader["i"]

        child_box_offsets = reader.unpack("iiii")
        reader.assert_pad(16)

        # Box triangle indices are stored separately (earlier in file).
        if triangle_count > 0:
            triangle_indices = list(reader.unpack(f"{triangle_count}i", offset=triangles_offset))
        else:
            triangle_indices = []

        if child_box_offsets == (0, 0, 0, 0):
            child_boxes = []
        elif 0 in child_box_offsets:
            raise ValueError(f"Child box offsets should be all zero (leaf) or non-zero, not: {child_box_offsets}")
        else:
            child_boxes = []
            for child_box_offset in child_box_offsets:
                reader.seek(child_box_offset)
                child_boxes.append(cls.from_nvm_reader(reader))  # recur (no need to reset reader position)

        return cls(start_corner, end_corner, triangle_indices, child_boxes)

    def to_nvm_writer(self, writer: BinaryWriter, triangle_index_offsets: deque[int]) -> int:
        """Pack `NVMBox` to `writer`. Returns start offset of pack. Dequeues triangle indices from given list.

        Boxes are packed depth-first, starting with the deepest zero-indexed child of the root box, and ending with the
        root box itself. A queue of triangle indices (packed earlier in the same order) are passed in.
        """

        if not self.child_boxes:
            child_box_offsets = [0, 0, 0, 0]
        else:
            child_box_offsets = [
                child_box.to_nvm_writer(writer, triangle_index_offsets)
                for child_box in self.child_boxes
            ]

        box_offset = writer.position
        writer.pack("3f", *self.start_corner)
        writer.pack("i", len(self.triangle_indices))
        writer.pack("3f", *self.end_corner)
        writer.pack("i", triangle_index_offsets.popleft())
        writer.pack("4i", *child_box_offsets)
        writer.pad(16)
        return box_offset

    @property
    def is_leaf(self):
        return not self.child_boxes


@dataclass(slots=True)
class NVMEventEntity:
    """List of triangle indices that can be toggled from EMEVD with `entity_id`.

    There is generally a corresponding `MSBNavigationEvent` in the MSB, but I don't believe it does anything - it's
    probably just to make a note of this entity ID, or to allow use of the ID in EMEVD, etc.
        TODO: Confirm that by removing MSB events and seeing if the EMEVD navmesh commands still work in DS1.
    """
    entity_id: int
    triangle_indices: list[int]

    @classmethod
    def from_nvm_reader(cls, reader: BinaryReader) -> NVMEventEntity:
        entity_id, index_offset, index_count = reader.unpack("3i")
        reader.assert_pad(4)
        triangle_indices = list(reader.unpack(f"{index_count}i", offset=index_offset))
        return cls(entity_id, triangle_indices)

    def to_nvm_writer(self, writer: BinaryWriter, index_offset: int):
        writer.pack("4i", self.entity_id, index_offset, len(self.triangle_indices), 0)


@dataclass(slots=True)
class NVM(GameFile):
    """Holds a navigation mesh (vertices and triangles), per-triangle navigation flags, groups of triangles that can be
    manipulated with EMEVD scripts, and a box quad-tree hierarchy that covers the mesh (which is simple to generate)."""

    # TODO: Always correct for DS1. Not sure about DeS.
    BOX_LEVELS: tp.ClassVar[int] = 3  # number of nested quaternary levels in box tree
    BOX_PADDING: tp.ClassVar[float] = 0.5  # in-game distance units

    # Absolute cross-products smaller than this will NOT be counted as outside triangle.
    # NOTE: I can't find any tolerance that produces EXACTLY the same box contents as the vanilla files in DS1.
    #  The best inspection I can muster simply indicates that some barely-outside faces are still assigned to boxes,
    #  but similarly narrow gaps are correctly interpreted in other cases (maybe a triangle vs. quad test thing).
    #  It almost certainly should not matter.
    BOX_TRIANGLE_TOLERANCE: tp.ClassVar[float] = 1E-9

    big_endian: bool = False
    vertices: np.ndarray = field(default_factory=lambda: np.zeros((1, 3), dtype=np.float32))
    triangles: list[NVMTriangle] = field(default_factory=list)
    root_box: NVMBox = None
    event_entities: list[NVMEventEntity] = field(default_factory=list)

    def __post_init__(self):
        if self.root_box is None:
            # Quadtree boxes are automatically generated from vertex extents.
            self.generate_quadtree_boxes()

    @dataclass(slots=True)
    class NVMHeaderStruct(BinaryStruct):
        endianness: int = field(**Binary(asserted=[1, 0x1000000]))  # 1 (LE) or 0x1000000 (BE)
        vertices_count: int
        vertices_offset: int = field(init=False, **Binary(asserted=0x80))  # immediately after this header
        triangles_count: int
        triangles_offset: int  # predictable from vertex count
        root_box_offset: int  # last data in file
        _pad1: bytes = field(init=False, **BinaryPad(4))
        entities_count: int  # triangles marked with entity IDs (matching `MSBNavigation` events)
        entities_offset: int
        _pad2: bytes = field(init=False, **BinaryPad(92))

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        endian_byte = reader.peek("i")[0]
        if endian_byte == 1:
            reader.default_byte_order = ByteOrder.LittleEndian
        elif endian_byte == 0x1000000:
            reader.default_byte_order = ByteOrder.BigEndian

        header = cls.NVMHeaderStruct.from_bytes(reader)
        expected_triangles_offset = 0x80 + header.vertices_count * 0xC
        if header.triangles_offset != expected_triangles_offset:
            # Check for error case of 64-bit vertices (offset from end of header will be exactly double expected).
            double_triangles_offset = 0x80 + header.vertices_count * 0x18
            if header.triangles_offset == double_triangles_offset:
                _LOGGER.warning("`NVM` file appears to have 64-bit vertices. Will truncate to 32-bit vertices.")
                dtype = np.dtype("<f8") if reader.default_byte_order == ByteOrder.LittleEndian else np.dtype(">f8")
                vertices = np.frombuffer(reader.read(8 * 3 * header.vertices_count), dtype=dtype)
                vertices = vertices.astype(np.float32)
            else:
                raise ValueError(
                    f"Expected an NVM triangles offset of {hex(expected_triangles_offset)}, not header value "
                    f"{hex(header.triangles_offset)} (and not due to incorrectly 64-bit vertices)."
                )
        else:
            # Read flat array of [x0, y0, z0, x1, y1, z1, ...] single-precision vertices.
            dtype = np.dtype("<f4") if reader.default_byte_order == ByteOrder.LittleEndian else np.dtype(">f4")
            vertices = np.frombuffer(reader.read(4 * 3 * header.vertices_count), dtype=dtype)

        vertices.shape = (header.vertices_count, 3)
        triangles = [NVMTriangle.from_nvm_reader(reader) for _ in range(header.triangles_count)]

        reader.seek(header.root_box_offset)
        root_box = NVMBox.from_nvm_reader(reader)
        if (box_count := len(cls.get_all_boxes(root_box))) != 85:
            _LOGGER.warning(
                f"`NVM` has {box_count} boxes in its hierarchy, but 85 are always expected "
                f"(root + three levels of division into four)."
            )

        reader.seek(header.entities_offset)
        event_entities = [NVMEventEntity.from_nvm_reader(reader) for _ in range(header.entities_count)]
        return cls(
            big_endian=reader.default_byte_order == ByteOrder.BigEndian,
            vertices=vertices,
            triangles=triangles,
            root_box=root_box,
            event_entities=event_entities,
        )

    def to_writer(self) -> BinaryWriter:

        # Validate dtype and shape of vertices array.
        if self.vertices.dtype != np.float32:
            raise ValueError(f"`NVM.vertices` array must contain 32-bit floats, not {self.vertices.dtype}.")
        if self.vertices.shape[1] != 3:
            raise ValueError(f"`NVM.vertices` array must have shape (N, 3), not {self.vertices.shape}.")

        writer = BinaryWriter(ByteOrder.big_endian_bool(self.big_endian))
        self.NVMHeaderStruct(
            endianness=0x1000000 if self.big_endian else 1,
            vertices_count=self.vertices.shape[0],
            triangles_count=len(self.triangles),
            triangles_offset=RESERVED,
            root_box_offset=RESERVED,
            entities_count=len(self.event_entities),
            entities_offset=RESERVED,
        ).to_writer(writer, reserve_obj=self)

        writer.append(self.vertices.tobytes())

        writer.fill_with_position("triangles_offset", obj=self)
        for triangle in self.triangles:
            triangle.to_nvm_writer(writer)

        box_triangle_index_offsets = deque()

        def write_box_triangle_indices(box: NVMBox):
            """Recursive depth-first indices. Note that the root box's indices are written LAST, and its deepest zero-
            indexed child's indices are written FIRST."""
            # Recur on children (if any).
            for child_box in box.child_boxes:
                write_box_triangle_indices(child_box)
            if box.triangle_indices:
                box_triangle_index_offsets.append(writer.position)
                writer.pack(f"{len(box.triangle_indices)}i", *box.triangle_indices)
            else:
                box_triangle_index_offsets.append(0)

        write_box_triangle_indices(self.root_box)

        root_box_offset = self.root_box.to_nvm_writer(writer, box_triangle_index_offsets)
        writer.fill("root_box_offset", root_box_offset, obj=self)

        if self.event_entities:
            entity_triangles_index_offsets = []
            for entity in self.event_entities:
                entity_triangles_index_offsets.append(writer.position)
                writer.pack(f"{len(entity.triangle_indices)}i", *entity.triangle_indices)

            writer.fill_with_position("entities_offset", obj=self)
            for entity, entity_triangles_offset in zip(self.event_entities, entity_triangles_index_offsets):
                entity.to_nvm_writer(writer, entity_triangles_offset)
        else:
            writer.fill("entities_offset", 0, obj=self)

        return writer

    @staticmethod
    def get_all_boxes(root_box: NVMBox) -> list[tuple[NVMBox, tuple[int, ...]]]:
        """Returns a list of tuples, each containing a box and an index sequence that shows its nesting, such as
        `(1, 3, 0)` (first child of third child of first child of root box).

        List is depth-first.
        """

        all_boxes = [root_box]  # type: list[NVMBox]
        all_indices = [tuple()]  # type: list[tuple[int, ...]]
        current_index = []  # type: list[int]

        def add_children(box: NVMBox):
            if not box.child_boxes:
                return  # leaf (no further children)
            for i, child_box in enumerate(box.child_boxes):
                if child_box is not None and child_box not in all_boxes:
                    current_index.append(i)
                    all_boxes.append(child_box)
                    all_indices.append(tuple(current_index))
                    add_children(child_box)
                    current_index.pop()

        add_children(root_box)

        return list(zip(all_boxes, all_indices))

    def get_vertex_bounds(
        self,
        rotation: Vector3 = None,
        translation: Vector3 = None,
        padding: tp.Sequence[float, float, float] | float | int = None,
    ) -> tuple[Vector3, Vector3]:
        """Get min/max bounds of all vertices.

        Supports optional pre-rotation and translation offset (e.g. for creating 'MSB-baked' MCP AABBs) and global or
        per-coordinate padding.
        """
        if rotation is not None:
            # Euler angles in radians given (e.g. from MSB). Use to rotate all vertices before computing AABB.
            rot_mat = Matrix3.from_euler_angles(rotation, radians=True)
            aabb_vertices = self.vertices @ rot_mat.data  # rotate each vertex (row)
        else:
            aabb_vertices = self.vertices  # won't be modified
        if translation is None:
            translation = Vector3.zero()
        if padding is None:
            padding = Vector3.zero()
        elif isinstance(padding, (int, float)):
            padding = Vector3([padding, padding, padding])

        aabb_start = Vector3(np.min(aabb_vertices, axis=0)) - padding + translation
        aabb_end = Vector3(np.max(aabb_vertices, axis=0)) + padding + translation
        return aabb_start, aabb_end

    def generate_quadtree_boxes(self):
        """Use level count and bordering to automatically generate three layers of quadtree `NVMBox` instances.

        These boxes simply divide the axis-aligned XZ extents of the mesh into eight, and stretch Y as needed (same for
        all boxes). Leaf boxes contain bounded mesh vertices, though some may still be empty. Padding is added on each
        side.

        NOTE: Child box order (0, 1, 2, 3) is lowX/lowZ, highX/lowZ, highX/highZ, lowX/highZ.
        """
        bounds_min, bounds_max = self.get_vertex_bounds(padding=self.BOX_PADDING)

        # Every three rows in this array will be one triangle. (We don't care about the Y coordinate but keep it.)
        all_triangle_vertices = self.vertices[[i for t in self.triangles for i in t.vertex_indices]]
        # Reshape to 3D array so that each row is one triangle (3 vertices of 3 floats).
        all_triangle_vertices = all_triangle_vertices.reshape((len(self.triangles), 3, 3))

        # Compute `is_clockwise` for each triangle from the sign of the cross product of line (a, b) and point c in XZ.
        b_from_a = all_triangle_vertices[:, 1] - all_triangle_vertices[:, 0]
        point_from_a = all_triangle_vertices[:, 2] - all_triangle_vertices[:, 0]
        all_triangle_abc_cross = b_from_a[:, 0] * point_from_a[:, 2] - b_from_a[:, 2] * point_from_a[:, 0]
        is_clockwise = all_triangle_abc_cross < 0  # boolean array

        def create_box(start_corner: Vector3, end_corner: Vector3, level: int) -> NVMBox:
            # Box will either start or end at these halfway points, depending on its index.

            if level == self.BOX_LEVELS:  # leaf boxes have indices
                triangle_indices = self.get_triangle_indices_in_box(
                    all_triangle_vertices, is_clockwise, start_corner, end_corner
                )
                return NVMBox(
                    start_corner,
                    end_corner,
                    triangle_indices,
                    child_boxes=[],
                )

            child_boxes = []
            x_bisect = start_corner.x + (end_corner.x - start_corner.x) / 2.0
            z_bisect = start_corner.z + (end_corner.z - start_corner.z) / 2.0
            for i in range(4):
                if i in {0, 3}:  # low X
                    x_start, x_end = start_corner.x, x_bisect
                else:  # high X
                    x_start, x_end = x_bisect, end_corner.x
                if i in {0, 1}:  # low Z
                    z_start, z_end = start_corner.z, z_bisect
                else:  # high Z
                    z_start, z_end = z_bisect, end_corner.z

                child_start_corner = Vector3([x_start, bounds_min.y, z_start])
                child_end_corner = Vector3([x_end, bounds_max.y, z_end])

                child_box = create_box(child_start_corner, child_end_corner, level + 1)
                child_boxes.append(child_box)

            return NVMBox(
                start_corner,
                end_corner,
                triangle_indices=[],  # non-leaf boxes do NOT have indices
                child_boxes=child_boxes,
            )

        # Start recursive box construction.
        self.root_box = create_box(bounds_min, bounds_max, level=0)

    def get_triangle_indices_in_box(
        self, triangle_vertices: np.ndarray, is_clockwise: np.ndarray, start_corner: Vector3, end_corner: Vector3
    ) -> list[int]:
        """For automatic AABB quad-tree box generation.

        Any triangle with a vertex in the box will count; the trickier problem is detecting when a triangle edge passes
        through the box without any vertices in it.

        Triangles can be part of multiple leaf boxes.

        TODO: Currently guessing that box intervals are half-open (closed at start, open at end). The border will ensure
         that no edge vertices are lost anyway, and vertices are obviously not likely to land exactly on the bounds.
        """
        triangle_indices = []

        quad_vertices = np.array([
            [start_corner.x, 0.0, start_corner.z],
            [end_corner.x, 0.0, start_corner.z],
            [end_corner.x, 0.0, end_corner.z],
            [start_corner.x, 0.0, end_corner.z],
        ])

        for i, (triangle, clockwise) in enumerate(zip(triangle_vertices, is_clockwise)):
            if self.collides(quad_vertices, triangle, clockwise):
                triangle_indices.append(i)

        return triangle_indices

    @classmethod
    def collides(cls, aabb_vertices: np.ndarray, triangle: np.ndarray, clockwise: bool) -> bool:
        """2D collision test for an AABB quad and a triangle (2D array)."""

        # If triangle is fully outside ANY of the four sides of the AABB, there is no collision.
        # We do this check first because it's faster.
        if (triangle[:, 0] < aabb_vertices[0, 0]).all():
            return False
        if (triangle[:, 0] > aabb_vertices[2, 0]).all():
            return False
        if (triangle[:, 2] < aabb_vertices[0, 2]).all():
            return False
        if (triangle[:, 2] > aabb_vertices[2, 2]).all():
            return False

        # We need to check if (a) any triangle vertex lies in the box (easy) or (b) any triangle edge passes through
        # the box (harder). We do this by checking if all box vertices are outside each triangle edge; we need to know
        # whether the triangle vertices are clockwise to know which side of the edge line is 'outside'.
        tolerance = cls.BOX_TRIANGLE_TOLERANCE
        for a, b in ((0, 1), (1, 2), (2, 0)):
            if all(is_outside(triangle[a], triangle[b], v, clockwise, tolerance) for v in aabb_vertices):
                # All quad vertices are outside this triangle edge. No collision.
                return False

        # Triangle collides with AABB.
        return True


def line_point_cross_xz(a: np.ndarray, b: np.ndarray, point: np.ndarray) -> float:
    b_from_a = b - a
    point_from_a = point - a
    return b_from_a[0] * point_from_a[2] - b_from_a[2] * point_from_a[0]


def is_outside(
    tri_a: np.ndarray, tri_b: np.ndarray, point: np.ndarray, tri_clockwise: bool, tolerance: float = 0.0
) -> bool:
    """Uses line/point 'cross product' (determinant) to determine if `point` is outside the triangle edge
    `(tri_a, tri_b)` (using `clockwise` to determine which side of the line is outside).

    Returns True if `point` is outside the edge.

    Values less than `tolerance` in the expected 'outside' direction will still return False.
    """
    cross = line_point_cross_xz(tri_a, tri_b, point)
    if tri_clockwise:
        return cross > tolerance  # outside == left
    return cross < -tolerance  # outside == right
