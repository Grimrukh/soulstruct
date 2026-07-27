"""Tests for the DSR navmesh graph files: `.mcg` (node/edge graph) and `.mcp` (navmesh AABB partition).

These two files reference MSB navmesh parts *by index*, and reference each other's structures by index too,
so the critical invariants are:

    - MCP AABB count == MSB `navmeshes` count (1:1, index-matched).
    - MCG node/edge order must survive a dereference -> reindex -> pack cycle unchanged.
    - `node.connected_nodes` and `node.connected_edges` must stay the same length and in lockstep.
    - Every `edge.navmesh` must be an `MSBNavmesh` that is actually in the attached MSB.

Both formats are byte-stable in Soulstruct, so we assert byte-identity against the vanilla resources.
"""
from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from soulstruct.darksouls1r.maps import MSB
from soulstruct.darksouls1r.maps.navmesh import MCG, MCGNode, MCGEdge, MCP, NavmeshAABB, NavmeshGraph
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.misc import MISSING_REF

MAP_STEM = "m10_00_00_00"


def assert_bytes_equal(actual: bytes, expected: bytes, context: str = "") -> None:
    """Local copy of the `conftest` helper (`tests/darksouls1r/` is a package, so `conftest` is not importable)."""
    if actual == expected:
        return
    prefix = f"{context}: " if context else ""
    limit = min(len(actual), len(expected))
    for i in range(limit):
        if actual[i] != expected[i]:
            raise AssertionError(
                f"{prefix}byte mismatch at offset 0x{i:X} ({actual[i]:#04x} != {expected[i]:#04x}); "
                f"lengths {len(actual)} vs {len(expected)}."
            )
    raise AssertionError(f"{prefix}length differs ({len(actual)} != {len(expected)}), common prefix matches.")


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mcg_path(resource) -> Path:
    return resource(f"{MAP_STEM}.mcg")


@pytest.fixture
def mcp_path(resource) -> Path:
    return resource(f"{MAP_STEM}.mcp")


@pytest.fixture
def msb_path(resource) -> Path:
    return resource(f"{MAP_STEM}.msb")


@pytest.fixture
def map_dir(mcg_path, mcp_path, tmp_path) -> Path:
    """Writable copy of the map directory holding just the MCG and MCP, for `NavmeshGraph`."""
    map_dir = tmp_path / MAP_STEM
    map_dir.mkdir()
    shutil.copy(mcg_path, map_dir / mcg_path.name)
    shutil.copy(mcp_path, map_dir / mcp_path.name)
    return map_dir


@pytest.fixture
def msb(msb_path) -> MSB:
    return MSB.from_path(msb_path)


@pytest.fixture
def graph(map_dir, msb) -> NavmeshGraph:
    return NavmeshGraph(map_path=map_dir, msb=msb, map_stem=MAP_STEM)


# ---------------------------------------------------------------------------
# MCG: standalone read / write
# ---------------------------------------------------------------------------


def test_mcg_read(mcg_path):
    mcg = MCG.from_path(mcg_path)
    assert len(mcg.nodes) == 55
    assert len(mcg.edges) == 107
    assert mcg.unknowns == (0, 0, 0)
    assert "55 nodes" in repr(mcg) and "107 edges" in repr(mcg)


def test_mcg_repack_is_byte_identical(mcg_path):
    mcg = MCG.from_path(mcg_path)
    assert_bytes_equal(bytes(mcg), mcg_path.read_bytes(), "MCG repack")


