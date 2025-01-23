from __future__ import annotations

__all__ = ["Event", "EventSignature"]

import abc
import logging
import re
import struct
import typing as tp
from dataclasses import dataclass, field
from types import GenericAlias

from soulstruct.base.game_types import GAME_INT_TYPE, Flag, GameObjectInt, GameEnumsManager
from soulstruct.utilities.binary import *

from .instruction import Instruction, EventArgRepl
from .event_layers import EventLayers
from ..enums import OnRestBehavior
from ..evs.adv_decompiler import AdvancedDecompiler

_LOGGER = logging.getLogger("soulstruct")


# TODO: Merge with `binary` module types.
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
    # TODO: Extra one in Elden Ring? 200? 'Postconstructor'?
}

_INSTRUCTION_RE = re.compile(r" *(\w+)\((.*)\)")  # groups = (instruction_name, args)
_ARG_TUPLE_START_RE = re.compile(r"(\w[\w_]*)=([\[(]).*")  # groups = (arg_name, bracket_type)
_CONDITION_RE = re.compile(r" *(AND|OR)_(\d+)\.Add\((.*)\)")  # groups = (condition_type, condition_i, condition)
_MAIN_AWAIT_RE = re.compile(r" *MAIN\.Await\((.*)\)")  # groups = (condition_type, condition_i, condition)
_IF_BLOCK_RE = re.compile(r" *if (.*):")  # groups = (condition)
_LABEL_RE = re.compile(r"DefineLabel\((\d+)\)")
_GOTO_RE = re.compile(r"Goto.*\(Label\.L(\d+)[,)].*")


# Auto-detected event argument names that are NOT preferred over other names.
# Order here is also important: early names are even LESS preferred than later ones.
_VAGUE_ARG_NAMES = [
    "left", "right",
    "entity", "other_entity", "target_entity", "owner_entity", "anchor_entity", "attacked_entity",
    "destination", "source_entity", "copy_draw_parent", "line_intersects", "flag",
    "dummy_id",
]


