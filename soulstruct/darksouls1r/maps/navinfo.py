"""Classes for MCG and MCP files, and other navmesh-related tools.

Currently only set up for DS1R.

Detailed information about the relationship between MSB navmeshes and collisions, MCP files, and MCG files:

    - A navmesh is a simple mesh comprised of triangular faces. Each face has a certain flag associated with it, which
    are enumerated in `NavmeshType` (e.g. "Solid", "Wall", "Cliff", "Ladder").

    - Enemy pathing is plotted out as a sequence of moves from face to face (to the center of each face, specifically).
    Some enemies are not permitted to have paths planned out over faces with certain flags (e.g. only some characters
    can climb ladders).

    - Navmeshes are generally (about 95% of the time) 1:1 with collisions and generally have matching model indices
    (e.g. "n0003B0" is generally congruent with collision "h0003B0"). Sometimes, one navmesh can cover multiple
    collisions, but I don't believe I've seen one collision cover multiple navmeshes in DS1.

    - Each navmesh in a map has a corresponding "room" in that map's MCP file. These rooms simply index the navmeshes
    in the order they are contained inside the MSB. These rooms are simple "AABBs" (axis-aligned bounding boxes) aligned
    to the world axes, so they aren't particularly veridical to the map geometry. Each room is connected to a list of
    other rooms.

    - Each map also has an MCG file containing a graph that helps AI use the navmesh. The nodes on this graph are
    "gates" between MCP rooms, with "edges" connecting them that each pass through one room index from the MCP.

    - The MCP navmesh rooms control *backread*, based on the player's distance from that room's box (likely a simple
    raycast). The game also only seems to check the distance to rooms that are connected to the one the player is
    standing inside (or was last standing inside). This is why it is CRITICAL that your MCP files are accurate to your
    navmeshes, particularly for connections between maps (as the backread status of other maps' collisions REQUIRES this
    navmesh raycast to succeed, whereas collisions inside the same map can use display groups).

    - The "navmesh groups" of navmeshes that are in backread (because their corresponding rooms are close enough and
    connected) are used to upgrade two backread tables, one "normal" (possibly characters, objects, etc., or possibly
    unused) and one "hit" (collisions). In DS1, the distances for "normal" backread (enabled at 20m, disabled at 25m)
    are smaller than for "hit" backread (enabled after spending 0.2s closer than 80m, disabled after spending 1.3s
    further than 90m). You can play with these values in the debug menu (`GAME > WorldBackRead`).

    - By default (i.e. without any navmeshes and no navmesh-produced backread), the player's current collision has
    backread 4 (low + hi poly versions), all other collisions in the current map have backread 2 (low poly only), and
    all collisions in all other loaded maps have backread 0.

    - These backreads states are "upgraded" by navmesh backread groups. If a navmesh's MCP AABB is within the "hit"
    backread distance, it is loaded (appears under "WorldBackRead" menu).

    - The distance to the room the player is current inside is always 0.0. If the player is standing inside multiple
    rooms, the game appears to prefer the room that matches the player's navmesh, or that is inside the map of the
    player's current collision? Unclear exactly how this preferential system works, but it does seem that the game only
    checks the distance of rooms that are linked to the last room the player was inside.

    - Any collisions whose navmesh groups are covered by the navmesh group of a triggered navmesh will be "upgraded".
    Collisions in the current map will go from backread 2 to backread 4. Collisions in connected maps will go from
    backread 0 to backread 2.

    - That is, navmesh groups and an intact navmesh-produced backread system are NECESSARY to get collisions in other
    connected maps to load. The connection's display groups alone can't get backread high enough to give the other map's
    collisions any actual physics!

    - The *draw groups* of collisions appear to be used for *children only*! Actual collision physics are determined
    solely by backread state, which is determined by navmesh rooms and navmesh groups.

Notes for functional navmesh system:

    - Every navmesh must have at least one "related" node. Related nodes are nodes that have an edge passing through
    that navmesh's AABB (as referenced by `edge.connected_aabb`) or nodes that explicitly reference that AABB through
    their `node.connected_aabb` attribute. The game uses this direct connection IF AND ONLY IF the navmesh has no nodes
    that are related through edges - that is, a "dead end" navmesh that has no edges within it.

    - Every navmesh must have at least one connected AABB in its `aabb.connected_aabbs` attribute, or it will never
    enter backread, even when standing on it (and may screw up other navmeshes nearby as well).

    - Gate node positions do not affect backread, but the connectivity BETWEEN them does seem to inform which navmeshes
    can enter backread from a distance. As long as the two requirements above are met (and `MapConnection` instances are
    set up properly), you will probably be able to navigate the world without issues, as navmeshes enter backread "just
    in time" when walking on them, but proper connected nodes are needed for the actual raycasting 80m/90m system to
    work. This will need to be done for enemy behavior anyway.

    - It should go without saying that breaking correspondence between the connected nodes and edges of nodes will
    cause major issues, so don't do this.
"""
from __future__ import annotations

__all__ = [
    "MCP",
    "NavmeshAABB",
    "MCG",
    "GateNode",
    "GateEdge",
    "NavInfo",
    "NavInfoError",
    "NavmeshSyncError",
    "ExistingConnectionError",
]

import copy
import shutil
import struct
import typing as tp
from itertools import product
from pathlib import Path

from soulstruct.exceptions import SoulstructError
from soulstruct.base.game_file import GameFile
from soulstruct.darksouls1ptde.maps.msb import MSB as PTDE_MSB
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader
from soulstruct.utilities.maths import Vector3, Matrix3

from .msb import MSB
from .parts import MSBNavmesh


class NavInfoError(SoulstructError):
    """Base exception raised by `NavInfo`."""


class NavmeshSyncError(NavInfoError):
    """Number of MSB navmeshes does not match number of MCP AABBs in `NavInfo`."""


class ExistingConnectionError(NavInfoError):
    """Tried to connect two MCG nodes or MCP AABBs that are already connected."""


