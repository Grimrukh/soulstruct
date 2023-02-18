from __future__ import annotations

__all__ = ["Instruction", "EventArg"]

import abc
import logging
import struct
import typing as tp
from dataclasses import dataclass, field
from types import GenericAlias

from soulstruct.utilities.binary import *

from .event_layers import EventLayers
from .utils import get_byte_offset_from_struct, get_instruction_args

if tp.TYPE_CHECKING:
    from .entity_enums_manager import GameEnumsManager
    from .event import EventSignature

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class EventArgStruct(BinaryStruct):
    """Supports all games."""
    instruction_line: varuint
    write_from_byte: varuint
    read_from_byte: varuint
    bytes_to_write: int  # does NOT have variable size
    unknown: int


# TODO: rename `EventArgReplacement` to distinguish from actual arguments (with multiple possible replacements).
@dataclass(slots=True)
class EventArg:
    """Overrides argument data in a particular instruction using from dynamic args attached to the event.

    Supports all games.
    """
    instruction_line: int
    write_from_byte: int = 0
    read_from_byte: int = 0
    bytes_to_write: int = 0
    unknown: int = 0

    # These are assigned later, from the `Instruction` that uses the replacement, then combined after that into
    # `SingleEventArg` instances for the `Event`.
    arg_index: int = -1
    name: str = ""
    fmt: str = ""  # format characters such as 'i', 'B', 'H'
    py_type_hint: tp.Type | GenericAlias = None  # EMEDF game types or `typing.Union` hints

    @classmethod
    def from_emevd_reader(cls, reader: BinaryReader) -> EventArg:
        return EventArgStruct.reader_to_object(reader, cls)

    @property
    def arg_range(self) -> tuple[int, int]:
        return self.read_from_byte, self.read_from_byte + self.bytes_to_write - 1

    def to_numeric(self):
        # TODO: Should include `unknown`, since (as of Elden Ring?) it is not always zero.
        return f"({self.write_from_byte} <- {self.read_from_byte}, {self.bytes_to_write})"

    def to_emevd_writer(self, writer: BinaryWriter):
        """Simple write; all data should be present."""
        return EventArgStruct.object_to_writer(self, writer)

    def __repr__(self) -> str:
        if self.unknown == 0:
            return (
                f"EventArg(line={self.instruction_line}, write_from_bytes={self.write_from_byte}, "
                f"read_from_byte={self.read_from_byte}, bytes_to_write={self.bytes_to_write})"
            )
        return (
            f"EventArg(line={self.instruction_line}, write_from_bytes={self.write_from_byte}, "
            f"read_from_byte={self.read_from_byte}, bytes_to_write={self.bytes_to_write}, unknown={self.unknown})"
        )


@dataclass(slots=True)
class InstructionStruct(BinaryStruct):
    """Supports all games."""
    category: uint
    index: uint
    base_args_size: varuint
    base_args_local_offset: varint
    event_layers_local_offset: varint
    # Pad 4 (or maybe align to 8) for 32-bit classes.


