"""Python wrapper for `oo2core_6_win64.dll`, which is used for (de)compression in Sekiro and Elden Ring.

Soulstruct will automatically search for this DLL in its own path (Python package or executable) and the Sekiro and
Elden Ring paths specified in `config`. Use `SET_DLL_PATH(path)` if you want to set it yourself.

Adapted from `SoulsFormats` by TKGP:
    https://github.com/JKAnderson/SoulsFormats/blob/master/SoulsFormats/Util/Oodle26.cs
"""
from __future__ import annotations

__all__ = [
    "MissingOodleDLLError",
    "OodleDLLError",
    "compress",
    "decompress",
    "LOAD_DLL",
]

import ctypes as c
import logging
import typing as tp
from enum import IntEnum
from functools import wraps
from pathlib import Path

from soulstruct.config import SEKIRO_PATH, ELDEN_RING_PATH
from soulstruct.utilities.files import PACKAGE_PATH


_LOGGER = logging.getLogger(__name__)


__DLL_NAME = "oo2core_6_win64.dll"
__DLL = None  # type: tp.Optional[c.WinDLL]


__DLL_Compress = None  # type: tp.Optional[tp.Callable]
__DLL_Decompress = None  # type: tp.Optional[tp.Callable]
__DLL_GetCompressedBufferSizeNeeded = None  # type: tp.Optional[tp.Callable]
__DLL_CompressOptions_GetDefault = None  # type: tp.Optional[tp.Callable]
__DLL_GetDecodeBufferSize = None  # type: tp.Optional[tp.Callable]


class MissingOodleDLLError(Exception):
    """Exception raised if the Oodle DLL cannot be found or loaded."""
    pass


class OodleDLLError(Exception):
    """Exception raised if you try to call an Oodle function in this module without the DLL being loaded."""
    pass


# region Enums
class CtypesEnum(IntEnum):
    """A ctypes-compatible IntEnum superclass."""
    @classmethod
    def from_param(cls, obj):
        return int(obj)


class CheckCRC(CtypesEnum):
    No = 0
    Yes = 1
    Force32 = 0x40000000


class CompressionLevel(CtypesEnum):
    Null = 0
    SuperFast = 1
    VeryFast = 2
    Fast = 3
    Normal = 4

    Optimal1 = 5
    Optimal2 = 6
    Optimal3 = 7
    Optimal4 = 8
    Optimal5 = 9

    HyperFast1 = -1
    HyperFast2 = -2
    HyperFast3 = -3
    HyperFast4 = -4

    HyperFast = HyperFast1
    Optimal = Optimal2
    Max = Optimal5
    Min = HyperFast4

    Force32 = 0x40000000
    Invalid = Force32


class Compressor(CtypesEnum):
    Invalid = -1
    Null = 3

    Kraken = 8
    Leviathan = 13
    Mermaid = 9
    Selkie = 11
    Hydra = 12

    BitKnit = 10
    LZB16 = 4
    LZNA = 7
    LZH = 0
    LZHLW = 1
    LZNIB = 2
    LZBLW = 5
    LZA = 6

    Count = 14
    Force32 = 0x40000000


class DecodeThreadPhase(CtypesEnum):
    ThreadPhase1 = 1
    ThreadPhase2 = 2
    ThreadPhaseAll = 3
    Unthreaded = ThreadPhaseAll


class FuzzSafe(CtypesEnum):
    No = 0
    Yes = 1


class Profile(CtypesEnum):
    Main = 0
    Reduced = 1
    Force32 = 0x40000000


class Verbosity(CtypesEnum):
    Null = 0
    Minimal = 1
    Some = 2
    Lots = 3
    Force32 = 0x40000000
# endregion