class NavmeshAABB(BinaryObject):

    STRUCT = BinaryStruct(
        ("__map_id", "4b"),  # always just the current map; also, parts are reversed, so m12_01_00_00 has [0, 0, 1, 12]
        ("__index", "i"),  # always identical to actual index in `MCP` file
        ("__connected_aabbs_count", "i"),
        ("__connected_aabbs_offset", "i"),
        ("aabb_start", "3f"),
        ("aabb_end", "3f"),
    )

    map_id: tuple[int, int, int, int]
    aabb_start: Vector3
    aabb_end: Vector3
    _connected_navmesh_indices: list[int, ...]
    connected_aabbs: list[NavmeshAABB, ...]

    def __init__(self, reader: BinaryReader = None, /, **kwargs):
        """Simple AABB (axis-aligned bounding box) around a navmesh (indexed directly from MSB), with a list of other
        `NavmeshAABB` instances (indexed) that this one connects to.

        `NavmeshAABB`s are also indexed by `GateEdge`s in MCG files, which connect `Gate` nodes that generally lie close
        to transitions between navmeshes.

        More importantly, I believe that the navmesh distances used for backread purposes use simple raycasts into
        these AABB volumes.
        """
        self.map_id = (-1, -1, -1, -1)
        self.aabb_start = Vector3(0, 0, 0)
        self.aabb_end = Vector3(1, 1, 1)
        self.connected_aabbs = []  # constructed by `MCP` from indices below
        self._connected_navmesh_indices = []
        super().__init__(reader, **kwargs)

    def unpack(self, reader: BinaryReader):
        """`connected_navmeshes` is constructed by calling `MCP`."""
        room = reader.unpack_struct(self.STRUCT)
        map_id = room.pop("__map_id")  # reversed
        self.map_id = (map_id[3], map_id[2], map_id[1], map_id[0])
        self._connected_navmesh_indices = []
        with reader.temp_offset(room.pop("__connected_aabbs_offset")):
            for _ in range(room.pop("__connected_aabbs_count")):
                self._connected_navmesh_indices.append(reader.unpack_value("<i"))

        self.set(**room)

    def set_connected_aabbs(self, aabbs: list[NavmeshAABB, ...]):
        self.connected_aabbs = [aabbs[i] for i in self._connected_navmesh_indices]
        self._connected_navmesh_indices = []

    def pack(self, aabb_index: int, connected_aabbs_offset: int):
        """Packs the `NavmeshAABB` header definition.

        Connected AABBs are packed further into `MCP` and the starting offset passed to this.
        """
        return self.STRUCT.pack(
            __map_id=list(reversed(self.map_id)),
            __index=aabb_index,
            __connected_aabbs_count=len(self.connected_aabbs),
            __connected_aabbs_offset=connected_aabbs_offset,
            aabb_start=list(self.aabb_start),
            aabb_end=list(self.aabb_end),
        )

    def pack_connected_navmesh_indices(self, navmesh_aabbs: list[NavmeshAABB, ...]) -> bytes:
        self._connected_navmesh_indices = [navmesh_aabbs.index(aabb) for aabb in self.connected_aabbs]
        return struct.pack(f"<{len(self._connected_navmesh_indices)}i", *self._connected_navmesh_indices)

    def add_translate(self, translate: tp.Union[Vector3, list, tuple]):
        """Add `translate` to AABB start and end."""
        self.aabb_start += translate
        self.aabb_end += translate

    def rotate_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        enclose_original=True,
    ):
        """Modify entity `aabb_start` and `aabb_end` by rotating it around some pivot in world coordinates (defaults to
        the world origin). A single rotation value is a shortcut for Y rotation only.

        If `enclose_original=True` (default), the size of the rotated AABB will be modified to fully enclose what the
        original AABB would have looked like if it were properly rotated (as the AABB is aligned to the world axes).
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
            self.aabb_start = Vector3([min(v[i] for v in rotated_vertices) for i in range(3)])
            self.aabb_end = Vector3([max(v[i] for v in rotated_vertices) for i in range(3)])
        else:
            self.aabb_start = (rotation @ (self.aabb_start - pivot_point)) + pivot_point
            self.aabb_end = (rotation @ (self.aabb_end - pivot_point)) + pivot_point

    @property
    def volume_center(self):
        return (self.aabb_start + self.aabb_end) / 2

    def get_vertices(self, swap_yz=False):
        """Extrapolate all eight vertices of the AABB."""
        x, y, z = zip(self.aabb_start, self.aabb_end)  # (start, end) for each dimension
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

    @property
    def connected_aabb_count(self):
        """Given in `repr` below, so may as well have a matching property."""
        return len(self.connected_aabbs)

    def __repr__(self) -> str:
        return (
            f"NavmeshAABB(\n"
            f"    map_id={self.map_id},\n"
            f"    aabb_start={self.aabb_start},\n"
            f"    aabb_end={self.aabb_end},\n"
            f"    connected_aabb_count={len(self.connected_aabbs)},\n"
            f")"
        )

    def copy(self) -> NavmeshAABB:
        """Return a deep copy of this NavmeshAABB."""
        return copy.deepcopy(self)

    def draw(self, label="", axes=None, show=False, aabb_color="cyan"):
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
        if label:
            axes.text(self.volume_center[0], self.volume_center[2], self.volume_center[1], label, c="black")
        axes.add_collection3d(
            Poly3DCollection(
                self.get_faces(swap_yz=True), facecolors=aabb_color, linewidths=0.1, edgecolors="red", alpha=0.05
            )
        )
        if show:
            plt.show()


class MCP(GameFile):

    HEADER_STRUCT = BinaryStruct(
        ("__two", "i", 2),  # 0x2000000 for Demon's Souls (big endian)
        ("__unknown", "i", 4228561),  # for DSR at least
        ("__aabbs_count", "i"),
        ("__aabbs_offset", "i"),
    )

    aabbs: list[NavmeshAABB, ...]

    def __init__(self, mcp_source=None, dcx_magic=()):
        """Straightforward file containing AABB volumes for navmeshes in the MSB.

        The number of AABBs must exactly match the number of `MSBNavmesh` entries in the corresponding MSB. Each one
        also lists indices of connected navmeshes (referenced here directly as other `NavmeshAABB` instances for
        convenience) for backread purposes.
        """
        self.aabbs = []
        super().__init__(mcp_source, dcx_magic)

    def unpack(self, reader: BinaryReader, **kwargs):
        header = reader.unpack_struct(self.HEADER_STRUCT)
        reader.seek(header.pop("__aabbs_offset"))
        self.aabbs = [NavmeshAABB(reader) for _ in range(header.pop("__aabbs_count"))]
        for aabb in self.aabbs:
            # Resolve indices into `NavmeshAABB` instances.
            aabb.set_connected_aabbs(self.aabbs)

    def pack(self) -> bytes:
        offset = self.HEADER_STRUCT.size
        connected_navmesh_indices_offsets = []
        all_packed_connected_navmesh_indices = b""
        for aabb in self.aabbs:
            connected_navmesh_indices_offsets.append(offset)
            packed_connected_navmesh_indices = aabb.pack_connected_navmesh_indices(self.aabbs)
            all_packed_connected_navmesh_indices += packed_connected_navmesh_indices
            offset += len(packed_connected_navmesh_indices)

        packed = self.HEADER_STRUCT.pack(
            __aabbs_count=len(self.aabbs),
            __aabbs_offset=offset,
        )
        packed += all_packed_connected_navmesh_indices
        for i, aabb in enumerate(self.aabbs):
            packed += aabb.pack(i, connected_navmesh_indices_offsets[i])
        return packed

    def __getitem__(self, navmesh_index: int):
        return self.aabbs[navmesh_index]

    def __iter__(self):
        return iter(self.aabbs)

    def new_aabb(
        self, map_id, aabb_start, aabb_end, connected_aabbs: list[tp.Union[int, NavmeshAABB], ...]
    ) -> NavmeshAABB:
        """Add a new `NavmeshAABB` instance to the end of the MCP AABB list, connected to all given AABB instances or
        indices, and return it.
        """
        connected_aabbs = [self.aabbs[i] if isinstance(i, int) else i for i in connected_aabbs]
        aabb = NavmeshAABB(
            map_id=map_id,
            aabb_start=aabb_start,
            aabb_end=aabb_end,
            connected_aabbs=connected_aabbs,
        )
        self.aabbs.append(aabb)
        return aabb

    def duplicate_aabb(self, source: tp.Union[int, NavmeshAABB], **kwargs) -> NavmeshAABB:
        """Duplicate given `NavmeshAABB` instance or index."""
        if isinstance(source, int):
            source = self.aabbs[source]
        elif not isinstance(source, NavmeshAABB):
            raise TypeError(
                f"`source` AABB to duplicate must be an `NavmeshAABB` or index of an existing one, not {type(source)}."
            )
        aabb = source.copy()
        aabb.set(**kwargs)
        self.aabbs.append(aabb)
        return aabb

    def delete_aabb(self, aabb: tp.Union[int, NavmeshAABB]):
        """Delete `aabb`, which can be an `NavmeshAABB` instance in this `MCP` or an index of one.

        Also removes the AABB from the `.connected_navmeshes` list of all other `NavmeshAABB` instances.

        Remember to also:
            - remove the corresponding navmesh in the MSB.
            - delete any edges that pass through this AABB in the MCG. (`NavInfo` wrapper method handles this.)
        """
        if isinstance(aabb, int):
            aabb = self.aabbs[aabb]
        elif not isinstance(aabb, NavmeshAABB):
            raise TypeError(
                f"`aabb` to delete must be an `NavmeshAABB` or index of an existing one, not {type(aabb)}."
            )
        elif aabb not in self.aabbs:
            raise ValueError("Given `aabb` is not a `NavmeshAABB` instance in this `MCP`.")
        self.aabbs.remove(aabb)
        for other_aabb in self.aabbs:
            if aabb in other_aabb.connected_aabbs:
                other_aabb.connected_aabbs.remove(aabb)

    def disconnect_aabbs(
        self,
        first_group: set[tp.Union[int, NavmeshAABB], ...],
        second_group: set[tp.Union[int, NavmeshAABB], ...],
    ):
        """Disconnects all AABBBs in `first_group` from all AABBs in `second_group`."""
        if isinstance(first_group, int):
            first_group = {self.aabbs[first_group]}
        elif isinstance(first_group, NavmeshAABB):
            first_group = {first_group}
        else:
            first_group = {self.aabbs[i] if isinstance(i, int) else i for i in first_group}
        if isinstance(second_group, int):
            second_group = {self.aabbs[second_group]}
        elif isinstance(second_group, NavmeshAABB):
            second_group = {second_group}
        else:
            second_group = {self.aabbs[i] if isinstance(i, int) else i for i in second_group}

        intersection = first_group.intersection(second_group)
        if intersection:
            raise ValueError(f"AABBs cannot be in both groups to be disconnected: {intersection}")
        for aabb in self.aabbs:
            if aabb in first_group:
                aabb.connected_aabbs = [r for r in aabb.connected_aabbs if r not in second_group]
            elif aabb in second_group:
                aabb.connected_aabbs = [r for r in aabb.connected_aabbs if r not in first_group]

    def move_in_world(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        enclose_original=True,
        selected_aabbs: tp.Iterable[tp.Union[int, NavmeshAABB]] = None,
    ):
        """Rotate and then translate all `NavmeshAABB`s in MCP in world coordinates, so that an entity with a translate
        of `start_translate` and rotate of `start_rotate` ends up with a translate of `end_translate` and a rotate of
        `end_rotate`. Use `selected_aabbs` (indices or `NavmeshAABB` instances) to specify only a subset of AABBs to
        move.

        Works by simply shifting the `aabb_start` and `aabb_end` points of each AABB.

        If `enclose_original=True` (default), each AABB will be upsized as necessary when rotated to guarantee that it
        completely contains its original volume. If multiple sequential rotations are expected, it is best to disable
        this until the last rotation, or it may grow unnecessarily large.
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

        self.rotate_all_aabbs_in_world(
            m_world_rotate, enclose_original=enclose_original, selected_aabbs=selected_aabbs
        )
        self.translate_all(translation, selected_aabbs=selected_aabbs)

    def rotate_all_aabbs_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        enclose_original=True,
        selected_aabbs: tp.Iterable[tp.Union[int, NavmeshAABB]] = None,
    ):
        """Rotate every `NavmeshAABB` in the map around the given pivot by the given Euler angles coordinate system.

        The pivot defaults to the world origin.

        Use `selected_aabbs` (indices or `NavmeshAABB` instances) to specify only a subset of AABBs to move.
        """
        if isinstance(rotation, (int, float)):
            rotation = Matrix3.from_euler_angles(0.0, rotation, 0.0)  # single rotation value interpreted as Y rotation
        elif isinstance(rotation, (Vector3, list, tuple)):
            rotation = Matrix3.from_euler_angles(rotation)
        elif not isinstance(rotation, Matrix3):
            raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
        pivot_point = Vector3(pivot_point)
        for i, aabb in enumerate(self.aabbs):
            if selected_aabbs is None or i in selected_aabbs or aabb in selected_aabbs:
                aabb.rotate_in_world(rotation, pivot_point, radians=radians, enclose_original=enclose_original)

    def translate_all(
        self,
        translate: tp.Union[Vector3, list, tuple],
        selected_aabbs: tp.Iterable[tp.Union[int, NavmeshAABB]] = None,
    ):
        """Translate every `NavmeshAABB` in the map by the given `translate` vector.

        Use `selected_aabbs` (indices or `NavmeshAABB` instances) to specify only a subset of AABBs to move.
        """
        for i, aabb in enumerate(self.aabbs):
            if selected_aabbs is None or i in selected_aabbs or aabb in selected_aabbs:
                aabb.add_translate(translate)

    def draw(self, aabb_color="cyan", aabb_labels: tp.Union[str, list[str]] = None, axes=None, auto_show=True):
        """Draw all AABBs in `MCP` and their connections in 3D."""
        if aabb_labels == "auto":
            aabb_labels = list(range(len(self.aabbs)))
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ModuleNotFoundError("Optional `matplotlib` module is needed to draw MCG graphs.")
        if axes is None:
            fig = plt.figure(figsize=(8, 8))
            axes = fig.add_subplot(111, projection="3d")
        else:
            fig = axes.figure
        for i, aabb in enumerate(self.aabbs):
            aabb.draw(label=aabb_labels[i] if aabb_labels else None, axes=axes, aabb_color=aabb_color)
            for connected_aabb in aabb.connected_aabbs:
                x, z, y = zip(aabb.volume_center, connected_aabb.volume_center)  # NOTE: y, z swapped
                axes.plot(x, y, z, color="red")

        # Get min/max values on each axis to simulate equal aspect ratio.
        mins = Vector3([min(aabb.aabb_start[i] for aabb in self.aabbs) for i in range(3)])
        maxs = Vector3([max(aabb.aabb_end[i] for aabb in self.aabbs) for i in range(3)])
        mids = (mins + maxs) / 2
        max_range = max(maxs - mins) / 2
        axes.set_xlim(mids.x - max_range, mids.x + max_range)
        axes.set_ylim(mids.z - max_range, mids.z + max_range)
        axes.set_zlim(mids.y - max_range, mids.y + max_range)

        axes.set(xlabel="X", ylabel="Z", zlabel="Y")
        fig.tight_layout()
        if auto_show:
            plt.show()


