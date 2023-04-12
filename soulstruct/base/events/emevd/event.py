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

from .enums import OnRestBehavior
from .instruction import Instruction, EventArgRepl
from .event_layers import EventLayers

try:
    Self = tp.Self
except AttributeError:
    Self = "Event"

_LOGGER = logging.getLogger(__name__)


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
}

_INSTRUCTION_RE = re.compile(r" *(\w+)\((.*)\)")  # groups = (instruction_name, args)
_ARG_TUPLE_START_RE = re.compile(r"(\w[\w_]*)=([\[(]).*")  # groups = (arg_name, bracket_type)
_CONDITION_RE = re.compile(r" *(AND|OR)_(\d+)\.Add\((.*)\)")  # groups = (condition_type, condition_i, condition)
_MAIN_AWAIT_RE = re.compile(r" *MAIN\.Await\((.*)\)")  # groups = (condition_type, condition_i, condition)
_IF_BLOCK_RE = re.compile(r" *if (.*):")  # groups = (condition)
_LABEL_RE = re.compile(r"DefineLabel\((\d+)\)")
_GOTO_RE = re.compile(r"Goto.*\(Label\.L(\d+)[,)].*")

# High-level decompilation.
_HLD_IF_CONDITION_RE = re.compile(
    r"^(?P<indent> *)If(?P<finished>Finished)?Condition(?P<state>True|False)\("
    r"(?P<condition>(MAIN|((AND|OR)_\d+))), input_condition=(?P<input_condition>(MAIN|((AND|OR)_\d+)))\)$"
)
_HLD_IF_COMPARISON_RE = re.compile(
    r"^(?P<indent> *)If(?P<test>.*?)(?P<comp>Equal|NotEqual|GreaterThan|LessThan|GreaterThanOrEqual|LessThanOrEqual)"
    r"\((?P<condition>(MAIN|((AND|OR)_\d+)))(?P<pre_args>.*?), value=(?P<value>[\w_.]+)(?P<post_args>, .*?)?\)$"
)
_HLD_IF_RE = re.compile(
    r"^(?P<indent> *)If(?P<test>.*)\((?P<condition>(MAIN|((AND|OR)_\d+)))(?P<args>.*?)\)$"
)
_HLD_SKIP_RE = re.compile(
    r"^(?P<indent> *)SkipLinesIf(?P<test>.*)\((?P<line_count>\d+)(?P<args>.*?)\)$"
)
_HLD_UNCONDITIONAL_SKIP_RE = re.compile(
    r"^(?P<indent> *)SkipLines\((?P<line_count>\d+)\)$"
)
_HLD_RETURN_CONDITION_RE = re.compile(
    r"^(?P<indent> *)(?P<return_type>End|Restart)If(?P<finished>Finished)?Condition(?P<state>True|False)\("
    r"input_condition=(?P<condition>((AND|OR)_\d+))\)$"
)
_HLD_RETURN_RE = re.compile(
    r"^(?P<indent> *)(?P<return_type>End|Restart)If(?P<test>.*)\((?P<args>.*?)\)$"
)

_COMPARISON_OPERATORS = {
    "Equal": "==",
    "NotEqual": "!=",
    "GreaterThan": ">",
    "LessThan": "<",
    "GreaterThanOrEqual": ">=",
    "LessThanOrEqual": "<=",
}


