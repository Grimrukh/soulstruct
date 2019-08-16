import ast
from collections import OrderedDict
import glob
from io import BytesIO
import os
from queue import Queue
import re
import struct
from typing import List, Tuple
from soulstruct.utilities.core import BinaryStruct, read_chars_from_buffer
from soulstruct.dcx import DCX
from .ezl_parser import *
from .functions import COMMANDS, COMMANDS_BANK_ID_BY_TYPE_NAME, TEST_FUNCTIONS_ID_BY_TYPE_NAME

__all__ = ['EsdSyntaxError', 'EsdValueError', 'BaseESD']


class EsdError(Exception):
    def __init__(self, lineno, msg):
        super().__init__(f"LINE {lineno}: {msg}")


class EsdSyntaxError(EsdError):
    pass


class EsdValueError(EsdError):
    pass


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
            """ Unpack multiple states from the same state table.

            Returns a dictionary of states, because it's always possible (if yet unseen) that state indices are not
            contiguous. State 0 is not repeated, as it generally is in the packed table.
            """

            state_dict = OrderedDict()
            esd_buffer.seek(state_machine_offset)
            struct_dicts = cls.STRUCT.unpack(esd_buffer, count=count)

            for d in struct_dicts:
                conditions = cls.Condition.unpack(
                    esd_type,
                    esd_buffer,
                    d.condition_pointers_offset,
                    count=d.condition_pointers_count,
                )

                enter_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d.enter_commands_offset,
                    count=d.enter_commands_count,
                )

                exit_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d.exit_commands_offset,
                    count=d.exit_commands_count,
                )

                ongoing_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d.ongoing_commands_offset,
                    count=d.ongoing_commands_offset,
                )

                # State 0 will be overwritten when repeated at the end of the table, rather than added.
                state_dict[d.index] = cls(esd_type, d.index, conditions, enter_commands, exit_commands,
                                          ongoing_commands)

            return state_dict

        def __eq__(self, other_state):
            return self.__dict__ == other_state.__dict__

        @property
        def html_title_bar(self):
            return (f'<br><div style="font-size:35px;font-weight:bold;margin-top:10px"><a name="ezstate_{self.index}">'
                    f'EzState {self.index}</a></div>')

        def to_py(self, from_states: set = None):
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
                    s += command.to_py()
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
                            s += condition.to_py(comment=comment)

                s += '\n'
            if self.ongoing_commands:
                s += f'    def ongoing(self):\n'
                for command in self.ongoing_commands:
                    s += command.to_py()
                s += '\n'
            if self.exit_commands:
                s += f'    def exit(self):\n'
                for command in self.exit_commands:
                    s += command.to_py()
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
            pointers = cls.POINTER_STRUCT.unpack(esd_buffer, count=count)
            for p in pointers:
                esd_buffer.seek(p.condition_offset)
                d = cls.STRUCT.unpack(esd_buffer, count=None)

                pass_commands = cls.Command.unpack(
                    esd_type,
                    esd_buffer,
                    d.pass_commands_offset,
                    count=d.pass_commands_count,
                )

                subconditions = cls.unpack(
                    esd_type,
                    esd_buffer,
                    d.subcondition_pointers_offset,
                    count=d.subcondition_pointers_count,
                )

                test_ezl = read_chars_from_buffer(esd_buffer, offset=d.test_ezl_offset, length=d.test_ezl_size)

                if d.next_state_offset > 0:
                    esd_buffer.seek(d.next_state_offset)
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

        def to_py(self, indent=2, comment=False):
            ind = '    ' * indent
            c = '# ' if comment else ''
            s = f'{ind}{c}if {decompile(self.test_ezl, self.esd_type)}:\n'
            if self.pass_commands:
                for command in self.pass_commands:
                    s += command.to_py(indent=indent + 1, comment=comment)
            if self.subconditions:
                if len(self.subconditions) == 1 and self.subconditions[0].test_ezl == b'\x41\xa1':
                    if self.subconditions[0].next_state_index != -1:
                        s += f'{ind}    return State_{self.subconditions[0].next_state_index}\n'
                    else:
                        s += f'{ind}    return -1\n'
                else:
                    for condition in self.subconditions:
                        s += condition.to_py(indent=indent + 1, comment=comment)
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
            struct_dicts = cls.STRUCT.unpack(esd_buffer, count=count)

            for d in struct_dicts:
                if d.args_offset > 0:
                    esd_buffer.seek(d.args_offset)
                    arg_structs = cls.ARG_STRUCT.unpack(esd_buffer, count=d.args_count)
                    args = [read_chars_from_buffer(esd_buffer, offset=a.arg_ezl_offset, length=a.arg_ezl_size)
                            for a in arg_structs]
                else:
                    args = []
                commands.append(cls(esd_type, d.bank, d.index, args))

            return commands

        def __eq__(self, other_command):
            return (self.bank == other_command.bank
                    and self.index == other_command.index
                    and self.args == other_command.args)

        def __hash__(self):
            return hash((self.bank, self.index, tuple(self.args)))

        def to_py(self, indent=2, comment=False):
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

    def __init__(self, esd_source, esd_type=None):
        """ Source can be one of:
            - file path of a '.esd[.dcx]' file.
            - raw binary data (e.g. from a BND entry).
        """

        esd_type = esd_type.upper() if esd_type is not None else None

        self.magic = ()
        self.esd_name = ''
        self.file_tail = b''
        self._dcx = False
        self.esd_type = esd_type

        self.auto_path_name = ''
        self.state_machines = OrderedDict()

        if isinstance(esd_source, bytes):
            self.unpack(BytesIO(esd_source), esd_type)

        elif isinstance(esd_source, str):

            if os.path.isdir(esd_source):
                self.auto_path_name = esd_source
                if self.auto_path_name.endswith('.py'):
                    self.auto_path_name = self.auto_path_name[:-3]
                self.compile_from_esp_dir(esd_source)

            elif esd_source.endswith('.esd.dcx'):
                if esd_type not in {'CHR', 'TALK'}:
                    raise ValueError("esd_type must be 'CHR' or 'TALK'. This cannot be safely auto-detected from"
                                     "packed ESD resources.")
                esd_dcx = DCX(esd_source)
                self.auto_path_name = esd_source[:-8]
                self._dcx = True
                try:
                    self.unpack(BytesIO(esd_dcx.data), esd_type)
                except Exception:
                    raise IOError(f"Could not interpret file '{esd_source}' as binary ESD data.\n"
                                  f"You should only use the '.esd[.dcx]' extension for actual game-ready\n"
                                  f"ESD, which you can create with the `pack()` method of this class.")

            elif esd_source.endswith('.esd'):
                if esd_type not in {'CHR', 'TALK'}:
                    raise ValueError("esd_type must be 'CHR' or 'TALK'. This cannot be safely auto-detected from"
                                     "packed ESD resources.")
                self.auto_path_name = esd_source[:-4]
                with open(esd_source, 'rb') as esd_buffer:
                    self.unpack(esd_buffer, esd_type)

    def unpack(self, esd_buffer, esd_type):

        if esd_type not in {'CHR', 'TALK'}:
            raise ValueError("esd_type must be 'CHR' or 'TALK'. This cannot be safely auto-detected.")
        self.esd_type = esd_type

        header = self.EXTERNAL_HEADER_STRUCT.unpack(esd_buffer)
        # Internal offsets start here, so we reset the buffer.
        esd_buffer = BytesIO(esd_buffer.read())

        internal_header = self.INTERNAL_HEADER_STRUCT.unpack(esd_buffer)
        self.magic = internal_header.magic
        state_machine_headers = self.STATE_MACHINE_HEADER_STRUCT.unpack(esd_buffer, count=header.state_machine_count)
        print(f"# Number of state machines: {len(state_machine_headers)}")  # todo

        for state_machine_header in state_machine_headers:
            states = self.State.unpack(
                self.esd_type,
                esd_buffer,
                state_machine_header.state_machine_offset,
                count=state_machine_header.state_count,
            )
            self.state_machines[state_machine_header.state_machine_index] = states

        if internal_header.esd_name_length > 0:
            esd_name_offset = internal_header.esd_name_offset
            esd_name_length = internal_header.esd_name_length
            # Note the given length is the length of the final string. The actual UTF-16 encoded bytes are twice that.
            self.esd_name = read_chars_from_buffer(
                esd_buffer, offset=esd_name_offset, length=2 * esd_name_length, encoding='utf-16le')
            esd_buffer.seek(esd_name_offset + 2 * esd_name_length)
            self.file_tail = esd_buffer.read()
        else:
            self.esd_name = ''
            esd_buffer.seek(header.unk_offset_1)  # after packed EZL
            self.file_tail = esd_buffer.read()

    def compile_from_esp_dir(self, esp_dir):
        # Compile header first.
        header_path = glob.glob(os.path.join(esp_dir, 'ESD_Header*'))
        if not header_path:
            raise FileNotFoundError("Could not find 'ESD_Header file in directory.")
        self.read_esp_header(header_path[0])

        for esp_path in glob.glob(os.path.join(esp_dir, 'StateMachine_*')):
            esp_name = os.path.basename(esp_path)
            print(f"# Compiling {esp_name}...")
            esp_match = re.match(r'StateMachine_(x?)(\d*)\.(py|esp)', esp_name)
            if esp_match is None:
                raise NameError(f"State machine resources should all be in format 'StateMachine_i' for main machines\n"
                                f"or 'StateMachine_xi' for callable machines, not '{os.path.basename(esp_path)}'")
            if esp_match.group(1) == 'x':
                state_machine_index = 0x80000000 - int(esp_match.group(2))
            else:
                state_machine_index = int(esp_match.group(2))
            compiler = ESPCompiler(esp_path, self)
            self.state_machines[state_machine_index] = compiler.states

    def read_esp_header(self, header_path):
        with open(header_path, 'r') as f:
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
        if self.esd_type not in {'CHR', 'TALK'}:
            raise ValueError(f"ESD type must be 'CHR' or 'TALK', not {repr(self.esd_type)}")
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
            if sm_i == 1:
                for s in sm:
                    print(s)
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
            esd_path = self.auto_path_name
            if dcx:
                if not esd_path.endswith('.esd.dcx'):
                    esd_path += '.esd.dcx'
            else:
                if not esd_path.endswith('.esd'):
                    esd_path += '.esd'
        if os.path.dirname(esd_path):
            os.makedirs(os.path.dirname(esd_path), exist_ok=True)
        packed = self.pack()
        with open(esd_path, 'wb') as f:
            f.write(DCX(packed, magic=self.DCX_MAGIC).pack() if dcx else packed)

    def get_next_states(self, condition: Condition):
        next_states = []
        for subcondition in condition.subconditions:
            next_states += self.get_next_states(subcondition)
        if condition.next_state_index != -1:
            next_states.append(condition.next_state_index)
        return next_states

    def to_py(self, state_machine_index=1):
        """ Writes each state machine to a separate script. """

        # Scan each state to build 'from' lists.
        from_states = {}
        for i, state in self.state_machines[state_machine_index].items():
            for condition in state.conditions:
                for next_state in self.get_next_states(condition):
                    from_states.setdefault(next_state, set()).add(i)

        s = ('from soulstruct.esd import State\n'
             'from soulstruct.esd.functions import *\n\n')
        for i, state in self.state_machines[state_machine_index].items():
            s += state.to_py(from_states=from_states.get(i, None))
        s = s.strip('\n') + '\n'  # End with just one newline.
        return s

    def write_py(self, py_dir_path=None):
        """ Write ESD to a collection of Python-like 'ESP' scripts (one per state machine) in the specified folder. """
        if py_dir_path is None:
            py_dir_path = self.auto_path_name
            if not py_dir_path.endswith('.esp'):
                py_dir_path += '.esp'
        os.makedirs(py_dir_path, exist_ok=True)
        for i, state_machine in self.state_machines.items():
            if i >= 0x70000000:
                # 'Callable' state machine.
                state_machine_path = os.path.join(py_dir_path, f'StateMachine_x{0x80000000 - i}.py')
            else:
                # Primary state machine.
                state_machine_path = os.path.join(py_dir_path, f'StateMachine_{i}.py')
            with open(state_machine_path, 'w', encoding='utf-8') as state_machine_file:
                state_machine_py = self.to_py(i)
                state_machine_file.write(state_machine_py)
        header = (f"ESD_NAME = {repr(self.esd_name)}\n"
                  f"ESD_TYPE = {repr(self.esd_type)}\n"
                  f"MAGIC = {repr(self.magic)}\n")
        with open(os.path.join(py_dir_path, f'ESD_Header.py'), 'w', encoding='utf-8') as header_file:
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
            html_path = self.auto_path_name + '.html'
        with open(html_path, 'w', encoding='shift-jis') as output_file:
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
            if state_machine_index == 1:
                print('CONDITION BEFORE:', condition)
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
            if state_machine_index == 1:
                print('CONDITION AFTER:', condition)
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
        print('\n\nState:', index, self.current_state_machine_index)

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


