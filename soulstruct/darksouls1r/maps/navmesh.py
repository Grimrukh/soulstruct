"""Classes for MCG and MCP files, and other navmesh-related tools.

Currently only set up for DS1R.

Some notes about navmeshes:
    - A navmesh is a simple mesh comprised of triangular faces. Each face has a certain flag associated with it, which
    are enumerated in `NavmeshType` (e.g. "Solid", "Wall", "Cliff", "Ladder").
    - Enemy pathing is plotted out as a sequence of moves from face to face (to the center of each face, specifically).
    Some enemies are not permitted to have paths planned out over faces with certain flags (e.g. only some characters
    can climb ladders).
    - Navmeshes are generally (about 95% of the time) 1:1 with collisions and generally have matching model indices
    (e.g. "n0003B0_0000" is generally congruent with collision "h0003B0_0000"). Sometimes, one navmesh can cover
    multiple collisions, but I don't believe I've seen one collision cover multiple navmeshes in DS1.
    - Each navmesh in a map has a corresponding "room" in that map's MCP file. These rooms simply index the navmeshes
    in the order they are contained inside the MSB. These rooms are just boxes aligned to the world axes, so they aren't
    particularly veridical to the map geometry. Each room is connected to a list of other rooms.
    - Each map also has an MCG file containing a graph that helps AI use the navmesh. The nodes on this graph are
    "gates" between MCP rooms; the edges that connect them refer to a specific room index (the room that edge is a path
    through).
    - The MCP navmesh rooms control *backread*, based on the player's distance from that room's box (likely a simple
    raycast). The game also only seems to check the distance of rooms that are connected to the one the player is
    standing inside (or was last standing inside).
    - The "navmesh groups" of navmeshes that are in backread (because their corresponding rooms are close enough and
    connected) are used to upgrade two backread tables, one "normal" and one "hit".
    - There are two sets of rules, one for "normal" backread (possibly characters, objects, etc., or possibly unused)
    and one for "hit" backread (collisions). The distances for "normal" backread (enabled at 20m, disabled at 25m) are
    smaller than for "hit" backread (enabled after spending 0.2s closer than 80m, disabled after spending 1.3s further
    than 90m).
    - By default (i.e. without any navmeshes and no navmesh-produced backread), the player's current collision has
    backread 4 (low + hi poly versions), all other collisions in the current map have backread 2 (low poly only), and
    all collisions in all other loaded maps have backread 0.
    - These backreads states are "upgraded" by navmesh backread groups. If a navmesh's MCP room is within the "hit"
    backread distance, it is loaded (appears under "WorldBackRead" menu).
    - The distance to the room the player is current inside is always 0.0. If the player is standing inside multiple
    rooms, the game appears to prefer the room that matches the player's navmesh, or that is inside the map of the
    player's current collision? Unclear exactly how this preferential system works, but it does seem that the game only
    checks the distance of rooms that are linked to the last room the player was inside.
    - Any collisions whose navmesh groups are covered by the navmesh group of a loaded navmesh will be "upgraded".
    Collisions in the current map will go from backread 2 to backread 4. Collisions in connected maps will go from
    backread 0 to backread 2.
    - That is, navmesh groups and an intact navmesh-produced backread system are *necessary* to get collisions in
    connected maps to load. The connection's display groups can't get backread high enough to give the collision
    any physics!
    - The *draw groups* of collisions appear to be used for *children only*! Actual collision physics are determined
    solely by backread state, which is determined by navmesh rooms and groups.
"""
from __future__ import annotations

__all__ = ["MCP", "MCG", "NavmeshGraph"]

import copy
import shutil
import struct
import typing as tp
from itertools import product
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.darksouls1r.maps.msb import MSB
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader
from soulstruct.utilities.maths import Vector3, Matrix3


