from __future__ import annotations

__all__ = ["Event"]

import abc
import logging
import re
import struct
import typing as tp

from soulstruct.base.game_types.basic_types import Flag
from .enums import RestartType
from .instruction import Instruction, EventArg

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryStruct, BinaryReader
    from .core import EMEVD
    from .entity_enums_manager import EntityEnumsManager

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

_INSTRUCTION_RE = re.compile(r" *([\w\d]+)\((.*)\)")  # groups = (instruction_name, args)
_ARG_TUPLE_START_RE = re.compile(r"(\w[\w\d_]*)=([\[(]).*")  # groups = (arg_name, bracket_type)
_CONDITION_RE = re.compile(r" *(AND|OR)_(\d+)\.Add\((.*)\)")  # groups = (condition_type, condition_i, condition)
_MAIN_AWAIT_RE = re.compile(r" *MAIN\.Await\((.*)\)")  # groups = (condition_type, condition_i, condition)
_LABEL_RE = re.compile(r"DefineLabel\((\d+)\)")
_GOTO_RE = re.compile(r"Goto.*\(Label\.L(\d+)[,)].*")

# High-level decompilation.
_HLC_IF_CONDITION_RE = re.compile(
    r"^(?P<indent> *)If(?P<finished>Finished)?Condition(?P<state>True|False)\("
    r"(?P<condition>(MAIN|((AND|OR)_\d+))), input_condition=(?P<input_condition>(MAIN|((AND|OR)_\d+)))\)$"
)
_HLC_IF_COMPARISON_RE = re.compile(
    r"^(?P<indent> *)If(?P<test>.*?)(?P<comp>Equal|NotEqual|GreaterThan|LessThan|GreaterThanOrEqual|LessThanOrEqual)"
    r"\((?P<condition>(MAIN|((AND|OR)_\d+)))(?P<pre_args>.*?), value=(?P<value>[\w\d_.]+)(?P<post_args>, .*?)?\)$"
)
_HLC_IF_RE = re.compile(
    r"^(?P<indent> *)If(?P<test>.*)\((?P<condition>(MAIN|((AND|OR)_\d+)))(?P<args>.*?)\)$"
)
_HLC_SKIP_RE = re.compile(
    r"^(?P<indent> *)SkipLinesIf(?P<test>.*)\((?P<line_count>\d+)(?P<args>.*?)\)$"
)
_HLC_UNCONDITIONAL_SKIP_RE = re.compile(
    r"^(?P<indent> *)SkipLines\((?P<line_count>\d+)\)$"
)
_HLC_RETURN_CONDITION_RE = re.compile(
    r"^(?P<indent> *)(?P<return_type>End|Restart)If(?P<finished>Finished)?Condition(?P<state>True|False)\("
    r"input_condition=(?P<condition>((AND|OR)_\d+))\)$"
)
_HLC_RETURN_RE = re.compile(
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


class Event(abc.ABC):

    instructions: list[Instruction]

    HEADER_STRUCT: BinaryStruct
    Instruction: tp.Type[Instruction]
    EventArg: tp.Type[EventArg]
    EMEDF_TESTS: dict[str, dict[str, str]]
    EMEDF_COMPARISON_TESTS: dict[str, dict[str, str]]
    WRAP_LIMIT = 120  # PyCharm default line length
    USE_HIGH_LEVEL_LANGUAGE = True

    def __init__(self, event_id=0, restart_type=0, instructions=None):
        self.event_id = event_id
        self.restart_type = restart_type
        self.instructions = instructions if instructions else []

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

            if event_id := d["event_id"] in event_dict:
                _LOGGER.warning(
                    f"Event ID {event_id} appears multiple times in EMEVD file. Only the first one will be kept."
                )
            else:
                event_dict[d["event_id"]] = cls(d["event_id"], d["restart_type"], instruction_list)

        return event_dict

    def update_run_event_instructions(self, all_event_arg_fmts: dict[int, str], common_func_emevd: EMEVD = None):
        """Iterates over instructions and updates any `RunEvent` or `RunCommonEvent` instructions with event arguments
        with their proper `args` and `arg_types` values.

        Called after all events have been loaded and `update_evs_function_args()` has been called (to scan events and
        detect their arguments).
        """
        all_common_arg_fmts = common_func_emevd.all_event_arg_fmts if common_func_emevd else {}

        for instruction in self.instructions:
            if (event_id := instruction.get_called_event()) is not None:
                if event_id in all_event_arg_fmts:
                    var_format = all_event_arg_fmts[event_id]
                else:
                    # Event is not defined locally. Check common events, if provided.
                    # TODO: These special indices (0, 6) should be defined more centrally.
                    if instruction.index == 6 and event_id in all_common_arg_fmts:
                        var_format = all_common_arg_fmts[event_id]
                    else:
                        if instruction.index == 0:
                            _LOGGER.warning(f"Map event {event_id} was run, but is not defined in map.")
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

    def process_all_event_args(self) -> dict[tuple[int, int], EventArg]:
        """Process event arg information for ALL instructions at once.

        Returns a dictionary that maps each (i, j) arg read range to a single generic `EventArg` storing combined
        information about all individual uses (replacements) with that event arg.
        """
        all_event_args = {}
        for instruction in self.instructions:
            try:
                instruction.process_event_args()
            except ValueError as ex:
                raise ValueError(
                    f"Error occurred while processing event args in instruction "
                    f"{self.instructions.index(instruction)}, {instruction.instruction_id}], of "
                    f"event {self.event_id}.\n    Error: {ex}"
                )
            for event_arg in instruction.event_args:
                if event_arg.arg_range not in all_event_args:
                    all_event_args[event_arg.arg_range] = self.EventArg.generic(event_arg.arg_range)
                all_event_args[event_arg.arg_range].add_info(event_arg)

        # Sort by arg range before returning.
        return {arg_range: all_event_args[arg_range] for arg_range in sorted(all_event_args)}

    def update_evs_function_args(
        self,
        all_event_arg_names: dict,
        all_event_arg_fmts: dict,
        all_event_arg_types: dict,
    ):
        all_event_args = self.process_all_event_args()
        all_arg_names = []
        all_arg_fmts = []
        all_arg_py_types = []

        for (i, j), generic_event_arg in all_event_args.items():
            generic_event_arg.remove_generic_names()
            arg_name, arg_fmt, arg_py_types = generic_event_arg.get_combined_info(all_arg_names, self.event_id)

            default_arg_name = f"arg_{i}_{j}"
            for instruction in self.instructions:
                # Replace default arg name with detected EVS arg name.
                for arg_index, old_arg_name in enumerate(instruction.evs_args_list):
                    if old_arg_name == default_arg_name:
                        instruction.evs_args_list[arg_index] = arg_name

            all_arg_names.append(arg_name)
            all_arg_fmts.append(arg_fmt)
            all_arg_py_types.append(arg_py_types)

        # TODO: Event argument type hint should be able to be a single game type, if possible.
        evs_function_arg_strings = [
            f"{arg_name}: {EVS_ARG_TYPES[arg_type]}" for arg_name, arg_type in zip(all_arg_names, all_arg_fmts)
        ]
        if evs_function_arg_strings:
            evs_function_arg_strings = ["_"] + evs_function_arg_strings  # prepend blank argument for slot intellisense

        # TODO: warn/raise if key already exists.
        all_event_arg_names[self.event_id] = all_arg_names
        all_event_arg_fmts[self.event_id] = "".join(all_arg_fmts)
        all_event_arg_types[self.event_id] = all_arg_py_types

        return ", ".join(evs_function_arg_strings)

    def to_evs(
        self,
        enums_manager: EntityEnumsManager,
        all_event_arg_names: dict,
        all_event_arg_fmts: dict,
        all_event_arg_types: dict,
        is_common_func=False,
    ) -> str:
        """Convert single event script to EVS."""
        function_name = _SPECIAL_EVENT_NAMES.get(
            self.event_id, f"CommonFunc_{self.event_id}" if is_common_func else f"Event_{self.event_id}"
        )
        function_docstring = f'"""{"CommonFunc" if is_common_func else "Event"} {self.event_id}"""'
        # starts with an empty '_' slot arg, if any other args exist
        function_args = self.update_evs_function_args(
            all_event_arg_names,
            all_event_arg_fmts,
            all_event_arg_types,
        )

        try:
            event_flag_enum = enums_manager.check_out_enum(self.event_id, Flag)
            restart_type_decorator = f"@{RestartType(self.restart_type).name}({event_flag_enum})\n"
        except enums_manager.MissingEntityError:
            restart_type_decorator = f"@{RestartType(self.restart_type).name}({self.event_id})\n"

        function_def = self.indent_and_wrap_function_def(function_name, function_args, wrap_limit=self.WRAP_LIMIT)
        function_def += f"\n    {function_docstring}"
        evs_event_string = restart_type_decorator + function_def

        instruction_lines = [instr.to_evs(enums_manager, all_event_arg_fmts) for instr in self.instructions]

        if self.USE_HIGH_LEVEL_LANGUAGE:
            try:
                instruction_lines = self.high_level_evs_decompile(instruction_lines)
            except Exception as ex:
                _LOGGER.error(
                    f"Error while trying to decompile event {self.event_id} with high-level language:\n  {ex}")
                raise

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
            if match := _HLC_IF_CONDITION_RE.match(line):
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
            elif match := _HLC_IF_COMPARISON_RE.match(line):
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
            elif match := _HLC_IF_RE.match(line):
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
            elif not conditions_only and (match := _HLC_SKIP_RE.match(line)):
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
                if unconditional_match := _HLC_UNCONDITIONAL_SKIP_RE.match(instruction_lines[i + line_count]):
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
            elif not conditions_only and (match := _HLC_RETURN_CONDITION_RE.match(line)):
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
            elif not conditions_only and (match := _HLC_RETURN_RE.match(line)):
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
        for i, instruction in enumerate(self.instructions):
            # print(f"    Instruction {i} ({instruction.category}, {instruction.index})")
            instructions_binary += instruction.to_binary(base_arg_offset)

            arg_binary = instruction.args_list_to_binary()
            # print(f"        Offset {hex(0x33600 + base_arg_offset)}: {arg_binary}")
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
            else:
                raise ValueError(f"Cannot indent/wrap malformed instruction or condition group definition: {instr}")

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
