import logging
import re

from .emedf import ArgType
from .exceptions import NumericEmevdError

__all__ = ["build_numeric"]


_LOGGER = logging.getLogger(__name__)


INSTRUCTION_RE = re.compile(r" +(\d+)\[(\d+)] \(([iIhHbBfs|]*)\)\[([\d, .-]*)] ?(<[\d, ]*>)?")
EVENT_ARG_REPLACEMENT_RE = re.compile(r" +\^\((\d+) <- (\d+), (\d+)\)")
EVENT_HEADER_RE = re.compile(r"^(\d+), ([012])")


class MissingInstructionError(Exception):
    """Raised when an instruction `(category, index)` cannot be found in EMEDF dictionary."""
    def __init__(self, category: int, index: int):
        super().__init__(f"Instruction ({category}, {index}) is not present in EMEDF dictionary.")


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

        if not event_lines:
            # No events (e.g., some overworld tiles in Elden Ring).
            return events, linked_offsets, strings

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
                category = int(m_instruction.group(1))
                index = int(m_instruction.group(2))
                display_arg_types = m_instruction.group(3)
                args_list_string = m_instruction.group(4)
                if m_instruction.group(5) is not None:
                    event_layers = [int(e) for e in m_instruction.group(5)[1:-1].split(", ")]
                else:
                    event_layers = None

                # Check the argument list against the format_string.
                split_arg_list = args_list_string.split(",")
                # Remove required|optional separator and replace 's' with 'I' (string offset).
                struct_arg_types = display_arg_types.replace("|", "").replace("s", "I")
                if split_arg_list == [""]:
                    split_arg_list = []
                if len(struct_arg_types) != len(split_arg_list):
                    print(m_instruction, args_list_string)
                    _LOGGER.error(
                        f"Number of args ({len(struct_arg_types)}) does not match length of the instruction "
                        f"format string ('{display_arg_types}') (line {lineno}) (args = {split_arg_list})"
                    )
                    raise NumericEmevdError(
                        lineno,
                        f"Number of args ({len(struct_arg_types)}) does not match length of the instruction "
                        f"format string ('{display_arg_types}') (Line {lineno})",
                    )

                args_list = []
                for i, fmt in enumerate(struct_arg_types):
                    arg = split_arg_list[i]
                    try:
                        arg_type = ArgType.from_fmt(fmt)
                    except ValueError:
                        raise NumericEmevdError(lineno, f"Invalid arg type: '{fmt}'")
                    if arg_type == ArgType.f32:
                        args_list.append(float(arg))
                    else:
                        parsed_arg = int(arg)
                        min_value, max_value = arg_type.get_type_min_max()
                        if arg_type == ArgType.u32 and parsed_arg == -1:
                            _LOGGER.warning(
                                f"-1 given for unsigned integer. Converting to {max_value}."
                            )
                            parsed_arg = max_value  # -1 is still acceptable for unsigned types
                        elif arg_type == ArgType.s32 and parsed_arg == 2 ** 32 - 1:
                            _LOGGER.warning(
                                f"Unsigned max value ({ArgType.s32.get_type_min_max()[1]}) given for signed integer. "
                                f"Converting to -1.")
                            parsed_arg = -1
                        if min_value <= parsed_arg <= max_value:
                            # `-1` is acceptable even for signed types (e.g., as a default).
                            args_list.append(parsed_arg)
                        else:
                            _LOGGER.error(
                                f"Argument '{arg}' is not inside the permitted range of data type "
                                f"'{fmt}': ({min_value}, {max_value}) (line {lineno}) "
                                f"(instruction = {category}[{index}], "
                                f"args_format = {display_arg_types}, args_list = {args_list_string})"
                            )
                            raise NumericEmevdError(
                                lineno,
                                f"Argument '{arg}' is not inside the permitted range of data type "
                                f"'{fmt}': ({min_value}, {max_value}) (line {lineno}) "
                                f"(instruction = {category}[{index}], "
                                f"args_format = {display_arg_types}, args_list = {args_list_string})"
                            )

                instr = event_class.Instruction(category, index, display_arg_types, args_list, event_layers)
                instruction_list.append(instr)

            elif m_arg_r:
                if len(instruction_list) >= 1:
                    # Parse the line as an arg replacement for the previous line.
                    write_from_byte = int(m_arg_r.group(1))
                    read_from_byte = int(m_arg_r.group(2))
                    bytes_to_write = int(m_arg_r.group(3))

                    event_arg = event_class.EventArg(
                        len(instruction_list) - 1, write_from_byte, read_from_byte, bytes_to_write
                    )
                    instruction_list[-1].event_args.append(event_arg)
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
