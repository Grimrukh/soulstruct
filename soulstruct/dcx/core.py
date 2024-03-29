"""
This module originally used a `DCX` class, but I changed it to static functions to avoid the unnecessary OOP confusion
when loading files, since `DCX(data).pack()` and `DCX(path).data` were the most common use cases anyway.
"""
from __future__ import annotations

__all__ = [
    "DCXType",
    "compress",
    "decompress",
    "is_dcx",
]

import logging
import typing as tp
import zlib
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import *

from . import oodle

_LOGGER = logging.getLogger("soulstruct")


class DCXError(SoulstructError):
    pass


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

    # Game default aliases.
    DES = DCX_EDGE
    DS1_DS2 = DCX_DFLT_10000_24_9
    BB_DS3 = DCX_DFLT_10000_44_9
    SEKIRO = DCX_DFLT_11000_44_9
    ER_REGULATION = DCX_DFLT_11000_44_9_15

    def get_version_info(self) -> tuple[bytes, int, int, int, int, int]:
        return DCX_VERSION_INFO[self]

    def has_dcx_extension(self):
        return self.value >= 2

    def process_path(self, path: Path | str) -> Path | str:
        """Add or remove '.dcx' extension to/from `path` as appropriate.

        Returns `Path` or `str` (depending on input type).
        """
        is_path = isinstance(path, Path)
        path = Path(path)
        new_path = path.with_name(path.name.removesuffix(".dcx"))
        if self.has_dcx_extension():
            new_path = path.with_name(path.name + ".dcx")
        return new_path if is_path else str(new_path)

    @classmethod
    def detect(cls, reader: BinaryReader) -> DCXType:
        """Detect type of DCX. Resets offset when done."""
        with reader.temp_offset():
            magic = reader.peek(4)
            if magic == b"DCP\0":  # rare, only for older games and DeS test maps
                # Possible file pattern for DFLT or EDGE compression.
                dcx_fmt = reader.peek(4, 4)
                if dcx_fmt == b"DCP\0":
                    return cls.DCP_DFLT
                elif dcx_fmt == b"EDGE":
                    return cls.DCP_EDGE
                else:
                    return cls.Unknown

            if magic != b"DCX\0":
                b0, b1 = reader.unpack("BB")
                if b0 == 0x78 and (b1 in {0x01, 0x5E, 0x9C, 0xDA}):
                    return cls.Zlib
                return cls.Unknown  # very unlikely to be DCX at this point

            try:
                header = DCXHeaderStruct.from_bytes(reader)
            except BinaryFieldValueError as ex:
                _LOGGER.error(f"Error while trying to detect `DCXType`: {ex}")
                return cls.Unknown

            header_version_info = header.get_version_info()
            for dcx_type, version_info in DCX_VERSION_INFO.items():
                if version_info == header_version_info:
                    return dcx_type

            _LOGGER.error(
                f"Unknown configuration of DCX version fields in DCX header: {header_version_info}\n"
                "  Maybe tell Grimrukh about this new DCX format..."
            )
            return cls.Unknown


DCX_VERSION_INFO = {
    DCXType.DCP_DFLT: (),
    DCXType.DCX_DFLT_10000_24_9: (b"DFLT", 0x10000, 0x24, 0x2C, 0x9000000, 0),
    DCXType.DCX_DFLT_10000_44_9: (b"DFLT", 0x10000, 0x44, 0x4C, 0x9000000, 0),
    DCXType.DCX_DFLT_11000_44_8: (b"DFLT", 0x11000, 0x44, 0x4C, 0x8000000, 0),
    DCXType.DCX_DFLT_11000_44_9: (b"DFLT", 0x11000, 0x44, 0x4C, 0x9000000, 0),
    DCXType.DCX_DFLT_11000_44_9_15: (b"DFLT", 0x11000, 0x44, 0x4C, 0x9000000, 0xF000000),
    DCXType.DCX_KRAK: (b"KRAK", 0x11000, 0x44, 0x4C, 0x6000000, 0),
}


@dataclass(slots=True)
class DCPHeaderStruct(BinaryStruct):
    """Early, abbreviated compression version (Demon's Souls only)."""
    dcp: bytes = field(init=False, **BinaryString(4, asserted=b"DCP"))
    dflt: bytes = field(init=False, **BinaryString(4, asserted=b"DFLT"))
    unks: list[int] = field(init=False, **BinaryArray(6, asserted=[0x20, 0x9000000, 0, 0, 0, 0x10100]))
    dcs: bytes = field(init=False, **BinaryString(4, b"DCS"))
    decompressed_size: int
    compressed_size: int

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian


@dataclass(slots=True)
class DCXHeaderStruct(BinaryStruct):
    """Compression header (with variation in the `version` fields) in all FromSoft games after Demon's Souls.

    NOTE: Not asserting the five 'version' fields so that we can guess when a new format is available.
    """
    dcx: bytes = field(init=False, **BinaryString(4, asserted=b"DCX"))
    version1: int  # = field(**Binary(asserted=(0x10000, 0x11000)))  # 1
    unk1: int = field(init=False, **Binary(asserted=0x18))
    unk2: int = field(init=False, **Binary(asserted=0x24))
    version2: int  # = field(**Binary(asserted=(0x24, 0x44)))  # 2
    version3: int  # = field(**Binary(asserted=(0x2C, 0x4C)))  # 3
    dcs: bytes = field(init=False, **BinaryString(4, b"DCS"))
    decompressed_size: int
    compressed_size: int
    dcp: bytes = field(init=False, **BinaryString(4, asserted=b"DCP"))
    compression_type: bytes = field(**BinaryString(4, asserted=(b"DFLT", b"KRAK")))
    unk3: int = field(init=False, **Binary(asserted=0x20))
    version4: int  # = field(**Binary(asserted=(0x6000000, 0x8000000, 0x9000000)))  # 3
    unk4: int = field(init=False, **Binary(asserted=0))
    version5: int  # = field(**Binary(asserted=(0, 0xF000000)))  # 4
    unk5: int = field(init=False, **Binary(asserted=0))
    unk6: int = field(init=False, **Binary(asserted=0x10100))
    dca: bytes = field(init=False, **BinaryString(4, asserted=b"DCA"))
    compressed_header_size: int = field(init=False, **Binary(asserted=8))

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian

    def get_version_info(self) -> tuple[bytes, int, int, int, int, int]:
        """Actually used."""
        return self.compression_type, self.version1, self.version2, self.version3, self.version4, self.version5


def decompress(dcx_source: bytes | BinaryReader | tp.BinaryIO | Path | str) -> tuple[bytes, DCXType]:
    """Decompress the given file path, raw bytes, or buffer/reader.

    Returns a tuple containing the decompressed `bytes` and a `DCXInfo` instance that can be used to compress later
    with the same DCX type/parameters.
    """
    reader = BinaryReader(dcx_source, default_byte_order=ByteOrder.BigEndian)  # always big-endian
    dcx_type = DCXType.detect(reader)

    if dcx_type == DCXType.Unknown:
        raise DCXError("Unknown DCX type. Cannot decompress.")
    if dcx_type == DCXType.DCP_DFLT:
        header = DCPHeaderStruct.from_bytes(reader, byte_order=ByteOrder.BigEndian)
    else:
        header = DCXHeaderStruct.from_bytes(reader, byte_order=ByteOrder.BigEndian)

    compressed = reader.read(header.compressed_size)

    if dcx_type == DCXType.DCX_KRAK:
        decompressed = oodle.decompress(compressed, header.decompressed_size)
    else:
        decompressed = zlib.decompressobj().decompress(compressed)

    if len(decompressed) != header.decompressed_size:
        raise DCXError("Decompressed DCX data size does not match size in header.")
    return decompressed, dcx_type


def compress(raw_data: bytes, dcx_type: DCXType) -> bytes:
    """Compress `raw_data` with DCX of `dcx_type`.

    Returns bytes that are ready to be written to a DCX file.
    """
    if dcx_type == DCXType.DCX_KRAK:
        compressed = oodle.compress(raw_data)  # default compressor and compression level are correct
    else:
        compressed = zlib.compress(raw_data, level=7)

    if dcx_type == DCXType.DCP_DFLT:
        header = bytes(DCPHeaderStruct(
            decompressed_size=len(raw_data),
            compressed_size=len(compressed),
        ))
    else:
        version_info = dcx_type.get_version_info()
        header = bytes(DCXHeaderStruct(
            version1=version_info[1],
            version2=version_info[2],
            version3=version_info[3],
            compression_type=version_info[0],
            decompressed_size=len(raw_data),
            compressed_size=len(compressed),
            version4=version_info[4],
            version5=version_info[5],
        ))
    return header + compressed


def is_dcx(reader: BinaryReader) -> bool:
    """Checks if file data starts with DCX (or DCP) magic."""
    return reader["4s", 0] in {b"DCP\0", b"DCX\0"}
