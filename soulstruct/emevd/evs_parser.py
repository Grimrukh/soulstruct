import ast
from collections import OrderedDict
from functools import partial
import importlib
import os
import re
from soulstruct.emevd import game_types as gt
from soulstruct.emevd.core import header, define_args


_AND_SLOTS = [1, 2, 3, 4, 5, 6, 7]
_OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7]
_RESTART_TYPES = {'NeverRestart': 0, 'RestartOnRest': 1, 'UnknownRestart': 2}
_EVENT_DOCSTRING_RE = re.compile(r'(\w+ )?([0-9]+)(:\s*.*)?')
_EVS_ARG_TYPES = {'int': 'i', 'uint': 'I', 'float': 'f', 'short': 'h', 'ushort': 'H', 'char': 'b', 'uchar': 'B',
                  'str': 's'}


class EmevdError(Exception):
    def __init__(self, lineno, msg):
        super().__init__(f"LINE {lineno}: {msg}")


class EmevdSyntaxError(EmevdError):
    pass


class InvalidConstantError(EmevdError):
    """ Raised when a constant name can't be found. """
    def __init__(self, lineno, constant):
        super().__init__(lineno, f"No constant called '{constant}'.")


class InvalidConstantAttributeError(EmevdError):
    """ This error is fatal. """
    def __init__(self, lineno, constant, attr):
        super().__init__(lineno, f"Constant '{constant}' has no attribute '{attr}'.")


class ConditionError(Exception):
    pass


class ConditionNameError(ConditionError):
    pass


class ConditionLimitError(ConditionError):
    pass


