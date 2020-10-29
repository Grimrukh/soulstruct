"""
autoAssemble([[
aobscanmodule(findit6,DarkSoulsRemastered.exe,4C 8B 05 ? ? ? ? 48 63 C9 48 8D 04 C9 41 3B 54 C0 10)
registersymbol(findit6)
]])
local addr = getAddress("findit6")
addr = addr + readInteger(addr + 3) + 7
unregisterSymbol("Param")
registerSymbol("Param", addr, true)

autoAssemble([[
aobscanmodule(findit8,DarkSoulsRemastered.exe,48 8B 05 ? ? ? ? 44 38 80 ? ? ? ? ? ? 44 38 41 49 0F 84 ? ? ? ? 66 0F 6E 41 38 48 8B 41 10 0F 28 0D ? ? ? ? 48 89 BC 24 ? ? ? ? 0F 5B C0 4C 89 A4 24)
registersymbol(findit8)
]])
local addr = getAddress("findit8")
addr = addr + readInteger(addr + 3) + 7
unregisterSymbol("DbgEventBase")
registerSymbol("DbgEventBase", addr, true)

autoAssemble([[
aobscanmodule(findit9,DarkSoulsRemastered.exe,48 8B 05 ? ? ? ? 48 8B 40 08 48 8B 40 38 0F B7 50 0A 3B CA ? ? 8B C9 48 83 C1 04 48 8D 0C 49 8B 04 88)
registersymbol(findit9)
]])
local addr = getAddress("findit9")
addr = addr + readInteger(addr + 3) + 7
unregisterSymbol("ThrowParam")
registerSymbol("ThrowParam", addr, true)

autoAssemble([[
aobscanmodule(findit10,DarkSoulsRemastered.exe,48 8B 0D ? ? ? ? E8 ? ? ? ? 48 8B 4E 68)
registersymbol(findit10)
]])
local addr = getAddress("findit10")
addr = addr + readInteger(addr + 3) + 7
unregisterSymbol("ChrFollowCam")
registerSymbol("ChrFollowCam", addr, true)

autoAssemble([[
aobscanmodule(findit11,DarkSoulsRemastered.exe,48 8B 1D ? ? ? ? 48 8D 94 24 ? ? ? ? 4C 8B F1 0F 29 7C 24 40)
registersymbol(findit11)
]])
local addr = getAddress("findit11")
addr = addr + readInteger(addr + 3) + 7
unregisterSymbol("FRPGNETBase")
registerSymbol("FRPGNETBase", addr, true)

autoAssemble([[
aobscanmodule(findit13,DarkSoulsRemastered.exe,48 89 05 ? ? ? ? 48 83 3D ? ? ? ? 00 ? ? 4C 8B 05 ? ? ? ? 4C 89 44 24 48 BA 08 00 00 00 B9 58 60 00 00)
registersymbol(findit13)
]])
local addr = getAddress("findit13")
addr = addr + readInteger(addr + 3) + 7
unregisterSymbol("NetworkProp")
registerSymbol("NetworkProp", addr, true)

"""
import ctypes as c
import logging
import re
import struct
import typing as tp
from collections import namedtuple
from ctypes import wintypes as w

from soulstruct.core import SoulstructError

try:
    import psutil
except ImportError:
    psutil = None

_LOGGER = logging.getLogger(__name__)
__all__ = ["MemoryHook", "MemoryHookError", "DSRMemoryHook"]

kernel32 = c.WinDLL("kernel32", use_last_error=True)
ERROR_PARTIAL_COPY = 0x012B
PROCESS_VM_READ = 0x0010
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
kernel32.ReadProcessMemory.argtypes = (
    w.HANDLE,  # _In_  hProcess
    w.LPCVOID,  # _In_  lpBaseAddress
    w.LPVOID,  # _Out_ lpBuffer
    SIZE_T,  # _In_  nSize
    PSIZE_T,  # _Out_ lpNumberOfBytesRead
)

