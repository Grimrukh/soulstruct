from __future__ import annotations

__all__ = ["Condition"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.utilities.binary import *

from .command import Command
from .ezl_parser import decompile

try:
    Self = tp.Self
except AttributeError:
    Self = "Condition"


@dataclass(slots=True)
class ConditionStruct(NewBinaryStruct):
    next_state_offset: varint  # offset to the actual `State` header (where `index` is conveniently first)
    pass_commands_offset: varint
    pass_commands_count: varint
    subcondition_pointers_offset: varint
    subcondition_pointers_count: varint
    test_ezl_offset: varint
    test_ezl_size: varint


@dataclass(slots=True)
class Condition:
    """A single condition belonging to one `State` that will send the machine to another `State` if it passes."""
    ESD_TYPE: tp.ClassVar[ESDType]

    next_state_index: int
    test_ezl: bytes
    pass_commands: list[Command] = field(default_factory=list)
    subconditions: list[Condition] = field(default_factory=list)
    _indent: int = 0

    @classmethod
    def from_esd_reader(cls, reader: BinaryReader) -> Self:
        condition_struct = ConditionStruct.from_bytes(reader)

        if condition_struct.pass_commands_offset > 0:
            reader.seek(condition_struct.pass_commands_offset)
            pass_commands = [Command.from_esd_reader(reader) for _ in range(condition_struct.pass_commands_count)]
        else:
            pass_commands = []

        subconditions = []
        if condition_struct.subcondition_pointers_offset > 0:
            reader.seek(condition_struct.subcondition_pointers_offset)
            subcondition_offsets = reader.unpack(f"{len(condition_struct.subcondition_pointers_count)}v")
            for offset in subcondition_offsets:
                reader.seek(offset)
                subconditions.append(Condition.from_esd_reader(reader))  # safe recursion
                # TODO: Increase _indent of subcondition?

        reader.seek(condition_struct.test_ezl_offset)
        test_ezl = reader.unpack_bytes(length=condition_struct.test_ezl_size)

        if condition_struct.next_state_offset > 0:
            reader.seek(condition_struct.next_state_offset)
            next_state_index = reader.unpack_value("v")
        else:
            next_state_index = -1

        return cls(next_state_index, test_ezl, pass_commands, subconditions)

    def to_esd_writer(self, writer: BinaryWriter, state_index_offsets: dict[int, int]):
        if self.next_state_index != -1:
            try:
                next_state_offset = state_index_offsets[self.next_state_index]
            except KeyError:
                raise ValueError(f"Condition has non-existent next state index: {self.next_state_index}.")
        else:
            next_state_offset = -1
        ConditionStruct.object_to_writer(
            self,
            writer,
            next_state_offset=next_state_offset,
            pass_commands_count=len(self.pass_commands),
            subcondition_pointers_count=len(self.subconditions),
            test_ezl_size=len(self.test_ezl),
        )

    def pack_subconditions(
        self, writer: BinaryWriter, state_index_offsets: dict[int, int], all_conditions: dict[Condition, int]
    ):
        if not self.subconditions:
            writer.fill("subconditions_offset", -1, self)
            return  # no subconditions to pack

        writer.fill_with_position("subconditions_offset", self)
        # Pack these subconditions first, then recur on them.
        for subcondition in self.subconditions:
            if subcondition not in all_conditions:
                all_conditions[subcondition] = writer.position
                subcondition.to_esd_writer(writer, state_index_offsets)
        for subcondition in self.subconditions:
            subcondition.pack_subconditions(writer, state_index_offsets, all_conditions)

    def pack_pass_commands(self, writer: BinaryWriter) -> int:
        """Returns the number of pass commands."""
        if not self.pass_commands:
            writer.fill("pass_commands_offset", -1, self)
            return 0  # no pass commands to pack

        writer.fill_with_position("pass_commands_offset", self)
        for pass_command in self.pass_commands:
            pass_command.to_esd_writer(writer)
        return len(self.pass_commands)

    def pack_subconditions_pass_commands(self, writer: BinaryWriter) -> int:
        """Returns the number of pass commands found."""
        count = 0
        for subcondition in self.subconditions:
            count += subcondition.pack_pass_commands(writer)
        for subcondition in self.subconditions:
            count += subcondition.pack_subconditions_pass_commands(writer)
        return count

    def pack_pass_command_args(self, writer: BinaryWriter) -> int:
        """Returns total number of pass command args."""
        count = 0
        for pass_command in self.pass_commands:
            count += pass_command.pack_args_offsets(writer)
        return count

    def pack_subconditions_pass_command_args(self, writer: BinaryWriter) -> int:
        """Returns total number of pass command args."""
        count = 0
        for subcondition in self.subconditions:
            count += subcondition.pack_pass_command_args(writer)
        for subcondition in self.subconditions:
            count += subcondition.pack_subconditions_pass_command_args(writer)
        return count

    def pack_test_data(self, writer: BinaryWriter):
        writer.fill_with_position("test_ezl_offset", self)
        writer.append(self.test_ezl)

    def pack_subconditions_test_data(self, writer: BinaryWriter):
        for subcondition in self.subconditions:
            subcondition.pack_test_data(writer)
        for subcondition in self.subconditions:
            subcondition.pack_subconditions_test_data(writer)

    def pack_pass_command_arg_data(self, writer: BinaryWriter):
        for pass_command in self.pass_commands:
            pass_command.pack_args_data(writer)

    def pack_subconditions_pass_command_arg_data(self, writer: BinaryWriter):
        for subcondition in self.subconditions:
            subcondition.pack_pass_command_arg_data(writer)
        for subcondition in self.subconditions:
            subcondition.pack_subconditions_pass_command_arg_data(writer)

    def pack_subconditions_pointers(self, writer: BinaryWriter, all_condition_offsets: dict[Condition, int]) -> int:
        """Returns total number of pointers found."""
        if not self.subconditions:
            writer.fill("subcondition_pointers_offset", -1, self)
            return 0

        writer.fill_with_position("subcondition_pointers_offset", self)
        count = 0
        for subcondition in self.subconditions:
            try:
                subcondition_offset = all_condition_offsets[subcondition]
            except KeyError:
                raise ValueError("Could not find subcondition in packed conditions dictionary.")
            writer.pack("v", subcondition_offset)
            count += 1
        for subcondition in self.subconditions:
            count += subcondition.pack_subconditions_pointers(writer, all_condition_offsets)
        return count

    def __hash__(self):
        """Allows `Condition` instances to be used as dict keys, so we can track redundant instances during pack."""
        return hash((self.next_state_index, self.test_ezl, tuple(self.pass_commands), tuple(self.subconditions)))

    def __eq__(self, other_condition: Condition):
        """Required for checking if the `Condition` already exists as a dictionary key."""
        return (
            self.next_state_index == other_condition.next_state_index
            and self.test_ezl == other_condition.test_ezl
            and self.pass_commands == other_condition.pass_commands
            and self.subconditions == other_condition.subconditions
        )

    def to_esp(self, indent=2, comment=False):
        ind = "    " * indent
        c = "# " if comment else ""
        s = f"{ind}{c}if {decompile(self.test_ezl, self.ESD_TYPE)}:\n"
        if self.pass_commands:
            for command in self.pass_commands:
                s += command.to_esp(indent=indent + 1, comment=comment)
        if self.subconditions:
            if len(self.subconditions) == 1 and self.subconditions[0].test_ezl == b"\x41\xa1":
                if self.subconditions[0].next_state_index != -1:
                    s += f"{ind}    return State_{self.subconditions[0].next_state_index}\n"
                else:
                    s += f"{ind}    return -1\n"
            else:
                for condition in self.subconditions:
                    s += condition.to_esp(indent=indent + 1, comment=comment)
        if self.next_state_index != -1:
            s += f"{ind}{c}    return State_{self.next_state_index}\n"
        return s

    def to_html(self):
        state_fmt = '<br><div style="color:black;line-height:0.5;margin-left:{}px;">{}</div>'
        expression_fmt = (
            '<br><div style="color:black;line-height:1;margin-left:{}px;font-family:sans-serif">IF: ' "{}</div>"
        )
        command_fmt = '<br><div style="color:black;font-weight:bold;line-height:0.5;margin-left:{}px;">{}</div>'
        string = ""
        string += expression_fmt.format(20 * (2 + self._indent), decompile(self.test_ezl, self.ESD_TYPE))
        if self.next_state_index != -1:
            string += state_fmt.format(
                20 * (3 + self._indent),
                '---> <a href="#esd_{index}">State {index}' "</a>".format(index=self.next_state_index),
            )
        if self.pass_commands:
            string += command_fmt.format(20 * (2 + self._indent), "Commands:")
            for command in self.pass_commands:
                string += command.to_html()
        if self.subconditions:
            for condition in self.subconditions:
                string += condition.to_html()
        return string
