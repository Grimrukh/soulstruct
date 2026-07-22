"""Dark Souls III EMEVD / EVS tests.

Most tests here are pure-unit (no game data). The final section round-trips real `common_func` and
map EMEVD files if a DS3 installation is configured (`ds3_root` fixture), and is skipped otherwise.
"""
from __future__ import annotations

import inspect

import pytest

from soulstruct.base.events.evs.conditions import EVSConditionManager
from soulstruct.darksouls3.events.emevd import EMEVD
from soulstruct.darksouls3.events.emevd.core import Event, Instruction
from soulstruct.darksouls3.events.emevd.compiler import EVSInstructionCompiler
from soulstruct.darksouls3.events.emevd.emedf import EMEDF, EMEDF_ALIASES
from soulstruct.darksouls3.events.emevd.evs import EVSParser
from soulstruct.darksouls3.events.enums import ConditionGroup, ItemType


@pytest.fixture
def compiler() -> EVSInstructionCompiler:
    cond_manager = EVSConditionManager(EVSParser.OR_SLOTS, EVSParser.AND_SLOTS)
    return EVSInstructionCompiler(cond_manager)


# ---------------------------------------------------------------------------
# Class configuration
# ---------------------------------------------------------------------------


def test_emevd_class_configuration():
    assert EMEVD.EVENT_CLASS is Event
    assert Event.INSTRUCTION_CLASS is Instruction
    assert EMEVD.EVS_PARSER is EVSParser
    assert EMEVD.STRING_ENCODING == "utf-16le"
    assert EMEVD.LONG_VARINTS is True
    # (has_header, unknown, version): DS3 EMEVD header version.
    assert EMEVD.HEADER_VERSION_INFO == (True, 0, 205)


def test_instruction_class_uses_ds3_emedf():
    assert Instruction.EMEDF is EMEDF
    from soulstruct.darksouls3.events.emevd.decompiler import DECOMPILER, OPT_ARGS_DECOMPILER

    assert Instruction.DECOMPILER is DECOMPILER
    assert Instruction.OPT_ARGS_DECOMPILER is OPT_ARGS_DECOMPILER


def test_evs_parser_configuration():
    assert EVSParser.SUPPORTS_COMMON_FUNC is True
    assert EVSParser.COMPILER_CLASS is EVSInstructionCompiler
    # Condition slots must be disjoint, non-zero and sorted away from `MAIN`.
    assert set(EVSParser.OR_SLOTS).isdisjoint(EVSParser.AND_SLOTS)
    assert all(slot < 0 for slot in EVSParser.OR_SLOTS)
    assert all(slot > 0 for slot in EVSParser.AND_SLOTS)
    assert len(EVSParser.OR_SLOTS) == len(EVSParser.AND_SLOTS) == 15
    assert EVSParser.SPECIAL_EVENT_NAMES == {0: "Constructor", 50: "Preconstructor"}


def test_condition_group_enum_covers_evs_slots():
    """Every EVS condition slot must exist in the DS3 `ConditionGroup` enum."""
    values = {int(member) for member in ConditionGroup}
    for slot in (*EVSParser.OR_SLOTS, *EVSParser.AND_SLOTS, 0):
        assert slot in values, f"Condition slot {slot} missing from `ConditionGroup`."


def test_emevd_empty_binary_roundtrip(tmp_path):
    emevd = EMEVD()
    packed = bytes(emevd)
    reloaded = EMEVD.from_bytes(packed)
    assert reloaded.events == {}
    assert bytes(reloaded) == packed


# ---------------------------------------------------------------------------
# Compiler behaviour (pure unit)
# ---------------------------------------------------------------------------


def test_custom_instruction_registry_is_populated():
    names = EVSInstructionCompiler._CUSTOM_FUNC_NAMES
    assert "Move" in names
    assert "PlayCutscene" in names
    assert "IfActionButton" in names
    assert "RunEvent" in names and "RunCommonEvent" in names
    # Every registered name must actually be a capitalised method on the class.
    for name in names:
        assert name[0].isupper()
        assert callable(getattr(EVSInstructionCompiler, name))


def test_custom_condition_arg_indices_match_signatures():
    """`_CUSTOM_FUNC_CONDITION_ARGS` records the positional index of `condition`/`input_condition`."""
    for name, (cond_index, input_index) in EVSInstructionCompiler._CUSTOM_FUNC_CONDITION_ARGS.items():
        params = list(inspect.signature(getattr(EVSInstructionCompiler, name)).parameters)[1:]  # drop `self`
        if cond_index is None:
            assert "condition" not in params, name
        else:
            assert params[cond_index] == "condition", name
        if input_index is None:
            assert "input_condition" not in params, name
        else:
            assert params[input_index] == "input_condition", name


def test_base_compile_simple_instruction(compiler):
    lines = compiler.compile("EnableFlag", 11000000)
    assert len(lines) == 1
    assert "2003[02]" in lines[0]
    assert "11000000" in lines[0]


def test_partial_instruction_bakes_kwargs(compiler):
    """`EnableTreasure`/`DisableTreasure` are partials of `SetTreasureState` (2005, 4)."""
    enabled = compiler.compile("EnableTreasure", 1000)[0]
    disabled = compiler.compile("DisableTreasure", 1000)[0]
    assert "2005[04]" in enabled and "2005[04]" in disabled
    assert enabled != disabled


def test_award_item_lot_wrapper_selects_host_only(compiler):
    host_only = compiler.compile("AwardItemLot", 60000, host_only=True)[0]
    all_players = compiler.compile("AwardItemLot", 60000, host_only=False)[0]
    assert host_only != all_players
    assert host_only == compiler.compile("AwardItemLotToHostOnly", 60000)[0]
    assert all_players == compiler.compile("AwardItemLotToAllPlayers", 60000)[0]