kernel32.CloseHandle.argtypes = (w.HANDLE,)


MemoryPointer = namedtuple("MemoryPointer", ("sequence", "address_func"))
MemoryValue = namedtuple("CheatEntry", ("pointer", "jumps", "size", "fmt"))


DSR_POINTER_TABLE = {
    "WORLD_CHR_BASE": 0x141d151b0,  # Scanning just takes too long.
    # "WORLD_CHR_BASE": MemoryPointer(
    #     br"\x48\x8B\x05....\x48\x8B\x48\x68\x48\x85\xC9\x0F\x84....\x48\x39\x5e\x10\x0F\x84....\x48",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    "DISPLAY_GROUP_BASE": 0x141D1E500,  # This is a pointer base I discovered, so I don't know what to call it.
    # "CHR_CLASS_BASE": MemoryPointer(
    #     br"\x48\x8B\x05....\x48\x85\xC0..\xF3\x0F\x58\x80\xAC\x00\x00\x00",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "CHR_CLASS_WARP": MemoryPointer(
    #     br"\x48\x8B\x05....\x66\x0F\x7F\x80\xA0\x0B\x00\x00\x0F\x28\x02\x66\x0F\x7F\x80\xB0\x0B\x00\x00\xC6\x80",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "CAM_MAN_BASE": MemoryPointer(
    #     br"\x48\x8B\x05....\x48\x63\xD1\x48\x8B\x44\xD0\x08\xC3",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "LOCK_TGT_BASE": MemoryPointer(
    #     br"\x48\x8B\x0D....\x89\x99....\x4C\x89\x6D\x58",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "MENU_MAN_BASE": MemoryPointer(
    #     br"\x48\x8B\x05....\x89\x88\x28\x08\x00\x00\x85\xC9",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "WORLD_CHR_DBG_BASE": MemoryPointer(
    #     br"\x48\x8B\x05....\x48\x8B\x80\xF0\x00\x00\x00\x48\x85\xC0",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
    # "WORLD_CHR_BASE_P": MemoryPointer(
    #     br"\x48\x89\x05....\x48\x89\x5C\x24\x38\x48\x85\xDB..\x48\x8B\x03",
    #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
}


DSR_VALUE_TABLE = {
    "player_angle": MemoryValue("WORLD_CHR_BASE", (0x68, 0x68, 0x28, 0x4), 4, "<f"),
    "player_x": MemoryValue("WORLD_CHR_BASE", (0x68, 0x68, 0x28, 0x10), 4, "<f"),
    "player_y": MemoryValue("WORLD_CHR_BASE", (0x68, 0x68, 0x28, 0x14), 4, "<f"),
    "player_z": MemoryValue("WORLD_CHR_BASE", (0x68, 0x68, 0x28, 0x18), 4, "<f"),
    "active_display_groups": MemoryValue("DISPLAY_GROUP_BASE", (0x178, 0xC0, 0x8, 0x348, 0x88, 0x40, 0x10, 0xA8),
                                         16, "<IIII"),
    # "stable_angle": MemoryValue("CHR_CLASS_WARP", 0xBB4, 4, "<f"),
    # "stable_x": MemoryValue("CHR_CLASS_WARP", 0xBA0, 4, "<f"),
    # "stable_y": MemoryValue("CHR_CLASS_WARP", 0xBA4, 4, "<f"),
    # "stable_z": MemoryValue("CHR_CLASS_WARP", 0xBA8, 4, "<f"),
}


