from __future__ import annotations

__all__ = ["ESPCompiler"]

import ast
import re
import struct
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path
from queue import Queue

from .esd_type import ESDType
from .exceptions import ESDError, ESDSyntaxError, ESDValueError
from .ezl_parser import FUNCTION_ARG_BYTES_BY_COUNT, OPERATORS_BY_NODE
from .functions import COMMANDS_BANK_ID_BY_TYPE_NAME, TEST_FUNCTIONS_ID_BY_TYPE_NAME
from .command import Command
from .condition import Condition
from .state import State


_STATE_DOCSTRING_RE = re.compile(r"([0-9]+)(:\s*.*)?")
_COMMAND_DEFAULT_RE = re.compile(r"Command_(?:talk|chr)_(\d*)_(\d*)")
_TEST_DEFAULT_RE = re.compile(r"Test_(?:talk|chr)_(\d*)")


@dataclass(slots=True)
class ESPCompiler:
    """Builds a single ESD state machine. """

    esp_path: Path
    esd_type: ESDType
    docstring: str = ""
    state_info: dict = field(default_factory=dict)
    states: dict[int, State] = field(default_factory=dict)

    registers: list[tuple] = field(default_factory=lambda: [()] * 8)
    state_call_set: set = field(default_factory=set)
    to_write_count: int = 0
    # List of first-time function calls to save for every (sub)condition in order.
    to_write: Queue = field(default_factory=Queue)
    # Maps function calls to register index 0-8.
    written: dict = field(default_factory=dict)
    current_to_write: list = field(default_factory=list)

    tree: ast.Module = field(init=False)

    def __post_init__(self):
        with open(self.esp_path, encoding="utf-8") as script:
            self.tree = ast.parse(script.read())

        self.compile_script()

    def compile_script(self):
        """Top-level node traversal.

        The only acceptable nodes at this top level are ImportFrom (for importing your constants) and FunctionDef (for
        your event scripts).
        """
        self.docstring = ast.get_docstring(self.tree)

        for node in self.tree.body[1:]:

            if isinstance(node, ast.Import):
                raise ESDSyntaxError(
                    node.lineno,
                    "All imports should be of the form 'from your_constants import *' (other than "
                    "'from soulstruct.{game}.ezstate.esd.functions import *').",
                )
            elif isinstance(node, ast.ImportFrom):
                # TODO: self.import_constants(node)
                pass
            elif isinstance(node, ast.ClassDef):
                self.scan_state(node)
            else:
                raise ESDSyntaxError(
                    node.lineno,
                    f"Invalid content: {node.__class__}. The only valid top-level EVS lines are "
                    f"from-imports and class definitions.",
                )

        for state in self.state_info.values():
            self.states[state["state_id"]] = self.build_state(state["state_id"], state["nodes"])

    def build_state(self, state_id, nodes):
        """`nodes` is a sequence of the non-docstring nodes of the state class definition."""
        state_id = state_id
        conditions = []
        enter_commands = []
        exit_commands = []
        ongoing_commands = []

        for node in nodes:
            if not isinstance(node, ast.FunctionDef):
                raise ESDSyntaxError(node.lineno, "Non-function appeared in state class.")

            if node.name == "previous_states":
                # Ignore informative method.
                continue
            elif node.name == "test":
                if conditions:
                    raise ESDSyntaxError(node.lineno, "test() method defined more than once.")
                conditions = self.build_conditions(node.body)
            elif node.name == "enter":
                if enter_commands:
                    raise ESDSyntaxError(node.lineno, "enter() method defined more than once.")
                enter_commands = [self.build_command(command_node) for command_node in node.body]
            elif node.name == "exit":
                if exit_commands:
                    raise ESDSyntaxError(node.lineno, "exit() method defined more than once.")
                exit_commands = [self.build_command(command_node) for command_node in node.body]
            elif node.name == "ongoing":
                if ongoing_commands:
                    raise ESDSyntaxError(node.lineno, "ongoing() method defined more than once.")
                ongoing_commands = [self.build_command(command_node) for command_node in node.body]
            else:
                raise ESDSyntaxError(node.lineno, f"Unexpected state function: '{node.name}'.")

        return State(state_id, conditions, enter_commands, exit_commands, ongoing_commands)

    def scan_state(self, node):
        """Get state name, description (from docstring), and node list."""
        state_name = node.name
        docstring = ast.get_docstring(node)
        if docstring is None:
            raise ESDSyntaxError(node.lineno, f"No docstring given for state {state_name}.")
        try:
            state_id, description = _STATE_DOCSTRING_RE.match(docstring).group(1, 2)
        except AttributeError:
            raise ESDSyntaxError(node.lineno, f"Invalid docstring for event {state_name}.")
        self.state_info[state_name] = {
            "state_id": int(state_id),
            "description": description,
            "nodes": node.body[1:],  # skip docstring
        }

    def build_command(self, node: ast.stmt):
        """Pass in the body of a function def, or a list of nodes before 'return' in a test block."""
        call_node = get_call(node)
        if call_node is None:
            raise ESDSyntaxError(node.lineno, f"Expected only function calls, not node type {type(node)}.")

        if (sm_index := get_called_state_machine(call_node)) is not None:
            bank = 6  # TODO: True in every game/file?
            f_id = 0x80000000 - sm_index
            if not isinstance(f_id, int):
                raise ESDValueError(node.lineno, "State machine call must have an integer index.")
        else:
            if not isinstance(call_node.func, ast.Name):
                raise ESDError(node.lineno, f"Could not parse function call node: {call_node}. Must be just a name.")
            try:
                bank, f_id = COMMANDS_BANK_ID_BY_TYPE_NAME[self.esd_type, call_node.func.id]
            except KeyError:
                command_match = _COMMAND_DEFAULT_RE.match(call_node.func.id)
                if not command_match:
                    raise ESDError(node.lineno, f"Invalid enter/exit/ongoing command: {call_node.func.id}")
                bank, f_id = command_match.group(1, 2)
                bank, f_id = int(bank), int(f_id)

        # TODO: Check arg count against canonical function, once available, and order keyword args.
        args = call_node.args + [keyword.value for keyword in call_node.keywords]
        command_args = [self.compile_ezl(arg) + b"\xa1" for arg in args]
        return Command(bank, f_id, command_args)

    def reset_condition_registers(self):
        self.registers = [()] * 8
        self.state_call_set = set()
        self.to_write_count = 0  # number of registers used; cannot exceed 8.
        self.to_write = Queue()  # queue of first-time function calls to save for every (sub)condition in order
        self.written = {}  # maps function calls to register index 0-8
        self.current_to_write = []

    def build_conditions(self, if_nodes):
        """Each node in the test() method should be an IF block containing:
            - optional sequence of 'pass commands'
            - optional sequence of subcondition IF blocks
            - optional return statement specifying a state class name to change to

        I'm only guessing that the 'pass commands' are run before the subconditions. In most resources (e.g. talk
        resources), pass command and subconditions are not used, but they are used extensively in, say, enemyCommon.esd,
        which is the core file controlling dynamic behavior in DS1.

        Returns a list of Condition instances.
        """
        if len(if_nodes) == 1 and isinstance(if_nodes[0], ast.Return):
            if isinstance(if_nodes[0].value, ast.UnaryOp):
                if (
                    isinstance(if_nodes[0].value.op, ast.USub)
                    and is_number_literal(if_nodes[0].value.operand)
                    and if_nodes[0].value.operand.value == 1
                ):
                    # Last state of callable state machine.
                    return [Condition(-1, b"\x41\xa1", [], [])]
                print(if_nodes[0].value.op, if_nodes[0].value.operand)
                raise ESDSyntaxError(if_nodes[0].lineno, f"Next state must be a valid State class or -1.")
            if not isinstance(if_nodes[0].value, ast.Name):
                print("Node:", if_nodes[0].value)
                raise ESDSyntaxError(if_nodes[0].lineno, "Condition IF block should return a state class name.")
            if if_nodes[0].value.id not in self.state_info:
                raise ESDError(if_nodes[0].lineno, f"Could not find a state class named '{if_nodes[0].value.id}'.")
            next_state_id = self.state_info[if_nodes[0].value.id]["state_id"]
            return [Condition(next_state_id, b"\x41\xa1", [], [])]

        for i, node in enumerate(if_nodes):
            if not isinstance(node, ast.If):
                raise ESDSyntaxError(node.lineno, "test() method must contain only IF blocks.")
            if node.orelse:
                if i != len(if_nodes) - 1:
                    raise ESDSyntaxError(node.lineno, "'else' block should only appear at the end of the tests.")
                if_nodes.append(
                    ast.If(
                        test=ast.Constant(value=1),
                        body=node.orelse,
                        orelse=[],
                    )
                )

        conditions = []
        self.plan_condition_registers(if_nodes)  # Determines upcoming register saves/loads.

        for if_node in if_nodes:

            self.current_to_write = self.to_write.get()  # type: list
            test_ezl = self.compile_ezl(if_node.test) + b"\xa1"

            pass_commands = []
            subcondition_nodes = []
            next_state_id = -1

            pass_commands_allowed = True
            subconditions_allowed = True

            for j, node in enumerate(if_node.body):
                if get_call(node):
                    if not pass_commands_allowed:
                        raise ESDSyntaxError(node.lineno, "Encountered a pass command out of order in IF block.")
                    pass_commands.append(self.build_command(node))
                elif isinstance(node, ast.If):
                    if not subconditions_allowed:
                        raise ESDSyntaxError(node.lineno, "Encountered a subcondition out of order in IF block.")
                    pass_commands_allowed = False
                    subcondition_nodes.append(node)
                elif isinstance(node, ast.Return):
                    if j != len(if_node.body) - 1:
                        raise ESDSyntaxError(node.lineno, "'return NextState' should be last statement in IF block.")
                    if isinstance(node.value, ast.Constant) and node.value.n == -1:
                        # Last state of callable state machine.
                        next_state_id = -1
                    else:
                        if not isinstance(node.value, ast.Name):
                            raise ESDSyntaxError(node.lineno, "Condition IF block should return a state class name.")
                        if node.value.id not in self.state_info:
                            raise ESDError(node.lineno, f"Could not find a state class named '{node.value.id}'.")
                        next_state_id = self.state_info[node.value.id]["state_id"]

            # Condition registers are *not* reset when scanning and building subconditions.
            subconditions = self.build_conditions(subcondition_nodes) if subcondition_nodes else ()

            conditions.append(
                Condition(next_state_id, test_ezl, pass_commands, subconditions)
            )

        return conditions

    def plan_condition_registers(self, if_node_list):
        """Recursively scans conditions and any subconditions, determines the first eight repeated function calls that
        will be saved in/loaded from registers during build, and records their conditions in a queue.

        I have no idea how the original ESD compiler determines which functions to store in registers, given their
        limited availability. I'm simply storing the first eight functions that are used for a second time. I'm also
        assuming that the same registers are used for all subconditions.

        TODO: At least verify that subconditions use the same register state as parent conditions (check enemyCommon).
        """
        for i, if_node in enumerate(if_node_list):
            if not isinstance(if_node, ast.If):
                raise ESDSyntaxError(if_node.lineno, "test() method must contain only IF blocks.")

            # Process test nodes.
            first_time_calls = []
            call_list = self.get_calls(if_node.test)
            for call in call_list:
                if call in self.state_call_set and self.to_write_count < 8:
                    # Call occurs more than once, so we will use a register for it.
                    first_time_calls.append(call)
                    self.to_write_count += 1
                else:
                    self.state_call_set.add(call)
            self.to_write.put(first_time_calls)  # add to queue

            # Find and recursively process subconditions under the same register state. Order of encountered IF blocks
            # will be preserved in the 'to_write' queue.
            subconditions_allowed = True
            subcondition_nodes = []
            for body_node in if_node.body:
                if not isinstance(body_node, ast.If):
                    subconditions_allowed = False
                elif isinstance(body_node, ast.If):
                    if not subconditions_allowed:
                        raise ESDSyntaxError(body_node.lineno, "Encountered a subcondition out of order in IF block.")
                    subcondition_nodes.append(body_node)
            self.plan_condition_registers(subcondition_nodes)

    @staticmethod
    def parse_args(arg_nodes):
        args = []
        for node in arg_nodes:
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                args.append(node.value)
            elif (
                isinstance(node, ast.UnaryOp)
                and isinstance(node.op, ast.USub)
                and is_number_literal(node.operand)
            ):
                args.append(-node.operand.value)
            elif isinstance(node, (ast.Subscript, ast.Name)):
                args.append(node)
            else:
                raise ESDValueError(node.lineno, "Function arguments must be numeric literals.")
        return tuple(args)

    def save_into_next_available_register(self, call):
        for i in range(len(self.registers)):
            if not self.registers[i]:
                self.registers[i] = call
                self.current_to_write.remove(call)
                return struct.pack("B", i + 167)

    def compile_test_function(self, call_node: ast.Call, equals=None):
        if call_node.keywords:
            raise ESDSyntaxError(call_node.lineno, "You cannot use keyword arguments in test functions (yet).")
        if not isinstance(call_node.func, ast.Name):
            raise ESDSyntaxError(
                call_node.lineno, f"Test function call must be a simple function name, not: {call_node.func}"
            )
        try:
            f_id = TEST_FUNCTIONS_ID_BY_TYPE_NAME[self.esd_type, call_node.func.id]
        except KeyError:
            try:
                f_id = int(_TEST_DEFAULT_RE.match(call_node.func.id).group(1))
            except AttributeError:
                raise ESDValueError(call_node.lineno, f"Invalid ESD function name: '{call_node.func.id}'.")
        args = self.parse_args(call_node.args)
        call = (f_id, *args)

        if call in self.registers:
            # Load from register.
            return struct.pack("B", self.registers.index(call) + 175)

        compiled = self.compile_number(f_id) + b"".join(self.compile_ezl(arg) for arg in args)
        compiled += FUNCTION_ARG_BYTES_BY_COUNT[len(args)]
        if call in self.current_to_write:
            compiled += self.save_into_next_available_register(call)
            self.current_to_write.remove(call)
        if equals is not None:
            if equals == 0:
                compiled += b"\x40\x95"
            elif equals == 1:
                compiled += b"\x41\x95"
            else:
                raise ValueError("Internal error: 'equals' arg should only be 0 or 1 (or None).")
        return compiled

    def compile_ezl(self, node):

        if isinstance(node, (int, float)):
            return self.compile_number(node)

        if is_number_literal(node):
            return self.compile_number(node.value)

        if isinstance(node, str):
            return self.compile_string(node)

        if is_string_literal(node):
            return self.compile_string(node.value)

        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                if is_number_literal(node.operand):
                    return self.compile_number(-node.operand.value)
                raise ESDSyntaxError(node.lineno, "Tried to negate a non-numeric value. (TODO: Implement Negate op.)")
            elif isinstance(node.op, ast.Not):
                if call_node := get_call(node.operand):
                    return self.compile_test_function(call_node, equals=1)
                raise ESDSyntaxError(node.lineno, "'not' keyword can only be applied to function calls.")

        if isinstance(node, ast.BoolOp):
            compiled = b""
            is_and = True if isinstance(node.op, ast.And) else False  # must be Or if false
            for i, value in enumerate(node.values):
                compiled += self.compile_ezl(value)
                if is_and and not self.current_to_write:
                    # There are no register writes remaining in this test, and no need to continue evaluation either.
                    # Append 'terminate if false' symbol for efficiency.
                    compiled += b"\xb7"
                else:
                    # Append 'continue if false' symbol for some reason. TODO: Is this necessary? When?
                    compiled += b"\xa6"
                if i > 0:
                    # Operator is added *per value*, as the chained comparison in Python is represented by one node.
                    compiled += b"\x98" if is_and else b"\x99"
            return compiled

        if isinstance(node, ast.BinOp):
            if type(node.op) not in OPERATORS_BY_NODE:
                raise ESDSyntaxError(node.lineno, f"Invalid binary operator: {type(node.op)}")
            return self.compile_ezl(node.left) + self.compile_ezl(node.right) + OPERATORS_BY_NODE[type(node.op)]

        if isinstance(node, ast.Compare):
            if len(node.comparators) != 1 or len(node.ops) != 1:
                # TODO: Redundant after scan. Have to figure out which errors are checked where.
                raise ESDSyntaxError(node.lineno, "Comparison should compare exactly two values.")
            if type(node.ops[0]) not in OPERATORS_BY_NODE:
                raise ESDSyntaxError(node.lineno, f"Invalid comparison operator: {type(node.ops[0])}")
            return (
                self.compile_ezl(node.left)
                + self.compile_ezl(node.comparators[0])
                + OPERATORS_BY_NODE[type(node.ops[0])]
            )

        if isinstance(node, ast.Call):
            return self.compile_test_function(node)

        if isinstance(node, ast.Name):
            if node.id == "MACHINE_CALL_STATUS":
                return b"\xb9"
            elif node.id == "ONGOING":
                return b"\xba"
            raise ESDSyntaxError(node.lineno, "Only valid name symbols are MACHINE_CALL_STATUS and ONGOING.")

        if isinstance(node, ast.Subscript):
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "MACHINE_ARGS"
                and is_number_literal(node.slice)
            ):
                return self.compile_number(node.slice.value) + b"\xb8"
            raise ESDSyntaxError(node.lineno, "Only valid subscripted symbol is `MACHINE_ARGS[i]`.")

        raise TypeError(
            f"Invalid node type appeared in condition test: {type(node)}.\n"
            f"Conditions must be bools, boolean ops, comparisons, function calls, or a permitted name."
        )

    @staticmethod
    def compile_number(n):
        if isinstance(n, int):
            if -64 <= n < 63:
                return struct.pack("B", n + 64)
            return b"\x82" + struct.pack("<i", n)
        elif isinstance(n, float):
            # TODO: How can I determine if I should write a single or double?
            #  Maybe certain resources only use singles OR doubles.
            #  For now, I'm just always writing a double.
            # return b'\x80' + struct.pack('<f', n)
            return b"\x81" + struct.pack("<d", n)  # Always double for now.
        else:
            raise ValueError(f"Cannot compile number {n} of type {type(n)}.")

    @staticmethod
    def compile_string(s):
        return b"\xa5" + s.encode("utf-16le") + b"\0\0"

    def get_calls(self, node) -> list[tuple]:
        """Recursively collects a list of call tuples (f_id, arg1, arg2, ...) contained inside the given test node."""
        if isinstance(node, ast.Constant):
            return []

        elif isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, (ast.Not, ast.USub)):
                # TODO: The only other unary operator is UAdd, which is harmless.
                # TODO: Not true, there's also Invert, which shouldn't be allowed.
                raise ESDSyntaxError(node.lineno, f"Only unary operators allowed are 'not' and '-', not {type(node)}.")
            return self.get_calls(node.operand)

        elif isinstance(node, ast.BoolOp):
            call_list = []
            for value in node.values:
                call_list += self.get_calls(value)
            return call_list

        elif isinstance(node, ast.BinOp):
            return self.get_calls(node.left) + self.get_calls(node.right)

        elif isinstance(node, ast.Compare):
            if len(node.comparators) != 1:
                raise ESDSyntaxError(node.lineno, "Comparison should compare exactly two values.")
            return self.get_calls(node.left) + self.get_calls(node.comparators[0])

        elif isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ESDSyntaxError(
                    node.lineno, f"Function call must be a simple function name, not: {node.func}"
                )
            function_name = node.func.id
            return [(function_name, *self.parse_args(node.args))]

        raise ESDSyntaxError(
            node.lineno,
            f"Invalid node type appeared in condition: {type(node)}\n"
            f"Conditions must be bools, boolean ops, comparisons, or function calls.",
        )

    @staticmethod
    def get_ast_sequence(node) -> list[str | int]:
        """List/tuple can only contain numeric/string literals."""
        if isinstance(node, (ast.Tuple, ast.List)):
            t = []
            for e in node.elts:
                if isinstance(e, ast.Constant) and isinstance(e.value, (int, float, str)):
                    t.append(e.value)
                else:
                    raise ESDValueError(node.lineno, f"Sequences must contain only numeric/string literals.")
            return t
        raise ESDSyntaxError(node.lineno, f"Expected a list or tuple node, but found: {type(node)}")