@dataclass(slots=True)
class Instruction(abc.ABC):

    # EMEVD 'environment' class attributes that must be set by game-specific subclasses.
    EMEDF: tp.ClassVar[dict[tuple[int, int], dict]]
    DECOMPILER: tp.ClassVar[dict[tuple[int, int], tp.Callable]]
    OPT_ARGS_DECOMPILER: tp.ClassVar[dict[tuple[int, int], tp.Callable]]
    DECOMPILE: tp.ClassVar[tp.Callable]

    category: int
    index: int
    display_args_fmt: str = ""

    # `EventArg` replacements, which specify offsets used to determine which part of the packed `Event` arguments they
    # read from and which index in `args_list` they replace. Order does not matter.
    # TODO: sort immediately when added?
    event_arg_replacements: list[EventArg] = field(default_factory=list)
    # Actual Python values of instruction arguments, unpacked directly from the `EMEVD` file. Includes 'dummy' values
    # waiting to be replaced in-game by an `EventArg` from above.
    args_list: list[tp.Any] = field(default_factory=list)
    # Processed version of `args_list` where the 'dummy' values overwritten by an `EventArg` are replaced with unique
    # arg string names ('arg_i_j' by default for `EventArg` reading from `Event` packed arg range `(i, j)`.
    evs_args_list: list[tp.Any] = field(default_factory=list)
    # Universal add-on data for instructions used by some later games. Instructions with event layers will only run if
    # the game currently considers those layers active.
    event_layers: EventLayers | None = None

    def __post_init__(self):
        if len(self.struct_args_fmt) != len(self.args_list):
            raise ValueError(
                f"Length of argument list ({len(self.args_list)}) in instruction {self.instruction_id} does not match "
                f"length of format string '{self.display_args_fmt}' ({len(self.struct_args_fmt)})."
            )

    @property
    def instruction_id(self) -> str:
        return f"{self.category}[{self.index:02d}]"

    @property
    def struct_args_fmt(self) -> str:
        """Used for actually packing/unpacking event argument data.

        Note that "0i" is added to end by the caller if needed for converting packed data aligned to four bytes.
        """
        return self.display_args_fmt.replace("s", "I").replace("|", "")

    @classmethod
    def from_emevd_reader(cls, reader: BinaryReader, base_arg_data_offset: int, event_layers_offset: int):

        header = InstructionStruct.from_bytes(reader)
        if not reader.long_varints:
            reader.assert_pad(4)  # TODO: alignment would be nicer?

        # Process arguments.
        try:
            args_format, args_list = get_instruction_args(
                reader,
                header.category,
                header.index,
                base_arg_data_offset + header.base_args_local_offset,
                header.base_args_size,
                cls.EMEDF,
            )
        except KeyError:
            # args_size = struct_dicts[i + 1]["first_base_arg_offset"] - d["first_base_arg_offset"]
            # reader.seek(base_arg_data_offset + d["first_base_arg_offset"])
            # raw_data = reader.read(args_size)
            _LOGGER.error(f"Error while processing instruction arguments.")
            raise

        # Process event layers.
        if header.event_layers_local_offset > 0:
            with reader.temp_offset(event_layers_offset + header.event_layers_local_offset):
                event_layers = EventLayers.from_emevd_reader(reader)
        else:
            event_layers = None

        return cls(
            category=header.category,
            index=header.index,
            display_args_fmt=args_format,
            event_arg_replacements=[],  # added later
            args_list=args_list,
            event_layers=event_layers,
        )

    @property
    def base_args_size(self):
        """Calculate size of instruction arguments (aligned to 4 with '0i' suffix)."""
        return struct.calcsize(f"@{self.struct_args_fmt}0i")

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
            f"({self.display_args_fmt})" + repr(self.args_list)
        ]
        if self.event_layers:
            numeric[-1] += self.event_layers.to_numeric()
        for replacement in self.event_arg_replacements:
            numeric.append("    ^" + replacement.to_numeric())
        return numeric

    def to_evs(self, enums_manager: GameEnumsManager, event_signatures: dict[int, EventSignature]) -> str:
        """Convert single event instruction to EVS."""
        args, opt_args = self.get_required_and_optional_args()

        if (
            (called_event_id := self.get_called_event()) is not None
            and opt_args and called_event_id in event_signatures
        ):
            opt_arg_types = event_signatures[called_event_id].get_full_fmt()
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
        separator_index = self.display_args_fmt.find("|")
        if separator_index == -1:
            required_args = self.evs_args_list
            optional_args = []
        else:
            required_args = self.evs_args_list[:separator_index]
            optional_args = self.evs_args_list[separator_index:]
        return required_args, optional_args

    def process_event_arg_replacements(self):
        """Adds name, fmt, and Python type information to `EventArg` replacements in this instruction.

        Also builds `evs_args_list`, using `arg_i_j` names for event arguments. These default names may be overwritten
        later based on how ALL the different Instructions in the same event use them.

        SIDE EFFECTS:
            Sorts `self.event_args` by arg range (original order is often random).
            Regenerates `self.evs_args_list`.
        """

        # Elden Ring overwrites value 10000 a lot.
        # TODO: More systematic. Really, instruction args should only be able to override their own `internal_default`.
        permitted = [0, 0.0, -1, 2 ** 32 - 1, 1, 10, 10000]  # NOTE: Strings are permitted to overwrite anything.
        arg_offset_dict = get_byte_offset_from_struct(self.display_args_fmt)

        # Sort event args by arg range.
        self.event_arg_replacements = sorted(self.event_arg_replacements, key=lambda x: x.arg_range)

        # Start with default argument list.
        self.evs_args_list = self.args_list.copy()

        for arg_r in self.event_arg_replacements:
            try:
                arg_index, argument_byte_type = arg_offset_dict[arg_r.write_from_byte]
            except KeyError:
                raise ValueError(
                    f"No argument in '{self.event_arg_replacements}' begins at byte {arg_r.write_from_byte}. "
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

            value_to_overwrite = self.args_list[arg_index]
            evs_arg_name = list(self.EMEDF[self.category, self.index]["args"])[arg_index]
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
                        f"{value_to_overwrite} (position {arg_index}) in instruction {self.instruction_id} "
                        f"with args {self.args_list} (types '{self.display_args_fmt}')"
                    )

            self.evs_args_list[arg_index] = default_arg_name  # will generally be replaced with an EVS name later

            # Store information from instruction on `EventArgReplacement`.
            arg_r.arg_index = arg_index
            arg_r.name = evs_arg_name
            arg_r.fmt = argument_byte_type
            arg_r.py_type_hint = arg_py_type

    def to_emevd_writer(self, writer: BinaryWriter):
        InstructionStruct.object_to_writer(self, writer)
        if not writer.long_varints:
            writer.pad(4)

    def pack_base_args(self, writer: BinaryWriter, base_args_start_offset: int):
        if self.category == 1014:  # 'DefineLabel' category has NO arg data offset, not even to empty bytes
            writer.fill("base_args_local_offset", -1, obj=self)
            return
        writer.fill("base_args_local_offset", writer.position - base_args_start_offset, obj=self)
        packed_base_args = struct.pack(f"@{self.struct_args_fmt}0i", *self.args_list) if self.args_list else b""
        writer.append(packed_base_args)

    def pack_event_layers(
        self, writer: BinaryWriter, existing_event_layers: dict[EventLayers, int], event_layers_start_offset: int
    ):
        if not self.event_layers:
            writer.fill("event_layers_local_offset", -1, obj=self)
        elif self.event_layers in existing_event_layers:
            writer.fill("event_layers_local_offset", existing_event_layers[self.event_layers], obj=self)
        else:
            # Write new `EventLayers`.
            relative_offset = event_layers_start_offset - writer.position
            writer.fill("event_layers_local_offset", relative_offset, obj=self)
            existing_event_layers[self.event_layers] = relative_offset
            self.event_layers.to_emevd_writer(writer)

    def __repr__(self) -> str:
        text = (
            f"Instruction({self.category}, {self.index}, "
            f"display_arg_types=\"{self.display_args_fmt}\", args={self.args_list})"
        )
        if self.event_layers is not None:
            text = text[:-1] + f", event_layers={self.event_layers})"
        return text
