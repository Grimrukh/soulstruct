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


class DCXVersionInfo(tp.NamedTuple):
    compression_type: bytes
    version1: int
    version2: int
    version3: int | None  # not constant for `DCX_EDGE`
    version4: int
    version5: int
    version6: int
    version7: int

    def __eq__(self, other: DCXVersionInfo):
        """Fields must be equal unless one or both is `None`."""
        for field_name in self._fields:
            if getattr(self, field_name) is None or getattr(other, field_name) is None:
                continue
            if getattr(self, field_name) != getattr(other, field_name):
                return False
        return True

    def __repr__(self) -> str:
        """Convert `int` fields to hex strings."""
        s = f"DCXVersionInfo("
        for _field in self.__annotations__:
            v = getattr(self, _field)
            if isinstance(v, int):
                s += f"{_field}={hex(v)}, "
            else:
                s += f"{_field}={v}, "
        return s[:-2] + ")"


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

    def get_version_info(self) -> DCXVersionInfo:
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
                if version_info is None:
                    continue
                if version_info == header_version_info:
                    return dcx_type

            _LOGGER.error(
                f"Unknown configuration of DCX version fields in DCX header:\n"
                f" {header_version_info}\n"
                "  Maybe tell Grimrukh about this new DCX format..."
            )
            return cls.Unknown


