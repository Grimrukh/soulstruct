"""Shared pytest fixtures and helpers for the Soulstruct test suite.

Design goals:
    - **Path-independent.** No test may depend on the current working directory. Use the
      `resources` fixture (per-game `resources/` dir) or a `*_root` game-directory fixture.
    - **Graceful skipping.** Tests that need an unpacked vanilla game directory are skipped
      (not failed) when that game is not installed on this machine. Game roots are read live
      from `soulstruct.config.Config`, so any machine with the data will run them.
    - **No test pollution.** All output goes to pytest's `tmp_path`; nothing is written into
      the repository tree.
"""
from __future__ import annotations

__all__ = [
    "GAME_ROOT_FIXTURE_NAMES",
    "binary_roundtrip",
    "json_roundtrip",
    "assert_bytes_equal",
]

import typing as tp
from pathlib import Path

import pytest

from soulstruct.config import Config

if tp.TYPE_CHECKING:
    from soulstruct.base.base_binary_file import BaseBinaryFile

TESTS_DIR = Path(__file__).parent


# ---------------------------------------------------------------------------
# Game directory fixtures
# ---------------------------------------------------------------------------

# Maps fixture name -> (Config attribute, human-readable game name).
_GAME_ROOTS = {
    "des_root": ("DES_PATH", "Demon's Souls"),
    "desr_root": ("DESR_PATH", "Demon's Souls Remake"),
    "ptde_root": ("PTDE_PATH", "Dark Souls: Prepare to Die Edition"),
    "dsr_root": ("DSR_PATH", "Dark Souls: Remastered"),
    "ds2_root": ("DS2_PATH", "Dark Souls II"),
    "ds2_sotfs_root": ("DS2_SOTFS_PATH", "Dark Souls II: Scholar of the First Sin"),
    "bb_root": ("BB_PATH", "Bloodborne"),
    "ds3_root": ("DS3_PATH", "Dark Souls III"),
    "sekiro_root": ("SEK_PATH", "Sekiro: Shadows Die Twice"),
    "er_root": ("ER_PATH", "Elden Ring"),
}

GAME_ROOT_FIXTURE_NAMES = tuple(_GAME_ROOTS)


def _make_game_root_fixture(config_attr: str, game_name: str):
    """Build a fixture that returns an existing game root `Path` or skips the test."""

    def _fixture() -> Path:
        root = getattr(Config, config_attr)
        if not root or not Path(root).is_dir():
            pytest.skip(
                f"{game_name} directory not found (Config.{config_attr} = {root!r}). "
                f"Set it in your `soulstruct_config.json` to run this test."
            )
        return Path(root)

    _fixture.__doc__ = f"Unpacked vanilla {game_name} root directory, or skip."
    return pytest.fixture(scope="session")(_fixture)


for _fixture_name, (_attr, _game) in _GAME_ROOTS.items():
    globals()[_fixture_name] = _make_game_root_fixture(_attr, _game)
del _fixture_name, _attr, _game


# ---------------------------------------------------------------------------
# Resource fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def tests_dir() -> Path:
    """Absolute path to the `tests/` directory."""
    return TESTS_DIR


@pytest.fixture
def resources(request: pytest.FixtureRequest) -> Path:
    """Absolute path to the `resources/` directory beside the calling test module.

    Skips the test if that directory does not exist, so a partial checkout does not fail.
    """
    res_dir = Path(request.path).parent / "resources"
    if not res_dir.is_dir():
        pytest.skip(f"No `resources` directory at {res_dir}.")
    return res_dir


@pytest.fixture
def resource(resources: Path):
    """Callable returning an absolute path to a named file in the module's `resources/` dir.

    Skips the test if the file is absent (these binaries are large and may not all be committed).
    """

    def _get(name: str) -> Path:
        path = resources / name
        if not path.is_file():
            pytest.skip(f"Test resource not available: {path}")
        return path

    return _get


# ---------------------------------------------------------------------------
# Round-trip helpers
# ---------------------------------------------------------------------------


def assert_bytes_equal(actual: bytes, expected: bytes, context: str = "") -> None:
    """Assert two byte strings are identical, reporting the first differing offset."""
    if actual == expected:
        return
    prefix = f"{context}: " if context else ""
    if len(actual) != len(expected):
        # Still locate the first difference in the common prefix, if any.
        limit = min(len(actual), len(expected))
        for i in range(limit):
            if actual[i] != expected[i]:
                raise AssertionError(
                    f"{prefix}byte mismatch at offset 0x{i:X} "
                    f"({actual[i]:#04x} != {expected[i]:#04x}) and length differs "
                    f"({len(actual)} != {len(expected)})."
                )
        raise AssertionError(f"{prefix}length differs ({len(actual)} != {len(expected)}), common prefix matches.")
    for i, (a, b) in enumerate(zip(actual, expected)):
        if a != b:
            raise AssertionError(f"{prefix}byte mismatch at offset 0x{i:X} ({a:#04x} != {b:#04x}).")


def binary_roundtrip(binary_file: BaseBinaryFile, tmp_path: Path, name: str = "_roundtrip"):
    """Write `binary_file` to `tmp_path`, read it back with the same class, and return the reloaded file.

    This is the single most valuable assertion for a binary format: unpack -> pack -> unpack must
    be stable. It does NOT assert byte-identity with the original game file, which is often
    infeasible (padding, ordering, optional blocks); use `assert_bytes_equal` for formats known
    to be byte-stable.
    """
    write_path = tmp_path / name
    binary_file.write(write_path)
    return type(binary_file).from_path(write_path)


def json_roundtrip(binary_file: BaseBinaryFile, tmp_path: Path, name: str = "_roundtrip.json"):
    """Write `binary_file` to JSON, read it back, and return the reloaded file.

    Only valid for classes implementing `write_json` / `from_json`.
    """
    write_path = tmp_path / name
    binary_file.write_json(write_path)
    return type(binary_file).from_json(write_path)


# ---------------------------------------------------------------------------
# Collection tweaks
# ---------------------------------------------------------------------------


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "game_data: test requires an unpacked vanilla game directory.")
    config.addinivalue_line("markers", "slow: test reads a whole game directory and is slow.")
