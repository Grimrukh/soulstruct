"""Tests for `soulstruct.dcx` -- DCX/DCP compression wrappers.

Most of these are pure unit tests (no game data required): we compress in-memory data with every
supported `DCXType` and assert that `decompress()` recovers it exactly *and* re-detects the same type.
"""
from __future__ import annotations

import zlib
from pathlib import Path

import pytest

from soulstruct.dcx import DCXType, compress, decompress, is_dcx
from soulstruct.dcx.core import (
    DCX_VERSION_INFO,
    DCXError,
    DCXHeaderStruct,
    DCXVersionInfo,
)
from soulstruct.dcx import oodle
from soulstruct.utilities.binary import BinaryReader, ByteOrder


# Deterministic, moderately compressible payload that spans multiple 0x10000 EDGE chunks.
SAMPLE = (b"SOULSTRUCT_DCX_TEST_PAYLOAD_" * 8000)[:200_000]
SMALL = b"a tiny payload that fits in one chunk"


def _oodle_available() -> bool:
    try:
        oodle.compress(b"x" * 64)
    except Exception:
        return False
    return True


OODLE_AVAILABLE = _oodle_available()


# DCX types that are expected to fully round-trip through `compress()` -> `decompress()`.
WORKING_DCX_TYPES = [
    DCXType.DCX_EDGE,
    DCXType.DCX_DFLT_10000_24_9,
    DCXType.DCX_DFLT_10000_44_9,
    DCXType.DCX_DFLT_11000_44_8,
    DCXType.DCX_DFLT_11000_44_9,
    DCXType.DCX_DFLT_11000_44_9_15,
]


# region Round-trips


@pytest.mark.parametrize("dcx_type", WORKING_DCX_TYPES, ids=lambda t: t.name)
def test_compress_decompress_roundtrip_large(dcx_type: DCXType):
    """Core contract: `decompress(compress(data, t)) == (data, t)`."""
    packed = compress(SAMPLE, dcx_type)
    assert is_dcx(BinaryReader(packed))
    unpacked, detected_type = decompress(packed)
    assert bytes(unpacked) == SAMPLE
    assert detected_type == dcx_type


@pytest.mark.parametrize(
    "dcx_type",
    [
        pytest.param(
            DCXType.DCX_EDGE,
            marks=pytest.mark.xfail(
                reason="BUG: `_compress_dcx_edge()` always deflates each chunk but sets the chunk's "
                       "`is_compressed` flag to `chunk_compressed_size < decompressed_chunk_size`. When "
                       "deflate does not shrink the chunk (small or incompressible data) the flag is 0 and "
                       "the raw deflate stream is handed back to the caller verbatim -> data corruption.",
                strict=False,
            ),
        ),
        *WORKING_DCX_TYPES[1:],
    ],
    ids=lambda t: t.name,
)
def test_compress_decompress_roundtrip_small(dcx_type: DCXType):
    packed = compress(SMALL, dcx_type)
    assert is_dcx(BinaryReader(packed))
    unpacked, detected_type = decompress(packed)
    assert bytes(unpacked) == SMALL
    assert detected_type == dcx_type


@pytest.mark.xfail(
    reason="BUG: see `test_compress_decompress_roundtrip_small` -- incompressible DCX_EDGE chunks are "
           "written deflated but flagged as uncompressed.",
    strict=False,
)
def test_edge_incompressible_data_roundtrip():
    """Deliberately incompressible payload, which trips the `is_compressed` flag bug in every chunk."""
    import os

    payload = os.urandom(0x30000)
    unpacked, _ = decompress(compress(payload, DCXType.DCX_EDGE))
    assert bytes(unpacked) == payload


def test_decompress_always_returns_bytes():
    for dcx_type in WORKING_DCX_TYPES:
        data, _ = decompress(compress(SAMPLE, dcx_type))
        assert isinstance(data, bytes), f"{dcx_type.name} returned {type(data).__name__}"


@pytest.mark.skipif(not OODLE_AVAILABLE, reason="`oo2core_6_win64.dll` not loadable on this machine.")
@pytest.mark.parametrize("payload", [SMALL, SAMPLE], ids=["small", "large"])
def test_krak_roundtrip(payload: bytes):
    """Oodle/Kraken compression (Sekiro, Elden Ring)."""
    packed = compress(payload, DCXType.DCX_KRAK)
    unpacked, detected_type = decompress(packed)
    assert unpacked == payload
    assert detected_type == DCXType.DCX_KRAK


