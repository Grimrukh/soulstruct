from __future__ import annotations

__all__ = [
    "PACKAGE_PATH",
    "find_dcx",
    "create_bak",
    "word_wrap",
    "camel_case_to_spaces",
    "floatify",
    "find_steam_common_paths",
    "traverse_path_tree",
    "BinaryStruct",
    "BaseStruct",
    "AttributeDict",
    "BiDict",
    "read_chars_from_bytes",
    "read_chars_from_buffer",
    "pad_chars",
    "get_startupinfo",
]

import abc
import ctypes
import io
import logging
import os
import re
import string
import struct
import subprocess
import sys
import textwrap
import typing as tp
from pathlib import Path


_LOGGER = logging.getLogger(__name__)


def PACKAGE_PATH(*relative_parts):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"), *relative_parts)
    return Path(__file__).absolute().parent.joinpath("..", *relative_parts)


def find_dcx(file_path):
    """Returns DCX (preferred) or non-DCX version of the given file path.

    It doesn't matter if the file path already ends with '.dcx'. If neither file exists, FileNotFoundError is raised.
    """
    file_path = Path(file_path)
    if file_path.suffix == ".dcx":
        no_dcx, dcx = (file_path.parent / file_path.stem, file_path)
    else:
        no_dcx, dcx = (file_path, file_path.with_suffix(file_path.suffix + ".dcx"))
    if Path(dcx).is_file():
        return dcx
    elif Path(no_dcx).is_file():
        return no_dcx
    raise FileNotFoundError(f"Could not find DCX or non-DCX version of {file_path}.")


def create_bak(file_path):
    file_path = Path(file_path)
    if file_path.is_file() and not file_path.with_suffix(file_path.suffix + ".bak").is_file():
        backup_path = str(file_path.with_suffix(file_path.suffix + ".bak"))
        os.rename(str(file_path), backup_path)
        _LOGGER.info(f"Created {repr(backup_path)} backup file.")
        return True
    return False


def word_wrap(text, line_limit=50):
    return "\n".join(textwrap.wrap(text, line_limit))


def camel_case_to_spaces(camel_string: str) -> str:
    """Preserves consecutive capitals (e.g. JSONFileName -> JSON File Name) and non-alphabetical symbols.

    Needs two passes to handle cases of singular capital letters and numbers/symbols (which need spaces on both sides).
    """
    camel_string = re.sub(r"([A-Z])([A-Z])([a-z])|([0-9%]+)([A-Z])", r"\1\4 \2\3\5", camel_string)  # ABc -> A Bc
    camel_string = re.sub(r"([a-z])([A-Z])|([A-Za-z])([0-9%]+)", r"\1\3 \2\4", camel_string)  # aB -> a B
    return camel_string


def floatify(int32: int, signed=False) -> float:
    """Utility function that re-interprets a 32-bit unsigned (default) or signed integer as a single float.

    This could be useful if you have any old EMEVD scripts that incorrectly represent float event arguments as integers.
    """
    pack_fmt = "<i" if signed else "<I"
    return struct.unpack("<f", struct.pack(pack_fmt, int32))[0]


def find_steam_common_paths():
    """Not using anymore. Seems to cause 'WinError 87' OSErrors for some people for some drives."""
    steam_common_paths = []
    for drive in _get_drives():
        for arch in {"", " (x86)"}:
            common_path = Path(drive, f"Program Files{arch}/Steam/steamapps/common/")
            if common_path.is_dir():
                steam_common_paths.append(common_path)
    return steam_common_paths


def traverse_path_tree(tree, cur=()):
    if isinstance(tree, dict):
        for node, leaf in tree.items():
            for path in traverse_path_tree(leaf, cur + (node,)):
                yield path
    elif isinstance(tree, (list, tuple)):
        for item in tree:
            if isinstance(item, str):
                yield cur + (item,)
            else:  # dict
                for path in traverse_path_tree(item, cur):
                    yield path
    else:
        raise ValueError(f"Invalid type encountered in path tree: {type(tree)}")


