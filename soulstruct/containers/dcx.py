"""NOTE: This file is Python 3.9 compatible for Blender 3.X use.

This module originally used a `DCX` class, but I changed it to static functions to avoid the unnecessary OOP confusion
when loading files, since `DCX(data).pack()` and `DCX(path).data` were the most common use cases anyway.
"""
from __future__ import annotations

__all__ = [
    "DCXType",
    "compress",
    "decompress",
]

import logging
import zlib
from enum import Enum

from soulstruct.containers import oodle
from soulstruct.utilities.binary import BinaryStruct, BinaryReader, ReadableTyping

_LOGGER = logging.getLogger(__name__)


class DCXType(Enum):
    Unknown = -1  # could not be detected
    Null = 0  # no compression
    Zlib = 1  # not really DCX but supported
    DCP_EDGE = 2  # DCP header, chunked deflate compression. Used in ACE:R TPFs.
    DCP_DFLT = 3  # DCP header, deflate compression. Used in DeS test maps.
    DCX_EDGE = 4  # DCX header, chunked deflate compression. Primarily used in DeS.
    DCX_DFLT_10000_24_9 = 5  # DCX header, deflate compression. Primarily used in DS1 and DS2.
    DCX_DFLT_10000_44_9 = 6  # DCX header, deflate compression. Primarily used in BB and DS3.
    DCX_DFLT_11000_44_8 = 7  # DCX header, deflate compression. Used for the backup regulation in DS3 save files.
    DCX_DFLT_11000_44_9 = 8  # DCX header, deflate compression. Used in Sekiro.
    DCX_DFLT_11000_44_9_15 = 9  # DCX header, deflate compression. Used in the ER regulation.
    DCX_KRAK = 10  # DCX header, Oodle compression. Used in Sekiro and Elden Ring.

    @classmethod
    def detect(cls, reader: BinaryReader) -> DCXType:
        """Detect type of DCX. Resets offset when done."""
        old_offset = reader.tell()

        dcx_type = cls.Unknown

        magic = reader.unpack_value("4s")
        if magic == b"DCP\0":  # rare, only for older games and DeS test maps
            # Possible file pattern for DFLT or EDGE compression.
            dcx_fmt = reader.unpack_value("4s", offset=4)
            if dcx_fmt == b"DCP\0":
                dcx_type = cls.DCP_DFLT
            elif dcx_fmt == b"EDGE":
                dcx_type = cls.DCP_EDGE
        elif magic == b"DCX\0":
            dcx_fmt = reader.unpack_value("4s", offset=0x28)
            if dcx_fmt == b"EDGE":
                dcx_type = cls.DCX_EDGE
            elif dcx_fmt == b"DFLT":
                # Check four unknown header fields to determine DFLT subtype.
                unk04 = reader.unpack_value("i", offset=0x4)
                unk10 = reader.unpack_value("i", offset=0x10)
                unk30 = reader.unpack_value("i", offset=0x30)
                unk38 = reader.unpack_value("B", offset=0x38)
                if unk10 == 0x24:
                    dcx_type = cls.DCX_DFLT_10000_24_9
                elif unk10 == 0x44:
                    if unk04 == 0x10000:
                        dcx_type = cls.DCX_DFLT_10000_44_9
                    elif unk04 == 0x11000:
                        if unk30 == 0x8000000:
                            dcx_type = cls.DCX_DFLT_11000_44_8
                        elif unk30 == 0x9000000:
                            if unk38 == 15:
                                dcx_type = cls.DCX_DFLT_11000_44_9_15
                            elif unk38 == 0:
                                dcx_type = cls.DCX_DFLT_11000_44_9
            elif dcx_fmt == b"KRAK":  # requires `oo2core_6_win64.dll`
                dcx_type = cls.DCX_KRAK
        else:
            b0 = reader.unpack_value("B", offset=0)
            b1 = reader.unpack_value("B", offset=1)
            if b0 == 0x78 and (b1 in {0x01, 0x5E, 0x9C, 0xDA}):
                dcx_type = cls.Zlib

        reader.seek(old_offset)
        return dcx_type


