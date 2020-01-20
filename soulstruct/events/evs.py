import ast
import importlib
import logging
import re
import sys
from collections import OrderedDict
from functools import partial
from pathlib import Path

import soulstruct.game_types as gt
from soulstruct.events.numeric import SET_INSTRUCTION_ARG_TYPES
from soulstruct.events.internal import *

__all__ = ["EvsParser", "EmevdError"]
_LOGGER = logging.getLogger(__name__)

# TODO: Set up unit tests on vanilla scripts, and some examples that make use of high-level functionality.
# TODO: Support event function imports from '.common_func', including kwarg names.


class EvsParser(object):

    def __init__(self, evs_path_or_string, game_module=None, map_name=None, script_path=None):
        """Converts Python-like EVS code to numeric EMEVD (in `.numeric_emevd`), which can be fed to an `EMEVD` class.

        Args:
            evs_path_or_string: string or Path pointing to an EVS file, or direct string input (auto-detected based on
                any newlines being present in value).
            game_module: appropriate imported events game module (e.g. `soulstruct.events.darksouls1`).
            map_name: optional override for map name, which will otherwise be auto-detected from the EVS file name.
        """

        if script_path:
            sys.path.append(str(script_path))

        if not game_module:
            raise ValueError("No game specified. Try importing this class from the appropriate game events subpackage.")

        self.game_name = game_module.name
        SET_INSTRUCTION_ARG_TYPES(game_module.EMEVD.Event.Instruction.INSTRUCTION_ARG_TYPES)

        if isinstance(evs_path_or_string, Path) or '\n' not in evs_path_or_string:
            evs_path_or_string = Path(evs_path_or_string)
            with evs_path_or_string.open('r', encoding='utf-8') as script:
                self.tree = ast.parse(script.read())
            self.map_name = evs_path_or_string.name.split('.')[0] if map_name is None else map_name
        else:
            self.tree = ast.parse(evs_path_or_string)
            self.map_name = map_name

        self.linked_offsets = []
        self.strings_with_offsets = []
        self.event_layers = []

        # Global namespace with game-specific enums and constants. May be updated with user imports and definitions.
        self.globals = vars(game_module.enums)
        self.globals.update(vars(game_module.constants))
        # Note that there is no event-specific local namespace, except for this dictionary of 'for' loop variables:
        self.for_vars = {}

        self.instructions = {name: attr for name, attr in vars(game_module.instructions).items()
                             if not name.startswith('__')}
        self.tests = {name: attr for name, attr in vars(game_module.tests).items() if not name.startswith('_')
                      and (isinstance(attr, ConstantCondition) or getattr(attr, '__module__', '').endswith('tests'))}
        self.events = OrderedDict()  # Maps your event names to their IDs, so you can call them to initialize them.

        if self.game_name == 'darksouls1':
            self.conditions = [''] * 15  # Reset for every new event. Contains names of conditions.
        elif self.game_name in {'bloodborne', 'darksouls3'}:
            self.conditions = [''] * 31  # Reset for every new event. Contains names of conditions.
        else:
            raise ValueError(f"Invalid game name: {repr(self.game_name)}")
        self.held_conditions = []  # These conditions won't be re-allocated.
        self.finished_conditions = []  # These conditions need to be accessed with 'finished' instruction versions.

        self.script_event_flags = {}
        self.current_event = {}
        self.event_function_strings = []

        self.numeric_emevd = ''

        self._compile_evs()

    # ~~~~~~~~~~~~~~~~~~~
    #  FIRST PASS METHODS: These scan the event functions and collect information about each script.
    # ~~~~~~~~~~~~~~~~~~~

    def _scan_event(self, node: ast.FunctionDef):
        """Confirm syntax of event function and add it to self.events dictionary.

        An event should look like:

        @RestartOnRest
        def EventName(arg1: int, arg2: float):
            ''' [FlagName] 11020100: [Description] '''
            ...
        """
        event_name = self._validate_event_name(node)

        docstring = ast.get_docstring(node)
        if docstring is None:
            raise EmevdSyntaxError(node.lineno, f"No docstring given for event {event_name}. See EVS documentation.")
        try:
            flag_name, event_id, description = _EVENT_DOCSTRING_RE.match(docstring).group(1, 2, 3)
        except AttributeError:
            raise EmevdSyntaxError(node.lineno, f"Invalid docstring for event {event_name}. See EVS documentation.")

        event_id = int(event_id)
        if event_id == 0:
            if event_name.lower() not in {'event0', 'constructor'}:
                raise EmevdSyntaxError(node.lineno, "Event 0 must be called CONSTRUCTOR (or 'Event0').")
        elif event_id == 50:
            if event_name.lower() not in {'event50', 'preconstructor'}:
                raise EmevdSyntaxError(node.lineno, "Event 50 must be called PRECONSTRUCTOR (or 'Event50').")
        elif event_name.lower() in {'constructor', 'preconstructor'}:
            raise EmevdSyntaxError(
                node.lineno, "Builtin event names CONSTRUCTOR and PRECONSTRUCTOR are reserved for events 0 and 50.")

        flag_name = None if not flag_name else flag_name.rstrip()  # Remove trailing space.
        description = '' if not description else description.lstrip(':')  # Remove leading colon.

        arg_dict, arg_types, arg_classes = _parse_event_arguments(node)
        restart_type = _parse_decorator(node)

        if flag_name in self.globals:
            if self.globals[flag_name] != event_id:
                raise EmevdSyntaxError(node.lineno,
                                       f"Event flag name '{flag_name}' for event ID {event_id} clashes with the ID of "
                                       f"a constant with the same name.")
        elif flag_name:
            self.script_event_flags[flag_name] = int(event_id)  # Loaded into constants later under EVENTS enum.

        self.events[event_name] = {
            'name': event_name,
            'id': int(event_id),
            'args': arg_dict,  # OrderedDict
            'arg_types': arg_types,
            'arg_classes': arg_classes,
            'flag_name': flag_name,
            'restart_type': restart_type,
            'nodes': node.body[1:],  # Skips docstring.
            'description': description.lstrip(':')
        }

    def _validate_event_name(self, event_node: ast.FunctionDef):
        name = event_node.name
        if name in self.instructions or name in {'Await', 'EnableThisFlag', 'DisableThisFlag'}:
            raise EmevdSyntaxError(event_node.lineno, f"Event name cannot match an instruction name ({name}).")
        if name in _BUILTIN_NAMES:
            raise EmevdSyntaxError(event_node.lineno, f"Event name cannot match a builtin EVS name ({name}).")
        if name in self.events:
            raise EmevdSyntaxError(event_node.lineno, f"An event named {name} has already been defined in this script.")
        # TODO: Check if event name is already in common_func (when supported).
        return name

    # ~~~~~~~~~~~~~~~~
    #  COMPILE METHODS: These produce numeric EMEVD lines.
    # ~~~~~~~~~~~~~~~~

    def _compile_evs(self):
        """Top-level node traversal."""
        emevd_docstring = ast.get_docstring(self.tree)
        if emevd_docstring is not None:
            docstring_groups = re.split(r'\n{2,}', emevd_docstring)
            for group in docstring_groups:
                if group.startswith('linked:'):
                    for offset in group[8:].split('\n'):
                        if offset.strip():
                            self.linked_offsets += [int(offset.strip())]
                elif group.startswith('strings:'):
                    for offset_with_string in group[9:].split('\n'):
                        self.strings_with_offsets.append(offset_with_string)

        for node in self.tree.body[1:]:
            if isinstance(node, ast.Import):
                _import_module(node, self.globals)
            elif isinstance(node, ast.ImportFrom):
                _import_from(node, self.globals)
            elif isinstance(node, ast.FunctionDef):
                self._scan_event(node)
            elif isinstance(node, ast.Assign):
                self._assign_name(node)
            else:
                raise EmevdSyntaxError(
                    node.lineno, f"Invalid content: {node.__class__}. The only valid global EVS lines are "
                                 f"from-imports, event script function definitions, and global name assignments.")

        if self.script_event_flags:
            # noinspection PyTypeChecker
            self.globals['EVENTS'] = gt.Flag('EVENTS', self.script_event_flags)

        for event_name, event_function in self.events.items():
            self.current_event = self.events[event_name]
            self.for_vars = {}
            self.conditions = [''] * 15
            self.finished_conditions = []
            parsed_event = self._compile_event_function(event_function)  # numeric format
            self.event_function_strings.append('\n'.join(parsed_event))

        self.numeric_emevd = '\n\n'.join(self.event_function_strings)
        self.numeric_emevd += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_offsets)
        self.numeric_emevd += "\n\nstrings:\n" + "\n".join(self.strings_with_offsets)

    def _compile_event_function(self, event_function: dict):
        """ Writes header, then iterates over all nodes in function body. """

        event_emevd = _header(event_function['id'], event_function['restart_type'])

        for node in event_function['nodes']:
            built_function = self._compile_event_body_node(node)
            if built_function is None:
                raise EmevdSyntaxError(node.lineno, "Builder returned None for instruction.")
            event_emevd += built_function

        return event_emevd

    def _compile_event_body_node(self, node):
        """ Recursive node compiler. Every line must be an instruction (from my set, not the base EMEVD set), an IF
        statement, or an assignment to a Condition() call. """

        # INSTRUCTION or GAME TYPE METHOD
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return self._compile_function_expression(node.value)

        # AWAIT
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Await):
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
                condition_call_name = node.value.func.id
                if condition_call_name != 'Condition':
                    raise ValueError
            except (AttributeError, ValueError):
                raise EmevdSyntaxError(
                    node.lineno, "Cannot create local variables inside event script functions. Define them globally\n"
                                 "instead, or import them from other modules.")
            else:
                return self._assign_condition(node)

        # RETURN
        if isinstance(node, ast.Return):
            if node.value is None or (isinstance(node.value, ast.Name) and node.value.id == 'END'):
                return self.instructions['End']()
            elif isinstance(node.value, ast.Name) and node.value.id == 'RESTART':
                return self.instructions['Restart']()
            else:
                raise EmevdSyntaxError(node.lineno,
                                       f"Invalid return value '{node.value}'. It should be None (empty) to end the "
                                       f"event, or the constant RESTART to restart it.")

        raise EmevdSyntaxError(
            node.lineno, f"Invalid line: {ast.dump(node)}. Must be a Condition() assignment, IF/ELSE block, "
                         f"or instruction.")

    def _compile_event_call(self, node: ast.Call):
        """Shortcut for RunEvent(...) instruction."""
        name, args, kwargs = self._parse_function_call(node)
        event_dict = self.events[name]
        kwargs = self._parse_keyword_nodes(node.keywords)
        event_layer_string = _format_event_layers(kwargs.pop('event_layers', None))

        if not (args or kwargs) and not event_dict['args']:
            # Event can be called with no arguments (defaults to slot 0).
            instruction = self.instructions['RunEvent'](event_dict['id'])
            instruction[0] += event_layer_string
            return instruction

        slot = kwargs.pop('slot', None)
        if slot is None:
            if kwargs and len(args) != 1:
                raise EmevdValueError(
                    node.lineno, "If using keyword arguments when running events by calling them directly, you "
                                 "must either have a 'slot' keyword argument or have exactly one positional "
                                 "argument (slot) before the keyword arguments.")
            slot, args = args[0], args[1:]
        if not isinstance(slot, int):
            raise EmevdValueError(node.lineno, "Slot ('slot' keyword or first positional argument) must be an integer.")

        if kwargs:
            args = []
            for arg_name in event_dict['arg_dict']:
                try:
                    args.append(kwargs.pop(arg_name))  # order event arguments correctly
                except KeyError:
                    raise EmevdValueError(node.lineno, f"Missing keyword argument in event call: {arg_name}")
            if kwargs:
                raise EmevdValueError(node.lineno, f"Invalid keyword arguments in event call: {kwargs}")
        else:
            if len(args) != len(event_dict['args']):
                raise EmevdValueError(
                    node.lineno, f"Number of positional arguments in event call (excluding the slot) "
                                 f"does not match the event function signature:\n"
                                 f"    {['slot'] + list(event_dict['args'].keys())}.")

        event_id = event_dict['id']
        slot = 0 if slot is None else slot
        args = (0,) if not args else args
        arg_types = None if not event_dict['arg_types'] else event_dict['arg_types']

        instruction = self.instructions['RunEvent'](event_id, slot=slot, args=args, arg_types=arg_types)
        instruction[0] += event_layer_string
        return instruction

    def _compile_instruction(self, node: ast.Call):
        """Build instruction arguments and call the instruction (which will return a numeric line)."""
        name, args, kwargs = self._parse_function_call(node)
        try:
            instruction_lines = self.instructions[name](*args, **kwargs)  # includes event arg load lines
        except Exception as e:
            raise EmevdSyntaxError(node.lineno, f"Failed to compile instruction {name}.\n    Error: {str(e)}")
        try:
            instruction_lines[0] += _format_event_layers(kwargs.pop('event_layers', None))
        except TypeError:
            raise EmevdSyntaxError(node.lineno, f"'event_layers' must be a list, tuple, or single integer.")
        return instruction_lines

    def _compile_function_expression(self, node: ast.Call):

        if isinstance(node.func, ast.Attribute):
            # Method of a game object.
            attr = node.func.attr
            game_object = self._parse_nodes(node.func.value)
            if not isinstance(game_object, gt.GameObject):
                raise EmevdSyntaxError(
                    node.lineno, "Only methods of builtin GameObject types can be called as instructions.")
            _, args, kwargs = self._parse_function_call(node)
            try:
                return getattr(game_object, attr)(*args, **kwargs)
            except AttributeError:
                raise EmevdAttributeError(node.lineno, game_object.__name__, attr)
            except Exception as e:
                raise EmevdValueError(node.lineno, f"Error occurred in GameObject method call:\n    {str(e)}")

        name = node.func.id
        if name in self.events:
            return self._compile_event_call(node)

        if name == 'Condition':
            raise EmevdError(node.lineno, "You must assign the Condition() to a variable.")

        if name == 'Await':
            if node.keywords or len(node.args) != 1:
                raise EmevdSyntaxError(node.lineno, "Await() takes exactly one positional argument (condition).")
            return self._compile_condition(node.args[0], condition=0)

        if name in {'EnableThisFlag', 'DisableThisFlag'}:
            if self.events['args']:
                raise EmevdNameError(
                    node.lineno, "Cannot use 'EnableThisFlag' or 'DisableThisFlag' shortcuts in an event that "
                                 "takes arguments (the slot number cannot be determined from within).")
            if name == 'EnableThisFlag':
                return self.instructions['EnableFlag'](self.current_event['id'])
            return self.instructions['DisableFlag'](self.current_event['id'])

        if name in self.instructions:
            return self._compile_instruction(node)

        raise EmevdSyntaxError(
            node.lineno, f"Name {repr(name)} cannot be called in an expression. Only instructions and GameObject\n"
                         f"methods can be called outside of assignments and argument values.")

    def _compile_for(self, node: ast.For):
        try:
            for_iter = self._parse_nodes(node.iter, allowed_calls=['range', 'zip'])
        except Exception as e:
            raise EmevdSyntaxError(node.lineno, f"Invalid 'for' loop iterable. Error:\n    {str(e)}")
        for_emevd = []
        for_var = node.target
        if isinstance(for_var, ast.Name):
            if for_var in self.for_vars:
                raise EmevdSyntaxError(
                    node.lineno, f"Variable {repr(for_var.id)} is already a 'for' loop variable in this scope.")
            if for_var in self.current_event['args']:
                raise EmevdSyntaxError(
                    node.lineno, f"Loop variable {repr(for_var.id)} is already the name of an event argument.")
            for iter_value in for_iter:
                self.for_vars[for_var.id] = iter_value
                for for_node in node.body:
                    for_emevd += self._compile_event_body_node(for_node)
                self.for_vars.pop(for_var.id)
        elif isinstance(for_var, ast.Tuple):
            for sub_var in for_var.elts:
                if not isinstance(sub_var, ast.Name):
                    # TODO: Implement arbitrary depth values.
                    raise EmevdSyntaxError(node.lineno, "'for' loop variables cannot currently use nested tuples.")
                if sub_var in self.for_vars:
                    raise EmevdSyntaxError(
                        node.lineno, f"Variable {repr(sub_var.id)} is already a 'for' loop variable in this scope.")
                if sub_var in self.current_event['args']:
                    raise EmevdSyntaxError(
                        node.lineno, f"Loop variable {repr(sub_var.id)} is already the name of an event argument.")
            for iter_value in for_iter:
                for i, sub_var in enumerate(for_var.elts):
                    self.for_vars[sub_var.id] = iter_value[i]
                for for_node in node.body:
                    for_emevd += self._compile_event_body_node(for_node)
                for sub_var in for_var.elts:
                    self.for_vars.pop(sub_var.id)

        return for_emevd

    def _compile_if(self, node: ast.If):

        if_emevd = []

        # 0. Check if body is just one end/restart function.
        if len(node.body) == 1 and isinstance(node.body[0], ast.Return) and not node.orelse:
            return_node = node.body[0]
            if return_node.value is None or (isinstance(return_node.value, ast.Name) and return_node.value.id == 'END'):
                try:
                    return self._compile_skip_or_terminate(node.test, end_event=True)
                except NoSkipOrTerminateError:
                    # Continue to try building skip (though it will have to be a chain) or full condition.
                    pass
            elif isinstance(return_node.value, ast.Name) and return_node.value.id == 'RESTART':
                try:
                    return self._compile_skip_or_terminate(node.test, restart_event=True)
                except NoSkipOrTerminateError:
                    # Continue to try building skip (though it will have to be a chain) or full condition.
                    pass
            else:
                raise EmevdSyntaxError(node.lineno,
                                       f"Invalid return value '{node.value}'. It should be None (empty) to end the "
                                       f"event, or the constant RESTART to restart it.")

        # 1. Build the body of the IF statement.
        body_emevd = []
        for child_node in node.body:
            try:
                body_emevd += self._compile_event_body_node(child_node)
            except TypeError:
                raise EmevdSyntaxError(node.lineno, f"Error IF block:\n  {ast.dump(node)}")

        # 2. Build the test line. This could be a simple skip, a multi-line chain skip, or a fully-fledged Condition,
        #    depending on the test. Note that the body length has 1 added (an extra skip line) if there is an ELSE body
        #    in the statement, and does not include arg replacement lines.
        body_length = len([line for line in body_emevd if not line.startswith('    ^')]) + bool(node.orelse)
        test_emevd = self._compile_test(node.test, body_length=body_length)

        # 3. Build the ELSE body of the IF statement, if it exists.
        else_emevd = []
        for child_node in node.orelse:
            else_emevd += self._compile_event_body_node(child_node)

        # 4. Put these components together. Note that an extra skip line is added if an ELSE body is present.
        if_emevd += test_emevd + body_emevd
        if else_emevd:
            skip_line_count = len([line for line in else_emevd if not line.startswith('    ^')])
            if_emevd += self.instructions['SkipLines'](skip_line_count)
            if_emevd += else_emevd

        return if_emevd

    def _compile_test(self, node, body_length, negate=False):
        """ Tries a simple skip, then a chain skip, then resorts to building a condition. Argument 'node'
        should be the test node of the If node. """
        test_emevd = []

        # 1. If the test starts with a 'not' operator, simply recur this method on the operand with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                return self._compile_test(node.operand, body_length, negate=not negate)
            raise EmevdSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        try:
            # 2a. Try to build a simple or chain skip.
            test_emevd += self._compile_skip_or_terminate(node, skip_lines=body_length, negate=negate)
        except NoSkipOrTerminateError:
            # 2b. If the skip failed (returned None), we build a full condition.
            test_emevd += self._compile_condition(node, skip_lines=body_length, negate=negate)

        return test_emevd

    def _compile_skip_or_terminate(self, node, skip_lines=0, end_event=False, restart_event=False, negate=False,
                                   chain=False):

        if sum((skip_lines > 0, end_event, restart_event)) != 1:
            raise EmevdSyntaxError(
                node.lineno, "(internal) You can use 'skip_lines, 'end_event', or 'restart_event', but not multiples.")

        # 1. Resolve any opening 'not' operators by recurring this method with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                return self._compile_skip_or_terminate(node.operand, skip_lines=skip_lines, end_event=end_event,
                                                       restart_event=restart_event, negate=not negate)
            raise EmevdSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        # 2. The condition is an event argument with a callable, testable game type.
        if isinstance(node, ast.Name) and node.id in self.current_event['args']:
            if node.id in self.current_event['arg_classes']:
                arg = self.current_event['args'][node.id]
                arg_class = self.current_event['arg_classes'][node.id]
                test_func = partial(arg_class.__call__, arg)
                if not callable(test_func):
                    raise EmevdValueError(node.lineno, f"Event argument type {repr(arg_class)} is not testable.")
                return test_func(negate=negate, skip_lines=skip_lines, end_event=end_event, restart_event=restart_event)
            raise EmevdValueError(
                node.lineno, f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                             f"such as Flag (tests for enabled state), Region (tests if player is inside), etc.")

        # 3. The condition is a previously-defined Condition() instance.
        if isinstance(node, ast.Name) and node.id in self.conditions:
            i = self.conditions.index(node.id)
            try:
                return self._compile_condition_skip_or_terminate(i, negate, skip_lines, end_event, restart_event)
            except ValueError:
                raise EmevdError(
                    node.lineno, "(internal) Cannot resolve simple condition check: 'skip_lines, 'end_event', and "
                                 "'restart_event are all 0 or False.")

        # 4. The condition is a builtin test constant (e.g. THIS_FLAG, HOST, OFFLINE, SKULL_LANTERN_ACTIVE, ...)
        if isinstance(node, ast.Name) and node.id in self.tests:
            try:
                test = self.tests[node.id]
            except KeyError:  # No other permitted names.
                raise EmevdNameError(node.lineno, node.id)
            if isinstance(test, ConstantCondition):
                return test(negate=negate, skip_lines=skip_lines, end_event=end_event, restart_event=restart_event)
            if isinstance(test, gt.FlagRange):
                raise EmevdSyntaxError(node.lineno, "Cannot implicitly use a FlagRange as a condition. Call any() "
                                                    "or all() on it (with or without 'not' in front) to test it.")
            if isinstance(test, gt.Character):
                raise EmevdSyntaxError(node.lineno, "Cannot implicitly use a Character as a test. Call IsAlive(), "
                                                    "IsDead(), etc. on the Character to test its state.")
            raise NoSkipOrTerminateError

        # 5. The condition is a callable 'boolean' object in the global namespace that requires no arguments.
        if isinstance(node, (ast.Attribute, ast.Name)):
            test_func = self._parse_nodes(node)  # This will raise an EmevdNameError if the name is invalid.
            if isinstance(test_func, gt.FlagRange):
                raise EmevdValueError(
                    node.lineno, "Cannot implicitly use a FlagRange as a condition.\n"
                                 "Call any() or all() on it (with or without 'not' in front) to test it.")
            if not callable(test_func):
                raise EmevdValueError(node.lineno, f"Object {repr(test_func)} is not testable.")
            return test_func(negate=negate, skip_lines=skip_lines, end_event=end_event, restart_event=restart_event)

        # 6. The condition is a binary comparison operation.
        if isinstance(node, ast.Compare):
            return self._compile_simple_comparison(node, negate, skip_lines)

        # 7. The condition is a test function call.
        if isinstance(node, ast.Call) and node.func.id in self.tests:
            test_function = self.tests[node.func.id]
            # Get arguments.
            args = self._parse_nodes(node.args)
            kwargs = self._parse_keyword_nodes(node.keywords)
            return test_function(*args, skip_lines=skip_lines, negate=negate, end_event=end_event,
                                 restart_event=restart_event, **kwargs)  # This will raise the same error as below.

        # 8. The condition is any() or all() called on a FlagRange of a sequence of simple skips that can be chained.
        if isinstance(node, ast.Call):
            if node.func.id in ('any', 'all'):
                if len(node.args) != 1:
                    raise EmevdSyntaxError(node.lineno, f"{node.func.id} must have one argument (sequence/FlagRange).")
                if not isinstance(node.args[0], (ast.List, ast.Tuple)):
                    return self._compile_range_test(node, negate, skip_lines)
                if not chain and skip_lines > 0:
                    return self._compile_chain_test(node, negate=negate, skip_lines=skip_lines)

        # Failed to build simple/chain skip or terminate.
        raise NoSkipOrTerminateError

    def _compile_simple_comparison(self, node: ast.Compare, negate, skip_lines):
        left_node, op_node, comparison_value = _validate_comparison_node(node)
        if isinstance(left_node, ast.Name):
            name = left_node.id
            try:
                arg = self.current_event['args'][name]
            except KeyError:
                raise NoSkipOrTerminateError
            if negate:
                return self.instructions['SkipLinesIfComparison'](
                    skip_lines, NEG_COMPARISON_NODES[op_node], arg, comparison_value)
            return self.instructions['SkipLinesIfComparison'](
                skip_lines, COMPARISON_NODES[op_node], arg, comparison_value)
        raise NoSkipOrTerminateError

    def _compile_range_test(self, node: ast.Call, negate, skip_lines):
        tests = ['AllOff', 'AnyOn'] if node.func.id == 'all' else ['AllOn', 'AnyOff']
        # range()
        if isinstance(node.args[0], ast.Call) and node.args[0].func.id == 'range':
            if len(node.args[0].args) != 2:
                raise EmevdSyntaxError(
                    node.lineno, "'range' used inside all() or any() must have exactly two arguments (first, last).")
            first, last = self._parse_nodes(node.args[0].args)
            return self.instructions['SkipLinesIfFlagRange' + tests[negate]](skip_lines, (first, last))
        else:
            fr = self._parse_nodes(node.args[0])
            if isinstance(fr, gt.FlagRange):
                return self.instructions['SkipLinesIfFlagRange' + tests[negate]](skip_lines, fr)
            raise EmevdSyntaxError(node.lineno, "The only valid non-sequence argument to 'all' is a FlagRange.")

    def _compile_chain_test(self, node: ast.Call, negate, skip_lines):
        sequence = node.args[0].elts
        n_args = len(sequence)
        negate = not negate if node.func.id == 'any' else negate
        skip_negate = node.func.id == 'any'

        if skip_lines > 0:
            chain_skip_emevd = []
            for i, arg in enumerate(sequence):
                chain_skip_lines = n_args - i if negate else skip_lines + n_args - i - 1
                # Next line will raise a NoSkipOrTerminateError if a non-simple test is present.
                chain_skip_emevd += self._compile_skip_or_terminate(
                    arg, skip_lines=chain_skip_lines, negate=skip_negate, chain=True)
            if chain_skip_emevd:
                if negate:
                    chain_skip_emevd += self.instructions['SkipLines'](skip_lines)  # Extra skip required.
                return chain_skip_emevd

        raise NoSkipOrTerminateError

    def _compile_condition(self, node, negate=False, condition=None, skip_lines=0):
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
                return self._compile_condition(
                    node.operand, negate=not negate, condition=condition, skip_lines=skip_lines)
            raise EmevdSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        # OR / AND (recurred)
        if isinstance(node, ast.BoolOp):
            return self._compile_boolean_condition(node, negate=negate, condition=condition, skip_lines=skip_lines)

        # Compare
        if isinstance(node, ast.Compare):
            node, op_node, comparison_value = _validate_comparison_node(node)
            emevd_args += [op_node, comparison_value]

        # Testable event argument
        if isinstance(node, ast.Name) and node.id in self.current_event['args']:
            if node.id in self.current_event['arg_classes']:
                arg = self.current_event['args'][node.id]
                arg_class = self.current_event['arg_classes'][node.id]
                test_func = partial(arg_class.__call__, arg)
                if not callable(test_func):
                    raise EmevdValueError(node.lineno, f"Event argument type {repr(arg_class)} is not testable.")
                return test_func(negate=negate, condition=condition, skip_lines=skip_lines)
            raise EmevdValueError(
                node.lineno, f"Cannot use an event argument as a test condition unless it has a testable game type\n "
                             f"such as Flag (tests for enabled state), Region (tests if player is inside), etc.")

        # Existing condition
        if isinstance(node, ast.Name) and node.id in self.conditions:
            i = self.conditions.index(node.id)
            if i in self.finished_conditions:
                raise EmevdSyntaxError(node.lineno, f"Finished condition {node.id} cannot be an input condition.")
            self.finished_conditions.append(i)
            logic = 'False' if negate else 'True'
            return self.instructions[f'IfCondition{logic}'](condition, i)

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
                    *emevd_args, negate=negate, condition=condition, skip_lines=skip_lines, **emevd_kwargs)
            except (NoSkipOrTerminateError, NoNegateError):
                # No builtin tests for terminating/negating condition. Need to construct a temporary one.
                condition_emevd = []
                temp_condition = self._check_out_TEMP(node.lineno)
                skip_negate = False if skip_lines > 0 else negate  # avoids double negative with negated skip
                logic = ('True' if negate else 'False') if skip_lines > 0 else ('False' if negate else 'True')
                instr = f'SkipLinesIfCondition{logic}'
                condition_emevd += self._compile_condition(node_to_recur, negate=skip_negate, condition=temp_condition)
                condition_emevd += self.instructions[instr](skip_lines, temp_condition)
                return condition_emevd
            except ValueError:
                raise EmevdError(node.lineno, f"(internal) Error occurred in test function: {node.id}.")

        # Constant / Event Argument
        if isinstance(node, (ast.Attribute, ast.Name)):
            test_func = self._parse_nodes(node)  # This will raise an EmevdNameError if the name is invalid.
            if isinstance(test_func, gt.FlagRange):
                raise EmevdValueError(
                    node.lineno, "Cannot implicitly use a FlagRange as a condition.\n"
                                 "Call any() or all() on it (with or without 'not' in front) to test it.")
            if not callable(test_func):
                raise EmevdValueError(node.lineno, f"Object {repr(test_func)} is not testable.")
            return test_func(negate=negate, condition=condition, skip_lines=skip_lines)

        # Failure to compile the condition will be raised as a genuine syntax error, unlike the skip/terminate compiler.
        raise EmevdSyntaxError(node.lineno, f"Invalid node for condition content:\n{ast.dump(node)}")

    def _compile_condition_skip_or_terminate(self, condition, negate=False, skip_lines=0, end_event=False,
                                             restart_event=False):
        if skip_lines > 0:
            if negate:
                if condition in self.finished_conditions:
                    return self.instructions['SkipLinesIfFinishedConditionTrue'](skip_lines, condition)
                self.finished_conditions.append(condition)  # Condition is now finished.
                return self.instructions['SkipLinesIfConditionTrue'](skip_lines, condition)
            if condition in self.finished_conditions:
                return self.instructions['SkipLinesIfFinishedConditionFalse'](skip_lines, condition)
            self.finished_conditions.append(condition)  # Condition is now finished.
            return self.instructions['SkipLinesIfConditionFalse'](skip_lines, condition)
        elif end_event:
            if negate:
                if condition in self.finished_conditions:
                    return self.instructions['EndIfFinishedConditionFalse'](condition)
                self.finished_conditions.append(condition)  # Condition is now finished.
                return self.instructions['EndIfConditionFalse'](condition)
            if condition in self.finished_conditions:
                return self.instructions['EndIfFinishedConditionTrue'](condition)
            self.finished_conditions.append(condition)  # Condition is now finished.
            return self.instructions['EndIfConditionTrue'](condition)
        elif restart_event:
            if negate:
                if condition in self.finished_conditions:
                    return self.instructions['RestartIfFinishedConditionFalse'](condition)
                self.finished_conditions.append(condition)  # Condition is now finished.
                return self.instructions['RestartIfConditionFalse'](condition)
            if condition in self.finished_conditions:
                return self.instructions['RestartIfFinishedConditionTrue'](condition)
            self.finished_conditions.append(condition)  # Condition is now finished.
            return self.instructions['RestartIfConditionTrue'](condition)
        else:
            raise ValueError

    def _compile_boolean_condition(self, node: ast.BoolOp, negate, condition, skip_lines):
        if isinstance(node.op, ast.Or):
            i = self._check_out_OR(node.lineno)
        elif isinstance(node.op, ast.And):
            i = self._check_out_AND(node.lineno)
        else:
            raise EmevdSyntaxError(node.lineno, "Only valid boolean operations are OR / AND.")

        condition_emevd = []

        for v in node.values:
            condition_emevd += self._compile_condition(v, condition=i)

        finished = 'Finished' if i in self.finished_conditions else ''

        if skip_lines > 0:
            logic = 'True' if negate else 'False'
            instr = f'SkipLinesIf{finished}Condition{logic}'
            condition_emevd += self.instructions[instr](skip_lines, i)
        elif finished:
            raise EmevdValueError(node.lineno, "Cannot use a finished condition as an input to another condition.")
        else:
            logic = 'False' if negate else 'True'
            instr = f'IfCondition{logic}'
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
                raise EmevdSyntaxError(node.lineno, "Values can only be assigned to (any number of) single names.")
            name = target.id
            if name in self.instructions or name in {'Await', 'EnableThisFlag', 'DisableThisFlag'}:
                raise EmevdSyntaxError(node.lineno, f"Cannot assign to an instruction name ({name}).")
            if name in _BUILTIN_NAMES:
                raise EmevdSyntaxError(node.lineno, f"Cannot assign to a builtin EVS name ({name}).")
            if name in self.events:
                raise EmevdSyntaxError(node.lineno, f"Cannot assign to an existing event name ({name}).")
            else:
                self.globals[name] = value  # will override any previous value

    def _assign_condition(self, node: ast.Assign):
        if len(node.targets) != 1:
            raise EmevdSyntaxError(node.lineno, "Can only assign a Condition to one name.")
        if len(node.value.args) != 1 or len(node.value.keywords) > 1:
            raise EmevdSyntaxError(node.lineno,
                                   "Condition should have one positional argument (and/or with any number of "
                                   "operands) and an optional keyword argument 'hold' that can be True or False "
                                   "(default).")
        condition_name = node.targets[0].id
        if condition_name == '_':
            raise EmevdSyntaxError(node.lineno, "Condition name cannot be '_' (builtin symbol for temp condition).")
        condition_argument = node.value.args[0]
        hold = False
        if len(node.value.keywords) == 1:
            hold_keyword = node.value.keywords[0]
            if hold_keyword.arg != 'hold':
                raise EmevdSyntaxError(node.lineno,
                                       "The only keyword argument allowed in Condition() is 'hold', to prevent the "
                                       "interpreter from re-using the underlying index after it has been used (so "
                                       "you can call it again as a 'finished' condition).")
            if not isinstance(hold_keyword.value, ast.NameConstant) or hold_keyword.value.value is None:
                raise EmevdSyntaxError(node.lineno,
                                       f"'hold' can be True or False (default), "
                                       f"not {node.value.keywords[0].value}.")
            elif hold_keyword.value.value == 'True':
                hold = True

        if not isinstance(condition_argument, ast.BoolOp):
            i = self._check_out_AND(node.lineno, name=condition_name, hold=hold)
            return self._compile_condition(condition_argument, condition=i)

        if isinstance(condition_argument.op, ast.Or):
            i = self._check_out_OR(node.lineno, name=condition_name, hold=hold)
        elif isinstance(condition_argument.op, ast.And):
            i = self._check_out_AND(node.lineno, name=condition_name, hold=hold)
        else:
            raise EmevdSyntaxError(node.lineno, "Only valid boolean operations are OR and AND.")

        condition_emevd = []
        for v in condition_argument.values:
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
                raise EmevdSyntaxError(node.lineno, "Object attributes can only be read, not assigned to or deleted.")
            attribute_stack.append(current_node.attr)
            current_node = current_node.value  # generally Name or Call

        value = self._parse_nodes(current_node)
        while attribute_stack:
            attr = attribute_stack.pop()
            try:
                value = getattr(value, attr)
            except AttributeError:
                raise EmevdAttributeError(node.lineno, value, attr)
        return value

    def _parse_name(self, node: ast.Name, test=False):
        """Get named object from parser namespace.

        Looks in current event arguments first, then global namespace. Raises an EmevdNameError if name not found.
        """
        name = node.id
        if name in self.current_event['args']:
            arg = self.current_event['args'][name]
            if test and name in self.current_event['arg_classes']:
                # Bake arg into game type __call__ as 'self' (becomes a valid zero-argument test call).
                return partial(self.current_event['arg_classes'][name].__call__, arg)
            else:
                return arg

        # Look in tests first (boolean objects), then 'for' loop variables, then globals.
        if name in self.tests:
            return self.tests[name]
        if name in self.for_vars:
            return self.for_vars[name]
        if name in self.globals:
            return self.globals[name]
        raise EmevdNameError(node.lineno, name)

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
        raise EmevdSyntaxError(node.lineno, f"Unsupported binary operation: {node.op}")

    def _parse_function_call(self, node: ast.Call):
        """Return the name (or None), positional args, and keyword arguments of function call node.

        If the function is an Attribute node rather a Name, then the returned name will be None.
        """
        if isinstance(node.func, ast.Name):
            name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            name = None
        else:
            raise EmevdSyntaxError(node.lineno, f"Invalid callable node type: {type(node)}")
        args = self._parse_nodes(node.args)
        kwargs = self._parse_keyword_nodes(node.keywords)
        return name, args, kwargs

    def _compile_game_type_method(self, node, name, args, kwargs):
        """Parses and executes a game type method call, which are the only valid expressions other than instructions."""
        try:
            func = self.globals[name]
        except KeyError:
            raise EmevdNameError(node.lineno, name)
        if not callable(func):
            raise EmevdCallableError(node.lineno, name)
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
        node = nodes
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -node.operand.n
        elif isinstance(node, ast.Attribute):
            return self._parse_attributes(node)
        elif isinstance(node, ast.Name):
            return self._parse_name(node)
        elif isinstance(node, ast.BinOp):
            return self._parse_bin_op(node)
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.NameConstant):
            return node.value
        elif isinstance(node, (ast.List, ast.Tuple)):
            return [self._parse_nodes(sequence_node, allowed_calls=allowed_calls) for sequence_node in node.elts]
        elif isinstance(node, ast.Call):
            name, args, kwargs = self._parse_function_call(node)
            if name is not None and name in allowed_calls:
                return self._execute_function_call(name, args, kwargs, node.lineno)
            raise EmevdValueError(node.lineno, f"Invalid callable: {repr(name)}.")
        raise EmevdSyntaxError(
            node.lineno, f"Could not parse node of type {type(node)}. Node dump:\n    {ast.dump(node)}")

    def _execute_function_call(self, name, args, kwargs, lineno):
        try:
            func = self.globals[name]
        except KeyError:
            try:
                # noinspection PyUnresolvedReferences
                func = __builtins__[name]
            except KeyError:
                raise EmevdNameError(lineno, name)
        if not callable(func):
            raise EmevdCallableError(lineno, name)
        return func(*args, **kwargs)

    def _parse_keyword_nodes(self, keywords):
        """Returns a kwargs dictionary built from the given keyword node(s)."""
        if isinstance(keywords, ast.keyword):
            return {keywords.arg: self._parse_nodes(keywords.value)}
        return {kw.arg: self._parse_nodes(kw.value) for kw in keywords}

    # ~~~~~~~~~~~~~~~~~~
    #  CONDITION METHODS: These provide and manage conditions that are in use by the current event.
    # ~~~~~~~~~~~~~~~~~~

    def _check_out_OR(self, lineno, name='_', hold=False):
        """ Check out next available OR condition register index. """
        if name != '_' and name in self.conditions:
            raise ConditionNameError(lineno, f"A condition named '{name}' already exists in this event.")
        for i in _OR_SLOTS:
            if self.conditions[i] == '':
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        # Failed to find an empty condition, so get a non-held finished one. TODO: confirm this is safe in-game.
        for i in _OR_SLOTS:
            if i in self.finished_conditions and i not in self.held_conditions:
                self.finished_conditions.remove(i)
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        raise ConditionLimitError(lineno, "No available OR conditions left in this event.")

    def _check_out_AND(self, lineno, name='_', hold=False):
        """ Check out next available AND condition register index. """
        if name != '_' and name in self.conditions:
            raise ConditionNameError(lineno, f"A condition named '{name}' already exists in this event.")
        for i in _AND_SLOTS:
            if self.conditions[i] == '':
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        # Failed to find an empty condition, so get a non-held finished one. TODO: confirm this is safe in-game.
        for i in _AND_SLOTS:
            if i in self.finished_conditions and i not in self.held_conditions:
                self.finished_conditions.remove(i)
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        raise ConditionLimitError(lineno, "No available AND conditions left in this event.")

    def _check_out_TEMP(self, lineno):
        """ Check out highest-numbered condition of either OR type (preferred) or AND type for temporary use (e.g when
        a simple skip cannot be used in a one-line IF statement, like 'if HealthRatio(PLAYER) <= 0: ...').

        This serves no purpose other than a convention (started by FromSoft themselves) to distinguish temporary
        one-test conditions from meaningful conditions containing multiple tests.
        """
        try:
            highest_or = max([abs(c) for c in _OR_SLOTS if not self.conditions[c]])
        except ValueError:
            highest_or = 0
        try:
            highest_and = max([c for c in _AND_SLOTS if not self.conditions[c]])
        except ValueError:
            highest_and = 0

        if highest_or == highest_and == 0:
            raise ConditionLimitError(lineno, "No conditions available to check out a temporary condition.")

        if highest_or >= highest_and:
            self.conditions[-highest_or] = '_'
            return -highest_or
        else:
            self.conditions[highest_and] = '_'
            return highest_and


