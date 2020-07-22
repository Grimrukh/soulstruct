import logging
import re
from enum import Enum

from soulstruct.events.internal import get_write_offset, format_event_layers

__all__ = ["SET_INSTRUCTION_ARG_TYPES", "to_numeric", "build_numeric"]
_LOGGER = logging.getLogger(__name__)


ELEMENT_MIN_MAX = {
    "b": (-128, 127),
    "B": (0, 255),
    "h": (-32768, 32767),
    "H": (0, 65535),
    "i": (-2147483648, 2147483647),
    "I": (0, 4294967295),
}
INSTRUCTION_RE = re.compile(r" [ ]*(\d+)\[(\d+)\] \(([iIhHbBfs|]*)\)\[([\d, .-]*)\][ ]?(<[\d, ]*>)?")
EVENT_ARG_REPLACEMENT_RE = re.compile(r" [ ]*\^\((\d+) <- (\d+), (\d+)\)")
EVENT_HEADER_RE = re.compile(r"^(\d+), ([012])")

INSTRUCTION_ARG_TYPES = {}  # Set by game module.


def SET_INSTRUCTION_ARG_TYPES(arg_types):
    global INSTRUCTION_ARG_TYPES
    INSTRUCTION_ARG_TYPES = arg_types


class NumericEmevdError(Exception):
    def __init__(self, lineno, msg):
        super().__init__(f"LINE {lineno}: {msg}")


def to_numeric(instruction_info, *args, arg_types=None, event_layers=None):
    """Instruction info should be (class, index, [defaults]), with defaults assumed all zeroes if absent.

    `event_layers` is supported here for intellisense purposes, and does function, but the EVS parser will always
    process it separately anyway (as it's too clunky, API-wise, to pass it through every instruction).
    """
    global INSTRUCTION_ARG_TYPES
    if not INSTRUCTION_ARG_TYPES:
        raise AttributeError("EMEVD instruction arg types have not been set with `SET_INSTRUCTION_ARG_TYPES`.")
    event_args = []
    arg_loads = []
    event_layer_string = format_event_layers(event_layers)
    if arg_types is None:
        try:
            arg_types = INSTRUCTION_ARG_TYPES[instruction_info[0]][instruction_info[1]]
        except KeyError:
            raise KeyError(f"Could not find instruction {instruction_info[0]}[{instruction_info[1]:02d} in type dict.")
    for i, arg in enumerate(args):
        if isinstance(arg, Enum):
            event_args.append(args[i].value)
        elif isinstance(arg, bool):
            event_args.append(int(arg))
        elif isinstance(arg, tuple):
            # Start offset and size of an event argument.
            write_offset = get_write_offset(arg_types, i)
            arg_loads.append(f"    ^({write_offset} <- {arg[0]}, {arg[1]})")
            if len(instruction_info) == 3:
                # Use optional dummy dictionary.
                event_args.append(instruction_info[2][i])
            else:
                event_args.append(0)
        else:
            event_args.append(arg)
    instruction_string = f"{instruction_info[0]: 5d}[{instruction_info[1]:02d}] ({arg_types}){event_args}"
    return [instruction_string + event_layer_string] + arg_loads


