"""Tests for the shared EVS (Python-like event script) compiler in `soulstruct.base.events.evs`.

The Dark Souls 1: Remastered `EVSParser` subclass is used as a concrete vehicle; everything
exercised here lives in the base package (`evs/core.py`, `evs/compiler.py`, `evs/conditions.py`,
`evs/utils.py`, `evs/adv_decompiler.py`).
"""
from __future__ import annotations

import ast
from pathlib import Path

import pytest

from soulstruct.base.events.evs.adv_decompiler import AdvancedDecompiler
from soulstruct.base.events.evs.conditions import ConditionGroupState, EVSConditionManager
from soulstruct.base.events.evs.exceptions import (
    EVSError,
    EVSNameError,
    EVSSyntaxError,
    EVSValueError,
    NoNegateError,
    NoSkipOrReturnError,
)
from soulstruct.base.events.evs.utils import (
    COMPARISON_NODES,
    CONDITION_GROUP_RE,
    EVENT_DOCSTRING_RE,
    MAP_ID_RE,
    NEG_COMPARISON_NODES,
    RESTART_TYPES,
    as_condition_node,
    as_event_statement_node,
    as_skip_return_node,
    parse_event_arguments,
)
from soulstruct.darksouls1r.events import EMEVD
from soulstruct.darksouls1r.events.emevd.evs import EVSParser

DOCSTRING = '"""m10_00_00_00\n\nlinked:\n\n\nstrings:\n\n"""\n'


def parse(body: str, name: str = "m10_00_00_00", docstring: bool = True) -> EVSParser:
    return EVSParser((DOCSTRING if docstring else "") + body, name=name)


def numeric_lines(parser: EVSParser) -> list[str]:
    return parser.numeric_emevd.split("\n\nlinked:")[0].splitlines()


CONSTRUCTOR = '@ContinueOnRest(0)\ndef Constructor():\n    """Event 0"""\n'


# ---------------------------------------------------------------------------
# Pure-unit: regexes, node validators, comparison maps
# ---------------------------------------------------------------------------


def test_comparison_node_maps_are_exact_negations():
    """`NEG_COMPARISON_NODES[op]` must be the EMEVD comparison type of `not op`."""
    assert set(COMPARISON_NODES) == set(NEG_COMPARISON_NODES)
    inverse = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Gt: ast.LtE, ast.LtE: ast.Gt, ast.Lt: ast.GtE,
               ast.GtE: ast.Lt}
    for op, negated_op in inverse.items():
        assert NEG_COMPARISON_NODES[op] == COMPARISON_NODES[negated_op]


def test_restart_types_match_on_rest_behavior_enum():
    from soulstruct.base.events.enums import OnRestBehavior
    assert RESTART_TYPES == {member.name: member.value for member in OnRestBehavior}


@pytest.mark.parametrize(
    "name, expected", [("m10_02_00_00", ("10", "02")), ("m99_00_00_00", ("99", "00")), ("common", None)]
)
def test_map_id_re(name, expected):
    match = MAP_ID_RE.match(name)
    assert (match.groups() if match else None) == expected


@pytest.mark.parametrize(
    "name, groups",
    [("MAIN", ("MAIN", None, None)), ("AND_01", ("AND_01", "AND", "01")), ("OR_7", ("OR_7", "OR", "7"))],
)
def test_condition_group_re(name, groups):
    assert CONDITION_GROUP_RE.match(name).group(1, 2, 3) == groups


def test_event_docstring_re():
    assert EVENT_DOCSTRING_RE.match("11020100: Description").group(1, 2) == ("11020100", ": Description")
    assert EVENT_DOCSTRING_RE.match("11020100").group(1) == "11020100"
    assert EVENT_DOCSTRING_RE.match("no id here") is None


def test_node_type_guards():
    assert as_condition_node(ast.parse("f()", mode="eval").body) is not None
    with pytest.raises(EVSSyntaxError):
        as_condition_node(ast.parse("[1, 2]", mode="eval").body)
    with pytest.raises(EVSSyntaxError):
        as_skip_return_node(ast.parse("a or b", mode="eval").body)
    with pytest.raises(EVSSyntaxError):
        as_event_statement_node(ast.parse("import os").body[0])