def test_mcg_binary_roundtrip_preserves_graph(mcg_path, tmp_path):
    mcg = MCG.from_path(mcg_path)
    mcg.write(tmp_path / f"{MAP_STEM}.mcg")
    reload = MCG.from_path(tmp_path / f"{MAP_STEM}.mcg")

    assert len(reload.nodes) == len(mcg.nodes)
    assert len(reload.edges) == len(mcg.edges)
    for a, b in zip(mcg.nodes, reload.nodes):
        assert a.translate == b.translate
        assert a.unknown_offset == b.unknown_offset
        assert a.dead_end_navmesh_index == b.dead_end_navmesh_index
        # Connections must survive in the SAME ORDER (indices are positional).
        assert [mcg.nodes.index(n) for n in a.connected_nodes] == [reload.nodes.index(n) for n in b.connected_nodes]
        assert [mcg.edges.index(e) for e in a.connected_edges] == [reload.edges.index(e) for e in b.connected_edges]
    for a, b in zip(mcg.edges, reload.edges):
        assert a.node_a_triangles == b.node_a_triangles
        assert a.node_b_triangles == b.node_b_triangles
        assert a.map_id == b.map_id
        assert a.cost == pytest.approx(b.cost)
        assert a.navmesh_index == b.navmesh_index
        assert mcg.nodes.index(a.node_a) == reload.nodes.index(b.node_a)
        assert mcg.nodes.index(a.node_b) == reload.nodes.index(b.node_b)


def test_mcg_node_edge_lists_are_in_lockstep(mcg_path):
    """`validate_connections()` is the core MCG invariant: N connected nodes <-> N connected edges."""
    mcg = MCG.from_path(mcg_path)
    for node in mcg.nodes:
        node.validate_connections()  # raises `ValueError` if broken


def test_mcg_edge_endpoints_are_consistent_with_node_connections(mcg_path):
    """If node X lists edge E, then E must have X as one of its two endpoints (and vice versa)."""
    mcg = MCG.from_path(mcg_path)
    for node in mcg.nodes:
        for other_node, edge in zip(node.connected_nodes, node.connected_edges):
            assert edge.node_a is node or edge.node_b is node
            assert edge.is_connecting_nodes(node, other_node)
    for edge in mcg.edges:
        assert any(e is edge for e in edge.node_a.connected_edges)
        assert any(e is edge for e in edge.node_b.connected_edges)


def test_mcg_edge_map_ids_match_map_stem(mcg_path):
    mcg = MCG.from_path(mcg_path)
    for edge in mcg.edges:
        assert edge.map_id == (10, 0, 0, 0)


def test_mcg_navmesh_indices_are_in_range(mcg_path, msb):
    mcg = MCG.from_path(mcg_path)
    navmesh_count = len(msb.navmeshes)
    for edge in mcg.edges:
        assert 0 <= edge.navmesh_index < navmesh_count
    for node in mcg.nodes:
        assert -1 <= node.dead_end_navmesh_index < navmesh_count


# ---------------------------------------------------------------------------
# MCP
# ---------------------------------------------------------------------------


def test_mcp_read(mcp_path):
    mcp = MCP.from_path(mcp_path)
    assert len(mcp.aabbs) == 41
    assert mcp[0] is mcp.aabbs[0]
    assert list(mcp) == mcp.aabbs


def test_mcp_repack_is_byte_identical(mcp_path):
    mcp = MCP.from_path(mcp_path)
    assert_bytes_equal(bytes(mcp), mcp_path.read_bytes(), "MCP repack")


def test_mcp_binary_roundtrip_preserves_aabbs(mcp_path, tmp_path):
    mcp = MCP.from_path(mcp_path)
    mcp.write(tmp_path / f"{MAP_STEM}.mcp")
    reload = MCP.from_path(tmp_path / f"{MAP_STEM}.mcp")
    assert len(reload.aabbs) == len(mcp.aabbs)
    for a, b in zip(mcp.aabbs, reload.aabbs):
        assert a.map_id == b.map_id
        assert a.aabb_start == b.aabb_start
        assert a.aabb_end == b.aabb_end
        # Connection index ORDER must be preserved exactly.
        assert a.connected_navmesh_part_indices == b.connected_navmesh_part_indices


def test_mcp_aabb_connections_are_symmetric_and_in_range(mcp_path):
    mcp = MCP.from_path(mcp_path)
    count = len(mcp.aabbs)
    for i, aabb in enumerate(mcp.aabbs):
        assert i not in aabb.connected_navmesh_part_indices, "AABB must not connect to itself."
        for j in aabb.connected_navmesh_part_indices:
            assert 0 <= j < count
            assert i in mcp.aabbs[j].connected_navmesh_part_indices, (
                f"AABB {i} -> {j} connection is not mirrored back."
            )


