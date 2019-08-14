from io import BytesIO
import os
import re
import struct
try:
    from .config import LIVE_GAME_PATH, TEMP_GAME_PATH, DEFAULT_GAME_PATH
except ImportError:
    print("# No Soulstruct configuration file detected ('config.py'). Creating now...\n")
    if not os.path.isfile(os.path.join(os.path.dirname(__file__), 'config.py')):
        try:
            temp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'workspace'))
            with open(os.path.join(os.path.dirname(__file__), 'config.py'), 'w') as f:
                f.write("LIVE_GAME_PATH = 'C:\\Program Files\\Steam\\steamapps\\common\\DARK SOULS REMASTERED\\'\n")
                f.write(f"TEMP_GAME_PATH = {repr(temp_dir)}\n")
                f.write(f"DEFAULT_GAME_PATH = {repr(temp_dir)}\n")
            print("# Configuration file created successfully.\n"
                  "# Edit this file to set the directories of your game and temporary workspace,\n"
                  "# which will be used throughout Soulstruct, as well as the default directory\n"
                  "# to use when any structures or GUIs are loaded without specifying a directory.")
        except PermissionError:
            print("# ERROR: Could not import 'config.py' Soulstruct configuration file.\n"
                  "# Using default directory values, which may not work.")
        LIVE_GAME_PATH = 'C:/Program Files/Steam/steamapps/common/DARK SOULS REMASTERED/'
        TEMP_GAME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'workspace'))
        DEFAULT_GAME_PATH = TEMP_GAME_PATH

__all__ = ['LIVE_GAME', 'TEMP_GAME', 'DEFAULT_GAME', 'DEFAULT_GAME_DCX', 'PACKAGE_PATH',
           'BinaryStruct', 'read_chars_from_bytes', 'read_chars_from_buffer']


def LIVE_GAME(relative_path):
    return os.path.join(LIVE_GAME_PATH, relative_path)


def TEMP_GAME(relative_path):
    return os.path.join(TEMP_GAME_PATH, relative_path)


def DEFAULT_GAME(relative_path):
    return os.path.join(DEFAULT_GAME_PATH, relative_path)


def DEFAULT_GAME_DCX(relative_path):
    """Looks for the '.dcx' version first, then the non-DCX version as a backup.

    Returns a tuple of (absolute_path, is_dcx).
    """
    abs_path = os.path.join(DEFAULT_GAME_PATH, relative_path)
    if abs_path.endswith('.dcx'):
        no_dcx = abs_path[:-4]
        dcx = abs_path
    else:
        no_dcx = abs_path
        dcx = abs_path + '.dcx'
    if os.path.isfile(dcx):
        return dcx, True
    if os.path.isfile(no_dcx):
        return no_dcx, True
    raise FileNotFoundError(f"Could not find DCX or non-DCX version of {abs_path}.")


def PACKAGE_PATH(relative_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))


