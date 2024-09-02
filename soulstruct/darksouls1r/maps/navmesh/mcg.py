from __future__ import annotations

__all__ = [
    "MCGNode",
    "MCGEdge",
    "MCG",
]

import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation
from soulstruct.utilities.misc import MISSING_REF, IDList

from .utilities import ExistingConnectionError, import_matplotlib_plt

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.maps.parts import MSBNavmesh
    from .mcp import NavmeshAABB

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MCGNode:

    @dataclass(slots=True)
    class MCGNodeHeader(BinaryStruct):
        connection_count: int
        translate: Vector3
        connected_nodes_offset: int
        connected_edges_offset: int
        dead_end_navmesh_index: int
        unknown_offset: int

    translate: Vector3 = field(default_factory=Vector3.zero)
    # TODO: Large offset that increases (usually) by varying multiples of 16. No clue currently what it is.
    unknown_offset: int = 0
    # If set, this indicates that this is the ONLY node connecting to this navmesh.
    dead_end_navmesh: MSBNavmesh | None = field(default_factory=lambda: MISSING_REF)
    connected_nodes: list[MCGNode] = field(default_factory=list)
    connected_edges: list[MCGEdge] = field(default_factory=list)

    # Temporary indices.
    dead_end_navmesh_index: int | None = None  # not hidden
    _connected_node_indices: list[int] | None = None
    _connected_edge_indices: list[int] | None = None

    @property
    def is_navmesh_deferenced(self):
        return self.dead_end_navmesh is not MISSING_REF

    @property
    def has_dead_end_navmesh(self):
        """Works even if `dead_end_navmesh` is not yet deferenced."""
        return (
            self.dead_end_navmesh_index is not None and self.dead_end_navmesh_index >= 0
            or self.dead_end_navmesh is not MISSING_REF and self.dead_end_navmesh is not None
        )

    @classmethod
    def from_mcg_reader(cls, reader: BinaryReader) -> MCGNode:
        header = cls.MCGNodeHeader.from_bytes(reader)

        with reader.temp_offset(header.connected_nodes_offset):
            _connected_node_indices = list(reader.unpack(f"{header.connection_count}i"))

        with reader.temp_offset(header.connected_edges_offset):
            _connected_edge_indices = list(reader.unpack(f"{header.connection_count}i"))

        return cls(
            header.translate,
            header.unknown_offset,
            dead_end_navmesh_index=header.dead_end_navmesh_index,
            _connected_node_indices=_connected_node_indices,
            _connected_edge_indices=_connected_edge_indices,
        )

    def set_dead_end_navmesh_reference(self, navmeshes: list[MSBNavmesh] | IDList[MSBNavmesh]):
        """De-reference the dead end navmesh index to a navmesh instance. May be `None`."""
        if self.dead_end_navmesh_index is None:
            raise ValueError("Node dead-end navmesh index has already been set (ID consumed).")
        if self.dead_end_navmesh_index == -1:
            self.dead_end_navmesh = None
        elif self.dead_end_navmesh_index > -1:
            self.dead_end_navmesh = navmeshes[self.dead_end_navmesh_index]
        self.dead_end_navmesh_index = None

    def set_connected_nodes_edges_references(self, gate_nodes: list[MCGNode], gate_edges: list[MCGEdge]):
        """De-reference other connected `MCGNode` instances and `MCGEdge` instances."""
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

    def set_dead_end_navmesh_index(self, navmeshes: list[MSBNavmesh] | IDList[MSBNavmesh]):
        if self.dead_end_navmesh is MISSING_REF:
            raise ValueError("MCGNode has not had its dead-end navmesh deferenced.")
        self.dead_end_navmesh_index = navmeshes.index(self.dead_end_navmesh) if self.dead_end_navmesh else -1
        self.dead_end_navmesh = MISSING_REF

    def to_mcg_writer(self, writer: BinaryWriter, connected_nodes_offset: int, connected_edges_offset: int):
        """The offsets passed in are written earlier in the file, and are already known.

        No reserved fields.
        """
        if self.dead_end_navmesh_index is None:
            raise ValueError(
                "MCG `MCGNode.dead_end_navmesh` has not been indexed (e.g. with `MCG.set_indices(navmeshes)`."
            )
        self.validate_connections()

        self.MCGNodeHeader(
            connection_count=len(self.connected_nodes),
            translate=self.translate,
            connected_nodes_offset=connected_nodes_offset,
            connected_edges_offset=connected_edges_offset,
            dead_end_navmesh_index=self.dead_end_navmesh_index,
            unknown_offset=self.unknown_offset,
        ).to_writer(writer)

    def pack_connected_node_indices(self, mcg_writer: BinaryWriter, mcg_nodes: list[MCGNode]):
        _connected_node_indices = [mcg_nodes.index(node) for node in self.connected_nodes]
        mcg_writer.pack(f"<{len(_connected_node_indices)}i", *_connected_node_indices)

    def pack_connected_edge_indices(self, mcg_writer: BinaryWriter, mcg_edges: list[MCGEdge]):
        _connected_edge_indices = [mcg_edges.index(edge) for edge in self.connected_edges]
        mcg_writer.pack(f"<{len(_connected_edge_indices)}i", *_connected_edge_indices)

    def get_touching_navmeshes(self) -> list[MSBNavmesh]:
        """Return only the navmesh part instances in `navmeshes` that are touched by this node.

        "Touching a node" means that a navmesh is used by a connected edge or is the `dead_end_navmesh` of this node.
        """
        if self.dead_end_navmesh is MISSING_REF:
            raise ValueError("MCGNode has not had its dead-end navmesh deferenced.")
        touched_navmeshes = []
        for edge in self.connected_edges:
            if edge.navmesh not in touched_navmeshes:
                touched_navmeshes.append(edge.navmesh)
        if self.dead_end_navmesh and self.dead_end_navmesh not in touched_navmeshes:
            # NOTE: Dead-end navmeshes should never appear as edge navmeshes (they shouldn't contain any), but checking
            # just in case.
            touched_navmeshes.append(self.dead_end_navmesh)
        return touched_navmeshes

    def add_connection(self, other_node: MCGNode, edge: MCGEdge):
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
        if self.dead_end_navmesh is not MISSING_REF:
            return (
                f"MCGNode({self.translate}, "
                f"connected_nodes=<{len(self.connected_nodes)} nodes>, "
                f"connected_edges=<{len(self.connected_edges)} edges>, "
                f"dead_end_navmesh=<{self.dead_end_navmesh.name if self.dead_end_navmesh else 'None'}>"
                f")"
            )
        return (
            f"MCGNode({self.translate}, "
            f"connected_nodes=<{len(self.connected_nodes)} nodes>, "
            f"connected_edges=<{len(self.connected_edges)} edges>, "
            f"dead_end_navmesh_index={self.dead_end_navmesh_index}"
            f")"
        )


