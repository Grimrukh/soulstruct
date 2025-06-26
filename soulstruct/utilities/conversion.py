from __future__ import annotations

__all__ = ["int_group_to_bit_set", "bit_set_to_int_group", "floatify"]

import logging
import struct

_LOGGER = logging.getLogger(__name__)


def int_group_to_bit_set(flag_group, assert_size=None):
    """Get draw or display group 128/256-bit field <a, b, c, ...> where a, b, c, ... are the little-endian bit
    zero-based indices of the draw groups bit field (which is unpacked/packed internally as 4/8 32-bit integers).

    So draw groups `[0b01001..110, 0b0, 0b000...001, 0b100...000]` would return `{1, 4, 29, 30, 95, 96}`.
    """
    if not isinstance(flag_group, (list, tuple)) or (assert_size and len(flag_group) != assert_size):
        raise ValueError(f"Flag group must be a sequence of {assert_size} integers.")
    return set([32 * i + j for i in range(4) for j in range(32) if (2 ** j) & flag_group[i]])


def bit_set_to_int_group(enabled_flags, group_size):
    """Opposite of above method. Converts set (or sequence) of flags to an N-integer bit field array for packing."""
    max_flag = 32 * group_size - 1
    if not isinstance(enabled_flags, set):
        enabled_flags_set = set(enabled_flags)
        if len(enabled_flags_set) != len(enabled_flags):
            _LOGGER.warning("Some flags values were present in flag sequence more than once. Ignoring repeats.")
        enabled_flags = enabled_flags_set
    flag_group = [0] * group_size
    for flag in enabled_flags:
        if not isinstance(flag, int):
            raise ValueError(f"Non-integer value {flag} appeared in flag set (draw/display/navmesh/backread groups).")
        if not 0 <= flag <= max_flag:
            raise ValueError(f"Invalid draw/display/navmesh/backread index {flag} (must be between 0 and {max_flag}).")
        flag_group[flag // 32] += 2 ** (flag % 32)
    return flag_group


def floatify(int32: int, signed=False) -> float:
    """Utility function that re-interprets a 32-bit unsigned (default) or signed integer as a single float.

    This could be useful if you have any old EMEVD scripts that incorrectly represent float event arguments as integers.
    """
    pack_fmt = "<i" if signed else "<I"
    return struct.unpack("<f", struct.pack(pack_fmt, int32))[0]
