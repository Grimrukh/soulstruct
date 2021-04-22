from __future__ import annotations

__all__ = ["Instruction"]

import abc
import logging
import struct
import typing as tp

from .event_layers import EventLayers
from .utils import get_byte_offset_from_struct, get_instruction_args

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryStruct, BinaryReader
    from .decompiler import InstructionDecompiler

_LOGGER = logging.getLogger(__name__)


class Instruction(abc.ABC):
    DECOMPILER: InstructionDecompiler = None
    INSTRUCTION_ARG_TYPES = {}
    EventLayers: tp.Type[EventLayers] = None
    HEADER_STRUCT: BinaryStruct = None

    def __init__(self, instruction_class, instruction_index, args_format="", args_list=None, event_layers=None):
        if len(args_format.replace("|", "")) != len(args_list):
            raise ValueError(
                f"Length of argument list ({len(args_list)}) in Instruction {instruction_class}"
                f"[{instruction_index}] does not match length of format string '{args_format}' "
                f"({len(args_format.replace('|', ''))})."
            )
        self.instruction_class = instruction_class
        self.instruction_index = instruction_index
        self.visible_args_format = args_format  # preserves 's' for printing output
        self.args_format = args_format.replace("s", "I")
        self.args_list = args_list if args_list else []
        self.event_args = []  # Added after construction.
        self.verbose_args_list = []  # So we don't modify 'args_list'.
        if isinstance(event_layers, (list, tuple)):
            self.event_layers = self.EventLayers(event_layers)
        elif isinstance(event_layers, self.EventLayers):
            self.event_layers = event_layers
        else:
            self.event_layers = None
        self.event_layers_offset = None  # Set by Event class during EMEVD packing.

    @classmethod
    def unpack(cls, reader: BinaryReader, base_arg_data_offset, event_layers_table_offset, count=1):
        """Unpack some number of Instructions into a list, starting from the current file offset."""

        instructions = []
        struct_dicts = reader.unpack_structs(cls.HEADER_STRUCT, count=count)
        for i, d in enumerate(struct_dicts):

            # Process arguments.
            try:
                args_format, args_list = get_instruction_args(
                    reader,
                    d["instruction_class"],
                    d["instruction_index"],
                    base_arg_data_offset + d["first_base_arg_offset"],
                    d["base_args_size"],
                    cls.INSTRUCTION_ARG_TYPES,
                )
            except KeyError:
                args_size = struct_dicts[i + 1]["first_base_arg_offset"] - d["first_base_arg_offset"]
                reader.seek(base_arg_data_offset + d["first_base_arg_offset"])
                raw_data = reader.read(args_size)
                _LOGGER.error(f"Error while processing instruction arguments. Raw arg data: {raw_data}")
                raise

            # Process event layers.
            if d["first_event_layers_offset"] > 0:
                event_layers = cls.EventLayers.unpack(reader, event_layers_table_offset + d["first_event_layers_offset"])
            else:
                event_layers = None

            instructions.append(
                cls(d["instruction_class"], d["instruction_index"], args_format, args_list, event_layers)
            )

        return instructions

    @property
    def args_size(self):
        return struct.calcsize("@" + self.args_format.replace("|", "") + "0i")

    @property
    def event_arg_count(self):
        return len(self.event_args)

    def to_numeric(self):
        numeric = [
            f"{self.instruction_class: 5d}[{self.instruction_index:02d}] "
            f"({self.visible_args_format})" + repr(self.args_list)
        ]
        if self.event_layers:
            numeric[-1] += self.event_layers.to_numeric()
        for replacement in self.event_args:
            numeric.append("    ^" + replacement.to_numeric())
        return numeric

    def to_evs(self, event_arg_types):
        args, opt_args = self.get_required_and_optional_args()
        opt_arg_types = None
        if (
            self.instruction_class == 2000
            and self.instruction_index == 0
            and opt_args
            and args[1] in event_arg_types
        ):
            opt_arg_types = event_arg_types[args[1]]
        instruction = self.DECOMPILER.decompile(
            self.instruction_class, self.instruction_index, args, opt_args, opt_arg_types
        )
        if self.event_layers:
            instruction = instruction[:-1] + self.event_layers.to_evs()
        return instruction

    def get_required_and_optional_args(self):
        split_point = self.visible_args_format.find("|")
        if split_point == -1:
            required_args = self.verbose_args_list
            optional_args = []
        else:
            required_args = self.verbose_args_list[:split_point]
            optional_args = self.verbose_args_list[split_point:]
        return required_args, optional_args

    def apply_event_args(self):
        """ Inserts arg replacements into the appropriate places in their instructions for readability (verbose
        output only). The arg replacements are represented as 'Xi:j', where i and j specify the byte range read
        from the arguments passed to the RunEvent instruction.

        Also returns a dictionary that allows the RunEvent instruction to guess the format of its arguments,
        based on how they are actually used in the event instructions.
        """

        permitted = [0, 0.0, -1, 1, 10]  # Strings are permitted to overwrite anything.
        arg_offset_dict = get_byte_offset_from_struct("@" + self.visible_args_format.replace("|", ""))

        instruction_arg_set = set()
        instruction_arg_types = {}

        self.verbose_args_list = self.args_list.copy()

        for arg_r in self.event_args:
            try:
                argument_index, argument_byte_type = arg_offset_dict[arg_r.write_from_byte]
            except KeyError:
                raise ValueError(
                    f"No argument in '{self.event_args}' begins at byte {arg_r.write_from_byte}. "
                    f"Your replacement commands are misaligned."
                )

            if (
                not (argument_byte_type == "s" and arg_r.bytes_to_write == 4)
                and struct.calcsize(argument_byte_type) < arg_r.bytes_to_write
            ):
                # Byte type 's' is actually a four-byte offset into the packed strings.
                raise ValueError(
                    f"You cannot write {arg_r.bytes_to_write} bytes over an argument of type "
                    f"{argument_byte_type} (it's too small)."
                )
            value_to_overwrite = self.args_list[argument_index]
            arg_name = f"arg_{arg_r.read_from_byte}_{arg_r.read_from_byte + arg_r.bytes_to_write - 1}"

            if value_to_overwrite not in permitted and value_to_overwrite != arg_name and argument_byte_type != "s":
                _LOGGER.error(
                    f"Parameter {arg_name} is overwriting non-zero value {value_to_overwrite} "
                    f"(position {argument_index}) in instruction {self.instruction_class}[{self.instruction_index}] "
                    f"with args {self.args_list} (format {self.args_format})"
                )
                raise ValueError(
                    f"Parameter {arg_name} is overwriting non-zero value {value_to_overwrite} "
                    f"(position {argument_index})."
                )

            self.verbose_args_list[argument_index] = arg_name

            instruction_arg_set.add((arg_r.read_from_byte, arg_r.read_from_byte + arg_r.bytes_to_write - 1))
            if arg_name not in instruction_arg_types:
                instruction_arg_types[arg_name] = set(argument_byte_type)
            else:
                instruction_arg_types[arg_name].add(argument_byte_type)

        return instruction_arg_set, instruction_arg_types

    def args_list_to_binary(self):
        if self.args_list:
            format_string = "@" + self.args_format.replace("|", "") + "0i"
            return struct.pack(format_string, *self.args_list)
        else:
            return b""

    def event_event_args_to_binary(self):
        return b"".join([arg_replacement.to_binary() for arg_replacement in self.event_args])

    def to_binary(self, first_base_arg_offset):
        if self.event_layers_offset is None:
            raise ValueError("Instruction event layer offset not set. (Only use EMEVD.pack() to pack events.)")
        struct_dict = {
            "instruction_class": self.instruction_class,
            "instruction_index": self.instruction_index,
            "base_args_size": self.args_size,
            "first_base_arg_offset": first_base_arg_offset,
            "first_event_layers_offset": self.event_layers_offset,
        }
        return self.HEADER_STRUCT.pack(struct_dict)