@dataclass(slots=True)
class MCGEdge:
    """Edge between two `MCGNode` instances in an `MCG` file.

    Note that these objects in the `MCG` file reference indices of navmesh parts in the `MSB` file.

    Each edge specifies the exact triangles on the attached navmesh (which should have flag `NavmeshFlag.Exit`) that are
    located at its start and end nodes (which, interestingly, do not simply specify it themselves).
    """

    @dataclass(slots=True)
    class MCGEdgeHeader(BinaryStruct):
        _node_a_index: int
        node_a_triangles_count: int
        node_a_triangles_offset: int
        _node_b_index: int
        node_b_triangles_count: int
        node_b_triangles_offset: int
        navmesh_index: int
        _reversed_map_id: list[int] = field(**BinaryArray(4, byte))  # stored as (DD, CC, BB, AA) reversed format
        cost: float  # for AI navigation, presumably

    node_a_triangles: list[int] = field(default_factory=list)
    node_b_triangles: list[int] = field(default_factory=list)
    map_id: tuple[int, int, int, int] = (-1, -1, -1, -1)  # NOTE: -1 cannot be packed to this `byte` field (must be set)
    cost: float = 0.0

    node_a: MCGNode = field(default_factory=lambda: MISSING_REF)
    node_b: MCGNode = field(default_factory=lambda: MISSING_REF)
    navmesh: MSBNavmesh = field(default_factory=lambda: MISSING_REF)

    _node_a_index: int | None = None
    _node_b_index: int | None = None
    navmesh_index: int | None = None  # not hidden

    @property
    def is_navmesh_deferenced(self):
        return self.navmesh is not MISSING_REF

    @classmethod
    def from_mcg_reader(cls, reader: BinaryReader) -> MCGEdge:
        edge = cls.MCGEdgeHeader.from_bytes(reader)

        with reader.temp_offset(edge.node_a_triangles_offset):
            node_a_triangles = list(reader.unpack(f"{edge.node_a_triangles_count}i"))

        with reader.temp_offset(edge.node_b_triangles_offset):
            node_b_triangles = list(reader.unpack(f"{edge.node_b_triangles_count}i"))

        _reversed_map_id = edge.pop("_reversed_map_id")
        map_id = (_reversed_map_id[3], _reversed_map_id[2], _reversed_map_id[1], _reversed_map_id[0])

        return edge.to_object(
            cls,
            map_id=map_id,
            node_a_triangles=node_a_triangles,
            node_b_triangles=node_b_triangles,
        )

    def set_navmesh_reference(self, navmeshes: list[MSBNavmesh] | IDList[MSBNavmesh]):
        if self.navmesh_index is None:
            raise ValueError("Edge navmesh reference has already been set (ID consumed).")
        self.navmesh = navmeshes[self.navmesh_index]
        self.navmesh_index = None  # consumed

    def set_node_references(self, mcg_nodes: list[MCGNode]):
        self.node_a = mcg_nodes[self._node_a_index]
        self._node_a_index = None  # consumed
        self.node_b = mcg_nodes[self._node_b_index]
        self._node_b_index = None  # consumed

    def set_navmesh_index(self, navmeshes: list[MSBNavmesh] | IDList[MSBNavmesh]):
        self.navmesh_index = navmeshes.index(self.navmesh)
        self.navmesh = MISSING_REF

    def to_mcg_writer(
        self,
        writer: BinaryWriter,
        node_a_triangles_offset: int,
        node_b_triangles_offset: int,
        mcg_nodes: list[MCGNode],
    ):
        """The offsets passed in are written earlier in the file and are already known."""
        if self.navmesh_index is None:
            raise ValueError(
                "MCG `MCGEdge.navmesh` has not been indexed (e.g. with `MCG.set_indices(navmeshes)`."
            )
        if -1 in self.map_id:
            raise ValueError(f"Map ID of MCG `MCGEdge` has not been changed from invalid default: {self.map_id}")
        _reversed_map_id = list(reversed(self.map_id))
        self.MCGEdgeHeader(
            _node_a_index=mcg_nodes.index(self.node_a),
            node_a_triangles_count=len(self.node_a_triangles),
            node_a_triangles_offset=node_a_triangles_offset,
            _node_b_index=mcg_nodes.index(self.node_b),
            node_b_triangles_count=len(self.node_b_triangles),
            node_b_triangles_offset=node_b_triangles_offset,
            navmesh_index=self.navmesh_index,
            _reversed_map_id=_reversed_map_id,
            cost=self.cost,
        ).to_writer(writer)

    def pack_node_a_triangles(self, writer: BinaryWriter):
        """Happens before header write."""
        return writer.pack(f"{len(self.node_a_triangles)}i", *self.node_a_triangles)

    def pack_node_b_triangles(self, writer: BinaryWriter):
        """Happens before header write."""
        return writer.pack(f"{len(self.node_b_triangles)}i", *self.node_b_triangles)

    def is_connecting_nodes(self, first_node: MCGNode, second_node: MCGNode) -> bool:
        """Returns `True` if this edge connects the two given nodes in either direction, and `False` if not."""
        return (
            first_node is self.node_a and second_node is self.node_b
            or first_node is self.node_b and second_node is self.node_a
        )

    def __repr__(self) -> str:
        if self.navmesh is not MISSING_REF:
            return (
                f"MCGEdge(\n"
                f"    node_a={self.node_a},\n"
                f"    node_b={self.node_b},\n"
                f"    navmesh=<{self.navmesh.name if self.navmesh else 'None'}>,\n"
                f"    map_id={self.map_id},\n"
                f"    cost={self.cost},\n"
                f")"
            )
        return (
            f"MCGEdge(\n"
            f"    node_a={self.node_a},\n"
            f"    node_b={self.node_b},\n"
            f"    navmesh_index={self.navmesh_index},  # not dereferenced\n"
            f"    map_id={self.map_id},\n"
            f"    cost={self.cost},\n"
            f")"
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

    nodes: list[MCGNode] = field(default_factory=list)
    edges: list[MCGEdge] = field(default_factory=list)
    unknowns: tuple[int, int, int] = (0, 0, 0)  # DS1 default

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> MCG:
        header = cls.MCGHeaderStruct.from_bytes(reader)
        unknowns = (header.unk0, header.unk1, header.unk2)
        reader.seek(header.nodes_offset)
        nodes = [MCGNode.from_mcg_reader(reader) for _ in range(header.nodes_count)]
        reader.seek(header.edges_offset)
        edges = [MCGEdge.from_mcg_reader(reader) for _ in range(header.edges_count)]

        mcg = cls(nodes=nodes, edges=edges, unknowns=unknowns)
        mcg.set_node_edge_references()
        # NOTE:
        return mcg

    def set_navmesh_references(self, navmeshes: list[MSBNavmesh] | IDList[MSBNavmesh]):
        for node in self.nodes:
            node.set_dead_end_navmesh_reference(navmeshes)
        for edge in self.edges:
            edge.set_navmesh_reference(navmeshes)

    def set_node_edge_references(self):
        for node in self.nodes:
            node.set_connected_nodes_edges_references(self.nodes, self.edges)
        for edge in self.edges:
            edge.set_node_references(self.nodes)

    def set_navmesh_indices(self, navmeshes: list[MSBNavmesh] | IDList[MSBNavmesh]):
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

        edge_node_a_triangles_offsets = []
        edge_node_b_triangle_offsets = []
        for edge in self.edges:
            edge_node_a_triangles_offsets.append(writer.position)
            edge.pack_node_a_triangles(writer)
            edge_node_b_triangle_offsets.append(writer.position)
            edge.pack_node_b_triangles(writer)

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
                writer, edge_node_a_triangles_offsets[i], edge_node_b_triangle_offsets[i], self.nodes
            )

        writer.fill_with_position("nodes_offset", obj=self)
        for i, node in enumerate(self.nodes):
            node.to_mcg_writer(writer, connected_node_offsets[i], connected_edge_offsets[i])

        return writer

    def get_navmesh_triangles_by_node(self, allow_clashes=False) -> list[dict[str, None | tuple[int, list[int]]]]:
        """Get a list of `((navmesh_a_index, navmesh_a_triangles), (navmesh_b_index, navmesh_b_triangles))` tuples.

        Tuple elements may be `None` if only one or zero connected navmeshes are detected, which is obviously unusual.

        Can optionally permit (with a logged warning) cases where a node has different faces in edges in the same
        navmesh, which is not ideal but could be fixed later.

        Dead-end navmeshes stored on nodes imply that only one other navmesh has edges connected to that node, so we
        move it to being navmesh 'b' on the node.
        """
        all_node_navmesh_triangles = []
        for node in self.nodes:

            node_navmesh_dict = {"a": None, "b": None}

            for edge in node.connected_edges:
                navmesh_index = edge.navmesh_index
                if navmesh_index is None:
                    raise ValueError(
                        "`MCGEdge` navmesh has been deferenced. Cannot use `get_navmesh_triangles_by_node`."
                    )
                if edge.node_a is node:
                    triangles = edge.node_a_triangles
                elif edge.node_b is node:
                    triangles = edge.node_b_triangles
                else:
                    raise ValueError(f"Node {node} is not an endpoint node of apparently connected edge {edge}.")

                found = False
                for key in ("a", "b"):
                    if found:
                        break
                    if node_navmesh_dict[key] is None:
                        # First edge/navmesh.
                        node_navmesh_dict[key] = (navmesh_index, triangles)
                        found = True
                    else:
                        existing_navmesh_index, existing_triangles = node_navmesh_dict[key]
                        if existing_navmesh_index == navmesh_index:
                            # Check triangles are consistent.
                            if triangles != node_navmesh_dict[key][1]:
                                msg = (
                                     f"Node {node} has inconsistent navmesh triangle indices across edges through "
                                     f"navmesh index {navmesh_index}: {existing_triangles} vs. {triangles}"
                                )
                                if allow_clashes:
                                    _LOGGER.warning(f"{msg}. Using first indices: {existing_triangles}")
                                else:
                                    raise ValueError(msg)
                            found = True

            # Warn or raise errors about various connection problems.
            if node_navmesh_dict["a"] is None and node_navmesh_dict["b"] is None:
                _LOGGER.warning(f"Node {node} has no edges in any navmesh.")
            elif node.dead_end_navmesh_index != -1:
                if node_navmesh_dict["b"] is not None:
                    navmesh_a_index = node_navmesh_dict["a"][0]
                    navmesh_b_index = node_navmesh_dict["b"][0]
                    _LOGGER.warning(
                        f"Node {node} has edges in two navmesh indices ({navmesh_a_index}, {navmesh_b_index}) "
                        f"AND a dead-end navmesh index ({node.dead_end_navmesh_index}). Ignoring dead-end index."
                    )
                else:
                    # Use dead-end as navmesh B. Lack of triangle indices implies it's a dead end locally, and lack of
                    # edges in a second navmesh implies it globally.
                    node_navmesh_dict["b"] = (node.dead_end_navmesh_index, [])
            elif node_navmesh_dict["b"] is None and node.dead_end_navmesh_index == -1:
                _LOGGER.warning(f"Node {node} has edges in only one navmesh, but no dead-end navmesh.")

            all_node_navmesh_triangles.append(node_navmesh_dict)

        return all_node_navmesh_triangles

    def get_edges_in_navmesh(self, navmesh: MSBNavmesh) -> list[MCGEdge]:
        """Return a list of all `MCGEdge` instances attached to the given `MSBNavmesh`."""
        return [edge for edge in self.edges if edge.navmesh is navmesh]

    def disconnect_nodes(
        self,
        first_node: int | MCGNode,
        second_node: int | MCGNode,
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
            forward_match = edge.node_a == first_node and edge.node_b == second_node
            backward_match = edge.node_a == second_node and edge.node_b == first_node
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
        node_a: int | MCGNode,
        node_b: int | MCGNode,
        edge_navmesh: int | MSBNavmesh,
        node_a_triangles: list[int],
        node_b_triangles: list[int],
        cost: float = None,  # defaults to twice the distance between the nodes
        map_id=None,  # defaults to `map_id` of last edge in `MCG`
        ignore_connected=False,
    ):
        """Create a new `MCGEdge` that connects the given nodes, with the given navmesh and cost.

        Also updates the `connected_nodes` and `connected_edges` lists of the nodes accordingly. If `map_id` is None,
        copies from last edge (as all edges in an MCG will generally have the same map ID). If `cost` is None, it will
        default to twice the distance between the nodes (a very rough observed heuristic).

        Note that `node_a` must always be the node with the smaller MCG index. They will be reversed if necessary.

        If `ignore_connected=False`, an `ExistingConnectionError` is raised if the nodes are already connected.
        """
        if isinstance(node_a, int):
            node_a_index = node_a
            node_a = self.nodes[node_a]
        else:
            try:
                node_a_index = self.nodes.index(node_a)
            except ValueError:
                raise ValueError(f"Node {node_a} not found in MCG.")
        if isinstance(node_b, int):
            node_b_index = node_b
            node_b = self.nodes[node_b]
        else:
            try:
                node_b_index = self.nodes.index(node_b)
            except ValueError:
                raise ValueError(f"Node {node_b} not found in MCG.")

        if node_a_index == node_b_index:
            raise ValueError(f"Cannot connect node index {node_a_index} to itself: {node_a}")

        # Reverse nodes if necessary so node A is lowest index.
        if node_a_index > node_b_index:
            node_a, node_b = node_b, node_a
            node_a_triangles, node_b_triangles = node_b_triangles, node_a_triangles
            node_b_index, node_a_index = node_a_index, node_b_index

        # Check edge doesn't already exist.
        for i, edge in enumerate(self.edges):
            if edge.is_connecting_nodes(node_a, node_b):
                if ignore_connected:
                    return  # don't raise error, just return
                raise ValueError(f"Nodes {node_a} and {node_b} are already connected by edge with index {i}.")

        if map_id is None:
            if not self.edges:
                raise ValueError("Must specify `map_id` manually as no edges are currently in the MCG.")
            map_id = self.edges[-1].map_id

        if cost is None:
            # Default cost is twice edge length.
            cost = 2 * abs(node_a.translate - node_b.translate)

        new_edge = MCGEdge(
            node_a=node_a,
            node_b=node_b,
            navmesh=edge_navmesh,
            node_a_triangles=node_a_triangles,
            node_b_triangles=node_b_triangles,
            cost=cost,
            map_id=map_id,
        )

        node_a.connected_nodes.append(node_b)
        node_a.connected_edges.append(new_edge)

        node_b.connected_nodes.append(node_a)
        node_b.connected_edges.append(new_edge)

        _LOGGER.info(f"Created new edge between node indices {node_a_index} and {node_b_index}.")

    def delete_edge(self, edge: int | MCGEdge):
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
        selected_nodes: tp.Iterable[int | MCGNode] = None,
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
            color = "red" if node.dead_end_navmesh_index is None else "green"
            axes.scatter(node.translate.x, node.translate.z, node.translate.y, s=20, c=color, alpha=0.5)
            if node_labels is not None:
                axes.text(node.translate.x, node.translate.z, node.translate.y, node_labels[i], c=color)
        for edge in self.edges:
            x, y, z = zip(edge.node_a.translate, edge.node_b.translate)
            axes.plot3D(x, z, y, c="black", alpha=0.5)  # NOTE: y and z swapped
        if auto_show:
            plt.show()

    def __repr__(self) -> str:
        return f"MCG(nodes=<{len(self.nodes)} nodes>, edges=<{len(self.edges)} edges>)"
