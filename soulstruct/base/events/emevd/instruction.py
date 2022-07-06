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
    from .entity_enums_manager import EntityEnumsManager
    from .event import EventArg

_LOGGER = logging.getLogger(__name__)


class Instruction(abc.ABC):

    event_args: list[EventArg]
    event_layers: tp.Optional[EventLayers]

    EventLayers: tp.Type[EventLayers] = None
    HEADER_STRUCT: BinaryStruct = None

    EMEDF: dict[tuple[int, int], dict]
    DECOMPILER: dict[tuple[int, int], tp.Callable]
    OPT_ARGS_DECOMPILER: dict[tuple[int, int], tp.Callable]
    DECOMPILE: tp.Callable

    def __init__(self, category, index, display_arg_types="", args_list=(), event_layers=None):
        self.category = category
        self.index = index
        self.display_arg_types = display_arg_types

        if len(self.struct_arg_types) != len(args_list):
            raise ValueError(
                f"Length of argument list ({len(args_list)}) in instruction {self.instruction_id} does not match "
                f"length of format string '{display_arg_types}' ({len(self.struct_arg_types)})."
            )

        self.args_list = args_list if args_list else []
        self.event_args = []  # added after construction
        self.evs_args_list = []  # e.g. `[0, 1000800, 'arg_0_3', 5.0]`
        if isinstance(event_layers, (list, tuple)):
            self.event_layers = self.EventLayers(event_layers)
        elif isinstance(event_layers, self.EventLayers):
            self.event_layers = event_layers
        else:
            self.event_layers = None
        self.event_layers_offset = None  # Set by Event class during EMEVD packing.

    @property
    def instruction_id(self) -> str:
        return f"{self.category}[{self.index:02d}]"

    @property
    def struct_arg_types(self):
        """Used for actually packing/unpacking event argument data.

        Note that "0i" is added to end by the caller if needed for converting packed data aligned to four bytes.
        """
        return self.display_arg_types.replace("s", "I").replace("|", "")

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
                    d["category"],
                    d["index"],
                    base_arg_data_offset + d["first_base_arg_offset"],
                    d["base_args_size"],
                    cls.EMEDF,
                )
            except KeyError:
                args_size = struct_dicts[i + 1]["first_base_arg_offset"] - d["first_base_arg_offset"]
                reader.seek(base_arg_data_offset + d["first_base_arg_offset"])
                raw_data = reader.read(args_size)
                _LOGGER.error(f"Error while processing instruction arguments. Raw arg data: {raw_data}")
                raise

            # Process event layers.
            if d["first_event_layers_offset"] > 0:
                event_layers = cls.EventLayers.unpack(
                    reader, event_layers_table_offset + d["first_event_layers_offset"]
                )
            else:
                event_layers = None

            instructions.append(
                cls(d["category"], d["index"], args_format, args_list, event_layers)
            )

        return instructions

    @property
    def args_size(self):
        return struct.calcsize(f"@{self.struct_arg_types}0i")

    @property
    def event_arg_count(self):
        return len(self.event_args)

    def get_called_event(self) -> tp.Optional[int]:
        """Returns called event ID if instruction is `RunEvent` or `RunCommonEvent`. Returns `None` otherwise."""
        if self.category == 2000:
            if self.index == 0:
                return self.args_list[1]
            elif self.index == 6:  # no `slot` argument
                return self.args_list[0]
        return None

    def to_numeric(self):
        numeric = [
            f"{self.category: 5d}[{self.index:02d}] "
            f"({self.display_arg_types})" + repr(self.args_list)
        ]
        if self.event_layers:
            numeric[-1] += self.event_layers.to_numeric()
        for replacement in self.event_args:
            numeric.append("    ^" + replacement.to_numeric())
        return numeric

    def to_evs(self, event_arg_types, enums_manager: EntityEnumsManager = None) -> str:
        """Convert single event instruction to EVS."""
        args, opt_args = self.get_required_and_optional_args()

        if (called_event_id := self.get_called_event()) is not None and opt_args and called_event_id in event_arg_types:
            opt_arg_types = event_arg_types[called_event_id]
        else:
            opt_arg_types = ""

        try:
            instruction = self.DECOMPILE(
                self.category, self.index, args, opt_args, opt_arg_types, enums_manager=enums_manager
            )
        except Exception as ex:
            raise ValueError(
                f"Error while decompiling instruction ({self.category}, {self.index}):\n"
                f"  {ex}\n"
                f"  args = {self.evs_args_list}"
            )
        if self.event_layers:
            if instruction[-2:] == "()":
                instruction = instruction[:-1] + self.event_layers.to_evs() + ")"
            else:
                instruction = instruction[:-1] + ", " + self.event_layers.to_evs() + ")"  # with comma
        return instruction

    def get_required_and_optional_args(self) -> tuple[list[str], list[str]]:
        separator_index = self.display_arg_types.find("|")
        if separator_index == -1:
            required_args = self.evs_args_list
            optional_args = []
        else:
            required_args = self.evs_args_list[:separator_index]
            optional_args = self.evs_args_list[separator_index:]
        return required_args, optional_args

    def process_event_args(self) -> dict[tuple[int, int], tuple[set[str], set[str]]]:
        """Inserts arg replacements into the appropriate places in their instructions for readability.

        By default, the arg replacements are represented as "arg_i_j", where i and j specify the start and end
        (exclusive) of the byte range read from the arguments passed to the `RunEvent` instruction. The `Event` class
        may replace these default names with more useful argument names, detected from the corresponding argument names
        across the full set of instructions in the event that actually use them.

        Returns a dictionary mapping start-stop bytes for reading the arg `(i, j)` to two sets:
            - a set of format characters (e.g, `"i"`, "f"`) determined from the instruction's known arg format. The set
            values in this dictionary will generally only contain one format string, unless the event argument is used
            for inconsistently-sized fields within the same instruction.
            - a set of argument names taken from the instructions in `EMEDF`, which are used to generate a more useful
            name for the event arg than the default 'arg_i_j'. Again, this will only contain multiple names if the same
            event argument is used for multiple arguments within the same instruction, which would be very unusual.
        """

        permitted = [0, 0.0, -1, 1, 10]  # NOTE: Strings are permitted to overwrite anything.
        arg_offset_dict = get_byte_offset_from_struct(self.display_arg_types)

        instruction_arg_types_names = {}

        self.evs_args_list = self.args_list.copy()

        for arg_r in self.event_args:
            try:
                argument_index, argument_byte_type = arg_offset_dict[arg_r.write_from_byte]
            except KeyError:
                raise ValueError(
                    f"No argument in '{self.event_args}' begins at byte {arg_r.write_from_byte}. "
                    f"Your replacement commands are probably misaligned. Arg offset dict: {arg_offset_dict}"
                )

            # Byte type "s" is actually a four-byte offset into the packed strings.
            if (
                not (argument_byte_type == "s" and arg_r.bytes_to_write == 4)
                and struct.calcsize(argument_byte_type) < arg_r.bytes_to_write
            ):
                raise ValueError(
                    f"You cannot write event argument with size {arg_r.bytes_to_write} bytes over an argument of type "
                    f"{argument_byte_type} (it's too small).\n"
                    f"    Instruction: {self.instruction_id}\n"
                    f"    Event arg: {arg_r}"
                )

            value_to_overwrite = self.args_list[argument_index]
            evs_arg_name = list(self.EMEDF[self.category, self.index]["args"])[argument_index]
            if evs_arg_name == "slot":
                # Not permitted as an event argument (conflicts with `RunEvent` slot).
                evs_arg_name = "event_slot"
            default_arg_name = f"arg_{arg_r.read_from_byte}_{arg_r.read_from_byte + arg_r.bytes_to_write - 1}"

            if value_to_overwrite not in permitted and argument_byte_type != "s":
                _LOGGER.error(
                    f"Event argument '{default_arg_name}' ({evs_arg_name}) is overwriting non-zero value "
                    f"{value_to_overwrite} (position {argument_index}) in instruction {self.category}[{self.index}] "
                    f"with args {self.args_list} (types '{self.display_arg_types}')"
                )
                # raise ValueError(
                #     f"Parameter {arg_name} is overwriting non-zero value {value_to_overwrite} "
                #     f"(position {argument_index})."
                # )

            self.evs_args_list[argument_index] = default_arg_name  # will generally be replaced with an EVS name later

            arg_range = (arg_r.read_from_byte, arg_r.read_from_byte + arg_r.bytes_to_write - 1)

            if arg_range not in instruction_arg_types_names:
                instruction_arg_types_names[arg_range] = (set(), set())
            instruction_arg_types_names[arg_range][0].add(argument_byte_type)
            instruction_arg_types_names[arg_range][1].add(evs_arg_name)

        return {arg_range: instruction_arg_types_names[arg_range] for arg_range in sorted(instruction_arg_types_names)}

    def args_list_to_binary(self):
        if self.args_list:
            return struct.pack(f"@{self.struct_arg_types}0i", *self.args_list)
        else:
            return b""

    def event_event_args_to_binary(self):
        return b"".join([arg_replacement.to_binary() for arg_replacement in self.event_args])

    def to_binary(self, first_base_arg_offset):
        """Note that instruction category 1014 (DefineLabel) does not use `first_base_arg_offset`."""
        if self.event_layers_offset is None:
            raise ValueError("Instruction event layer offset not set. (Only use EMEVD.pack() to pack events.)")
        struct_dict = {
            "category": self.category,
            "index": self.index,
            "base_args_size": self.args_size,
            "first_base_arg_offset": first_base_arg_offset if self.category != 1014 else -1,
            "first_event_layers_offset": self.event_layers_offset,
        }
        return self.HEADER_STRUCT.pack(struct_dict)

    def __repr__(self) -> str:
        text = (
            f"Instruction({self.category}, {self.index}, "
            f"display_arg_types=\"{self.display_arg_types}\", args={self.args_list})"
        )
        if self.event_layers is not None:
            text = text[:-1] + f", event_layers={self.event_layers})"
        return text
