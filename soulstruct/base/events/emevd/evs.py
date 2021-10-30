__all__ = ["EVSParser", "EVSError"]

import abc
import ast
import importlib
import importlib.util  # TODO: needed? IDE doesn't think so...
import logging
import re
import typing as tp
from functools import partial
from pathlib import Path

import soulstruct.game_types as gt
from soulstruct.utilities.files import import_arbitrary_file
from .exceptions import NoNegateError, NoSkipOrReturnError
from .numeric import SET_INSTRUCTION_ARG_TYPES
from .utils import (
    COMPARISON_NODES,
    NEG_COMPARISON_NODES,
    ConstantCondition,
    EventArgumentData,
    format_event_layers,
    get_write_offset,
)

_LOGGER = logging.getLogger(__name__)


# TODO: Set up unit tests on vanilla scripts, and some examples that make use of high-level functionality.
# TODO: Support event function imports from '.common_func', including kwarg names.


_RESTART_TYPES = {"NeverRestart": 0, "RestartOnRest": 1, "UnknownRestart": 2}  # avoiding circular import
_EVENT_DOCSTRING_RE = re.compile(r"(\w+ )?([0-9]+)(:\s*.*)?", re.DOTALL)
_EVS_TYPES = ("B", "b", "H", "h", "I", "i", "f", "s")
_PY_TYPES = {"uchar": "B", "char": "b", "ushort": "H", "short": "h", "uint": "I", "int": "i", "float": "f", "str": "s"}
_BUILTIN_NAMES = {"Condition", "EVENTS", "slot", "event_layers"}.union(_RESTART_TYPES.keys())
_GAME_IMPORT_RE = re.compile(r"^(from|import) soulstruct\.\w[\w\d]+\.events")


EventStatementTyping = tp.Union[ast.Expr, ast.For, ast.If, ast.Assign, ast.Return]
EventStatementTypes = (ast.Expr, ast.For, ast.If, ast.Assign, ast.Return)
ConditionNodeTyping = tp.Union[ast.UnaryOp, ast.BoolOp, ast.Compare, ast.Name, ast.Attribute, ast.Call]
ConditionNodeTypes = (ast.UnaryOp, ast.BoolOp, ast.Compare, ast.Name, ast.Attribute, ast.Call)
SkipReturnTyping = tp.Union[ast.UnaryOp, ast.Name, ast.Attribute, ast.Compare, ast.Call]
SkipReturnTypes = (ast.UnaryOp, ast.Name, ast.Attribute, ast.Compare, ast.Call)


class EventInfo(tp.NamedTuple):
    name: str
    id: int
    args: dict[str, tuple[int, int]]
    arg_types: str
    arg_classes: dict[str, tp.Type[gt.GameObject]]
    flag_name: str
    restart_type: int
    nodes: list[ast.stmt]
    description: str