@dataclass(slots=True)
class SingleEventArg:
    """Unlike `EventArgReplacement`, this represents an actual single event argument as it appears in the decompiled
    `RunEvent` instruction, and its signature information for the EVS event function.

    It holds all the formats, names, and Python types that appear where it is used in instructions.
    """
    # We default to unsigned integers.
    DEFAULT_ARG_SIZE_TYPE: tp.ClassVar[dict[int, str]] = {1: "B", 2: "H", 4: "I"}

    arg_range: tuple[int, int]  # start and (exclusive) end offsets; corresponds to `(i, j)` in default argument names
    fmts: set[str] = field(default_factory=set)
    names: set[str] = field(default_factory=set)
    py_types: set[type | GenericAlias] = field(default_factory=set)  # each could be from a `typing.Union`
    sizes: set[int] = field(default_factory=set)  # replacement sizes (most important attribute!)

    # Computed from above sets.
    combined_name: str = ""
    combined_fmt: str = ""
    combined_py_types: tuple[type, ...] = ()
    # Subset of the above; ONLY contains game types (for enum lookups).
    combined_game_types: tuple[GAME_INT_TYPE, ...] = ()

    def record_repl_usage(self, event_arg_repl: EventArgRepl):
        """Merge in information from a single replacement usage."""
        self.names.add(event_arg_repl.name)
        self.fmts.add(event_arg_repl.fmt)
        self.py_types.add(event_arg_repl.py_type_hint)
        self.sizes.add(event_arg_repl.size)

    def remove_generic_names(self):
        """Remove non-preferred arg names."""
        # TODO: Should check compatible 'classes' of names, so 'character__flag' doesn't just become 'character', etc.
        for vague_arg_name in (
            "event_arg",
            "entity", "other_entity", "target_entity", "owner_entity", "anchor_entity", "attacked_entity",
            "destination", "source_entity", "copy_draw_parent", "line_intersects", "flag", "left", "right",
            "dummy_id",
        ):
            if len(self.names) >= 2 and vague_arg_name in self.names:
                self.names.remove(vague_arg_name)

    def compute_combined_info(self, existing_arg_names: set[str], event_id: int = -1):
        """Parse the sets of formats, names, Python types, and sizes, then decide on usage in signature."""
        if not self.names:
            _LOGGER.warning(f"Event arg {self.arg_range} in event {event_id} has no usages in instructions.")
            return

        if len(self.sizes) > 1:
            _LOGGER.error(
                f"Detected multiple sizes for event arg {self.arg_range} in event {event_id}: {self.sizes}. "
                f"This is a critical error that must be fixed in your EMEVD source file."
            )
            return

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
        self.combined_name = arg_name

        # Size reigns supreme over usage formats, which may be ambiguous (e.g. args of any integer size can be used in
        # the same comparison instructions).
        size = next(iter(self.sizes))
        self.combined_fmt = self.guess_arg_fmt(event_id, arg_name, size)

        all_py_types = []
        all_game_types = []
        for py_type in self.py_types:
            try:  # convert `typing.Union` to `tuple`
                origin = tp.get_origin(py_type)
            except AttributeError:  # implies `py_type` is a real Python type (no `__origin__`)
                all_py_types.append(py_type)
                if issubclass(py_type, GameObjectInt):
                    all_game_types.append(py_type)
            else:
                union_types = tp.get_args(py_type) if origin is tp.Union else ()
                for union_type in union_types:
                    if union_type not in all_py_types:
                        all_py_types.append(union_type)
                        if issubclass(union_type, GameObjectInt):
                            all_game_types.append(union_type)
        self.combined_py_types = tuple(all_py_types)
        self.combined_game_types = tuple(all_game_types)

    def guess_arg_fmt(self, event_id: int, name: str, size: int) -> str:
        """Guess the most appropriate format for this event arg based on its usage in instructions.

        Logs warnings when incompatible types or invalid usage sizes are detected.
        """

        default_fmt = self.DEFAULT_ARG_SIZE_TYPE[size]

        if len(self.fmts) == 1:
            unique_fmt = next(iter(self.fmts))
            fmt_size = struct.calcsize(unique_fmt)
            if fmt_size < size:
                _LOGGER.warning(
                    f"Detected usage format '{unique_fmt}' for event arg '{name}' in event {event_id} has size "
                    f"{struct.calcsize(unique_fmt)}, which is smaller than the replacement size {size}. Fix this! "
                    f"Using default integer type '{default_fmt}' for this arg."
                )
                return default_fmt
            elif fmt_size == size:
                # Only one format used, and it matches the replacement `size`. Format override.
                return unique_fmt
            else:
                # Only one format used, and it is larger than our replacement `size`.
                if unique_fmt in "fs":
                    # Default format is byte or short, but detected unique format is float or string ref.
                    _LOGGER.warning(
                        f"Detected incompatible usage format for event arg '{name}' in event {event_id}: "
                        f"{unique_fmt}. Fix this! Using default integer type '{default_fmt}' for this arg."
                    )
                return default_fmt
        else:
            # Check all usage formats for incompatible or too-small types.
            # If all usages are compatible, we can use the most specific (smallest) type.
            smallest_fmt = ""
            smallest_fmt_size = 4
            has_int_usage = False
            has_str_usage = False
            has_float_usage = False
            for fmt in self.fmts:
                fmt_size = struct.calcsize(fmt)
                if fmt in "bBhHiI":
                    has_int_usage = True
                    if has_str_usage or has_float_usage:
                        _LOGGER.warning(
                            f"Detected incompatible usage formats for event arg '{name}' in event {event_id}: "
                            f"{self.fmts}. Fix this! Using default integer type '{default_fmt}' for this arg."
                        )
                        return default_fmt
                elif fmt == "f":
                    has_float_usage = True
                    if has_int_usage or has_str_usage:
                        _LOGGER.warning(
                            f"Detected incompatible usage formats for event arg '{name}' in event {event_id}: "
                            f"{self.fmts}. Fix this! Using default integer type '{default_fmt}' for this arg."
                        )
                        return default_fmt
                elif fmt == "s":
                    has_str_usage = True
                    if has_int_usage or has_float_usage:
                        _LOGGER.warning(
                            f"Detected incompatible usage formats for event arg '{name}' in event {event_id}: "
                            f"{self.fmts}. Fix this! Using default integer type '{default_fmt}' for this arg."
                        )
                        return default_fmt

                if fmt_size < size:
                    _LOGGER.warning(
                        f"At least one detected usage format for event arg '{name}' in event {event_id} has "
                        f"size smaller than {size}: {self.fmts}. Fix this! Using default integer type '{default_fmt}' "
                        f"for this arg."
                    )
                    return default_fmt
                elif fmt_size < smallest_fmt_size:
                    # Found new smallest (valid) format.
                    smallest_fmt = fmt
                    smallest_fmt_size = fmt_size

            return smallest_fmt if smallest_fmt else default_fmt


