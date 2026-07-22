"""Tests for `soulstruct.base.ezstate`: the ESD binary format, the EZL expression
compiler/decompiler, and the ESP (Python-like) script round-trip.
"""
from __future__ import annotations

import contextlib
import io
import logging
import struct
from pathlib import Path

import pytest

from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.base.ezstate.esd.exceptions import ESDError, ESDSyntaxError, ESDTypeError
from soulstruct.base.ezstate.esd.command import Command
from soulstruct.base.ezstate.esd.condition import Condition
from soulstruct.base.ezstate.esd.state import State
from soulstruct.base.ezstate.esd import ezl_parser
from soulstruct.base.ezstate.esd.ezl_parser import (
    decompile,
    split_by_and_or,
    FUNCTION_ARG_BYTES_BY_COUNT,
    OPERATORS_BY_NODE,
    CLEAR_REGISTERS,
    SET_INTERNAL_SYMBOLS,
)
from soulstruct.base.ezstate.esd.functions import (
    COMMANDS,
    TEST_FUNCTIONS,
    COMMANDS_BANK_ID_BY_TYPE_NAME,
    TEST_FUNCTIONS_ID_BY_TYPE_NAME,
)


TALK = ESDType.TALK


def _quiet():
    """Context manager that swallows stdout (several ESD methods `print()`; finding M7)."""
    return contextlib.redirect_stdout(io.StringIO())


# ---------------------------------------------------------------------------
# EZL decompiler: literals
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("byte_val, expected", [(0x00, -64), (0x40, 0), (0x41, 1), (0x7f, 63)])
def test_decompile_small_int_literals(byte_val, expected):
    assert decompile(bytes([byte_val, 0xa1]), TALK) == str(expected)


def test_decompile_int32_literal():
    assert decompile(b"\x82" + struct.pack("<i", -123456) + b"\xa1", TALK) == "-123456"


def test_decompile_float_literals():
    assert decompile(b"\x80" + struct.pack("<f", 0.5) + b"\xa1", TALK) == "0.5"
    assert decompile(b"\x81" + struct.pack("<d", 1.25) + b"\xa1", TALK) == "1.25"


def test_decompile_string_literal():
    ezl = b"\xa5" + "hi".encode("utf-16-le") + b"\0\0" + b"\xa1"
    assert decompile(ezl, TALK) == repr("hi")


def test_decompile_machine_symbols():
    assert decompile(b"\x42\xb8\xa1", TALK) == "MACHINE_ARGS[2]"
    assert decompile(b"\xb9\xa1", TALK) == "MACHINE_CALL_STATUS"
    assert decompile(b"\xba\xa1", TALK) == "ONGOING"


@pytest.mark.parametrize(
    "op_byte, symbol",
    [
        (0x8c, "+"), (0x8e, "-"), (0x8f, "*"), (0x90, "/"),
        (0x91, "<="), (0x92, ">="), (0x93, "<"), (0x94, ">"),
        (0x95, "=="), (0x96, "!="), (0x98, "and"), (0x99, "or"),
    ],
)
def test_decompile_binary_operators(op_byte, symbol):
    # 3 <op> 2
    assert decompile(bytes([0x43, 0x42, op_byte, 0xa1]), TALK) == f"3 {symbol} 2"


def test_decompile_operator_precedence_parentheses():
    # (1 or 2) * 3 -> parenthesised because `or` has lower priority than `*`
    ezl = bytes([0x41, 0x42, 0x99, 0x43, 0x8f, 0xa1])
    assert decompile(ezl, TALK) == "(1 or 2) * 3"


def test_decompile_function_call_zero_args():
    result = decompile(bytes([0x41, 0x84, 0xa1]), TALK)
    assert result.endswith("()")
    assert TEST_FUNCTIONS[TALK][1][0] in result


def test_decompile_function_call_with_args():
    # Stack order: function ID first, then each argument, then the arg-count byte.
    ezl = bytes([0x41, 0x45, 0x46, 0x86, 0xa1])  # f_id=1, args (5, 6)
    result = decompile(ezl, TALK)
    assert result == f"{TEST_FUNCTIONS[TALK][1][0]}(5, 6)"


