from __future__ import annotations

__all__ = ["EVSParser", "EVSError"]

import abc
import ast
import copy
import logging
import re
import typing as tp
from functools import partial
from pathlib import Path

from soulstruct.base.game_types.basic_types import GameObjectInt, FlagRange, MapFlagSuffix
from soulstruct.games import Game, get_game
from ..emevd.utils import (
    EventArgumentData,
    format_event_layers,
)

from .compiler import EVSInstructionCompiler
from .conditions import EVSConditionManager, ConditionGroupState
from .exceptions import *
from .utils import *

_LOGGER = logging.getLogger("soulstruct")


class EVSParser(abc.ABC):

    # These names are handled fully internally by this parser and have PYI stub definitions only.
    SPECIAL_NAMES: set[str] = {"Await", "EnableThisFlag", "DisableThisFlag", "Condition", "HeldCondition"}

    # Class variables overridden by game-specific subclasses.
    EMEDF_ALIASES: dict[str, tp.Any] = None
    EMEDF_TESTS: dict[str, tp.Any] = None
    EMEDF_COMPARISON_TESTS: dict[str, tp.Any] = None
    EVENTS_MODULE = None  # type: tp.Any
    GAME_TYPES = None  # type: tp.Any
    OR_SLOTS = []  # type: list[int]
    AND_SLOTS = []  # type: list[int]
    COMPILER_CLASS: type[EVSInstructionCompiler]
    SUPPORTS_COMMON_FUNC: bool = False
    USES_COMMON_FUNC_SLOT: bool = False
    SPECIAL_EVENT_NAMES: dict[int, str] = None

    # Internal state.
    tree: ast.Module
    name: str
    map_base_flag: tp.Optional[int]
    script_directory: tp.Optional[Path]
    linked_offsets: list[int]
    strings_with_offsets: list[str]
    locals: dict[str, tp.Any]  # local event function namespace (constants only)
    globals: dict[str, tp.Any]  # global script namespace
    for_vars: dict[str, tp.Any]  # local to each event function
    events: dict[str, EventInfo]  # information about each event function (collected before proper statement parsing)
    event_ids: set[int]  # set of event IDs used, so duplicates can easily be spotted
    common_func_events: dict[str, EventInfo]  # imported or passed in from another EVS module
    common_func_event_ids: set[int]  # imported or passed in from another EVS module
    script_event_flags: dict[str, int]
    current_event: tp.Optional[EventInfo]
    event_function_strings: dict[str, str]  # maps function names (NOT IDs) to their numeric strings, in defined order
    cond_manager: EVSConditionManager | None
    debug_enabled: bool = False

    numeric_emevd: str

    def __init__(self, evs_source: str | Path, name=None, script_directory=None, common_func_evs: EVSParser = None):
        """Converts Python-like EVS code to numeric EMEVD (in `.numeric_emevd`), which can be fed to an `EMEVD` class.

        Args:
            evs_source: string or Path pointing to an EVS file, or direct string input (auto-detected based on
                any newlines being present in value).
            name: optional override for map name, which will otherwise be auto-detected from the EVS file name.
            script_directory: optional override for the directory from which to search for relative imports.
        """
        if isinstance(evs_source, Path) or "\n" not in evs_source:
            evs_path = Path(evs_source)
            with evs_path.open("r", encoding="utf-8") as script:
                evs_string = script.read()
            self.name = evs_path.name.split(".")[0] if name is None else name
            self.script_directory = Path(script_directory) if script_directory else evs_path.parent
        else:
            evs_string = evs_source  # raw EVS source given
            self.name = name
            self.script_directory = Path(script_directory) if script_directory else None

        if self.name is not None and (map_id_match := MAP_ID_RE.match(self.name)):
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
        # Event-specific namespaces:
        self.locals = {}
        self.for_vars = {}

        self.events = {}  # Maps your event names to their IDs, so you can call them to initialize them.
        self.event_ids = set()  # Used to ensure the same ID is not repeated.
        self.common_func_events = {}
        self.common_func_event_ids = set()

        self.script_event_flags = {}
        self.current_event = None
        self.event_function_strings = {}
        self.numeric_emevd = ""

        self._import_common_funcs(evs_string, common_func_evs)
        # Strip '# [COMMON_FUNC]' imports from the EVS string before it is parsed properly, as we don't want to
        # actually try to import those EVS scripts as real Python modules.
        evs_string = re.sub(COMMON_FUNC_IMPORT_RE, "\n", evs_string)
        self.tree = ast.parse(evs_string)

        self.cond_manager = EVSConditionManager(self.OR_SLOTS, self.AND_SLOTS)
        self.compiler = self.COMPILER_CLASS(self.cond_manager)

        self._compile_evs()

    def get_static_copy(self):
        pass

    @classmethod
    def get_game(cls) -> Game:
        if match := re.match(GAME_MODULE_RE, cls.__module__):
            return get_game(match.group(1))
        raise ValueError(f"Could not detect game name from module of class `{cls.__name__}`: {cls.__module__}")

    def _import_common_funcs(self, evs_string: str, common_func_evs: EVSParser | None):

        if common_func_evs:
            # "Pre-imported".
            self.common_func_events = common_func_evs.events.copy()  # shallow
            self.common_func_event_ids = common_func_evs.event_ids.copy()  # shallow

        cf_module_name = ""
        names = []

        for common_func_import_match in re.finditer(COMMON_FUNC_IMPORT_RE, evs_string):
            # TODO: Could theoretically support importing from multiple COMMON_FUNC modules (especially for DS1).
            cf_module_name, names_str = common_func_import_match.groups()
            level = len(cf_module_name) - len(cf_module_name.lstrip("."))  # number of dots at start of module name
            cf_module_name = cf_module_name.lstrip(".")
            if level == 1:
                level = 0  # single dot is the same as no dot (same directory)
            if common_func_evs:
                # noinspection PyUnresolvedReferences
                module_suffix = cf_module_name.split(".")[-1]
                if module_suffix == common_func_evs.name:
                    # Attached `common_func` is compatible with loaded one. Don't import it again.
                    continue
                raise self._EVSCommonFuncImportError(
                    cf_module_name, "", "Can currently only import/pass in one [COMMON_FUNC] module."
                )

            names_str = names_str.lstrip("(").rstrip(")")
            names = [name.strip("\n ") for name in names_str.split(",")]
            names = [name for name in names if name]  # remove empty strings (but not sure how these would occur)

            if names != ["*"] and "*" in names_str:
                raise self._EVSCommonFuncImportError(
                    cf_module_name, names, "Invalid imported names from COMMON_FUNC (contains asterisk)."
                )

            cf_module_path = self.script_directory / ("../" * level + cf_module_name.replace(".", "/") + ".py")
            if not cf_module_path.is_file():
                raise self._EVSCommonFuncImportError(
                    cf_module_name, "", f"Cannot import missing COMMON_FUNC file: {cf_module_path}"
                )

            if self.SUPPORTS_COMMON_FUNC:
                common_func_evs = self.__class__(
                    cf_module_path, script_directory=self.script_directory
                )
            else:
                # "Template" mode to assist early games like DS1 with common-func-like imports.
                common_func_evs = self.__class__(  # force this map's base flag
                    cf_module_path, name=self.name, script_directory=self.script_directory
                )

            self.common_func_events = common_func_evs.events.copy()  # shallow
            self.common_func_event_ids = common_func_evs.event_ids.copy()  # shallow

            # Otherise, star import preserves all names from common module.

        if not names:
            # Nothing to filter, either because we star-imported or didn't import at all.
            return

        for cf_name in names:
            if cf_name not in self.common_func_events:
                raise self._EVSCommonFuncImportError(
                    cf_module_name, cf_name, "Common func name not found in parsed EVS source file."
                )

        # Remove non-imported names from our copy of common events and IDs.
        for event_name in tuple(self.common_func_events):
            if event_name not in names:
                event_info = self.common_func_events.pop(event_name)
                self.common_func_event_ids.remove(event_info.id)

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
                raise self._EVSSyntaxError(
                    node,
                    f"No docstring given for event {event_name}, and no event ID was given in the decorator. See EVS "
                    f"documentation for more details."
                )
            description = ""
        else:
            try:
                doc_event_id, description = EVENT_DOCSTRING_RE.match(docstring).group(1, 2)
            except AttributeError:
                if event_id == -1:
                    raise self._EVSSyntaxError(
                        node,
                        f"Invalid docstring for event {event_name}. Note that the docstring must start with an event "
                        f"ID if one is not given in the decorator. See EVS documentation for more details."
                    )
                description = ""
            else:
                doc_event_id = int(doc_event_id)
                if event_id != -1 and event_id != doc_event_id:
                    raise self._EVSSyntaxError(node, f"Different event IDs were given in decorator and docstring.")
                event_id = doc_event_id

        if event_id in self.event_ids:
            raise self._EVSSyntaxError(node, f"Event ID {event_id} is defined multiple times in EVS script.")

        if event_id in self.SPECIAL_EVENT_NAMES:
            expected_name = self.SPECIAL_EVENT_NAMES[event_id]  # case-sensitive
            expected_default_name = f"Event{event_id}"
            if event_name not in {expected_name, expected_default_name}:
                raise self._EVSSyntaxError(
                    
                    node,
                    f"Event with ID {event_id} must be called '{expected_name}' or '{expected_default_name}'.",
                )
        elif event_name.lower() in {name.lower() for name in self.SPECIAL_EVENT_NAMES.values()}:  # case-insensitive
            raise self._EVSSyntaxError(
                
                node,
                f"Special event name '{event_name}' cannot be used for event ID {event_id}.",
            )

        description = "" if not description else description.lstrip(":")  # Remove leading colon.

        arg_dict, arg_types, arg_classes = parse_event_arguments(self.name, node, self.globals)

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
            raise self._EVSSyntaxError(event_node, f"Event name cannot match an instruction name ({name}).")
        if name in BUILTIN_NAMES or CONDITION_GROUP_RE.match(name):
            raise self._EVSSyntaxError(event_node, f"Event name cannot match a builtin EVS name ({name}).")
        if name in self.events:
            raise self._EVSSyntaxError(event_node, f"Event name '{name}' has already been defined in script.")
        # TODO: Check if event name is already in common_func (when supported).
        return name

    # ~~~~~~~~~~~~~~~~
    #  COMPILE METHODS: These produce numeric EMEVD lines (except for `_compile_evs()`).
    # ~~~~~~~~~~~~~~~~

    def _compile_evs(self) -> None:
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
            # Parse root-level module nodes.
            if isinstance(node, ast.Import):
                self.globals |= import_module(self.name, node, ignore_names=ignore_import_names)
            elif isinstance(node, ast.ImportFrom):
                self.globals |= import_from(self.name, node, self.script_directory, ignore_names=ignore_import_names)
            elif isinstance(node, ast.FunctionDef):
                self._scan_event(node)
            elif isinstance(node, ast.Assign):
                self._assign_name(node, is_local=False)
            elif isinstance(node, ast.ClassDef):
                continue  # Class definitions (e.g. enums) are collected from the real Python parser.
            elif isinstance(node, ast.AnnAssign):
                continue  # type hints are allowed and ignored
            else:
                raise self._EVSSyntaxError(
                    
                    node,
                    f"Invalid content: {node.__class__}. The only valid global EVS lines are "
                    f"from-imports, event script function definitions, and global name assignments.",
                )

        if self.common_func_events and not self.SUPPORTS_COMMON_FUNC:
            # Add "template" style common_func events in now, after local events.
            self.events |= self.common_func_events
            self.event_ids |= self.common_func_event_ids

        for event_name, event_function in self.events.items():
            self.current_event = self.events[event_name]
            self.for_vars = {}
            self.locals = {}
            self.cond_manager.reset(self.current_event.id)

            # 'Compile' EVS event into a list of numeric EMEVD lines.
            parsed_event = self._compile_event_function(event_function)

            self.event_function_strings[event_name] = "\n".join(parsed_event)

        self.numeric_emevd = "\n\n".join(self.event_function_strings.values())
        self.numeric_emevd += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_offsets)
        self.numeric_emevd += "\n\nstrings:\n" + "\n".join(self.strings_with_offsets)

    def _compile_event_function(self, event_info: EventInfo) -> list[str]:
        """Compile an event function into a list of numeric EMEVD lines.

        Writes numeric header, then iterates over all nodes in function body.
        """

        event_emevd = [f"{event_info.id}, {event_info.on_rest_behavior}"]

        if not event_info.nodes:
            # Empty event functions can cause problems. Add a dummy 'End()' instruction.
            event_emevd += self.compiler.compile("End")
            _LOGGER.warning(f"Event {event_info.name} has no instructions. Added dummy 'End()' instruction.")
            return event_emevd

        for node in event_info.nodes:
            node = as_event_statement_node(
                node,
                f"Invalid line: {ast.dump(node)}. Must be `Condition()` assignment, IF/ELSE block, or instruction.",
            )
            built_function = self._compile_event_body_node(node)
            if built_function is None:
                raise self._EVSSyntaxError(node, "Builder returned None for instruction.")
            event_emevd += built_function

        return event_emevd

    def _compile_event_body_node(self, node: EventStatementTyping) -> list[str]:
        """Recursive node compiler.

        Every line must be an instruction (from my set, not the base EMEVD set), an IF statement, or an assignment to a
        `Condition()` call.
        """

        # INSTRUCTION or GAME TYPE METHOD or CONDITION METHOD
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return self._compile_function_expression(node.value)

        # `await` BUILT-IN KEYWORD
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Await):
            cond_node = as_condition_node(
                node.value.value,
                "`await` expression must be a `Condition` or boolean expression.",
            )
            return self._compile_condition(cond_node, condition_group=self.cond_manager.MAIN)

        # FOR
        if isinstance(node, ast.For):
            return self._compile_for(node)

        # IF
        if isinstance(node, ast.If):
            return self._compile_if(node)

        # ASSIGN
        if isinstance(node, ast.Assign):
            if isinstance(node.value, ast.Call):
                if isinstance(node.value.func, ast.Name):
                    if node.value.func.id in {"Condition", "HeldCondition"}:
                        # This is a Condition/HeldCondition assignment.
                        return self._assign_condition(node, held=node.value.func.id == "HeldCondition")

            # Assign local variable.
            self._assign_name(node, is_local=True)
            return []  # no EMEVD

        # RETURN
        if isinstance(node, ast.Return):
            if node.value is None or (isinstance(node.value, ast.Name) and node.value.id == "END"):
                return self.compiler.compile("End")
            if isinstance(node.value, ast.Name) and node.value.id == "RESTART":
                return self.compiler.compile("Restart")
            raise self._EVSSyntaxError(
                node,
                f"Invalid return value '{node.value}'. It should be None (empty) to end the "
                f"event, or the constant RESTART to restart it.",
            )

        raise self._EVSSyntaxError(
            node,
            f"Invalid line: {ast.dump(node)}. Must be `Condition()` assignment, IF/ELSE block, or instruction.",
        )

    def _compile_event_call(self, node: ast.Call, is_common_func=False):
        """Shortcut for `RunEvent(...)` instruction."""
        name, args, kwargs = self._parse_function_call(node)
        event_info = self.common_func_events[name] if is_common_func else self.events[name]
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
                raise self._EVSValueError(
                    node,
                    "If using keyword arguments when running events by calling them directly, you "
                    "must either have a 'slot' keyword argument or have exactly one positional "
                    "argument (slot) before the keyword arguments.",
                )
            slot, args = args[0], args[1:]
        if not isinstance(slot, int):
            raise self._EVSValueError(
                node, "Slot ('slot' keyword or first positional argument) must be an integer."
            )

        if is_common_func and not self.USES_COMMON_FUNC_SLOT:
            if slot != 0:
                raise self._EVSSyntaxError(
                    
                    node,
                    f"This game does not support non-zero slot arguments for imported common events.",
                )
            slot = None

        if kwargs:
            args = []
            for arg_name in event_info.args:
                try:
                    args.append(kwargs.pop(arg_name))  # order event arguments correctly
                except KeyError:
                    raise self._EVSValueError(node, f"Missing keyword argument in event call: {arg_name}")
            if kwargs:
                raise self._EVSValueError(node, f"Invalid keyword arguments in event call: {kwargs}")
        else:
            if len(args) != len(event_info.args):
                print(name, args, kwargs)
                print(event_info.args)
                raise self._EVSValueError(
                    node,
                    f"Number of positional arguments in event call (excluding the slot), {len(args)}, does not match "
                    f"the event function signature:\n"
                    f"    {['slot'] + list(event_info.args.keys())}.",
                )

        event_id = event_info.id
        args = (0,) if not args else args
        arg_types = event_info.arg_types or None

        instr_name = "RunCommonEvent" if is_common_func else "RunEvent"
        # We can discard the returned evaluated condition groups set here.
        if slot is None:
            instruction = self.compiler.compile(instr_name, event_id, args=args, arg_types=arg_types)
        else:
            instruction = self.compiler.compile(instr_name, event_id, slot=slot, args=args, arg_types=arg_types)
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
            raise self._EVSSyntaxError(node, "If given, `event_layers` must be a list, tuple, or single integer.")
        return instruction_lines

    def _check_condition_group_add(self, node: ast.Call) -> ConditionGroupState | None:
        """Returns condition index if this is a condition group `.Add()` or `.Await()` call, or `None` otherwise."""
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "Add"
            and isinstance(node.func.value, ast.Name)
            and (match := CONDITION_GROUP_RE.match(node.func.value.id))
        ):
            if match.group(1) == "MAIN":
                _LOGGER.warning(f"MAIN condition used in an `Add()` call on line {node.lineno}. This is unusual.")
                return self.cond_manager.MAIN

            i = (-1 if match.group(2) == "OR" else 1) * int(match.group(3))
            return self.cond_manager[i]
        elif (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "Await"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "MAIN"
        ):
            return self.cond_manager.MAIN
        return None

    def _compile_function_expression(self, node: ast.Call) -> list[str]:

        # `{Condition}.Add()` or `MAIN.Await()`
        if (condition := self._check_condition_group_add(node)) is not None:
            if node.keywords or len(node.args) != 1:
                raise self._EVSSyntaxError(
                    node,
                    ".Add() or .Await() take exactly one positional argument (Condition or boolean expression)."
                )
            arg = as_condition_node(
                node.args[0],
                f".Add() or .Await() argument must be a Condition or boolean expression, not: {type(node.args[0])}.",
            )
            return self._compile_condition(arg, condition_group=condition)

        if isinstance(node.func, ast.Attribute):
            # Method of a game object or `.Add` method of a condition group.
            attr = node.func.attr
            game_object = self._parse_nodes(node.func.value)
            if not isinstance(game_object, GameObjectInt):
                raise self._EVSSyntaxError(
                    node, "Only methods of `GameObjectInt` subclasses can be called as instructions."
                )
            _, args, kwargs = self._parse_function_call(node)
            try:
                return getattr(game_object, attr)(*args, **kwargs)
            except AttributeError:
                raise self._EVSAttributeError(node, game_object.__name__, attr)
            except Exception as e:
                raise self._EVSValueError(node, f"Error occurred in GameObjectInt method call:\n    {str(e)}")

        if not isinstance(node.func, ast.Name):
            raise self._EVSSyntaxError(node, "Function must be a name.")
        name = node.func.id

        if name in {"enable_debug", "disable_debug"}:
            if node.keywords or node.args:
                raise self._EVSSyntaxError(node, f"`{name}()` takes no arguments.")
            self.debug_enabled = name == "enable_debug"
            EVSConditionManager.DEBUG_ENABLED = self.debug_enabled  # TODO: slightly hacky
            return []  # no EMEVD

        if name in self.events:
            # NOTE: "Template" style common_func events have already been added to local `self.events`.
            return self._compile_event_call(node)
        if self.common_func_events and self.SUPPORTS_COMMON_FUNC and name in self.common_func_events:
            return self._compile_event_call(node, is_common_func=True)

        if name == "Condition":
            raise self._EVSError(node, "You must assign the Condition() to a variable.")
        if name == "HeldCondition":
            raise self._EVSError(node, "You must assign the HeldCondition() to a variable.")

        if name == "Await":
            if node.keywords or len(node.args) != 1:
                raise self._EVSSyntaxError(
                    node,
                    "Await() takes exactly one positional argument (Condition or boolean expression)."
                )
            arg = as_condition_node(
                node.args[0],
                f"Await() argument must be a Condition or boolean expression, not: {type(node.args[0])}.",
            )
            return self._compile_condition(arg, condition_group=self.cond_manager.MAIN)

        if name in {"EnableThisFlag", "DisableThisFlag"}:
            if self.current_event.args:
                raise self._EVSSyntaxError(
                    node,
                    "Cannot use 'EnableThisFlag' or 'DisableThisFlag' shortcuts in an event that "
                    "takes arguments (the slot number cannot be determined from within).",
                )
            if name == "EnableThisFlag":
                return self._compile_instr(node, "EnableFlag", self.current_event.id)
            return self._compile_instr(node, "DisableFlag", self.current_event.id)

        # Assume function is a valid EMEDF or custom compiler instruction (error will obviously be raised if not).
        return self._compile_instruction(node)

    def _compile_for(self, node: ast.For) -> list[str]:
        try:
            for_iter = self._parse_nodes(node.iter, allowed_calls=("range", "zip"))
        except Exception as e:
            raise self._EVSSyntaxError(node, f"Invalid 'for' loop iterable. Error:\n    {str(e)}")
        for_emevd = []
        for_var = node.target
        if isinstance(for_var, ast.Name):
            if for_var.id in self.for_vars:
                raise self._EVSSyntaxError(
                    node, f"Variable {repr(for_var.id)} is already a 'for' loop variable in this scope."
                )
            if for_var in self.current_event.args:
                raise self._EVSSyntaxError(
                    node, f"Loop variable {repr(for_var.id)} is already the name of an event argument."
                )
            for iter_value in for_iter:
                self.for_vars[for_var.id] = iter_value
                for for_node in node.body:
                    for_node = as_event_statement_node(for_node, "Invalid statement type.")
                    for_emevd += self._compile_event_body_node(for_node)
                self.for_vars.pop(for_var.id)
        elif isinstance(for_var, ast.Tuple):
            for sub_var in for_var.elts:
                if not isinstance(sub_var, ast.Name):
                    # TODO: Implement arbitrary depth values.
                    raise self._EVSSyntaxError(node, "`for` loop variables cannot currently use nested tuples.")
                if sub_var.id in self.for_vars:
                    raise self._EVSSyntaxError(
                        node, f"Variable {repr(sub_var.id)} is already a 'for' loop variable in this scope."
                    )
                if sub_var in self.current_event.args:
                    raise self._EVSSyntaxError(
                        node, f"Loop variable {repr(sub_var.id)} is already the name of an event argument."
                    )
            for iter_value in for_iter:
                for i, sub_var in enumerate(for_var.elts):
                    assert isinstance(sub_var, ast.Name)  # checked above
                    self.for_vars[sub_var.id] = iter_value[i]
                for for_node in node.body:
                    for_node = as_event_statement_node(for_node, "Invalid statement type.")
                    for_emevd += self._compile_event_body_node(for_node)
                for sub_var in for_var.elts:
                    assert isinstance(sub_var, ast.Name)  # checked above
                    self.for_vars.pop(sub_var.id)

        return for_emevd

    def _compile_if(self, node: ast.If) -> list[str]:

        if_emevd = []

        # 0. Check if body is just one end/restart function.
        if len(node.body) == 1 and isinstance(node.body[0], ast.Return) and not node.orelse:
            return_node = node.body[0]
            assert isinstance(return_node, ast.Return)
            if return_node.value is None or (isinstance(return_node.value, ast.Name) and return_node.value.id == "END"):
                try:
                    try:
                        skip_return_node = as_skip_return_node(node.test)
                    except EVSSyntaxError:
                        raise NoSkipOrReturnError
                    return self._compile_skip_or_return(skip_return_node, end_event=True)
                except NoSkipOrReturnError:
                    # Continue to try building skip (though it will have to be a chain) or full condition.
                    pass
            elif isinstance(return_node.value, ast.Name) and return_node.value.id == "RESTART":
                try:
                    try:
                        skip_return_node = as_skip_return_node(node.test)
                    except EVSSyntaxError:
                        raise NoSkipOrReturnError
                    return self._compile_skip_or_return(skip_return_node, restart_event=True)
                except NoSkipOrReturnError:
                    # Continue to try building skip (though it will have to be a chain) or full condition.
                    pass
            else:
                raise self._EVSSyntaxError(
                    node,
                    f"Invalid return value '{return_node.value}'. It should be None (empty) to end the "
                    f"event, or the constant RESTART to restart it.",
                )

        # 1. Build the body of the IF statement.
        body_emevd = []
        for child_node in node.body:
            statement_node = as_event_statement_node(child_node, "Invalid statement node.")
            try:
                body_emevd += self._compile_event_body_node(statement_node)
            except TypeError as ex:
                raise self._EVSSyntaxError(node, f"Error in IF block:\n  {ast.dump(node)}\nError: {ex}")

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
            statement_node = as_event_statement_node(child_node, "Invalid statement node.")
            else_emevd += self._compile_event_body_node(statement_node)

        # 4. Put these components together. Note that an extra skip line is added if an ELSE body is present.
        if_emevd += test_emevd + body_emevd
        if else_emevd:
            skip_line_count = len([line for line in else_emevd if not line.startswith("    ^")])
            if_emevd += self._compile_instr(node, "SkipLines", skip_line_count)
            if_emevd += else_emevd

        return if_emevd

    def _compile_test(self, node, body_length, negate=False) -> list[str]:
        """Tries a simple skip, then a chain skip, then resorts to building a condition.

        Argument `node` should be the test node of the `ast.If` node.
        """
        test_emevd = []

        # 1. If the test starts with a 'not' operator, simply recur this method on the operand with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                return self._compile_test(node.operand, body_length, negate=not negate)
            raise self._EVSSyntaxError(node, "The 'not' keyword is the only valid unary operator.")

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
    ) -> list[str]:
        if sum((skip_lines > 0, end_event, restart_event)) != 1:
            raise self._EVSSyntaxError(
                
                node,
                "(internal) You can use 'skip_lines, 'end_event', or 'restart_event', but not multiples."
            )

        # 1. Resolve any opening 'not' operators by recurring this method with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                skip_return_node = as_skip_return_node(
                    node.operand, f"Invalid `not` expression type: {type(node.operand)}"
                )
                return self._compile_skip_or_return(
                    skip_return_node,
                    skip_lines=skip_lines,
                    end_event=end_event,
                    restart_event=restart_event,
                    negate=not negate,
                )
            raise self._EVSSyntaxError(node, "The `not` keyword is the only valid unary operator.")

        # 2. The condition is an event argument with a callable, testable game type.
        if isinstance(node, ast.Name) and node.id in self.current_event.args:
            if node.id in self.current_event.arg_classes:
                arg = self.current_event.args[node.id]
                arg_class = self.current_event.arg_classes[node.id]
                try:
                    return self.compiler.compile_game_object_test(
                        arg,  # may not be an instance of `arg_class` but will be testable as that type
                        arg_class,
                        negate=negate,
                        skip_lines=skip_lines,
                        end_event=end_event,
                        restart_event=restart_event,
                    )
                except TypeError:
                    raise self._EVSValueError(
                        
                        node,
                        f"Event argument type {repr(arg_class)} is not testable.",
                    )
            raise self._EVSValueError(
                
                node,
                f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                f"such as `Flag` (tests for enabled state), `Region` (tests if player is inside), etc.",
            )

        # 3a. The condition is a standard or previously-defined `Condition` wrapped with `LastResult()`.
        is_last_result = False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "LastResult":

            if node.keywords or len(node.args) != 1:
                raise self._EVSSyntaxError(
                    node,
                    "LastResult() takes exactly one positional argument: a Condition object or integer index."
                )

            # Try to evaluate contents as a condition below.
            node = node.args[0]
            is_last_result = True

        # 3. The node specifies a condition group. Integers are not permitted in this context (`if -3` is nonsense).
        if isinstance(node, ast.Name):
            # noinspection PyTypeChecker
            condition_group = self._get_condition_group_state(node, integer_permitted=False)
            if condition_group.index == 0:
                _LOGGER.warning(
                    f"MAIN condition used in a skip/return instruction on line {node.lineno}. This is unusual."
                )
            try:
                return self._compile_condition_skip_or_return(
                    node,
                    condition_group=condition_group,
                    is_last_result=is_last_result,
                    negate=negate,
                    skip_lines=skip_lines,
                    end_event=end_event,
                    restart_event=restart_event,
                )
            except ValueError:
                raise self._EVSError(
                    node,
                    "(internal) Cannot resolve simple condition check: 'skip_lines, 'end_event', and "
                    "'restart_event' are all 0 or False.",
                )
        elif is_last_result:
            raise self._EVSSyntaxError(
                node, "`LastResult()` must be called on a Condition object or built-in."
            )

        # 5. The condition is a 'compilable' game object in the global namespace that requires no arguments.
        if isinstance(node, (ast.Attribute, ast.Name)):
            game_object = self._parse_nodes(node)  # This will raise an EmevdNameError if the name is invalid.
            if not isinstance(game_object, GameObjectInt):
                raise self._EVSValueError(
                    node, f"Only (some) `GameObjectObject` subclasses are directly testable."
                )
            if isinstance(game_object, FlagRange):
                raise self._EVSValueError(
                    node,
                    "Cannot implicitly use a `FlagRange` as a condition.\n"
                    "Call `any()`, `all()`, `not any()`, or `not all()` on it to test it.",
                )
            try:
                return self.compiler.compile_game_object_test(
                    game_object,
                    negate=negate,
                    skip_lines=skip_lines,
                    end_event=end_event,
                    restart_event=restart_event,
                )
            except TypeError:
                raise self._EVSValueError(node, f"Object `{game_object}` is not testable.")

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
                    raise self._EVSSyntaxError(
                        node, f"{node.func.id} must have one argument (sequence or `FlagRange`)."
                    )
                arg = node.args[0]
                if not isinstance(arg, (ast.List, ast.Tuple)):
                    return self._compile_range_test(node, negate, skip_lines)
                if not chain and skip_lines > 0:
                    assert isinstance(arg, (ast.List, ast.Tuple))
                    return self._compile_chain_test(arg, node.func.id, negate=negate, skip_lines=skip_lines)

        # Failed to build simple/chain skip or return.
        raise NoSkipOrReturnError

    def _compile_simple_comparison(self, node: ast.Compare, negate, skip_lines) -> list[str]:
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

    def _compile_range_test(self, node: ast.Call, negate, skip_lines) -> list[str]:
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
                raise self._EVSSyntaxError(
                    
                    node,
                    "`range()` used inside `all()` or `any()` must have exactly two arguments: `(first, last)`.",
                )
            first, last = self._parse_nodes(arg.args)
            return self._compile_instr(node, "SkipLinesIfFlagRange" + tests[negate], skip_lines, (first, last))
        else:
            flag_range = self._parse_nodes(arg)
            if isinstance(flag_range, FlagRange):
                return self._compile_instr(node, "SkipLinesIfFlagRange" + tests[negate], skip_lines, flag_range)
            raise self._EVSSyntaxError(node, "The only valid non-sequence argument to 'all' is a FlagRange.")

    def _compile_chain_test(self, node: tp.Union[ast.Tuple, ast.List], func_name: str, negate, skip_lines) -> list[str]:
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
                try:
                    skip_return_node = as_skip_return_node(arg)
                except EVSSyntaxError:
                    raise NoSkipOrReturnError
                # Next line may also raise a `NoSkipOrReturnError` if a non-simple test is present.
                chain_skip_emevd += self._compile_skip_or_return(
                    skip_return_node, skip_lines=chain_skip_lines, negate=skip_negate, chain=True
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
        condition_group: ConditionGroupState = None,
        skip_lines=0,
    ) -> list[str]:
        """Called on the argument of Condition() or Await()/await, or on a non-simple Python `if` node that cannot be
        handled solely by skipping or returning.

        Always results in the use of a condition group, but if `skip_lines > 0` is given instead of `condition`, that
        group may just be temporary group that is immediately used in a line skip.
        """
        if condition_group is None and skip_lines == 0:
            raise ValueError("Either 'condition' index or 'skip_lines' count must be specified.")
        if condition_group is not None and skip_lines != 0:
            raise ValueError("Do not use 'condition' and 'skip_lines' at the same time.")
        if skip_lines < 0:
            raise ValueError("Cannot skip a negative number of lines.")

        if condition_group is not None and not isinstance(condition_group, ConditionGroupState):
            raise self._EVSError(
                
                node,
                "(internal) Invalid 'condition' argument. Must be a ConditionGroupState or None.",
            )

        emevd_args = []
        emevd_kwargs = {}

        # NOT (recurred)
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                cond_node = as_condition_node(node.operand, "Invalid condition expression.")
                return self._compile_condition(
                    cond_node, negate=not negate, condition_group=condition_group, skip_lines=skip_lines
                )
            raise self._EVSSyntaxError(node, "The 'not' keyword is the only valid unary operator.")

        # OR / AND
        if isinstance(node, ast.BoolOp):
            # This method will be called again within for each condition group that needs building/attaching.
            return self._compile_boolean_condition(
                node, negate=negate, output_condition_group=condition_group, skip_lines=skip_lines
            )

        # Compare
        if isinstance(node, ast.Compare):
            node, op_node, comparison_value = self._validate_comparison_node(node)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id not in self.EMEDF_COMPARISON_TESTS:
                    raise self._EVSSyntaxError(
                        node, f"Invalid test function for binary comparison: {node.func.id}"
                    )
                emevd_args += self._parse_nodes(node.args)
                emevd_kwargs.update(self._parse_keyword_nodes(node.keywords))
                emevd_kwargs.update(
                    comparison_type=(NEG_COMPARISON_NODES if negate else COMPARISON_NODES)[op_node],
                    value=comparison_value,
                )

                # Construct a transient node with the full comparison test name to be caught by the 'Test function'
                # section below (we have already provided the appropriate args/kwargs; no other node information used).
                node = copy.deepcopy(node.func)
                node.id = self.EMEDF_COMPARISON_TESTS[node.id]["test_name"]
            else:
                raise self._EVSSyntaxError(
                    node,
                    "Left value in a binary comparison must be a test function call, "
                    "such as `if Health(character) <= 0.1: ...`."
                )

        # Testable event argument
        if isinstance(node, ast.Name) and node.id in self.current_event.args:
            if node.id in self.current_event.arg_classes:
                arg = self.current_event.args[node.id]
                arg_class = self.current_event.arg_classes[node.id]
                try:
                    return self.compiler.compile_game_object_test(
                        arg,  # may not be an instance of `arg_class` but will be testable as that type
                        arg_class,
                        negate=negate,
                        condition_group=condition_group,
                        skip_lines=skip_lines,
                    )
                except TypeError:
                    raise self._EVSValueError(
                        node, f"Event argument type {repr(arg_class)} is not testable."
                    )
            raise self._EVSValueError(
                node,
                f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                f"such as `Flag` (tests for enabled state), `Region` (tests if player is inside), etc.",
            )

        # CONDITION GROUP (e.g. `AND_01` or a custom `Condition` instance). Naked integers are not permitted here.
        if isinstance(node, ast.Name):

            # noinspection PyTypeChecker
            input_condition_group = self._get_condition_group_state(node, integer_permitted=False)

            if input_condition_group:
                if condition_group is None:
                    raise self._EVSSyntaxError(
                        
                        node,
                        f"(internal) Tried to compile condition group '{node.id}' into `condition=None`.",
                    )
                if input_condition_group.stale and not (
                    condition_group.index == 0 and self.cond_manager.just_awaited_main
                ):
                    # NOTE: We don't issue this warning for back-to-back `MAIN.Await()` calls.

                    # TODO: Couple more edge cases to catch here, such as this sequence from m31_19_00_00 in ER:
                    #   OR_5.Add(OR_2)
                    #   MAIN.Await(OR_5)
                    #   AND_10.Add(OR_5)  <- AND_10 is NOT stale
                    #   MAIN.Await(AND_10)

                    _LOGGER.warning(
                        f"Line {node.lineno}: Condition group {node.id} is marked as stale, suggesting that it has not "
                        f"had any new conditions added to it this frame, but is still being used as an input condition."
                    )

                logic = "False" if negate else "True"
                return self._compile_instr(
                    node, f"IfCondition{logic}", condition_group.index, input_condition_group.index
                )

        # Call
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "LastResult":
                raise self._EVSSyntaxError(
                    node,
                    "As `LastResult(condition)` must use line skips or gotos, when using it in a boolean operation, "
                    "please use `any()` or `all()` in front of it to force the use of line skips rather than a full "
                    "Condition."
                )
            emevd_args += self._parse_nodes(node.args)
            emevd_kwargs.update(self._parse_keyword_nodes(node.keywords))
            node = node.func  # -> ast.Name (parsed below)

        # Test function
        if isinstance(node, ast.Name) and node.id in self.EMEDF_TESTS:
            try:
                return self._try_compile_test(
                    node,
                    *emevd_args,
                    negate=negate,
                    condition_group=condition_group,
                    skip_lines=skip_lines,
                    **emevd_kwargs,
                )
            except (NoSkipOrReturnError, NoNegateError):
                # No builtin tests for skipping, terminating, and/or negating condition. Need temp Condition.
                condition_emevd = []
                temp_condition = self.cond_manager.check_out_TEMP(self.name, node.lineno, self.current_event.id)
                skip_negate = False if skip_lines > 0 else negate  # avoids double negative with negated skip
                logic = str(bool(negate) if skip_lines > 0 else not bool(negate))
                # Compile temporary condition.
                condition_emevd += self._try_compile_test(
                    node, *emevd_args, negate=skip_negate, condition_group=temp_condition, **emevd_kwargs
                )
                instr = f"SkipLinesIfCondition{logic}"
                condition_emevd += self._compile_instr(node, instr, skip_lines, temp_condition)
                return condition_emevd
            except ValueError as ex:
                raise self._EVSError(node, f"Error occurred in test function '{node.id}': {ex}")

        # Constant / Event Argument
        if isinstance(node, (ast.Attribute, ast.Name)):
            game_object = self._parse_nodes(node)  # This will raise an `EmevdNameError` if the name is invalid.
            if not isinstance(game_object, GameObjectInt):
                raise self._EVSValueError(
                    node,
                    f"Only (some) `GameObjectInt` subclasses are directly testable, not {type(game_object).__name__}.",
                )
            elif isinstance(game_object, FlagRange):
                raise self._EVSValueError(
                    node,
                    "Cannot implicitly use a `FlagRange` as a condition.\n"
                    "Call any() or all() on it (with or without 'not' in front) to test it.",
                )
            try:
                return self.compiler.compile_game_object_test(
                    game_object,
                    negate=negate,
                    condition_group=condition_group,
                    skip_lines=skip_lines,
                )
            except TypeError:
                raise self._EVSValueError(node, f"Object {repr(game_object)} is not testable.")
            except (NoSkipOrReturnError, NoNegateError):
                # No builtin tests for terminating/negating condition. Need to construct a temporary one.
                condition_emevd = []
                temp_condition = self.cond_manager.check_out_TEMP(self.name, node.lineno, self.current_event.id)
                skip_negate = False if skip_lines > 0 else negate  # avoids double negative with negated skip
                logic = str(bool(negate) if skip_lines > 0 else not bool(negate))
                instr = f"SkipLinesIfCondition{logic}"
                condition_emevd += self._compile_condition(node, negate=skip_negate, condition_group=temp_condition)
                condition_emevd += self._compile_instr(node, instr, skip_lines, temp_condition)
                return condition_emevd

        # Failure to compile the condition will be raised as a genuine syntax error, unlike the skip/return compiler.
        # noinspection PyTypeChecker
        raise self._EVSSyntaxError(node, f"Invalid node for condition content:\n{ast.dump(node)}")

    def _compile_condition_skip_or_return(
        self,
        node,
        condition_group: ConditionGroupState,
        is_last_result=False,
        negate=False,
        skip_lines=0,
        end_event=False,
        restart_event=False,
    ) -> list[str]:

        if is_last_result and not condition_group.stale:
            _LOGGER.warning(
                f"{self.name} line {node.lineno}: LastResult() used on condition group {condition_group.index} (name "
                f"'{condition_group.name}') that is not marked as stale. It may not have been evaluated yet, or it may "
                f"have already been re-used with new tests."
            )

        eval_type = "LastConditionResult" if is_last_result else "Condition"

        if skip_lines > 0:
            if negate:
                return self._compile_instr(node, f"SkipLinesIf{eval_type}True", skip_lines, condition_group.index)
            return self._compile_instr(node, f"SkipLinesIf{eval_type}False", skip_lines, condition_group.index)
        elif end_event:
            if negate:
                return self._compile_instr(node, f"EndIf{eval_type}False", condition_group.index)
            return self._compile_instr(node, f"EndIf{eval_type}True", condition_group.index)
        elif restart_event:
            if negate:
                return self._compile_instr(node, f"RestartIf{eval_type}False", condition_group.index)
            return self._compile_instr(node, f"RestartIf{eval_type}True", condition_group.index)
        else:
            raise ValueError

    def _compile_boolean_condition(
        self, node: ast.BoolOp, negate: bool, output_condition_group: ConditionGroupState | None, skip_lines: int
    ) -> list[str]:
        """Compile an `or` or `and` expression used as a Condition/Await/test argument."""

        # We check out a new condition group for the output of this boolean operation, which will serve as either the
        # condition for a line skip (if `skip_lines` > 0) or to be loaded into `output_condition`.
        if isinstance(node.op, ast.Or):
            temp_condition = self.cond_manager.check_out_OR(self.name, node, self.current_event.id)
        elif isinstance(node.op, ast.And):
            temp_condition = self.cond_manager.check_out_AND(self.name, node, self.current_event.id)
        else:
            raise self._EVSSyntaxError(node, "Only valid boolean operations are OR / AND.")

        condition_emevd = []

        for v in node.values:
            # Call root condition compiler function again. Nested boolean operations may come back here.
            try:
                cond_node = as_condition_node(v)
            except EVSSyntaxError:
                continue  # continue below
            condition_emevd += self._compile_condition(cond_node, condition_group=temp_condition)

        if skip_lines > 0:
            logic = "True" if negate else "False"
            instr = f"SkipLinesIfCondition{logic}"
            condition_emevd += self._compile_instr(node, instr, skip_lines, temp_condition)
        else:
            logic = "False" if negate else "True"
            instr = f"IfCondition{logic}"
            condition_emevd += self._compile_instr(node, instr, output_condition_group, temp_condition)
            output_condition_group.children.add(temp_condition)
        return condition_emevd

    def _compile_instr(self, node, instr_name, *args, **kwargs) -> list[str]:
        """Try to `COMPILE` instruction, raising a syntax error if it fails.

        `COMPILE` function also takes our `ConditionGroupManager` and marks conditions as old or assigns children as
        appropriate to the instruction (based on EMEDF information).
        """
        try:
            return self.compiler.compile(instr_name, *args, **kwargs)
        except Exception as ex:
            args_string = ", ".join(str(x) for x in args)
            kwargs_string = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
            call_string = args_string + (", " if args_string and kwargs_string else "") + kwargs_string
            raise self._EVSSyntaxError(
                node,
                f"Failed to auto-compile instruction call {instr_name}({call_string}).\n"
                f"    Error: {ex}"
            )

    def _get_condition_group_state(self, node, integer_permitted=False) -> ConditionGroupState | None:
        """Resolve local `Condition` object, built-in name like `AND_01`, or (if permitted) a naked index into a
        managed, indexed `ConditionGroupState`.

        Returns `None` if the node cannot be interpreted as a condition group.
        """
        if integer_permitted and isinstance(node, ast.Constant) and isinstance(node.value, int):
            try:
                return self.cond_manager[node.value]
            except IndexError:
                raise self._EVSSyntaxError(node, f"Condition index {node.value} is out of range.")

        if isinstance(node, ast.Name) and node.id in self.cond_manager.names:
            try:
                return self.cond_manager[node.id]
            except IndexError:
                raise self._EVSSyntaxError(
                    
                    node,
                    f"Condition group {node.id} is not defined in this event function.",
                )

        if isinstance(node, ast.Name) and (match := CONDITION_GROUP_RE.match(node.id)):
            # Extract condition group index directly from name.
            if match.group(1) == "MAIN":
                i = 0
            else:
                i = (-1 if match.group(2) == "OR" else 1) * int(match.group(3))
            try:
                return self.cond_manager[i]
            except IndexError:
                raise self._EVSSyntaxError(
                    node,
                    f"Condition group {node.id} is not defined in this event function. "
                    f"Check that you have defined it with `Condition()` or `HeldCondition()`.",
                )

        return None

    def _try_compile_test(
        self,
        node: ast.Name,
        *args,
        condition_group: ConditionGroupState = None,
        skip_lines=0,
        negate=False,
        end_event=False,
        restart_event=False,
        **kwargs,
    ) -> list[str]:
        test_name = node.id
        tests = self.EMEDF_TESTS[test_name]
        event_layers = format_event_layers(kwargs.pop("event_layers", None))
        instruction_lines = []

        if skip_lines > 0:
            if condition_group is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if "skip_if" not in tests:
                raise NoSkipOrReturnError
            if negate:
                if "skip_if_not" in tests:
                    instr_name = tests["skip_if_not"]
                else:
                    raise self._EVSError(
                        
                        node,
                        f"Cannot support `not` keyword with SkipLines-based test function '{test_name}'.",
                    )
            else:
                instr_name = tests["skip_if"]
            # `line_count` is always the first positional argument.
            instruction_lines = self._compile_instr(node, instr_name, skip_lines, *args, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition_group is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if negate:
                if "if_not" in tests:
                    instr_name = tests["if_not"]
                else:
                    raise self._EVSError(
                        
                        node,
                        f"Cannot support `not` keyword with Condition-based test function '{test_name}'.",
                    )
            else:
                instr_name = tests["if"]

            # "if" is always present in tests. `condition` is always the first positional argument.
            instruction_lines = self._compile_instr(node, instr_name, condition_group.index, *args, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if "end_if" not in tests:
                raise NoSkipOrReturnError
            if negate:
                if "end_if_not" in tests:
                    instr_name = tests["end_if_not"]
                else:
                    raise self._EVSError(
                        node, f"Cannot support `not` keyword with End-based test function '{test_name}'."
                    )
            else:
                instr_name = tests["end_if"]
            instruction_lines = self._compile_instr(node, instr_name, *args, **kwargs)

        if restart_event:
            if "restart_if" not in tests:
                raise NoSkipOrReturnError
            if negate:
                if "restart_if_not" in tests:
                    instr_name = tests["restart_if_not"]
                else:
                    raise self._EVSError(
                        node,
                        f"Cannot yet support `not` keyword with Restart-based test function '{test_name}'.",
                    )
            else:
                instr_name = tests["restart_if"]
            instruction_lines = self._compile_instr(node, instr_name, *args, **kwargs)

        if instruction_lines:
            instruction_lines[0] += event_layers
            return instruction_lines

        raise ValueError("Must specify one condition outcome (condition, skip_lines, end_event, restart_event).")

    # ~~~~~~~~~~~~~~~~~~~~
    #  ASSIGNMENT METHODS: These create global/local objects, including Conditions, from assignment nodes.
    # ~~~~~~~~~~~~~~~~~~~~

    def _assign_name(self, node: ast.Assign, is_local: bool):
        """Assign object to name of your choosing.

        Can be used outside event functions (`is_local = False`) or inside them (`is_local = True`).
        """
        value = self._parse_nodes(node.value)
        for target in node.targets:
            if not isinstance(target, ast.Name):
                raise self._EVSSyntaxError(node, "Values can only be assigned to (any number of) single names.")
            name = target.id
            if name in self.EMEDF_ALIASES or name in self.SPECIAL_NAMES:
                raise self._EVSSyntaxError(node, f"Cannot assign to an instruction/reserved name ({name}).")
            if name in BUILTIN_NAMES:
                raise self._EVSSyntaxError(node, f"Cannot assign to a builtin EVS name ({name}).")
            if name in self.events:
                raise self._EVSSyntaxError(node, f"Cannot assign to an existing event name ({name}).")

            if is_local:
                if name in self.current_event.args:
                    raise self._EVSSyntaxError(node, f"Cannot re-assign to an event argument name ({name}).")
                if name in self.globals:
                    raise self._EVSSyntaxError(node, f"Cannot re-assign to a global name ({name}) in event function.")
                # NOTE: You can replace previously defined locals.
                self.locals[name] = value
            else:
                # NOTE: You can replace previously defined globals.
                self.globals[name] = value  # will override any previous value

    def _assign_condition(self, node: ast.Assign, held=False):
        if len(node.targets) != 1:
            raise self._EVSSyntaxError(node, "Can only assign a Condition to one name.")
        assert isinstance(node.value, ast.Call)
        if len(node.value.args) != 1 or len(node.value.keywords) > 1:
            raise self._EVSSyntaxError(
                node,
                "Condition should have one positional argument (and/or with any number of "
                "operands) and an optional keyword argument 'hold' that can be True or False "
                "(default).",
            )
        name_node = node.targets[0]
        assert isinstance(name_node, ast.Name)
        condition_name = name_node.id
        if condition_name == "_":
            raise self._EVSSyntaxError(node, "Condition name cannot be '_' (builtin symbol for temp condition).")
        condition_argument = node.value.args[0]
        hold = held
        if len(node.value.keywords) == 1:
            if held:
                raise self._EVSSyntaxError(node, "HeldCondition() does not allow any keyword arguments.")
            hold_keyword = node.value.keywords[0]
            if hold_keyword.arg != "hold":
                raise self._EVSSyntaxError(
                    node,
                    "The only keyword argument allowed in Condition() is 'hold', to prevent the "
                    "interpreter from re-using the underlying index after it has been used (so "
                    "you can call it again as a 'finished' condition).",
                )
            if not isinstance(hold_keyword.value, ast.Constant) or hold_keyword.value.value is None:
                raise self._EVSSyntaxError(
                    node, f"'hold' can be True or False (default), " f"not {node.value.keywords[0].value}."
                )
            elif hold_keyword.value.value == "True":
                hold = True

        if isinstance(condition_argument, ast.BoolOp):
            if isinstance(condition_argument.op, ast.Or):
                i = self.cond_manager.check_out_OR(
                    self.name, node, self.current_event.id, name=condition_name, hold=hold
                )
            else:
                assert isinstance(condition_argument.op, ast.And)
                i = self.cond_manager.check_out_AND(
                    self.name, node, self.current_event.id, name=condition_name, hold=hold
                )
        else:
            cond_node = as_condition_node(
                condition_argument, f"Invalid Condition argument type: {type(condition_argument)}"
            )
            i = self.cond_manager.check_out_AND(self.name, node, self.current_event.id, name=condition_name, hold=hold)
            return self._compile_condition(cond_node, condition_group=i)

        condition_emevd = []
        for v in condition_argument.values:
            v = as_condition_node(v)
            condition_emevd += self._compile_condition(v, condition_group=i)
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
                raise self._EVSSyntaxError(node, "Object attributes can only be read, not assigned to or deleted.")
            attribute_stack.append(current_node.attr)
            current_node = current_node.value  # generally Name or Call

        value = self._parse_nodes(current_node)
        while attribute_stack:
            attr = attribute_stack.pop()
            try:
                value = getattr(value, attr)
            except AttributeError:
                raise self._EVSAttributeError(node, value, attr)
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
                raise self._EVSSyntaxError(node, f"Cannot use reserved event argument {repr(name)}.")
            offset, size = self.current_event.args[name]
            arg_class = self.current_event.arg_classes.get(name, None)
            arg = EventArgumentData(offset, size, arg_class)
            if test and name in self.current_event.arg_classes:
                # TODO: Never used.
                # Bake arg into game type `__call__` method as 'self' (becomes a valid zero-argument test call).
                return partial(self.current_event.arg_classes[name].__call__, arg)
            return arg

        # Check if name is a condition group. We return just the index here; it will be used to retrieve the
        # appropriate `ConditionGroupState` as necessary.
        if match := CONDITION_GROUP_RE.match(name):
            if match.group(1) == "MAIN":
                return 0
            condition = (-1 if match.group(2) == "OR" else 1) * int(match.group(3))
            if condition not in self.AND_SLOTS and condition not in self.OR_SLOTS:
                raise self._EVSValueError(
                    node, f"Invalid condition group name for EMEVD: {name} (group index {condition})"
                )
            return condition

        # Look in 'for' loop variables, then locals, then globals.
        if name in self.for_vars:
            return self.for_vars[name]
        if name in self.locals:
            return self.locals[name]
        if name in self.globals:
            return self.globals[name]
        raise self._EVSNameError(node, name)

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
        raise self._EVSSyntaxError(node, f"Unsupported binary operation: {node.op}")

    def _parse_function_call(self, node: ast.Call, allowed_calls=()):
        """Return the name (or None), positional args, and keyword arguments of function call node.

        If the function is an Attribute node rather a Name, then the returned name will be None.
        """
        if isinstance(node.func, ast.Name):
            name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            name = None
        else:
            raise self._EVSSyntaxError(node, f"Invalid callable node type: {type(node)}")
        args = self._parse_nodes(node.args, allowed_calls=allowed_calls)
        kwargs = self._parse_keyword_nodes(node.keywords, allowed_calls=allowed_calls)
        return name, args, kwargs

    def _compile_game_type_method(self, node, name, args, kwargs) -> list[str]:
        """Parses and executes a game type method call, which are the only valid expressions other than instructions.

        TODO: Currently unused. Remove?
        """
        try:
            func = self.globals[name]
        except KeyError:
            raise self._EVSNameError(node, name)
        if not callable(func):
            raise self._EVSCallableError(node, name)
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
                raise self._EVSSyntaxError(
                    node,
                    f"`USub` node operand must be a number literal, not {type(node.operand)}."
                )
            return -node.operand.value
        elif isinstance(node, ast.Attribute):
            return self._parse_attributes(node)
        elif isinstance(node, ast.Name):
            if node.id in self.events:
                # Event function object can be used as an alias for its event ID in other instructions.
                return self.events[node.id].id
            return self._parse_name(node)
        elif isinstance(node, ast.BinOp):
            return self._parse_bin_op(node)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, (ast.List, ast.Tuple)):
            return [self._parse_nodes(sequence_node, allowed_calls=allowed_calls) for sequence_node in node.elts]
        elif isinstance(node, ast.Call):
            name, args, kwargs = self._parse_function_call(node, allowed_calls=allowed_calls)
            if name is not None and name in allowed_calls:
                return self._execute_function_call(name, args, kwargs, node.lineno)
            raise self._EVSValueError(node, f"Invalid callable: {repr(name)}.")
        raise self._EVSSyntaxError(
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
                raise self._EVSNameError(lineno, name)
        if not callable(func):
            raise self._EVSCallableError(lineno, name)
        return func(*args, **kwargs)

    def _parse_keyword_nodes(self, keywords, allowed_calls=()):
        """Returns a kwargs dictionary built from the given keyword node(s)."""
        if isinstance(keywords, ast.keyword):
            return {keywords.arg: self._parse_nodes(keywords.value, allowed_calls=allowed_calls)}
        return {kw.arg: self._parse_nodes(kw.value, allowed_calls=allowed_calls) for kw in keywords}

    def _parse_decorator(self, event_node: ast.FunctionDef) -> tuple[int, int]:
        """Extract `OnRestBehavior` enum value (default is 0) and event ID (default is -1) from function decorator."""
        decorators = event_node.decorator_list
        if not decorators:
            return RESTART_TYPES["ContinueOnRest"], -1

        if len(decorators) > 1:
            raise self._EVSSyntaxError(
                
                event_node,
                f"Event function cannot have more than one decorator (restart type).\n"
                f"Must be one of: {', '.join(RESTART_TYPES)}",
            )

        dec_node = decorators[0]
        if isinstance(dec_node, ast.Name):  # e.g. just `@ContinueOnRest`
            name = dec_node.id
            event_id = -1
        elif isinstance(dec_node, ast.Call):  # e.g. `@ContinueOnRest(11020000)`
            name, args, kwargs = self._parse_function_call(dec_node)
            if kwargs or len(args) != 1 or not isinstance(args[0], int):
                raise self._EVSSyntaxError(
                    
                    event_node,
                    f"Event function decorator must have exactly one numeric argument (event ID).",
                )
            event_id = args[0]
            if isinstance(event_id, MapFlagSuffix):
                if self.map_base_flag is None:
                    # noinspection PyTypeChecker
                    raise self._EVSSyntaxError(
                        
                        dec_node,
                        f"MapFlagSuffix `{event_id}` cannot be used when map base flag is unknown. (Pass `map_name` to "
                        f"the EVS parser explicitly if your EVS file name does not start with the usual 'mAA_BB_'.)",
                    )
                event_id += self.map_base_flag
        else:
            raise self._EVSSyntaxError(
                
                event_node,
                f"Event function decorator must be `@ContinueOnRest`, `@RestartOnRest`, or `@EndOnRest`, with the event"
                f" ID given as a decorator argument (e.g., `@RestartOnRest(11020100)`), not: {dec_node}.",
            )

        try:
            on_rest_behavior = RESTART_TYPES[name]
        except KeyError:
            raise self._EVSSyntaxError(
                
                event_node,
                f"Event function decorator name is not a valid event restart type: {dec_node.id}\n"
                f"Must be one of: {', '.join(RESTART_TYPES)}",
            )

        return on_rest_behavior, event_id

    def _validate_comparison_node(self, node):
        """ Comparisons must:
            (a) only involve two values;
            (b) have a non-numeric value on the left and a numeric value or attribute on the right.
        """
        if len(node.comparators) != 1:
            raise self._EVSSyntaxError(node, "Comparisons must be binary.")

        if isinstance(node.left, ast.Constant):
            raise self._EVSSyntaxError(
                node, "Comparisons must be between a name or function (left) and number (right)."
            )

        comparator = self._parse_nodes(node.comparators[0])
        if not isinstance(comparator, (int, float, EventArgumentData)):
            raise self._EVSSyntaxError(
                node,
                f"Comparisons must be between a name or function (left) and number or event argument (right), but "
                f"right value is {comparator}."
            )

        if node.ops[0].__class__ not in COMPARISON_NODES:
            raise self._EVSSyntaxError(
                node, f"Only valid comparisons operators are: ==, !=, >, <, >=, <= (not {node.ops[0]})"
            )

        return node.left, node.ops[0].__class__, comparator

    # EVS exception wrappers that pass in `self.name` automatically.

    def _EVSError(self, node, msg: str):
        return EVSError(self.name, node, msg)

    def _EVSSyntaxError(self, node, msg: str):
        return EVSSyntaxError(self.name, node, msg)

    def _EVSValueError(self, node, msg: str):
        return EVSValueError(self.name, node, msg)

    def _EVSImportError(self, node, module, msg: str):
        return EVSImportError(self.name, node, module, msg)

    def _EVSImportFromError(self, node, module, name, msg):
        return EVSImportFromError(self.name, node, module, name, msg)

    def _EVSCommonFuncImportError(self, module, name, msg: str):
        return EVSCommonFuncImportError(self.name, module, name, msg)

    def _EVSNameError(self, node, msg: str):
        return EVSNameError(self.name, node, msg)

    def _EVSAttributeError(self, node, name, attribute):
        return EVSAttributeError(self.name, node, name, attribute)

    def _EVSCallableError(self, node, name: str):
        return EVSCallableError(self.name, node, name)
