from __future__ import annotations

__all__ = ["State"]

import abc
import typing as tp

from soulstruct.darksouls1ptde.game_types.internal_types import ESDType

from .command import Command
from .condition import Condition
from .ezl_parser import CLEAR_REGISTERS

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryStruct, BinaryReader


class State(abc.ABC):
    """A single state that the EzState machine (ESD file) can occupy at a moment in time.

    Lists of enter, ongoing (per frame), and exit `Command`s may be executed.

    A list of `Condition`s is checked each frame to see if the state machine should change to a new state.
    """

    STRUCT: BinaryStruct = None
    ESD_TYPE: ESDType = None

    Condition: tp.Type[Condition] = None
    Command: tp.Type[Command] = None

    def __init__(self, index, conditions, enter_commands, exit_commands, ongoing_commands):
        self.index = index
        self.conditions = conditions  # type: list[Condition]
        self.enter_commands = enter_commands  # type: list[Command]
        self.exit_commands = exit_commands  # type: list[Command]
        self.ongoing_commands = ongoing_commands  # type: list[Command]

    @classmethod
    def unpack(cls, esd_reader: BinaryReader, state_machine_offset, count) -> dict[int, State]:
        """Unpack multiple states from the same state table.

        Returns a dictionary of states, because it's always possible (if yet unseen) that state indices are not
        contiguous. State 0 is not repeated, as it generally is in the packed table.
        """

        state_dict = {}
        esd_reader.seek(state_machine_offset)
        struct_dicts = esd_reader.unpack_structs(cls.STRUCT, count=count)

        for d in struct_dicts:
            conditions = cls.Condition.unpack(
                esd_reader, d["condition_pointers_offset"], count=d["condition_pointers_count"],
            )

            enter_commands = cls.Command.unpack(
                esd_reader, d["enter_commands_offset"], count=d["enter_commands_count"],
            )

            exit_commands = cls.Command.unpack(
                esd_reader, d["exit_commands_offset"], count=d["exit_commands_count"],
            )

            ongoing_commands = cls.Command.unpack(
                esd_reader, d["ongoing_commands_offset"], count=d["ongoing_commands_count"],
            )

            # State 0 will be overwritten when repeated at the end of the table, rather than added.
            state_dict[d["index"]] = cls(
                d["index"], conditions, enter_commands, exit_commands, ongoing_commands,
            )

        return state_dict

    def __eq__(self, other_state):
        return self.__dict__ == other_state.__dict__

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
