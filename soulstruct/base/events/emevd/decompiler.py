
__all__ = [
    "base_decompiler_instruction",
    "reprocess_opt_args",
    "looks_like_entity_id",
    "assemble_arg_string",
    "base_decompile_run_event",
    "base_decompile_run_common_event",
]

import logging
import struct
import typing as tp

from soulstruct.base.game_types.game_enums_manager import GameEnumsManager
from soulstruct.base.events.emevd.enums import BaseEMEVDFlags
from soulstruct.base.game_types import GameObject

_LOGGER = logging.getLogger(__name__)


def reprocess_opt_args(integer_args, arg_type_string):
    """Re-interpret integer data as a given struct."""
    true_arg_type_string = arg_type_string.replace("s", "I")
    packed = struct.pack(len(integer_args) * "I", *integer_args)
    return struct.unpack("@" + true_arg_type_string, packed[: struct.calcsize(true_arg_type_string)])


def looks_like_entity_id(value: int, event_id: int = None):
    """Guesses if `value` is an entity ID. Used with `RunEvent{Common}` calls.

    TODO: Currently blindly converting seven-digit integers in event calls, under the probably safe
     assumption that there will be no false positives. Also including four-digit integers starting with 6
     (NPC entity IDs), unless `event_id` is 11210117 (DS1R arena event - super hacky).
     Ideally, we would inspect if the event argument is used in ANY instruction as a `MapEntity`.
    """
    if not isinstance(value, int) or event_id == 11210717:
        return False
    return len(str(value)) == 7 or (len(str(value)) == 4 and str(value)[0] == "6")


class EnumValue:
    """Stores information about an `IntEnum` value, including a proper `repr` for string formatting and `eq` for
    useful value comparisons."""
    def __init__(self, enum: type, value: int):
        self.type = enum
        self.type_name = enum.__name__
        self.instance = enum(value)
        self.name = enum(value).name
        self.value = value

    def __repr__(self):
        return f"{self.type_name}.{self.name}"

    def __eq__(self, other: int):
        return self.value == other

    def __getattr__(self, name):
        return getattr(self.instance, name)


class Variable(str):
    """String subclass for event arguments whose `repr` does not include quotes."""

    def __repr__(self) -> str:
        return f"{self}"


def _process_arg_types(
    args: dict[str, tp.Any],
    emedf_args_info: dict,
    enums_module: tp.Any,
    enums_manager: GameEnumsManager,
):
    """Convert arguments to their appropriate types and (if `enums_manager` is given) game-defined enums."""
    for arg_name, arg_value in args.items():
        if isinstance(arg_value, str):  # event argument (will be printed as a valid Python variable name)
            args[arg_name] = Variable(arg_value)
            continue

        arg_type = emedf_args_info[arg_name]["type"]

        if arg_type in {int, float, tuple}:
            continue  # no processing needed

        if arg_type is bool:  # convert `int` to `bool`
            args[arg_name] = bool(arg_value)
            continue

        # From here, `arg_type` must be a Union type hint or game enum class.

        try:
            origin = tp.get_origin(arg_type)
        except AttributeError:
            union_types = ()  # implies `arg_type` is a class for checks below
        else:
            union_types = tuple(t for t in tp.get_args(arg_type) if t is not int) if origin is tp.Union else ()
            if len(union_types) == 1:
                arg_type = union_types[0]
                union_types = ()
                if arg_type is bool:
                    args[arg_name] = bool(arg_value)
                    continue
            else:
                if bool in union_types:  # convert `int` to `bool`
                    args[arg_name] = bool(arg_value)
                    continue

            # All union types should be `MapEntity` subclasses; this will be enforced by the checkout method
            # below (invalid types will have no entity ID dictionaries).

        if union_types or issubclass(arg_type, GameObject):

            if arg_value == 10000:
                args[arg_name] = Variable("PLAYER")
                continue
            if 10001 <= arg_value <= 10009:
                args[arg_name] = Variable(f"CLIENT_PLAYER_{arg_value - 10000}")
                continue

            # Look up entity ID from imported module enums (generally parsed in `EMEVD.to_evs()`).

            try:
                if union_types:
                    args[arg_name] = Variable(enums_manager.check_out_enum(arg_value, *union_types))
                else:  # single class
                    args[arg_name] = Variable(enums_manager.check_out_enum(arg_value, arg_type))
            except GameEnumsManager.EnumManagerError:
                pass
            continue  # leave as entity ID if not replaced

        try:
            enum = getattr(enums_module, arg_type.__name__)  # get real enum class from game-specific module
        except AttributeError:
            raise ValueError(f"Invalid enum type for decompiler (arg '{arg_name}'): {arg_type.__name__}")
        if issubclass(enum, BaseEMEVDFlags):
            if arg_value == 0:
                args[arg_name] = 0
            else:
                flag_enum_values = []
                for flag_value in enum:
                    if arg_value == flag_value:
                        # Use exact flag.
                        flag_enum_values = [EnumValue(enum, flag_value)]
                        break
                    if arg_value & flag_value == flag_value:
                        flag_enum_values.append(EnumValue(enum, flag_value))
                args[arg_name] = Variable(" | ".join(f"{v}" for v in flag_enum_values))
        elif enum.__name__ == "ConditionGroup":
            # Omit enum type name from variable (e.g., just `OR_1`).
            try:
                enum_value = EnumValue(enum, arg_value)
            except ValueError:
                raise ValueError(f"Invalid {str(enum)} value: {arg_value}")
            args[arg_name] = Variable(enum_value.name)
        else:
            try:
                args[arg_name] = EnumValue(enum, arg_value)
            except ValueError:
                raise ValueError(f"Invalid {str(enum)} value: {arg_value}")