@dataclass(slots=True)
class EventSignature:
    """Holds information about a single `Event`'s variable arguments inferred from their usage in its instructions."""
    event_args: list[SingleEventArg]

    def get_full_fmt(self) -> str:
        return "".join(arg.combined_fmt for arg in self.event_args)

    def get_evs_arg_names(self) -> list[str]:
        """Add index suffices to names, e.g. 'text' -> 'text_1', for duplicates."""
        name_instances = {}  # maps names to their number of uses so suffixes can be appended
        arg_names = []
        for event_arg in self.event_args:
            name = event_arg.combined_name
            if name in name_instances:
                count = name_instances[name]
                name_instances[name] += 1
                name = f"{name}_{count}"
            else:
                name_instances[name] = 1
            arg_names.append(name)
        return arg_names

    def get_evs_arg_string(self, prepend_slot=True) -> str:
        """Combine `names` and `py_types` into an EVS event function argument signature."""
        arg_strings = []
        arg_names = self.get_evs_arg_names()
        for event_arg, name in zip(self.event_args, arg_names, strict=True):
            game_object_int_types = {
                py_type for py_type in event_arg.combined_py_types
                if issubclass(py_type, GameObjectInt)
            }
            if len(game_object_int_types) == 1:
                py_type_name = next(iter(game_object_int_types)).__name__ + " | int"
            else:  # missing or ambiguous game type
                py_type_name = EVS_ARG_TYPES[event_arg.combined_fmt]
            arg_strings.append(f"{name}: {py_type_name}")
        if arg_names and prepend_slot:
            # Prepend blank argument for slot intellisense (if any arguments exist).
            arg_strings = ["_"] + arg_strings
        return ", ".join(arg_strings)

    def __repr__(self) -> str:
        if not self.event_args:
            return "EventSignature()"

        lines = [f"EventSignature(", f"    \"{self.get_full_fmt()}\""]
        for arg in self.event_args:
            lines.append(f"    {arg.combined_name}: {arg.combined_fmt} ({arg.combined_py_types})")
        lines.append(")")
        return "\n".join(lines)


class EventStruct(BinaryStruct):
    event_id: varuint
    instructions_count: varuint
    instructions_local_offset: varint
    event_arg_replacements_count: varuint
    event_arg_replacements_local_offset: varint
    on_rest_behavior: uint  # always 32-bit
    _pad1: bytes = binary_pad(4, init=False)