@pytest.mark.xfail(
    reason="BUG: `_compress_dcx_zstd()` passes both `compression_params` and `write_content_size` to "
           "`zstd.ZstdCompressor`, which raises ValueError. DCX_ZSTD (new ER regulation) cannot be written.",
    strict=False,
)
def test_zstd_roundtrip():
    packed = compress(SAMPLE, DCXType.DCX_ZSTD)
    unpacked, detected_type = decompress(packed)
    assert unpacked == SAMPLE
    assert detected_type == DCXType.DCX_ZSTD


def test_dcp_dflt_roundtrip():
    packed = compress(SMALL, DCXType.DCP_DFLT)
    print(packed[:16].hex(sep=' '))
    unpacked, detected_type = decompress(packed)
    assert unpacked == SMALL
    assert detected_type == DCXType.DCP_DFLT


@pytest.mark.xfail(
    reason="BUG: `DCXType.DCP_EDGE` has no entry in `DCX_VERSION_INFO`, so `compress()` raises `KeyError`. "
           "The enum member is effectively unsupported.",
    strict=False,
)
def test_dcp_edge_compress_supported():
    compress(SMALL, DCXType.DCP_EDGE)


def test_edge_chunking_is_exercised():
    """`SAMPLE` is >0x10000 bytes so DCX_EDGE must produce multiple chunks."""
    assert len(SAMPLE) > 0x10000
    packed = compress(SAMPLE, DCXType.DCX_EDGE)
    reader = BinaryReader(packed, byte_order=ByteOrder.BigEndian)
    header = DCXHeaderStruct.from_bytes(reader)
    chunk_count = (header.version3 - 0x50) // 0x10
    assert chunk_count == (len(SAMPLE) // 0x10000) + 1


# endregion


# region Detection


def test_is_dcx_false_for_plain_data():
    assert not is_dcx(BinaryReader(b"BND4" + b"\0" * 60))


def test_detect_unknown_for_plain_data():
    assert DCXType.detect(BinaryReader(b"BND4" + b"\0" * 60)) == DCXType.Unknown


def test_detect_zlib_stream():
    """Bare zlib streams (not really DCX) are detected as `DCXType.Zlib`."""
    data = zlib.compress(b"hello world" * 100, level=9)
    assert data[0] == 0x78
    assert DCXType.detect(BinaryReader(data)) == DCXType.Zlib


def test_detect_resets_reader_offset():
    packed = compress(SMALL, DCXType.DCX_DFLT_10000_24_9)
    reader = BinaryReader(packed, byte_order=ByteOrder.BigEndian)
    reader.seek(4)
    DCXType.detect(reader)
    assert reader.position == 4


def test_decompress_unknown_raises():
    with pytest.raises(DCXError):
        decompress(b"NOTDCX" + b"\0" * 100)


def test_decompress_accepts_path(tmp_path: Path):
    packed = compress(SMALL, DCXType.DCX_DFLT_10000_44_9)
    p = tmp_path / "sample.dcx"
    p.write_bytes(packed)
    assert decompress(p) == (SMALL, DCXType.DCX_DFLT_10000_44_9)
    assert decompress(str(p)) == (SMALL, DCXType.DCX_DFLT_10000_44_9)
    assert decompress(bytearray(packed)) == (SMALL, DCXType.DCX_DFLT_10000_44_9)


# endregion


# region DCXVersionInfo / DCXType helpers


def test_version_info_table_is_unambiguous():
    """No two known DCX types may have equal version info, or detection would be order-dependent."""
    known = {t: v for t, v in DCX_VERSION_INFO.items() if v is not None}
    for type_a, info_a in known.items():
        for type_b, info_b in known.items():
            if type_a is type_b:
                continue
            assert info_a != info_b, f"{type_a.name} and {type_b.name} have indistinguishable version info."


def test_version_info_none_fields_are_wildcards():
    a = DCXVersionInfo(b"DFLT", 0x10000, 0x24, None, 9, 0, 0, 0x010100)
    b = DCXVersionInfo(b"DFLT", 0x10000, 0x24, 0x2C, 9, 0, 0, 0x010100)
    assert a == b
    c = DCXVersionInfo(b"KRAK", 0x10000, 0x24, 0x2C, 9, 0, 0, 0x010100)
    assert a != c


def test_all_dcx_types_have_version_info_or_are_special():
    """Every `DCXType` that `compress()` may be asked to build a DCX header for needs version info."""
    special = {DCXType.Unknown, DCXType.Null, DCXType.Zlib, DCXType.DCP_DFLT, DCXType.DCP_EDGE}
    for dcx_type in DCXType:
        if dcx_type in special:
            continue
        assert DCX_VERSION_INFO.get(dcx_type) is not None, f"{dcx_type.name} missing from `DCX_VERSION_INFO`."


def test_has_dcx_extension():
    assert not DCXType.Null.has_dcx_extension()
    assert not DCXType.Zlib.has_dcx_extension()
    assert DCXType.DCX_DFLT_10000_24_9.has_dcx_extension()
    assert DCXType.DCX_KRAK.has_dcx_extension()


def test_process_path_adds_extension():
    assert DCXType.DCX_KRAK.process_path(Path("a/b.flver")).name == "b.flver.dcx"
    assert DCXType.Null.process_path(Path("a/b.flver.dcx")).name == "b.flver"
    assert DCXType.Null.process_path("a/b.flver.dcx").endswith("b.flver")


def test_process_path_is_idempotent():
    once = DCXType.DCX_KRAK.process_path(Path("a/b.flver"))
    twice = DCXType.DCX_KRAK.process_path(once)
    assert once == twice


def test_process_path_rejects_bad_type():
    with pytest.raises(NotImplementedError):
        DCXType.DCX_KRAK.process_path(123)


def test_from_member_name():
    assert DCXType.from_member_name("DCX_KRAK") is DCXType.DCX_KRAK
    assert DCXType.from_member_name("Null") is DCXType.Null


def test_game_default_aliases():
    """Alias members must be the same objects as their canonical members."""
    assert DCXType.DS1_DS2 is DCXType.DCX_DFLT_10000_24_9
    assert DCXType.BB_DS3 is DCXType.DCX_DFLT_10000_44_9
    assert DCXType.SEKIRO is DCXType.DCX_DFLT_11000_44_9
    assert DCXType.ER is DCXType.DCX_KRAK
    assert DCXType.ER_REGULATION is DCXType.DCX_ZSTD
    assert DCXType.DES is DCXType.DCX_EDGE


# endregion


# region Real game files


def test_decompress_real_dsr_parambnd(tests_dir: Path):
    """DSR files use `DCX_DFLT_10000_24_9`; recompression must be self-consistent."""
    path = tests_dir / "darksouls1r" / "resources" / "GameParam.parambnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    data, dcx_type = decompress(path.read_bytes())
    assert dcx_type == DCXType.DCX_DFLT_10000_24_9
    assert data[:4] == b"BND3"
    repacked = compress(data, dcx_type)
    assert decompress(repacked) == (data, dcx_type)


def test_decompress_real_bloodborne_parambnd(tests_dir: Path):
    """Bloodborne files use `DCX_DFLT_10000_44_9`."""
    path = tests_dir / "bloodborne" / "resources" / "gameparam.parambnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing test resource: {path}")
    data, dcx_type = decompress(path.read_bytes())
    assert dcx_type == DCXType.DCX_DFLT_10000_44_9
    assert data[:4] == b"BND4"


@pytest.mark.skipif(not OODLE_AVAILABLE, reason="`oo2core_6_win64.dll` not loadable on this machine.")
def test_decompress_real_elden_ring_krak(er_root: Path):
    """Elden Ring uses Oodle/Kraken for almost everything."""
    path = er_root / "msg" / "engus" / "ngword.msgbnd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing Elden Ring file: {path}")
    data, dcx_type = decompress(path.read_bytes())
    assert dcx_type == DCXType.DCX_KRAK
    assert data[:4] == b"BND4"
    # Round-trip through our own compressor.
    assert decompress(compress(data, DCXType.DCX_KRAK)) == (data, DCXType.DCX_KRAK)


# endregion
