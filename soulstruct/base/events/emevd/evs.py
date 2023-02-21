from __future__ import annotations

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

from soulstruct.base.game_types.basic_types import GameObject, FlagRange, MapFlagSuffix
from soulstruct.games import Game, get_game
from soulstruct.utilities.files import import_arbitrary_file
from .exceptions import NoNegateError, NoSkipOrReturnError
from .utils import (
    COMPARISON_NODES,
    NEG_COMPARISON_NODES,
    EventArgumentData,
    format_event_layers,
    get_write_offset,
)

_LOGGER = logging.getLogger(__name__)


# TODO: Set up unit tests on vanilla scripts, and some examples that make use of high-level functionality.
# TODO: Support event function imports from '.common_func', including kwarg names.


_MAP_ID_RE = re.compile(r"m(\d\d)_(\d\d)_")
_COMMON_FUNC_IMPORT_RE = re.compile(
    r"\n *# *\[COMMON_FUNC] *\nfrom (?P<dots>\.*)(?P<module>[\w_]+) +import \(?(?P<names>[*\w_, \n]+)\)?\n"
)
_RESTART_TYPES = {"ContinueOnRest": 0, "RestartOnRest": 1, "EndOnRest": 2}  # avoiding circular import
_EVENT_DOCSTRING_RE = re.compile(r"(\d+)(:\s*.*)?", re.DOTALL)
_CONDITION_GROUP_RE = re.compile(r"(MAIN|(AND|OR)_(\d+))")
_EVS_TYPES = ("B", "b", "H", "h", "I", "i", "f", "s")
_PY_TYPES = {"uchar": "B", "char": "b", "ushort": "H", "short": "h", "uint": "I", "int": "i", "float": "f", "str": "s"}
_BUILTIN_NAMES = {"Condition", "MAIN", "slot", "event_layers"}.union(_RESTART_TYPES.keys())
_IGNORE_IMPORT_RE = re.compile(r"^import typing.*")
_GAME_MODULE_RE = re.compile(r"^soulstruct\.(\w+)\..*$")


_EVENT_ARG_TYPE_MSG = f"""
    fmt character in: {repr(_EVS_TYPES)}
         fmt type in: ({', '.join(_PY_TYPES)})
           game type: e.g. `Flag`, `Character`, `Object`
         game typing: e.g. `FlagTyping`, `CharacterTyping`, `ObjectTyping`
     game type | int: e.g. `Flag | int`, `Character | int`, `Object | int`
"""


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
    arg_classes: dict[str, GAME_TYPE]
    on_rest_behavior: int
    nodes: list[ast.stmt]
    description: str