def test_mcp_aabbs_are_well_formed(mcp_path):
    mcp = MCP.from_path(mcp_path)
    for i, aabb in enumerate(mcp.aabbs):
        for axis in range(3):
            assert aabb.aabb_start[axis] <= aabb.aabb_end[axis], f"AABB {i} is inverted on axis {axis}."
        assert len(aabb.get_vertices()) == 8
        assert len(aabb.get_faces()) == 6
        assert aabb.connected_navmesh_count == len(aabb.connected_navmesh_part_indices)


def test_mcp_aabb_translate_and_copy():
    aabb = NavmeshAABB(
        map_id=(10, 0, 0, 0),
        aabb_start=Vector3([-1.0, -2.0, -3.0]),
        aabb_end=Vector3([1.0, 2.0, 3.0]),
        connected_navmesh_part_indices=[1, 2],
    )
    clone = aabb.copy()
    clone.add_translate(Vector3([10.0, 0.0, 0.0]))
    assert clone.aabb_start.x == pytest.approx(9.0)
    assert clone.aabb_end.x == pytest.approx(11.0)
    assert aabb.aabb_start.x == pytest.approx(-1.0), "`copy()` must be a deep copy."
    assert clone.connected_navmesh_part_indices is not aabb.connected_navmesh_part_indices


def test_mcp_disconnect_aabbs():
    aabbs = [
        NavmeshAABB(map_id=(10, 0, 0, 0), connected_navmesh_part_indices=[1, 2]),
        NavmeshAABB(map_id=(10, 0, 0, 0), connected_navmesh_part_indices=[0, 2]),
        NavmeshAABB(map_id=(10, 0, 0, 0), connected_navmesh_part_indices=[0, 1]),
    ]
    mcp = MCP(aabbs=aabbs)
    mcp.disconnect_aabbs({0}, {1})
    assert mcp.aabbs[0].connected_navmesh_part_indices == [2]
    assert mcp.aabbs[1].connected_navmesh_part_indices == [2]
    assert mcp.aabbs[2].connected_navmesh_part_indices == [0, 1]

    with pytest.raises(ValueError):
        mcp.disconnect_aabbs({0, 1}, {1, 2})  # overlapping groups


# ---------------------------------------------------------------------------
# MSB <-> MCG/MCP correspondence
# ---------------------------------------------------------------------------


def test_aabb_count_matches_msb_navmesh_count(graph):
    graph.check_aabb_count()  # raises `ValueError` on mismatch
    assert len(graph.aabbs) == len(graph.navmeshes)


def test_check_aabb_count_detects_mismatch(graph):
    graph.mcp.aabbs.pop()
    with pytest.raises(ValueError, match="does not match the number of AABBs"):
        graph.check_aabb_count()


def test_graph_dereferences_navmesh_parts(graph):
    """After construction, MCG edges/nodes hold real `MSBNavmesh` instances, not indices."""
    for edge in graph.edges:
        assert edge.is_navmesh_deferenced
        assert edge.navmesh_index is None
        assert any(n is edge.navmesh for n in graph.navmeshes)
    for node in graph.nodes:
        assert node.is_navmesh_deferenced
        assert node.dead_end_navmesh is None or any(n is node.dead_end_navmesh for n in graph.navmeshes)


def test_get_navmesh_accepts_index_name_and_instance(graph):
    navmesh = graph.navmeshes[3]
    assert graph._get_navmesh(3) is navmesh
    assert graph._get_navmesh(navmesh.name) is navmesh
    assert graph._get_navmesh(navmesh) is navmesh
    with pytest.raises(TypeError):
        graph._get_navmesh(3.5)


def test_get_navmesh_aabb_is_index_matched(graph):
    for i, navmesh in enumerate(graph.navmeshes):
        assert graph.get_navmesh_aabb(navmesh) is graph.mcp.aabbs[i]
        assert graph.get_navmesh_aabb(navmesh.name) is graph.mcp.aabbs[i]


