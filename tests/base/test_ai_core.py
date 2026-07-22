"""Tests for `soulstruct.base.ai`: `LuaBND`, `LuaInfo`, `LuaGNL` and the goal/script model.

Lua compilation/decompilation itself shells out to bundled binaries and is not exercised here.
"""
from __future__ import annotations

import logging
from pathlib import Path

import pytest

from soulstruct.base.ai.lua import LuaError
from soulstruct.base.ai.lua_scripts import GoalType, LuaGoalScript, LuaUnknownScript
from soulstruct.base.ai.luagnl import LuaGNL
from soulstruct.base.ai.luainfo import LuaInfo, LuaInfoStruct
from soulstruct.base.ai.luabnd import LuaBND, DS1_GOALS_WITH_NO_SCRIPT
from soulstruct.utilities.binary import ByteOrder


# ---------------------------------------------------------------------------
# GoalType
# ---------------------------------------------------------------------------


def test_goal_type_values():
    assert GoalType.Battle == "battle"
    assert GoalType.Logic == "logic"
    assert GoalType.Unknown == "unknown"
    assert GoalType("battle") is GoalType.Battle


@pytest.mark.parametrize(
    "battle, logic, name, expected",
    [
        (True, False, "", GoalType.Battle),
        (False, True, "Foo_Interupt", GoalType.Logic),
        (False, False, "", GoalType.Unknown),
    ],
)
def test_goal_type_from_interrupt_info(battle, logic, name, expected):
    assert GoalType.from_interrupt_info(battle, logic, name) is expected


@pytest.mark.parametrize(
    "battle, logic, name",
    [(True, True, ""), (True, False, "Foo_Interupt"), (False, True, ""), (False, False, "Foo")],
)
def test_goal_type_from_interrupt_info_rejects_invalid(battle, logic, name):
    with pytest.raises(LuaError):
        GoalType.from_interrupt_info(battle, logic, name)


# ---------------------------------------------------------------------------
# LuaGoalScript / LuaUnknownScript
# ---------------------------------------------------------------------------


def test_goal_auto_script_name():
    assert LuaGoalScript(goal_id=1234, goal_name="X1234Battle", goal_type=GoalType.Battle).script_name == (
        "001234_battle.lua"
    )
    assert LuaGoalScript(goal_id=1234, goal_name="X1234_Logic", goal_type=GoalType.Logic).script_name == (
        "001234_logic.lua"
    )
    unknown = LuaGoalScript(goal_id=1, goal_name="CrystalLizardRunaway", goal_type=GoalType.Unknown)
    assert unknown.script_name == "crystal_lizard_runaway.lua"


def test_goal_explicit_script_name_is_kept():
    goal = LuaGoalScript(goal_id=1, goal_name="X", goal_type=GoalType.Battle, script_name="custom.lua")
    assert goal.script_name == "custom.lua"


def test_goal_interrupt_details():
    battle = LuaGoalScript(goal_id=1, goal_name="XBattle", goal_type=GoalType.Battle)
    assert battle.get_interrupt_details() == {
        "has_battle_interrupt": True, "has_logic_interrupt": False, "logic_interrupt_name": "",
    }
    logic = LuaGoalScript(goal_id=1, goal_name="X_Logic", goal_type=GoalType.Logic)
    assert logic.get_interrupt_details() == {
        "has_battle_interrupt": False, "has_logic_interrupt": True, "logic_interrupt_name": "X_Interupt",
    }
    unknown = LuaGoalScript(goal_id=1, goal_name="X", goal_type=GoalType.Unknown)
    assert unknown.get_interrupt_details()["logic_interrupt_name"] == ""


def test_goal_logic_name_must_end_in_logic():
    goal = LuaGoalScript(goal_id=1, goal_name="Bad", goal_type=GoalType.Logic, script_name="x.lua")
    with pytest.raises(LuaError):
        goal.get_interrupt_details()
    with pytest.raises(LuaError):
        goal.validate_goal_name()


def test_goal_validate_warns_for_odd_battle_name(caplog):
    goal = LuaGoalScript(goal_id=1, goal_name="Odd", goal_type=GoalType.Battle)
    with caplog.at_level(logging.WARNING):
        goal.validate_goal_name()
    assert any("does not end in 'Battle'" in r.message for r in caplog.records)


def test_goal_repr():
    goal = LuaGoalScript(goal_id=12, goal_name="XBattle", goal_type=GoalType.Battle)
    assert repr(goal) == "LuaGoal(000012, 'XBattle', <GoalType.Battle: 'battle'>)"


def test_goal_copy_is_deep():
    goal = LuaGoalScript(goal_id=1, goal_name="XBattle", goal_type=GoalType.Battle, script="print('x')")
    other = goal.copy()
    other.script = "changed"
    assert goal.script == "print('x')"


def test_script_write_and_load(tmp_path):
    goal = LuaGoalScript(goal_id=1, goal_name="XBattle", goal_type=GoalType.Battle, script="-- lua\n")
    goal.write_script(tmp_path / "x.lua")
    assert (tmp_path / "x.lua").read_text(encoding="shift_jis_2004") == "-- lua\n"
    goal.script = ""
    goal.load_script(tmp_path / "x.lua")
    assert goal.script == "-- lua\n"