class EVSParser(abc.ABC):

    EMEDF_ALIASES: dict[str, tp.Any] = None
    EMEDF_TESTS: dict[str, tp.Any] = None
    EMEDF_COMPARISON_TESTS: dict[str, tp.Any] = None
    EVENTS_MODULE = None  # type: tp.Any
    GAME_TYPES = None  # type: tp.Any
    OR_SLOTS = []  # type: list[int, ...]
    AND_SLOTS = []  # type: list[int, ...]
    COMPILER: dict[str, tp.Callable]
    COMPILE: tp.Callable
    COMPILE_OBJECT_TEST: tp.Callable
    SUPPORTS_COMMON_FUNC: bool = False
    USES_COMMON_FUNC_SLOT: bool = False

    tree: ast.Module
    map_name: str
    map_base_flag: tp.Optional[int]
    script_directory: tp.Optional[Path]
    linked_offsets: list[int]
    strings_with_offsets: list[str]
    globals: dict[str, tp.Any]  # global script namespace
    for_vars: dict[str, tp.Any]  # local to each event function

    events: dict[str, EventInfo]  # information about each event function (collected before proper statement parsing)
    common_func_evs: EVSParser | None  # parser instance called on a COMMON_FUNC tagged import
    event_ids: set[int]  # set of event IDs used, so duplicates can easily be spotted

    held_conditions: list[int]
    finished_conditions: list[int]
    script_event_flags: dict[str, int]
    current_event: tp.Optional[EventInfo]
    event_function_strings: dict[str, str]  # maps function names (NOT IDs) to their numeric strings, in defined order

    numeric_emevd: str

    def __init__(self, evs_source: str | Path, map_name=None, script_directory=None):
        """Converts Python-like EVS code to numeric EMEVD (in `.numeric_emevd`), which can be fed to an `EMEVD` class.

        Args:
            evs_source: string or Path pointing to an EVS file, or direct string input (auto-detected based on
                any newlines being present in value).
            map_name: optional override for map name, which will otherwise be auto-detected from the EVS file name.
        """
        if isinstance(evs_source, Path) or "\n" not in evs_source:
            evs_path = Path(evs_source)
            with evs_path.open("r", encoding="utf-8") as script:
                evs_string = script.read()
            self.map_name = evs_path.name.split(".")[0] if map_name is None else map_name
            self.script_directory = Path(script_directory) if script_directory else evs_path.parent
        else:
            evs_string = evs_source  # raw EVS source given
            self.map_name = map_name
            self.script_directory = Path(script_directory) if script_directory else None

        if self.map_name is not None and (map_id_match := _MAP_ID_RE.match(self.map_name)):
            area, block = map_id_match.groups()
            self.map_base_flag = 10000000 + int(area) * 100000 + int(block) * 10000  # e.g. 11020000 for m10_02
        else:
            self.map_base_flag = None

        self.linked_offsets = []
        self.strings_with_offsets = []

        # Global namespace with game-specific enums and constants. May be updated with user imports and definitions.
        self.globals = vars(self.EVENTS_MODULE.enums)
        self.globals.update(vars(self.EVENTS_MODULE.constants))
        self.globals.update(vars(self.GAME_TYPES))
        # Note that there is no event-specific local namespace, except for this dictionary of 'for' loop variables:
        self.for_vars = {}

        self.events = {}  # Maps your event names to their IDs, so you can call them to initialize them.
        self.common_func_evs = None
        self.event_ids = set()  # Used to ensure the same ID is not repeated.

        self._reset_conditions()

        self.held_conditions = []  # These conditions won't be re-allocated.
        self.finished_conditions = []  # These conditions need to be accessed with 'finished' instruction variants.
        self.yoked_conditions = {}  # Maps conditions to sets of other conditions that have been loaded into them.

        self.script_event_flags = {}
        self.current_event = None
        self.event_function_strings = {}

        evs_string = self._import_common_funcs(evs_string)

        self.tree = ast.parse(evs_string)
        self.numeric_emevd = ""
        self._compile_evs()

    @classmethod
    def get_game(cls) -> Game:
        if match := re.match(_GAME_MODULE_RE, cls.__module__):
            return get_game(match.group(1))
        raise ValueError(f"Could not detect game name from module of class `{cls.__name__}`: {cls.__module__}")

    def _reset_conditions(self):
        """Reset for every new event. Contains names of `Condition` and/or `HeldCondition` instances created in EVS."""
        self.conditions = [""] * (len(self.OR_SLOTS) + len(self.AND_SLOTS) + 1)

    def _import_common_funcs(self, evs_string: str):
        for common_func_import_match in re.finditer(_COMMON_FUNC_IMPORT_RE, evs_string):
            # TODO: Could theoretically support importing from multiple COMMON_FUNC modules (especially for DS1).
            groups = common_func_import_match.groupdict()
            level = len(groups["dots"])
            if level == 1:
                level = 0  # single dot is the same as no dot (same directory)
            cf_module_name = groups["module"]
            if self.common_func_evs:
                raise EVSCommonFuncImportError(cf_module_name, "", "Can only import one [COMMON_FUNC] module.")
            if groups["names"] != "*" and "*" in groups["names"]:
                raise EVSCommonFuncImportError(
                    cf_module_name, groups["names"], "Invalid import names from COMMON_FUNC (contains asterisk)."
                )
            cf_module_path = self.script_directory / ("../" * level + cf_module_name.replace(".", "/") + ".py")
            if not cf_module_path.is_file():
                raise EVSCommonFuncImportError(
                    cf_module_name, "", f"Cannot import missing COMMON_FUNC file: {cf_module_path}."
                )
            if self.SUPPORTS_COMMON_FUNC:
                self.common_func_evs = self.__class__(
                    cf_module_path, script_directory=self.script_directory
                )
            else:
                self.common_func_evs = self.__class__(  # force this map's base flag
                    cf_module_path, map_name=self.map_name, script_directory=self.script_directory
                )
            if groups["names"] != "*":
                cf_imported_names = [name.strip(" \n") for name in groups["names"].split(",")]
                for cf_name in cf_imported_names:
                    if cf_name not in self.common_func_evs.events:
                        raise EVSCommonFuncImportError(
                            cf_module_name, cf_name, "Common func name not found in parsed EVS source file."
                        )
                # Remove non-imported names from common EVS.
                for event_name in tuple(self.common_func_evs.events):
                    if event_name not in cf_imported_names:
                        event_info = self.common_func_evs.events.pop(event_name)
                        self.common_func_evs.event_ids.remove(event_info.id)
            # Otherise, star import preserves all names from common module.

        # Strip these imports from the EVS string before it is parsed properly.
        return re.sub(_COMMON_FUNC_IMPORT_RE, "\n", evs_string)

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
        on_rest_behavior, event_id = self._parse_decorator(node)

        docstring = ast.get_docstring(node)
        if docstring is None:
            if event_id == -1:
                raise EVSSyntaxError(
                    node,
                    f"No docstring given for event {event_name}, and no event ID was given in the decorator. See EVS "
                    f"documentation for more details."
                )
            description = ""
        else:
            try:
                doc_event_id, description = _EVENT_DOCSTRING_RE.match(docstring).group(1, 2)
            except AttributeError:
                if event_id == -1:
                    raise EVSSyntaxError(
                        node,
                        f"Invalid docstring for event {event_name}. Note that the docstring must start with an event "
                        f"ID if one is not given in the decorator. See EVS documentation for more details."
                    )
                description = ""
            else:
                doc_event_id = int(doc_event_id)
                if event_id != -1 and event_id != doc_event_id:
                    raise EVSSyntaxError(node, f"Different event IDs were given in decorator and docstring.")
                event_id = doc_event_id

        if event_id in self.event_ids:
            raise EVSSyntaxError(node, f"Event ID {event_id} is defined multiple times in EVS script.")
        elif event_id == 0:
            if event_name.lower() not in {"event0", "constructor"}:
                raise EVSSyntaxError(node, "Event 0 must be called 'Constructor' (or 'Event0').")
        elif event_id == 50:
            if event_name.lower() not in {"event50", "preconstructor"}:
                raise EVSSyntaxError(node, "Event 50 must be called 'Preconstructor' (or 'Event50').")
        elif event_name.lower() in {"constructor", "preconstructor"}:
            raise EVSSyntaxError(
                node, "Builtin event names 'Constructor' and 'Preconstructor' are reserved for events 0 and 50."
            )

        description = "" if not description else description.lstrip(":")  # Remove leading colon.

        arg_dict, arg_types, arg_classes = _parse_event_arguments(node, self.globals)

        self.events[event_name] = EventInfo(
            name=event_name,
            id=event_id,
            args=arg_dict,
            arg_types=arg_types,
            arg_classes=arg_classes,
            on_rest_behavior=on_rest_behavior,
            nodes=node.body if docstring is None else node.body[1:],  # skip docstring, if present
            description=description.lstrip(":"),
        )
        self.event_ids.add(event_id)

    def _validate_event_name(self, event_node: ast.FunctionDef):
        name = event_node.name
        if name in self.EMEDF_ALIASES or name in {"Await", "EnableThisFlag", "DisableThisFlag"}:
            raise EVSSyntaxError(event_node, f"Event name cannot match an instruction name ({name}).")
        if name in _BUILTIN_NAMES or _CONDITION_GROUP_RE.match(name):
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

        game = self.get_game()
        ignore_import_names = [
            "typing",
            f"soulstruct.{game.submodule_name}.events",
            f"soulstruct.{game.submodule_name}.events.instructions",
            f"soulstruct.{game.submodule_name}.events.tests",
        ]

        for node in self.tree.body[1:]:
            if isinstance(node, ast.Import):
                self.globals |= _import_module(node, ignore_names=ignore_import_names)
            elif isinstance(node, ast.ImportFrom):
                self.globals |= _import_from(node, self.script_directory, ignore_names=ignore_import_names)
            elif isinstance(node, ast.FunctionDef):
                self._scan_event(node)
            elif isinstance(node, ast.Assign):
                self._assign_name(node)
            elif isinstance(node, ast.ClassDef):
                continue  # Class definitions (e.g. enums) are collected from the real Python parser.
            elif isinstance(node, ast.AnnAssign):
                continue  # type hints are allowed and ignored
            else:
                raise EVSSyntaxError(
                    node.lineno,
                    f"Invalid content: {node.__class__}. The only valid global EVS lines are "
                    f"from-imports, event script function definitions, and global name assignments.",
                )

        if self.common_func_evs and not self.SUPPORTS_COMMON_FUNC:
            # Add common_func events in now, after local events.
            self.events |= self.common_func_evs.events
            self.event_ids |= self.common_func_evs.event_ids

        for event_name, event_function in self.events.items():
            self.current_event = self.events[event_name]
            self.for_vars = {}
            self._reset_conditions()
            self.finished_conditions = []
            parsed_event = self._compile_event_function(event_function)  # numeric format
            self.event_function_strings[event_name] = "\n".join(parsed_event)

        self.numeric_emevd = "\n\n".join(self.event_function_strings.values())
        self.numeric_emevd += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_offsets)
        self.numeric_emevd += "\n\nstrings:\n" + "\n".join(self.strings_with_offsets)

    def _compile_event_function(self, event_info: EventInfo):
        """ Writes header, then iterates over all nodes in function body. """

        event_emevd = _header(event_info.id, event_info.on_rest_behavior)

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
                return self.COMPILE("End")
            elif isinstance(node.value, ast.Name) and node.value.id == "RESTART":
                return self.COMPILE("Restart")
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

    def _compile_event_call(self, node: ast.Call, is_common_func=False):
        """Shortcut for RunEvent(...) instruction."""
        name, args, kwargs = self._parse_function_call(node)
        event_info = self.common_func_evs.events[name] if is_common_func else self.events[name]
        kwargs = self._parse_keyword_nodes(node.keywords)
        event_layer_string = format_event_layers(kwargs.pop("event_layers", None))

        if not args and not kwargs and not event_info.args:
            # Events with no arguments can be called with no argument, ignoring `event_layers` (`slot` defaults to 0).
            # Common events can also be called without arguments.
            if is_common_func:
                instruction = self._compile_instr(node, "RunCommonEvent", event_info.id)
            else:
                instruction = self._compile_instr(node, "RunEvent", event_info.id)
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

        if is_common_func and not self.USES_COMMON_FUNC_SLOT:
            if slot != 0:
                raise EVSSyntaxError(
                    node.lineno, f"This game does not support non-zero slot arguments for imported common events."
                )
            slot = None

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
                print(name, args, kwargs)
                print(event_info.args)
                raise EVSValueError(
                    node,
                    f"Number of positional arguments in event call (excluding the slot), {len(args)}, does not match "
                    f"the event function signature:\n"
                    f"    {['slot'] + list(event_info.args.keys())}.",
                )

        event_id = event_info.id
        args = (0,) if not args else args
        arg_types = event_info.arg_types if event_info.arg_types else None

        instr_name = "RunCommonEvent" if is_common_func else "RunEvent"
        if slot is None:
            instruction = self.COMPILER[instr_name](event_id, args=args, arg_types=arg_types)
        else:
            instruction = self.COMPILER[instr_name](event_id, slot=slot, args=args, arg_types=arg_types)
        instruction[0] += event_layer_string
        return instruction

    def _compile_instruction(self, node: ast.Call):
        """Build instruction arguments and call the instruction (which will return a numeric line)."""
        name, args, kwargs = self._parse_function_call(node)
        event_layers = kwargs.pop("event_layers", None)
        instruction_lines = self._compile_instr(node, name, *args, **kwargs)

        try:
            instruction_lines[0] += format_event_layers(event_layers)
        except TypeError:
            raise EVSSyntaxError(node, "If given, `event_layers` must be a list, tuple, or single integer.")
        return instruction_lines

    @staticmethod
    def _check_condition_group_add(node: ast.Call) -> tp.Optional[int]:
        """Returns condition index if this is a condition group `.Add()` or `.Await()` call, or `None` otherwise."""
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "Add"
            and isinstance(node.func.value, ast.Name)
            and (match := _CONDITION_GROUP_RE.match(node.func.value.id))
        ):
            if match.group(1) == "MAIN":
                _LOGGER.warning(f"MAIN condition used in an `Add()` call on line {node.lineno}. This is unusual.")
                return 0
            return (-1 if match.group(2) == "OR" else 1) * int(match.group(3))
        elif (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "Await"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "MAIN"
        ):
            return 0
        return None

    def _compile_function_expression(self, node: ast.Call):

        if (condition := self._check_condition_group_add(node)) is not None:
            if node.keywords or len(node.args) != 1:
                raise EVSSyntaxError(
                    node,
                    ".Add() or .Await() take exactly one positional argument (Condition or boolean expression)."
                )
            arg = node.args[0]
            if not isinstance(arg, ConditionNodeTypes):
                raise EVSSyntaxError(
                    node,
                    f".ADd() or .Await() argument must be a Condition or boolean expression, not: {type(arg)}."
                )
            return self._compile_condition(arg, condition=condition)

        if isinstance(node.func, ast.Attribute):
            # Method of a game object or `.Add` method of a condition group.
            attr = node.func.attr
            game_object = self._parse_nodes(node.func.value)
            if not isinstance(game_object, GameObject):
                raise EVSSyntaxError(
                    node, "Only methods of `GameObject` subclasses can be called as instructions."
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
        if self.common_func_evs and self.SUPPORTS_COMMON_FUNC and name in self.common_func_evs.events:
            return self._compile_event_call(node, is_common_func=True)

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
                return self._compile_instr(node, "EnableFlag", self.current_event.id)
            return self._compile_instr(node, "DisableFlag", self.current_event.id)

        if name in self.EMEDF_ALIASES or name in self.COMPILER:
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

        # 2. Build the test line. This could be a simple skip, a multi-line chain skip, or a skip that uses a fully-
        #    fledged Condition, depending on the test. Note that the body length has 1 added (an extra skip line) if
        #    there is an ELSE body in the statement, and does not include arg replacement lines.
        body_length = len([line for line in body_emevd if not line.startswith("    ^")])
        if node.orelse:
            body_length += 1
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
            if_emevd += self._compile_instr(node, "SkipLines", skip_line_count)
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
                try:
                    return self.COMPILE_OBJECT_TEST(
                        arg_class,
                        arg,
                        negate=negate,
                        skip_lines=skip_lines,
                        end_event=end_event,
                        restart_event=restart_event,
                    )
                except TypeError:
                    raise EVSValueError(node.lineno, f"Event argument type {repr(arg_class)} is not testable.")
            raise EVSValueError(
                node.lineno,
                f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                f"such as `Flag` (tests for enabled state), `Region` (tests if player is inside), etc.",
            )

        # 3. The condition is a previously-defined `Condition` or `HeldCondition` instance.
        if isinstance(node, ast.Name) and node.id in self.conditions:
            i = self.conditions.index(node.id)
            if i > len(self.AND_SLOTS):
                # Negative OR slot, e.g., 9 -> -6 for MAIN/7/7 slot games
                i -= len(self.conditions)
            try:
                return self._compile_condition_skip_or_return(node, i, negate, skip_lines, end_event, restart_event)
            except ValueError:
                raise EVSError(
                    node.lineno,
                    "(internal) Cannot resolve simple condition check: 'skip_lines, 'end_event', and "
                    "'restart_event' are all 0 or False.",
                )

        # 4. The condition is a condition group such as `AND_01`. (It cannot be `MAIN`.)
        if isinstance(node, ast.Name) and (match := _CONDITION_GROUP_RE.match(node.id)):
            if match.group(1) == "MAIN":
                _LOGGER.warning(
                    f"MAIN condition used in a skip/return instruction on line {node.lineno}. This is unusual."
                )
                i = 0
            else:
                i = (-1 if match.group(2) == "OR" else 1) * int(match.group(3))
            try:
                return self._compile_condition_skip_or_return(node, i, negate, skip_lines, end_event, restart_event)
            except ValueError:
                raise EVSError(
                    node.lineno,
                    "(internal) Cannot resolve simple condition check: 'skip_lines, 'end_event', and "
                    "'restart_event' are all 0 or False.",
                )

        # 5. The condition is a 'compilable' game object in the global namespace that requires no arguments.
        if isinstance(node, (ast.Attribute, ast.Name)):
            game_object = self._parse_nodes(node)  # This will raise an EmevdNameError if the name is invalid.
            if not isinstance(game_object, GameObject):
                raise EVSValueError(
                    node.lineno, f"Only (some) `GameObjectObject` subclasses are directly testable."
                )
            if isinstance(game_object, FlagRange):
                raise EVSValueError(
                    node.lineno,
                    "Cannot implicitly use a `FlagRange` as a condition.\n"
                    "Call `any()`, `all()`, `not any()`, or `not all()` on it to test it.",
                )
            try:
                return self.COMPILE_OBJECT_TEST(
                    type(game_object),
                    game_object,
                    negate=negate,
                    skip_lines=skip_lines,
                    end_event=end_event,
                    restart_event=restart_event,
                )
            except TypeError:
                raise EVSValueError(node.lineno, f"Object `{game_object}` is not testable.")

        # 6. The condition is a binary comparison operation.
        if isinstance(node, ast.Compare):
            return self._compile_simple_comparison(node, negate, skip_lines)

        # 7. The condition is a test function call.
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in self.EMEDF_TESTS:
            # Get arguments.
            args = self._parse_nodes(node.args)
            kwargs = self._parse_keyword_nodes(node.keywords)
            # TODO: event_layers
            return self._try_compile_test(
                node.func,
                *args,
                skip_lines=skip_lines, negate=negate, end_event=end_event, restart_event=restart_event,
                **kwargs,
            )  # This will raise the same error as below.

        # 8. The condition is any() or all() called on a FlagRange or a sequence of simple skips that can be chained.
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
        left_node, op_node, comparison_value = self._validate_comparison_node(node)
        if isinstance(left_node, ast.Name):
            name = left_node.id
            try:
                arg = self.current_event.args[name]
            except KeyError:
                raise NoSkipOrReturnError
            if not negate:  # note inversion
                return self._compile_instr(
                    node, "SkipLinesIfValueComparison", skip_lines, NEG_COMPARISON_NODES[op_node], arg, comparison_value
                )
            return self._compile_instr(
                node, "SkipLinesIfValueComparison", skip_lines, COMPARISON_NODES[op_node], arg, comparison_value
            )
        raise NoSkipOrReturnError

    def _compile_range_test(self, node: ast.Call, negate, skip_lines):
        """`node` must be an `all()` or `any()` call with a single argument (already checked by caller).

        This single argument must be a `range()` call or `FlagRange` object.
        """
        assert isinstance(node.func, ast.Name)
        arg = node.args[0]

        # Note negation here, because this will be a skip.
        if node.func.id == "all":
            tests = ["AllDisabled", "AnyEnabled"]
        else:  # if node.func.id == "any":
            tests = ["AllEnabled", "AnyDisabled"]

        if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name) and arg.func.id == "range":
            if len(arg.args) != 2:
                raise EVSSyntaxError(
                    node, "`range()` used inside `all()` or `any()` must have exactly two arguments: `(first, last)`."
                )
            first, last = self._parse_nodes(arg.args)
            return self._compile_instr(node, "SkipLinesIfFlagRange" + tests[negate], skip_lines, (first, last))
        else:
            flag_range = self._parse_nodes(arg)
            if isinstance(flag_range, FlagRange):
                return self._compile_instr(node, "SkipLinesIfFlagRange" + tests[negate], skip_lines, flag_range)
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
                    chain_skip_emevd += self._compile_instr(node, "SkipLines", skip_lines)  # Extra skip required.
                return chain_skip_emevd

        raise NoSkipOrReturnError

    def _compile_condition(
        self,
        node: ConditionNodeTyping,
        negate=False,
        condition=None,
        skip_lines=0,
    ):
        """Called on the argument of Condition() or Await(), or on a non-simple IF test node.

        Always results in the use of a condition group, but if `skip_lines` is given instead of `condition`, that group
        may just be temporary group that is immediately used in a line skip.
        """
        if condition is None and skip_lines == 0:
            raise ValueError("Either 'condition' index or 'skip_lines' count must be specified.")
        if condition is not None and skip_lines != 0:
            raise ValueError("Do not use 'condition' and 'skip_lines' at the same time.")
        if skip_lines < 0:
            raise ValueError("Cannot skip a negative number of lines.")

        emevd_args = []
        emevd_kwargs = {}

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
            node, op_node, comparison_value = self._validate_comparison_node(node)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id not in self.EMEDF_COMPARISON_TESTS:
                    raise EVSSyntaxError(node.lineno, f"Invalid test function for binary comparison: {node.func.id}")
                emevd_args += self._parse_nodes(node.args)
                emevd_kwargs.update(self._parse_keyword_nodes(node.keywords))
                emevd_kwargs.update(
                    comparison_type=(NEG_COMPARISON_NODES if negate else COMPARISON_NODES)[op_node],
                    value=comparison_value,
                )
                node = node.func  # `Name` node handled below.
                # Modify test name, e.g., `HealthRatio` -> `HealthRatioComparison`, so 'Test function' check catches it.
                node.id = self.EMEDF_COMPARISON_TESTS[node.id]["test_name"]
            else:
                raise EVSSyntaxError(
                    node.lineno,
                    "Left value in a binary comparison must be a test function call, "
                    "such as `if Health(character) <= 0.1: ...`."
                )

        # Testable event argument
        if isinstance(node, ast.Name) and node.id in self.current_event.args:
            if node.id in self.current_event.arg_classes:
                arg = self.current_event.args[node.id]
                arg_class = self.current_event.arg_classes[node.id]
                try:
                    return self.COMPILE_OBJECT_TEST(
                        arg_class,
                        arg,
                        negate=negate,
                        condition=condition,
                        skip_lines=skip_lines,
                    )
                except TypeError:
                    raise EVSValueError(node.lineno, f"Event argument type {repr(arg_class)} is not testable.")
            raise EVSValueError(
                node.lineno,
                f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                f"such as `Flag` (tests for enabled state), `Region` (tests if player is inside), etc.",
            )

        # Existing condition (with standard name)
        if isinstance(node, ast.Name) and (match := _CONDITION_GROUP_RE.match(node.id)):
            if not isinstance(condition, int):
                raise EVSSyntaxError(
                    node.lineno, f"(internal) Tried to compile custom condition '{node.id}' with `condition=None`."
                )
            if match.group(1) == "MAIN":
                _LOGGER.warning(f"MAIN condition used in another condition on line {node.lineno}. This is unusual.")
                i = 0  # does happen very rarely
            else:
                i = (-1 if match.group(2) == "OR" else 1) * int(match.group(3))
                if i in self.finished_conditions:
                    # This condition slot is being used again. It is no longer considered 'finished' and cannot be used
                    # in 'IfFinishedCondition' checks.
                    self.finished_conditions.remove(i)
                self._check_finished_conditions(condition, i)
            logic = "False" if negate else "True"
            return self._compile_instr(node, f"IfCondition{logic}", condition, i)

        # Existing condition (with custom name)
        if isinstance(node, ast.Name) and node.id in self.conditions:
            if not isinstance(condition, int):
                raise EVSSyntaxError(
                    node.lineno, f"(internal) Tried to compile custom condition '{node.id}' with `condition=None`."
                )
            i = self.conditions.index(node.id)
            if i > len(self.AND_SLOTS):
                # Negative OR slot, e.g., 9 -> -6 for MAIN/7/7 slot games
                i -= len(self.conditions)
            if i in self.finished_conditions:
                # This condition slot is being used again. It is no longer considered 'finished' and cannot be used in
                # 'IfFinishedCondition' checks.
                self.finished_conditions.remove(i)
            self._check_finished_conditions(condition, i)
            logic = "False" if negate else "True"
            return self._compile_instr(node, f"IfCondition{logic}", condition, i)

        # Call
        if isinstance(node, ast.Call):
            emevd_args += self._parse_nodes(node.args)
            emevd_kwargs.update(self._parse_keyword_nodes(node.keywords))
            node = node.func  # -> ast.Name (parsed below)

        # Test function
        if isinstance(node, ast.Name) and node.id in self.EMEDF_TESTS:
            try:
                return self._try_compile_test(
                    node, *emevd_args, negate=negate, condition=condition, skip_lines=skip_lines, **emevd_kwargs
                )
            except (NoSkipOrReturnError, NoNegateError):
                # No builtin tests for skipping, terminating, and/or negating condition. Need temp Condition.
                condition_emevd = []
                temp_condition = self._check_out_TEMP(node.lineno)
                skip_negate = False if skip_lines > 0 else negate  # avoids double negative with negated skip
                logic = str(bool(negate) if skip_lines > 0 else not bool(negate))
                # Compile temporary condition.
                condition_emevd += self._try_compile_test(
                    node, *emevd_args, negate=skip_negate, condition=temp_condition, **emevd_kwargs
                )
                instr = f"SkipLinesIfCondition{logic}"
                condition_emevd += self._compile_instr(node, instr, skip_lines, temp_condition)
                return condition_emevd
            except ValueError as ex:
                raise EVSError(node.lineno, f"Error occurred in test function '{node.id}': {ex}")

        # Constant / Event Argument
        if isinstance(node, (ast.Attribute, ast.Name)):
            game_object = self._parse_nodes(node)  # This will raise an `EmevdNameError` if the name is invalid.
            if not isinstance(game_object, GameObject):
                raise EVSValueError(
                    node.lineno,
                    f"Only (some) `GameObject` subclasses are directly testable, not {type(game_object).__name__}.",
                )
            elif isinstance(game_object, FlagRange):
                raise EVSValueError(
                    node.lineno,
                    "Cannot implicitly use a `FlagRange` as a condition.\n"
                    "Call any() or all() on it (with or without 'not' in front) to test it.",
                )
            try:
                return self.COMPILE_OBJECT_TEST(
                    type(game_object),
                    game_object,
                    negate=negate,
                    condition=condition,
                    skip_lines=skip_lines,
                )
            except TypeError:
                raise EVSValueError(node.lineno, f"Object {repr(game_object)} is not testable.")
            except (NoSkipOrReturnError, NoNegateError):
                # No builtin tests for terminating/negating condition. Need to construct a temporary one.
                condition_emevd = []
                temp_condition = self._check_out_TEMP(node.lineno)
                skip_negate = False if skip_lines > 0 else negate  # avoids double negative with negated skip
                logic = str(bool(negate) if skip_lines > 0 else not bool(negate))
                instr = f"SkipLinesIfCondition{logic}"
                condition_emevd += self._compile_condition(node, negate=skip_negate, condition=temp_condition)
                condition_emevd += self._compile_instr(node, instr, skip_lines, temp_condition)
                return condition_emevd

        # Failure to compile the condition will be raised as a genuine syntax error, unlike the skip/return compiler.
        # noinspection PyTypeChecker
        raise EVSSyntaxError(node.lineno, f"Invalid node for condition content:\n{ast.dump(node)}")

    def _compile_condition_skip_or_return(
        self, node, condition, negate=False, skip_lines=0, end_event=False, restart_event=False
    ):
        if skip_lines > 0:
            if negate:
                if condition in self.finished_conditions:
                    return self._compile_instr(node, "SkipLinesIfFinishedConditionTrue", skip_lines, condition)
                return self._compile_instr(node, "SkipLinesIfConditionTrue", skip_lines, condition)
            if condition in self.finished_conditions:
                return self._compile_instr(node, "SkipLinesIfFinishedConditionFalse", skip_lines, condition)
            return self._compile_instr(node, "SkipLinesIfConditionFalse", skip_lines, condition)
        elif end_event:
            if negate:
                if condition in self.finished_conditions:
                    return self._compile_instr(node, "EndIfFinishedConditionFalse", condition)
                return self._compile_instr(node, "EndIfConditionFalse", condition)
            if condition in self.finished_conditions:
                return self._compile_instr(node, "EndIfFinishedConditionTrue", condition)
            return self._compile_instr(node, "EndIfConditionTrue", condition)
        elif restart_event:
            if negate:
                if condition in self.finished_conditions:
                    return self._compile_instr(node, "RestartIfFinishedConditionFalse", condition)
                return self._compile_instr(node, "RestartIfConditionFalse", condition)
            if condition in self.finished_conditions:
                return self._compile_instr(node, "RestartIfFinishedConditionTrue", condition)
            return self._compile_instr(node, "RestartIfConditionTrue", condition)
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
            condition_emevd += self._compile_instr(node, instr, skip_lines, i)
        elif finished:
            raise EVSValueError(node, "Cannot use a finished condition as an input to another condition.")
        else:
            logic = "False" if negate else "True"
            instr = f"IfCondition{logic}"
            condition_emevd += self._compile_instr(node, instr, condition, i)
            self._check_finished_conditions(condition, i)
        return condition_emevd

    def _compile_instr(self, node, instr_name, *args, **kwargs) -> list[str]:
        """Try to `COMPILE` instruction, raising a syntax error if it fails."""
        try:
            return self.COMPILE(instr_name, *args, **kwargs)
        except Exception as ex:
            print(instr_name, args, kwargs)
            raise EVSSyntaxError(node, f"Failed to auto-compile instruction {instr_name}.\n    Error: {ex}")

    def _check_finished_conditions(self, output_condition: int, input_condition: int):
        if output_condition == 0:
            self.finished_conditions.append(input_condition)
            if input_condition in self.yoked_conditions:
                # We pop condition keys first, as some dodgy vanilla events do create loops of condition groups.
                yoked_conditions = sorted(self.yoked_conditions.pop(input_condition))
                self._finish_yoked_conditions(*yoked_conditions)  # recursive
        else:
            # Input condition `i` is now yoked to `condition` and will be finished whenever `condition` is loaded
            # into MAIN (0).
            self.yoked_conditions.setdefault(output_condition, set()).add(input_condition)

    def _finish_yoked_conditions(self, *conditions: int):
        for condition in conditions:
            if condition not in self.finished_conditions:
                self.finished_conditions.append(condition)
            if condition in self.yoked_conditions:
                yoked_conditions = sorted(self.yoked_conditions.pop(condition))
                self._finish_yoked_conditions(*yoked_conditions)

    def _try_compile_test(
        self,
        node: ast.Name,
        *args,
        condition=None,
        skip_lines=0,
        negate=False,
        end_event=False,
        restart_event=False,
        **kwargs,
    ):
        tests = self.EMEDF_TESTS[node.id]
        event_layers = format_event_layers(kwargs.pop("event_layers", None))
        instruction_lines = []

        if negate:
            # TODO: Look up 'negate' key of test to redirect (or raise `NoNegateError`).
            # tests = tests["negate"]
            raise EVSError(node, f"Cannot yet support `not` keyword with test functions.")

        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if "skip" not in tests:
                raise NoSkipOrReturnError
            # `line_count` is always the first positional argument.
            instruction_lines = self._compile_instr(node, tests["skip"], skip_lines, *args, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            # "if" is always present in tests. `condition` is always the first positional argument.
            instruction_lines = self._compile_instr(node, tests["if"], condition, *args, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if "end" not in tests:
                raise NoSkipOrReturnError
            instruction_lines = self._compile_instr(node, tests["end"], *args, **kwargs)

        if restart_event:
            if "restart" not in tests:
                raise NoSkipOrReturnError
            instruction_lines = self._compile_instr(node, tests["restart"], *args, **kwargs)

        if instruction_lines:
            instruction_lines[0] += event_layers
            return instruction_lines

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

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
            if name in self.EMEDF_ALIASES or name in {"Await", "EnableThisFlag", "DisableThisFlag"}:
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
        if self.current_event and name in self.current_event.args:
            # Name is an event argument.
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

        # Check if name is a condition group.
        if match := _CONDITION_GROUP_RE.match(name):
            if match.group(1) == "MAIN":
                return 0
            condition = (-1 if match.group(2) == "OR" else 1) * int(match.group(3))
            if condition not in self.AND_SLOTS + self.OR_SLOTS:
                raise EVSValueError(node, f"Invalid condition group name for EMEVD: {name} (group index {condition})")
            return condition

        # Look in 'for' loop variables, then globals.
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
        elif isinstance(node.op, ast.BitOr):
            return left | right
        elif isinstance(node.op, ast.BitAnd):
            return left & right
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

    def _validate_comparison_node(self, node):
        """ Comparisons must:
            (a) only involve two values;
            (b) have a non-numeric value on the left and a numeric value or attribute on the right.
        """
        if len(node.comparators) != 1:
            raise EVSSyntaxError(node, "Comparisons must be binary.")

        if isinstance(node.left, ast.Num):
            raise EVSSyntaxError(
                node, "Comparisons must be between a name or function (left) and number (right)."
            )

        comparator = self._parse_nodes(node.comparators[0])
        if not isinstance(comparator, (int, float, EventArgumentData)):
            raise EVSSyntaxError(
                node,
                f"Comparisons must be between a name or function (left) and number or event argument (right), but "
                f"right value is {comparator}."
            )

        if node.ops[0].__class__ not in COMPARISON_NODES:
            raise EVSSyntaxError(
                node, f"Only valid comparisons operators are: ==, !=, >, <, >=, <= (not {node.ops[0]})"
            )

        return node.left, node.ops[0].__class__, comparator

    def _parse_decorator(self, event_node: ast.FunctionDef) -> tuple[int, int]:
        """Extract `OnRestBehavior` enum value (default is 0) and event ID (default is -1) from function decorator."""
        decorators = event_node.decorator_list
        if not decorators:
            return _RESTART_TYPES["ContinueOnRest"], -1

        if len(decorators) > 1:
            raise EVSSyntaxError(
                event_node,
                f"Event function cannot have more than one decorator (restart type).\n"
                f"Must be one of: {', '.join(_RESTART_TYPES)}",
            )

        dec_node = decorators[0]
        if isinstance(dec_node, ast.Name):  # e.g. just `@ContinueOnRest`
            name = dec_node.id
            event_id = -1
        elif isinstance(dec_node, ast.Call):  # e.g. `@ContinueOnRest(11020000)`
            name, args, kwargs = self._parse_function_call(dec_node)
            if kwargs or len(args) != 1 or not isinstance(args[0], int):
                raise EVSSyntaxError(
                    event_node,
                    f"Event function decorator must have exactly one numeric argument (event ID).",
                )
            event_id = args[0]
            if isinstance(event_id, MapFlagSuffix):
                if self.map_base_flag is None:
                    # noinspection PyTypeChecker
                    raise EVSSyntaxError(
                        dec_node,
                        f"MapFlagSuffix `{event_id}` cannot be used when map base flag is unknown. (Pass `map_name` to "
                        f"the EVS parser explicitly if your EVS file name does not start with the usual 'mAA_BB_'.)",
                    )
                event_id += self.map_base_flag
        else:
            raise EVSSyntaxError(
                event_node,
                f"Event function decorator must be `@ContinueOnRest`, `@RestartOnRest`, or `@EndOnRest`, with the event"
                f" ID given as a decorator argument (e.g., `@RestartOnRest(11020100)`), not: {dec_node}.",
            )

        try:
            on_rest_behavior = _RESTART_TYPES[name]
        except KeyError:
            raise EVSSyntaxError(
                event_node,
                f"Event function decorator name is not a valid event restart type: {dec_node.id}\n"
                f"Must be one of: {', '.join(_RESTART_TYPES)}",
            )

        return on_rest_behavior, event_id

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
        """Check out next available AND condition register index."""
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
    event_node: ast.FunctionDef, namespace: dict[str, tp.Any],
) -> tuple[dict[str, tuple[int, int]], str, dict[str, GAME_TYPE]]:
    """Parse argument nodes of given event function node and return:
        - dictionary mapping argument names to `(write_offset, size)` tuples for creating `EventArgRepl` instances
        - event's argument format string, e.g. `"iIIBh"`
        - dictionary mapping argument names (where applicable) to `GameObject` subclasses
    """
    arg_names = []  # type: list[str]
    arg_types = ""
    arg_classes = {}  # type: dict[str, GAME_TYPE]

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

        if isinstance(arg_type_node, ast.BinOp):
            # `{GameObject} | int` type hints are accepted (but no others).
            if not isinstance(arg_type_node.op, ast.BitOr):
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type: {repr(arg_type_node)}. "
                    f"Valid type hints: {_EVENT_ARG_TYPE_MSG}"
                )
            if not isinstance(arg_type_node.left, ast.Name):
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type (left of |): {repr(arg_type_node.left)}. "
                    f"Valid type hints: {_EVENT_ARG_TYPE_MSG}"
                )
            if not isinstance(arg_type_node.right, ast.Name):
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type (right of |): {repr(arg_type_node.right)}. "
                    f"Valid type hints: {_EVENT_ARG_TYPE_MSG}"
                )
            left_name = arg_type_node.left.id
            right_name = arg_type_node.right.id
            if left_name == "int":
                arg_type_node = arg_type_node.right  # process class name below
            elif right_name == "int":
                arg_type_node = arg_type_node.left  # process class name below
            else:
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type. If '|' is used, one side must be `int` and the other must be "
                    f"a game type. Valid type hints: {_EVENT_ARG_TYPE_MSG}"
                )

        if isinstance(arg_type_node, ast.Constant) and isinstance(arg_type_node.value, str):
            if arg_type_node.value not in _EVS_TYPES:
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type string {repr(arg_type_node.value)}. "
                    f"Valid type hints: {_EVENT_ARG_TYPE_MSG}"
                )
            arg_type = arg_type_node.value

        elif isinstance(arg_type_node, ast.Name):
            try:
                arg_type = _PY_TYPES[arg_type_node.id]
            except KeyError:
                class_name = arg_type_node.id
                class_name = class_name.removesuffix("Typing")  # not decompiled but could be used
                try:
                    arg_class = namespace[class_name]
                except KeyError:
                    raise EVSSyntaxError(
                        event_node,
                        f"{repr(class_name)} is not a valid game type for argument hinting.",
                    )
                try:
                    fmt = arg_class.get_event_arg_fmt()
                except AttributeError:
                    raise EVSSyntaxError(
                        event_node,
                        f"{repr(class_name)} is not a valid game type for argument hinting.",
                    )
                else:
                    arg_classes[arg_name] = arg_class
                    arg_type = fmt
        else:
            raise EVSSyntaxError(
                event_node,
                f"Every event argument needs a type. Valid type hints: {_EVENT_ARG_TYPE_MSG}"
            )

        arg_types += arg_type

    arg_dict = {name: value for name, value in zip(arg_names, _define_args(arg_types))}

    return arg_dict, arg_types, arg_classes


