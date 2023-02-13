from __future__ import annotations

__all__ = [
    "BinderFlags",
    "BinderError",
    "BinderEntryNotFoundError",
    "BinderVersion",
    "BinderHeaderV3",
    "BinderHeaderV4",
    "BinderVersion4Info",
    "Binder",
]

import enum
import io
import logging
import re
import typing as tp
from pathlib import Path
from dataclasses import dataclass, field

from soulstruct.base.base_binary_file import BaseBinaryFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.files import read_json, write_json

from .binder_hash import BinderHashTable
from .dcx import DCXType, compress, decompress, is_dcx
from .entry import BinderEntry, BinderEntryFlags, BinderEntryHeader

try:
    from typing import Self
except ImportError:  # < Python 3.11
    Self = "Binder"

if tp.TYPE_CHECKING:
    from soulstruct.base.game_file import GameFile

_LOGGER = logging.getLogger(__name__)


class BinderFlags(int):
    """Bit flags for binder file. Note that the bit order is 'big endian' here.

    NOTE: 46 (00101110) appears to be the most common value by far (in PTDE, DSR, and BB at least). This:
        has_ids | has_names_1 | has_names_2 | has_compression

    TODO: Determine which file types in which games use which magic values, so they can be initialized to defaults.
    """

    @property
    def is_big_endian(self):
        return self & 0b0000_0001  # 0x80

    @property
    def has_ids(self):
        return self & 0b0000_0010  # 0x40

    @property
    def has_names_1(self):
        return self & 0b0000_0100  # 0x20

    @property
    def has_names_2(self):
        return self & 0b0000_1000  # 0x10

    @property
    def has_names(self):
        """Looks for either 'names' flag. Unsure what the difference is."""
        return self & (0b0000_0100 | 0b0000_1000)

    @property
    def has_long_offsets(self):
        return self & 0b0001_0000  # 0x08

    @property
    def has_compression(self):
        return self & 0b0010_0000  # 0x04

    @property
    def has_flag_6(self):
        return self & 0b0100_0000  # 0x02

    @property
    def has_flag_7(self):
        return self & 0b1000_0000  # 0x01

    @classmethod
    def from_byte(cls, byte_value: int, bit_big_endian: bool) -> BinderFlags:
        """Read a byte, reverse it if necessary, and return flags integer."""
        flags = cls(byte_value)
        if not bit_big_endian and not (flags.is_big_endian and not flags.has_flag_7):
            # Reverse bit order.
            flags = cls(int(f"{flags:08b}"[::-1], 2))
        return flags

    def to_byte(self, bit_big_endian: bool) -> int:
        if not bit_big_endian and not (self.is_big_endian and not self.has_flag_7):
            return int(f"{self:08b}"[::-1], 2)
        return int(self)

    def get_bnd_entry_header_size(self) -> int:
        """Calculate binder entry header size."""
        size = 16  # Base size.
        if self.has_ids:
            size += 4
        if self.has_names_1 or self.has_names_2:
            size += 4
        if self.has_compression:
            size += 8
        size += 8 if self.has_long_offsets else 4
        return size


class BinderError(Exception):
    pass


class BinderEntryNotFoundError(BinderError, KeyError):
    """Raised when a `BinderEntry` is not found.

    Subclass of `KeyError` for legacy compatibility.
    """


BinderSourceTyping = tp.Union[str, Path, bytes, bytearray, BinderEntry, io.BufferedIOBase, BinaryReader]
T = tp.TypeVar("T", bound="BaseBinder")


class BinderVersion(enum.Enum):
    """Version used for BND and BXF files."""
    V3 = 3  # used before Dark Souls 2 (2014)
    V4 = 4  # used from Dark Souls 2 (2014) onwards


@dataclass(slots=True)
class BinderHeaderV3(NewBinaryStruct):
    _version: bytes = field(init=False, **Binary(length=4, asserted=b"BND3"))
    signature: str = field(**Binary(length=8, encoding="ASCII", rstrip_null=True))
    flags: byte
    big_endian: bool
    bit_big_endian: bool
    _pad1: bytes = field(init=False, **BinaryPad(1))
    entry_count: int
    file_size: int
    _pad2: bytes = field(init=False, **BinaryPad(8))

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian


@dataclass(slots=True)
class BinderHeaderV4(NewBinaryStruct):
    _version: bytes = field(init=False, **Binary(length=4, asserted=b"BND4"))
    unknown1: bool
    unknown2: bool
    _pad1: bytes = field(init=False, **BinaryPad(3))
    big_endian: bool
    bit_little_endian: bool
    _pad2: bytes = field(init=False, **BinaryPad(1))
    _entry_count: int
    _header_size: long = field(init=False, **Binary(asserted=0x40))
    signature: str = field(**Binary(length=8, encoding="ASCII", rstrip_null=True))
    _entry_header_size: long
    _data_offset: long
    unicode: bool
    flags: byte
    hash_table_type: byte = field(**Binary(asserted=[0, 1, 4, 128]))
    _pad3: bytes = field(init=False, **BinaryPad(5))
    _hash_table_offset: long  # only non-zero if `hash_table_type = 4`

    def get_default_byte_order(self) -> ByteOrder:
        return ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian


@dataclass(slots=True)
class BDTHeaderV3(NewBinaryStruct):
    _version: bytes = field(init=False, **Binary(length=4, asserted=b"BDF3"))
    signature: str = field(**Binary(length=8, encoding="ASCII", rstrip_null=True))
    _pad1: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True)
