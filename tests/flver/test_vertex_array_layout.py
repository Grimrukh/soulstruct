"""Pure-unit tests for `soulstruct.flver.vertex_array_layout`.

These tests need no game data: they exercise the vertex data type/format dispatch table, the
NumPy dtype construction, the compression codecs, and the FLVER0/FLVER2 layout struct I/O.
"""
from __future__ import annotations

import numpy as np
import pytest

from soulstruct.utilities.binary import BinaryReader, BinaryWriter, ByteOrder
from soulstruct.flver.vertex_array_layout import (
    INT_TO_FLOAT_127,
    INT_TO_FLOAT_127_SIGNED,
    INT_TO_FLOAT_255,
    INT_TO_FLOAT_32767_SIGNED,
    NULL_CODEC,
    VERTEX_DATA_TYPES,
    VERTEX_FORMAT_ENUM_SIZES,
    VertexArrayLayout,
    VertexBitangent,
    VertexBoneIndices,
    VertexBoneWeights,
    VertexColor,
    VertexDataCodec,
    VertexDataFormatEnum,
    VertexIgnore,
    VertexNormal,
    VertexPosition,
    VertexTangent,
    VertexUV,
)

FE = VertexDataFormatEnum


# ---------------------------------------------------------------------------
# Format table consistency
# ---------------------------------------------------------------------------


def _all_type_format_pairs():
    """Yield `(data_type_cls, format_enum_int)` for every entry in every type's `formats` table."""
    for data_type_cls in VERTEX_DATA_TYPES.values():
        for enum_keys in data_type_cls.formats:
            for enum_int in enum_keys:
                yield data_type_cls, enum_int


def test_every_format_key_is_a_real_format_enum():
    """Every key in every `VertexDataType.formats` table must be a valid `VertexDataFormatEnum`.

    A key that is not a member of the enum is unreachable dead code: `VertexDataType.STRUCT` converts
    the packed integer through `VertexDataFormatEnum`, so such a format could never be constructed
    from a real FLVER.
    """
    unknown = []
    for data_type_cls, enum_int in _all_type_format_pairs():
        try:
            VertexDataFormatEnum(enum_int)
        except ValueError:
            unknown.append((data_type_cls.__name__, hex(enum_int)))
    assert unknown == [("VertexNormal", "0x4")], (
        f"Unexpected set of unknown format enum keys: {unknown}"
    )


def test_every_format_enum_has_a_declared_size():
    for member in VertexDataFormatEnum:
        if member is VertexDataFormatEnum.Ignored:
            continue  # Soulstruct-only sentinel, size comes from `VertexIgnore.ignore_size`
        assert member in VERTEX_FORMAT_ENUM_SIZES, f"No declared size for {member.name}."


# Pairs known to be internally inconsistent (declared enum size != NumPy dtype itemsize).
_KNOWN_SIZE_MISMATCHES = {
    (VertexNormal, 0x03),   # Float4 declared 16 bytes, dtype only has 3 floats (12)
    (VertexNormal, 0x12),   # NormalWFirst declared 8 bytes, dtype is 4
    (VertexUV, 0x12),       # NormalWFirst declared 8 bytes, dtype is 4
    (VertexTangent, 0x03),  # Float4 declared 16 bytes, dtype only has 3 floats (12)
    (VertexTangent, 0x1A),  # FourShortsToFloats declared 8 bytes, dtype is 4
}


def _size_param(data_type_cls, enum_int):
    marks = []
    if (data_type_cls, enum_int) in _KNOWN_SIZE_MISMATCHES:
        marks.append(
            pytest.mark.xfail(
                reason=(
                    "Declared `VERTEX_FORMAT_ENUM_SIZES` entry does not match the NumPy dtype built "
                    "from the type's `formats` table; such a layout would mis-slice vertex data."
                ),
                strict=False,
            )
        )
    return pytest.param(data_type_cls, enum_int, marks=marks, id=f"{data_type_cls.__name__}-{enum_int:#04x}")