def _import_module(node: ast.Import, ignore_names: list[str] = ()) -> dict[str, tp.Any]:
    module_dict = {}
    for alias in node.names:
        name = alias.name
        if name in ignore_names:
            continue
        try:
            module = importlib.import_module(alias.name)
            importlib.reload(module)
        except ImportError as e:
            raise EVSImportError(node, alias.name, str(e))
        as_name = alias.asname if alias.asname is not None else name
        try:
            module_dict[as_name] = getattr(module, name)
        except AttributeError as e:
            raise EVSImportError(node, name, str(e))
    del module
    return module_dict


def _import_from(
    node: ast.ImportFrom, script_directory: Path, ignore_names: list[str] = ()
) -> dict[str, tp.Any]:
    """Import names into given namespace dictionary."""
    if node.module in ignore_names:
        return {}
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
                "`script_directory` needed for relative import, but was not given to `EVSParser` or auto-detected.",
            )
        level = 0 if node.level == 0 else node.level - 1  # single dot (level 1) is the same as no dot (level 0)
        module_path = script_directory / ("../" * level + node.module.replace(".", "/") + ".py")
        if not module_path.is_file():
            raise EVSImportError(node, node.module, f"Cannot import missing module file: {module_path}")
        module = import_arbitrary_file(module_path)

    module_dict = {}
    for alias in node.names:
        name = alias.name
        if name in ignore_names:
            continue  # already imported
        if name == "*":
            if "__all__" in vars(module):
                all_names = vars(module)["__all__"]
            else:
                # Get all names that were defined in the module and don't begin with an underscore.
                module_name = node.module.split(".")[-1]  # `__module__` is name-only in certain contexts I think
                all_names = [
                    n
                    for n, attr in vars(module).items()
                    if not n.startswith("_") and (
                        not hasattr(attr, "__module__") or attr.__module__ in (node.module, module_name)
                    )
                ]
            for name_ in all_names:
                try:
                    module_dict[name_] = getattr(module, name_)
                except AttributeError as e:
                    _LOGGER.error(
                        f"EVS error: could not import {name_} from module {node.module} " f"(__all__ = {all_names})"
                    )
                    raise EVSImportFromError(node, node.module, name_, str(e))
        else:
            as_name = alias.asname if alias.asname is not None else name
            try:
                module_dict[as_name] = getattr(module, name)
            except AttributeError as e:
                raise EVSImportFromError(node, node.module, name, str(e))
    del module
    return module_dict


