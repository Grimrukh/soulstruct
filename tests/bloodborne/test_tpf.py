"""Bloodborne TPF (texture container) tests.

Bloodborne TPFs are PS4-platform DDS containers compressed with `DCX_DFLT_10000_44_9`. The committed
resource is a single-texture map ground TPF.
"""
from __future__ import annotations

import pytest

from soulstruct.containers.tpf import TPF, TPFPlatform
from soulstruct.dcx import DCXType
from soulstruct.games import BLOODBORNE

TPF_NAME = "m21_00_ground_051_a.tpf.dcx"


@pytest.fixture
def bb_tpf(resource) -> TPF:
    return TPF.from_path(resource(TPF_NAME))


def test_tpf_loads(bb_tpf):
    assert len(bb_tpf.textures) == 1
    texture = bb_tpf.textures[0]
    assert texture.stem
    assert texture.data


def test_tpf_platform_is_ps4(bb_tpf):
    """Bloodborne is PS4-only, so its TPFs use the PS4 platform (which changes the texture header layout)."""
    assert bb_tpf.platform == TPFPlatform.PS4


def test_tpf_dcx_type_is_bloodborne_default(bb_tpf):
    assert bb_tpf.dcx_type == DCXType.DCX_DFLT_10000_44_9
    assert BLOODBORNE.default_dcx_type == DCXType.DCX_DFLT_10000_44_9


def test_tpf_binary_roundtrip(bb_tpf, tmp_path):
    """unpack -> pack -> unpack must be stable."""
    written = bb_tpf.write(tmp_path / TPF_NAME)
    reloaded = TPF.from_path(written[0])
    assert reloaded.platform == bb_tpf.platform
    assert reloaded.encoding_type == bb_tpf.encoding_type
    assert reloaded.tpf_flags == bb_tpf.tpf_flags
    assert len(reloaded.textures) == len(bb_tpf.textures)
    for source, reload in zip(bb_tpf.textures, reloaded.textures):
        assert source.stem == reload.stem
        assert source.format == reload.format
        assert source.data == reload.data


def test_tpf_repack_is_byte_stable(bb_tpf):
    """Packing the same `TPF` twice must produce identical bytes (no ordering/padding nondeterminism)."""
    first = bytes(bb_tpf)
    second = bytes(bb_tpf)
    assert first == second


def test_tpf_uncompressed_roundtrip(bb_tpf, tmp_path):
    """Round-trip with DCX explicitly disabled, isolating TPF packing from DCX compression."""
    bb_tpf.dcx_type = DCXType.Null
    written = bb_tpf.write(tmp_path / "uncompressed.tpf")
    assert written[0].name == "uncompressed.tpf"
    reloaded = TPF.from_path(written[0])
    assert reloaded.dcx_type == DCXType.Null
    assert len(reloaded.textures) == len(bb_tpf.textures)
    assert reloaded.textures[0].data == bb_tpf.textures[0].data


@pytest.mark.game_data
@pytest.mark.slow
def test_vanilla_chrtpfbhd_sample(bb_root, tmp_path):
    """Round-trip a handful of vanilla character TPFs, if Bloodborne is installed."""
    chr_dir = bb_root / "chr"
    if not chr_dir.is_dir():
        pytest.skip(f"Missing chr directory: {chr_dir}")
    tpf_paths = sorted(chr_dir.glob("*.tpf.dcx"))[:5]
    if not tpf_paths:
        pytest.skip("No standalone character TPFs found.")
    for tpf_path in tpf_paths:
        tpf = TPF.from_path(tpf_path)
        reloaded = TPF.from_bytes(bytes(tpf))
        assert len(reloaded.textures) == len(tpf.textures)
