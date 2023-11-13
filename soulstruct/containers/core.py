from __future__ import annotations

__all__ = [
    "BinderFlags",
    "BinderError",
    "EntryNotFoundError",
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
from soulstruct.dcx import DCXType, compress, decompress, is_dcx
from soulstruct.utilities.binary import *
from soulstruct.utilities.files import read_json, write_json

from .binder_hash import BinderHashTable
from .entry import BinderEntry, BinderEntryHeader

try:
    from typing import Self
except ImportError:  # < Python 3.11
    Self = "Binder"

_LOGGER = logging.getLogger(__name__)


# Flexible entry-finding typing that can be passed to `Binder.__getitem__` and a few other methods.
ENTRY_SPEC = tp.Union[int, str, Path, re.Pattern]


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


class EntryNotFoundError(BinderError, KeyError):
    """Raised when a `BinderEntry` is not found.

    Subclass of `KeyError` for legacy compatibility.
    """


class MultipleEntriesFoundError(BinderError, ValueError):
    """Raised when multiple `BinderEntry` instances are found matching a given entry specification, usually only when
    `assert_unique=True`.

    Subclass of `ValueError` for legacy compatibility.
    """


BinderSourceTyping = tp.Union[str, Path, bytes, bytearray, BinderEntry, io.BufferedIOBase, BinaryReader]
T = tp.TypeVar("T", bound="BaseBinder")


class BinderVersion(enum.Enum):
    """Version used for BND and BXF files."""
    V3 = 3  # used before Dark Souls 2 (2014)
    V4 = 4  # used from Dark Souls 2 (2014) onwards


@dataclass(slots=True)
class BinderHeaderV3(BinaryStruct):
    version: bytes = field(**BinaryString(4, asserted=[b"BND3", b"BHF3"]))
    signature: str = field(**BinaryString(8, encoding="ASCII", rstrip_null=True))
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
class BinderHeaderV4(BinaryStruct):
    version: bytes = field(**BinaryString(4, asserted=[b"BND4", b"BHF4"]))
    unknown1: bool
    unknown2: bool
    _pad1: bytes = field(init=False, **BinaryPad(3))
    big_endian: bool
    bit_little_endian: bool
    _pad2: bytes = field(init=False, **BinaryPad(1))
    entry_count: int
    # NOTE: No `file_size` in V4.
    _header_size: long = field(init=False, **Binary(asserted=0x40))
    signature: str = field(**BinaryString(8, encoding="ASCII", rstrip_null=True))
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
class BDTHeaderV3(BinaryStruct):
    _version: bytes = field(init=False, **BinaryString(4, asserted=b"BDF3"))
    signature: str = field(**BinaryString(8, encoding="ASCII", rstrip_null=True))
    _pad1: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True)
class BDTHeaderV4(BinaryStruct):
    _version: bytes = field(init=False, **BinaryString(4, asserted=b"BDT4"))
    unknown1: bool
    unknown2: bool
    _pad1: bytes = field(init=False, **BinaryPad(3))
    big_endian: bool
    bit_little_endian: bool
    _pad2: bytes = field(init=False, **BinaryPad(5))
    _header_size: long = field(init=False, **Binary(asserted=0x30))
    signature: str = field(**BinaryString(8, encoding="ASCII", rstrip_null=True))
    _pad3: bytes = field(init=False, **BinaryPad(16))


@dataclass(slots=True)
class BinderVersion4Info:
    """Defaults are simply the most common observed values."""
    unknown1: bool = False
    unknown2: bool = False
    unicode: bool = True
    hash_table_type: int = 0  # 4 is also very common

    most_recent_hash_table: bytes = field(init=False, repr=False, default=b"")
    most_recent_entry_count: int = field(init=False, repr=False, default=0)
    most_recent_paths: list[str] = field(init=False, repr=False, default_factory=list)