class BDTHeaderV4(NewBinaryStruct):
    _version: bytes = field(init=False, **Binary(length=4, asserted=b"BDT4"))
    unknown1: bool
    unknown2: bool
    _pad1: bytes = field(init=False, **BinaryPad(3))
    big_endian: bool
    bit_little_endian: bool
    _pad2: bytes = field(init=False, **BinaryPad(5))
    _header_size: long = field(init=False, **Binary(asserted=0x30))
    signature: str = field(**Binary(length=8, encoding="ASCII", rstrip_null=True))
    _pad3: bytes = field(init=False, **BinaryPad(16))


@dataclass(slots=True)
class BinderVersion4Info:
    """Defaults are simply the most common observed values."""
    unknown1: bool = False
    unknown2: bool = False
    unicode: bool = True
    hash_table_type: int = 0

    most_recent_hash_table: bytes = field(init=False, repr=False, default=b"")
    most_recent_entry_count: int = field(init=False, repr=False, default=0)
    most_recent_paths: list[str] = field(init=False, repr=False, default_factory=list)


@dataclass(slots=True)
class Binder(BaseBinaryFile):
    """Collection of files, with their own internal IDs, paths, and flags, glued together into one file on disk.

    The binder can be a `BND` file, which contains the entry headers and data together, or split into a `BHD` (BHF
    byte signature) entry header file and `BDT` (BDF byte signature) entry data file. The formats are basically
    identical in both cases; they are simply split up for the `BXF` file (with a useless copied header in the BDT). The
    `is_split_bxf` bool field determines whether the loaded binder came from these split files.

    There are currently two supported binder versions: V3 (prior to Dark Souls 2) and V4 (Dark Souls 2 onwards). V4
    binders have some extra information in them and can optionally have UTF-16 path encoding and hash tables generated
    from the entry paths.

    Binders can be written as unpacked folders (similar to Yabber by TKGP) which contain `binder_manifest.json` files
    detailing all the contained entries. Where possible, these unpacked files do NOT use nested directories, but instead
    have their directory trees (from their entry paths) recorded in the manifest.

    TODO: Support 'auto scanning' unpacked folders, so you don't have to edit the manifest manually when adding or
     removing files from the binder. Just need to supply some rule that maps file name patterns to (sequences of) IDs.

    This class is subclassed by numerous Python classes that handle particular binders, such as `GameParamBND`.
    """

    # Enforced name of manifest file.
    MANIFEST_NAME: tp.ClassVar[str] = "binder_manifest.json"

    # Binder entry path encoding.
    # NOTE: Binder entry paths are *not* encoded in `shift_jis_2004`, unlike most other strings, but are just
    # `shift-jis`. The relevant difference is that escaped backslashes are decoded to the yen symbol in
    # `shift_jis_2004`, which we do not want in these files.
    ENTRY_PATH_ENCODING: tp.ClassVar[str] = "shift-jis"

    # Default `BinderEntry.flags` to use when creating new entries with `Binder` utility methods.
    # Default is the most common observed value by far.
    DEFAULT_ENTRY_FLAGS: tp.ClassVar[BinderEntryFlags] = BinderEntryFlags(0x2)

    signature: str = "07D7R6"
    flags: BinderFlags = BinderFlags(0b00101110)  # most common flags by far (IDs, names1, names2, compression)
    big_endian: bool = False
    bit_big_endian: bool = False
    version: BinderVersion = BinderVersion.V4  # default geared for newer games
    v4_info: BinderVersion4Info | None = field(default_factory=BinderVersion4Info)  # only used by `BinderVersion.V4`
    is_split_bxf: bool = False  # NOTE: not included in manifest (inferred from combined `binder_type` string in there)

    entries: list[BinderEntry] = field(default_factory=list)

    # NOTE: Standard `from_dict()` class method will attempt to interpret actual entry content from the dictionary, i.e.
    # a bonafide full JSON version of the entire binder. Use `from_unpacked_path()` to load an unpacked directory or
    # manifest JSON inside one.

    # region Read Methods

    @classmethod
    def from_bytes(
        cls,
        data: bytes | bytearray | tp.BinaryIO | BinaryReader | BinderEntry,
        bdt_data: bytes | bytearray | tp.BinaryIO | BinaryReader | BinderEntry | None = None,
    ) -> Self:
        """Load `Binder` from just `data` (BND file) or split `data` and `bdt_data` (BXF file)."""
        reader = BinaryReader(data) if not isinstance(data, BinaryReader) else data  # type: BinaryReader

        if is_dcx(reader):
            try:
                data, dcx_type = decompress(reader)
            finally:
                reader.close()
            reader = BinaryReader(data)
        else:
            dcx_type = DCXType.Null

        if bdt_data is None:
            # BND file.
            try:
                instance = cls.from_reader(reader)
                instance.dcx_type = dcx_type
            except Exception:
                _LOGGER.error(f"Error occurred while reading `{cls.__name__}` from binary data. See traceback.")
                raise
            finally:
                reader.close()
            return instance

        bdt_reader = BinaryReader(bdt_data) if not isinstance(bdt_data, BinaryReader) else bdt_data

        if is_dcx(bdt_reader):
            try:
                bdt_data, bdt_dcx_type = decompress(bdt_reader)
            finally:
                bdt_reader.close()
            bdt_reader = BinaryReader(bdt_data)
        else:
            bdt_dcx_type = DCXType.Null

        if dcx_type != bdt_dcx_type:
            raise ValueError(f"BHD and BDT files have different DCX compression: {dcx_type} vs. {bdt_dcx_type}")

        try:
            instance = cls.from_reader(reader, bdt_reader)
            instance.dcx_type = dcx_type
        except Exception:
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` from binary data. See traceback.")
            raise
        finally:
            reader.close()
            bdt_reader.close()

        return instance

    @classmethod
    def from_path(cls, path: str | Path, bdt_path: str | Path | None = None) -> Self:
        path = Path(path)
        reader = BinaryReader(path)
        first_four_bytes = reader.peek(4)

        if first_four_bytes == b"DCX\0":
            # Unpack DCX now and assign `dcx_type` manually below (so we don't do it again in `from_reader()`).
            try:
                data, dcx_type = decompress(reader)
            finally:
                reader.close()
            reader = BinaryReader(data)
            first_four_bytes = reader.peek(4)
        else:
            dcx_type = None  # will not be assigned

        if first_four_bytes[:3] == b"BHF":
            if bdt_path is None:
                # Try to auto-detect BDT file next to `path`.
                name_parts = path.name.split(".")
                bdt_name = name_parts[0] + "." + ".".join(name_parts[1:]).replace("bhd", "bdt")
                if bdt_name == path.name:
                    raise ValueError(f"Could not guess name of BDT file from BHD file: {path}")
                bdt_path = path.with_name(bdt_name)
                if not bdt_path.is_file():
                    raise FileNotFoundError(f"Could not find BDT data file next to BHD header file: {bdt_path}")
            bdt_reader = BinaryReader(bdt_path)
        elif first_four_bytes[:3] == b"BND":
            if bdt_path is not None:
                raise ValueError("Cannot pass in `bdt_path` when `path` is a BND file.")
            bdt_reader = None
        else:
            raise ValueError(f"Cannot detect `Binder` file type from first four bytes: {first_four_bytes}")

        try:
            binder = cls.from_bytes(reader, bdt_reader)
        except Exception:
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` with path '{path}'. See traceback.")
            raise
        binder.path = path
        if dcx_type is not None:
            binder.dcx_type = dcx_type
        return binder

    @classmethod
    def from_reader(cls, reader: BinaryReader, bdt_reader: BinaryReader | None = None) -> Self:
        version_bytes = reader.peek(4)

        if version_bytes[:3] == b"BHF":
            if bdt_reader is None:
                raise ValueError("BDT reader required to load split BHD/BDT binder.")
            entry_reader = bdt_reader
            # Skip useless BDT header.
            if version_bytes[3] == b"3":
                entry_reader.read(0x10)
            elif version_bytes[3] == b"4":
                entry_reader.read(0x30)
            else:
                raise ValueError(f"Unsupported BHD/BDT version: {version_bytes}")
        else:
            entry_reader = reader  # headers and entries in same file

        if version_bytes in {b"BND3", b"BHF3"}:
            binder, entry_headers = cls._read_header_v3(reader)
        elif version_bytes in {b"BND4", b"BHF4"}:
            binder, entry_headers = cls._read_header_v4(reader)
        else:
            raise ValueError(f"Could not detect BND version from first four bytes: {version_bytes}:")

        binder.entries = [BinderEntry.from_header(entry_reader, entry_header) for entry_header in entry_headers]
        if binder.v4_info:
            # Set existing V4 hash properties.
            binder.v4_info.most_recent_entry_count = len(binder.entries)
            binder.v4_info.most_recent_paths = [entry.path for entry in binder.entries]

        return binder

    @classmethod
    def _read_header_v3(cls, reader: BinaryReader) -> tuple[Self, list[BinderEntryHeader]]:
        # Test for endianness is a little complicated, as `flags.is_big_endian` can override the header `big_endian`.
        big_endian, bit_big_endian = reader.unpack("??", offset=0xD)
        flags_fmt = ">B" if bit_big_endian else "<B"
        flags = BinderFlags.from_byte(reader.unpack_value(flags_fmt, offset=0xC), bit_big_endian)
        byte_order = ByteOrder.BigEndian if (big_endian or flags.is_big_endian) else ByteOrder.LittleEndian

        header_struct = BinderHeaderV3.from_bytes(reader, byte_order=byte_order)

        entry_headers = [
            BinderEntryHeader.from_reader_v3(reader, flags, header_struct.bit_big_endian)
            for _ in range(header_struct.entry_count)
        ]

        binder = cls(
            signature=header_struct.signature,
            big_endian=big_endian,
            bit_big_endian=bit_big_endian,
            entries=[],  # assigned later
            version=BinderVersion.V3,
            v4_info=None,
        )
        return binder, entry_headers

    @classmethod
    def _read_header_v4(cls, reader: BinaryReader) -> tuple[Self, list[BinderEntryHeader]]:
        """Less endian complexity than V3."""
        byte_order = BinaryCondition(
            (0x9, 1), [(ByteOrder.BigEndian, b"\01"), (ByteOrder.LittleEndian, b"\00")]
        )(reader)
        reader.default_byte_order = byte_order
        header_struct = BinderHeaderV4.from_bytes(reader, byte_order=byte_order)  # type: BinderHeaderV4

        flags = BinderFlags.from_byte(header_struct.flags, not header_struct.bit_little_endian)
        flags_header_size = flags.get_bnd_entry_header_size()

        _entry_header_size = header_struct.pop("_entry_header_size")
        _hash_table_offset = header_struct.pop("_hash_table_offset")
        _entry_count = header_struct.pop("_entry_count")
        _data_offset = header_struct.pop("_data_offset")

        if _entry_header_size != flags_header_size:
            raise ValueError(
                f"Expected BND entry header size {flags_header_size} based on flags\n"
                f"{flags:08b}, but BND header says {_entry_header_size}."
            )

        if header_struct.hash_table_type != 4 and _hash_table_offset != 0:
            _LOGGER.warning(
                f"Found non-zero hash table offset {_hash_table_offset}, but header says this Binder has "
                f"no hash table."
            )

        entry_headers = [
            BinderEntryHeader.from_reader_v4(reader, flags, not header_struct.bit_little_endian, header_struct.unicode)
            for _ in range(_entry_count)
        ]

        v4_info = header_struct.to_object(BinderVersion4Info)

        if v4_info.hash_table_type == 4:
            # Save the initial hash table (found in header).
            reader.seek(_hash_table_offset)
            v4_info.most_recent_hash_table = reader.read(_data_offset - _hash_table_offset)

        binder = cls(
            signature=header_struct.signature,
            flags=flags,
            big_endian=header_struct.big_endian,
            bit_big_endian=not header_struct.bit_little_endian,  # REVERSED
            entries=[],  # assigned later
            version=BinderVersion.V4,
            v4_info=v4_info,
        )

        return binder, entry_headers

    @classmethod
    def from_unpacked_path(cls, path: str | Path) -> Self:
        """Load manifest JSON or unpacked directory containing a manifest JSON."""
        path = Path(path)
        if path.is_dir():
            directory = path
            manifest_path = directory / cls.MANIFEST_NAME
            if not manifest_path.exists():
                raise FileNotFoundError(f"Binder manifest JSON file not found: {manifest_path}")
        elif path.name == cls.MANIFEST_NAME:
            directory = path.parent
            manifest_path = path
        else:
            raise ValueError(
                f"Invalid file source for `{cls.__name__}`: {path}. Must be a manifest JSON file or unpacked folder "
                f"containing one."
            )
        manifest = read_json(manifest_path, encoding="shift-jis")
        manifest = cls.process_manifest_header(manifest)
        entry_dicts = manifest.pop("entries")
        use_id_prefix = manifest.pop("use_id_prefix")
        binder = cls.from_dict(manifest)
        binder.add_entries_from_manifest(entry_dicts, directory, use_id_prefix)
        if directory.suffix == ".unpacked":  # only this suffix is automatically removed
            binder.path = directory.with_name(directory.name[:-9])
        else:
            binder.path = directory  # writing this path will conflict with this unpacked folder source
        return binder

    @classmethod
    def process_manifest_header(cls, manifest: dict) -> dict[str, tp.Any]:
        """Parse manifest dictionary and return a dictionary that can be passed to `Binder.from_dict()`.

        Does not modify input `manifest`. Other keys may be present in `manifest`, and will be ignored.
        """
        binder_kwargs = manifest.copy()
        for required_key in ("binder_type", "signature", "flags", "big_endian", "bit_big_endian"):
            if required_key not in binder_kwargs:
                raise BinderError(f"Binder manifest JSON file does not contain '{required_key}' key.")

        binder_type = binder_kwargs.pop("binder_type")
        if binder_type[:3] == "BXF":
            is_split_bxf = True
        elif binder_type[:3] == "BND":
            is_split_bxf = False
        else:
            raise ValueError(
                f"Invalid Binder manifest `binder_type`: {binder_type}. Must be of format '{{BND|BXF}}{{3|4}}'."
            )
        version = int(binder_type[3])
        if version not in {3, 4}:
            raise ValueError(
                f"Invalid Binder manifest `binder_type`: {binder_type}. Must be of format '{{BND|BXF}}{{3|4}}'."
            )
        binder_kwargs["is_split_bxf"] = is_split_bxf
        binder_kwargs["version"] = version
        binder_kwargs["flags"] = BinderFlags(manifest["flags"])
        binder_kwargs["dcx_type"] = DCXType(manifest["dcx_type"])
        return binder_kwargs

    # endregion

    # region Write Methods

    def write(
        self,
        file_path: None | str | Path = None,
        bdt_file_path: None | str | Path = None,
        make_dirs=True,
        check_hash=False,
    ):
        """Writes both the `BHD` and `BDT` files at once.

        Missing directories in given path will be created automatically if `make_dirs` is True. Otherwise, they must
        already exist.

        Will compress with DCX automatically and add `.dcx` file extension if `.dcx_type` is defined. Will also
        automatically create a `.bak` version of the `file_path`, if a backup does not already exist.

        Args:
            file_path (None, str, Path): file path to write `BHD` to. Defaults to `self.path`, which is automatically
                set at instance creation if a file path is used as a source.
            bdt_file_path (None, str, Path): file path to write `BDT` to. Defaults to `self.path` with "bdt"
                replacing "bhd", if a file path is used as a source.
            make_dirs (bool): if True, any absent directories in both `file_path` and `bdt_file_path` will be created.
            check_hash (bool): if True, files will not be written if both BHD and BDT files with same hashes already
                exist. (Default: False)
        """
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)

        if self.is_split_bxf:
            if bdt_file_path is None:
                # Auto-set BDT path.
                name_parts = file_path.name.split(".")
                bdt_name = name_parts[0] + "." + ".".join(name_parts[1:]).replace("bhd", "bdt")
                bdt_file_path = file_path.with_name(bdt_name)
            elif make_dirs:  # only needed if not next to BHD file (as will be the case above)
                bdt_file_path.parent.mkdir(parents=True, exist_ok=True)
            packed_bhd, packed_bdt = self.get_split_bytes()
            if check_hash and file_path.is_file() and bdt_file_path.is_file():
                bhd_match = get_blake2b_hash(file_path) == get_blake2b_hash(packed_bhd)
                bdt_match = get_blake2b_hash(bdt_file_path) == get_blake2b_hash(packed_bdt)
                if bhd_match and bdt_match:
                    return  # don't write files (both match)
            self.create_bak(file_path, make_dirs=make_dirs)
            self.create_bak(bdt_file_path, make_dirs=make_dirs)
            with file_path.open("wb") as f:
                f.write(packed_bhd)
            with bdt_file_path.open("wb") as f:
                f.write(packed_bdt)
        else:
            if bdt_file_path is not None:
                raise ValueError("Cannot pass in `bdt_file_path` when `Binder.is_split_bxf == False`.")
            super(Binder, self).write(file_path, make_dirs=make_dirs, check_hash=check_hash)

    def write_split(
        self,
        bhd_path_or_entry: None | str | Path | BinderEntry,
        bdt_path_or_entry: None | str | Path | BinderEntry,
        make_dirs=True,
        check_hash=False,
    ):
        """Writes both the `BHD` and `BDT` files at once, but also supports writing their data into an existing
        `BinderEntry`. Most useful for split 'CHRTPFBHD/BDT' files in `chr` folders, where the BHD header file is
        inside the `chrbnd` but the BDT file is a real file sitting next to it.

        Note that any `BinderEntry` written into will still need to be written separately.

        Missing directories in given path will be created automatically if `make_dirs` is True. Otherwise, they must
        already exist.

        Will compress with DCX automatically and add `.dcx` file extension if `.dcx_type` is defined. Will also
        automatically create a `.bak` version of the `file_path`, if a backup does not already exist.

        Args:
            bhd_path_or_entry (None, str, Path, BinderEntry): file path or `BinderEntry` to write `BHD` to.
            bdt_path_or_entry (None, str, Path, BinderEntry): file path or `BinderEntry` to write `BDT` to.
            make_dirs (bool): if True, any absent directories in either path will be created.
            check_hash (bool): if True, files will not be written if both BHD and BDT files with same hashes already
                exist. (Default: False)
        """

        packed_bhd, packed_bdt = self.get_split_bytes()

        for path_or_entry, packed in zip((bhd_path_or_entry, bdt_path_or_entry), (packed_bhd, packed_bdt)):
            if isinstance(path_or_entry, (str, Path)):
                path_or_entry = Path(path_or_entry)
                if make_dirs:
                    path_or_entry.parent.mkdir(parents=True, exist_ok=True)
                if check_hash and path_or_entry.is_file():
                    bhd_match = get_blake2b_hash(path_or_entry) == get_blake2b_hash(packed)
                    if not bhd_match:
                        self.create_bak(path_or_entry, make_dirs=make_dirs)
                        path_or_entry.write_bytes(packed)
                else:
                    self.create_bak(path_or_entry, make_dirs=make_dirs)
                    path_or_entry.write_bytes(packed)
            elif isinstance(path_or_entry, BinderEntry):
                path_or_entry.set_uncompressed_data(packed)

    def __bytes__(self) -> bytes:
        """Only permitted when `is_split_bxf == False`.

        Applies `dcx_type` DCX automatically.
        """
        if self.is_split_bxf:
            raise TypeError(
                "Cannot convert split BXF binder (`is_split_bxf=True`) to single `bytes`. Use `get_split_bytes()` to "
                "return a tuple of two `bytes` objects."
            )
        return super(Binder, self).__bytes__()

    def get_split_bytes(self) -> tuple[bytes, bytes]:
        """Applies `dcx_type` DCX automatically.

        NOTE: I haven't ever actually seen a BHD/BDT file with DCX. Generally the entries have it instead.
        """
        bhd_writer, bdt_writer = self._to_split_writers()
        packed_bhd = bytes(bhd_writer)
        packed_bdt = bytes(bdt_writer)
        if self.dcx_type != DCXType.Null:
            packed_bhd = compress(packed_bhd, self.dcx_type)
            packed_bdt = compress(packed_bdt, self.dcx_type)
        return packed_bhd, packed_bdt

    def to_writer(self) -> BinaryWriter:
        if self.is_split_bxf:
            raise TypeError(
                "Cannot write split BXF binder (`is_split_bxf=True`) with singular `_to_writer()`. Use "
                "`get_split_bytes()` to return a tuple of two `bytes` objects or `write()`/`write_split()` to write "
                "the two split BHD/BDT files directly."
            )

        if self.version == BinderVersion.V3:
            writer = self._header_to_writer_v3()
            self._entries_into_writer_v3(writer, writer)
        elif self.version == BinderVersion.V4:
            writer = self._header_to_writer_v4()
            rebuild_hash_table = self._check_v4_hash_table() if self.v4_info.hash_table_type == 4 else False
            self._entries_into_writer_v4(writer, writer, rebuild_hash_table)
        else:
            raise ValueError(f"Cannot pack BND version: {self.version}")

        return writer

    def _to_split_writers(self) -> tuple[BinaryWriter, BinaryWriter]:
        if not self.is_split_bxf:
            _LOGGER.warning("Calling `_to_writer_split()` on `Binder` with `is_split_bxf=False`, which is unusual.")

        if self.version == BinderVersion.V3:
            header_writer = self._header_to_writer_v3()
            entry_writer = BDTHeaderV3.object_to_writer(self, byte_order=header_writer.default_byte_order)
            self._entries_into_writer_v3(header_writer, entry_writer)
        elif self.version == BinderVersion.V4:
            header_writer = self._header_to_writer_v4()
            rebuild_hash_table = self._check_v4_hash_table() if self.v4_info.hash_table_type == 4 else False
            entry_writer = BDTHeaderV4.object_to_writer(self, byte_order=header_writer.default_byte_order)
            self._entries_into_writer_v4(header_writer, entry_writer, rebuild_hash_table)
        else:
            raise ValueError(f"Cannot pack BND version: {self.version}")

        return header_writer, entry_writer

    def _header_to_writer_v3(self) -> BinaryWriter:

        return BinderHeaderV3(
            signature=self.signature,
            flags=byte(self.flags.to_byte(self.bit_big_endian)),
            big_endian=self.big_endian,
            bit_big_endian=self.bit_big_endian,
            entry_count=len(self.entries),
            file_size=RESERVED,
        ).to_writer(reserve_obj=self)

    def _entries_into_writer_v3(self, header_writer: BinaryWriter, entry_writer: BinaryWriter):
        """Write entries into given `entry_writer` and fill offsets in `header_writer`.

        NOTE: Both writers should be the same for BND files.
        """

        sorted_entries = list(sorted(self.entries, key=lambda e: e.id))
        sorted_entry_headers = [entry.get_header(self.flags) for entry in sorted_entries]
        for entry_header in sorted_entry_headers:
            entry_header.into_bnd3_writer(entry_writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            for entry, entry_header in zip(sorted_entries, sorted_entry_headers):
                packed_path = entry.get_packed_path(encoding=self.ENTRY_PATH_ENCODING)
                entry_header.pack_path(header_writer, entry_writer, packed_path)

        for entry, entry_header in zip(sorted_entries, sorted_entry_headers):
            entry_header.pack_path(header_writer, entry_writer, entry.data)

        header_writer.fill("_file_size", entry_writer.position, obj=self)

    def _header_to_writer_v4(self) -> BinaryWriter:

        if self.v4_info is None:
            raise AttributeError("`Binder version `V4` must have a `v4_info`.")

        return BinderHeaderV4(
            unknown1=self.v4_info.unknown1,
            unknown2=self.v4_info.unknown2,
            big_endian=self.big_endian,
            bit_little_endian=not self.bit_big_endian,  # REVERSED
            _entry_count=len(self.entries),
            signature=self.signature,
            _entry_header_size=long(self.flags.get_bnd_entry_header_size()),
            _data_offset=RESERVED,
            unicode=self.v4_info.unicode,
            flags=byte(self.flags.to_byte(self.bit_big_endian)),
            hash_table_type=byte(self.v4_info.hash_table_type),
            _hash_table_offset=RESERVED,  # only non-zero for hash table type 4
        ).to_writer(reserve_obj=self)

    def _check_v4_hash_table(self) -> bool:
        if self.v4_info is None:
            raise AttributeError("`Binder version `V4` must have a `v4_info`.")

        rebuild_hash_table = not self.v4_info.most_recent_hash_table

        if not self.v4_info.most_recent_hash_table or len(self.entries) != self.v4_info.most_recent_entry_count:
            rebuild_hash_table = True
        else:
            # Check if any entry paths have changed.
            for i, entry in enumerate(self.entries):
                if entry.path != self.v4_info.most_recent_paths[i]:
                    rebuild_hash_table = True
                    break

        self.v4_info.most_recent_entry_count = len(self.entries)
        self.v4_info.most_recent_paths = [entry.path for entry in self.entries]

        return rebuild_hash_table

    def _entries_into_writer_v4(
        self, header_writer: BinaryWriter, entry_writer: BinaryWriter, rebuild_hash_table=False
    ):
        """Write entries into given `entry_writer` and fill offsets in `header_writer`.

        NOTE: Both writers should be the same for BND files.
        """

        sorted_entries = list(sorted(self.entries, key=lambda e: e.id))
        sorted_entry_headers = [entry.get_header(self.flags) for entry in sorted_entries]
        for entry_header in sorted_entry_headers:
            entry_header.into_bnd4_writer(entry_writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            path_encoding = entry_writer.get_utf_16_encoding() if self.v4_info.unicode else self.ENTRY_PATH_ENCODING
            for entry, entry_header in zip(sorted_entries, sorted_entry_headers):
                entry_header.pack_path(header_writer, entry_writer, entry.get_packed_path(encoding=path_encoding))

        if self.v4_info.hash_table_type == 4:
            header_writer.fill_with_position("_hash_table_offset", obj=self)
            if rebuild_hash_table:
                header_writer.append(BinderHashTable.build_hash_table(self.entries))
            else:
                header_writer.append(self.v4_info.most_recent_hash_table)
        else:
            header_writer.fill("_hash_table_offset", 0, obj=self)

        header_writer.fill("_data_offset", entry_writer.position, obj=self)

        for entry, entry_header in zip(sorted_entries, sorted_entry_headers):
            # Ten pad bytes between entries (for byte-perfect writes).
            entry_header.pack_path(header_writer, entry_writer, entry.data + b"\0" * 10)

    def get_manifest_header(self) -> dict[str, tp.Any]:
        """Construct manifest header dictionary depending on file type."""
        binder_type = f"BXF{self.version.value}" if self.is_split_bxf else f"BND{self.version.value}"
        manifest = {
            "binder_type": binder_type,
            "signature": self.signature,
            "flags": self.flags,
            "big_endian": self.big_endian,
            "bit_big_endian": self.bit_big_endian,
        }
        if self.version == BinderVersion.V4:
            if self.v4_info is None:
                raise AttributeError("`Binder` with version `V4` must have a `v4_info`.")
            manifest |= {
                "unknown1": self.v4_info.unknown1,
                "unknown2": self.v4_info.unknown2,
                "unicode": self.v4_info.unicode,
                "hash_table_type": self.v4_info.hash_table_type,
            }

        # Final keys (more metadata than real binder data).
        manifest |= {
            "use_id_prefix": self.has_repeated_entry_names,
            "dcx_type": self.dcx_type.name,
        }
        return manifest

    def write_unpacked_directory(self, directory: str | Path | None = None):
        if not self.flags.has_names:
            raise NotImplementedError(
                "Writing unpacked binder directories is only supported for binder formats with path strings."
            )
        if directory is None:
            if self.path:
                directory = self.path.with_suffix(self.path.suffix + ".unpacked")
            else:
                raise ValueError("Cannot detect `directory` for unpacked binder automatically.")
        else:
            directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)

        entry_tree_dict = {}
        use_index_prefix = self.has_repeated_entry_names

        for i, entry in enumerate(self.entries):
            entry_directory = str(Path(entry.path).parent)  # no trailing backslash
            entry_dict = {"flags": entry.flags, "id": entry.entry_id if self.flags.has_ids else i, "name": entry.name}
            entry_tree_dict.setdefault(entry_directory, []).append(entry_dict)
            entry_file_name = f"__{entry.entry_id}__{entry.name}" if use_index_prefix else entry.name
            with (directory / entry_file_name).open("wb") as f:
                f.write(entry.data)

        json_dict = self.get_manifest_header()
        json_dict["entries"] = entry_tree_dict

        # NOTE: Binder manifest is always encoded in shift-JIS, not `shift_jis_2004`.
        write_json(directory / "binder_manifest.json", json_dict, encoding="shift-jis")

    def to_dict(self) -> dict:
        raise TypeError("Base `Binder` cannot be written to dictionary. Use `write_unpacked_directory()` instead.")

    # endregion

    # region Entry Management

    def add_entries_from_manifest(self, entries: dict, directory: str | Path, use_id_prefix: bool):
        directory = Path(directory)
        unsorted_entries = {}  # maps ID to `(path, data, flags)` tuple
        for root, entry_dicts in entries.items():
            for entry in entry_dicts:
                find_entry_basename = f"__{entry['id']}__{entry['name']}" if use_id_prefix else entry['name']
                with (directory / find_entry_basename).open("rb") as entry_file:
                    entry_data = entry_file.read()
                unsorted_entries[entry['id']] = (f"{root}\\{entry['name']}", entry_data, entry['flags'])
        for entry_id, (path, data, flags) in sorted(unsorted_entries.items()):
            self.add_entry(BinderEntry(entry_id=entry_id, path=path, data=data, flags=flags))

    def add_entry(self, entry: BinderEntry):
        if entry in self.entries:
            raise BinderError(f"Given `BinderEntry` instance with ID {entry.entry_id} is already in this binder.")
        if entry.entry_id in self.entries_by_id:
            _LOGGER.warning(f"Entry ID {entry.entry_id} appears more than once in this binder. You should fix this!")
        self.entries.append(entry)

    def remove_entry(self, entry: BinderEntry):
        if entry not in self.entries:
            raise KeyError(f"Entry `{entry}` is not in this Binder. Cannot remove it.")
        self.entries.remove(entry)

    def remove_entry_id(self, entry_id: int) -> BinderEntry:
        entry = self.entries_by_id[entry_id]
        self.entries.remove(entry)
        return entry

    def remove_entry_path(self, entry_path: Path | str):
        entry = self.entries_by_path[str(entry_path)]
        self.entries.remove(entry)
        return entry

    def remove_entry_name(self, entry_name: str):
        entry = self.entries_by_name[entry_name]
        self.entries.remove(entry)
        return entry

    def clear_entries(self):
        """Remove all entries from the BND."""
        self.entries.clear()

    # endregion

    @property
    def entries_by_id(self) -> dict[int, BinderEntry]:
        """Dictionary mapping entry IDs to entries.

        If there are multiple entries with the same ID in the BND, this will raise a `BinderError`. This should never
        happen; if it does, fix it by accessing the culprit entries with `.entries` and changing one or more IDs.
        """
        entries = {}
        for entry in self.entries:
            if entry.entry_id in entries:
                raise BinderError(f"There are multiple entries with ID {entry.entry_id}.")
            entries[entry.entry_id] = entry
        return entries

    @property
    def entries_by_path(self) -> dict[str, BinderEntry]:
        """Dictionary mapping entry paths to (classed) entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this property will raise a `BinderError`.
        """
        entries = {}
        for entry in self.entries:
            if entry.path in entries:
                raise BinderError(f"Path '{entry.path}' appears in multiple `BNDEntry` paths.")
            entries[entry.path] = entry
        return entries

    @property
    def entries_by_name(self) -> dict[str, BinderEntry]:
        """Dictionary mapping entry basenames to (classed) entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this property will raise an exception.
        """
        entries = {}
        for entry in self.entries:
            if entry.name in entries:
                raise ValueError(f"Basename '{entry.name}' appears in multiple BND entry paths.")
            entries[entry.name] = entry
        return entries

    @property
    def entry_count(self) -> int:
        return len(self.entries)

    @property
    def highest_entry_id(self) -> int | None:
        """Returns largest `entry_id` of all current entries. Useful for calculating a new ID in most cases.

        Returns `None` if there are no entries.
        """
        if not self.entries:
            return None
        return max(entry.entry_id for entry in self.entries)

    @property
    def has_repeated_entry_names(self):
        entry_names = [e.name for e in self.entries]
        return len(set(entry_names)) < len(entry_names)

    def get_first_new_entry_id_in_range(self, min_id_inclusive: int, max_id_exclusive: int) -> int:
        """Get the first new entry ID available in the given half-open range."""
        if not self.entries:
            return min_id_inclusive
        entries_by_id = self.entries_by_id
        for entry_id in range(min_id_inclusive, max_id_exclusive):
            if entry_id not in entries_by_id:
                return entry_id
        raise BinderEntryNotFoundError(
            f"No entry ID in the range [{min_id_inclusive}, {max_id_exclusive}) is available."
        )

    def find_entries_matching_name(self, regex: str | re.Pattern) -> list[BinderEntry]:
        """Returns a list of entries whose names match the given `regex` pattern."""
        return [entry for entry in self.entries if re.match(regex, entry.name)]

    def find_entry_matching_name(self, regex: str | re.Pattern) -> BinderEntry:
        """Returns a single entry whose name matches the given `regex` pattern.

        Only one match must exist.
        """
        matches = [entry for entry in self.entries if re.match(regex, entry.name)]
        if len(matches) > 1:
            raise ValueError(f"Found multiple Binder entries with name matching '{regex}'.")
        if not matches:
            raise BinderEntryNotFoundError(f"No Binder entries found with name matching '{regex}'.")
        return matches[0]

    @classmethod
    def get_default_entry_path(cls, entry_name: str) -> str:
        """Optional method that can be overridden (usually by a game subclass) to generate a full entry path."""
        raise BinderError("`get_default_entry_path()` not defined on this `Binder` class/subclass.")

    def get_default_entry_id(self, entry_name: str) -> int:
        """Method that can be overridden (usually by a game subclass) to generate a full entry path.
        
        Default method simply returns the ID after the highest currently ID (which may leave gaps in earlier ranges).
        """
        return self.highest_entry_id + 1

    def add_or_replace_entry_name(
        self, entry_name: str, game_file: GameFile, new_entry_id: int = None, new_entry_flags: BinderFlags = None
    ):
        """Create or replace `BinderEntry` with name `entry_name` using data from packed `game_file`.
        
        If `entry_name` is already in the Binder (with any parent path), that entry's data will simply be replaced;
        `new_entry_id` will not be used/generated and the existing entry's full path and flags will be kept.
        
        Otherwise, a new `BinderEntry` will be created. If `new_entry_id` is not given, `get_default_entry_id()` will
        be called; `entry_name` will be passed through `get_default_entry_path()` unless it already contains a double
        backslash (NOTE: subclass must define this method); and `flags` will be copied from `DEFAULT_ENTRY_FLAGS` on
        this class (default `0x2`).
        """
        try:
            existing_entry = self.entries_by_name[entry_name]
        except (ValueError, KeyError):
            # Create new entry.
            entry_path = self.get_default_entry_path(entry_name) if r"\\" not in entry_name else entry_name
            if new_entry_id is None:
                new_entry_id = self.get_default_entry_id(entry_name)
            if new_entry_flags is None:
                new_entry_flags = self.DEFAULT_ENTRY_FLAGS
            entry = BinderEntry(bytes(game_file), new_entry_id, entry_path, new_entry_flags)
            self.add_entry(entry)
        else:
            # Just modify existing entry's data.
            existing_entry.set_from_game_file(game_file)

    def add_or_replace_entry_id(
        self, entry_id: int, game_file: GameFile, new_entry_name: str = None, new_entry_flags: BinderFlags = None
    ):
        """Create or replace `BinderEntry` with ID `entry_id` using data from packed `game_file`.

        If `entry_id` is already in the Binder, that entry's data will simply be replaced; `new_entry_name` will not be
        used and the existing entry's full path and flags will be kept.

        Otherwise, a new `BinderEntry` will be created. `new_entry_name` must be given in this case, and will be passed
        through `get_default_entry_path()` if it does not contain a double backslash; `flags` will be copied from
        `DEFAULT_ENTRY_FLAGS` on this class (default `0x2`).
        """
        try:
            existing_entry = self.entries_by_id[entry_id]
        except (ValueError, KeyError):
            # Create new entry.
            if new_entry_name is None:
                raise ValueError(f"`new_entry_name` must be given for new entry ID {entry_id} to be created.")
            entry_path = self.get_default_entry_path(new_entry_name) if r"\\" not in new_entry_name else new_entry_name
            if new_entry_flags is None:
                new_entry_flags = self.DEFAULT_ENTRY_FLAGS
            entry = BinderEntry(bytes(game_file), entry_id, entry_path, new_entry_flags)
            self.add_entry(entry)
        else:
            # Just modify existing entry's data.
            existing_entry.set_from_game_file(game_file)

    def __getitem__(self, id_or_path_or_name) -> BinderEntry:
        """Shortcut for access by ID (int) or path (str) or basename (str).

        If the path of one entry is the basename of another entry, the former will be given precedence here, but this
        should never happen.
        """
        if isinstance(id_or_path_or_name, int):
            return self.entries_by_id[id_or_path_or_name]
        elif isinstance(id_or_path_or_name, str):
            try:
                return self.entries_by_path[id_or_path_or_name]
            except KeyError:
                try:
                    return self.entries_by_name[id_or_path_or_name]
                except KeyError:
                    raise BinderEntryNotFoundError(f"No entry with this ID/path/name: {id_or_path_or_name}")
        raise TypeError("`BND` key should be an entry ID (int) or path/basename (str).")

    def __iter__(self) -> tp.Iterator[BinderEntry]:
        return iter(self.entries)

    def __len__(self):
        return len(self.entries)

    def __repr__(self):
        if not self.entries:
            return
        entries = f",\n    ".join(repr(entry) for entry in self.entries)
        if entries:
            entries = f"\n    {entries},\n"
        return f"{self.__class__.__name__}({entries})"