class BinaryStruct:
    BYTE_ORDER_RE = re.compile(r"[<>@].*")
    PAD_RE = re.compile(r"([0-9]*)?x")
    JIS_FORMAT_RE = re.compile(r"([0-9]*)?j")
    CHARS_FORMAT_RE = re.compile(r"([0-9]*)?s")
    OTHER_FORMAT_RE = re.compile(r"([0-9]*)?(?!s)")

    def __init__(self, *fields, byte_order="<"):
        """Flexible binary unpacker/repacker."""
        self.fields = []  # field dictionaries
        self._struct_format = []  # Format chunks with different byte order are stored in sub-format strings.
        self._struct_length = []  # Number of values to be packed using each sub-format string.
        self.size = 0
        self.add_fields(*fields, byte_order=byte_order)

    def add_fields(self, *fields, byte_order=None):
        """Add new fields to the BinaryStruct.

        Args:
             *fields: sequence of fields to add.
             byte_order: byte order for the added fields to use, which can be different from the byte order of other
                fields. By default, the most recent byte order is used.

        Returns:
            field_list, struct_format
        """
        if not fields:
            return
        if byte_order is None:
            if self._struct_format:
                byte_order = self._struct_format[-1][0]
                new_fmt = False
            else:
                byte_order = "<"  # default
                new_fmt = True
        elif not self._struct_format or byte_order != self._struct_format[-1][0]:
            if byte_order not in {"<", ">", "@"}:
                raise ValueError("byte_order must be '<', '>', or '@'.")
            new_fmt = True
        else:
            # Append to most recent sub-format (same byte order).
            new_fmt = False

        sub_fmt = ""
        sub_fmt_length = 0
        new_fields = []

        for field in fields:
            if isinstance(field, str):
                # Pad string.
                if self.PAD_RE.match(field):
                    new_fields.append({"fmt": field, "length": 0})
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
                    d["asserted"] = asserted
                except IndexError:
                    pass
            else:
                raise TypeError(
                    "Each field should be a single pad '#x' format string, a (name, format) "
                    "pair, or a (name, format, asserted) triplet."
                )

            if self.BYTE_ORDER_RE.match(fmt):
                raise ValueError("Individual field format should not have its own byte order. Pass as a keyword arg.")
            if self.JIS_FORMAT_RE.match(fmt):
                jis_size = int(fmt[:-1]) if fmt[:-1] else 1
                fmt = str(jis_size) + "s"
                d["jis_size"] = jis_size
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
        if field["length"] == 0:
            # Ignore.
            return
        value = unpacked_values[index : index + field["length"]]
        if field["length"] == 1:
            # Unzip single values.
            value = value[0]
        else:
            # Convert tuples to lists.
            value = list(value)
        if "jis_size" in field:
            value = read_chars_from_bytes(value, length=len(value), encoding="shift_jis_2004")
            value = value.rstrip("\0")
        if "asserted" in field:
            if value != field["asserted"]:
                raise ValueError(
                    f"Field '{field['name']}' contained {value} instead of asserted value {field['asserted']}."
                )
        return value

    def unpack(self, source, *fields, byte_order=None, include_asserted=True) -> AttributeDict:
        """Unpack a single struct from source data.

        If any 'fields' are specified (same allowed formats as the constructor above), only those fields will be
        unpacked, and they will then be added to the BinaryStruct. This allows you to dynamically build the BinaryStruct
        on the fly if the structure itself depends on the values read (e.g. a big-endian flag). The same BinaryStruct
        can then be used for repacking later.

        Args:
            source: bytes or open buffer to unpack from.
            fields: optional list of new fields to simultaneously add and unpack (instead of full struct).
            byte_order: byte order of the new fields.
            include_asserted: include any asserted fields in the returned dictionary.

        Returns:
            AttributeDict
        """
        if fields:
            # Unpack just the given fields after adding them to the BinaryStruct.
            struct_fields, struct_fmt = self.add_fields(*fields, byte_order=byte_order)
            size = struct.calcsize(struct_fmt)
            data = source if isinstance(source, bytes) else source.read(size)  # type: bytes
            try:
                unpacked = struct.unpack(struct_fmt, data)
            except struct.error:
                _LOGGER.error(f"Failed to unpack data:", data)
                raise
            output = AttributeDict()
            unpacked_index = 0
            for field in struct_fields:
                if field["length"] > 0 and (include_asserted or "asserted" not in field):
                    output[field["name"]] = self._unpack_field(unpacked, field, unpacked_index)
                unpacked_index += field["length"]
            return output

        offset = 0
        data = source if isinstance(source, bytes) else source.read(self.size)  # type: bytes
        unpacked = []
        for sub_fmt in self._struct_format:
            size = struct.calcsize(sub_fmt)
            try:
                unpacked += struct.unpack(sub_fmt, data[offset : offset + size])
            except struct.error:
                _LOGGER.error(
                    f"Failed to unpack data at offset {offset} with sub-format {sub_fmt}: "
                    f"{data[offset:offset + size]}"
                )
                raise
            offset += size
        output = AttributeDict()
        unpacked_index = 0
        for field in self.fields:
            if field["length"] > 0 and (include_asserted or "asserted" not in field):
                output[field["name"]] = self._unpack_field(unpacked, field, unpacked_index)
            unpacked_index += field["length"]
        return output

    def unpack_count(self, source, count, include_asserted=True) -> tp.List[AttributeDict]:
        """Unpack `count` identical structs from `source`. See `unpack()` for more.

        Args:
            source: bytes or open buffer to unpack from.
            count: number of contiguous structs to unpack from source.
            include_asserted: include asserted fields in the output dictionary. (Default: True)

        Returns:
            list[AttributeDict]
        """
        return [self.unpack(source, include_asserted=include_asserted) for _ in range(count)]

    def pack(self, struct_dicts=None, **struct_kwargs) -> bytes:
        if struct_dicts and struct_kwargs:
            raise ValueError("You cannot use both the `struct_dicts` argument and the single-struct `**struct_kwargs`.")
        elif struct_kwargs:
            # You can pass a single struct dictionary as keyword arguments.
            struct_dicts = (struct_kwargs,)
        if not isinstance(struct_dicts, (list, tuple)):
            struct_dicts = (struct_dicts,)
        output = b""
        for struct_dict_ in struct_dicts:
            struct_dict = struct_dict_.copy()  # Does not modify the input dictionary.
            to_pack = []
            for field in self.non_padding_fields:
                name = field["name"]
                if "asserted" in field:
                    # Asserted values are written automatically, but you are permitted to pass the asserted value too.
                    if name in struct_dict and struct_dict[name] != field["asserted"]:
                        raise ValueError(
                            f"Field '{name}' has value {struct_dict[name]} instead of "
                            f"asserted value {field['asserted']}."
                        )
                    value = field["asserted"]
                else:
                    try:
                        value = struct_dict.pop(name)
                    except KeyError:
                        raise KeyError(f"Field '{name}' missing from struct dictionary.")
                if "jis_size" in field:
                    if not isinstance(value, str):
                        raise TypeError(f"Expected a string in JIS field '{name}', but received: {value}.")
                    jis_bytes = value.encode("shift_jis_2004")
                    jis_bytes += b"\0" * (field["jis_size"] - len(jis_bytes))  # pad string back to original size
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
                    output += struct.pack(sub_fmt, *to_pack[pack_index : pack_index + sub_fmt_length])
                except struct.error:
                    _LOGGER.error(
                        f"Failed to pack data at offset {pack_index} with sub-format {sub_fmt} and length "
                        f"{sub_fmt_length}: {to_pack[pack_index:pack_index + sub_fmt_length]}"
                    )
                    raise
        return output

    def pack_from_object(self, obj) -> bytes:
        """Attempts to build complete struct dictionary from attributes of given object `obj`.

        All non-constant fields must be present as attributes, or an exception will be raised.
        """
        struct_dict = {}
        for field in self.non_padding_fields:
            if field["length"] == 0:
                continue  # padding
            try:
                struct_dict[field["name"]] = getattr(obj, field["name"])
            except AttributeError:
                if "asserted" not in field:
                    raise AttributeDict(
                        f"Non-asserted field {repr(field)} is not an attribute of given object {obj}. Cannot pack."
                    )
        return self.pack((struct_dict,))

    def copy(self):
        bs = BinaryStruct()
        bs.fields = self.fields
        bs._struct_format = self._struct_format
        bs._struct_length = self._struct_length
        bs.size = self.size
        return bs

    @staticmethod
    def set_repeated_fields(struct_dict, field_start, value):
        """Looks for all fields in struct_dict that start with the given string and sets their value to 'value'."""
        for key in struct_dict:
            if key.startswith(field_start):
                struct_dict[key] = value

    def __repr__(self):
        s = f"BinaryStruct: {' '.join(self._struct_format)}\n"
        for i, field in enumerate(self.fields):
            s += f"    {field.get('name', 'x')} :: {field['fmt']}"
            if "asserted" in field:
                s += f" (== {field['asserted']})\n"
            else:
                s += "\n"
        return s

    @property
    def struct_format(self):
        return self._struct_format

    @property
    def non_padding_fields(self):
        """Return only non-padding fields (including asserted fields)."""
        return [field for field in self.fields if field["length"] != 0]