class EVSParser(abc.ABC):

    GAME_MODULE = None  # type: tp.Any
    OR_SLOTS = []  # type: list[int, ...]
    AND_SLOTS = []  # type: list[int, ...]
    CONDITION_COUNT = 0
    INSTRUCTION_ARG_TYPES = {}

    tree: ast.Module
    map_name: str
    script_directory: tp.Optional[Path]
    linked_offsets: list[int]
    strings_with_offsets: list[str]
    globals: dict[str, tp.Any]  # global script namespace
    for_vars: dict[str, tp.Any]  # local to each event function

    instructions: dict[str, tp.Callable]
    tests: dict[str, tp.Union[tp.Callable, ConstantCondition, gt.FlagRange, gt.Character]]
    events: dict[str, EventInfo]  # information about each event function (collected before proper statement parsing)

    held_conditions: list[int]
    finished_conditions: list[int]
    script_event_flags: dict[str, int]
    current_event: tp.Optional[EventInfo]
    event_function_strings: list[str]

    numeric_emevd: str

    def __init__(self, evs_path_or_string: tp.Union[str, Path], map_name=None, script_directory=None):
        """Converts Python-like EVS code to numeric EMEVD (in `.numeric_emevd`), which can be fed to an `EMEVD` class.

        Args:
            evs_path_or_string: string or Path pointing to an EVS file, or direct string input (auto-detected based on
                any newlines being present in value).
            map_name: optional override for map name, which will otherwise be auto-detected from the EVS file name.
        """

        SET_INSTRUCTION_ARG_TYPES(self.INSTRUCTION_ARG_TYPES)

        if isinstance(evs_path_or_string, Path) or "\n" not in evs_path_or_string:
            evs_path = Path(evs_path_or_string)
            with evs_path.open("r", encoding="utf-8") as script:
                self.tree = ast.parse(script.read())
            self.map_name = evs_path.name.split(".")[0] if map_name is None else map_name
            self.script_directory = Path(script_directory) if script_directory else evs_path.parent
        else:
            self.tree = ast.parse(evs_path_or_string)
            self.map_name = map_name
            self.script_directory = Path(script_directory) if script_directory else None

        self.linked_offsets = []
        self.strings_with_offsets = []

        # Global namespace with game-specific enums and constants. May be updated with user imports and definitions.
        self.globals = vars(self.GAME_MODULE.enums)
        self.globals.update(vars(self.GAME_MODULE.constants))
        self.globals.update(vars(gt))
        # Note that there is no event-specific local namespace, except for this dictionary of 'for' loop variables:
        self.for_vars = {}

        self.instructions = {
            name: attr for name, attr in vars(self.GAME_MODULE.instructions).items() if not name.startswith("__")
        }
        self.tests = {
            name: attr
            for name, attr in vars(self.GAME_MODULE.tests).items()
            if not name.startswith("_")
            and (isinstance(attr, ConstantCondition) or getattr(attr, "__module__", "").endswith("tests"))
        }
        self.events = {}  # Maps your event names to their IDs, so you can call them to initialize them.
        self.event_ids = set()  # Used to ensure the same ID is not repeated.

        self._reset_conditions()

        self.held_conditions = []  # These conditions won't be re-allocated.
        self.finished_conditions = []  # These conditions need to be accessed with 'finished' instruction variants.

        self.script_event_flags = {}
        self.current_event = None
        self.event_function_strings = []

        self.numeric_emevd = ""

        self._compile_evs()

    def _reset_conditions(self):
        """Reset for every new event. Contains names of conditions."""
        self.conditions = [""] * self.CONDITION_COUNT

    # ~~~~~~~~~~~~~~~~~~~
    #  FIRST PASS METHODS: These scan the event functions and collect information about each script.
    # ~~~~~~~~~~~~~~~~~~~

    def _scan_event(self, node: ast.FunctionDef):
        """Confirm syntax of event function and add it to `self.events` dictionary.

        An event should look like:

        @RestartOnRest
        def EventName(arg1: int, arg2: float):
            ''' [FlagName] 11020100: [Description] '''
            ...
        """
        event_name = self._validate_event_name(node)

        docstring = ast.get_docstring(node)
        if docstring is None:
            raise EVSSyntaxError(node, f"No docstring given for event {event_name}. See EVS documentation.")
        try:
            flag_name, event_id, description = _EVENT_DOCSTRING_RE.match(docstring).group(1, 2, 3)
        except AttributeError:
            raise EVSSyntaxError(node, f"Invalid docstring for event {event_name}. See EVS documentation.")

        event_id = int(event_id)
        if event_id in self.event_ids:
            raise EVSSyntaxError(node, f"Event ID {event_id} is defined multiple times in EVS script.")
        elif event_id == 0:
            if event_name.lower() not in {"event0", "constructor"}:
                raise EVSSyntaxError(node, "Event 0 must be called CONSTRUCTOR (or 'Event0').")
        elif event_id == 50:
            if event_name.lower() not in {"event50", "preconstructor"}:
                raise EVSSyntaxError(node, "Event 50 must be called PRECONSTRUCTOR (or 'Event50').")
        elif event_name.lower() in {"constructor", "preconstructor"}:
            raise EVSSyntaxError(
                node, "Builtin event names CONSTRUCTOR and PRECONSTRUCTOR are reserved for events 0 and 50."
            )

        flag_name = None if not flag_name else flag_name.rstrip()  # Remove trailing space.
        description = "" if not description else description.lstrip(":")  # Remove leading colon.

        arg_dict, arg_types, arg_classes = _parse_event_arguments(node)
        restart_type = _parse_decorator(node)

        if flag_name in self.globals:
            if self.globals[flag_name] != event_id:
                raise EVSSyntaxError(
                    node,
                    f"Event flag name '{flag_name}' for event ID {event_id} clashes with the ID of "
                    f"a constant with the same name.",
                )
        elif flag_name:
            self.script_event_flags[flag_name] = event_id  # Loaded into constants later under EVENTS enum.

        self.events[event_name] = EventInfo(
            name=event_name,
            id=event_id,
            args=arg_dict,
            arg_types=arg_types,
            arg_classes=arg_classes,
            flag_name=flag_name,
            restart_type=restart_type,
            nodes=node.body[1:],  # Skips docstring.
            description=description.lstrip(":"),
        )
        self.event_ids.add(event_id)

    def _validate_event_name(self, event_node: ast.FunctionDef):
        name = event_node.name
        if name in self.instructions or name in {"Await", "EnableThisFlag", "DisableThisFlag"}:
            raise EVSSyntaxError(event_node, f"Event name cannot match an instruction name ({name}).")
        if name in _BUILTIN_NAMES:
            raise EVSSyntaxError(event_node, f"Event name cannot match a builtin EVS name ({name}).")
        if name in self.events:
            raise EVSSyntaxError(event_node, f"An event named {name} has already been defined in this script.")
        # TODO: Check if event name is already in common_func (when supported).
        return name

    # ~~~~~~~~~~~~~~~~
    #  COMPILE METHODS: These produce numeric EMEVD lines.
    # ~~~~~~~~~~~~~~~~

    def _compile_evs(self):
        """Top-level node traversal."""
        emevd_docstring = ast.get_docstring(self.tree)
        if emevd_docstring is not None:
            docstring_groups = re.split(r"\n{2,}", emevd_docstring)
            for group in docstring_groups:
                if group.startswith("linked:"):
                    for offset in group[8:].split("\n"):
                        if offset.strip():
                            self.linked_offsets += [int(offset.strip())]
                elif group.startswith("strings:"):
                    for offset_with_string in group[9:].split("\n"):
                        self.strings_with_offsets.append(offset_with_string)
                # Otherwise ignore (you can add anything else to the docstring, provided you leave blank lines between).

        for node in self.tree.body[1:]:
            if isinstance(node, ast.Import):
                _import_module(node, self.globals)
            elif isinstance(node, ast.ImportFrom):
                _import_from(node, self.globals, self.script_directory)
            elif isinstance(node, ast.FunctionDef):
                self._scan_event(node)
            elif isinstance(node, ast.Assign):
                self._assign_name(node)
            elif isinstance(node, ast.ClassDef):
                continue  # Class definitions (e.g. enums) are collected from the real Python parser.
            else:
                raise EVSSyntaxError(
                    node.lineno,
                    f"Invalid content: {node.__class__}. The only valid global EVS lines are "
                    f"from-imports, event script function definitions, and global name assignments.",
                )

        if self.script_event_flags:
            # noinspection PyTypeChecker
            self.globals["EVENTS"] = gt.Flag("EVENTS", self.script_event_flags)

        for event_name, event_function in self.events.items():
            self.current_event = self.events[event_name]
            self.for_vars = {}
            self._reset_conditions()
            self.finished_conditions = []
            parsed_event = self._compile_event_function(event_function)  # numeric format
            self.event_function_strings.append("\n".join(parsed_event))

        self.numeric_emevd = "\n\n".join(self.event_function_strings)
        self.numeric_emevd += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_offsets)
        self.numeric_emevd += "\n\nstrings:\n" + "\n".join(self.strings_with_offsets)

    def _compile_event_function(self, event_info: EventInfo):
        """ Writes header, then iterates over all nodes in function body. """

        event_emevd = _header(event_info.id, event_info.restart_type)

        for node in event_info.nodes:
            if not isinstance(node, EventStatementTypes):
                raise EVSSyntaxError(
                    node,
                    f"Invalid line: {ast.dump(node)}. Must be `Condition()` assignment, IF/ELSE block, or instruction.",
                )
            built_function = self._compile_event_body_node(node)
            if built_function is None:
                raise EVSSyntaxError(node, "Builder returned None for instruction.")
            event_emevd += built_function

        return event_emevd

    def _compile_event_body_node(self, node: EventStatementTyping):
        """Recursive node compiler.

        Every line must be an instruction (from my set, not the base EMEVD set), an IF statement, or an assignment to a
        `Condition()` call.
        """

        # INSTRUCTION or GAME TYPE METHOD
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return self._compile_function_expression(node.value)

        # AWAIT
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Await):
            if not isinstance(node.value.value, ConditionNodeTypes):
                raise EVSSyntaxError(node.lineno, "`await` expression must be a Condition or boolean expression.")
            return self._compile_condition(node.value.value, condition=0)

        # FOR
        if isinstance(node, ast.For):
            return self._compile_for(node)

        # IF
        if isinstance(node, ast.If):
            return self._compile_if(node)

        # ASSIGN (CONDITION ONLY)
        if isinstance(node, ast.Assign):
            try:
                if not isinstance(node.value, ast.Call) or not isinstance(node.value.func, ast.Name):
                    raise ValueError
                if node.value.func.id not in {"Condition", "HeldCondition"}:
                    raise ValueError
            except ValueError:
                raise EVSSyntaxError(
                    node.lineno,
                    "Cannot create local variables inside event script functions. Define them globally or import them "
                    "from other modules. All assignment statements must be `c = Condition()` or `c = HeldCondition()` "
                    "statements.",
                )
            return self._assign_condition(node, held=node.value.func.id == "HeldCondition")

        # RETURN
        if isinstance(node, ast.Return):
            if node.value is None or (isinstance(node.value, ast.Name) and node.value.id == "END"):
                return self.instructions["End"]()
            elif isinstance(node.value, ast.Name) and node.value.id == "RESTART":
                return self.instructions["Restart"]()
            else:
                raise EVSSyntaxError(
                    node,
                    f"Invalid return value '{node.value}'. It should be None (empty) to end the "
                    f"event, or the constant RESTART to restart it.",
                )

        raise EVSSyntaxError(
            node,
            f"Invalid line: {ast.dump(node)}. Must be `Condition()` assignment, IF/ELSE block, or instruction.",
        )

    def _compile_event_call(self, node: ast.Call):
        """Shortcut for RunEvent(...) instruction."""
        name, args, kwargs = self._parse_function_call(node)
        event_info = self.events[name]
        kwargs = self._parse_keyword_nodes(node.keywords)
        event_layer_string = format_event_layers(kwargs.pop("event_layers", None))

        if not args and not kwargs and not event_info.args:
            # Events with no arguments can be called with no argument, ignoring `event_layers` (`slot` defaults to 0).
            instruction = self.instructions["RunEvent"](event_info.id)
            instruction[0] += event_layer_string
            return instruction

        slot = kwargs.pop("slot", None)
        if slot is None:
            if kwargs and len(args) != 1:
                raise EVSValueError(
                    node,
                    "If using keyword arguments when running events by calling them directly, you "
                    "must either have a 'slot' keyword argument or have exactly one positional "
                    "argument (slot) before the keyword arguments.",
                )
            slot, args = args[0], args[1:]
        if not isinstance(slot, int):
            raise EVSValueError(node, "Slot ('slot' keyword or first positional argument) must be an integer.")

        if kwargs:
            args = []
            for arg_name in event_info.args:
                try:
                    args.append(kwargs.pop(arg_name))  # order event arguments correctly
                except KeyError:
                    raise EVSValueError(node, f"Missing keyword argument in event call: {arg_name}")
            if kwargs:
                raise EVSValueError(node, f"Invalid keyword arguments in event call: {kwargs}")
        else:
            if len(args) != len(event_info.args):
                raise EVSValueError(
                    node,
                    f"Number of positional arguments in event call (excluding the slot) "
                    f"does not match the event function signature:\n"
                    f"    {['slot'] + list(event_info.args.keys())}.",
                )

        event_id = event_info.id
        slot = 0 if slot is None else slot
        args = (0,) if not args else args
        arg_types = event_info.arg_types if event_info.arg_types else None

        instruction = self.instructions["RunEvent"](event_id, slot=slot, args=args, arg_types=arg_types)
        instruction[0] += event_layer_string
        return instruction

    def _compile_instruction(self, node: ast.Call):
        """Build instruction arguments and call the instruction (which will return a numeric line)."""
        name, args, kwargs = self._parse_function_call(node)
        event_layers = kwargs.pop("event_layers", None)
        try:
            instruction_lines = self.instructions[name](*args, **kwargs)  # includes event arg load lines
        except Exception as e:
            raise EVSSyntaxError(node, f"Failed to compile instruction {name}.\n    Error: {str(e)}")
        try:
            instruction_lines[0] += format_event_layers(event_layers)
        except TypeError:
            raise EVSSyntaxError(node, f"If given, `event_layers` must be a list, tuple, or single integer.")
        return instruction_lines

    def _compile_function_expression(self, node: ast.Call):

        if isinstance(node.func, ast.Attribute):
            # Method of a game object.
            attr = node.func.attr
            game_object = self._parse_nodes(node.func.value)
            if not isinstance(game_object, gt.GameObject):
                raise EVSSyntaxError(
                    node, "Only methods of builtin GameObject types can be called as instructions."
                )
            _, args, kwargs = self._parse_function_call(node)
            try:
                return getattr(game_object, attr)(*args, **kwargs)
            except AttributeError:
                raise EVSAttributeError(node, game_object.__name__, attr)
            except Exception as e:
                raise EVSValueError(node, f"Error occurred in GameObject method call:\n    {str(e)}")

        if not isinstance(node.func, ast.Name):
            raise EVSSyntaxError(node, "Function must be a name.")
        name = node.func.id

        if name in self.events:
            return self._compile_event_call(node)

        if name == "Condition":
            raise EVSError(node, "You must assign the Condition() to a variable.")
        if name == "HeldCondition":
            raise EVSError(node, "You must assign the HeldCondition() to a variable.")

        if name == "Await":
            if node.keywords or len(node.args) != 1:
                raise EVSSyntaxError(
                    node,
                    "Await() takes exactly one positional argument (Condition or boolean expression)."
                )
            arg = node.args[0]
            if not isinstance(arg, ConditionNodeTypes):
                raise EVSSyntaxError(
                    node,
                    f"Await() argument must be a Condition or boolean expression, not: {type(arg)}."
                )
            return self._compile_condition(arg, condition=0)

        if name in {"EnableThisFlag", "DisableThisFlag"}:
            if self.current_event.args:
                raise EVSNameError(
                    node,
                    "Cannot use 'EnableThisFlag' or 'DisableThisFlag' shortcuts in an event that "
                    "takes arguments (the slot number cannot be determined from within).",
                )
            if name == "EnableThisFlag":
                return self.instructions["EnableFlag"](self.current_event.id)
            return self.instructions["DisableFlag"](self.current_event.id)

        if name in self.instructions:
            return self._compile_instruction(node)

        raise EVSSyntaxError(
            node,
            f"Name {repr(name)} cannot be called in an expression. Only instructions and GameObject\n"
            f"methods can be called outside of assignments and argument values.",
        )

    def _compile_for(self, node: ast.For):
        try:
            for_iter = self._parse_nodes(node.iter, allowed_calls=("range", "zip"))
        except Exception as e:
            raise EVSSyntaxError(node, f"Invalid 'for' loop iterable. Error:\n    {str(e)}")
        for_emevd = []
        for_var = node.target
        if isinstance(for_var, ast.Name):
            if for_var.id in self.for_vars:
                raise EVSSyntaxError(
                    node, f"Variable {repr(for_var.id)} is already a 'for' loop variable in this scope."
                )
            if for_var in self.current_event.args:
                raise EVSSyntaxError(
                    node, f"Loop variable {repr(for_var.id)} is already the name of an event argument."
                )
            for iter_value in for_iter:
                self.for_vars[for_var.id] = iter_value
                for for_node in node.body:
                    if not isinstance(for_node, EventStatementTypes):
                        raise EVSSyntaxError(node, f"Invalid statement type.")
                    for_emevd += self._compile_event_body_node(for_node)
                self.for_vars.pop(for_var.id)
        elif isinstance(for_var, ast.Tuple):
            for sub_var in for_var.elts:
                if not isinstance(sub_var, ast.Name):
                    # TODO: Implement arbitrary depth values.
                    raise EVSSyntaxError(node, "`for` loop variables cannot currently use nested tuples.")
                if sub_var.id in self.for_vars:
                    raise EVSSyntaxError(
                        node, f"Variable {repr(sub_var.id)} is already a 'for' loop variable in this scope."
                    )
                if sub_var in self.current_event.args:
                    raise EVSSyntaxError(
                        node, f"Loop variable {repr(sub_var.id)} is already the name of an event argument."
                    )
            for iter_value in for_iter:
                for i, sub_var in enumerate(for_var.elts):
                    assert isinstance(sub_var, ast.Name)  # checked above
                    self.for_vars[sub_var.id] = iter_value[i]
                for for_node in node.body:
                    if not isinstance(for_node, EventStatementTypes):
                        raise EVSSyntaxError(node, f"Invalid statement type.")
                    for_emevd += self._compile_event_body_node(for_node)
                for sub_var in for_var.elts:
                    assert isinstance(sub_var, ast.Name)  # checked above
                    self.for_vars.pop(sub_var.id)

        return for_emevd

    def _compile_if(self, node: ast.If):

        if_emevd = []

        # 0. Check if body is just one end/restart function.
        if len(node.body) == 1 and isinstance(node.body[0], ast.Return) and not node.orelse:
            return_node = node.body[0]
            assert isinstance(return_node, ast.Return)
            if return_node.value is None or (isinstance(return_node.value, ast.Name) and return_node.value.id == "END"):
                try:
                    if not isinstance(node.test, SkipReturnTypes):
                        raise NoSkipOrReturnError
                    return self._compile_skip_or_return(node.test, end_event=True)
                except NoSkipOrReturnError:
                    # Continue to try building skip (though it will have to be a chain) or full condition.
                    pass
            elif isinstance(return_node.value, ast.Name) and return_node.value.id == "RESTART":
                try:
                    if not isinstance(node.test, SkipReturnTypes):
                        raise NoSkipOrReturnError
                    return self._compile_skip_or_return(node.test, restart_event=True)
                except NoSkipOrReturnError:
                    # Continue to try building skip (though it will have to be a chain) or full condition.
                    pass
            else:
                raise EVSSyntaxError(
                    node,
                    f"Invalid return value '{return_node.value}'. It should be None (empty) to end the "
                    f"event, or the constant RESTART to restart it.",
                )

        # 1. Build the body of the IF statement.
        body_emevd = []
        for child_node in node.body:
            if not isinstance(child_node, EventStatementTypes):
                raise EVSSyntaxError(child_node.lineno, f"Invalid statement node.")
            try:
                body_emevd += self._compile_event_body_node(child_node)
            except TypeError:
                raise EVSSyntaxError(node, f"Error in IF block:\n  {ast.dump(node)}")

        # 2. Build the test line. This could be a simple skip, a multi-line chain skip, or a fully-fledged Condition,
        #    depending on the test. Note that the body length has 1 added (an extra skip line) if there is an ELSE body
        #    in the statement, and does not include arg replacement lines.
        body_length = len([line for line in body_emevd if not line.startswith("    ^")]) + bool(node.orelse)
        test_emevd = self._compile_test(node.test, body_length=body_length)

        # 3. Build the ELSE body of the IF statement, if it exists.
        else_emevd = []
        for child_node in node.orelse:
            if not isinstance(child_node, EventStatementTypes):
                raise EVSSyntaxError(child_node.lineno, f"Invalid statement node.")
            else_emevd += self._compile_event_body_node(child_node)

        # 4. Put these components together. Note that an extra skip line is added if an ELSE body is present.
        if_emevd += test_emevd + body_emevd
        if else_emevd:
            skip_line_count = len([line for line in else_emevd if not line.startswith("    ^")])
            if_emevd += self.instructions["SkipLines"](skip_line_count)
            if_emevd += else_emevd

        return if_emevd

    def _compile_test(self, node, body_length, negate=False):
        """Tries a simple skip, then a chain skip, then resorts to building a condition.

        Argument `node` should be the test node of the If node.
        """
        test_emevd = []

        # 1. If the test starts with a 'not' operator, simply recur this method on the operand with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                return self._compile_test(node.operand, body_length, negate=not negate)
            raise EVSSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        try:
            # 2a. Try to build a simple or chain skip.
            test_emevd += self._compile_skip_or_return(node, skip_lines=body_length, negate=negate)
        except NoSkipOrReturnError:
            # 2b. If the skip failed (returned None), we build a full condition.
            test_emevd += self._compile_condition(node, skip_lines=body_length, negate=negate)

        return test_emevd

    def _compile_skip_or_return(
        self,
        node: SkipReturnTyping,
        skip_lines=0,
        end_event=False,
        restart_event=False,
        negate=False,
        chain=False,
    ):

        if sum((skip_lines > 0, end_event, restart_event)) != 1:
            raise EVSSyntaxError(
                node, "(internal) You can use 'skip_lines, 'end_event', or 'restart_event', but not multiples."
            )

        # 1. Resolve any opening 'not' operators by recurring this method with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                if not isinstance(node.operand, SkipReturnTypes):
                    raise EVSSyntaxError(node.lineno, f"Invalid `not` expression type: {type(node.operand)}")
                return self._compile_skip_or_return(
                    node.operand,
                    skip_lines=skip_lines,
                    end_event=end_event,
                    restart_event=restart_event,
                    negate=not negate,
                )
            raise EVSSyntaxError(node.lineno, "The `not` keyword is the only valid unary operator.")

        # 2. The condition is an event argument with a callable, testable game type.
        if isinstance(node, ast.Name) and node.id in self.current_event.args:
            if node.id in self.current_event.arg_classes:
                arg = self.current_event.args[node.id]
                arg_class = self.current_event.arg_classes[node.id]
                test_func = partial(arg_class.__call__, arg)
                if not callable(test_func):
                    raise EVSValueError(node.lineno, f"Event argument type {repr(arg_class)} is not testable.")
                return test_func(negate=negate, skip_lines=skip_lines, end_event=end_event, restart_event=restart_event)
            raise EVSValueError(
                node.lineno,
                f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                f"such as Flag (tests for enabled state), Region (tests if player is inside), etc.",
            )

        # 3. The condition is a previously-defined Condition() or HeldCondition() instance.
        if isinstance(node, ast.Name) and node.id in self.conditions:
            i = self.conditions.index(node.id)
            try:
                return self._compile_condition_skip_or_return(i, negate, skip_lines, end_event, restart_event)
            except ValueError:
                raise EVSError(
                    node.lineno,
                    "(internal) Cannot resolve simple condition check: 'skip_lines, 'end_event', and "
                    "'restart_event' are all 0 or False.",
                )

        # 4. The condition is a builtin test constant (e.g. THIS_FLAG, HOST, OFFLINE, SKULL_LANTERN_ACTIVE, ...)
        if isinstance(node, ast.Name) and node.id in self.tests:
            try:
                test = self.tests[node.id]
            except KeyError:  # No other permitted names.
                raise EVSNameError(node.lineno, node.id)
            if isinstance(test, ConstantCondition):
                return test(negate=negate, skip_lines=skip_lines, end_event=end_event, restart_event=restart_event)
            if isinstance(test, gt.FlagRange):
                raise EVSSyntaxError(
                    node.lineno,
                    "Cannot implicitly use a FlagRange as a condition. Call any() "
                    "or all() on it (with or without 'not' in front) to test it.",
                )
            if isinstance(test, gt.Character):
                raise EVSSyntaxError(
                    node.lineno,
                    "Cannot implicitly use a Character as a test. Call IsAlive(), "
                    "IsDead(), etc. on the Character to test its state.",
                )
            raise NoSkipOrReturnError

        # 5. The condition is a callable 'boolean' object in the global namespace that requires no arguments.
        if isinstance(node, (ast.Attribute, ast.Name)):
            test_func = self._parse_nodes(node)  # This will raise an EmevdNameError if the name is invalid.
            if isinstance(test_func, gt.FlagRange):
                raise EVSValueError(
                    node.lineno,
                    "Cannot implicitly use a FlagRange as a condition.\n"
                    "Call `any()`, `all()`, `not any()`, or `not all()` on it to test it.",
                )
            if not callable(test_func):
                raise EVSValueError(node.lineno, f"Object {repr(test_func)} is not testable.")
            try:
                return test_func(negate=negate, skip_lines=skip_lines, end_event=end_event, restart_event=restart_event)
            except TypeError as ex:
                if "unexpected keyword argument" in str(ex):
                    raise NoSkipOrReturnError  # This object does not support simple/chain skip or return.
                raise

        # 6. The condition is a binary comparison operation.
        if isinstance(node, ast.Compare):
            return self._compile_simple_comparison(node, negate, skip_lines)

        # 7. The condition is a test function call.
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in self.tests:
            test_function = self.tests[node.func.id]
            # Get arguments.
            args = self._parse_nodes(node.args)
            kwargs = self._parse_keyword_nodes(node.keywords)
            return test_function(
                *args, skip_lines=skip_lines, negate=negate, end_event=end_event, restart_event=restart_event, **kwargs
            )  # This will raise the same error as below.

        # 8. The condition is any() or all() called on a FlagRange of a sequence of simple skips that can be chained.
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ("any", "all"):
                if len(node.args) != 1:
                    raise EVSSyntaxError(node.lineno, f"{node.func.id} must have one argument (sequence/FlagRange).")
                arg = node.args[0]
                if not isinstance(arg, (ast.List, ast.Tuple)):
                    return self._compile_range_test(node, negate, skip_lines)
                if not chain and skip_lines > 0:
                    assert isinstance(arg, (ast.List, ast.Tuple))
                    return self._compile_chain_test(arg, node.func.id, negate=negate, skip_lines=skip_lines)

        # Failed to build simple/chain skip or return.
        raise NoSkipOrReturnError

    def _compile_simple_comparison(self, node: ast.Compare, negate, skip_lines):
        left_node, op_node, comparison_value = _validate_comparison_node(node)
        if isinstance(left_node, ast.Name):
            name = left_node.id
            try:
                arg = self.current_event.args[name]
            except KeyError:
                raise NoSkipOrReturnError
            if not negate:  # note inversion
                return self.instructions["SkipLinesIfComparison"](
                    skip_lines, NEG_COMPARISON_NODES[op_node], arg, comparison_value
                )
            return self.instructions["SkipLinesIfComparison"](
                skip_lines, COMPARISON_NODES[op_node], arg, comparison_value
            )
        raise NoSkipOrReturnError

    def _compile_range_test(self, node: ast.Call, negate, skip_lines):
        """`node` must be an `all()` or `any()` call with a single argument (already checked by caller).

        This single argument must be a `range()` call or `FlagRange` object.
        """
        assert isinstance(node.func, ast.Name)
        arg = node.args[0]

        # Note negation here, because this will be a skip.
        tests = ["AllOff", "AnyOn"] if node.func.id == "all" else ["AllOn", "AnyOff"]  # "any"

        if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name) and arg.func.id == "range":
            if len(arg.args) != 2:
                raise EVSSyntaxError(
                    node, "`range()` used inside `all()` or `any()` must have exactly two arguments: `(first, last)`."
                )
            first, last = self._parse_nodes(arg.args)
            return self.instructions["SkipLinesIfFlagRange" + tests[negate]](skip_lines, (first, last))
        else:
            flag_range = self._parse_nodes(arg)
            if isinstance(flag_range, gt.FlagRange):
                return self.instructions["SkipLinesIfFlagRange" + tests[negate]](skip_lines, flag_range)
            raise EVSSyntaxError(node, "The only valid non-sequence argument to 'all' is a FlagRange.")

    def _compile_chain_test(self, node: tp.Union[ast.Tuple, ast.List], func_name: str, negate, skip_lines):
        """`node` must be an `any()` or `all()` call with a single argument that is a `list` or `tuple` (already checked
        by caller).
        """
        assert isinstance(node, (ast.Tuple, ast.List))
        sequence = node.elts
        n_args = len(sequence)
        negate = not negate if func_name == "any" else negate
        skip_negate = func_name == "any"

        if skip_lines > 0:
            chain_skip_emevd = []
            for i, arg in enumerate(sequence):
                chain_skip_lines = n_args - i if negate else skip_lines + n_args - i - 1
                if not isinstance(arg, SkipReturnTypes):
                    raise NoSkipOrReturnError
                # Next line may also raise a `NoSkipOrReturnError` if a non-simple test is present.
                chain_skip_emevd += self._compile_skip_or_return(
                    arg, skip_lines=chain_skip_lines, negate=skip_negate, chain=True
                )
            if chain_skip_emevd:
                if negate:
                    chain_skip_emevd += self.instructions["SkipLines"](skip_lines)  # Extra skip required.
                return chain_skip_emevd

        raise NoSkipOrReturnError

    def _compile_condition(
        self,
        node: ConditionNodeTyping,
        negate=False,
        condition=None,
        skip_lines=0,
    ):
        """Called on the argument of Condition() or Await(), or on a non-simple IF test node."""
        if condition is None and skip_lines == 0:
            raise ValueError("Either 'condition' index or 'skip_lines' count must be specified.")
        if condition is not None and skip_lines != 0:
            raise ValueError("Do not use 'condition' and 'skip_lines' at the same time.")
        if skip_lines < 0:
            raise ValueError("Cannot skip a negative number of lines.")

        emevd_args = []
        emevd_kwargs = {}
        node_to_recur = node

        # NOT (recurred)
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                if not isinstance(node.operand, ConditionNodeTypes):
                    raise EVSSyntaxError(node.lineno, "Invalid condition expression.")
                return self._compile_condition(
                    node.operand, negate=not negate, condition=condition, skip_lines=skip_lines
                )
            raise EVSSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        # OR / AND (recurred)
        if isinstance(node, ast.BoolOp):
            return self._compile_boolean_condition(node, negate=negate, condition=condition, skip_lines=skip_lines)

        # Compare
        if isinstance(node, ast.Compare):
            node, op_node, comparison_value = _validate_comparison_node(node)
            emevd_args += [op_node, comparison_value]

        # Testable event argument
        if isinstance(node, ast.Name) and node.id in self.current_event.args:
            if node.id in self.current_event.arg_classes:
                arg = self.current_event.args[node.id]
                arg_class = self.current_event.arg_classes[node.id]
                test_func = partial(arg_class.__call__, arg)
                if not callable(test_func):
                    raise EVSValueError(node.lineno, f"Event argument type {repr(arg_class)} is not testable.")
                try:
                    return test_func(negate=negate, condition=condition, skip_lines=skip_lines)
                except AttributeError:
                    raise EVSValueError(node.lineno, f"Cannot parse test function of '{node.id}'")
            raise EVSValueError(
                node.lineno,
                f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                f"such as Flag (tests for enabled state), Region (tests if player is inside), etc.",
            )

        # Existing condition
        if isinstance(node, ast.Name) and node.id in self.conditions:
            i = self.conditions.index(node.id)
            if i in self.finished_conditions:
                raise EVSSyntaxError(
                    node.lineno, f"Finished condition {node.id} cannot be an input condition. You must use line skips."
                )
            self.finished_conditions.append(i)
            logic = "False" if negate else "True"
            return self.instructions[f"IfCondition{logic}"](condition, i)

        # Call
        if isinstance(node, ast.Call):
            emevd_args += self._parse_nodes(node.args)
            emevd_kwargs.update(self._parse_keyword_nodes(node.keywords))
            node = node.func  # -> ast.Name (parsed below)

        # Test function
        if isinstance(node, ast.Name) and node.id in self.tests:
            test_function = self.tests[node.id]
            try:
                return test_function(
                    *emevd_args, negate=negate, condition=condition, skip_lines=skip_lines, **emevd_kwargs
                )
            except (NoSkipOrReturnError, NoNegateError):
                # No builtin tests for terminating/negating condition. Need to construct a temporary one.
                # either skip_lines > 0 or negate == True (or both) since one of these errors have been raised
                condition_emevd = []
                temp_condition = self._check_out_TEMP(node.lineno)

                if skip_lines > 0:
                    # if skip_lines > 0, then this is part of an if and we need to use SkipLinesIfConditionTrue/False with the temp condition
                    # NoSkipOrReturn must have been raised, so we compile the test using a temp condition first and skip depending on its result
                    condition_emevd += self._compile_condition(node_to_recur, negate=False, condition=temp_condition)
                    condition_emevd += self.instructions[f"SkipLinesIfCondition{str(negate)}"](skip_lines, temp_condition)

                else:
                    # if skip_lines == 0, then this is part of an Await and we need to use IfConditionTrue/False with condition 0 and the temp condition as input
                    # NoNegateError must have been raised, so negate must be True; therefore IfConditionFalse is always used here
                    condition_emevd += self._compile_condition(node_to_recur, negate=False, condition=temp_condition)
                    condition_emevd += self.instructions["IfConditionFalse"](0, temp_condition)

                return condition_emevd
            except ValueError as ex:
                raise EVSError(node.lineno, f"Error occurred in test function '{node.id}': {ex}")

        # Constant / Event Argument
        if isinstance(node, (ast.Attribute, ast.Name)):
            test_func = self._parse_nodes(node)  # This will raise an EmevdNameError if the name is invalid.
            if isinstance(test_func, gt.FlagRange):
                raise EVSValueError(
                    node.lineno,
                    "Cannot implicitly use a FlagRange as a condition.\n"
                    "Call any() or all() on it (with or without 'not' in front) to test it.",
                )
            if not callable(test_func):
                raise EVSValueError(node.lineno, f"Object {repr(test_func)} is not testable.")
            try:
                return test_func(negate=negate, condition=condition, skip_lines=skip_lines)
            except (NoSkipOrReturnError, NoNegateError):
                # No builtin tests for terminating/negating condition. Need to construct a temporary one.
                condition_emevd = []
                temp_condition = self._check_out_TEMP(node.lineno)
                skip_negate = False if skip_lines > 0 else negate  # avoids double negative with negated skip
                logic = str(bool(negate) if skip_lines > 0 else not bool(negate))
                instr = f"SkipLinesIfCondition{logic}"
                condition_emevd += self._compile_condition(node_to_recur, negate=skip_negate, condition=temp_condition)
                condition_emevd += self.instructions[instr](skip_lines, temp_condition)
                return condition_emevd

        # Failure to compile the condition will be raised as a genuine syntax error, unlike the skip/return compiler.
        # noinspection PyTypeChecker
        raise EVSSyntaxError(node.lineno, f"Invalid node for condition content:\n{ast.dump(node)}")

    def _compile_condition_skip_or_return(
        self, condition, negate=False, skip_lines=0, end_event=False, restart_event=False
    ):
        if skip_lines > 0:
            if negate:
                if condition in self.finished_conditions:
                    return self.instructions["SkipLinesIfFinishedConditionTrue"](skip_lines, condition)
                self.finished_conditions.append(condition)  # Condition is now finished.
                return self.instructions["SkipLinesIfConditionTrue"](skip_lines, condition)
            if condition in self.finished_conditions:
                return self.instructions["SkipLinesIfFinishedConditionFalse"](skip_lines, condition)
            self.finished_conditions.append(condition)  # Condition is now finished.
            return self.instructions["SkipLinesIfConditionFalse"](skip_lines, condition)
        elif end_event:
            if negate:
                if condition in self.finished_conditions:
                    return self.instructions["EndIfFinishedConditionFalse"](condition)
                self.finished_conditions.append(condition)  # Condition is now finished.
                return self.instructions["EndIfConditionFalse"](condition)
            if condition in self.finished_conditions:
                return self.instructions["EndIfFinishedConditionTrue"](condition)
            self.finished_conditions.append(condition)  # Condition is now finished.
            return self.instructions["EndIfConditionTrue"](condition)
        elif restart_event:
            if negate:
                if condition in self.finished_conditions:
                    return self.instructions["RestartIfFinishedConditionFalse"](condition)
                self.finished_conditions.append(condition)  # Condition is now finished.
                return self.instructions["RestartIfConditionFalse"](condition)
            if condition in self.finished_conditions:
                return self.instructions["RestartIfFinishedConditionTrue"](condition)
            self.finished_conditions.append(condition)  # Condition is now finished.
            return self.instructions["RestartIfConditionTrue"](condition)
        else:
            raise ValueError

    def _compile_boolean_condition(self, node: ast.BoolOp, negate, condition, skip_lines):
        if isinstance(node.op, ast.Or):
            i = self._check_out_OR(node)
        elif isinstance(node.op, ast.And):
            i = self._check_out_AND(node)
        else:
            raise EVSSyntaxError(node, "Only valid boolean operations are OR / AND.")

        condition_emevd = []

        for v in node.values:
            if isinstance(v, ConditionNodeTypes):
                condition_emevd += self._compile_condition(v, condition=i)

        finished = "Finished" if i in self.finished_conditions else ""

        if skip_lines > 0:
            logic = "True" if negate else "False"
            instr = f"SkipLinesIf{finished}Condition{logic}"
            condition_emevd += self.instructions[instr](skip_lines, i)
        elif finished:
            raise EVSValueError(node, "Cannot use a finished condition as an input to another condition.")
        else:
            logic = "False" if negate else "True"
            instr = f"IfCondition{logic}"
            condition_emevd += self.instructions[instr](condition, i)

        if i not in self.finished_conditions:
            self.finished_conditions.append(i)

        return condition_emevd

    # ~~~~~~~~~~~~~~~~~~~~
    #  ASSIGNMENT METHODS: These create global/local objects, including Conditions, from assignment nodes.
    # ~~~~~~~~~~~~~~~~~~~~

    def _assign_name(self, node: ast.Assign):
        """Assign object to name of your choosing. Can only be used outside any event function scripts."""
        value = self._parse_nodes(node.value)
        for target in node.targets:
            if not isinstance(target, ast.Name):
                raise EVSSyntaxError(node, "Values can only be assigned to (any number of) single names.")
            name = target.id
            if name in self.instructions or name in {"Await", "EnableThisFlag", "DisableThisFlag"}:
                raise EVSSyntaxError(node, f"Cannot assign to an instruction name ({name}).")
            if name in _BUILTIN_NAMES:
                raise EVSSyntaxError(node, f"Cannot assign to a builtin EVS name ({name}).")
            if name in self.events:
                raise EVSSyntaxError(node, f"Cannot assign to an existing event name ({name}).")
            else:
                self.globals[name] = value  # will override any previous value

    def _assign_condition(self, node: ast.Assign, held=False):
        if len(node.targets) != 1:
            raise EVSSyntaxError(node, "Can only assign a Condition to one name.")
        assert isinstance(node.value, ast.Call)
        if len(node.value.args) != 1 or len(node.value.keywords) > 1:
            raise EVSSyntaxError(
                node,
                "Condition should have one positional argument (and/or with any number of "
                "operands) and an optional keyword argument 'hold' that can be True or False "
                "(default).",
            )
        name_node = node.targets[0]
        assert isinstance(name_node, ast.Name)
        condition_name = name_node.id
        if condition_name == "_":
            raise EVSSyntaxError(node, "Condition name cannot be '_' (builtin symbol for temp condition).")
        condition_argument = node.value.args[0]
        hold = held
        if len(node.value.keywords) == 1:
            if held:
                raise EVSSyntaxError(node, "HeldCondition() does not allow any keyword arguments.")
            hold_keyword = node.value.keywords[0]
            if hold_keyword.arg != "hold":
                raise EVSSyntaxError(
                    node,
                    "The only keyword argument allowed in Condition() is 'hold', to prevent the "
                    "interpreter from re-using the underlying index after it has been used (so "
                    "you can call it again as a 'finished' condition).",
                )
            if not isinstance(hold_keyword.value, ast.NameConstant) or hold_keyword.value.value is None:
                raise EVSSyntaxError(
                    node, f"'hold' can be True or False (default), " f"not {node.value.keywords[0].value}."
                )
            elif hold_keyword.value.value == "True":
                hold = True

        if isinstance(condition_argument, ast.BoolOp):
            if isinstance(condition_argument.op, ast.Or):
                i = self._check_out_OR(node, name=condition_name, hold=hold)
            else:
                assert isinstance(condition_argument.op, ast.And)
                i = self._check_out_AND(node, name=condition_name, hold=hold)
        else:
            if not isinstance(condition_argument, ConditionNodeTypes):
                raise EVSSyntaxError(node, f"Invalid Condition argument type: {type(condition_argument)}")
            i = self._check_out_AND(node, name=condition_name, hold=hold)
            return self._compile_condition(condition_argument, condition=i)

        condition_emevd = []
        for v in condition_argument.values:
            if not isinstance(v, ConditionNodeTypes):
                raise EVSSyntaxError(node, f"Invalid Condition argument type: {type(v)}")
            condition_emevd += self._compile_condition(v, condition=i)
        return condition_emevd

    # ~~~~~~~~~~~~~~~~
    #  PARSING METHODS: These return Python objects from nodes, not numeric EMEVD lines.
    # ~~~~~~~~~~~~~~~~

    def _parse_attributes(self, node: ast.Attribute):
        """Unpack and apply all nested Attribute nodes to their root object."""
        current_node = node
        attribute_stack = []  # stack
        while isinstance(current_node, ast.Attribute):
            if not isinstance(current_node.ctx, ast.Load):
                raise EVSSyntaxError(node, "Object attributes can only be read, not assigned to or deleted.")
            attribute_stack.append(current_node.attr)
            current_node = current_node.value  # generally Name or Call

        value = self._parse_nodes(current_node)
        while attribute_stack:
            attr = attribute_stack.pop()
            try:
                value = getattr(value, attr)
            except AttributeError:
                raise EVSAttributeError(node, value, attr)
        return value

    def _parse_name(self, node: ast.Name, test=False):
        """Get named object from parser namespace.

        Looks in current event arguments first, then global namespace. Raises an `EvsNameError` if name not found or
        an `EvsSyntaxError` if the name is a reserved event argument (currently "slot" and "event_layers").
        """
        name = node.id
        if name in self.current_event.args:
            if name in {"slot", "event_layers"}:
                raise EVSSyntaxError(node, f"Cannot use reserved event argument {repr(name)}.")
            arg = EventArgumentData(
                offset_tuple=self.current_event.args[name],
                arg_class=self.current_event.arg_classes.get(name, None),
            )
            if test and name in self.current_event.arg_classes:
                # TODO: Never used.
                # Bake arg into game type `__call__` method as 'self' (becomes a valid zero-argument test call).
                return partial(self.current_event.arg_classes[name].__call__, arg)
            return arg

        # Look in tests first (boolean objects), then 'for' loop variables, then globals.
        if name in self.tests:
            return self.tests[name]
        if name in self.for_vars:
            return self.for_vars[name]
        if name in self.globals:
            return self.globals[name]
        raise EVSNameError(node, name)

    def _parse_bin_op(self, node: ast.BinOp):
        """Parse simple binary operations."""
        left = self._parse_nodes(node.left)
        right = self._parse_nodes(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
        elif isinstance(node.op, ast.FloorDiv):
            return left // right
        raise EVSSyntaxError(node, f"Unsupported binary operation: {node.op}")

    def _parse_function_call(self, node: ast.Call):
        """Return the name (or None), positional args, and keyword arguments of function call node.

        If the function is an Attribute node rather a Name, then the returned name will be None.
        """
        if isinstance(node.func, ast.Name):
            name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            name = None
        else:
            raise EVSSyntaxError(node, f"Invalid callable node type: {type(node)}")
        args = self._parse_nodes(node.args)
        kwargs = self._parse_keyword_nodes(node.keywords)
        return name, args, kwargs

    def _compile_game_type_method(self, node, name, args, kwargs):
        """Parses and executes a game type method call, which are the only valid expressions other than instructions."""
        try:
            func = self.globals[name]
        except KeyError:
            raise EVSNameError(node, name)
        if not callable(func):
            raise EVSCallableError(node, name)
        return func(*args, **kwargs)

    def _parse_nodes(self, nodes, allowed_calls=()):
        """Returns the object(s) parsed from the given node as though it were standard Python.

        This includes string and numeric literals, imported and defined names, attributes, and lists/tuples of those
        things. Calls are only allowed if the name of the call is in the 'allowed_calls' argument. (Attribute calls are
        never allowed.)

        If a sequence of arg nodes is given, the function will recur on each of them and return a list.
        """
        if isinstance(nodes, (list, tuple)):
            return [self._parse_nodes(node, allowed_calls=allowed_calls) for node in nodes]

        if not isinstance(nodes, ast.AST):
            raise TypeError(f"Encountered non-node object to parse: {nodes}")
        node = nodes
        assert isinstance(node, ast.AST)

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            if not isinstance(node.operand, ast.Constant) or not isinstance(node.operand.value, (int, float)):
                raise EVSSyntaxError(
                    node.lineno,
                    f"`USub` node operand must be a number literal, not {type(node.operand)}."
                )
            return -node.operand.value
        elif isinstance(node, ast.Attribute):
            return self._parse_attributes(node)
        elif isinstance(node, ast.Name):
            return self._parse_name(node)
        elif isinstance(node, ast.BinOp):
            return self._parse_bin_op(node)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, (ast.List, ast.Tuple)):
            return [self._parse_nodes(sequence_node, allowed_calls=allowed_calls) for sequence_node in node.elts]
        elif isinstance(node, ast.Call):
            name, args, kwargs = self._parse_function_call(node)
            if name is not None and name in allowed_calls:
                return self._execute_function_call(name, args, kwargs, node.lineno)
            raise EVSValueError(node.lineno, f"Invalid callable: {repr(name)}.")
        raise EVSSyntaxError(
            node, f"Could not parse node of type {type(node)}. Node dump:\n    {ast.dump(node)}"
        )

    def _execute_function_call(self, name, args, kwargs, lineno):
        try:
            func = self.globals[name]
        except KeyError:
            try:
                # noinspection PyUnresolvedReferences
                func = __builtins__[name]
            except KeyError:
                raise EVSNameError(lineno, name)
        if not callable(func):
            raise EVSCallableError(lineno, name)
        return func(*args, **kwargs)

    def _parse_keyword_nodes(self, keywords):
        """Returns a kwargs dictionary built from the given keyword node(s)."""
        if isinstance(keywords, ast.keyword):
            return {keywords.arg: self._parse_nodes(keywords.value)}
        return {kw.arg: self._parse_nodes(kw.value) for kw in keywords}

    # ~~~~~~~~~~~~~~~~~~
    #  CONDITION METHODS: These provide and manage conditions that are in use by the current event.
    # ~~~~~~~~~~~~~~~~~~

    def _check_out_OR(self, node: ast.AST, name="_", hold=False):
        """ Check out next available OR condition register index. """
        if name != "_" and name in self.conditions:
            raise ConditionNameError(node, f"A condition named '{name}' already exists in this event.")
        for i in self.OR_SLOTS:
            if self.conditions[i] == "":
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        # Failed to find an empty condition, so get a non-held finished one. TODO: confirm this is safe in-game.
        for i in self.OR_SLOTS:
            if i in self.finished_conditions and i not in self.held_conditions:
                self.finished_conditions.remove(i)
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        raise ConditionLimitError(node, "No available OR conditions left in this event.")

    def _check_out_AND(self, node: ast.AST, name="_", hold=False):
        """ Check out next available AND condition register index. """
        if name != "_" and name in self.conditions:
            raise ConditionNameError(node, f"A condition named '{name}' already exists in this event.")
        for i in self.AND_SLOTS:
            if self.conditions[i] == "":
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        # Failed to find an empty condition, so get a non-held finished one. TODO: confirm this is safe in-game.
        for i in self.AND_SLOTS:
            if i in self.finished_conditions and i not in self.held_conditions:
                self.finished_conditions.remove(i)
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        raise ConditionLimitError(node, "No available AND conditions left in this event.")

    def _check_out_TEMP(self, lineno):
        """ Check out highest-numbered condition of either OR type (preferred) or AND type for temporary use (e.g when
        a simple skip cannot be used in a one-line IF statement, like 'if HealthRatio(PLAYER) <= 0: ...').

        This serves no purpose other than a convention (started by FromSoft themselves) to distinguish temporary
        one-test conditions from meaningful conditions containing multiple tests.
        """
        try:
            highest_or = max([abs(c) for c in self.OR_SLOTS if not self.conditions[c]])
        except ValueError:
            highest_or = 0
        try:
            highest_and = max([c for c in self.AND_SLOTS if not self.conditions[c]])
        except ValueError:
            highest_and = 0

        if highest_or == highest_and == 0:
            raise ConditionLimitError(lineno, "No conditions available to check out a temporary condition.")

        if highest_or >= highest_and:
            self.conditions[-highest_or] = "_"
            return -highest_or
        else:
            self.conditions[highest_and] = "_"
            return highest_and


