import logging

_LOGGER = logging.getLogger(__name__)


def int_group_to_bit_set(flag_group):
    """Get draw or display group 128-bit field <a, b, c, ...> where a, b, c, ... are the little-endian bit
    zero-based indices of the draw groups bit field (which is unpacked/packed internally as four 32-bit integers).

    So draw groups `[0b01001..110, 0b0, 0b000...001, 0b100...000]` would return `{1, 4, 29, 30, 95, 96}`.
    """
    if not isinstance(flag_group, (list, tuple)) or len(flag_group) != 4:
        raise ValueError("Flag group must be a sequence of four integers.")
    return set([32 * i + j for i in range(4) for j in range(32) if (2 ** j) & flag_group[i]])


def bit_set_to_int_group(enabled_flags):
    """Opposite of above method. Converts set (or sequence) of flags to a four-integer bit field array for packing."""
    if not isinstance(enabled_flags, set):
        enabled_flags_set = set(enabled_flags)
        if len(enabled_flags_set) != len(enabled_flags):
            _LOGGER.warning("Some flags values were present in flag sequence more than once. Ignoring repeats.")
        enabled_flags = enabled_flags_set
    flag_group = [0, 0, 0, 0]
    for flag in enabled_flags:
        if not isinstance(flag, int):
            raise ValueError(f"Non-integer value {flag} appeared in flag set (draw/display/navmesh/backread groups).")
        if not 0 <= flag <= 127:
            raise ValueError(f"Invalid draw/display/navmesh/backread index {flag} (must be between 0 and 127).")
        flag_group[flag // 32] += 2 ** (flag % 32)
    return flag_group
