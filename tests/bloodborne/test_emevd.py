"""Bloodborne EMEVD (event script) tests.

Everything here except the `bb_root` test is a pure-unit test: EVS source text is compiled to an `EMEVD`,
packed to bytes, unpacked again, and decompiled back to EVS. No game files are needed.
"""
from __future__ import annotations

import pytest

from soulstruct.bloodborne.events.emevd import EMEVD
from soulstruct.bloodborne.events.emevd.core import Event, Instruction
from soulstruct.bloodborne.events.emevd.emedf import EMEDF, EMEDF_ALIASES
from soulstruct.bloodborne.events.emevd.evs import EVSParser
from soulstruct.games import BLOODBORNE

MAP_STEM = "m21_00_00_00"


SIMPLE_EVS = '''
from soulstruct.bloodborne.events import *


@ContinueOnRest(0)
def Constructor():
    """Test constructor."""
    RunEvent(11210000, slot=0, args=(11215000,))
    RunEvent(11210001, slot=0, args=(0,))


@RestartOnRest(11210000)
def Event_11210000(_, flag: uint):
    """Enable then disable a flag."""
    IfFlagEnabled(MAIN, flag)
    EnableFlag(11215000)
    Wait(1.0)
    DisableFlag(11215000)


@ContinueOnRest(11210001)
def Event_11210001(_):
    """Condition groups, skips and labels."""
    IfFlagEnabled(AND_1, 11215000)
    IfFlagDisabled(AND_1, 11215001)
    IfConditionTrue(MAIN, AND_1)
    SkipLinesIfFlagEnabled(1, 11215002)
    EnableFlag(11215003)
    DefineLabel(0)
'''


# ---------------------------------------------------------------------------
# Class wiring
# ---------------------------------------------------------------------------


def test_emevd_class_constants():
    """Bloodborne EMEVD: 64-bit ('long varints'), UTF-16-LE strings, header version (False, 0, 204)."""
    assert EMEVD.LONG_VARINTS is True
    assert EMEVD.STRING_ENCODING == "utf-16le"
    assert EMEVD.HEADER_VERSION_INFO == (False, 0, 204)
    assert EMEVD.EVENT_CLASS is Event
    assert EMEVD.EVS_PARSER is EVSParser
    assert Event.INSTRUCTION_CLASS is Instruction
    assert Instruction.EMEDF is EMEDF


def test_emevd_default_dcx_type_is_bloodborne_default():
    """Bloodborne uses `DCX_DFLT_10000_44_9` for every compressed file type."""
    from soulstruct.dcx import DCXType
    from soulstruct.bloodborne.params import GameParamBND
    from soulstruct.bloodborne.text import MSGBND

    assert BLOODBORNE.default_dcx_type == DCXType.DCX_DFLT_10000_44_9
    # `dcx_type` defaults to `None`, which resolves to the game default at pack time.
    assert EMEVD().dcx_type is None
    assert EMEVD()._get_dcx_type() == DCXType.DCX_DFLT_10000_44_9
    assert GameParamBND()._get_dcx_type() == DCXType.DCX_DFLT_10000_44_9
    assert MSGBND()._get_dcx_type() == DCXType.DCX_DFLT_10000_44_9


def test_special_event_names():
    """Bloodborne (unlike DS1) has both a constructor (0) and preconstructor (50)."""
    assert EVSParser.SPECIAL_EVENT_NAMES == {0: "Constructor", 50: "Preconstructor"}


# ---------------------------------------------------------------------------
# EVS -> EMEVD -> bytes -> EMEVD -> EVS
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def compiled_emevd() -> EMEVD:
    return EMEVD.from_evs_string(SIMPLE_EVS, map_name=MAP_STEM)


def test_evs_string_compiles(compiled_emevd):
    assert sorted(compiled_emevd.events) == [0, 11210000, 11210001]