class EmevdCompiler(object):
    """ Compiles Python-like EVS code to Dark Souls EMEVD scripts. """
    def __init__(self, evs_path, game_module=None):

        if not game_module:
            raise ValueError("No game specified. Try importing this class from the appropriate game emevd subpackage.")

        self.game_name = game_module.NAME

        with open(evs_path, encoding='utf-8') as script:
            self.tree = ast.parse(script.read())

        self.map_name = os.path.basename(evs_path).split('.')[0]
        self.linked_offsets = []
        self.strings_with_offsets = []
        self.event_layers = []

        # Game-specific constants. Will be updated to also include any user star-imported constants.
        self.constants = {name: attr for name, attr in vars(game_module.enums).items() if name != 'gt'}
        self.constants.update({name: attr for name, attr in vars(game_module.constants).items() if name != 'gt'})

        self.instructions = vars(game_module.instructions)
        self.tests = vars(game_module.tests)
        self.events = OrderedDict()  # Maps your event names to their IDs, so you can call them to initialize them.

        if self.game_name == 'ds1':
            self.conditions = [''] * 15  # Reset for every new event. Contains names of conditions.
        elif self.game_name in {'bb', 'ds3'}:
            self.conditions = [''] * 31
        else:
            raise ValueError(f"Invalid game name: {repr(self.game_name)}")
        self.held_conditions = []  # These conditions won't be re-allocated.
        self.finished_conditions = []  # These conditions need to be accessed with 'finished' instruction versions.

        self.script_event_flags = {}
        self.current_event_name = None
        self.event_function_strings = []

        self.numeric_emevd = ''

        self.build_script()

    def build_script(self):
        """ Top-level node traversal. Only acceptable nodes at this top level are ImportFrom (for importing your
        constants) and FunctionDef (for your event scripts). """

        docstring_groups = re.split(r'\n{2,}', ast.get_docstring(self.tree))
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
                raise EmevdSyntaxError(node.lineno,
                                       "All imports should be of the form 'from your_constants import *' (other than "
                                       "'from soulstruct.emevd.<game> import *').")
            elif isinstance(node, ast.ImportFrom):
                self.import_constants(node)

            elif isinstance(node, ast.FunctionDef):
                self.scan_event(node)

            else:
                raise EmevdSyntaxError(node.lineno,
                                       f"Invalid content: {node.__class__}. The only valid top-level EVS lines are "
                                       f"from-imports and even function definitions.")

        if self.script_event_flags:
            # noinspection PyTypeChecker
            self.constants['EVENTS'] = gt.Flag('EVENTS', self.script_event_flags)

        for event_name, event_function in self.events.items():
            self.current_event_name = event_name
            self.conditions = [''] * 15
            self.finished_conditions = []
            self.event_function_strings.append('\n'.join(self.build_event(event_function)))

        self.numeric_emevd = '\n\n'.join(self.event_function_strings)
        self.numeric_emevd += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_offsets)
        self.numeric_emevd += "\n\nstrings:\n" + "\n".join(self.strings_with_offsets)

    def import_constants(self, node: ast.ImportFrom):
        """ Import constants into 'constants' attribute. """
        if len(node.names) != 1 or node.names[0].name != '*':
            raise EmevdSyntaxError(node.lineno,
                                   "You must use star import for your constants, e.g. 'from your_constants import *'.")
        if node.module == 'emevd':
            # Skip this import, which is for intelli-sense only.
            return
        module = importlib.import_module(node.module)
        if "__all__" in vars(module):
            names = vars(module)["__all__"]
        else:
            # Get all names that were defined in the module (where possible) and don't begin with an underscore.
            names = [name for name, attr in vars(module).items() if not name.startswith("_")
                     and (not hasattr(attr, '__module__') or attr.__module__ == node.module)]
        self.constants.update({name: getattr(module, name) for name in names})

    def scan_event(self, node: ast.FunctionDef):
        """ Make sure that event function has the right design. It should look like:

        @RestartOnRest
        def EventName(arg1: int, arg2: float):
            ''' [FlagName] 11020100: [Description] '''
            ...
        """
        event_name = node.name

        docstring = ast.get_docstring(node)
        if docstring is None:
            raise EmevdSyntaxError(node.lineno, f"No docstring given for event {event_name}.")
        try:
            flag_name, event_id, description = _EVENT_DOCSTRING_RE.match(docstring).group(1, 2, 3)
        except AttributeError:
            raise EmevdSyntaxError(node.lineno, f"Invalid docstring for event {event_name}.")

        # TODO: Basic checks on event ID, like how it can't be zero, etc.
        flag_name = None if not flag_name else flag_name.rstrip()  # Remove trailing space.
        description = '' if not description else description.lstrip(':')  # Remove leading colon.

        arg_names = []
        arg_types = ''
        arg_classes = {}
        if any(v for k, v in vars(node.args).items() if k != 'args'):
            raise EmevdSyntaxError(node.lineno,
                                   "Event function should have positional arguments only with type annotations.")
        for arg in node.args.args:
            arg_type_node = arg.annotation
            if isinstance(arg_type_node, ast.Str):
                if arg_type_node.s not in 'BbHhIifs':
                    raise EmevdSyntaxError(node.lineno,
                                           f"Invalid event argument type '{arg_type_node.s}'. "
                                           f"Must be one of: B b H h I i f s")
                arg_type = arg_type_node.s
            elif isinstance(arg_type_node, ast.Name):
                try:
                    arg_type = _EVS_ARG_TYPES[arg_type_node.id]
                except KeyError:
                    if arg_type_node.id in gt.GAME_TYPES:
                        arg_classes[arg.arg] = getattr(gt, arg_type_node.id)
                        arg_type = 'I'
                    else:
                        raise EmevdSyntaxError(node.lineno, f"Invalid argument type: {arg_type_node.id}")
            else:
                raise EmevdSyntaxError(node.lineno, "Every event argument needs a type. It can be a format character "
                                                    "in 'BbHhIif, a Python int or float, or a Dark Souls type (e.g. "
                                                    "Flag, Character).")
            arg_names.append(arg.arg)
            arg_types += arg_type

        arg_values = define_args(arg_types)
        args = {name: value for name, value in zip(arg_names, arg_values)}

        if node.decorator_list:
            if len(node.decorator_list) > 1:
                raise EmevdSyntaxError(node.lineno,
                                       f"Event function can have up to one decorator: "
                                       f"{[d.id for d in node.decorator_list]}.")
            if node.decorator_list[0].id not in _RESTART_TYPES:
                raise EmevdSyntaxError(node.lineno, f"Invalid decorator: {[d.id for d in node.decorator_list]}.")
            restart_type = _RESTART_TYPES[node.decorator_list[0].id]
        else:
            restart_type = 0

        if flag_name in self.constants:
            if self.constants[flag_name] != event_id:
                raise EmevdSyntaxError(node.lineno,
                                       f"Event flag name '{flag_name}' for event ID {event_id} clashes with the ID of "
                                       f"a constant with the same name.")
        elif flag_name:
            self.script_event_flags[flag_name] = int(event_id)  # Loaded into constants later under EVENTS enum.

        self.events[event_name] = {
            'id': int(event_id),
            'args': args,
            'arg_types': arg_types,
            'arg_classes': arg_classes,
            'flag_name': flag_name,
            'restart_type': restart_type,
            'nodes': node.body[1:],  # Skips docstring.
            'description': description.lstrip(':')
        }

    def build_event(self, event_function: dict):
        """ Writes header, then iterates over all nodes in function body. """

        event_emevd = header(event_function['id'], event_function['restart_type'])

        for node in event_function['nodes']:
            built_function = self.build_event_body_node(node)
            if built_function is None:
                raise EmevdSyntaxError(node.lineno, "Builder returned None for instruction.")
            event_emevd += built_function

        return event_emevd

    def build_event_body_node(self, node):
        """ Recursive node compiler. Every line must be an instruction (from my set, not the base EMEVD set), an IF
        statement, or an assignment to a Condition() call. """

        # INSTRUCTION or RUN EVENT
        if is_function_expression(node):
            name = node.value.func.id
            arg_nodes = node.value.args
            keyword_nodes = node.value.keywords

            if name in self.events:
                # Run event (2000[00]).
                event_dict = self.events[name]
                args = [self._parse_function_arg(arg_node) for arg_node in arg_nodes]
                if keyword_nodes:
                    raise EmevdSyntaxError(node.lineno,
                                           "When running an event using its function name, use only positional "
                                           "arguments (because order matters). The first argument must be the slot "
                                           "number. (To run a common event in DS3, call RunCommonEvent() explicitly.)")
                if event_dict['args'] and len(args) != len(event_dict['args']) + 1:
                    raise EmevdSyntaxError(node.lineno,
                                           f"Number of arguments (excluding the first slot argument) does not match "
                                           f"the event function signature: "
                                           f"{['slot'] + list(event_dict['args'].keys())}.")
                if not event_dict['args'] and args:
                    raise EmevdSyntaxError(node.lineno, f"Event function '{name}' takes no arguments.")

                if args:
                    return self.instructions['RunEvent'](
                        event_dict['id'], args[0], args=args[1:], arg_types=event_dict['arg_types'])
                return self.instructions['RunEvent'](event_dict['id'])

            if name == 'Condition':
                raise EmevdError(node.lineno, "You must assign the Condition() to a variable.")

            if name == 'Await':
                if keyword_nodes or len(arg_nodes) != 1:
                    raise EmevdSyntaxError(node.lineno,
                                           "Await() should have exactly one argument (a condition). You can use "
                                           "boolean operations to build it inline.")
                return self.build_condition(arg_nodes[0], condition=0)

            if name in {'EnableThisFlag', 'DisableThisFlag'}:
                if self.events['args']:
                    raise InvalidConstantError(node.lineno,
                                               "Cannot use EnableThisFlag on an event that takes arguments, as the "
                                               "slot number cannot be inspected.")
                if name == 'EnableThisFlag':
                    return self.instructions['EnableFlag'](self.current_event_id)
                return self.instructions['DisableFlag'](self.current_event_id)

            if name in self.instructions:
                # We need to build args and kwargs properly now. Each argument or kwarg value could be a literal or a
                # name of a previously defined constant.
                args = [self._parse_function_arg(arg_node) for arg_node in arg_nodes]
                kwargs = {keyword.arg: self._parse_function_arg(keyword.value) for keyword in keyword_nodes}
                if 'event_layers' in kwargs:
                    event_layers = kwargs.pop('event_layers')
                    if not isinstance(event_layers, (list, tuple)):
                        print(event_layers)
                        raise EmevdSyntaxError(node.lineno, f"'event_layers' value must be a list or tuple, but "
                                                            f"received value {event_layers}")
                    formatted_event_layers = '<' + str(event_layers)[1:-1] + '>'
                else:
                    formatted_event_layers = ''
                try:
                    instruction_lines = self.instructions[name](*args, **kwargs)  # includes event arg load lines
                    instruction_lines[0] += formatted_event_layers
                    return instruction_lines
                except Exception as e:
                    raise EmevdSyntaxError(node.lineno, f"Failed to compile instruction.\n    Error: {str(e)}")

            raise EmevdSyntaxError(node.lineno, f"Invalid instruction: {name}")

        # AWAIT KEYWORD
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Await):
            return self.build_condition(node.value.value, condition=0)

        # IF
        if is_if(node):
            return self.build_if(node)

        # ASSIGN (CONDITION)
        if is_condition_assignment(node):
            if len(node.targets) != 1:
                raise EmevdSyntaxError(node.lineno, "Can only assign a Condition to one name.")
            if len(node.value.args) != 1 or len(node.value.keywords) > 1:
                raise EmevdSyntaxError(node.lineno,
                                       "Condition should have one positional argument (and/or with any number of "
                                       "operands) and an optional keyword argument 'hold' that can be True or False "
                                       "(default).")
            condition_name = node.targets[0].id
            if condition_name == '_':
                raise EmevdSyntaxError(node.lineno, "Condition name cannot be '_'.")
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
                i = self.check_out_AND(name=condition_name, hold=hold)
                return self.build_condition(condition_argument, condition=i)

            if isinstance(condition_argument.op, ast.Or):
                i = self.check_out_OR(name=condition_name, hold=hold)
            elif isinstance(condition_argument.op, ast.And):
                i = self.check_out_AND(name=condition_name, hold=hold)
            else:
                raise EmevdSyntaxError(node.lineno, "Only valid boolean operations are OR and AND.")

            condition_emevd = []

            for v in condition_argument.values:
                condition_emevd += self.build_condition(v, condition=i)

            return condition_emevd

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

    def build_if(self, node: ast.If):

        if_emevd = []

        # 0. Check if body is just one end/restart function.
        if len(node.body) == 1 and isinstance(node.body[0], ast.Return) and not node.orelse:
            return_node = node.body[0]
            if return_node.value is None or (isinstance(return_node.value, ast.Name) and return_node.value.id == 'END'):
                try:
                    return self.build_skip_or_terminate(node.test, end_event=True)
                except gt.NoSkipOrTerminateError:
                    # Continue to try building skip (though it will have to be a chain) or full condition.
                    pass
            elif isinstance(return_node.value, ast.Name) and return_node.value.id == 'RESTART':
                try:
                    return self.build_skip_or_terminate(node.test, restart_event=True)
                except gt.NoSkipOrTerminateError:
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
                body_emevd += self.build_event_body_node(child_node)
            except TypeError:
                raise EmevdSyntaxError(node.lineno, f"Error IF block:\n  {ast.dump(node)}")

        # 2. Build the test line. This could be a simple skip, a multi-line chain skip, or a fully-fledged Condition,
        #    depending on the test. Note that the body length has 1 added (an extra skip line) if there is an ELSE body
        #    in the statement, and does not include arg replacement lines.
        body_length = len([line for line in body_emevd if not line.startswith('    ^')]) + bool(node.orelse)
        test_emevd = self.build_test(node.test, body_length=body_length)

        # 3. Build the ELSE body of the IF statement, if it exists.
        else_emevd = []
        for child_node in node.orelse:
            else_emevd += self.build_event_body_node(child_node)

        # 4. Put these components together. Note that an extra skip line is added if an ELSE body is present.
        if_emevd += test_emevd + body_emevd
        if else_emevd:
            if_emevd += self.instructions['SkipLines'](len([line for line in else_emevd if not line.startswith('    ^')]))
            if_emevd += else_emevd

        return if_emevd

    def build_test(self, node, body_length, negate=False):
        """ Tries a simple skip, then a chain skip, then resorts to building a condition. Argument 'node'
        should be the test node of the If node. """

        test_emevd = []

        # 1. If the test starts with a 'not' operator, simply recur this method on the operand with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                return self.build_test(node.operand, body_length, negate=not negate)
            raise EmevdSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        try:
            # 2a. Try to build a simple or chain skip.
            test_emevd += self.build_skip_or_terminate(node, skip_lines=body_length, negate=negate)
        except gt.NoSkipOrTerminateError:
            # 2b. If the skip failed (returned None), we build a full condition.
            test_emevd += self.build_condition(node, skip_lines=body_length, negate=negate)

        return test_emevd

    def build_skip_or_terminate(self, node, skip_lines=0, end_event=False, restart_event=False, negate=False,
                                chain=False):

        if sum((skip_lines > 0, end_event, restart_event)) != 1:
            raise EmevdSyntaxError(node.lineno,
                                   "You can use skip_lines, end_event, or restart_event, but not multiples.")

        # 1. Resolve any opening 'not' operators by recurring this method with 'negate' inverted.
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                return self.build_skip_or_terminate(node.operand, skip_lines=skip_lines, end_event=end_event,
                                                    restart_event=restart_event, negate=not negate)
            raise EmevdSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        # 2a. The condition is a constant.
        if isinstance(node, (ast.Attribute, ast.Name)):

            # 2a(ii). Constant.
            try:
                constant_test_function = self._get_constant(node, test=True)
            except InvalidConstantError:
                pass
            else:
                return constant_test_function(negate=negate, skip_lines=skip_lines,
                                              end_event=end_event, restart_event=restart_event)

        if isinstance(node, ast.Name):

            name = node.id

            # 2a(i). Condition (previously created and assigned to a name).
            try:
                i = self.conditions.index(name)  # Check if name is in condition list.
            except ValueError:
                pass
            else:
                try:
                    return self._resolve_condition_skip_or_terminate(i, negate, skip_lines, end_event, restart_event)
                except ValueError:
                    raise EmevdError(node.lineno, "Cannot resolve simple condition check: skip_lines, end_event,\n"
                                                  "and restart_event are all 0 or False.")

            # 2a(ii). Constant.
            try:
                constant_test_function = self._get_constant(node, test=True)
            except InvalidConstantError:
                pass
            else:
                return constant_test_function(negate=negate, skip_lines=skip_lines,
                                              end_event=end_event, restart_event=restart_event)

            # 2a(iii). EMEVD Test with no additional arguments (e.g. THIS_FLAG, ONLINE, HOST, SKULL_LANTERN_ACTIVE, ...)
            try:
                test = self.tests[name]
            except KeyError:
                raise EmevdSyntaxError(node.lineno, f"Encountered unknown name: {name}")
            else:
                if isinstance(test, gt.ConstantCondition):
                    return test(negate=negate, skip_lines=skip_lines, end_event=end_event, restart_event=restart_event)
                if isinstance(test, (gt.Flag, gt.Object, gt.Map)):
                    test(negate=negate, skip_lines=skip_lines)
                if isinstance(test, gt.FlagRange):
                    raise EmevdSyntaxError(node.lineno, "Cannot implicitly use a FlagRange as a condition. Call any() "
                                                        "or all() on it (with or without 'not' in front) to test it.")
                if isinstance(test, gt.Character):
                    raise EmevdSyntaxError(node.lineno, "Cannot implicitly use a Character as a test. Call IsAlive(), "
                                                        "IsDead(), etc. on the Character to test its state.")

        # 2b. The condition is a binary comparison operation.
        if isinstance(node, ast.Compare):

            left_node, op_node, comparison_value = self._validate_comparison_node(node)

            if isinstance(left_node, ast.Name):
                name = left_node.id
                try:
                    arg = self.current_event_args[name]
                except KeyError:
                    raise gt.NoSkipOrTerminateError
                    # raise EmevdSyntaxError(node.lineno, f"Unrecognized event argument: {name}")

                if negate:
                    return self.instructions['SkipLinesIfComparison'](
                        skip_lines, gt.NEG_COMPARISON_NODES[op_node], arg, comparison_value)
                return self.instructions['SkipLinesIfComparison'](
                    skip_lines, gt.COMPARISON_NODES[op_node], arg, comparison_value)

        # 2c. The condition is a function expression (must be an EMEVD test that takes arguments, or any() or all()
        # called on a FlagRange or a sequence of simple skips that can be chained together).
        if isinstance(node, ast.Call):

            # 2c(i) The function is an EMEVD test that takes arguments.
            try:
                test_function = self.tests[node.func.id]
            except KeyError:
                pass
            else:
                # Get arguments.
                args = [self._parse_function_arg(arg_node) for arg_node in node.args]
                kwargs = {keyword.arg: self._parse_function_arg(keyword.value) for keyword in node.keywords}
                return test_function(*args, skip_lines=skip_lines, negate=negate, end_event=end_event,
                                     restart_event=restart_event, **kwargs)  # This will raise the same error as below.

            # 2c(i). The function is any()
            if node.func.id == 'any':
                # TODO: accept range(first, last) as well.
                if len(node.args) != 1:
                    raise EmevdSyntaxError(node.lineno, "'any' must have one argument (a sequence or FlagRange).")

                if not isinstance(node.args[0], (ast.List, ast.Tuple)):
                    fr = self._get_constant(node.args[0])
                    if isinstance(fr, gt.FlagRange):
                        if negate:
                            return self.instructions['SkipLinesIfFlagRangeAnyOn'](skip_lines, fr)
                        return self.instructions['SkipLinesIfFlagRangeAllOff'](skip_lines, fr)
                    raise EmevdSyntaxError(node.lineno, "The only valid non-sequence argument to 'any' is a FlagRange.")

                sequence = node.args[0].elts
                n_args = len(sequence)

                if skip_lines > 0 and not chain:
                    chain_skip_emevd = []
                    for i, arg in enumerate(sequence):
                        chain_skip_lines = n_args - i if not negate else skip_lines + n_args - i - 1
                        try:
                            skip_emevd = self.build_skip_or_terminate(
                                arg, skip_lines=chain_skip_lines, negate=True, chain=True)
                        except gt.NoSkipOrTerminateError:
                            # Non-simple test featured in chain. Proceed to build condition.
                            pass
                        else:
                            chain_skip_emevd += skip_emevd
                    if chain_skip_emevd:
                        if not negate:
                            chain_skip_emevd += self.instructions['SkipLines'](skip_lines)  # Extra skip required.
                        return chain_skip_emevd

            if node.func.id == 'all':
                # TODO: accept range(first, last) as well.
                if len(node.args) != 1:
                    raise EmevdSyntaxError(node.lineno, "'all' must have one argument (a sequence or FlagRange).")

                if not isinstance(node.args[0], (ast.List, ast.Tuple)):
                    fr = self._get_constant(node.args[0])
                    if isinstance(fr, gt.FlagRange):
                        if negate:
                            return self.instructions['SkipLinesIfFlagRangeAnyOff'](skip_lines, fr)
                        return self.instructions['SkipLinesIfFlagRangeAllOn'](skip_lines, fr)
                    raise EmevdSyntaxError(node.lineno, "The only valid non-sequence argument to 'all' is a FlagRange.")

                sequence = node.args[0].elts
                n_args = len(sequence)

                if skip_lines > 0 and not chain:
                    # Try building chain skip.
                    chain_skip_emevd = []
                    for i, arg in enumerate(sequence):
                        chain_skip_lines = n_args - i if negate else skip_lines + n_args - i - 1
                        try:
                            skip_emevd = self.build_skip_or_terminate(
                                arg, skip_lines=chain_skip_lines, negate=False, chain=True)
                        except gt.NoSkipOrTerminateError:
                            # Non-simple test featured in chain. Proceed to build condition.
                            pass
                        else:
                            chain_skip_emevd += skip_emevd
                    if chain_skip_emevd:
                        if negate:
                            chain_skip_emevd += self.instructions['SkipLines'](skip_lines)  # Extra skip required.
                        return chain_skip_emevd

        # Failed to build simple/chain skip or terminate.
        raise gt.NoSkipOrTerminateError

    def build_condition(self, node, negate=False, condition=None, skip_lines=0):
        """ Called on the argument of Condition() or Await(), and a non-simple IF test node. """
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
                return self.build_condition(
                    node.operand, negate=not negate, condition=condition, skip_lines=skip_lines)
            raise EmevdSyntaxError(node.lineno, "The 'not' keyword is the only valid unary operator.")

        # OR / AND (recurred)
        if isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.Or):
                i = self.check_out_OR()
            elif isinstance(node.op, ast.And):
                i = self.check_out_AND()
            else:
                raise EmevdSyntaxError(node.lineno, "Only valid boolean operations are OR and AND.")

            condition_emevd = []

            for v in node.values:
                condition_emevd += self.build_condition(v, condition=i)
            if skip_lines > 0:
                if negate:
                    if i in self.finished_conditions:
                        condition_emevd += self.instructions['SkipLinesIfFinishedConditionTrue'](skip_lines, i)
                    else:
                        condition_emevd += self.instructions['SkipLinesIfConditionTrue'](skip_lines, i)
                        self.finished_conditions.append(i)
                else:
                    if i in self.finished_conditions:
                        condition_emevd += self.instructions['SkipLinesIfFinishedConditionFalse'](skip_lines, i)
                    else:
                        condition_emevd += self.instructions['SkipLinesIfConditionFalse'](skip_lines, i)
                        self.finished_conditions.append(i)
            else:
                if negate:
                    if i in self.finished_conditions:
                        raise EmevdSyntaxError(node.lineno, "Cannot use a finished condition as an input to another "
                                                            "condition.")
                    else:
                        condition_emevd += self.instructions['IfConditionFalse'](condition, i)
                        self.finished_conditions.append(i)
                else:
                    if i in self.finished_conditions:
                        raise EmevdSyntaxError(node.lineno, "Cannot use a finished condition as an input to another "
                                                            "condition.")
                    else:
                        condition_emevd += self.instructions['IfConditionTrue'](condition, i)
                        self.finished_conditions.append(i)

            return condition_emevd

        # Compare
        if isinstance(node, ast.Compare):
            node, op_node, comparison_value = self._validate_comparison_node(node)
            emevd_args += [op_node, comparison_value]

        # Call
        if isinstance(node, ast.Call):
            emevd_args += [self._parse_function_arg(arg_node) for arg_node in node.args]
            emevd_kwargs.update({keyword.arg: self._parse_function_arg(keyword.value) for keyword in node.keywords})
            node = node.func

        # Constant / Event Argument
        if isinstance(node, (ast.Attribute, ast.Name)):
            try:
                constant_test_function = self._get_constant(node, test=True)
            except InvalidConstantError:
                pass
            else:
                # No front-end args or kwargs.
                try:
                    return constant_test_function(negate=negate, condition=condition, skip_lines=skip_lines)
                except TypeError:
                    raise EmevdSyntaxError(node.lineno,
                                           f"Invalid constant test function: {constant_test_function}. This\ngenerally "
                                           f"occurs when you try to use an argument in a condition without specifying "
                                           f"the argument's type properly (e.g. Flag).")

        # Name
        if isinstance(node, ast.Name):

            name = node.id

            # Existing condition
            try:
                i = self.conditions.index(name)
            except ValueError:
                pass
            else:
                if i in self.finished_conditions:
                    raise EmevdSyntaxError(node.lineno, "Finished conditions cannot be used in other conditions.")
                self.finished_conditions.append(i)
                if negate:
                    return self.instructions['IfConditionFalse'](condition, i)
                return self.instructions['IfConditionTrue'](condition, i)

            # Test function
            try:
                test_function = self.tests[name]
            except KeyError:
                [print(k, v) for k, v in self.tests.items()]
                raise EmevdSyntaxError(node.lineno, f"Unrecognized test function name: {name}")

            try:
                return test_function(
                    *emevd_args, negate=negate, condition=condition, skip_lines=skip_lines, **emevd_kwargs)
            except (gt.NoSkipOrTerminateError, gt.NoNegateError):
                condition_emevd = []
                temp_condition = self.check_out_AND()  # TODO: use check_out_temporary().
                if skip_lines > 0:
                    # Avoids double negative with negated skip.
                    condition_emevd += self.build_condition(node_to_recur, negate=False, condition=temp_condition)
                    if negate:
                        condition_emevd += self.instructions['SkipLinesIfConditionTrue'](skip_lines, temp_condition)
                    else:
                        condition_emevd += self.instructions['SkipLinesIfConditionFalse'](skip_lines, temp_condition)
                else:
                    condition_emevd += self.build_condition(node_to_recur, negate=negate, condition=temp_condition)
                    if negate:
                        condition_emevd += self.instructions['IfConditionFalse'](condition, temp_condition)
                    else:
                        condition_emevd += self.instructions['IfConditionTrue'](condition, temp_condition)

                return condition_emevd
            except ValueError:
                raise EmevdSyntaxError(node.lineno, f"Error occurred in instruction.")

        raise EmevdSyntaxError(node.lineno,
                               f"Invalid node for condition content:\n{ast.dump(node)}")

    def check_out_OR(self, name='_', hold=False):
        """ Check out next available OR condition register index. """
        if name != '_' and name in self.conditions:
            raise ConditionNameError(f"A condition named '{name}' already exists in this event.")
        for i in _OR_SLOTS:
            if self.conditions[i] == '':
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        # Failed to find an empty condition, so get a finished one.
        # TODO: Need to actually confirm this is fine to do (i.e. conditions can be re-used).
        for i in _OR_SLOTS:
            if i in self.finished_conditions and i not in self.held_conditions:
                self.finished_conditions.remove(i)
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        raise ConditionLimitError("No available OR conditions left in this event.")

    def check_out_AND(self, name='_', hold=False):
        """ Check out next available AND condition register index. """
        if name != '_' and name in self.conditions:
            raise ConditionNameError(f"A condition named '{name}' already exists in this event.")
        for i in _AND_SLOTS:
            if self.conditions[i] == '':
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        # Failed to find an empty condition, so get a finished one.
        # TODO: Need to actually confirm this is fine to do.
        for i in _AND_SLOTS:
            if i in self.finished_conditions and i not in self.held_conditions:
                self.finished_conditions.remove(i)
                self.conditions[i] = name
                if hold:
                    self.held_conditions.append(i)
                return i

        raise ConditionLimitError("No available AND conditions left in this event.")

    def check_out_temporary(self):
        """ Check out highest-numbered condition of either AND type (preferred) or OR type for temporary use (e.g when
        a simple skip cannot be used in a one-line IF statement, like 'if HealthRatio(PLAYER) <= 0: ...').

        Call `clear_temporary_conditions()` when the skip is complete to free these up again.
        """
        # TODO
        return self.check_out_AND()

    def clear_temporary_conditions(self):
        # TODO
        pass

    @property
    def current_event_id(self):
        return self.events[self.current_event_name]['id']

    @property
    def current_event_args(self):
        return self.events[self.current_event_name]['args']

    @property
    def current_event_arg_classes(self):
        return self.events[self.current_event_name]['arg_classes']

    def _get_constant(self, node, test=False):
        if isinstance(node, ast.Attribute):
            try:
                return getattr(self.constants[node.value.id], node.attr)
            except AttributeError:
                raise InvalidConstantAttributeError(node.lineno, node.value.id, node.attr)
            except KeyError:
                raise InvalidConstantError(node.lineno, node.value.id)
        elif isinstance(node, ast.Name):
            try:
                arg = self.current_event_args[node.id]
            except KeyError:
                pass
            else:
                if test and node.id in self.current_event_arg_classes:
                    return partial(self.current_event_arg_classes[node.id].__call__, arg)
                else:
                    return arg
            try:
                return self.constants[node.id]
            except KeyError:
                raise InvalidConstantError(node.lineno, node.id)
        raise EmevdError(node.lineno, "Constant can only be evaluated from a Name or Attribute node.")

    def _resolve_condition_skip_or_terminate(self, condition, negate=False, skip_lines=0,
                                             end_event=False, restart_event=False):
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

    @staticmethod
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

        if node.ops[0].__class__ not in gt.COMPARISON_NODES:
            raise EmevdSyntaxError(node.lineno,
                                   f"Only valid comparisons operators are: ==, !=, >, <, >=, <= (not {node.ops[0]})")

        return node.left, node.ops[0].__class__, node.comparators[0].n

    def _parse_function_arg(self, node):
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -node.operand.n
        if isinstance(node, (ast.Attribute, ast.Name)):
            return self._get_constant(node)
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.NameConstant):
            return node.value
        elif isinstance(node, (ast.List, ast.Tuple)):
            return [self._parse_function_arg(elt) for elt in node.elts]
        else:
            raise EmevdSyntaxError(node.lineno, f"Instruction arguments must be strings, numbers, or "
                                                f"predefined constants, not {ast.dump(node)}.")


def is_function_expression(node):
    return isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)


def is_if(node):
    return isinstance(node, ast.If)


def is_condition_assignment(node):
    return isinstance(node, ast.Assign) and node.value.func.id == 'Condition'


if __name__ == '__main__':
    EmevdCompiler('example.evs')