def test_evs_error_extracts_lineno_from_node():
    node = ast.parse("x = 1\ny = 2").body[1]
    error = EVSError("m10_00_00_00", node, "boom")
    assert error.lineno == 2
    assert "LINE 2" in str(error) and "m10_00_00_00" in str(error)


def test_parse_event_arguments_types_and_offsets():
    node = ast.parse(
        "def Event_1(_, character: Character | int, flag: uint, ratio: float, tiny: uchar): pass"
    ).body[0]
    from soulstruct.darksouls1r import game_types
    namespace = vars(game_types)
    arg_dict, arg_types, arg_classes = parse_event_arguments("m10_00_00_00", node, namespace)
    assert arg_types == "iIfB"
    assert list(arg_dict) == ["character", "flag", "ratio", "tiny"]
    assert [offset for offset, _ in arg_dict.values()] == [0, 4, 8, 12]
    assert [size for _, size in arg_dict.values()] == [4, 4, 4, 1]
    assert arg_classes["character"] is namespace["Character"]


def test_parse_event_arguments_rejects_defaults_and_varargs():
    for source in (
        "def Event_1(_, flag: uint = 3): pass",
        "def Event_1(_, *args): pass",
        "def Event_1(_, **kwargs): pass",
        "def Event_1(_, *, flag: uint): pass",
        "def Event_1(_, flag): pass",  # no type hint
        "def Event_1(_, flag: NotAGameType): pass",
    ):
        node = ast.parse(source).body[0]
        with pytest.raises(EVSSyntaxError):
            parse_event_arguments("m10_00_00_00", node, {})


def test_parse_event_arguments_skips_slot_placeholders():
    node = ast.parse("def Event_1(_, slot, event_layers, flag: uint): pass").body[0]
    arg_dict, arg_types, _ = parse_event_arguments("m10_00_00_00", node, {})
    assert list(arg_dict) == ["flag"] and arg_types == "I"


# ---------------------------------------------------------------------------
# Pure-unit: condition group manager
# ---------------------------------------------------------------------------


def _manager() -> EVSConditionManager:
    return EVSConditionManager(EVSParser.OR_SLOTS, EVSParser.AND_SLOTS)


def test_condition_manager_indexing():
    manager = _manager()
    assert manager.MAIN.index == 0
    assert manager[0] is manager.MAIN
    for i in EVSParser.AND_SLOTS:
        assert manager[i].index == i
    for i in EVSParser.OR_SLOTS:
        assert manager[i].index == i


def test_condition_manager_checkout_and_reset():
    manager = _manager()
    manager.reset(11000100)
    and_1 = manager.check_out_AND("m10", ast.parse("x = 1").body[0], 11000100, name="my_cond")
    assert and_1.index == EVSParser.AND_SLOTS[0] and and_1.name == "my_cond"
    assert manager["my_cond"] is and_1
    or_cond = manager.check_out_OR("m10", ast.parse("x = 1").body[0], 11000100)
    # NOTE: despite the docstring ("closest to 0"), OR slots are sorted ascending, so the
    # MOST negative slot is checked out first (unlike AND slots, which start at 1).
    assert or_cond.index == min(EVSParser.OR_SLOTS)
    manager.reset(0)
    assert and_1.name == "" and not and_1.active and not and_1.stale


def test_condition_manager_rejects_duplicate_names():
    from soulstruct.base.events.evs.exceptions import ConditionNameError
    manager = _manager()
    manager.reset(0)
    node = ast.parse("x = 1").body[0]
    manager.check_out_AND("m10", node, 0, name="dupe")
    with pytest.raises(ConditionNameError):
        manager.check_out_AND("m10", node, 0, name="dupe")


def test_condition_manager_exhaustion_raises():
    from soulstruct.base.events.evs.exceptions import ConditionLimitError
    manager = _manager()
    manager.reset(0)
    node = ast.parse("x = 1").body[0]
    for i in range(len(EVSParser.AND_SLOTS)):
        manager.check_out_AND("m10", node, 0, name=f"c{i}")
    with pytest.raises(ConditionLimitError):
        manager.check_out_AND("m10", node, 0, name="one_too_many")


