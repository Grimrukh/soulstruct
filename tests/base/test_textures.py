"""Tests for `soulstruct.base.textures`: DDS header parsing, mipmap maths, DXGI format info, and the
console (PS3/PS4) Morton swizzle/deswizzle pair.
"""
from __future__ import annotations

import contextlib
import io
import logging
from pathlib import Path

import pytest

from soulstruct.base.textures.dds.core import DDS, DDSHeader, DDSPixelFormat, DX10Header, DDSImage
from soulstruct.base.textures.dds.enums import (
    DXGI_FORMAT,
    DXGI_FORMAT_BPP,
    DDPF,
    D3D10_RESOURCE_DIMENSION,
    ALPHA_MODE,
)
from soulstruct.base.textures.dds.utilities import morton
from soulstruct.base.textures.dds.swizzle import (
    swizzle_dds_bytes_ps3,
    swizzle_dds_bytes_ps4,
    DDSSwizzleError,
)
from soulstruct.base.textures.dds.deswizzle import (
    deswizzle_dds_bytes_ps3,
    deswizzle_dds_bytes_ps4,
    DDSDeswizzleError,
)
from soulstruct.base.textures.texconv import TexconvConfig, TexconvError, texconv_to_dds


def _quiet():
    """`deswizzle_dds_bytes_ps3` contains stray `print()` calls (finding M7)."""
    return contextlib.redirect_stdout(io.StringIO())


# ---------------------------------------------------------------------------
# DDS header structs (pure unit)
# ---------------------------------------------------------------------------


def test_dds_header_sizes():
    """DDS magic + header is exactly 128 bytes; the DX10 extension adds 20."""
    pf = DDSPixelFormat(flags=0, fourcc=b"DXT1")
    header = DDSHeader(
        flags=0, height=4, width=4, pitch_or_linear_size=8, depth=0, mipmap_count=1,
        reserved_1=[0] * 11, pixelformat=pf, caps1=0, caps2=0, caps3=0, caps4=0, reserved_2=0,
    )
    assert len(bytes(header.to_writer())) == 128
    dx10 = DX10Header.get_default(DXGI_FORMAT.BC1_UNORM)
    assert len(bytes(dx10.to_writer())) == 20


def test_dx10_header_defaults():
    dx10 = DX10Header.get_default(DXGI_FORMAT.BC7_UNORM)
    assert dx10.dxgi_format is DXGI_FORMAT.BC7_UNORM
    assert dx10.resource_dimension is D3D10_RESOURCE_DIMENSION.TEXTURE2D
    assert dx10.array_size == 1
    assert dx10.misc_flag == 0
    assert dx10.alpha_mode is ALPHA_MODE.UNKNOWN


@pytest.mark.parametrize(
    "tpf_format, expected_flags, expected_bits",
    [
        (6, DDPF.ALPHAPIXELS | DDPF.RGB, 16),
        (9, DDPF.ALPHAPIXELS | DDPF.RGB, 32),
        (10, DDPF.RGB, 32),
        (16, DDPF.ALPHA, 8),
        (105, DDPF.ALPHAPIXELS | DDPF.RGB, 32),
    ],
)
def test_pixelformat_from_fourcc_tpf_format(tpf_format, expected_flags, expected_bits):
    pf = DDSPixelFormat.from_fourcc_tpf_format(b"\0\0\0\0", tpf_format)
    assert pf.flags & expected_flags == expected_flags
    assert pf.rgb_bit_count == expected_bits


def test_pixelformat_fourcc_sets_flag():
    pf = DDSPixelFormat.from_fourcc_tpf_format(b"DXT5", 0)
    assert pf.fourcc == b"DXT5"
    assert pf.flags & DDPF.FOURCC


def test_pixelformat_unknown_tpf_format_is_ignored():
    pf = DDSPixelFormat.from_fourcc_tpf_format(b"DXT1", 999)
    assert pf.rgb_bit_count == 0  # no match arm ran