def test_decompile_unknown_function_id_falls_back():
    ezl = b"\x82" + struct.pack("<i", 9999) + b"\x84\xa1"
    assert decompile(ezl, TALK) == f"Test_{TALK}_9999()"


def test_decompile_func_prefix():
    result = decompile(bytes([0x41, 0x84, 0xa1]), TALK, func_prefix="self.")
    assert result.startswith("self.")


def test_decompile_registers_roundtrip():
    CLEAR_REGISTERS()
    # 1 -> call -> save to register 0 (0xa7) -> load register 0 (0xaf)
    ezl = bytes([0x41, 0x84, 0xa7, 0xaf, 0xa1])
    result = decompile(ezl, TALK)
    name = TEST_FUNCTIONS[TALK][1][0]
    assert result == f"{name}(){name}()"


def test_decompile_internal_symbols_are_off_by_default():
    assert decompile(bytes([0x41, 0xa6, 0xa1]), TALK) == "1"
    assert decompile(bytes([0x41, 0xb7, 0xa1]), TALK) == "1"


@pytest.mark.xfail(
    reason="M19: with internal symbols on, the 0xa6/0xb7 handlers do `output[-1] += '...'`, which "
           "raises TypeError whenever the top of the stack is a numeric literal rather than a string.",
    strict=False,
)
def test_decompile_internal_symbols_toggle():
    CLEAR_REGISTERS()
    try:
        SET_INTERNAL_SYMBOLS(True)
        assert decompile(bytes([0x41, 0xa6, 0xa1]), TALK).endswith("...")
        assert decompile(bytes([0x41, 0xb7, 0xa1]), TALK).endswith("!")
    finally:
        SET_INTERNAL_SYMBOLS(False)


def test_decompile_rejects_early_end_of_line():
    with pytest.raises(ESDError):
        decompile(b"\xa1\x41\xa1", TALK)


def test_decompile_rejects_unknown_byte():
    with pytest.raises(ESDError):
        decompile(b"\xfe\xa1", TALK)


@pytest.mark.xfail(
    reason="M15: `0x8d` (unary negate) and `0x97` (unknown) fall into the binary-operator range but "
           "are absent from `BINARY_OPERATORS_BY_BYTE`, so a bare `KeyError` escapes instead of `ESDError`.",
    strict=False,
)
@pytest.mark.parametrize("op_byte", [0x8d, 0x97])
def test_decompile_unhandled_operator_raises_esd_error(op_byte):
    with pytest.raises(ESDError):
        decompile(bytes([0x41, 0x42, op_byte, 0xa1]), TALK)


def test_decompile_module_state_is_global():
    """M16: registers and the symbol flag are module-level globals, not per-call state."""
    assert isinstance(ezl_parser._REGISTERS, list) and len(ezl_parser._REGISTERS) == 8
    CLEAR_REGISTERS()
    assert ezl_parser._REGISTERS == [""] * 8


# ---------------------------------------------------------------------------
# EZL lookup tables
# ---------------------------------------------------------------------------


def test_function_arg_bytes_by_count():
    assert FUNCTION_ARG_BYTES_BY_COUNT[0] == b"\x84"
    assert FUNCTION_ARG_BYTES_BY_COUNT[6] == b"\x8a"
    assert len(FUNCTION_ARG_BYTES_BY_COUNT) == 7


def test_operators_by_node_are_unique():
    assert len(set(OPERATORS_BY_NODE.values())) == len(OPERATORS_BY_NODE)


def test_function_tables_built_from_stub_file():
    assert set(COMMANDS) == {ESDType.CHR, ESDType.TALK}
    assert COMMANDS[TALK], "expected TALK commands parsed from functions.pyi"
    assert TEST_FUNCTIONS[TALK], "expected TALK test functions parsed from functions.pyi"
    # Inverse tables must be consistent.
    for (esd_type, name), (bank, f_id) in COMMANDS_BANK_ID_BY_TYPE_NAME.items():
        assert COMMANDS[esd_type][bank][f_id][0] == name
    for (esd_type, name), f_id in TEST_FUNCTIONS_ID_BY_TYPE_NAME.items():
        assert TEST_FUNCTIONS[esd_type][f_id][0] == name