class MCPRoom(BinaryObject):

    STRUCT = BinaryStruct(
        ("map_id", "4b"),
        ("index", "i"),
        ("__connected_rooms_count", "i"),
        ("__connected_rooms_offset", "i"),
        ("box_start", "3f"),
        ("box_end", "3f"),
    )

    map_id: tuple[int, int, int, int]
    index: int
    box_start: Vector3
    box_end: Vector3
    connected_rooms: list[int]

    def __init__(self, reader: BinaryReader = None, /, **kwargs):
        """Simple bounding box around a navmesh (indexed directly from MSB), with a list of other NavRoom indices that
        this one connects to.

        MCPRooms are also referenced by the MCGNodes in MCG files, which connect to one another through edges in rooms.

        More importantly, I believe that the navmesh distances used for backread purposes use simple raycasts into
        these volumes.
        """
        self.map_id = (-1, -1, -1, -1)
        self.index = -1  # separate (but generally equal) to indexing in MCP
        self.box_start = Vector3(0, 0, 0)
        self.box_end = Vector3(1, 1, 1)
        self.connected_rooms = []  # `.index` of connected MCPRooms
        super().__init__(reader, **kwargs)

    def unpack(self, reader: BinaryReader):
        room = reader.unpack_struct(self.STRUCT)

        self.connected_rooms = []
        with reader.temp_offset(room.pop("__connected_rooms_offset")):
            for _ in range(room.pop("__connected_rooms_count")):
                self.connected_rooms.append(reader.unpack_value("i"))

        self.set(**room)

    def pack(self, connected_rooms_offset: int):
        """Connected rooms should be packed separately and the starting offset passed to this."""
        return self.STRUCT.pack(
            map_id=self.map_id,
            index=self.index,
            connected_rooms_count=len(self.connected_rooms),
            connected_rooms_offset=connected_rooms_offset,
            box_start=list(self.box_start),
            box_end=list(self.box_end),
        )

    def pack_connected_rooms(self):
        room_count = len(self.connected_rooms)
        return struct.pack(f"<{room_count}i", *self.connected_rooms)

    def remove_connected_room(self, room_index):
        """Remove the given local room index from this room's connection list."""
        self.connected_rooms = [room for room in self.connected_rooms if room != room_index]

    def translate(self, translate: tp.Union[Vector3, list, tuple]):
        """Add `translate` to `box_start` and `box_end` of room."""
        self.box_start += translate
        self.box_end += translate

    def rotate_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        enclose_original=True,
    ):
        """Modify entity `box_start` and `box_end` by rotating it around some pivot in world coordinates (defaults to
        the world origin). A single rotation value is a shortcut for Y rotation only.

        If `enclose_original=True` (default), the size of the rotated room will be modified to fully enclose what the
        original box would have looked like if it were properly rotated (as the room's box must be aligned to the
        world axes).
        """
        if isinstance(rotation, (int, float)):
            rotation = Matrix3.from_euler_angles(0.0, rotation, 0.0, radians=radians)
        elif isinstance(rotation, (Vector3, list, tuple)):
            rotation = Matrix3.from_euler_angles(rotation, radians=radians)
        elif not isinstance(rotation, Matrix3):
            raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
        pivot_point = Vector3(pivot_point)

        if enclose_original:
            rotated_vertices = [(rotation @ (Vector3(v) - pivot_point)) + pivot_point for v in self.get_vertices()]
            self.box_start = Vector3([min(v[i] for v in rotated_vertices) for i in range(3)])
            self.box_end = Vector3([max(v[i] for v in rotated_vertices) for i in range(3)])
        else:
            self.box_start = (rotation @ (self.box_start - pivot_point)) + pivot_point
            self.box_end = (rotation @ (self.box_end - pivot_point)) + pivot_point

    @property
    def volume_center(self):
        return (self.box_start + self.box_end) / 2

    def get_vertices(self, swap_yz=False):
        """Extrapolate all eight vertices of the room's box."""
        x, y, z = zip(self.box_start, self.box_end)  # (start, end) for each dimension
        if swap_yz:
            return list(product(x, z, y))
        return list(product(x, y, z))

    def get_faces(self, swap_yz=False):
        v = self.get_vertices(swap_yz)
        return (
            (v[0], v[1], v[3], v[2]),  # front
            (v[4], v[5], v[7], v[6]),  # back
            (v[0], v[1], v[5], v[4]),  # left
            (v[2], v[3], v[7], v[6]),  # right
            (v[1], v[3], v[7], v[5]),  # top
            (v[0], v[2], v[6], v[4]),  # bottom
        )

    def copy(self) -> MCPRoom:
        """Return a deep copy of this MCPRoom."""
        return copy.deepcopy(self)

    def draw(self, axes=None, show=False, room_color="cyan", label_room=False):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ModuleNotFoundError("Optional `matplotlib` module is needed to draw MCG graphs.")
        from mpl_toolkits.mplot3d.art3d import Poly3DCollection

        if axes is None:
            fig = plt.figure()
            axes = fig.add_subplot(111, projection="3d")
        vertices = self.get_vertices(swap_yz=True)
        axes.scatter(*zip(*vertices), c="green", s=1, alpha=0.1)  # note y/z swapped
        if label_room:
            axes.text(self.volume_center[0], self.volume_center[2], self.volume_center[1], self.index, c="black")
        axes.add_collection3d(
            Poly3DCollection(
                self.get_faces(swap_yz=True), facecolors=room_color, linewidths=0.1, edgecolors="red", alpha=0.1
            )
        )
        if show:
            plt.show()


