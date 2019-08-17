import os
import zlib
from soulstruct.utilities import BinaryStruct


class DCX(object):

    # TODO: Support types of DCX other than DCP-DFLT.

    # NOTE: completely big-endian.
    HEADER_STRUCT = BinaryStruct(
        ('dcx_name', '4s', b'DCX\0'),
        ('unk1', 'i', 65536),
        ('unk2', 'i', 24),
        ('unk3', 'i', 36),
        ('magic1', 'i'),  # Differs between games.
        ('magic2', 'i'),  # Differs between games.
        ('dcs_name', '4s', b'DCS\0'),
        ('decompressed_size', 'I'),
        ('compressed_size', 'I'),
        ('dcp_name', '4s', b'DCP\0'),
        ('dflt_name', '4s', b'DFLT'),
        ('unk4', '6i', (32, 150994944, 0, 0, 0, 65792)),
        ('dca_name', '4s', b'DCA\0'),
        ('compressed_header_size', 'i', 8),  # TODO: asserting for now, haven't come across any variation
        byte_order='>',
    )

    def __init__(self, dcx_source, magic=()):

        self.dcx_path = None
        self.data = b''
        self.magic = magic

        if isinstance(dcx_source, str):
            self.dcx_path = dcx_source
            with open(dcx_source, 'rb') as file:
                self.unpack(file)
        elif isinstance(dcx_source, bytes):
            self.data = dcx_source

    def unpack(self, dcx_buffer):
        if self.magic:
            raise ValueError("DCX magic bytes were set manually before unpack.")
        header = self.HEADER_STRUCT.unpack(dcx_buffer)
        if header.magic1 not in {36, 68}:
            raise ValueError(f"Expected 36 or 68 at offset 0x16 but found {header.magic1}.")
        if header.magic2 not in {44, 76}:
            raise ValueError(f"Expected 36 or 68 at offset 0x20 but found {header.magic1}.")
        self.magic = (header.magic1, header.magic2)
        compressed = dcx_buffer.read().rstrip(b'\0')  # Nulls stripped from the end.
        if len(compressed) != header.compressed_size:
            # No error raised.
            print(f"WARNING: Compressed data size ({len(compressed)}) does not match size in header "
                  f"({header.compressed_size}).")
        self.data = zlib.decompressobj().decompress(compressed)
        if len(self.data) != header.decompressed_size:
            raise ValueError("Decompressed data size does not match size in header.")

    def pack(self):
        compressed = zlib.compress(self.data, level=7)
        header = self.HEADER_STRUCT.pack({
            'magic1': self.magic[0],
            'magic2': self.magic[1],
            'decompressed_size': len(self.data),
            'compressed_size': len(compressed),
        })
        return header + compressed

    def write_packed(self, dcx_path=None):
        if dcx_path is None:
            if self.dcx_path is None:
                raise ValueError("DCX path cannot be determined automatically.")
            dcx_path = self.dcx_path
        packed = self.pack()
        with open(dcx_path, 'wb') as file:
            file.write(packed)

    def write_unpacked(self, data_path=None):
        if data_path is None:
            if self.dcx_path is None:
                raise ValueError("DCX path cannot be determined automatically.")
            data_path = os.path.splitext(self.dcx_path)[0]
        with open(data_path, 'wb') as file:
            file.write(self.data)