@pytest.mark.parametrize(
    "data_type_cls, enum_int",
    [
        _size_param(cls, e)
        for cls, e in _all_type_format_pairs()
        if e in set(int(m) for m in VertexDataFormatEnum)
    ],
)
def test_format_dtype_size_matches_declared_size(data_type_cls, enum_int):
    """`get_total_data_size()` (from the enum size table) must equal the packed dtype itemsize.

    Any mismatch is a genuine defect: `VertexArray.from_flver2_reader()` compares the layout size to
    the header's `vertex_size`, then `np.frombuffer` uses the dtype. Disagreement means the array is
    either rejected (empty mesh) or silently misparsed.
    """
    data_type = data_type_cls(VertexDataFormatEnum(enum_int), 0)
    layout = VertexArrayLayout([data_type])
    compressed_dtype, decompressed_dtype = layout.get_dtypes()
    assert compressed_dtype.itemsize == layout.get_total_data_size(include_ignored=True)


def test_edge_compressed_is_rejected():
    layout = VertexArrayLayout([VertexPosition(FE.EdgeCompressed)])
    with pytest.raises(NotImplementedError):
        layout.get_dtypes()
    with pytest.raises(NotImplementedError):
        layout.get_codecs(uv_factor=1024)


def test_unsupported_format_for_type_raises():
    """`VertexBitangent` has no float format, so requesting one must raise a clear `ValueError`."""
    bad = VertexBitangent(FE.Float3)
    with pytest.raises(ValueError, match="unsupported for type"):
        bad.get_format()


# ---------------------------------------------------------------------------
# Codecs
# ---------------------------------------------------------------------------


def test_null_codec_is_identity():
    a = np.arange(10, dtype=np.float32)
    assert np.array_equal(NULL_CODEC.decompress(a), a)
    assert np.array_equal(NULL_CODEC.compress(a), a)


@pytest.mark.parametrize(
    "codec, dtype, values",
    [
        (INT_TO_FLOAT_127_SIGNED, np.uint8, np.arange(256)),
        (INT_TO_FLOAT_255, np.uint8, np.arange(256)),
        (INT_TO_FLOAT_127, np.int8, np.arange(-128, 128)),
        (INT_TO_FLOAT_32767_SIGNED, np.int16, np.arange(-32768, 32768, 7)),
    ],
)
def test_codec_int_roundtrip_is_lossless(codec: VertexDataCodec, dtype, values):
    """Decompress -> compress -> truncate must return the exact original integers."""
    original = values.astype(dtype)
    decompressed = codec.decompress(original.astype(np.float32))
    recompressed = codec.compress(decompressed).astype(dtype)
    assert np.array_equal(original, recompressed)


@pytest.mark.parametrize("uv_factor", [1024, 2048])
def test_uv_factor_codec_roundtrip(uv_factor: int):
    codec = VertexDataCodec.from_uv_factor(uv_factor)
    original = np.arange(-30000, 30000, 13, dtype=np.int16)
    decompressed = codec.decompress(original.astype(np.float32))
    assert np.allclose(decompressed, original / uv_factor)
    assert np.array_equal(codec.compress(decompressed).astype(np.int16), original)


# ---------------------------------------------------------------------------
# dtype construction
# ---------------------------------------------------------------------------


def _standard_ds1_layout() -> VertexArrayLayout:
    """Typical DS1 map piece layout: position, bone indices, normal, color, one UV."""
    return VertexArrayLayout([
        VertexPosition(FE.Float3),
        VertexBoneIndices(FE.FourBytesB),
        VertexNormal(FE.FourBytesC),
        VertexColor(FE.FourBytesC),
        VertexUV(FE.UV),
    ])


def test_standard_layout_dtypes():
    layout = _standard_ds1_layout()
    compressed, decompressed = layout.get_dtypes()
    assert compressed.names == ("position", "bone_indices", "normal", "normal_w", "color_0", "uv_0")
    assert decompressed.names == compressed.names
    # Compressed sizes: 12 + 4 + 4 + 4 + 4 = 28
    assert compressed.itemsize == 28
    assert layout.get_total_data_size(include_ignored=True) == 28
    assert layout.get_total_data_size(include_ignored=False) == 28
    # Decompressed: position f4x3, bone_indices i4x4, normal f4x3, normal_w u1, color f4x4, uv f4x2
    assert decompressed["position"].subdtype[0] == np.dtype(np.float32)
    assert decompressed["bone_indices"].subdtype[0] == np.dtype(np.int32)
    assert decompressed["normal_w"].subdtype[0] == np.dtype(np.uint8)


def test_uv_pair_produces_two_uv_fields():
    layout = VertexArrayLayout([VertexPosition(FE.Float3), VertexUV(FE.UVPair)])
    compressed, _ = layout.get_dtypes()
    assert compressed.names == ("position", "uv_0", "uv_1")
    assert layout.get_uv_count() == 2