class CompressOptions(c.Structure):
    _fields_ = [
        ("verbosity", c.c_uint),
        ("minMatchLen", c.c_int),
        ("seekChunkReset", c.c_bool),
        ("seekChunkLen", c.c_int),
        ("profile", c.c_int),  # `Profile`
        ("dictionarySize", c.c_int),
        ("spaceSpeedTradeoffBytes", c.c_int),
        ("maxHuffmansPerChunk", c.c_int),
        ("sendQuantumCRCs", c.c_bool),
        ("maxLocalDictionarySize", c.c_int),
        ("makeLongRangeMatcher", c.c_int),
        ("matchTableSizeLog2", c.c_int),
    ]

    def __repr__(self):
        return (
            f"CompressOptions(\n"
            f"    verbosity={self.verbosity}\n"
            f"    minMatchLen={self.minMatchLen}\n"
            f"    seekChunkReset={self.seekChunkReset}\n"
            f"    seekChunkLen={self.seekChunkLen}\n"
            f"    profile={self.profile}\n"
            f"    dictionarySize={self.dictionarySize}\n"
            f"    spaceSpeedTradeoffBytes={self.spaceSpeedTradeoffBytes}\n"
            f"    maxHuffmansPerChunk={self.maxHuffmansPerChunk}\n"
            f"    sendQuantumCRCs={self.sendQuantumCRCs}\n"
            f"    maxLocalDictionarySize={self.maxLocalDictionarySize}\n"
            f"    makeLongRangeMatcher={self.makeLongRangeMatcher}\n"
            f"    matchTableSizeLog2={self.matchTableSizeLog2}\n"
            f")"
        )


