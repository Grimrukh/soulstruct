import logging
import zlib
from pathlib import Path

from soulstruct.utilities import BinaryStruct

_LOGGER = logging.getLogger(__name__)


class DCX:

    # TODO: Support types of DCX other than DCP-DFLT.

    # NOTE: completely big-endian.
    HEADER_STRUCT = BinaryStruct(
        ("dcx_name", "4s", b"DCX\0"),
        ("unk1", "i", 65536),
        ("unk2", "i", 24),
        ("unk3", "i", 36),
        ("magic1", "i"),  # Differs between games.
        ("magic2", "i"),  # Differs between games.
        ("dcs_name", "4s", b"DCS\0"),
        ("decompressed_size", "I"),
        ("compressed_size", "I"),
        ("dcp_name", "4s", b"DCP\0"),
        ("dflt_name", "4s", b"DFLT"),
        ("unk4", "6i", (32, 150994944, 0, 0, 0, 65792)),
        ("dca_name", "4s", b"DCA\0"),
        ("compressed_header_size", "i", 8),  # TODO: asserting for now, haven't come across any variation
        byte_order=">",
    )

    def __init__(self, dcx_source, magic=()):

        self.dcx_path = None
        self.data = b""
        try:
            # Pair of DCX magic values, or empty tuple to not use DCX.
            self.magic = tuple(magic) if magic is not None else ()
            if len(self.magic) != 2 or not all(isinstance(m, int) for m in self.magic):
                raise ValueError
        except (ValueError, TypeError):
            raise ValueError(f"`magic` should be empty (or None) or a sequence of two values.")

        if isinstance(dcx_source, (str, Path)):
            self.dcx_path = Path(dcx_source)
            with self.dcx_path.open("rb") as file:
                self.unpack(file)
        elif isinstance(dcx_source, bytes):
            self.data = dcx_source

    def unpack(self, dcx_buffer):
        if self.magic:
            raise ValueError("`DCX.magic` cannot be set manually before unpack.")
        header = self.HEADER_STRUCT.unpack(dcx_buffer)
        if header["magic1"] not in {36, 68}:
            raise ValueError(f"Expected 36 or 68 at offset 0x16 but found {header['magic1']}.")
        if header["magic2"] not in {44, 76}:
            raise ValueError(f"Expected 36 or 68 at offset 0x20 but found {header['magic1']}.")
        self.magic = (header["magic1"], header["magic2"])
        compressed = dcx_buffer.read().rstrip(b"\0")  # Nulls stripped from the end.
        if len(compressed) != header["compressed_size"]:
            # No error raised.
            _LOGGER.warning(
                f"Compressed data size ({len(compressed)}) does not match size in header "
                f"({header['compressed_size']}) in file {self.dcx_path}."
            )
        self.data = zlib.decompressobj().decompress(compressed)
        if len(self.data) != header["decompressed_size"]:
            raise ValueError("Decompressed data size does not match size in header.")

    def pack(self):
        compressed = zlib.compress(self.data, level=7)
        header = self.HEADER_STRUCT.pack(
            {
                "magic1": self.magic[0],
                "magic2": self.magic[1],
                "decompressed_size": len(self.data),
                "compressed_size": len(compressed),
            }
        )
        return header + compressed

    def write_packed(self, dcx_path=None):
        if dcx_path is None:
            if self.dcx_path is None:
                raise ValueError("DCX path cannot be determined automatically.")
            dcx_path = self.dcx_path
        packed = self.pack()
        with open(dcx_path, "wb") as file:
            file.write(packed)

    def write_unpacked(self, data_path=None):
        if data_path is None:
            if self.dcx_path is None:
                raise ValueError("DCX path cannot be determined automatically.")
            data_path = self.dcx_path.parent / self.dcx_path.stem
        else:
            data_path = Path(data_path)
        with data_path.open("wb") as file:
            file.write(self.data)

    @classmethod
    def get_data_and_magic(cls, dcx_source):
        dcx = cls(dcx_source)
        return dcx.data, dcx.magic
