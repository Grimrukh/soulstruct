__all__ = ["Command"]

import abc

from soulstruct.game_types.internal_types import ESDType
from soulstruct.utilities import read_chars_from_buffer
from soulstruct.utilities.binary_struct import BinaryStruct

from .functions import COMMANDS
from .ezl_parser import decompile


class Command(abc.ABC):
    STRUCT: BinaryStruct = None
    ARG_STRUCT: BinaryStruct = None
    ESD_TYPE: ESDType = None

    def __init__(self, bank, index, command_args=(), indent=0):
        self.bank = bank
        self.index = index
        self.args = command_args
        self.__indent = indent

    @classmethod
    def unpack(cls, esd_buffer, commands_offset, count=1):
        """ Returns a list of Command instances. """
        commands = []
        if commands_offset == -1:
            return commands
        struct_dicts = cls.STRUCT.unpack_count(esd_buffer, count=count, offset=commands_offset)

        for d in struct_dicts:
            if d["args_offset"] > 0:
                esd_buffer.seek(d["args_offset"])
                arg_structs = cls.ARG_STRUCT.unpack_count(esd_buffer, count=d["args_count"])
                args = [
                    read_chars_from_buffer(esd_buffer, offset=a["arg_ezl_offset"], length=a["arg_ezl_size"])
                    for a in arg_structs
                ]
            else:
                args = []
            commands.append(cls(d["bank"], d["index"], args))

        return commands

    def __eq__(self, other_command):
        return (
            self.bank == other_command.bank
            and self.index == other_command.index
            and self.args == other_command.args
        )

    def __hash__(self):
        return hash((self.bank, self.index, tuple(self.args)))

    def to_esp(self, indent=2, comment=False):
        ind = "    " * indent
        c = "# " if comment else ""
        try:
            command_name, arg_names, arg_types = COMMANDS[self.ESD_TYPE][self.bank][self.index]
        except KeyError:
            if self.bank == 6:
                # Start a child state machine.
                arguments = ", ".join([f"{decompile(arg, self.ESD_TYPE)}" for arg in self.args])
                return f"{ind}{c}CALL_STATE_MACHINE[{0x80000000 - self.index}]({arguments})\n"
            command_name = f"Command_{self.ESD_TYPE.value}_{self.bank}_{self.index}"
            arg_names = ()
        if len(arg_names) != len(self.args):
            arguments = ", ".join([f"{decompile(arg, self.ESD_TYPE)}" for arg in self.args])
        else:
            arguments = ", ".join(
                [f"{arg_name}={decompile(arg, self.ESD_TYPE)}" for arg_name, arg in zip(arg_names, self.args)]
            )
        return f"{ind}{c}{command_name}({arguments})\n"

    def to_html(self):
        try:
            command_name, arg_names, arg_types = COMMANDS[self.ESD_TYPE][self.bank][self.index]
        except KeyError:
            command_name = f"Command_{self.ESD_TYPE.value}_{self.bank}_{self.index}"
            arg_names = ()
        fmt = '<br><div style="color:black;line-height:1;margin-left:{}px;">{}({})</div>'
        return fmt.format(
            20 * (2 + self.__indent),
            command_name,
            ", ".join(
                [f"{arg_name}={decompile(arg, self.ESD_TYPE)}" for arg_name, arg in zip(arg_names, self.args)]
            ),
        )