class BinaryStruct(object):

    BYTE_ORDER_RE = re.compile(r'[<>@].*')
    PAD_RE = re.compile(r'([0-9]*)?x')
    JIS_FORMAT_RE = re.compile(r'([0-9]*)?j')
    CHARS_FORMAT_RE = re.compile(r'([0-9]*)?s')
    OTHER_FORMAT_RE = re.compile(r'([0-9]*)?(?!s)')

    def __init__(self, *fields, byte_order='<'):
        """
        We need to remember a field format string, a list of field names, a dictionary that maps field
        indices to asserted values, and a list of indices that need to be decoded to JIS.
        """
        self.fields = []  # field dictionaries
        self._struct_format = []  # Format chunks with different byte order are stored in sub-format strings.
        self._struct_length = []  # Number of values to be packed using each sub-format string.
        self.size = 0
        self.add_fields(*fields, byte_order=byte_order)

    def add_fields(self, *fields, byte_order=None):
        """ Add new fields to the BinaryStruct. By default, the most recent byte order is used.

        Returns a list of the new fields added and their combined struct format.
        """
        if not fields:
            return
        if byte_order is None:
            if self._struct_format:
                byte_order = self._struct_format[-1][0]
                new_fmt = False
            else:
                byte_order = '<'  # default
                new_fmt = True
        elif not self._struct_format or byte_order != self._struct_format[-1][0]:
            if byte_order not in {'<', '>', '@'}:
                raise ValueError("byte_order must be '<', '>', or '@'.")
            new_fmt = True
        else:
            # Append to most recent sub-format (same byte order).
            new_fmt = False

        sub_fmt = ''
        sub_fmt_length = 0
        new_fields = []

        for field in fields:
            if isinstance(field, str):
                # Pad string.
                if self.PAD_RE.match(field):
                    new_fields.append({'fmt': field, 'length': 0})
                    sub_fmt += field
                    continue
                else:
                    raise ValueError("Only pad strings are permitted outside field tuples.")

            d = {}

            if isinstance(field, (list, tuple)):
                name = field[0]
                fmt = field[1]
                try:
                    asserted = field[2]
                    if isinstance(asserted, tuple):
                        asserted = list(asserted)
                    d['asserted'] = asserted
                except IndexError:
                    pass
            else:
                raise TypeError("Each field should be a single pad '#x' format string, a (name, format) "
                                "pair, or a (name, format, asserted) triplet.")

            if self.BYTE_ORDER_RE.match(fmt):
                raise ValueError("Individual field format should not have its own byte order. Pass as a keyword arg.")
            if self.JIS_FORMAT_RE.match(fmt):
                jis_size = int(fmt[:-1]) if fmt[:-1] else 1
                fmt = str(jis_size) + 's'
                d['jis_size'] = jis_size
                length = 1  # This is not the struct byte size, but rather the number of values that will be unpacked.
            elif self.CHARS_FORMAT_RE.match(fmt):
                length = 1
            else:
                try:
                    length = self.OTHER_FORMAT_RE.match(fmt).group(1)
                    length = int(length) if length else 1
                except AttributeError:
                    raise ValueError(f"Invalid field format: '{fmt}'.")
            d.update(name=name, fmt=fmt, length=length)
            new_fields.append(d)
            sub_fmt += fmt
            sub_fmt_length += length

        self.fields += new_fields
        if new_fmt:
            self._struct_format.append(byte_order + sub_fmt)
            self._struct_length.append(sub_fmt_length)
        else:
            self._struct_format[-1] += sub_fmt
            self._struct_length[-1] += sub_fmt_length
        self.size = sum(struct.calcsize(sub_fmt) for sub_fmt in self._struct_format)

        return new_fields, byte_order + sub_fmt

    @staticmethod
    def _unpack_field(unpacked_values, field, index):
        if field['length'] == 0:
            # Ignore.
            return
        value = unpacked_values[index:index + field['length']]
        if field['length'] == 1:
            # Unzip single values.
            value = value[0]
        else:
            # Convert tuples to lists.
            value = list(value)
        if 'jis_size' in field:
            value = read_chars_from_bytes(value, length=len(value), encoding='shift_jis_2004')
            value = value.rstrip('\0')
        if 'asserted' in field:
            if value != field['asserted']:
                raise ValueError(
                    f"Field '{field['name']}' contained {value} instead of asserted value {field['asserted']}.")
        return value

    def unpack(self, source, *fields, byte_order=None, count=None):
        """ Unpack one or more structs from source data.

        If any 'fields' are specified (same allowed formats as the constructor above), only those fields will be
        unpacked, and they will then be added to the BinaryStruct. This allows you to dynamically build the BinaryStruct
        on the fly if the structure itself depends on the values read (e.g. a big-endian flag). The same BinaryStruct
        can then be used for repacking later.

        Args:
            source: bytes or open buffer to unpack from.
            fields: list of new fields to simultaneously add and unpack.
            byte_order: byte order of the new fields.
            count: number of contiguous structs to unpack from source. If None (default), a single struct is returned.
                   Otherwise, the contiguous structs (even if count == 1) are returned in a list. Cannot be used if
                   'fields' is used.

        Returns:
            AttributeDict (or List[AttributeDict] if 'count' is not None) with unpacked fields.
        """
        outputs = []

        if fields:
            # Unpack just the given fields after adding them to the BinaryStruct.
            if count is not None:
                raise ValueError("Cannot use 'count' when dynamically adding/unpacking new fields.")
            struct_fields, struct_fmt = self.add_fields(*fields, byte_order=byte_order)
            size = struct.calcsize(struct_fmt)
            data = source if isinstance(source, bytes) else source.read(size)  # type: bytes
            try:
                unpacked = struct.unpack(struct_fmt, data)
            except struct.error:
                print(f'Data:', data)
                raise
            output = AttributeDict()
            unpacked_index = 0
            for field in struct_fields:
                if field['length'] > 0:
                    output[field['name']] = self._unpack_field(unpacked, field, unpacked_index)
                unpacked_index += field['length']
            return output

        offset = 0
        unzip = False
        if count is None:
            count = 1
            unzip = True
        data = source if isinstance(source, bytes) else source.read(self.size * count)  # type: bytes

        for i in range(count):
            unpacked = []
            for sub_fmt in self._struct_format:
                size = struct.calcsize(sub_fmt)
                try:
                    unpacked += struct.unpack(sub_fmt, data[offset:offset + size])
                except struct.error:
                    print(f'Struct sub-format:', sub_fmt)
                    print(f'Offset {offset}:', data[offset:offset + size])
                    raise
                offset += size
            output = AttributeDict()
            unpacked_index = 0
            for field in self.fields:
                if field['length'] > 0:
                    output[field['name']] = self._unpack_field(unpacked, field, unpacked_index)
                    unpacked_index += field['length']
            outputs.append(output)
        if unzip:
            return outputs[0]
        return outputs

    def pack(self, struct_dicts=None, **struct_kwargs):
        if struct_dicts and struct_kwargs:
            raise ValueError("You cannot use both the 'struct_dicts' var args and the single-struct kwargs.")
        elif struct_kwargs:
            # You can easily pass a single struct dictionary as keyword arguments.
            struct_dicts = (struct_kwargs,)
        if not isinstance(struct_dicts, (list, tuple)):
            struct_dicts = (struct_dicts,)
        output = b''
        for struct_dict_ in struct_dicts:
            struct_dict = struct_dict_.copy()  # Does not modify the input dictionary.
            to_pack = []
            for field in self.fields:
                if field['length'] == 0:
                    # Padding.
                    continue
                name = field['name']
                if 'asserted' in field:
                    # Asserted values are written automatically, but you are permitted to pass the asserted value too.
                    if name in struct_dict and struct_dict[name] != field['asserted']:
                        raise ValueError(f"Field '{name}' has value {struct_dict[name]} instead of "
                                         f"asserted value {field['asserted']}.")
                    value = field['asserted']
                else:
                    try:
                        value = struct_dict.pop(name)
                    except KeyError:
                        raise KeyError(f"Field '{name}' missing from struct dictionary.")
                if 'jis_size' in field:
                    if not isinstance(value, str):
                        raise TypeError(f"Expected a string in JIS field '{name}', but received: {value}.")
                    jis_bytes = value.encode('shift_jis_2004')
                    jis_bytes += b'\0' * (field['jis_size'] - len(jis_bytes))  # pad string back to original size
                    value = [jis_bytes]
                elif isinstance(value, (list, tuple)):
                    value = list(value)
                else:
                    value = [value]
                to_pack += value
            if struct_dict:
                raise ValueError(f"Struct dict has leftover keys: {struct_dict}")
            pack_index = 0
            for sub_fmt, sub_fmt_length in zip(self._struct_format, self._struct_length):
                try:
                    output += struct.pack(sub_fmt, *to_pack[pack_index:pack_index + sub_fmt_length])
                except struct.error:
                    print("Struct sub-format:", sub_fmt, f"(length: {sub_fmt_length})")
                    print("To Pack:", to_pack[pack_index:pack_index + sub_fmt_length])
                    raise
        return output

    def copy(self):
        bs = BinaryStruct()
        bs.fields = self.fields
        bs._struct_format = self._struct_format
        bs._struct_length = self._struct_length
        bs.size = self.size
        return bs

    @staticmethod
    def set_repeated_fields(struct_dict, field_start, value):
        """ Looks for all fields in struct_dict that start with the given string and sets their value to 'value'. """
        for key in struct_dict:
            if key.startswith(field_start):
                struct_dict[key] = value

    def __repr__(self):
        s = f"BinaryStruct: {' '.join(self._struct_format)}\n"
        for i, field in enumerate(self.fields):
            s += f"    {field.get('name', 'x')} :: {field['fmt']}"
            if 'asserted' in field:
                s += f" (== {field['asserted']})\n"
            else:
                s += '\n'
        return s

    @property
    def struct_format(self):
        return self._struct_format