def test_dds_roundtrip_synthetic():
    pf = DDSPixelFormat(flags=DDPF.FOURCC, fourcc=b"DXT1")
    header = DDSHeader(
        flags=0x1007, height=8, width=8, pitch_or_linear_size=32, depth=0, mipmap_count=1,
        reserved_1=[0] * 11, pixelformat=pf, caps1=0x1000, caps2=0, caps3=0, caps4=0, reserved_2=0,
    )
    dds = DDS(header=header, dx10_header=None, data=b"\x01" * 32)
    data = bytes(dds)
    reloaded = DDS.from_bytes(data)
    assert reloaded.fourcc == "DXT1"
    assert reloaded.dxgi_format is None
    assert reloaded.header.width == 8 and reloaded.header.height == 8
    assert reloaded.data == b"\x01" * 32
    assert bytes(reloaded) == data
    assert "DXT1" in repr(reloaded)


def test_dds_roundtrip_with_dx10_header():
    pf = DDSPixelFormat(flags=DDPF.FOURCC, fourcc=b"DX10")
    header = DDSHeader(
        flags=0x1007, height=4, width=4, pitch_or_linear_size=16, depth=0, mipmap_count=1,
        reserved_1=[0] * 11, pixelformat=pf, caps1=0x1000, caps2=0, caps3=0, caps4=0, reserved_2=0,
    )
    dds = DDS(header=header, dx10_header=DX10Header.get_default(DXGI_FORMAT.BC7_UNORM), data=b"\x02" * 16)
    reloaded = DDS.from_bytes(bytes(dds))
    assert reloaded.fourcc == "DX10"
    assert reloaded.dxgi_format is DXGI_FORMAT.BC7_UNORM
    assert reloaded.texconv_format == "BC7_UNORM"
    assert "DX10" in repr(reloaded)


def test_dds_empty_fourcc_property():
    pf = DDSPixelFormat(flags=0, fourcc=b"\0\0\0\0")
    header = DDSHeader(
        flags=0, height=1, width=1, pitch_or_linear_size=4, depth=0, mipmap_count=1,
        reserved_1=[0] * 11, pixelformat=pf, caps1=0, caps2=0, caps3=0, caps4=0, reserved_2=0,
    )
    dds = DDS(header=header, dx10_header=None, data=b"")
    assert dds.fourcc == ""
    assert dds.texconv_format == ""
    assert dds.pixelformat is header.pixelformat


def test_dds_rejects_non_dds_data():
    with pytest.raises(Exception):
        DDS.from_bytes(b"NOPE" + b"\0" * 200)


# ---------------------------------------------------------------------------
# `DDSImage` mipmap maths
# ---------------------------------------------------------------------------


def test_dds_image_pad_to():
    assert DDSImage.pad_to(5, 4) == 8
    assert DDSImage.pad_to(8, 4) == 8
    assert DDSImage.pad_to(1, 1) == 1