def test_script_write_errors_when_empty(tmp_path):
    goal = LuaGoalScript(goal_id=1, goal_name="XBattle", goal_type=GoalType.Battle)
    with pytest.raises(LuaError):
        goal.write_script(tmp_path / "x.lua")
    with pytest.raises(LuaError):
        goal.write_bytecode(tmp_path / "x.lua")


def test_bytecode_write(tmp_path):
    goal = LuaGoalScript(
        goal_id=1, goal_name="XBattle", goal_type=GoalType.Battle, bytecode=b"\x1bLua"
    )
    goal.write_bytecode(tmp_path / "x.lua")
    assert (tmp_path / "x.lua").read_bytes() == b"\x1bLua"


def test_lua_unknown_script():
    other = LuaUnknownScript(name="common")
    assert other.script_name == "common.lua"
    assert repr(other) == "LuaUnknownScript(name='common')"
    assert not hasattr(other, "goal_name")  # see M12


def test_ds1_goals_with_no_script_table():
    assert "Default_Logic" in DS1_GOALS_WITH_NO_SCRIPT
    assert isinstance(DS1_GOALS_WITH_NO_SCRIPT, tuple)


# ---------------------------------------------------------------------------
# LuaGNL / LuaInfo (pure unit)
# ---------------------------------------------------------------------------


def test_luagnl_defaults():
    gnl = LuaGNL()
    assert gnl.names == []
    assert gnl.byte_order is ByteOrder.LittleEndian
    assert gnl.long_varints is False


@pytest.mark.parametrize("long_varints, expected", [(False, "shift_jis_2004"), (True, "utf-16-le")])
def test_luagnl_encoding(long_varints, expected):
    assert LuaGNL.get_encoding(ByteOrder.LittleEndian, long_varints) == expected


def test_luainfo_encoding():
    assert LuaInfo.get_encoding(ByteOrder.LittleEndian, False) == "shift_jis_2004"
    assert LuaInfo.get_encoding(ByteOrder.LittleEndian, True) == "utf-16-le"
    assert LuaInfo.get_encoding(ByteOrder.BigEndian, True) == "utf-16-be"


def test_luainfo_struct_signature():
    # `lua_version` and `endian_one` are asserted/`init=False`; only `goal_count` is settable.
    data = bytes(LuaInfoStruct(goal_count=0).to_writer())
    assert len(data) == 16
    assert data.startswith(b"LUAI")


@pytest.mark.xfail(
    reason="M13: `LuaInfo.get_long_varints()` logs 'Defaulting to 8' for a zero goal count but then "
           "falls off the end of the function and returns `None`.",
    strict=False,
)
def test_luainfo_get_long_varints_zero_goals(caplog):
    from soulstruct.utilities.binary import BinaryReader

    with caplog.at_level(logging.WARNING):
        result = LuaInfo.get_long_varints(BinaryReader(b"\0" * 64), 0)
    assert result is True


@pytest.mark.xfail(
    reason="H6: `LuaGNL.to_writer()` does `for i, name in self.names`, unpacking each `str`.",
    strict=False,
)
def test_luagnl_binary_roundtrip():
    gnl = LuaGNL(names=["Foo_Activate", "Foo_Update"])
    reloaded = LuaGNL.from_bytes(bytes(gnl))
    assert reloaded.names == gnl.names


@pytest.mark.xfail(
    reason="H7: `LuaGoalScript.pack_logic_interrupt_name()` fills 'logic_interrupt_name' but the "
           "struct field is 'logic_interrupt_name_offset'; goal name strings are never packed either.",
    strict=False,
)
def test_luainfo_binary_roundtrip():
    goals = [
        LuaGoalScript(goal_id=1, goal_name="AlphaBattle", goal_type=GoalType.Battle),
        LuaGoalScript(goal_id=2, goal_name="Beta_Logic", goal_type=GoalType.Logic),
    ]
    info = LuaInfo(goals=goals)
    reloaded = LuaInfo.from_bytes(bytes(info))
    assert [(g.goal_id, g.goal_name, g.goal_type) for g in reloaded.goals] == [
        (1, "AlphaBattle", GoalType.Battle), (2, "Beta_Logic", GoalType.Logic)
    ]


# ---------------------------------------------------------------------------
# Real DSR `LuaBND`
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def dsr_luabnd_path() -> Path:
    from soulstruct.config import Config

    root = Config.DSR_PATH
    if not root:
        pytest.skip("DSR directory not found (set Config.DSR_PATH to run).")
    path = Path(root) / "script" / "m10_00_00_00.luabnd.dcx"
    if not path.is_file():
        pytest.skip(f"DSR AI script not found: {path}")
    return path


@pytest.fixture(scope="module")
def dsr_luabnd(dsr_luabnd_path):
    logging.disable(logging.WARNING)
    try:
        return LuaBND.from_path(dsr_luabnd_path)
    finally:
        logging.disable(logging.NOTSET)


