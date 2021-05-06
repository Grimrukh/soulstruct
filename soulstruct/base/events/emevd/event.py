from __future__ import annotations

__all__ = ["Event", "EventArg"]

import abc
import logging
import re
import struct
import typing as tp

from .enums import RestartType
from .instruction import Instruction

if tp.TYPE_CHECKING:
    from soulstruct.game_types.msb_types import MapEntity
    from soulstruct.utilities.binary import BinaryStruct, BinaryReader
    from .utils import EntityEnumsManager

_LOGGER = logging.getLogger(__name__)


EVS_ARG_TYPES = {
    "i": "int",
    "I": "uint",
    "f": "float",
    "h": "short",
    "H": "ushort",
    "b": "char",
    "B": "uchar",
    "s": "int",
}

_SPECIAL_EVENT_NAMES = {
    0: "Constructor",
    50: "Preconstructor",
}

_INSTRUCTION_RE = re.compile(r"([\w\d]+)\((.*)\)")  # groups = (instruction_name, args)
_LABEL_RE = re.compile(r"DefineLabel\((\d+)\)")


class EventArg(abc.ABC):
    HEADER_STRUCT: BinaryStruct = None

    def __init__(self, instruction_line, write_from_byte=0, read_from_byte=0, bytes_to_write=0, zero=0):
        """Overrides argument data in a particular instruction using from dynamic args attached to the event."""
        self.line = instruction_line
        self.write_from_byte = write_from_byte
        self.read_from_byte = read_from_byte
        self.bytes_to_write = bytes_to_write
        if zero != 0:
            raise ValueError("Last field of arg replacement must be zero.")

    @classmethod
    def unpack(cls, reader: BinaryReader, count=1):
        event_args = []
        struct_dicts = reader.unpack_structs(cls.HEADER_STRUCT, count=count)
        for d in struct_dicts:
            event_args.append(cls(**d))
        return event_args

    def to_numeric(self):
        return f"({self.write_from_byte} <- {self.read_from_byte}, {self.bytes_to_write})"

    def to_binary(self):
        return self.HEADER_STRUCT.pack(
            instruction_line=self.line,
            write_from_byte=self.write_from_byte,
            read_from_byte=self.read_from_byte,
            bytes_to_write=self.bytes_to_write,
        )


