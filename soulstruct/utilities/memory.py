from __future__ import annotations

__all__ = [
    "MemoryHook",
    "MemoryHookCallError",
    "UnhookedError",
    "BasePointerSearch",
    "MemoryValue",
    "memory_hook_validate",
    "memory_hook_cache",
]

import abc
import ctypes as c
import functools
import io
import logging
import re
import struct
import typing as tp
from dataclasses import dataclass, field

import numpy
from rich.console import Console

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.files import APPDATA_PATH, read_json, write_json
from soulstruct.utilities.kernel32 import *

if tp.TYPE_CHECKING:
    from ctypes import wintypes as w

try:
    # noinspection PyPackageRequirements
    import psutil
except ImportError:
    psutil = None

_LOGGER = logging.getLogger(__name__)


class UnhookedError(SoulstructError):
    """Raised when hook is lost. It will attempt to be reacquired on each call."""
    pass


class MemoryHookCallError(SoulstructError):
    """Raised by errors that occur when process IS hooked."""
    pass


class BasePointerSearch(tp.NamedTuple):
    sequence: bytes
    address_func: tp.Optional[tp.Callable[[MemoryHook, int], int]] = None


class MemoryValue(tp.NamedTuple):
    pointer: str
    jumps: tp.Sequence[int]
    size: int
    fmt: str


def memory_hook_validate(method):
    """Decorator that checks the hooked process is still valid before continuing.

    Tries to re-establish hook on call.
    """
    @functools.wraps(method)
    def wrapped(*args, **kwargs):
        self = args[0]  # type: MemoryHook
        if not self.process or not self.process.is_running():
            # Lost (or never found) process. Try to reconnect.
            if not self.find_process():
                raise UnhookedError(f"Could not hook into process '{self.PROCESS_NAME}'.")
        return method(*args, **kwargs)

    return wrapped


def memory_hook_cache(method):
    """Updates cache from address cache file before calling method, then writes latest address cache."""

    @functools.wraps(method)
    def wrapped(*args, **kwargs):
        self = args[0]  # type: MemoryHook
        if not self.ADDRESS_CACHE_NAME:
            return method(*args, **kwargs)

        self._read_cached()
        result = method(*args, **kwargs)
        self._write_cached()

        return result

    return wrapped


@dataclass(slots=True)
class BufferedMemory(io.BufferedIOBase):
    """Interface that mimics `io.BufferedIOBase` with data from a hooked memory process, from a given start address.

    Currently only implements `read(n)`, `tell()`, and `seek(offset, whence)`.

    Args:
        hook (MemoryHook): hooked process to read from.
        start_address (int): initial address to read from.
        chunk_size (int): number of bytes to read at once.
        max_size (int): if given, raise an `IOError` if more than this many bytes are read.
    """

    hook: MemoryHook = field(repr=False)
    start_address: int
    chunk_size: int = 1024  # number of bytes to read at once
    max_size: int | None = None

    _current_address: int = field(init=False, default=0)  # next process address to buffer data from
    _stream_offset: int = field(init=False, default=0)  # relative to `start_address`
    _bytes_read: int = field(init=False, default=0)
    _buffer: bytes = field(init=False, default=b"")

    # noinspection PyMethodOverriding
    def read(self, size: int) -> bytes:
        output = b""
        if self.max_size is not None and self._bytes_read + size > self.max_size:
            raise IOError(f"Tried to read more than specified maximum bytes ({self.max_size}) from process.")
        bytes_to_read = size

        while bytes_to_read > 0:
            if not self._buffer:
                self._buffer = self.hook.read(self._current_address, self.chunk_size)
                self._current_address += self.chunk_size  # address for next buffer read

            if bytes_to_read >= len(self._buffer):
                output += self._buffer
                bytes_to_read -= len(self._buffer)
                self._buffer = b""
            else:  # less than buffer size
                output += self._buffer[:bytes_to_read]
                self._buffer = self._buffer[bytes_to_read:]
                bytes_to_read = 0
        self._stream_offset += size
        return output

    def tell(self):
        return self._stream_offset

    def seek(self, offset: int, whence: int = None):
        self._current_address = self.start_address + offset
        self._stream_offset = offset
        self._buffer = b""