# region Node Type Guards

def is_number_literal(node: ast.AST) -> tp.TypeGuard[ast.Constant]:
    return isinstance(node, ast.Constant) and isinstance(node.value, (int, float))


def is_integer_literal(node: ast.AST) -> tp.TypeGuard[ast.Constant]:
    return isinstance(node, ast.Constant) and isinstance(node.value, int)


def is_string_literal(node: ast.AST) -> tp.TypeGuard[ast.Constant]:
    return isinstance(node, ast.Constant) and isinstance(node.value, str)


def is_bool(node: ast.AST) -> tp.TypeGuard[ast.Constant]:
    return isinstance(node, ast.Constant) and isinstance(node.value, bool)


def get_call(node: ast.AST) -> ast.Call | None:
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        return node.value
    return None


def get_called_state_machine(node: ast.Call) -> int | None:
    """Returns the index of the called state machine if the node is a CALL_STATE_MACHINE call, or None otherwise.

    For example:
        `CALL_STATE_MACHINE[0x79999998](arg1, arg2)` -> 0x79999998
    """
    if (
        isinstance(node.func, ast.Subscript)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "CALL_STATE_MACHINE"
        and isinstance(node.func.slice, ast.Constant)
        and is_number_literal(node.func.slice.value)
    ):
        return node.func.slice.value.value
    return None