class GateNode(BinaryObject):

    STRUCT = BinaryStruct(
        ("__connection_count", "i"),
        ("translate", "3f"),
        ("__connected_nodes_offset", "i"),
        ("__connected_edges_offset", "i"),
        ("__connected_aabb_index", "i"),
        ("unknown_offset", "i"),  # large offset (MB range) that mostly (but not always) ascends
    )

    translate: Vector3
    _connected_aabb_index: int
    connected_aabb: tp.Optional[NavmeshAABB]
    unknown_offset: int
    _connected_node_indices: list[int, ...]
    connected_nodes: list[GateNode, ...]
    _connected_edge_indices: list[int, ...]
    connected_edges: list[GateEdge, ...]

    def __init__(self, reader: BinaryReader = None, /, **kwargs):
        self._connected_aabb_index = -1
        self._connected_node_indices = []  # type: list[int, ...]
        self._connected_edge_indices = []  # type: list[int, ...]
        self.connected_aabb = None
        self.connected_nodes = []  # constructed by `MCG`
        self.connected_edges = []  # edges connect to `connected_nodes` with the same index
        super().__init__(reader, **kwargs)

    def unpack(self, reader: BinaryReader):
        node = reader.unpack_struct(self.STRUCT)
        connection_count = node.pop("__connection_count")

        self._connected_node_indices = []
        with reader.temp_offset(node.pop("__connected_nodes_offset")):
            for _ in range(connection_count):
                self._connected_node_indices.append(reader.unpack_value("<i"))

        self._connected_edge_indices = []
        with reader.temp_offset(node.pop("__connected_edges_offset")):
            for _ in range(connection_count):
                self._connected_edge_indices.append(reader.unpack_value("<i"))

        self._connected_aabb_index = node.pop("__connected_aabb_index")

        self.set(**node)

    def set_connected_aabb_nodes_edges(
        self, aabbs: list[NavmeshAABB], gate_nodes: list[GateNode, ...], gate_edges: list[GateEdge, ...]
    ):
        if self._connected_aabb_index != -1:
            self.connected_aabb = aabbs[self._connected_aabb_index]
        self.connected_nodes = [gate_nodes[i] for i in self._connected_node_indices]
        self.connected_edges = [gate_edges[i] for i in self._connected_edge_indices]
        self._connected_node_indices = []
        self._connected_edge_indices = []

    def validate_connections(self):
        """Checks that connected node count and connected edge count are identical.

        Raises a `ValueError` if not. Called at the start of most methods.
        """
        if (node_count := len(self.connected_nodes)) != (edge_count := len(self.connected_edges)):
            raise ValueError(
                f"Number of connected nodes ({node_count}) does not match number of connected edges ({edge_count})."
            )

    def pack(self, connected_nodes_offset: int, connected_edges_offset: int, aabbs: list[NavmeshAABB]):
        self.validate_connections()
        return self.STRUCT.pack(
            __connection_count=len(self.connected_nodes),
            translate=list(self.translate),
            __connected_nodes_offset=connected_nodes_offset,
            __connected_edges_offset=connected_edges_offset,
            __connected_aabb_index=aabbs.index(self.connected_aabb) if self.connected_aabb else -1,
            unknown_offset=self.unknown_offset,
        )

    def pack_connected_node_indices(self, mcg_nodes: list[GateNode, ...]) -> bytes:
        self._connected_node_indices = [mcg_nodes.index(node) for node in self.connected_nodes]
        node_count = len(self._connected_node_indices)
        return struct.pack(f"<{node_count}i", *self._connected_node_indices)

    def pack_connected_edge_indices(self, mcg_edges: list[GateEdge, ...]):
        self._connected_edge_indices = [mcg_edges.index(edge) for edge in self.connected_edges]
        edge_count = len(self._connected_edge_indices)
        return struct.pack(f"<{edge_count}i", *self._connected_edge_indices)

    def add_connection(self, other_node: GateNode, edge: GateEdge):
        """Add a connection to `other_node` via `edge`.

        Raises an `ExistingConnectionError` if the nodes are already connected.
        """
        if other_node in self.connected_nodes or edge in self.connected_edges:
            raise ExistingConnectionError("Nodes are already connected.")
        self.connected_nodes.append(other_node)
        self.connected_edges.append(edge)

    def remove_connections(
        self, nodes: tp.Iterable[tp.Union[int, GateNode]] = (), edges: tp.Iterable[tp.Union, int, GateEdge] = ()
    ):
        """Remove connections to all given `nodes` or through any given `edges` and corresponding edges/nodes."""
        raise NotImplementedError("`node.remove_connections` currently not working as intended!")
        self.validate_connections()
        if isinstance(nodes, int):
            nodes = {self.connected_nodes[nodes]}
        elif isinstance(nodes, GateNode):
            nodes = {nodes}
        else:
            nodes = {self.connected_nodes[i] if isinstance(i, int) else i for i in edges}
        if isinstance(edges, int):
            edges = {self.connected_edges[edges]}
        elif isinstance(edges, GateEdge):
            edges = {edges}
        else:
            edges = {self.connected_edges[i] if isinstance(i, int) else i for i in edges}
        self.connected_edges = []
        self.connected_nodes = []
        for edge, node in zip(self.connected_edges, self.connected_nodes):
            if node not in nodes and edge not in edges:
                self.connected_edges.append(edge)
                self.connected_nodes.append(node)

    def delete_edges_in_aabb(self, aabb: NavmeshAABB):
        node_connections_to_delete = []
        for connected_node, connected_edge in zip(self.connected_nodes, self.connected_edges):
            if connected_edge.aabb is aabb:
                node_connections_to_delete.append(connected_node)
        self.remove_connections(nodes=node_connections_to_delete)

    def rotate_in_world(
        self, rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float], pivot_point=(0, 0, 0), radians=False
    ):
        """Modify node `translate` by rotating it around some `pivot_point` by `rotation` Euler angles` in world."""
        if isinstance(rotation, (int, float)):
            # Single rotation value is a shortcut for Y rotation.
            rotation = Matrix3.from_euler_angles(0.0, rotation, 0.0, radians=radians)
        elif isinstance(rotation, (Vector3, list, tuple)):
            rotation = Matrix3.from_euler_angles(rotation, radians=radians)
        elif not isinstance(rotation, Matrix3):
            raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
        pivot_point = Vector3(pivot_point)

        self.translate = (rotation @ (self.translate - pivot_point)) + pivot_point