def test_define_label_wrapper_range(compiler):
    assert compiler.compile("DefineLabel", 0) == compiler.compile("DefineLabel_0")
    assert compiler.compile("DefineLabel", 20) == compiler.compile("DefineLabel_20")
    with pytest.raises(ValueError):
        compiler.compile("DefineLabel", 21)
    with pytest.raises(ValueError):
        compiler.compile("DefineLabel", -1)


def test_if_player_item_state_partials_agree(compiler):
    explicit = compiler.compile("IfPlayerItemState", 1, True, 12345, ItemType.Weapon)
    partial = compiler.compile("IfPlayerHasWeapon", 1, 12345)
    assert explicit == partial


def test_run_event_arg_types_prefix(compiler):
    """`RunEvent` prepends 'iI' for the (slot, event_id) args it always packs."""
    line = compiler.compile("RunEvent", 11000000, slot=0, args=(1000, 2000), arg_types="ii")[0]
    assert "2000[00]" in line
    assert "iIi|i" in line


def test_unknown_instruction_raises(compiler):
    with pytest.raises(ValueError, match="not found in EMEDF"):
        compiler.compile("ThisInstructionDoesNotExist")


def test_base_compile_rejects_unknown_keyword(compiler):
    with pytest.raises(ValueError, match="Invalid keyword argument"):
        compiler.compile("EnableFlag", flag=11000000, nonsense=1)


@pytest.mark.xfail(
    reason="BUG: DS3 EMEDF `RunCommonEvent` (2000, 6) has no `slot` argument (correctly -- the DS3 "
           "instruction takes only `event_id` + args), but `EVSInstructionCompiler.RunCommonEvent` "
           "was copy-pasted from Elden Ring and unconditionally forwards `slot=slot` to "
           "`_base_compile`, which raises `ValueError`. This breaks EVS compilation of ANY DS3 "
           "script that calls a `common_func` event (darksouls3/events/emevd/compiler.py:67-69).",
    strict=False,
)
def test_run_common_event_compiles(compiler):
    line = compiler.compile("RunCommonEvent", 20005110, args=(1000, 2000), arg_types="ii")[0]
    assert "2000[06]" in line


@pytest.mark.xfail(
    reason="Same root cause as `test_run_common_event_compiles`: the `slot` kwarg is rejected by "
           "`_base_compile` because DS3 EMEDF (2000, 6) has no `slot` arg.",
    strict=False,
)
def test_run_common_event_no_args_compiles(compiler):
    """This is the exact call the EVS parser makes for a bare `CommonFunc_XXX()` call."""
    line = compiler.compile("RunCommonEvent", 20005110, args=(0,), arg_types=None)[0]
    assert "2000[06]" in line


@pytest.mark.xfail(
    reason="Even if `slot` were accepted, `RunCommonEvent` builds `full_arg_types = 'iI' + ...`, "
           "which is the (slot, event_id) prefix of `RunEvent`. DS3's instruction packs only "
           "`event_id`, so the prefix should be 'I' (darksouls3/events/emevd/compiler.py:64).",
    strict=False,
)
def test_run_common_event_arg_types_prefix(compiler):
    line = compiler.compile("RunCommonEvent", 20005110, args=(1000,), arg_types="i")[0]
    assert "(Ii)" in line or "Ii" in line.split("(")[1].split(")")[0]


# ---------------------------------------------------------------------------
# Game-data round-trips (skipped without a DS3 installation)
# ---------------------------------------------------------------------------


@pytest.mark.game_data
def test_common_func_emevd_binary_roundtrip(ds3_root, tmp_path):
    from conftest import binary_roundtrip

    path = ds3_root / "event/common_func.emevd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing DS3 EMEVD: {path}")
    emevd = EMEVD.from_path(path)
    assert emevd.events
    reloaded = binary_roundtrip(emevd, tmp_path, "common_func.emevd.dcx")
    assert set(reloaded.events) == set(emevd.events)


@pytest.mark.slow
@pytest.mark.game_data
def test_all_emevd_binary_roundtrip(ds3_root, tmp_path):
    from conftest import binary_roundtrip

    event_dir = ds3_root / "event"
    if not event_dir.is_dir():
        pytest.skip(f"Missing DS3 event directory: {event_dir}")
    paths = sorted(event_dir.glob("*.emevd.dcx"))
    if not paths:
        pytest.skip("No DS3 EMEVD files found.")
    for path in paths:
        emevd = EMEVD.from_path(path)
        reloaded = binary_roundtrip(emevd, tmp_path, path.name)
        assert set(reloaded.events) == set(emevd.events), path.name


@pytest.mark.slow
@pytest.mark.game_data
def test_emevd_evs_decompile_and_recompile(ds3_root, tmp_path):
    """Full EVS round-trip: EMEVD -> EVS text -> EMEVD.

    This is the test that exercises the `RunCommonEvent` compiler bug on real data.
    """
    path = ds3_root / "event/m30_00_00_00.emevd.dcx"
    if not path.is_file():
        pytest.skip(f"Missing DS3 EMEVD: {path}")
    emevd = EMEVD.from_path(path)
    evs_path = tmp_path / "m30_00_00_00.evs.py"
    emevd.write_evs(evs_path)
    recompiled = EMEVD.from_evs_path(evs_path)
    assert set(recompiled.events) == set(emevd.events)


def test_emedf_alias_count_is_stable():
    """Sanity floor so an accidentally-truncated EMEDF is caught immediately."""
    assert len(EMEDF) > 300
    assert len(EMEDF_ALIASES) > 600