# Maps DCX types to their expected header `BinaryStruct`s.
DCX_HEADER_STRUCTS = {
    DCXType.DCP_DFLT: BinaryStruct(
        ("type", "4s", b"DCP\0"),
        ("subtype", "4s", b"DFLT"),
        ("unks", "6i", (0x20, 0x9000000, 0, 0, 0, 0x10100)),
        ("dcs", "4s", b"DCS\0"),
        ("decompressed_size", "i"),
        ("compressed_size", "i"),
        byte_order=">",
    ),
    # TODO: DCP_EDGE
    # TODO: DCX_EDGE
    DCXType.DCX_DFLT_10000_24_9: BinaryStruct(
        ("type", "4s", b"DCX\0"),
        ("unks1", "5i", (0x10000, 0x18, 0x24, 0x24, 0x2C)),
        ("dcs", "4s", b"DCS\0"),
        ("decompressed_size", "i"),
        ("compressed_size", "i"),
        ("dcp", "4s", b"DCP\0"),
        ("dflt", "4s", b"DFLT"),
        ("unks2", "6i", (0x20, 0x9000000, 0, 0, 0, 0x10100)),
        ("dca", "4s", b"DCA\0"),
        ("compressed_header_size", "i", 8),
        byte_order=">",
    ),
    DCXType.DCX_DFLT_10000_44_9: BinaryStruct(
        ("type", "4s", b"DCX\0"),
        ("unks1", "5i", (0x10000, 0x18, 0x24, 0x44, 0x4C)),
        ("dcs", "4s", b"DCS\0"),
        ("decompressed_size", "i"),
        ("compressed_size", "i"),
        ("dcp", "4s", b"DCP\0"),
        ("dflt", "4s", b"DFLT"),
        ("unks2", "6i", (0x20, 0x9000000, 0, 0, 0, 0x10100)),
        ("dca", "4s", b"DCA\0"),
        ("compressed_header_size", "i", 8),
        byte_order=">",
    ),
    DCXType.DCX_DFLT_11000_44_8: BinaryStruct(
        ("type", "4s", b"DCX\0"),
        ("unks1", "5i", (0x11000, 0x18, 0x24, 0x44, 0x4C)),
        ("dcs", "4s", b"DCS\0"),
        ("decompressed_size", "i"),
        ("compressed_size", "i"),
        ("dcp", "4s", b"DCP\0"),
        ("dflt", "4s", b"DFLT"),
        ("unks2", "6i", (0x20, 0x8000000, 0, 0, 0, 0x10100)),
        ("dca", "4s", b"DCA\0"),
        ("compressed_header_size", "i", 8),
        byte_order=">",
    ),
    DCXType.DCX_DFLT_11000_44_9: BinaryStruct(
        ("type", "4s", b"DCX\0"),
        ("unks1", "5i", (0x11000, 0x18, 0x24, 0x44, 0x4C)),
        ("dcs", "4s", b"DCS\0"),
        ("decompressed_size", "i"),
        ("compressed_size", "i"),
        ("dcp", "4s", b"DCP\0"),
        ("dflt", "4s", b"DFLT"),
        ("unks2", "6i", (0x20, 0x9000000, 0, 0, 0, 0x10100)),
        ("dca", "4s", b"DCA\0"),
        ("compressed_header_size", "i", 8),
        byte_order=">",
    ),
    DCXType.DCX_DFLT_11000_44_9_15: BinaryStruct(
        ("type", "4s", b"DCX\0"),
        ("unks1", "5i", (0x11000, 0x18, 0x24, 0x44, 0x4C)),
        ("dcs", "4s", b"DCS\0"),
        ("decompressed_size", "i"),
        ("compressed_size", "i"),
        ("dcp", "4s", b"DCP\0"),
        ("dflt", "4s", b"DFLT"),
        ("unks2", "6i", (0x20, 0x9000000, 0, 0xF000000, 0, 0x10100)),
        ("dca", "4s", b"DCA\0"),
        ("compressed_header_size", "i", 8),
        byte_order=">",
    ),

    DCXType.DCX_KRAK: BinaryStruct(
        ("type", "4s", b"DCX\0"),
        ("unks1", "5i", (0x11000, 0x18, 0x24, 0x44, 0x4C)),
        ("dcs", "4s", b"DCS\0"),
        ("decompressed_size", "I"),
        ("compressed_size", "I"),
        ("dcp", "4s", b"DCP\0"),
        ("dflt", "4s", b"KRAK"),
        ("unks2", "6i", (0x20, 0x6000000, 0, 0, 0, 0x10100)),
        ("dca", "4s", b"DCA\0"),
        ("compressed_header_size", "i", 8),
        byte_order=">",
    ),
}


# TODO: Add default DCX types to `Game` class instances.
"""
DemonsSouls = Type.DCX_EDGE
DarkSouls1 = Type.DCX_DFLT_10000_24_9
DarkSouls2 = Type.DCX_DFLT_10000_24_9
Bloodborne = Type.DCX_DFLT_10000_44_9
DarkSouls3 = Type.DCX_DFLT_10000_44_9
Sekiro = Type.DCX_KRAK
EldenRing = Type.DCX_KRAK
"""


def decompress(dcx_source: ReadableTyping) -> tuple[bytes, DCXType]:
    """Decompress the given file path, raw bytes, or buffer/reader.

    Returns a tuple containing the decompressed `bytes` and a `DCXInfo` instance that can be used to compress later
    with the same DCX type/parameters.
    """
    reader = BinaryReader(dcx_source, byte_order=">")  # always big-endian
    dcx_type = DCXType.detect(reader)

    if dcx_type == DCXType.Unknown:
        raise ValueError("Unknown DCX type. Cannot decompress.")

    header = reader.unpack_struct(DCX_HEADER_STRUCTS[dcx_type], byte_order=">")
    compressed = reader.read(header["compressed_size"])  # TODO: do I need to rstrip nulls?

    if dcx_type == DCXType.DCX_KRAK:
        decompressed = oodle.decompress(compressed, header["decompressed_size"])
    else:
        decompressed = zlib.decompressobj().decompress(compressed)

    if len(decompressed) != header["decompressed_size"]:
        raise ValueError("Decompressed DCX data size does not match size in header.")
    return decompressed, dcx_type


def compress(raw_data: bytes, dcx_type: DCXType) -> bytes:
    """Compress `raw_data` with DCX of `dcx_type`.

    Returns bytes that are ready to be written to a DCX file.
    """
    if dcx_type == DCXType.DCX_KRAK:
        compressed = oodle.compress(raw_data)  # default compressor and compression level are correct
    else:
        compressed = zlib.compress(raw_data, level=7)

    header = DCX_HEADER_STRUCTS[dcx_type].pack(
        decompressed_size=len(raw_data),
        compressed_size=len(compressed),
    )
    return header + compressed
