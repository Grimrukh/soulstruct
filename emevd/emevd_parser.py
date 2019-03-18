from collections import OrderedDict
from io import BytesIO
import os
import re
from struct import calcsize, pack, unpack
from emevd.evs_parser import EmevdCompiler
from emevd import verbose


INSTRUCTION_RE = re.compile(r" [ ]*(\d+)\[(\d+)\] \(([iIhHbBf|]*)\)\[([\d, .-]*)\]")
PARAM_RE = re.compile(r" [ ]*\^\((\d+) <- (\d+), (\d+)\)")
HEADER_RE = re.compile(r"^(\d+), ([012])")
ELEMENT_MIN_MAX = {'b': (-128, 127), 'B': (0, 255), 'h': (-32768, 32767), 'H': (0, 65535),
                   'i': (-2147483648, 2147483647), 'I': (0, 4294967295)}


COMMAND_ARG_TYPE_DICT = {
    2000: {0: '@iII', 1: '@iI', 2: '@B', 3: '@B', 4: '@I', 5: '@B'},
    2001: {},
    2002: {1: '@iI', 2: '@iIiBB', 3: '@iIi', 4: '@iIiBBi', 5: '@iIffifi'},
    2003: {1: '@iiBB', 2: '@iB', 3: '@iB', 4: '@i', 5: '@iiiiiii', 6: '@iB',
           7: '@iB', 8: '@iiB', 9: '@i', 10: '@h', 11: '@bihh', 12: '@i',
           13: '@iIB', 14: '@BBi', 15: '@i', 16: '@I', 17: '@IIB', 18: '@iiBBB',
           19: '@hh', 20: '@i', 21: '@B', 22: '@iiB', 23: '@i', 24: '@iii',
           25: '@iiiii', 26: '@iB', 27: '@B', 28: '@i', 29: '@Bb', 30: '@B',
           31: '@iII', 32: '@iI', 33: '@i', 34: '@iiii', 35: '@ii', 36: '@i',
           37: '@', 38: '@', 39: '@', 40: '@', 41: '@iifi'},
    2004: {1: '@iB', 2: '@iB', 3: '@iBii', 4: '@iB', 5: '@iB', 6: '@iiB',
           7: '@i', 8: '@ii', 9: '@iiiiii', 10: '@iB', 11: '@ii', 12: '@iB',
           13: '@ii', 14: '@ii', 15: '@iB', 16: '@i', 17: '@iiB', 18: '@iif',
           19: '@ii', 20: '@i', 21: '@ii', 22: '@ihhiffBB', 23: '@iiiB',
           24: '@iiii', 25: '@iif', 26: '@iBB', 27: '@iBB', 28: '@ii',
           29: '@iB', 30: '@iB', 31: '@iB', 32: '@iiBii', 33: '@ii', 34: '@iBb',
           35: '@iB', 36: '@iii', 37: '@i', 38: '@B', 39: '@iB', 40: '@iBiii',
           41: '@iBii', 42: '@iBiii', 43: '@iB', 44: '@iB', 45: '@ii',
           46: '@B', 47: '@'},
    2005: {1: '@ib', 2: '@i', 3: '@iB', 4: '@iB', 5: '@iii', 6: '@iiB',
           7: '@ii', 8: '@ib', 9: '@iiiiifff', 10: '@iBBB', 11: '@iih',
           12: '@i', 13: '@iB', 14: '@iiiB', 15: '@i'},
    2006: {1: '@iB', 2: '@i', 3: '@iiii', 4: '@iii', 5: '@ii'},
    2007: {1: '@ihhif', 2: '@B', 3: '@iB', 4: '@iB', 5: '@i', 6: '@i', 7: '@i',
           8: '@i', 9: '@i'},
    2008: {1: '@ii', 2: '@iiiiff', 3: '@BBH'},
    2009: {0: '@iii', 1: '@iii', 2: '@iii', 3: '@iiffi', 4: '@i', 5: '@ii', 6: '@B'},
    2010: {1: '@BHiii', 2: '@iii', 3: '@iB'},
    2011: {1: '@iB', 2: '@iB'},
    2012: {1: '@iB'},
    1000: {0: '@Bb', 1: '@BBb', 2: '@BBb', 3: '@B', 4: '@B', 5: '@Bbii',
           6: '@Bbii', 7: '@BBb', 8: '@BBb', 9: '@f'},
    1001: {0: '@f', 1: '@i', 2: '@ff', 3: '@ii'},
    1003: {0: '@BBi', 1: '@BBBi', 2: '@BBBi', 3: '@BBBii', 4: '@BBBii', 5: '@Bb',
           6: '@Bb', 7: '@BBBB', 8: '@BBBB'},
    1005: {0: '@Bi', 1: '@BBi', 2: '@BBi'},
    0: {0: '@bBb', 1: '@bbii'},
    1: {0: '@bf', 1: '@bi', 2: '@bff', 3: '@bii'},
    3: {0: '@bBBi', 1: '@bBBii', 2: '@bBii', 3: '@bBiif', 4: '@bBiB', 5: '@biifhfiBi',
        6: '@bb', 7: '@bBi', 8: '@bBBB', 9: '@bI', 10: '@bBiibi', 11: '@bBBB',
        12: '@biBBI', 13: '@biifhfiBi', 14: '@bi', 15: '@bii', 16: '@bBiB',
        17: '@bBB', 18: '@biifhfiBii', 19: '@biifhfiBii', 20: '@biBBiB',
        21: '@bB', 22: '@bB'},
    4: {0: '@biB', 1: '@bii', 2: '@bibf', 3: '@bib', 4: '@biiB', 5: '@biiB',
        6: '@biiib', 7: '@biB', 8: '@biiB', 9: '@biB', 10: '@bB', 11: '@bB',
        12: '@bB', 13: '@bBI', 14: '@biBi'},
    5: {0: '@bBi', 1: '@bii', 2: '@bi', 3: '@bibi'},
    11: {0: '@bi', 1: '@bi', 2: '@bi'}
}