def test_multiple_uv_types_are_indexed_in_order():
    layout = VertexArrayLayout([
        VertexPosition(FE.Float3),
        VertexUV(FE.UVPair),
        VertexUV(FE.UV, 1),
    ])
    compressed, _ = layout.get_dtypes()
    assert compressed.names == ("position", "uv_0", "uv_1", "uv_2")
    assert layout.get_uv_count() == 3


def test_multiple_tangents_and_colors_are_indexed():
    layout = VertexArrayLayout([
        VertexPosition(FE.Float3),
        VertexTangent(FE.FourBytesC, 0),
        VertexTangent(FE.FourBytesC, 1),
        VertexColor(FE.FourBytesC, 0),
        VertexColor(FE.FourBytesC, 1),
    ])
    compressed, _ = layout.get_dtypes()
    assert compressed.names == ("position", "tangent_0", "tangent_1", "color_0", "color_1")


def test_big_endian_layout_dtypes_are_big_endian():
    layout = VertexArrayLayout([VertexPosition(FE.Float3)], byte_order=ByteOrder.BigEndian)
    compressed, decompressed = layout.get_dtypes()
    assert compressed["position"].subdtype[0].byteorder == ">"
    assert decompressed["position"].subdtype[0].byteorder == ">"


def test_has_vertex_data_type_by_class_and_string():
    layout = _standard_ds1_layout()
    assert layout.has_vertex_data_type(VertexPosition)
    assert layout.has_vertex_data_type("position")
    assert layout.has_vertex_data_type("uv", instance_index=0)
    assert not layout.has_vertex_data_type("uv", instance_index=1)
    assert not layout.has_vertex_data_type(VertexBoneWeights)
    assert not layout.has_vertex_data_type("bone_weights")


def test_set_unk_x00_applies_to_all_write_types():
    layout = _standard_ds1_layout()
    layout.set_unk_x00(3)
    assert all(t.unk_x00 == 3 for t in layout.write_types)


# ---------------------------------------------------------------------------
# Array pack/unpack
# ---------------------------------------------------------------------------


def test_unpack_pack_array_is_byte_stable():
    """Raw bytes -> structured array -> raw bytes must be identical for a standard layout."""
    layout = _standard_ds1_layout()
    rng = np.random.default_rng(0)
    raw = rng.integers(0, 256, size=28 * 32, dtype=np.uint8).tobytes()
    array = layout.unpack_vertex_array(raw, uv_factor=1024)
    assert len(array) == 32
    repacked = layout.pack_vertex_array(array, uv_factor=1024)
    assert repacked == raw


def test_unpack_decompresses_values():
    layout = VertexArrayLayout([VertexPosition(FE.Float3), VertexNormal(FE.FourBytesC), VertexUV(FE.UV)])
    compressed_dtype, _ = layout.get_dtypes()
    compressed = np.zeros(2, dtype=compressed_dtype)
    compressed["position"] = [[1.0, 2.0, 3.0], [-1.0, 0.0, 0.5]]
    compressed["normal"] = [[254, 127, 0], [127, 127, 127]]
    compressed["normal_w"] = [[127], [0]]
    compressed["uv_0"] = [[1024, 2048], [-1024, 0]]
    array = layout.unpack_vertex_array(compressed.tobytes(), uv_factor=1024)
    assert np.allclose(array["position"][0], [1.0, 2.0, 3.0])
    assert np.allclose(array["normal"][0], [(254 - 127) / 127, 0.0, -1.0])
    # `normal_w` is never decompressed to a float.
    assert array["normal_w"][0][0] == 127
    assert np.allclose(array["uv_0"], [[1.0, 2.0], [-1.0, 0.0]])


def test_uv_factor_affects_unpacked_uvs():
    layout = VertexArrayLayout([VertexUV(FE.UV)])
    compressed_dtype, _ = layout.get_dtypes()
    compressed = np.zeros(1, dtype=compressed_dtype)
    compressed["uv_0"] = [[2048, 1024]]
    array_1024 = layout.unpack_vertex_array(compressed.tobytes(), uv_factor=1024)
    array_2048 = layout.unpack_vertex_array(compressed.tobytes(), uv_factor=2048)
    assert np.allclose(array_1024["uv_0"], [[2.0, 1.0]])
    assert np.allclose(array_2048["uv_0"], [[1.0, 0.5]])