class ESPCompiler(object):

    registers: List[Tuple]
    _STATE_DOCSTRING_RE = re.compile(r'([0-9]+)(:\s*.*)?')
    _COMMAND_DEFAULT_RE = re.compile(r'Command_(?:TALK|CHR)_(\d*)_(\d*)')
    _TEST_DEFAULT_RE = re.compile(r'Test_(?:TALK|CHR)_(\d*)')

    def __init__(self, esp_path, esd_object):
        """ Builds a single state machine. """

        self.ESD = esd_object  # type: BaseESD
        self.docstring = ''
        self.state_machine_index = None
        self.state_info = {}
        self.states = {}

        # Condition state.
        self.registers = [()] * 8
        self.state_call_set = set()
        self.to_write_count = 0
        self.to_write = Queue()  # list of first-time function calls to save for every (sub)condition in order
        self.written = {}  # maps function calls to register index 0-8
        self.current_to_write = []

        with open(esp_path, encoding='utf-8') as script:
            self.tree = ast.parse(script.read())

        self.compile_script()

    def compile_script(self):
        """ Top-level node traversal. Only acceptable nodes at this top level are ImportFrom (for importing your
        constants) and FunctionDef (for your event scripts). """

        self.docstring = ast.get_docstring(self.tree)

        for node in self.tree.body[1:]:

            if isinstance(node, ast.Import):
                raise EsdSyntaxError(node.lineno,
                                     "All imports should be of the form 'from your_constants import *' (other than "
                                     "'from soulstruct.esd import *').")
            elif isinstance(node, ast.ImportFrom):
                # TODO: self.import_constants(node)
                pass
            elif isinstance(node, ast.ClassDef):
                self.scan_state(node)
            else:
                raise EsdSyntaxError(node.lineno,
                                     f"Invalid content: {node.__class__}. The only valid top-level EVS lines are "
                                     f"from-imports and class definitions.")

        for state in self.state_info.values():
            self.states[state['index']] = self.build_state(state['index'], state['nodes'])

    def build_state(self, index, nodes):
        """ Nodes are the non-docstring nodes of the state class definition. """

        index = index
        conditions = []
        enter_commands = []
        exit_commands = []
        ongoing_commands = []

        for node in nodes:
            if not isinstance(node, ast.FunctionDef):
                raise EsdSyntaxError(node.lineno, "Non-function appeared in state class.")

            if node.name == 'previous_states':
                # Ignore informative method.
                continue
            elif node.name == 'test':
                if conditions:
                    raise EsdSyntaxError(node.lineno, "test() method defined more than once.")
                conditions = self.build_conditions(node.body)
            elif node.name == 'enter':
                if enter_commands:
                    raise EsdSyntaxError(node.lineno, "enter() method defined more than once.")
                enter_commands = [self.build_command(command_node) for command_node in node.body]
            elif node.name == 'exit':
                if exit_commands:
                    raise EsdSyntaxError(node.lineno, "exit() method defined more than once.")
                exit_commands = [self.build_command(command_node) for command_node in node.body]
            elif node.name == 'ongoing':
                if ongoing_commands:
                    raise EsdSyntaxError(node.lineno, "ongoing() method defined more than once.")
                ongoing_commands = [self.build_command(command_node) for command_node in node.body]
            else:
                raise EsdSyntaxError(node.lineno, f"Unexpected state function: '{node.name.id}'.")

        return self.ESD.State(self.ESD.esd_type, index, conditions, enter_commands, exit_commands, ongoing_commands)

    def scan_state(self, node):
        """ Get state name. """
        state_name = node.name
        docstring = ast.get_docstring(node)
        if docstring is None:
            raise EsdSyntaxError(node.lineno, f"No docstring given for state {state_name}.")
        try:
            state_index, description = self._STATE_DOCSTRING_RE.match(docstring).group(1, 2)
        except AttributeError:
            raise EsdSyntaxError(node.lineno, f"Invalid docstring for event {state_name}.")
        self.state_info[state_name] = {
            'index': int(state_index),
            'description': description,
            'nodes': node.body[1:],  # skip docstring
        }

    def build_command(self, node):
        """ Pass in the body of a function def, or a list of nodes before 'return' in a test block. """
        if self.is_state_machine_call(node):
            bank = 6  # TODO: True in every game/file?
            f_id = 0x80000000 - node.value.func.slice.value.n
            if not isinstance(f_id, int):
                raise EsdValueError(node.lineno, "State machine call must have an integer index.")
        elif self.is_call(node):
            try:
                bank, f_id = COMMANDS_BANK_ID_BY_TYPE_NAME[self.ESD.esd_type, node.value.func.id]
            except KeyError:
                bank, f_id = self._COMMAND_DEFAULT_RE.match(node.value.func.id).group(1, 2)
                bank, f_id = int(bank), int(f_id)
        else:
            raise EsdSyntaxError(node.lineno, f"Expected only function calls, not node type {type(node)}.")
        # TODO: Check arg count against canonical function, once available, and order keyword args.
        args = node.value.args + [keyword.value for keyword in node.value.keywords]
        command_args = [self.compile_ezl(arg) + b'\xa1' for arg in args]
        return self.ESD.Command(self.ESD.esd_type, bank, f_id, command_args)

    def reset_condition_registers(self):
        self.registers = [()] * 8
        self.state_call_set = set()
        self.to_write_count = 0  # number of registers used; cannot exceed 8.
        self.to_write = Queue()  # queue of first-time function calls to save for every (sub)condition in order
        self.written = {}  # maps function calls to register index 0-8
        self.current_to_write = []

    def build_conditions(self, if_nodes):
        """ Each node in the test() method should be an IF block containing:
            - optional sequence of 'pass commands'
            - optional sequence of subcondition IF blocks
            - optional return statement specifying a state class name to change to

        I'm only guessing that the 'pass commands' are run before the subconditions. In most resources (e.g. talk
        resources), pass command and subconditions are not used, but they are used extensively in, say, enemyCommon.esd,
        which is the core file controlling dynamic behavior in DS1.

        Returns a list of Condition instances.
        """
        if len(if_nodes) == 1 and isinstance(if_nodes[0], ast.Return):
            if isinstance(if_nodes[0].value, ast.UnaryOp):
                if (isinstance(if_nodes[0].value.op, ast.USub) and isinstance(if_nodes[0].value.operand, ast.Num)
                        and if_nodes[0].value.operand.n == 1):
                    # Last state of callable state machine.
                    return [self.ESD.Condition(self.ESD.esd_type, -1, b'\x41\xa1', [], [])]
                print(if_nodes[0].value.op, if_nodes[0].value.operand)
                raise EsdSyntaxError(if_nodes[0].lineno, f"Next state must be a valid State class or -1.")
            if not isinstance(if_nodes[0].value, ast.Name):
                print("Node:", if_nodes[0].value)
                raise EsdSyntaxError(if_nodes[0].lineno, "Condition IF block should return a state class name.")
            if if_nodes[0].value.id not in self.state_info:
                raise EsdError(if_nodes[0].lineno, f"Could not find a state class named '{if_nodes[0].value.id}'.")
            next_state_index = self.state_info[if_nodes[0].value.id]['index']
            return [self.ESD.Condition(self.ESD.esd_type, next_state_index, b'\x41\xa1', [], [])]

        for i, node in enumerate(if_nodes):
            if not isinstance(node, ast.If):
                raise EsdSyntaxError(node.lineno, "test() method must contain only IF blocks.")
            if node.orelse:
                if i != len(if_nodes) - 1:
                    raise EsdSyntaxError(node.lineno, "'else' block should only appear at the end of the tests.")
                if_nodes.append(ast.If(test=ast.Num(n=1), body=node.orelse, orelse=[]))

        conditions = []
        self.plan_condition_registers(if_nodes)  # Determines upcoming register saves/loads.

        for if_node in if_nodes:

            self.current_to_write = self.to_write.get()  # type: list
            test_ezl = self.compile_ezl(if_node.test) + b'\xa1'

            pass_commands = []
            subcondition_nodes = []
            next_state_index = -1

            pass_commands_allowed = True
            subconditions_allowed = True

            for j, node in enumerate(if_node.body):
                if self.is_call(node):
                    if not pass_commands_allowed:
                        raise EsdSyntaxError(node.lineno, "Encountered a pass command out of order in IF block.")
                    pass_commands.append(self.build_command(node))
                elif isinstance(node, ast.If):
                    if not subconditions_allowed:
                        raise EsdSyntaxError(node.lineno, "Encountered a subcondition out of order in IF block.")
                    pass_commands_allowed = False
                    subcondition_nodes.append(node)
                elif isinstance(node, ast.Return):
                    if j != len(if_node.body) - 1:
                        raise EsdSyntaxError(node.lineno, "'return NextState' should be last statement in IF block.")
                    if isinstance(node.value, ast.Num) and node.value.n == -1:
                        # Last state of callable state machine.
                        next_state_index = -1
                    else:
                        if not isinstance(node.value, ast.Name):
                            raise EsdSyntaxError(node.lineno, "Condition IF block should return a state class name.")
                        if node.value.id not in self.state_info:
                            raise EsdError(node.lineno, f"Could not find a state class named '{node.value.id}'.")
                        next_state_index = self.state_info[node.value.id]['index']

            # Condition registers are *not* reset when scanning and building subconditions.
            subconditions = self.build_conditions(subcondition_nodes) if subcondition_nodes else ()

            conditions.append(self.ESD.Condition(self.ESD.esd_type, next_state_index, test_ezl,
                                                 pass_commands, subconditions))

        return conditions

    def plan_condition_registers(self, if_node_list):
        """ Recursively scans conditions and any subconditions, determines the first eight repeated function calls that
        will be saved in/loaded from registers during build, and records their conditions in a queue.

        I have no idea how the original ESD compiler determines which functions to store in registers, given their
        limited availability. I'm simply storing the first eight functions that are used for a second time. I'm also
        assuming that the same registers are used for all subconditions.

        TODO: At least verify that subconditions use the same register state as parent conditions (check enemyCommon).
        """
        for i, if_node in enumerate(if_node_list):
            if not isinstance(if_node, ast.If):
                raise EsdSyntaxError(if_node.lineno, "test() method must contain only IF blocks.")

            # Process test nodes.
            first_time_calls = []
            call_list = self.get_calls(if_node.test)
            for call in call_list:
                if call in self.state_call_set and self.to_write_count < 8:
                    # Call occurs more than once, so we will use a register for it.
                    first_time_calls.append(call)
                    self.to_write_count += 1
                else:
                    self.state_call_set.add(call)
            self.to_write.put(first_time_calls)  # add to queue

            # Find and recursively process subconditions under the same register state. Order of encountered IF blocks
            # will be preserved in the 'to_write' queue.
            subconditions_allowed = True
            subcondition_nodes = []
            for body_node in if_node.body:
                if not isinstance(body_node, ast.If):
                    subconditions_allowed = False
                elif isinstance(body_node, ast.If):
                    if not subconditions_allowed:
                        raise EsdSyntaxError(body_node.lineno, "Encountered a subcondition out of order in IF block.")
                    subcondition_nodes.append(body_node)
            self.plan_condition_registers(subcondition_nodes)

    @staticmethod
    def parse_args(arg_nodes):
        args = []
        for node in arg_nodes:
            if isinstance(node, ast.Num):
                args.append(node.n)
            elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                args.append(-node.operand.n)
            elif isinstance(node, (ast.Subscript, ast.Name)):
                args.append(node)
            else:
                raise EsdValueError(node.lineno, "Function arguments must be numeric literals.")
        return tuple(args)

    def save_into_next_available_register(self, call):
        for i in range(len(self.registers)):
            if not self.registers[i]:
                self.registers[i] = call
                self.current_to_write.remove(call)
                return struct.pack('B', i + 167)

    def compile_test_function(self, call_node: ast.Call, equals=None):
        if call_node.keywords:
            raise EsdSyntaxError(call_node.lineno, "You cannot use keyword arguments in test functions (yet).")
        try:
            f_id = TEST_FUNCTIONS_ID_BY_TYPE_NAME[self.ESD.esd_type, call_node.func.id]
        except KeyError:
            try:
                f_id = int(self._TEST_DEFAULT_RE.match(call_node.func.id).group(1))
            except AttributeError:
                raise EsdValueError(call_node.lineno, f"Invalid ESD function name: '{call_node.func.id}'.")
        args = self.parse_args(call_node.args)
        call = (f_id, *args)

        if call in self.registers:
            # Load from register.
            return struct.pack('B', self.registers.index(call) + 175)

        compiled = self.compile_number(f_id) + b''.join(self.compile_ezl(arg) for arg in args)
        compiled += FUNCTION_ARG_BYTES_BY_COUNT[len(args)]
        if call in self.current_to_write:
            compiled += self.save_into_next_available_register(call)
            self.current_to_write.remove(call)
        if equals is not None:
            if equals == 0:
                compiled += b'\x40\x95'
            elif equals == 1:
                compiled += b'\x41\x95'
            else:
                raise ValueError("Internal error: 'equals' arg should only be 0 or 1 (or None).")
        return compiled

    def compile_ezl(self, node):

        if isinstance(node, (int, float)):
            return self.compile_number(node)

        if isinstance(node, ast.Num):
            return self.compile_number(node.n)

        if isinstance(node, str):
            return self.compile_string(node)

        if isinstance(node, ast.Str):
            return self.compile_string(node.s)

        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                if isinstance(node.operand, ast.Num):
                    return self.compile_number(-node.operand.n)
                raise EsdSyntaxError(node.lineno, "Tried to negate a non-numeric value. (TODO: Implement Negate op.)")
            elif isinstance(node.op, ast.Not):
                if self.is_call(node.operand):
                    return self.compile_test_function(node.operand, equals=1)
                raise EsdSyntaxError(node.lineno, "'not' keyword can only be applied to function calls.")

        if isinstance(node, ast.BoolOp):
            compiled = b''
            is_and = True if isinstance(node.op, ast.And) else False  # must be Or if false
            for i, value in enumerate(node.values):
                compiled += self.compile_ezl(value)
                if is_and and not self.current_to_write:
                    # There are no register writes remaining in this test, and no need to continue evaluation either.
                    # Append 'terminate if false' symbol for efficiency.
                    compiled += b'\xb7'
                else:
                    # Append 'continue if false' symbol for some reason. TODO: Is this necessary? When?
                    compiled += b'\xa6'
                if i > 0:
                    # Operator is added *per value*, as the chained comparison in Python is represented by one node.
                    compiled += b'\x98' if is_and else b'\x99'
            return compiled

        if isinstance(node, ast.BinOp):
            if type(node.op) not in OPERATORS_BY_NODE:
                raise EsdSyntaxError(node.lineno, f"Invalid binary operator: {type(node.op)}")
            return self.compile_ezl(node.left) + self.compile_ezl(node.right) + OPERATORS_BY_NODE[type(node.op)]

        if isinstance(node, ast.Compare):
            if len(node.comparators) != 1 or len(node.ops) != 1:
                # TODO: Redundant after scan. Have to figure out which errors are checked where.
                raise EsdSyntaxError(node.lineno, "Comparison should compare exactly two values.")
            if type(node.ops[0]) not in OPERATORS_BY_NODE:
                raise EsdSyntaxError(node.lineno, f"Invalid comparison operator: {type(node.ops[0])}")
            return (self.compile_ezl(node.left) + self.compile_ezl(node.comparators[0])
                    + OPERATORS_BY_NODE[type(node.ops[0])])

        if isinstance(node, ast.Call):
            return self.compile_test_function(node)

        if isinstance(node, ast.Name):
            if node.id == 'MACHINE_CALL_STATUS':
                return b'\xb9'
            elif node.id == 'ONGOING':
                return b'\xba'
            raise EsdSyntaxError(node.lineno, "Only valid name symbols are MACHINE_CALL_STATUS and ONGOING.")

        if isinstance(node, ast.Subscript):
            if (isinstance(node.value, ast.Name) and node.value.id == 'MACHINE_ARGS'
                    and isinstance(node.slice, ast.Index) and isinstance(node.slice.value, ast.Num)):
                return self.compile_number(node.slice.value.n) + b'\xb8'
            raise EsdSyntaxError(node.lineno, "Only valid subscripted symbol is MACHINE_ARGS[i].")

        raise TypeError(f"Invalid node type appeared in condition test: {type(node)}.\n"
                        f"Conditions must be bools, boolean ops, comparisons, function calls, or a permitted name.")

    @staticmethod
    def compile_number(n):
        if isinstance(n, int):
            if -64 <= n < 63:
                return struct.pack('B', n + 64)
            return b'\x82' + struct.pack('<i', n)
        elif isinstance(n, float):
            # TODO: How can I determine if I should write a single or double?
            #  I guess I could just always write a double.
            #  Or, maybe certain resources only use singles OR doubles.
            # return b'\x80' + struct.pack('<f', n)
            return b'\x81' + struct.pack('<d', n)  # Always double for now.
        else:
            raise ValueError(f"Cannot compile number {n} of type {type(n)}.")

    @staticmethod
    def compile_string(s):
        return b'\xa5' + s.encode('utf-16le') + b'\0\0'

    def get_calls(self, node):
        """ Returns a list of calls contained inside the given test node.

        Returns a list of call tuples (f_id, arg1, arg2, ...).
        """
        if self.is_bool(node) or isinstance(node, (ast.Name, ast.Num)):
            return []

        elif isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, (ast.Not, ast.USub)):
                # TODO: The only other unary operator is UAdd, which is harmless.
                # TODO: Not true, there's also Invert, which shouldn't be allowed.
                raise EsdSyntaxError(node.lineno, f"Only unary operators allowed are 'not' and '-', not {type(node)}.")
            return self.get_calls(node.operand)

        elif isinstance(node, ast.BoolOp):
            call_list = []
            for value in node.values:
                call_list += self.get_calls(value)
            return call_list

        elif isinstance(node, ast.BinOp):
            return self.get_calls(node.left) + self.get_calls(node.right)

        elif isinstance(node, ast.Compare):
            if len(node.comparators) != 1:
                raise EsdSyntaxError(node.lineno, "Comparison should compare exactly two values.")
            return self.get_calls(node.left) + self.get_calls(node.comparators[0])

        elif isinstance(node, ast.Call):
            function_name = node.func.id
            return [(function_name, *self.parse_args(node.args))]

        raise EsdSyntaxError(node.lineno, f"Invalid node type appeared in condition: {type(node)}\n"
                                          f"Conditions must be bools, boolean ops, comparisons, or function calls.")

    @staticmethod
    def is_bool(node):
        return isinstance(node, ast.NameConstant) and node.value in {True, False}

    @staticmethod
    def is_call(node):
        return isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)

    @staticmethod
    def is_state_machine_call(node):
        return (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Subscript)
                and isinstance(node.value.func.value, ast.Name) and node.value.func.value.id == 'CALL_STATE_MACHINE'
                and isinstance(node.value.func.slice, ast.Index) and isinstance(node.value.func.slice.value, ast.Num))

    @staticmethod
    def get_ast_sequence(node):
        """ List/tuple can only contain literals. """
        if isinstance(node, (ast.Tuple, ast.List)):
            t = []
            for e in node.elts:
                if isinstance(e, ast.Num):
                    t.append(e.n)
                elif isinstance(e, ast.Str):
                    t.append(e.s)
                else:
                    raise EsdValueError(node.lineno, f"Sequences must contain only numeric/string literals.")
            return t
        raise EsdSyntaxError(node.lineno, f"Expected a list or tuple node, but found: {type(node)}")
