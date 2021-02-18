from __future__ import annotations

__all__ = ["MemoryHook", "DSRMemoryHook"]

import ctypes as c
import io
import logging
import pickle
import re
import struct
import typing as tp
from ctypes import wintypes as w

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities import PACKAGE_PATH

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.params.draw_param import DrawParam

try:
    import numpy
except ImportError:
    numpy = None

try:
    import psutil
except ImportError:
    psutil = None

_LOGGER = logging.getLogger(__name__)
__all__ = ["MemoryHook", "MemoryHookError", "DSRMemoryHook"]

kernel32 = c.WinDLL("kernel32", use_last_error=True)
ERROR_PARTIAL_COPY = 0x012B
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
PROCESS_VM_OPERATION = 0x0008
PROCESS_ALL_ACCESS = 0x1F0FFF
SIZE_T = c.c_size_t
PSIZE_T = c.POINTER(SIZE_T)


def _check_zero(result, _, args):  # second arg is `func` (unused here)
    if not result:
        raise c.WinError(c.get_last_error())
    return args


kernel32.OpenProcess.errcheck = _check_zero
kernel32.OpenProcess.restype = w.HANDLE
kernel32.OpenProcess.argtypes = (
    w.DWORD,  # _In_ dwDesiredAccess
    w.BOOL,  # _In_ bInheritHandle
    w.DWORD,  # _In_ dwProcessId
)

kernel32.ReadProcessMemory.errcheck = _check_zero
kernel32.ReadProcessMemory.restype = bool
kernel32.ReadProcessMemory.argtypes = (
    w.HANDLE,  # _In_  hProcess
    w.LPCVOID,  # _In_  lpBaseAddress
    w.LPVOID,  # _Out_ lpBuffer
    SIZE_T,  # _In_  nSize
    PSIZE_T,  # _Out_ lpNumberOfBytesRead
)

kernel32.WriteProcessMemory.errcheck = _check_zero
kernel32.WriteProcessMemory.restype = bool
kernel32.WriteProcessMemory.argtypes = (
    w.HANDLE,  # _In_  hProcess
    w.LPCVOID,  # _In_ lpBaseAddress
    w.LPVOID,  # _In_ lpBuffer
    SIZE_T,  # _In_  nSize
    c.POINTER(SIZE_T),  # _Out_ lpNumberOfBytesWritten
)

kernel32.CloseHandle.argtypes = (w.HANDLE,)


class BasePointerSearch(tp.NamedTuple):
    sequence: bytes
    address_func: tp.Optional[tp.Callable[[MemoryHook, int], int]] = None


class MemoryValue(tp.NamedTuple):
    pointer: str
    jumps: tp.Sequence[int, ...]
    size: int
    fmt: str