def test_condition_group_state_activate_deactivate():
    parent = ConditionGroupState(index=1)
    child = ConditionGroupState(index=-1)
    parent.activate_with_child(child)
    assert parent.active and not parent.stale and child in parent.children
    parent.deactivate()
    assert not parent.active and parent.stale and not parent.children


def test_condition_manager_deactivate_all_marks_stale():
    manager = _manager()
    manager.reset(0)
    cond = manager.check_out_AND("m10", ast.parse("x = 1").body[0], 0, name="c")
    cond.activate()
    manager.deactivate_all()
    assert cond.stale and not cond.active


def test_condition_manager_rejects_out_of_range_or_group():
    manager = _manager()
    out_of_range = min(EVSParser.OR_SLOTS) - 1
    with pytest.raises((IndexError, KeyError)):
        manager[out_of_range]


def test_check_out_temp_does_not_clobber_named_condition():
    manager = _manager()
    manager.reset(0)
    for i in range(len(EVSParser.AND_SLOTS)):
        manager.check_out_AND("m10", ast.parse("x = 1").body[0], 0, name=f"c{i}")
    named = manager["c%d" % (len(EVSParser.AND_SLOTS) - 1)]
    manager.check_out_TEMP("m10", 1, 0)
    assert named.name != "_"


# ---------------------------------------------------------------------------
# EVS compilation: happy paths
# ---------------------------------------------------------------------------


def test_simple_instruction_compiles():
    parser = parse(CONSTRUCTOR + "    EnableFlag(11000001)\n")
    assert numeric_lines(parser) == ["0, 0", " 2003[02] (iB)[11000001, 1]"]


def test_special_event_names_and_ids():
    parser = parse(
        "@ContinueOnRest(0)\ndef Constructor():\n    \"\"\"Event 0\"\"\"\n    EnableFlag(1)\n\n"
        "@RestartOnRest(50)\ndef Preconstructor():\n    \"\"\"Event 50\"\"\"\n    EnableFlag(2)\n"
    )
    assert parser.event_ids == {0, 50}
    assert numeric_lines(parser)[3] == "50, 1"


def test_event_id_from_docstring_only():
    parser = parse('def Event_11000100():\n    """11000100: description"""\n    EnableFlag(1)\n')
    assert parser.events["Event_11000100"].id == 11000100
    assert parser.events["Event_11000100"].description == " description"


def test_duplicate_event_id_rejected():
    body = (
        '@ContinueOnRest(11000100)\ndef Event_A():\n    """Event"""\n    EnableFlag(1)\n\n'
        '@ContinueOnRest(11000100)\ndef Event_B():\n    """Event"""\n    EnableFlag(2)\n'
    )
    with pytest.raises(EVSSyntaxError, match="defined multiple times"):
        parse(body)


def test_event_name_cannot_shadow_instruction():
    with pytest.raises(EVSSyntaxError, match="cannot match an instruction name"):
        parse('@ContinueOnRest(1)\ndef EnableFlag():\n    """Event 1"""\n    EnableFlag(1)\n')


def test_event_with_arguments_emits_replacements():
    parser = parse(
        '@RestartOnRest(11000100)\ndef Event_11000100(_, flag: Flag | int, ratio: float):\n'
        '    """Event 11000100"""\n'
        '    EnableFlag(flag)\n'
    )
    lines = numeric_lines(parser)
    assert lines[0] == "11000100, 1"
    assert lines[1] == " 2003[02] (iB)[0, 1]"
    assert lines[2] == "    ^(0 <- 0, 4)"
    assert parser.events["Event_11000100"].arg_types == "if"


def test_event_call_by_name_with_keywords():
    parser = parse(
        CONSTRUCTOR + "    Event_11000100(0, flag=11000002)\n\n"
        '@ContinueOnRest(11000100)\ndef Event_11000100(_, flag: Flag | int):\n'
        '    """Event 11000100"""\n    EnableFlag(flag)\n'
    )
    assert " 2000[00] (iIi)[0, 11000100, 11000002]" in numeric_lines(parser)


