from __future__ import annotations

__all__ = [
    "GateNode",
    "GateEdge",
    "MCG",
]

import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation
from soulstruct.utilities.misc import MISSING_REF

from .utilities import ExistingConnectionError, import_matplotlib_plt

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.maps.parts import MSBNavmesh
    from .mcp import NavmeshAABB

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class GateNode:

    @dataclass(slots=True)
    class GateNodeHeader(BinaryStruct):
        connection_count: int
        translate: Vector3
        connected_nodes_offset: int
        connected_edges_offset: int
        dead_end_navmesh_index: int
        unknown_offset: int

    translate: Vector3 = field(default_factory=Vector3.zero)
    # TODO: Large offset that increases (usually) by varying multiples of 16. No clue currently what it is.
    unknown_offset: int = 0
    dead_end_navmesh: MSBNavmesh | None = MISSING_REF  # indicates this is the only node connecting to this navmesh
    connected_nodes: list[GateNode] = field(default_factory=list)
    connected_edges: list[GateEdge] = field(default_factory=list)

    # Temporary indices.
    _dead_end_navmesh_index: int | None = None
    _connected_node_indices: list[int] | None = None
    _connected_edge_indices: list[int] | None = None

    @classmethod
    def from_mcg_reader(cls, reader: BinaryReader) -> GateNode:
        header = cls.GateNodeHeader.from_bytes(reader)

        with reader.temp_offset(header.connected_nodes_offset):
            _connected_node_indices = list(reader.unpack(f"{header.connection_count}i"))

        with reader.temp_offset(header.connected_edges_offset):
            _connected_edge_indices = list(reader.unpack(f"{header.connection_count}i"))

        return cls(
            header.translate,
            header.unknown_offset,
            _dead_end_navmesh_index=header.dead_end_navmesh_index,
            _connected_node_indices=_connected_node_indices,
            _connected_edge_indices=_connected_edge_indices,
        )

    def set_dead_end_navmesh_reference(self, navmeshes: list[MSBNavmesh]):
        """De-reference the dead end navmesh index to a navmesh instance. May be `None`."""
        if self._dead_end_navmesh_index == -1:
            self.dead_end_navmesh = None
        elif self._dead_end_navmesh_index > -1:
            self.dead_end_navmesh = navmeshes[self._dead_end_navmesh_index]
        self._dead_end_navmesh_index = None

    def set_connected_nodes_edges_references(self, gate_nodes: list[GateNode], gate_edges: list[GateEdge]):
        """De-reference other connected `GateNode` instances and `GateEdge` instances."""
        self.connected_nodes = [gate_nodes[i] for i in self._connected_node_indices]
        self._connected_node_indices = None
        self.connected_edges = [gate_edges[i] for i in self._connected_edge_indices]
        self._connected_edge_indices = None

    def validate_connections(self):
        """Checks that connected node count and connected edge count are identical.

        Raises a `ValueError` if not. Called at the start of most methods.
        """
        if (node_count := len(self.connected_nodes)) != (edge_count := len(self.connected_edges)):
            raise ValueError(
                f"Number of connected nodes ({node_count}) does not match number of connected edges ({edge_count})."
            )

    def set_dead_end_navmesh_index(self, navmeshes: list[MSBNavmesh]):
        self._dead_end_navmesh_index = navmeshes.index(self.dead_end_navmesh) if self.dead_end_navmesh else -1
        self.dead_end_navmesh = MISSING_REF

    def to_mcg_writer(self, writer: BinaryWriter, connected_nodes_offset: int, connected_edges_offset: int):
        """The offsets passed in are written earlier in the file, and are already known.

        No reserved fields.
        """
        if self._dead_end_navmesh_index is None:
            raise ValueError(
                "MCG `GateNode.dead_end_navmesh` has not been indexed (e.g. with `MCG.set_indices(navmeshes)`."
            )
        self.validate_connections()

        self.GateNodeHeader(
            connection_count=len(self.connected_nodes),
            translate=self.translate,
            connected_nodes_offset=connected_nodes_offset,
            connected_edges_offset=connected_edges_offset,
            dead_end_navmesh_index=self._dead_end_navmesh_index,
            unknown_offset=self.unknown_offset,
        ).to_writer(writer)

    def pack_connected_node_indices(self, mcg_writer: BinaryWriter, mcg_nodes: list[GateNode]):
        _connected_node_indices = [mcg_nodes.index(node) for node in self.connected_nodes]
        mcg_writer.pack(f"<{len(_connected_node_indices)}i", *_connected_node_indices)

    def pack_connected_edge_indices(self, mcg_writer: BinaryWriter, mcg_edges: list[GateEdge]):
        _connected_edge_indices = [mcg_edges.index(edge) for edge in self.connected_edges]
        mcg_writer.pack(f"<{len(_connected_edge_indices)}i", *_connected_edge_indices)

    def get_touching_navmeshes(self) -> list[MSBNavmesh]:
        """Return only the navmesh part instances in `navmeshes` that are touched by this node.

        "Touching a node" means that a navmesh is used by a connected edge or is the `dead_end_navmesh` of this node.
        """
        if self.dead_end_navmesh is MISSING_REF:
            raise ValueError("GateNode has not had its dead-end navmesh deferenced.")
        touched_navmeshes = []
        for edge in self.connected_edges:
            if edge.navmesh not in touched_navmeshes:
                touched_navmeshes.append(edge.navmesh)
        if self.dead_end_navmesh and self.dead_end_navmesh not in touched_navmeshes:
            # NOTE: Dead-end navmeshes should never appear as edge navmeshes (they shouldn't contain any), but checking
            # just in case.
            touched_navmeshes.append(self.dead_end_navmesh)
        return touched_navmeshes

    def add_connection(self, other_node: GateNode, edge: GateEdge):
        """Add a connection to `other_node` via `edge`.

        Raises an `ExistingConnectionError` if the nodes are already connected.
        """
        if other_node in self.connected_nodes or edge in self.connected_edges:
            raise ExistingConnectionError("Nodes are already connected.")
        self.connected_nodes.append(other_node)
        self.connected_edges.append(edge)

    def rotate_in_world(
        self,
        rotation: Matrix3 | Vector3 | list | tuple | int | float,
        pivot_point: Vector3 | tuple[float, float, float] = (0.0, 0.0, 0.0),
        radians=False,
    ):
        """Modify node `translate` by rotating it around some `pivot_point` by `rotation` Euler angles in world."""
        rotation = resolve_rotation(rotation, radians=radians)
        pivot_point = Vector3(pivot_point)
        self.translate = (rotation @ (self.translate - pivot_point)) + pivot_point

    def __repr__(self) -> str:
        if self.dead_end_navmesh:
            return (
                f"GateNode({self.translate}, "
                f"connected_nodes=<{len(self.connected_nodes)}>, "
                f"connected_edges=<{len(self.connected_edges)}>, "
                f"dead_end_navmesh=<{self.dead_end_navmesh.name}>"
                f")"
            )
        return (
            f"GateNode({self.translate}, "
            f"connected_nodes=<{len(self.connected_nodes)}>, "
            f"connected_edges=<{len(self.connected_edges)}>"
            f")"
        )