class AttributeDict(dict):
    """Simple dict extension that allows you to access values as attributes using dot notation."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self.update(*args, **kwargs)

    def update(self, *args, **kwargs):
        for d in args + (kwargs,):
            dict.update(self, d)
        return self


def read_chars_from_bytes(data, offset=0, length=None, encoding=None):
    """Read characters from a bytes object (an encoded string). Use 'read_chars_from_buffer' if you are using a buffer.

    If 'length=None' (default), characters will be read until null termination from the given offset. Otherwise,
    'length' bytes will be read and all null padding bytes will be stripped from the right side.

    Use 'encoding' to automatically decode the bytes into a string before returning (e.g. 'shift_jis_2004'). Note that
    if 'utf-16-le' is specified as the encoding with no length, a double-null termination of b'\0\0' is required to
    terminate the string (as single nulls can appear in the two-byte characters).
    """
    bytes_per_char = 2 if encoding is not None and encoding.replace('-', '') == 'utf16le' else 1
    if length is not None:
        stripped_array = data[offset:offset + length].rstrip().rstrip(b'\0' * bytes_per_char)  # remove spaces and nulls
        if encoding is not None:
            return stripped_array.decode(encoding)
        return stripped_array
    else:
        # Find null termination.
        null_termination = data[offset:].find(b'\0' * bytes_per_char)
        if null_termination == -1:
            raise ValueError("No null termination found for characters.")
        array = data[offset:offset + null_termination]
        if encoding is not None:
            try:
                return array.decode(encoding)
            except UnicodeDecodeError:
                print('Could not decode characters (returning raw bytes):', array)
                return array
        return array


def read_chars_from_buffer(buffer, offset=None, length=None, encoding=None, reset_old_offset=True):
    """Read characters from a buffer (type IOBase). Use 'read_chars_from_bytes' if your data is already in bytes format.

    If 'offset' is None, the buffer will be read from the current position. Otherwise, by default, the buffer will be
    reset to whatever offset it was at after the string has been read. (Set 'reset_old_offset=False' to prevent this.)

    If 'length' is None, the chars are assumed to be null-terminated (with b'\x00'). Otherwise, 'length' characters will
    be read, and any null padding at the right end will be stripped.

    Use 'encoding' to automatically decode the bytes into a string before returning (e.g. 'shift_jis_2004'). Note that
    if 'utf-16-le' is specified as the encoding with no length, a double-null termination of b'\0\0' is required to
    terminate the string (as single nulls can appear in the two-byte characters).
    """
    if length == 0:
        if not reset_old_offset and not isinstance(buffer, bytes):
            buffer.seek(offset)
        return '' if encoding is not None else b''

    if isinstance(buffer, bytes):
        buffer = BytesIO(buffer)
    chars = []
    old_offset = None
    bytes_per_char = 2 if encoding is not None and encoding.replace('-', '') == 'utf16le' else 1

    if offset is not None:
        old_offset = buffer.tell()
        buffer.seek(offset)

    while 1:
        c = buffer.read(bytes_per_char)
        if not c and length is None:
            raise ValueError("Ran out of bytes to read before null termination was found.")
        if length is None and c == b'\x00' * bytes_per_char:
            # Null termination.
            array = b''.join(chars)
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            if encoding is not None:
                try:
                    return array.decode(encoding)
                except UnicodeDecodeError:
                    print('Could not decode characters (returning raw bytes):', array)
                    return array
            return array
        elif len(chars) == length:
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            stripped_array = b''.join(chars)  # used to strip spaces as well, but not anymore
            stripped_array.rstrip()  # remove spaces
            stripped_array.rstrip(b'\0' * bytes_per_char)  # remove null characters
            if encoding is not None:
                return stripped_array.decode(encoding)
            return stripped_array
        else:
            chars.append(c)
