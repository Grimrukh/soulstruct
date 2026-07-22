"""Tests for reading DSR `TPF` texture containers.

`TPF` is a game-independent container (`soulstruct.containers.tpf`), but DSR map textures are the most
common consumer: `map/mXX/mXX_YY_*.tpfbhd` split Binders hold `*.tpf.dcx` entries like the committed
`m10_00_arch_01.tpf.dcx` resource.

Note the current API: textures expose `stem`, `data`, `get_dds()` / `get_dds_fourcc()` /
`get_headerized_data()`. (The old `TPFTexture.name` / `get_dds_header()` names no longer exist.)
"""
from __future__ import annotations

from pathlib import Path

import pytest

from soulstruct.dcx import DCXType
from soulstruct.containers.tpf import TPF, TPFTexture

TPF_NAME = "m10_00_arch_01.tpf.dcx"


@pytest.fixture
def tpf_path(resource) -> Path:
    return resource(TPF_NAME)


@pytest.fixture
def tpf(tpf_path) -> TPF:
    return TPF.from_path(tpf_path)


def test_tpf_read(tpf):
    assert tpf.dcx_type != DCXType.Null, "DSR map TPFs are DCX-compressed."
    assert len(tpf.textures) == 1
    texture = tpf.textures[0]
    assert isinstance(texture, TPFTexture)
    assert texture.stem == "m10_00_arch_01"
    assert texture.data


def test_texture_dds_header(tpf):
    texture = tpf.textures[0]
    assert texture.get_dds_fourcc() == b"DXT1"
    dds = texture.get_dds()
    assert dds is not None
    # DS1 TPF entry data already carries its own DDS header, so `get_headerized_data()` is a no-op.
    assert texture.data.startswith(b"DDS ")
    assert texture.get_headerized_data() == texture.data


def test_tpf_binary_roundtrip(tpf, tmp_path):
    tpf.write(tmp_path / TPF_NAME)
    reload = TPF.from_path(tmp_path / TPF_NAME)
    assert len(reload.textures) == len(tpf.textures)
    for a, b in zip(tpf.textures, reload.textures):
        assert a.stem == b.stem
        assert a.format == b.format
        assert a.texture_type == b.texture_type
        assert a.texture_flags == b.texture_flags
        assert a.data == b.data
    assert reload.platform == tpf.platform
    assert reload.encoding_type == tpf.encoding_type
    assert reload.tpf_flags == tpf.tpf_flags


@pytest.mark.xfail(
    reason="BUG (fidelity): vanilla DS1 TPF textures store `mipmap_count = 0` (meaning 'read the count "
           "from the embedded DDS header'), but Soulstruct recomputes and writes the real count (10), "
           "silently mutating the field on every round-trip.",
    strict=False,
)
def test_tpf_roundtrip_preserves_mipmap_count(tpf, tmp_path):
    tpf.write(tmp_path / TPF_NAME)
    reload = TPF.from_path(tmp_path / TPF_NAME)
    assert reload.textures[0].mipmap_count == tpf.textures[0].mipmap_count == 0


def test_tpf_repack_is_idempotent(tpf):
    """Repacking is not byte-identical to vanilla (DCX recompression), but must be a fixed point."""
    once = bytes(tpf)
    twice = bytes(TPF.from_bytes(once))
    assert twice == once


def test_texture_data_can_be_exported_as_dds(tpf, tmp_path):
    texture = tpf.textures[0]
    dds_path = tmp_path / f"{texture.stem}.dds"
    texture.write_dds(dds_path)
    written = dds_path.read_bytes()
    assert written.startswith(b"DDS ")
    assert written == texture.data


@pytest.mark.slow
@pytest.mark.game_data
def test_dsr_map_tpfbhd_textures_load(dsr_root):
    """Read every TPF entry from one DSR map-area TPFBHD split Binder."""
    from soulstruct.containers import Binder

    area_dir = dsr_root / "map/m10"
    if not area_dir.is_dir():
        pytest.skip(f"Missing DSR map area directory: {area_dir}")
    bhd_paths = sorted(area_dir.glob("m*.tpfbhd"))
    if not bhd_paths:
        pytest.skip(f"No TPFBHD binders in {area_dir}.")

    bhd = Binder.from_path(bhd_paths[0])
    assert bhd.entries
    checked = 0
    for entry in bhd.entries[:25]:  # a full BHD has hundreds of textures; a sample is enough
        entry_tpf = entry.to_binary_file(TPF)
        assert entry_tpf.textures
        for texture in entry_tpf.textures:
            assert texture.stem
            assert texture.data
        checked += 1
    assert checked > 0