class GateEdge(BinaryObject):
    """Edge between two `GateNode` instances in an `MCG` file.

    Note that these objects in the `MCG` file reference indices of `NavmeshAABB` instances in the `MCP` file.

    The two file types (`MCG` and `MCP`) must be carefully synchronized with each other, and also with the actual
    Navmeshes in the MSB, which correspond one-to-one in order to AABBs in the `MCP` file.

    Each edge has two sets of unknown indices (too large to be AABBs, nodes, edges, or navmesh parts) and one unknown
    float, which seems very loosely related to the edge length in my research (though is sometimes five digits). TK
    suspects these are weights, for AI computations presumably.
    """

    STRUCT = BinaryStruct(
        ("_start_node_index", "i"),
        ("__unk1_count", "i"),  # unknown indices; likely related to use of start node
        ("__unk1_offset", "i"),
        ("_end_node_index", "i"),
        ("__unk2_count", "i"),  # unknown indices; likely related to use of end node
        ("__unk2_offset", "i"),
        ("_aabb_index", "i"),
        ("map_id", "4b"),
        ("cost", "f"),  # for AI navigation, presumably
    )

    _start_node_index: tp.Optional[int]
    start_node: tp.Optional[GateNode]
    _end_node_index: tp.Optional[int]
    end_node: tp.Optional[GateNode]
    _aabb_index: tp.Optional[int]
    aabb: tp.Optional[NavmeshAABB]
    map_id: tuple[int, int, int, int]
    cost: float

    unk1_indices: list[int, ...]
    unk2_indices: list[int, ...]

    DEFAULTS = {
        "_start_node_index": None,
        "_end_node_index": None,
        "_aabb_index": None,
        "map_id": (-1, -1, -1, -1),
    }

    def __init__(self, reader: BinaryReader = None, /, **kwargs):
        self.unk1_indices = []
        self.unk2_indices = []
        self.cost = 1.0
        self.start_node = None
        self.end_node = None
        self.aabb = None
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

    def set_aabb_nodes(self, aabbs: list[NavmeshAABB, ...], gate_nodes: list[GateNode, ...]):
        self.start_node = gate_nodes[self._start_node_index]
        self._start_node_index = None  # resolved
        self.end_node = gate_nodes[self._end_node_index]
        self._end_node_index = None  # resolved
        self.aabb = aabbs[self._aabb_index]
        self._aabb_index = None  # resolved

    def pack(
        self,
        unk1_offset: int,
        unk2_offset: int,
        gate_nodes: list[GateNode, ...],
        aabbs: list[NavmeshAABB, ...],
    ) -> bytes:
        return self.STRUCT.pack(
            _start_node_index=gate_nodes.index(self.start_node),
            __unk1_count=len(self.unk1_indices),
            __unk1_offset=unk1_offset,
            _end_node_index=gate_nodes.index(self.end_node),
            __unk2_count=len(self.unk2_indices),
            __unk2_offset=unk2_offset,
            _aabb_index=aabbs.index(self.aabb),
            map_id=self.map_id,
            cost=self.cost,
        )

    def pack_unk1_indices(self):
        index_count = len(self.unk1_indices)
        return struct.pack(f"<{index_count}i", *self.unk1_indices)

    def pack_unk2_indices(self):
        index_count = len(self.unk2_indices)
        return struct.pack(f"<{index_count}i", *self.unk2_indices)

    def does_edge_connect_nodes(self, first_node: GateNode, second_node: GateNode) -> bool:
        """Returns `True` if this edge connects the two given nodes in either direction, and `False` if not."""
        return (self.start_node, self.end_node) in {(first_node, second_node), (second_node, first_node)}


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

    nodes: list[GateNode]
    edges: list[GateEdge]
    unknowns: tuple[int, int, int]

    def __init__(self, mcg_source=None, dcx_magic=()):
        self.unknowns = (-1, -1, -1)
        super().__init__(mcg_source, dcx_magic=dcx_magic)

    def unpack(self, reader: BinaryReader, **kwargs):
        mcg = reader.unpack_struct(self.HEADER_STRUCT)
        self.unknowns = (mcg["__unk0"], mcg["__unk1"], mcg["__unk2"])
        reader.seek(mcg["__nodes_offset"])
        self.nodes = [GateNode(reader) for _ in range(mcg["__nodes_count"])]
        reader.seek(mcg["__edges_offset"])
        self.edges = [GateEdge(reader) for _ in range(mcg["__edges_count"])]

    def set_references(self, aabbs: list[NavmeshAABB, ...]):
        for node in self.nodes:
            node.set_connected_aabb_nodes_edges(aabbs, self.nodes, self.edges)
        for edge in self.edges:
            edge.set_aabb_nodes(aabbs, self.nodes)

    def pack(self, aabbs: list[NavmeshAABB, ...]) -> bytes:
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
            packed_node_offsets = node.pack_connected_node_indices(self.nodes)
            packed_connection_offsets += packed_node_offsets
            offset += len(packed_node_offsets)

            connected_edge_offsets.append(offset if node.connected_edges else 0)
            packed_edge_offsets = node.pack_connected_edge_indices(self.edges)
            packed_connection_offsets += packed_edge_offsets
            offset += len(packed_edge_offsets)

        edges_offset = offset
        packed_edges = b""
        for i, edge in enumerate(self.edges):
            packed_edges += edge.pack(edge_unk1_offsets[i], edge_unk2_offsets[i], self.nodes, aabbs)

        offset += len(packed_edges)
        nodes_offset = offset
        packed_nodes = b""
        for i, node in enumerate(self.nodes):
            packed_nodes += node.pack(connected_node_offsets[i], connected_edge_offsets[i], aabbs)

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

    def get_edges_in_aabb(self, aabb: NavmeshAABB) -> list[GateEdge, ...]:
        """Return a list of all `GateEdge` instances in the given `NavmeshAABB`."""
        return [edge for edge in self.edges if edge.aabb is aabb]

    def delete_edge_between_nodes(
        self,
        first_node: tp.Union[int, GateNode],
        second_node: tp.Union[int, GateNode],
        allow_missing=True,
    ):
        """Looks for and deletes the edge between the two nodes (in either direction). This is generally safer than
        calling `delete_edge()` directly, since node indices are probably more stable while editing maps.

        If `allow_missing=False`, this raises a `ValueError` if no edge between the two nodes is found. By default, this
        error is suppressed. Always raises an error if multiple edges are found, since this should never happen.
        """
        if isinstance(first_node, int):
            first_node_index = first_node
            first_node = self.nodes[first_node]
        else:
            first_node_index = self.nodes.index(first_node)
        if isinstance(second_node, int):
            second_node_index = second_node
            second_node = self.nodes[second_node]
        else:
            second_node_index = self.nodes.index(second_node)
        edge_matches = []
        for edge in self.edges:
            forward_match = edge.start_node == first_node and edge.end_node == second_node
            backward_match = edge.start_node == second_node and edge.end_node == first_node
            if forward_match or backward_match:
                edge_matches.append(edge)
        if not edge_matches:
            if allow_missing:
                return  # do nothing, don't complain
            raise ValueError(
                f"No edges found that connect node index {first_node_index} and node index {second_node_index}."
            )
        elif len(edge_matches) > 1:
            raise ValueError(
                f"Multiple edges found that connect node index {first_node_index} and node index {second_node_index}. "
                f"This should never happen!"
            )
        edge = edge_matches[0]
        self.delete_edge(edge)

    def add_edge_between_nodes(
        self,
        first_node: tp.Union[int, GateNode],
        second_node: tp.Union[int, GateNode],
        aabb: tp.Union[int, NavmeshAABB],
        ignore_existing=True,
        map_id=None,  # defaults to `map_id` of last edge in `MCG`
    ):
        """If `map_id` is None, copies from last edge. (Also copies unknown indices from last edge.)"""
        if isinstance(first_node, int):
            first_node = self.nodes[first_node]
        if isinstance(second_node, int):
            second_node = self.nodes[second_node]

        # Check edge doesn't already exist.
        for i, edge in enumerate(self.edges):
            if edge.does_edge_connect_nodes(first_node, second_node):
                if ignore_existing:
                    return  # don't raise error, just return
                raise ValueError(f"Nodes {first_node} and {second_node} are already connected by edge with index {i}.")

        if not self.edges:
            raise ValueError("Currently cannot create new edges without any to copy (for unknown data).")

        new_edge = copy.deepcopy(self.edges[-1])
        if map_id is not None:
            new_edge.map_id = map_id
        new_edge.start_node = first_node
        new_edge.end_node = second_node
        new_edge.aabb = aabb
        first_node.connected_nodes.append(second_node)
        first_node.connected_edges.append(new_edge)
        second_node.connected_nodes.append(first_node)
        second_node.connected_edges.append(new_edge)
        # TODO: Log info instead of printing.
        print(
            f"Created new edge between node indices {self.nodes.index(first_node)} and {self.nodes.index(second_node)}."
        )

    def delete_edge(self, edge: tp.Union[int, GateEdge]):
        """Delete given `edge` from in `MCG` and remove all references to its connection in nodes.

        Currently assumes that no two edges have identical (or reversed) start and end nodes, which should be true.
        """
        if isinstance(edge, int):
            edge = self.edges[edge]
        elif edge not in self.edges:
            raise ValueError("Given `edge` is not an edge in this `MCG`.")
        edge.start_node.remove_connections(nodes={edge.end_node})
        edge.end_node.remove_connections(nodes={edge.start_node})
        self.edges.remove(edge)

    def move_in_world(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        selected_nodes: tp.Iterable[tp.Union[int, NavmeshAABB]] = None,
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

        self.rotate_all_nodes_in_world(m_world_rotate, selected_nodes=selected_nodes)
        self.translate_all(translation, selected_nodes=selected_nodes)

    def rotate_all_nodes_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        selected_nodes: tp.Iterable[tp.Union[int, NavmeshAABB]] = None,
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
            if selected_nodes is None or i in selected_nodes or node in selected_nodes:
                node.rotate_in_world(rotation, pivot_point=pivot_point, radians=radians)

    def translate_all(
        self,
        translate: tp.Union[Vector3, list, tuple],
        selected_nodes: tp.Iterable[tp.Union[int, NavmeshAABB]] = None,
    ):
        """Translate every node in the MCG by the given vector."""
        for i, node in enumerate(self.nodes):
            if selected_nodes is None or i in selected_nodes or node in selected_nodes:
                node.translate += translate

    def draw(self, node_labels: tp.Union[None, str, list[str]] = None, axes=None, auto_show=True):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ModuleNotFoundError("Optional `matplotlib` module is needed to draw MCG graphs.")
        if node_labels == "auto":
            node_labels = [str(i) for i in range(len(self.nodes))]
        if axes is None:
            fig = plt.figure()
            axes = fig.add_subplot(111, projection="3d")
        for i, node in enumerate(self.nodes):
            color = "red" if node.connected_aabb is None else "green"
            axes.scatter(node.translate.x, node.translate.z, node.translate.y, s=20, c=color, alpha=0.5)
            if node_labels is not None:
                axes.text(node.translate.x, node.translate.z, node.translate.y, node_labels[i], c=color)
        for edge in self.edges:
            x, y, z = zip(edge.start_node.translate, edge.end_node.translate)
            axes.plot3D(x, z, y, c="black", alpha=0.5)  # NOTE: y and z swapped
        if auto_show:
            plt.show()


class NavInfo:

    def __init__(
        self,
        map_path: tp.Union[str, Path],
        msb_source: tp.Union[None, MSB, str, Path] = None,
        map_id: str = None,
    ):
        """Simple wrapper for both MCP and MCG, which will generally be edited together, as they contain absolute
        references to one another (and the MSB).

        Loads MSB to validate navmesh AABB indices. Provides useful methods for joint editing/moving of MCP and MCG.

        Args:
            map_path (str or Path): Folder containing MCP and MCG files (e.g. '{game_root}/map/m10_01_00_00').
            msb_source (str, Path, or MSB): MSB instance or file path. If None (default), searched for in standard map
                directory structure.
        """
        self.map_path = Path(map_path)
        if not self.map_path.is_dir():
            raise ValueError(f"Map directory does not exist: {str(map_path)}")
        self.map_id = self.map_path.name if map_id is None else map_id

        if isinstance(msb_source, (MSB, PTDE_MSB)):
            self.msb_path = msb_source.path
            self._msb = msb_source
        else:
            if msb_source is None:
                self.msb_path = (self.map_path / f"../MapStudio/{self.map_id}.msb").resolve()
            else:
                self.msb_path = Path(msb_source)
            try:
                self._msb = MSB(self.msb_path)
            except FileNotFoundError:
                raise FileNotFoundError(f"Could not find MSB file: {str(self.msb_path)}")

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
        self.mcg.set_references(self.mcp.aabbs)

    @property
    def msb(self):
        """You can't change the attached MSB instance."""
        return self._msb

    @property
    def navmeshes(self):
        """Shortcut for getting list of Navmesh instances from MSB parts."""
        return self._msb.parts.Navmeshes

    @property
    def aabbs(self):
        return self.mcp.aabbs

    @property
    def nodes(self):
        return self.mcg.nodes

    @property
    def edges(self):
        return self.mcg.edges

    def check_navmesh_sync(self):
        """Raises a `NavmeshSyncError` if the number of MSB Navmeshes does not match the number of MCP AABBs.

        This will no doubt occur briefly as new `MSB` and `NavInfo` instances are constructed, but most `NavInfo`
        methods should not be called at that time.
        """
        # TODO: Convert to decorator once PyCharm fixes decorator `self` issue.
        if (navmesh_count := len(self.navmeshes)) != (aabb_count := len(self.mcp.aabbs)):
            raise NavmeshSyncError(
                f"Number of navmeshes in MSB ({navmesh_count}) does not match the number of AABBs in "
                f"MCP ({aabb_count}). This should be fixed ASAP, or navmesh functionality will be broken."
            )

        nodeless_navmesh_indices = []
        for i, aabb in enumerate(self.aabbs):
            if not self.get_related_nodes(aabb):
                nodeless_navmesh_indices.append(i)
        if nodeless_navmesh_indices:
            # TODO: I thought related nodes were necessary, but vanilla m12_01 has navmeshes without any?
            # print(
            #     f"Found navmesh (AABB) indices with no related nodes: {nodeless_navmesh_indices}. Every navmesh
            #     f"needs at least one related node (with an edge in that AABB or a direct connection) for the navmesh
            #     f"system to function properly, including collision backread."
            # )
            pass

    def get_related_nodes(self, aabb: tp.Union[NavmeshAABB, str, MSBNavmesh], direct_connections_only=False):
        """Return all MCG nodes with at least one edge in the given `AABB` or corresponding MSB navmesh/name."""
        if isinstance(aabb, (str, MSBNavmesh)):
            aabb = self.get_navmesh_aabb(aabb)
        return [
            node for node in self.nodes
            if (not direct_connections_only and any(edge.aabb is aabb for edge in node.connected_edges))
            or node.connected_aabb is aabb
        ]

    def get_navmesh_aabb(self, navmesh: tp.Union[str, MSBNavmesh]) -> NavmeshAABB:
        """Get `NavmeshAABB` with the same index as `navmesh` index in MSB.

        `navmesh` can be an `MSBNavmesh` entry or the name of one. Obviously, if you already have its index in the MSB,
        you can look up the AABB directly already.
        """
        self.check_navmesh_sync()
        if not isinstance(navmesh, MSBNavmesh):
            navmesh = self._msb.parts.get_entry_by_name(navmesh)  # type: MSBNavmesh
        navmesh_index = self.navmeshes.index(navmesh)
        return self.mcp.aabbs[navmesh_index]

    def get_aabb_navmesh(self, aabb: NavmeshAABB) -> MSBNavmesh:
        """Get `MSBNavmesh` entry with the same index as `aabb` in MCP."""
        self.check_navmesh_sync()
        aabb_index = self.mcp.aabbs.index(aabb)
        return self.navmeshes[aabb_index]

    def connect_nodes(
        self,
        start_node: GateNode,
        end_node: GateNode,
        aabb: tp.Union[NavmeshAABB, str, MSBNavmesh],
        edge_indices_1=(1, 2),  # TODO: unknown purpose or good defaults
        edge_indices_2=(3, 4),  # TODO: unknown purpose or good defaults
        edge_cost=1.0,
    ):
        """Connect two nodes with a new edge. Raises an `ExistingConnectionError` if the nodes are already connected.

        TODO: The unknown edge indices definitely matter to some degree, but we don't know what they index.
        """
        if end_node in start_node.connected_nodes or start_node in end_node.connected_nodes:
            raise ExistingConnectionError("Given nodes are already connected by an edge.")
        if isinstance(aabb, (str, MSBNavmesh)):
            aabb = self.get_navmesh_aabb(aabb)
        edge = GateEdge(
            unk1_indices=list(edge_indices_1),
            unk2_indices=list(edge_indices_2),
            cost=edge_cost,
            start_node=start_node,
            end_node=end_node,
            aabb=aabb,
        )
        self.edges.append(edge)
        start_node.add_connection(end_node, edge)
        end_node.add_connection(start_node, edge)

    def delete_aabb_and_edges_inside(self, aabb: NavmeshAABB):
        """Delete MCP `aabb` and any MCG edges that pass through it."""
        self.mcp.delete_aabb(aabb)
        # Delete edges that pass through deleted AABB.
        for edge in self.mcg.get_edges_in_aabb(aabb):
            self.mcg.delete_edge(edge)

    def connect_aabbs(
        self, first_aabb: tp.Union[NavmeshAABB, str, MSBNavmesh], second_aabb: tp.Union[NavmeshAABB, str, MSBNavmesh]
    ):
        """Connect the two given AABBs, which can also be given as MSB navmeshes or names thereof.

        Does NOT modify nodes or edges.
        """
        self.check_navmesh_sync()
        if isinstance(first_aabb, (str, MSBNavmesh)):
            first_aabb = self.get_navmesh_aabb(first_aabb)
        if isinstance(second_aabb, (str, MSBNavmesh)):
            second_aabb = self.get_navmesh_aabb(second_aabb)
        if first_aabb in second_aabb.connected_aabbs or second_aabb in first_aabb.connected_aabbs:
            raise ExistingConnectionError("Given AABBs are already connected.")
        first_aabb.connected_aabbs.append(second_aabb)
        second_aabb.connected_aabbs.append(first_aabb)

    def disconnect_aabbs(
        self, first_aabb: tp.Union[NavmeshAABB, str, MSBNavmesh], second_aabb: tp.Union[NavmeshAABB, str, MSBNavmesh]
    ):
        """Disconnect the two given MCP AABBs, which can also be given as MSB navmeshes or names thereof.

        Any MCG nodes with edges through both of these navmesh AABBs will also have their edge through `second_navmesh`
        deleted.
        """
        self.check_navmesh_sync()
        if isinstance(first_aabb, (str, MSBNavmesh)):
            first_aabb = self.get_navmesh_aabb(first_aabb)
        if isinstance(second_aabb, (str, MSBNavmesh)):
            second_aabb = self.get_navmesh_aabb(second_aabb)
        self.mcp.disconnect_aabbs({first_aabb}, {second_aabb})
        for node in self.mcg.nodes:
            edge_in_first_aabb = any(edge.aabb is first_aabb for edge in node.connected_edges)
            edge_in_second_aabb = any(edge.aabb is second_aabb for edge in node.connected_edges)
            if edge_in_first_aabb and edge_in_second_aabb:
                node.delete_edges_in_aabb(second_aabb)

    def add_aabbs_nodes_edges(
        self,
        aabbs: tp.Iterable[NavmeshAABB],
        nodes: tp.Iterable[GateNode],
        edges: tp.Iterable[GateEdge],
    ):
        """Add new AABBs, nodes, and edges to this `NavInfo` instance simultaneously.

        These new entry instances should generally only contain references to one another, and (for AABBs in particular)
        be added synchronously with MSB navmesh parts to ensure a 1:1 mapping.

        Note that every navmesh/AABB index must have at least one related node, with an edge passing through it or a
        direction reference through `node.connected_aabb`. Navmeshes with no related nodes will not function properly,
        even for collision backread, where the nodes' actual positions don't matter.
        """
        self.aabbs.extend(aabbs)
        self.nodes.extend(nodes)
        self.edges.extend(edges)

    def move_in_world(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float] = None,
        enclose_original=True,
        selected_aabbs: tp.Iterable[tp.Union[int, NavmeshAABB], ...] = None,
        selected_nodes: tp.Iterable[tp.Union[int, GateNode], ...] = None,
    ):
        """Rotate and then translate all AABBs in MCP (enclosing original AABBs by default) and all nodes in MCG in
        world coordinates, so that an entity with a translate of `start_translate` and rotate of `start_rotate` ends up
        with a translate of `end_translate` and a rotate of `end_rotate`.
        """
        self.mcp.move_in_world(
            start_translate,
            end_translate,
            start_rotate,
            end_rotate,
            enclose_original=enclose_original,
            selected_aabbs=selected_aabbs,
        )
        self.mcg.move_in_world(start_translate, end_translate, start_rotate, end_rotate, selected_nodes=selected_nodes)

    def to_string(self):
        """Print out a list of MCG nodes, their connections, and the AABBs those connective edges go through."""
        used_aabbs = set()
        output = ""
        try:
            self.check_navmesh_sync()
            navmeshes_valid = True
        except NavmeshSyncError as ex:
            navmeshes_valid = False
            output += f"WARNING: {ex}.\n"

        for i, aabb in enumerate(self.mcp.aabbs):
            output += f"AABB {i}"
            if navmeshes_valid:
                navmesh = self.get_aabb_navmesh(aabb)
                output += f" ({navmesh.name}):\n"
            else:
                output += f":\n"
            output += f"  AABB start: {aabb.aabb_start}\n"
            output += f"  AABB end:   {aabb.aabb_end}\n"
            for connected_aabb in aabb.connected_aabbs:
                output += f"    --> AABB {self.mcp.aabbs.index(connected_aabb)}"
                if navmeshes_valid:
                    connected_aabb_navmesh = self.get_aabb_navmesh(connected_aabb)
                    output += f" ({connected_aabb_navmesh.name})\n"
                else:
                    output += "\n"

        for i, node in enumerate(self.mcg.nodes):
            output += f"Node {i} [{node.translate}]:\n"
            for j, (connected_node, connected_edge) in enumerate(zip(node.connected_nodes, node.connected_edges)):
                used_aabbs.add(connected_edge.aabb)
                if navmeshes_valid:
                    edge_aabb_navmesh = self.get_aabb_navmesh(connected_edge.aabb)
                    aabb_info = f"(AABB {self.mcp.aabbs.index(connected_edge.aabb)}, {edge_aabb_navmesh.name})"
                else:
                    aabb_info = f"(AABB {self.mcp.aabbs.index(connected_edge.aabb)})"
                output += f"    --> {self.mcg.nodes.index(connected_node)} {aabb_info}\n"
        for aabb in self.mcp.aabbs:
            if aabb not in used_aabbs:
                output += f"NO EDGES: AABB {self.mcp.aabbs.index(aabb)}\n"
        return output

    def draw(
        self,
        aabb_color="cyan",
        label_aabbs=True,
        label_nodes=True,
        axes=None,
        auto_show=True,
        focus_xzy=None,
        focus_size=50,
    ):
        import matplotlib.pyplot as plt

        if axes is None:
            fig = plt.figure(figsize=(8, 8))
            axes = fig.add_subplot(111, projection="3d")

        aabb_labels = [n.name for n in self.navmeshes] if label_aabbs else None
        node_labels = [
            f"{i} ({self.get_aabb_navmesh(node.connected_aabb).name})" if node.connected_aabb else f"{i}"
            for i, node in enumerate(self.nodes)
        ] if label_nodes else None

        self.mcp.draw(aabb_color=aabb_color, aabb_labels=aabb_labels, axes=axes, auto_show=False)
        self.mcg.draw(node_labels=node_labels, axes=axes, auto_show=False)

        if focus_xzy is not None:
            x, z, y = focus_xzy
            axes.set(
                xlim=(x - focus_size, x + focus_size),
                ylim=(y - focus_size, y + focus_size),
                zlim=(z - focus_size, z + focus_size),
            )

        if auto_show:
            plt.show()
        return axes

    def write(self, map_path=None, write_msb=False, msb_path=None):
        if map_path is None:
            mcp_path = mcg_path = None  # use original paths
        else:
            mcp_path = Path(map_path / f"{self.map_id}.mcp")
            mcg_path = Path(map_path / f"{self.map_id}.mcg")
        self.mcp.write(mcp_path)
        self.mcg.write(mcg_path, aabbs=self.aabbs)
        # print(f"# MCP and MCG files written for map {self.map_id}.")
        if write_msb:
            self._msb.write(msb_path)
            # print(f"# MSB file (from NavInfo) written for map {self.map_id}.")


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


def draw_multiple_maps(map_ids):
    import matplotlib.pyplot as plt
    from soulstruct import DSR_PATH

    fig = plt.figure(figsize=(8, 8))
    axes = fig.add_subplot(111, projection="3d")
    colors = ("cyan", "blue", "green", "pink")
    for i, map_id in enumerate(map_ids):
        graph = NavInfo(DSR_PATH + f"/map/{map_id}")
        graph.draw(axes=axes, auto_show=False, aabb_color=colors[i])
    plt.show()