# Scanning just takes too long, so useful bases have their addresses hard-coded.
DSR_BASE_POINTER_TABLE = {
    # "WORLD_CHR_BASE": BasePointerSearch(
    #     br"\x48\x8B\x05....\x48\x8B\x48\x68\x48\x85\xC9\x0F\x84....\x48\x39\x5e\x10\x0F\x84....\x48",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    "WORLD_CHR_BASE": 0x141D151B0,
    # "CHR_CLASS_BASE": BasePointerSearch(
    #     br"\x48\x8B\x05....\x48\x85\xC0..\xF3\x0F\x58\x80\xAC\x00\x00\x00",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "CHR_CLASS_WARP": BasePointerSearch(
    #     br"\x48\x8B\x05....\x66\x0F\x7F\x80\xA0\x0B\x00\x00\x0F\x28\x02\x66\x0F\x7F\x80\xB0\x0B\x00\x00\xC6\x80",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "CAM_MAN_BASE": BasePointerSearch(
    #     br"\x48\x8B\x05....\x48\x63\xD1\x48\x8B\x44\xD0\x08\xC3",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "CHR_FOLLOW_CAM": BasePointerSearch(
    #     br"\x48\x8B\x0D....\xE8....\x48\x8B\x4E\x68",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "LOCK_TGT_BASE": BasePointerSearch(
    #     br"\x48\x8B\x0D....\x89\x99....\x4C\x89\x6D\x58",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "MENU_MAN_BASE": BasePointerSearch(
    #     br"\x48\x8B\x05....\x89\x88\x28\x08\x00\x00\x85\xC9",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "WORLD_CHR_DBG_BASE": BasePointerSearch(
    #     br"\x48\x8B\x05....\x48\x8B\x80\xF0\x00\x00\x00\x48\x85\xC0",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "PARAM": BasePointerSearch(
    #     br"\x4C\x8B\x05....\x48\x63\xC9\x48\x8D\x04\xC9\x41\x3B\x54\xC0\x10",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "THROW_PARAM": BasePointerSearch(
    #     br"\x48\x8B\x05....\x48\x8B\x40\x08\x48\x8B\x40\x38\x0F\xB7\x50\x0A\x3B\xCA..\x8B\xC9\x48\x83\xC1\x04\x48\x8D"
    #     br"\x0C\x49\x8B\x04\x88",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "DBG_EVENT_BASE": BasePointerSearch(
    #     br"\x48\x8B\x05....\x44\x38\x80......\x44\x38\x41\x49\x0F\x84....\x66\x0F\x6E\x41\x38\x48\x8B\x41\x10\x0F\x28"
    #     br"\x0D....\x48\x89\xBC\x24....\x0F\x5B\xC0\x4C\x89\xA4\x24",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "FRPG_NET_BASE": BasePointerSearch(
    #     br"\x48\x8B\x1D....\x48\x8D\x94\x24....\x4C\x8B\xF1\x0F\x29\x7C\x24\x40",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "NETWORK_PROP": BasePointerSearch(
    #     br"\x48\x89\x05....\x48\x83\x3D....\x00..\x4C\x8B\x05....\x4C\x89\x44\x24\x48\xBA\x08\x00\x00\x00\xB9\x58\x60"
    #     br"\x00\x00",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "WORLD_CHR_BASE_P": BasePointerSearch(
    #     br"\x48\x89\x05....\x48\x89\x5C\x24\x38\x48\x85\xDB..\x48\x8B\x03",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "WORLD_CHR_BASE_P": 0x141acd758,
}

_PLAYER_TRANSFORM_PTRS = (0x68, 0x68, 0x28)  # WORLD_CHR_BASE
_DISPLAY_GROUP_PTRS = (0x20, 0x58, 0x498, 0x58, 0x2C0, 0x4E8)  # WORLD_CHR_BASE
_DISP_GROUP_DEBUG_PTRS = (0x4C0, 0x68, 0xA8)

DSR_VALUE_TABLE = {
    "player_angle": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x4,), 4, "<f"),
    "player_x": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x10,), 4, "<f"),
    "player_y": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x14,), 4, "<f"),
    "player_z": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x18,), 4, "<f"),
    "m10_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x850,), 16, "<IIII"),
    "m10_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0xAC0,), 16, "<IIII"),
    "m10_02_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0xD30,), 16, "<IIII"),
    "m11_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0xFA0,), 16, "<IIII"),
    "m12_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1210,), 16, "<IIII"),
    "m12_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1480,), 16, "<IIII"),
    "m13_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x16F0,), 16, "<IIII"),
    "m13_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1960,), 16, "<IIII"),
    "m13_02_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1BD0,), 16, "<IIII"),
    "m14_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1E40,), 16, "<IIII"),
    "m14_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x20B0,), 16, "<IIII"),
    "m15_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2320,), 16, "<IIII"),
    "m15_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2590,), 16, "<IIII"),
    "m16_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2800,), 16, "<IIII"),
    "m17_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2A70,), 16, "<IIII"),
    "m18_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2CE0,), 16, "<IIII"),
    "m18_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2F50,), 16, "<IIII"),
    # "stable_angle": MemoryValue("CHR_CLASS_WARP", (0xBB4,), 4, "<f"),
    # "stable_x": MemoryValue("CHR_CLASS_WARP", (0xBA0,), 4, "<f"),
    # "stable_y": MemoryValue("CHR_CLASS_WARP", (0xBA4,), 4, "<f"),
    # "stable_z": MemoryValue("CHR_CLASS_WARP", (0xBA8,), 4, "<f"),
}