def _dll_func_wrapper(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if __DLL is None:
            raise OodleDLLError("`oo2core_6_win64.dll` not found or loaded. Cannot handle DCX_KRAK compression.")
        return func(*args, **kwargs)
    return wrapped


@_dll_func_wrapper
def compress(
    raw_buf: bytes,
    compressor: Compressor = Compressor.Kraken,
    level: CompressionLevel = CompressionLevel.Optimal2,
) -> bytes:
    """Compress data with Oodle. Default parameters are appropriate for Sekiro and Elden Ring (DCX_KRAK)."""
    raw_buf_size = len(raw_buf)
    # noinspection PyCallingNonCallable,PyTypeChecker
    raw_buf_array = (c.c_char * raw_buf_size)(*raw_buf)
    max_comp_buf_size = __DLL_GetCompressedBufferSizeNeeded(raw_buf_size)
    comp_buf_array = (c.c_char * max_comp_buf_size)()

    p_options = __DLL_CompressOptions_GetDefault(compressor, level)
    p_options.contents.seekChunkReset = True  # required for the game to not crash --TK
    p_options.contents.seekChunkLen = 0x40000  # already default, but included for authenticity --TK

    actual_comp_buf_size = __DLL_Compress(
        compressor,
        raw_buf_array,
        raw_buf_size,
        comp_buf_array,
        level,
        p_options,
        c.c_void_p(),
        c.c_void_p(),
        c.c_void_p(),
        0,
    )

    return comp_buf_array.raw[:actual_comp_buf_size]


@_dll_func_wrapper
def decompress(comp_buf: bytes, decompressed_size: int):
    """Uses the same default values as `SoulsFormats`.

    Note that `decompressed_size` is required, and can be found in the `DCX` header.
    """
    comp_buf_size = len(comp_buf)
    # noinspection PyCallingNonCallable,PyTypeChecker
    comp_buf_array = (c.c_char * comp_buf_size)(*comp_buf)
    max_raw_buf_size = __DLL_GetDecodeBufferSize(decompressed_size, True)
    raw_buf_array = (c.c_char * max_raw_buf_size)()

    actual_raw_buf_size = __DLL_Decompress(
        comp_buf_array,
        comp_buf_size,
        raw_buf_array,
        decompressed_size,
        FuzzSafe.Yes,
        CheckCRC.No,
        Verbosity.Null,
        c.c_void_p(),
        0,
        c.c_void_p(),
        c.c_void_p(),
        c.c_void_p(),
        0,
        DecodeThreadPhase.Unthreaded,
    )

    if actual_raw_buf_size == 0:
        _LOGGER.warning("Oodle decompression returned zero. Using expected decompressed size instead.")
        return raw_buf_array.raw[:decompressed_size]

    return raw_buf_array.raw[:actual_raw_buf_size]


def find_oodle_dll() -> str:
    """Try to find DLL at Soulstruct, Sekiro, or Elden Ring paths."""
    _auto_oodle_locations = (
        PACKAGE_PATH(__DLL_NAME),
        PACKAGE_PATH("..", __DLL_NAME),
        Path(SEKIRO_PATH, __DLL_NAME),
        Path(ELDEN_RING_PATH, __DLL_NAME),
    )
    for _location in _auto_oodle_locations:
        if _location.exists():
            return str(_location)

    # DLL not found in one of these default locations.
    _LOGGER.warning(
        f"Could not find `oo2core_6_win64.dll` in Soulstruct, Sekiro, or Elden Ring paths.\n"
        f"You will not be able to compress/decompress Sekiro or Elden Ring files using Soulstruct.\n"
        f"Call `oodle.LOAD_DLL(path)` to load the DLL from an arbitrary path."
    )
    return ""


def LOAD_DLL(dll_path: str = ""):
    """Load Oodle DLL from specified path, or search for it in default locations."""

    if not hasattr(c, "WinDLL"):
        raise MissingOodleDLLError(
            "Can currently only load Oodle DLL on Windows. Oodle (DCX_KRAK) compression unavailable."
        )

    if not dll_path:
        dll_path = find_oodle_dll()
        if not dll_path:
            raise MissingOodleDLLError(
                "Could not find `oo2core_6_win64.dll` in Soulstruct, Sekiro, or Elden Ring paths."
            )

    global __DLL
    global __DLL_Compress, __DLL_Decompress
    global __DLL_GetCompressedBufferSizeNeeded, __DLL_CompressOptions_GetDefault, __DLL_GetDecodeBufferSize

    if not Path(dll_path).exists():
        raise MissingOodleDLLError(f"Oodle DLL path invalid: {dll_path}")

    try:
        __DLL = c.WinDLL(dll_path)  # uses `stdcall` convention, not `cdecl`
    except Exception as ex:
        raise MissingOodleDLLError(f"Failed to load Oodle DLL from path '{dll_path}'. Error: {ex}")

    __DLL_Compress = __DLL["OodleLZ_Compress"]
    __DLL_Compress.restype = c.c_long
    __DLL_Compress.argtypes = (
        Compressor,  # compressor
        c.POINTER(c.c_char),  # rawBuf
        c.c_long,  # rawLen
        c.POINTER(c.c_char),  # compBuf
        CompressionLevel,  # level
        c.POINTER(CompressOptions),  # pOptions
        c.c_void_p,  # dictionaryBase
        c.c_void_p,  # lrm
        c.c_void_p,  # scratchMem
        c.c_long,  # scratchSize
    )

    __DLL_CompressOptions_GetDefault = __DLL["OodleLZ_CompressOptions_GetDefault"]
    __DLL_CompressOptions_GetDefault.restype = c.POINTER(CompressOptions)
    # noinspection PyTypeChecker
    __DLL_CompressOptions_GetDefault.argtypes = (
        Compressor,  # compressor
        CompressionLevel,  # lzLevel
    )

    __DLL_Decompress = __DLL["OodleLZ_Decompress"]
    __DLL_Decompress.restype = c.c_long
    __DLL_Decompress.argtypes = (
        c.POINTER(c.c_char),  # compBuf
        c.c_long,  # compBufSize
        c.POINTER(c.c_char),  # rawBuf
        c.c_long,  # rawLen (known uncompressed size)
        c.c_int,  # fuzzSafe
        CheckCRC,  # checkCRC
        Verbosity,  # verbosity
        c.c_void_p,  # decBufBase
        c.c_long,  # decBufSize
        c.c_void_p,  # fpCallback
        c.c_void_p,  # callbackUserData
        c.c_void_p,  # decoderMemory
        c.c_long,  # decoderMemorySize
        c.c_int,  # threadPhase
    )

    __DLL_GetCompressedBufferSizeNeeded = __DLL["OodleLZ_GetCompressedBufferSizeNeeded"]
    __DLL_GetCompressedBufferSizeNeeded.restype = c.c_long
    __DLL_GetCompressedBufferSizeNeeded.argtypes = (
        c.c_long,  # rawSize
    )

    __DLL_GetDecodeBufferSize = __DLL["OodleLZ_GetDecodeBufferSize"]
    __DLL_GetDecodeBufferSize.restype = c.c_long
    __DLL_GetDecodeBufferSize.argtypes = (
        c.c_long,  # rawSize
        c.c_bool,  # corruptionPossible
    )


# Load DLL automatically.
try:
    LOAD_DLL()
except MissingOodleDLLError as load_ex:
    _LOGGER.warning(
        f"Could not find/load Oodle DLL. DCX_KRAK compression/decompression will be unavailable. Error: {load_ex}"
    )
