import ast
import re
import struct
from queue import Queue
from typing import List, Tuple, TYPE_CHECKING

from soulstruct.esd.errors import EsdError, EsdSyntaxError, EsdValueError
from soulstruct.esd.ezl_parser import FUNCTION_ARG_BYTES_BY_COUNT, OPERATORS_BY_NODE
from soulstruct.esd.functions import COMMANDS_BANK_ID_BY_TYPE_NAME, TEST_FUNCTIONS_ID_BY_TYPE_NAME

if TYPE_CHECKING:
    from soulstruct.esd.core import BaseESD


class ESPCompiler(object):

    registers: List[Tuple]
    _STATE_DOCSTRING_RE = re.compile(r'([0-9]+)(:\s*.*)?')
    _COMMAND_DEFAULT_RE = re.compile(r'Command_(?:TALK|CHR)_(\d*)_(\d*)')
    _TEST_DEFAULT_RE = re.compile(r'Test_(?:TALK|CHR)_(\d*)')

    def __init__(self, esp_path, esd_object):
        """ Builds a single state machine. """

        self.ESD = esd_object  # type: BaseESD
        self.docstring = ''
        self.state_machine_index = None
        self.state_info = {}
        self.states = {}

        # Condition state.
        self.registers = [()] * 8
        self.state_call_set = set()
        self.to_write_count = 0
        self.to_write = Queue()  # list of first-time function calls to save for every (sub)condition in order
        self.written = {}  # maps function calls to register index 0-8
        self.current_to_write = []

        with open(esp_path, encoding='utf-8') as script:
            self.tree = ast.parse(script.read())

        self.compile_script()

    def compile_script(self):
        """ Top-level node traversal. Only acceptable nodes at this top level are ImportFrom (for importing your
        constants) and FunctionDef (for your event scripts). """

        self.docstring = ast.get_docstring(self.tree)

        for node in self.tree.body[1:]:

            if isinstance(node, ast.Import):
                raise EsdSyntaxError(node.lineno,
                                     "All imports should be of the form 'from your_constants import *' (other than "
                                     "'from soulstruct.esd import *').")
            elif isinstance(node, ast.ImportFrom):
                # TODO: self.import_constants(node)
                pass
            elif isinstance(node, ast.ClassDef):
                self.scan_state(node)
            else:
                raise EsdSyntaxError(node.lineno,
                                     f"Invalid content: {node.__class__}. The only valid top-level EVS lines are "
                                     f"from-imports and class definitions.")

        for state in self.state_info.values():
            self.states[state['index']] = self.build_state(state['index'], state['nodes'])

    def build_state(self, index, nodes):
        """ Nodes are the non-docstring nodes of the state class definition. """

        index = index
        conditions = []
        enter_commands = []
        exit_commands = []
        ongoing_commands = []

        for node in nodes:
            if not isinstance(node, ast.FunctionDef):
                raise EsdSyntaxError(node.lineno, "Non-function appeared in state class.")

            if node.name == 'previous_states':
                # Ignore informative method.
                continue
            elif node.name == 'test':
                if conditions:
                    raise EsdSyntaxError(node.lineno, "test() method defined more than once.")
                conditions = self.build_conditions(node.body)
            elif node.name == 'enter':
                if enter_commands:
                    raise EsdSyntaxError(node.lineno, "enter() method defined more than once.")
                enter_commands = [self.build_command(command_node) for command_node in node.body]
            elif node.name == 'exit':
                if exit_commands:
                    raise EsdSyntaxError(node.lineno, "exit() method defined more than once.")
                exit_commands = [self.build_command(command_node) for command_node in node.body]
            elif node.name == 'ongoing':
                if ongoing_commands:
                    raise EsdSyntaxError(node.lineno, "ongoing() method defined more than once.")
                ongoing_commands = [self.build_command(command_node) for command_node in node.body]
            else:
                raise EsdSyntaxError(node.lineno, f"Unexpected state function: '{node.name.id}'.")

        return self.ESD.State(self.ESD.esd_type, index, conditions, enter_commands, exit_commands, ongoing_commands)

    def scan_state(self, node):
        """ Get state name. """
        state_name = node.name
        docstring = ast.get_docstring(node)
        if docstring is None:
            raise EsdSyntaxError(node.lineno, f"No docstring given for state {state_name}.")
        try:
            state_index, description = self._STATE_DOCSTRING_RE.match(docstring).group(1, 2)
        except AttributeError:
            raise EsdSyntaxError(node.lineno, f"Invalid docstring for event {state_name}.")
        self.state_info[state_name] = {
            'index': int(state_index),
            'description': description,
            'nodes': node.body[1:],  # skip docstring
        }

    def build_command(self, node):
        """ Pass in the body of a function def, or a list of nodes before 'return' in a test block. """
        if self.is_state_machine_call(node):
            bank = 6  # TODO: True in every game/file?
            f_id = 0x80000000 - node.value.func.slice.value.n
            if not isinstance(f_id, int):
                raise EsdValueError(node.lineno, "State machine call must have an integer index.")
        elif self.is_call(node):
            try:
                bank, f_id = COMMANDS_BANK_ID_BY_TYPE_NAME[self.ESD.esd_type, node.value.func.id]
            except KeyError:
                command_match = self._COMMAND_DEFAULT_RE.match(node.value.func.id)
                if not command_match:
                    raise EsdError(node.lineno, f"Invalid enter/exit/ongoing command: {node.value.func.id}")
                bank, f_id = command_match.group(1, 2)
                bank, f_id = int(bank), int(f_id)
        else:
            raise EsdSyntaxError(node.lineno, f"Expected only function calls, not node type {type(node)}.")
        # TODO: Check arg count against canonical function, once available, and order keyword args.
        args = node.value.args + [keyword.value for keyword in node.value.keywords]
        command_args = [self.compile_ezl(arg) + b'\xa1' for arg in args]
        return self.ESD.Command(self.ESD.esd_type, bank, f_id, command_args)

    def reset_condition_registers(self):
        self.registers = [()] * 8
        self.state_call_set = set()
        self.to_write_count = 0  # number of registers used; cannot exceed 8.
        self.to_write = Queue()  # queue of first-time function calls to save for every (sub)condition in order
        self.written = {}  # maps function calls to register index 0-8
        self.current_to_write = []

    def build_conditions(self, if_nodes):
        """ Each node in the test() method should be an IF block containing:
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
                if (isinstance(if_nodes[0].value.op, ast.USub) and isinstance(if_nodes[0].value.operand, ast.Num)
                        and if_nodes[0].value.operand.n == 1):
                    # Last state of callable state machine.
                    return [self.ESD.Condition(self.ESD.esd_type, -1, b'\x41\xa1', [], [])]
                print(if_nodes[0].value.op, if_nodes[0].value.operand)
                raise EsdSyntaxError(if_nodes[0].lineno, f"Next state must be a valid State class or -1.")
            if not isinstance(if_nodes[0].value, ast.Name):
                print("Node:", if_nodes[0].value)
                raise EsdSyntaxError(if_nodes[0].lineno, "Condition IF block should return a state class name.")
            if if_nodes[0].value.id not in self.state_info:
                raise EsdError(if_nodes[0].lineno, f"Could not find a state class named '{if_nodes[0].value.id}'.")
            next_state_index = self.state_info[if_nodes[0].value.id]['index']
            return [self.ESD.Condition(self.ESD.esd_type, next_state_index, b'\x41\xa1', [], [])]

        for i, node in enumerate(if_nodes):
            if not isinstance(node, ast.If):
                raise EsdSyntaxError(node.lineno, "test() method must contain only IF blocks.")
            if node.orelse:
                if i != len(if_nodes) - 1:
                    raise EsdSyntaxError(node.lineno, "'else' block should only appear at the end of the tests.")
                if_nodes.append(ast.If(test=ast.Num(n=1), body=node.orelse, orelse=[]))

        conditions = []
        self.plan_condition_registers(if_nodes)  # Determines upcoming register saves/loads.

        for if_node in if_nodes:

            self.current_to_write = self.to_write.get()  # type: list
            test_ezl = self.compile_ezl(if_node.test) + b'\xa1'

            pass_commands = []
            subcondition_nodes = []
            next_state_index = -1

            pass_commands_allowed = True
            subconditions_allowed = True

            for j, node in enumerate(if_node.body):
                if self.is_call(node):
                    if not pass_commands_allowed:
                        raise EsdSyntaxError(node.lineno, "Encountered a pass command out of order in IF block.")
                    pass_commands.append(self.build_command(node))
                elif isinstance(node, ast.If):
                    if not subconditions_allowed:
                        raise EsdSyntaxError(node.lineno, "Encountered a subcondition out of order in IF block.")
                    pass_commands_allowed = False
                    subcondition_nodes.append(node)
                elif isinstance(node, ast.Return):
                    if j != len(if_node.body) - 1:
                        raise EsdSyntaxError(node.lineno, "'return NextState' should be last statement in IF block.")
                    if isinstance(node.value, ast.Num) and node.value.n == -1:
                        # Last state of callable state machine.
                        next_state_index = -1
                    else:
                        if not isinstance(node.value, ast.Name):
                            raise EsdSyntaxError(node.lineno, "Condition IF block should return a state class name.")
                        if node.value.id not in self.state_info:
                            raise EsdError(node.lineno, f"Could not find a state class named '{node.value.id}'.")
                        next_state_index = self.state_info[node.value.id]['index']

            # Condition registers are *not* reset when scanning and building subconditions.
            subconditions = self.build_conditions(subcondition_nodes) if subcondition_nodes else ()

            conditions.append(self.ESD.Condition(self.ESD.esd_type, next_state_index, test_ezl,
                                                 pass_commands, subconditions))

        return conditions

    def plan_condition_registers(self, if_node_list):
        """ Recursively scans conditions and any subconditions, determines the first eight repeated function calls that
        will be saved in/loaded from registers during build, and records their conditions in a queue.

        I have no idea how the original ESD compiler determines which functions to store in registers, given their
        limited availability. I'm simply storing the first eight functions that are used for a second time. I'm also
        assuming that the same registers are used for all subconditions.

        TODO: At least verify that subconditions use the same register state as parent conditions (check enemyCommon).
        """
        for i, if_node in enumerate(if_node_list):
            if not isinstance(if_node, ast.If):
                raise EsdSyntaxError(if_node.lineno, "test() method must contain only IF blocks.")

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
                        raise EsdSyntaxError(body_node.lineno, "Encountered a subcondition out of order in IF block.")
                    subcondition_nodes.append(body_node)
            self.plan_condition_registers(subcondition_nodes)

    @staticmethod
    def parse_args(arg_nodes):
        args = []
        for node in arg_nodes:
            if isinstance(node, ast.Num):
                args.append(node.n)
            elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                args.append(-node.operand.n)
            elif isinstance(node, (ast.Subscript, ast.Name)):
                args.append(node)
            else:
                raise EsdValueError(node.lineno, "Function arguments must be numeric literals.")
        return tuple(args)

    def save_into_next_available_register(self, call):
        for i in range(len(self.registers)):
            if not self.registers[i]:
                self.registers[i] = call
                self.current_to_write.remove(call)
                return struct.pack('B', i + 167)

    def compile_test_function(self, call_node: ast.Call, equals=None):
        if call_node.keywords:
            raise EsdSyntaxError(call_node.lineno, "You cannot use keyword arguments in test functions (yet).")
        try:
            f_id = TEST_FUNCTIONS_ID_BY_TYPE_NAME[self.ESD.esd_type, call_node.func.id]
        except KeyError:
            try:
                f_id = int(self._TEST_DEFAULT_RE.match(call_node.func.id).group(1))
            except AttributeError:
                raise EsdValueError(call_node.lineno, f"Invalid ESD function name: '{call_node.func.id}'.")
        args = self.parse_args(call_node.args)
        call = (f_id, *args)

        if call in self.registers:
            # Load from register.
            return struct.pack('B', self.registers.index(call) + 175)

        compiled = self.compile_number(f_id) + b''.join(self.compile_ezl(arg) for arg in args)
        compiled += FUNCTION_ARG_BYTES_BY_COUNT[len(args)]
        if call in self.current_to_write:
            compiled += self.save_into_next_available_register(call)
            self.current_to_write.remove(call)
        if equals is not None:
            if equals == 0:
                compiled += b'\x40\x95'
            elif equals == 1:
                compiled += b'\x41\x95'
            else:
                raise ValueError("Internal error: 'equals' arg should only be 0 or 1 (or None).")
        return compiled

    def compile_ezl(self, node):

        if isinstance(node, (int, float)):
            return self.compile_number(node)

        if isinstance(node, ast.Num):
            return self.compile_number(node.n)

        if isinstance(node, str):
            return self.compile_string(node)

        if isinstance(node, ast.Str):
            return self.compile_string(node.s)

        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                if isinstance(node.operand, ast.Num):
                    return self.compile_number(-node.operand.n)
                raise EsdSyntaxError(node.lineno, "Tried to negate a non-numeric value. (TODO: Implement Negate op.)")
            elif isinstance(node.op, ast.Not):
                if self.is_call(node.operand):
                    return self.compile_test_function(node.operand, equals=1)
                raise EsdSyntaxError(node.lineno, "'not' keyword can only be applied to function calls.")

        if isinstance(node, ast.BoolOp):
            compiled = b''
            is_and = True if isinstance(node.op, ast.And) else False  # must be Or if false
            for i, value in enumerate(node.values):
                compiled += self.compile_ezl(value)
                if is_and and not self.current_to_write:
                    # There are no register writes remaining in this test, and no need to continue evaluation either.
                    # Append 'terminate if false' symbol for efficiency.
                    compiled += b'\xb7'
                else:
                    # Append 'continue if false' symbol for some reason. TODO: Is this necessary? When?
                    compiled += b'\xa6'
                if i > 0:
                    # Operator is added *per value*, as the chained comparison in Python is represented by one node.
                    compiled += b'\x98' if is_and else b'\x99'
            return compiled

        if isinstance(node, ast.BinOp):
            if type(node.op) not in OPERATORS_BY_NODE:
                raise EsdSyntaxError(node.lineno, f"Invalid binary operator: {type(node.op)}")
            return self.compile_ezl(node.left) + self.compile_ezl(node.right) + OPERATORS_BY_NODE[type(node.op)]

        if isinstance(node, ast.Compare):
            if len(node.comparators) != 1 or len(node.ops) != 1:
                # TODO: Redundant after scan. Have to figure out which errors are checked where.
                raise EsdSyntaxError(node.lineno, "Comparison should compare exactly two values.")
            if type(node.ops[0]) not in OPERATORS_BY_NODE:
                raise EsdSyntaxError(node.lineno, f"Invalid comparison operator: {type(node.ops[0])}")
            return (self.compile_ezl(node.left) + self.compile_ezl(node.comparators[0])
                    + OPERATORS_BY_NODE[type(node.ops[0])])

        if isinstance(node, ast.Call):
            return self.compile_test_function(node)

        if isinstance(node, ast.Name):
            if node.id == 'MACHINE_CALL_STATUS':
                return b'\xb9'
            elif node.id == 'ONGOING':
                return b'\xba'
            raise EsdSyntaxError(node.lineno, "Only valid name symbols are MACHINE_CALL_STATUS and ONGOING.")

        if isinstance(node, ast.Subscript):
            if (isinstance(node.value, ast.Name) and node.value.id == 'MACHINE_ARGS'
                    and isinstance(node.slice, ast.Index) and isinstance(node.slice.value, ast.Num)):
                return self.compile_number(node.slice.value.n) + b'\xb8'
            raise EsdSyntaxError(node.lineno, "Only valid subscripted symbol is MACHINE_ARGS[i].")

        raise TypeError(f"Invalid node type appeared in condition test: {type(node)}.\n"
                        f"Conditions must be bools, boolean ops, comparisons, function calls, or a permitted name.")

    @staticmethod
    def compile_number(n):
        if isinstance(n, int):
            if -64 <= n < 63:
                return struct.pack('B', n + 64)
            return b'\x82' + struct.pack('<i', n)
        elif isinstance(n, float):
            # TODO: How can I determine if I should write a single or double?
            #  I guess I could just always write a double.
            #  Or, maybe certain resources only use singles OR doubles.
            # return b'\x80' + struct.pack('<f', n)
            return b'\x81' + struct.pack('<d', n)  # Always double for now.
        else:
            raise ValueError(f"Cannot compile number {n} of type {type(n)}.")

    @staticmethod
    def compile_string(s):
        return b'\xa5' + s.encode('utf-16le') + b'\0\0'

    def get_calls(self, node):
        """ Returns a list of calls contained inside the given test node.

        Returns a list of call tuples (f_id, arg1, arg2, ...).
        """
        if self.is_bool(node) or isinstance(node, (ast.Name, ast.Num)):
            return []

        elif isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, (ast.Not, ast.USub)):
                # TODO: The only other unary operator is UAdd, which is harmless.
                # TODO: Not true, there's also Invert, which shouldn't be allowed.
                raise EsdSyntaxError(node.lineno, f"Only unary operators allowed are 'not' and '-', not {type(node)}.")
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
                raise EsdSyntaxError(node.lineno, "Comparison should compare exactly two values.")
            return self.get_calls(node.left) + self.get_calls(node.comparators[0])

        elif isinstance(node, ast.Call):
            function_name = node.func.id
            return [(function_name, *self.parse_args(node.args))]

        raise EsdSyntaxError(node.lineno, f"Invalid node type appeared in condition: {type(node)}\n"
                                          f"Conditions must be bools, boolean ops, comparisons, or function calls.")

    @staticmethod
    def is_bool(node):
        return isinstance(node, ast.NameConstant) and node.value in {True, False}

    @staticmethod
    def is_call(node):
        return isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)

    @staticmethod
    def is_state_machine_call(node):
        return (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Subscript)
                and isinstance(node.value.func.value, ast.Name) and node.value.func.value.id == 'CALL_STATE_MACHINE'
                and isinstance(node.value.func.slice, ast.Index) and isinstance(node.value.func.slice.value, ast.Num))

    @staticmethod
    def get_ast_sequence(node):
        """ List/tuple can only contain literals. """
        if isinstance(node, (ast.Tuple, ast.List)):
            t = []
            for e in node.elts:
                if isinstance(e, ast.Num):
                    t.append(e.n)
                elif isinstance(e, ast.Str):
                    t.append(e.s)
                else:
                    raise EsdValueError(node.lineno, f"Sequences must contain only numeric/string literals.")
            return t
        raise EsdSyntaxError(node.lineno, f"Expected a list or tuple node, but found: {type(node)}")
