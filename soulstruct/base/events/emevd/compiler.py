
__all__ = ["base_compile_instruction", "BooleanTestCompiler"]

import typing as tp
from enum import Enum

from .exceptions import NoNegateError, NoSkipOrReturnError
from .utils import EventArgumentData, get_write_offset


def base_compile_instruction(emedf_aliases: dict, instr_name: str, *args, arg_types="", **kwargs) -> list[str]:
    """Compile instruction from EMEDF information.

    If positional `args` are used, they must be ordered correctly for EMEDF and not repeated in `kwargs`, just like
    regular Python.
    """
    category, index, instr_info = emedf_aliases[instr_name]
    emedf_args_info = instr_info["args"]
    evs_args_info = instr_info.get("evs_args", emedf_args_info)

    is_partial = "partials" in instr_info and instr_name in instr_info["partials"]
    partial_kwargs = instr_info["partials"][instr_name] if is_partial else {}
    signature = [arg_name for arg_name in evs_args_info if arg_name not in partial_kwargs]

    # Build real `evs_kwargs` from `args` and `kwargs`. Default values for missing arguments will be attempted below.
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
                    f"Missing required argument for instruction '{instr_name}' ({category}, {index}): {evs_arg_name}"
                )
            if callable(default):
                try:
                    default = default(evs_kwargs)
                except ValueError as ex:
                    raise ValueError(
                        f"Could not automatically determine default value for argument '{evs_arg_name}' in instruction "
                        f"'{instr_name}' ({category}, {index}). Error: {ex}"
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

    def _append_emevd_arg(value):
        if value is None:
            raise ValueError(
                f"Encountered `None` as argument value in EVS in instruction ({category}, {index}): {instr_name}"
            )

        if isinstance(value, EventArgumentData):
            value = value.offset_tuple

        if isinstance(value, Enum):
            arg_list.append(value.value)
        elif isinstance(value, bool):
            arg_list.append(int(value))
        elif isinstance(value, tuple):
            # Start offset and size of an event argument.
            write_offset = get_write_offset(arg_types, i)
            arg_loads.append(f"    ^({write_offset} <- {value[0]}, {value[1]})")
            internal_default = arg_info.get("internal_default", 0)
            arg_list.append(internal_default)  # value that will be overridden by event argument
        else:
            arg_list.append(value)

    # Convert EVS arguments to EMEVD.
    for i, (arg_name, arg_info) in enumerate(emedf_args_info.items()):
        if "from_evs" in arg_info:
            _append_emevd_arg(arg_info["from_evs"](evs_kwargs))
        elif arg_info["type"] is tuple:
            # Unpack values.
            for element in evs_kwargs.pop(arg_name):
                _append_emevd_arg(element)
        elif arg_name not in evs_kwargs:
            raise ValueError(
                f"Argument '{arg_name}' in instruction '{instr_name}' ({category}, {index}) has no 'from_evs' function "
                f"defined in EMEDF."
            )
        else:
            _append_emevd_arg(evs_kwargs.pop(arg_name))

    instruction_string = f"{category: 5d}[{index:02d}] ({arg_types}){arg_list}"
    return [instruction_string] + arg_loads


class BooleanTestCompiler:
    """Simple container for test functions.

    Initialize with available EMEVD test functions, then use call it directly (e.g., for built-in tests like `HOST`)
    or call `compile_object(game_object)` to pass a single `game_object` to the underlying functions.
    """

    def __init__(
        self,
        compile_instruction: tp.Callable,
        skip_if_true="",
        skip_if_false="",
        if_true="",
        if_false="",
        end_if_true="",
        end_if_false="",
        restart_if_true="",
        restart_if_false="",
    ):
        self._compile_instruction = compile_instruction
        self.skip_if_true = skip_if_true
        self.skip_if_false = skip_if_false
        self.if_true = if_true
        self.if_false = if_false
        self.end_if_true = end_if_true
        self.end_if_false = end_if_false
        self.restart_if_true = restart_if_true
        self.restart_if_false = restart_if_false

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
                return self._compile_instruction(self.skip_if_true, skip_lines)
            return self._compile_instruction(self.skip_if_false, skip_lines)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.if_false:
                    raise NoNegateError  # Some game types only have a positive condition test (e.g. IfObjectActivated).
                return self._compile_instruction(self.if_false, condition)
            return self._compile_instruction(self.if_true, condition)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.end_if_false:
                    raise NoSkipOrReturnError
                return self._compile_instruction(self.end_if_false)
            if not self.end_if_true:
                raise NoSkipOrReturnError
            return self._compile_instruction(self.end_if_true)

        if restart_event:
            if negate:
                if not self.restart_if_false:
                    raise NoSkipOrReturnError
                return self._compile_instruction(self.restart_if_false)
            if not self.restart_if_true:
                raise NoSkipOrReturnError
            return self._compile_instruction(self.restart_if_true)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    def compile_object(
        self,
        game_object,
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
                return self._compile_instruction(self.skip_if_true, skip_lines, game_object)
            return self._compile_instruction(self.skip_if_false, skip_lines, game_object)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.if_false:
                    raise NoNegateError  # Some game types only have a positive condition test (e.g. IfObjectActivated).
                return self._compile_instruction(self.if_false, condition, game_object)
            return self._compile_instruction(self.if_true, condition, game_object)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if not self.end_if_false:
                    raise NoSkipOrReturnError
                return self._compile_instruction(self.end_if_false, game_object)
            if not self.end_if_true:
                raise NoSkipOrReturnError
            return self._compile_instruction(self.end_if_true, game_object)

        if restart_event:
            if negate:
                if not self.restart_if_false:
                    raise NoSkipOrReturnError
                return self._compile_instruction(self.restart_if_false, game_object)
            if not self.restart_if_true:
                raise NoSkipOrReturnError
            return self._compile_instruction(self.restart_if_true, game_object)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")
