import struct

import pytest

from soulstruct.bloodborne.maps import NVA
from soulstruct.dcx import DCXType, compress


def make_nva() -> bytes:
    # Two placement records followed by a section this reader does not interpret.
    data = bytearray(32 + 2 * 144 + 16)
    struct.pack_into("<4s7I", data, 0, b"NVMA", 4, len(data), 0, 0, 3, 288, 2)
    struct.pack_into("<3f", data, 32, 1.0, 2.0, 3.0)
    struct.pack_into("<3f", data, 48, 0.0, 0.5, -1.0)
    struct.pack_into("<3f", data, 64, -1.0, 1.0, 1.0)
    struct.pack_into("<2i", data, 80, 240100007, 7)
    struct.pack_into("<2i", data, 96, 10, 2)
    struct.pack_into("<h", data, 106, 3)
    struct.pack_into("<2i", data, 224, -1, -1)
    return bytes(data)


@pytest.mark.parametrize("dcx", [False, True])
def test_read_placements(tmp_path, dcx):
    raw = make_nva()
    path = tmp_path / ("map.nva.dcx" if dcx else "map.nva")
    path.write_bytes(compress(raw, DCXType.BB_DS3) if dcx else raw)

    entry, placeholder = NVA.from_path(path).navmesh_placements
    assert entry.translate == (1.0, 2.0, 3.0)
    assert entry.rotate == (0.0, 0.5, -1.0)
    assert entry.scale == (-1.0, 1.0, 1.0)
    assert (entry.name_id, entry.model_id) == (240100007, 7)
    assert (entry.vertex_count, entry.reference_count, entry.node_count) == (10, 2, 3)
    assert not entry.is_placeholder
    assert placeholder.is_placeholder


@pytest.mark.parametrize("offset,value", [(4, 5), (8, 1000), (24, 144), (28, 3)])
def test_reject_invalid_header(offset, value):
    data = bytearray(make_nva())
    struct.pack_into("<I", data, offset, value)
    with pytest.raises(ValueError, match="NVA"):
        NVA.from_bytes(bytes(data))


def test_reject_truncated_header():
    with pytest.raises(ValueError, match="Truncated NVA header"):
        NVA.from_bytes(b"NVMA")
