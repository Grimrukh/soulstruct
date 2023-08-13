from __future__ import annotations

import copy
import logging
import typing as tp
from dataclasses import dataclass, field
from itertools import product

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation

from .utilities import import_matplotlib_plt

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.maps.msb import MSB
    from soulstruct.darksouls1r.maps.parts import MSBNavmesh

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class NavmeshAABBStruct(BinaryStruct):
    map_id: list[int] = field(**BinaryArray(4, byte))  # stored as (DD, CC, BB, AA) reversed format
    _index: int  # just index in `MCP` file
    connected_aabbs_count: int
    connected_aabbs_offset: int
    aabb_start: Vector3
    aabb_end: Vector3


@dataclass(slots=True)
class NavmeshAABB:
    """Simple AABB (axis-aligned bounding box) around a navmesh part (indexed directly from MSB), with a list of other
    navmesh part (or equivalently, `NavmeshAABB`) indices that this one connects to.

    More importantly, I believe that the navmesh distances used for backread purposes use simple raycasts into these
    AABB volumes.

    NOTE: Connected navmesh parts are not dereferenced because it is likely not worth it. The corresponding navmesh
    parts can be retrieved with the `get_connected_*()` methods as needed.
    """

    map_id: tuple[int, int, int, int] = (-1, -1, -1, -1)  # NOTE: -1 cannot be packed to this `byte` field (must be set)
    aabb_start: Vector3 = field(default_factory=Vector3.zero)
    aabb_end: Vector3 = field(default_factory=Vector3.zero)
    connected_navmesh_part_indices: list[int] = field(default_factory=list)

    @classmethod
    def from_mcp_reader(cls, reader: BinaryReader):
        """`connected_navmeshes` is constructed by calling `MCP`."""
        aabb = NavmeshAABBStruct.from_bytes(reader)

        _reversed_map_id = aabb.pop("map_id")
        map_id = (_reversed_map_id[3], _reversed_map_id[2], _reversed_map_id[1], _reversed_map_id[0])
        with reader.temp_offset(aabb.pop("connected_aabbs_offset")):
            connected_navmesh_indices = list(reader.unpack(f"{aabb.pop('connected_aabbs_count')}i"))

        return cls(map_id, aabb.aabb_start, aabb.aabb_end, connected_navmesh_indices)

    def to_mcp_writer(self, writer: BinaryWriter, aabb_index: int, connected_aabbs_offset: int):
        """Packs the `NavmeshAABBStruct` header definition.

        Connected navmeshes are packed further into `MCP` and the starting offset passed to this.
        """
        return NavmeshAABBStruct(
            map_id=list(reversed(self.map_id)),
            _index=aabb_index,
            connected_aabbs_count=len(self.connected_navmesh_part_indices),
            connected_aabbs_offset=connected_aabbs_offset,
            aabb_start=self.aabb_start,
            aabb_end=self.aabb_end,
        ).to_writer(writer)

    def pack_connected_navmesh_indices(self, writer: BinaryWriter):
        writer.pack(f"{len(self.connected_navmesh_part_indices)}i", *self.connected_navmesh_part_indices)

    def get_connected_aabbs(self, aabbs: list[NavmeshAABB]) -> list[NavmeshAABB]:
        return [aabbs[index] for index in self.connected_navmesh_part_indices]

    def get_connected_navmesh_parts(self, msb: MSB) -> list[MSBNavmesh]:
        return [msb.navmeshes[index] for index in self.connected_navmesh_part_indices]

    def get_connected_navmesh_part_names(self, msb: MSB) -> list[str]:
        return [msb.navmeshes[index].name for index in self.connected_navmesh_part_indices]

    def add_translate(self, translate: Vector3):
        """Add `translate` to AABB start and end."""
        self.aabb_start += translate
        self.aabb_end += translate

    def rotate_in_world(
        self,
        rotation: Matrix3 | Vector3 | list | tuple | int | float,
        pivot_point: Vector3 | list | tuple = (0, 0, 0),
        radians=False,
        enclose_original=True,
    ):
        """Modify entity `aabb_start` and `aabb_end` by rotating it around some pivot in world coordinates (defaults to
        the world origin). A single rotation value is a shortcut for Y rotation only.

        If `enclose_original=True` (default), the size of the rotated AABB will be modified to fully enclose what the
        original AABB would have looked like if it were properly rotated (as the AABB is aligned to the world axes).
        """
        rotation = resolve_rotation(rotation, radians=radians)
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
    def connected_navmesh_count(self):
        """Given in `repr` below, so may as well have a matching property."""
        return len(self.connected_navmesh_part_indices)

    def __repr__(self) -> str:
        return (
            f"NavmeshAABB(\n"
            f"    map_id={self.map_id},\n"
            f"    aabb_start={self.aabb_start},\n"
            f"    aabb_end={self.aabb_end},\n"
            f"    connected_navmesh_indices={self.connected_navmesh_part_indices},\n"
            f")"
        )

    def copy(self) -> NavmeshAABB:
        """Return a deep copy of this NavmeshAABB."""
        return copy.deepcopy(self)

    def draw(self, label="", axes=None, show=False, aabb_color="cyan"):
        plt = import_matplotlib_plt(raise_if_missing=True)
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