def build_numeric(numeric_string: str, event_class):
    """Parses the text data from the given numeric-style string into a dictionary of events suitable for use as an
    `EMEVD` source, which can then be packed to binary.

    Raises a ValueError if the numeric input cannot be parsed for any reason.
    """
    # TODO: Allow whitespace on blank lines between events.
    text_events = re.split(r"\n{2,}", numeric_string)

    events = {}
    linked_offsets = []
    strings = b""

    lineno = 0
    for text_event in text_events:
        if text_event.startswith("linked:"):
            for offset in text_event[8:].split("\n"):
                if offset.strip():
                    linked_offsets += [int(offset.strip())]
            continue

        if text_event.startswith("strings:"):
            for offset_with_string in text_event[9:].split("\n"):
                if not offset_with_string:
                    continue
                z_string = offset_with_string.split(":", 1)[-1].strip().encode("utf-16le") + b"\0\0"
                strings += z_string
            continue

        event_lines = text_event.splitlines()
        header_line = event_lines[0]
        m = EVENT_HEADER_RE.match(header_line)
        if not m:
            _LOGGER.error(f"Error parsing event header line: {header_line}")
            raise NumericEmevdError(lineno, f"Error parsing header line: '{header_line}'.")
        event_id = int(m.group(1))
        restart_type = int(m.group(2))

        instruction_list = []
        for instruction_or_event_arg in event_lines[1:]:
            lineno += 1
            m_instruction = INSTRUCTION_RE.match(instruction_or_event_arg)
            m_arg_r = EVENT_ARG_REPLACEMENT_RE.match(instruction_or_event_arg)

            if m_instruction:
                # Parse the line as an instruction.
                instruction_class = int(m_instruction.group(1))
                instruction_index = int(m_instruction.group(2))
                args_format = m_instruction.group(3)
                args_list_string = m_instruction.group(4)
                if m_instruction.group(5) is not None:
                    event_layers = [int(e) for e in m_instruction.group(5)[1:-1].split(", ")]
                else:
                    event_layers = None

                # Check the argument list against the format_string.
                split_arg_list = args_list_string.split(",")
                # Remove required|optional separator and replace 's' with 'I' (string offset).
                raw_args_format = args_format.replace("|", "").replace("s", "I")
                if split_arg_list == [""]:
                    split_arg_list = []
                if len(raw_args_format) != len(split_arg_list):
                    _LOGGER.error(
                        f"Number of args ({len(raw_args_format)}) does not match length of the instruction "
                        f"format string ('{args_format}') (line {lineno}) (args = {split_arg_list})"
                    )
                    raise NumericEmevdError(
                        lineno,
                        f"Number of args ({len(raw_args_format)}) does not match length of the instruction "
                        f"format string ('{args_format}') (Line {lineno})",
                    )

                args_list = []
                for i, element in enumerate(raw_args_format):
                    arg = split_arg_list[i]
                    if element == "f":
                        args_list.append(float(arg))
                    elif element in ELEMENT_MIN_MAX:
                        min_value, max_value = ELEMENT_MIN_MAX[element]
                        parsed_arg = int(arg)
                        if min_value <= parsed_arg <= max_value:
                            args_list.append(parsed_arg)
                        else:
                            _LOGGER.error(
                                f"Argument '{arg}' is not inside the permitted range of data type "
                                f"'{element}' {repr(ELEMENT_MIN_MAX[element])} (line {lineno}) "
                                f"(instruction = {instruction_class}[{instruction_index}], "
                                f"args_format = {args_format}, args_list = {args_list_string})"
                            )
                            raise NumericEmevdError(
                                lineno,
                                f"Argument '{arg}' is not inside the permitted range of data type "
                                f"'{element}' {repr(ELEMENT_MIN_MAX[element])} (Line {lineno})",
                            )
                instruction_list.append(
                    event_class.Instruction(instruction_class, instruction_index, args_format, args_list, event_layers)
                )

            elif m_arg_r:
                if len(instruction_list) >= 1:
                    # Parse the line as an arg replacement for the previous line.
                    write_from_byte = int(m_arg_r.group(1))
                    read_from_byte = int(m_arg_r.group(2))
                    bytes_to_write = int(m_arg_r.group(3))

                    instruction_list[-1].event_args.append(
                        event_class.EventArg(len(instruction_list) - 1, write_from_byte, read_from_byte, bytes_to_write)
                    )
                else:
                    raise NumericEmevdError(
                        lineno,
                        f"Parameter replacement '{instruction_or_event_arg}' does not follow an " f"instruction line.",
                    )
            else:
                # Malformed line.
                raise NumericEmevdError(
                    lineno,
                    f"Line '{instruction_or_event_arg}' cannot be parsed as an instruction or event arg "
                    f"replacement.",
                )
        events[event_id] = event_class(event_id, restart_type, instruction_list)

    return events, linked_offsets, strings