class MCP(GameFile):

    HEADER_STRUCT = BinaryStruct(
        ("two", "i", 2),  # 0x2000000 for Demon's Souls (big endian)
        ("unknown", "i"),
        ("__rooms_count", "i"),
        ("__rooms_offset", "i"),
    )

    unknown: int
    rooms: list[MCPRoom]

    def __init__(self, mcp_source=None, dcx_magic=()):
        self.unknown = -1
        self.rooms = []  # type: list[MCPRoom]
        super().__init__(mcp_source, dcx_magic)

    def unpack(self, reader: BinaryReader, **kwargs):
        header = reader.unpack_struct(self.HEADER_STRUCT)
        self.unknown = header["unknown"]
        reader.seek(header.pop("__rooms_offset"))
        self.rooms = [MCPRoom(reader) for _ in range(header.pop("rooms_count"))]

    def pack(self) -> bytes:
        offset = self.HEADER_STRUCT.size
        connected_rooms_offsets = []
        all_connected_rooms = b""
        for room in self.rooms:
            connected_rooms_offsets.append(offset)
            connected_rooms = room.pack_connected_rooms()
            all_connected_rooms += connected_rooms
            offset += len(connected_rooms)

        packed = self.HEADER_STRUCT.pack(
            unknown=self.unknown,
            __rooms_count=len(self.rooms),
            __rooms_offset=offset,
        )
        packed += all_connected_rooms
        for i, room in enumerate(self.rooms):
            packed += room.pack(connected_rooms_offsets[i])
        return packed

    def __getitem__(self, room_index):
        for room in self.rooms:
            if room.index == room_index:
                return room
        raise ValueError(f"No MCPRoom with local index {room_index}.")

    def __iter__(self):
        return iter(self.rooms)

    @property
    def max_index(self):
        return max(room.index for room in self.rooms)

    def get_room_index(self, room_index) -> MCPRoom:
        """Return MCPRoom instance with given index. Raises an error if 0 or multiple rooms are found."""
        rooms = [room for room in self.rooms if room.index == room_index]
        if not rooms:
            raise IndexError(f"No MCP room with index {room_index}.")
        elif len(rooms) > 1:
            raise IndexError(f"Multiple MCP rooms found with local index {room_index}.")
        return rooms[0]

    def add_room(self, map_id, box_start, box_end, connected_rooms) -> MCPRoom:
        """Add a new `MCPRoom` instance to the end of the MCP room list, connected to all given room indices, and
        return it. The index is the maximum existing room index plus one."""
        room = MCPRoom(
            map_id=map_id,
            index=self.max_index + 1,
            box_start=box_start,
            box_end=box_end,
            connected_rooms=connected_rooms,
        )
        self.rooms.append(room)
        return room

    def duplicate_room(self, source_index, **kwargs) -> MCPRoom:
        """Duplicate given room index. By default, new index is maximum existing room index plus one."""
        kwargs.setdefault("index", self.max_index + 1)
        room = self.get_room_index(source_index).copy()
        room.set(**kwargs)
        self.rooms.append(room)
        return room

    def delete_room(self, room_index, update_indices=True):
        """Delete room with given local index (NOT absolute index in MCP, which is never used) and remove that room from
        connected list of all other rooms. By default, updates indices of higher-numbered rooms; you should only disable
        this if you know you won't be deleting the corresponding navmesh from the MSB, for some reason.

        Remember to also (a) remove the corresponding navmesh in the MSB and (b) delete any edges that pass through
        this room in the MCG. NavmeshGraph method handles the latter.
        """
        room_to_delete = self.get_room_index(room_index)  # validates index
        self.rooms.remove(room_to_delete)
        for room in self.rooms:
            room.remove_connected_room(room_index)
        if update_indices:
            for room in self.rooms:
                if room.index > room_index:
                    room.index -= 1
                room.connected_rooms = [(r - 1 if r > room_index else r) for r in room.connected_rooms]

    def disconnect_rooms(self, first_group, second_group):
        """Disconnects all rooms with indices in `first_group` from all rooms with indices in `second_group`."""
        first_group = {first_group} if isinstance(first_group, int) else set(first_group)
        second_group = {second_group} if isinstance(second_group, int) else set(second_group)
        intersection = first_group.intersection(second_group)
        if intersection:
            raise ValueError(f"Rooms cannot be in both disconnection groups: {intersection}")
        for room in self.rooms:
            if room.index in first_group:
                for index_to_remove in second_group:
                    room.remove_connected_room(index_to_remove)
            elif room.index in second_group:
                for index_to_remove in first_group:
                    room.remove_connected_room(index_to_remove)

    def move_in_world(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        enclose_original=True,
        selected_room_indices=None,
    ):
        """Rotate and then translate all NavRooms in MCP in world coordinates, so that an entity with a translate of
        `start_translate` and rotate of `start_rotate` ends up with a translate of `end_translate` and a rotate of
        `end_rotate`.

        Works by simply shifting the `box_start` and `box_end` points of each room.
        """
        if start_translate is None:
            start_translate = Vector3.zero()
        elif not isinstance(start_translate, Vector3):
            start_translate = Vector3(start_translate)
        if end_translate is None:
            end_translate = Vector3.zero()
        elif not isinstance(end_translate, Vector3):
            end_translate = Vector3(end_translate)
        if start_rotate is None:
            start_rotate = Vector3.zero()
        elif isinstance(start_rotate, (int, float)):
            start_rotate = Vector3(0, start_rotate, 0)
        else:
            start_rotate = Vector3(start_rotate)
        if end_rotate is None:
            end_rotate = Vector3.zero()
        elif isinstance(end_rotate, (int, float)):
            end_rotate = Vector3(0, end_rotate, 0)
        else:
            end_rotate = Vector3(end_rotate)

        # Compute global rotation matrix required to get from `start_rotate` to `end_rotate`.
        m_start_rotate = Matrix3.from_euler_angles(start_rotate)
        m_end_rotate = Matrix3.from_euler_angles(end_rotate)
        m_world_rotate = m_end_rotate @ m_start_rotate.T

        # Apply global rotation to start point to determine required global translation.
        translation = end_translate - (m_world_rotate @ start_translate)  # type: Vector3

        self.rotate_all_rooms_in_world(
            m_world_rotate, enclose_original=enclose_original, selected_room_indices=selected_room_indices
        )
        self.translate_all(translation, selected_room_indices=selected_room_indices)

    def rotate_all_rooms_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        enclose_original=True,
        selected_room_indices=None,
    ):
        """Rotate every NavRoom in the map around the given pivot by the given Euler angles coordinate system.

        The pivot defaults to the world origin.
        """
        if isinstance(rotation, (int, float)):
            rotation = Matrix3.from_euler_angles(0.0, rotation, 0.0)  # single rotation value interpreted as Y rotation
        elif isinstance(rotation, (Vector3, list, tuple)):
            rotation = Matrix3.from_euler_angles(rotation)
        elif not isinstance(rotation, Matrix3):
            raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
        pivot_point = Vector3(pivot_point)
        for room in self.rooms:
            if selected_room_indices is None or room.index in selected_room_indices:
                room.rotate_in_world(
                    rotation, pivot_point=pivot_point, radians=radians, enclose_original=enclose_original
                )

    def translate_all(self, translate: tp.Union[Vector3, list, tuple], selected_room_indices=None):
        """Translate every NavRoom in the map by the given vector."""
        for room in self.rooms:
            if selected_room_indices is None or room.index in selected_room_indices:
                room.translate(translate)

    def draw(self, room_color="cyan", label_rooms=False, axes=None, auto_show=True):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ModuleNotFoundError("Optional `matplotlib` module is needed to draw MCG graphs.")
        if axes is None:
            fig = plt.figure(figsize=(8, 8))
            axes = fig.add_subplot(111, projection="3d")
        else:
            fig = axes.figure
        for room in self.rooms:
            room.draw(axes, room_color=room_color, label_room=label_rooms)
            for connected_room in (self.get_room_index(i) for i in room.connected_rooms if i > room.index):
                x, z, y = zip(room.volume_center, connected_room.volume_center)  # y, z swapped
                axes.plot(x, y, z, color="red")

        # Get min/max values on each axis to simulate equal aspect ratio.
        mins = Vector3([min(room.box_start[i] for room in self.rooms) for i in range(3)])
        maxs = Vector3([max(room.box_end[i] for room in self.rooms) for i in range(3)])
        mids = (mins + maxs) / 2
        max_range = max(maxs - mins) / 2
        axes.set_xlim(mids.x - max_range, mids.x + max_range)
        axes.set_ylim(mids.z - max_range, mids.z + max_range)
        axes.set_zlim(mids.y - max_range, mids.y + max_range)

        axes.set(xlabel="X", ylabel="Z", zlabel="Y")
        fig.tight_layout()
        if auto_show:
            plt.show()


