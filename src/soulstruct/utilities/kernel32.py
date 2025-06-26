
__all__ = [
    "kernel32", "PROCESS_VM_READ", "PROCESS_VM_WRITE", "PROCESS_VM_OPERATION", "PROCESS_ALL_ACCESS", "SIZE_T", "PSIZE_T"
]

import ctypes as c
from ctypes import wintypes as w


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
