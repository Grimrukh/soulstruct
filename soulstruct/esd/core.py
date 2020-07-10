import ast
import copy
import logging
import re
import struct
from collections import OrderedDict
from io import BytesIO
from pathlib import Path
from typing import List, Dict

from soulstruct.utilities.core import BinaryStruct, read_chars_from_buffer
from soulstruct.dcx import DCX

from .esp import ESPCompiler
from .ezl_parser import decompile, SET_INTERNAL_SYMBOLS, CLEAR_REGISTERS
from .functions import COMMANDS

__all__ = ["BaseESD", "get_esd_class"]
_LOGGER = logging.getLogger(__name__)


class BaseESD(object):

    EXTERNAL_HEADER_STRUCT = None  # type: BinaryStruct
    INTERNAL_HEADER_STRUCT = None  # type: BinaryStruct
    STATE_MACHINE_HEADER_STRUCT = None  # type: BinaryStruct
    DCX_MAGIC = None

    class State(object):

        STRUCT = None  # type: BinaryStruct
        Condition = None
        Command = None

        def __init__(self, esd_type, index, conditions, enter_commands, exit_commands, ongoing_commands):
            self.index = index
            self.conditions = conditions  # type: List[BaseESD.Condition]
            self.enter_commands = enter_commands  # type: List[BaseESD.Command]
            self.exit_commands = exit_commands  # type: List[BaseESD.Command]
            self.ongoing_commands = ongoing_commands  # type: List[BaseESD.Command]
            self.esd_type = esd_type

        @classmethod
        def unpack(cls, esd_type, esd_buffer, state_machine_offset, count):
            """Unpack multiple states from the same state table.

            Returns a dictionary of states, because it's always possible (if yet unseen) that state indices are not
            contiguous. State 0 is not repeated, as it generally is in the packed table.
            """

            state_dict = OrderedDict()
            esd_buffer.seek(state_machine_offset)
            struct_dicts = cls.STRUCT.unpack_count(esd_buffer, count=count)

            for d in struct_dicts:
                conditions = cls.Condition.unpack(
                    esd_type,
                    esd_buffer,
                    d["condition_pointers_offset"],
                    count=d["condition_pointers_count"],
                )

                enter_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d["enter_commands_offset"],
                    count=d["enter_commands_count"],
                )

                exit_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d["exit_commands_offset"],
                    count=d["exit_commands_count"],
                )

                ongoing_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d["ongoing_commands_offset"],
                    count=d["ongoing_commands_offset"],
                )

                # State 0 will be overwritten when repeated at the end of the table, rather than added.
                state_dict[d["index"]] = cls(esd_type, d["index"], conditions, enter_commands, exit_commands,
                                             ongoing_commands)

            return state_dict

        def __eq__(self, other_state):
            return self.__dict__ == other_state.__dict__

        @property
        def html_title_bar(self):
            return (f'<br><div style="font-size:35px;font-weight:bold;margin-top:10px"><a name="ezstate_{self.index}">'
                    f'EzState {self.index}</a></div>')

        def to_esp(self, from_states: set = None):
            s = f'\nclass State_{self.index}(State):\n'  # TODO: Allow user-defined state name dict.
            s += f'    """ {self.index}: No description. """\n\n'

            if from_states is not None:
                from_state_list = ', '.join(('State_' + str(s) for s in sorted(from_states)))
                s += (f"    def previous_states(self):\n"
                      f"        return [{from_state_list}]\n\n")

            comment = False
            if self.enter_commands:
                s += f'    def enter(self):\n'
                for command in self.enter_commands:
                    s += command.to_esp()
                s += '\n'
            if self.conditions:
                s += f'    def test(self):\n'
                if len(self.conditions) == 1 and self.conditions[0].test_ezl == b'\x41\xa1':
                    if self.conditions[0].next_state_index != -1:
                        s += f'        return State_{self.conditions[0].next_state_index}\n'
                    else:
                        s += f'        return -1\n'
                else:
                    for i, condition in enumerate(self.conditions):
                        if not comment and condition.test_ezl == b'\x41\xa1':
                            if i == 0:
                                s += f'        return State_{self.conditions[0].next_state_index}\n'
                            else:
                                s += f'        else:\n            return State_{condition.next_state_index}\n'
                            if i < len(self.conditions) - 1:
                                s += '        # UNREACHABLE:\n'
                                comment = True
                        else:
                            s += condition.to_esp(comment=comment)

                s += '\n'
            if self.ongoing_commands:
                s += f'    def ongoing(self):\n'
                for command in self.ongoing_commands:
                    s += command.to_esp()
                s += '\n'
            if self.exit_commands:
                s += f'    def exit(self):\n'
                for command in self.exit_commands:
                    s += command.to_esp()
                s += '\n'
            return s

        def to_html(self):
            s = self.html_title_bar
            fmt = '<br><div style="font-size:20px;font-weight:bold;margin-left:10px">{}</div>'
            if self.enter_commands:
                s += fmt.format('(ENTER) Commands:')
                for command in self.enter_commands:
                    s += command.to_html()
            if self.conditions:
                s += fmt.format('State Change Conditions:')
                CLEAR_REGISTERS()
                for condition in self.conditions:
                    s += condition.to_html()
            if self.exit_commands:
                s += fmt.format('(EXIT) Commands:')
                for command in self.exit_commands:
                    s += command.to_html()
            if self.ongoing_commands:
                s += fmt.format('(ONGOING) Commands:')
                for command in self.ongoing_commands:
                    s += command.to_html()

            return s

    class Condition(object):

        Command = None
        STRUCT = None  # type: BinaryStruct
        POINTER_STRUCT = None  # type: BinaryStruct
        STATE_ID_FORMAT = None

        def __init__(self, esd_type, next_state_index, test_ezl, pass_commands=(), subconditions=(), print_indent=0):
            self.next_state_index = next_state_index
            self.test_ezl = test_ezl
            self.pass_commands = pass_commands
            self.subconditions = subconditions
            self.__indent = print_indent
            self.esd_type = esd_type

        @classmethod
        def unpack(cls, esd_type, esd_buffer, condition_pointers_offset, count=1):
            """ Returns a list of conditions. """
            conditions = []
            if condition_pointers_offset == -1:
                return conditions
            esd_buffer.seek(condition_pointers_offset)
            pointers = cls.POINTER_STRUCT.unpack_count(esd_buffer, count=count)
            for p in pointers:
                esd_buffer.seek(p["condition_offset"])
                d = cls.STRUCT.unpack(esd_buffer)

                pass_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d["pass_commands_offset"],
                    count=d["pass_commands_count"],
                )

                subconditions = cls.unpack(
                    esd_type,
                    esd_buffer,
                    d["subcondition_pointers_offset"],
                    count=d["subcondition_pointers_count"],
                )

                test_ezl = read_chars_from_buffer(esd_buffer, offset=d["test_ezl_offset"], length=d["test_ezl_size"])

                if d["next_state_offset"] > 0:
                    esd_buffer.seek(d["next_state_offset"])
                    next_state_index, = struct.unpack(
                        cls.STATE_ID_FORMAT, esd_buffer.read(struct.calcsize(cls.STATE_ID_FORMAT)))
                else:
                    next_state_index = -1

                conditions.append(cls(esd_type, next_state_index, test_ezl, pass_commands, subconditions))

            return conditions

        def __hash__(self):
            """ Allows conditions to be used as dictionary keys, so we can track existing conditions during pack. """
            return hash((self.next_state_index, self.test_ezl, tuple(self.pass_commands), tuple(self.subconditions)))

        def __eq__(self, other_condition):
            """ Required for checking if the condition already exists as a dictionary key. """
            return (self.next_state_index == other_condition.next_state_index
                    and self.test_ezl == other_condition.test_ezl
                    and self.pass_commands == other_condition.pass_commands
                    and self.subconditions == other_condition.subconditions)

        def to_esp(self, indent=2, comment=False):
            ind = '    ' * indent
            c = '# ' if comment else ''
            s = f'{ind}{c}if {decompile(self.test_ezl, self.esd_type)}:\n'
            if self.pass_commands:
                for command in self.pass_commands:
                    s += command.to_esp(indent=indent + 1, comment=comment)
            if self.subconditions:
                if len(self.subconditions) == 1 and self.subconditions[0].test_ezl == b'\x41\xa1':
                    if self.subconditions[0].next_state_index != -1:
                        s += f'{ind}    return State_{self.subconditions[0].next_state_index}\n'
                    else:
                        s += f'{ind}    return -1\n'
                else:
                    for condition in self.subconditions:
                        s += condition.to_esp(indent=indent + 1, comment=comment)
            if self.next_state_index != -1:
                s += f'{ind}{c}    return State_{self.next_state_index}\n'
            return s

        def to_html(self):
            state_fmt = '<br><div style="color:black;line-height:0.5;margin-left:{}px;">{}</div>'
            expression_fmt = ('<br><div style="color:black;line-height:1;margin-left:{}px;font-family:sans-serif">IF: '
                              '{}</div>')
            command_fmt = '<br><div style="color:black;font-weight:bold;line-height:0.5;margin-left:{}px;">{}</div>'
            string = ''
            string += expression_fmt.format(20 * (2 + self.__indent), decompile(self.test_ezl, self.esd_type))
            if self.next_state_index != -1:
                string += state_fmt.format(20 * (3 + self.__indent), '---> <a href="#ezstate_{index}">State {index}'
                                                                     '</a>'.format(index=self.next_state_index))
            if self.pass_commands:
                string += command_fmt.format(20 * (2 + self.__indent), 'Commands:')
                for command in self.pass_commands:
                    string += command.to_html()
            if self.subconditions:
                for condition in self.subconditions:
                    string += condition.to_html()
            return string

    class Command(object):

        STRUCT = BinaryStruct(
            ('bank', 'i'),  # Values of 1, 5, 6, 7 have been encountered.
            ('index', 'i'),
            ('args_offset', 'i'),
            ('args_count', 'i'),
        )

        ARG_STRUCT = BinaryStruct(
            ('arg_ezl_offset', 'i'),
            ('arg_ezl_size', 'i'),
        )

        def __init__(self, esd_type, bank, index, command_args=(), indent=0):
            self.bank = bank
            self.index = index
            self.args = command_args
            self.esd_type = esd_type
            self.__indent = indent

        @classmethod
        def unpack(cls, esd_type, esd_buffer, commands_offset, count=1):
            """ Returns a list of Command instances. """
            commands = []
            if commands_offset == -1:
                return commands
            esd_buffer.seek(commands_offset)
            struct_dicts = cls.STRUCT.unpack_count(esd_buffer, count=count)

            for d in struct_dicts:
                if d["args_offset"] > 0:
                    esd_buffer.seek(d["args_offset"])
                    arg_structs = cls.ARG_STRUCT.unpack_count(esd_buffer, count=d["args_count"])
                    args = [read_chars_from_buffer(esd_buffer, offset=a["arg_ezl_offset"], length=a["arg_ezl_size"])
                            for a in arg_structs]
                else:
                    args = []
                commands.append(cls(esd_type, d["bank"], d["index"], args))

            return commands

        def __eq__(self, other_command):
            return (self.bank == other_command.bank
                    and self.index == other_command.index
                    and self.args == other_command.args)

        def __hash__(self):
            return hash((self.bank, self.index, tuple(self.args)))

        def to_esp(self, indent=2, comment=False):
            ind = '    ' * indent
            c = '# ' if comment else ''
            try:
                command_name, arg_names, arg_types = COMMANDS[self.esd_type][self.bank][self.index]
            except KeyError:
                if self.bank == 6:
                    # Start a child state machine.
                    arguments = ', '.join([f'{decompile(arg, self.esd_type)}' for arg in self.args])
                    return f'{ind}{c}CALL_STATE_MACHINE[{0x80000000 - self.index}]({arguments})\n'
                command_name = f'Command_{self.esd_type}_{self.bank}_{self.index}'
                arg_names = ()
            if len(arg_names) != len(self.args):
                arguments = ', '.join([f'{decompile(arg, self.esd_type)}' for arg in self.args])
            else:
                arguments = ', '.join([f'{arg_name}={decompile(arg, self.esd_type)}'
                                       for arg_name, arg in zip(arg_names, self.args)])
            return f'{ind}{c}{command_name}({arguments})\n'

        def to_html(self):
            try:
                command_name, arg_names, arg_types = COMMANDS[self.esd_type][self.bank][self.index]
            except KeyError:
                command_name = f'Command_{self.esd_type}_{self.bank}_{self.index}'
                arg_names = ()
            fmt = '<br><div style="color:black;line-height:1;margin-left:{}px;">{}({})</div>'
            return fmt.format(20 * (2 + self.__indent), command_name,
                              ', '.join([f'{arg_name}={decompile(arg, self.esd_type)}'
                                         for arg_name, arg in zip(arg_names, self.args)]))

    def __init__(self, esd_source, esd_type=None, esd_name=""):
        """ Source can be one of:
            - file path of a '.esd[.dcx]' file.
            - raw binary data (e.g. from a BND entry).
            - '.esp' file (must a single state machine with index 1, and `esd_name` must also be given).
            - '.esp' directory with a file `ESD_Header.esp.py` and separate state machine files `StateMachine_i.esp.py`
              (or `StateMachine_xi.esp.py` for callable state machines).
        """

        esd_type = esd_type.lower() if esd_type is not None else None

        self.magic = ()
        self.esd_name = esd_name
        self.file_tail = b''
        self._dcx = False
        self.esd_type = esd_type

        self.auto_path = Path()
        self.state_machines = OrderedDict()  # type: Dict[int, Dict[int, BaseESD.State]]

        if isinstance(esd_source, bytes):
            self.unpack(BytesIO(esd_source), esd_type)

        elif isinstance(esd_source, (Path, str)):
            esd_source = Path(esd_source)

            if esd_source.is_dir():
                self.auto_path = esd_source
                self.compile_from_esp_dir(esd_source)

            elif esd_source.name.endswith(".esp.py"):
                self.esd_name = esd_source.name[:-7]
                self.auto_path = esd_source.parent / self.esd_name
                self.compile_from_esp_single_file(esd_source)

            elif esd_source.name.endswith('.esd.dcx'):
                if esd_type not in {'chr', 'talk'}:
                    raise ValueError("esd_type must be 'chr' or 'talk'. This cannot be safely auto-detected from"
                                     "packed ESD resources.")
                esd_dcx = DCX(esd_source)
                self.auto_path = esd_source.parent / esd_source.name[:-8]
                self._dcx = True
                try:
                    self.unpack(BytesIO(esd_dcx.data), esd_type)
                except Exception:
                    raise IOError(f"Could not interpret file '{esd_source}' as binary ESD data. "
                                  f"You should only use the '.esd[.dcx]' extension for actual game-ready "
                                  f"ESD, which you can create with the `pack()` method of this class.")

            elif esd_source.name.endswith('.esd'):
                if esd_type not in {'chr', 'talk'}:
                    raise ValueError("esd_type must be 'chr' or 'talk'. This cannot be safely auto-detected from "
                                     "packed ESD resources.")
                self.auto_path = esd_source.parent / esd_source.stem
                with esd_source.open("rb") as esd_buffer:
                    self.unpack(esd_buffer, esd_type)

    def unpack(self, esd_buffer, esd_type: str):
        if esd_type not in {'chr', 'talk'}:
            raise ValueError(f"esd_type must be 'chr' or 'talk', not {esd_type}. This cannot be safely auto-detected.")
        self.esd_type = esd_type

        header = self.EXTERNAL_HEADER_STRUCT.unpack(esd_buffer)
        # Internal offsets start here, so we reset the buffer.
        esd_buffer = BytesIO(esd_buffer.read())

        internal_header = self.INTERNAL_HEADER_STRUCT.unpack(esd_buffer)
        self.magic = internal_header["magic"]
        state_machine_headers = self.STATE_MACHINE_HEADER_STRUCT.unpack_count(
            esd_buffer, count=header["state_machine_count"],
        )

        for state_machine_header in state_machine_headers:
            states = self.State.unpack(
                self.esd_type,
                esd_buffer,
                state_machine_header["state_machine_offset"],
                count=state_machine_header["state_count"],
            )
            self.state_machines[state_machine_header["state_machine_index"]] = states

        if internal_header["esd_name_length"] > 0:
            esd_name_offset = internal_header["esd_name_offset"]
            esd_name_length = internal_header["esd_name_length"]
            # Note the given length is the length of the final string. The actual UTF-16 encoded bytes are twice that.
            self.esd_name = read_chars_from_buffer(
                esd_buffer, offset=esd_name_offset, length=2 * esd_name_length, encoding='utf-16le')
            esd_buffer.seek(esd_name_offset + 2 * esd_name_length)
            self.file_tail = esd_buffer.read()
        else:
            self.esd_name = ""
            esd_buffer.seek(header["unk_offset_1"])  # after packed EZL
            self.file_tail = esd_buffer.read()

    def compile_from_esp_dir(self, esp_dir):
        esp_dir = Path(esp_dir)

        header_path = list(esp_dir.glob("ESD_Header*"))
        if not header_path:
            raise FileNotFoundError("Could not find 'ESD_Header file in directory.")
        self.read_esp_header(header_path[0])

        self.state_machines = {}
        for esp_path in esp_dir.glob("StateMachine_*"):
            _LOGGER.info(f"Compiling ESD state machine: {esp_path.name}")
            esp_match = re.match(r'StateMachine_(x?)(\d*)(\.esp)?(\.py)?', esp_path.name)
            if esp_match is None:
                raise ValueError(f"State machine resources should all be in format 'StateMachine_i.esp.py' for main "
                                 f"machines or 'StateMachine_xi.esp.py' for callable machines, not '{esp_path.name}'.")
            if esp_match.group(1) == 'x':
                state_machine_index = 0x80000000 - int(esp_match.group(2))
            else:
                state_machine_index = int(esp_match.group(2))
            compiler = ESPCompiler(esp_path, self)
            self.state_machines[state_machine_index] = compiler.states

    def compile_from_esp_single_file(self, esp_file):
        esp_file = Path(esp_file)
        self.esd_type = "talk"
        self.magic = (0, 0, 0, 0)
        _LOGGER.debug(f"Compiling single-file ESD state machine: {esp_file.name}")
        compiler = ESPCompiler(esp_file, self)
        self.state_machines = {1: compiler.states}

    def read_esp_header(self, header_path: Path):
        with header_path.open("r") as f:
            for line in f:
                line = line.strip(' \r\n')
                if not line:
                    continue
                if line.startswith('ESD_NAME = '):
                    self.esd_name = ast.literal_eval(line[len('ESD_NAME = '):])
                elif line.startswith('ESD_TYPE = '):
                    self.esd_type = ast.literal_eval(line[len('ESD_TYPE = '):])
                elif line.startswith('MAGIC = '):
                    magic = line[len('MAGIC = '):]
                    try:
                        self.magic = tuple(ast.literal_eval(magic))
                    except ValueError:
                        raise ValueError(f"Could not read MAGIC value from ESD_Header: {magic}")
                else:
                    raise ValueError(f"Invalid ESD Header line: {line}")
        if self.esd_type not in {'chr', 'talk'}:
            raise ValueError(f"ESD type must be 'chr' or 'talk', not {repr(self.esd_type)}")
        if len(self.magic) != 4:
            raise ValueError(f"MAGIC should be a four-element sequence.")

    def pack(self):
        """ Packs tables and computes new byte offsets for them. """
        # TODO: is 'existing commands' a thing for enemyCommon.esd? Probably, but only for efficiency.
        tables = _ESDPacker(self)

        external_header = self.EXTERNAL_HEADER_STRUCT.pack(tables.external_header)
        packed = b''
        packed += self.INTERNAL_HEADER_STRUCT.pack(tables.internal_header)
        for sm_i, sm in tables.state_machine_headers.items():
            assert len(packed) == tables.offsets['state_machine_headers'][sm_i]
            packed += self.STATE_MACHINE_HEADER_STRUCT.pack(sm)
        for sm_i, sm in tables.state_machines.items():
            assert len(packed) == tables.offsets['state_machines'][sm_i]
            packed += self.State.STRUCT.pack(sm)
        assert len(packed) == tables.offsets['conditions']
        packed += self.Condition.STRUCT.pack(tables.conditions)
        assert len(packed) == tables.offsets['commands']
        packed += self.Command.STRUCT.pack(tables.commands)
        assert len(packed) == tables.offsets['command_args']
        packed += self.Command.ARG_STRUCT.pack(tables.command_args)
        assert len(packed) == tables.offsets['condition_pointers']
        packed += self.Condition.POINTER_STRUCT.pack(tables.condition_pointers)
        assert len(packed) == tables.offsets['ezl']
        packed += tables.ezl
        assert len(packed) == tables.offsets['esd_name']
        packed += tables.esd_name
        assert len(packed) == tables.offsets['file_tail']
        packed += tables.file_tail

        return external_header + packed

    def write_packed(self, esd_path=None, dcx=None):
        if dcx is None:
            dcx = self._dcx
        if not esd_path:
            esd_path = self.auto_path
            if dcx:
                if not esd_path.name.endswith('.esd.dcx'):
                    if esd_path.suffix == '.esd':
                        esd_path = esd_path.parent / esd_path.name + '.dcx'
                    else:
                        esd_path = esd_path.parent / esd_path.name + '.esd.dcx'
            else:
                if not esd_path.suffix == '.esd':
                    esd_path = esd_path.parent / esd_path.name + '.esd'
        else:
            esd_path = Path(esd_path)
        esd_path.parent.mkdir(parents=True, exist_ok=True)
        packed = self.pack()
        with esd_path.open("wb") as f:
            f.write(DCX(packed, magic=self.DCX_MAGIC).pack() if dcx else packed)

    def copy(self):
        return copy.deepcopy(self)

    def get_next_states(self, condition: Condition):
        next_states = []
        for subcondition in condition.subconditions:
            next_states += self.get_next_states(subcondition)
        if condition.next_state_index != -1:
            next_states.append(condition.next_state_index)
        return next_states

    def to_esp(self, state_machine_index=1):
        """Writes each state machine to a separate script."""
        # Scan each state to build 'from' lists.
        from_states = {}
        for i, state in self.state_machines[state_machine_index].items():
            for condition in state.conditions:
                for next_state in self.get_next_states(condition):
                    from_states.setdefault(next_state, set()).add(i)
        s = ('from soulstruct.esd import State\n'
             'from soulstruct.esd.functions import *\n\n')
        for i, state in self.state_machines[state_machine_index].items():
            s += state.to_esp(from_states=from_states.get(i, None))
        s = s.strip('\n') + '\n'  # End with just one newline.
        return s

    def write_esp(self, esp_directory=None, force_folder=False):
        """Write ESD to a collection of Python-like 'ESP' scripts (one per state machine) in the specified folder.

        If only one state machine is present and `esd_type` is 'talk', it will be written to a single file in the given
        directory named after the internal name (discarding any junk at the end of it), with the unknown 'magic' bytes
        discarded (neither the internal name nor magic matters in-game). You can disable this behavior and force an ESP
        folder to be written even in this case by setting `force_folder=True`.
        """
        if esp_directory is None:
            esp_directory = self.auto_path
            if not esp_directory.suffix == ".esp":
                esp_directory = esp_directory.with_suffix(esp_directory.suffix + ".esp")
        else:
            esp_directory = Path(esp_directory)

        single_file = (len(self.state_machines) == 1 and 1 in self.state_machines
                       and self.esd_type == "talk" and not esp_directory.is_dir() and not force_folder)

        # TODO: read from single file

        if single_file:
            # Write single 'talk' state machine to a single ESP file.
            if esp_directory.suffix != ".py":
                esp_directory = esp_directory.with_suffix(esp_directory.suffix + ".py")
            esp_directory.parent.mkdir(parents=True, exist_ok=True)
            with esp_directory.open(mode="w", encoding="utf-8") as esp_file:
                state_machine_py = self.to_esp(1)
                esp_file.write(state_machine_py)
            return

        esp_directory.mkdir(parents=True, exist_ok=True)
        for i, state_machine in self.state_machines.items():
            if i >= 0x70000000:
                # 'Callable' state machine.
                state_machine_path = esp_directory / f'StateMachine_x{0x80000000 - i}.esp.py'
            else:
                # Primary state machine.
                state_machine_path = esp_directory / f'StateMachine_{i}.esp.py'
            with state_machine_path.open(mode="w", encoding='utf-8') as state_machine_file:
                state_machine_py = self.to_esp(i)
                state_machine_file.write(state_machine_py)
        header = (f"ESD_NAME = {repr(self.esd_name)}\n"
                  f"ESD_TYPE = {repr(self.esd_type)}\n"
                  f"MAGIC = {repr(self.magic)}\n")
        with (esp_directory / "ESD_Header.esp.py").open(mode="w", encoding='utf-8') as header_file:
            header_file.write(header)

    def to_html(self):

        SET_INTERNAL_SYMBOLS(True)

        html = ("<html><head></head><body>"
                "<meta charset=\"shift-jis\"><br>"
                "NOTES:<br>"
                "  <b>&</b>: this expression has been evaluated in a previous condition of this state, and loaded<br>"
                "  here from one of eight registers. (We currently believe this is only used for function calls,<br>"
                "  so if you see it used with any other type of expression, please show us!)<br>"
                "  <b>...</b>: interpreter should continue even if the previous value is false. (This seems to be<br>"
                "  the default behavior anyway, so this symbol seems useless, and I haven't been able to detect<br>"
                "  a pattern for when it's actually used.)<br>"
                "  <b>!</b>: interpreter should stop if the previous value is false. (Optimizes 'and' operations,<br>"
                "  but not if there's a register save to be done later in the test script.)<br>")

        for state_machine in self.state_machines.values():
            for state in state_machine.values():
                html += state.to_html()

        SET_INTERNAL_SYMBOLS(False)

        return html + '</body></html>'

    def write_html(self, html_path=None):
        if html_path is None:
            html_path = self.auto_path.with_suffix(self.auto_path.suffix + ".html")
        else:
            html_path = Path(html_path)
        with html_path.open(mode="w", encoding='shift-jis') as output_file:
            output_file.write(self.to_html())


