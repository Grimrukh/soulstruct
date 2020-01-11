"""BND magic information.

BND ("binder") resources are simple containers that glue multiple resources of the same type together. They are used
across all FromSoft games, and come in two primary version (BND3 and BND4), but there are different subtypes of BND
within each version as well, marked by a certain "magic" byte in the header. Classifications of each magic type are
specified here.

TODO: Determine which file types in which games use which magic values.
"""

BND_MAGIC_VALUES = (
    0x00, 0x06, 0x0C, 0x0E, 0x1C, 0x20, 0x24, 0x26, 0x2A,
    0x2C, 0x2E, 0x30, 0x3E, 0x40, 0x54, 0x60, 0x64, 0x67,
    0x70, 0x74, 0x80, 0x91, 0xA0, 0xE0, 0xE4, 0xF0, 0xF4,
)

IS_BIG_ENDIAN = {
    0x67, 0x80, 0x91, 0xA0, 0xE0, 0xE4, 0xF0, 0xF4,
}
HAS_ID = {
    0x06, 0x0E, 0x26, 0x2A, 0x2E, 0x3E, 0x40, 0x54, 0x60, 0x64, 0x67, 0x70, 0x74, 0xE0, 0xE4, 0xF0, 0xF4,
}
HAS_PATH = {
    0x06, 0x0C, 0x0E, 0x1C, 0x20, 0x24, 0x26, 0x2A, 0x2C, 0x2E, 0x30, 0x3E,
    0x54, 0x60, 0x64, 0x67, 0x70, 0x74, 0x91, 0xA0, 0xE0, 0xE4, 0xF0, 0xF4
}
HAS_UNCOMPRESSED_SIZE = {
    0x24, 0x26, 0x2A, 0x2C, 0x2E, 0x3E, 0x54, 0x64, 0x67, 0x74, 0xE4, 0xF4,
}
HAS_64BIT_OFFSET = {
    0x1C, 0x3E,
}

def is_big_endian(magic):
    return magic in IS_BIG_ENDIAN

def has_id(magic):
    return magic in HAS_ID

def has_path(magic):
    return magic in HAS_PATH

def has_uncompressed_size(magic):
    return magic in HAS_UNCOMPRESSED_SIZE

def has_64bit_offsets(magic):
    return magic in HAS_64BIT_OFFSET

def header_size(magic):
    """ Calculate BND header size based on magic. """
    if magic not in BND_MAGIC_VALUES:
        raise ValueError(f"Invalid BND magic value: {hex(magic)}")
    size = 16  # Base size.
    size += 4 if has_id(magic) else 0
    size += 4 if has_path(magic) else 0
    size += 8 if has_uncompressed_size(magic) else 0
    size += 8 if has_64bit_offsets(magic) else 4
    return size


BND_ENTRY_MAGIC_VALUES = (
    0x00, 0x02, 0x03, 0x0A, 0x40, 0x50, 0xC0,
)

IS_ENTRY_COMPRESSED = {
    0x03, 0xC0,
}

def is_entry_compressed(magic):
    return magic in IS_ENTRY_COMPRESSED
