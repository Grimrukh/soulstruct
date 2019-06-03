from collections import OrderedDict
from io import BytesIO
import os
import re
import struct
from soulstruct.core import BinaryStruct, read_chars
from soulstruct.dcx import DCX
from soulstruct.emevd.evs_parser import EmevdCompiler
from soulstruct.emevd import verbose
from soulstruct.emevd.shared import decompiler
from soulstruct.emevd.shared.enums import RestartType

INSTRUCTION_RE = re.compile(r" [ ]*(\d+)\[(\d+)\] \(([iIhHbBfs|]*)\)\[([\d, .-]*)\]")
EVENT_ARG_REPLACEMENT_RE = re.compile(r" [ ]*\^\((\d+) <- (\d+), (\d+)\)")
HEADER_RE = re.compile(r"^(\d+), ([012])")
ELEMENT_MIN_MAX = {'b': (-128, 127), 'B': (0, 255),
                   'h': (-32768, 32767), 'H': (0, 65535),
                   'i': (-2147483648, 2147483647), 'I': (0, 4294967295)}
EVS_ARG_TYPES = {'i': 'int', 'I': 'uint', 'f': 'float', 'h': 'short', 'H': 'ushort', 'b': 'char', 'B': 'uchar',
                 's': 'int'}

EVENT_ARG_TYPES = {}  # Global dictionary that maps event IDs to their type strings. Refreshed each verbose/EVS build.


def get_byte_offset_from_struct(format_string):
    """ Returns a dictionary of {byte_offset: (struct_index, struct_format)}. The byte offsets indicate where the
    associated element in the struct format string begins. Note that endian-type '@' (native byte alignment) is
    critical here, as EMEVD uses byte-aligned packed binary data. """
    endian = format_string[0]
    format_string = format_string[1:]
    byte_offset_array = {}
    for i in range(0, len(format_string)):
        offset = struct.calcsize(endian + format_string[:i + 1]) - struct.calcsize(endian + format_string[i])
        byte_offset_array[offset] = (i, format_string[i])
    return byte_offset_array