class _ESDPacker(object):

    def __init__(self, esd: BaseESD):
        self.__updated = False
        self.esd = esd.__class__

        # Various constants.
        self.magic = esd.magic
        self.esd_name = esd.esd_name.encode('utf-16le')
        self.file_tail = esd.file_tail

        self.state_machine_headers = OrderedDict()
        self.state_machines = OrderedDict()
        self.conditions = []
        self.commands = []
        self.command_args = []
        self.condition_pointers = []  # only table that is simply an integer sequence for direct packing
        self.ezl = b''  # packed byte code language for command arguments and condition tests

        self.state_indices = {}  # {state_index: state_index_in_sequence}  (in case state indices are missing)

        self.offsets = {
            'state_machine_headers': OrderedDict(),  # index: offset
            'state_machines': OrderedDict(),  # index: offset
            'conditions': 0,
            'commands': 0,
            'command_args': 0,
            'condition_pointers': 0,
            'ezl': 0,
            'esd_name': 0,
            'file_tail': 0,
            'end_of_file': 0,
        }

        # Build tables with relative within-table offsets.
        for state_machine_index, state_machine in esd.state_machines.items():
            self.current_state_machine_index = state_machine_index
            self.existing_condition_pointers = {}  # TODO: Current resetting it for every state machine.
            self.state_machines[state_machine_index] = self.build_state_machine(state_machine)
            self.state_machine_headers[state_machine_index] = {
                'state_machine_index': state_machine_index,  # index starts at 1
                'state_machine_offset': len(self.state_machine_headers) * self.esd.STATE_MACHINE_HEADER_STRUCT.size,
                'state_count': len(self.state_machines[state_machine_index]) - 1,  # state 0 repeat not included
                'state_machine_offset_2': len(self.state_machine_headers) * self.esd.STATE_MACHINE_HEADER_STRUCT.size,
            }

        self.__update_offsets()

        self.__update_tables()

        self.external_header = {
            'internal_data_size': self.offsets['end_of_file'],  # excludes external header
            'state_machine_count': len(self.state_machine_headers),
            'state_count': sum([len(sm) for sm in self.state_machines.values()]),  # includes repeated state
            'condition_count': len(self.conditions),
            'command_count': len(self.commands),
            'command_arg_count': len(self.command_args),
            'condition_pointers_offset': self.offsets['condition_pointers'],
            'condition_pointers_count': len(self.condition_pointers),
            'esd_name_offset_minus_1': self.offsets['esd_name'] - 1 if self.esd_name else self.offsets['end_of_file'],
            'esd_name_length': len(self.esd_name) // 2,
            'unk_offset_1': self.offsets['esd_name'] if self.esd_name else self.offsets['end_of_file'],
            'unk_offset_2': self.offsets['file_tail'],
        }

        self.internal_header = {
            'magic': self.magic,
            'state_machine_count': len(self.state_machine_headers),
            'esd_name_offset': self.offsets['esd_name'] if self.esd_name else self.offsets['end_of_file'],
            'esd_name_length': len(self.esd_name) // 2,
        }

    def __update_offsets(self):
        state_machine_headers_offset = self.esd.INTERNAL_HEADER_STRUCT.size
        for state_machine_index in self.state_machine_headers:
            self.offsets['state_machine_headers'][state_machine_index] = (
                    state_machine_headers_offset +
                    len(self.offsets['state_machine_headers']) * self.esd.STATE_MACHINE_HEADER_STRUCT.size)
        state_machines_offset = (state_machine_headers_offset +
                                 len(self.state_machine_headers) * self.esd.STATE_MACHINE_HEADER_STRUCT.size)
        state_machine_total_size = 0
        for state_machine_index, sm in self.state_machines.items():
            self.offsets['state_machines'][state_machine_index] = (state_machines_offset + state_machine_total_size)
            state_machines_offset += len(sm) * self.esd.State.STRUCT.size
        self.offsets['conditions'] = state_machines_offset + state_machine_total_size
        self.offsets['commands'] = self.offsets['conditions'] + len(self.conditions) * self.esd.Condition.STRUCT.size
        self.offsets['command_args'] = self.offsets['commands'] + len(self.commands) * self.esd.Command.STRUCT.size
        self.offsets['condition_pointers'] = (self.offsets['command_args']
                                              + len(self.command_args) * self.esd.Command.ARG_STRUCT.size)
        self.offsets['ezl'] = (self.offsets['condition_pointers']
                               + len(self.condition_pointers) * self.esd.Condition.POINTER_STRUCT.size)
        self.offsets['esd_name'] = self.offsets['ezl'] + len(self.ezl)
        self.offsets['file_tail'] = self.offsets['esd_name'] + len(self.esd_name)
        self.offsets['end_of_file'] = self.offsets['file_tail'] + len(self.file_tail)

    def __update_tables(self):
        if self.__updated:
            raise ValueError("ESDPacker has already updated the tables.")
        for sm_index, header in self.state_machine_headers.items():
            header['state_machine_offset'] = header['state_machine_offset_2'] = self.offsets['state_machines'][sm_index]
        for sm in self.state_machines.values():
            states_done = set()
            for state in sm:
                if state['index'] not in states_done:
                    state['condition_pointers_offset'] += self.offsets['condition_pointers']
                    if state['enter_commands_offset'] >= 0:
                        state['enter_commands_offset'] += self.offsets['commands']
                    if state['exit_commands_offset'] >= 0:
                        state['exit_commands_offset'] += self.offsets['commands']
                    if state['ongoing_commands_offset'] >= 0:
                        state['ongoing_commands_offset'] += self.offsets['commands']
                    states_done.add(state['index'])
        for condition in self.conditions:
            state_machine_index = condition.pop('__state_machine_index__')
            state_machine_offset = self.offsets['state_machines'][state_machine_index]
            if condition['next_state_offset'] >= 0:
                # 'next_state_offset' is actually an absolute state index before this.
                relative_state_offset = self.state_indices[condition['next_state_offset']] * self.esd.State.STRUCT.size
                condition['next_state_offset'] = state_machine_offset + relative_state_offset
            if condition['pass_commands_offset'] >= 0:
                condition['pass_commands_offset'] += self.offsets['commands']
            if condition['subcondition_pointers_offset'] >= 0:
                condition['subcondition_pointers_offset'] += self.offsets['condition_pointers']
            if condition['test_ezl_offset'] >= 0:
                condition['test_ezl_offset'] += self.offsets['ezl']
        for command in self.commands:
            if command['args_offset'] >= 0:
                command['args_offset'] += self.offsets['command_args']
        for command_arg in self.command_args:
            command_arg['arg_ezl_offset'] += self.offsets['ezl']
        for condition_pointer in self.condition_pointers:
            condition_pointer['condition_offset'] += self.offsets['conditions']
        self.__updated = True

    def build_state_machine(self, state_machine: dict):
        built = []
        for index, state in state_machine.items():
            self.state_indices[index] = len(built)
            built_state = self.build_state(index, state)
            built.append(built_state)
        if len(built) > 1:
            built.append(built[0])  # First state (generally index 0) repeats at end of table (if not alone).
        return built

    def build_state(self, index: int, state: BaseESD.State):
        built = {
            'index': index,
            'condition_pointers_offset': None,
            'condition_pointers_count': None,
            'enter_commands_offset': None,
            'enter_commands_count': None,
            'exit_commands_offset': None,
            'exit_commands_count': None,
            'ongoing_commands_offset': None,
            'ongoing_commands_count': None,
        }

        condition_pointers_offset, condition_pointers_count = self.build_condition_list(state.conditions)
        built['condition_pointers_offset'] = condition_pointers_offset
        built['condition_pointers_count'] = condition_pointers_count

        enter_commands = []
        for enter_command in state.enter_commands:
            enter_commands.append(self.build_command(enter_command))
        built['enter_commands_offset'] = enter_commands[0] if enter_commands else -1
        built['enter_commands_count'] = len(enter_commands)

        exit_commands = []
        for exit_command in state.exit_commands:
            exit_commands.append(self.build_command(exit_command))
        built['exit_commands_offset'] = exit_commands[0] if exit_commands else -1
        built['exit_commands_count'] = len(exit_commands)

        ongoing_commands = []
        for ongoing_command in state.ongoing_commands:
            ongoing_commands.append(self.build_command(ongoing_command))
        built['ongoing_commands_offset'] = ongoing_commands[0] if ongoing_commands else -1
        built['ongoing_commands_count'] = len(ongoing_commands)

        return built

    def build_condition_list(self, condition_list):
        """ Ensures that adjacent conditions are built sequentially before blocks of subconditions. """
        condition_pointers = []
        subconditions_to_build = []
        for condition in condition_list:
            condition_pointer_offset, condition_dict, subconditions = self.build_condition(condition)
            condition_pointers.append(condition_pointer_offset)
            if condition_dict is not None:
                subconditions_to_build.append((condition_dict, subconditions))

        for condition_dict, subconditions in subconditions_to_build:
            offset, count = self.build_condition_list(subconditions)
            condition_dict['subcondition_pointers_offset'] = offset
            condition_dict['subcondition_pointers_count'] = count

        return (condition_pointers[0] if condition_pointers else -1), len(condition_pointers)

    def build_condition(self, condition: BaseESD.Condition):

        built = {
            '__state_machine_index__': self.current_state_machine_index,  # removed later
            'next_state_offset': condition.next_state_index,  # converted to offset later
            'pass_commands_offset': None,
            'pass_commands_count': None,
            'subcondition_pointers_offset': None,
            'subcondition_pointers_count': None,
            'test_ezl_offset': None,
            'test_ezl_size': None,
        }

        pass_commands = []
        for pass_command in condition.pass_commands:
            pass_commands.append(self.build_command(pass_command))
        built['pass_commands_offset'] = pass_commands[0] if pass_commands else -1
        built['pass_commands_count'] = len(pass_commands)

        # TODO: Need to pack conditions breadth-first rather than depth-first...
        subconditions_to_build = list(condition.subconditions)

        built['test_ezl_offset'] = self.build_ezl(condition.test_ezl)
        built['test_ezl_size'] = len(condition.test_ezl)

        this_pointer_offset = len(self.condition_pointers) * self.esd.Condition.POINTER_STRUCT.size
        if condition in self.existing_condition_pointers:
            self.condition_pointers.append({'condition_offset': self.existing_condition_pointers[condition]})
            return this_pointer_offset, None, None

        this_condition_offset = len(self.conditions) * self.esd.Condition.STRUCT.size
        self.condition_pointers.append({'condition_offset': this_condition_offset})
        self.conditions.append(built)
        self.existing_condition_pointers[condition] = this_condition_offset
        return this_pointer_offset, built, subconditions_to_build

    def build_command(self, command: BaseESD.Command):
        this_command_offset = len(self.commands) * self.esd.Command.STRUCT.size
        built = {
            'bank': command.bank,
            'index': command.index,
            'args_offset': len(self.command_args) * self.esd.Command.ARG_STRUCT.size if command.args else -1,
            'args_count': len(command.args),
        }
        for arg in command.args:
            self.command_args.append({'arg_ezl_offset': self.build_ezl(arg), 'arg_ezl_size': len(arg)})
        self.commands.append(built)
        return this_command_offset

    def build_ezl(self, ezl_bytes):
        # TODO: Conditions and commands are currently intermingled (ordered by state), which is not true for the
        #  original resources (where all condition data comes before all command data), but it shouldn't matter at all.
        this_offset = len(self.ezl)
        self.ezl += ezl_bytes
        return this_offset