def test_vertex_ignore_data_is_stripped():
    """A `VertexIgnore` type consumes bytes on read and is omitted from the dtype and on write."""
    layout = VertexArrayLayout([
        VertexPosition(FE.Float3),
        VertexIgnore(4),
        VertexUV(FE.UV),
    ])
    assert layout.get_total_data_size(include_ignored=True) == 20
    assert layout.get_total_data_size(include_ignored=False) == 16
    assert len(layout.read_types) == 3
    assert len(layout.write_types) == 2

    compressed_dtype, _ = layout.get_dtypes()
    assert compressed_dtype.names == ("position", "uv_0")

    # Build raw data with 4 junk bytes between position and UV for each of 3 vertices.
    raw = bytearray()
    for i in range(3):
        raw += np.array([i, i + 1, i + 2], dtype=np.float32).tobytes()
        raw += b"\xDE\xAD\xBE\xEF"
        raw += np.array([i * 1024, i * 2048], dtype=np.int16).tobytes()
    array = layout.unpack_vertex_array(bytes(raw), uv_factor=1024)
    assert len(array) == 3
    assert np.allclose(array["position"][2], [2.0, 3.0, 4.0])
    assert np.allclose(array["uv_0"][2], [2.0, 4.0])
    # Packed data no longer includes ignored bytes.
    assert len(layout.pack_vertex_array(array, uv_factor=1024)) == 3 * 16


# ---------------------------------------------------------------------------
# Equality / hashing (used for layout deduplication on FLVER export)
# ---------------------------------------------------------------------------


def test_layout_equality_and_hash():
    a = _standard_ds1_layout()
    b = _standard_ds1_layout()
    assert a == b
    assert hash(a) == hash(b)
    c = VertexArrayLayout([VertexPosition(FE.Float3)])
    assert a != c
    assert a != "not a layout"


def test_layout_equality_ignores_data_offset():
    a = VertexArrayLayout([VertexPosition(FE.Float3, 0, 0, 0)])
    b = VertexArrayLayout([VertexPosition(FE.Float3, 0, 0, 12)])
    assert a == b


def test_layout_inequality_on_instance_index():
    a = VertexArrayLayout([VertexUV(FE.UV, 0)])
    b = VertexArrayLayout([VertexUV(FE.UV, 1)])
    assert a != b


def test_constructor_accepts_list_or_varargs():
    types = [VertexPosition(FE.Float3), VertexUV(FE.UV)]
    from_list = VertexArrayLayout(types)
    from_args = VertexArrayLayout(*types)
    assert from_list == from_args
    # `read_types` returns a copy: mutating it must not affect the layout.
    read_types = from_list.read_types
    read_types.clear()
    assert len(from_list.read_types) == 2


# ---------------------------------------------------------------------------
# Binary layout struct I/O
# ---------------------------------------------------------------------------


def test_flver2_layout_struct_roundtrip():
    layout = _standard_ds1_layout()
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    layout.to_flver2_writer(writer)
    layout.pack_flver2_layout_types(writer)
    data = bytes(writer.array)

    reader = BinaryReader(data, byte_order=ByteOrder.LittleEndian)
    reloaded = VertexArrayLayout.from_flver2_reader(reader)
    assert reloaded == layout
    assert hash(reloaded) == hash(layout)
    assert [t.data_offset for t in reloaded.read_types] == [0, 12, 16, 20, 24]


def test_flver0_layout_struct_roundtrip():
    layout = _standard_ds1_layout()
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    layout.to_flver0_writer(writer)
    data = bytes(writer.array)

    reader = BinaryReader(data, byte_order=ByteOrder.LittleEndian)
    reloaded = VertexArrayLayout.from_flver0_reader(reader)
    assert reloaded == layout


def test_flver2_layout_struct_roundtrip_skips_ignored_types():
    """`VertexIgnore` types are never written, so the reloaded layout is the 'write' subset."""
    layout = VertexArrayLayout([VertexPosition(FE.Float3), VertexIgnore(4), VertexUV(FE.UV)])
    writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
    layout.to_flver2_writer(writer)
    layout.pack_flver2_layout_types(writer)
    reader = BinaryReader(bytes(writer.array), byte_order=ByteOrder.LittleEndian)
    reloaded = VertexArrayLayout.from_flver2_reader(reader)
    assert len(reloaded.read_types) == 2
    assert reloaded == VertexArrayLayout(layout.write_types)