class MCGNode(BinaryObject):

    STRUCT = BinaryStruct(
        ("__connection_count", "i"),
        ("translate", "3f"),
        ("__connected_nodes_offset", "i"),
        ("__connected_edges_offset", "i"),
        ("unknowns", "ii"),
    )

    translate: Vector3
    unknowns: tuple[int, int]
    connected_node_indices: list[int]
    connected_edge_indices: list[int]

    def __init__(self, reader: BinaryReader = None, /, **kwargs):
        self.connected_node_indices = []
        self.connected_edge_indices = []  # edges connect to `connected_nodes` with the same index
        self.unknowns = (-1, -1)
        super().__init__(reader, **kwargs)

    def unpack(self, reader: BinaryReader):
        node = reader.unpack_struct(self.STRUCT)
        connection_count = node.pop("__connection_count")

        self.connected_node_indices = []
        with reader.temp_offset(node.pop("__connected_nodes_offset")):
            for _ in range(connection_count):
                self.connected_node_indices.append(reader.unpack_value("<i"))

        self.connected_edge_indices = []
        with reader.temp_offset(node.pop("__connected_edges_offset")):
            for _ in range(connection_count):
                self.connected_edge_indices.append(reader.unpack_value("<i"))

        self.set(**node)

    def validate(self):
        if len(self.connected_nodes) != len(self.connected_edges):
            raise ValueError(f"Number of connected nodes does not match number of connected edges.")

    def pack(self, connected_nodes_offset: int, connected_edges_offset: int):
        self.validate()
        return self.STRUCT.pack(
            __connection_count=len(self.connected_nodes),
            translate=list(self.translate),
            __connected_nodes_offset=connected_nodes_offset,
            __connected_edges_offset=connected_edges_offset,
            unknowns=self.unknowns,
        )

    def pack_connected_nodes(self):
        node_count = len(self.connected_nodes)
        return struct.pack(f"<{node_count}i", *self.connected_nodes)

    def pack_connected_edges(self):
        edge_count = len(self.connected_edges)
        return struct.pack(f"<{edge_count}i", *self.connected_edges)

    def remove_connected_nodes(self, node_indices):
        """Remove connections to all given nodes, and remove corresponding connected edges."""
        self.validate()
        if isinstance(node_indices, int):
            node_indices = (node_indices,)
        self.connected_edges = [
            edge for edge, node in zip(self.connected_edges, self.connected_nodes) if node not in node_indices
        ]
        self.connected_nodes = [node for node in self.connected_nodes if node not in node_indices]

    def rotate_in_world(
        self, rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float], pivot_point=(0, 0, 0), radians=False
    ):
        """Modify node `translate` by rotating it around some pivot in world coordinates (defaults to the world
        origin)."""
        if isinstance(rotation, (int, float)):
            # Single rotation value is a shortcut for Y rotation.
            rotation = Matrix3.from_euler_angles(0.0, rotation, 0.0, radians=radians)
        elif isinstance(rotation, (Vector3, list, tuple)):
            rotation = Matrix3.from_euler_angles(rotation, radians=radians)
        elif not isinstance(rotation, Matrix3):
            raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
        pivot_point = Vector3(pivot_point)

        self.translate = (rotation @ (self.translate - pivot_point)) + pivot_point


class MCGEdge(BinaryObject):
    """Note that these objects, in the `MCG` file, reference absolute indices of `MCPRoom` instances in the `MCP` file.

    The two file types (`MCG` and `MCP`) must be carefully synchronized.
    """

    STRUCT = BinaryStruct(
        ("start_node", "i"),
        ("__unk1_count", "i"),  # unknown indices; likely related to use of start node
        ("__unk1_offset", "i"),
        ("end_node", "i"),
        ("__unk2_count", "i"),  # unknown indices; likely related to use of end node
        ("__unk2_offset", "i"),
        ("mcp_room_index", "i"),
        ("map_id", "4b"),
        ("unknown", "f"),  # possibly a weight?
    )

    start_node: int
    end_node: int
    mcp_room_index: int
    map_id: tuple[int, int, int, int]
    unknown: float

    unk1_indices: list[int, ...]
    unk2_indices: list[int, ...]

    DEFAULTS = {
        "mcp_room_index": -1,
        "map_id": (-1, -1, -1, -1),
    }

    def __init__(self, reader: BinaryReader = None, /, **kwargs):
        self.unk1_indices = []
        self.unk2_indices = []
        super().__init__(reader, **kwargs)

    def unpack(self, reader: BinaryReader):
        edge = reader.unpack_struct(self.STRUCT)

        self.unk1_indices = []
        with reader.temp_offset(edge.pop("__unk1_offset")):
            for _ in range(edge.pop("__unk1_count")):
                self.unk1_indices.append(reader.unpack_value("<i"))

        self.unk2_indices = []
        with reader.temp_offset(edge.pop("__unk2_offset")):
            for _ in range(edge.pop("__unk2_count")):
                self.unk2_indices.append(reader.unpack_value("<i"))

        self.set(**edge)

    def pack(self, unk1_offset: int, unk2_offset: int) -> bytes:
        return self.STRUCT.pack(
            start_node=self.start_node,
            __unk1_count=len(self.unk1_indices),
            __unk1_offset=unk1_offset,
            end_node=self.end_node,
            __unk2_count=len(self.unk2_indices),
            __unk2_offset=unk2_offset,
            mcp_room_index=self.mcp_room_index,
            map_id=self.map_id,
            unknown=self.unknown,
        )

    def pack_unk1_indices(self):
        index_count = len(self.unk1_indices)
        return struct.pack(f"<{index_count}i", *self.unk1_indices)

    def pack_unk2_indices(self):
        index_count = len(self.unk2_indices)
        return struct.pack(f"<{index_count}i", *self.unk2_indices)