class MemoryHook(abc.ABC):
    """Hooks into running game and edits values at given memory addresses (like CheatEngine)."""

    PROCESS_NAME: tp.ClassVar[str]
    BASE_ADDRESS: tp.ClassVar[int]
    ADDRESS_CACHE_NAME: tp.ClassVar[str] = ""  # must be defined to read/write cached addresses

    BASE_POINTER_TABLE: tp.ClassVar[dict[str, tp.Union[int, BasePointerSearch]]] = {}
    VALUE_TABLE: tp.ClassVar[dict[str, MemoryValue]] = {}

    # Base address and at least one jump offset for event flags (not including flag-specific offset).
    EVENT_FLAG_OFFSETS: tp.ClassVar[tuple[int, ...]] = ()

    MemoryHookCallError = MemoryHookCallError
    UnhookedError = UnhookedError

    process: psutil.Process | None
    p_handle: w.HANDLE | None

    value_table: dict[str, MemoryValue]  # mapping of value names to `MemoryValue` objects
    _address_cache: dict[str, int]  # cached addresses for pointers (loaded from/written to `ADDRESS_CACHE_NAME` file)
    base_pointer_table: dict[str, int]  # named, resolved base pointer addresses
    process: psutil.Process | None  # process handle for the hooked game
    p_handle: w.HANDLE | None  # Windows handle for the hooked process (for reading/writing memory)
    _console: Console

    def __init__(self, clear_address_cache: bool = False):

        if psutil is None:
            raise ModuleNotFoundError("`psutil` package required to use Soulstruct `MemoryHook`.")

        self.value_table = self.VALUE_TABLE.copy()
        self._address_cache = {}
        self.base_pointer_table = {}

        if clear_address_cache and self.ADDRESS_CACHE_NAME:
            self._write_cached()
            _LOGGER.info(f"Cleared address cache for '{self.PROCESS_NAME}'.")

        self.process = None
        self.p_handle = None
        self.find_process()

        self._console = Console()

        if self.p_handle and self.BASE_POINTER_TABLE:
            self._load_pointer_table(self.BASE_POINTER_TABLE)

    def find_process(self) -> bool:
        for p in psutil.process_iter():
            if p.name() == self.PROCESS_NAME:
                self.process = p
                _LOGGER.info(f"Found '{self.PROCESS_NAME}' process with PID: {p.pid}")
                break
        else:
            # _LOGGER.warning(f"Could not find process '{self.PROCESS_NAME}'.")
            return False

        self.p_handle = kernel32.OpenProcess(
            PROCESS_VM_READ + PROCESS_VM_WRITE + PROCESS_VM_OPERATION,
            False,
            self.process.pid,
        )
        _LOGGER.info(f"Process handle for '{self.PROCESS_NAME}' opened successfully.")
        if self.BASE_POINTER_TABLE:
            try:
                self._load_pointer_table(self.BASE_POINTER_TABLE)
                _LOGGER.info(f"Base pointer table for '{self.PROCESS_NAME}' loaded successfully.")
            except MemoryHookCallError as ex:
                _LOGGER.error(f"Could not load base pointer table for '{self.PROCESS_NAME}'. Error: {ex}")
                return False
        return True

    def __del__(self):
        try:
            kernel32.CloseHandle(self.p_handle)
        except AttributeError:
            pass

    @memory_hook_validate
    def _load_pointer_table(self, pointer_dict: dict[str, tp.Union[int, BasePointerSearch]]):
        self.base_pointer_table = {}
        pointers_to_find = {}  # type: dict[str, BasePointerSearch]
        for pointer_name, pointer in pointer_dict.items():
            if isinstance(pointer, int):
                self.base_pointer_table[pointer_name] = pointer
            elif isinstance(pointer, BasePointerSearch):
                pointers_to_find[pointer_name] = pointer
            else:
                raise TypeError(f"`pointer_dict` values must be integers (known addresses) or `BasePointerSearch`s.")

        if pointers_to_find:
            _LOGGER.info(f"Scanning game memory for {len(pointers_to_find)} pointers...")
            pointer_addresses = self.scan(pointers_to_find, use_regex=True)
            for pointer_name, address in pointer_addresses.items():
                if address is None:
                    raise MemoryHookCallError(f"Could not locate memory pointer: {pointer_name}")
                self.base_pointer_table[pointer_name] = address

    @memory_hook_validate
    def read(self, address, size, fmt=""):
        buffer = (c.c_char * size)()
        bytes_read = SIZE_T()
        try:
            kernel32.ReadProcessMemory(self.p_handle, address, buffer, size, c.byref(bytes_read))
        except WindowsError as e:
            raise MemoryHookCallError(e)
        value = bytes(buffer[:bytes_read.value])
        if fmt:
            values = struct.unpack(fmt, value)
            if len(values) == 1:
                return values[0]
            return values
        return value

    @memory_hook_validate
    def write(self, address, data, fmt=""):
        if fmt:
            data = struct.pack(fmt, *data)
        elif not isinstance(data, bytes):
            raise TypeError("Data to write to memory must be `bytes`, or 'fmt' must be given to convert a sequence.")
        size = len(data)
        buffer = c.create_string_buffer(data)
        bytes_written = SIZE_T(0)
        try:
            kernel32.WriteProcessMemory(self.p_handle, address, buffer, size, c.byref(bytes_written))
        except WindowsError as e:
            raise MemoryHookCallError(e)

    def get_buffer_at_address(self, address: int, chunk_size: int = 1024, maximum_size: int = None):
        return BufferedMemory(self, address, chunk_size, maximum_size)

    def read_int16(self, address):
        return self.read(address, size=2, fmt="<h")

    def read_int32(self, address):
        return self.read(address, size=4, fmt="<i")

    def read_int64(self, address):
        return self.read(address, size=8, fmt="<q")

    def read_uint16(self, address):
        return self.read(address, size=2, fmt="<H")

    def read_uint32(self, address):
        return self.read(address, size=4, fmt="<I")

    def read_uint64(self, address):
        return self.read(address, size=8, fmt="<Q")

    def read_float(self, address):
        return self.read(address, size=4, fmt="<f")

    def read_double(self, address):
        return self.read(address, size=8, fmt="<d")

    def read_z_bytes(self, address) -> bytes:
        """Read a null-terminated single-byte-character string, without decoding it."""
        raw_string = b""
        read_address = address
        while True:
            value = self.read(read_address, size=1)
            if value[0] == 0:
                # Null termination found.
                return raw_string
            raw_string += value
            read_address += 1

    def read_z_string(self, address, encoding: str) -> str:
        """Read a null-terminated single-byte-character string."""
        raw_string = b""
        read_address = address
        while True:
            value = self.read(read_address, size=1)
            if value[0] == 0:
                # Null termination found.
                return raw_string.decode(encoding)
            raw_string += value
            read_address += 1

    def read_utf16_z_string(self, address, big_endian=False) -> str:
        """Read a null-terminated UTF-16 string."""
        raw_string = b""
        read_address = address
        while True:
            value = self.read(read_address, size=2)
            if value[0] == 0 and value[1] == 0:
                # Null termination found.
                return raw_string.decode("utf-16-be" if big_endian else "utf-16-le")
            raw_string += value
            read_address += 2

    def write_int16(self, address, value):
        return self.write(address, data=(value,), fmt="<h")

    def write_int32(self, address, value):
        return self.write(address, data=(value,), fmt="<i")

    def write_int64(self, address, value):
        return self.write(address, data=(value,), fmt="<q")

    def write_uint16(self, address, value):
        return self.write(address, data=(value,), fmt="<H")

    def write_uint32(self, address, value):
        return self.write(address, data=(value,), fmt="<I")

    def write_uint64(self, address, value):
        return self.write(address, data=(value,), fmt="<Q")

    def write_float(self, address, value):
        return self.write(address, data=(value,), fmt="<f")

    def write_double(self, address, value):
        return self.write(address, data=(value,), fmt="<d")

    @abc.abstractmethod
    def get_event_flag_offset_mask(self, flag_id: int) -> tuple[int, int]:
        pass

    @memory_hook_validate
    def read_event_flag(self, flag_id: int) -> bool:
        _, _, mask, flags32 = self._get_address_offset_mask_flags32(flag_id)
        return flags32 & mask != 0

    @memory_hook_validate
    def write_event_flag(self, flag_id: int, state: bool):
        address, offset, mask, flags32 = self._get_address_offset_mask_flags32(flag_id)
        if state:
            flags32 |= mask
        else:
            flags32 &= ~mask
        self.write_uint32(address + offset, flags32)

    def _get_address_offset_mask_flags32(self, flag_id: int) -> tuple[int, int, int, int]:
        """Code common to read/write for event flags."""
        offset, mask = self.get_event_flag_offset_mask(flag_id)

        if not self.EVENT_FLAG_OFFSETS:
            raise ValueError(f"No `EVENT_FLAG_OFFSETS` defined for `{self.__class__.__name__}`.")
        address = self.EVENT_FLAG_OFFSETS[0]
        for jump in self.EVENT_FLAG_OFFSETS[1:]:
            address = self.read_int64(address + jump)
        return self.read_uint32(address + offset)

    @staticmethod
    def _rolling_window(a, size):
        """From https://stackoverflow.com/questions/7100242/python-numpy-first-occurrence-of-subarray."""
        if not numpy:
            raise ModuleNotFoundError("Cannot use `_rolling_window()` without `numpy` package.")
        shape = a.shape[:-1] + (a.shape[-1] - size + 1, size)
        strides = a.strides + (a.strides[-1],)
        return numpy.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

    @memory_hook_validate
    def scan(
        self,
        pointers: dict[str, bytes | BasePointerSearch],
        chunk_size=8192,
        prefer_numpy=False,  # TODO: numpy method is slower and more restrictive, even with chunk size 8192!
        use_regex=False,
        address_range: tuple[int, int] = None,
        ignore_repeats=False,
    ) -> tp.Union[int, None, dict[str, tp.Union[int, None]]]:
        """Scan process memory, `chunk_size` at a time, looking for all the pointer byte-strings specified in
        `pointers` dictionary.

        Returns a dictionary mapping pointer names to the address where `pointer.sequence` starts. If
        `pointer.address_func` is not `None`, the address will be fed through that function first. If the address is
        not found, the dictionary value will be `None`.
        """
        use_numpy = prefer_numpy and numpy
        pointer_int32_dict = {}
        if use_numpy:
            for pointer_name, pointer in pointers.items():
                if isinstance(pointer, BasePointerSearch):
                    sequence = pointer.sequence
                elif isinstance(pointer, bytes):
                    sequence = pointer
                else:
                    raise TypeError(f"Unsupported pointer type: {pointer}")
                if len(sequence) % 4:
                    raise ValueError(f"Pointer sequence length must be divisible by 4 (found length {len(sequence)}).")
                int32_count = len(sequence) // 4
                pointer_int32_dict[pointer_name] = struct.unpack("I" * int32_count, sequence)
            largest_sequence_size = max(len(p) for p in pointer_int32_dict.values())
            stride = 4 * (chunk_size - largest_sequence_size)
        else:
            largest_sequence_size = max(
                len(p.sequence if isinstance(p, BasePointerSearch) else p) for p in pointers.values()
            )
            stride = chunk_size - largest_sequence_size

        if largest_sequence_size >= chunk_size:
            raise ValueError("Chunk size must be larger than all sequences being searched.")

        if use_numpy:
            array = numpy.zeros(chunk_size, "l")
            buffer = None
        else:
            array = None
            # noinspection PyCallingNonCallable,PyTypeChecker
            buffer = (c.c_char * chunk_size)()

        bytes_read = SIZE_T()
        if address_range is None:
            search_from_address = self.BASE_ADDRESS
            max_address = 0x7FFFFFFF
        else:
            search_from_address, max_address = address_range
        found_pointers = {pointer_name: None for pointer_name in pointers}  # type: dict[str, int | None]
        while True:

            if max_address is not None and search_from_address > max_address:
                break  # not found

            try:
                result = kernel32.ReadProcessMemory(
                    self.p_handle,
                    search_from_address,
                    array.ctypes.data if use_numpy else buffer,
                    array.itemsize * array.size if use_numpy else chunk_size,
                    c.byref(bytes_read),
                )
                if not result:
                    raise WindowsError("`ReadProcessMemory` returned null.")
            except WindowsError as e:
                if search_from_address == self.BASE_ADDRESS:
                    _LOGGER.error(f"Could not read first {chunk_size} bytes of process {self.pid}.", exc_info=True)
                    raise MemoryHookCallError(e)
                elif "Invalid access to memory location" in str(e):
                    break  # return anything found already
                else:
                    # Ignore any other error and proceed to next chunk.
                    search_from_address += stride
                    continue
            else:
                if use_numpy:
                    for pointer_name, int32_sequence in pointer_int32_dict.items():
                        hits = numpy.all(self._rolling_window(array, len(int32_sequence)) == int32_sequence, axis=1)
                        if numpy.any(hits):

                            if not ignore_repeats and found_pointers[pointer_name] is not None:
                                raise MemoryHookCallError(f"Scan found multiple matches for pointer {pointer_name}.")

                            first_hit = numpy.argmax(hits)
                            address = search_from_address + 4 * first_hit
                            if address_func := pointers[pointer_name].address_func is not None:
                                found_pointers[pointer_name] = int(address_func(self, address))
                            else:
                                found_pointers[pointer_name] = int(address)
                else:
                    data = bytes(buffer[: bytes_read.value])
                    for pointer_name, pointer in pointers.items():
                        if isinstance(pointer, BasePointerSearch):
                            sequence = pointer.sequence
                            address_func = pointer.address_func
                        elif isinstance(pointer, bytes):
                            sequence = pointer
                            address_func = None
                        else:
                            raise TypeError(f"Unsupported pointer type: {pointer}")
                        address = None
                        if use_regex:
                            if match := re.search(sequence, data, re.DOTALL):
                                address = search_from_address + match.start()
                        else:
                            if (index := data.find(sequence)) != -1:
                                address = search_from_address + index
                        if address is not None:
                            if not ignore_repeats and found_pointers[pointer_name] is not None:
                                raise MemoryHookCallError(f"Scan found multiple matches for pointer {pointer_name}.")
                            if address_func is not None:
                                found_pointers[pointer_name] = address_func(self, address)
                            else:
                                found_pointers[pointer_name] = address

                if ignore_repeats and all(v is not None for v in found_pointers.values()):
                    break  # all pointers found and repeats ignored
                search_from_address += stride

        return found_pointers

    @memory_hook_validate
    def single_scan(
        self,
        pointer: bytes | BasePointerSearch,
        chunk_size=8192,
        prefer_numpy=False,  # TODO: numpy method is slower and more restrictive, even with chunk size 8192!
        use_regex=False,
        address_range: tuple[int, int] = None,
        ignore_repeats=False,
    ) -> int | None:
        scan_result = self.scan(
            pointers={"x": pointer},
            chunk_size=chunk_size,
            prefer_numpy=prefer_numpy,
            use_regex=use_regex,
            address_range=address_range,
            ignore_repeats=ignore_repeats,
        )
        return scan_result["x"]

    @memory_hook_validate
    def get(self, value_name):
        try:
            entry_data = self.value_table[value_name]
        except KeyError:
            raise KeyError(f"Invalid value table key: {value_name}")
        if entry_data.pointer not in self.base_pointer_table:
            raise MemoryHookCallError(
                f"Pointer {repr(entry_data.pointer)} for {repr(value_name)} has not been registered."
            )
        address = self.base_pointer_table[entry_data.pointer]
        address = self.read_int64(address)  # First jump has offset zero.
        if address == 0:
            raise MemoryHookCallError(
                f"Pointer {repr(entry_data.pointer)} for {repr(value_name)} is 0, which suggests it "
                f"has not been loaded in-game (are you only in the main menu?)."
            )
        for jump in entry_data.jumps[:-1]:
            try:
                address = self.read_int64(address + jump)
            except MemoryHookCallError as ex:
                MemoryHookCallError(f"Memory hook error encountered while reading field {value_name}: {ex}")
        # noinspection PyCallingNonCallable,PyTypeChecker
        buffer = (c.c_char * entry_data.size)()
        bytes_read = SIZE_T()
        try:
            kernel32.ReadProcessMemory(
                self.p_handle, address + entry_data.jumps[-1], buffer, entry_data.size, c.byref(bytes_read)
            )
        except WindowsError as e:
            _LOGGER.error(f"Error reading value {repr(value_name)} from game.", exc_info=True)
            raise MemoryHookCallError(e)
        values = struct.unpack(entry_data.fmt, bytearray(buffer[: bytes_read.value]))
        if len(values) == 1:
            return values[0]
        return values

    def try_hooked(self):
        if not self.process or not self.process.is_running():
            # Lost (or never found) process. Try to reconnect.
            return self.find_process()
        return True

    def _read_cached(self):
        """TODO: Ideally wouldn't be calling this (and the write) on frequent real-time calls."""
        _cache_path = APPDATA_PATH(self.ADDRESS_CACHE_NAME)
        try:
            self._address_cache = read_json(_cache_path)
        except (FileNotFoundError, EOFError, ValueError):
            self._address_cache = {}

    def _write_cached(self):
        _cache_path = APPDATA_PATH(self.ADDRESS_CACHE_NAME)
        try:
            write_json(_cache_path, self._address_cache)
        except (PermissionError, ValueError):
            _LOGGER.error(f"Could not write address cache for '{self.PROCESS_NAME}' hook to '{_cache_path}'.")
            _LOGGER.debug("This may be because the file is read-only or you do not have permission to write to it.")

    @property
    def pid(self):
        return self.process.pid if self.process is not None else -1

    @property
    def hooked(self) -> bool:
        return self.process and self.process.is_running()