# ---------------------------------------------------------------------------
# `split_by_and_or`
# ---------------------------------------------------------------------------


def test_split_by_and_or_simple():
    assert split_by_and_or("a and b") == ["a", "and b"]


def test_split_by_and_or_preserves_calls():
    lines = split_by_and_or("Foo(1, 2) and Bar(3)")
    assert lines[0] == "Foo(1, 2)"
    assert lines[1] == "and Bar(3)"


def test_split_by_and_or_indents_parenthesised_blocks():
    lines = split_by_and_or("a and (b or c)")
    assert any(line.startswith("    ") for line in lines)
    assert "".join(line.strip() for line in lines).replace(" ", "") == "aand(borc)"


# ---------------------------------------------------------------------------
# `Command` / `Condition` value semantics
# ---------------------------------------------------------------------------


def test_command_hash_and_eq():
    a = Command(1, 2, [b"\x41\xa1"])
    b = Command(1, 2, [b"\x41\xa1"])
    c = Command(1, 3, [b"\x41\xa1"])
    assert a == b and hash(a) == hash(b)
    assert a != c
    assert len({a, b, c}) == 2


def test_condition_hash_and_eq():
    a = Condition(1, b"\x41\xa1", [Command(1, 2)], [])
    b = Condition(1, b"\x41\xa1", [Command(1, 2)], [])
    c = Condition(2, b"\x41\xa1", [Command(1, 2)], [])
    assert a == b and hash(a) == hash(b)
    assert a != c
    assert len({a, b, c}) == 2


def test_state_repr():
    s = State(5, [Condition(-1, b"\x41\xa1")], [Command(1, 1)], [], [])
    r = repr(s)
    assert "State[5]" in r and "1 conditions" in r and "enter commands" in r


def test_state_copy_is_deep():
    s = State(0, [Condition(1, b"\x41\xa1", [Command(1, 1, [b"\x41\xa1"])])])
    s2 = s.copy()
    assert s2 == s or s2.state_id == s.state_id
    assert s2.conditions[0] is not s.conditions[0]
    assert s2.conditions[0].pass_commands[0] is not s.conditions[0].pass_commands[0]


def test_esd_type_enum():
    assert ESDType("talk") is ESDType.TALK
    assert ESDType("chr") is ESDType.CHR


# ---------------------------------------------------------------------------
# Synthetic ESD binary round-trips
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def talk_esd_cls():
    from soulstruct.darksouls1r.ezstate import TalkESD

    return TalkESD


def _simple_esd(talk_esd_cls, name="test.esd"):
    # NOTE: every EZL `bytes` value must be a *distinct* object -- command arg offsets are reserved
    # by `id(arg_bytes)` (finding L9), so reusing one literal for two args collides.
    # NOTE: commands with arguments must NOT go on the *first* state of a machine -- see H15.
    return talk_esd_cls(
        magic=[0, 0, 0, 0],
        esd_name=name,
        state_machines={
            1: {
                0: State(0, [Condition(1, bytes([0x41, 0xa1]))]),
                1: State(
                    1,
                    [Condition(0, bytes([0x41, 0xa1]))],
                    enter_commands=[Command(1, 1, [bytes([0x41, 0xa1])])],
                ),
            }
        },
    )


@pytest.mark.xfail(
    reason="L9: `Command.pack_args_offsets()` reserves arg offsets keyed on `id(arg_bytes)`, so two "
           "arguments that happen to be the same `bytes` object raise 'already reserved'.",
    strict=False,
)
def test_esd_shared_arg_bytes_object(talk_esd_cls):
    shared = b"\x41\xa1"
    esd = talk_esd_cls(
        magic=[0, 0, 0, 0],
        esd_name="x.esd",
        state_machines={
            1: {0: State(0, [Condition(-1, shared)], enter_commands=[Command(1, 1, [shared, shared])])}
        },
    )
    bytes(esd)