def test_event_call_missing_keyword_rejected():
    body = (
        CONSTRUCTOR + "    Event_11000100(0)\n\n"
        '@ContinueOnRest(11000100)\ndef Event_11000100(_, flag: Flag | int):\n'
        '    """Event 11000100"""\n    EnableFlag(flag)\n'
    )
    with pytest.raises(EVSValueError, match="does not match the event function signature"):
        parse(body)


def test_run_event_arg_types():
    parser = parse(CONSTRUCTOR + '    RunEvent(11000100, args=(1, 2.0), arg_types="if")\n')
    assert " 2000[00] (iIi|f)[0, 11000100, 1, 2.0]" in numeric_lines(parser)


def test_for_loop_unrolls():
    parser = parse(CONSTRUCTOR + "    for f in range(3):\n        EnableFlag(11000001 + f)\n")
    assert numeric_lines(parser)[1:] == [
        " 2003[02] (iB)[11000001, 1]",
        " 2003[02] (iB)[11000002, 1]",
        " 2003[02] (iB)[11000003, 1]",
    ]


def test_for_loop_with_zip_tuple_target():
    parser = parse(
        CONSTRUCTOR + "    for f, s in zip([1, 2], [0, 1]):\n        EnableFlag(f)\n"
    )
    assert len(numeric_lines(parser)) == 3


def test_for_loop_duplicate_variable_rejected():
    with pytest.raises(EVSSyntaxError, match="already a 'for' loop variable"):
        parse(CONSTRUCTOR + "    for f in range(2):\n        for f in range(2):\n            EnableFlag(f)\n")


def test_global_and_local_assignment():
    parser = parse(
        "MY_FLAG = 11000009\n\n" + CONSTRUCTOR + "    local_flag = 11000010\n    EnableFlag(MY_FLAG)\n"
        "    EnableFlag(local_flag)\n"
    )
    assert numeric_lines(parser)[1:] == [
        " 2003[02] (iB)[11000009, 1]",
        " 2003[02] (iB)[11000010, 1]",
    ]


def test_assignment_to_reserved_name_rejected():
    with pytest.raises(EVSSyntaxError, match="Cannot assign to"):
        parse("EnableFlag = 1\n\n" + CONSTRUCTOR + "    EnableFlag(1)\n")


def test_binary_operations_in_arguments():
    parser = parse("BASE = 11000000\n\n" + CONSTRUCTOR + "    EnableFlag(BASE + 2 * 3 - 1)\n")
    assert numeric_lines(parser)[1] == " 2003[02] (iB)[11000005, 1]"


def test_return_end_and_restart():
    parser = parse(CONSTRUCTOR + "    return\n")
    assert numeric_lines(parser)[1].startswith(" 1000[04]") or "1000" in numeric_lines(parser)[1]
    parser = parse(CONSTRUCTOR + "    return RESTART\n")
    assert len(numeric_lines(parser)) == 2


def test_invalid_return_value_rejected():
    with pytest.raises(EVSSyntaxError, match="Invalid return value"):
        parse(CONSTRUCTOR + "    return 5\n")


def test_condition_group_and_await():
    parser = parse(
        CONSTRUCTOR
        + "    my_cond = Condition(FlagEnabled(11000001) and FlagEnabled(11000002))\n"
        + "    MAIN.Await(my_cond)\n"
    )
    lines = numeric_lines(parser)
    # Two `IfFlagEnabled` tests loaded into AND_1, then AND_1 loaded into MAIN.
    assert lines[1].startswith("    3[00]") and lines[2].startswith("    3[00]")
    assert lines[3].startswith("    0[00]")


def test_or_condition_uses_negative_index():
    parser = parse(
        CONSTRUCTOR
        + "    c = Condition(FlagEnabled(11000001) or FlagEnabled(11000002))\n"
        + "    MAIN.Await(c)\n"
    )
    lines = numeric_lines(parser)
    # See `test_condition_manager_checkout_and_reset`: the most negative OR slot is used first.
    assert f"[{min(EVSParser.OR_SLOTS)}, " in lines[1]


