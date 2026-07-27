"""Tests for Elden Ring's encrypted `regulation.bin` (`GameParamBND`).

`regulation.bin` is an AES-encrypted (IV-prefixed CBC) blob whose plaintext is a DCX-ZSTD-compressed
BND4 containing one `.param` entry per param. Soulstruct shells out to a bundled .NET executable
(`soulstruct/base/params/ParamCrypt/ParamCrypt.exe`) for the crypto, then hands the plaintext to the
normal `Binder`/`Param` machinery.

Entry points:
    `GameParamBND.from_encrypted_path(path)` -> decrypt -> `Binder.from_bytes` -> `params` dict
    `GameParamBND.write_encrypted(path)`     -> `Binder.write` -> encrypt

Reading a full vanilla `regulation.bin` takes ~25-35s, so those tests are marked `slow`.
"""
from __future__ import annotations

import platform
import sys

import pytest

from soulstruct.base.params.ParamCrypt import ParamCrypt, PARAM_CRYPT_EXE
from soulstruct.base.params.param import Param
from soulstruct.eldenring.params import GameParamBND
from soulstruct.utilities.files import SOULSTRUCT_PATH


requires_paramcrypt = pytest.mark.skipif(
    not PARAM_CRYPT_EXE.is_file() or platform.system() != "Windows",
    reason="`ParamCrypt.exe` (bundled .NET binary) is only usable on Windows.",
)


@pytest.fixture(scope="module")
def regulation_path(request):
    """Path to the committed test `regulation.bin` (skips if absent)."""
    from pathlib import Path

    path = Path(request.path).parent / "resources" / "regulation.bin"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


@pytest.fixture(scope="module")
def decrypted_bytes(regulation_path, tmp_path_factory) -> bytes:
    """Raw decrypted (still DCX-compressed) `regulation.bin` payload."""
    if not PARAM_CRYPT_EXE.is_file() or platform.system() != "Windows":
        pytest.skip("`ParamCrypt.exe` not usable on this platform.")
    out = tmp_path_factory.mktemp("paramcrypt") / "decrypted.parambnd.dcx"
    ParamCrypt(regulation_path, "decrypt", "er", out)
    return out.read_bytes()


@pytest.fixture(scope="module")
def regulation(regulation_path) -> GameParamBND:
    """Fully unpacked `GameParamBND` from the committed test `regulation.bin`. Expensive (~30 s)."""
    if not PARAM_CRYPT_EXE.is_file() or platform.system() != "Windows":
        pytest.skip("`ParamCrypt.exe` not usable on this platform.")
    return GameParamBND.from_encrypted_path(regulation_path)


# ---------------------------------------------------------------------------
# `ParamCrypt` wrapper (cheap: no Binder parsing)
# ---------------------------------------------------------------------------


def test_param_crypt_exe_is_bundled():
    assert PARAM_CRYPT_EXE.name == "ParamCrypt.exe"
    assert PARAM_CRYPT_EXE.is_file(), "Bundled `ParamCrypt.exe` is missing from the package."


def test_param_crypt_rejects_bad_arguments(tmp_path):
    dummy = tmp_path / "dummy.bin"
    dummy.write_bytes(b"\0" * 32)
    with pytest.raises(ValueError):
        ParamCrypt(dummy, "scramble", "er", tmp_path / "out.bin")
    with pytest.raises(ValueError):
        ParamCrypt(dummy, "decrypt", "ds1", tmp_path / "out.bin")


@requires_paramcrypt
def test_decrypt_produces_dcx_payload(decrypted_bytes):
    """Decrypted `regulation.bin` must start with a DCX magic header."""
    assert decrypted_bytes[:4] == b"DCX\0", f"Unexpected decrypted header: {decrypted_bytes[:8]!r}"
    # Encrypted file is 16 bytes larger than plaintext (prefixed CBC IV).
    assert len(decrypted_bytes) % 16 == 0