class MCG(GameFile):

    HEADER_STRUCT = BinaryStruct(
        ("one", "i", 1),  # 0x1000000 in Demon's Souls (big endian)
        ("__unk0", "i"),
        ("__nodes_count", "i"),
        ("__nodes_offset", "i"),
        ("__edges_count", "i"),
        ("__edges_offset", "i"),
        ("__unk1", "i"),
        ("__unk2", "i"),
    )

    unknowns: tuple[int, int, int]

    def __init__(self, mcg_source=None, dcx_magic=()):
        self.unknowns = (-1, -1, -1)
        super().__init__(mcg_source, dcx_magic=dcx_magic)

    def unpack(self, reader: BinaryReader, **kwargs):
        mcg = reader.unpack_struct(self.HEADER_STRUCT)
        self.unknowns = (mcg["__unk0"], mcg["__unk1"], mcg["__unk2"])
        reader.seek(mcg["__nodes_offset"])
        self.nodes = [MCGNode(reader) for _ in range(mcg["__nodes_count"])]
        reader.seek(mcg["__edges_offset"])
        self.edges = [MCGEdge(reader) for _ in range(mcg["__edges_count"])]

    def pack(self):
        offset = self.HEADER_STRUCT.size
        edge_unk1_offsets = []
        edge_unk2_offsets = []
        packed_edge_unk_offsets = b""
        for edge in self.edges:
            edge_unk1_offsets.append(offset)
            packed_unk1_indices = edge.pack_unk1_indices()
            packed_edge_unk_offsets += packed_unk1_indices
            offset += len(packed_unk1_indices)

            edge_unk2_offsets.append(offset)
            packed_unk2_indices = edge.pack_unk2_indices()
            packed_edge_unk_offsets += packed_unk2_indices
            offset += len(packed_unk2_indices)

        connected_node_offsets = []
        connected_edge_offsets = []
        packed_connection_offsets = b""
        for node in self.nodes:
            connected_node_offsets.append(offset if node.connected_nodes else 0)
            packed_node_offsets = node.pack_connected_nodes()
            packed_connection_offsets += packed_node_offsets
            offset += len(packed_node_offsets)

            connected_edge_offsets.append(offset if node.connected_edges else 0)
            packed_edge_offsets = node.pack_connected_edges()
            packed_connection_offsets += packed_edge_offsets
            offset += len(packed_edge_offsets)

        edges_offset = offset
        packed_edges = b""
        for i, edge in enumerate(self.edges):
            packed_edges += edge.pack(edge_unk1_offsets[i], edge_unk2_offsets[i])

        offset += len(packed_edges)
        nodes_offset = offset
        packed_nodes = b""
        for i, node in enumerate(self.nodes):
            packed_nodes += node.pack(connected_node_offsets[i], connected_edge_offsets[i])

        packed = self.HEADER_STRUCT.pack(
            __unk0=self.unknowns[0],
            __nodes_count=len(self.nodes),
            __nodes_offset=nodes_offset,
            __edges_count=len(self.edges),
            __edges_offset=edges_offset,
            __unk1=self.unknowns[1],
            __unk2=self.unknowns[2],
        )
        packed += packed_edge_unk_offsets
        packed += packed_connection_offsets
        packed += packed_edges
        packed += packed_nodes
        return packed

    def get_edge_indices_in_room(self, room_index: int):
        """Return a list of all edge indices in the given MCP room."""
        return [i for i, edge in enumerate(self.edges) if edge.mcp_room_index == room_index]

    def delete_edge_between_nodes(self, first_node_index: int, second_node_index: int, allow_missing=True):
        """Looks for and deletes the edge between the two nodes (in either direction). This is generally safer than
        calling `delete_edge` directly, since node indices are probably more stable while editing maps.

        By default, raises an error if no such edge is found. Always raises an error if multiple edges are found, since
        this should never happen.
        """
        edge_index_matches = []
        for i, edge in enumerate(self.edges):
            if (edge.start_node == first_node_index and edge.end_node == second_node_index) or (
                edge.start_node == second_node_index and edge.end_node == first_node_index
            ):
                edge_index_matches.append(i)
        if not edge_index_matches:
            if allow_missing:
                return  # do nothing, don't complain
            raise ValueError(f"No edges found that connect node {first_node_index} and node {second_node_index}.")
        elif len(edge_index_matches) > 1:
            raise ValueError(
                f"Multiple edges found that connect node {first_node_index} and node {second_node_index}. "
                f"This should't happen!"
            )
        edge_index = edge_index_matches[0]
        self.delete_edge(edge_index)

    def add_edge_between_nodes(
        self, first_node_index: int, second_node_index: int, room_index: int, allow_repeat=False, map_id=None
    ):
        """If `map_id` is None, copies from last edge. (Also copies unknown indices from last edge.)"""
        if not allow_repeat:
            # Check edge doesn't already exist.
            edge_index_matches = []
            for i, edge in enumerate(self.edges):
                if (edge.start_node == first_node_index and edge.end_node == second_node_index) or (
                    edge.start_node == second_node_index and edge.end_node == first_node_index
                ):
                    edge_index_matches.append(i)
            if edge_index_matches:
                raise ValueError(
                    f"Nodes {first_node_index} and {second_node_index} already connected by edge "
                    f"{edge_index_matches}."
                )
        new_edge_index = len(self.edges)
        new_edge = copy.deepcopy(self.edges[-1])
        new_edge.start_node = first_node_index
        new_edge.end_node = second_node_index
        if map_id is not None:
            new_edge.map_id = map_id
        new_edge.mcp_room_index = room_index
        start_node = self.nodes[first_node_index]
        start_node.connected_nodes.append(second_node_index)
        start_node.connected_edges.append(new_edge_index)
        end_node = self.nodes[second_node_index]
        end_node.connected_nodes.append(first_node_index)
        end_node.connected_edges.append(new_edge_index)
        print(f"Created edge {new_edge_index} between nodes {first_node_index} and {second_node_index}.")

    def delete_edge(self, edge_index: int):
        """Delete edge with given index (in MCG) and remove all references to its connection in nodes.

        Currently assumes that no two edges have identical (or reversed) start and end nodes, which should be true.

        Also remember than edge indices above the given index will change as soon as the deletion is complete, so when
        deleting multiple edges, do it in reverse index order for the least headaches.
        """
        try:
            edge = self.edges[edge_index]
        except IndexError:
            raise IndexError(f"Invalid edge index {edge_index} (edge count = {len(self.edges)}).")
        start_node = self.nodes[edge.start_node]
        end_node = self.nodes[edge.end_node]
        start_node.remove_connected_nodes((edge.end_node,))
        end_node.remove_connected_nodes((edge.start_node,))
        self.edges.remove(edge)
        for node in self.nodes:
            # Renumber (subtract one from) all edges greater than deleted index.
            node.connected_edges = [(i - 1 if i > edge_index else i) for i in node.connected_edges]

    def move_in_world(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        selected_node_indices=None,
    ):
        """Rotate and then translate all nodes in MCG in world coordinates, so that an entity with a translate of
        `start_translate` and rotate of `start_rotate` ends up with a translate of `end_translate` and a rotate of
        `end_rotate`.

        Works by simply shifting the `.translate` points of each node.
        """
        if start_translate is None:
            start_translate = Vector3.zero()
        elif not isinstance(start_translate, Vector3):
            start_translate = Vector3(start_translate)
        if end_translate is None:
            end_translate = Vector3.zero()
        elif not isinstance(end_translate, Vector3):
            end_translate = Vector3(end_translate)
        if start_rotate is None:
            start_rotate = Vector3.zero()
        elif isinstance(start_rotate, (int, float)):
            start_rotate = Vector3(0, start_rotate, 0)
        else:
            start_rotate = Vector3(start_rotate)
        if end_rotate is None:
            end_rotate = Vector3.zero()
        elif isinstance(end_rotate, (int, float)):
            end_rotate = Vector3(0, end_rotate, 0)
        else:
            end_rotate = Vector3(end_rotate)

        # Compute global rotation matrix required to get from `start_rotate` to `end_rotate`.
        m_start_rotate = Matrix3.from_euler_angles(start_rotate)
        m_end_rotate = Matrix3.from_euler_angles(end_rotate)
        m_world_rotate = m_end_rotate @ m_start_rotate.T

        # Apply global rotation to start point to determine required global translation.
        translation = end_translate - (m_world_rotate @ start_translate)  # type: Vector3

        self.rotate_all_nodes_in_world(m_world_rotate, selected_node_indices=selected_node_indices)
        self.translate_all(translation, selected_node_indices=selected_node_indices)

    def rotate_all_nodes_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        selected_node_indices=None,
    ):
        """Rotate every node in the MCG around the given pivot by the given Euler angles coordinate system.

        The pivot defaults to the world origin.
        """
        if isinstance(rotation, (int, float)):
            rotation = Matrix3.from_euler_angles(0.0, rotation, 0.0)  # single rotation value interpreted as Y rotation
        elif isinstance(rotation, (Vector3, list, tuple)):
            rotation = Matrix3.from_euler_angles(rotation)
        elif not isinstance(rotation, Matrix3):
            raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
        pivot_point = Vector3(pivot_point)
        for i, node in enumerate(self.nodes):
            if selected_node_indices is None or i in selected_node_indices:
                node.rotate_in_world(rotation, pivot_point=pivot_point, radians=radians)

    def translate_all(self, translate: tp.Union[Vector3, list, tuple], selected_node_indices=None):
        """Translate every node in the MCG by the given vector."""
        for i, node in enumerate(self.nodes):
            if selected_node_indices is None or i in selected_node_indices:
                node.translate += translate

    def draw(self, label_nodes=False, axes=None, auto_show=True):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ModuleNotFoundError("Optional `matplotlib` module is needed to draw MCG graphs.")
        if axes is None:
            fig = plt.figure()
            axes = fig.add_subplot(111, projection="3d")
        for i, node in enumerate(self.nodes):
            axes.scatter(node.translate.x, node.translate.z, node.translate.y, s=20, c="green", alpha=0.5)
            if label_nodes:
                axes.text(node.translate.x, node.translate.z, node.translate.y, i, c="green")
        for edge in self.edges:
            start_node = self.nodes[edge.start_node]
            end_node = self.nodes[edge.end_node]
            x, y, z = zip(start_node.translate, end_node.translate)
            axes.plot3D(x, z, y, c="black", alpha=0.5)  # note y/z swapped
        if auto_show:
            plt.show()


