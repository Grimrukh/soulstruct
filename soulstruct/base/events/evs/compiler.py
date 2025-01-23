from __future__ import annotations

__all__ = ["EVSInstructionCompiler", "BooleanTestCompiler"]

import abc
from dataclasses import dataclass
import inspect
import logging
import typing as tp
from enum import Enum

from soulstruct.base.game_types import *
from ..emevd.utils import EventArgumentData
from .exceptions import NoNegateError, NoSkipOrReturnError
from .utils import get_write_offset

if tp.TYPE_CHECKING:
    from .conditions import EVSConditionManager, ConditionGroupState

_LOGGER = logging.getLogger("soulstruct")


class EVSInstructionCompiler(abc.ABC):
    """Wraps a dictionary of functions and exposes a handy method/decorator for adding functions to the dictionary.
    
    Also references the same `EVSConditionManager` as `EVSParser` to manage condition group states.

    This dictionary maps EVS instruction function names to functions that produce actual numeric output. These functions
    may take different arguments to a single underlying instruction (e.g., tuples as flag ranges, `GameMap` instances)
    or merge multiple underlying instructions into one interface for simplicity, such as `IfActionButton` or
    `PlayCutscene`. If a function name does not appear in here, it will found as an 'alias' in EMEDF and compiled
    automatically. (Such functions should still appear in the PYI module for intelli-sense.)
    """
    EMEDF_ALIASES: tp.ClassVar[dict[str, tuple[int, int, dict]]]
    _CUSTOM_FUNC_NAMES: tp.ClassVar[set[str]]
    _CUSTOM_FUNC_CONDITION_ARGS: tp.ClassVar[dict[str, tuple[int, int]]]
    
    cond_manager: EVSConditionManager

    def __init__(self, cond_manager: EVSConditionManager):
        self.cond_manager = cond_manager

    def compile(self, instr_name: str, *args, **kwargs) -> list[str]:
        """Compile instruction using `COMPILER` function if available, or fall back to `_base_compile`
        that purely uses EMEDF. Also falls back if `instr_name` starts with an underscore (e.g. for a wrapped custom
        instruction with the same name as an internal base EMEDF instruction).
        """
        if instr_name in self._CUSTOM_FUNC_NAMES:

            if self.cond_manager.DEBUG_ENABLED:
                _LOGGER.debug(f"Compiling custom instruction '{instr_name}' with args {args} and kwargs {kwargs}.")

            output_condition_index, input_condition_index = self._CUSTOM_FUNC_CONDITION_ARGS[instr_name]
            if output_condition_index is not None:
                condition = kwargs.get("condition", args[output_condition_index])
                if input_condition_index is not None:
                    input_condition = kwargs.get("input_condition", args[input_condition_index])
                    self.cond_manager[condition].activate_with_child(input_condition)
                else:
                    self.cond_manager[condition].activate()

            return getattr(self, instr_name)(*args, **kwargs)

        return self._base_compile(instr_name.lstrip("_"), *args, **kwargs)

    def _base_compile(self, instr_name: str, *args, arg_types="", **kwargs) -> list[str]:
        """Compile instruction from EMEDF information.

        Updates managed EVS condition groups in `cond` (if given) based on the instruction's condition arguments,
        including deactivating all condition groups if the instruction is a 'frame-ending' instruction like
        `MAIN.Await()` / `Wait()`.

        If positional `args` are used, they must be ordered correctly for EMEDF and not repeated in `kwargs`, just like
        regular Python.

        Returns a list of numeric instruction strings.
        """
        if instr_name not in self.EMEDF_ALIASES:
            raise ValueError(f"Instruction '{instr_name}' not found in EMEDF.")

        category, index, instr_info = self.EMEDF_ALIASES[instr_name]
        emedf_args_info = instr_info["args"]
        evs_args_info = instr_info.get("evs_args", emedf_args_info)

        is_partial = "partials" in instr_info and instr_name in instr_info["partials"]
        partial_kwargs = instr_info["partials"][instr_name] if is_partial else {}
        signature = [arg_name for arg_name in evs_args_info if arg_name not in partial_kwargs]

        # Build real `evs_kwargs` from `args` and `kwargs`. Default values for missing arguments will be found below.
        args = list(args)
        evs_kwargs = {}
        for evs_arg_name in tuple(signature):
            if args:
                evs_kwargs[evs_arg_name] = args.pop(0)
                signature.remove(evs_arg_name)
            elif evs_arg_name in kwargs:
                if evs_arg_name in evs_kwargs:
                    # Positional argument was also given as keyword. Invalid usage.
                    raise ValueError(
                        f"Keyword argument '{evs_arg_name}' for instruction '{instr_name}' was already given as a "
                        f"position argument."
                    )
                evs_kwargs[evs_arg_name] = kwargs.pop(evs_arg_name)
                signature.remove(evs_arg_name)

        if kwargs:
            raise ValueError(
                f"Invalid keyword argument(s) for instruction ({category}, {index}) '{instr_name}': {list(kwargs)}\n"
                f"    Constructed kwargs: {evs_kwargs}"
            )

        self.update_condition_manager(category, index, instr_name, evs_kwargs)

        if is_partial:
            # Fill in baked keyword arguments and redirect name.
            for arg_name, baked_value in instr_info["partials"][instr_name].items():
                if arg_name in evs_kwargs:
                    raise ValueError(
                        f"Keyword '{arg_name}' should not be given to partially baked instruction '{instr_name}'."
                    )
                evs_kwargs[arg_name] = baked_value
            instr_name = instr_info["alias"]

        # Fill in default EVS arguments.
        for evs_arg_name, evs_arg_info in evs_args_info.items():
            if not evs_arg_info:
                evs_arg_info = emedf_args_info[evs_arg_name]
            if evs_arg_name not in evs_kwargs or evs_kwargs[evs_arg_name] is None:
                # Some custom instructions may pass in `None` as a value that needs a default here.
                default = evs_arg_info["default"]
                if default is None:
                    raise ValueError(
                        f"Missing required argument for instruction '{instr_name}' "
                        f"({category}, {index}): {evs_arg_name}"
                    )
                if callable(default):
                    try:
                        default = default(evs_kwargs)
                    except ValueError as ex:
                        raise ValueError(
                            f"Could not automatically determine default value for argument '{evs_arg_name}' in "
                            f"instruction  '{instr_name}' ({category}, {index}). Error: {ex}"
                        )
                evs_kwargs[evs_arg_name] = default
                if evs_arg_name in signature:
                    signature.remove(evs_arg_name)

        if signature:
            raise ValueError(f"Arguments not found for instruction ({category}, {index}) '{instr_name}': {signature}")

        if not arg_types:
            arg_types = "".join(arg["internal_type"].get_fmt() for arg in emedf_args_info.values())
        arg_list = []
        arg_loads = []

        arg_index = 0  # used as enumerator below

        def _append_emevd_arg(value):
            nonlocal arg_index

            if value is None:
                raise ValueError(
                    f"Encountered `None` as argument value in EVS in instruction ({category}, {index}): {instr_name}"
                )

            if isinstance(value, EventArgumentData):
                value = (value.offset, value.size)

            if isinstance(value, Enum):
                arg_list.append(value.value)
            elif isinstance(value, bool):
                arg_list.append(int(value))
            elif isinstance(value, tuple):
                # Start offset and size of an event argument.
                write_offset = get_write_offset(arg_types, arg_index)
                arg_loads.append(f"    ^({write_offset} <- {value[0]}, {value[1]})")
                internal_default = arg_info.get("internal_default", 0)
                arg_list.append(internal_default)  # value that will be overridden by event argument
            else:
                arg_list.append(value)

        # Convert EVS arguments to EMEVD.
        for arg_name, arg_info in emedf_args_info.items():
            if "from_evs" in arg_info:
                _append_emevd_arg(arg_info["from_evs"](evs_kwargs))
                arg_index += 1
            elif arg_info["type"] is tuple:
                # Unpack values.
                for element in evs_kwargs.pop(arg_name):
                    _append_emevd_arg(element)
                    arg_index += 1
            elif arg_name in evs_kwargs:
                _append_emevd_arg(evs_kwargs.pop(arg_name))
                arg_index += 1
            else:
                raise ValueError(
                    f"Argument '{arg_name}' in instruction '{instr_name}' ({category}, {index}) has no "
                    "'from_evs' function defined in EMEDF."
                )

        instruction_string = f"{category: 5d}[{index:02d}] ({arg_types}){arg_list}"
        return [instruction_string] + arg_loads

    def update_condition_manager(self, category: int, index: int, instr_name: str, evs_kwargs: dict[str, tp.Any]):
        """Find and update state of any input/output conditions used in this instruction.
        
        Obviously, there could be complex branching conditions in events that make it impossible to track the actual 
        state of condition groups without knowing the exact path through the event based on game state and event args.
        """

        self.cond_manager.just_awaited_main = False  # enabled below if appropriate

        if (category, index) == (0, 0):  # `IfConditionState()`
            # Even if we're loading into MAIN, this final load might have relevance to EVS management at some point.
            output_condition = self.cond_manager[evs_kwargs["condition"]]
            input_condition = self.cond_manager[evs_kwargs["input_condition"]]
            output_condition.activate_with_child(input_condition)
            if output_condition.index == 0:
                # `MAIN.Await()` call deactivates all condition groups and makes active ones stale.
                self.cond_manager.deactivate_all()
                self.cond_manager.just_awaited_main = True
            return

        if category < 1000:
            # Test instruction categories that always have a first `condition` argument.
            try:
                output_condition = self.cond_manager[evs_kwargs["condition"]]
            except KeyError:
                _LOGGER.warning(
                    f"Could not find argument `condition` for instruction '{instr_name}'. This is unexpected. "
                    f"Cannot track condition group usage."
                )
            else:
                output_condition.activate()  # will disable `stale`
            return
        
        if category == 1001:
            # 'Wait' instruction that also resets condition groups.
            # TODO: There are some other instructions that do this, like "AwaitDialogResponse" (2007, 10) in ER.
            self.cond_manager.deactivate_all()

    def compile_game_object_test(
        self,
        game_object: tp.Union[GameObject, tuple],
        game_object_type: GAME_TYPE = None,
        negate=False,
        condition_group: ConditionGroupState = None,
        skip_lines=0,
        end_event=False,
        restart_event=False,
    ) -> list[str]:
        """Allows usage of `GameObject` enum values as boolean tests in EVS script.

        This base class version supports the most common base game types and relies on instructions that are known to
        exist in all games' EMEDF.
        """
        if game_object_type is None:
            game_object_type = type(game_object)

        test = BooleanTestCompiler(self)

        if issubclass(game_object_type, Map):
            test.if_true = "IfInsideMap"
            test.if_false = "IfOutsideMap"
        elif issubclass(game_object_type, Flag):
            test.set_all("FlagEnabled", "FlagDisabled")
        elif issubclass(game_object_type, Region):
            if game_object_type.__name__ == "RegionPoints":
                _LOGGER.warning(
                    f"Used a member of an enum called `RegionPoints` as a boolean test for being inside or outside "
                    f"a Region, which will not work for volumeless points."
                )
            test.if_true = "IfPlayerInsideRegion"
            test.if_false = "IfPlayerOutsideRegion"
        elif issubclass(game_object_type, Object):
            test.set_all("ObjectNotDestroyed", "ObjectDestroyed")  # True == object NOT destroyed
        elif issubclass(game_object_type, Character):
            test.if_true = "IfCharacterAlive"
            test.if_false = "IfCharacterDead"
        elif issubclass(game_object_type, ObjActEvent):
            test.if_true = "IfObjectActivated"
        else:
            raise TypeError(
                f"Game object type `{game_object_type.__name__}` cannot be used as a boolean directly in EVS script."
            )

        return test.compile_object(
            game_object,
            negate=negate,
            condition_group=condition_group,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
        )

    # noinspection PyUnusedLocal
    def RunEvent(self, event_id, slot=0, args=(0,), arg_types="", event_layers=None):
        """Run the given `event_id`, which must be defined in the same script.

        You can omit `arg_types` if all the arguments are unsigned integers (which is usually the case).

        Note that you can also call the name of the event directly and pass in the given arguments normally.

        Note that `event_layers` is supported as an argument here for intellisense purposes, as this is the instruction
        it will most commonly be used with, but it can be used with any instruction. The EVS parser handles this keyword
        argument separately, so it will never actually be passed to an instruction function like this one.
        """
        if not arg_types:
            # Assume all signed integers, unless the only argument is zero.
            arg_types = "I" if args == (0,) else "i" * len(args)
        if len(args) != len(arg_types):
            raise ValueError("Number of event arguments does not match length of argument type string in RunEvent.")
        full_arg_types = "iI" + str(arg_types[0])
        if len(arg_types) > 1:
            full_arg_types += f"|{arg_types[1:]}"
        return self._base_compile("RunEvent", slot=slot, event_id=event_id, args=args, arg_types=full_arg_types)

    @classmethod
    def process_custom_instructions(cls):
        """Looks at all methods defined on class that start with a capital letter and inspects their arguments for
        output and input conditions, so the `EVSConditionManager` can update condition group states.
        """

        # First, clear class dictionaries, as they may have been set by a parent class (e.g. PTDE -> DSR).
        cls._CUSTOM_FUNC_NAMES = set()
        cls._CUSTOM_FUNC_CONDITION_ARGS = {}
        
        for method_name in dir(cls):
            if not method_name[0].isupper():
                continue
            method = getattr(cls, method_name)
            if not callable(method):
                continue
            cls._CUSTOM_FUNC_NAMES.add(method_name)
            sig = inspect.signature(method)
            condition_index = None
            input_condition_index = None
            for i, param in enumerate(sig.parameters.values()):
                if param.name == "condition":
                    condition_index = i - 1  # ignore `self` argument
                if param.name == "input_condition":
                    input_condition_index = i - 1  # ignore `self` argument
            
            cls._CUSTOM_FUNC_CONDITION_ARGS[method_name] = (condition_index, input_condition_index)


