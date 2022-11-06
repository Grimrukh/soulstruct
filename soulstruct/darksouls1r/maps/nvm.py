from __future__ import annotations

__all__ = ["NVMTriangle", "NavmeshType", "NVMBox", "NVMEventEntity", "NVM"]

import logging
from collections import deque
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.games import DarkSoulsDSRType
from soulstruct.utilities.binary import BinaryReader, BinaryWriter, BinaryStruct
from soulstruct.utilities.maths import Vector3
from ..events.emevd.enums import NavmeshType

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class NVMTriangle:

    vertex_indices: tuple[int, int, int]
    connected_indices: tuple[int, int, int]  # connected triangle indices along the 1-2, 2-3, and 1-3 edges
    obstacle_count: int  # number of breakable objects on this triangle
    all_flags: int  # used by AI to check if this triangle can be navigated by a given character
    flag: None | NavmeshType = field(init=False, default=None)

    def __post_init__(self):
        if self.all_flags == NavmeshType.Default:
            self.flag = NavmeshType.Default
        elif self.all_flags in {NavmeshType.Obstacle, NavmeshType.Obstacle | NavmeshType.Degenerate}:
            self.flag = NavmeshType.Obstacle
        elif self.all_flags == NavmeshType.Degenerate:
            self.flag = NavmeshType.Degenerate
        else:
            single_flag = self.all_flags & ~NavmeshType.Degenerate & ~NavmeshType.Obstacle
            try:
                self.flag = NavmeshType(single_flag)
            except ValueError:  # unexpected multiple flags
                self.flag = None

    @classmethod
    def unpack(cls, reader: BinaryReader) -> NVMTriangle:
        vertex_indices = reader.unpack("3i")
        connected_indices = reader.unpack("3i")

        obstacles_and_flags = reader.unpack("I")[0]
        if obstacles_and_flags & 3 != 0:
            raise ValueError(f"Lowest two bits of NVMTriangle obstacle/flag int != 0: {obstacles_and_flags:010b}")
        obstacle_count = (obstacles_and_flags >> 2) & 0x3FFF
        all_flags = cls.reverse_flags_bits(obstacles_and_flags >> 16)
        return NVMTriangle(vertex_indices, connected_indices, obstacle_count, all_flags)

    def pack(self, writer: BinaryWriter):
        writer.pack("6i", *self.vertex_indices, *self.connected_indices)
        obstacles_and_flags = (self.obstacle_count << 2) | (self.reverse_flags_bits(self.all_flags) << 16)
        writer.pack("i", obstacles_and_flags)

    @property
    def is_obstacle(self):
        return self.all_flags & NavmeshType.Obstacle == NavmeshType.Obstacle

    @property
    def is_degenerate(self):
        return self.all_flags & NavmeshType.Degenerate == NavmeshType.Degenerate

    @staticmethod
    def reverse_flags_bits(n):
        return int(f"{{0:016b}}".format(n)[::-1], 2)


@dataclass(slots=True)
class NVMBox:
    """AABB in a quaternary tree structure that covers the navmesh."""

    start_corner: Vector3
    end_corner: Vector3
    triangle_indices: list[int]  # list of triangles contained in this box (only used for leaf box nodes)
    child_boxes: list[None | NVMBox]  # four child boxes that subdivide this one

    @classmethod
    def unpack(cls, reader: BinaryReader) -> NVMBox:
        start_corner = Vector3(reader.unpack("3f"))
        triangle_count = reader.unpack_value("i")
        end_corner = Vector3(reader.unpack("3f"))
        triangles_offset = reader.unpack_value("i")

        child_box_offsets = reader.unpack("iiii")
        reader.assert_pad(16)

        if triangle_count > 0:
            triangle_indices = list(reader.unpack(f"{triangle_count}i", offset=triangles_offset))
        else:
            triangle_indices = []

        child_boxes = []
        for child_box_offset in child_box_offsets:
            if child_box_offset == 0:
                child_boxes.append(None)
            else:
                reader.seek(child_box_offset)
                child_boxes.append(cls.unpack(reader))  # recur (no need to reset reader position)

        return cls(start_corner, end_corner, triangle_indices, child_boxes)

    def pack(self, writer: BinaryWriter, triangle_index_offsets: deque[int]) -> int:
        """Pack `NVMBox` to `writer`. Returns start offset of pack. Dequeues triangle indices from given list."""

        child_box_offsets = []
        for child_box in self.child_boxes:
            if child_box is not None:
                child_box_offsets.append(child_box.pack(writer, triangle_index_offsets))
            else:
                child_box_offsets.append(0)

        box_offset = writer.position
        writer.pack("3f", *self.start_corner)
        writer.pack("i", len(self.triangle_indices))
        writer.pack("3f", *self.end_corner)
        writer.pack("i", triangle_index_offsets.popleft())
        writer.pack("4i", *child_box_offsets)
        writer.pad(16)
        return box_offset