def test_every_navmesh_has_a_gate_node(graph):
    """A navmesh with no related node is broken in-game (it can never enter backread)."""
    orphans = [n.name for n in graph.navmeshes if not graph.get_navmesh_gate_nodes(n)]
    assert not orphans, f"Navmeshes with no MCG gate node: {orphans}"


def test_every_aabb_has_at_least_one_connection(graph):
    orphans = [i for i, aabb in enumerate(graph.aabbs) if not aabb.connected_navmesh_part_indices]
    assert not orphans, f"AABBs with no connections (never enter backread): {orphans}"


def test_mcg_edges_in_navmesh_lookup(graph):
    total = 0
    for navmesh in graph.navmeshes:
        edges = graph.mcg.get_edges_in_navmesh(navmesh)
        for edge in edges:
            assert edge.navmesh is navmesh
        total += len(edges)
    assert total == len(graph.edges), "Every edge must belong to exactly one navmesh."


# ---------------------------------------------------------------------------
# The critical round-trip: dereference -> reindex -> pack -> reload
# ---------------------------------------------------------------------------


def test_navmesh_graph_write_roundtrip_is_byte_identical(graph, mcg_path, mcp_path, tmp_path):
    """`NavmeshGraph.write()` reindexes MCG navmesh references. Nothing may be reordered or dropped."""
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    graph.write(out_dir)
    assert_bytes_equal((out_dir / f"{MAP_STEM}.mcg").read_bytes(), mcg_path.read_bytes(), "MCG via NavmeshGraph")
    assert_bytes_equal((out_dir / f"{MAP_STEM}.mcp").read_bytes(), mcp_path.read_bytes(), "MCP via NavmeshGraph")


def test_navmesh_graph_write_restores_references(graph, tmp_path):
    """After `write()`, the graph must still be usable (references restored, not left as indices)."""
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    graph.write(out_dir)
    for edge in graph.edges:
        assert edge.is_navmesh_deferenced
        assert any(n is edge.navmesh for n in graph.navmeshes)
    # Writing a second time must produce the same bytes (idempotent).
    out_dir_2 = tmp_path / "out2"
    out_dir_2.mkdir()
    graph.write(out_dir_2)
    assert_bytes_equal(
        (out_dir_2 / f"{MAP_STEM}.mcg").read_bytes(),
        (out_dir / f"{MAP_STEM}.mcg").read_bytes(),
        "second NavmeshGraph write",
    )


def test_set_navmesh_indices_then_references_is_lossless(mcg_path, msb):
    """MCG index <-> reference conversion must be exactly reversible."""
    mcg = MCG.from_path(mcg_path)
    original_edge_indices = [edge.navmesh_index for edge in mcg.edges]
    original_node_indices = [node.dead_end_navmesh_index for node in mcg.nodes]

    mcg.set_navmesh_references(msb.navmeshes)
    assert all(edge.navmesh_index is None for edge in mcg.edges)
    mcg.set_navmesh_indices(msb.navmeshes)

    assert [edge.navmesh_index for edge in mcg.edges] == original_edge_indices
    assert [node.dead_end_navmesh_index for node in mcg.nodes] == original_node_indices
    assert all(edge.navmesh is MISSING_REF for edge in mcg.edges)


def test_double_dereference_raises(mcg_path, msb):
    mcg = MCG.from_path(mcg_path)
    mcg.set_navmesh_references(msb.navmeshes)
    with pytest.raises(ValueError):
        mcg.set_navmesh_references(msb.navmeshes)


def test_writing_dereferenced_mcg_raises(mcg_path, msb):
    """Packing an MCG whose navmesh references have not been re-indexed must fail loudly, not silently."""
    mcg = MCG.from_path(mcg_path)
    mcg.set_navmesh_references(msb.navmeshes)
    with pytest.raises(ValueError):
        bytes(mcg)


# ---------------------------------------------------------------------------
# Graph editing
# ---------------------------------------------------------------------------