@dataclass(slots=True)
class Event(abc.ABC):
    """A single contained event function that appears in an event script.
    
    Event functions run in parallel when called with `RunEvent` (or `RunCommonEvent`) and frequently pause themselves
    until certain conditions are met. Their `on_rest_behavior` type indicates what happens when the player rests at a
    checkpoint (by default, they continue unaffected, but they can also restart or simply end).

    Each map runs events 50 (the 'preconstructor') and 0 (the 'constructor') automatically when loaded, which are mostly
    responsible for starting every other event. The same event can be called multiple times with different `slot`
    arguments passed to `Run{Common}Event`, and will function independently.

    When an event ends (even if it restarts), the event flag that has the same ID as the event (plus the called `slot`
    of the event instance) will be enabled.

    Events also have `EventArgRepl` instances attached to them, which represent where any packed event data passed to
    the `Run{Common}Event` instruction is used inside the event. Soulstruct will attach each `EventArgRepl` to the
    `Instruction` it affects, rather than keeping them in the `Event` instance.
    """
    
    # Game-specific class attributes.
    INSTRUCTION_CLASS: tp.ClassVar[type[Instruction]]
    EMEDF_TESTS: tp.ClassVar[dict[str, dict[str, str]]]
    EMEDF_COMPARISON_TESTS: tp.ClassVar[dict[str, dict[str, str]]]
    WRAP_LIMIT: tp.ClassVar[int] = 120  # PyCharm default line length
    USE_ADVANCED_DECOMPILER: tp.ClassVar[bool] = True

    event_id: int = 0
    on_rest_behavior: OnRestBehavior = OnRestBehavior.ContinueOnRest
    instructions: list[Instruction] = field(default_factory=list)

    # Generated by inspecting all `EventArgReplacement` occurrences in all instructions.
    # Refreshed by all 'decompiled' packing/writing methods just before usage, in case instructions are directly
    # modified and the event arg replacements are changed.
    signature: EventSignature = field(init=False)

    def __post_init__(self):
        self.process_all_event_arg_replacements()
        self.update_signature()
        # Caller should call `event.update_run_event_instructions(event_signatures)` with dict of all event signatures.

    @classmethod
    def from_emevd_reader(
        cls,
        reader: BinaryReader,
        instruction_table_offset: int,
        base_arg_data_offset: int,
        event_arg_table_offset: int,
        event_layers_table_offset: int,
    ) -> tp.Self:
        event_struct = EventStruct.from_bytes(reader)

        # Defined here in case there are no instructions.
        instructions = []

        if event_struct.instructions_local_offset != -1:
            with reader.temp_offset(instruction_table_offset + event_struct.instructions_local_offset):
                instructions = [
                    cls.INSTRUCTION_CLASS.from_emevd_reader(reader, base_arg_data_offset, event_layers_table_offset)
                    for _ in range(event_struct.instructions_count)
                ]

        if event_struct.event_arg_replacements_local_offset != -1:
            with reader.temp_offset(event_arg_table_offset + event_struct.event_arg_replacements_local_offset):
                # Read `EventArgRepl`s but attach each one to its `Instruction` rather than here.
                event_arg_replacements = [
                    EventArgRepl.from_emevd_reader(reader)
                    for _ in range(event_struct.event_arg_replacements_count)
                ]
                for replacement in event_arg_replacements:
                    instructions[replacement.instruction_line].event_arg_replacements.append(replacement)

        return cls(event_struct.event_id, OnRestBehavior(event_struct.on_rest_behavior), instructions)

    def process_all_event_arg_replacements(self):
        """NOTE: `update_signature()` should always be called AFTER this, as this function will (re-)assign default
        EVS argument names to instructions for event arguments."""
        for i, instruction in enumerate(self.instructions):
            try:
                instruction.process_event_arg_replacements()
            except ValueError as ex:
                raise ValueError(
                    f"Error occurred while processing event args in instruction {i}, {instruction.instruction_id}], "
                    f"of event {self.event_id}.\n    Error: {ex}"
                )

    def update_run_event_instructions(
        self,
        event_signatures: dict[int, EventSignature] = None,
        common_signatures: dict[int, EventSignature] = None,
    ):
        """Iterates over instructions and updates any `Run{Common}Event` instructions with event arguments with their
        proper `args` and `arg_types` values.

        If a `RunEvent` instruction contains more arguments than the event can actually use (which is fine by the game -
        the extra packed argument data will simply never be indexed into), this will log a warning, and you should see
        error highlighting in your decompiled EVS script (wrong number of arguments).

        Can be called with 'local' `event_signatures` and/or `common_signatures`. Only events run with `RunCommonEvent`
        will be searched for in `common_signatures`, if given. (`RunCommonEvent` will also search for events in
        `event_signatures` first, even though this is rare.)

        TODO: Doesn't Bloodborne use 'RunEvent' even for common events (from `common.emevd`)?
        """
        if not event_signatures and not common_signatures:
            return  # nothing to do

        for instruction in self.instructions:
            if (event_id := instruction.get_called_event()) is not None:
                if event_signatures and event_id in event_signatures:
                    var_format = event_signatures[event_id].get_full_fmt()
                else:
                    # Event is not defined locally. Check common (func) events, if provided.
                    # TODO: These special indices (0, 6) should be defined more centrally.
                    if instruction.index == 6 and common_signatures and event_id in common_signatures:
                        var_format = common_signatures[event_id].get_full_fmt()
                    else:
                        if event_signatures and instruction.index == 0:  # `RunEvent`
                            _LOGGER.warning(f"Map event {event_id} was run, but is not defined in map EMEVD.")
                        # No information to use to modify this instruction.
                        continue
                if not var_format:
                    # No arguments (zero). Leave "I" in arg types.
                    continue

                var_ind = instruction.display_args_fmt.find("|")
                if var_ind == -1:
                    # Only one argument (maybe zero).
                    new_display_types = f"{instruction.struct_args_fmt[:-1]}{var_format[0]}"
                else:
                    new_display_types = f"{instruction.struct_args_fmt[:var_ind - 1]}{var_format[0]}|{var_format[1:]}"

                old_format = "@" + instruction.struct_args_fmt  # property processes old display types
                instruction.display_args_fmt = new_display_types
                new_format = instruction.struct_args_fmt  # property processes new display types set above

                # TODO: calcsize difference is not the correct way to check this. It should be more about the length of
                #  'args_list', or the size of the packed data.

                old_packed_size = struct.calcsize(old_format + "0i")  # aligned to 4
                new_packed_size = struct.calcsize(new_format + "0i")  # aligned to 4

                if new_packed_size < old_packed_size:
                    # `RunEvent` instruction contains more argument data than the event can take. This will not cause a
                    # fatal error in the game, as the extra data will simply never be used. However, as we cannot use
                    # the event signature to detect the format of the excess data, we must represent it with integers.
                    excess_size = old_packed_size - new_packed_size  # always a multiple of four
                    new_format_with_excess = new_format + f"{excess_size // 4}I"
                    _LOGGER.warning(
                        f"Found {excess_size} extra bytes of arguments in event-running {instruction}. Extra argument "
                        f"data will be included in EMEVD as unsigned integers, but will never have an effect in game, "
                        f"as the corresponding event {event_id} does not use it."
                    )
                    try:
                        real_args = list(
                            struct.unpack(
                                new_format_with_excess + "0i", struct.pack(old_format + "0i", *instruction.args_list)
                            )
                        )
                    except struct.error:
                        _LOGGER.error(
                            f"Failed to handle excess event arguments for instruction {instruction} with original "
                            f"arguments {old_format} and new padded arguments {new_format_with_excess}. Args: "
                            f"{instruction.args_list}"
                        )
                        raise
                else:
                    # `RunEvent` instruction argument data matches size of expected event arguments.
                    try:
                        real_args = list(struct.unpack(
                            new_format + "0i", struct.pack(old_format + "0i", *instruction.args_list))
                        )
                    except struct.error:
                        _LOGGER.error(
                            f"Failed to convert event arguments for instruction {instruction} from old format "
                            f"{old_format} to new format {new_format}. Args: {instruction.args_list}"
                        )
                        raise
                instruction.args_list = real_args

    @property
    def instruction_count(self):
        return len(self.instructions)

    @property
    def total_args_size(self):
        return sum([i.base_args_size for i in self.instructions])

    @property
    def event_arg_replacements_count(self):
        return sum([len(i.event_arg_replacements) for i in self.instructions])

    def to_numeric(self) -> str:
        numeric_string = f"{self.event_id}, {self.on_rest_behavior}"
        for instruction in self.instructions:
            numeric_string += "\n" + "\n".join(instruction.to_numeric())
        return numeric_string

    def update_signature(self):
        """Process event arg information for ALL instructions at once and update event `signature`.

        Also updates the `evs_args_list` in each instruction with the new argument names.
        """
        single_event_args = {}  # type: dict[tuple[int, int], SingleEventArg]
        for instruction in self.instructions:
            for event_arg_repl in instruction.event_arg_replacements:
                if event_arg_repl.arg_range not in single_event_args:
                    # First occurrence of this event arg being used as a replacement. (Info still added on next line.)
                    single_event_args[event_arg_repl.arg_range] = SingleEventArg(event_arg_repl.arg_range)
                single_event_args[event_arg_repl.arg_range].record_repl_usage(event_arg_repl)

        # Sort into list by arg range `(start_byte, stop_byte)` and compute combined attributes.
        event_args = sorted(single_event_args.values(), key=lambda arg: arg.arg_range)
        event_arg_names = set()
        for event_arg in event_args:
            event_arg.remove_generic_names()
            event_arg.compute_combined_info(event_arg_names, self.event_id)

        self.signature = EventSignature(event_args)

        # Use new event argument names from signature in instructions.
        for event_arg, arg_name in zip(self.signature.event_args, self.signature.get_evs_arg_names(), strict=True):
            if not arg_name:
                continue  # unusual
            for instruction in self.instructions:
                for replacement in instruction.event_arg_replacements:
                    if replacement.arg_range == event_arg.arg_range and replacement.arg_index != -1:
                        instruction.evs_args_list[replacement.arg_index] = arg_name

    def to_evs(
        self,
        enums_manager: GameEnumsManager,
        event_signatures: dict[int, EventSignature],
        function_prefix="Event",
    ) -> str:
        """Convert ('decompile') single event script to EVS."""

        # Preference for naming: special event name (e.g. Constructor), 'Event_{flag_enum_name}', or 'Event_{event_id}'.
        event_flag_enum = None
        if self.event_id in _SPECIAL_EVENT_NAMES:
            function_name = _SPECIAL_EVENT_NAMES[self.event_id]
        else:
            try:
                event_flag_enum = enums_manager.check_out_enum_variable(self.event_id, Flag)
            except enums_manager.EnumManagerError:
                function_name = f"{function_prefix}_{self.event_id}"
            else:
                just_enum_name = event_flag_enum.split(".")[-1].lstrip("_")
                function_name = f"{function_prefix}_{just_enum_name}"

        function_docstring = f'"""Event {self.event_id}"""'
        # starts with an empty '_' slot arg, if any other args exist
        self.process_all_event_arg_replacements()
        self.update_signature()

        if event_flag_enum is not None:
            on_rest_behavior_decorator = f"@{OnRestBehavior(self.on_rest_behavior).name}({event_flag_enum})\n"
        else:
            on_rest_behavior_decorator = f"@{OnRestBehavior(self.on_rest_behavior).name}({self.event_id})\n"

        function_def = _indent_and_wrap_function_def(
            function_name, self.signature.get_evs_arg_string(), wrap_limit=self.WRAP_LIMIT
        )
        function_def += f"\n    {function_docstring}"
        evs_event_string = on_rest_behavior_decorator + function_def

        instruction_lines = [instr.to_evs(enums_manager, event_signatures) for instr in self.instructions]

        if self.USE_ADVANCED_DECOMPILER:
            adv_decompiler = AdvancedDecompiler(self.EMEDF_TESTS, self.EMEDF_COMPARISON_TESTS)
            try:
                instruction_lines = adv_decompiler.adv_decompile(instruction_lines)
            except (ValueError, KeyError, IndexError) as ex:
                _LOGGER.error(
                    f"Error while trying to decompile event {self.event_id} with high-level language. Using simple "
                    f"EVS output. Error:\n  {ex}")

        # Some final simple sugar that we can always add.
        for instr_line in instruction_lines:
            if label_match := _LABEL_RE.match(instr_line):
                # Add a label comment for visual ease.
                evs_event_string = evs_event_string.rstrip("\n ")  # we want exactly two newlines
                evs_event_string += f"\n\n    # --- Label {label_match.group(1)} --- #"
            new_lines = _indent_and_wrap_instruction(instr_line, wrap_limit=self.WRAP_LIMIT, indent=4)
            # TODO: Goto comment needs to contribute to max line length for wrap. Also might just be redundant.
            # if goto_match := _GOTO_RE.match(instr_line):
            #     label = goto_match.group(1)
            #     new_lines_split = new_lines.split("\n")
            #     new_lines_split[1] = new_lines_split[1] + f"  # --> Label {label}"
            #     new_lines = "\n".join(new_lines_split)
            evs_event_string += new_lines

        return evs_event_string

    def to_emevd_writer(self, writer: BinaryWriter):
        EventStruct.object_to_writer(self, writer, instructions_count=len(self.instructions))

    def pack_instructions(self, writer: BinaryWriter, instructions_offset: int):
        writer.fill("instructions_local_offset", writer.position - instructions_offset, obj=self)
        for instruction in self.instructions:
            instruction.to_emevd_writer(writer)

    def pack_instruction_base_args(self, writer: BinaryWriter, base_args_data_offset: int):
        for instruction in self.instructions:
            instruction.pack_base_args(writer, base_args_data_offset)

    def pack_event_arg_replacements(self, writer: BinaryWriter, event_arg_replacements_offset: int) -> int:
        """Returns the number of event arg replacements written (for summing in EMEVD header)."""
        event_arg_replacements = []  # type: list[EventArgRepl]
        for instruction in self.instructions:
            event_arg_replacements += instruction.event_arg_replacements

        if event_arg_replacements:
            # Sort arg replacements to better match original EMEVD resources. (Should be purely cosmetic.)
            event_arg_replacements_local_offset = writer.position - event_arg_replacements_offset
            writer.fill("event_arg_replacements_local_offset", event_arg_replacements_local_offset, obj=self)
            for replacement in sorted(
                event_arg_replacements, key=lambda arg_r: (arg_r.read_offset, arg_r.instruction_line)
            ):
                replacement.to_emevd_writer(writer)
        else:
            writer.fill("event_arg_replacements_local_offset", -1, obj=self)

        return len(event_arg_replacements)

    def pack_instruction_event_layers(
        self, writer: BinaryWriter, existing_event_layers: dict[EventLayers, int], event_layers_start_offset: int
    ):
        """Checks `existing_event_layers` (which maps packed `event_layers_uint` to offsets for reuse)."""
        for instruction in self.instructions:
            instruction.pack_event_layers(writer, existing_event_layers, event_layers_start_offset)