class MemoryHook:
    """Hooks into running game and edits values at given memory addresses (a la CheatEngine)."""

    BASE_ADDRESS = 0x400000  # memory of process starts here

    def __init__(self, game_pid, pointer_table, value_table):
        self.pid = game_pid
        self.pointer_table = pointer_table  # type: tp.Dict[str, MemoryPointer]
        self.pointers = {}  # dynamic addresses
        self.value_table = value_table  # type: tp.Dict[str, MemoryValue]
        self.process_handle = kernel32.OpenProcess(PROCESS_VM_READ, False, self.pid)

        self._load_pointer_table()

    def __del__(self):
        kernel32.CloseHandle(self.process_handle)

    def _load_pointer_table(self):
        for pointer_name, pointer_data in self.pointer_table.items():
            _LOGGER.info(f"Scanning game memory for {pointer_name}...")
            if isinstance(pointer_data, MemoryPointer):
                pointer_address = self.scan(pointer_data.sequence)
                if pointer_address is None:
                    raise MemoryHookError(f"Could not locate memory pointer: {pointer_name}")
                self.pointers[pointer_name] = pointer_data.address_func(self, pointer_address)
            elif isinstance(pointer_data, int):
                self.pointers[pointer_name] = pointer_data
            else:
                raise TypeError(f"Pointer value must be a `MemoryPointer` or raw int address.")

    def _read(self, address, size, fmt=""):
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

    def read_int32(self, address):
        return self._read(address, size=4, fmt="<i")

    def read_int64(self, address):
        return self._read(address, size=8, fmt="<q")

    def read_float(self, address):
        return self._read(address, size=4, fmt="<f")

    def read_double(self, address):
        return self._read(address, size=8, fmt="<d")

    def scan(self, byte_sequence: bytes, chunk_size=10000):
        """Find a given byte sequence in process memory (looking in the first `search_size` bytes)."""
        if len(byte_sequence) >= chunk_size:
            raise ValueError("Chunk size must be larger than byte sequence being searched.")
        buffer = (c.c_char * chunk_size)()
        bytes_read = SIZE_T()
        search_from_address = self.BASE_ADDRESS
        i = 0
        while 1:
            try:
                i += 1
                kernel32.ReadProcessMemory(
                    self.process_handle, search_from_address, buffer, chunk_size, c.byref(bytes_read)
                )
            except WindowsError as e:
                if search_from_address == self.BASE_ADDRESS:
                    _LOGGER.error(f"Could not read first {chunk_size} bytes of process {self.pid}.", exc_info=True)
                    raise MemoryHookError(e)
                elif "Invalid access to memory location" in str(e):
                    return None
                else:
                    # Ignore error.
                    search_from_address += chunk_size - len(byte_sequence)
                    continue
            else:
                data = bytes(buffer[: bytes_read.value])
                match = re.search(byte_sequence, data, re.DOTALL)
                if match:
                    address = search_from_address + match.start()
                    return address
                search_from_address += chunk_size - len(byte_sequence)  # prevents byte sequence from being truncated

    def get(self, value_name):
        try:
            entry_data = self.value_table[value_name]
        except KeyError:
            raise KeyError(f"Invalid value table key: {value_name}")
        if entry_data.pointer not in self.pointers:
            raise MemoryHookError(f"Pointer {repr(entry_data.pointer)} for {repr(value_name)} has not been registered.")
        address = self.pointers[entry_data.pointer]
        address = self.read_int64(address)  # First jump has offset zero.
        if address == 0:
            raise MemoryHookError(
                f"Pointer {repr(entry_data.pointer)} for {repr(value_name)} is 0, which suggests it "
                f"has not been loaded in-game (are you only in the main menu?)."
            )
        for jump in entry_data.jumps[:-1]:
            address = self.read_int64(address + jump)
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

        super().__init__(dsr_pid, DSR_POINTER_TABLE, DSR_VALUE_TABLE)


def test_dsr_hook():
    hook = DSRMemoryHook()
    for pointer_base, pointer_value in hook.pointers.items():
        print(f"{pointer_base}: {hex(pointer_value)}")
    print(hook.get("player_angle"))
    print(hook.get("player_x"))
    print(hook.get("player_y"))
    print(hook.get("player_z"))
    print(hook.get("active_display_groups"))


if __name__ == '__main__':
    test_dsr_hook()
