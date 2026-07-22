"""Tests for DS1 PTDE EMEVD: binary unpack/pack stability, EVS compilation, and EVS round-trips.

The pure-unit tests (EVS string -> numeric) always run. The vanilla-game tests need `ptde_root`.
"""
from __future__ import annotations

import logging

import pytest

from soulstruct.darksouls1ptde.events.emevd import EMEVD
from soulstruct.darksouls1ptde.events.emevd.core import Event, Instruction
from soulstruct.darksouls1ptde.events.emevd.evs import EVSParser
from soulstruct.darksouls1ptde.events.event_directory import EventDirectory
from soulstruct.darksouls1ptde.maps.constants import ALL_MAPS
from soulstruct.dcx import DCXType


# EVS scripts decompiled from these vanilla PTDE maps contain a bare `pass` statement (emitted by
# `adv_decompiler` for an empty `if` block), which `as_event_statement_node` rejects. See report.
EVS_REPARSE_FAILURES = {
    "m10_01_00_00",
    "m10_02_00_00",
    "m14_01_00_00",
    "m15_00_00_00",
}

# EMEVDs where the EVS round-trip legitimately *optimises* the instruction stream, e.g. collapsing
# `SkipLinesIfFlagEnabled(1, ...) + End()` into `EndIfFlagDisabled(...)`. Packed bytes therefore
# differ from vanilla, but the result is semantically equivalent and is an EVS fixpoint.
EVS_ROUND_TRIP_OPTIMISED = {
    "m12_01_00_00",
    "m14_00_00_00",
}


SIMPLE_EVS = '''
from soulstruct.darksouls1ptde.events import *


@ContinueOnRest(0)
def Constructor():
    RunEvent(11000000)
    RunEvent(11000001, slot=0, args=(1000, 2000))


@RestartOnRest(11000000)
def Event_11000000():
    """Docstring."""
    IfFlagEnabled(AND_1, 100)
    IfCharacterDead(AND_1, 1000000)
    IfConditionTrue(MAIN, AND_1)
    EnableFlag(101)
    DisableFlag(102)
    Wait(1.0)


@RestartOnRest(11000001)
def Event_11000001(_, character: int, region: int):
    IfCharacterInsideRegion(AND_1, character, region)
    IfConditionTrue(MAIN, AND_1)
    Move(character, destination=region, destination_type=CoordEntityType.Region)
'''


# ---------------------------------------------------------------------------
# Pure-unit: class configuration
# ---------------------------------------------------------------------------


def test_ptde_emevd_class_configuration():
    """PTDE is uncompressed: EMEVD must resolve to a `Null` DCX type (DSR uses DCX)."""
    from soulstruct.games import DARK_SOULS_PTDE

    assert DARK_SOULS_PTDE.default_dcx_type == DCXType.Null
    # PTDE `EMEVD` leaves `dcx_type` as `None`, which resolves to the game default when packing.
    assert EMEVD()._get_dcx_type() == DCXType.Null
    assert EMEVD.STRING_ENCODING == "utf-8"
    assert EMEVD.LONG_VARINTS is False
    assert EMEVD.HEADER_VERSION_INFO == (False, 0, 204)
    assert EMEVD.EVENT_CLASS is Event
    assert EMEVD.EVS_PARSER is EVSParser
    assert Event.INSTRUCTION_CLASS is Instruction


def test_evs_parser_condition_slots():
    """DS1 has 7 AND and 7 OR condition groups (`MAIN` is 0)."""
    assert EVSParser.AND_SLOTS == [1, 2, 3, 4, 5, 6, 7]
    assert EVSParser.OR_SLOTS == [-1, -2, -3, -4, -5, -6, -7]
    assert EVSParser.SPECIAL_EVENT_NAMES == {0: "Constructor", 50: "Preconstructor"}


def test_event_directory_configuration():
    assert EventDirectory.FILE_CLASS is EMEVD
    assert set(EventDirectory.ALL_MAPS) == set(ALL_MAPS)
    # `EventDirectory` keys by EMEVD stem, which is what all `map_property` getters use.
    assert EventDirectory.MAP_STEM_ATTRIBUTE == "emevd_file_stem"


# ---------------------------------------------------------------------------
# Pure-unit: EVS compilation
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def simple_emevd() -> EMEVD:
    return EMEVD.from_evs_string(SIMPLE_EVS, map_name="m10_00_00_00")


def test_evs_string_compiles(simple_emevd):
    assert set(simple_emevd.events) == {0, 11000000, 11000001}