def _parse_event_arguments(
    event_node: ast.FunctionDef
) -> tuple[dict[str, tuple[int, int]], str, dict[str, tp.Type[gt.GameObject]]]:
    """Parse argument nodes of given event function node and return:
        - dictionary mapping argument names to `(write_offset, size)` tuples for creating `EventArg` instances
        - event's argument format string, e.g. `"iIIBh"`
        - dictionary mapping argument names (where applicable) to `GameObject` subclasses
    """
    arg_names = []  # type: list[str]
    arg_types = ""
    arg_classes = {}  # type: dict[str, tp.Type[gt.GameObject]]

    if event_node.args.defaults:
        raise EVSSyntaxError(event_node, "You cannot provide default values for event arguments.")
    if event_node.args.vararg or event_node.args.kwarg:
        raise EVSSyntaxError(event_node, "You cannot use `*args` or `**kwargs` in event functions.")
    if event_node.args.kwonlyargs:
        raise EVSSyntaxError(event_node, "You cannot have keyword-only arguments in event functions.")

    for arg_node in event_node.args.args:
        arg_name = arg_node.arg
        if arg_name == "_":
            continue  # recommended intellisense placeholder for the first `slot` arg
        if arg_name in {"slot", "event_layers"}:
            # Previously raised an error here, but now allowing them for IDE purposes (but they do nothing). An error
            # will still be raised if you try to use either of these names in the event function body.
            continue
        arg_names.append(arg_name)

        arg_type_node = arg_node.annotation

        if isinstance(arg_type_node, ast.Constant) and isinstance(arg_type_node.value, str):
            if arg_type_node.value not in _EVS_TYPES:
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type string {repr(arg_type_node)}. "
                    f"Must be one of: {' '.join(_EVS_TYPES)}",
                )
            arg_type = arg_type_node.value

        elif isinstance(arg_type_node, ast.Name):
            try:
                arg_type = _PY_TYPES[arg_type_node.id]
            except KeyError:
                class_name = arg_type_node.id
                if class_name in gt.EMEVD_GAME_TYPES:
                    arg_classes[arg_name] = getattr(gt, class_name)
                    arg_type = "I"
                else:
                    raise EVSSyntaxError(
                        event_node,
                        f"{repr(class_name)} is not a valid game type for argument hinting.\n"
                        f"The available types are: {gt.EMEVD_GAME_TYPES}",
                    )
        else:
            raise EVSSyntaxError(
                event_node,
                f"Every event argument needs a type. You can specify any type with a type format\n"
                f"character in {repr(_EVS_TYPES)}, use a Soulstruct game type like `Flag` or `Character`,\n"
                f"or use the Python built-in types `int` (signed), `float`, or (in very rare cases) `str`.",
            )

        arg_types += arg_type

    arg_dict = {name: value for name, value in zip(arg_names, _define_args(arg_types))}

    return arg_dict, arg_types, arg_classes