def _indent_and_wrap_instruction(instr: str, wrap_limit=121, indent=4):
    """Indent instruction with `indent` spaces and put each argument on a separate line if the instruction exceeds
    `wrap_limit`."""
    existing_indent = " " * (len(instr) - len(instr.lstrip(" ")))
    base_indent = " " * indent
    indented_instr = f"\n{base_indent}{instr}"
    if len(indented_instr) <= wrap_limit:
        return indented_instr
    if not (match := _INSTRUCTION_RE.match(instr)):
        if match := _CONDITION_RE.match(instr):
            # Indent and wrap condition.
            c_type, c_index, condition = match.group(1, 2, 3)
            wrapped_condition = _indent_and_wrap_instruction(
                condition, wrap_limit=wrap_limit - len(existing_indent), indent=len(existing_indent) + indent
            )
            wrapped_condition = wrapped_condition.lstrip("\n ")
            return f"\n{base_indent}{existing_indent}{c_type}_{c_index}.Add({wrapped_condition})"
        elif match := _MAIN_AWAIT_RE.match(instr):
            # Indent and wrap condition.
            condition = match.group(1)
            wrapped_condition = _indent_and_wrap_instruction(
                condition, wrap_limit=wrap_limit - len(existing_indent), indent=len(existing_indent) + indent
            )
            wrapped_condition = wrapped_condition.lstrip("\n ")
            return f"\n{base_indent}{existing_indent}MAIN.Await({wrapped_condition})"
        elif match := _IF_BLOCK_RE.match(instr):
            # Indent and wrap condition.
            condition = match.group(1)
            wrapped_condition = _indent_and_wrap_instruction(
                condition, wrap_limit=wrap_limit - len(existing_indent), indent=len(existing_indent) + indent
            )
            wrapped_condition = wrapped_condition.lstrip("\n ")
            return f"\n{base_indent}{existing_indent}if {wrapped_condition}:"
        else:
            raise ValueError(f"Cannot indent/wrap malformed instruction or condition group definition: '{instr}'")

    # Indent and wrap basic instruction.
    instr_name, instr_args_string = match.group(1, 2)
    if not instr_args_string:
        return indented_instr  # shouldn't happen (super-long instruction name)
    arg_indent = existing_indent + base_indent + "    "
    args = instr_args_string.split(", ")
    i = 0
    arg_strings = []
    while i < len(args):
        arg = args[i]
        if tuple_match := _ARG_TUPLE_START_RE.match(arg):
            # Consume additional args to reconstruct and properly indent tuple argument.
            arg_name, opening_bracket = tuple_match.group(1, 2)
            closing_bracket = ")" if opening_bracket == "(" else "]"
            event_args = [arg[len(arg_name) + 2:]]  # first arg value
            i += 1
            if event_args[0].endswith(closing_bracket):  # e.g., `event_layers=[2]`
                event_args[0] = event_args[0][:-1]  # cut off closing bracket
            else:
                while not (test_arg := args[i]).endswith(closing_bracket):
                    event_args.append(test_arg)
                    i += 1
                event_args.append(test_arg[:-1])  # cut off closing bracket

            one_line_event_args = f"{arg_name}={opening_bracket}{', '.join(event_args)}{closing_bracket},"
            if len(arg_indent + one_line_event_args) <= wrap_limit:
                arg_strings.append(one_line_event_args)
            else:
                # Place each args element on a separate line, further indented.
                arg_strings.append(f"{arg_name}={opening_bracket}")
                arg_strings += [" " * 4 + event_arg + "," for event_arg in event_args]
                arg_strings.append(f"{closing_bracket},")
        else:
            arg_strings.append(arg + ",")
        i += 1

    arg_lines = "\n".join(arg_indent + arg_string for arg_string in arg_strings)
    return f"\n{base_indent}{existing_indent}{instr_name}(\n{arg_lines}\n{base_indent}{existing_indent})"


def _indent_and_wrap_function_def(function_name: str, function_args, wrap_limit=120):
    one_line_def = f"def {function_name}({function_args}):"
    if len(one_line_def) <= wrap_limit:
        return one_line_def
    arg_indent = " " * 4
    arg_lines = ",\n".join(arg_indent + arg_string for arg_string in function_args.split(", "))
    return f"def {function_name}(\n{arg_lines},\n):"