class Event(abc.ABC):

    HEADER_STRUCT: BinaryStruct = None
    Instruction: tp.Type[Instruction] = None
    EventArg: tp.Type[EventArg] = None
    EVENT_ARG_TYPES = {}  # updated on load and before each write
    WRAP_LIMIT = 121  # PyCharm default line length

    DEFAULT_ARG_SIZE_TYPE = {1: "B", 2: "H", 4: "I"}

    def __init__(self, event_id=0, restart_type=0, instructions=None):
        self.event_id = event_id
        self.restart_type = restart_type
        self.instructions = instructions if instructions else []  # type: list[Instruction]

    @classmethod
    def unpack_event_dict(
        cls,
        reader: BinaryReader,
        instruction_table_offset,
        base_arg_data_offset,
        event_arg_table_offset,
        event_layers_table_offset,
        count=1,
    ) -> dict[int, Event]:
        event_dict = {}
        struct_dicts = reader.unpack_structs(cls.HEADER_STRUCT, count=count)

        for d in struct_dicts:
            reader.seek(instruction_table_offset + d["first_instruction_offset"])
            instruction_list = cls.Instruction.unpack(
                reader, base_arg_data_offset, event_layers_table_offset, count=d["instruction_count"]
            )

            reader.seek(event_arg_table_offset + d["first_event_arg_offset"])
            event_args = cls.EventArg.unpack(reader, count=d["event_arg_count"])

            for arg_r in event_args:
                # Attach event arg replacements to their instruction line.
                instruction_list[arg_r.line].event_args.append(arg_r)

            event_dict[d["event_id"]] = cls(d["event_id"], d["restart_type"], instruction_list)

        return event_dict

    def update_run_event_instructions(self):
        """Iterates over instructions and updates any `RunEvent` or `RunCommonEvent` instructions with event arguments
        with their proper `args_format` and `args_list` values.

        Called after all events have been loaded and `update_evs_function_args()` has been called (to scan events and
        detect their arguments).
        """
        for instruction in self.instructions:
            if (event_id := instruction.get_called_event()) is not None:
                try:
                    var_format = self.EVENT_ARG_TYPES[event_id]
                except KeyError:
                    # Undefined event was called. This has only been seen once in vanilla files, in DSR m12_01_00_00,
                    # where event `4294967295` (2 ** 32 - 1) is run near the end of the constructor for unknown reasons.
                    # TODO: Handle imported common events.
                    _LOGGER.warning(f"Event {event_id} was run, but is not defined anywhere.")
                    continue
                if not var_format:
                    # No arguments (zero). Leave "I" in arg types.
                    continue

                var_ind = instruction.display_arg_types.find("|")
                if var_ind == -1:
                    # Only one argument (maybe zero).
                    new_display_types = f"{instruction.struct_arg_types[:-1]}{var_format[0]}"
                else:
                    new_display_types = f"{instruction.struct_arg_types[:var_ind - 1]}{var_format[0]}|{var_format[1:]}"

                old_format = "@" + instruction.struct_arg_types
                instruction.display_arg_types = new_display_types
                try:
                    real_args = list(struct.unpack(
                        instruction.struct_arg_types + "0i", struct.pack(old_format + "0i", *instruction.args_list))
                    )
                except struct.error:
                    _LOGGER.error(
                        f"Failed to convert event arguments for instruction {instruction} from old format {old_format} "
                        f"to new format {instruction.struct_arg_types}. Args: {instruction.args_list}"
                    )
                    raise
                instruction.args_list = real_args

    @property
    def instruction_count(self):
        return len(self.instructions)

    @property
    def total_args_size(self):
        return sum([i.args_size for i in self.instructions])

    @property
    def event_arg_count(self):
        return sum([i.event_arg_count for i in self.instructions])

    def to_numeric(self):
        event_string = f"{self.event_id}, {self.restart_type}"
        for instruction in self.instructions:
            event_string += "\n" + "\n".join(instruction.to_numeric())
        return event_string

    def process_all_event_args(self) -> dict[tuple[int, int], set[str]]:
        """Process event args for all instructions and maintain a dictionary mapping `(read_start, read_stop)` event
        arg tuples to sets of detected format strings (should generally only contain one value)."""
        event_arg_types = {}
        for instruction in self.instructions:
            try:
                instruction_arg_types = instruction.process_event_args()
            except ValueError:
                raise ValueError(
                    f"Error occurred while applying event args in instruction "
                    f"{self.instructions.index(instruction)} of event {self.event_id}."
                )
            for arg_range, arg_types in instruction_arg_types.items():
                arg_range_types = event_arg_types.setdefault(arg_range, set())
                arg_range_types |= arg_types
        return {arg_range: event_arg_types[arg_range] for arg_range in sorted(event_arg_types)}

    def update_evs_function_args(self):
        event_arg_types = self.process_all_event_args()
        all_arg_names = []
        all_arg_types = []
        for (i, j), arg_types in event_arg_types.items():
            arg_name = f"arg_{i}_{j}"
            if len(arg_types) > 1:
                # Multiple detected types. Acceptable (using default integer type) only if they all the same size.
                sizes = {struct.calcsize(fmt) for fmt in arg_types}
                if len(sizes) == 1:
                    arg_size = next(iter(sizes))
                    arg_type = self.DEFAULT_ARG_SIZE_TYPE[arg_size]
                    _LOGGER.warning(
                        f"Detected multiple types for event arg '{arg_name}' in event {self.event_id}: {arg_types}. "
                        f"Using default type '{arg_type}' for this arg size ({arg_size})."
                    )
                else:
                    raise ValueError(
                        f"Detected multiple types for event arg '{arg_name}' in event {self.event_id}: {arg_types}. "
                        f"They have incompatible sizes, which is not permitted."
                    )
            else:
                arg_type = next(iter(arg_types))

            all_arg_names.append(arg_name)
            all_arg_types.append(arg_type)

        evs_function_arg_strings = [
            f"{arg_name}: {EVS_ARG_TYPES[arg_type]}" for arg_name, arg_type in zip(all_arg_names, all_arg_types)
        ]
        if evs_function_arg_strings:
            evs_function_arg_strings = ["_"] + evs_function_arg_strings  # prepend blank argument for slot intellisense

        # Record event function args in class attribute.
        self.EVENT_ARG_TYPES[self.event_id] = "".join(all_arg_types)

        return ", ".join(evs_function_arg_strings)

    def to_evs(self, enums_manager: EntityEnumsManager):
        """Convert single event script to EVS.

        If `enums` is given (e.g. via `EMEVD.to_evs()`), it should map `MapEntity` subclass names to dictionaries that
        map entity IDs to enum attributes to print in their place (e.g. `1510100: <Characters.BlackKnight2>`).

        If `enums` is given and `warn_missing_enums=True`, entity IDs that do not appear in `enums` will cause a warning
        to be logged.
        """
        function_name = _SPECIAL_EVENT_NAMES.get(self.event_id, f"Event{self.event_id}")
        function_docstring = f'""" {self.event_id}: Event {self.event_id} """'
        function_args = self.update_evs_function_args()  # starts with an empty '_' slot arg, if any other args exist
        restart_type_decorator = f"@{RestartType(self.restart_type).name}\n" if self.restart_type != 0 else ""
        function_def = self._indent_and_wrap_function_def(function_name, function_args, wrap_limit=self.WRAP_LIMIT)
        function_def += f"\n    {function_docstring}"
        evs_event_string = restart_type_decorator + function_def
        for i, instr in enumerate(self.instructions):
            instruction = instr.to_evs(self.EVENT_ARG_TYPES, enums_manager)
            if label_match := _LABEL_RE.match(instruction):
                if evs_event_string[-1] != "\n":
                    evs_event_string += "\n"
                evs_event_string += f"\n    # --- {label_match.group(1)} --- #"
            evs_event_string += self._indent_and_wrap_instruction(instruction, wrap_limit=self.WRAP_LIMIT, indent=4)
        return evs_event_string

    def to_binary(self, instruction_offset, first_base_arg_offset, first_event_arg_offset):
        if self.event_arg_count == 0:
            first_event_arg_offset = -1

        event_binary = self.HEADER_STRUCT.pack(
            event_id=self.event_id,
            instruction_count=self.instruction_count,
            first_instruction_offset=instruction_offset,
            event_arg_count=self.event_arg_count,
            first_event_arg_offset=first_event_arg_offset,
            restart_type=self.restart_type,
        )

        base_arg_offset = first_base_arg_offset

        instructions_binary = b""
        args_binary = b""
        event_args_list = []
        for instruction in self.instructions:
            instructions_binary += instruction.to_binary(base_arg_offset)

            arg_binary = instruction.args_list_to_binary()
            args_binary += arg_binary
            base_arg_offset += len(arg_binary)

            event_args_list += instruction.event_args

        # Collect and sort arg replacements to better match actual EMEVD resources. (Should be purely cosmetic.)
        sorted_event_args = sorted(event_args_list, key=lambda arg_r: (arg_r.read_from_byte, arg_r.line))
        event_args_binary = b"".join([arg_r.to_binary() for arg_r in sorted_event_args])

        return event_binary, instructions_binary, args_binary, event_args_binary

    @staticmethod
    def _indent_and_wrap_instruction(instr: str, wrap_limit=121, indent=4):
        """Indent instruction with `indent` spaces and put each argument on a separate line if the instruction exceeds
        `wrap_limit`."""
        name_indent = " " * indent
        indented_instr = f"\n{name_indent}{instr}"
        if len(indented_instr) <= wrap_limit:
            return indented_instr
        if not (match := _INSTRUCTION_RE.match(instr)):
            raise ValueError(f"Malformed instruction generated: {instr}")
        instr_name, instr_args_string = match.group(1, 2)
        if not instr_args_string:
            return indented_instr  # shouldn't happen (super-long instruction name)
        arg_indent = name_indent + "    "
        args = instr_args_string.split(", ")
        i = 0
        arg_strings = []
        while i < len(args):
            arg = args[i]
            if arg.startswith("args=("):
                # Consume additional args to reconstruct and properly indent tuple argument.
                event_args = [arg[6:]]
                i += 1
                while not (test_arg := args[i]).endswith(")"):
                    event_args.append(test_arg)
                    i += 1
                event_args.append(test_arg[:-1])  # cut off closing parenthesis
                one_line_event_args = f"args=({', '.join(event_args)}),"
                if len(arg_indent + one_line_event_args) <= wrap_limit:
                    arg_strings.append(one_line_event_args)
                else:
                    # Place each args element on a separate line, further indented.
                    arg_strings.append("args=(")
                    arg_strings += [" " * 4 + event_arg + "," for event_arg in event_args]
                    arg_strings.append("),")
            elif arg.startswith("event_layers=["):
                # Consume additional args to reconstruct event layers list (not bothering to handle multi-line).
                event_layer_indices = [arg[14:]]
                i += 1
                while not (test_arg := args[i]).endswith("]"):
                    event_layer_indices.append(test_arg)
                    i += 1
                event_layer_indices.append(test_arg[:-1])  # cut off closing bracket
                one_line_event_layers = f"event_layers=[{', '.join(event_layer_indices)}],"
                arg_strings.append(one_line_event_layers)
            elif map_match := re.match(r"(\w*map=)\((\d+)", arg):
                # Consume one additional arg to get map tuple.
                map_indices = [map_match.group(2)]
                i += 1
                while not (test_arg := args[i]).endswith(")"):
                    map_indices.append(test_arg)
                    i += 1
                map_indices.append(test_arg[:-1])  # cut off closing parenthesis
                one_line_map_tuple = f"{map_match.group(1)}({', '.join(map_indices)}),"
                arg_strings.append(one_line_map_tuple)
            else:
                arg_strings.append(arg + ",")
            i += 1

        arg_lines = "\n".join(arg_indent + arg_string for arg_string in arg_strings)
        return f"\n{name_indent}{instr_name}(\n{arg_lines}\n{name_indent})"

    @staticmethod
    def _indent_and_wrap_function_def(function_name: str, function_args, wrap_limit=121):
        one_line_def = f"def {function_name}({function_args}):"
        if len(one_line_def) <= wrap_limit:
            return one_line_def
        arg_indent = " " * 4
        arg_lines = ",\n".join(arg_indent + arg_string for arg_string in function_args.split(", "))
        return f"def {function_name}(\n{arg_lines},\n):"
