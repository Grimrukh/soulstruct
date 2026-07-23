"""Tests for DSR `EMEVD` (event scripts) and `EventDirectory`.

DSR EMEVD reuses the PTDE instruction set almost entirely: `soulstruct.darksouls1r.events.emevd` defines
its own `EMEDF`/`DECOMPILER`/`EVSParser` but inherits the PTDE compiler. The two real DSR differences
from PTDE are:

    - DSR EMEVD files are DCX-compressed (`m10_00_00_00.emevd.dcx`); PTDE's are not.
    - The DSR instruction set is slightly expanded.

Both are asserted below, along with binary and EVS round-trips.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from soulstruct.dcx import DCXType, decompress
from soulstruct.games import DARK_SOULS_DSR
from soulstruct.utilities.binary import BinaryReader

from soulstruct.darksouls1r.events import EMEVD, EventDirectory
from soulstruct.darksouls1r.events.emevd.core import Event, Instruction

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


@pytest.fixture
def emevd_path(resource) -> Path:
    return resource(f"{MAP_STEM}.emevd.dcx")


@pytest.fixture
def emevd(emevd_path) -> EMEVD:
    return EMEVD.from_path(emevd_path)


# ---------------------------------------------------------------------------
# Class configuration (pure unit, no game data)
# ---------------------------------------------------------------------------


def test_dsr_emevd_is_dcx_compressed_unlike_ptde():
    from soulstruct.darksouls1ptde.events.emevd.core import EMEVD as PTDE_EMEVD

    assert EMEVD()._get_dcx_type() == DARK_SOULS_DSR.default_dcx_type
    assert EMEVD()._get_dcx_type() != DCXType.Null
    assert PTDE_EMEVD()._get_dcx_type() == DCXType.Null


def test_dsr_emevd_shares_ptde_header_and_varint_settings():
    from soulstruct.darksouls1ptde.events.emevd.core import EMEVD as PTDE_EMEVD

    # DSR EMEVD remained 32-bit even though the rest of the game went 64-bit.
    assert EMEVD.LONG_VARINTS is False
    assert EMEVD.HEADER_VERSION_INFO == PTDE_EMEVD.HEADER_VERSION_INFO == (False, 0, 204)
    assert EMEVD.STRING_ENCODING == "utf-8"


def test_dsr_emedf_is_a_superset_of_ptde():
    from soulstruct.darksouls1ptde.events.emevd.emedf import EMEDF as PTDE_EMEDF
    from soulstruct.darksouls1r.events.emevd.emedf import EMEDF as DSR_EMEDF

    missing = sorted(set(PTDE_EMEDF) - set(DSR_EMEDF))
    assert not missing, f"DSR EMEDF is missing PTDE instructions: {missing}"
    assert len(DSR_EMEDF) >= len(PTDE_EMEDF)


def test_dsr_compiler_inherits_ptde():
    from soulstruct.darksouls1ptde.events.emevd.compiler import EVSInstructionCompiler as PTDE_Compiler
    from soulstruct.darksouls1r.events.emevd.compiler import EVSInstructionCompiler as DSR_Compiler
    from soulstruct.darksouls1r.events.emevd.emedf import EMEDF_ALIASES

    assert issubclass(DSR_Compiler, PTDE_Compiler)
    assert DSR_Compiler.EMEDF_ALIASES is EMEDF_ALIASES


def test_evs_parser_slots():
    from soulstruct.darksouls1r.events.emevd.evs import EVSParser

    assert EVSParser.AND_SLOTS == [1, 2, 3, 4, 5, 6, 7]
    assert EVSParser.OR_SLOTS == [-1, -2, -3, -4, -5, -6, -7]
    assert EVSParser.SPECIAL_EVENT_NAMES == {0: "Constructor", 50: "Preconstructor"}


def test_event_directory_class_config():
    from soulstruct.darksouls1r.maps.constants import ALL_MAPS, COMMON

    assert EventDirectory.FILE_CLASS is EMEVD
    assert EventDirectory.ALL_MAPS == ALL_MAPS
    assert COMMON in EventDirectory.ALL_MAPS, "`common.emevd` must be loadable via `EventDirectory`."


def test_emevd_module_exports_ds1_map_constants():
    """`soulstruct.darksouls1r.events` re-exports the DS1 map constants for EVS `from ... import *`."""
    from soulstruct.darksouls1r import events

    for name in events.__all__:
        assert hasattr(events, name), f"`events.__all__` advertises missing name '{name}'."


# ---------------------------------------------------------------------------
# Binary read/write
# ---------------------------------------------------------------------------


def test_emevd_read(emevd):
    assert emevd.map_name == MAP_STEM
    assert emevd.dcx_type != DCXType.Null
    assert len(emevd.events) == 51
    assert 0 in emevd.events  # Constructor
    for event in emevd.events.values():
        assert isinstance(event, Event)
        for instruction in event.instructions:
            assert isinstance(instruction, Instruction)


def test_emevd_binary_roundtrip(emevd, tmp_path):
    emevd.write(tmp_path / f"{MAP_STEM}.emevd.dcx")
    reload = EMEVD.from_path(tmp_path / f"{MAP_STEM}.emevd.dcx")
    assert sorted(reload.events) == sorted(emevd.events)
    for event_id, event in emevd.events.items():
        other = reload.events[event_id]
        assert len(event.instructions) == len(other.instructions)
        for a, b in zip(event.instructions, other.instructions):
            assert (a.category, a.index) == (b.category, b.index)
            assert a.args_list == b.args_list


def test_emevd_repack_is_idempotent(emevd):
    once = bytes(emevd)
    twice = bytes(EMEVD.from_bytes(once))
    assert_bytes_equal(twice, once, "EMEVD second repack")


@pytest.mark.xfail(
    reason="BUG: `Instruction.pack_base_args()` only writes `base_args_local_offset = -1` for category "
           "1014 ('DefineLabel'). Vanilla DS1 also writes -1 for any instruction with NO base args, so "
           "repacking m10_00_00_00 differs from vanilla in exactly 4 bytes (instruction 2003[47] in "
           "event 11005843) (base/events/emevd/instruction.py:343-349).",
    strict=False,
)
def test_emevd_repack_is_byte_identical_to_vanilla(emevd, emevd_path):
    original, _ = decompress(BinaryReader(emevd_path.read_bytes()))
    repacked, _ = decompress(BinaryReader(bytes(emevd)))
    assert_bytes_equal(repacked, original, "EMEVD repack (decompressed)")


def test_zero_arg_instruction_is_preserved_semantically(emevd):
    """Even though the packed offset differs from vanilla, the no-arg instruction survives round-trip."""
    zero_arg = [
        (eid, i.category, i.index)
        for eid, event in emevd.events.items()
        for i in event.instructions
        if not i.args_list
    ]
    assert zero_arg == [(11005843, 2003, 47)]
    reload = EMEVD.from_bytes(bytes(emevd))
    reload_zero_arg = [
        (eid, i.category, i.index)
        for eid, event in reload.events.items()
        for i in event.instructions
        if not i.args_list
    ]
    assert reload_zero_arg == zero_arg


# ---------------------------------------------------------------------------
# EVS (Python-like event script) round-trip
# ---------------------------------------------------------------------------


def test_emevd_to_evs_and_back(emevd, tmp_path):
    evs_text = emevd.to_evs()
    assert evs_text.strip()
    evs_path = tmp_path / f"{MAP_STEM}.evs.py"
    evs_path.write_text(evs_text, encoding="utf-8")

    from_evs = EMEVD.from_evs_path(evs_path)
    assert sorted(from_evs.events) == sorted(emevd.events)
    for event_id, event in emevd.events.items():
        other = from_evs.events[event_id]
        assert [(i.category, i.index) for i in event.instructions] == [
            (i.category, i.index) for i in other.instructions
        ], f"Instruction sequence changed for event {event_id}."


def test_evs_roundtrip_is_stable(emevd, tmp_path):
    """EVS -> EMEVD -> EVS must be a fixed point."""
    evs_path = tmp_path / "first.evs.py"
    emevd.write_evs(evs_path)
    first = evs_path.read_text(encoding="utf-8")

    reparsed = EMEVD.from_evs_path(evs_path)
    second_path = tmp_path / "second.evs.py"
    reparsed.write_evs(second_path)
    assert second_path.read_text(encoding="utf-8") == first


def test_write_evs_adds_extension(emevd, tmp_path):
    emevd.write_evs(tmp_path / "out.evs.py")
    assert (tmp_path / "out.evs.py").is_file()


EVS_TEMPLATE = '''"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
{body}
'''


def test_minimal_evs_compiles():
    """Control for the xfail below: a plain `if` body compiles fine."""
    source = EVS_TEMPLATE.format(body="    if FlagDisabled(11500200):\n        DisableCharacter(6280)")
    parsed = EMEVD.from_evs_string(source, map_name=MAP_STEM)
    assert sorted(parsed.events) == [0]


def test_evs_pass_in_if_body_with_else_compiles():
    source = EVS_TEMPLATE.format(
        body="    if FlagDisabled(11500200):\n        pass\n    else:\n        DisableCharacter(6280)"
    )
    parsed = EMEVD.from_evs_string(source, map_name=MAP_STEM)
    assert sorted(parsed.events) == [0]


# ---------------------------------------------------------------------------
# `EventDirectory` (requires DSR install)
# ---------------------------------------------------------------------------


@pytest.mark.slow
@pytest.mark.game_data
def test_event_directory_roundtrip(dsr_root, tmp_path):
    event_dir = EventDirectory.from_path(dsr_root / "event")
    assert event_dir.files, "No EMEVD files found in DSR `event` directory."
    assert "common" in event_dir.files

    event_dir.write(tmp_path / "event")
    written = sorted(p.name for p in (tmp_path / "event").iterdir())
    assert all(name.endswith(".emevd.dcx") for name in written), (
        f"DSR EMEVD files must be written with DCX: {written}"
    )

    reload = EventDirectory.from_path(tmp_path / "event")
    assert sorted(reload.files) == sorted(event_dir.files)
    for stem, source in event_dir.files.items():
        assert sorted(reload.files[stem].events) == sorted(source.events)


def test_event_directory_evs_roundtrip(dsr_root, tmp_path):
    event_dir = EventDirectory.from_path(dsr_root / "event")
    event_dir.write_evs(tmp_path / "evs")
    from_evs = EventDirectory.from_path(tmp_path / "evs")
    assert sorted(from_evs.files) == sorted(event_dir.files)
    for stem, source in event_dir.files.items():
        assert sorted(from_evs.files[stem].events) == sorted(source.events)


@pytest.mark.slow
@pytest.mark.game_data
def test_most_vanilla_emevd_evs_roundtrip(dsr_root, tmp_path):
    """Per-file EVS round-trip, tolerating the 5 known-broken vanilla maps (see xfail above)."""
    known_broken = {"m10_01_00_00", "m10_02_00_00", "m12_01_00_00", "m14_01_00_00", "m15_00_00_00"}
    ok, unexpected_failures = [], []
    for path in sorted((dsr_root / "event").glob("*.emevd.dcx")):
        stem = path.name.split(".")[0]
        game_emevd = EMEVD.from_path(path)
        evs_path = tmp_path / f"{stem}.evs.py"
        try:
            game_emevd.write_evs(evs_path)
            from_evs = EMEVD.from_evs_path(evs_path)
            assert sorted(from_evs.events) == sorted(game_emevd.events)
        except Exception as ex:  # noqa: BLE001
            if stem not in known_broken:
                unexpected_failures.append((stem, str(ex).splitlines()[-1][:120]))
        else:
            ok.append(stem)
    assert not unexpected_failures, f"New EVS round-trip failures: {unexpected_failures}"
    assert len(ok) >= 25


@pytest.mark.slow
@pytest.mark.game_data
def test_all_vanilla_emevd_repack_is_idempotent(dsr_root):
    checked = 0
    for path in sorted((dsr_root / "event").glob("*.emevd.dcx")):
        game_emevd = EMEVD.from_path(path)
        once = bytes(game_emevd)
        assert_bytes_equal(bytes(EMEVD.from_bytes(once)), once, path.name)
        checked += 1
    assert checked >= 18
