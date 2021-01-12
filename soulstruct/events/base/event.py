from __future__ import annotations

import typing as tp
from collections import OrderedDict

from soulstruct.events.base.enums import RestartType

from .instruction import Instruction

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary_struct import BinaryStruct

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


class EventArg:
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
    def unpack(cls, file, count=1):
        event_args = []
        struct_dicts = cls.HEADER_STRUCT.unpack_count(file, count=count)
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


class Event:
    HEADER_STRUCT: BinaryStruct = None
    Instruction = Instruction
    EventArg = EventArg
    EVENT_ARG_TYPES = {}  # Set before each EVS write.
    WRAP_LIMIT = 120  # PyCharm default line length.

    def __init__(self, event_id=0, restart_type=0, instructions=None):
        if self.HEADER_STRUCT is None:
            raise NotImplementedError("You cannot instantiate BaseEvent. Use a game-specific child.")
        self.event_id = event_id
        self.restart_type = restart_type
        self.instructions = instructions if instructions else []

    @classmethod
    def unpack(
        cls,
        file,
        instruction_table_offset,
        base_arg_data_offset,
        event_arg_table_offset,
        event_layers_table_offset,
        count=1,
    ):

        event_dict = OrderedDict()
        struct_dicts = cls.HEADER_STRUCT.unpack_count(file, count=count)

        for d in struct_dicts:
            file.seek(instruction_table_offset + d["first_instruction_offset"])
            instruction_list = cls.Instruction.unpack(
                file, base_arg_data_offset, event_layers_table_offset, count=d["instruction_count"]
            )

            file.seek(event_arg_table_offset + d["first_event_arg_offset"])
            event_args = cls.EventArg.unpack(file, count=d["event_arg_count"])

            for arg_r in event_args:
                # Attach event arg replacements to their instruction line.
                instruction_list[arg_r.line].event_args.append(arg_r)

            event_dict[d["event_id"]] = cls(d["event_id"], d["restart_type"], instruction_list)

        return event_dict

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

    def guess_parameter_types(self):
        event_arg_set = set()
        event_arg_types = {}
        for instruction in self.instructions:
            try:
                instruction_arg_set, instruction_arg_types = instruction.apply_event_args()
            except ValueError:
                raise ValueError(
                    f"Error occurred while applying event args in instruction "
                    f"{self.instructions.index(instruction)} of event {self.event_id}."
                )
            event_arg_set = event_arg_set.union(instruction_arg_set)
            for arg, arg_types in instruction_arg_types.items():
                event_arg_types[arg] = event_arg_types.setdefault(arg, set()).union(arg_types)
        return list(sorted(event_arg_set)), event_arg_types

    def get_evs_function_args(self):
        # TODO: 'next(iter(set))' is a hack to get a random type hint, in case multiple types are suggested.
        #  Usually the set will only have one element in it.
        sorted_parameter_list, event_arg_types = self.guess_parameter_types()
        evs_function_args_names = [f"arg_{i}_{j}" for i, j in sorted_parameter_list]
        evs_function_args_types = [EVS_ARG_TYPES[next(iter(event_arg_types[arg]))] for arg in evs_function_args_names]
        evs_function_args = [
            f"{arg_name}: {arg_type}" for arg_name, arg_type in zip(evs_function_args_names, evs_function_args_types)
        ]
        if evs_function_args:
            evs_function_args = ["_"] + evs_function_args  # add blank argument for slot (for intellisense)
        self.EVENT_ARG_TYPES[self.event_id] = "".join(
            [next(iter(event_arg_types[arg])) for arg in evs_function_args_names]
        )
        return ", ".join(evs_function_args)

    def to_evs(self, game_module):
        if self.event_id == 0:
            function_name = "Constructor"
        elif self.event_id == 50:
            function_name = "Preconstructor"
        else:
            function_name = f"Event{self.event_id}"
        function_docstring = f'""" {self.event_id}: Event {self.event_id} """'
        function_args = self.get_evs_function_args()  # Starts with an empty '_' slot arg, if any other args exist.
        restart_type_decorator = f"@{RestartType(self.restart_type).name}\n" if self.restart_type != 0 else ""
        function_def = indent_and_wrap_function_def(function_name, function_args, wrap_limit=self.WRAP_LIMIT)
        function_def += f"\n    {function_docstring}"
        evs_event_string = restart_type_decorator + function_def
        for i, instr in enumerate(self.instructions):
            instruction = instr.to_evs(game_module, self.EVENT_ARG_TYPES)
            if instruction.startswith("DefineLabel("):
                label = instruction.split(")")[0][len("DefineLabel(") :]
            else:
                label = None
            if label is not None:
                if evs_event_string[-1] != "\n":
                    evs_event_string += "\n"
                evs_event_string += f"\n    # --- {label} --- #"
            evs_event_string += indent_and_wrap_instruction(instruction, wrap_limit=self.WRAP_LIMIT, indent=4)
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


def indent_and_wrap_instruction(instr: str, wrap_limit=120, indent=4):
    """Indent instruction and wrap its arguments if the instruction exceed the given wrap limit."""
    instr = " " * indent + instr
    if len(instr) <= wrap_limit:
        return "\n" + instr
    instr_def = instr.split("(")[0] + "("
    def_length = len(instr_def)
    max_arg_length = wrap_limit - def_length
    args = list(reversed(instr[def_length:-1].split(" ")))
    arg_lines = []
    arg_line = ""
    while args:
        arg = args.pop()
        arg += " " if args else ")"
        if len(arg_line + arg) <= max_arg_length:
            arg_line += arg
        else:
            arg_lines.append(arg_line)
            arg_line = arg
    if arg_line:
        arg_lines.append(arg_line)
    instr = "\n" + instr_def + arg_lines[0]
    for arg_line in arg_lines[1:]:
        instr += "\n" + " " * def_length + arg_line
    return instr


def indent_and_wrap_function_def(function_name, function_args, wrap_limit=120):
    function_name = f"def {function_name}("
    if len(function_name) + len(function_args) + 2 <= wrap_limit:
        return function_name + f"{function_args}):"
    def_length = len(function_name)
    max_arg_length = wrap_limit - def_length
    args = list(reversed([arg.strip(" ):") for arg in function_args.split(",")]))
    arg_lines = []
    arg_line = ""
    while args:
        arg = args.pop()
        arg += ", " if args else "):"
        if len(arg_line + arg) <= max_arg_length:
            arg_line += arg
        else:
            arg_lines.append(arg_line)
            arg_line = arg
    if arg_line:
        arg_lines.append(arg_line)
    function = function_name + arg_lines[0]
    for arg_line in arg_lines[1:]:
        function += "\n" + " " * def_length + arg_line
    return function