def test_emevd_binary_roundtrip(compiled_emevd, tmp_path):
    """unpack -> pack -> unpack must be byte-stable for EMEVD."""
    packed = bytes(compiled_emevd)
    reloaded = EMEVD.from_bytes(packed)
    assert sorted(reloaded.events) == sorted(compiled_emevd.events)
    repacked = bytes(reloaded)
    assert repacked == packed


def test_emevd_write_read_path(compiled_emevd, tmp_path):
    """`write()` auto-appends '.dcx' because Bloodborne's default DCX type is not `Null`."""
    written = compiled_emevd.write(tmp_path / f"{MAP_STEM}.emevd")
    assert len(written) == 1
    assert written[0].name == f"{MAP_STEM}.emevd.dcx"
    reloaded = EMEVD.from_path(written[0])
    assert sorted(reloaded.events) == sorted(compiled_emevd.events)


def test_emevd_decompiles_to_evs(compiled_emevd):
    evs = compiled_emevd.to_evs()
    assert "from soulstruct.bloodborne.events import *" in evs
    assert "def Constructor():" in evs
    assert "def Event_11210000(" in evs
    # `IfFlagEnabled(MAIN, ...)` should decompile to the higher-level `MAIN.Await(...)` form.
    assert "MAIN.Await(" in evs


def test_evs_decompile_recompile_is_stable(compiled_emevd):
    """Decompiled EVS must recompile to identical EMEVD bytes."""
    evs = compiled_emevd.to_evs()
    recompiled = EMEVD.from_evs_string(evs, map_name=MAP_STEM)
    assert bytes(recompiled) == bytes(compiled_emevd)


def test_numeric_string_roundtrip(compiled_emevd):
    numeric = compiled_emevd.to_numeric()
    reloaded = EMEVD.from_numeric_string(numeric, map_name=MAP_STEM)
    assert bytes(reloaded) == bytes(compiled_emevd)


# ---------------------------------------------------------------------------
# Instruction-level behaviour
# ---------------------------------------------------------------------------


def test_unknown_instruction_raises():
    bad_evs = SIMPLE_EVS.replace("EnableFlag(11215000)", "ThisInstructionDoesNotExist(1)")
    with pytest.raises(Exception):
        EMEVD.from_evs_string(bad_evs, map_name=MAP_STEM)


def test_define_label_rejects_out_of_range():
    bad_evs = SIMPLE_EVS.replace("DefineLabel(0)", "DefineLabel(12)")
    with pytest.raises(Exception):
        EMEVD.from_evs_string(bad_evs, map_name=MAP_STEM)


def test_bloodborne_extends_ptde_instruction_set():
    """Bloodborne's EMEDF is built as `PTDE_EMEDF | {...}`; PTDE IDs must all still be present."""
    from soulstruct.darksouls1ptde.events.emevd.emedf import EMEDF as PTDE_EMEDF

    missing = [key for key in PTDE_EMEDF if key not in EMEDF]
    assert not missing, f"PTDE instruction IDs lost in Bloodborne EMEDF: {missing}"
    assert len(EMEDF) > len(PTDE_EMEDF), "Bloodborne should add instructions on top of PTDE."


def test_bloodborne_only_instructions_present():
    """Spot-check a few Bloodborne-era instruction aliases that DS1 does not have."""
    for alias in ("PlayLogParameterOutput", "StopPlayLogMeasurement", "SetLockedCameraSlot"):
        assert alias in EMEDF_ALIASES, f"Expected Bloodborne alias '{alias}' in EMEDF."


# ---------------------------------------------------------------------------
# Game data (skipped unless Bloodborne is installed)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
@pytest.mark.slow
def test_vanilla_common_emevd_roundtrip(bb_root, tmp_path):
    """Read vanilla `common.emevd.dcx`, repack, and confirm byte stability."""
    from conftest import assert_bytes_equal

    path = bb_root / "event/common.emevd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing vanilla EMEVD: {path}")
    emevd = EMEVD.from_path(path)
    reloaded = EMEVD.from_bytes(bytes(emevd))
    assert sorted(reloaded.events) == sorted(emevd.events)
    assert_bytes_equal(bytes(reloaded), bytes(emevd), "common.emevd repack")