DCX_VERSION_INFO = {
    DCXType.DCP_DFLT: None,
    DCXType.DCX_EDGE: DCXVersionInfo(b"EDGE", 0x10000, 0x24, None, 0x9000000, 0x10000, 0, 0x100100),
    DCXType.DCX_DFLT_10000_24_9: DCXVersionInfo(b"DFLT", 0x10000, 0x24, 0x2C, 0x9000000, 0, 0, 0x10100),
    DCXType.DCX_DFLT_10000_44_9: DCXVersionInfo(b"DFLT", 0x10000, 0x44, 0x4C, 0x9000000, 0, 0, 0x10100),
    DCXType.DCX_DFLT_11000_44_8: DCXVersionInfo(b"DFLT", 0x11000, 0x44, 0x4C, 0x8000000, 0, 0, 0x10100),
    DCXType.DCX_DFLT_11000_44_9: DCXVersionInfo(b"DFLT", 0x11000, 0x44, 0x4C, 0x9000000, 0, 0, 0x10100),
    DCXType.DCX_DFLT_11000_44_9_15: DCXVersionInfo(b"DFLT", 0x11000, 0x44, 0x4C, 0x9000000, 0, 0xF000000, 0x10100),
    DCXType.DCX_KRAK: DCXVersionInfo(b"KRAK", 0x11000, 0x44, 0x4C, 0x6000000, 0, 0, 0x10100),
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
    version1: int  # [0x10000, 0x11000]
    unk1: int = field(init=False, **Binary(asserted=0x18))
    unk2: int = field(init=False, **Binary(asserted=0x24))
    version2: int  # [0x24, 0x44]
    version3: int  # [0x2C, 0x4C, `0x50 + chunk_count * 0x10` (DCX_EDGE)]
    dcs: bytes = field(init=False, **BinaryString(4, b"DCS"))
    decompressed_size: int
    compressed_size: int
    dcp: bytes = field(init=False, **BinaryString(4, asserted=b"DCP"))
    compression_type: bytes = field(**BinaryString(4, asserted=(b"EDGE", b"DFLT", b"KRAK")))
    unk3: int = field(init=False, **Binary(asserted=0x20))
    version4: int  # [0x6000000, 0x8000000, 0x9000000]
    version5: int  # [0, 0x10000]
    version6: int  # [0, 0xF000000]
    unk5: int = field(init=False, **Binary(asserted=0))
    version7: int  # [0x10100, 0x101000]

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian

    def get_version_info(self) -> DCXVersionInfo:
        """Extract non-constant field values."""
        return DCXVersionInfo(
            compression_type=self.compression_type,
            version1=self.version1,
            version2=self.version2,
            version3=self.version3,
            version4=self.version4,
            version5=self.version5,
            version6=self.version6,
            version7=self.version7,
        )


@dataclass(slots=True)
class DCXEdgeSubheader(BinaryStruct):
    dca: bytes = field(init=False, **BinaryString(4, asserted=b"DCA"))
    dca_size: int
    egdt: bytes = field(init=False, **BinaryString(4, asserted=b"EgdT"))
    unk1: int = field(init=False, **Binary(asserted=0x10100))
    unk2: int = field(init=False, **Binary(asserted=0x24))
    unk3: int = field(init=False, **Binary(asserted=0x10))
    unk4: int = field(init=False, **Binary(asserted=0x10000))
    last_block_decompressed_size: int
    egdt_size: int
    chunk_count: int
    unk5: int = field(init=False, **Binary(asserted=0x100000))

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian


def _decompress_dcx_edge(reader: BinaryReader, header: DCXHeaderStruct) -> tuple[bytes, DCXType]:
    dca_start = reader.position  # position of 'DCA' magic
    subheader = DCXEdgeSubheader.from_bytes(reader)
    if header.version3 != 0x50 + subheader.chunk_count * 0x10:
        raise DCXError("DCX_EDGE header 'version3' field does not match expected value (0x50 + chunk_count * 0x10).")
    if subheader.last_block_decompressed_size not in {0x10000, header.decompressed_size % 0x10000}:
        raise DCXError("DCX_EDGE subheader 'last_block_decompressed_size' does not match expected value.")
    if subheader.egdt_size != 0x24 + subheader.chunk_count * 0x10:
        print(subheader)
        raise DCXError("DCX_EDGE subheader 'egdt_size' does not match expected value.")

    chunks_offset = dca_start + subheader.dca_size
    decompressed = bytearray()
    for _ in range(subheader.chunk_count):
        reader.unpack_value("i", asserted=0)
        offset, size, is_compressed_int = reader.unpack("3i")
        if is_compressed_int not in {0, 1}:
            raise DCXError("DCX_EDGE chunk 'is_compressed' field is not 0 or 1.")
        chunk = reader.unpack_bytes(length=size, offset=chunks_offset + offset)
        if is_compressed_int:
            # Decompress using DEFLATE method.
            decompressor = zlib.decompressobj(-zlib.MAX_WBITS)
            decompressed_chunk = decompressor.decompress(chunk)
            decompressed_chunk += decompressor.flush()
            decompressed += decompressed_chunk
        else:
            decompressed += chunk
    return decompressed, DCXType.DCX_EDGE


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

    if dcx_type == DCXType.DCX_EDGE:
        return _decompress_dcx_edge(reader, header)

    reader.unpack_bytes(length=4, asserted=b"DCA")
    reader.unpack_value("i", asserted=8)  # compressed header size
    compressed = reader.read(header.compressed_size)

    if dcx_type == DCXType.DCX_KRAK:
        decompressed = oodle.decompress(compressed, header.decompressed_size)
    else:
        decompressed = zlib.decompressobj().decompress(compressed)

    if len(decompressed) != header.decompressed_size:
        raise DCXError("Decompressed DCX data size does not match size in header.")
    return decompressed, dcx_type


def _compress_dcx_edge(raw_data: bytes) -> bytes:
    """Use DEFLATE compression and return compressed chunks after packed subheader."""
    writer = BinaryWriter(byte_order=ByteOrder.BigEndian)

    chunk_count = len(raw_data) // 0x10000
    last_block_decompressed_size = len(raw_data) % 0x10000
    if last_block_decompressed_size > 0:
        chunk_count += 1  # add one more chunk for the remainder

    version_info = DCXType.DCX_EDGE.get_version_info()
    header = DCXHeaderStruct(
        version1=version_info.version1,
        version2=version_info.version2,
        version3=0x50 + chunk_count * 0x10,
        compression_type=version_info.compression_type,
        decompressed_size=len(raw_data),
        compressed_size=RESERVED,
        version4=version_info.version4,
        version5=version_info.version5,
        version6=version_info.version6,
        version7=version_info.version7,
    )
    header.to_writer(writer)

    dca_start = writer.position
    egdt_start = dca_start + 8  # after b'DCA\0' magic and 'dca_size'
    subheader = DCXEdgeSubheader(
        dca_size=RESERVED,
        last_block_decompressed_size=last_block_decompressed_size,
        egdt_size=RESERVED,
        chunk_count=chunk_count,
    )
    subheader.to_writer(writer)

    for i in range(chunk_count):
        writer.pack("i", 0)  # pad
        writer.reserve(f"offset{i}", "i")
        writer.reserve(f"size{i}", "i")
        writer.reserve(f"is_compressed{i}", "i")

    subheader.fill(writer, "dca_size", writer.position - dca_start)
    subheader.fill(writer, "egdt_size", writer.position - egdt_start)
    
    data_start = writer.position
    compressed_size = 0
    for i in range(chunk_count):
        # 64 KB chunks, except for whatever is left in the last one.
        decompressed_chunk_size = 0x10000 if i < chunk_count - 1 else last_block_decompressed_size
        compressor = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-zlib.MAX_WBITS)
        raw_offset = i * 0x10000
        decompressed_chunk = raw_data[raw_offset:raw_offset + decompressed_chunk_size]
        chunk = compressor.compress(decompressed_chunk)
        chunk += compressor.flush(zlib.Z_FINISH)
        chunk_compressed_size = len(chunk)
        
        writer.fill(f"offset{i}", writer.position - data_start)
        writer.fill(f"size{i}", chunk_compressed_size)
        writer.fill(f"is_compressed{i}", int(chunk_compressed_size < decompressed_chunk_size))
        compressed_size += chunk_compressed_size
        writer.append(chunk)
        writer.pad_align(0x10)

    header.fill(writer, "compressed_size", compressed_size)

    return bytes(writer)


def compress(raw_data: bytes, dcx_type: DCXType) -> bytes:
    """Compress `raw_data` with DCX of `dcx_type`.

    Returns bytes that are ready to be written to a DCX file.
    """
    if dcx_type == DCXType.DCX_EDGE:
        return _compress_dcx_edge(raw_data)

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
            version1=version_info.version1,
            version2=version_info.version2,
            version3=version_info.version3,
            compression_type=version_info.compression_type,
            decompressed_size=len(raw_data),
            compressed_size=len(compressed),
            version4=version_info.version4,
            version5=version_info.version5,
            version6=version_info.version6,
            version7=version_info.version7,
        ))
        header += b"DCA\0" + b"\x00\x00\x00\x08"
    return header + compressed


def is_dcx(reader: BinaryReader) -> bool:
    """Checks if file data starts with DCX (or DCP) magic."""
    return reader["4s", 0] in {b"DCP\0", b"DCX\0"}