@pytest.mark.xfail(
    reason="H15: `ESD.to_writer()` deep-copies the first state as a trailing dummy, but "
           "`copy.deepcopy()` returns the *same* immutable `bytes` objects for command args, which "
           "then collide with the original's `id()`-keyed offset reservations.",
    strict=False,
)
def test_esd_first_state_with_command_args(talk_esd_cls):
    esd = talk_esd_cls(
        magic=[0, 0, 0, 0],
        esd_name="x.esd",
        state_machines={
            1: {
                0: State(
                    0,
                    [Condition(1, bytes([0x41, 0xa1]))],
                    enter_commands=[Command(1, 1, [bytes([0x41, 0xa1])])],
                ),
                1: State(1, [Condition(0, bytes([0x41, 0xa1]))]),
            }
        },
    )
    bytes(esd)


def test_synthetic_esd_binary_roundtrip(talk_esd_cls):
    esd = _simple_esd(talk_esd_cls)
    data = bytes(esd)
    esd2 = talk_esd_cls.from_bytes(data)
    assert set(esd2.state_machines) == {1}
    assert set(esd2.state_machines[1]) == {0, 1}
    assert esd2.state_machines[1][0].conditions[0].next_state_id == 1
    assert esd2.state_machines[1][1].enter_commands[0].bank == 1
    assert esd2.state_machines[1][1].enter_commands[0].args == [bytes([0x41, 0xa1])]
    assert bytes(esd2) == data  # second pack must be stable


def test_synthetic_esd_no_name(talk_esd_cls):
    esd = _simple_esd(talk_esd_cls, name="")
    esd2 = talk_esd_cls.from_bytes(bytes(esd))
    assert esd2.esd_name == ""


def test_esd_reader_must_start_at_zero(talk_esd_cls):
    from soulstruct.utilities.binary import BinaryReader

    reader = BinaryReader(bytes(_simple_esd(talk_esd_cls)))
    reader.seek(4)
    with pytest.raises(ValueError):
        talk_esd_cls.from_reader(reader)


@pytest.mark.xfail(
    reason="H2: `esd_name_length=len(self.esd_name) // 2` halves the stored character count, so the "
           "internal ESD name is truncated on every write.",
    strict=False,
)
def test_esd_name_survives_roundtrip(talk_esd_cls):
    esd = _simple_esd(talk_esd_cls, name="t100613")
    esd2 = talk_esd_cls.from_bytes(bytes(esd))
    assert esd2.esd_name == "t100613"


@pytest.mark.xfail(
    reason="C2: subcondition pass-commands are packed twice (`pack_conditions` returns a flattened "
           "list *and* `pack_subconditions_*` recurses), and the reader does `len(int)`.",
    strict=False,
)
def test_esd_with_subconditions_roundtrip(talk_esd_cls):
    sub = Condition(-1, b"\x41\xa1")
    cond = Condition(1, b"\x41\xa1", [], [sub])
    esd = talk_esd_cls(
        magic=[0, 0, 0, 0],
        esd_name="sub.esd",
        state_machines={1: {0: State(0, [cond]), 1: State(1, [])}},
    )
    esd2 = talk_esd_cls.from_bytes(bytes(esd))
    assert len(esd2.state_machines[1][0].conditions[0].subconditions) == 1


def test_esd_get_next_states(talk_esd_cls):
    esd = _simple_esd(talk_esd_cls)
    cond = Condition(3, b"\x41\xa1", [], [Condition(4, b"\x41\xa1"), Condition(-1, b"\x41\xa1")])
    assert sorted(esd.get_next_states(cond)) == [3, 4]


# ---------------------------------------------------------------------------
# Real DS1R talk ESD
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def dsr_resources(request) -> Path:
    path = Path(request.config.rootpath) / "tests" / "darksouls1r" / "resources"
    if not path.is_dir():
        pytest.skip(f"No DS1R resources directory: {path}")
    return path


@pytest.fixture(scope="module")
def t100613_esd(dsr_resources, talk_esd_cls):
    path = dsr_resources / "t100613.esd"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    return talk_esd_cls.from_path(path)