@dataclass(slots=True)
class SingleEventArg:
    """Unlike `EventArgReplacement`, this represents an actual single event argument as it appears in the decompiled
    `RunEvent` instruction, and its signature information for the EVS event function.

    It holds all the formats, names, and Python types that appear where it is used in instructions.
    """
    DEFAULT_ARG_SIZE_TYPE: tp.ClassVar[dict[int, str]] = {1: "B", 2: "H", 4: "I"}

    arg_range: tuple[int, int]  # start and (exclusive) end offsets; corresponds to `(i, j)` in default argument names
    fmts: set[str] = field(default_factory=set)
    names: set[str] = field(default_factory=set)
    py_types: set[tp.Type | GenericAlias] = field(default_factory=set)  # each could be from a `typing.Union`

    # Computed from above sets.
    combined_name: str = field(default="")
    combined_fmt: str = field(default="")
    combined_py_types: tuple[tp.Type, ...] = ()
    # Subset of the above; ONLY contains game types (for enum lookups).
    combined_game_types: tuple[GAME_INT_TYPE, ...] = ()

    def add_info(self, event_arg: EventArgRepl):
        """Merge in information from a single replacement usage."""
        self.names.add(event_arg.name)
        self.fmts.add(event_arg.fmt)
        self.py_types.add(event_arg.py_type_hint)

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

    def compute_combined_info(self, existing_arg_names: set[str], event_id: int = -1):
        """Parse the sets of formats, names, and Python types and decide what to use for EVS function signatures."""

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

        if len(self.fmts) > 1:
            # Multiple detected types. Acceptable (using default integer type) only if they all the same size.
            sizes = {struct.calcsize(fmt) for fmt in self.fmts}
            if len(sizes) == 1:
                arg_size = next(iter(sizes))
                self.combined_fmt = self.DEFAULT_ARG_SIZE_TYPE[arg_size]
                _LOGGER.warning(
                    f"Detected multiple types for event arg '{arg_name}' in event {event_id}: {self.fmts}. "
                    f"Using default type '{self.combined_fmt}' for this arg size ({arg_size})."
                )
            else:
                raise ValueError(
                    f"Detected multiple types for event arg '{arg_name}' in event {event_id}: {self.fmts}. "
                    f"They have incompatible sizes, which is not permitted."
                )
        else:
            self.combined_fmt = next(iter(self.fmts))

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
            game_object_types = {
                py_type for py_type in event_arg.combined_py_types
                if issubclass(py_type, GameObjectInt)
            }
            if len(game_object_types) == 1:
                py_type_name = next(iter(game_object_types)).__name__ + " | int"
            else:  # missing or ambiguous game type
                py_type_name = EVS_ARG_TYPES[event_arg.combined_fmt]
            arg_strings.append(f"{name}: {py_type_name}")
        if arg_names and prepend_slot:
            # Prepend blank argument for slot intellisense (if any arguments exist).
            arg_strings = ["_"] + arg_strings
        return ", ".join(arg_strings)