def assemble_arg_string(defaults: dict, *args, **kwargs):
    """Assemble a string of `args` (without argument names) and `kwargs` (with argument names) in the given order.
    Any kwarg whose value matches the same key's value in `defaults` is left out.

    The values of `args` and `kwargs` should be ready for string formatting.
    """
    arguments = [f"{arg}" for arg in args]
    for kwarg, value in kwargs.items():
        try:
            default = defaults[kwarg]
        except KeyError:
            arguments.append(f"{kwarg}={value}")
        else:
            if value != default:
                arguments.append(f"{kwarg}={value}")
    return ", ".join(arguments)


def base_decompiler_instruction(
    emedf: dict,
    decompiler_funcs: dict[tuple[int, int], tp.Callable],
    opt_args_decompiler_funcs: dict[tuple[int, int], tp.Callable],
    enums_module: tp.Any,
    category: int,
    index: int,
    req_args: list[tp.Any],
    opt_args: list[tp.Any],
    opt_arg_types="",
    enums_manager: GameEnumsManager = None,
):
    instr_info = emedf[category, index]
    emedf_args_info = instr_info["args"]
    if len(emedf_args_info) != len(req_args):
        raise ValueError(
            f"Cannot decompile instruction ({category}, {index}): number of arguments in EMEDF "
            f"({len(emedf_args_info)}) does not match number of (required) argument values given ({len(req_args)})."
        )
    args_dict = {arg_name: req_args[i] for i, arg_name in enumerate(emedf_args_info)}
    _process_arg_types(args_dict, emedf_args_info, enums_module, enums_manager)

    if (category, index) in opt_args_decompiler_funcs:
        # Manual function will check event args for entity IDs.
        return opt_args_decompiler_funcs[category, index](
            *args_dict.values(), *opt_args, arg_types=opt_arg_types, enums_manager=enums_manager
        )

    if opt_args or opt_arg_types:
        raise ValueError(f"Cannot pass `opt_args` or `opt_arg_types` to instruction ({category}, {index}).")

    if (category, index) in decompiler_funcs:
        return decompiler_funcs[category, index](*args_dict.values())

    evs_name = instr_info["alias"]
    emedf_args_info = instr_info["args"]
    evs_args_info = instr_info.get("evs_args", emedf_args_info)
    arg_strings = []
    evs_args = {}
    for evs_arg_name, evs_arg_info in evs_args_info.items():
        if "to_evs" in evs_arg_info:
            # Convert to EVS args.
            evs_args[evs_arg_name] = evs_arg_info['to_evs'](args_dict)
        elif evs_arg_name in emedf_args_info:
            # Default to EMEDF value and redirect info.
            evs_args[evs_arg_name] = args_dict[evs_arg_name]
            if not evs_arg_info:
                evs_args_info[evs_arg_name] = emedf_args_info[evs_arg_name]
        else:
            raise ValueError(f"EVS argument '{evs_arg_name}' does not define 'to_evs' or appear in EMEDF args.")

    # Check values against partials.
    filtered_evs_args = evs_args.copy()
    if "partials" in instr_info:
        for partial_evs_name, partial_kwargs in instr_info["partials"].items():
            partial_kwargs = {k: v for k, v in partial_kwargs.items() if k != "__docstring"}
            if all(evs_args[k] == v for k, v in partial_kwargs.items()):
                # Full partial kwargs match. Use this EVS name and remove partial keywords.
                evs_name = partial_evs_name
                for k in partial_kwargs:
                    filtered_evs_args.pop(k)
                break  # first match takes precedence (e.g., matching PLAYER rather than just Character type)

    # Omit default values (including for partials, which use the same default values for non-baked keywords) and hide
    # keyword names as long as `hide_name` remains True.
    hiding_names = True
    for evs_arg_name, arg_value in filtered_evs_args.items():
        hide_name = evs_args_info[evs_arg_name].get("hide_name", False)
        if hide_name and not hiding_names:
            print(f"# WARNING: 'hide_name' is False then True again for instruction '{evs_name}'.")
        hiding_names &= hide_name
        default = evs_args_info[evs_arg_name]["default"]
        if default is not None:
            if callable(default):
                try:
                    default = default(filtered_evs_args)
                except (AttributeError, ValueError):
                    # Default cannot be calculated from raw EMEVD arguments.
                    default = None
            if default is not None and arg_value == default:
                # Omit from arguments.
                continue
        # Otherwise, generate string.
        arg_strings.append(f"{arg_value}" if hiding_names else f"{evs_arg_name}={arg_value}")

    return f"{evs_name}({', '.join(arg_strings)})"


