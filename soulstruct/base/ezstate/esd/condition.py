__all__ = ["Condition"]

import abc
import typing as tp

from soulstruct.utilities.binary import BinaryStruct, BinaryReader
from soulstruct.darksouls1ptde.game_types.internal_types import ESDType

from .command import Command
from .ezl_parser import decompile


class Condition(abc.ABC):
    """A single condition belonging to one `State` that will send the machine to another `State` if it passes."""

    STRUCT: BinaryStruct = None
    POINTER_STRUCT: BinaryStruct = None
    STATE_ID_STRUCT: BinaryStruct = None
    ESD_TYPE: ESDType = None

    Command: tp.Type[Command] = None

    def __init__(self, next_state_index, test_ezl, pass_commands=(), subconditions=(), print_indent=0):
        self.next_state_index = next_state_index
        self.test_ezl = test_ezl
        self.pass_commands = pass_commands
        self.subconditions = subconditions
        self.__indent = print_indent

    @classmethod
    def unpack(cls, esd_reader: BinaryReader, condition_pointers_offset, count=1):
        """Returns a list of `Condition` instances`."""
        conditions = []
        if condition_pointers_offset == -1:
            return conditions
        pointers = esd_reader.unpack_structs(cls.POINTER_STRUCT, count=count, offset=condition_pointers_offset)
        for p in pointers:
            d = esd_reader.unpack_struct(cls.STRUCT, offset=p["condition_offset"])
            pass_commands = cls.Command.unpack(
                esd_reader, d["pass_commands_offset"], count=d["pass_commands_count"],
            )
            subconditions = cls.unpack(  # safe recursion
                esd_reader, d["subcondition_pointers_offset"], count=d["subcondition_pointers_count"],
            )
            test_ezl = esd_reader.unpack_bytes(offset=d["test_ezl_offset"], length=d["test_ezl_size"])
            if d["next_state_offset"] > 0:
                next_state_index = esd_reader.unpack_struct(
                    cls.STATE_ID_STRUCT, offset=d["next_state_offset"]
                )["state_id"]
            else:
                next_state_index = -1
            conditions.append(cls(next_state_index, test_ezl, pass_commands, subconditions))

        return conditions

    def __hash__(self):
        """Allows `Condition` instances to be used as dict keys, so we can track redundant instances during pack."""
        return hash((self.next_state_index, self.test_ezl, tuple(self.pass_commands), tuple(self.subconditions)))

    def __eq__(self, other_condition):
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
        string += expression_fmt.format(20 * (2 + self.__indent), decompile(self.test_ezl, self.ESD_TYPE))
        if self.next_state_index != -1:
            string += state_fmt.format(
                20 * (3 + self.__indent),
                '---> <a href="#esd_{index}">State {index}' "</a>".format(index=self.next_state_index),
            )
        if self.pass_commands:
            string += command_fmt.format(20 * (2 + self.__indent), "Commands:")
            for command in self.pass_commands:
                string += command.to_html()
        if self.subconditions:
            for condition in self.subconditions:
                string += condition.to_html()
        return string