@dataclass(slots=True)
class GateEdge:
    """Edge between two `GateNode` instances in an `MCG` file.

    Note that these objects in the `MCG` file reference indices of navmesh parts in the `MSB` file.

    Each edge specifies the exact triangles on the attached navmesh (which should have flag `NavmeshType.Gate`) that are
    located at its start and end nodes (which, interestingly, do not simply specify it themselves).
    """

    @dataclass(slots=True)
    class GateEdgeHeader(BinaryStruct):
        _start_node_index: int
        start_node_triangles_count: int
        start_node_triangles_offset: int
        _end_node_index: int
        end_node_triangles_count: int
        end_node_triangles_offset: int
        _navmesh_part_index: int
        _reversed_map_id: list[int] = field(**BinaryArray(4, byte))  # stored as (DD, CC, BB, AA) reversed format
        cost: float  # for AI navigation, presumably

    start_node_triangle_indices: list[int] = field(default_factory=list)
    end_node_triangle_indices: list[int] = field(default_factory=list)
    map_id: tuple[int, int, int, int] = (-1, -1, -1, -1)  # NOTE: -1 cannot be packed to this `byte` field (must be set)
    cost: float = 0.0

    start_node: GateNode = MISSING_REF
    end_node: GateNode = MISSING_REF
    navmesh: MSBNavmesh = MISSING_REF

    _start_node_index: int | None = None
    _end_node_index: int | None = None
    _navmesh_part_index: int | None = None

    @classmethod
    def from_mcg_reader(cls, reader: BinaryReader) -> GateEdge:
        edge = cls.GateEdgeHeader.from_bytes(reader)

        with reader.temp_offset(edge.start_node_triangles_offset):
            start_node_triangle_indices = list(reader.unpack(f"{edge.start_node_triangles_count}i"))

        with reader.temp_offset(edge.end_node_triangles_offset):
            end_node_triangle_indices = list(reader.unpack(f"{edge.end_node_triangles_count}i"))

        _reversed_map_id = edge.pop("_reversed_map_id")
        map_id = (_reversed_map_id[3], _reversed_map_id[2], _reversed_map_id[1], _reversed_map_id[0])

        return edge.to_object(
            cls,
            map_id=map_id,
            start_node_triangle_indices=start_node_triangle_indices,
            end_node_triangle_indices=end_node_triangle_indices,
        )

    def set_navmesh_reference(self, navmeshes: list[MSBNavmesh]):
        self.navmesh = navmeshes[self._navmesh_part_index]
        self._navmesh_part_index = None  # consumed

    def set_node_references(self, gate_nodes: list[GateNode]):
        self.start_node = gate_nodes[self._start_node_index]
        self._start_node_index = None  # consumed
        self.end_node = gate_nodes[self._end_node_index]
        self._end_node_index = None  # consumed

    def set_navmesh_index(self, navmeshes: list[MSBNavmesh]):
        self._navmesh_part_index = navmeshes.index(self.navmesh)
        self.navmesh = MISSING_REF

    def to_mcg_writer(
        self,
        writer: BinaryWriter,
        start_node_triangles_offset: int,
        end_node_triangles_offset: int,
        gate_nodes: list[GateNode],
    ):
        """The offsets passed in are written earlier in the file and are already known."""
        if self._navmesh_part_index is None:
            raise ValueError(
                "MCG `GateEdge.navmesh` has not been indexed (e.g. with `MCG.set_indices(navmeshes)`."
            )
        if -1 in self.map_id:
            raise ValueError(f"Map ID of MCG `GateEdge` has not been changed from invalid default: {self.map_id}")
        _reversed_map_id = list(reversed(self.map_id))
        self.GateEdgeHeader(
            _start_node_index=gate_nodes.index(self.start_node),
            start_node_triangles_count=len(self.start_node_triangle_indices),
            start_node_triangles_offset=start_node_triangles_offset,
            _end_node_index=gate_nodes.index(self.end_node),
            end_node_triangles_count=len(self.end_node_triangle_indices),
            end_node_triangles_offset=end_node_triangles_offset,
            _navmesh_part_index=self._navmesh_part_index,
            _reversed_map_id=_reversed_map_id,
            cost=self.cost,
        ).to_writer(writer)

    def pack_start_node_triangle_indices(self, writer: BinaryWriter):
        """Happens before header write."""
        index_count = len(self.start_node_triangle_indices)
        return writer.pack(f"{index_count}i", *self.start_node_triangle_indices)

    def pack_end_node_triangle_indices(self, writer: BinaryWriter):
        """Happens before header write."""
        index_count = len(self.end_node_triangle_indices)
        return writer.pack(f"{index_count}i", *self.end_node_triangle_indices)

    def is_connecting_nodes(self, first_node: GateNode, second_node: GateNode) -> bool:
        """Returns `True` if this edge connects the two given nodes in either direction, and `False` if not."""
        return (
            first_node is self.start_node and second_node is self.end_node
            or first_node is self.end_node and second_node is self.start_node
        )