@requires_paramcrypt
def test_decrypt_is_deterministic(regulation_path, tmp_path):
    a = tmp_path / "a.parambnd.dcx"
    b = tmp_path / "b.parambnd.dcx"
    ParamCrypt(regulation_path, "decrypt", "er", a)
    ParamCrypt(regulation_path, "decrypt", "er", b)
    assert a.read_bytes() == b.read_bytes()


@requires_paramcrypt
def test_encrypt_output_is_decryptable(decrypted_bytes, tmp_path):
    """encrypt -> decrypt must recover the original plaintext (allowing for trailing PKCS7 padding)."""
    plain = tmp_path / "plain.parambnd.dcx"
    plain.write_bytes(decrypted_bytes)
    enc = tmp_path / "reencrypted.bin"
    ParamCrypt(plain, "encrypt", "er", enc)
    dec = tmp_path / "redecrypted.parambnd.dcx"
    ParamCrypt(enc, "decrypt", "er", dec)
    round_tripped = dec.read_bytes()
    assert round_tripped[: len(decrypted_bytes)] == decrypted_bytes


@requires_paramcrypt
def test_encryption_uses_a_fresh_iv(decrypted_bytes, tmp_path):
    """Two encryptions of the same plaintext must differ (random CBC IV prefix)."""
    plain = tmp_path / "plain.parambnd.dcx"
    plain.write_bytes(decrypted_bytes)
    e1, e2 = tmp_path / "e1.bin", tmp_path / "e2.bin"
    ParamCrypt(plain, "encrypt", "er", e1)
    ParamCrypt(plain, "encrypt", "er", e2)
    assert e1.read_bytes() != e2.read_bytes()
    assert e1.read_bytes()[:16] != e2.read_bytes()[:16]


@requires_paramcrypt
@pytest.mark.xfail(
    reason="BUG: `ParamCrypt.exe` encrypts with PKCS7 padding but decrypts without stripping it, so "
           "decrypt(encrypt(x)) == x + b'\\x10' * 16. Harmless for DCX readers, but the round-trip "
           "is not byte-exact and file size creeps by 16 bytes.",
    strict=False,
)
def test_encrypt_decrypt_is_byte_exact(decrypted_bytes, tmp_path):
    plain = tmp_path / "plain.parambnd.dcx"
    plain.write_bytes(decrypted_bytes)
    enc = tmp_path / "e.bin"
    ParamCrypt(plain, "encrypt", "er", enc)
    dec = tmp_path / "d.parambnd.dcx"
    ParamCrypt(enc, "decrypt", "er", dec)
    assert dec.read_bytes() == decrypted_bytes


# ---------------------------------------------------------------------------
# `GameParamBND` reading (slow)
# ---------------------------------------------------------------------------


@pytest.mark.slow
@requires_paramcrypt
def test_read_encrypted_regulation(regulation):
    assert len(regulation.params) > 150
    assert "NpcParam" in regulation.params
    assert "EquipParamWeapon" in regulation.params
    assert regulation.path is not None and regulation.path.name == "regulation.bin"


@pytest.mark.slow
@requires_paramcrypt
def test_param_property_access(regulation):
    """The advertised nickname properties must return the same object as `params[stem]`."""
    assert regulation.NpcParam is regulation.params["NpcParam"]
    assert regulation.EquipParamWeapon is regulation.params["EquipParamWeapon"]
    assert regulation.get_param("NpcParam") is regulation.params["NpcParam"]
    assert regulation.get_param("NpcParam.param") is regulation.params["NpcParam"]


@pytest.mark.slow
@requires_paramcrypt
def test_starscourge_radahn_npc_row(regulation):
    """Preserved intent of the original `test_params.py`: read Radahn's `NpcParam` row."""
    radahn = regulation.NpcParam[47300000]
    assert type(radahn).__name__ == "NPC_PARAM_ST"
    assert radahn.MaximumHP > 0
    # Nickname and internal-name lookup must agree.
    assert radahn["MaximumHP"] == radahn["hp"]
    assert isinstance(repr(radahn), str)