def test_evs_numeric_output(simple_emevd):
    numeric = simple_emevd.to_numeric()
    # Constructor calls both events (2000[00] == `RunEvent`).
    assert "2000[00] (iII)[0, 11000000, 0]" in numeric
    assert "2000[00] (iIi|i)[0, 11000001, 1000, 2000]" in numeric
    # `EnableFlag(101)` / `DisableFlag(102)` are partials of (2003, 2).
    assert "2003[02] (iB)[101, 1]" in numeric
    assert "2003[02] (iB)[102, 0]" in numeric
    # `Wait(1.0)` is (1001, 0).
    assert "1001[00] (f)[1.0]" in numeric


def test_evs_binary_round_trip(simple_emevd, tmp_path):
    """EVS -> EMEVD -> bytes -> EMEVD must be numerically identical."""
    path = tmp_path / "m10_00_00_00.emevd"
    simple_emevd.write(path)
    assert path.is_file()
    reloaded = EMEVD.from_path(path)
    assert reloaded.to_numeric() == simple_emevd.to_numeric()
    assert bytes(reloaded) == bytes(simple_emevd)


def test_numeric_round_trip(simple_emevd):
    reloaded = EMEVD.from_numeric_string(simple_emevd.to_numeric(), map_name="m10_00_00_00")
    assert reloaded.to_numeric() == simple_emevd.to_numeric()


def test_evs_round_trip_of_own_output(simple_emevd):
    """Decompiling our own compiled script and recompiling must be stable."""
    evs = simple_emevd.to_evs()
    recompiled = EMEVD.from_evs_string(evs, map_name="m10_00_00_00")
    assert bytes(recompiled) == bytes(simple_emevd)


def test_evs_bad_keyword_is_rejected():
    from soulstruct.base.events.emevd.exceptions import EMEVDError

    bad = SIMPLE_EVS.replace("EnableFlag(101)", "EnableFlag(flag=101, nonsense=1)")
    with pytest.raises(EMEVDError):
        EMEVD.from_evs_string(bad, map_name="m10_00_00_00")


@pytest.mark.xfail(
    reason=(
        "`EVSInstructionCompiler._base_compile()` silently discards surplus POSITIONAL arguments "
        "(only surplus keyword arguments raise), so typos like `EnableFlag(101, 202)` compile."
    ),
    strict=False,
)
def test_evs_surplus_positional_args_are_rejected():
    from soulstruct.base.events.emevd.exceptions import EMEVDError

    bad = SIMPLE_EVS.replace("EnableFlag(101)", "EnableFlag(101, 202, 303)")
    with pytest.raises(EMEVDError):
        EMEVD.from_evs_string(bad, map_name="m10_00_00_00")


def test_unknown_instruction_is_rejected():
    from soulstruct.base.events.emevd.exceptions import EMEVDError

    bad = SIMPLE_EVS.replace("EnableFlag(101)", "ThisInstructionDoesNotExist(101)")
    with pytest.raises(EMEVDError):
        EMEVD.from_evs_string(bad, map_name="m10_00_00_00")


# ---------------------------------------------------------------------------
# Vanilla game data
# ---------------------------------------------------------------------------


def _vanilla_emevd_paths(ptde_root):
    return sorted((ptde_root / "event").glob("*.emevd"))


@pytest.fixture(scope="module")
def emevd_stems(ptde_root):
    return [p.stem for p in _vanilla_emevd_paths(ptde_root)]


def test_vanilla_event_directory_loads(ptde_root):
    directory = EventDirectory.from_path(ptde_root / "event")
    # Every `Map` in `ALL_MAPS` should have an EMEVD file.
    for game_map in ALL_MAPS:
        assert game_map.emevd_file_stem in directory.files, (
            f"Missing EMEVD for {game_map.name} ({game_map.emevd_file_stem})."
        )
    assert directory.Common is directory.files["common"]
    assert directory.UndeadBurg is directory.files["m10_01_00_00"]


@pytest.mark.slow
def test_vanilla_emevd_binary_round_trip(ptde_root, tmp_path):
    """unpack -> pack -> unpack must be byte-stable for every vanilla PTDE EMEVD."""
    for path in _vanilla_emevd_paths(ptde_root):
        emevd = EMEVD.from_path(path)
        assert emevd.dcx_type == DCXType.Null, f"{path.name} should be uncompressed in PTDE."
        packed = bytes(emevd)
        out_path = tmp_path / path.name
        emevd.write(out_path)
        reloaded = EMEVD.from_path(out_path)
        assert bytes(reloaded) == packed, f"{path.name}: repack not stable."
        assert reloaded.to_numeric() == emevd.to_numeric(), f"{path.name}: numeric not stable."