class NavmeshGraph:

    def __init__(self, map_path: tp.Union[str, Path], msb_path=None, map_id: str = None):
        """Simple container for both MCP and MCG, which will generally be edited together.

        Loads MSB to validate navmesh room indices. Provides useful methods for joint editing/moving of MCP and MCG.

        Args:
            map_path (str or Path): Folder containing MCP and MCG files.
            msb_path (str or Path): MSB file path. If None (default), searched for in standard map directory structure.
        """
        self.map_path = Path(map_path)
        if not self.map_path.is_dir():
            raise ValueError(f"Map directory does not exist: {str(map_path)}")
        self.map_id = self.map_path.name if map_id is None else map_id
        if msb_path is None:
            self.msb_path = (self.map_path / f"../MapStudio/{self.map_id}.msb").resolve()
        else:
            self.msb_path = Path(msb_path)
        mcp_path = self.map_path / f"{self.map_id}.mcp"
        mcg_path = self.map_path / f"{self.map_id}.mcg"
        try:
            self.mcp = MCP(mcp_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find MCP file: {str(mcp_path)}")
        try:
            self.mcg = MCG(mcg_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find MCG file: {str(mcg_path)}")
        try:
            self._msb = MSB(self.msb_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find MSB file: {str(self.msb_path)}")
        self._navmeshes_valid = True
        self.check_navmeshes()

    @property
    def msb(self):
        """You can't change the attached MSB instance."""
        return self._msb

    @property
    def navmeshes(self):
        """Shortcut for getting list of Navmesh instances from MSB parts."""
        return self._msb.parts.Navmeshes

    def check_navmeshes(self):
        navmesh_count = len(self.navmeshes)
        room_count = len(self.mcp.rooms)
        max_room_index = self.mcp.max_index
        if navmesh_count < max_room_index + 1:
            # At least one room has an invalid index into the MSB navmeshes.
            print(
                f"WARNING: Number of navmeshes in MSB ({len(self.navmeshes)}) is less than the maximum room index "
                f"plus 1 ({max_room_index}) This should be fixed ASAP!"
            )
            self._navmeshes_valid = False
        else:
            if navmesh_count > max_room_index + 1:
                print(f"WARNING: More navmeshes than largest room index. Not a fatal error, but should be fixed.")
            elif navmesh_count != room_count:
                print(f"WARNING: Navmesh count is not equal to room count. Not a fatal error, but should be fixed.")
            self._navmeshes_valid = True

    def get_room_from_navmesh_name(self, navmesh_name):
        if not self._navmeshes_valid:
            raise ValueError(
                "Cannot reliably get room index from navmesh name if navmesh/room counts do not match.\n"
                "(Call `.check_navmeshes()` after fixing this issue to re-validate.)"
            )
        navmesh_matches = [i for i, navmesh in enumerate(self.navmeshes) if navmesh.name == navmesh_name]
        if not navmesh_matches:
            raise ValueError(f"No navmeshes in MSB with name {navmesh_name}.")
        elif len(navmesh_matches) > 1:
            raise ValueError(f"Multiple navmeshes in MSB with name {navmesh_name}. This shouldn't happen!")
        navmesh_index = navmesh_matches[0]
        return self.mcp.get_room_index(navmesh_index)

    def get_navmesh_name_from_room_index(self, room_index):
        if not self._navmeshes_valid:
            raise ValueError(
                "Cannot reliably get navmesh name from room index if navmesh/room counts do not match.\n"
                "(Call `.check_navmeshes()` after fixing this issue to re-validate.)"
            )
        room_mcp_index_matches = [room.index for room in self.mcp.rooms if room.index == room_index]
        if not room_mcp_index_matches:
            raise ValueError(f"No rooms in MCP with index {room_index}.")
        elif len(room_mcp_index_matches) > 1:
            raise ValueError(f"Multiple rooms in MCP with index {room_index}. This shouldn't happen!")
        return self.navmeshes[room_mcp_index_matches[0]].name

    def delete_room_and_edges_inside(self, room_index, update_room_indices=True):
        """Delete MCP rooms and any edges that pass through them. Updates room indices by default."""
        self.mcp.delete_room(room_index, update_indices=update_room_indices)
        # Delete edges that pass through deleted room.
        for edge_index in self.mcg.get_edge_indices_in_room(room_index):
            self.mcg.delete_edge(edge_index)
        if update_room_indices:
            # Renumber room indices above deleted index across MCG edges.
            for edge in self.mcg.edges:
                if edge.mcp_room_index > room_index:
                    edge.mcp_room_index -= 1

    def move_in_world(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        enclose_original=True,
        selected_room_indices=None,
        selected_node_indices=None,
    ):
        """Rotate and then translate all rooms in MCP (enclosing original rooms by default) and all nodes in MCG in
        world coordinates, so that an entity with a translate of `start_translate` and rotate of `start_rotate` ends up
        with a translate of `end_translate` and a rotate of `end_rotate`.
        """
        self.mcp.move_in_world(
            start_translate,
            end_translate,
            start_rotate,
            end_rotate,
            enclose_original=enclose_original,
            selected_room_indices=selected_room_indices,
        )
        self.mcg.move_in_world(
            start_translate, end_translate, start_rotate, end_rotate, selected_node_indices=selected_node_indices
        )

    def to_string(self):
        """Print out a list of MCG nodes, their connections, and the rooms those connective edges go through."""
        used_rooms = set()
        output = ""

        for room in self.mcp.rooms:
            output += f"Room {room.index}"
            if self._navmeshes_valid:
                navmesh_name = self.get_navmesh_name_from_room_index(room.index)
                output += f" ({navmesh_name}):\n"
            else:
                output += f":\n"
            output += f"  Box start: {room.box_start}\n"
            output += f"  Box end: {room.box_end}\n"
            for connected_room_index in room.connected_rooms:
                output += f"    --> Room {connected_room_index}"
                if self._navmeshes_valid:
                    navmesh_name = self.get_navmesh_name_from_room_index(connected_room_index)
                    output += f" ({navmesh_name})\n"
                else:
                    output += "\n"

        for i, node in enumerate(self.mcg.nodes):
            output += f"Node {i} [{node.translate}]:\n"
            for j, connected_node_index in enumerate(node.connected_nodes):
                edge = self.mcg.edges[node.connected_edges[j]]
                used_rooms.add(edge.mcp_room_index)
                if self._navmeshes_valid:
                    navmesh_name = self.get_navmesh_name_from_room_index(edge.mcp_room_index)
                    room_info = f"(Room {edge.mcp_room_index}, {navmesh_name})"
                else:
                    room_info = f"(Room {edge.mcp_room_index})"
                output += f"    --> {connected_node_index} {room_info}\n"
        for room in self.mcp.rooms:
            if room.index not in used_rooms:
                output += f"NO EDGES: Room {room.index}\n"
        return output

    def draw(self, room_color="cyan", label_rooms=False, label_nodes=False, axes=None, auto_show=True):
        import matplotlib.pyplot as plt

        if axes is None:
            fig = plt.figure(figsize=(8, 8))
            axes = fig.add_subplot(111, projection="3d")
        self.mcp.draw(room_color=room_color, label_rooms=label_rooms, axes=axes, auto_show=False)
        self.mcg.draw(label_nodes=label_nodes, axes=axes, auto_show=False)
        if auto_show:
            plt.show()

    def save(self, map_path=None, write_msb=False, msb_path=None):
        if map_path is None:
            mcp_path = mcg_path = None  # use original paths
        else:
            mcp_path = Path(map_path / f"{self.map_id}.mcp")
            mcg_path = Path(map_path / f"{self.map_id}.mcg")
        self.mcp.write(mcp_path)
        self.mcg.write(mcg_path)
        # print(f"# MCP and MCG files written for map {self.map_id}.")
        if write_msb:
            self._msb.write(msb_path)
            # print(f"# MSB file (from NavmeshGraph) written for map {self.map_id}.")


def backup_all_mcp_msg(source_map, dest_map):
    """Arguments should be 'map' directory (e.g. in game root)."""
    for mcg_path in Path(source_map).glob("*/*.mcg"):
        dest_path = Path(dest_map, mcg_path.parent.relative_to(source_map))
        dest_path.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(mcg_path), str(dest_path))
    for mcp_path in Path(source_map).glob("*/*.mcp"):
        dest_path = Path(dest_map, mcp_path.parent.relative_to(source_map))
        dest_path.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(mcp_path), str(dest_path))


# TODO: Move to tests.

TEST_MAP = "m12_00_00_01"


def test_mcp(axes=None, show=False):
    from soulstruct import DSR_PATH

    test = MCP(DSR_PATH + f"/map/{TEST_MAP}/{TEST_MAP}.mcp")
    for i, room in enumerate(test.rooms):
        print(f"Room {i}:\n" f"    Box: {room.get_vertices()}\n")

    test.draw(axes, show)
    return test


def test_mcg(axes=None, auto_show=False):
    from soulstruct import DSR_PATH

    test = MCG(DSR_PATH + f"/map/{TEST_MAP}/{TEST_MAP}.mcg")
    for i, node in enumerate(test.nodes):
        print(f"Node {i}:\n" f"     -> nodes: {node.connected_nodes}\n" f"    via edges: {node.connected_edges}")

    test.draw(axes, auto_show=auto_show)
    return test


def test_draw_mcp_mcg():
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(8, 8))
    axes = fig.add_subplot(111, projection="3d")
    test_mcp(axes)
    test_mcg(axes)
    plt.show()