def base_decompile_run_event(
    slot: int, event_id: int, first_arg: int, *opt_args, arg_types: str, enums_manager: GameEnumsManager = None
):
    """Shared across all games."""
    if not opt_args and first_arg == 0:
        # `args` and `arg_types` not needed.
        # NOTE: Some Bloodborne events use non-zero slots for events without optional arguments.
        if slot != 0:
            if event_id in enums_manager.all_event_ids:
                return f"Event_{event_id}({slot=})"
            return f"RunEvent({event_id}, {slot=})"
        if event_id in enums_manager.all_event_ids:
            return f"Event_{event_id}()"

    event_args = (first_arg, *opt_args)

    if (
        arg_types and "f" in arg_types and not arg_types.strip("i").strip("f")
        and all(isinstance(i, int) for i in event_args)
    ):
        # Process incorrectly unpacked arguments (e.g. floats represented by integers).
        try:
            event_args = reprocess_opt_args(event_args, arg_types)
        except struct.error:
            _LOGGER.error(
                f"Error interpreting event arguments for event ID {event_id}: "
                f"args = {event_args}, arg_types = {arg_types}"
            )
            raise

    if enums_manager is not None:
        new_args = list(event_args)
        for i, arg in enumerate(event_args):
            if looks_like_entity_id(arg, event_id):
                try:
                    new_args[i] = Variable(enums_manager.check_out_enum(arg))
                except GameEnumsManager.EnumManagerError:
                    pass  # do nothing
        event_args = tuple(new_args)

    if event_id in enums_manager.all_event_ids:
        # Arg types are given in event definition and are not needed in this call.
        # TODO: Support multiline.
        return f"Event_{event_id}({slot}, {', '.join(repr(e) for e in event_args)})"

    if not arg_types or not arg_types.strip("i"):
        # No arg types, or all signed integers (default). "arg_types" keyword omitted.
        return f"RunEvent({event_id}, {slot=}, args={event_args})"
    return f"RunEvent({event_id}, {slot=}, args={event_args}, arg_types=\"{arg_types}\")"


def base_decompile_run_common_event(
    event_id: int, first_arg: int, *opt_args, arg_types: str, enums_manager: GameEnumsManager = None, slot=None,
):
    """Shared across games from Dark Souls 3 onward.

    TODO:
        - Unrelated: use `with EVENT_LAYERS(0, 1, 2):` block for event layers, rather than tacked-on argument.
    """
    if not opt_args and first_arg == 0:
        # `args` and `arg_types` not needed. (Yes, there are common events called without arguments.)
        if slot is None or slot == 0:
            if event_id in enums_manager.all_common_event_ids:
                return f"CommonFunc_{event_id}()"  # default slot
            return f"RunCommonEvent({event_id})"  # default slot
        if event_id in enums_manager.all_common_event_ids:
            return f"CommonFunc_{event_id}({slot=})"
        return f"RunCommonEvent({event_id}, {slot=})"

    event_args = (first_arg, *opt_args)

    if (
        arg_types and "f" in arg_types and not arg_types.strip("i").strip("f")
        and all(isinstance(i, int) for i in event_args)
    ):
        # Process incorrectly unpacked arguments (e.g. floats represented by integers).
        try:
            event_args = reprocess_opt_args(event_args, arg_types)
        except struct.error:
            _LOGGER.error(
                f"Error interpreting event arguments for event ID {event_id}: "
                f"args = {event_args}, arg_types = {arg_types}"
            )
            raise

    if enums_manager is not None:
        new_args = list(event_args)
        for i, arg in enumerate(event_args):
            if looks_like_entity_id(arg, event_id):
                try:
                    new_args[i] = Variable(enums_manager.check_out_enum(arg))
                except GameEnumsManager.EnumManagerError:
                    pass  # do nothing
        event_args = tuple(new_args)

    if event_id in enums_manager.all_common_event_ids:
        # Arg types are given in event definition and are not needed in this call.
        # NOTE: Even if `slot` is None, slot 0 is written for function signature match.
        if slot is None:
            return f"CommonFunc_{event_id}(0, {', '.join(repr(e) for e in event_args)})"
        return f"CommonFunc_{event_id}({slot}, {', '.join(repr(e) for e in event_args)})"

    if not arg_types or not arg_types.strip("i"):
        # No arg types, or all signed integers (default). "arg_types" keyword omitted.
        if slot is None:
            return f"RunCommonEvent({event_id}, args={event_args})"
        return f"RunCommonEvent({event_id}, {slot=}, args={event_args})"
    if slot is None:
        return f"RunCommonEvent({event_id}, args={event_args}, arg_types=\"{arg_types}\")"
    return f"RunCommonEvent({event_id}, {slot=}, args={event_args}, arg_types=\"{arg_types}\")"