def test_disconnect_nodes_removes_edge_everywhere(graph, tmp_path):
    edge = graph.edges[0]
    node_a, node_b = edge.node_a, edge.node_b
    edge_count = len(graph.edges)

    graph.mcg.disconnect_nodes(node_a, node_b, ignore_unconnected=False)

    assert len(graph.edges) == edge_count - 1
    assert not any(e is edge for e in graph.edges)
    for node in graph.nodes:
        assert not any(e is edge for e in node.connected_edges)
        node.validate_connections()

    # Resulting MCG must still pack and reload with the expected counts.
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    graph.write(out_dir)
    reload = MCG.from_path(out_dir / f"{MAP_STEM}.mcg")
    assert len(reload.edges) == edge_count - 1
    assert len(reload.nodes) == len(graph.nodes)


def test_disconnect_unconnected_nodes(graph):
    # Find two nodes that are definitely not directly connected.
    node_a = graph.nodes[0]
    node_b = next(
        n for n in graph.nodes
        if n is not node_a and not any(cn is n for cn in node_a.connected_nodes)
    )
    graph.mcg.disconnect_nodes(node_a, node_b)  # silently ignored by default
    with pytest.raises(ValueError, match="No edges found"):
        graph.mcg.disconnect_nodes(node_a, node_b, ignore_unconnected=False)


def test_delete_edge_by_index(graph):
    edge = graph.edges[5]
    graph.mcg.delete_edge(5)
    assert not any(e is edge for e in graph.edges)
    for node in graph.nodes:
        node.validate_connections()


def test_remove_node_removes_its_edges(graph):
    node = graph.nodes[0]
    node_edges = [e for e in graph.edges if e.node_a is node or e.node_b is node]
    assert node_edges
    node_count, edge_count = len(graph.nodes), len(graph.edges)

    graph.remove_node(node)

    assert len(graph.nodes) == node_count - 1
    assert len(graph.edges) == edge_count - len(node_edges)
    assert not any(n is node for n in graph.nodes)
    for other in graph.nodes:
        assert not any(n is node for n in other.connected_nodes)
        other.validate_connections()


def test_new_node_is_appended(graph):
    node_count = len(graph.nodes)
    node = graph.new_node(Vector3([1.0, 2.0, 3.0]))
    assert graph.nodes[-1] is node
    assert len(graph.nodes) == node_count + 1
    assert node.connected_nodes == [] and node.connected_edges == []


def test_connect_and_disconnect_navmesh_aabbs(graph):
    from soulstruct.base.maps.navmesh.utilities import ExistingConnectionError, MissingConnectionError

    first, second = graph.navmeshes[0], graph.navmeshes[1]
    i, j = 0, 1
    # Force a known disconnected state.
    graph.disconnect_navmesh_aabbs(first, second, ignore_unconnected=True)
    assert j not in graph.aabbs[i].connected_navmesh_part_indices
    assert i not in graph.aabbs[j].connected_navmesh_part_indices

    graph.connect_navmesh_aabbs(first, second)
    assert j in graph.aabbs[i].connected_navmesh_part_indices
    assert i in graph.aabbs[j].connected_navmesh_part_indices

    with pytest.raises(ExistingConnectionError):
        graph.connect_navmesh_aabbs(first, second)
    graph.connect_navmesh_aabbs(first, second, ignore_connected=True)  # no error

    graph.disconnect_navmesh_aabbs(first, second)
    with pytest.raises(MissingConnectionError):
        graph.disconnect_navmesh_aabbs(first, second)


def test_node_add_connection_rejects_duplicates():
    from soulstruct.base.maps.navmesh.utilities import ExistingConnectionError

    node_a, node_b = MCGNode(), MCGNode()
    edge = MCGEdge(node_a=node_a, node_b=node_b)
    node_a.add_connection(node_b, edge)
    node_a.validate_connections()
    with pytest.raises(ExistingConnectionError):
        node_a.add_connection(node_b, edge)


def test_node_validate_connections_detects_desync():
    node = MCGNode()
    node.connected_nodes.append(MCGNode())
    with pytest.raises(ValueError, match="does not match number of connected edges"):
        node.validate_connections()