class MemoryHook:
    """Hooks into running game and edits values at given memory addresses (a la CheatEngine)."""

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

    BasePointerSearch = BasePointerSearch
    MemoryValue = MemoryValue
    BASE_ADDRESS = 0x400000  # memory of process starts here

    def __init__(self, game_pid, base_pointer_table: dict[str, tp.Union[int, BasePointerSearch]], value_table):
        self.pid = game_pid
        self.base_pointer_table = {}  # type: dict[str, int]  # named, resolved base pointer addresses
        self.value_table = value_table  # type: dict[str, MemoryValue]
        self.process_handle = kernel32.OpenProcess(
            PROCESS_VM_READ + PROCESS_VM_WRITE + PROCESS_VM_OPERATION, False, self.pid
        )

        self._load_pointer_table(base_pointer_table)

    def __del__(self):
        try:
            kernel32.CloseHandle(self.process_handle)
        except AttributeError:
            pass

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
            pointer_addresses = self.scan(pointers_to_find)
            for pointer_name, address in pointer_addresses.items():
                if address is None:
                    raise MemoryHookError(f"Could not locate memory pointer: {pointer_name}")
                self.base_pointer_table[pointer_name] = address

    def read(self, address, size, fmt=""):
        buffer = (c.c_char * size)()
        bytes_read = SIZE_T()
        try:
            kernel32.ReadProcessMemory(self.process_handle, address, buffer, size, c.byref(bytes_read))
        except WindowsError as e:
            raise MemoryHookError(e)
        value = bytes(buffer[: bytes_read.value])
        if fmt:
            values = struct.unpack(fmt, value)
            if len(values) == 1:
                return values[0]
            return values
        return value

    def write(self, address, data, fmt=""):
        if fmt:
            data = struct.pack(fmt, *data)
        elif not isinstance(data, bytes):
            raise TypeError("Data to write to memory must be `bytes`, or 'fmt' must be given to convert a sequence.")
        size = len(data)
        buffer = c.create_string_buffer(data)
        bytes_written = SIZE_T(0)
        try:
            kernel32.WriteProcessMemory(self.process_handle, address, buffer, size, c.byref(bytes_written))
        except WindowsError as e:
            raise MemoryHookError(e)

    def BufferedProcessMemory(self, address: int, chunk_size: int = 1024, maximum_size: int = None):
        return self._ProcessStream(self, address, chunk_size, maximum_size)

    def read_int16(self, address):
        return self.read(address, size=2, fmt="<h")

    def read_int32(self, address):
        return self.read(address, size=4, fmt="<i")

    def read_int64(self, address):
        return self.read(address, size=8, fmt="<q")

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

    def write_float(self, address, value):
        return self.write(address, data=(value,), fmt="<f")

    def write_double(self, address, value):
        return self.write(address, data=(value,), fmt="<d")

    @staticmethod
    def _rolling_window(a, size):
        """From https://stackoverflow.com/questions/7100242/python-numpy-first-occurrence-of-subarray."""
        if not numpy:
            raise ModuleNotFoundError("Cannot use `_rolling_window()` without `numpy` package.")
        shape = a.shape[:-1] + (a.shape[-1] - size + 1, size)
        strides = a.strides + (a.strides[-1],)
        return numpy.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

    def scan(
        self,
        pointer_dict: tp.Union[BasePointerSearch, dict[str, BasePointerSearch]],
        chunk_size=8192,
        prefer_numpy=False,  # TODO: numpy method is slower and more restrictive, even with chunk size 8192!
        use_regex=False,
        max_address=None,
        ignore_repeats=False,
    ) -> tp.Union[int, None, dict[str, tp.Union[int, None]]]:
        """Scan process memory, `chunk_size` at a time, looking for all the pointer byte-strings specified in
        `pointer_dict`.

        Returns a dictionary mapping pointer names to the address where `pointer.sequence` starts. If
        `pointer.address_func` is not `None`, the address will be fed through that function first. If the address is
        not found, the dictionary value will be `None`.
        """
        if isinstance(pointer_dict, BasePointerSearch):
            return self.scan({"x": pointer_dict}, chunk_size, prefer_numpy, use_regex, max_address, ignore_repeats)["x"]

        use_numpy = prefer_numpy and numpy
        pointer_int32_dict = {}
        if use_numpy:
            for pointer_name, pointer in pointer_dict.items():
                if len(pointer.sequence) % 4:
                    raise ValueError(
                        f"`BasePointerSearch.sequence` must have a length divisible by 4 "
                        f"(found length {len(pointer.sequence)})."
                    )
                int32_count = len(pointer.sequence) // 4
                pointer_int32_dict[pointer_name] = struct.unpack("I" * int32_count, pointer.sequence)
            largest_sequence_size = max(len(p) for p in pointer_int32_dict.values())
            stride = 4 * (chunk_size - largest_sequence_size)
        else:
            largest_sequence_size = max(len(p.sequence) for p in pointer_dict.values())
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
        search_from_address = self.BASE_ADDRESS
        found_pointers = {pointer_name: None for pointer_name in pointer_dict}
        while 1:

            if max_address is not None and search_from_address > max_address:
                break  # not found

            try:
                result = kernel32.ReadProcessMemory(
                    self.process_handle,
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
                    raise MemoryHookError(e)
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
                                raise MemoryHookError(f"Scan found multiple matches for pointer {pointer_name}.")

                            first_hit = numpy.argmax(hits)
                            address = search_from_address + 4 * first_hit
                            if address_func := pointer_dict[pointer_name].address_func is not None:
                                found_pointers[pointer_name] = int(address_func(self, address))
                            else:
                                found_pointers[pointer_name] = int(address)
                else:
                    data = bytes(buffer[: bytes_read.value])
                    for pointer_name, pointer in pointer_dict.items():
                        address = None
                        if use_regex:
                            if match := re.search(pointer.sequence, data, re.DOTALL):
                                address = search_from_address + match.start()
                        else:
                            if (index := data.find(pointer.sequence)) != -1:
                                address = search_from_address + index
                        if address is not None:
                            if not ignore_repeats and found_pointers[pointer_name] is not None:
                                raise MemoryHookError(f"Scan found multiple matches for pointer {pointer_name}.")

                            if address_func := pointer.address_func is not None:
                                found_pointers[pointer_name] = address_func(self, address)
                            else:
                                found_pointers[pointer_name] = address

                if ignore_repeats and all(v is not None for v in found_pointers.values()):
                    break  # all pointers found and repeats ignored
                search_from_address += stride

        return found_pointers

    def get(self, value_name):
        try:
            entry_data = self.value_table[value_name]
        except KeyError:
            raise KeyError(f"Invalid value table key: {value_name}")
        if entry_data.pointer not in self.base_pointer_table:
            raise MemoryHookError(f"Pointer {repr(entry_data.pointer)} for {repr(value_name)} has not been registered.")
        address = self.base_pointer_table[entry_data.pointer]
        address = self.read_int64(address)  # First jump has offset zero.
        if address == 0:
            raise MemoryHookError(
                f"Pointer {repr(entry_data.pointer)} for {repr(value_name)} is 0, which suggests it "
                f"has not been loaded in-game (are you only in the main menu?)."
            )
        for jump in entry_data.jumps[:-1]:
            try:
                address = self.read_int64(address + jump)
            except MemoryHookError as ex:
                MemoryHookError(f"Memory hook error encountered while reading field {value_name}: {ex}")
        buffer = (c.c_char * entry_data.size)()
        bytes_read = SIZE_T()
        try:
            kernel32.ReadProcessMemory(
                self.process_handle, address + entry_data.jumps[-1], buffer, entry_data.size, c.byref(bytes_read)
            )
        except WindowsError as e:
            _LOGGER.error(f"Error reading value {repr(value_name)} from game.", exc_info=True)
            raise MemoryHookError(e)
        values = struct.unpack(entry_data.fmt, bytearray(buffer[: bytes_read.value]))
        if len(values) == 1:
            return values[0]
        return values


class MemoryHookError(SoulstructError):
    pass


class DSRMemoryHook(MemoryHook):

    _DRAW_PARAM_MARKER = b"\xb8\xdf\x36\x41\x01\x00\x00\x00"

    try:
        with PACKAGE_PATH("__ds1r_cache__").open("rb") as f_:
            _CACHED_DRAW_PARAM_ADDRESSES = pickle.load(f_)  # type: dict
    except (FileNotFoundError, EOFError, ValueError):
        _CACHED_DRAW_PARAM_ADDRESSES = {}  # cached addresses of UTF-16 strings

    def __init__(self, dsr_pid=None):
        if dsr_pid is None:
            if psutil is None:
                raise ModuleNotFoundError("`psutil` required for determining DSR PID.")
            for p in psutil.process_iter():
                if p.name() == "DarkSoulsRemastered.exe":
                    dsr_pid = p.pid
            if dsr_pid is None:
                raise RuntimeError("Could not find `DarkSoulsRemastered.exe` process.")
            print(f"Found Dark Souls Remastered process ID: {dsr_pid}")

        super().__init__(dsr_pid, DSR_BASE_POINTER_TABLE, DSR_VALUE_TABLE)

    def write_draw_param_to_memory(self, draw_param: DrawParam, area_id: int, slot=0):
        """Write the given `draw_param` for area `area_id` and slot `slot` to game memory.

        You MUST NOT change the number of rows in the `DrawParam` since the last time the game was loaded, as the size
        of the binary `DrawParam` data must stay the same. This method will check the DrawParam header to try to
        prevent this, as otherwise the game will definitely crash from invalid memory.
        """
        if slot not in {0, 1}:
            raise ValueError(f"Slot must be 0 or 1, not {slot}.")
        if not draw_param.param_info:
            raise ValueError(f"Cannot write to game memory for DrawParam type '{draw_param.param_type}'.")
        nickname = draw_param.param_info["nickname"]

        param_string = f"m{area_id}_{'1_' if slot == 1 else ''}{draw_param.param_info['file_name']}"
        param_string_bytes = param_string.encode("utf-16-le")

        new_binary = draw_param.pack(sort=False)

        data_address = -1
        existing_header = b""
        if (cached_address := self._CACHED_DRAW_PARAM_ADDRESSES.get((nickname, area_id, slot), -1)) != -1:
            # Try cached address first.
            existing_header = self.read(cached_address, 44)
            if existing_header[12:] == new_binary[12:44]:
                data_address = cached_address
        if data_address == -1:
            param_string_search = BasePointerSearch(param_string_bytes)
            param_string_address = self.scan(param_string_search, max_address=0x40000000)
            if param_string_address is None:
                raise MemoryError(f"Could not find memory address of DrawParam '{nickname}' in game memory.")
            string_offset_search = BasePointerSearch(self._DRAW_PARAM_MARKER + struct.pack("Q", param_string_address))
            string_offset_address = self.scan(string_offset_search, max_address=0x40000000)
            data_address = self.read(string_offset_address + 56, 8, "q")
            self._CACHED_DRAW_PARAM_ADDRESSES[nickname, area_id, slot] = data_address
            # print(hex(param_string_address), hex(string_offset_address), hex(data_address))
            existing_header = self.read(data_address, 44)  # up to end of param name (32j)

        if existing_header != new_binary[:44]:
            raise ValueError(
                f"Start of new DrawParam header does not match start of existing DrawParam header:\n"
                f"  New: {new_binary[:44]}\n"
                f"  Old: {existing_header}"
            )
        self.write(data_address, new_binary)

        with PACKAGE_PATH("__ds1r_cache__").open("wb") as f:
            pickle.dump(self._CACHED_DRAW_PARAM_ADDRESSES, f)


def test_dsr_hook():
    hook = DSRMemoryHook()
    print("Base pointers:")
    for pointer_base, pointer_value in hook.base_pointer_table.items():
        print(f"  {pointer_base}: {hex(pointer_value)}")
    print("Current values:")
    for field in DSR_VALUE_TABLE:
        try:
            print(f"  {field} = {hook.get(field)}")
        except MemoryHookError:
            pass


if __name__ == '__main__':
    test_dsr_hook()
