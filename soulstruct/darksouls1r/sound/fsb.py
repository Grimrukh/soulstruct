"""
Adapted from `DarkSouls1SoundProjects` by HotPocketRemix, with much gratitude.

`fsbext` used for extracting sound data from FSBs. Thanks to Luigi Auriemma:
    http://aluigi.altervista.org/papers/fsbext.zip
"""
from __future__ import annotations

import binascii
import copy
import logging
import subprocess as sp
import struct
import typing as tp
import uuid
from enum import IntEnum, unique
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.files import PACKAGE_PATH
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader

__all__ = ["FSB", "FSBSample", "FSBSampleHeader", "FSBHeaderVersion", "FSBHeaderMode", "FSBSampleMode", "fsbext"]

_LOGGER = logging.getLogger(__name__)


def fsbext(fsb_path: Path | str, options=""):
    """Call `fsbext.exe` with given options on `fsb_path`."""
    executable = PACKAGE_PATH("darksouls1r/sound/fsbext.exe")
    if not executable.is_file():
        raise FileNotFoundError("`fsbext.exe` is missing from Soulstruct package. Cannot extract FSB file.")
    sp.call(f"{executable} {options} {fsb_path}")


def tag(tag_name: str, value: tp.Any = ""):
    if value == "":
        return f"<{tag_name}/>"
    return f"<{tag_name}>{value}</{tag_name}>"


def new_guid() -> str:
    return f"<guid>{{{str(uuid.uuid4())}}}</guid>"


@unique
class FSBSampleMode(IntEnum):
    FSOUND_LOOP_OFF = 0x00000001
    FSOUND_LOOP_NORMAL = 0x00000002
    FSOUND_LOOP_BIDI = 0x00000004
    FSOUND_8BITS = 0x00000008
    FSOUND_16BITS = 0x00000010
    FSOUND_MONO = 0x00000020
    FSOUND_STEREO = 0x00000040
    FSOUND_UNSIGNED = 0x00000080
    FSOUND_SIGNED = 0x00000100
    FSOUND_MPEG = 0x00000200
    FSOUND_CHANNELMODE_ALLMONO = 0x00000400
    FSOUND_CHANNELMODE_ALLSTEREO = 0x00000800
    FSOUND_HW3D = 0x00001000
    FSOUND_2D = 0x00002000
    FSOUND_SYNCPOINTS_NONAMES = 0x00004000
    FSOUND_DUPLICATE = 0x00008000
    FSOUND_CHANNELMODE_PROTOOLS = 0x00010000
    FSOUND_MPEGACCURATE = 0x00020000
    FSOUND_MPEG_LAYER2 = 0x00040000
    FSOUND_HW2D = 0x00080000
    FSOUND_3D = 0x00100000
    FSOUND_32BITS = 0x00200000
    FSOUND_IMAADPCM = 0x00400000
    FSOUND_VAG = 0x00800000
    FSOUND_XMA = 0x01000000
    FSOUND_GCADPCM = 0x02000000
    FSOUND_MULTICHANNEL = 0x04000000
    FSOUND_OGG = 0x08000000
    FSOUND_MPEG_LAYER3 = 0x10000000
    FSOUND_IMAADPCMSTEREO = 0x20000000
    FSOUND_IGNORETAGS = 0x40000000
    FSOUND_SYNCPOINTS = 0x80000000