def test_real_talk_esd_loads(t100613_esd):
    esd = t100613_esd
    assert esd.esd_name == "t100613"
    assert list(esd.state_machines) == [1]
    assert len(esd.state_machines[1]) > 10
    assert len(esd.magic) == 4


def test_real_talk_esd_structural_roundtrip(t100613_esd, talk_esd_cls):
    esd2 = talk_esd_cls.from_bytes(bytes(t100613_esd))
    assert set(esd2.state_machines) == set(t100613_esd.state_machines)
    for sm_index, states in t100613_esd.state_machines.items():
        assert set(esd2.state_machines[sm_index]) == set(states)
        for state_id, state in states.items():
            other = esd2.state_machines[sm_index][state_id]
            assert [c.next_state_id for c in other.conditions] == [c.next_state_id for c in state.conditions]
            assert [c.test_ezl for c in other.conditions] == [c.test_ezl for c in state.conditions]
            assert len(other.enter_commands) == len(state.enter_commands)
            assert len(other.exit_commands) == len(state.exit_commands)
            assert len(other.ongoing_commands) == len(state.ongoing_commands)


@pytest.mark.xfail(
    reason="H2: the internal ESD name shrinks on every write, so pack -> unpack -> pack is not "
           "idempotent (the file gets 2 bytes shorter).",
    strict=False,
)
def test_real_talk_esd_repack_is_stable(t100613_esd, talk_esd_cls):
    once = bytes(t100613_esd)
    twice = bytes(talk_esd_cls.from_bytes(once))
    assert once == twice


def test_real_talk_esd_first_pack_matches_original_size(t100613_esd, dsr_resources):
    """The first repack of a vanilla talk ESD is the same size as the original file."""
    original = (dsr_resources / "t100613.esd").stat().st_size
    assert len(bytes(t100613_esd)) == original


def test_real_talk_esd_all_conditions_decompile(t100613_esd):
    count = 0
    for states in t100613_esd.state_machines.values():
        for state in states.values():
            for condition in state.conditions:
                text = decompile(condition.test_ezl, ESDType.TALK)
                assert isinstance(text, str)
                count += 1
    assert count > 10


def test_real_talk_esd_to_html(t100613_esd):
    with _quiet():
        html = t100613_esd.to_html()
    assert html.startswith("<html>") and html.endswith("</html>")
    # The global symbol flag must be restored after `to_html()`.
    assert ezl_parser._SHOW_INTERNAL_SYMBOLS is False


def test_real_talkesdbnd_roundtrip(dsr_resources):
    from soulstruct.darksouls1r.ezstate import TalkESDBND

    path = dsr_resources / "m10_00_00_00.talkesdbnd.dcx"
    if not path.is_file():
        pytest.skip(f"Test resource not available: {path}")
    logging.disable(logging.WARNING)
    try:
        bnd = TalkESDBND.from_path(path)
        assert len(bnd.talk) > 1
        assert all(isinstance(k, int) for k in bnd.talk)
        assert list(iter(bnd)) == list(bnd.talk)
        assert "TalkESDBND" in repr(bnd)
        data = bytes(bnd)
        bnd2 = TalkESDBND.from_bytes(data)
    finally:
        logging.disable(logging.NOTSET)
    assert set(bnd2.talk) == set(bnd.talk)
    for talk_id, esd in bnd.talk.items():
        other = bnd2.talk[talk_id]
        assert set(other.state_machines) == set(esd.state_machines)


# ---------------------------------------------------------------------------
# ESP (Python script) compile / decompile
# ---------------------------------------------------------------------------


def test_esp_decompile_recompile_roundtrip(t100613_esd, talk_esd_cls, tmp_path):
    with _quiet():
        esp = t100613_esd.to_esp(1)
    assert esp.startswith('"""TALK ESD STATE MACHINE 1"""')
    path = tmp_path / "t100613.esp.py"
    path.write_text(esp, encoding="utf-8")
    with _quiet():
        esd2 = talk_esd_cls.from_esp_file(path)
    assert set(esd2.state_machines[1]) == set(t100613_esd.state_machines[1])
    for state_id, state in t100613_esd.state_machines[1].items():
        other = esd2.state_machines[1][state_id]
        assert len(other.conditions) == len(state.conditions)
        assert [c.next_state_id for c in other.conditions] == [c.next_state_id for c in state.conditions]


