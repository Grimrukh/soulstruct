from __future__ import annotations

__all__ = ["State"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.utilities.binary import *

from .command import Command
from .condition import Condition
from .ezl_parser import CLEAR_REGISTERS

try:
    Self = tp.Self
except AttributeError:
    Self = "State"


@dataclass(slots=True)
class StateStruct(BinaryStruct):
    index: varint
    condition_pointers_offset: varint
    condition_pointers_count: varint
    enter_commands_offset: varint
    enter_commands_count: varint
    exit_commands_offset: varint
    exit_commands_count: varint
    ongoing_commands_offset: varint
    ongoing_commands_count: varint


@dataclass(slots=True)
class State:
    """A single state that the EzState machine (ESD file) can occupy at a moment in time.

    Lists of enter, ongoing (per frame), and exit `Command`s may be executed.

    A list of `Condition`s is checked each frame to see if the state machine should change to a new state.
    """
    ESD_TYPE: tp.ClassVar[ESDType]

    index: int
    conditions: list[Condition] = field(default_factory=list)
    enter_commands: list[Command] = field(default_factory=list)
    exit_commands: list[Command] = field(default_factory=list)
    ongoing_commands: list[Command] = field(default_factory=list)

    @classmethod
    def from_esd_reader(cls, reader: BinaryReader) -> Self:
        """Unpack a `State` from ESD file binary."""

        state_struct = StateStruct.from_bytes(reader)

        conditions = []
        if state_struct.condition_pointers_offset != -1:  # otherwise, state has no conditions
            reader.seek(state_struct.condition_pointers_offset)
            condition_offsets = reader.unpack(f"{len(state_struct.condition_pointers_count)}v")
            for offset in condition_offsets:
                reader.seek(offset)
                conditions.append(Condition.from_esd_reader(reader))

        if state_struct.enter_commands_offset != -1:
            reader.seek(state_struct.enter_commands_offset)
            enter_commands = [Command.from_esd_reader(reader) for _ in range(state_struct.enter_commands_count)]
        else:
            enter_commands = []

        if state_struct.exit_commands_offset != -1:
            reader.seek(state_struct.exit_commands_offset)
            exit_commands = [Command.from_esd_reader(reader) for _ in range(state_struct.exit_commands_count)]
        else:
            exit_commands = []

        if state_struct.ongoing_commands_offset != -1:
            reader.seek(state_struct.ongoing_commands_offset)
            ongoing_commands = [Command.from_esd_reader(reader) for _ in range(state_struct.ongoing_commands_count)]
        else:
            ongoing_commands = []

        return cls(state_struct.index, conditions, enter_commands, exit_commands, ongoing_commands)

    def to_esd_writer(self, writer: BinaryWriter):
        StateStruct.object_to_writer(
            self,
            writer,
            condition_pointers_count=len(self.conditions),
            enter_commands_count=len(self.enter_commands),
            exit_commands_count=len(self.exit_commands),
            ongoing_commands_count=len(self.ongoing_commands),
        )

    def pack_conditions(
        self, writer: BinaryWriter, state_index_offsets: dict[int, int], all_condition_offsets: dict[Condition, int]
    ):
        """Pack all conditions and (recursively) subconditions in this State.

        Checks and updates a dictionary mapping `Condition` instances to the offsets at which they were written. This is
        required later to write the `condition_pointers`, which are near the very end of the ESD file.
        """
        # Pack condition headers first, then recur on subconditions.
        for condition in self.conditions:
            if condition not in all_condition_offsets:  # `Condition` and `Command` have hash/eq methods to enable this
                all_condition_offsets[condition] = writer.position
                condition.to_esd_writer(writer, state_index_offsets)
        for condition in self.conditions:
            condition.pack_subconditions(writer, state_index_offsets, all_condition_offsets)

    def pack_commands(self, writer: BinaryWriter) -> int:
        """Returns the total number of `Command`s found in this `State`."""
        # Condition pass commands are first.
        count = 0
        for condition in self.conditions:
            count += condition.pack_pass_commands(writer)
        for condition in self.conditions:
            count += condition.pack_subconditions_pass_commands(writer)
        # Then State commands.
        for command in self.enter_commands:
            command.to_esd_writer(writer)
        for command in self.exit_commands:
            command.to_esd_writer(writer)
        for command in self.ongoing_commands:
            command.to_esd_writer(writer)
        count += len(self.enter_commands) + len(self.exit_commands) + len(self.ongoing_commands)
        return count

    def pack_command_args(self, writer: BinaryWriter) -> int:
        """Returns the total number of `Command` arguments found in this `State`."""
        # Condition pass commands are first.
        count = 0
        for condition in self.conditions:
            count += condition.pack_pass_command_args(writer)
        for condition in self.conditions:
            count += condition.pack_subconditions_pass_command_args(writer)
        # Then State commands.
        for command in self.enter_commands:
            count += command.pack_args_offsets(writer)
        for command in self.exit_commands:
            count += command.pack_args_offsets(writer)
        for command in self.ongoing_commands:
            count += command.pack_args_offsets(writer)
        return count

    def pack_condition_test_data(self, writer: BinaryWriter):
        for condition in self.conditions:
            condition.pack_test_data(writer)
        for condition in self.conditions:
            condition.pack_subconditions_test_data(writer)

    def pack_command_arg_data(self, writer: BinaryWriter):
        # Condition pass commands are first.
        for condition in self.conditions:
            condition.pack_pass_command_arg_data(writer)
        for condition in self.conditions:
            condition.pack_subconditions_pass_command_arg_data(writer)
        # Then State commands.
        for command in self.enter_commands:
            command.pack_args_data(writer)
        for command in self.exit_commands:
            command.pack_args_data(writer)
        for command in self.ongoing_commands:
            command.pack_args_data(writer)

    def pack_condition_pointers(self, writer: BinaryWriter, all_condition_offsets: dict[Condition, int]) -> int:
        """Returns total number of `Condition` pointers used in this `State`."""
        if not self.conditions:
            writer.fill("condition_pointers_offset", -1 , obj=self)
            return 0

        writer.fill_with_position("condition_pointers_offset", obj=self)
        count = 0
        for condition in self.conditions:
            try:
                condition_offset = all_condition_offsets[condition]
            except KeyError:
                raise ValueError(f"Could not find condition of state {self.index} in packed conditions dictionary.")
            writer.pack("v", condition_offset)
            count += 1
        for condition in self.conditions:
            count += condition.pack_subconditions_pointers(writer, all_condition_offsets)
        return count

    @property
    def html_title_bar(self):
        return (
            f'<br><div style="font-size:35px;font-weight:bold;margin-top:10px"><a name="esd_{self.index}">'
            f"EzState {self.index}</a></div>"
        )

    def to_esp(self, from_states: set = None):
        s = f"\nclass State_{self.index}(State):\n"  # TODO: Allow user-defined state name dict.
        s += f'    """ {self.index}: No description. """\n\n'

        if from_states is not None:
            from_state_list = ", ".join(("State_" + str(s) for s in sorted(from_states)))
            s += f"    def previous_states(self):\n" f"        return [{from_state_list}]\n\n"

        comment = False
        if self.enter_commands:
            s += f"    def enter(self):\n"
            for command in self.enter_commands:
                s += command.to_esp()
            s += "\n"
        if self.conditions:
            s += f"    def test(self):\n"
            if len(self.conditions) == 1 and self.conditions[0].test_ezl == b"\x41\xa1":
                if self.conditions[0].next_state_index != -1:
                    s += f"        return State_{self.conditions[0].next_state_index}\n"
                else:
                    s += f"        return -1\n"
            else:
                for i, condition in enumerate(self.conditions):
                    if not comment and condition.test_ezl == b"\x41\xa1":
                        if i == 0:
                            s += f"        return State_{self.conditions[0].next_state_index}\n"
                        else:
                            s += f"        else:\n            return State_{condition.next_state_index}\n"
                        if i < len(self.conditions) - 1:
                            s += "        # UNREACHABLE:\n"
                            comment = True
                    else:
                        s += condition.to_esp(comment=comment)

            s += "\n"
        if self.ongoing_commands:
            s += f"    def ongoing(self):\n"
            for command in self.ongoing_commands:
                s += command.to_esp()
            s += "\n"
        if self.exit_commands:
            s += f"    def exit(self):\n"
            for command in self.exit_commands:
                s += command.to_esp()
            s += "\n"
        return s

    def to_html(self):
        s = self.html_title_bar
        fmt = '<br><div style="font-size:20px;font-weight:bold;margin-left:10px">{}</div>'
        if self.enter_commands:
            s += fmt.format("(ENTER) Commands:")
            for command in self.enter_commands:
                s += command.to_html()
        if self.conditions:
            s += fmt.format("State Change Conditions:")
            CLEAR_REGISTERS()
            for condition in self.conditions:
                s += condition.to_html()
        if self.exit_commands:
            s += fmt.format("(EXIT) Commands:")
            for command in self.exit_commands:
                s += command.to_html()
        if self.ongoing_commands:
            s += fmt.format("(ONGOING) Commands:")
            for command in self.ongoing_commands:
                s += command.to_html()

        return s

    def __repr__(self) -> str:
        s = f"State[{self.index}](<{len(self.conditions)} conditions>"
        if self.enter_commands:
            s += f", <{len(self.enter_commands)} enter commands>"
        if self.ongoing_commands:
            s += f", <{len(self.ongoing_commands)} ongoing commands>"
        if self.exit_commands:
            s += f", <{len(self.exit_commands)} exit commands>"
        s += ")"
        return s