def test_explicit_condition_group_add():
    parser = parse(CONSTRUCTOR + "    AND_1.Add(FlagEnabled(11000001))\n    MAIN.Await(AND_1)\n")
    assert len(numeric_lines(parser)) == 3


def test_if_block_compiles_to_skip():
    parser = parse(CONSTRUCTOR + "    if FlagEnabled(11000001):\n        EnableFlag(2)\n")
    lines = numeric_lines(parser)
    assert lines[1].startswith(" 1003[01]")  # SkipLinesIfFlagDisabled
    assert lines[1].endswith("[1, 0, 0, 11000001]")  # skip 1 line


def test_if_else_block_adds_unconditional_skip():
    parser = parse(
        CONSTRUCTOR + "    if FlagEnabled(11000001):\n        EnableFlag(2)\n    else:\n        EnableFlag(3)\n"
    )
    lines = numeric_lines(parser)
    assert lines[1].endswith("[2, 0, 0, 11000001]")  # skip 2 lines (body + unconditional skip)
    assert lines[3].startswith(" 1000[03]")  # SkipLines


def test_not_operator_inverts_test():
    positive = parse(CONSTRUCTOR + "    if FlagEnabled(11000001):\n        EnableFlag(2)\n")
    negative = parse(CONSTRUCTOR + "    if not FlagEnabled(11000001):\n        EnableFlag(2)\n")
    assert numeric_lines(positive)[1] != numeric_lines(negative)[1]


def test_comparison_test_compiles():
    parser = parse(CONSTRUCTOR + "    MAIN.Await(HealthRatio(PLAYER) <= 0.5)\n")
    assert len(numeric_lines(parser)) >= 2


def test_flag_range_any_all():
    parser = parse(CONSTRUCTOR + "    if all(range(11000001, 11000005)):\n        EnableFlag(2)\n")
    assert len(numeric_lines(parser)) == 3


def test_unary_operator_other_than_not_rejected():
    with pytest.raises(EVSSyntaxError, match="only valid unary operator"):
        parse(CONSTRUCTOR + "    if -FlagEnabled(11000001):\n        EnableFlag(2)\n")


def test_undefined_name_raises_name_error_with_line():
    with pytest.raises(EVSNameError) as exc_info:
        parse(CONSTRUCTOR + "    EnableFlag(UNDEFINED_NAME)\n")
    assert exc_info.value.lineno == 12


def test_invalid_global_statement_rejected():
    with pytest.raises(EVSSyntaxError, match="Invalid content"):
        parse("while True:\n    pass\n\n" + CONSTRUCTOR + "    EnableFlag(1)\n")


def test_empty_event_gets_dummy_end():
    parser = parse('@ContinueOnRest(11000100)\ndef Event_11000100():\n    """Event 11000100"""\n')
    assert len(numeric_lines(parser)) == 2  # header + End()


def test_enable_this_flag_shortcut():
    parser = parse('@ContinueOnRest(11000100)\ndef Event_11000100():\n    """Event"""\n    EnableThisFlag()\n')
    assert numeric_lines(parser)[1] == " 2003[02] (iB)[11000100, 1]"


def test_enable_this_flag_rejected_with_args():
    body = (
        '@ContinueOnRest(11000100)\ndef Event_11000100(_, flag: Flag | int):\n'
        '    """Event"""\n    EnableThisFlag()\n'
    )
    with pytest.raises(EVSSyntaxError, match="cannot be determined from within"):
        parse(body)


def test_compiled_evs_can_be_packed_to_binary():
    emevd = EMEVD.from_evs_string(
        DOCSTRING + CONSTRUCTOR + "    EnableFlag(11000001)\n", map_name="m10_00_00_00"
    )
    assert bytes(emevd.to_writer())


# ---------------------------------------------------------------------------
# `AdvancedDecompiler` (pure unit)
# ---------------------------------------------------------------------------


def _adv(lines, tests=None, comparison_tests=None):
    return AdvancedDecompiler(tests or {}, comparison_tests or {}).adv_decompile(list(lines))