# ---------------------------------------------------------------------------
# Known bugs
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    reason="BUG: `MCG.connect_nodes()` never appends the new `MCGEdge` to `self.edges`, so the graph is "
           "left inconsistent and cannot be packed (base/maps/navmesh/mcg.py:619-635).",
    strict=False,
)
def test_connect_nodes_adds_edge_to_mcg(graph, tmp_path):
    edge_count = len(graph.edges)
    node_a, node_b = graph.nodes[0], graph.nodes[5]
    graph.connect_nodes(node_a, node_b, graph.navmeshes[0], [1], [2], cost=1.0)

    assert len(graph.edges) == edge_count + 1, "New edge was not added to `MCG.edges`."
    new_edge = graph.edges[-1]
    assert any(e is new_edge for e in node_a.connected_edges)
    assert any(e is new_edge for e in node_b.connected_edges)

    out_dir = tmp_path / "out"
    out_dir.mkdir()
    graph.write(out_dir)  # would raise `ValueError: list.index(x): x not in list`
    reload = MCG.from_path(out_dir / f"{MAP_STEM}.mcg")
    assert len(reload.edges) == edge_count + 1


def test_navmesh_graph_write_accepts_str_path(graph, tmp_path):
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    graph.write(str(out_dir))
    assert (out_dir / f"{MAP_STEM}.mcg").is_file()


@pytest.mark.xfail(
    reason="BUG: `MCP.from_msb_mcg_nvm_paths()` calls `mcp_path.stem` before converting `mcp_path` to a "
           "`Path`, so the documented `str` argument raises AttributeError "
           "(base/maps/navmesh/mcp.py:267).",
    strict=False,
)
def test_mcp_from_paths_accepts_str_mcp_path(map_dir, msb_path):
    MCP.from_msb_mcg_nvm_paths(
        msb_class=MSB,
        mcp_path=str(map_dir / f"{MAP_STEM}.mcp"),
        msb_path=msb_path,
        mcg_path=map_dir / f"{MAP_STEM}.mcg",
        nvmbnd_path=map_dir / f"{MAP_STEM}.nvmbnd.dcx",  # missing; `stem` error should come first
    )


# ---------------------------------------------------------------------------
# Whole-game sweep (slow, requires DSR install)
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.game_data
def test_all_dsr_map_navmesh_graphs(dsr_root, tmp_path):
    """Read every vanilla DSR MCG/MCP, check MSB correspondence, and confirm byte-stable repacking."""
    map_root = dsr_root / "map"
    msb_root = map_root / "MapStudio"
    checked = 0
    for mcg_file in sorted(map_root.glob("m*/m*.mcg")):
        map_stem = mcg_file.stem
        if map_stem.startswith("m99"):
            continue  # DSR test maps; their MSBs use non-vanilla `MSBCollision` values Soulstruct rejects
        msb_file = msb_root / f"{map_stem}.msb"
        mcp_file = mcg_file.with_suffix(".mcp")
        if not msb_file.is_file() or not mcp_file.is_file():
            continue

        map_msb = MSB.from_path(msb_file)
        map_graph = NavmeshGraph(map_path=mcg_file.parent, msb=map_msb, map_stem=map_stem)
        map_graph.check_aabb_count()

        for node in map_graph.nodes:
            node.validate_connections()
        for edge in map_graph.edges:
            assert any(n is edge.navmesh for n in map_msb.navmeshes)

        out_dir = tmp_path / map_stem
        out_dir.mkdir(exist_ok=True)
        map_graph.write(out_dir)
        assert_bytes_equal((out_dir / f"{map_stem}.mcg").read_bytes(), mcg_file.read_bytes(), f"{map_stem} MCG")
        assert_bytes_equal((out_dir / f"{map_stem}.mcp").read_bytes(), mcp_file.read_bytes(), f"{map_stem} MCP")
        checked += 1

    assert checked >= 10, f"Expected to check at least 10 DSR maps, only found {checked}."