@dataclass(slots=True, kw_only=True)
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

    # For convenience.
    EntryNotFoundError: tp.ClassVar = EntryNotFoundError

    # Enforced name of manifest file.
    MANIFEST_NAME: tp.ClassVar[str] = "binder_manifest.json"

    # Binder entry path encoding.
    # NOTE: Binder entry paths are NOT encoded in `shift_jis_2004`, unlike most other strings, but are rather just
    # `shift-jis`. The relevant difference is that escaped backslashes are decoded to the yen symbol in the former
    # expanded encoding, which we do not want in these files.
    ENTRY_PATH_ENCODING: tp.ClassVar[str] = "shift-jis"

    # Default `BinderEntry.flags` to use when creating new entries with `Binder` utility methods.
    # Default (2) is the most common observed value by far.
    DEFAULT_ENTRY_FLAGS: tp.ClassVar[int] = 0b0000_0010  # 2

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

        # BHD/BDT file.
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
            if version_bytes[3:4] == b"3":
                entry_reader.read(0x10)
            elif version_bytes[3:4] == b"4":
                entry_reader.read(0x30)
            else:
                raise ValueError(f"Unsupported BHD/BDT version: {version_bytes}")
        else:
            entry_reader = reader  # headers and entries in same file

        if version_bytes in {b"BND3", b"BHF3"}:
            header_kwargs, entry_headers = cls._read_header_v3(reader)
        elif version_bytes in {b"BND4", b"BHF4"}:
            header_kwargs, entry_headers = cls._read_header_v4(reader)
        else:
            raise ValueError(f"Could not detect BND version from first four bytes: {version_bytes}:")

        entries = [BinderEntry.from_header(entry_reader, entry_header) for entry_header in entry_headers]
        if v4_info := header_kwargs.get("v4_info", None):
            # Set existing V4 hash properties.
            v4_info.most_recent_entry_count = len(entries)
            v4_info.most_recent_paths = [entry.path for entry in entries]

        return cls(entries=entries, is_split_bxf=bdt_reader is not None, **header_kwargs)

    @classmethod
    def _read_header_v3(cls, reader: BinaryReader) -> tuple[dict[str, tp.Any], list[BinderEntryHeader]]:
        # Test for endianness is a little complicated, as `flags.is_big_endian` can override the header `big_endian`.
        big_endian, bit_big_endian = reader.unpack("??", offset=0xD)
        flags_fmt = ">B" if bit_big_endian else "<B"
        flags = BinderFlags.from_byte(reader[flags_fmt, 0xC], bit_big_endian)
        byte_order = ByteOrder.BigEndian if (big_endian or flags.is_big_endian) else ByteOrder.LittleEndian

        header_struct = BinderHeaderV3.from_bytes(reader, byte_order=byte_order)

        entry_headers = [
            BinderEntryHeader.from_reader_v3(reader, flags, header_struct.bit_big_endian)
            for _ in range(header_struct.entry_count)
        ]

        header_kwargs = dict(
            signature=header_struct.signature,
            big_endian=big_endian,
            bit_big_endian=bit_big_endian,
            version=BinderVersion.V3,
            v4_info=None,
        )
        return header_kwargs, entry_headers

    @classmethod
    def _read_header_v4(cls, reader: BinaryReader) -> tuple[dict[str, tp.Any], list[BinderEntryHeader]]:
        """Less endian complexity than V3."""
        byte_order = ByteOrder.from_reader_peek(reader, 1, 9, b"\01", b"\00")
        reader.default_byte_order = byte_order
        header_struct = BinderHeaderV4.from_bytes(reader, byte_order=byte_order)  # type: BinderHeaderV4

        flags = BinderFlags.from_byte(header_struct.flags, not header_struct.bit_little_endian)
        flags_header_size = flags.get_bnd_entry_header_size()

        _entry_header_size = header_struct.pop("_entry_header_size")
        _hash_table_offset = header_struct.pop("_hash_table_offset")
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
            for _ in range(header_struct.entry_count)
        ]

        v4_info = header_struct.to_object(BinderVersion4Info)

        if v4_info.hash_table_type == 4:
            # Save the initial hash table (found in header).
            hash_table_size = _data_offset - _hash_table_offset if _data_offset > 0 else _hash_table_offset
            reader.seek(_hash_table_offset)
            v4_info.most_recent_hash_table = reader.read(hash_table_size)

        header_kwargs = dict(
            signature=header_struct.signature,
            flags=flags,
            big_endian=header_struct.big_endian,
            bit_big_endian=not header_struct.bit_little_endian,  # REVERSED
            version=BinderVersion.V4,
            v4_info=v4_info,
        )

        return header_kwargs, entry_headers

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

        # 'entries' is a dictionary mapping entry path roots to either (a) entry dictionaries containing 'flags', 'id',
        # and 'name' keys, or (b) entry names only if 'flags' is default and 'id' is just the entry index.
        entries = manifest.pop("entries")

        use_id_prefix = manifest.pop("use_id_prefix")
        binder = cls.from_dict(manifest)
        binder.add_entries_from_manifest(entries, directory, use_id_prefix)
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
        try:
            version = BinderVersion(int(binder_type[3]))
        except ValueError:
            raise ValueError(
                f"Invalid Binder manifest `binder_type`: {binder_type}. Must be of format '{{BND|BXF}}{{3|4}}'."
            )
        binder_kwargs["is_split_bxf"] = is_split_bxf
        binder_kwargs["version"] = version
        binder_kwargs["flags"] = BinderFlags(manifest["flags"])
        binder_kwargs["dcx_type"] = DCXType[manifest["dcx_type"]]

        if version == BinderVersion.V4:
            # Read V4-specific info.
            try:
                binder_kwargs["v4_info"] = BinderVersion4Info(
                    unknown1=binder_kwargs.pop("unknown1"),
                    unknown2=binder_kwargs.pop("unknown2"),
                    unicode=binder_kwargs.pop("unicode"),
                    hash_table_type=binder_kwargs.pop("hash_table_type"),
                )
            except KeyError:
                raise BinderError(
                    "Binder manifest JSON file does not contain all required keys for Binder V4: "
                    "'unknown1', 'unknown2', 'unicode', 'hash_table_type'."
                )

        return binder_kwargs

    @classmethod
    def empty_bnd3(cls):
        """Create an empty Binder V3 (BND3)."""
        return cls(version=BinderVersion.V3, v4_info=None)

    @classmethod
    def empty_bxf3(cls):
        """Create an empty split Binder V3 (BXF3)."""
        return cls(version=BinderVersion.V3, v4_info=None, is_split_bxf=True)

    # endregion

    # region Write Methods

    def write(
        self,
        file_path: None | str | Path = None,
        bdt_file_path: None | str | Path = None,
        make_dirs=True,
        check_hash=False,
    ) -> Path | None:
        """Writes the `BND` file, or writes both the `BHD` and `BDT` files at once for split binders.

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

        Returns:
            Path | None: path of written BND or BHD (not BDT) file. `None` if nothing new is written.
        """
        file_path = self.get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)

        if self.is_split_bxf:
            if bdt_file_path is None:
                # Auto-set BDT path.
                name_parts = file_path.name.split(".")
                bdt_name = name_parts[0] + "." + ".".join(name_parts[1:]).replace("bhd", "bdt")
                bdt_file_path = file_path.with_name(bdt_name)
            else:
                bdt_file_path = Path(bdt_file_path)
                if make_dirs:  # only needed if not next to BHD file (as will be the case above)
                    bdt_file_path.parent.mkdir(parents=True, exist_ok=True)
            packed_bhd, packed_bdt = self.get_split_bytes()
            if check_hash and file_path.is_file() and bdt_file_path.is_file():
                bhd_match = get_blake2b_hash(file_path) == get_blake2b_hash(packed_bhd)
                bdt_match = get_blake2b_hash(bdt_file_path) == get_blake2b_hash(packed_bdt)
                if bhd_match and bdt_match:
                    return None  # don't write files (both match)
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
        return file_path

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

        writer.fill_with_position("file_size", obj=self)

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

        # File size is zero for BXF.
        header_writer.fill("file_size", 0, obj=self)

        return header_writer, entry_writer

    def _header_to_writer_v3(self) -> BinaryWriter:

        return BinderHeaderV3(
            version=b"BHF3" if self.is_split_bxf else b"BND3",
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

        sorted_entries = list(sorted(self.entries, key=lambda e: e.entry_id))
        sorted_entry_headers = [entry.get_header(self.flags) for entry in sorted_entries]
        for entry_header in sorted_entry_headers:
            entry_header.into_bnd3_writer(header_writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            for entry, entry_header in zip(sorted_entries, sorted_entry_headers):
                packed_path = entry.get_packed_path(encoding=self.ENTRY_PATH_ENCODING)
                entry_header.pack_path(header_writer, packed_path)

        for entry, entry_header in zip(sorted_entries, sorted_entry_headers):
            entry_writer.pad_align(16)
            entry_header.pack_data(header_writer, entry_writer, entry.data)

    def _header_to_writer_v4(self) -> BinaryWriter:

        if self.v4_info is None:
            raise AttributeError("`Binder version `V4` must have a `v4_info`.")

        return BinderHeaderV4(
            version=b"BHF4" if self.is_split_bxf else b"BND4",
            unknown1=self.v4_info.unknown1,
            unknown2=self.v4_info.unknown2,
            big_endian=self.big_endian,
            bit_little_endian=not self.bit_big_endian,  # REVERSED
            entry_count=len(self.entries),
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

        sorted_entries = list(sorted(self.entries, key=lambda e: e.entry_id))
        sorted_entry_headers = [entry.get_header(self.flags) for entry in sorted_entries]
        for entry_header in sorted_entry_headers:
            entry_header.into_bnd4_writer(header_writer, self.flags, self.bit_big_endian)

        if self.flags.has_names:
            path_encoding = entry_writer.get_utf_16_encoding() if self.v4_info.unicode else self.ENTRY_PATH_ENCODING
            for entry, entry_header in zip(sorted_entries, sorted_entry_headers):
                entry_header.pack_path(header_writer, entry.get_packed_path(encoding=path_encoding))

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
            # Ten pad bytes between entry data blocks (for byte-perfect writes).
            entry_header.pack_data(header_writer, entry_writer, entry.data + b"\0" * 10)

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

        entry_tree_dict = {}  # type: dict[str, list[dict[str, int | str]]]
        use_index_prefix = self.has_repeated_entry_names

        # Although the unpacked folder reader supports a mixture of entry names and entry dictionaries, this writer only
        # does one or the other depending on whether any non-default entry flags or non-index entry IDs are present.
        use_entry_names_only = all(
            entry.flags == self.DEFAULT_ENTRY_FLAGS and entry.entry_id == i
            for i, entry in enumerate(self.entries)
        )

        for i, entry in enumerate(self.entries):
            entry_directory = str(Path(entry.path).parent)  # no trailing backslash

            if use_entry_names_only:
                entry_tree_dict.setdefault(entry_directory, []).append(entry.name)
            else:
                entry_dict = {
                    "flags": entry.flags,
                    "id": entry.entry_id if self.flags.has_ids else i,
                    "name": entry.name,
                }
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

    def add_entries_from_manifest(
        self,
        entries: dict[str, list[str | dict[str, int | str]]],
        directory: str | Path,
        use_id_prefix: bool,
    ):
        """Add entries from a manifest dictionary mapping entry roots to entry data names/dicts in `directory`."""
        directory = Path(directory)
        auto_entry_id = None  # type: int | None  # used to set entry IDs automatically (from index) if not given
        unsorted_entries = {}  # maps ID to created `BinderEntry`s
        for root, root_entries in entries.items():
            for entry in root_entries:
                if isinstance(entry, str):
                    # Just entry 'name'. ID will be auto-set and flags will be default.
                    if auto_entry_id is None:
                        auto_entry_id = 0  # any 'id' given manually in subsequent entries must now match this!
                    entry_name = entry
                    entry_id = auto_entry_id
                    entry_flags = 2
                elif isinstance(entry, dict):
                    entry_name = entry["name"]
                    if "id" in entry:
                        entry_id = entry["id"]
                        if auto_entry_id is not None and entry_id != auto_entry_id:
                            raise ValueError(
                                f"Entry '{entry_name}' has custom ID {entry_id} in manifest, which does not match its "
                                f"automatic index ID {entry_id} as calculated from prior entries without a custom ID."
                            )
                    else:
                        entry_id = auto_entry_id
                    entry_flags = entry.get("flags", 2)
                else:
                    raise TypeError(f"Invalid entry type in manifest: {entry}. Must be `str` (name only) or `dict`.")

                entry_file_name = f"__{entry_id}__{entry_name}" if use_id_prefix else entry_name
                entry_file_path = directory / entry_file_name
                if not entry_file_path.is_file():
                    raise FileNotFoundError(f"Could not find Binder entry file: {entry_file_path}")
                entry_data = entry_file_path.read_bytes()
                entry_path = str(Path(root).joinpath(entry_name))
                unsorted_entries[entry_id] = BinderEntry(
                    entry_id=entry_id,
                    path=entry_path,
                    data=entry_data,
                    flags=entry_flags,
                )

                if auto_entry_id is not None:
                    auto_entry_id += 1

        # Add entries in ID order.
        for entry_id, binder_entry in sorted(unsorted_entries.items()):
            self.add_entry(binder_entry)

    def add_entry(self, entry: BinderEntry):
        if id(entry) in {id(e) for e in self.entries}:
            raise BinderError(f"Given `BinderEntry` instance with ID {entry.entry_id} is already in this binder.")
        if entry.entry_id in {e.id for e in self.entries}:
            _LOGGER.warning(
                f"Entry ID {entry.entry_id} appears more than once in this Binder. Entry still added, but you should"
                f"fix this."
            )
        self.entries.append(entry)

    def remove_entry(self, entry: BinderEntry):
        """NOTE: Uses `id()` to remove the exact same entry instance. Does not check for field-wise entry equality."""
        if id(entry) not in {id(e) for e in self.entries}:
            raise KeyError(f"Entry `{entry}` is not in this Binder. Cannot remove it.")
        self.entries.remove(entry)

    def remove_entry_id(self, entry_id: int) -> BinderEntry:
        entry = self.find_entry_id(entry_id, assert_unique=True)
        self.entries.remove(entry)
        return entry

    def remove_entry_path(self, entry_path: Path | str):
        entry = self.find_entry_path(entry_path, assert_unique=True)
        self.entries.remove(entry)
        return entry

    def remove_entry_name(self, entry_name: str):
        entry = self.find_entry_name(entry_name, assert_unique=True)
        self.entries.remove(entry)
        return entry

    def clear_entries(self):
        """Remove all entries from the Binder."""
        self.entries.clear()

    def create_default_entry(
        self,
        entry_data: bytes,
        entry_id: int = None,
        entry_name: str = None,
        entry_path: str | Path = None,
        entry_flags: int = None,
    ) -> BinderEntry:
        """Create a new `BinderEntry`, attempting to replace whichever fields are NOT given with defaults provided by
        this `Binder` subclass.

        Exactly ONE of `entry_name` and `entry_path` should be given.

        Does NOT add the created entry to this Binder automatically.
        """
        if entry_path is None:
            if entry_name is not None:
                entry_path = self.get_default_new_entry_path(entry_name)
            else:
                raise ValueError("Either `entry_name` or `entry_path` must be given.")
        elif entry_name is not None:
            raise ValueError("Only one of `entry_name` or `entry_path` may be given.")
        else:
            # May be needed to get default ID below.
            entry_name = Path(entry_path).name
        if entry_id is None:
            entry_id = self.get_default_new_entry_id(entry_name)
        if entry_flags is None:
            entry_flags = self.DEFAULT_ENTRY_FLAGS
        return BinderEntry(entry_data, entry_id, entry_path, entry_flags)

    def set_default_entry(
        self,
        entry_spec: ENTRY_SPEC,
        new_id: int = None,
        new_name: str = None,
        new_path: str | Path = None,
        new_flags: int = None,
        new_data: bytes = b"",
    ) -> BinderEntry:
        """Retrieve or create `BinderEntry` specified by `entry_spec`, a la `dict.setdefault()`.

        If an entry is not found, the `new_` arguments are passed to `create_default_entry()`, which is added to the
        Binder automatically. Otherwise, these arguments are ignored - their values will NOT be set to the existing
        entry's values.

        Returns the found or created `BinderEntry`.

        Will always raise a `MultipleEntriesFoundError` if multiple existing entries are found.
        """
        try:
            # NOTE: Will raise an unhandled `MultipleEntriesFoundError` if multiple entries are found.
            return self[entry_spec]
        except EntryNotFoundError:
            # Create new entry. Value of `entry_spec` is redirected to the appropriate creation argument.

            if isinstance(entry_spec, int):
                if new_id is not None:
                    raise ValueError("`new_id` should not be given when `entry_spec` is already an entry ID.")
                new_id = entry_spec
            elif self.looks_like_entry_path(entry_spec):
                new_path = str(entry_spec)
            elif isinstance(entry_spec, str):
                new_name = entry_spec
            entry = self.create_default_entry(new_data, new_id, new_name, new_path, new_flags)
            self.add_entry(entry)
            return entry

    # endregion

    # region Entry Lookup

    def get_entries_by_id(self) -> dict[int, BinderEntry]:
        """Get a dictionary mapping entry IDs to entries.

        If there are multiple entries with the same ID in the BND, this will raise a `BinderError`. This should never
        happen; if it does, fix it by accessing the culprit entries with `.entries` and changing one or more IDs.
        """
        entries = {}
        for entry in self.entries:
            if entry.entry_id in entries:
                raise BinderError(f"There are multiple entries with ID {entry.entry_id}.")
            entries[entry.entry_id] = entry
        return entries

    def get_entries_by_path(self) -> dict[str, BinderEntry]:
        """Get a dictionary mapping entry paths to entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this method will raise a `MultipleEntriesFoundError`.
        """
        entries = {}
        for entry in self.entries:
            if entry.path in entries:
                raise MultipleEntriesFoundError(f"Multiple entries have path '{entry.path}'.")
            entries[entry.path] = entry
        return entries

    def get_entries_by_name(self) -> dict[str, BinderEntry]:
        """Get a dictionary mapping entry basenames to entries.

        The same path and/or basename may appear in multiple paths in a BND (e.g. vanilla 'item.msgbnd' in Dark Souls
        Remastered). If it does, this method will raise a `MultipleEntriesFoundError`.
        """
        entries = {}
        for entry in self.entries:
            if entry.name in entries:
                raise MultipleEntriesFoundError(f"Multiple entry paths have base name '{entry.name}'.")
            entries[entry.name] = entry
        return entries

    def _find_entry_by_attr(self, attr: str, value: int | str, assert_unique=False):
        """Shared code for finding an entry with `getattr(entry, attr) == value`.

        If `assert_unique` is True, will check all entries and raise a `BinderError` if multiple hits are found.
        """
        found = None
        for entry in self.entries:
            if getattr(entry, attr) == value:
                if not assert_unique:
                    return entry
                if found:
                    raise MultipleEntriesFoundError(f"Multiple entries found with `{attr} == {value}`.")
                found = entry
        if found:
            return found
        raise EntryNotFoundError(f"No entry found with `{attr} == {value}`.")

    def find_entry_id(self, entry_id: int, assert_unique=False):
        """Return the first entry with the given `entry_id`.

        If `assert_unique` is True, will check all entries and raise a `BinderError` if multiple have the same ID.
        """
        return self._find_entry_by_attr("entry_id", entry_id, assert_unique)

    def find_entry_name(self, entry_name: str, assert_unique=False):
        """Return the first entry with the given `entry_name`."""
        return self._find_entry_by_attr("name", entry_name, assert_unique)

    def find_entry_path(self, entry_path: str | Path, assert_unique=False):
        """Return the first entry with the given `entry_path`."""
        return self._find_entry_by_attr("path", str(entry_path), assert_unique)

    def _find_entries_matching_attr(
        self,
        pattern: str | re.Pattern,
        attr: str,
        return_multiple: bool,
        assert_unique: bool,
        flags=0,
        escape=False,
    ) -> BinderEntry | list[BinderEntry]:
        """Shared code to match single/multiple entry names or paths."""
        if escape:
            pattern = re.escape(pattern)
        matches = [entry for entry in self.entries if re.match(pattern, getattr(entry, attr), flags=flags)]
        if return_multiple:
            return matches
        if not matches:
            raise EntryNotFoundError(f"No Binder entries found with {attr} matching '{pattern}'.")
        if len(matches) > 1 and assert_unique:
            raise ValueError(
                f"Found multiple Binder entries with {attr} matching '{pattern}':\n  {[m.path for m in matches]}"
            )        
        return matches[0]

    def find_entry_matching_path(
        self, pattern: str | re.Pattern, flags=0, escape=False, assert_unique=False,
    ) -> BinderEntry:
        """Returns a single entry whose full path matches the given regex `pattern`.

        Only one match must exist. Use `find_entries_matching_path()` if you want to find multiple matches.
        """
        return self._find_entries_matching_attr(pattern, "path", False, assert_unique, flags=flags, escape=escape)

    def find_entries_matching_path(self, pattern: str | re.Pattern, flags=0, escape=False) -> list[BinderEntry]:
        """Returns a list of entries whose paths match the given `regex` pattern."""
        return self._find_entries_matching_attr(pattern, "path", True, False, flags=flags, escape=escape)

    def find_entry_matching_name(
        self, pattern: str | re.Pattern, flags=0, escape=False, assert_unique=False
    ) -> BinderEntry:
        """Returns a single entry whose name matches the given regex `pattern`.

        Only one match must exist. Use `find_entries_matching_name()` if you want to find multiple matches.
        """
        return self._find_entries_matching_attr(pattern, "name", False, assert_unique, flags=flags, escape=escape)

    def find_entries_matching_name(self, pattern: str | re.Pattern, flags=0, escape=False) -> list[BinderEntry]:
        """Returns a list of entries whose names match the given `regex` pattern."""
        return self._find_entries_matching_attr(pattern, "name", True, False, flags=flags, escape=escape)

    def __getitem__(self, entry_spec: int | Path | str | re.Pattern) -> BinderEntry:
        """Convenient shortcut for finding an entry by ID (int), full path (Path), name only (str), or by matching
        its name with regex (`re.Pattern`).

        If `entry_spec` is a string that looks like a Path (contains a forward slash or backslash), it will be treated
        as a full path. Obviously, these characters can never appear in a file name, so this is a safe assumption.

        The only standard entry-finding method not supported here is matching the entry's full path with regex, which
        can be done with `find_entry_matching_path()`.

        Finding methods are called with `assert_unique=True`, which means a `BinderError` will be raised if multiple
        entries are found. If you want to allow multiple hits and only return the first, or return all of those multiple
        hits, use the appropriate method directly.
        """
        if isinstance(entry_spec, str) and ("\\" in entry_spec or "/" in entry_spec):
            entry_spec = Path(entry_spec)

        if isinstance(entry_spec, int):
            return self.find_entry_id(entry_spec, assert_unique=True)
        if isinstance(entry_spec, Path):
            return self.find_entry_path(entry_spec, assert_unique=True)
        if isinstance(entry_spec, str):
            return self.find_entry_name(entry_spec, assert_unique=True)
        if isinstance(entry_spec, re.Pattern):
            return self.find_entry_matching_name(entry_spec, assert_unique=True)

        raise TypeError(
            "Key for `binder[]` should be an entry ID (int), path (Path/str), name (str), or pattern (`re.Pattern`)."
        )

    # endregion

    # region Binder Properties

    def get_entry_ids(self) -> list[int]:
        return [entry.entry_id for entry in self.entries]

    def get_entry_paths(self) -> list[str]:
        return [entry.path for entry in self.entries]

    def get_entry_names(self) -> list[str]:
        return [entry.name for entry in self.entries]

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
        all_entry_ids = {entry.entry_id for entry in self.entries}
        for entry_id in range(min_id_inclusive, max_id_exclusive):
            if entry_id not in all_entry_ids:
                return entry_id
        raise EntryNotFoundError(
            f"No entry ID in the range [{min_id_inclusive}, {max_id_exclusive}) is available."
        )

    @classmethod
    def get_default_new_entry_path(cls, entry_name: str) -> str:
        """Optional method that can be overridden (usually by a game subclass) to generate a full entry path.
        
        NOTE: Some simple binders, like TPFBHD map texture binders, do not even need their entries to have full paths.
        However, to avoid dangerous silent problems caused by binders doing this in general, this method does NOT do
        that by default.
        """
        raise BinderError(
            f"`get_default_new_entry_path()` not defined on this `Binder` class/subclass: `{cls.__name__}`"
        )

    def get_default_new_entry_id(self, entry_name: str) -> int:
        """Method that can be overridden (usually by a game subclass) to generate a default new entry ID.
        
        Default method simply returns the ID after the highest currently ID (which may leave gaps in earlier ranges).
        """
        return self.highest_entry_id + 1

    def __iter__(self) -> tp.Iterator[BinderEntry]:
        return iter(self.entries)

    def __len__(self):
        return len(self.entries)

    def __bool__(self):
        """Implemented so that instances with no entries do not evaluate as `False` (they may have other attributes)."""
        return True

    def __repr__(self):
        if not self.entries:
            return
        entries = f",\n    ".join(repr(entry) for entry in self.entries)
        if entries:
            entries = f"\n    {entries},\n"
        return f"{self.__class__.__name__}({entries})"

    @staticmethod
    def looks_like_entry_path(entry_spec: ENTRY_SPEC):
        """Test if `entry_spec` looks like a full entry path (i.e. contains a forward slash or backslash).
        
        Some simple binders do not even need parent paths for their entries (i.e. entry path == entry name). This
        method will 'fail' for such cases, but that's safer behavior for the majority of binders.
        """
        return (
            isinstance(entry_spec, Path)
            or (isinstance(entry_spec, str) and ("\\" in entry_spec or "/" in entry_spec))
        )