@dataclass(slots=True)
class MCG(GameFile):

    @dataclass(slots=True)
    class MCGHeaderStruct(BinaryStruct):
        one: int = field(init=False, **Binary(asserted=1))  # 0x1000000 in Demon's Souls (big endian)
        unk0: int
        nodes_count: int
        nodes_offset: int
        edges_count: int
        edges_offset: int
        unk1: int
        unk2: int

    nodes: list[GateNode] = field(default_factory=list)
    edges: list[GateEdge] = field(default_factory=list)
    unknowns: tuple[int, int, int] = (0, 0, 0)  # DS1 default

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> MCG:
        header = cls.MCGHeaderStruct.from_bytes(reader)
        unknowns = (header.unk0, header.unk1, header.unk2)
        reader.seek(header.nodes_offset)
        nodes = [GateNode.from_mcg_reader(reader) for _ in range(header.nodes_count)]
        reader.seek(header.edges_offset)
        edges = [GateEdge.from_mcg_reader(reader) for _ in range(header.edges_count)]

        mcg = cls(nodes=nodes, edges=edges, unknowns=unknowns)
        mcg.set_node_edge_references()
        # NOTE:
        return mcg

    def set_navmesh_references(self, navmeshes: list[MSBNavmesh]):
        for node in self.nodes:
            node.set_dead_end_navmesh_reference(navmeshes)
        for edge in self.edges:
            edge.set_navmesh_reference(navmeshes)

    def set_node_edge_references(self):
        for node in self.nodes:
            node.set_connected_nodes_edges_references(self.nodes, self.edges)
        for edge in self.edges:
            edge.set_node_references(self.nodes)

    def set_navmesh_indices(self, navmeshes: list[MSBNavmesh]):
        """Convert dead-end navmesh references (MSB parts) to indices.

        Must be called just prior to `write()` or `bytes(mcg)`.
        """
        for node in self.nodes:
            node.set_dead_end_navmesh_index(navmeshes)
        for edge in self.edges:
            edge.set_navmesh_index(navmeshes)

    def to_writer(self) -> BinaryWriter:

        if self.nodes and not self.nodes[0].dead_end_navmesh is not None:
            raise ValueError("MCG.set_navmesh_indices(navmeshes)` must be called before writing it.")

        writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
        self.MCGHeaderStruct(
            unk0=self.unknowns[0],
            nodes_count=len(self.nodes),
            nodes_offset=RESERVED,
            edges_count=len(self.edges),
            edges_offset=RESERVED,
            unk1=self.unknowns[1],
            unk2=self.unknowns[2],
        ).to_writer(writer, self)

        edge_start_node_triangle_offsets = []
        edge_end_node_triangle_offsets = []
        for edge in self.edges:
            edge_start_node_triangle_offsets.append(writer.position)
            edge.pack_start_node_triangle_indices(writer)
            edge_end_node_triangle_offsets.append(writer.position)
            edge.pack_end_node_triangle_indices(writer)

        connected_node_offsets = []
        connected_edge_offsets = []
        for node in self.nodes:
            connected_node_offsets.append(writer.position if node.connected_nodes else 0)
            node.pack_connected_node_indices(writer, self.nodes)
            connected_edge_offsets.append(writer.position if node.connected_edges else 0)
            node.pack_connected_edge_indices(writer, self.edges)

        writer.fill_with_position("edges_offset", obj=self)
        for i, edge in enumerate(self.edges):
            edge.to_mcg_writer(
                writer, edge_start_node_triangle_offsets[i], edge_end_node_triangle_offsets[i], self.nodes
            )

        writer.fill_with_position("nodes_offset", obj=self)
        for i, node in enumerate(self.nodes):
            node.to_mcg_writer(writer, connected_node_offsets[i], connected_edge_offsets[i])

        return writer

    def get_edges_in_navmesh(self, navmesh: MSBNavmesh) -> list[GateEdge]:
        """Return a list of all `GateEdge` instances attached to the given `MSBNavmesh`."""
        return [edge for edge in self.edges if edge.navmesh is navmesh]

    def disconnect_nodes(
        self,
        first_node: int | GateNode,
        second_node: int | GateNode,
        ignore_unconnected=True,
    ):
        """Looks for and deletes the edge between the two nodes (in either direction).

        This is generally safer than deleting MCG edges directly by index, since it is easier to work with node indices
        than edge indices (because edges are more likely to appear/disappear than nodes).

        If `ignore_unconnected=False`, this raises a `ValueError` if no edge between the two nodes is found. By default,
        this error is suppressed. Always raises an error if multiple edges are found, since this should never happen.
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
            if ignore_unconnected:
                return  # do nothing, don't complain
            raise ValueError(
                f"No edges found that connect node index {first_node_index} and node index {second_node_index}."
            )
        elif len(edge_matches) > 1:
            raise ValueError(
                f"Multiple edges found that connect node index {first_node_index} and node index {second_node_index}. "
                f"This should never happen in a well-formed `MCG`!"
            )
        edge = edge_matches[0]
        self.delete_edge(edge)

    def connect_nodes(
        self,
        start_node: int | GateNode,
        end_node: int | GateNode,
        edge_navmesh: int | MSBNavmesh,
        start_node_navmesh_triangle_indices: list[int],
        end_node_navmesh_triangle_indices: list[int],
        cost: float = None,  # defaults to twice the distance between the nodes
        map_id=None,  # defaults to `map_id` of last edge in `MCG`
        ignore_connected=False,
    ):
        """Create a new `GateEdge` that connects the given nodes, with the given navmesh and cost.

        Also updates the `connected_nodes` and `connected_edges` lists of the nodes accordingly. If `map_id` is None,
        copies from last edge (as all edges in an MCG will generally have the same map ID). If `cost` is None, it will
        default to twice the distance between the nodes (a very rough observed heuristic).

        Note that `start_node` must always be the node with the smaller MCG index. They will be reversed if necessary.

        If `ignore_connected=False`, an `ExistingConnectionError` is raised if the nodes are already connected.
        """
        if isinstance(start_node, int):
            first_node_index = start_node
            start_node = self.nodes[start_node]
        else:
            try:
                first_node_index = self.nodes.index(start_node)
            except ValueError:
                raise ValueError(f"Start node {start_node} not found in MCG.")
        if isinstance(end_node, int):
            second_node_index = end_node
            end_node = self.nodes[end_node]
        else:
            try:
                second_node_index = self.nodes.index(end_node)
            except ValueError:
                raise ValueError(f"End node {end_node} not found in MCG.")

        # Reverse nodes if necessary.
        if first_node_index > second_node_index:
            start_node, end_node = end_node, start_node
            start_node_navmesh_triangle_indices, end_node_navmesh_triangle_indices = (
                end_node_navmesh_triangle_indices,
                start_node_navmesh_triangle_indices,
            )
            second_node_index, first_node_index = first_node_index, second_node_index

        # Check edge doesn't already exist.
        for i, edge in enumerate(self.edges):
            if edge.is_connecting_nodes(start_node, end_node):
                if ignore_connected:
                    return  # don't raise error, just return
                raise ValueError(f"Nodes {start_node} and {end_node} are already connected by edge with index {i}.")

        if map_id is None:
            if not self.edges:
                raise ValueError("Must specify `map_id` as no edges are currently in the MCG.")
            map_id = self.edges[-1].map_id

        if cost is None:
            cost = 2 * abs(start_node.translate - end_node.translate)

        new_edge = GateEdge(
            start_node=start_node,
            end_node=end_node,
            navmesh=edge_navmesh,
            start_node_triangle_indices=start_node_navmesh_triangle_indices,
            end_node_triangle_indices=end_node_navmesh_triangle_indices,
            cost=cost,
            map_id=map_id,
        )

        start_node.connected_nodes.append(end_node)
        start_node.connected_edges.append(new_edge)

        end_node.connected_nodes.append(start_node)
        end_node.connected_edges.append(new_edge)

        _LOGGER.info(f"Created new edge between node indices {first_node_index} and {second_node_index}.")

    def delete_edge(self, edge: int | GateEdge):
        """Delete given `edge` from in `MCG` and remove all references to its connection in nodes.

        Currently, assumes that no two edges have identical (or reversed) start and end nodes, which should be true.

        Use of `mcg.disconnect_nodes()` is recommended instead of this method, as it will automatically find the edge
        and delete it, rather than the user needing to deal directly with existing edges at all.
        """
        if isinstance(edge, int):
            edge = self.edges[edge]
        elif edge not in self.edges:
            raise ValueError("Given `edge` is not an edge in this `MCG`.")
        for node in self.nodes:
            connected_nodes = []
            connected_edges = []
            for n, e in zip(node.connected_nodes, node.connected_edges):
                if e is not edge:
                    connected_nodes.append(n)
                    connected_edges.append(e)
            node.connected_nodes = connected_nodes
            node.connected_edges = connected_edges
        self.edges.remove(edge)

    def move_in_world(
        self,
        start_translate: Vector3 = None,
        end_translate: Vector3 = None,
        start_rotate: Vector3 | list | tuple | int | float = None,
        end_rotate: Vector3 | list | tuple | int | float = None,
        selected_nodes: tp.Iterable[int | GateNode] = None,
    ):
        """Rotate and then translate all nodes in MCG in world coordinates, so that an entity with a translate of
        `start_translate` and rotate of `start_rotate` ends up with a translate of `end_translate` and a rotate of
        `end_rotate`.

        Works by simply shifting the `.translate` points of each node.
        """
        if start_translate is None:
            start_translate = Vector3.zero()
        elif not isinstance(start_translate, Vector3):
            raise TypeError(f"`start_translate` must be a `Vector3`, not {start_translate}.")
        if end_translate is None:
            end_translate = Vector3.zero()
        elif not isinstance(end_translate, Vector3):
            raise TypeError(f"`end_translate` must be a `Vector3`, not {end_translate}.")
        m_start_rotate = resolve_rotation(start_rotate)
        m_end_rotate = resolve_rotation(end_rotate)

        # Compute global rotation matrix required to get from `start_rotate` to `end_rotate`.
        m_world_rotate = m_end_rotate @ m_start_rotate.T

        # Apply global rotation to start point to determine required global translation.
        translation = end_translate - (m_world_rotate @ start_translate)  # type: Vector3

        self.rotate_all_nodes_in_world(m_world_rotate, selected_nodes=selected_nodes)
        self.translate_all(translation, selected_nodes=selected_nodes)

    def rotate_all_nodes_in_world(
        self,
        rotation: Matrix3 | Vector3 | list | tuple | int | float,
        pivot_point: Vector3 | tuple[float, float, float] = (0.0, 0.0, 0.0),
        radians=False,
        selected_nodes: tp.Iterable[int | NavmeshAABB] = None,
    ):
        """Rotate every node in the MCG around the given pivot by the given Euler angles coordinate system.

        The pivot defaults to the world origin.
        """
        rotation = resolve_rotation(rotation)
        pivot_point = Vector3(pivot_point)
        for i, node in enumerate(self.nodes):
            if selected_nodes is None or i in selected_nodes or node in selected_nodes:
                node.rotate_in_world(rotation, pivot_point=pivot_point, radians=radians)

    def translate_all(
        self,
        translate: Vector3 | list | tuple,
        selected_nodes: tp.Iterable[int | NavmeshAABB] = None,
    ):
        """Translate every node in the MCG by the given vector."""
        for i, node in enumerate(self.nodes):
            if selected_nodes is None or i in selected_nodes or node in selected_nodes:
                node.translate += translate

    def draw(self, node_labels: None | str | list[str] = None, axes=None, auto_show=True):
        plt = import_matplotlib_plt(raise_if_missing=True)
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