def _parse_decorator(event_node: ast.FunctionDef) -> int:
    """Extract `RestartType` enum value from function decorator (default is 0)."""
    decorators = event_node.decorator_list
    if decorators:
        if len(decorators) > 1:
            raise EVSSyntaxError(
                event_node,
                f"Event function cannot have more than one decorator (restart type).\n"
                f"Must be one of: {', '.join(_RESTART_TYPES)}",
            )
        dec_node = decorators[0]
        if not isinstance(dec_node, ast.Name):
            raise EVSSyntaxError(
                event_node,
                f"Event function decorator must be a single name, not: {dec_node}.\n"
                f"Must be one of: {', '.join(_RESTART_TYPES)}",
            )
        try:
            return _RESTART_TYPES[dec_node.id]
        except KeyError:
            raise EVSSyntaxError(
                event_node,
                f"Invalid event function decorator: {dec_node.id}\n"
                f"Must be one of: {', '.join(_RESTART_TYPES)}",
            )
    return _RESTART_TYPES["NeverRestart"]


def _validate_comparison_node(node):
    """ Comparisons must:
        (a) only involve two values;
        (b) have a non-numeric value on the left and a numeric value on the right.
    """
    if len(node.comparators) != 1:
        raise EVSSyntaxError(node, "Comparisons must be binary.")

    if isinstance(node.left, ast.Num) or not isinstance(node.comparators[0], ast.Num):
        raise EVSSyntaxError(
            node, "Comparisons must be between a name or function (left) " "and number (right)."
        )

    if node.ops[0].__class__ not in COMPARISON_NODES:
        raise EVSSyntaxError(
            node, f"Only valid comparisons operators are: ==, !=, >, <, >=, <= (not {node.ops[0]})"
        )

    return node.left, node.ops[0].__class__, node.comparators[0].n