def get_byte_offset_from_struct(format_string):
    """ Returns a dictionary of {byte_offset: (struct_index, struct_format)}. The byte offsets indicate where the
    associated element in the struct format string begins. Note that endian-type '@' (native byte alignment) is
    critical here, as EMEVD uses byte-aligned packed binary data. """
    endian = format_string[0]
    format_string = format_string[1:]
    byte_offset_array = {}
    for i in range(0, len(format_string)):
        offset = calcsize(endian + format_string[:i + 1]) - calcsize(endian + format_string[i])
        byte_offset_array[offset] = (i, format_string[i])
    return byte_offset_array


class BinaryStruct(OrderedDict):

    def unpack(self, buffer, count=1, offset_start=0):
        if isinstance(buffer, bytes):
            buffer = BytesIO(buffer)
        outputs = {}
        for i in range(count):
            output = {}
            offset = buffer.tell() - offset_start
            for field_name, field_fmt in self.items():
                if isinstance(field_fmt, (list, tuple)):
                    try:
                        field_fmt, asserted_values = field_fmt
                    except ValueError:
                        raise ValueError("Each field format in BinaryStruct must be a single format string or a "
                                         "(format_string, asserted_values) pair.")
                else:
                    asserted_values = None
                unpacked = unpack(field_fmt, buffer.read(calcsize(field_fmt)))
                if len(unpacked) == 1:
                    # Expand tuple automatically for single value.
                    field_output = unpacked[0]
                else:
                    field_output = unpacked
                if asserted_values is not None and field_output != asserted_values:
                    raise ValueError(f"Field '{field_name}' did not contain asserted value(s) {asserted_values}, but "
                                     f"instead contained: {field_output}.")
                output[field_name] = field_output
            outputs[offset] = output
        return outputs

    def pack(self, sequences):
        if not isinstance(sequences, (list, tuple)):
            sequences = (sequences,)
        output = b''
        for sequence in sequences:
            if isinstance(sequence, (list, tuple)):
                # Check number of entries matches number of fields in struct.
                if len(sequence) != len(self.keys()):
                    print(f"{self.__class__.__name__} keys:", self.keys())
                    print('Sequence values ({}):'.format(len(sequence)), sequence)
                    raise ValueError('List/tuple must have correct number of fields.')
                for i, field_fmt in enumerate(self.values()):
                    if isinstance(field_fmt, (list, tuple)):
                        try:
                            field_fmt, asserted_values = field_fmt
                        except ValueError:
                            raise ValueError("Each field format in BinaryStruct must be a single format string or a "
                                             "(format_string, asserted_values) pair.")
                    else:
                        asserted_values = None
                    field = sequence[i]
                    if asserted_values is not None and asserted_values != field:
                        raise ValueError(
                            f"Field with index {i} did not contain asserted value(s) {asserted_values}, but "
                            f"instead contained: {field}.")
                    if not isinstance(field, (tuple, list)):
                        field = (field,)
                    # print(pack(field_fmt, *field))
                    output += pack(field_fmt, *field)
            elif isinstance(sequence, dict):
                # Check keys match (exluding asserted fields).
                if set([k for k, v in self.items() if isinstance(v, str)]) != set(sequence.keys()):
                    print(f"{self.__class__.__name__} keys:", set([k for k, v in self.items() if isinstance(v, str)]))
                    print('Dictionary keys:', sequence.keys())
                    raise ValueError(f"Dictionary keys must match non-asserted fields in {self.__class__.__name__}.")
                for field_name, field_fmt in self.items():
                    if isinstance(field_fmt, (list, tuple)):
                        try:
                            field_fmt, asserted_values = field_fmt
                        except ValueError:
                            raise ValueError("Each field format in BinaryStruct must be a single format string or a "
                                             "(format_string, asserted_values) pair.")
                        else:
                            field = asserted_values
                    else:
                        field = sequence[field_name]

                    if not isinstance(field, (tuple, list)):
                        field = (field,)
                    # print(pack(field_fmt, *field))
                    output += pack(field_fmt, *field)
        return output

    @property
    def size(self):
        formats = []
        for v in self.values():
            if isinstance(v, (list, tuple)):
                formats.append(v[0])
            else:
                formats.append(v)
        return calcsize(''.join(fmt for fmt in formats))