def test_dds_image_read_uncompressed():
    from soulstruct.utilities.binary import BinaryReader

    width = height = 4
    mipmap_count = 3
    bpp = 4  # RGBA8
    sizes = [(width // 2 ** i) * (height // 2 ** i) * bpp for i in range(mipmap_count)]
    data = b"".join(bytes([i + 1]) * size for i, size in enumerate(sizes))
    images = DDSImage.read_uncompressed_images(
        BinaryReader(data), width, height, pad_dimensions=1, image_count=1,
        mipmap_count=mipmap_count, image_alignment=1, bytes_per_pixel=bpp,
    )
    assert len(images) == 1
    assert [len(m) for m in images[0].mipmap_levels] == sizes
    assert bytes(images[0]) == data


def test_dds_image_read_compressed():
    from soulstruct.utilities.binary import BinaryReader

    width = height = 16
    mipmap_count = 3
    bytes_per_block = 8  # BC1
    sizes = []
    for i in range(mipmap_count):
        w, h = width // 2 ** i, height // 2 ** i
        sizes.append(max(1, w // 4) * max(1, h // 4) * bytes_per_block)
    data = b"".join(bytes([i + 1]) * size for i, size in enumerate(sizes))
    images = DDSImage.read_compressed_images(
        BinaryReader(data), width, height, pad_dimensions=1, image_count=1,
        mipmap_count=mipmap_count, image_alignment=1, bytes_per_block=bytes_per_block,
    )
    assert [len(m) for m in images[0].mipmap_levels] == sizes


def test_dds_image_read_compressed_tiny_mipmaps():
    """Mipmaps below 4x4 still take one full block."""
    from soulstruct.utilities.binary import BinaryReader

    data = b"\x00" * 1000
    images = DDSImage.read_compressed_images(
        BinaryReader(data), 4, 4, pad_dimensions=1, image_count=1,
        mipmap_count=3, image_alignment=1, bytes_per_block=8,
    )
    assert [len(m) for m in images[0].mipmap_levels] == [8, 8, 8]


def test_dds_image_multiple_images():
    from soulstruct.utilities.binary import BinaryReader

    images = DDSImage.read_uncompressed_images(
        BinaryReader(b"\x00" * 1000), 2, 2, pad_dimensions=1, image_count=6,
        mipmap_count=1, image_alignment=1, bytes_per_pixel=4,
    )
    assert len(images) == 6  # e.g. a cubemap


# ---------------------------------------------------------------------------
# DXGI format info
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    reason="L23: `DXGI_FORMAT_BPP` omits P208/V208/V408/FORCE_UINT, so `get_format_info()` raises a "
           "bare `KeyError` for those formats.",
    strict=False,
)
def test_dxgi_bpp_table_covers_all_formats():
    missing = [f.name for f in DXGI_FORMAT if f not in DXGI_FORMAT_BPP]
    assert not missing, missing


def test_dxgi_bpp_table_covers_common_formats():
    common = [
        "R8G8B8A8_UNORM", "B8G8R8A8_UNORM", "B5G5R5A1_UNORM", "R8_UNORM",
        "BC1_UNORM", "BC2_UNORM", "BC3_UNORM", "BC4_UNORM", "BC5_UNORM", "BC7_UNORM",
    ]
    for name in common:
        fmt = getattr(DXGI_FORMAT, name)
        assert fmt in DXGI_FORMAT_BPP, name
        assert DXGI_FORMAT_BPP[fmt] > 0


@pytest.mark.parametrize(
    "format_name, bpp, block_size",
    [
        ("R8G8B8A8_UNORM", 32, 1),
        ("B8G8R8A8_UNORM", 32, 1),
        ("R8_UNORM", 8, 1),
        ("BC1_UNORM", 4, 4),
        ("BC3_UNORM", 8, 4),
        ("BC7_UNORM", 8, 4),
    ],
)
def test_dxgi_format_info_bpp_and_block(format_name, bpp, block_size):
    fmt = getattr(DXGI_FORMAT, format_name)
    got_bpp, got_block, _ = fmt.get_format_info()
    assert got_bpp == bpp
    assert got_block == block_size


@pytest.mark.parametrize("format_name, expected_bytes", [("R8G8B8A8_UNORM", 4), ("BC1_UNORM", 8)])
def test_dxgi_bytes_per_pixel_set_correct_cases(format_name, expected_bytes):
    fmt = getattr(DXGI_FORMAT, format_name)
    assert fmt.get_format_info()[2] == expected_bytes


@pytest.mark.xfail(
    reason="H8: `get_format_info()` hard-codes `pixel_block_size * 2` (= 8) bytes per block for all "
           "block-compressed formats, but BC2/BC3/BC5/BC6H/BC7 use 16 bytes per 4x4 block.",
    strict=False,
)
@pytest.mark.parametrize("format_name", ["BC2_UNORM", "BC3_UNORM", "BC5_UNORM", "BC7_UNORM"])
def test_dxgi_bytes_per_pixel_set_8bpp_blocks(format_name):
    fmt = getattr(DXGI_FORMAT, format_name)
    bpp, block, bytes_per_set = fmt.get_format_info()
    assert bytes_per_set == bpp * block * block // 8 == 16


# ---------------------------------------------------------------------------
# Morton index permutation
# ---------------------------------------------------------------------------


def test_morton_is_a_permutation():
    for sx, sy in [(4, 4), (8, 8), (8, 4), (4, 8)]:
        indices = [morton(t, sx, sy) for t in range(sx * sy)]
        assert sorted(indices) == list(range(sx * sy)), (sx, sy)


def test_morton_identity_for_single_tile():
    assert morton(0, 1, 1) == 0


def test_morton_reorders_indices():
    """The Morton map is a non-trivial permutation (not the identity)."""
    indices = [morton(t, 4, 4) for t in range(16)]
    assert indices != list(range(16))
    assert sorted(indices) == list(range(16))


# ---------------------------------------------------------------------------
# Swizzle / deswizzle
# ---------------------------------------------------------------------------


def _bc1_buffer(width: int, height: int) -> bytes:
    bpp, _, _ = DXGI_FORMAT.BC1_UNORM.get_format_info()
    n = (width * height * bpp) // 8
    return bytes((i * 7 + 3) % 251 for i in range(n))


def test_deswizzle_ps3_is_a_permutation_of_input():
    data = _bc1_buffer(16, 16)
    with _quiet():
        result = deswizzle_dds_bytes_ps3(data, DXGI_FORMAT.BC1_UNORM, 16, 16)
    assert len(result) == len(data)
    assert sorted(result) == sorted(data)


def test_swizzle_deswizzle_ps3_square_roundtrip():
    data = _bc1_buffer(16, 16)
    with _quiet():
        swizzled = swizzle_dds_bytes_ps3(data, DXGI_FORMAT.BC1_UNORM, 16, 16)
        back = deswizzle_dds_bytes_ps3(swizzled, DXGI_FORMAT.BC1_UNORM, 16, 16)
    assert back == data


@pytest.mark.xfail(
    reason="H9: `swizzle_dds_bytes_ps3` applies the Morton map in the SAME direction as the "
           "deswizzler, which is only self-inverse for square textures.",
    strict=False,
)
@pytest.mark.parametrize("width, height", [(32, 16), (64, 32)])
def test_swizzle_deswizzle_ps3_non_square_roundtrip(width, height):
    data = _bc1_buffer(width, height)
    with _quiet():
        swizzled = swizzle_dds_bytes_ps3(data, DXGI_FORMAT.BC1_UNORM, width, height)
        back = deswizzle_dds_bytes_ps3(swizzled, DXGI_FORMAT.BC1_UNORM, width, height)
    assert back == data


@pytest.mark.xfail(
    reason="H9: `swizzle_dds_bytes_ps4` drops the macro-tile (i, j) offsets used by "
           "`deswizzle_dds_bytes_ps4`, so the two are not inverses.",
    strict=False,
)
@pytest.mark.parametrize("width, height", [(16, 16), (64, 64)])
def test_swizzle_deswizzle_ps4_roundtrip(width, height):
    data = _bc1_buffer(width, height)
    swizzled = swizzle_dds_bytes_ps4(data, DXGI_FORMAT.BC1_UNORM, width, height)
    back = deswizzle_dds_bytes_ps4(swizzled, DXGI_FORMAT.BC1_UNORM, width, height)
    assert back == data


def test_deswizzle_ps4_output_size():
    data = _bc1_buffer(64, 64)
    result = deswizzle_dds_bytes_ps4(data, DXGI_FORMAT.BC1_UNORM, 64, 64)
    assert len(result) == len(data)


@pytest.mark.parametrize("fn, error", [
    (deswizzle_dds_bytes_ps3, DDSDeswizzleError),
    (deswizzle_dds_bytes_ps4, DDSDeswizzleError),
    (swizzle_dds_bytes_ps3, DDSSwizzleError),
    (swizzle_dds_bytes_ps4, DDSSwizzleError),
])
def test_swizzlers_reject_tiny_buffers(fn, error):
    with pytest.raises(error):
        with _quiet():
            fn(b"\0" * 4, DXGI_FORMAT.BC1_UNORM, 16, 16)


def test_deswizzle_ps3_prints_debug_output():
    """M7: `deswizzle_dds_bytes_ps3` still contains two debug `print()` calls."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        deswizzle_dds_bytes_ps3(_bc1_buffer(16, 16), DXGI_FORMAT.BC1_UNORM, 16, 16)
    assert "Deswizzle PS3" in buf.getvalue(), "the debug print() calls were removed"


# ---------------------------------------------------------------------------
# `texconv` argument validation (no subprocess run)
# ---------------------------------------------------------------------------


def test_texconv_rejects_typeless_formats(tmp_path):
    config = TexconvConfig(
        output_dir=str(tmp_path), dds_format="BC1_TYPELESS", is_dx10=True,
        mipmap_count=1, input_path=tmp_path / "x.dds",
    )
    with pytest.raises(TexconvError):
        texconv_to_dds(config)


def test_texconv_config_is_a_named_tuple(tmp_path):
    config = TexconvConfig(str(tmp_path), "BC1_UNORM", True, 3, tmp_path / "x.dds")
    assert config.dds_format == "BC1_UNORM"
    assert config.mipmap_count == 3
    assert len(config) == 5


def test_batch_texconv_uses_starmap_incorrectly():
    """H10: `batch_texconv_to_dds` calls `pool.starmap` on 5-field `TexconvConfig` tuples."""
    import importlib
    import inspect

    texconv_module = importlib.import_module("soulstruct.base.textures.texconv")
    source = inspect.getsource(texconv_module.batch_texconv_to_dds)
    assert "starmap" in source, "batch_texconv_to_dds no longer uses starmap - finding H10 is fixed"


# ---------------------------------------------------------------------------
# Real TPF textures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def dsr_tpf(request):
    from soulstruct.containers.tpf import TPF

    path = Path(request.config.rootpath) / "tests" / "darksouls1r" / "resources" / "m10_00_arch_01.tpf.dcx"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    logging.disable(logging.WARNING)
    try:
        return TPF.from_path(path)
    finally:
        logging.disable(logging.NOTSET)


@pytest.fixture(scope="module")
def bb_tpf(request):
    from soulstruct.containers.tpf import TPF

    path = Path(request.config.rootpath) / "tests" / "bloodborne" / "resources" / "m21_00_ground_051_a.tpf.dcx"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    logging.disable(logging.WARNING)
    try:
        return TPF.from_path(path)
    finally:
        logging.disable(logging.NOTSET)


def test_dsr_tpf_dds_header_parsing(dsr_tpf):
    assert dsr_tpf.platform == 0  # PC: full DDS headers present
    texture = dsr_tpf.textures[0]
    dds = DDS.from_bytes(texture.data)
    assert dds.fourcc == "DXT1"
    assert dds.dx10_header is None
    assert dds.header.width == 512 and dds.header.height == 256
    assert dds.header.mipmap_count == 10
    assert dds.header.pixelformat.flags & DDPF.FOURCC


def test_dsr_tpf_dds_repack_is_byte_identical(dsr_tpf):
    texture = dsr_tpf.textures[0]
    dds = DDS.from_bytes(texture.data)
    assert bytes(dds) == texture.data
    assert bytes(DDS.from_bytes(bytes(dds))) == texture.data


def test_dsr_tpf_data_size_matches_mipmap_chain(dsr_tpf):
    """DXT1: total data must equal the sum of all mipmap block counts."""
    dds = DDS.from_bytes(dsr_tpf.textures[0].data)
    width, height, mips = dds.header.width, dds.header.height, dds.header.mipmap_count
    expected = 0
    for i in range(mips):
        w, h = max(1, width >> i), max(1, height >> i)
        expected += max(1, (w + 3) // 4) * max(1, (h + 3) // 4) * 8
    assert len(dds.data) == expected


def test_dsr_tpf_binary_roundtrip(dsr_tpf):
    from soulstruct.containers.tpf import TPF

    data = bytes(dsr_tpf)
    reloaded = TPF.from_bytes(data)
    assert len(reloaded.textures) == len(dsr_tpf.textures)
    assert bytes(reloaded) == data


def test_bloodborne_tpf_is_headerless(bb_tpf):
    """Console (PS4) TPF textures store raw data with no DDS header."""
    assert bb_tpf.platform != 0
    with pytest.raises(Exception):
        DDS.from_bytes(bb_tpf.textures[0].data)


def test_bloodborne_tpf_headerized_dds(bb_tpf):
    texture = bb_tpf.textures[0]
    dds = texture.get_headerized_dds()
    assert isinstance(dds, DDS)
    assert dds.header.width == 2048 and dds.header.height == 2048
    assert dds.fourcc == "DXT1"
    assert bytes(DDS.from_bytes(bytes(dds))) == bytes(dds)


def test_bloodborne_tpf_binary_roundtrip(bb_tpf):
    from soulstruct.containers.tpf import TPF

    data = bytes(bb_tpf)
    reloaded = TPF.from_bytes(data)
    assert len(reloaded.textures) == len(bb_tpf.textures)
    assert bytes(reloaded) == data