@pytest.mark.slow
def test_vanilla_emevd_numeric_round_trip(ptde_root):
    for path in _vanilla_emevd_paths(ptde_root):
        emevd = EMEVD.from_path(path)
        reloaded = EMEVD.from_numeric_string(emevd.to_numeric(), map_name=path.stem)
        assert reloaded.to_numeric() == emevd.to_numeric(), f"{path.name}: numeric round-trip failed."


@pytest.mark.slow
def test_vanilla_emevd_decompiles_to_evs(ptde_root, caplog):
    """Every vanilla EMEVD must decompile to a non-trivial EVS script without raising."""
    with caplog.at_level(logging.CRITICAL):
        for path in _vanilla_emevd_paths(ptde_root):
            emevd = EMEVD.from_path(path)
            evs = emevd.to_evs()
            assert "from soulstruct.darksouls1ptde.events import *" in evs
            assert len(evs.splitlines()) > 5, f"{path.name}: suspiciously short EVS output."


@pytest.mark.slow
def test_vanilla_emevd_evs_round_trip(ptde_root, caplog):
    """EMEVD -> EVS -> EMEVD must produce identical packed bytes, and EVS must be a fixpoint.

    The fixpoint check (`to_evs()` of the recompiled EMEVD equals the original EVS) is the strongest
    invariant that holds universally: the decompiler legitimately *optimises* a couple of vanilla
    maps by collapsing `SkipLinesIf<test>(1, ...) + End()` into `EndIf<not test>(...)`, so their
    packed bytes differ (see `EVS_ROUND_TRIP_OPTIMISED`).
    """
    failures = []
    with caplog.at_level(logging.CRITICAL):
        for path in _vanilla_emevd_paths(ptde_root):
            if path.stem in EVS_REPARSE_FAILURES:
                continue  # covered by dedicated xfail test below
            emevd = EMEVD.from_path(path)
            packed = bytes(emevd)
            try:
                evs = emevd.to_evs()
                recompiled = EMEVD.from_evs_string(evs, map_name=path.stem)
            except Exception as ex:  # noqa: BLE001
                failures.append(f"{path.name}: {type(ex).__name__}: {str(ex)[:120]}")
                continue
            if recompiled.to_evs() != evs:
                failures.append(f"{path.name}: EVS decompilation is not a fixpoint.")
            expect_same_bytes = path.stem not in EVS_ROUND_TRIP_OPTIMISED
            if expect_same_bytes and bytes(recompiled) != packed:
                failures.append(f"{path.name}: EVS round-trip changed packed bytes.")
            if not expect_same_bytes and bytes(recompiled) == packed:
                failures.append(
                    f"{path.name}: expected byte difference (stale `EVS_ROUND_TRIP_OPTIMISED` entry)."
                )
    assert not failures, "EVS round-trip failures:\n  " + "\n  ".join(failures)


@pytest.mark.slow
@pytest.mark.xfail(
    reason=(
        "`adv_decompiler` emits a bare `pass` for empty `if` blocks, but `as_event_statement_node` "
        "does not accept `ast.Pass`, so the decompiled EVS cannot be recompiled."
    ),
    strict=False,
)
@pytest.mark.parametrize("stem", sorted(EVS_REPARSE_FAILURES))
def test_vanilla_emevd_evs_round_trip_pass_statement_bug(ptde_root, stem, caplog):
    path = ptde_root / "event" / f"{stem}.emevd"
    if not path.is_file():
        pytest.skip(f"Missing vanilla EMEVD: {path}")
    with caplog.at_level(logging.CRITICAL):
        emevd = EMEVD.from_path(path)
        evs = emevd.to_evs()
        assert "\n        pass\n" in evs or "\n    pass\n" in evs, (
            f"{stem} no longer contains a bare `pass`; the xfail list may be stale."
        )
        recompiled = EMEVD.from_evs_string(evs, map_name=stem)
    assert bytes(recompiled) == bytes(emevd)


def test_vanilla_common_emevd_has_expected_events(ptde_root):
    emevd = EMEVD.from_path(ptde_root / "event" / "common.emevd")
    assert 0 in emevd.events, "`common.emevd` must have a Constructor event (ID 0)."
    assert len(emevd.events) > 10