class BaseStruct(abc.ABC):
    STRUCT: BinaryStruct = None


class AttributeDict(dict):
    """Simple dict extension that redirects `__getattr__` to `__getitem__`, allowing dot notation field access."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self.update(*args, **kwargs)

    def update(self, *args, **kwargs):
        for d in args + (kwargs,):
            dict.update(self, d)
        return self


class BiDict(dict):
    def __init__(self, *args):
        """Initialized with pairs of values to be connected."""
        super().__init__()
        self.__keys = []
        self.__values = []
        for arg in args:
            if not isinstance(arg, tuple) or len(arg) != 2:
                raise ValueError("BiDict can only be initialized with (value_1, value_2) tuple pair args.")
            self.__setitem__(*arg)

    def __setitem__(self, value_1, value_2):
        """Removes any pre-existing connections using either value.

        Order of values determines whether they will appear in `keys()` or `values()`.
        """
        if value_1 in self:
            del self[value_1]
            try:
                self.__keys.remove(value_1)
            except ValueError:
                pass
            try:
                self.__values.remove(value_1)
            except ValueError:
                pass
        if value_2 in self:
            del self[value_2]
            try:
                self.__keys.remove(value_2)
            except ValueError:
                pass
            try:
                self.__values.remove(value_2)
            except ValueError:
                pass
        super().__setitem__(value_1, value_2)
        super().__setitem__(value_2, value_1)
        self.__keys.append(value_1)
        self.__values.append(value_2)

    def __delitem__(self, key):
        super().__delitem__(key)
        super().__delitem__(self[key])

    def __len__(self):
        return super().__len__() // 2

    def __iter__(self):
        return iter(self.__keys)

    def keys(self):
        """Returns first elements of all set pairs."""
        return self.__keys

    def values(self):
        """Returns second elements of all set pairs."""
        return self.__values

    def items(self):
        """Returns all set pairs in order."""
        return zip(self.__keys, self.__values)


def _get_drives():
    drives = []
    bit_mask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bit_mask & 1:
            drives.append(letter + ":/")
        bit_mask >>= 1
    return drives


def read_chars_from_bytes(data, offset=0, length=None, encoding=None, ignore_encoding_error_for_these_chars=()):
    """Read characters from a bytes object (an encoded string). Use 'read_chars_from_buffer' if you are using a buffer.

    If 'length=None' (default), characters will be read until null termination from the given offset. Otherwise,
    'length' bytes will be read and all null padding bytes will be stripped from the right side.

    Use 'encoding' to automatically decode the bytes into a string before returning (e.g. 'shift_jis_2004'). Note that
    if 'utf-16-le' is specified as the encoding with no length, a double-null termination of b'\0\0' is required to
    terminate the string (as single nulls can appear in the two-byte characters).
    """
    bytes_per_char = 2 if encoding is not None and encoding.replace("-", "") == "utf16le" else 1
    if length is not None:
        stripped_array = (
            data[offset : offset + length].rstrip().rstrip(b"\0" * bytes_per_char)
        )  # remove spaces and nulls
        if encoding is not None:
            return stripped_array.decode(encoding)
        return stripped_array
    else:
        # Find null termination.
        null_termination = data[offset:].find(b"\0" * bytes_per_char)
        if null_termination == -1:
            raise ValueError("No null termination found for characters.")
        array = data[offset : offset + null_termination]
        if encoding is not None:
            try:
                return array.decode(encoding)
            except UnicodeDecodeError:
                if array in ignore_encoding_error_for_these_chars:
                    return array
                raise
        return array


def read_chars_from_buffer(
    buffer, offset=None, length=None, reset_old_offset=True, encoding=None, ignore_encoding_error_for_these_chars=()
):
    """Read characters from a buffer (type IOBase). Use 'read_chars_from_bytes' if your data is already in bytes format.

    Args:
        buffer: byte-format data stream to read from.

        offset: offset to seek() in buffer before starting to read characters. Defaults to current offset.

        reset_old_offset: if True, and 'offset' is not None, the buffer offset will be restored to its original position
            (at function call time) before returning. (Default: True)

        length: number of characters to read (i.e. the length of the returned string). If None (default), characters
            will be read until a null termination is encountered. Otherwise, if a length is specified, any spaces at
            the end of the string will be stripped, then any nulls at the end will be stripped.

        encoding: attempt to decode characters in this encoding before returning. If 'utf-16-le' is specified, this
            function will infer that characters are two bytes long (and null terminations will be two bytes). Otherwise,
            it assumes they are one byte long. You can decode the characters yourself if you want to use another
            multiple-bytes-per-character encoding.

        ignore_encoding_error_for_these_chars: if a decoding error occurs for any character (bytes) in this sequence,
            the encoded bytes will be returned instead of raising a UnicodeDecodeError.
    """
    if length == 0:
        if not reset_old_offset and not isinstance(buffer, bytes):
            buffer.seek(offset)
        return "" if encoding is not None else b""

    if isinstance(buffer, bytes):
        buffer = io.BytesIO(buffer)
    chars = []
    old_offset = None
    bytes_per_char = 2 if encoding is not None and encoding.replace("-", "") == "utf16le" else 1

    if offset is not None:
        old_offset = buffer.tell()
        buffer.seek(offset)

    while 1:
        c = buffer.read(bytes_per_char)
        if not c and length is None:
            raise ValueError("Ran out of bytes to read before null termination was found.")
        if length is None and c == b"\x00" * bytes_per_char:
            # Null termination.
            array = b"".join(chars)
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            if encoding is not None:
                try:
                    return array.decode(encoding)
                except UnicodeDecodeError:
                    if array in ignore_encoding_error_for_these_chars:
                        return array
                    raise
            return array
        elif len(chars) == length:
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            stripped_array = b"".join(chars)  # used to strip spaces as well, but not anymore
            stripped_array.rstrip()  # remove spaces
            stripped_array.rstrip(b"\0" * bytes_per_char)  # remove null characters
            if encoding is not None:
                return stripped_array.decode(encoding)
            return stripped_array
        else:
            chars.append(c)


def pad_chars(text, encoding=None, null_terminate=True, pad_to_multiple_of=4):
    """Pad text out to given multiple of byte length with null bytes. Optionally, encode it first."""
    if pad_to_multiple_of < 0 or not isinstance(pad_to_multiple_of, int):
        raise ValueError("pad must be an integer greater than zero.")
    if encoding is not None:
        encoded = text.encode(encoding) + (b"\0" if null_terminate else b"")
    else:
        encoded = text + ("\0" if null_terminate else "")
    pad = b"\0" if encoding is not None else "\0"
    while len(encoded) % pad_to_multiple_of != 0:
        encoded += pad
    return encoded


def get_startupinfo():
    """Disables command window for PyInstaller `--noconsole` option.

    See `https://github.com/pyinstaller/pyinstaller/wiki/Recipe-subprocess`
    """
    if hasattr(subprocess, "STARTUPINFO"):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    else:
        si = None
    return si