def test_luabnd_loads_goals(dsr_luabnd):
    assert len(dsr_luabnd.goals) > 5
    assert all(isinstance(g, LuaGoalScript) for g in dsr_luabnd.goals)
    assert all(g.goal_type in (GoalType.Battle, GoalType.Logic, GoalType.Unknown) for g in dsr_luabnd.goals)
    assert "LuaBND" in repr(dsr_luabnd)


def test_luabnd_goals_have_bytecode(dsr_luabnd):
    with_code = [g for g in dsr_luabnd.goals if g.bytecode]
    assert with_code, "expected at least one goal with compiled bytecode"
    assert all(g.bytecode.startswith(b"\x1bLua") for g in with_code)


def test_luabnd_get_goal(dsr_luabnd):
    goal = dsr_luabnd.goals[0]
    assert dsr_luabnd.get_goal(goal.goal_id, goal.goal_type) is goal
    assert dsr_luabnd.get_goal_index(goal.goal_id, goal.goal_type) == 0
    with pytest.raises(KeyError):
        dsr_luabnd.get_goal(-12345, GoalType.Battle)
    goal_dict = dsr_luabnd.get_goal_dict()
    assert goal_dict[(goal.goal_id, goal.goal_type)] is goal


def test_luabnd_sort_goals(dsr_luabnd_path):
    logging.disable(logging.WARNING)
    try:
        luabnd = LuaBND.from_path(dsr_luabnd_path)
    finally:
        logging.disable(logging.NOTSET)
    luabnd.sort_goals()
    ids = [(g.goal_id, g.goal_type) for g in luabnd.goals]
    assert ids == sorted(ids)
    luabnd.sort_goals(key=lambda g: -g.goal_id)
    assert [g.goal_id for g in luabnd.goals] == sorted((g.goal_id for g in luabnd.goals), reverse=True)


def test_luabnd_get_all_script_names(dsr_luabnd):
    names = dsr_luabnd.get_all_script_names()
    assert names
    assert all(n.endswith(".lua") for n in names)


def test_luabnd_gnl_names(dsr_luabnd):
    names = dsr_luabnd.get_gnl_names()
    assert names, "expected LuaGNL global function names"
    assert all(isinstance(n, str) for n in names)
    # Goal activation functions should be registered.
    assert any(n.endswith("_Activate") for n in names)


def test_luainfo_reads_from_real_luabnd(dsr_luabnd):
    info = dsr_luabnd.find_entry_by_id(1000001).to_binary_file(LuaInfo)
    assert len(info.goals) == len(dsr_luabnd.goals)
    assert info.long_varints is False  # DSR LuaInfo files are 32-bit (inherited from PTDE)
    assert info.byte_order is ByteOrder.LittleEndian


def test_luagnl_reads_from_real_luabnd(dsr_luabnd):
    gnl = dsr_luabnd.find_entry_by_id(1000000).to_binary_file(LuaGNL)
    assert len(gnl.names) > 10
    assert all(isinstance(n, str) and n for n in gnl.names)


def test_luabnd_write_all_compiled_scripts(dsr_luabnd, tmp_path):
    goals_with_code = [g for g in dsr_luabnd.goals if g.bytecode]
    for goal in goals_with_code[:3]:
        goal.write_bytecode(tmp_path / goal.script_name)
        assert (tmp_path / goal.script_name).read_bytes() == goal.bytecode


def test_luabnd_decompile_all_rejects_lua32(dsr_luabnd_path):
    logging.disable(logging.WARNING)
    try:
        luabnd = LuaBND.from_path(dsr_luabnd_path)
    finally:
        logging.disable(logging.NOTSET)
    luabnd.is_lua_32 = True
    with pytest.raises(ValueError):
        luabnd.decompile_all()


def test_goal_name_regex_patterns():
    battle_script = LuaBND._get_goal_name_re(GoalType.Battle, 120000, is_script=True)
    assert battle_script.search("function Inunezumi120000Battle_Activate(")
    battle_bytes = LuaBND._get_goal_name_re(GoalType.Battle, 120000, is_script=False)
    assert battle_bytes.search(b"\0Inunezumi120000Battle_Activate\0")
    logic_script = LuaBND._get_goal_name_re(GoalType.Logic, 120000, is_script=True)
    assert logic_script.search("function Inunezumi120000_Logic(")
    with pytest.raises(ValueError):
        LuaBND._get_goal_name_re(GoalType.Unknown, 1, is_script=True)


@pytest.mark.xfail(
    reason="M11: `_get_goal_name_re(..., is_script=True)` returns a non-MULTILINE pattern whose `^` "
           "anchor cannot match after the first line (and `luabnd.py:120` passes `re.MULTILINE` as "
           "the `pos` argument of `search`).",
    strict=False,
)
def test_goal_name_regex_matches_later_lines():
    pattern = LuaBND._get_goal_name_re(GoalType.Battle, 120000, is_script=True)
    script = "-- header comment\nfunction Inunezumi120000Battle_Activate(ai)\n"
    assert pattern.search(script) is not None
