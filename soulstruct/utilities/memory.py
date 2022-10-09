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
import pickle
import re
import struct
import typing as tp

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.files import PACKAGE_PATH
from soulstruct.utilities.kernel32 import *

if tp.TYPE_CHECKING:
    from ctypes import wintypes as w

try:
    # noinspection PyPackageRequirements
    import numpy
except ImportError:
    numpy = None

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
    jumps: tp.Sequence[int, ...]
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
    """Updates cache from `__address_cache__` file before calling method, then writes latest `__address_cache__`."""

    @functools.wraps(method)
    def wrapped(*args, **kwargs):
        self = args[0]  # type: MemoryHook
        try:
            with PACKAGE_PATH("__address_cache__").open("rb") as f:
                self._address_cache = pickle.load(f)
        except (FileNotFoundError, EOFError, ValueError):
            self._address_cache = {}
        result = method(*args, **kwargs)
        with PACKAGE_PATH("__address_cache__").open("wb") as f:
            pickle.dump(self._address_cache, f)
        return result

    return wrapped


class MemoryHook(abc.ABC):
    """Hooks into running game and edits values at given memory addresses (like CheatEngine)."""

    PROCESS_NAME: str
    BASE_ADDRESS: int

    EVENT_FLAG_OFFSETS = ()  # base address and jump offsets for event flags (not including flag-specific offset)
    BASE_POINTER_TABLE: dict[str, tp.Union[int, BasePointerSearch]] = {}
    VALUE_TABLE: dict[str, MemoryValue] = {}

    MemoryHookCallError = MemoryHookCallError
    UnhookedError = UnhookedError

    class _ProcessStream(io.BufferedIOBase):

        def __init__(self, hook: MemoryHook, address: int, chunk_size: int = 1024, maximum_size: int = None):
            """Interface that mimics `io.BufferedIOBase` with data from a hooked memory process.

            Currently only implements `read(n)`.

            Args:
                hook (MemoryHook): hooked process to read from.
                address (int): initial address to read from.
                chunk_size (int): number of bytes to read at once.
                maximum_size (int): if given, raise an `IOError` if more than this many bytes are read.
            """
            self._hook = hook
            self._start_address = address
            self._current_address = address  # next process address to buffer data from
            self._stream_offset = 0  # relative to `self._start_address`
            self._chunk_size = chunk_size
            self._max_size = maximum_size
            self._bytes_read = 0
            self._buffer = b""

        # noinspection PyMethodOverriding
        def read(self, size: int) -> bytes:
            output = b""
            if self._max_size is not None and self._bytes_read + size > self._max_size:
                raise IOError(f"Tried to read more than specified maximum bytes ({self._max_size}) from process.")
            bytes_to_read = size

            while bytes_to_read > 0:
                if not self._buffer:
                    self._buffer = self._hook.read(self._current_address, self._chunk_size)
                    self._current_address += self._chunk_size  # address for next buffer read

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
            self._current_address = self._start_address + offset
            self._stream_offset = offset
            self._buffer = b""

    process: psutil.Process | None
    p_handle: w.HANDLE | None

    def __init__(self):

        if psutil is None:
            raise ModuleNotFoundError("`psutil` package required to use Soulstruct `MemoryHook`.")

        self.value_table = self.VALUE_TABLE
        self._address_cache = {}
        self.base_pointer_table = {}  # type: dict[str, int]  # named, resolved base pointer addresses

        self.process = None
        self.p_handle = None
        self.find_process()

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
        value = bytes(buffer[: bytes_read.value])
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

    def BufferedProcessMemory(self, address: int, chunk_size: int = 1024, maximum_size: int = None):
        return self._ProcessStream(self, address, chunk_size, maximum_size)

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
    def get_event_flag_offset_mask(self, flag_id: int):
        pass

    @memory_hook_validate
    def read_event_flag(self, flag_id: int) -> bool:
        offset, mask = self.get_event_flag_offset_mask(flag_id)

        if not self.EVENT_FLAG_OFFSETS:
            raise ValueError(f"No `EVENT_FLAG_OFFSETS` defined for `{self.__class__.__name__}`.")
        address = self.EVENT_FLAG_OFFSETS[0]
        for jump in self.EVENT_FLAG_OFFSETS[1:]:
            address = self.read_int64(address + jump)
        flags32 = self.read_uint32(address + offset)
        return flags32 & mask != 0

    @memory_hook_validate
    def write_event_flag(self, flag_id: int, state: bool):
        offset, mask = self.get_event_flag_offset_mask(flag_id)

        if not self.EVENT_FLAG_OFFSETS:
            raise ValueError(f"No `EVENT_FLAG_OFFSETS` defined for `{self.__class__.__name__}`.")
        address = self.EVENT_FLAG_OFFSETS[0]
        for jump in self.EVENT_FLAG_OFFSETS[1:]:
            address = self.read_int64(address + jump)
        flags32 = self.read_uint32(address + offset)
        if state:
            flags32 |= mask
        else:
            flags32 &= ~mask
        self.write_uint32(address + offset, flags32)

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
            buffer = (c.c_char * chunk_size)()

        bytes_read = SIZE_T()
        if address_range is None:
            search_from_address = self.BASE_ADDRESS
            max_address = 0x7FFFFFFF
        else:
            search_from_address, max_address = address_range
        found_pointers = {pointer_name: None for pointer_name in pointers}
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

    @property
    def pid(self):
        return self.process.pid if self.process is not None else -1

    @property
    def hooked(self) -> bool:
        return self.process and self.process.is_running()