class FSBSampleHeader(BinaryObject):
    """Wavetable data that is written to the FSB file.

    Most of this information is not represented in the FDP, but comes directly from the sound sample file (WAV).
    """

    STRUCT = BinaryStruct(
        ("total_size", "H"),
        ("_name", "30s"),
        ("length", "I"),
        ("compressed_length", "I"),
        ("loop_start", "I"),
        ("loop_end", "I"),
        ("mode_flags", "I"),
        ("deffreq", "i"),
        ("defvol", "H"),
        ("defpan", "h"),
        ("defpri", "H"),
        ("channel_count", "H"),
        ("mindistance", "f"),
        ("maxdistance", "f"),
        ("size_32bits", "I"),
        ("varvol", "H"),
        ("varpan", "h"),
    )

    total_size: int
    _name: bytes
    name: str
    length: int
    compressed_length: int
    loop_start: int
    loop_end: int
    mode_flags: int
    deffreq: int
    defvol: int
    defpan: int
    defpri: int
    channel_count: int
    mindistance: float
    maxdistance: float
    size_32bits: int
    varvol: int
    varpan: int

    @property
    def name(self) -> str:
        return self._name.rstrip(b"\0").decode()

    @name.setter
    def name(self, value: str):
        if len(value) > 29:
            raise ValueError(f"`FSBSampleHeader.name` must be 29 characters or less: {value}")
        self._name = value.rstrip("\0").encode() + b"\0"

    unpack = BinaryObject.default_unpack
    pack = BinaryObject.default_pack

    def to_xml_lines(self, sample_path: Path = None) -> list[str]:
        """Convert FSB sample header to XML string for use in an FMOD Designer Project file (FDP).

        Returns a list of lines to be formatted/indented as needed by the caller.

        Args:
            sample_path: path to sample's packed file, found in corresponding FEV file (e.g. 'bank/m10/mysound.wav').
                Defaults to the name of the sample, which will probably be missing some directories in DS1.
        """
        if sample_path is not None:
            if sample_path.name != self.name:
                raise ValueError(f"Sample path '{sample_path}' does not share sample name '{self.name}'.")
        else:
            sample_path = Path(self.name)

        # All f-strings to preserve nice string alignment.
        return [
            "<waveform>",
            tag("filename", sample_path),
            new_guid(),
            tag("mindistance", self.mindistance),
            tag("maxdistance", self.maxdistance),
            tag("deffreq", self.deffreq),
            tag("defvol", self.defvol),
            tag("defpan", self.defpan),
            tag("defpri", self.defpri),
            tag("xmafiltering", "0"),
            tag("channelmode", self.compute_channel_mode()),
            tag("quality_crossplatform", "0"),
            tag("quality", "-1"),
            tag("optimisedratereduction", "100"),
            tag("enableratereduction", "1"),
            tag("notes"),
            "</waveform>",
        ]

    def compute_channel_mode(self):
        """Attempt to compute channel mode from the mode flags.

        This is not comprehensive, because this was not assumed to be needed so the channel mode is a menu index rather
        than independent of other settings.
        """
        if self.mode_flags & FSBSampleMode.FSOUND_STEREO and self.mode_flags & FSBSampleMode.FSOUND_CHANNELMODE_ALLMONO:
            return 1
        if self.mode_flags & FSBSampleMode.FSOUND_MULTICHANNEL:
            if self.mode_flags & FSBSampleMode.FSOUND_CHANNELMODE_ALLMONO:
                return 1
            if self.mode_flags & FSBSampleMode.FSOUND_CHANNELMODE_ALLSTEREO:
                return 2
            if self.mode_flags & FSBSampleMode.FSOUND_CHANNELMODE_PROTOOLS:
                return 3
        return 0


class FSBSample:

    header: FSBSampleHeader
    metadata: bytes
    data: bytes

    def __init__(self, header: FSBSampleHeader, metadata: bytes, data: bytes):
        self.header = header
        self.metadata = metadata
        self.data = data

    @classmethod
    def unpack_from(cls, reader: BinaryReader, data_offset: int):
        header = FSBSampleHeader(reader)
        metadata_size = header.total_size - FSBSampleHeader.STRUCT.size
        metadata = reader.read(metadata_size)
        with reader.temp_offset(data_offset):
            data = reader.read(header.compressed_length)
        return FSBSample(header, metadata, data)

    def __repr__(self):
        return (
            f"FSBSample(\n"
            f"    name={self.header.name},\n"
            f"    length={self.header.length},\n"
            f"    compressed_length={self.header.compressed_length},\n"
            f"    length={self.header.length},\n"
            f"    loop_start={self.header.loop_start},\n"
            f"    loop_end={self.header.loop_end},\n"
            f"    mode_flags={self.header.mode_flags},\n"
            f"    deffreq={self.header.deffreq},\n"
            f"    defvol={self.header.defvol},\n"
            f"    defpan={self.header.defpan},\n"
            f"    defpri={self.header.defpri},\n"
            f"    channel_count={self.header.channel_count},\n"
            f"    mindistance={self.header.mindistance},\n"
            f"    maxdistance={self.header.maxdistance},\n"
            f"    varvol={self.header.varvol},\n"
            f"    varpan={self.header.varpan},\n"
            f"    metadata={binascii.hexlify(self.metadata).decode()},\n"
            f")\n"
        )