def test_esp_write_directory_creates_files(t100613_esd, tmp_path):
    with _quiet():
        t100613_esd.write_esp_directory(tmp_path / "esp")
    assert (tmp_path / "esp" / "ESD_Header.esp.py").is_file()
    assert (tmp_path / "esp" / "StateMachine_1.esp.py").is_file()
    header = (tmp_path / "esp" / "ESD_Header.esp.py").read_text(encoding="utf-8")
    assert "ESD_NAME = " in header and "MAGIC = " in header


@pytest.mark.xfail(
    reason="H14: `write_esp_directory()` writes `ESD_TYPE = 'TALK'` (the enum *name*) but "
           "`read_esp_header()` does `ESDType(...)`, which needs the value 'talk' -- so no "
           "Soulstruct-written ESP directory can be read back.",
    strict=False,
)
def test_esp_write_and_read_directory(t100613_esd, talk_esd_cls, tmp_path):
    with _quiet():
        t100613_esd.write_esp_directory(tmp_path / "esp")
        esd2 = talk_esd_cls.from_esp_directory(tmp_path / "esp")
    assert esd2.esd_name == t100613_esd.esd_name  # header preserves the name exactly
    assert list(esd2.magic) == list(t100613_esd.magic)
    assert set(esd2.state_machines) == {1}


def test_esp_header_type_mismatch_is_rejected(tmp_path):
    from soulstruct.darksouls1r.ezstate import TalkESD

    header = tmp_path / "ESD_Header.esp.py"
    header.write_text("ESD_NAME = 'x.esd'\nESD_TYPE = 'chr'\nMAGIC = [0, 0, 0, 0]\n", encoding="utf-8")
    with pytest.raises(ESDTypeError):
        TalkESD.read_esp_header(header)


def test_esp_header_bad_magic_is_rejected(tmp_path):
    from soulstruct.darksouls1r.ezstate import TalkESD

    header = tmp_path / "ESD_Header.esp.py"
    header.write_text("ESD_NAME = 'x.esd'\nESD_TYPE = 'talk'\nMAGIC = [0, 0]\n", encoding="utf-8")
    with pytest.raises(ValueError):
        TalkESD.read_esp_header(header)


def test_esp_compiler_rejects_non_if_in_test(tmp_path, talk_esd_cls):
    src = (
        '"""TALK ESD STATE MACHINE 1"""\n\n'
        "class State_0(State):\n"
        '    """ 0: x """\n\n'
        "    def test(self):\n"
        "        if MACHINE_CALL_STATUS == 1:\n"
        "            return State_0\n"
        "        return State_0\n"
    )
    path = tmp_path / "t9.esp.py"
    path.write_text(src, encoding="utf-8")
    with pytest.raises(Exception) as exc_info:
        with _quiet():
            talk_esd_cls.from_esp_file(path)
    assert "IF blocks" in str(exc_info.value)


@pytest.mark.xfail(
    reason="M20: `ESPCompiler.get_calls()` handles no `ast.Name`/`ast.Subscript` nodes, so any test "
           "expression using MACHINE_CALL_STATUS / ONGOING / MACHINE_ARGS[i] fails register planning "
           "even though `compile_ezl()` supports them.",
    strict=False,
)
def test_esp_compiler_handles_else_block(tmp_path, talk_esd_cls):
    src = (
        '"""TALK ESD STATE MACHINE 1"""\n\n'
        "class State_0(State):\n"
        '    """ 0: x """\n\n'
        "    def test(self):\n"
        "        if MACHINE_CALL_STATUS == 1:\n"
        "            return State_0\n"
        "        else:\n"
        "            return State_0\n"
    )
    path = tmp_path / "t8.esp.py"
    path.write_text(src, encoding="utf-8")
    with _quiet():
        esd = talk_esd_cls.from_esp_file(path)
    assert len(esd.state_machines[1][0].conditions) == 2