def test_adv_decompiler_condition_add_and_await():
    out = _adv([
        "IfConditionTrue(AND_1, input_condition=OR_1)",
        "IfConditionFalse(MAIN, input_condition=AND_1)",
    ])
    assert out[0] == "AND_1.Add(OR_1)"
    assert "MAIN.Await(not AND_1)" in out


def test_adv_decompiler_generic_test_to_condition_add():
    out = _adv(["IfFlagEnabled(AND_1, 11000001)"], tests={"FlagEnabled": {"if": "IfFlagEnabled"}})
    assert out == ["AND_1.Add(FlagEnabled(11000001))"]


def test_adv_decompiler_leaves_unknown_test_alone():
    line = "IfSomethingWeird(AND_1, 5)"
    assert _adv([line]) == [line]


def test_adv_decompiler_skip_becomes_if_block():
    tests = {"FlagEnabled": {"if": "IfFlagEnabled", "skip_if_not": "SkipLinesIfFlagDisabled"}}
    out = _adv(["SkipLinesIfFlagDisabled(1, 11000001)", "EnableFlag(2)"], tests=tests)
    assert out[0] == "if FlagEnabled(11000001):"
    assert out[1] == "    EnableFlag(2)"


def test_adv_decompiler_skip_with_else_block():
    tests = {"FlagEnabled": {"if": "IfFlagEnabled", "skip_if_not": "SkipLinesIfFlagDisabled"}}
    out = _adv(
        ["SkipLinesIfFlagDisabled(2, 11000001)", "EnableFlag(2)", "SkipLines(1)", "EnableFlag(3)"],
        tests=tests,
    )
    assert out[0] == "if FlagEnabled(11000001):"
    assert "else:" in out


def test_adv_decompiler_flags_useless_and_overlong_skips():
    out = _adv(["SkipLinesIfFlagDisabled(0, 1)", "EnableFlag(2)"])
    assert "useless skip" in out[0]
    out = _adv(["SkipLinesIfFlagDisabled(9, 1)", "EnableFlag(2)"])
    assert "skip goes past end of event" in out[0]


def test_adv_decompiler_condition_based_skip():
    out = _adv(["SkipLinesIfConditionFalse(1, input_condition=AND_1)", "EnableFlag(2)"])
    assert out[0] == "if AND_1:"


def test_adv_decompiler_return_condition():
    out = _adv(["EndIfConditionTrue(input_condition=AND_1)"])
    assert out[0] == "if AND_1:" and out[1] == "    return"
    out = _adv(["RestartIfLastConditionResultFalse(input_condition=OR_2)"])
    assert out[0] == "if not LastResult(OR_2):" and out[1] == "    return RESTART"


def test_adv_decompiler_trailing_end_becomes_return():
    out = _adv(["EnableFlag(1)", "End()"])
    assert out[-1] == "return"
    out = _adv(["EnableFlag(1)", "Restart()"])
    assert out[-1] == "return RESTART"


def test_adv_decompiler_frame_stack_is_balanced():
    decompiler = AdvancedDecompiler({}, {})
    decompiler.adv_decompile(["EnableFlag(1)"])
    assert decompiler._frame_stack == []


# ---------------------------------------------------------------------------
# Full decompile / recompile fidelity (needs the committed test resource)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def ds1r_emevd_path(tests_dir: Path) -> Path:
    path = tests_dir / "darksouls1r" / "resources" / "m10_00_00_00.emevd.dcx"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return path


def test_decompile_recompile_is_byte_identical(ds1r_emevd_path: Path, tmp_path: Path):
    """The flagship guarantee: EMEVD -> EVS -> EMEVD must be lossless."""
    emevd = EMEVD.from_path(ds1r_emevd_path)
    original = bytes(emevd.to_writer())
    evs_path = tmp_path / "m10_00_00_00.evs.py"
    evs_path.write_text(emevd.to_evs(), encoding="utf-8")
    recompiled = EMEVD.from_evs_path(evs_path)
    assert bytes(recompiled.to_writer()) == original


