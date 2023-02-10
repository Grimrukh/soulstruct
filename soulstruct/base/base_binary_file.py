from __future__ import annotations

__all__ = ["BaseBinaryFile", "BASE_BINARY_FILE_T"]

import abc
import copy
import logging
import re
import typing as tp
from dataclasses import dataclass, asdict, field
from pathlib import Path

from soulstruct.games import Game, get_game
from soulstruct.utilities.binary import *
from soulstruct.utilities.files import create_bak, read_json, write_json
from soulstruct.containers.dcx import DCXType, compress, decompress, is_dcx

if tp.TYPE_CHECKING:
    from soulstruct.containers.entry import BinderEntry

try:
    Self = tp.Self
except ImportError:  # < Python 3.11
    Self = "BaseBinaryFile"

_LOGGER = logging.getLogger(__name__)


_GAME_MODULE_RE = re.compile(r"^soulstruct\.(\w+)\..*$")


@dataclass(slots=True)
class BaseBinaryFile(abc.ABC):
    """Base class for anything that is represented in binary at some point: notably `GameFile` and `BaseBinder`.

    Includes methods for recording and automating DCX compression.
    """

    # Utility class shortcuts.
    Reader: tp.ClassVar[tp.Type[BinaryReader]] = BinaryReader
    Writer: tp.ClassVar[tp.Type[BinaryWriter]] = BinaryWriter

    # If given, extension will be enforced (before DCX is checked) when calling `.write()`.
    EXT: tp.ClassVar[str] = ""

    # Records origin path of file if loaded from disk (or a `BinderEntry`). Not always available.
    path: Path | None = field(default=None, kw_only=True)
    # Default DCX compression type for file. If `None`, then `get_game().default_dcx_type` will be used.
    dcx_type: DCXType | None = field(default=None, kw_only=True)

    # region Read Methods

    @classmethod
    @abc.abstractmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        pass

    @abc.abstractmethod
    def to_writer(self) -> BinaryWriter:
        pass

    def __bytes__(self) -> bytes:
        """Applies `dcx_type` DCX automatically."""
        packed = bytes(self.to_writer())
        dcx_type = self._get_dcx_type()
        if dcx_type != DCXType.Null:
            return compress(packed, dcx_type)
        return packed

    @classmethod
    def from_path(cls, path: str | Path) -> Self:
        path = Path(path)
        try:
            game_file = cls.from_bytes(BinaryReader(path))
        except Exception:
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` with path '{path}'. See traceback.")
            raise
        game_file.path = path
        return game_file

    @classmethod
    def from_bytes(cls, data: bytes | bytearray | tp.BinaryIO | BinaryReader | BinderEntry) -> Self:
        """Load instance from binary data or binary stream (or `BinderEntry.data`)."""
        reader = BinaryReader(data) if not isinstance(data, BinaryReader) else data  # type: BinaryReader

        if is_dcx(reader):
            try:
                data, dcx_type = decompress(reader)
            finally:
                reader.close()
            reader = BinaryReader(data)
        else:
            dcx_type = DCXType.Null

        try:
            instance = cls.from_reader(reader)
            instance.dcx_type = dcx_type
        except Exception:
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` from binary data. See traceback.")
            raise
        finally:
            reader.close()
        return instance

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """Load file from given `data` dictionary. Simply calls initializer by default."""
        # noinspection PyArgumentList
        return cls(**data)

    @classmethod
    def from_json(cls, json_path: str | Path) -> Self:
        json_dict = read_json(json_path)
        # TODO: Some kind of fancy recursive JSON reader that checks field types and converts dictionaries to
        #  `BaseBinaryFile` subclasses.
        return cls.from_dict(json_dict)

    # endregion

    def write(self, file_path: None | str | Path = None, make_dirs=True, check_hash=False):
        """Pack game file into `bytes`, then write to given `file_path` (or `self.path` if not given).

        Missing directories in given path will be created automatically if `make_dirs` is True. Otherwise, they must
        already exist.

        Will compress with DCX automatically and add `.dcx` file extension if `.dcx_type` is not `Null`. Will also
        automatically create a `.bak` version of the `file_path`, if a backup does not already exist.

        Args:
            file_path (None, str, Path): file path to write to. Defaults to `self.path`, which is automatically set at
                instance creation if a file path is used as a source.
            make_dirs (bool): if True, any directories in `file_path` that are missing will be created. (Default: True)
            check_hash (bool): if True, file will not be written if file with same hash already exists. (Default: False)
        """
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        packed_dcx = bytes(self)
        if check_hash and file_path.is_file():
            if get_blake2b_hash(file_path) == get_blake2b_hash(packed_dcx):
                return  # don't write file
        create_bak(file_path)
        with file_path.open("wb") as f:
            f.write(packed_dcx)

    def to_dict(self) -> dict:
        """Create a dictionary from file instance. Uses `dataclasses.asdict()` by default."""
        return asdict(self)

    def write_json(self, file_path: None | str | Path, encoding="utf-8", indent=4):
        """Create a dictionary from instance and write it to a JSON file.

        The file path will have the `.json` suffix added automatically if missing.
        """
        json_dict = self.to_dict()
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            file_path = self.path
        file_path = Path(file_path)
        if file_path.suffix != ".json":
            file_path = file_path.with_suffix(file_path.suffix + ".json")
        write_json(file_path, json_dict, indent=indent, encoding=encoding)

    def create_bak(self, file_path: None | str | Path = None, make_dirs=True):
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        create_bak(file_path)

    def copy(self):
        return copy.deepcopy(self)

    def _get_file_path(self, file_path: None | str | Path) -> Path:
        """Get default path of binary file, based on `EXT` and `dcx_type`."""
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            file_path = self.path
        file_path = Path(file_path)

        # 1. Remove any existing ".dcx" extension.
        while file_path.suffix == ".dcx":
            file_path = file_path.with_name(file_path.stem)  # remove '.dcx' (may add back below)

        # 2. If `EXT` is defined, add that extension to the path.
        if self.EXT and file_path.suffix != self.EXT:
            file_path = file_path.with_suffix(file_path.suffix + self.EXT)

        # 3. If `dcx_type` is not `Null`, add ".dcx" extension to the path.
        if self._get_dcx_type() != DCXType.Null and not file_path.suffix == ".dcx":
            file_path = file_path.with_suffix(file_path.suffix + ".dcx")  # add ".dcx"

        return file_path

    def _get_dcx_type(self) -> DCXType:
        if self.dcx_type is None:
            try:
                return self.get_game().default_dcx_type
            except ValueError:
                _LOGGER.warning(
                    f"Could not detect default DCX type for game-independent file class {self.cls_name}. "
                    f"Not using any compression."
                )
                return DCXType.Null
        return self.dcx_type

    @classmethod
    def from_bak(cls, file_path: Path | str, create_bak_if_missing=True) -> Self:
        """Looks for a `.bak` version of the given path to open preferentially, or optionally creates it if missing."""
        file_path = Path(file_path)
        bak_path = file_path.with_name(file_path.name + ".bak")
        if bak_path.is_file():
            game_file = cls.from_path(bak_path)
            game_file.path = game_file.path.with_suffix("")  # remove ".bak" extension
            return game_file
        else:
            game_file = cls.from_path(file_path)
            if create_bak_if_missing:
                create_bak(file_path)
            return game_file

    @classmethod
    def get_game(cls) -> Game:
        if match := re.match(_GAME_MODULE_RE, cls.__module__):
            return get_game(match.group(1))
        raise ValueError(f"Could not detect game name from module of class `{cls.__name__}`: {cls.__module__}")

    @property
    def cls_name(self) -> str:
        return self.__class__.__name__


BASE_BINARY_FILE_T = tp.TypeVar("BASE_BINARY_FILE_T", bound="BaseBinaryFile")
