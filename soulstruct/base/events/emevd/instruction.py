from __future__ import annotations

__all__ = ["Instruction", "EventArg"]

import abc
import logging
import struct
import typing as tp

from .event_layers import EventLayers
from .utils import get_byte_offset_from_struct, get_instruction_args

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryStruct, BinaryReader
    from .entity_enums_manager import EntityEnumsManager

_LOGGER = logging.getLogger(__name__)


class EventArg(abc.ABC):
    DEFAULT_ARG_SIZE_TYPE = {1: "B", 2: "H", 4: "I"}
    HEADER_STRUCT: BinaryStruct = None

    names: set[str]
    fmts: set[str]  # format characters such as 'i', 'B', 'H'
    py_types: set[type]  # EMEDF game types or unions such as `Flag`, `int`, `CharacterTyping`

    def __init__(self, instruction_line, write_from_byte=0, read_from_byte=0, bytes_to_write=0, unknown=0):
        """Overrides argument data in a particular instruction using from dynamic args attached to the event."""
        self.line = instruction_line
        self.write_from_byte = write_from_byte
        self.read_from_byte = read_from_byte
        self.bytes_to_write = bytes_to_write
        self.unknown = unknown

        self.names = set()
        self.fmts = set()
        self.py_types = set()

    @classmethod
    def unpack(cls, reader: BinaryReader, count=1):
        event_args = []
        struct_dicts = reader.unpack_structs(cls.HEADER_STRUCT, count=count)
        for d in struct_dicts:
            event_args.append(cls(**d))
        return event_args

    @property
    def arg_range(self) -> tuple[int, int]:
        return self.read_from_byte, self.read_from_byte + self.bytes_to_write - 1

    @classmethod
    def generic(cls, arg_range: tuple[int, int]):
        """Return an `EventArg` that only contains information needed for EVS decompilation, not EMEVD packing."""
        return cls(0, 0, arg_range[0], arg_range[1] - arg_range[0], 0)

    def to_numeric(self):
        # TODO: Should include `unknown`, since (as of Elden Ring?) it is not always zero.
        return f"({self.write_from_byte} <- {self.read_from_byte}, {self.bytes_to_write})"

    def to_binary(self):
        return self.HEADER_STRUCT.pack(
            instruction_line=self.line,
            write_from_byte=self.write_from_byte,
            read_from_byte=self.read_from_byte,
            bytes_to_write=self.bytes_to_write,
            unknown=self.unknown,
        )

    def add_info(self, other: EventArg):
        """Merge in name, fmt, and py_type sets."""
        self.names |= other.names
        self.fmts |= other.fmts
        self.py_types |= other.py_types

    def remove_generic_names(self):
        # Remove non-preferred arg names.
        # TODO: Should check 'classes' of names, so 'character__flag' doesn't just become 'character', etc.
        for vague_arg_name in (
            "entity", "other_entity", "target_entity", "owner_entity", "anchor_entity", "attacked_entity",
            "destination", "source_entity", "copy_draw_parent", "line_intersects", "flag", "left", "right",
            "model_point",
        ):
            if len(self.names) >= 2 and vague_arg_name in self.names:
                self.names.remove(vague_arg_name)

    def get_combined_arg_name(self, existing_arg_names: tp.Iterable[str]):
        try_arg_name = "__".join(sorted(self.names))

        # Add suffix to distinguish duplicate event arg names.
        if try_arg_name in existing_arg_names:
            arg_duplicate_index = 1
            arg_name = try_arg_name + f"_{arg_duplicate_index}"
            while arg_name in existing_arg_names:
                arg_duplicate_index += 1
                arg_name = try_arg_name + f"_{arg_duplicate_index}"
        else:
            arg_name = try_arg_name
        return arg_name

    def get_combined_fmt(self, event_id: int | str = "unknown", arg_name: str = "unknown") -> str:
        if len(self.fmts) > 1:
            # Multiple detected types. Acceptable (using default integer type) only if they all the same size.
            sizes = {struct.calcsize(fmt) for fmt in self.fmts}
            if len(sizes) == 1:
                arg_size = next(iter(sizes))
                fmt = self.DEFAULT_ARG_SIZE_TYPE[arg_size]
                _LOGGER.warning(
                    f"Detected multiple types for event arg '{fmt}' in event {event_id}: {self.fmts}. "
                    f"Using default type '{fmt}' for this arg size ({arg_size})."
                )
                return fmt
            else:
                raise ValueError(
                    f"Detected multiple types for event arg '{arg_name}' in event {event_id}: {self.fmts}. "
                    f"They have incompatible sizes, which is not permitted."
                )
        else:
            return next(iter(self.fmts))

    def get_combined_py_types(self) -> tuple[tp.Type, ...]:
        """Returns a tuple of types for checking by breaking up Union objects."""
        all_py_types = []
        for py_type in self.py_types:
            try:
                origin = tp.get_origin(py_type)
            except AttributeError:
                all_py_types.append(py_type)  # implies `py_type` is a real Python type
            else:
                union_types = tp.get_args(py_type) if origin is tp.Union else ()
                for union_type in union_types:
                    if union_type not in all_py_types:
                        all_py_types.append(union_type)
        return tuple(all_py_types)

    def get_combined_info(
        self, existing_arg_names: tp.Iterable[str], event_id: int
    ) -> tuple[str, str, tuple[tp.Type, ...]]:
        arg_name = self.get_combined_arg_name(existing_arg_names)
        fmt = self.get_combined_fmt(event_id, arg_name)
        py_types = self.get_combined_py_types()

        return arg_name, fmt, py_types

    def __repr__(self) -> str:
        if self.unknown == 0:
            return (
                f"EventArg(line={self.line}, write_from_bytes={self.write_from_byte}, "
                f"read_from_byte={self.read_from_byte}, bytes_to_write={self.bytes_to_write})"
            )
        return (
            f"EventArg(line={self.line}, write_from_bytes={self.write_from_byte}, "
            f"read_from_byte={self.read_from_byte}, bytes_to_write={self.bytes_to_write}, unknown={self.unknown})"
        )


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

    def to_evs(self, enums_manager: EntityEnumsManager, all_event_arg_fmts: dict[int, str]) -> str:
        """Convert single event instruction to EVS."""
        args, opt_args = self.get_required_and_optional_args()

        if (
            (called_event_id := self.get_called_event()) is not None
            and opt_args and called_event_id in all_event_arg_fmts
        ):
            opt_arg_types = all_event_arg_fmts[called_event_id]
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

    def process_event_args(self):
        """Adds name, fmt, and Python type information to `EventArg` replacements in this instruction.

        Also builds `evs_args_list`, using `arg_i_j` names for event arguments. These default names may be overwritten
        later based on how ALL the different Instructions in the same event use them.
        """

        # Elden Ring overwrites value 10000 a lot.
        # TODO: More systematic. Really, instruction args should only be able to override their own `internal_default`.
        permitted = [0, 0.0, -1, 2 ** 32 - 1, 1, 10, 10000]  # NOTE: Strings are permitted to overwrite anything.
        arg_offset_dict = get_byte_offset_from_struct(self.display_arg_types)

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

            arg_info = self.EMEDF[self.category, self.index]["args"][evs_arg_name]
            arg_py_type = arg_info["type"]

            if value_to_overwrite not in permitted and argument_byte_type != "s":
                if value_to_overwrite != arg_info.get("internal_default", None):
                    _LOGGER.error(
                        f"Event argument '{default_arg_name}' ({evs_arg_name}) is overwriting unusual default value "
                        f"{value_to_overwrite} (position {argument_index}) in instruction {self.instruction_id} "
                        f"with args {self.args_list} (types '{self.display_arg_types}')"
                    )

            self.evs_args_list[argument_index] = default_arg_name  # will generally be replaced with an EVS name later
            arg_r.names.add(evs_arg_name)
            arg_r.fmts.add(argument_byte_type)
            arg_r.py_types.add(arg_py_type)

        # Sort event args by arg range.
        self.event_args = sorted(self.event_args, key=lambda x: x.arg_range)

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