def _import_from_common_func(
    module_name: str, namespace: dict, script_directory: Path, names: list[str], level: int
):
    """Import names into given namespace dictionary."""
    try:
        # Try to import and reload module normally.
        module = importlib.import_module(module_name)
        importlib.reload(module)
    except ImportError:
        # Try to import module on path.
        if script_directory is None:
            raise EVSCommonFuncImportError(
                module_name,
                "",
                "`script_directory` needed for relative import, but was not given to `EVSParser` or be detected.",
            )
        module_path = script_directory / ("../" * level + module_name.replace(".", "/") + ".py")
        if not module_path.is_file():
            raise EVSCommonFuncImportError(module_name, "", "Cannot import missing module file.")
        module = import_arbitrary_file(module_path)

    for name in names:
        if name == "*":
            raise EVSCommonFuncImportError(module_name, "", "Cannot star import from COMMON_FUNC module.")
        try:
            namespace[name] = getattr(module, name)
        except AttributeError as ex:
            raise EVSCommonFuncImportError(module_name, name, str(ex))
    del module


def _header(event_id, on_rest_behavior=0):
    return [f"{event_id}, {on_rest_behavior}"]


def _define_args(arg_types: str) -> list[tuple[int, int]]:
    """Converts an argument format string (e.g. `"iIIfB"`) to a list of `(write_offset, size)` tuples, usually for
    generating `EventArgRepl` instances."""
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


class EVSCommonFuncImportError(EVSError):
    """Raised when a [COMMON_FUNC]-tagged import cannot be completed."""

    def __init__(self, module, name, msg):
        if name == "":
            super().__init__(0, f"Could not import COMMON_FUNC module {repr(module)}. Error: {msg}")
        else:
            super().__init__(0, f"Could not import {repr(name)} from COMMON_FUNC module {repr(module)}. Error: {msg}")


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
