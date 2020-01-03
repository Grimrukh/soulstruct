import abc
import struct
from collections import OrderedDict
from io import BytesIO
from pathlib import Path

from soulstruct.dcx import DCX
from soulstruct.events.evs import EvsParser
from soulstruct.events.numeric import build_numeric
from soulstruct.utilities import BaseStruct, read_chars_from_buffer, create_bak

from .event import BaseEvent


class BaseEMEVD(BaseStruct):
    Event = BaseEvent
    GAME_MODULE = None
    STRING_ENCODING = None
    DCX_MAGIC = None

    def __init__(self, emevd_source, script_path=None):

        if not self.GAME_MODULE:
            raise NotImplementedError("You cannot instantiate BaseEMEVD. Use a game-specific child, e.g. "
                                      "`from soulstruct.events.darksoul1 import EMEVD`.")

        self.events = OrderedDict()
        self.packed_strings = b''
        self.linked_file_offsets = []  # Offsets into packed strings.
        self.dcx = False

        if isinstance(emevd_source, EvsParser):
            self.map_name = emevd_source.map_name
            events, linked_file_offsets, packed_strings = build_numeric(emevd_source.numeric_emevd, self.Event)
            self.events.update(events)
            self.linked_file_offsets = linked_file_offsets
            self.packed_strings = packed_strings

        elif isinstance(emevd_source, dict):
            self.map_name = None
            try:
                self.linked_file_offsets = emevd_source.pop('linked')
            except KeyError:
                print("WARNING: No linked file offsets found in EMEVD source.")
            try:
                self.packed_strings = emevd_source.pop('strings')
            except KeyError:
                print("WARNING: No strings found in EMEVD source.")
            self.events.update(OrderedDict(emevd_source))

        elif isinstance(emevd_source, str) and '\n' in emevd_source:
            parsed = EvsParser(emevd_source, game_module=self.GAME_MODULE, script_path=script_path)
            self.map_name = parsed.map_name
            events, self.linked_file_offsets, self.packed_strings = build_numeric(parsed.numeric_emevd, self.Event)
            self.events.update(events)

        elif isinstance(emevd_source, Path) or (isinstance(emevd_source, str) and '\n' not in emevd_source):
            emevd_path = Path(emevd_source)
            self.map_name = emevd_path.stem

            if emevd_path.suffix in {'.evs', '.py'}:
                parsed = EvsParser(emevd_path, game_module=self.GAME_MODULE, script_path=script_path)
                self.map_name = parsed.map_name
                events, self.linked_file_offsets, self.packed_strings = build_numeric(parsed.numeric_emevd, self.Event)
                self.events.update(events)

            elif emevd_path.suffix == '.txt':
                try:
                    self.build_from_numeric_path(emevd_path)
                except Exception:
                    raise IOError(f"Could not interpret file '{str(emevd_path)}' as numeric-style EMEVD.\n"
                                  f"(Note that you cannot use verbose-style text files as EMEVD input.)\n"
                                  f"If your file is an EVS script, change the extension to '.py' or '.evs'.")

            elif emevd_path.name.endswith(".emevd.dcx"):
                emevd_data = DCX(emevd_path).data
                self.dcx = True  # DCX magic of EMEVD is applied automatically at pack.
                self.map_name = emevd_path.name.split('.')[0]  # Strip all extensions.
                try:
                    self.unpack(BytesIO(emevd_data))
                except Exception:
                    raise IOError(f"Could not interpret file '{str(emevd_path)}' as binary EMEVD data.\n"
                                  f"You should only use the '.emevd[.dcx]' extension for actual game-ready\n"
                                  f"EMEVD, which you can create with the `pack()` method of this class.")

            elif emevd_path.suffix == ".emevd":
                try:
                    with emevd_path.open('rb') as f:
                        self.unpack(f)
                except Exception:
                    raise IOError(f"Could not interpret file '{str(emevd_source)}' as binary EMEVD data.\n"
                                  f"You should only use the '.emevd' extension for actual game-ready\n"
                                  f"EMEVD, which you can create with the `pack()` method of this class.")

            else:
                raise TypeError(f"Cannot open EMEVD from source {emevd_source} with type {type(emevd_source)}.")

        elif isinstance(emevd_source, bytes):
            self.map_name = None
            self.unpack(BytesIO(emevd_source))

        else:
            raise TypeError(f"Cannot open EMEVD from source type: {type(emevd_source)}")

    def unpack(self, emevd_buffer):
        header = self.STRUCT.unpack(emevd_buffer)

        emevd_buffer.seek(header.event_table_offset)
        self.events.update(self.Event.unpack(
            emevd_buffer, header.instruction_table_offset, header.base_arg_data_offset,
            header.event_arg_table_offset, header.event_layers_table_offset, count=header.event_count))

        if header.packed_strings_size != 0:
            emevd_buffer.seek(header.packed_strings_offset)
            self.packed_strings = emevd_buffer.read(header.packed_strings_size)

        if header.linked_files_count != 0:
            emevd_buffer.seek(header.linked_files_table_offset)
            # These are relative offsets into the packed string data.
            for _ in range(header.linked_files_count):
                self.linked_file_offsets.append(struct.unpack('<Q', emevd_buffer.read(8))[0])

    def build_from_numeric_path(self, numeric_path):
        numeric_path = Path(numeric_path)
        with numeric_path.open('r', encoding='utf-8') as f:
            numeric_string = f.read()
        events, self.linked_file_offsets, self.packed_strings = build_numeric(numeric_string, self.Event)
        self.events.update(events)

    @property
    def event_count(self):
        return len(self.events)

    @property
    def instruction_count(self):
        return sum([e.instruction_count for e in self.events.values()])

    def build_event_layers_table(self):
        """Scans all Instructions for event layers and packs them into a table.

        Also sets the offset within each Instruction so that it can be packed.
        """
        packed_event_layers_table = []
        for event in self.events.values():
            for instruction in event.instructions:
                if instruction.event_layers:
                    packed_event_layers = instruction.event_layers.pack()
                    try:
                        existing_offset = (packed_event_layers_table.index(packed_event_layers)
                                           * self.Event.Instruction.EventLayers.STRUCT.size)
                        instruction.event_layers_offset = existing_offset
                    except ValueError:
                        new_offset = self.Event.Instruction.EventLayers.STRUCT.size * len(packed_event_layers_table)
                        packed_event_layers_table.append(packed_event_layers)
                        instruction.event_layers_offset = new_offset
                else:
                    # No event layers for this instruction.
                    instruction.event_layers_offset = -1
        return packed_event_layers_table

    @abc.abstractmethod
    def compute_base_args_size(self, existing_data_size):
        """Works different for DS1 vs. other games."""
        ...

    @abc.abstractmethod
    def pad_after_base_args(self, emevd_binary_after_base_args):
        """Works different for DS1 vs. other games."""
        ...

    @property
    def event_arg_count(self):
        return sum([e.event_arg_count for e in self.events.values()])

    def compute_table_offsets(self, event_layers_table):
        offsets = {'event': self.STRUCT.size}
        offsets['instruction'] = offsets['event'] + self.Event.STRUCT.size * self.event_count
        # Ignore empty unknown table.
        offsets['event_layers'] = offsets['instruction'] + self.Event.Instruction.STRUCT.size * self.instruction_count
        offsets['base_arg_data'] = offsets['event_layers'] + (self.Event.Instruction.EventLayers.STRUCT.size
                                                              * len(event_layers_table))
        offsets['event_arg'] = offsets['base_arg_data'] + self.compute_base_args_size(offsets['base_arg_data'])
        offsets['linked_files'] = offsets['event_arg'] + self.Event.EventArg.STRUCT.size * self.event_arg_count
        offsets['packed_strings'] = offsets['linked_files'] + 8 * len(self.linked_file_offsets)
        offsets['end_of_file'] = offsets['packed_strings'] + len(self.packed_strings)
        return offsets

    def build_emevd_header(self):
        # TODO: Stop calculating offsets twice. Just calculate them during binary pack and create header last.
        event_layers_table = self.build_event_layers_table()  # TODO: Also building this twice...
        offsets = self.compute_table_offsets(event_layers_table)
        header_dict = {
            'file_size_1': offsets['end_of_file'],
            'event_count': self.event_count,
            'event_table_offset': offsets['event'],
            'instruction_count': self.instruction_count,
            'instruction_table_offset': offsets['instruction'],
            'unknown_table_offset': offsets['base_arg_data'],  # Absent.
            'event_layers_count': len(event_layers_table),
            'event_layers_table_offset': offsets['event_layers'],
            'event_arg_count': self.event_arg_count,
            'event_arg_table_offset': offsets['event_arg'],
            'linked_files_count': len(self.linked_file_offsets),
            'linked_files_table_offset': offsets['linked_files'],
            'base_arg_data_size': self.compute_base_args_size(offsets['base_arg_data']),  # Note different table order.
            'base_arg_data_offset': offsets['base_arg_data'],
            'packed_strings_size': len(self.packed_strings),
            'packed_strings_offset': offsets['packed_strings'],
        }
        return self.STRUCT.pack(header_dict)

    def get_linked_file_names(self):
        names = []
        for offset in self.linked_file_offsets:
            names.append(read_chars_from_buffer(self.packed_strings, offset=offset))
        return names

    def unpack_strings(self):
        strings = []
        string_buffer = BytesIO(self.packed_strings)
        while string_buffer.tell() != len(self.packed_strings):
            offset = string_buffer.tell()
            string = read_chars_from_buffer(string_buffer, reset_old_offset=False, encoding=self.STRING_ENCODING)
            strings.append((str(offset), string))  # repr to include double backslash
        return strings

    def to_numeric(self):
        numeric_output = "\n\n".join([event.to_numeric() for event in self.events.values()])
        numeric_output += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_file_offsets)
        numeric_output += "\n\nstrings:\n" + "\n".join(s[0] + ': ' + s[1] for s in self.unpack_strings())
        return numeric_output

    def get_evs_docstring(self):
        docstring = '"""'
        docstring += "\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_file_offsets)
        docstring += "\n\nstrings:\n" + "\n".join(s[0] + ': ' + repr(s[1]).strip("'") for s in self.unpack_strings())
        docstring += '\n"""'
        return docstring

    def to_evs(self):
        docstring = self.get_evs_docstring()
        imports = f'from {self.GAME_MODULE.__name__} import *'
        for event in self.events.values():
            # Build global optional event argument dictionary.
            event.get_evs_function_args()
        evs_events = [event.to_evs(self.GAME_MODULE) for event in self.events.values()]
        return docstring + '\n' + "\n\n\n".join([imports] + evs_events) + '\n'

    def pack(self, dcx=None):
        if dcx is None:
            # Auto-detect DCX compression from source file (if applicable).
            dcx = self.dcx

        event_table_binary = b''
        instr_table_binary = b''
        argument_data_binary = b''
        arg_r_binary = b''

        current_instruction_offset = 0
        current_arg_data_offset = 0
        current_event_arg_offset = 0

        header = self.build_emevd_header()

        for e in self.events.values():
            e_bin, i_bin, a_bin, p_bin = e.to_binary(
                current_instruction_offset, current_arg_data_offset, current_event_arg_offset)

            event_table_binary += e_bin
            instr_table_binary += i_bin
            argument_data_binary += a_bin
            arg_r_binary += p_bin

            if len(i_bin) != self.Event.Instruction.STRUCT.size * e.instruction_count:
                raise ValueError(f"Event ID: {e.event_id} returned packed instruction binary of size {len(i_bin)} but "
                                 f"reports {e.instruction_count} total instructions (with expected size "
                                 f"{self.Event.Instruction.STRUCT.size * e.instruction_count}).")
            if len(p_bin) != self.Event.EventArg.STRUCT.size * e.event_arg_count:
                raise ValueError(f"Event ID: {e.event_id} returned packed arg replacement binary of size {len(p_bin)} "
                                 f"but reports {e.event_arg_count} total replacements (with expected size "
                                 f"{self.Event.EventArg.STRUCT.size * e.event_arg_count}).")
            if len(a_bin) != e.total_args_size:
                raise ValueError(f"Event ID: {e.event_id} returned packed argument data binary of size {len(a_bin)} "
                                 f"but reports expected size to be {e.total_args_size}).")

            current_instruction_offset += len(i_bin)
            current_arg_data_offset += len(a_bin)
            current_event_arg_offset += len(p_bin)

        linked_file_data_binary = struct.pack('<' + 'Q' * len(self.linked_file_offsets), *self.linked_file_offsets)
        event_layers_table = self.build_event_layers_table()
        event_layers_binary = b''.join(event_layers_table)

        emevd_binary = b''
        offsets = self.compute_table_offsets(event_layers_table)
        if len(header) != offsets['event']:
            raise ValueError(f"Header was of size {len(header)} but expected size was {self.STRUCT.size}.")
        emevd_binary += header
        if len(emevd_binary) + len(event_table_binary) != offsets['instruction']:
            raise ValueError(f"Event table was of size {len(event_table_binary)} but expected size was "
                             f"{offsets['instruction'] - len(emevd_binary)}.")
        emevd_binary += event_table_binary
        if len(emevd_binary) + len(instr_table_binary) != offsets['event_layers']:
            raise ValueError(f"Instruction table was of size {len(instr_table_binary)} but expected size was "
                             f"{offsets['event_layers'] - len(emevd_binary)}.")
        emevd_binary += instr_table_binary
        if len(emevd_binary) + len(event_layers_binary) != offsets['base_arg_data']:
            raise ValueError(f"Event layers table was of size {len(event_layers_binary)} but expected size was "
                             f"{offsets['base_arg_data'] - len(emevd_binary)}.")

        emevd_binary += event_layers_binary

        # No argument data length check due to padding.
        emevd_binary += argument_data_binary
        emevd_binary = self.pad_after_base_args(emevd_binary)

        if len(emevd_binary) + len(arg_r_binary) != offsets['linked_files']:
            raise ValueError(f"Argument replacement table was of size {len(linked_file_data_binary)} but expected size "
                             f"was {offsets['linked_files'] - len(emevd_binary)}.")
        emevd_binary += arg_r_binary
        if len(emevd_binary) + len(linked_file_data_binary) != offsets['packed_strings']:
            raise ValueError(f"Linked file data was of size {len(linked_file_data_binary)} but expected size was "
                             f"{offsets['packed_strings'] - len(emevd_binary)}.")
        emevd_binary += linked_file_data_binary
        if len(emevd_binary) + len(self.packed_strings) != offsets['end_of_file']:
            raise ValueError(f"Packed string data was of size {len(linked_file_data_binary)} but expected size was "
                             f"{offsets['end_of_file'] - len(emevd_binary)}.")
        emevd_binary += self.packed_strings

        if dcx:
            return DCX(emevd_binary, magic=self.DCX_MAGIC).pack()
        return emevd_binary

    def write_emevd(self, emevd_path=None, dcx=None):
        if dcx is None:
            dcx = self.dcx
        if not emevd_path:
            emevd_path = self.map_name
            if dcx and not emevd_path.endswith('.emevd.dcx'):
                emevd_path += '.emevd.dcx'
            elif not emevd_path.endswith('.emevd'):
                emevd_path += '.emevd'
        emevd_path = Path(emevd_path)
        if emevd_path.parent:
            emevd_path.parent.mkdir(exist_ok=True, parents=True)
        create_bak(emevd_path)
        with emevd_path.open('wb') as f:
            f.write(self.pack(dcx))

    def write_numeric(self, numeric_path=None):
        if not numeric_path:
            numeric_path = self.map_name
            if not numeric_path.endswith('.numeric.txt'):
                numeric_path += '.numeric.txt'
        numeric_path = Path(numeric_path)
        if numeric_path.parent:
            numeric_path.parent.mkdir(exist_ok=True, parents=True)
        with numeric_path.open('w', encoding='utf-8') as f:
            f.write(self.to_numeric())

    def write_evs(self, evs_path=None):
        if not evs_path:
            evs_path = self.map_name
            if not evs_path.endswith('.evs.py'):
                evs_path += '.evs.py'
        evs_path = Path(evs_path)
        if evs_path.parent:
            evs_path.parent.mkdir(exist_ok=True, parents=True)
        with evs_path.open('w', encoding='utf-8') as f:
            f.write(self.to_evs())