@dataclass(slots=True)
class MCP(GameFile):
    """Straightforward file containing AABB volumes for navmeshes in the MSB.

    The number of AABBs must exactly match the number of `MSBNavmesh` entries in the corresponding MSB. Each one
    also lists indices of connected navmeshes (referenced here directly as other `NavmeshAABB` instances for
    convenience) for backread purposes.

    These AABBs are generated by simply taking the minimum and maximum navmesh vertex coordinates for each axis and
    adding `MESH_PADDING` additional space to those components. (Note that the vertical Y axis has more padding than
    the X or Z axes, unlike the NVM box quadtree.)

    The connections between AABBs can be inferred from nodes in the `MCG` graph. My investigation indicates that two
    navmesh AABBs are connected if and only if there exists a `GateNode` with an edge in each of those navmeshes, with
    three exceptions in vanilla DS1 where AABBs are connected but no shared node exists:
        - In m10_00 (Depths), n0032B0 completely covers n0033B0 (other side of bars that look into Giant Rat room).
        - In m12_01 (Royal Wood), n0049B1 completely covers n0050B0 (a patch in first half of Royal Wood).
        - In m13_02 (Great Hollow), n0107B2 has a drop-down to n0114B2, but there are two extremely close nodes at that
          connection point connected by a tiny edge that (incorrectly, I contend) passes through a third navmesh.
    """

    MESH_PADDING: tp.ClassVar[Vector3] = Vector3((0.5, 1.5, 0.5))  # in-game distance units

    @dataclass(slots=True)
    class MCPHeader(BinaryStruct):
        two: int = field(init=False, **Binary(asserted=2))  # 0x2000000 for Demon's Souls (big endian)
        unknown: int = field(init=False, **Binary(asserted=4228561))  # for DSR at least
        aabbs_count: int
        aabbs_offset: int

    aabbs: list[NavmeshAABB] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> MCP:
        header = cls.MCPHeader.from_bytes(reader)
        reader.seek(header.pop("aabbs_offset"))
        aabbs = [NavmeshAABB.from_mcp_reader(reader) for _ in range(header.pop("aabbs_count"))]
        return cls(aabbs=aabbs)

    def to_writer(self) -> BinaryWriter:
        writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
        self.MCPHeader(aabbs_count=len(self.aabbs), aabbs_offset=RESERVED).to_writer(writer, self)

        connected_navmesh_indices_offsets = []  # needed below
        for aabb in self.aabbs:
            connected_navmesh_indices_offsets.append(writer.position)
            aabb.pack_connected_navmesh_indices(writer)

        writer.fill_with_position("aabbs_offset", obj=self)
        for i, aabb in enumerate(self.aabbs):
            aabb.to_mcp_writer(writer, i, connected_navmesh_indices_offsets[i])
        return writer

    def __getitem__(self, navmesh_index: int):
        return self.aabbs[navmesh_index]

    def __iter__(self):
        return iter(self.aabbs)

    def disconnect_aabbs(
        self,
        first_group: set[int | NavmeshAABB],
        second_group: set[int | NavmeshAABB],
    ):
        """Disconnects all AABBBs in `first_group` from all AABBs in `second_group`."""
        if isinstance(first_group, int):
            first_group_indices = {first_group}
        elif isinstance(first_group, NavmeshAABB):
            try:
                first_group_indices = {self.aabbs.index(first_group)}
            except ValueError:
                raise IndexError(f"Given `first_group` AABB index {first_group} is out of bounds for this `MCP`.")
        else:
            first_group_indices = {i if isinstance(i, int) else self.aabbs.index(i) for i in first_group}

        if isinstance(second_group, int):
            second_group_indices = {second_group}
        elif isinstance(second_group, NavmeshAABB):
            try:
                second_group_indices = {self.aabbs.index(second_group)}
            except ValueError:
                raise IndexError(f"Given `second_group` AABB index {second_group} is out of bounds for this `MCP`.")
        else:
            second_group_indices = {i if isinstance(i, int) else self.aabbs.index(i) for i in second_group}

        intersection = first_group_indices.intersection(second_group_indices)
        if intersection:
            raise ValueError(f"AABB indices cannot be in both groups to be disconnected: {intersection}")

        for i, aabb in enumerate(self.aabbs):
            aabb: NavmeshAABB
            if i in first_group_indices:
                # Remove all second group indices.
                aabb.connected_navmesh_part_indices = [
                    j for j in aabb.connected_navmesh_part_indices if j not in second_group_indices
                ]
            elif i in second_group_indices:
                # Remove all first group indices.
                aabb.connected_navmesh_part_indices = [
                    j for j in aabb.connected_navmesh_part_indices if j not in first_group_indices
                ]

    def move_in_world(
        self,
        start_translate: Vector3 = None,
        end_translate: Vector3 = None,
        start_rotate: Vector3 = None,
        end_rotate: Vector3 = None,
        enclose_original=True,
        selected_aabbs: tp.Collection[int | NavmeshAABB] = None,
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
            raise TypeError(f"`start_translate` must be a `Vector3`, not {type(start_translate)}.")
        if end_translate is None:
            end_translate = Vector3.zero()
        elif not isinstance(end_translate, Vector3):
            raise TypeError(f"`end_translate` must be a `Vector3`, not {type(end_translate)}.")
        if start_rotate is None:
            start_rotate = Vector3.zero()
        elif not isinstance(start_rotate, Vector3):
            raise TypeError(f"`start_rotate` must be a `Vector3`, not {type(start_rotate)}.")
        if end_rotate is None:
            end_rotate = Vector3.zero()
        elif not isinstance(end_rotate, Vector3):
            raise TypeError(f"`end_rotate` must be a `Vector3`, not {type(end_rotate)}.")

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
        rotation: Matrix3 | Vector3 | list | tuple | int | float,
        pivot_point=(0, 0, 0),
        radians=False,
        enclose_original=True,
        selected_aabbs: tp.Iterable[int | NavmeshAABB] = None,
    ):
        """Rotate every `NavmeshAABB` in the map around the given pivot by the given Euler angles coordinate system.

        The pivot defaults to the world origin.

        Use `selected_aabbs` (indices or `NavmeshAABB` instances) to specify only a subset of AABBs to move.
        """
        rotation = resolve_rotation(rotation)
        pivot_point = Vector3(pivot_point)
        for i, aabb in enumerate(self.aabbs):
            if selected_aabbs is None or i in selected_aabbs or aabb in selected_aabbs:
                aabb.rotate_in_world(rotation, pivot_point, radians=radians, enclose_original=enclose_original)

    def translate_all(
        self,
        translate: Vector3 | list | tuple,
        selected_aabbs: tp.Iterable[int | NavmeshAABB] = None,
    ):
        """Translate every `NavmeshAABB` in the map by the given `translate` vector.

        Use `selected_aabbs` (indices or `NavmeshAABB` instances) to specify only a subset of AABBs to move.
        """
        for i, aabb in enumerate(self.aabbs):
            if selected_aabbs is None or i in selected_aabbs or aabb in selected_aabbs:
                aabb.add_translate(translate)

    def draw(self, aabb_color="cyan", aabb_labels: str | list[str] = None, axes=None, auto_show=True):
        """Draw all AABBs in `MCP` and their connections in 3D."""
        if aabb_labels == "auto":
            aabb_labels = list(range(len(self.aabbs)))
        plt = import_matplotlib_plt(raise_if_missing=True)
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
