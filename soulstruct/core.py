import functools
from io import BytesIO
import itertools
import re
import struct


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

        if byte_order not in {'<', '>', '@'}:
            raise ValueError("byte_order must be '<', '>', or '@'.")
        self._struct_format = byte_order
        self._fields = []  # (name, length) pairs
        self._field_length = []
        self._asserted_values = {}
        self._jis_field_size = {}
        for field in fields:
            if isinstance(field, str):
                if self.PAD_RE.match(field):
                    self._fields.append((field, 0))
                    self._struct_format += field
                    continue
                else:
                    raise ValueError("Only pad strings are permitted outside tuples.")
            elif isinstance(field, (list, tuple)):
                field_name = field[0]
                field_format = field[1]
                try:
                    asserted_value = field[2]
                    if isinstance(asserted_value, tuple):
                        asserted_value = list(asserted_value)
                except IndexError:
                    pass
                else:
                    self._asserted_values[field_name] = asserted_value
            else:
                raise TypeError("Each field should be a single pad '#x' format string, a (name, format) "
                                "pair, or a (name, format, asserted) triplet.")

            if self.BYTE_ORDER_RE.match(field_format):
                raise ValueError("Field format should not have its own byte order character.")
            if self.JIS_FORMAT_RE.match(field_format):
                self._jis_field_size[field_name] = int(field_format[:-1])
                field_format = field_format[:-1] + 's'
                field_length = 1
            elif self.CHARS_FORMAT_RE.match(field_format):
                field_length = 1
            else:
                try:
                    field_length = self.OTHER_FORMAT_RE.match(field_format).group(1)
                    field_length = 1 if not field_length else int(field_length)
                except AttributeError:
                    raise ValueError(f"Invalid field format: '{field_format}'.")
            self._fields.append((field_name, field_length))
            self._struct_format += field_format

        self.size = struct.calcsize(self._struct_format)

    def unpack(self, source, count=None):
        """ Unpack one or more structs from source data.

        Args:
            source: bytes or open buffer to unpack from.
            count: number of contiguous structs to unpack from source (returned as a list).

        Returns:
            dict (or list of dicts if 'count' is given) with unpacked fields.
        """
        outputs = []
        unzip = False
        if count is None:
            count = 1
            unzip = True
        data = source if isinstance(source, bytes) else source.read(self.size * count)  # type: bytes
        offset = 0
        for i in range(count):
            unpacked = struct.unpack(self._struct_format, data[offset:offset + self.size])
            offset += self.size
            output = AttributeDict()
            unpacked_index = 0
            for name, length in self._fields:
                if length == 0:
                    # Ignore.
                    continue
                value = unpacked[unpacked_index:unpacked_index + length]
                if length == 1:
                    # Unpack single values.
                    value = value[0]
                else:
                    # Convert tuples to lists.
                    value = list(value)
                unpacked_index += length
                if name in self._jis_field_size:
                    value = read_chars_from_bytes(value, length=len(value), encoding='shift_jis_2004')
                    value = value.rstrip('\0')
                if name in self._asserted_values:
                    asserted = self._asserted_values[name]
                    if value != asserted:
                        raise ValueError(
                            f"Field '{name}' contained {value} instead of asserted value {asserted}.")
                output[name] = value
            outputs.append(output)
        if unzip:
            return outputs[0]
        return outputs

    def pack(self, struct_dicts=None, **struct_kwargs):
        if struct_dicts and struct_kwargs:
            raise ValueError("You cannot use both the main 'struct' argument and struct kwargs.")
        elif struct_kwargs:
            # You can easily pass a single struct dictionary as keyword arguments.
            struct_dicts = (struct_kwargs,)
        if not isinstance(struct_dicts, (list, tuple)):
            struct_dicts = (struct_dicts,)
        output = b''
        for struct_dict_ in struct_dicts:
            # Check keys match (excluding asserted fields).
            struct_dict = struct_dict_.copy()
            to_pack = []
            for field_name, field_length in self._fields:
                if field_length == 0:
                    # Padding.
                    continue
                elif field_name in self._asserted_values:
                    if field_name in struct_dict and struct_dict[field_name] != self._asserted_values[field_name]:
                        raise ValueError(f"Field '{field_name}' has value {struct_dict[field_name]} instead of "
                                         f"asserted value {self._asserted_values[field_name]}.")
                    value = self._asserted_values[field_name]
                else:
                    try:
                        value = struct_dict.pop(field_name)
                    except KeyError:
                        raise KeyError(f"Field '{field_name}' missing from struct dictionary.")
                if field_name in self._jis_field_size:
                    if not isinstance(value, str):
                        raise TypeError(f"Expected a string in JIS field '{field_name}', but received: {value}.")
                    jis_bytes = value.encode('shift_jis_2004')
                    jis_bytes += b'\0' * (self._jis_field_size[field_name] - len(jis_bytes))  # pad encoded string
                    value = [jis_bytes]
                elif isinstance(value, (list, tuple)):
                    value = list(self._asserted_values[field_name])
                else:
                    value = [value]
                to_pack += value
            if struct_dict:
                raise ValueError(f"Struct dict has leftover keys: {struct_dict}")
            output += struct.pack(self._struct_format, *to_pack)
        return output

    @staticmethod
    def set_repeated_fields(struct_dict, field_start, value):
        """ Looks for all fields in struct_dict that start with the given string and sets their value to 'value'. """
        for key in struct_dict:
            if key.startswith(field_start):
                struct_dict[key] = value


class AttributeDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self.update(*args, **kwargs)

    def update(self, *args, **kwargs):
        for d in args + (kwargs,):
            dict.update(self, d)
        return self


def read_null_terminated_string(buffer, offset=None, encoding=None):
    if offset is not None:
        old_offset = buffer.tell()
        buffer.seek(offset)
    else:
        old_offset = None
    to_eof = iter(functools.partial(buffer.read, 1), b'')
    string = b''.join(itertools.takewhile('\0'.__ne__, to_eof))
    if encoding is not None:
        string = string.decode(encoding)
    if old_offset is not None:
        buffer.seek(old_offset)
    return string


def read_chars_from_bytes(data, offset=0, length=None, encoding=None):

    if length is not None:
        stripped_array = data[offset:offset + length].rstrip().replace(b'\x00', b'')
        if encoding is not None:
            return stripped_array.decode(encoding)
        return stripped_array
    else:
        # Find null termination.
        null_termination = data[offset:].find(b'\0')
        if null_termination == -1:
            raise ValueError("No null termination found for characters.")
        array = data[offset:offset + null_termination]
        if encoding is not None:
            try:
                return array.decode(encoding)
            except UnicodeDecodeError:
                print('Could not decode characters (returning raw):', array)
                return array
        return array


def read_chars(buffer, offset=None, length=None, encoding=None, reset_old_offset=True):
    # TODO: Buffer is too slow for this. Use bytes. (Actually, not sure if this is true.)
    """ Read characters from a buffer. If a bytes object is passed, it will be converted into a buffer automatically.

    If 'offset' is None, the buffer/bytes will be read from the start. Otherwise, the buffer will be reset to whatever
    offset it was at after the string has been read.

    If 'length' is None, the chars are assumed to be null-terminated (with b'\x00'). Otherwise, any null padding at the
    right end will be stripped.

    Use 'encoding' to automatically decode the bytes into a string before returning (e.g. 'shift_jis_2004'). """

    # traceback.print_stack()  # TODO

    if isinstance(buffer, bytes):
        buffer = BytesIO(buffer)
    chars = []
    old_offset = None
    bytes_per_char = 2 if encoding == 'utf-16le' else 1

    if offset is not None:
        old_offset = buffer.tell()
        buffer.seek(offset)

    while 1:
        c = buffer.read(bytes_per_char)
        if length is None and c == b'\x00' * bytes_per_char:
            # Null termination.
            array = b''.join(chars)
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            if encoding is not None:
                try:
                    return array.decode(encoding)
                except UnicodeDecodeError:
                    print('Could not decode characters (returning raw):', array)
                    return array
            return array
        elif len(chars) == length:
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            stripped_array = b''.join(chars).rstrip(b' \x00')
            if encoding is not None:
                return stripped_array.decode(encoding)
            return stripped_array
        else:
            chars.append(c)


def read_utf16le_string(buffer, offset=None, reset_to_old_offset=True):
    if not isinstance(buffer, BytesIO):
        buffer = BytesIO(buffer)
    chars = []
    if offset is not None:
        old_offset = buffer.tell()
        buffer.seek(offset)
    else:
        old_offset = None
    while True:
        c = buffer.read(2)
        if c == b'\x00\x00':
            # Null termination.
            if reset_to_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            return b''.join(chars).decode('utf-16le')
        chars.append(c)