_AND_SLOTS = [1, 2, 3, 4, 5, 6, 7]
_OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7]
_RESTART_TYPES = {'NeverRestart': 0, 'RestartOnRest': 1, 'UnknownRestart': 2}
_EVENT_DOCSTRING_RE = re.compile(r'(\w+ )?([0-9]+)(:\s*.*)?')
_EVS_TYPES = ('B', 'b', 'H', 'h', 'I', 'i', 'f', 's')
_PY_TYPES = {'uchar': 'B', 'char': 'b', 'ushort': 'H', 'short': 'h', 'uint': 'I', 'int': 'i', 'float': 'f', 'str': 's'}
_BUILTIN_NAMES = {'Condition', 'EVENTS'}.union(_RESTART_TYPES)


def _parse_event_arguments(event_node: ast.FunctionDef):
    arg_names = []
    arg_types = ''
    arg_classes = {}

    if event_node.args.defaults:
        raise EmevdSyntaxError(event_node.lineno, "You cannot provide default values for event arguments.")
    if event_node.args.vararg or event_node.args.kwarg:
        raise EmevdSyntaxError(event_node.lineno, "You cannot use *args or **kwargs in event functions.")
    if event_node.args.kwonlyargs:
        raise EmevdSyntaxError(event_node.lineno, "You cannot have keyword-only arguments in event functions.")

    for arg_node in event_node.args.args:
        arg_name = arg_node.arg
        if arg_name in {'slot', 'event_layers'}:
            raise EmevdSyntaxError(event_node.lineno, f"Event argument cannot be named 'slot' or 'event_layers'.")
        arg_names.append(arg_name)

        arg_type_node = arg_node.annotation

        if isinstance(arg_type_node, ast.Str):
            if arg_type_node.s not in _EVS_TYPES:
                raise EmevdSyntaxError(
                    event_node.lineno, f"Invalid event argument type string {repr(arg_type_node)}. "
                                       f"Must be one of: {' '.join(_EVS_TYPES)}")
            arg_type = arg_type_node.s

        elif isinstance(arg_type_node, ast.Name):
            try:
                arg_type = _PY_TYPES[arg_type_node.id]
            except KeyError:
                class_name = arg_type_node.id
                if class_name in gt.GAME_TYPES:
                    arg_classes[arg_name] = getattr(gt, class_name)
                    arg_type = 'I'
                else:
                    raise EmevdSyntaxError(
                        event_node.lineno, f"{repr(class_name)} is not a valid game type for argument hinting.\n"
                                           f"The available types are: {gt.GAME_TYPES}")
        else:
            raise EmevdSyntaxError(
                event_node.lineno, f"Every event argument needs a type. You can specify any type with a type format\n"
                                   f"character in {repr(_EVS_TYPES)}, use a special game type like Flag or Character,\n"
                                   f"or use the Python built-in types int (which is signed), float, or (unlikely) str.")

        arg_types += arg_type

    arg_values = _define_args(arg_types)
    arg_dict = OrderedDict()
    for name, value in zip(arg_names, arg_values):
        arg_dict[name] = value

    return arg_dict, arg_types, arg_classes