def get_instruction_args(file, instruction_class, instruction_index, first_arg_offset, event_args_size):
    previous_offset = file.tell()
    if event_args_size == 0:
        return "", []
    args_format = COMMAND_ARG_TYPE_DICT[instruction_class][instruction_index]
    required_args_size = calcsize(args_format)
    if required_args_size > event_args_size:
        raise ValueError(f"Documented size of minimum required args for instruction {instruction_class}"
                         f"[{instruction_index}] is {required_args_size}, but size of args specified in EMEVD file is "
                         f"only {event_args_size}.")
    file.seek(first_arg_offset)
    required_args = unpack(args_format, file.read(required_args_size))

    # Additional arguments may appear for the instruction 2000[00], 'RunEvent'. These instructions are tightly packed,
    # and are simply read here as unsigned integers; we need to actually parse the event to interpret them properly.

    extra_size = event_args_size - required_args_size
    if extra_size == 0:
        file.seek(previous_offset)
        return args_format[1:], list(required_args)
    elif instruction_class != 2000 or instruction_index != 0:
        # TODO: Might be cruel to raise this error when trying to unpack the binary file. Should be a warning here, and
        #  an error on repack.
        raise ValueError(f"Optional arguments are only permitted for instruction 2000[00], not instruction "
                         f"{instruction_class}[{instruction_index}].")
    elif extra_size % 4 != 0:
        # TODO: See above.
        raise ValueError(f"Optional argument size must be a multiple of four bytes.")

    varargs = [unpack('<I', file.read(4)) for _ in range(extra_size // 4)]
    file.seek(previous_offset)
    return args_format[1:] + "|" + "I" * (extra_size // 4), list(required_args) + varargs


class Event(object):

    STRUCT = BinaryStruct(
        event_id='I',
        instruction_count='I',
        first_instruction_offset='I',
        arg_replacement_count='I',
        first_arg_replacement_offset='i',  # why is this signed?
        restart_type='I',
        pad=('I', 0),
    )

    def __init__(self, event_id=0, restart_type=0, instruction_list=None):
        self.event_id = event_id
        self.restart_type = restart_type
        self.instruction_list = instruction_list if instruction_list else []

    @classmethod
    def unpack(cls, file, instruction_table_offset, base_arg_data_offset, arg_replacement_table_offset, count=1):

        events = []
        struct_dicts = cls.STRUCT.unpack(file, count=count)

        for d in struct_dicts.values():
            file.seek(instruction_table_offset + d['first_instruction_offset'])
            instruction_list = Instruction.unpack(file, base_arg_data_offset, count=d['instruction_count'])

            file.seek(arg_replacement_table_offset + d['first_arg_replacement_offset'])
            arg_replacements = ArgReplacement.unpack(file, count=d['arg_replacement_count'])

            for arg_r in arg_replacements:
                # Attach arg replacements to their instruction line.
                instruction_list[arg_r.line].arg_replacements.append(arg_r)

            events.append(cls(d['event_id'], d['restart_type'], instruction_list))

        return events

    @property
    def instruction_count(self):
        return len(self.instruction_list)

    @property
    def total_args_size(self):
        return sum([i.args_size for i in self.instruction_list])

    @property
    def arg_replacement_count(self):
        return sum([i.arg_replacement_count for i in self.instruction_list])

    def to_numeric(self):
        event_string = f"{self.event_id}, {self.restart_type}"
        for instruction in self.instruction_list:
            event_string += "\n " + "\n ".join(instruction.to_numeric())
        return event_string

    def build_parameter_types(self):
        """Applies any parameter replacement instructions to their
        instructions and attempts to build a string representing the types
        of all the parameters used. Since parameters are packed as binary
        data, some parameters may overlap or have different apparent types,
        although this never occurs in the normal files.
        """

        event_arg_set = set()
        event_arg_types = {}
        for instruction in self.instruction_list:
            instruction_arg_set, instruction_arg_types = instruction.apply_arg_replacements()
            event_arg_set = event_arg_set.union(instruction_arg_set)
            for x in instruction_arg_types:
                if x not in event_arg_types:
                    event_arg_types[x] = set(instruction_arg_types[x])
                else:
                    event_arg_types[x] = event_arg_types[x].union(instruction_arg_types[x])
        sorted_parameter_list = list(sorted(event_arg_set))
        event_args_list = [f'X{i}:{j}' for i, j in sorted_parameter_list]
        event_args_format = ''.join(['|'.join(''.join((event_arg_types[f'X{i}:{j}']))
                                              for i, j in sorted_parameter_list)])
        return f"Event Arguments: {{{', '.join([s for s in event_args_list])}}} ({event_args_format})"

    def to_verbose(self, suppress_line_numbers=False):
        verbose_event_string = (f"Event ID: {self.event_id}\nRestarts: "
                                f"{verbose.ENUM_RESTART_TYPE.get(self.restart_type, self.restart_type)}")
        verbose_event_string += "\n" + self.build_parameter_types()
        for i, instr in enumerate(self.instruction_list):
            verbose_event_string += "\n    "
            if not suppress_line_numbers:
                verbose_event_string += "%3d" % i + ' '
            verbose_event_string += instr.to_verbose()
        return verbose_event_string

    def to_binary(self, instruction_offset, first_base_arg_offset, first_arg_replacement_offset):
        if self.arg_replacement_count == 0:
            first_arg_replacement_offset = -1

        event_binary = self.STRUCT.pack(
            {
                'event_id': self.event_id,
                'instruction_count': self.instruction_count,
                'first_instruction_offset': instruction_offset,
                'arg_replacement_count': self.arg_replacement_count,
                'first_arg_replacement_offset': first_arg_replacement_offset,
                'restart_type': self.restart_type,
            }
        )

        base_arg_offset = first_base_arg_offset

        instructions_binary = b''
        args_binary = b''
        arg_replacements_list = []
        for instruction in self.instruction_list:
            instructions_binary += instruction.to_binary(base_arg_offset)

            arg_binary = instruction.args_list_to_binary()
            args_binary += arg_binary
            base_arg_offset += len(arg_binary)

            arg_replacements_list += instruction.arg_replacements

        # Collect and sort arg replacements to better match actual EMEVD files. (Should be purely cosmetic.)
        sorted_arg_replacements = sorted(arg_replacements_list, key=lambda arg_r: (arg_r.read_from_byte, arg_r.line))
        arg_replacements_binary = b''.join([arg_r.to_binary() for arg_r in sorted_arg_replacements])

        return event_binary, instructions_binary, args_binary, arg_replacements_binary


class Instruction(object):

    STRUCT = BinaryStruct(
        instruction_class='I',
        instruction_index='I',
        base_args_size='I',
        first_base_arg_offset='I',
        pad=('iI', (-1, 0)),
    )

    def __init__(self, instruction_class, instruction_index, args_format='', args_list=None):
        if len(args_format.replace('|', '')) != len(args_list):
            raise ValueError(f"Length of argument list ({len(args_list)}) in Instruction {instruction_class}"
                             f"[{instruction_index}] does not match length of format string '{args_format}'.")
        self.instruction_class = instruction_class
        self.instruction_index = instruction_index
        self.args_format = args_format
        self.args_list = args_list if args_list else []
        self.arg_replacements = []  # Added after construction.
        self.verbose_args_list = []  # So we don't modify 'args_list'.

    @classmethod
    def unpack(cls, file, base_arg_data_offset, count=1):
        """ Unpack some number of Instructions into a list, starting from the current file offset. """

        instructions = []
        struct_dicts = cls.STRUCT.unpack(file, count=count)
        for d in struct_dicts.values():
            args_format, args_list = get_instruction_args(
                file, d['instruction_class'], d['instruction_index'],
                base_arg_data_offset + d['first_base_arg_offset'], d['base_args_size'])
            instructions.append(cls(d['instruction_class'], d['instruction_index'], args_format, args_list))

        return instructions

    @property
    def args_size(self):
        return calcsize("@" + self.args_format.replace('|', ''))

    @property
    def arg_replacement_count(self):
        return len(self.arg_replacements)

    def to_numeric(self):
        numeric = [f"{self.instruction_class:04d}[{self.instruction_index:02d}] "
                   f"({self.args_format})" + repr(self.args_list)]
        for replacement in self.arg_replacements:
            numeric.append("   ^" + replacement.to_numeric())
        return numeric

    def to_verbose(self):
        split_point = self.args_format.find('|')
        if split_point == -1:
            required_args = self.verbose_args_list
            optional_args = []
        else:
            required_args = self.verbose_args_list[:split_point]
            optional_args = self.verbose_args_list[split_point:]
        return verbose.verbose_instruction(self.instruction_class, self.instruction_index, required_args, optional_args)

    def apply_arg_replacements(self):
        """ Inserts arg replacements into the appropriate places in their instructions for readability (verbose
        output only). The arg replacements are represented as 'Xi:j', where i and j specify the byte range read from
        the arguments passed to the RunEvent instruction.

        Also returns a dictionary that allows the RunEvent instruction to guess the format of its arguments, based on
        how they are actually used in the event instructions.
        """

        PERMITTED = [0, 0.0, -1, 1]
        arg_offset_dict = get_byte_offset_from_struct("@" + self.args_format.replace('|', ''))

        instruction_arg_set = set()
        instruction_arg_types = {}

        self.verbose_args_list = self.args_list.copy()

        for arg_r in self.arg_replacements:
            try:
                argument_index, argument_byte_type = arg_offset_dict[arg_r.write_from_byte]
            except KeyError:
                raise ValueError(f"No argument in '{self.arg_replacements}' begins at byte {arg_r.write_from_byte}. "
                                 f"Your replacement commands are misaligned.")

            if calcsize(argument_byte_type) < arg_r.bytes_to_write:
                raise ValueError(f"You cannot write {arg_r.bytes_to_write} bytes over an argument of type "
                                 f"{argument_byte_type} (it's too small).")
            value_to_overwrite = self.args_list[argument_index]
            arg_name = f"X{arg_r.read_from_byte}:{arg_r.read_from_byte + arg_r.bytes_to_write - 1}"

            if value_to_overwrite not in PERMITTED and value_to_overwrite != arg_name:
                raise ValueError(f"Parameter is overwriting non-zero value {value_to_overwrite}.")

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
            return pack(format_string, *self.args_list)
        else:
            return b''

    def arg_replacements_to_binary(self):
        return b''.join([arg_replacement.to_binary() for arg_replacement in self.arg_replacements])

    def to_binary(self, first_base_arg_offset):
        struct_dict = {
            'instruction_class': self.instruction_class,
            'instruction_index': self.instruction_index,
            'base_args_size': self.args_size,
            'first_base_arg_offset': first_base_arg_offset,
        }
        return self.STRUCT.pack(struct_dict)


class ArgReplacement(object):
    """ Overrides argument data in a particular instruction using from dynamic args attached to the event. (Each
    instance of this should be attached to a specific Instruction instance.) """

    STRUCT = BinaryStruct(
        instruction_line='I',
        write_from_byte='I',
        read_from_byte='I',
        bytes_to_write='I',
        pad=('I', 0),
    )

    def __init__(self, instruction_line, write_from_byte=0, read_from_byte=0, bytes_to_write=0, zero=0):
        self.line = instruction_line
        self.write_from_byte = write_from_byte
        self.read_from_byte = read_from_byte
        self.bytes_to_write = bytes_to_write
        if zero != 0:
            raise ValueError("Last field of arg replacement must be zero.")

    @classmethod
    def unpack(cls, file, count=1):

        arg_replacements = []
        struct_dicts = cls.STRUCT.unpack(file, count=count)

        for d in struct_dicts.values():
            d.pop('pad')
            arg_replacements.append(cls(**d))

        return arg_replacements

    def to_numeric(self):
        return f"({self.write_from_byte} <- {self.read_from_byte}, {self.bytes_to_write})"

    def to_binary(self):
        return pack("@IIII4x", self.line, self.write_from_byte, self.read_from_byte, self.bytes_to_write)


class Emevd(object):

    HEADER_STRUCT = BinaryStruct(
        version=('4s', b'EVD\x00'),
        pad_1=('I', 0),
        unknown=('I', 204),

        file_size_1='I',
        event_count='I',
        event_table_offset='I',
        instruction_count='I',
        instruction_table_offset='I',
        
        pad_2=('I', 0),
        args_offset_1='I',
        pad_3=('I', 0),
        args_offset_2='I',
        
        arg_replacement_count='I',
        arg_replacement_table_offset='I',
        
        pad_4=('I', 0),
        file_size_2='I',
        
        base_arg_data_size='I',
        base_arg_data_offset='I',
        
        pad_5=('I', 0),
        file_size_3='I',
        pad_6=('I', 0),
    )

    def __init__(self, emevd_source):

        if isinstance(emevd_source, EmevdCompiler):
            self.map_name = emevd_source.map_name
            self.events = numeric_string_to_event_list(emevd_source.numeric_emevd)

        elif isinstance(emevd_source, (list, tuple)):
            self.map_name = None
            self.events = emevd_source

        elif isinstance(emevd_source, str):
            self.map_name = os.path.basename(emevd_source.split('.')[0])

            if emevd_source.endswith('.py') or emevd_source.endswith('.evs'):
                emevd_source = EmevdCompiler(emevd_source)
                self.map_name = emevd_source.map_name
                self.events = numeric_string_to_event_list(emevd_source.numeric_emevd)
            elif emevd_source.endswith('.txt'):
                try:
                    self.events = numeric_file_to_event_list(emevd_source)
                except Exception:
                    raise IOError(f"Could not interpret file '{emevd_source}' as numeric-style EMEVD.\n"
                                  f"(Note that you cannot use verbose-style text files as EMEVD input.)\n"
                                  f"If your file is an EVS script, change the extension to '.py'' or '.evs'.")

            elif emevd_source.endswith('.emevd'):
                try:
                    with open(emevd_source, 'rb') as file:
                        self.header = self.HEADER_STRUCT.unpack(file)[0]

                        file.seek(self.header['event_table_offset'])
                        self.events = Event.unpack(
                            file, self.header['instruction_table_offset'], self.header['base_arg_data_offset'],
                            self.header['arg_replacement_table_offset'], count=self.header['event_count'])
                except Exception:
                    raise IOError(f"Could not interpret file '{emevd_source}' as binary EMEVD data.\n"
                                  f"You should only use the '.emevd' extension for actual game-ready\n"
                                  f"EMEVD, which you can create with the `pack()` method of this class.")

    @classmethod
    def build_from_emevd_file_path(cls, emevd_path):
        return cls(emevd_path)

    @classmethod
    def build_from_numeric_file_path(cls, numeric_path):
        return cls(numeric_file_to_event_list(numeric_path))

    @property
    def event_count(self):
        return len(self.events)

    @property
    def instruction_count(self):
        return sum([i.instruction_count for i in self.events])

    @property
    def args_size(self):
        # There is a z4 after the packed argument data, but it is included in the argument byte size given in the
        # header, so we add it here as well.
        return sum([i.total_args_size for i in self.events]) + 4

    @property
    def arg_replacement_count(self):
        return sum([i.arg_replacement_count for i in self.events])

    def compute_event_table_offset(self):
        return self.HEADER_STRUCT.size

    def compute_instruction_table_offset(self):
        return self.compute_event_table_offset() + Event.STRUCT.size * self.event_count

    def compute_base_arg_data_offset(self):
        return self.compute_instruction_table_offset() + Instruction.STRUCT.size * self.instruction_count

    def compute_arg_replacement_table_offset(self):
        return self.compute_base_arg_data_offset() + self.args_size

    def compute_file_size(self):
        return self.compute_arg_replacement_table_offset() + ArgReplacement.STRUCT.size * self.arg_replacement_count

    def build_emevd_header(self):
        file_size = self.compute_file_size()
        args_offset = self.compute_base_arg_data_offset()
        header_dict = {
            'file_size_1': file_size,
            'event_count': self.event_count,
            'event_table_offset': self.compute_event_table_offset(),
            'instruction_count': self.instruction_count,
            'instruction_table_offset': self.compute_instruction_table_offset(),
            'args_offset_1': args_offset,
            'args_offset_2': args_offset,
            'arg_replacement_count': self.arg_replacement_count,
            'arg_replacement_table_offset': self.compute_arg_replacement_table_offset(),
            'file_size_2': file_size,
            'base_arg_data_size': self.args_size,
            'base_arg_data_offset': self.compute_base_arg_data_offset(),
            'file_size_3': file_size,
        }
        return self.HEADER_STRUCT.pack(header_dict)

    def to_numeric(self):
        return "\n\n".join([event.to_numeric() for event in self.events])

    def to_verbose(self, suppress_line_numbers=False):
        return "\n\n".join([event.to_verbose(suppress_line_numbers) for event in self.events])

    def pack(self):
        event_table_binary = b''
        instr_table_binary = b''
        argument_data_binary = b''
        arg_r_binary = b''

        current_instruction_offset = 0
        current_arg_data_offset = 0
        current_arg_replacement_offset = 0

        header = self.build_emevd_header()

        for e in self.events:
            e_bin, i_bin, a_bin, p_bin = e.to_binary(
                current_instruction_offset, current_arg_data_offset, current_arg_replacement_offset)

            event_table_binary += e_bin
            instr_table_binary += i_bin
            argument_data_binary += a_bin
            arg_r_binary += p_bin

            if len(i_bin) != Instruction.STRUCT.size * e.instruction_count:
                raise ValueError(f"Event ID: {e.event_id} returned packed instruction binary of size {len(i_bin)} but "
                                 f"reports {e.instruction_count} total instructions (with expected size "
                                 f"{Instruction.STRUCT.size * e.instruction_count}).")
            if len(p_bin) != ArgReplacement.STRUCT.size * e.arg_replacement_count:
                raise ValueError(f"Event ID: {e.event_id} returned packed arg replacement binary of size {len(p_bin)} "
                                 f"but reports {e.arg_replacement_count} total replacements (with expected size "
                                 f"{ArgReplacement.STRUCT.size * e.arg_replacement_count}).")
            if len(a_bin) != e.total_args_size:
                raise ValueError(f"Event ID: {e.event_id} returned packed argument data binary of size {len(a_bin)} "
                                 f"but reports expected size to be {e.total_args_size}).")

            current_instruction_offset += len(i_bin)
            current_arg_data_offset += len(a_bin)
            current_arg_replacement_offset += len(p_bin)

        argument_data_binary += b'\x00\x00\x00\x00'  # Termination z4 for the packed ArgumentData

        emevd_binary = b''
        if len(header) != self.compute_event_table_offset():
            raise ValueError(
                f"Header was of size {len(header)} but expected size was {self.HEADER_STRUCT.size}.")
        emevd_binary += header
        if len(emevd_binary) + len(event_table_binary) != self.compute_instruction_table_offset():
            raise ValueError(f"Event table was of size {len(event_table_binary)} but expected size was "
                             f"{self.compute_instruction_table_offset() - len(emevd_binary)}.")
        emevd_binary += event_table_binary
        if len(emevd_binary) + len(instr_table_binary) != self.compute_base_arg_data_offset():
            raise ValueError(f"Instruction table was of size {len(instr_table_binary)} but expected size was "
                             f"{self.compute_base_arg_data_offset() - len(emevd_binary)}.")
        emevd_binary += instr_table_binary
        if len(emevd_binary) + len(argument_data_binary) != self.compute_arg_replacement_table_offset():
            raise ValueError(f"Argument data was of size {len(argument_data_binary)} but expected size was "
                             f"{self.compute_arg_replacement_table_offset() - len(emevd_binary)}.")
        emevd_binary += argument_data_binary
        if len(emevd_binary) + len(arg_r_binary) != self.compute_file_size():
            raise ValueError(f"Parameter replacement table was of size {len(arg_r_binary)} but expected size was "
                             f"{self.compute_file_size() - len(emevd_binary)}.")
        emevd_binary += arg_r_binary

        return emevd_binary

    def write_packed(self, emevd_path=None):
        if not emevd_path:
            emevd_path = self.map_name
            if not emevd_path.endswith('.emevd'):
                emevd_path += '.emevd'
        with open(emevd_path, 'wb') as f:
            f.write(self.pack())

    def write_numeric(self, numeric_path=None):
        if not numeric_path:
            numeric_path = self.map_name
            if not numeric_path.endswith('.numeric.txt'):
                numeric_path += '.numeric.txt'
        with open(numeric_path, 'w') as f:
            f.write(self.to_numeric())

    def write_verbose(self, verbose_path=None, suppress_line_numbers=False):
        if not verbose_path:
            verbose_path = self.map_name
            if not verbose_path.endswith('.verbose.txt'):
                verbose_path += '.verbose.txt'
        with open(verbose_path, 'w') as f:
            f.write(self.to_verbose(suppress_line_numbers=suppress_line_numbers))


def numeric_string_to_event_list(numeric_string):
    """ Parses the text data from the given numeric-style string into an Emevd() instance, which can then be packed to
    binary or made verbose. Raises a ValueError if the numeric input cannot be parsed for some reason. """

    # TODO: Allow whitespace on blank lines between events.
    text_events = re.split(r'\n{2,}', numeric_string)
    event_list = []

    for text_event in text_events:
        event_lines = text_event.splitlines()
        header_line = event_lines[0]
        m = HEADER_RE.match(header_line)
        if not m:
            raise ValueError(f"Error parsing header line: '{header_line}'.")
        event_id = int(m.group(1))
        restart_type = int(m.group(2))

        instruction_list = []
        for instruction_or_arg_replacement in event_lines[1:]:
            m_instruction = INSTRUCTION_RE.match(instruction_or_arg_replacement)
            m_arg_r = PARAM_RE.match(instruction_or_arg_replacement)

            if m_instruction:
                # Parse the line as an instruction.
                instruction_class = int(m_instruction.group(1))
                instruction_index = int(m_instruction.group(2))
                args_format = m_instruction.group(3)
                args_list_string = m_instruction.group(4)

                # Check the argument list against the format_string.
                split_arg_list = args_list_string.split(",")
                raw_args_format = args_format.replace('|', '')  # Remove required|optional separator.
                if split_arg_list == ['']:
                    split_arg_list = []
                if len(raw_args_format) != len(split_arg_list):
                    raise ValueError(f"Number of args ({len(raw_args_format)}) does not match length of the "
                                     f"instruction format string ('{args_format}')")

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
                            raise ValueError(f"Argument '{arg}' is not inside the permitted range of data type "
                                             f"'{element}' {repr(ELEMENT_MIN_MAX[element])}")
                instruction_list.append(Instruction(instruction_class, instruction_index, args_format, args_list))

            elif m_arg_r:
                if len(instruction_list) >= 1:
                    # Parse the line as an arg replacement for the previous line.
                    write_from_byte = int(m_arg_r.group(1))
                    read_from_byte = int(m_arg_r.group(2))
                    bytes_to_write = int(m_arg_r.group(3))

                    instruction_list[-1].arg_replacements.append(
                        ArgReplacement(len(instruction_list) - 1, write_from_byte, read_from_byte, bytes_to_write)
                    )
                else:
                    raise ValueError(f"Parameter replacement '{instruction_or_arg_replacement}' does not follow an "
                                     f"instruction line.")
            else:
                # Malformed line.
                raise ValueError(f"Line '{instruction_or_arg_replacement}' cannot be parsed as an instruction or "
                                 f"arg replacement.")
        event_list.append(Event(event_id, restart_type, instruction_list))

    return event_list


def numeric_file_to_event_list(numeric_path):
    with open(numeric_path, 'r') as f:
        numeric_string = f.read()

    return numeric_string_to_event_list(numeric_string)