@pytest.mark.xfail(
    reason="H12: `get_called_state_machine()` checks `is_number_literal(node.func.slice.value)`, "
           "which is an `int`, so `CALL_STATE_MACHINE[...]` (emitted by `Command.to_esp()`) never compiles.",
    strict=False,
)
def test_esp_compiler_call_state_machine(tmp_path, talk_esd_cls):
    src = (
        '"""TALK ESD STATE MACHINE 1"""\n\n'
        "class State_0(State):\n"
        '    """ 0: x """\n\n'
        "    def enter(self):\n"
        "        CALL_STATE_MACHINE[2147483647](1, 2)\n\n"
        "    def test(self):\n"
        "        return State_0\n"
    )
    path = tmp_path / "t7.esp.py"
    path.write_text(src, encoding="utf-8")
    with _quiet():
        esd = talk_esd_cls.from_esp_file(path)
    assert esd.state_machines[1][0].enter_commands[0].bank == 6


@pytest.mark.xfail(
    reason="M6: `get_calls()` keys register candidates by function *name* while "
           "`compile_test_function()` keys them by numeric ID, so EZL registers are never emitted.",
    strict=False,
)
def test_esp_compiler_uses_registers_for_repeated_calls(tmp_path, talk_esd_cls):
    src = (
        '"""TALK ESD STATE MACHINE 1"""\n\n'
        "class State_0(State):\n"
        '    """ 0: x """\n\n'
        "    def test(self):\n"
        "        if GetCurrentStateElapsedFrames() > 5 and GetCurrentStateElapsedFrames() < 10:\n"
        "            return State_0\n"
        "        else:\n"
        "            return State_0\n"
    )
    path = tmp_path / "t6.esp.py"
    path.write_text(src, encoding="utf-8")
    with _quiet():
        esd = talk_esd_cls.from_esp_file(path)
    ezl = esd.state_machines[1][0].conditions[0].test_ezl
    # A register save (0xa7-0xae) should appear when a call is used twice.
    assert any(0xa7 <= b <= 0xae for b in ezl), ezl.hex()


def test_condition_to_esp_prints_to_stdout(t100613_esd):
    """M7: `Condition.to_esp()` contains a stray `print(s)`."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        t100613_esd.to_esp(1)
    assert len(buf.getvalue()) > 100, "the stray `print()` in Condition.to_esp() was removed"


def test_esp_compiler_number_encoding():
    from soulstruct.base.ezstate.esd.esp_compiler import ESPCompiler

    assert ESPCompiler.compile_number(0) == b"\x40"
    assert ESPCompiler.compile_number(-64) == b"\x00"
    assert ESPCompiler.compile_number(1000) == b"\x82" + struct.pack("<i", 1000)
    assert ESPCompiler.compile_number(1.5) == b"\x81" + struct.pack("<d", 1.5)
    with pytest.raises(ValueError):
        ESPCompiler.compile_number("x")


@pytest.mark.xfail(
    reason="L10: `compile_number` uses `-64 <= n < 63`, so 63 (encodable as the single byte 0x7f) "
           "is written as a 5-byte int32 instead.",
    strict=False,
)
def test_esp_compiler_number_encoding_upper_bound():
    from soulstruct.base.ezstate.esd.esp_compiler import ESPCompiler

    assert ESPCompiler.compile_number(63) == b"\x7f"


def test_esp_compiler_string_encoding():
    from soulstruct.base.ezstate.esd.esp_compiler import ESPCompiler

    assert ESPCompiler.compile_string("hi") == b"\xa5" + "hi".encode("utf-16-le") + b"\0\0"
    # ...and it must decompile back to the same string.
    assert decompile(ESPCompiler.compile_string("hi") + b"\xa1", TALK) == repr("hi")


def test_esd_write_esp_file_rejects_multiple_state_machines(talk_esd_cls):
    esd = talk_esd_cls(
        magic=[0, 0, 0, 0],
        esd_name="x.esd",
        state_machines={1: {0: State(0)}, 2: {0: State(0)}},
    )
    with pytest.raises(ValueError):
        esd.write_esp_file()