def _parse_decorator(event_node: ast.FunctionDef):
    decorators = event_node.decorator_list
    if decorators:
        if len(decorators) > 1:
            raise EmevdSyntaxError(
                event_node.lineno, f"Event function cannot have more than one decorator (restart type).\n"
                                   f"Must be one of: {', '.join([d.id for d in decorators])}")
        try:
            return _RESTART_TYPES[decorators[0].id]
        except KeyError:
            raise EmevdSyntaxError(event_node.lineno, f"Invalid event function decorator: {decorators[0].id}\n"
                                                      f"Must be one of: {', '.join([d.id for d in decorators])}")
    return 0


def _validate_comparison_node(node):
    """ Comparisons must:
        (a) only involve two values;
        (b) have a non-numeric value on the left and a numeric value on the right.
    """
    if len(node.comparators) != 1:
        raise EmevdSyntaxError(node.lineno, "Comparisons must be binary.")

    if isinstance(node.left, ast.Num) or not isinstance(node.comparators[0], ast.Num):
        raise EmevdSyntaxError(node.lineno, "Comparisons must be between a name or function (left) "
                                            "and number (right).")

    if node.ops[0].__class__ not in COMPARISON_NODES:
        raise EmevdSyntaxError(node.lineno,
                               f"Only valid comparisons operators are: ==, !=, >, <, >=, <= (not {node.ops[0]})")

    return node.left, node.ops[0].__class__, node.comparators[0].n