@unique
class FSBHeaderMode(IntEnum):
    FORMAT = 0x01
    BASICHEADERS = 0x02
    ENCRYPTED = 0x04
    BIGENDIANPCM = 0x08
    NOTINTERLEAVED = 0x10
    MPEG_PADDED = 0x20
    MPEG_PADDED4 = 0x40


@unique
class FSBHeaderVersion(IntEnum):
    VERSION_3_0 = 0x0003_0000
    VERSION_3_1 = 0x0003_0001
    VERSION_4_0 = 0x0004_0000


class FSB(GameFile):
    """FMOD Sound Bank file, which holds the actual sound sample data."""

    version: int
    mode_flags: int
    bank_hash: int
    guid: str
    samples: list[FSBSample]

    STRUCT = BinaryStruct(
        ("signature", "4s", b"FSB4"),
        ("sample_count", "i"),
        ("sample_headers_size", "I"),
        ("sample_data_size", "I"),
        ("version", "I"),
        ("mode_flags", "I"),
        ("bank_hash", "8s"),  # unpacked as big-endian 8-bit integer manually
        ("_guid", "16s"),
    )

    BASIC_SAMPLE_STRUCT = BinaryStruct(
        ("length", "I"),
        ("compressed_length", "I"),
    )

    def unpack(self, reader: BinaryReader, **kwargs):
        data = reader.unpack_struct(self.STRUCT)
        self.version = FSBHeaderVersion(data["version"])
        self.mode_flags = data["mode_flags"]
        self.bank_hash = struct.unpack(">Q", data["bank_hash"])[0]
        self.guid = "-".join((
            data["_guid"][3::-1].hex(),  # first three chunks need to be reversed
            data["_guid"][5:3:-1].hex(),
            data["_guid"][7:5:-1].hex(),
            data["_guid"][8:10].hex(),
            data["_guid"][10:].hex(),
        ))

        data_offset = reader.position + data["sample_headers_size"]
        file_size = data_offset + data["sample_data_size"]

        self.samples = []
        for i in range(data["sample_count"]):
            if self.mode_flags & FSBHeaderMode.BASICHEADERS and i > 0:
                # Clone of first sample, with new length/compressed length information.
                sample = copy.deepcopy(self.samples[0])
                basic_sample_header = reader.unpack_struct(self.BASIC_SAMPLE_STRUCT)
                sample.header.length = basic_sample_header["length"]
                sample.header.compressed_length = basic_sample_header["length"]
            else:
                # New sample.
                sample = FSBSample.unpack_from(reader, data_offset=data_offset)
                data_offset += sample.header.compressed_length
            self.samples.append(sample)
        if data_offset != file_size:
            raise ValueError(f"Sample data end offset ({data_offset}) does not equal expected file size ({file_size}).")

    def pack(self, **kwargs) -> bytes:
        raise ValueError("FSB pack not implemented. Use FMOD Designer to build FEV/FSB from the generated FDP.")

    def __repr__(self):
        return (
            f"FSB(\n"
            f"    version={self.version},\n"
            f"    bank_hash={self.bank_hash},\n"
            f"    guid={self.guid},\n"
            f"    mode_flags={self.mode_flags},\n"
            f"    samples=<{len(self.samples)}>,\n"
            f")\n"
        )
