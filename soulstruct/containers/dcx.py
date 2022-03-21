"""NOTE: This file is Python 3.9 compatible for Blender 3.X use."""

import io
import logging
import zlib
import typing as tp
from pathlib import Path

from soulstruct.utilities.binary import BinaryStruct, BinaryReader

_LOGGER = logging.getLogger(__name__)


class DCX:

    # TODO: Support types of DCX other than DCP-DFLT.

    # NOTE: completely big-endian.
    HEADER_STRUCT = BinaryStruct(
        ("dcx_name", "4s", b"DCX\0"),
        ("unk1", "i", 65536),
        ("unk2", "i", 24),
        ("unk3", "i", 36),
        ("magic", "2i"),  # Differs between games.
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

    def __init__(self, dcx_source=None, magic=()):
        """Open a ".dcx" file, which is a compressed version of any FromSoftware file type (e.g. a BND).

        Use `.data` to get the `bytes` of the uncompressed file within. The `.magic` attribute specifies information
        about the DCX header.

        Note that the `GameFile` base class handles DCX automatically.
        """

        self.dcx_path = None
        self.data = b""
        self._magic = ()
        self.magic = magic

        if dcx_source is None:
            return
        elif isinstance(dcx_source, (str, Path)):
            self.dcx_path = Path(dcx_source)
        elif isinstance(dcx_source, bytes):
            if not self.magic:
                raise ValueError(f"If `dcx_source` is a `bytes` object, DCX `magic` must be given.")
            self.data = dcx_source
            return

        if isinstance(dcx_source, (str, Path, io.BufferedIOBase, BinaryReader)):
            self.unpack(BinaryReader(dcx_source))
        else:
            raise TypeError(f"Invalid DCX source type: {type(dcx_source)}")

    def unpack(self, dcx_reader: BinaryReader):
        if self.magic:
            raise ValueError("`DCX.magic` cannot be set manually before unpack.")
        header = dcx_reader.unpack_struct(self.HEADER_STRUCT)
        self.magic = header["magic"]
        compressed = dcx_reader.read().rstrip(b"\0")  # Nulls stripped from the end.
        if len(compressed) != header["compressed_size"]:
            # No error raised. This happens in some files.
            file_path = f" {self.dcx_path}" if self.dcx_path else ""
            _LOGGER.warning(
                f"Compressed data size ({len(compressed)}) does not match size in header "
                f"({header['compressed_size']}) in DCX-compressed file{file_path}."
            )
        self.data = zlib.decompressobj().decompress(compressed)
        if len(self.data) != header["decompressed_size"]:
            raise ValueError("Decompressed data size does not match size in header.")

    def pack(self):
        compressed = zlib.compress(self.data, level=7)
        header = self.HEADER_STRUCT.pack(
            {
                "magic": self.magic,
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

    @property
    def magic(self):
        return self._magic

    @magic.setter
    def magic(self, value: tp.Optional[tuple[int, int]]):
        try:
            # Pair of DCX magic values, or empty tuple to not use DCX.
            value = tuple(value) if value is not None else ()
            if value:
                if len(value) != 2:
                    raise ValueError(f"Expected DXC `magic` to be a sequence of two integers.")
                if value[0] not in {36, 68}:
                    raise ValueError(f"Expected DCX `magic[0]` (header offset 0x16) to be 36 or 68, not {value[0]}.")
                if value[1] not in {44, 76}:
                    raise ValueError(f"Expected DCX `magic[1]` (header offset 0x1a) to be 44 or 76, not {value[1]}.")
        except (ValueError, TypeError):
            raise ValueError(f"`magic` should be empty (or None) or a sequence of two integers, not {value}.")
        self._magic = value