def _format_event_layers(event_layers):
    if event_layers is None:
        return ''
    if isinstance(event_layers, int):
        event_layers = [event_layers]
    if not isinstance(event_layers, (list, tuple)):
        raise TypeError
    return f'<' + str(event_layers)[1:-1] + '>'


def _import_module(node: ast.Import, namespace: dict):
    for alias in node.names:
        name = alias.name
        if 'soulstruct.events' in name:
            return
        try:
            module = importlib.import_module(alias.name)
            importlib.reload(module)
        except ImportError as e:
            raise EmevdImportError(node.lineno, alias.name, str(e))
        as_name = alias.asname if alias.asname is not None else name
        try:
            namespace[as_name] = getattr(module, name)
        except AttributeError as e:
            raise EmevdImportFromError(node.lineno, node.module, name, str(e))


def _import_from(node: ast.ImportFrom, namespace: dict):
    """Import names into given namespace dictionary."""
    try:
        module = importlib.import_module(node.module)
        importlib.reload(module)
    except ImportError as e:
        raise EmevdImportError(node.lineno, node.module, str(e))
    for alias in node.names:
        name = alias.name
        if 'soulstruct.events' in name:
            return
        if name == '*':
            if "__all__" in vars(module):
                all_names = vars(module)["__all__"]
            else:
                # Get all names that were defined in the module and don't begin with an underscore.
                all_names = [n for n, attr in vars(module).items() if not n.startswith("_")
                             and (not hasattr(attr, '__module__') or attr.__module__ == node.module)]
            for name_ in all_names:
                try:
                    namespace[name_] = getattr(module, name_)
                except AttributeError as e:
                    _LOGGER.error(f"EVS error: could not import {name_} from module {node.module} "
                                  f"(__all__ = {all_names})")
                    raise EmevdImportFromError(node.lineno, node.module, name_, str(e))
        else:
            as_name = alias.asname if alias.asname is not None else name
            try:
                namespace[as_name] = getattr(module, name)
            except AttributeError as e:
                raise EmevdImportFromError(node.lineno, node.module, name, str(e))
    del module


