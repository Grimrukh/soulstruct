from __future__ import annotations

__all__ = ["Condition"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.utilities.binary import *

from .command import Command
from .ezl_parser import decompile, split_by_and_or


class ConditionStruct(BinaryStruct):
    next_state_offset: varint  # offset to the actual `State` header (where `state_id` is conveniently first)
    pass_commands_offset: varint
    pass_commands_count: varint
    subcondition_pointers_offset: varint
    subcondition_pointers_count: varint
    test_ezl_offset: varint
    test_ezl_size: varint


@dataclass(slots=True)
class Condition:
    """A single condition belonging to one `State` that will send the machine to another `State` if it passes."""

    next_state_id: int
    test_ezl: bytes
    pass_commands: list[Command] = field(default_factory=list)
    subconditions: list[Condition] = field(default_factory=list)
    _indent: int = 0

    @classmethod
    def from_esd_reader(cls, reader: BinaryReader) -> tp.Self:
        header = ConditionStruct.from_bytes(reader)

        if header.pass_commands_offset > 0:
            reader.seek(header.pass_commands_offset)
            pass_commands = [Command.from_esd_reader(reader) for _ in range(header.pass_commands_count)]
        else:
            pass_commands = []

        subconditions = []
        if header.subcondition_pointers_offset > 0:
            reader.seek(header.subcondition_pointers_offset)
            subcondition_offsets = reader.unpack(f"{len(header.subcondition_pointers_count)}v")
            for offset in subcondition_offsets:
                reader.seek(offset)
                subconditions.append(Condition.from_esd_reader(reader))  # safe recursion
                # TODO: Increase _indent of subcondition?

        reader.seek(header.test_ezl_offset)
        test_ezl = reader.unpack_bytes(length=header.test_ezl_size)

        if header.next_state_offset > 0:
            reader.seek(header.next_state_offset)
            next_state_id = reader["v"]
        else:
            next_state_id = -1

        return cls(next_state_id, test_ezl, pass_commands, subconditions)

    def to_esd_writer(self, writer: BinaryWriter, state_id_offsets: dict[int, int]):
        if self.next_state_id != -1:
            try:
                next_state_offset = state_id_offsets[self.next_state_id]
            except KeyError:
                raise ValueError(f"Condition has non-existent next state ID: {self.next_state_id}.")
        else:
            next_state_offset = -1
        ConditionStruct.object_to_writer(
            self,
            writer,
            next_state_offset=next_state_offset,
            pass_commands_count=len(self.pass_commands),
            subcondition_pointers_offset=RESERVED,
            subcondition_pointers_count=len(self.subconditions),
            test_ezl_size=len(self.test_ezl),
        )

    def pack_subconditions(
        self, writer: BinaryWriter, state_id_offsets: dict[int, int], all_condition_offsets: dict[Condition, int]
    ) -> list[Condition]:
        """Pack these subconditions first, then recur on them."""
        new_conditions = []
        for subcondition in self.subconditions:
            if subcondition not in all_condition_offsets:
                all_condition_offsets[subcondition] = writer.position
                subcondition.to_esd_writer(writer, state_id_offsets)
                new_conditions.append(subcondition)
        new_subconditions = []
        for subcondition in new_conditions:
            new_subconditions += subcondition.pack_subconditions(writer, state_id_offsets, all_condition_offsets)
        return new_conditions + new_subconditions

    def pack_pass_commands(self, writer: BinaryWriter) -> int:
        """Returns the number of pass commands."""
        if not self.pass_commands:
            writer.fill("pass_commands_offset", -1, obj=self)
            return 0  # no pass commands to pack

        writer.fill_with_position("pass_commands_offset", obj=self)
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
        writer.fill_with_position("test_ezl_offset", obj=self)
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

    def pack_subconditions_pointers(
        self,
        writer: BinaryWriter,
        all_condition_offsets: dict[Condition, int],
        recurred_conditions: set[Condition],
    ) -> int:
        """Returns total number of pointers found."""
        if not self.subconditions:
            writer.fill("subcondition_pointers_offset", -1, obj=self)
            return 0

        writer.fill_with_position("subcondition_pointers_offset", obj=self)
        count = 0
        for subcondition in self.subconditions:
            try:
                subcondition_offset = all_condition_offsets[subcondition]
            except KeyError:
                raise ValueError("Could not find subcondition in packed conditions dictionary.")
            writer.pack("v", subcondition_offset)
            count += 1
        for subcondition in self.subconditions:
            if subcondition not in recurred_conditions:
                count += subcondition.pack_subconditions_pointers(writer, all_condition_offsets, recurred_conditions)
                recurred_conditions.add(subcondition)
        return count

    def __hash__(self):
        """Allows `Condition` instances to be used as dict keys, so we can track redundant instances during pack."""
        return hash((self.next_state_id, self.test_ezl, tuple(self.pass_commands), tuple(self.subconditions)))

    def __eq__(self, other_condition: Condition):
        """Required for checking if the `Condition` already exists as a dictionary key."""
        return (
            self.next_state_id == other_condition.next_state_id
            and self.test_ezl == other_condition.test_ezl
            and self.pass_commands == other_condition.pass_commands
            and self.subconditions == other_condition.subconditions
        )

    def to_esp(self, esd_type: ESDType, indent=2, comment=False):
        ind = "    " * indent

        cond_expr = decompile(self.test_ezl, esd_type)
        if len(cond_expr) >= 119 - (len(ind) + 1) - (2 if comment else 0):
            lines = split_by_and_or(cond_expr)
            if comment:
                s = f"{ind}# if (\n"
                for line in lines:
                    s += f"{ind}#     {line}\n"
                s += f"{ind}# ):\n"
            else:
                s = f"{ind}if (\n"
                for line in lines:
                    s += f"{ind}    {line}\n"
                s += f"{ind}):\n"
        elif comment:
            s = f"{ind}# if {cond_expr}:\n"
        else:
            s = f"{ind}if {cond_expr}:\n"

        print(s)

        if self.pass_commands:
            for command in self.pass_commands:
                s += command.to_esp(esd_type, indent=indent + 1, comment=comment)
        if self.subconditions:
            if len(self.subconditions) == 1 and self.subconditions[0].test_ezl == b"\x41\xa1":
                if self.subconditions[0].next_state_id != -1:
                    s += f"{ind}    return State_{self.subconditions[0].next_state_id}\n"
                else:
                    s += f"{ind}    return -1\n"
            else:
                for condition in self.subconditions:
                    s += condition.to_esp(esd_type, indent=indent + 1, comment=comment)
        if self.next_state_id != -1:
            s += f"{ind}{'#' if comment else ''}    return State_{self.next_state_id}\n"
        return s

    def to_html(self, esd_type: ESDType):
        state_fmt = '<br><div style="color:black;line-height:0.5;margin-left:{}px;">{}</div>'
        expression_fmt = (
            '<br><div style="color:black;line-height:1;margin-left:{}px;font-family:sans-serif">IF: ' "{}</div>"
        )
        command_fmt = '<br><div style="color:black;font-weight:bold;line-height:0.5;margin-left:{}px;">{}</div>'
        string = ""
        string += expression_fmt.format(20 * (2 + self._indent), decompile(self.test_ezl, esd_type))
        if self.next_state_id != -1:
            string += state_fmt.format(
                20 * (3 + self._indent),
                '---> <a href="#esd_{state_id}">State {state_id}' "</a>".format(state_id=self.next_state_id),
            )
        if self.pass_commands:
            string += command_fmt.format(20 * (2 + self._indent), "Commands:")
            for command in self.pass_commands:
                string += command.to_html(esd_type)
        if self.subconditions:
            for condition in self.subconditions:
                string += condition.to_html(esd_type)
        return string