def get_instruction_args(file, instruction_class, instruction_index, first_arg_offset, event_args_size, format_dict):
    """ Process instruction arguments (required and optional) from EMEVD binary. """

    previous_offset = file.tell()
    if event_args_size == 0:
        return "", []
    try:
        args_format = format_dict[instruction_class][instruction_index]
    except KeyError:
        raise KeyError(f"Cannot find argument types for instruction {instruction_class}[{instruction_index}].")

    # 's' arguments are actually four-byte offsets into the packed string data, though we will keep the 's' symbol.
    true_args_format = args_format.replace('s', 'I')
    required_args_size = struct.calcsize(true_args_format)
    if required_args_size > event_args_size:
        raise ValueError(f"Documented size of minimum required args for instruction {instruction_class}"
                         f"[{instruction_index}] is {required_args_size}, but size of args specified in EMEVD file is "
                         f"only {event_args_size}.")

    file.seek(first_arg_offset)
    req_args = struct.unpack(true_args_format, file.read(required_args_size))

    # Additional arguments may appear for the instruction 2000[00], 'RunEvent'. These instructions are tightly packed,
    # and are simply read here as unsigned integers; we need to actually parse the event to interpret them properly.

    extra_size = event_args_size - required_args_size

    opt_arg_count = extra_size // 4
    if opt_arg_count == 0:
        file.seek(previous_offset)
        return args_format[1:], list(req_args)
    elif extra_size % 4 != 0:
        raise ValueError(f"Optional argument size must be a multiple of four bytes. Your EMEVD file seems malformed.")

    opt_args = [struct.unpack('<I', file.read(4))[0] for _ in range(opt_arg_count)]
    file.seek(previous_offset)
    return args_format[1:] + "|" + "I" * (extra_size // 4), list(req_args) + opt_args


class BaseEMEVD(object):

    GAME_MODULE = None
    HEADER_STRUCT: BinaryStruct = None
    STRING_ENCODING = None
    DCX_MAGIC = None

    class Event(object):

        use = 0
        STRUCT: BinaryStruct = None

        class Instruction(object):

            STRUCT: BinaryStruct = None
            INSTRUCTION_ARG_TYPES = {}

            def __init__(self, instruction_class, instruction_index, args_format='', args_list=None):
                if len(args_format.replace('|', '')) != len(args_list):
                    raise ValueError(f"Length of argument list ({len(args_list)}) in Instruction {instruction_class}"
                                     f"[{instruction_index}] does not match length of format string '{args_format}' "
                                     f"({len(args_format.replace('|', ''))}).")
                self.instruction_class = instruction_class
                self.instruction_index = instruction_index
                self.visible_args_format = args_format  # preserves 's' for printing output
                self.args_format = args_format.replace('s', 'I')
                self.args_list = args_list if args_list else []
                self.event_args = []  # Added after construction.
                self.verbose_args_list = []  # So we don't modify 'args_list'.

            @classmethod
            def unpack(cls, file, base_arg_data_offset, count=1):
                """ Unpack some number of Instructions into a list, starting from the current file offset. """

                instructions = []
                struct_dicts = cls.STRUCT.unpack(file, count=count)
                for i, d in enumerate(struct_dicts):
                    try:
                        args_format, args_list = get_instruction_args(
                            file, d.instruction_class, d.instruction_index,
                            base_arg_data_offset + d.first_base_arg_offset, d.base_args_size,
                            cls.INSTRUCTION_ARG_TYPES)
                    except KeyError:
                        print("Raw arg data:")
                        args_size = struct_dicts[i + 1].first_base_arg_offset - d.first_base_arg_offset
                        file.seek(base_arg_data_offset + d.first_base_arg_offset)
                        print(file.read(args_size))
                        raise

                    instructions.append(cls(d.instruction_class, d.instruction_index, args_format, args_list))

                return instructions

            @property
            def args_size(self):
                return struct.calcsize("@" + self.args_format.replace('|', ''))

            @property
            def event_arg_count(self):
                return len(self.event_args)

            def to_numeric(self):
                numeric = [f"{self.instruction_class:04d}[{self.instruction_index:02d}] "
                           f"({self.visible_args_format})" + repr(self.args_list)]
                for replacement in self.event_args:
                    numeric.append("   ^" + replacement.to_numeric())
                return numeric

            def to_verbose(self, game_module):
                return verbose.verbose_instruction(
                    self.instruction_class, self.instruction_index, *self.get_required_and_optional_args(), game_module)

            def to_evs(self, game_module):
                global EVENT_ARG_TYPES
                req_args, opt_args = self.get_required_and_optional_args()
                if self.instruction_class == 2000 and self.instruction_index == 0 and opt_args:
                    try:
                        opt_arg_types = EVENT_ARG_TYPES[req_args[1]]
                    except KeyError:
                        pass
                    else:
                        return decompiler.decompile_instruction(
                            game_module, self.instruction_class, self.instruction_index, req_args, opt_args,
                            opt_arg_types)
                return decompiler.decompile_instruction(
                    game_module, self.instruction_class, self.instruction_index, req_args, opt_args)

            def get_required_and_optional_args(self):
                split_point = self.visible_args_format.find('|')
                if split_point == -1:
                    required_args = self.verbose_args_list
                    optional_args = []
                else:
                    required_args = self.verbose_args_list[:split_point]
                    optional_args = self.verbose_args_list[split_point:]
                return required_args, optional_args

            def apply_event_event_args(self):
                """ Inserts arg replacements into the appropriate places in their instructions for readability (verbose
                output only). The arg replacements are represented as 'Xi:j', where i and j specify the byte range read
                from the arguments passed to the RunEvent instruction.

                Also returns a dictionary that allows the RunEvent instruction to guess the format of its arguments,
                based on how they are actually used in the event instructions.
                """

                permitted = [0, 0.0, -1, 1, 10]  # Strings are permitted to overwrite anything.
                arg_offset_dict = get_byte_offset_from_struct("@" + self.visible_args_format.replace('|', ''))

                instruction_arg_set = set()
                instruction_arg_types = {}

                self.verbose_args_list = self.args_list.copy()

                for arg_r in self.event_args:
                    try:
                        argument_index, argument_byte_type = arg_offset_dict[arg_r.write_from_byte]
                    except KeyError:
                        raise ValueError(
                            f"No argument in '{self.event_args}' begins at byte {arg_r.write_from_byte}. "
                            f"Your replacement commands are misaligned.")

                    if (not (argument_byte_type == 's' and arg_r.bytes_to_write == 4)
                            and struct.calcsize(argument_byte_type) < arg_r.bytes_to_write):
                        # Byte type 's' is actually a four-byte offset into the packed strings.
                        raise ValueError(f"You cannot write {arg_r.bytes_to_write} bytes over an argument of type "
                                         f"{argument_byte_type} (it's too small).")
                    value_to_overwrite = self.args_list[argument_index]
                    arg_name = f"ARG_{arg_r.read_from_byte}_{arg_r.read_from_byte + arg_r.bytes_to_write - 1}"

                    if (value_to_overwrite not in permitted and value_to_overwrite != arg_name
                            and argument_byte_type != 's'):
                        print(f"{self.instruction_class}[{self.instruction_index}]", self.args_format, self.args_list)
                        raise ValueError(f"Parameter {arg_name} is overwriting non-zero value {value_to_overwrite} "
                                         f"(position {argument_index}).")

                    self.verbose_args_list[argument_index] = arg_name

                    instruction_arg_set.add((arg_r.read_from_byte, arg_r.read_from_byte + arg_r.bytes_to_write - 1))
                    if arg_name not in instruction_arg_types:
                        instruction_arg_types[arg_name] = set(argument_byte_type)
                    else:
                        instruction_arg_types[arg_name].add(argument_byte_type)

                return instruction_arg_set, instruction_arg_types

            def args_list_to_binary(self):
                if self.args_list:
                    format_string = "@" + self.args_format.replace('|', '')
                    return struct.pack(format_string, *self.args_list)
                else:
                    return b''

            def event_event_args_to_binary(self):
                return b''.join([arg_replacement.to_binary() for arg_replacement in self.event_args])

            def to_binary(self, first_base_arg_offset):
                struct_dict = {
                    'instruction_class': self.instruction_class,
                    'instruction_index': self.instruction_index,
                    'base_args_size': self.args_size,
                    'first_base_arg_offset': first_base_arg_offset,
                }
                return self.STRUCT.pack(struct_dict)

        class EventArg(object):
            """ Overrides argument data in a particular instruction using from dynamic args attached to the event. (Each
            instance of this should be attached to a specific Instruction instance.) """

            STRUCT: BinaryStruct = None

            def __init__(self, instruction_line, write_from_byte=0, read_from_byte=0, bytes_to_write=0, zero=0):
                self.line = instruction_line
                self.write_from_byte = write_from_byte
                self.read_from_byte = read_from_byte
                self.bytes_to_write = bytes_to_write
                if zero != 0:
                    raise ValueError("Last field of arg replacement must be zero.")

            @classmethod
            def unpack(cls, file, count=1):

                event_args = []
                struct_dicts = cls.STRUCT.unpack(file, count=count)

                for d in struct_dicts:
                    event_args.append(cls(**d))

                return event_args

            def to_numeric(self):
                return f"({self.write_from_byte} <- {self.read_from_byte}, {self.bytes_to_write})"

            def to_binary(self):
                return self.STRUCT.pack(instruction_line=self.line, write_from_byte=self.write_from_byte,
                                        read_from_byte=self.read_from_byte, bytes_to_write=self.bytes_to_write)

        def __init__(self, event_id=0, restart_type=0, instruction_list=None):
            if not self.use:
                pass  # TODO
            self.event_id = event_id
            self.restart_type = restart_type
            self.instruction_list = instruction_list if instruction_list else []

        @classmethod
        def unpack(cls, file, instruction_table_offset, base_arg_data_offset, event_arg_table_offset, count=1):

            event_dict = OrderedDict()
            struct_dicts = cls.STRUCT.unpack(file, count=count)

            for d in struct_dicts:
                file.seek(instruction_table_offset + d['first_instruction_offset'])
                instruction_list = cls.Instruction.unpack(file, base_arg_data_offset, count=d['instruction_count'])

                file.seek(event_arg_table_offset + d['first_event_arg_offset'])
                event_args = cls.EventArg.unpack(file, count=d['event_arg_count'])

                for arg_r in event_args:
                    # Attach event arg replacements to their instruction line.
                    instruction_list[arg_r.line].event_args.append(arg_r)

                event_dict[d['event_id']] = cls(d['event_id'], d['restart_type'], instruction_list)

            return event_dict

        @property
        def instruction_count(self):
            return len(self.instruction_list)

        @property
        def total_args_size(self):
            return sum([i.args_size for i in self.instruction_list])

        @property
        def event_arg_count(self):
            return sum([i.event_arg_count for i in self.instruction_list])

        def to_numeric(self):
            event_string = f"{self.event_id}, {self.restart_type}"
            for instruction in self.instruction_list:
                event_string += "\n " + "\n ".join(instruction.to_numeric())
            return event_string

        def guess_parameter_types(self):
            event_arg_set = set()
            event_arg_types = {}
            for instruction in self.instruction_list:
                instruction_arg_set, instruction_arg_types = instruction.apply_event_event_args()
                event_arg_set = event_arg_set.union(instruction_arg_set)
                for x in instruction_arg_types:
                    if x not in event_arg_types:
                        event_arg_types[x] = set(instruction_arg_types[x])
                    else:
                        event_arg_types[x] = event_arg_types[x].union(instruction_arg_types[x])
            return list(sorted(event_arg_set)), event_arg_types

        def get_verbose_parameters(self):
            sorted_parameter_list, event_arg_types = self.guess_parameter_types()
            event_args_list = [f'ARG_{i}_{j}' for i, j in sorted_parameter_list]
            event_args_format = ''.join(['|'.join(''.join((event_arg_types[arg])) for arg in event_args_list)])
            return f"Event Arguments: {{{', '.join([s for s in event_args_list])}}} ({event_args_format})"

        def get_evs_function_args(self):
            global EVENT_ARG_TYPES
            sorted_parameter_list, event_arg_types = self.guess_parameter_types()
            evs_function_args_names = [f'ARG_{i}_{j}' for i, j in sorted_parameter_list]
            evs_function_args_types = [EVS_ARG_TYPES[next(iter(event_arg_types[arg]))] for arg in
                                       evs_function_args_names]
            evs_function_args = [f'{arg_name}: {arg_type}'
                                 for arg_name, arg_type in zip(evs_function_args_names, evs_function_args_types)]
            EVENT_ARG_TYPES[self.event_id] = ''.join(
                [next(iter(event_arg_types[arg])) for arg in evs_function_args_names])
            return ', '.join(evs_function_args)

        def to_verbose(self, game_module, with_line_numbers=False):
            verbose_event_string = (f"Event ID: {self.event_id}\nRestarts: "
                                    f"{verbose.ENUM_RESTART_TYPE.get(self.restart_type, self.restart_type)}")
            verbose_event_string += "\n" + self.get_verbose_parameters()  # Also creates 'X[i:j]' instruction arg names.
            for i, instr in enumerate(self.instruction_list):
                if with_line_numbers:
                    verbose_event_string += f'\n    {i:3d} {instr.to_verbose(game_module)}'
                else:
                    verbose_event_string += f'\n    {instr.to_verbose(game_module)}'
            return verbose_event_string

        def to_evs(self, game_module):
            if self.event_id == 0:
                function_name = 'Constructor'
            elif self.event_id == 50:
                function_name = 'Preconstructor'
            else:
                function_name = f'Event{self.event_id}'
            function_docstring = f'""" {self.event_id}: Event {self.event_id} """'
            function_args = self.get_evs_function_args()  # Also creates 'ARG_i_j' instruction arg names.
            evs_event_string = (f"@{RestartType(self.restart_type).name}\n"
                                f"def {function_name}({function_args}):\n"
                                f"    {function_docstring}")
            for i, instr in enumerate(self.instruction_list):
                evs_event_string += f"\n    {instr.to_evs(game_module)}"
            return evs_event_string

        def to_binary(self, instruction_offset, first_base_arg_offset, first_event_arg_offset):
            if self.event_arg_count == 0:
                first_event_arg_offset = -1

            event_binary = self.STRUCT.pack(
                {
                    'event_id': self.event_id,
                    'instruction_count': self.instruction_count,
                    'first_instruction_offset': instruction_offset,
                    'event_arg_count': self.event_arg_count,
                    'first_event_arg_offset': first_event_arg_offset,
                    'restart_type': self.restart_type,
                }
            )

            base_arg_offset = first_base_arg_offset

            instructions_binary = b''
            args_binary = b''
            event_args_list = []
            for instruction in self.instruction_list:
                instructions_binary += instruction.to_binary(base_arg_offset)

                arg_binary = instruction.args_list_to_binary()
                args_binary += arg_binary
                base_arg_offset += len(arg_binary)

                event_args_list += instruction.event_args

            # Collect and sort arg replacements to better match actual EMEVD files. (Should be purely cosmetic.)
            sorted_event_args = sorted(event_args_list, key=lambda arg_r: (arg_r.read_from_byte, arg_r.line))
            event_args_binary = b''.join([arg_r.to_binary() for arg_r in sorted_event_args])

            return event_binary, instructions_binary, args_binary, event_args_binary

    def __init__(self, emevd_source, vanilla_base_map=''):

        if not self.GAME_MODULE:
            raise ValueError("Do not use the BaseEMEVD class. Use the EMEVD class from the particular game you want.")

        self.events = OrderedDict()
        self.packed_strings = b''
        self.linked_file_offsets = []  # Offsets into packed strings.
        self._dcx = False

        if vanilla_base_map:
            if not os.path.isfile(vanilla_base_map):
                # Try resolving in local package directory.
                vanilla_base_map = os.path.join(
                    os.path.dirname(__file__), 'vanilla_numeric_ptd', vanilla_base_map + '.numeric.txt')
            if not os.path.isfile(vanilla_base_map):
                raise FileNotFoundError(f"Could not find vanilla numeric event file '{vanilla_base_map}' in package.")
            emevd_dict = numeric_file_to_emevd_dict(vanilla_base_map, self.GAME_MODULE)
            self.linked_file_offsets = emevd_dict.pop('linked')
            self.packed_strings = emevd_dict.pop('strings')
            self.events.update(emevd_dict)

        if isinstance(emevd_source, EmevdCompiler):
            self.map_name = emevd_source.map_name
            emevd_dict = numeric_string_to_event_dict(emevd_source.numeric_emevd, self.GAME_MODULE)
            self.linked_file_offsets = emevd_dict.pop('linked')
            self.packed_strings = emevd_dict.pop('strings')
            self.events.update(emevd_dict)

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

        elif isinstance(emevd_source, str):
            self.map_name = os.path.splitext(emevd_source)[0]

            if emevd_source.endswith('.py') or emevd_source.endswith('.evs'):
                emevd_source = EmevdCompiler(emevd_source, self.GAME_MODULE)
                self.map_name = emevd_source.map_name
                emevd_dict = numeric_string_to_event_dict(emevd_source.numeric_emevd, self.GAME_MODULE)
                self.linked_file_offsets = emevd_dict.pop('linked')
                self.packed_strings = emevd_dict.pop('strings')
                self.events.update(emevd_dict)

            elif emevd_source.endswith('.txt'):
                try:
                    emevd_dict = numeric_file_to_emevd_dict(emevd_source, self.GAME_MODULE)
                    self.linked_file_offsets = emevd_dict.pop('linked')
                    self.packed_strings = emevd_dict.pop('strings')
                    self.events.update(emevd_dict)
                except Exception:
                    raise IOError(f"Could not interpret file '{emevd_source}' as numeric-style EMEVD.\n"
                                  f"(Note that you cannot use verbose-style text files as EMEVD input.)\n"
                                  f"If your file is an EVS script, change the extension to '.py' or '.evs'.")

            elif emevd_source.endswith('.emevd.dcx'):
                emevd_data = DCX(emevd_source).data
                self._dcx = True
                self.map_name = os.path.splitext(self.map_name)[0]  # Strip both extensions.
                try:
                    self.unpack(BytesIO(emevd_data))
                except Exception:
                    raise IOError(f"Could not interpret file '{emevd_source}' as binary EMEVD data.\n"
                                  f"You should only use the '.emevd[.dcx]' extension for actual game-ready\n"
                                  f"EMEVD, which you can create with the `pack()` method of this class.")

            elif emevd_source.endswith('.emevd'):
                try:
                    with open(emevd_source, 'rb') as file:
                        self.unpack(file)
                except Exception:
                    raise IOError(f"Could not interpret file '{emevd_source}' as binary EMEVD data.\n"
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
        header = self.HEADER_STRUCT.unpack(emevd_buffer)

        emevd_buffer.seek(header.event_table_offset)
        self.events.update(self.Event.unpack(
            emevd_buffer, header.instruction_table_offset, header.base_arg_data_offset,
            header.event_arg_table_offset, count=header.event_count))

        if header.packed_strings_size != 0:
            emevd_buffer.seek(header.packed_strings_offset)
            self.packed_strings = emevd_buffer.read(header.packed_strings_size)

        if header.linked_files_count != 0:
            emevd_buffer.seek(header.linked_files_table_offset)
            # These are relative offsets into the packed string data.
            for _ in range(header.linked_files_count):
                self.linked_file_offsets.append(struct.unpack('<Q', emevd_buffer.read(8))[0])

    @classmethod
    def build_from_numeric_file_path(cls, numeric_path):
        return cls(numeric_file_to_emevd_dict(numeric_path, cls.GAME_MODULE))

    @property
    def event_count(self):
        return len(self.events)

    @property
    def instruction_count(self):
        return sum([e.instruction_count for e in self.events.values()])

    def compute_base_args_size(self, existing_data_size):
        """ Must be overridden, as it works different for DS1 vs. the rest. """
        raise NotImplementedError

    def pad_after_base_args(self, emevd_binary_after_base_args):
        """ Must be overridden, as it works different for DS1 vs. the rest. """
        raise NotImplementedError

    @property
    def event_arg_count(self):
        return sum([e.event_arg_count for e in self.events.values()])

    def compute_table_offsets(self):
        offsets = {'event': self.HEADER_STRUCT.size}
        offsets['instruction'] = offsets['event'] + self.Event.STRUCT.size * self.event_count
        # Ignore unknown table.
        # Ignore event layer table (for now).
        offsets['base_arg_data'] = offsets['instruction'] + self.Event.Instruction.STRUCT.size * self.instruction_count
        offsets['event_arg'] = offsets['base_arg_data'] + self.compute_base_args_size(offsets['base_arg_data'])
        offsets['linked_files'] = offsets['event_arg'] + self.Event.EventArg.STRUCT.size * self.event_arg_count
        offsets['packed_strings'] = offsets['linked_files'] + 8 * len(self.linked_file_offsets)
        offsets['end_of_file'] = offsets['packed_strings'] + len(self.packed_strings)
        return offsets

    def build_emevd_header(self):
        offsets = self.compute_table_offsets()
        header_dict = {
            'file_size_1': offsets['end_of_file'],
            'event_count': self.event_count,
            'event_table_offset': offsets['event'],
            'instruction_count': self.instruction_count,
            'instruction_table_offset': offsets['instruction'],
            'unknown_table_offset': offsets['base_arg_data'],  # Absent.
            'event_layer_table_offset': offsets['base_arg_data'],  # Absent.
            'event_arg_count': self.event_arg_count,
            'event_arg_table_offset': offsets['event_arg'],
            'linked_files_count': len(self.linked_file_offsets),
            'linked_files_table_offset': offsets['linked_files'],
            'base_arg_data_size': self.compute_base_args_size(offsets['base_arg_data']),  # Note different table order.
            'base_arg_data_offset': offsets['base_arg_data'],
            'packed_strings_size': len(self.packed_strings),
            'packed_strings_offset': offsets['packed_strings'],
        }
        return self.HEADER_STRUCT.pack(header_dict)

    def get_linked_file_names(self):
        names = []
        for offset in self.linked_file_offsets:
            names.append(read_chars(self.packed_strings, offset=offset))
        return names

    def unpack_strings(self):
        strings = []
        string_buffer = BytesIO(self.packed_strings)
        while string_buffer.tell() != len(self.packed_strings):
            offset = string_buffer.tell()
            string = read_chars(string_buffer, reset_old_offset=False, encoding=self.STRING_ENCODING)
            strings.append((str(offset), string))  # repr to include double backslash
        return strings

    def to_numeric(self):
        numeric_output = "\n\n".join([event.to_numeric() for event in self.events.values()])
        numeric_output += "\n\nlinked:\n" + "\n".join(str(offset) for offset in self.linked_file_offsets)
        numeric_output += "\n\nstrings:\n" + "\n".join(s[0] + ': ' + s[1] for s in self.unpack_strings())
        return numeric_output

    def to_verbose(self, game_module, with_line_numbers=False):
        return "\n\n".join([event.to_verbose(game_module, with_line_numbers) for event in self.events.values()])

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
        return docstring + '\n' + "\n\n\n".join([imports] + [event.to_evs(self.GAME_MODULE)
                                                             for event in self.events.values()]) + '\n'

    def pack(self, dcx=None):
        if dcx is None:
            # Auto-detect DCX compression from source file (if applicable).
            dcx = self._dcx

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

        emevd_binary = b''
        offsets = self.compute_table_offsets()
        if len(header) != offsets['event']:
            raise ValueError(f"Header was of size {len(header)} but expected size was {self.HEADER_STRUCT.size}.")
        emevd_binary += header
        if len(emevd_binary) + len(event_table_binary) != offsets['instruction']:
            raise ValueError(f"Event table was of size {len(event_table_binary)} but expected size was "
                             f"{offsets['instruction'] - len(emevd_binary)}.")
        emevd_binary += event_table_binary
        if len(emevd_binary) + len(instr_table_binary) != offsets['base_arg_data']:
            raise ValueError(f"Instruction table was of size {len(instr_table_binary)} but expected size was "
                             f"{offsets['base_arg_data'] - len(emevd_binary)}.")
        emevd_binary += instr_table_binary
        # if len(emevd_binary) + len(argument_data_binary) != offsets['event_arg']:
        #     raise ValueError(f"Argument data was of size {len(argument_data_binary)} but expected size was "
        #                      f"{offsets['event_arg'] - len(emevd_binary)}.")
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

    def write_packed(self, emevd_path=None, dcx=None):
        if not emevd_path:
            emevd_path = self.map_name
            if self._dcx:
                if not emevd_path.endswith('.emevd.dcx'):
                    emevd_path += '.emevd.dcx'
            else:
                if not emevd_path.endswith('.emevd'):
                    emevd_path += '.emevd'
        os.makedirs(os.path.dirname(emevd_path), exist_ok=True)
        with open(emevd_path, 'wb') as f:
            f.write(self.pack(dcx))

    def write_numeric(self, numeric_path=None):
        if not numeric_path:
            numeric_path = self.map_name
            if not numeric_path.endswith('.numeric.txt'):
                numeric_path += '.numeric.txt'
        os.makedirs(os.path.dirname(numeric_path), exist_ok=True)
        with open(numeric_path, 'w', encoding='utf-8') as f:
            f.write(self.to_numeric())

    def write_verbose(self, verbose_path=None, with_line_numbers=False):
        if not verbose_path:
            verbose_path = self.map_name
            if not verbose_path.endswith('.verbose.txt'):
                verbose_path += '.verbose.txt'
        os.makedirs(os.path.dirname(verbose_path), exist_ok=True)
        with open(verbose_path, 'w') as f:
            f.write(self.to_verbose(self.GAME_MODULE, with_line_numbers=with_line_numbers))

    def write_evs(self, evs_path=None):
        if not evs_path:
            evs_path = self.map_name
            if not evs_path.endswith('.evs'):
                evs_path += '.evs'
        os.makedirs(os.path.dirname(evs_path), exist_ok=True)
        with open(evs_path, 'w', encoding='utf-8') as f:
            f.write(self.to_evs())


def numeric_string_to_event_dict(numeric_string, game_module):
    """ Parses the text data from the given numeric-style string into an EMEVD() instance, which can then be packed to
    binary or made verbose. Raises a ValueError if the numeric input cannot be parsed for some reason. """

    # TODO: Allow whitespace on blank lines between events.
    text_events = re.split(r'\n{2,}', numeric_string)
    emevd_dict = OrderedDict()
    linked_offsets = []
    strings = b''

    lineno = 0
    for text_event in text_events:

        if text_event.startswith('linked:'):
            for offset in text_event[8:].split('\n'):
                if offset.strip():
                    linked_offsets += [int(offset.strip())]
            continue

        if text_event.startswith('strings:'):
            for offset_with_string in text_event[9:].split('\n'):
                if not offset_with_string:
                    continue
                z_string = offset_with_string.split(':', 1)[-1].strip().encode('utf-16le') + b'\0\0'
                strings += z_string
            continue

        event_lines = text_event.splitlines()
        header_line = event_lines[0]
        m = HEADER_RE.match(header_line)
        if not m:
            print(f'Event: {repr(text_event)}')
            raise ValueError(f"Error parsing header line: '{header_line}'.")
        event_id = int(m.group(1))
        restart_type = int(m.group(2))

        instruction_list = []
        for instruction_or_event_arg in event_lines[1:]:
            lineno += 1
            m_instruction = INSTRUCTION_RE.match(instruction_or_event_arg)
            m_arg_r = EVENT_ARG_REPLACEMENT_RE.match(instruction_or_event_arg)

            if m_instruction:
                # Parse the line as an instruction.
                instruction_class = int(m_instruction.group(1))
                instruction_index = int(m_instruction.group(2))
                args_format = m_instruction.group(3)
                args_list_string = m_instruction.group(4)

                # Check the argument list against the format_string.
                split_arg_list = args_list_string.split(",")
                # Remove required|optional separator and replace 's' with 'I' (string offset).
                raw_args_format = args_format.replace('|', '').replace('s', 'I')
                if split_arg_list == ['']:
                    split_arg_list = []
                if len(raw_args_format) != len(split_arg_list):
                    raise ValueError(f"Number of args ({len(raw_args_format)}) does not match length of the "
                                     f"instruction format string ('{args_format}') (Line {lineno})")

                args_list = []
                for i, element in enumerate(raw_args_format):
                    arg = split_arg_list[i]
                    if element == 'f':
                        args_list.append(float(arg))
                    elif element in ELEMENT_MIN_MAX:
                        min_value, max_value = ELEMENT_MIN_MAX[element]
                        parsed_arg = int(arg)
                        if min_value <= parsed_arg <= max_value:
                            args_list.append(parsed_arg)
                        else:
                            print(instruction_class, instruction_index, args_format, args_list_string)
                            raise ValueError(f"Argument '{arg}' is not inside the permitted range of data type "
                                             f"'{element}' {repr(ELEMENT_MIN_MAX[element])} (Line {lineno})")
                instruction_list.append(game_module.EMEVD.Event.Instruction(
                    instruction_class, instruction_index, args_format, args_list)
                )

            elif m_arg_r:
                if len(instruction_list) >= 1:
                    # Parse the line as an arg replacement for the previous line.
                    write_from_byte = int(m_arg_r.group(1))
                    read_from_byte = int(m_arg_r.group(2))
                    bytes_to_write = int(m_arg_r.group(3))

                    instruction_list[-1].event_args.append(
                        game_module.EMEVD.Event.EventArg(
                            len(instruction_list) - 1, write_from_byte, read_from_byte, bytes_to_write)
                    )
                else:
                    raise ValueError(f"Parameter replacement '{instruction_or_event_arg}' does not follow an "
                                     f"instruction line.")
            else:
                # Malformed line.
                raise ValueError(f"Line '{instruction_or_event_arg}' cannot be parsed as an instruction or "
                                 f"arg replacement.")
        emevd_dict[event_id] = game_module.EMEVD.Event(event_id, restart_type, instruction_list)

    emevd_dict['linked'] = linked_offsets
    emevd_dict['strings'] = strings

    return emevd_dict


def numeric_file_to_emevd_dict(numeric_path, game_module):
    with open(numeric_path, 'r', encoding='utf-8') as f:
        numeric_string = f.read()
    return numeric_string_to_event_dict(numeric_string, game_module)