def _header(event_id, restart_type=0):
    return [f"{event_id}, {restart_type}"]


def _define_args(arg_types):
    args = []
    for i, c in enumerate(arg_types):
        if c in 'Bb':
            c_size = 1
        elif c in 'Hh':
            c_size = 2
        elif c in 'Iif':
            c_size = 4
        else:
            raise ValueError(f"Invalid character {c} in arg_types.")
        args.append((get_write_offset(arg_types, i), c_size))
    return args


class EmevdError(Exception):
    def __init__(self, lineno, msg):
        self.lineno = lineno
        super().__init__(f"LINE {lineno}: {msg}")


class EmevdSyntaxError(EmevdError):
    pass


class EmevdValueError(EmevdError):
    pass


class EmevdImportError(EmevdError):
    """Raised when a module cannot be imported."""

    def __init__(self, lineno, module, msg):
        super().__init__(lineno, f"Could not import {repr(module)}. Error: {msg}")


class EmevdImportFromError(EmevdError):
    """Raised when a name cannot be imported from a module."""

    def __init__(self, lineno, module, name, msg):
        super().__init__(lineno, f"Could not import {repr(name)} from module {repr(module)}. Error: {msg}")


class EmevdNameError(EmevdError):
    """Raised when an invalid (undefined) name is parsed."""

    def __init__(self, lineno, name):
        super().__init__(lineno, f"Name {repr(name)} has not been imported or defined.")


class EmevdAttributeError(EmevdError):
    """Raised when an attribute of an object cannot be retrieved."""

    def __init__(self, lineno, name, attribute):
        super().__init__(lineno, f"Object {repr(name)} has no attribute {repr(attribute)}.")


class EmevdCallableError(EmevdError):
    """Raised when an un-callable object is called."""

    def __init__(self, lineno, name):
        super().__init__(lineno, f"Object {name} is not callable.")


class ConditionError(EmevdError):
    pass


class ConditionNameError(ConditionError):
    pass


class ConditionLimitError(ConditionError):
    pass