def test_move():
    import matplotlib.pyplot as plt
    from soulstruct import DSR_PATH

    mcg = MCG(DSR_PATH + f"/map/{TEST_MAP}/{TEST_MAP}.mcg")
    mcp = MCP(DSR_PATH + f"/map/{TEST_MAP}/{TEST_MAP}.mcp")

    fig = plt.figure(figsize=(16, 8))
    fig.canvas.set_window_title("Moved")
    axes_orig = fig.add_subplot(121, projection="3d")
    axes = fig.add_subplot(122, projection="3d")

    mcg.draw(axes_orig, auto_show=False)
    mcp.draw(axes_orig, auto_show=False)

    mcg.move_in_world((0, 0, 0), (0, 0, 0), 0, 45)
    mcp.move_in_world((0, 0, 0), (0, 0, 0), 0, 45, enclose_original=False)
    mcg.draw(axes, auto_show=False)
    mcp.draw(axes, auto_show=False)
    plt.show()


def draw_multiple_maps(map_ids):
    import matplotlib.pyplot as plt
    from soulstruct import DSR_PATH

    fig = plt.figure(figsize=(8, 8))
    axes = fig.add_subplot(111, projection="3d")
    colors = ("cyan", "blue", "green", "pink")
    for i, map_id in enumerate(map_ids):
        graph = NavmeshGraph(DSR_PATH + f"/map/{map_id}")
        graph.draw(axes=axes, auto_show=False, room_color=colors[i])
    plt.show()


if __name__ == "__main__":
    draw_multiple_maps(("m12_00_00_01", "m13_01_00_00"))