@dataclass(slots=True)
class BooleanTestCompiler:
    """Simple container for test functions.

    Initialize with available EMEVD test functions, then use call it directly (e.g., for built-in tests like `HOST`)
    or call `compile_object(game_object)` to pass a single `game_object` to the underlying functions.
    """

    compiler: EVSInstructionCompiler
    skip_if_true: str = ""
    skip_if_false: str = ""
    if_true: str = ""
    if_false: str = ""
    end_if_true: str = ""
    end_if_false: str = ""
    restart_if_true: str = ""
    restart_if_false: str = ""

    def set_all(self, true_name: str, false_name: str):
        """Set all eight test at once using the same basic template, e.g. 'FlagEnabled' and 'FlagDisabled'."""
        self.skip_if_true = f"SkipLinesIf{true_name}"
        self.skip_if_false = f"SkipLinesIf{false_name}"
        self.if_true = f"If{true_name}"
        self.if_false = f"If{false_name}"
        self.end_if_true = f"EndIf{true_name}"
        self.end_if_false = f"EndIf{false_name}"
        self.restart_if_true = f"RestartIf{true_name}"
        self.restart_if_false = f"RestartIf{false_name}"

    def __call__(
        self,
        negate=False,
        condition=None,
        skip_lines=0,
        end_event=False,
        restart_event=False,
    ) -> list[str]:
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if not self.skip_if_true or not self.skip_if_false:
                raise NoSkipOrReturnError  # Both of these functions must be defined.
            if negate:
                return self.compiler.compile(self.skip_if_true, skip_lines)
            return self.compiler.compile(self.skip_if_false, skip_lines)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.if_false:
                    raise NoNegateError  # Some game types only have a positive condition test (e.g. IfObjectActivated).
                return self.compiler.compile(self.if_false, condition)
            return self.compiler.compile(self.if_true, condition)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.end_if_false:
                    raise NoSkipOrReturnError
                return self.compiler.compile(self.end_if_false)
            if not self.end_if_true:
                raise NoSkipOrReturnError
            return self.compiler.compile(self.end_if_true)

        if restart_event:
            if negate:
                if not self.restart_if_false:
                    raise NoSkipOrReturnError
                return self.compiler.compile(self.restart_if_false)
            if not self.restart_if_true:
                raise NoSkipOrReturnError
            return self.compiler.compile(self.restart_if_true)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    def compile_object(
        self,
        game_object,
        negate=False,
        condition_group: ConditionGroupState = None,
        skip_lines=0,
        end_event=False,
        restart_event=False,
    ) -> list[str]:
        if skip_lines > 0:
            if condition_group is not None or end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if not self.skip_if_true or not self.skip_if_false:
                raise NoSkipOrReturnError  # Both of these functions must be defined.
            if negate:
                return self.compiler.compile(self.skip_if_true, skip_lines, game_object)
            return self.compiler.compile(self.skip_if_false, skip_lines, game_object)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition_group is not None:
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.if_false:
                    raise NoNegateError  # Some game types only have a positive condition test (e.g. IfObjectActivated).
                return self.compiler.compile(self.if_false, condition_group.index, game_object)
            return self.compiler.compile(self.if_true, condition_group.index, game_object)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.end_if_false:
                    raise NoSkipOrReturnError
                return self.compiler.compile(self.end_if_false, game_object)
            if not self.end_if_true:
                raise NoSkipOrReturnError
            return self.compiler.compile(self.end_if_true, game_object)

        if restart_event:
            if negate:
                if not self.restart_if_false:
                    raise NoSkipOrReturnError
                return self.compiler.compile(self.restart_if_false, game_object)
            if not self.restart_if_true:
                raise NoSkipOrReturnError
            return self.compiler.compile(self.restart_if_true, game_object)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")