def _import_module(node: ast.Import, namespace: dict[str, tp.Any]):
    for alias in node.names:
        name = alias.name
        if _GAME_IMPORT_RE.match(name):
            return
        try:
            module = importlib.import_module(alias.name)
            importlib.reload(module)
        except ImportError as e:
            raise EVSImportError(node, alias.name, str(e))
        as_name = alias.asname if alias.asname is not None else name
        try:
            namespace[as_name] = getattr(module, name)
        except AttributeError as e:
            raise EVSImportError(node, name, str(e))


def _import_from(node: ast.ImportFrom, namespace: dict, script_directory: Path):
    """Import names into given namespace dictionary."""
    try:
        # Try to import and reload module normally.
        module = importlib.import_module(node.module)
        importlib.reload(module)
    except ImportError:
        # Try to import module on path.
        if script_directory is None:
            raise EVSImportError(
                node,
                node.module,
                "`script_directory` needed for relative import, but was not given to `EVSParser` or be detected.",
            )
        level = 0 if node.level == 0 else node.level - 1  # single dot (level 1) is the same as no dot (level 0)
        module_path = script_directory / ("../" * level + node.module.replace(".", "/") + ".py")
        if not module_path.is_file():
            raise EVSImportError(node, node.module, f"Cannot import missing module file: {module_path}")
        module = import_arbitrary_file(module_path)

    for alias in node.names:
        name = alias.name
        if _GAME_IMPORT_RE.match(name):
            return  # already imported
        if name == "*":
            if "__all__" in vars(module):
                all_names = vars(module)["__all__"]
            else:
                # Get all names that were defined in the module and don't begin with an underscore.
                module_name = node.module.split(".")[-1]
                all_names = [
                    n
                    for n, attr in vars(module).items()
                    if not n.startswith("_") and (not hasattr(attr, "__module__") or attr.__module__ == module_name)
                ]
            for name_ in all_names:
                try:
                    namespace[name_] = getattr(module, name_)
                except AttributeError as e:
                    _LOGGER.error(
                        f"EVS error: could not import {name_} from module {node.module} " f"(__all__ = {all_names})"
                    )
                    raise EVSImportFromError(node, node.module, name_, str(e))
        else:
            as_name = alias.asname if alias.asname is not None else name
            try:
                namespace[as_name] = getattr(module, name)
            except AttributeError as e:
                raise EVSImportFromError(node, node.module, name, str(e))
    del module


