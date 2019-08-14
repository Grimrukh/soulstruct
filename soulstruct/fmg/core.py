"""
TODO:
    - Create an intelligent FMG unpacker that is aware of the relationship between the resources. So you can do something
    like `add_item(id, name, short_description, long_description)`.
"""
from io import BytesIO
from textwrap import wrap
from soulstruct.core import BinaryStruct, read_chars_from_buffer

__all__ = ['FMG']


class FMG(object):

    HEADER_STRUCT_BASE = (
        'x',
        ('big_endian', '?'),  # Only DeS is big-endian
        ('version', 'b'),  # 0 for DeS, 1 for DS1/DSR/DS2, 2 for BB/DS3
        'x')
    HEADER_STRUCT_ENDIAN = (
        ('file_size', 'i'),
        ('one', 'b', 1),
        ('unknown', 'b'),  # -1 for DeS, 0 otherwise
        '2x',
        ('range_count', 'i'),
        ('string_count', 'i'))
    HEADER_STRUCT_VERSION_0_1_END = (  # DeS, DS1/DSR, DS2, BB
        ('string_offsets_offset', 'i'),
        ('zero', 'i', 0))
    HEADER_STRUCT_VERSION_2_END = (  # DS3
        ('ds3_extra', 'i', 255),
        ('string_offsets_offset', 'q'),
        ('zero', 'q', 0))

    RANGE_STRUCT_BASE = (
        ('first_index', 'i'),
        ('first_id', 'i'),
        ('last_id', 'i'))
    RANGE_STRUCT_VERSION_2_END = ('4x',)

    STRING_OFFSET_VERSION_0_1 = (
        ('offset', 'i'),
    )
    STRING_OFFSET_VERSION_2 = (
        ('offset', 'q'),
    )

    def __init__(self, fmg_source, remove_empty_entries=True):

        self.header_struct = None
        self.range_struct = None
        self.string_offset_struct = None
        self.version = None
        self.unknown = None  # -1 for DeS, 0 otherwise
        self.big_endian = False
        
        self.fmg_path = None
        self.entries = {}

        if isinstance(fmg_source, dict):
            self.entries = fmg_source

        elif isinstance(fmg_source, bytes):
            self.unpack(BytesIO(fmg_source), remove_empty_entries)

        elif isinstance(fmg_source, str):
            self.fmg_path = fmg_source
            with open(fmg_source, 'rb') as file:
                self.unpack(file, remove_empty_entries)

        elif hasattr(fmg_source, 'data'):
            # Try reading .data attribute (e.g. BNDEntry).
            self.unpack(BytesIO(fmg_source.data), remove_empty_entries)

    @classmethod
    def new_ds1(cls, fmg_dict, remove_empty_entries=True):
        fmg = cls(fmg_dict, remove_empty_entries)
        fmg.version = 1
        fmg.unknown = 0
        fmg.big_endian = False
        fmg.header_struct = BinaryStruct(*cls.HEADER_STRUCT_BASE, *cls.HEADER_STRUCT_ENDIAN,
                                         *cls.HEADER_STRUCT_VERSION_0_1_END)
        fmg.range_struct = BinaryStruct(*cls.RANGE_STRUCT_BASE)
        fmg.string_offset_struct = BinaryStruct(*cls.STRING_OFFSET_VERSION_0_1)
        return fmg

    def unpack(self, fmg_buffer, remove_empty_entries=True):

        self.header_struct = BinaryStruct(*self.HEADER_STRUCT_BASE)
        self.range_struct = BinaryStruct(*self.RANGE_STRUCT_BASE)
        header = self.header_struct.unpack(fmg_buffer)
        self.version = header.version
        self.big_endian = header.big_endian
        byte_order = '>' if self.big_endian else '<'
        try:
            header.update(self.header_struct.unpack(fmg_buffer, *self.HEADER_STRUCT_ENDIAN, byte_order=byte_order))
        except ValueError:
            raise TypeError("Could not interpret file as an FMG.")
        if self.version in {0, 1}:
            header.update(self.header_struct.unpack(fmg_buffer, *self.HEADER_STRUCT_VERSION_0_1_END, 
                                                    byte_order=byte_order))
            self.string_offset_struct = BinaryStruct(*self.STRING_OFFSET_VERSION_0_1)
        elif self.version == 2:
            header.update(self.header_struct.unpack(fmg_buffer, *self.HEADER_STRUCT_VERSION_2_END,
                                                    byte_order=byte_order))
            self.range_struct.add_fields(*self.RANGE_STRUCT_VERSION_2_END)
            self.string_offset_struct = BinaryStruct(*self.STRING_OFFSET_VERSION_2)
        else:
            raise ValueError(f"Unsupported FMG file version: {self.version}")
        self.unknown = header.unknown
            
        # Groups of contiguous text string IDs are defined by ranges (first ID, last ID) to save space.
        ranges = self.range_struct.unpack(fmg_buffer, count=header.range_count, byte_order=byte_order)
        if fmg_buffer.tell() != header.string_offsets_offset:
            print("# WARNING: Range data did not end at string data offset given in FMG header.")
        string_offsets = self.string_offset_struct.unpack(fmg_buffer, count=header.string_count, byte_order=byte_order)

        # Text pointer table corresponds to all the IDs (joined together) of the above ranges, in order.
        for string_range in ranges:
            i = string_range.first_index
            for string_id in range(string_range.first_id, string_range.last_id + 1):
                if string_id in self.entries:
                    raise ValueError(f"Malformed FMG: Entry index {string_id} appeared more than once.")
                string_offset = string_offsets[i].offset
                if string_offset == 0:
                    if not remove_empty_entries:
                        # Empty text string. These will trigger in-game error messages, like ?PlaceName?.
                        # Distinct from ' ', which is intentionally blank text data (e.g. the unused area subtitles).
                        self.entries[string_id] = ''
                else:
                    string = read_chars_from_buffer(fmg_buffer, offset=string_offset, encoding='utf-16le')
                    if string or not remove_empty_entries:
                        self.entries[string_id] = string
                i += 1

    def pack(self, remove_empty_fields=True, double_space_to_double_newline=False, word_wrap_limit=None):
        """ Pack FMG to binary file. (DCX should never be used here.) If version was not set by an unpacked FMG,
        it must be set manually (fmg.version) before calling this. """

        if self.version not in {0, 1, 2}:
            raise AttributeError("FMG version must be 0, 1, or 2. Set it manually with fmg.version.")
        if self.unknown not in {-1, 0}:
            raise AttributeError("FMG 'unknown' field must be -1 (DeS only) or 0. Set it manually with fmg.unknown.")

        # Convert to sorted list (sorted by ID).
        if remove_empty_fields:
            fmg_entries = sorted([(k, v) for k, v in self.entries.items() if v != ''], key=lambda x: x[0])
        else:
            fmg_entries = sorted([(k, v) for k, v in self.entries.items()], key=lambda x: x[0])

        for i in range(len(fmg_entries)):
            # Optional: convert double spaces to double new lines.
            index, string = fmg_entries[i]
            if double_space_to_double_newline:
                string = string.replace('  ', '\n\n')
                fmg_entries[i] = (index, string)
            # Optional: insert new lines to wrap automatically.
            if word_wrap_limit is not None:
                lines = string.split('\n\n')
                if lines != [' ']:
                    # Wrap lines, and re-add manual newlines.
                    wrapped_lines = []
                    for line in lines:
                        if '\n' in line:
                            # Don't touch lines with newlines already in them.
                            wrapped_lines.append(line)
                        else:
                            wrapped_lines.append('\n'.join(wrap(line, word_wrap_limit)))
                    wrapped_string = '\n\n'.join(wrapped_lines).rstrip('\n')
                    if wrapped_string.count('\n') > 10:
                        # TODO: Line limits might be different after DS1.
                        line_count = wrapped_string.count('\n') + 1
                        print(f"\nWARNING: FMG index {index} is too long ({line_count} lines):")
                        print(wrapped_string)
                    fmg_entries[i] = (index, wrapped_string)

        # Encode all text entries and pack them, and record the offsets (will be globally offset later).
        relative_string_offset = 0
        packed_strings = b''
        string_offset_list = []

        for string_id, string in fmg_entries:
            if string == '':
                string_offset_list.append(-1)  # changed to zero when offsets become absolute
            null_terminated_text = string.encode('utf-16le') + b'\x00\x00'
            packed_strings += null_terminated_text
            string_offset_list.append(relative_string_offset)
            relative_string_offset += len(null_terminated_text)

        # Next, the ranges. We just make these as efficient as possible, but unlike FROM, we value the lack of clutter
        # from empty entries more highly than defining a handful less ranges.
        ranges = []
        range_start_index = None
        range_start = None
        range_stop = None
        for string_index, (string_id, _) in enumerate(fmg_entries):
            if range_start_index is None:
                range_start_index = string_index
                range_start = range_stop = string_id
            elif string_id == range_stop + 1:
                # Expand current range to include this string.
                range_stop += 1
            else:
                # Terminate last range...
                ranges.append(self.range_struct.pack(
                    first_index=range_start_index, first_id=range_start, last_id=range_stop)
                )
                # ... then start new one at this string.
                range_start_index = string_index
                range_start = range_stop = string_id

        if range_start is not None:
            # Terminate last range.
            ranges.append(self.range_struct.pack(
                first_index=range_start_index, first_id=range_start, last_id=range_stop)
            )

        packed_ranges = b''.join(ranges)

        # Compute table offsets.
        ranges_offset = self.header_struct.size
        string_offsets_offset = ranges_offset + len(packed_ranges)
        packed_strings_offset = string_offsets_offset + self.string_offset_struct.size * len(string_offset_list)
        file_size = packed_strings_offset + len(packed_strings)
        packed_string_offsets = b''
        for string_offset in string_offset_list:
            if string_offset == -1:
                packed_string_offsets += self.string_offset_struct.pack(offset=0)
            else:
                packed_string_offsets += self.string_offset_struct.pack(offset=packed_strings_offset + string_offset)

        packed_header = self.header_struct.pack(
            big_endian=self.big_endian,
            version=self.version,
            file_size=file_size,
            unknown=self.unknown,
            range_count=len(ranges),
            string_count=len(fmg_entries),
            string_offsets_offset=string_offsets_offset,
        )

        return packed_header + packed_ranges + packed_string_offsets + packed_strings

    def write_packed(self, fmg_path=None, **kwargs):
        if fmg_path is None:
            if self.fmg_path:
                fmg_path = self.fmg_path
            else:
                raise ValueError("FMG path could not be determined automatically (must be specified).")
        with open(fmg_path, 'wb') as output:
            output.write(self.pack(**kwargs))

    def __getitem__(self, index: int):
        return self.entries[index]

    def __setitem__(self, index: int, text: str):
        self.entries[index] = text

    def update(self, other_entries: dict):
        return self.entries.update(other_entries)

    def __iter__(self):
        return iter(self.entries.items())

    def __eq__(self, other):
        if isinstance(other, FMG):
            return self.entries == other.entries
        raise TypeError("Can only compare FMG to another FMG.")

    def __repr__(self):
        s = f"FMG Path: {str(self.fmg_path) if self.fmg_path is not None else '<Unknown>'}"
        for index, text in self.entries.items():
            s += f'\n    {index}: {text}'
        return s