@dataclass(slots=True)
class EventStruct(BinaryStruct):
    event_id: varuint
    instructions_count: varuint
    instructions_local_offset: varint
    event_arg_replacements_count: varuint
    event_arg_replacements_local_offset: varint
    on_rest_behavior: uint  # always 32-bit
    _pad1: bytes = field(init=False, **BinaryPad(4))


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

    Events also have `EventArgRepl` instances attached to them, which represent where any packed event data passed to the
    `Run{Common}Event` instruction is used inside the event. Soulstruct will attach each `EventArgRepl` to the `Instruction`
    it affects, rather than keeping them in the `Event` instance.
    """
    
    # Game-specific class attributes.
    INSTRUCTION_CLASS: tp.ClassVar[tp.Type[Instruction]]
    EMEDF_TESTS: tp.ClassVar[dict[str, dict[str, str]]]
    EMEDF_COMPARISON_TESTS: tp.ClassVar[dict[str, dict[str, str]]]
    WRAP_LIMIT: tp.ClassVar[int] = 120  # PyCharm default line length
    USE_HIGH_LEVEL_LANGUAGE: tp.ClassVar[bool] = True

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
    ) -> Self:
        event_struct = EventStruct.from_bytes(reader)

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
        """NOTE: `update_signature()` should always be called after this, as this function will (re-)assign default
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
        the extra packed argument data will simply never be index), this will log a warning, and you should see error
        highlighting in your decompiled EVS script (wrong number of arguments).

        Can be called with 'local' `event_signatures` and/or `common_signatures`. Only events run with `RunCommonEvent`
        will be searched for in `common_signatures`, if given. (`RunCommonEvent` will also search for events in
        `event_signatures` first, even though this is rare.)
        """
        if not event_signatures and not common_signatures:
            return  # nothing to do...

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
        """Process event arg information for ALL instructions at once.

        Returns a dictionary that maps each (i, j) arg read range to a single generic `EventArgRepl` storing combined
        information about all individual uses (replacements) with that event arg.

        Has NO side effects.
        """
        single_event_args = {}  # type: dict[tuple[int, int], SingleEventArg]
        for instruction in self.instructions:
            for event_arg in instruction.event_arg_replacements:
                if event_arg.arg_range not in single_event_args:
                    # First occurrence of this event arg being used as a replacement.
                    single_event_args[event_arg.arg_range] = SingleEventArg(event_arg.arg_range)
                single_event_args[event_arg.arg_range].add_info(event_arg)

        # Sort into list by arg range and compute combined attributes.
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
        """Convert single event script to EVS."""
        function_name = _SPECIAL_EVENT_NAMES.get(self.event_id, f"{function_prefix}_{self.event_id}")
        function_docstring = f'"""{function_prefix} {self.event_id}"""'
        # starts with an empty '_' slot arg, if any other args exist
        self.process_all_event_arg_replacements()
        self.update_signature()

        try:
            event_flag_enum = enums_manager.check_out_enum_variable(self.event_id, Flag)
            on_rest_behavior_decorator = f"@{OnRestBehavior(self.on_rest_behavior).name}({event_flag_enum})\n"
        except enums_manager.EnumManagerError:
            on_rest_behavior_decorator = f"@{OnRestBehavior(self.on_rest_behavior).name}({self.event_id})\n"

        function_def = self.indent_and_wrap_function_def(
            function_name, self.signature.get_evs_arg_string(), wrap_limit=self.WRAP_LIMIT
        )
        function_def += f"\n    {function_docstring}"
        evs_event_string = on_rest_behavior_decorator + function_def

        instruction_lines = [instr.to_evs(enums_manager, event_signatures) for instr in self.instructions]

        if self.USE_HIGH_LEVEL_LANGUAGE:
            try:
                instruction_lines = self.high_level_evs_decompile(instruction_lines)
            except Exception as ex:
                _LOGGER.error(
                    f"Error while trying to decompile event {self.event_id} with high-level language:\n  {ex}")
                # raise

        # SIMPLE DECOMPILATION
        for instr_line in instruction_lines:
            if label_match := _LABEL_RE.match(instr_line):
                evs_event_string = evs_event_string.rstrip("\n ")  # we want exactly two newlines
                evs_event_string += f"\n\n    # --- Label {label_match.group(1)} --- #"
            new_lines = self._indent_and_wrap_instruction(instr_line, wrap_limit=self.WRAP_LIMIT, indent=4)
            # TODO: Goto comment needs to contribute to max line length for wrap. Also might just be redundant.
            # if goto_match := _GOTO_RE.match(instr_line):
            #     label = goto_match.group(1)
            #     new_lines_split = new_lines.split("\n")
            #     new_lines_split[1] = new_lines_split[1] + f"  # --> Label {label}"
            #     new_lines = "\n".join(new_lines_split)
            evs_event_string += new_lines

        return evs_event_string

    def high_level_evs_decompile(self, instruction_lines: list[str], conditions_only=False):
        """Parses basic EVS output and replaces it with Python `if/else` tests and `Await()` calls where possible.

        Note that none of the input `instruction_lines` have been indented yet, so we can add our own indentation here
        as necessary and ALL of it will be indented by the rest of `to_evs()`.

        TODO:
            - Currently, only "End/RestartIf" and "SkipIf" instructions (that do NOT skip other skip instructions) are
            being converted to `if` blocks.
            - Work to do for "If" condition decompilation:
                - Uses a modified condition-building EVS syntax that hasn't actually been implemented.
                - Main struggle is with line skips that skip OTHER skips (skip chains) or condition instructions (so
                it's ambiguous as to where the group instance should first be defined in EVS).
        """
        output_lines = []

        i = 0
        while i < len(instruction_lines):
            line = instruction_lines[i]
            if match := _HLD_IF_CONDITION_RE.match(line):
                m = match.groupdict()
                indent = m["indent"]
                finished = m["finished"] is not None
                if finished:
                    # TODO: Cannot yet decompile these.
                    output_lines.append(line)
                    i += 1
                    continue
                state = m["state"] == "True"
                condition = m["condition"]
                input_condition = m["input_condition"]
                if not state:
                    input_condition = f"not {input_condition}"

                # TODO: If condition was just defined on previous line, we could move the whole thing here.
                #  However, this veers into "lost info" territory, as we won't know what condition number the game
                #  originally used (and would have to look ahead for "finished" usage).

                if condition == "MAIN":
                    if output_lines and output_lines[-1] != "":
                        output_lines.append("")
                    output_lines += [f"{indent}MAIN.Await({input_condition})", ""]
                    i += 1
                else:
                    output_lines.append(f"{indent}{condition}.Add({input_condition})")
                    i += 1
            elif match := _HLD_IF_COMPARISON_RE.match(line):
                m = match.groupdict()
                indent = m["indent"]
                test = m["test"]
                operator = _COMPARISON_OPERATORS[m["comp"]]
                if test not in self.EMEDF_COMPARISON_TESTS:
                    output_lines.append(line)
                    i += 1
                    continue
                condition = m["condition"]
                pre_args = m["pre_args"].removeprefix(", ")
                value = m["value"]
                post_args = m["post_args"] if m["post_args"] else ""
                if condition == "MAIN":
                    if output_lines and output_lines[-1] != "":
                        output_lines.append("")
                    output_lines += [f"{indent}MAIN.Await({test}({pre_args}{post_args}) {operator} {value})", ""]
                    i += 1
                else:
                    output_lines.append(f"{indent}{condition}.Add({test}({pre_args}{post_args}) {operator} {value})")
                    i += 1
            elif match := _HLD_IF_RE.match(line):
                m = match.groupdict()
                indent = m["indent"]
                test = m["test"]
                if test not in self.EMEDF_TESTS or "if" not in self.EMEDF_TESTS[test]:
                    output_lines.append(line)
                    i += 1
                    continue  # 'if' should always be in tests dict, but just for clarity
                condition = m["condition"]
                args = m["args"].removeprefix(", ")  # no need to split or parse (and could be empty)
                if condition == "MAIN":
                    if output_lines and output_lines[-1] != "":
                        output_lines.append("")
                    output_lines += [f"{indent}MAIN.Await({test}({args}))", ""]
                    i += 1
                else:
                    output_lines.append(f"{indent}{condition}.Add({test}({args}))")
                    i += 1
            elif not conditions_only and (match := _HLD_SKIP_RE.match(line)):
                m = match.groupdict()
                indent = m["indent"]
                test = m["test"]
                line_count = int(m["line_count"])
                if line_count == 0:
                    # Occurs rarely.
                    output_lines.append(f"{line}  # NOTE: useless skip")
                    i += 1
                    continue
                args = m["args"].removeprefix(", ")
                # Find negated skip.
                for test_name, tests in self.EMEDF_TESTS.items():
                    if tests.get("skip", "") == f"SkipLinesIf{test}":
                        break
                else:
                    output_lines.append(line)
                    i += 1
                    continue  # could not find test name (possibly no negation)
                if_block_lines = [f"{indent}{instruction_lines[i + 1 + j]}" for j in range(line_count)]
                if any("SkipLinesIf" in instr for instr in if_block_lines):
                    # Cannot yet skip other skips. Ignore this line, and recur on block lines for conditions only.
                    output_lines.append(line)
                    i += 1
                    output_lines += self.high_level_evs_decompile(if_block_lines, conditions_only=True)
                    i += len(if_block_lines)
                    continue
                if any("SkipLines(" in instr for instr in (
                    if_block_lines[:-1] if len(if_block_lines) > 1 else if_block_lines
                )):
                    # Cannot yet skip other unconditional skips EXCEPT as the last block instruction (`else`).
                    output_lines.append(line)
                    i += 1
                    output_lines += self.high_level_evs_decompile(if_block_lines, conditions_only=True)
                    i += len(if_block_lines)
                    continue
                if unconditional_match := _HLD_UNCONDITIONAL_SKIP_RE.match(instruction_lines[i + line_count]):
                    else_line_count = int(unconditional_match.groupdict()["line_count"])
                    else_block_lines = [
                        f"{indent}    {instruction_lines[i + line_count + 1 + j]}" for j in range(else_line_count)
                    ]
                    if any("SkipLines" in instr for instr in else_block_lines):
                        # Cannot yet skip other skips (conditional or unconditional) in `else` block.
                        output_lines.append(line)
                        i += 1
                        output_lines += self.high_level_evs_decompile(if_block_lines, conditions_only=True)
                        i += len(if_block_lines)
                        continue
                    if_block_lines = if_block_lines[:-1]  # ignore unconditional skip
                else:
                    else_line_count = 0
                    else_block_lines = []
                output_lines.append(f"{indent}if {test_name}({args}):")
                i += 1
                # Recur on indented `if` block (which contains no skips, as per above).
                output_lines += self.high_level_evs_decompile([f"    {if_line}" for if_line in if_block_lines])
                i += line_count
                if else_block_lines:
                    # Recur on indented `else` block (which contains no skips, as per above).
                    output_lines.append(f"{indent}else:")
                    # No need for `i += 1`, as `line_count` includes the unconditional skip that `else` is replacing.
                    output_lines += self.high_level_evs_decompile(else_block_lines)
                    i += else_line_count
            elif not conditions_only and (match := _HLD_RETURN_CONDITION_RE.match(line)):
                m = match.groupdict()
                indent = m["indent"]
                return_type = m["return_type"].lower()
                finished = m["finished"] is not None
                if finished:
                    # TODO: Cannot yet decompile these.
                    output_lines.append(line)
                    i += 1
                    continue
                state = m["state"] == "True"
                condition = m["condition"]
                if not state:
                    condition = f"not {condition}"
                output_lines.append(f"{indent}if {condition}:")
                output_lines.append(f"{indent}    return{' RESTART' if return_type == 'restart' else ''}")
                i += 1
            elif not conditions_only and (match := _HLD_RETURN_RE.match(line)):
                m = match.groupdict()
                indent = m["indent"]
                return_type = m["return_type"].lower()
                test = m["test"]
                if test not in self.EMEDF_TESTS or return_type not in self.EMEDF_TESTS[test]:
                    output_lines.append(line)
                    i += 1
                    continue  # ignore (no end/restart test)
                args = m["args"].removeprefix(", ")
                output_lines.append(f"{indent}if {test}({args}):")
                output_lines.append(f"{indent}    return{' RESTART' if return_type == 'restart' else ''}")
                i += 1
            else:
                output_lines.append(line)
                i += 1

        while output_lines[-1] == "":
            output_lines = output_lines[:-1]
        return output_lines

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
                event_arg_replacements, key=lambda arg_r: (arg_r.read_from_byte, arg_r.instruction_line)
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

    @staticmethod
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
                wrapped_condition = Event._indent_and_wrap_instruction(
                    condition, wrap_limit=wrap_limit - len(existing_indent), indent=len(existing_indent) + indent
                )
                wrapped_condition = wrapped_condition.lstrip("\n ")
                return f"\n{base_indent}{existing_indent}{c_type}_{c_index}.Add({wrapped_condition})"
            elif match := _MAIN_AWAIT_RE.match(instr):
                # Indent and wrap condition.
                condition = match.group(1)
                wrapped_condition = Event._indent_and_wrap_instruction(
                    condition, wrap_limit=wrap_limit - len(existing_indent), indent=len(existing_indent) + indent
                )
                wrapped_condition = wrapped_condition.lstrip("\n ")
                return f"\n{base_indent}{existing_indent}MAIN.Await({wrapped_condition})"
            elif match := _IF_BLOCK_RE.match(instr):
                # Indent and wrap condition.
                condition = match.group(1)
                wrapped_condition = Event._indent_and_wrap_instruction(
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

    @staticmethod
    def indent_and_wrap_function_def(function_name: str, function_args, wrap_limit=120):
        one_line_def = f"def {function_name}({function_args}):"
        if len(one_line_def) <= wrap_limit:
            return one_line_def
        arg_indent = " " * 4
        arg_lines = ",\n".join(arg_indent + arg_string for arg_string in function_args.split(", "))
        return f"def {function_name}(\n{arg_lines},\n):"
