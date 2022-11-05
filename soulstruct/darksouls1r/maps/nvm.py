from __future__ import annotations

__all__ = ["NVMTriangle", "NVMBox", "NVMEventEntity", "NVM"]

from collections import deque
from dataclasses import dataclass
from enum import IntEnum

from soulstruct.base.game_file import GameFile
from soulstruct.games import DarkSoulsDSRType
from soulstruct.utilities.binary import BinaryReader, BinaryWriter, BinaryStruct
from soulstruct.utilities.maths import Vector3


class TriangleFlags(IntEnum):
    NONE = 0x00000
    INSIDE_WALL = 0x0001
    BLOCK_GATE = 0x0002
    CLOSED_DOOR = 0x0004
    DOOR = 0x0008
    HOLE = 0x0010
    LADDER = 0x0020
    LARGE_SPACE = 0x0040
    EDGE = 0x0080
    EVENT = 0x0100
    LANDING_POINT = 0x0200
    FLOOR_TO_WALL = 0x0400
    DEGENERATE = 0x0800
    WALL = 0x1000
    BLOCK = 0x2000
    GATE = 0x4000
    DISABLE = 0x8000


@dataclass(slots=True)
class NVMTriangle:

    vertex_indices: tuple[int, int, int]
    connected_indices: tuple[int, int, int]  # connected triangle indices along the 1-2, 2-3, and 1-3 edges
    obstacle_count: int  # number of breakable objects on this triangle
    flags: int  # used by AI to check if this triangle can be navigated by a given character

    @classmethod
    def unpack(cls, reader: BinaryReader) -> NVMTriangle:
        vertex_indices = reader.unpack("3i")
        connected_indices = reader.unpack("3i")

        obstacles_and_flags = reader.unpack("i")[0]
        if obstacles_and_flags & 3 != 0:
            raise ValueError(f"Lowest two bits of NVMTriangle obstacle/flag int != 0: {obstacles_and_flags:010b}")
        obstacle_count = (obstacles_and_flags >> 2) & 0x3FFF
        flags = obstacles_and_flags >> 16

        return NVMTriangle(vertex_indices, connected_indices, obstacle_count, flags)

    def pack(self, writer: BinaryWriter):
        writer.pack("6i", *self.vertex_indices, *self.connected_indices)
        obstacles_and_flags = (self.obstacle_count << 2) | (self.flags << 16)
        writer.pack("i", obstacles_and_flags)

    def has_flag(self, triangle_flag: TriangleFlags) -> bool:
        return (self.flags & triangle_flag) > 0

    def add_flag(self, triangle_flag: TriangleFlags):
        self.flags |= triangle_flag.value


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
