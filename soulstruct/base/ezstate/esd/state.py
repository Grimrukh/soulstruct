from __future__ import annotations

__all__ = ["State"]

import copy
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
    state_id: varint
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

    state_id: int
    conditions: list[Condition] = field(default_factory=list)
    enter_commands: list[Command] = field(default_factory=list)
    exit_commands: list[Command] = field(default_factory=list)
    ongoing_commands: list[Command] = field(default_factory=list)

    @classmethod
    def from_esd_reader(cls, reader: BinaryReader) -> Self:
        """Unpack a `State` from ESD file binary."""

        header = StateStruct.from_bytes(reader)
        next_state_offset = reader.position  # reset at end of this call

        conditions = []
        if header.condition_pointers_offset != -1:  # otherwise, state has no conditions
            reader.seek(header.condition_pointers_offset)
            condition_offsets = reader.unpack(f"{header.condition_pointers_count}v")
            for offset in condition_offsets:
                reader.seek(offset)
                # TODO: Shared conditions will be unpacked multiple times here. Should all be unpacked in advance and
                #  keyed by offset (and copied), just like when packing. (Copying still faster than unpacking IMO.)
                conditions.append(Condition.from_esd_reader(reader))

        if header.enter_commands_offset != -1:
            reader.seek(header.enter_commands_offset)
            enter_commands = [Command.from_esd_reader(reader) for _ in range(header.enter_commands_count)]
        else:
            enter_commands = []

        if header.exit_commands_offset != -1:
            reader.seek(header.exit_commands_offset)
            exit_commands = [Command.from_esd_reader(reader) for _ in range(header.exit_commands_count)]
        else:
            exit_commands = []

        if header.ongoing_commands_offset != -1:
            reader.seek(header.ongoing_commands_offset)
            ongoing_commands = [Command.from_esd_reader(reader) for _ in range(header.ongoing_commands_count)]
        else:
            ongoing_commands = []

        reader.seek(next_state_offset)
        return cls(header.state_id, conditions, enter_commands, exit_commands, ongoing_commands)

    def copy(self) -> Self:
        """Create a deep copy of this `State`. (Needed for writing dummy duplicates of first state.)"""
        return copy.deepcopy(self)

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
        self, writer: BinaryWriter, state_id_offsets: dict[int, int], all_condition_offsets: dict[Condition, int]
    ) -> list[Condition]:
        """Pack all conditions and (recursively) subconditions in this State.

        Note that identical conditions are shared file-wide. That is, two `State`s that use the exact same `Condition`
        will shared offsets to an identical packed condition.

        Checks and updates a dictionary mapping `Condition` instances to the offsets at which they were written. This is
        required later to write the `condition_pointers`, which are near the very end of the ESD file.

        Returns a list of `Condition` instances newly created by this `State` (i.e. this State used them for the first
        time in the file). Only these Conditions will have their arguments and data packed later.
        """
        new_conditions = []  # subconditions only recursively packed for new conditions
        for condition in self.conditions:
            if condition not in all_condition_offsets:  # `Condition` and `Command` have hash/eq methods to enable this
                all_condition_offsets[condition] = writer.position
                condition.to_esd_writer(writer, state_id_offsets)
                new_conditions.append(condition)
        new_subconditions = []
        for condition in new_conditions:
            new_subconditions += condition.pack_subconditions(writer, state_id_offsets, all_condition_offsets)
        return new_conditions + new_subconditions

    def pack_commands(self, writer: BinaryWriter, conditions_to_pack: list[Condition]) -> int:
        """Returns the total number of `Command`s found in this `State`."""
        # Condition pass commands are first.
        count = 0
        # TODO: Check order that Commands appear. By State, or all Conditions first, etc...?
        for condition in conditions_to_pack:
            count += condition.pack_pass_commands(writer)
        for condition in conditions_to_pack:
            count += condition.pack_subconditions_pass_commands(writer)

        # Then State commands.

        if self.enter_commands:
            writer.fill_with_position("enter_commands_offset", obj=self)
            for command in self.enter_commands:
                command.to_esd_writer(writer)
        else:
            writer.fill("enter_commands_offset", -1, obj=self)

        if self.exit_commands:
            writer.fill_with_position("exit_commands_offset", obj=self)
            for command in self.exit_commands:
                command.to_esd_writer(writer)
        else:
            writer.fill("exit_commands_offset", -1, obj=self)

        if self.ongoing_commands:
            writer.fill_with_position("ongoing_commands_offset", obj=self)
            for command in self.ongoing_commands:
                command.to_esd_writer(writer)
        else:
            writer.fill("ongoing_commands_offset", -1, obj=self)

        count += len(self.enter_commands) + len(self.exit_commands) + len(self.ongoing_commands)
        return count

    def pack_command_args(self, writer: BinaryWriter, conditions_to_pack: list[Condition]) -> int:
        """Returns the total number of `Command` arguments found in this `State`."""
        # Condition pass commands are first.
        count = 0
        for condition in conditions_to_pack:
            count += condition.pack_pass_command_args(writer)
        for condition in conditions_to_pack:
            count += condition.pack_subconditions_pass_command_args(writer)
        # Then State commands.
        for command in self.enter_commands:
            count += command.pack_args_offsets(writer)
        for command in self.exit_commands:
            count += command.pack_args_offsets(writer)
        for command in self.ongoing_commands:
            count += command.pack_args_offsets(writer)
        return count

    def pack_condition_test_data(self, writer: BinaryWriter, conditions_to_pack: list[Condition]):
        for condition in conditions_to_pack:
            condition.pack_test_data(writer)
        for condition in conditions_to_pack:
            condition.pack_subconditions_test_data(writer)

    def pack_command_arg_data(self, writer: BinaryWriter, conditions_to_pack: list[Condition]):
        # Condition pass commands are first.
        for condition in conditions_to_pack:
            condition.pack_pass_command_arg_data(writer)
        for condition in conditions_to_pack:
            condition.pack_subconditions_pass_command_arg_data(writer)
        # Then State commands.
        for command in self.enter_commands:
            command.pack_args_data(writer)
        for command in self.exit_commands:
            command.pack_args_data(writer)
        for command in self.ongoing_commands:
            command.pack_args_data(writer)

    def pack_condition_pointers(
        self,
        writer: BinaryWriter,
        all_condition_offsets: dict[Condition, int],
        recurred_conditions: set[Condition],
    ) -> int:
        """Returns total number of `Condition` pointers used in this `State`.

        NOTE: Unlike the calls above, EVERY `Condition` in this State gets a pointer; some of those pointers may
        simply refer to the same `Condition` instance (already handled in `all_condition_offsets`).

        HOWEVER, each `Condition` instance only has its own subcondition pointers packed ONCE, which is checked with
        the `recurred_conditions` set passed in and modified here.
        """
        if not self.conditions:
            writer.fill("condition_pointers_offset", -1, obj=self)
            return 0

        writer.fill_with_position("condition_pointers_offset", obj=self)
        count = 0
        for condition in self.conditions:
            try:
                condition_offset = all_condition_offsets[condition]
            except KeyError:
                raise ValueError(f"Could not find condition of state {self.state_id} in packed conditions dictionary.")
            writer.pack("v", condition_offset)
            count += 1
        for condition in self.conditions:
            if condition not in recurred_conditions:
                # TODO: Sure would be easier if all subcondition pointers were packed first...
                # We make sure to call this only ONCE for each packed `Condition` instance.
                count += condition.pack_subconditions_pointers(writer, all_condition_offsets, recurred_conditions)
                recurred_conditions.add(condition)
        return count

    @property
    def html_title_bar(self):
        return (
            f'<br><div style="font-size:35px;font-weight:bold;margin-top:10px"><a name="esd_{self.state_id}">'
            f"EzState {self.state_id}</a></div>"
        )

    def to_esp(self, esd_type: ESDType, from_states: set = None):
        s = f"\nclass State_{self.state_id}(State):\n"  # TODO: Allow user-defined state name dict.
        s += f'    """ {self.state_id}: No description. """\n\n'

        if from_states is not None:
            from_state_list = ", ".join(("State_" + str(s) for s in sorted(from_states)))
            s += f"    def previous_states(self):\n" f"        return [{from_state_list}]\n\n"

        comment = False
        if self.enter_commands:
            s += f"    def enter(self):\n"
            for command in self.enter_commands:
                s += command.to_esp(esd_type)
            s += "\n"
        if self.conditions:
            s += f"    def test(self):\n"
            if len(self.conditions) == 1 and self.conditions[0].test_ezl == b"\x41\xa1":
                if self.conditions[0].next_state_id != -1:
                    s += f"        return State_{self.conditions[0].next_state_id}\n"
                else:
                    s += f"        return -1\n"
            else:
                for i, condition in enumerate(self.conditions):
                    if not comment and condition.test_ezl == b"\x41\xa1":
                        if i == 0:
                            s += f"        return State_{self.conditions[0].next_state_id}\n"
                        else:
                            s += f"        else:\n            return State_{condition.next_state_id}\n"
                        if i < len(self.conditions) - 1:
                            s += "        # UNREACHABLE:\n"
                            comment = True
                    else:
                        s += condition.to_esp(esd_type, comment=comment)

            s += "\n"
        if self.ongoing_commands:
            s += f"    def ongoing(self):\n"
            for command in self.ongoing_commands:
                s += command.to_esp(esd_type)
            s += "\n"
        if self.exit_commands:
            s += f"    def exit(self):\n"
            for command in self.exit_commands:
                s += command.to_esp(esd_type)
            s += "\n"
        return s

    def to_html(self, esd_type: ESDType):
        s = self.html_title_bar
        fmt = '<br><div style="font-size:20px;font-weight:bold;margin-left:10px">{}</div>'
        if self.enter_commands:
            s += fmt.format("(ENTER) Commands:")
            for command in self.enter_commands:
                s += command.to_html(esd_type)
        if self.conditions:
            s += fmt.format("State Change Conditions:")
            CLEAR_REGISTERS()
            for condition in self.conditions:
                s += condition.to_html(esd_type)
        if self.exit_commands:
            s += fmt.format("(EXIT) Commands:")
            for command in self.exit_commands:
                s += command.to_html(esd_type)
        if self.ongoing_commands:
            s += fmt.format("(ONGOING) Commands:")
            for command in self.ongoing_commands:
                s += command.to_html(esd_type)

        return s

    def __repr__(self) -> str:
        s = f"State[{self.state_id}](<{len(self.conditions)} conditions>"
        if self.enter_commands:
            s += f", <{len(self.enter_commands)} enter commands>"
        if self.ongoing_commands:
            s += f", <{len(self.ongoing_commands)} ongoing commands>"
        if self.exit_commands:
            s += f", <{len(self.exit_commands)} exit commands>"
        s += ")"
        return s
