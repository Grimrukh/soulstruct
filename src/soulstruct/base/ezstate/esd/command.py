from __future__ import annotations

__all__ = ["Command"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.utilities.binary import *

from .functions import COMMANDS
from .ezl_parser import decompile


class CommandStruct(BinaryStruct):
    bank: int
    index: int
    args_offset: varint
    args_count: varint


class CommandArgsStruct(BinaryStruct):
    arg_ezl_offset: varint
    arg_ezl_size: varint


@dataclass(slots=True)
class Command:

    bank: int
    index: int
    args: list[bytes] = field(default_factory=list)
    _indent: int = 0

    @classmethod
    def from_esd_reader(cls, reader: BinaryReader) -> tp.Self:
        """ Returns a list of Command instances. """
        header = CommandStruct.from_bytes(reader)

        args = []
        if header.args_offset > 0:
            with reader.temp_offset(header.args_offset):
                for _ in range(header.args_count):
                    arg_struct = CommandArgsStruct.from_bytes(reader)
                    args.append(reader.unpack_bytes(length=arg_struct.arg_ezl_size, offset=arg_struct.arg_ezl_offset))

        return cls(header.bank, header.index, args)

    def to_esd_writer(self, writer: BinaryWriter):
        CommandStruct.object_to_writer(self, writer, args_count=len(self.args))

    def pack_args_offsets(self, writer: BinaryWriter) -> int:
        """Pack offsets to packed EZL arg data. Returns number of args."""
        if not self.args:
            writer.fill("args_offset", -1, obj=self)
            return 0

        writer.fill_with_position("args_offset", obj=self)
        for arg_bytes in self.args:
            # Offsets are reserved using the bytes object IDs, so we don't use `CommandArgsStruct`.
            writer.reserve("arg_ezl_offset", "v", obj=arg_bytes)
            writer.pack("v", len(arg_bytes))
        return len(self.args)

    def pack_args_data(self, writer: BinaryWriter):
        """Pack EZL bytes."""
        # TODO: Conditions and commands are currently intermingled (ordered by state), which is not true for the
        #  original resources (where all condition data comes before all command data), but it shouldn't matter at all.
        for arg_bytes in self.args:
            writer.fill_with_position("arg_ezl_offset", obj=arg_bytes)
            writer.append(arg_bytes)

    def __hash__(self):
        return hash((self.bank, self.index, tuple(self.args)))

    def __eq__(self, other_command: Command):
        return (
            self.bank == other_command.bank
            and self.index == other_command.index
            and self.args == other_command.args
        )

    def to_esp(self, esd_type: ESDType, indent=2, comment=False):
        ind = "    " * indent
        c = "# " if comment else ""
        try:
            command_name, arg_names, arg_types = COMMANDS[esd_type][self.bank][self.index]
        except KeyError:
            if self.bank == 6:
                # Start a child state machine.
                arguments = ", ".join([f"{decompile(arg, esd_type)}" for arg in self.args])
                return f"{ind}{c}CALL_STATE_MACHINE[{0x80000000 - self.index}]({arguments})\n"
            command_name = f"Command_{esd_type.value}_{self.bank}_{self.index}"
            arg_names = ()
        if len(arg_names) != len(self.args):
            arguments = ", ".join([f"{decompile(arg, esd_type)}" for arg in self.args])
        else:
            arguments = ", ".join(
                [f"{arg_name}={decompile(arg, esd_type)}" for arg_name, arg in zip(arg_names, self.args)]
            )
        return f"{ind}{c}{command_name}({arguments})\n"

    def to_html(self, esd_type: ESDType):
        try:
            command_name, arg_names, arg_types = COMMANDS[esd_type][self.bank][self.index]
        except KeyError:
            command_name = f"Command_{esd_type.value}_{self.bank}_{self.index}"
            arg_names = ()
        fmt = '<br><div style="color:black;line-height:1;margin-left:{}px;">{}({})</div>'
        return fmt.format(
            20 * (2 + self._indent),
            command_name,
            ", ".join(
                [f"{arg_name}={decompile(arg, esd_type)}" for arg_name, arg in zip(arg_names, self.args)]
            ),
        )