def test_decompile_recompile_decompile_is_stable(ds1r_emevd_path: Path, tmp_path: Path):
    emevd = EMEVD.from_path(ds1r_emevd_path)
    evs_1 = emevd.to_evs()
    (tmp_path / "m10_00_00_00.evs.py").write_text(evs_1, encoding="utf-8")
    recompiled = EMEVD.from_evs_path(tmp_path / "m10_00_00_00.evs.py")
    assert recompiled.to_evs() == evs_1


# ---------------------------------------------------------------------------
# Known defects (xfail)
# ---------------------------------------------------------------------------


def test_script_without_module_docstring_keeps_first_statement():
    parser = parse(
        CONSTRUCTOR + "    EnableFlag(1)\n\n"
        '@ContinueOnRest(11000100)\ndef Event_11000100():\n    """Event"""\n    EnableFlag(2)\n',
        docstring=False,
    )
    assert set(parser.events) == {"Constructor", "Event_11000100"}


def test_import_typing_is_ignored_cleanly():
    parse("import typing\n\n" + CONSTRUCTOR + "    EnableFlag(11000001)\n")


def test_condition_hold_keyword_is_respected():
    parser = parse(CONSTRUCTOR + "    c = Condition(FlagEnabled(11000001), hold=True)\n    MAIN.Await(c)\n")
    held = [cond for cond in parser.cond_manager.conditions if cond.name == "c"]
    assert held and held[0].held is True


def test_parser_globals_do_not_leak_between_scripts():
    parse("LEAKED_NAME = 999\n\n" + CONSTRUCTOR + "    EnableFlag(11000001)\n")
    with pytest.raises(EVSNameError):
        parse(CONSTRUCTOR + "    EnableFlag(LEAKED_NAME)\n", name="m11_00_00_00")


@pytest.mark.xfail(
    reason="BUG (high): out-of-range OR condition groups wrap around to MAIN "
           "(`EVSConditionManager.__getitem__` uses the condition index as a list index), so "
           "`OR_15` in DS1 silently compiles to condition group 0.",
    strict=False,
)
def test_out_of_range_or_group_is_rejected():
    with pytest.raises(EVSError):
        parse(CONSTRUCTOR + "    OR_15.Add(FlagEnabled(11000001))\n    MAIN.Await(OR_15)\n")


@pytest.mark.xfail(
    reason="BUG: out-of-range AND groups raise a bare `IndexError` from "
           "`_check_condition_group_add` with no EVS file/line context.",
    strict=False,
)
def test_out_of_range_and_group_raises_evs_error():
    with pytest.raises(EVSError):
        parse(CONSTRUCTOR + "    AND_15.Add(FlagEnabled(11000001))\n")


def test_unknown_decorator_raises_evs_syntax_error():
    with pytest.raises(EVSSyntaxError):
        parse('@NotARestType(0)\ndef Constructor():\n    """Event 0"""\n    EnableFlag(1)\n')


def test_for_loop_variable_shadowing_event_arg_is_rejected():
    body = (
        '@ContinueOnRest(11000100)\ndef Event_11000100(_, flag: Flag | int):\n'
        '    """Event"""\n    for flag in range(3):\n        EnableFlag(flag)\n'
    )
    with pytest.raises(EVSSyntaxError, match="already the name of an event argument"):
        parse(body)


def test_invalid_boolean_operand_is_reported():
    with pytest.raises(EVSSyntaxError):
        parse(CONSTRUCTOR + "    MAIN.Await(FlagEnabled(11000001) and 5)\n")


def test_event_layers_keyword_can_be_packed():
    emevd = EMEVD.from_evs_string(
        DOCSTRING + CONSTRUCTOR + "    EnableFlag(11000001, event_layers=[0, 2])\n",
        map_name="m10_00_00_00",
    )
    assert bytes(emevd.to_writer())


def test_error_types_are_exported():
    """Sanity check that the EVS exception hierarchy is importable and consistent."""
    assert issubclass(EVSSyntaxError, EVSError)
    assert issubclass(EVSValueError, EVSError)
    assert issubclass(EVSNameError, EVSError)
    assert not issubclass(NoSkipOrReturnError, EVSError)
    assert not issubclass(NoNegateError, EVSError)