def _header(event_id, restart_type=0):
    return [f"{event_id}, {restart_type}"]


def _define_args(arg_types: str) -> list[tuple[int, int]]:
    """Converts an argument format string (e.g. `"iIIfB"`) to a list of `(write_offset, size)` tuples, usually for
    generating `EventArg` instances."""
    args = []
    for i, c in enumerate(arg_types):
        if c in "Bb":
            c_size = 1
        elif c in "Hh":
            c_size = 2
        elif c in "Iif":
            c_size = 4
        else:
            raise ValueError(f"Invalid format character '{c}' in `arg_types`.")
        args.append((get_write_offset(arg_types, i), c_size))
    return args


class EVSError(Exception):
    def __init__(self, lineno: tp.Union[ast.AST, EventStatementTyping, int], msg):
        if isinstance(lineno, ast.AST):
            lineno = lineno.lineno
        self.lineno = lineno
        super().__init__(f"LINE {lineno}: {msg}")


class EVSSyntaxError(EVSError):
    pass


class EVSValueError(EVSError):
    pass


class EVSImportError(EVSError):
    """Raised when a module cannot be imported."""

    def __init__(self, lineno, module, msg):
        super().__init__(
            lineno,
            f"Could not import {repr(module)}.\nError: {msg}",
        )


class EVSImportFromError(EVSError):
    """Raised when a name cannot be imported from a module."""

    def __init__(self, lineno, module, name, msg):
        super().__init__(lineno, f"Could not import {repr(name)} from module {repr(module)}. Error: {msg}")


class EVSNameError(EVSError):
    """Raised when an invalid (undefined) name is parsed."""

    def __init__(self, lineno, name):
        super().__init__(lineno, f"Name {repr(name)} has not been imported or defined.")


class EVSAttributeError(EVSError):
    """Raised when an attribute of an object cannot be retrieved."""

    def __init__(self, lineno, name, attribute):
        super().__init__(lineno, f"Object {repr(name)} has no attribute {repr(attribute)}.")


class EVSCallableError(EVSError):
    """Raised when an un-callable object is called."""

    def __init__(self, lineno, name):
        super().__init__(lineno, f"Object {name} is not callable.")


class ConditionError(EVSError):
    pass


class ConditionNameError(ConditionError):
    pass


class ConditionLimitError(ConditionError):
    pass