def get_esd_class(game_version: int, long: bool):

    if long:

        # End of internal header is zero padding DS1/DSR, -1 padding in later games
        internal_header_end = '16x' if game_version == 1 else ('internal_pad', '2q', [-1, -1])

        class ESD(BaseESD):
            EXTERNAL_HEADER_STRUCT = BinaryStruct(
                ('version', '4s', b'fsSL'),  # Note specific case.
                ('one', 'i', 1),
                ('game_version', '2i', [game_version, game_version]),
                ('table_size_offset', 'i', 84),
                ('internal_data_size', 'i'),  # excludes this external header
                ('unk', 'i', 6),
                ('internal_header_size', 'i', 72),
                ('internal_header_count', 'i', 1),
                ('state_machine_header_size', 'i', 32),
                ('state_machine_count', 'i'),
                ('state_size', 'i', 72),
                ('state_count', 'i'),
                ('condition_size', 'i', 56),
                ('condition_count', 'i'),
                ('command_size', 'i', 24),
                ('command_count', 'i'),
                ('command_arg_size', 'i', 16),
                ('command_arg_count', 'i'),
                ('condition_pointers_offset', 'i'),
                ('condition_pointers_count', 'i'),
                ('esd_name_offset_minus_1', 'i'),
                # Not sure why this is minus 1. Use the internal header for the real offset.
                ('esd_name_length', 'i'),  # equal to internal header
                ('unk_offset_1', 'i'),
                ('unk_size_1', 'i', 0),
                ('unk_offset_2', 'i'),
                ('unk_size_2', 'i', 0),
            )
            INTERNAL_HEADER_STRUCT = BinaryStruct(
                ('one', 'i', 1),
                ('magic', '4i'),
                '4x',
                ('state_machine_headers_offset', 'q', 72),
                ('state_machine_count', 'q'),
                ('esd_name_offset', 'q'),  # accurate, unlike external header
                ('esd_name_length', 'q'),
                # identical to external header entry; note this is only *half* the name byte size due to UTF-16
                internal_header_end
            )
            STATE_MACHINE_HEADER_STRUCT = BinaryStruct(
                ('state_machine_index', 'q'),
                ('state_machine_offset', 'q'),
                ('state_count', 'q'),  # number of states
                ('state_machine_offset_2', 'q'),  # duplicate
            )
            DCX_MAGIC = (36, 44)

            class State(BaseESD.State):
                Condition = None
                Command = None

                STRUCT = BinaryStruct(
                    ('index', 'q'),
                    ('condition_pointers_offset', 'q'),
                    ('condition_pointers_count', 'q'),
                    ('enter_commands_offset', 'q'),
                    ('enter_commands_count', 'q'),
                    ('exit_commands_offset', 'q'),
                    ('exit_commands_count', 'q'),
                    ('ongoing_commands_offset', 'q'),
                    ('ongoing_commands_count', 'q'),
                )

            class Condition(BaseESD.Condition):
                STRUCT = BinaryStruct(
                    ('next_state_offset', 'q'),
                    ('pass_commands_offset', 'q'),
                    ('pass_commands_count', 'q'),
                    ('subcondition_pointers_offset', 'q'),
                    ('subcondition_pointers_count', 'q'),
                    ('test_ezl_offset', 'q'),
                    ('test_ezl_size', 'q'),
                )
                POINTER_STRUCT = BinaryStruct(
                    ('condition_offset', 'q'),
                )
                STATE_ID_FORMAT = 'q'

            class Command(BaseESD.Command):
                STRUCT = BinaryStruct(
                    ('bank', 'i'),  # Values of 1, 5, 6, 7 have been encountered.
                    ('index', 'i'),
                    ('args_offset', 'q'),
                    ('args_count', 'q'),
                )
                ARG_STRUCT = BinaryStruct(
                    ('arg_ezl_offset', 'q'),
                    ('arg_ezl_size', 'q'),
                )

    else:

        # End of internal header is zero padding DS1/DSR, -1 padding in later games
        internal_header_end = '8x' if game_version == 1 else ('internal_pad', '2i', [-1, -1])

        class ESD(BaseESD):
            EXTERNAL_HEADER_STRUCT = BinaryStruct(
                ('version', '4s', b'fSSL'),  # Note specific case.
                ('one', 'i', 1),
                ('game_version', '2i', [game_version, game_version]),
                ('table_size_offset', 'i', 84),
                ('internal_data_size', 'i'),  # excludes header size
                ('unk', 'i', 6),
                ('internal_header_size', 'i', 44),
                ('internal_header_count', 'i', 1),
                ('state_machine_header_size', 'i', 16),
                ('state_machine_count', 'i'),
                ('state_size', 'i', 36),
                ('state_count', 'i'),
                ('condition_size', 'i', 28),
                ('condition_count', 'i'),
                ('command_size', 'i', 16),
                ('command_count', 'i'),
                ('command_arg_size', 'i', 8),
                ('command_arg_count', 'i'),
                ('condition_pointers_offset', 'i'),
                ('condition_pointers_count', 'i'),
                ('esd_name_offset_minus_1', 'i'),
                ('esd_name_length', 'i'),
                ('unk_offset_1', 'i'),
                ('unk_size_1', 'i', 0),
                ('unk_offset_2', 'i'),
                ('unk_size_2', 'i', 0),
            )
            INTERNAL_HEADER_STRUCT = BinaryStruct(
                ('one', 'i', 1),
                ('magic', '4i'),  # TODO: constant within games, at least?
                ('state_machine_headers_offset', 'i', 44),
                ('state_machine_count', 'i'),
                ('esd_name_offset', 'i'),  # accurate, unlike external header
                ('esd_name_length', 'i'),
                internal_header_end,
            )
            STATE_MACHINE_HEADER_STRUCT = BinaryStruct(
                ('state_machine_index', 'i'),
                ('state_machine_offset', 'i'),
                ('state_count', 'i'),  # number of states
                ('state_machine_offset_2', 'i'),  # duplicate
            )

            class State(BaseESD.State):
                STRUCT = BinaryStruct(
                    ('index', 'i'),
                    ('condition_pointers_offset', 'i'),
                    ('condition_pointers_count', 'i'),
                    ('enter_commands_offset', 'i'),
                    ('enter_commands_count', 'i'),
                    ('exit_commands_offset', 'i'),
                    ('exit_commands_count', 'i'),
                    ('ongoing_commands_offset', 'i'),
                    ('ongoing_commands_count', 'i'),
                )

            class Condition(BaseESD.Condition):
                STRUCT = BinaryStruct(
                    ('next_state_offset', 'i'),
                    ('pass_commands_offset', 'i'),
                    ('pass_commands_count', 'i'),
                    ('subcondition_pointers_offset', 'i'),
                    ('subcondition_pointers_count', 'i'),
                    ('test_ezl_offset', 'i'),
                    ('test_ezl_size', 'i'),
                )
                POINTER_STRUCT = BinaryStruct(
                    ('condition_offset', 'i'),
                )
                STATE_ID_FORMAT = 'i'

            class Command(BaseESD.Command):
                STRUCT = BinaryStruct(
                    ('bank', 'i'),  # Values of 1, 5, 6, 7 have been encountered.
                    ('index', 'i'),
                    ('args_offset', 'i'),
                    ('args_count', 'i'),
                )
                ARG_STRUCT = BinaryStruct(
                    ('arg_ezl_offset', 'i'),
                    ('arg_ezl_size', 'i'),
                )

    # Pass references between classes.
    ESD.State.Condition = ESD.Condition
    ESD.State.Command = ESD.Command
    ESD.Condition.Command = ESD.Command

    return ESD