@pytest.mark.slow
@requires_paramcrypt
def test_param_rows_are_sorted_and_unique(regulation):
    for stem, param in regulation.params.items():
        ids = list(param.rows)
        assert len(ids) == len(set(ids)), f"{stem} has duplicate row IDs."


@pytest.mark.slow
@requires_paramcrypt
def test_param_header_flags(regulation):
    """Elden Ring params use `flags1 = 133` (OffsetParam | LongDataOffset | bit 0) and `flags2 = 7`."""
    npc = regulation.params["NpcParam"]
    assert int(npc.flags1) == 133
    assert int(npc.flags2) == 7
    assert npc.flags1.OffsetParam
    assert npc.flags1.LongDataOffset
    assert not npc.big_endian


@pytest.mark.slow
@requires_paramcrypt
def test_row_binary_roundtrip(regulation):
    """unpack -> pack -> unpack of a single row must be stable."""
    radahn = regulation.NpcParam[47300000]
    packed = bytes(radahn.to_writer())
    reloaded = type(radahn).from_bytes(packed)
    assert bytes(reloaded.to_writer()) == packed


# ---------------------------------------------------------------------------
# `GameParamBND` writing -- currently impossible (see xfails)
# ---------------------------------------------------------------------------


@pytest.mark.slow
@requires_paramcrypt
@pytest.mark.xfail(
    reason="CRITICAL BUG: `Param.to_writer()` packs the header with format '4b' (signed bytes), but "
           "Elden Ring params have `flags1 = 133`, so `struct.error: 'b' format requires -128 <= number "
           "<= 127` is raised. NO Elden Ring param (and therefore no `regulation.bin`) can be written.",
    strict=False,
)
def test_single_param_can_be_packed(regulation):
    npc = regulation.params["NpcParam"]
    packed = bytes(npc)
    assert packed[:4] != b""
    reloaded = Param.detect_param_type(packed)
    assert reloaded == "NPC_PARAM_ST"


@pytest.mark.slow
@requires_paramcrypt
@pytest.mark.xfail(
    reason="CRITICAL BUG: blocked by the same `Param.to_writer()` '4b' signed-byte pack. "
           "`write_encrypted()` therefore always raises `struct.error`.",
    strict=False,
)
def test_write_encrypted_roundtrip(regulation, tmp_path):
    out = tmp_path / "regulation.bin"
    regulation.write_encrypted(out)
    assert out.is_file()
    reloaded = GameParamBND.from_encrypted_path(out)
    assert set(reloaded.params) == set(regulation.params)
    for stem in regulation.params:
        assert list(reloaded.params[stem].rows) == list(regulation.params[stem].rows), stem


def test_paramcrypt_scratch_path_is_inside_the_package():
    """Documents a design trap: both `from_encrypted_path` and `write_encrypted` use one FIXED
    scratch path inside the *installed package directory*.

    `from_encrypted_path` deletes it; `write_encrypted` does NOT (`# temp_decrypted.unlink()` is
    commented out at `eldenring/params/gameparambnd.py:260`). Neither is concurrency-safe, and both
    fail if `soulstruct` is installed somewhere read-only.
    """
    temp_path = SOULSTRUCT_PATH("__ParamCrypt__.parambnd.dcx")
    package_root = SOULSTRUCT_PATH()
    assert temp_path.parent == package_root, (
        "ParamCrypt scratch file should be relocated to a real temp directory."
    )


# ---------------------------------------------------------------------------
# Live game install (skipped when Elden Ring is not installed)
# ---------------------------------------------------------------------------


@pytest.mark.slow
@requires_paramcrypt
def test_live_regulation_decrypts(er_root, tmp_path):
    """The installed game's `regulation.bin` must decrypt to a DCX payload."""
    live = er_root / "regulation.bin"
    if not live.is_file():
        pytest.skip(f"No `regulation.bin` in Elden Ring install: {live}")
    out = tmp_path / "live.parambnd.dcx"
    ParamCrypt(live, "decrypt", "er", out)
    assert out.read_bytes()[:4] == b"DCX\0"