@dataclass(slots=True)
class NVMEventEntity:
    """List of triangle indices that can be toggled from EMEVD with `entity_id`.

    There is generally a corresponding `MSBNavigationEvent` in the MSB, but I don't believe it does anything - it's
    probably just to make a note of this entity ID. TODO: Confirm.
    """
    entity_id: int
    triangle_indices: list[int]

    @classmethod
    def unpack(cls, reader: BinaryReader) -> NVMEventEntity:
        entity_id, index_offset, index_count = reader.unpack("3i")
        reader.assert_pad(4)
        triangle_indices = list(reader.unpack(f"{index_count}i", offset=index_offset))
        return cls(entity_id, triangle_indices)

    def pack(self, writer: BinaryWriter, index_offset: int):
        writer.pack("4i", self.entity_id, index_offset, len(self.triangle_indices), 0)


class NVM(GameFile, DarkSoulsDSRType):

    big_endian: bool
    vertices: list[Vector3]
    triangles: list[NVMTriangle]
    root_box: NVMBox
    event_entities: list[NVMEventEntity]

    HEADER_STRUCT = BinaryStruct(
        ("big_endian", "i"),  # 1 (LE) or 0x1000000 (BE)
        ("vertex_count", "i"),
        ("vertex_offset", "i", 0x80),  # straight after header
        ("triangle_count", "i"),
        ("triangles_offset", "i"),  # predictable from vertex count
        ("root_box_offset", "i"),  # stored last
        "4x",
        ("entities_count", "i"),
        ("entities_offset", "i"),
        "92x",
    )

    def unpack(self, reader: BinaryReader, **kwargs):
        reader.byte_order = "<"
        first_byte = reader.peek_value("i")
        self.big_endian = first_byte != 1
        if self.big_endian:
            reader.byte_order = ">"

        header = reader.unpack_struct(self.HEADER_STRUCT)
        expected_triangles_offset = 0x80 + header["vertex_count"] * 0xC
        if header["triangles_offset"] != expected_triangles_offset:
            raise ValueError(
                f"Ttriangles offset for NVM should be {expected_triangles_offset}, not {header['triangles_offset']}.")

        self.vertices = [Vector3(reader.unpack("3f")) for _ in range(header["vertex_count"])]
        self.triangles = [NVMTriangle.unpack(reader) for _ in range(header["triangle_count"])]
        if any(triangle.flag is None for triangle in self.triangles):
            _LOGGER.warning("`NVM` has at least one triangle with multiple non-BLOCK non-DEGENERATE flags.")

        reader.seek(header["root_box_offset"])
        self.root_box = NVMBox.unpack(reader)

        reader.seek(header["entities_offset"])
        self.event_entities = [NVMEventEntity.unpack(reader) for _ in range(header["entities_count"])]

    def pack(self, **kwargs) -> bytes:
        writer = BinaryWriter(big_endian=self.big_endian)

        writer.pack("4i", 1, len(self.vertices), self.HEADER_STRUCT.size, len(self.triangles))
        writer.reserve("triangles_offset", "i")
        writer.reserve("root_box_offset", "i")
        writer.pad(4)
        writer.pack("i", len(self.event_entities))
        writer.reserve("entities_offset", "i")
        writer.pad(92)

        for vertex in self.vertices:
            writer.pack("3f", *vertex)

        writer.fill_with_position("triangles_offset")
        for triangle in self.triangles:
            triangle.pack(writer)

        box_triangle_index_offsets = deque()

        def write_box_triangle_indices(box: NVMBox):
            if box is None:
                return
            # Recur on children.
            for child_box in box.child_boxes:
                write_box_triangle_indices(child_box)
            if box.triangle_indices:
                box_triangle_index_offsets.append(writer.position)
                writer.pack(f"{len(box.triangle_indices)}i", *box.triangle_indices)
            else:
                box_triangle_index_offsets.append(0)

        write_box_triangle_indices(self.root_box)

        root_box_offset = self.root_box.pack(writer, box_triangle_index_offsets)
        writer.fill("root_box_offset", root_box_offset)

        if self.event_entities:
            entity_triangles_index_offsets = []
            for entity in self.event_entities:
                entity_triangles_index_offsets.append(writer.position)
                writer.pack(f"{len(entity.triangle_indices)}i", *entity.triangle_indices)

            writer.fill_with_position("entities_offset")
            for entity, entity_triangles_offset in zip(self.event_entities, entity_triangles_index_offsets):
                entity.pack(writer, entity_triangles_offset)
        else:
            writer.fill("entities_offset", 0)

        return writer.finish()

    def get_all_boxes(self) -> list[tuple[NVMBox, tuple[int]]]:
        """Returns a list of tuples, each containing a box and an index sequence that shows its nesting, such as
        `(1, 3, 0)` (first child of third child of first child of root box).

        List is depth-first.
        """

        all_boxes = [self.root_box]  # type: list[NVMBox]
        all_indices = [tuple()]  # type: list[tuple[int]]
        current_index = []  # type: list[int]

        def add_children(box: NVMBox):
            for i, child_box in enumerate(box.child_boxes):
                if child_box is not None and child_box not in all_boxes:
                    current_index.append(i)
                    all_boxes.append(child_box)
                    all_indices.append(tuple(current_index))
                    add_children(child_box)
                    current_index.pop()

        add_children(self.root_box)

        return list(zip(all_boxes, all_indices))
