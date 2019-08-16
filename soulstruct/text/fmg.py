from io import BytesIO
from textwrap import wrap
from soulstruct.utilities.core import BinaryStruct, read_chars_from_buffer

__all__ = ['FMG']


class FMG(object):

    PRE_HEADER_STRUCT = (  # Always little-endian
        'x',
        ('big_endian', '?'),  # Only DeS is big-endian
        ('version', 'b'),  # 0 for DeS, 1 for DS1/DSR/DS2, 2 for BB/DS3
        'x')

    HEADER_STRUCTS = {
        0: (
            ('file_size', 'i'),
            ('one', 'b', 1),
            ('version_magic', 'b', -1),
            '2x',
            ('range_count', 'i'),
            ('string_count', 'i'),
            ('string_offsets_offset', 'i'),
            ('zero', 'i', 0)),
        1: (
            ('file_size', 'i'),
            ('one', 'b', 1),
            ('version_magic', 'b', 0),
            '2x',
            ('range_count', 'i'),
            ('string_count', 'i'),
            ('string_offsets_offset', 'i'),
            ('zero', 'i', 0)),
        2: (
            ('file_size', 'i'),
            ('one', 'b', 1),
            ('version_magic', 'b', 0),
            '2x',
            ('range_count', 'i'),
            ('string_count', 'i'),
            ('version_3_extra', 'i', 255),
            ('string_offsets_offset', 'q'),
            ('zero', 'q', 0))
    }

    RANGE_STRUCTS = {0: (('first_index', 'i'), ('first_id', 'i'), ('last_id', 'i'))}
    RANGE_STRUCTS[1] = RANGE_STRUCTS[0]
    RANGE_STRUCTS[2] = RANGE_STRUCTS[0] + ('4x',)

    STRING_OFFSET_STRUCTS = {0: (('offset', 'i'),), 1: (('offset', 'i'),), 2: (('offset', 'q'),)}

    LINE_LIMIT = {
        'ds1': 11,
        'ds2': 11,  # TODO
        'bb': 11,  # TODO
        'ds3': 11,  # TODO
    }

    def __init__(self, fmg_source, remove_empty_entries=True, version=None):

        self.pre_header_struct = BinaryStruct(*self.PRE_HEADER_STRUCT)
        self.version = None
        self.big_endian = False

        self.header_struct = None
        self.range_struct = None
        self.string_offset_struct = None

        self.fmg_path = None
        self.entries = {}

        if fmg_source is None:
            return

        if isinstance(fmg_source, dict):
            self.entries = fmg_source
            self._set_version(version)
            return

        if version is not None:
            raise ValueError("You cannot specify 'version' when loading an FMG from file content. The version will\n"
                             "be automatically detected.")

        if isinstance(fmg_source, bytes):
            print("# WARNING: FMG was initialized with raw bytes, which means the FMG version is unknown.\n"
                  "#     You should use a class constructor like `FMG.new_ds1(fmg_dict)` instead of `FMG()`.")
            self.unpack(BytesIO(fmg_source), remove_empty_entries)

        elif isinstance(fmg_source, str):
            if version is not None:
                raise ValueError("You cannot specify 'version' when reading from an FMG file (version will\n"
                                 "be auto-detected).")
            self.fmg_path = fmg_source
            with open(fmg_source, 'rb') as file:
                self.unpack(file, remove_empty_entries)

        elif hasattr(fmg_source, 'data'):
            # Try reading .data attribute (e.g. BNDEntry).
            self.unpack(BytesIO(fmg_source.data), remove_empty_entries)

    def _set_version(self, version):
        if str(version).lower() in {'des', '0'}:
            self.version = v = 0
            self.big_endian = True
        elif str(version).lower() in {'ds1', 'ptd', 'dsr', 'ds2', 'bb', '1'}:
            self.version = v = 1
            self.big_endian = False
        elif str(version).lower() in {'ds3', '2'}:
            self.version = v = 2
            self.big_endian = False
        else:
            raise ValueError(f"Unrecognized FMG version: {version}. Try one in: ('ds1', 'ds2', 'bb', 'ds3').")

        byte_order = '>' if self.big_endian else '<'
        self.header_struct = BinaryStruct(*self.HEADER_STRUCTS[v], byte_order=byte_order)
        self.range_struct = BinaryStruct(*self.RANGE_STRUCTS[v], byte_order=byte_order)
        self.string_offset_struct = BinaryStruct(*self.STRING_OFFSET_STRUCTS[v], byte_order=byte_order)

    def unpack(self, fmg_buffer, remove_empty_entries=True):
        try:
            pre_header = self.pre_header_struct.unpack(fmg_buffer)
        except ValueError:
            raise ValueError("Could not read FMG header. Is the file/data correct?")
        try:
            self._set_version(pre_header.version)
        except ValueError:
            raise ValueError(f"Unrecognized FMG version in file content: {pre_header.version}.")
        header = self.header_struct.unpack(fmg_buffer)

        # Groups of contiguous text string IDs are defined by ranges (first ID, last ID) to save space.
        ranges = self.range_struct.unpack(fmg_buffer, count=header.range_count)
        if fmg_buffer.tell() != header.string_offsets_offset:
            print("# WARNING: Range data did not end at string data offset given in FMG header.")
        string_offsets = self.string_offset_struct.unpack(fmg_buffer, count=header.string_count)

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

    def pack(self, remove_empty_entries=True, pipe_to_newline=True, word_wrap_limit=None, max_lines='ds1'):
        """Pack text dictionary to binary FMG file.

        Args:
            remove_empty_entries: Ignore empty entries ('') when writing. This will remove many entries from the vanilla
                FMG files, and likely make some of them larger (as the ranges used to define them will be more broken
                up), but will make the dictionary much easier to read through. (Default: True)
            pipe_to_newline: Convert pipes ('|') to newlines ('\n'), which allows for nicer strings. Newline characters
                will still be treated normally. (Default: True)
            word_wrap_limit: Specify a horizontal character limit for automatic word wrapping. If None, no wrapping will
                be applied. (Default: None)
            max_lines: Maximum number of lines that should appear in each text entry. An error will be raised if any
                text exceeds this (and no file will be written). This is most useful for item descriptions when auto
                wrapping is used. You can also specify a game key in {'ds1', 'ds2', 'bb', 'ds3'} to use the line limit
                I have set for item descriptions in that game.

        Note that none of these arguments will modify the entries in this FMG instance.
        """
        if self.version not in {0, 1, 2}:
            raise AttributeError("FMG version must be 0, 1, or 2. Set it manually with text.version.")

        # Convert to sorted list (sorted by ID).
        if remove_empty_entries:
            fmg_entries = sorted([(k, v) for k, v in self.entries.items() if v != ''], key=lambda x: x[0])
        else:
            fmg_entries = sorted([(k, v) for k, v in self.entries.items()], key=lambda x: x[0])

        for i in range(len(fmg_entries)):
            # Optional: convert double spaces to double new lines.
            index, string = fmg_entries[i]
            if pipe_to_newline:
                string = string.replace('|', '\n')
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
                    if isinstance(max_lines, str):
                        try:
                            max_lines = self.LINE_LIMIT[max_lines]
                        except KeyError:
                            raise ValueError(f"Line limit for descriptions could not be "
                                             f"determined from key {repr(max_lines)}.")
                    if wrapped_string.count('\n') > max_lines - 1:
                        line_count = wrapped_string.count('\n') + 1
                        print(f"\nWARNING: FMG index {index} has {line_count} lines (max is {max_lines}):")
                        print(wrapped_string)
                    fmg_entries[i] = (index, wrapped_string)

        # Encode all text entries and pack them, and record the offsets (will be globally offset later).
        relative_string_offset = 0
        packed_strings = b''
        string_offset_list = []

        for string_id, string in fmg_entries:
            if string == '':
                string_offset_list.append(-1)  # changed to zero when offsets become absolute
            null_terminated_text = string.encode('utf-16le') + b'\0\0'
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
            range_count=len(ranges),
            string_count=len(fmg_entries),
            string_offsets_offset=string_offsets_offset,
        )

        return packed_header + packed_ranges + packed_string_offsets + packed_strings

    def write_packed(self, fmg_path=None, remove_empty_entries=True, pipe_to_newline=True,
                     word_wrap_limit=None, max_lines='ds1'):
        """Write binary FMG to given path.

        See `pack` for descriptions of the other arguments.
        """
        if fmg_path is None:
            if self.fmg_path:
                fmg_path = self.fmg_path
            else:
                raise ValueError("FMG path could not be determined automatically (must be specified).")
        with open(fmg_path, 'wb') as output:
            output.write(self.pack(remove_empty_entries=remove_empty_entries, pipe_to_newline=pipe_to_newline,
                                   word_wrap_limit=word_wrap_limit, max_lines=max_lines))

    def __getitem__(self, index: int):
        return self.entries[index]

    def __setitem__(self, index: int, text: str):
        self.entries[index] = text

    def update(self, entries):
        if isinstance(entries, dict):
            return self.entries.update(entries)
        elif isinstance(entries, FMG):
            return self.entries.update(entries.entries)
        raise TypeError(f"Can only call `FMG.update()` with a dictionary or another FMG, not {type(entries)}.")

    def find(self, search_string, replace_with=None):
        """Search for the given text in this FMG.

        Args:
            search_string: Text to find. The text can appear anywhere inside an entry to return a result.
            replace_with: String to replace the given text with in any results. (Default: None)
        """
        found_something = False
        for index, text in self.entries.items():
            if search_string in text:
                if not found_something:
                    print(f"\n~~~ FMG: {str(self.fmg_path) if self.fmg_path is not None else '<None>'}")
                    found_something = True
                print(f"\n  [{index}]:\n{text}")
                if replace_with is not None:
                    self.entries[index] = text.replace(search_string, replace_with)
                    print(f"  -> {self.entries[index]}")
        if not found_something:
            print(f"Could not find any occurrences of string {repr(search_string)}.")

    def __iter__(self):
        return iter(self.entries.items())

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.entries == other
        elif isinstance(other, FMG):
            return self.entries == other.entries
        raise TypeError("Can only test FMG equality with a dictionary or other FMG.")

    def __repr__(self):
        s = f"FMG Path: {str(self.fmg_path) if self.fmg_path is not None else '<None>'}"
        for index, text in self.entries.items():
            s += f'\n    {index}: {text}'
        return s
